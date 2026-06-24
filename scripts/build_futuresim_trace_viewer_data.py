#!/usr/bin/env python3
"""Build static FutureSim trace-viewer data from harness stdout JSONL files."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
from collections import defaultdict
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any


START_SIM_DATE = date(2025, 12, 24)
DAY_ADVANCED_RE = re.compile(r"Day advanced to (20\d{2}-\d{2}-\d{2})")
SECRET_RE = re.compile(
    r"(?i)(sk-[A-Za-z0-9_-]{20,}|[A-Za-z0-9_-]*(?:api|token|key)[A-Za-z0-9_-]*[=:][A-Za-z0-9_.-]{16,})"
)
DROP_KEYS = {"thinking", "signature"}
MAX_STRING_CHARS = 20000


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--run",
        action="append",
        default=[],
        metavar="AGENT|SLUG|MODEL|HARNESS|SEED|PATH",
        help="Run spec. Example: 'Fable 5|fable-5|claude-fable-5|Claude Code|r00|/path/claude_code_stdout.jsonl'",
    )
    parser.add_argument("--max-days", type=int, default=0, help="Optional sample-data limit.")
    parser.add_argument("--max-events-per-day", type=int, default=0, help="Optional sample-data limit.")
    parser.add_argument("--max-source-events", type=int, default=0, help="Optional per-run parse limit for local previews.")
    args = parser.parse_args()

    if not args.run:
        raise SystemExit("Pass at least one --run spec.")

    args.output.mkdir(parents=True, exist_ok=True)
    runs = []
    for spec in args.run:
        run = build_run(spec, args.output, args.max_days, args.max_events_per_day, args.max_source_events)
        if run["days"]:
            runs.append(run)

    manifest = {
        "version": 1,
        "created_at_utc": datetime.now(UTC).isoformat(),
        "runs": runs,
    }
    write_json(args.output / "manifest.json", manifest)


def build_run(spec: str, output: Path, max_days: int, max_events_per_day: int, max_source_events: int = 0) -> dict[str, Any]:
    agent_name, agent_slug, model, harness, seed_label, source = parse_run_spec(spec)
    source_path = Path(source)
    if not source_path.exists():
        raise SystemExit(f"Missing stdout JSONL: {source_path}")

    run_id = source_path.parents[2].name
    run_label = run_id
    harness_name = harness_condition(harness, source_path.parents[2] / "config.json")
    harness_slug = slugify(harness_name)
    run_dir = output / "runs" / agent_slug / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    days = defaultdict(list)
    current_day = START_SIM_DATE
    pending_next_day = False
    turn = 0
    forecast_history: dict[str, dict[str, float]] = {}

    with source_path.open(encoding="utf-8") as handle:
        for idx, line in enumerate(handle):
            if max_source_events and idx >= max_source_events:
                break
            if not line.strip():
                continue
            raw = json.loads(line)
            event = normalize_event(raw, idx, current_day.isoformat(), turn)
            annotate_forecast_history(event, forecast_history)
            if any(block.get("type") == "tool_use" and "next_day" in block.get("name", "") for block in event["blocks"]):
                pending_next_day = True

            if should_keep_event(event):
                if event["kind"] == "assistant":
                    turn += 1
                    event["turn"] = turn
                days[current_day.isoformat()].append(event)

            advanced = DAY_ADVANCED_RE.search(line)
            if advanced:
                current_day = date.fromisoformat(advanced.group(1))
                pending_next_day = False
            elif pending_next_day and event_has_tool_result(event):
                if "When your memory updates are complete" not in line:
                    current_day += timedelta(days=1)
                    pending_next_day = False
            if max_days and len(days) > max_days:
                break

    metrics = read_metrics(source_path.parents[2] / "daily_metrics.csv")
    if metrics:
        final_metric_date = max(
            (date.fromisoformat(row["date"]) for row in metrics if row.get("date")),
            default=None,
        )
        if final_metric_date and current_day >= final_metric_date:
            for row in metrics:
                if row.get("date"):
                    days.setdefault(row["date"], [])

    day_items = []
    for day_key in sorted(days):
        if max_days and len(day_items) >= max_days:
            break
        events = days[day_key]
        truncated = False
        if max_events_per_day and len(events) > max_events_per_day:
            events = events[:max_events_per_day]
            truncated = True
        shard = {
            "agent_slug": agent_slug,
            "agent_name": agent_name,
            "model": model,
            "harness": harness,
            "seed_label": seed_label,
            "run_id": run_id,
            "sim_date": day_key,
            "events": events,
            "truncated": truncated,
        }
        shard_path = run_dir / f"{day_key}.json"
        write_json(shard_path, shard)
        day_items.append({
            "date": day_key,
            "path": str(shard_path.relative_to(output)),
            "event_count": count_actions(events),
            "tool_call_count": count_tool_calls(events),
            "forecast_count": count_forecasts(events),
            "truncated": truncated,
        })

    if not day_items:
        run_dir.rmdir()
    elif sum(day["tool_call_count"] for day in day_items) == 0:
        archive_dir = output / "archive" / agent_slug / run_id
        if archive_dir.exists():
            shutil.rmtree(archive_dir)
        archive_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(run_dir), archive_dir)
        day_items = []

    return {
        "agent_name": agent_name,
        "agent_slug": agent_slug,
        "model": model,
        "harness": harness,
        "harness_name": harness_name,
        "harness_slug": harness_slug,
        "seed_label": seed_label,
        "run_id": run_id,
        "run_label": run_label,
        "source_filename": source_path.name,
        "metrics": metrics,
        "days": day_items,
    }


def parse_run_spec(spec: str) -> tuple[str, str, str, str, str, str]:
    parts = spec.split("|")
    if len(parts) != 6:
        raise SystemExit("--run must have 6 pipe-separated fields: AGENT|SLUG|MODEL|HARNESS|SEED|PATH")
    return tuple(part.strip() for part in parts)  # type: ignore[return-value]


def read_metrics(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    metrics = []
    with path.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            metrics.append({
                "date": row.get("date", ""),
                "brier_skill_score": parse_float(row.get("avg_brier")),
                "top1_accuracy": parse_float(row.get("accuracy")),
            })
    return metrics


def harness_condition(cli: str, path: Path) -> str:
    cli_name = cli_label(cli)
    if not path.exists():
        return f"{cli_name} - Base"
    config = json.loads(path.read_text(encoding="utf-8"))
    sim_name = str(config.get("sim_name") or "")
    config_path = str(config.get("config") or "")
    text = f"{sim_name} {config_path}".lower()
    parts = []
    if "activemem2" in text or "active_mem2" in text:
        parts.append("Active memory 2")
    if "ultracode" in text:
        parts.append("Ultracode")
    defaults = config.get("defaults") if isinstance(config.get("defaults"), dict) else {}
    handholding = config.get("handholding_version") or defaults.get("handholding_version")
    if handholding:
        parts.append(f"Handholding {handholding}")
    elif "handholding_v3" in text:
        parts.append("Handholding v3")
    if "v3_prompt" in text:
        parts.append("V3 prompt")
    if "netiso" in text:
        parts.append("Net-isolated")
    if "safe" in text:
        parts.append("Safe")
    condition = " + ".join(dict.fromkeys(parts)) if parts else "Base"
    return f"{cli_name} - {condition}"


def cli_label(value: str) -> str:
    labels = {
        "claude code": "Claude Code",
        "codex": "Codex",
        "opencode": "OpenCode",
        "open code": "OpenCode",
    }
    return labels.get(value.lower(), value)


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "default"


def parse_float(value: Any) -> float | None:
    if value in {None, ""}:
        return None
    return float(value)


def normalize_event(raw: dict[str, Any], idx: int, sim_date: str, turn: int) -> dict[str, Any]:
    kind = str(raw.get("type") or "event")
    payload = raw.get("payload") if isinstance(raw.get("payload"), dict) else {}
    message = raw.get("message") if isinstance(raw.get("message"), dict) else {}
    item = raw.get("item") if isinstance(raw.get("item"), dict) else {}
    part = raw.get("part") if isinstance(raw.get("part"), dict) else {}
    role = str(message.get("role") or raw.get("role") or "")
    blocks = normalize_blocks(message.get("content")) if message else []

    if is_compaction_event(raw):
        event_kind = "compaction"
        blocks = [{"type": "compaction", "text": compaction_preview(raw)}]
    elif kind == "response_item" and payload:
        event_kind, role, blocks = normalize_codex_payload(payload)
    elif kind == "assistant" or role == "assistant":
        event_kind = "assistant"
    elif kind == "user":
        event_kind = "user"
    elif kind == "system":
        event_kind = "system"
        blocks = [{"type": "system", "text": system_preview(raw)}]
    elif kind == "result":
        event_kind = "result"
        blocks = [{"type": "system", "text": system_preview(raw)}]
    elif item:
        event_kind, blocks = normalize_codex_item(item)
        role = "assistant" if event_kind == "assistant" else role
    elif part:
        event_kind, blocks = normalize_opencode_part(kind, part)
        role = "assistant" if event_kind == "assistant" else role
    else:
        event_kind = kind
        if not blocks:
            blocks = [{"type": "system", "text": compact_text(raw)}]

    return {
        "idx": idx,
        "turn": turn,
        "kind": event_kind,
        "subtype": raw.get("subtype", ""),
        "role": role,
        "sim_date": sim_date,
        "time": event_time(raw),
        "session": raw.get("session_id") or raw.get("sessionID") or item.get("session_id") or part.get("sessionID") or payload.get("session_id") or "",
        "preview": preview_from_blocks(blocks),
        "blocks": blocks,
    }


def should_keep_event(event: dict[str, Any]) -> bool:
    blocks = event["blocks"]
    if event["kind"] == "compaction":
        return True
    if any(block.get("type") == "tool_result" for block in blocks):
        return True
    if event["kind"] != "assistant":
        return False
    return any(
        block.get("type") == "tool_use"
        or (block.get("type") == "text" and str(block.get("text", "")).strip())
        for block in blocks
    )


def normalize_blocks(content: Any) -> list[dict[str, Any]]:
    if isinstance(content, str):
        text = clean_string(content)
        return [{"type": "text", "text": text}] if text.strip() else []
    if not isinstance(content, list):
        return []

    blocks = []
    for part in content:
        if not isinstance(part, dict):
            continue
        part_type = part.get("type")
        if part_type in {"text", "input_text", "output_text"}:
            text = clean_string(str(part.get("text", "")))
            if text.strip():
                blocks.append({"type": "text", "text": text})
        elif part_type == "tool_use":
            blocks.append({
                "type": "tool_use",
                "id": str(part.get("id", "")),
                "name": str(part.get("name", "")),
                "input": sanitize(part.get("input", {})),
            })
        elif part_type == "tool_result":
            blocks.append({
                "type": "tool_result",
                "tool_use_id": str(part.get("tool_use_id", "")),
                "content": tool_result_text(part),
                "is_error": bool(part.get("is_error", False)),
            })
    return blocks


def normalize_codex_payload(payload: dict[str, Any]) -> tuple[str, str, list[dict[str, Any]]]:
    payload_type = payload.get("type")
    role = str(payload.get("role") or "")
    if payload_type == "message":
        if role == "assistant":
            return "assistant", role, normalize_blocks(payload.get("content"))
        return "user", role, normalize_blocks(payload.get("content"))
    if payload_type == "function_call":
        return "assistant", "assistant", [{
            "type": "tool_use",
            "id": str(payload.get("call_id") or ""),
            "name": str(payload.get("name") or "tool"),
            "input": sanitize(parse_json_maybe(payload.get("arguments", {}))),
        }]
    if payload_type == "function_call_output":
        return "tool_result", "tool", [{
            "type": "tool_result",
            "tool_use_id": str(payload.get("call_id") or ""),
            "content": clean_string(str(payload.get("output") or "")),
            "is_error": False,
        }]
    return "system", role, []


def normalize_codex_item(item: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    item_type = item.get("type")
    if item_type == "agent_message":
        return "assistant", [{"type": "text", "text": clean_string(str(item.get("text", "")))}]
    if item_type in {"mcp_tool_call", "tool_call"}:
        tool_name = item.get("tool") or item.get("name") or "tool"
        call_id = str(item.get("id", ""))
        blocks = []
        if item.get("status") == "in_progress" or item.get("result") is None and not item.get("error"):
            blocks.append({
                "type": "tool_use",
                "id": call_id,
                "name": str(tool_name),
                "input": sanitize(item.get("arguments", item.get("input", {}))),
            })
            return "assistant", blocks
        blocks.append({
            "type": "tool_result",
            "tool_use_id": call_id,
            "content": tool_result_text({"content": item.get("result") or item.get("error") or ""}),
            "is_error": bool(item.get("error")),
        })
        return "tool_result", blocks
    if item_type == "command_execution":
        blocks = [{
            "type": "tool_use",
            "id": str(item.get("id", "")),
            "name": "Bash",
            "input": {"command": clean_string(str(item.get("command", "")))},
        }]
        if item.get("aggregated_output"):
            blocks.append({
                "type": "tool_result",
                "tool_use_id": str(item.get("id", "")),
                "content": clean_string(str(item.get("aggregated_output", ""))),
                "is_error": bool(item.get("exit_code")),
            })
        return "assistant", blocks
    return "system", [{"type": "system", "text": compact_text(item)}]


def normalize_opencode_part(kind: str, part: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    if part.get("type") == "text":
        return "assistant", [{"type": "text", "text": clean_string(str(part.get("text", "")))}]
    if part.get("type") == "tool":
        state = part.get("state") if isinstance(part.get("state"), dict) else {}
        call_id = str(part.get("callID") or part.get("id") or "")
        tool_name = str(part.get("tool") or state.get("title") or "tool")
        if kind == "tool_use" or state:
            blocks = [{
                "type": "tool_use",
                "id": call_id,
                "name": tool_name,
                "input": sanitize(state.get("input", {})),
            }]
            if state.get("status") in {"completed", "error"} or state.get("output") or state.get("error"):
                blocks.append({
                    "type": "tool_result",
                    "tool_use_id": call_id,
                    "content": clean_string(str(state.get("output") or state.get("error") or "")),
                    "is_error": state.get("status") == "error" or bool(state.get("error")),
                })
            return "assistant", blocks
    return "system", [{"type": "system", "text": compact_text(part)}]


def tool_result_text(part: dict[str, Any]) -> str:
    content = part.get("content", "")
    if isinstance(content, str):
        return content
    return compact_text(content, limit=20000)


def annotate_forecast_history(event: dict[str, Any], history: dict[str, dict[str, float]]) -> None:
    for block in event["blocks"]:
        if block.get("type") != "tool_use" or "submit_forecasts" not in str(block.get("name", "")):
            continue
        input_data = block.get("input") if isinstance(block.get("input"), dict) else {}
        qid = str(input_data.get("question_id") or "")
        outcomes = input_data.get("outcomes")
        if not qid or not isinstance(outcomes, dict):
            continue
        current = {str(name): float(prob) for name, prob in outcomes.items() if isinstance(prob, int | float)}
        if qid in history:
            input_data["previous_outcomes"] = history[qid]
        history[qid] = current


def is_compaction_event(raw: dict[str, Any]) -> bool:
    return raw.get("type") == "compacted" or raw.get("subtype") == "compact_boundary"


def compaction_preview(raw: dict[str, Any]) -> str:
    metadata = raw.get("compact_metadata") if isinstance(raw.get("compact_metadata"), dict) else {}
    if metadata:
        trigger = metadata.get("trigger") or "auto"
        pre_tokens = metadata.get("pre_tokens")
        post_tokens = metadata.get("post_tokens")
        if isinstance(pre_tokens, int) and isinstance(post_tokens, int):
            return f"Context compacted ({trigger}): {pre_tokens:,} -> {post_tokens:,} tokens"
        return f"Context compacted ({trigger})"

    payload = raw.get("payload") if isinstance(raw.get("payload"), dict) else {}
    history = payload.get("replacement_history") if isinstance(payload.get("replacement_history"), list) else []
    if history:
        return f"Context compacted: replaced {len(history)} prior messages"
    return "Context compacted"


def sanitize(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: sanitize(val) for key, val in value.items() if key not in DROP_KEYS}
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, str):
        return clean_string(value)
    return value


def parse_json_maybe(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def clean_string(value: str) -> str:
    if len(value) > MAX_STRING_CHARS:
        value = value[:MAX_STRING_CHARS] + "\n[...truncated]"
    return SECRET_RE.sub("[redacted]", value)


def event_time(raw: dict[str, Any]) -> str:
    ts = raw.get("timestamp") or raw.get("ts")
    if not ts:
        return ""
    try:
        parsed = datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
    except ValueError:
        return str(ts)
    return parsed.strftime("%H:%M:%S")


def compact_text(value: Any, limit: int = 1200) -> str:
    if isinstance(value, str):
        text = value
    else:
        text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    text = text.replace("\u001b", "")
    return text if len(text) <= limit else text[: limit - 15] + "\n[...truncated]"


def system_preview(raw: dict[str, Any]) -> str:
    if raw.get("subtype") == "init":
        tools = raw.get("tools") if isinstance(raw.get("tools"), list) else []
        model = raw.get("model", "")
        return f"Session started. Model: {model}. Tools: {len(tools)}."
    return compact_text(raw)


def preview_from_blocks(blocks: list[dict[str, Any]]) -> str:
    for block in blocks:
        if block["type"] == "text" and block.get("text"):
            return str(block["text"])[:220]
        if block["type"] == "compaction" and block.get("text"):
            return str(block["text"])[:220]
        if block["type"] == "tool_use":
            return f"{block.get('name', 'tool')} {compact_text(block.get('input', {}), 180)}"
    return ""


def event_has_tool_result(event: dict[str, Any]) -> bool:
    return any(block.get("type") == "tool_result" for block in event["blocks"])


def count_tool_calls(events: list[dict[str, Any]]) -> int:
    return sum(1 for event in events for block in event["blocks"] if block.get("type") == "tool_use")


def count_actions(events: list[dict[str, Any]]) -> int:
    return sum(
        1
        for event in events
        if event["kind"] == "assistant" and any(block.get("type") != "tool_result" for block in event["blocks"])
    )


def count_forecasts(events: list[dict[str, Any]]) -> int:
    return sum(
        1
        for event in events
        for block in event["blocks"]
        if block.get("type") == "tool_use" and "submit_forecasts" in block.get("name", "")
    )


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
