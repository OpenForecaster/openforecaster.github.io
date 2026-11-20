#!/usr/bin/env python3
"""Add each run's token totals to a trace viewer manifest.

    python3 scripts/build_futuresim_token_usage.py --data-dir futuresim/traces/data/q3 --runs-root <runs>

A run in <data-dir>/manifest.json whose folder (its `source_run`) is under --runs-root gets

    "tokens": {"main": {...}, "subagents": {...}, "other": {...}}

Each of the three holds `input`, `cached_input` and `output`:

* `input` is every token sent to the model, summed over its calls. An agent sends its whole
  context with each call, so the same text is counted many times and most of it is cached.
* `cached_input` is the part of `input` that the provider read from its prompt cache.
* `output` is every token the model generated, reasoning included.

"main" is the run's own agent, "subagents" the agents it started, and "other" the model calls the
harness made by itself (Muse's reminder sessions).

The numbers are read from each harness's session logs, the way analysis/src/q3_v8_output_tokens.py
in the simulator's repository counts output tokens, so the output totals here are the ones behind
its figure. stdout is not enough: Codex's reports usage for the first turn only, and Claude Code's
carries the output count from the start of a message, not from its end.

* Claude Code, `claude_config/projects/**/*.jsonl` (the main session and `subagents/`). A message
  is logged once per content block and each copy repeats its usage, so it is counted once per
  message id. A Claude Code process that ended normally also reports its own total (the
  `modelUsage` of a `result` line in stdout). That total covers the context-compaction calls,
  which the transcripts leave out, so it is used in place of the sum of the process's transcript
  messages, and the difference is put on the main agent. A process that was stopped reports
  nothing, and its compaction calls are not counted. Input is `input_tokens` +
  `cache_creation_input_tokens` + `cache_read_input_tokens`.
* Codex, `codex_sessions/**/*.jsonl`, one rollout per thread: the `token_usage_record` lines, which
  also cover context compaction. `input_tokens` already includes the cached ones.
* Muse, `muse_sessions/**/session.jsonl`: the usage records of the "provider" family. Besides the
  main agent and the sub-agents of its workflows, Muse runs reminder sessions of its own.
* Antigravity, `agy_conversations/*.jsonl`: the per-step counts. The main conversation is the one
  `agy_stdout.jsonl` opens and every other one is a sub-agent. Input is `input_tokens` +
  `cache_read_tokens`.

A run with none of these logs is left without the field. For a run that was restarted, the work of
the days that the restart redid is not in its folder and so is not counted.
"""

from __future__ import annotations

import argparse
import json
from bisect import bisect_right
from pathlib import Path
from typing import Any, Iterator

OWNERS = ("main", "subagents", "other")
QUANTITIES = ("input", "cached_input", "output")
Totals = dict[str, dict[str, int]]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data-dir", required=True, type=Path, help="Trace data root (holds manifest.json).")
    parser.add_argument("--runs-root", required=True, type=Path, help="Folder of runs that the manifest's source_run is under.")
    args = parser.parse_args()

    manifest_path = args.data_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    for run in manifest["runs"]:
        name = f"{run['agent_slug']} {run['seed_label']}"
        agent_dir = find_agent_dir(args.runs_root, run)
        totals = count_tokens(agent_dir) if agent_dir else None
        if totals is None:
            run.pop("tokens", None)
            print(f"{name}: no session logs, left without token totals")
            continue
        run["tokens"] = totals
        print(f"{name}: " + ", ".join(f"{q} {sum(totals[o][q] for o in OWNERS):,}" for q in QUANTITIES))
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def find_agent_dir(runs_root: Path, run: dict[str, Any]) -> Path | None:
    if not run.get("source_run"):
        return None
    agents = sorted(path for path in (runs_root / run["source_run"] / "agents").glob("*") if path.is_dir())
    return agents[0] if len(agents) == 1 else None


def count_tokens(agent_dir: Path) -> Totals | None:
    if (agent_dir / "claude_config" / "projects").is_dir():
        return claude_code_tokens(agent_dir)
    if (agent_dir / "codex_sessions").is_dir():
        return codex_tokens(agent_dir)
    if (agent_dir / "muse_sessions").is_dir():
        return muse_tokens(agent_dir)
    if (agent_dir / "agy_conversations").is_dir():
        return antigravity_tokens(agent_dir)
    return None


def empty_totals() -> Totals:
    return {owner: dict.fromkeys(QUANTITIES, 0) for owner in OWNERS}


def read_jsonl(path: Path) -> Iterator[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def claude_code_tokens(agent_dir: Path) -> Totals:
    totals = empty_totals()
    messages: dict[str, dict[str, Any]] = {}  # message id -> owner, first timestamp, counts
    for path in sorted((agent_dir / "claude_config" / "projects").rglob("*.jsonl")):
        owner = "subagents" if "subagents" in path.parts else "main"
        for event in read_jsonl(path):
            if event.get("type") != "assistant":
                continue
            usage = event["message"]["usage"]
            fresh = (usage.get("input_tokens") or 0) + (usage.get("cache_creation_input_tokens") or 0)
            cached = usage.get("cache_read_input_tokens") or 0
            counts = {"input": fresh + cached, "cached_input": cached, "output": usage.get("output_tokens") or 0}
            seen = messages.setdefault(event["message"]["id"], {"owner": owner, "first": event["timestamp"], "counts": counts})
            seen["first"] = min(seen["first"], event["timestamp"])
            seen["counts"] = {q: max(seen["counts"][q], counts[q]) for q in QUANTITIES}
    for message in messages.values():
        for quantity in QUANTITIES:
            totals[message["owner"]][quantity] += message["counts"][quantity]

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
    logged = [dict.fromkeys(QUANTITIES, 0) for _ in starts]
    for message in messages.values():
        if starts:
            process = logged[max(bisect_right(starts, message["first"]) - 1, 0)]
            for quantity in QUANTITIES:
                process[quantity] += message["counts"][quantity]
    for process_reported, process_logged in zip(reported, logged):
        if process_reported is not None:
            for quantity in QUANTITIES:
                totals["main"][quantity] += process_reported[quantity] - process_logged[quantity]
    return totals


def codex_tokens(agent_dir: Path) -> Totals:
    totals = empty_totals()
    for path in sorted((agent_dir / "codex_sessions").rglob("*.jsonl")):
        owner = None
        for event in read_jsonl(path):
            if event["type"] == "session_meta" and owner is None:
                # A root session's source is "exec"; a sub-agent thread's says who started it.
                owner = "subagents" if isinstance(event["payload"]["source"], dict) else "main"
            elif event["type"] == "token_usage_record":
                usage = event["payload"]["usage"]
                totals[owner]["input"] += usage["input_tokens"]
                totals[owner]["cached_input"] += usage["cached_input_tokens"]
                totals[owner]["output"] += usage["output_tokens"]
    return totals


def muse_tokens(agent_dir: Path) -> Totals:
    totals = empty_totals()
    owners = {"main_root": "main", "workflow_child": "subagents"}
    for path in sorted((agent_dir / "muse_sessions").rglob("session.jsonl")):
        for line in read_jsonl(path):
            event = (line.get("payload") or {}).get("event")
            record = event.get("record") if isinstance(event, dict) else None
            if isinstance(record, dict) and record.get("usage_family") == "provider":
                owner = owners.get(record["owner"]["owner_type"], "other")
                quantity = record["quantity"]
                totals[owner]["input"] += quantity["input_tokens"]
                totals[owner]["cached_input"] += quantity["cached_tokens"]
                totals[owner]["output"] += quantity["output_tokens"]
    return totals


def antigravity_tokens(agent_dir: Path) -> Totals:
    totals = empty_totals()
    main_ids = {
        event["conversation_id"]
        for event in read_jsonl(agent_dir / "agy_stdout.jsonl")
        if event.get("event") == "init"
    }
    for path in sorted((agent_dir / "agy_conversations").glob("*.jsonl")):
        owner = "main" if path.stem in main_ids else "subagents"
        for step in read_jsonl(path):
            cached = step.get("cache_read_tokens") or 0
            totals[owner]["input"] += (step.get("input_tokens") or 0) + cached
            totals[owner]["cached_input"] += cached
            totals[owner]["output"] += step.get("output_tokens") or 0
    return totals


if __name__ == "__main__":
    main()
