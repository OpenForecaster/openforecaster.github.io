#!/usr/bin/env python3
"""Add each run's token counts and wall-clock time to a trace viewer manifest.

    python3 scripts/build_futuresim_run_usage.py --data-dir futuresim/traces/data/q3 --runs-root <runs>

A run in <data-dir>/manifest.json whose folder (its `source_run`) is under --runs-root gets

    "tokens": {"main": {...}, "subagents": {...}, "other": {...}}
    "wall_clock": {"seconds": ..., "restarts": ..., "restart_wait_seconds": ...}

and each entry of its `days` gets `"tokens": {...}`, the counts of that simulation day.

Tokens
------
"main" is the run's own agent, "subagents" the agents it started, and "other" the model calls the
harness made by itself (Muse's reminder sessions). Each of the three holds

* `input`: every token sent to the model, summed over its calls. An agent sends its whole context
  with each call, so the same text is counted many times and most of it is cached.
* `cached_input`: the part of `input` that the provider read from its prompt cache.
* `output`: every token the model generated, reasoning included.
* `reasoning_output`: the part of `output` that was reasoning. Only Codex and Muse log it, so
  only their runs have this key.

A day's `tokens` holds `input`, `cached_input` and `output` over all three owners. The days of a
run add up to its totals.

The numbers are read from each harness's session logs, the way analysis/src/q3_v8_output_tokens.py
in the simulator's repository counts output tokens, so the output totals here are the ones behind
its figure. stdout is not enough: Codex's reports usage for the first turn only, and Claude Code's
carries the output count from the start of a message, not from its end.

* Claude Code, `claude_config/projects/**/*.jsonl` (the main session and `subagents/`). A message
  is logged once per content block and each copy repeats its usage, so it is counted once per
  message id. A Claude Code process that ended normally also reports its own total (the
  `modelUsage` of a `result` line in stdout). That total covers the context-compaction calls,
  which the transcripts leave out, so it is used in place of the sum of the process's transcript
  messages, and the difference is put on the main agent: in equal parts at the process's
  compactions, or over its messages if it had none (then the difference is small). A process that
  was stopped reports nothing, and its compaction calls are not counted. Input is `input_tokens` +
  `cache_creation_input_tokens` + `cache_read_input_tokens`.
* Codex, `codex_sessions/**/*.jsonl`, one rollout per thread: the `token_usage_record` lines, which
  also cover context compaction. `input_tokens` already includes the cached ones.
* Muse, `muse_sessions/**/session.jsonl`: the usage records of the "provider" family. Besides the
  main agent and the sub-agents of its workflows, Muse runs reminder sessions of its own.
* Antigravity, `agy_conversations/*.jsonl`: the per-step counts. The main conversation is the one
  `agy_stdout.jsonl` opens and every other one is a sub-agent. Input is `input_tokens` +
  `cache_read_tokens`.

Days
----
A model call belongs to the simulation day that was open when it was logged. In Claude Code a day
opens when the main agent's `next_day` call returns "Day advanced to <date>". Codex, Muse and
Antigravity are started once per day, and a day opens with the root agent's prompt for it
(futuresim_session_logs.day_prompts). The trace builder cuts the days at the same places.

Wall-clock time
---------------
`seconds` is the time from the run's first log record to its last, without the wait before each
restart. A run that was interrupted (a usage limit, a quota, a crashed job) was restarted later
in a new session, which opens with "Begin forecasting" as the first one does. The run's folder
holds nothing between the last record before such a session and the session's first record: the
run was stopped, or doing work on a day that the restart redid. That gap is left out; `restarts`
is how many there were and `restart_wait_seconds` their total. Everything else is counted: the
model's and the tools' time, the simulator's own step from one day to the next, and the seconds
a harness takes to start an agent again. In the 2026 Q3 runs no other silence is longer than
seven minutes, so no threshold is needed to tell a wait from work.

A run with none of these logs is left without the fields. For a run that was restarted, the work
of the days that the restart redid is not in its folder, so neither its tokens nor its time are
counted.
"""

from __future__ import annotations

import argparse
import json
import re
from bisect import bisect_left, bisect_right
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Iterator

from futuresim_session_logs import BEGIN_PREFIX, day_prompts

OWNERS = ("main", "subagents", "other")
QUANTITIES = ("input", "cached_input", "output")
REASONING = "reasoning_output"
DAY_ADVANCED_RE = re.compile(r"Day advanced to (20\d{2}-\d{2}-\d{2})")
Counts = dict[str, int]


@dataclass
class RunLog:
    """What a run's session logs say about its model calls and its time."""

    calls: list[tuple[float, str, Counts]] = field(default_factory=list)  # (time, owner, tokens)
    times: list[float] = field(default_factory=list)  # the time of every record, of any agent
    day_starts: list[tuple[float, str]] = field(default_factory=list)  # (time, the day that opens)
    restarts: list[float] = field(default_factory=list)  # the first record of each restarted session


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data-dir", required=True, type=Path, help="Trace data root (holds manifest.json).")
    parser.add_argument("--runs-root", required=True, type=Path, help="Folder of runs that the manifest's source_run is under.")
    args = parser.parse_args()

    manifest_path = args.data_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for run in manifest["runs"]:
        name = f"{run['agent_slug']} {run['seed_label']}"
        dates = sorted(day["date"] for day in run["days"])
        agent_dir = find_agent_dir(args.runs_root, run)
        log = read_log(agent_dir, date.fromisoformat(dates[0])) if agent_dir and dates else None
        if log is None:
            run.pop("tokens", None)
            run.pop("wall_clock", None)
            for day in run["days"]:
                day.pop("tokens", None)
            print(f"{name}: no session logs, left without tokens and wall-clock time")
            continue

        per_day = tokens_per_day(log, dates[0])
        unknown = sorted(set(per_day) - set(dates))
        if unknown:
            raise SystemExit(f"{name}: the session logs have model calls on {unknown}, which the trace has no day for")
        run["tokens"] = token_totals(log)
        run["wall_clock"] = wall_clock(log)
        for day in run["days"]:
            day["tokens"] = per_day.get(day["date"]) or dict.fromkeys(QUANTITIES, 0)
        print(
            f"{name}: "
            + ", ".join(f"{quantity} {sum(run['tokens'][owner][quantity] for owner in OWNERS):,}" for quantity in QUANTITIES)
            + f", {run['wall_clock']['seconds'] / 3600:.2f} h"
            + (f" without {run['wall_clock']['restart_wait_seconds'] / 3600:.2f} h before {run['wall_clock']['restarts']} restart(s)" if run["wall_clock"]["restarts"] else "")
        )
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def find_agent_dir(runs_root: Path, run: dict[str, Any]) -> Path | None:
    if not run.get("source_run"):
        return None
    agents = sorted(path for path in (runs_root / run["source_run"] / "agents").glob("*") if path.is_dir())
    return agents[0] if len(agents) == 1 else None


def read_log(agent_dir: Path, first_day: date) -> RunLog | None:
    if (agent_dir / "claude_config" / "projects").is_dir():
        return read_claude_code(agent_dir)
    for folder, read in (("codex_sessions", read_codex), ("muse_sessions", read_muse), ("agy_conversations", read_antigravity)):
        if (agent_dir / folder).is_dir():
            log, session_starts = read(agent_dir)
            prompts = day_prompts(agent_dir / folder, first_day)
            log.day_starts = [(time, day) for time, day, _ in prompts]
            # A session's own first records come a moment before its "Begin forecasting" prompt.
            session_starts.sort()
            for time, _, opens_session in prompts[1:]:
                if opens_session:
                    log.restarts.append(session_starts[max(bisect_right(session_starts, time) - 1, 0)])
            return log
    return None


# --- What the manifest gets -------------------------------------------------------------------


def token_totals(log: RunLog) -> dict[str, Counts]:
    quantities = QUANTITIES + ((REASONING,) if any(REASONING in counts for _, _, counts in log.calls) else ())
    totals = {owner: dict.fromkeys(quantities, 0) for owner in OWNERS}
    for _, owner, counts in log.calls:
        for quantity, amount in counts.items():
            totals[owner][quantity] += amount
    return totals


def tokens_per_day(log: RunLog, first_day: str) -> dict[str, Counts]:
    starts = sorted(log.day_starts)
    times = [time for time, _ in starts]
    per_day: dict[str, Counts] = {}
    for time, _, counts in log.calls:
        index = bisect_right(times, time) - 1
        totals = per_day.setdefault(starts[index][1] if index >= 0 else first_day, dict.fromkeys(QUANTITIES, 0))
        for quantity in QUANTITIES:
            totals[quantity] += counts[quantity]
    return per_day


def wall_clock(log: RunLog) -> dict[str, int]:
    times = sorted(log.times)
    waits = []
    for restart in log.restarts:
        index = bisect_left(times, restart)
        if index:
            waits.append(times[index] - times[index - 1])
    return {
        "seconds": round(times[-1] - times[0] - sum(waits)),
        "restarts": len(waits),
        "restart_wait_seconds": round(sum(waits)),
    }


# --- The four harnesses -----------------------------------------------------------------------


def read_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def iso_seconds(value: str) -> float:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()


def read_claude_code(agent_dir: Path) -> RunLog:
    log = RunLog()
    messages: dict[str, dict[str, Any]] = {}  # message id -> owner, first time, counts
    compactions: list[float] = []
    sessions: list[tuple[float, str]] = []  # (first record, first prompt) of each main session
    for path in sorted((agent_dir / "claude_config" / "projects").rglob("*.jsonl")):
        is_main = "subagents" not in path.parts
        first_time, first_prompt = None, None
        next_day_calls: set[str] = set()
        for event in read_jsonl(path):
            if not event.get("timestamp"):
                continue
            time = iso_seconds(event["timestamp"])
            log.times.append(time)
            first_time = time if first_time is None else first_time
            kind = event.get("type")
            content = (event.get("message") or {}).get("content")
            blocks = [block for block in content if isinstance(block, dict)] if isinstance(content, list) else []
            if kind == "assistant":
                usage = event["message"]["usage"]
                fresh = (usage.get("input_tokens") or 0) + (usage.get("cache_creation_input_tokens") or 0)
                cached = usage.get("cache_read_input_tokens") or 0
                counts = {"input": fresh + cached, "cached_input": cached, "output": usage.get("output_tokens") or 0}
                seen = messages.setdefault(event["message"]["id"], {"owner": "main" if is_main else "subagents", "first": time, "counts": counts})
                seen["first"] = min(seen["first"], time)
                seen["counts"] = {quantity: max(seen["counts"][quantity], counts[quantity]) for quantity in QUANTITIES}
                if is_main:
                    next_day_calls.update(block["id"] for block in blocks if block.get("type") == "tool_use" and "next_day" in block.get("name", ""))
            elif kind == "user" and is_main:
                if first_prompt is None:
                    texts = [content] if isinstance(content, str) else [block.get("text", "") for block in blocks if block.get("type") == "text"]
                    first_prompt = texts[0] if texts else None
                for block in blocks:
                    if block.get("type") == "tool_result" and block.get("tool_use_id") in next_day_calls:
                        advanced = DAY_ADVANCED_RE.search(json.dumps(block.get("content")))
                        if advanced:
                            log.day_starts.append((time, advanced.group(1)))
            elif kind == "system" and event.get("subtype") == "compact_boundary" and is_main:
                compactions.append(time)
        if is_main and first_time is not None:
            sessions.append((first_time, first_prompt or ""))
    log.calls = [(message["first"], message["owner"], message["counts"]) for message in messages.values()]
    log.restarts = [first_time for first_time, prompt in sorted(sessions)[1:] if prompt.startswith(BEGIN_PREFIX)]

    # One process per "init" line of stdout. Its transcript messages are the ones from its first
    # message up to the next process's first. A process that logged no message is skipped: a
    # resume that did nothing repeats the previous process's total.
    processes: list[dict[str, Any]] = []
    for event in read_jsonl(agent_dir / "claude_code_stdout.jsonl"):
        if event.get("type") == "system" and event.get("subtype") == "init":
            processes.append({"ids": [], "reported": None})
        elif not processes:
            continue
        elif event.get("type") == "assistant":
            processes[-1]["ids"].append(event["message"]["id"])
        elif event.get("type") == "result" and event.get("modelUsage"):
            models = event["modelUsage"].values()
            cached = sum(model.get("cacheReadInputTokens") or 0 for model in models)
            fresh = sum((model.get("inputTokens") or 0) + (model.get("cacheCreationInputTokens") or 0) for model in models)
            processes[-1]["reported"] = {
                "input": fresh + cached,
                "cached_input": cached,
                "output": sum(model.get("outputTokens") or 0 for model in models),
            }
    starts, reported = [], []
    for process in processes:
        own = [messages[message_id]["first"] for message_id in process["ids"] if message_id in messages]
        if own:
            starts.append(min(own))
            reported.append(process["reported"])
    logged: list[list[dict[str, Any]]] = [[] for _ in starts]
    for message in messages.values():
        if starts:
            logged[max(bisect_right(starts, message["first"]) - 1, 0)].append(message)
    for index, process_reported in enumerate(reported):
        if process_reported is None:
            continue
        missing = {quantity: process_reported[quantity] - sum(message["counts"][quantity] for message in logged[index]) for quantity in QUANTITIES}
        end = starts[index + 1] if index + 1 < len(starts) else float("inf")
        at = [time for time in compactions if starts[index] <= time < end] or [message["first"] for message in logged[index]]
        for position, time in enumerate(at):
            parts = {}
            for quantity in QUANTITIES:
                # Whole tokens that add up to the difference: the first `remainder` parts get one more.
                each, remainder = divmod(missing[quantity], len(at))
                parts[quantity] = each + (position < remainder)
            if any(parts.values()):
                log.calls.append((time, "main", parts))
    return log


def read_codex(agent_dir: Path) -> tuple[RunLog, list[float]]:
    log, session_starts = RunLog(), []
    for path in sorted((agent_dir / "codex_sessions").rglob("*.jsonl")):
        owner = None
        for event in read_jsonl(path):
            time = iso_seconds(event["timestamp"])
            log.times.append(time)
            if event["type"] == "session_meta" and owner is None:
                # A root session's source is "exec"; a sub-agent thread's says who started it.
                owner = "subagents" if isinstance(event["payload"]["source"], dict) else "main"
                if owner == "main":
                    session_starts.append(time)
            elif event["type"] == "token_usage_record":
                usage = event["payload"]["usage"]
                log.calls.append((time, owner, {
                    "input": usage["input_tokens"],
                    "cached_input": usage["cached_input_tokens"],
                    "output": usage["output_tokens"],
                    REASONING: usage["reasoning_output_tokens"],
                }))
    return log, session_starts


def read_muse(agent_dir: Path) -> tuple[RunLog, list[float]]:
    log, session_starts = RunLog(), []
    owners = {"main_root": "main", "workflow_child": "subagents"}
    for path in sorted((agent_dir / "muse_sessions").rglob("session.jsonl")):
        first_time = None
        for line in read_jsonl(path):
            if not line.get("recorded_at"):
                continue
            time = line["recorded_at"] / 1e6
            log.times.append(time)
            first_time = time if first_time is None else first_time
            event = (line.get("payload") or {}).get("event")
            record = event.get("record") if isinstance(event, dict) else None
            if isinstance(record, dict) and record.get("usage_family") == "provider":
                quantity = record["quantity"]
                log.calls.append((time, owners.get(record["owner"]["owner_type"], "other"), {
                    "input": quantity["input_tokens"],
                    "cached_input": quantity["cached_tokens"],
                    "output": quantity["output_tokens"],
                    REASONING: quantity["reasoning_tokens"],
                }))
        if path.parent.parent.name != "subagent" and first_time is not None:
            session_starts.append(first_time)
    return log, session_starts


def read_antigravity(agent_dir: Path) -> tuple[RunLog, list[float]]:
    log, session_starts = RunLog(), []
    main_ids = {
        event["conversation_id"]
        for event in read_jsonl(agent_dir / "agy_stdout.jsonl")
        if event.get("event") == "init"
    }
    for path in sorted((agent_dir / "agy_conversations").glob("*.jsonl")):
        owner = "main" if path.stem in main_ids else "subagents"
        first_time = None
        for step in read_jsonl(path):
            time = iso_seconds(step["created_at"])
            log.times.append(time)
            first_time = time if first_time is None else first_time
            cached = step.get("cache_read_tokens") or 0
            counts = {"input": (step.get("input_tokens") or 0) + cached, "cached_input": cached, "output": step.get("output_tokens") or 0}
            if any(counts.values()):
                log.calls.append((time, owner, counts))
        if owner == "main" and first_time is not None:
            session_starts.append(first_time)
    return log, session_starts


if __name__ == "__main__":
    main()
