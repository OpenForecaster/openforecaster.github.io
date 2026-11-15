#!/usr/bin/env python3
"""Read a Codex or Muse session-log directory as one FutureSim trace.

The trace viewer's data is normally built from a harness's stdout transcript. For two harnesses
that transcript leaves out most of the run, so their traces are built from the session logs:

* Codex, `agents/<agent>/codex_sessions/rollout-*.jsonl`. The root agent hands most questions to
  sub-agents, and each sub-agent has a rollout file of its own. stdout has the root agent only.
* Muse, `agents/<agent>/muse_sessions/**/session.jsonl`. stdout carries no tool arguments, and the
  sub-agents a workflow starts are separate sessions under `subagent/`.

read_session_log(path, start_date) returns (events, notes). Each event is a SessionEvent: a record
shaped like a Claude Code transcript line (which build_futuresim_trace_viewer_data.py already
normalizes), the simulation day it belongs to, and the sub-agent that produced it ("" for the root
agent).

Simulation days come from the root agent's own prompts ("Begin forecasting..." on the first day of
a session, "Simulation advanced to <date>..." after that), never from guessing at tool calls.
A sub-agent's event belongs to the day whose prompt was the last one before it.

Sub-agents run in parallel with the root agent. Interleaving them by time would make every thread
unreadable, so each stretch of one sub-agent's work within a day is kept together and placed in
the root agent's timeline at the moment that stretch began.

What the logs do not contain, and so the trace does not either: model reasoning (stored
encrypted), and the text of the messages Codex agents send each other (also encrypted; the call is
shown with a placeholder).

    python3 scripts/futuresim_session_logs.py PATH --start 2026-06-24     # per-day counts
"""

from __future__ import annotations

import argparse
import json
import re
from bisect import bisect_right
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ADVANCED_RE = re.compile(r"Simulation advanced to (20\d{2}-\d{2}-\d{2})")
BEGIN_PREFIX = "Begin forecasting"
ENCRYPTED_NOTE = "[encrypted in the session log]"
CODEX_COLLABORATION = "collaboration"


@dataclass
class SessionEvent:
    raw: dict[str, Any]
    day: str
    subagent: str = ""


@dataclass
class _Thread:
    """One agent's records, in the order it produced them."""

    thread_id: str
    label: str = ""  # "" for a root agent
    parent_id: str = ""
    # (time, stretch key, raw record). A stretch is one turn of a sub-agent.
    items: list[tuple[float, str, dict[str, Any]]] = field(default_factory=list)
    # Root agents only: (time, prompt text, index into items where that day's records start).
    prompts: list[tuple[float, str, int]] = field(default_factory=list)


def is_session_log(path: Path) -> bool:
    return path.is_dir() and path.name in {"codex_sessions", "muse_sessions"}


def read_session_log(path: Path, start_date: date) -> tuple[list[SessionEvent], list[str]]:
    if path.name == "codex_sessions":
        threads = _read_codex(path)
    elif path.name == "muse_sessions":
        threads = _read_muse(path)
    else:
        raise SystemExit(f"Not a session-log directory: {path}")
    return _merge(threads, start_date)


# --- Shared: days and placement ---------------------------------------------------------------


def _merge(threads: dict[str, _Thread], start_date: date) -> tuple[list[SessionEvent], list[str]]:
    notes: list[str] = []
    roots = sorted((t for t in threads.values() if not t.label), key=lambda t: t.prompts[0][0] if t.prompts else 0.0)
    if not roots:
        raise SystemExit("No root session found in the session log.")

    children: dict[str, list[_Thread]] = defaultdict(list)
    for thread in threads.values():
        if not thread.label:
            continue
        root = _root_of(thread, threads)
        if root is None:
            notes.append(f"sub-agent {thread.label}: no root session, {len(thread.items)} records left out")
            continue
        children[root.thread_id].append(thread)

    events: list[SessionEvent] = []
    previous_day: date | None = None
    for root in roots:
        if not root.prompts:
            notes.append(f"root session {root.thread_id}: no day prompts, {len(root.items)} records left out")
            continue
        days = _prompt_days(root.prompts, previous_day, start_date)
        previous_day = days[-1]
        starts = [prompt[0] for prompt in root.prompts]

        # Root records per day, in order.
        per_day: list[list[tuple[float, str, dict[str, Any]]]] = []
        for index, (_, _, first_item) in enumerate(root.prompts):
            end = root.prompts[index + 1][2] if index + 1 < len(root.prompts) else len(root.items)
            per_day.append([(time, "", raw) for time, _, raw in root.items[first_item:end]])
        if root.prompts[0][2]:
            notes.append(f"root session {root.thread_id}: {root.prompts[0][2]} records before the first prompt left out")

        # Sub-agent stretches, cut at day boundaries.
        stretches: dict[int, list[tuple[float, str, list[tuple[float, str, dict[str, Any]]]]]] = defaultdict(list)
        for child in children.get(root.thread_id, []):
            current: tuple[int, str] | None = None
            early = 0
            for time, stretch, raw in child.items:
                day_index = bisect_right(starts, time) - 1
                if day_index < 0:
                    early += 1
                    continue
                key = (day_index, stretch)
                if key != current:
                    stretches[day_index].append((time, child.label, []))
                    current = key
                stretches[day_index][-1][2].append((time, child.label, raw))
            if early:
                notes.append(f"sub-agent {child.label}: {early} records before its root session's first prompt left out")

        for day_index, day in enumerate(days):
            merged = _place(per_day[day_index], sorted(stretches.get(day_index, []), key=lambda s: s[0]))
            events.extend(SessionEvent(raw=raw, day=day.isoformat(), subagent=label) for _, label, raw in merged)

    return events, notes


def _root_of(thread: _Thread, threads: dict[str, _Thread]) -> _Thread | None:
    seen = set()
    current: _Thread | None = thread
    while current is not None and current.label and current.thread_id not in seen:
        seen.add(current.thread_id)
        current = threads.get(current.parent_id)
    return current if current is not None and not current.label else None


def _prompt_days(prompts: list[tuple[float, str, int]], previous_day: date | None, start_date: date) -> list[date]:
    """The simulation day each prompt of one root session opens.

    A session's first prompt ("Begin forecasting...") names no date: it is the day before the next
    prompt's, which also holds for a session that resumed a run part-way through.
    """
    stated = []
    for _, text, _ in prompts:
        match = ADVANCED_RE.search(text)
        stated.append(date.fromisoformat(match.group(1)) if match else None)
    days: list[date] = []
    for index, day in enumerate(stated):
        if day is None:
            following = stated[index + 1] if index + 1 < len(stated) else None
            if following is not None:
                day = following - timedelta(days=1)
            elif days:
                day = days[-1] + timedelta(days=1)
            elif previous_day is not None:
                day = previous_day + timedelta(days=1)
            else:
                day = start_date
        days.append(day)
    return days


def _place(root_items, stretches):
    """Insert each sub-agent stretch before the first root record that is later than its start."""
    merged = []
    pending = list(stretches)
    for item in root_items:
        while pending and pending[0][0] < item[0]:
            merged.extend(pending.pop(0)[2])
        merged.append(item)
    for _, _, items in pending:
        merged.extend(items)
    return merged


def _assistant(time: float, session: str, content: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "type": "assistant",
        "timestamp": datetime.fromtimestamp(time, timezone.utc).isoformat(),
        "session_id": session,
        "message": {"role": "assistant", "content": content},
    }


def _tool(call_id: str, name: str, arguments: Any) -> dict[str, Any]:
    return {"type": "tool_use", "id": call_id, "name": name, "input": arguments}


def _result(call_id: str, text: Any, is_error: bool = False) -> dict[str, Any]:
    return {"type": "tool_result", "tool_use_id": call_id, "content": text, "is_error": is_error}


def _json_or_text(value: Any) -> Any:
    if not isinstance(value, str):
        return value
    try:
        return json.loads(value)
    except json.JSONDecodeError:
        return value


def _mcp_text(result: Any) -> str:
    """The text of an MCP tool result ({"content": [{"type": "text", "text": ...}]})."""
    result = _json_or_text(result)
    if isinstance(result, dict) and isinstance(result.get("content"), list):
        texts = [part.get("text", "") for part in result["content"] if isinstance(part, dict)]
        return "\n".join(text for text in texts if text)
    if isinstance(result, str):
        return result
    return "" if result is None else json.dumps(result, ensure_ascii=False)


# --- Codex ------------------------------------------------------------------------------------


def _read_codex(sessions_dir: Path) -> dict[str, _Thread]:
    threads: dict[str, _Thread] = {}
    for path in sorted(sessions_dir.glob("rollout-*.jsonl")):
        thread = _read_codex_rollout(path)
        if thread is not None:
            threads[thread.thread_id] = thread
    return threads


def _iso_seconds(value: str) -> float:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


def _read_codex_rollout(path: Path) -> _Thread | None:
    with path.open(encoding="utf-8") as handle:
        meta = json.loads(handle.readline()).get("payload") or {}
        thread_id = str(meta.get("id") or "")
        if not thread_id:
            return None
        source = meta.get("source")
        spawn = source.get("subagent", {}).get("thread_spawn", {}) if isinstance(source, dict) else {}
        agent_path = str(spawn.get("agent_path") or meta.get("agent_path") or "")
        thread = _Thread(
            thread_id=thread_id,
            label=(agent_path.removeprefix("/root/") or thread_id[:8]) if isinstance(source, dict) else "",
            parent_id=str(spawn.get("parent_thread_id") or meta.get("parent_thread_id") or ""),
        )
        # A sub-agent's file opens with a copy of its parent's context; its own records follow.
        own_from = int(meta.get("subagent_history_start_ordinal") or 0)
        turn = ""
        calls: dict[str, dict[str, Any]] = {}

        for line in handle:
            # Most of the file is model context and token accounting; skip it without parsing.
            if "item_completed" not in line and "function_call" not in line and "task_started" not in line:
                continue
            record = json.loads(line)
            if int(record.get("ordinal") or 0) < own_from:
                continue
            payload = record.get("payload") if isinstance(record.get("payload"), dict) else {}
            kind, payload_type = record.get("type"), payload.get("type")
            time = _iso_seconds(record["timestamp"])

            if kind == "event_msg" and payload_type == "task_started":
                turn = str(payload.get("turn_id") or "")
            elif kind == "event_msg" and payload_type == "item_completed":
                if payload.get("thread_id") != thread_id or not isinstance(payload.get("item"), dict):
                    continue
                item = payload["item"]
                if item.get("type") == "UserMessage":
                    if not thread.label:
                        thread.prompts.append((time, _codex_text(item), len(thread.items)))
                    continue
                content = _codex_item(item)
                if content == "compaction":
                    thread.items.append((time, turn, {"type": "compacted", "timestamp": record["timestamp"], "session_id": thread_id}))
                elif content:
                    thread.items.append((time, turn, _assistant(time, thread_id, content)))
            elif kind == "response_item" and payload_type == "function_call":
                if payload.get("namespace") != CODEX_COLLABORATION:
                    continue
                call_id = str(payload.get("call_id") or "")
                raw = _assistant(time, thread_id, [_tool(call_id, str(payload.get("name") or "tool"), _collaboration_arguments(payload.get("arguments")))])
                calls[call_id] = raw
                thread.items.append((time, turn, raw))
            elif kind == "response_item" and payload_type == "function_call_output":
                raw = calls.pop(str(payload.get("call_id") or ""), None)
                output = payload.get("output")
                if raw is not None and output:
                    raw["message"]["content"].append(_result(str(payload.get("call_id")), output if isinstance(output, str) else json.dumps(output, ensure_ascii=False)))
    return thread


def _codex_text(item: dict[str, Any]) -> str:
    parts = item.get("content") if isinstance(item.get("content"), list) else []
    return "\n".join(str(part.get("text") or "") for part in parts if isinstance(part, dict)).strip()


def _codex_item(item: dict[str, Any]) -> list[dict[str, Any]] | str:
    """The content of one completed Codex item, "compaction", or [] for items that are not shown."""
    item_type = item.get("type")
    call_id = str(item.get("id") or "")
    if item_type == "AgentMessage":
        text = _codex_text(item)
        return [{"type": "text", "text": text}] if text else []
    if item_type == "CommandExecution":
        command = item.get("command")
        if isinstance(command, list):
            # ["/usr/bin/bash", "-lc", script]
            command = command[-1] if len(command) == 3 and command[1] in {"-lc", "-c"} else " ".join(str(part) for part in command)
        content = [_tool(call_id, "Bash", {"command": str(command or "")})]
        output = str(item.get("aggregated_output") or "")
        failed = bool(item.get("exit_code")) or item.get("status") == "failed"
        if output or failed:
            content.append(_result(call_id, output or f"[exit code {item.get('exit_code')}]", failed))
        return content
    if item_type == "McpToolCall":
        content = [_tool(call_id, str(item.get("tool") or "tool"), _json_or_text(item.get("arguments")) or {})]
        error = item.get("error")
        if error:
            content.append(_result(call_id, error if isinstance(error, str) else json.dumps(error, ensure_ascii=False), True))
        elif item.get("result") is not None:
            content.append(_result(call_id, _mcp_text(item.get("result")), item.get("status") == "failed"))
        return content
    if item_type == "FileChange":
        changes = _json_or_text(item.get("changes"))
        files = []
        if isinstance(changes, dict):
            for file_path, change in changes.items():
                change = change if isinstance(change, dict) else {}
                entry = {"path": file_path, "change": change.get("type", "")}
                if change.get("move_path"):
                    entry["moved_to"] = change["move_path"]
                if "content" in change:
                    entry["content"] = change["content"]
                if "unified_diff" in change:
                    entry["diff"] = change["unified_diff"]
                files.append(entry)
        content = [_tool(call_id, "file_change", {"files": files})]
        if item.get("status") == "failed":
            content.append(_result(call_id, str(item.get("stderr") or item.get("stdout") or "File change failed."), True))
        return content
    if item_type == "ContextCompaction":
        return "compaction"
    return []


def _collaboration_arguments(arguments: Any) -> Any:
    arguments = _json_or_text(arguments)
    if isinstance(arguments, dict) and "message" in arguments:
        arguments = {**arguments, "message": ENCRYPTED_NOTE}
    return arguments


# --- Muse -------------------------------------------------------------------------------------


def _read_muse(sessions_dir: Path) -> dict[str, _Thread]:
    threads: dict[str, _Thread] = {}
    for path in sorted(sessions_dir.rglob("session.jsonl")):
        if path.parent.parent.name == "subagent":
            continue
        root_id = path.parent.name
        root, labels = _read_muse_session(path, root_id, "")
        threads[root_id] = root
        for child_path in sorted((path.parent / "subagent").glob("*/session.jsonl")):
            child_id = child_path.parent.name
            child, _ = _read_muse_session(child_path, child_id, labels.get(child_id) or child_id[:8])
            child.parent_id = root_id
            threads[child_id] = child
    return threads


def _read_muse_session(path: Path, session_id: str, label: str) -> tuple[_Thread, dict[str, str]]:
    thread = _Thread(thread_id=session_id, label=label)
    labels: dict[str, str] = {}  # child session id -> the name its workflow gave it
    calls: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if "_committed" not in line and "user_intent.accepted" not in line and "workflow_child_lifecycle" not in line:
                continue
            record = json.loads(line)
            payload = record.get("payload") if isinstance(record.get("payload"), dict) else {}
            time = float(record.get("recorded_at") or 0) / 1e6
            payload_type = record.get("payload_type")

            if payload_type == "runtime.user_intent.accepted":
                if not label:
                    thread.prompts.append((time, _muse_prompt(payload), len(thread.items)))
                continue
            if payload_type != "runtime.session" or not isinstance(payload.get("event"), dict):
                continue
            event = payload["event"]
            kind = event.get("kind")
            if kind == "workflow_child_lifecycle":
                child = event.get("session_stream") if isinstance(event.get("session_stream"), dict) else {}
                if child.get("id") and event.get("label"):
                    labels[str(child["id"])] = str(event["label"])
            elif kind == "assistant_message_committed":
                text = str(event.get("text") or "").strip()
                if text:
                    thread.items.append((time, "", _assistant(time, session_id, [{"type": "text", "text": text}])))
            elif kind == "assistant_tool_calls_committed":
                content = []
                for call in event.get("tool_calls") or []:
                    call_id = str(call.get("call_id") or call.get("id") or "")
                    content.append(_tool(call_id, str(call.get("name") or "tool"), _json_or_text(call.get("args")) or {}))
                if content:
                    raw = _assistant(time, session_id, content)
                    for part in content:
                        calls[part["id"]] = raw
                    thread.items.append((time, "", raw))
            elif kind == "tool_result_batch_committed":
                for result in event.get("results") or []:
                    call_id = str(result.get("tool_call_id") or "")
                    raw = calls.pop(call_id, None)
                    if raw is None:
                        continue
                    name = next((part["name"] for part in raw["message"]["content"] if part.get("id") == call_id), "")
                    text, is_error = _muse_result(name, result.get("text"))
                    raw["message"]["content"].append(_result(call_id, text, is_error))
    return thread, labels


def _muse_prompt(payload: dict[str, Any]) -> str:
    texts = []
    for message in payload.get("model_messages") or []:
        for part in message.get("content") or [] if isinstance(message, dict) else []:
            if isinstance(part, dict) and part.get("text"):
                texts.append(str(part["text"]))
    return "\n".join(texts).strip()


def _muse_result(name: str, text: Any) -> tuple[str, bool]:
    """A tool result's text. The shell tool wraps its output in a JSON record; unwrap it."""
    text = "" if text is None else str(text)
    if name == "bash":
        record = _json_or_text(text)
        if isinstance(record, dict) and "output" in record:
            exit_code = record.get("exit_code")
            output = str(record.get("output") or "")
            failed = bool(exit_code)
            if failed and not output:
                output = f"[exit code {exit_code}]"
            return output, failed
    return text, False


# --- Command line: a quick look at what a log contains ----------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description="Print per-day counts for a Codex or Muse session-log directory.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--start", required=True, type=date.fromisoformat, help="First simulation day.")
    args = parser.parse_args()

    events, notes = read_session_log(args.path, args.start)
    per_day: dict[str, Counter] = defaultdict(Counter)
    for event in events:
        counts = per_day[event.day]
        counts["records"] += 1
        counts["sub-agent records"] += bool(event.subagent)
        for part in event.raw.get("message", {}).get("content", []):
            if part.get("type") == "tool_use":
                counts["tool calls"] += 1
                counts["forecasts"] += "submit_forecasts" in part["name"]
    for day in sorted(per_day):
        counts = per_day[day]
        print(day, *(f"{name}={counts[name]}" for name in ("records", "sub-agent records", "tool calls", "forecasts")))
    print(f"{len(per_day)} days, {len(events)} records")
    for note in notes:
        print("note:", note)


if __name__ == "__main__":
    main()
