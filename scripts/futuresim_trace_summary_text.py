#!/usr/bin/env python3
"""Day titles and segment labels for the trace viewer, written by a language model.

The rule-based summaries name a day by its counts ("12 forecast updates") and a segment by its
kind of tool call ("Research and forecast updates"). This script gives a model what it needs to
name them by subject instead, and puts what the model writes into the summary files.

  futuresim_trace_summary_text.py digest --data-dir futuresim/traces/data/q3 --market-csv <run>/market.csv --out <folder>
      Writes text files of about --days-per-file days of one run each. For a day they give its
      counts and, for each segment, who acted, the searches run, the questions forecast, the other
      work done and what the agent said.

  futuresim_trace_summary_text.py apply --data-dir futuresim/traces/data/q3 --text <folder> [--keep <folder>]
      Reads <agent_slug>__<run_id>*.jsonl from the folder. Each line is one day:
          {"date": "2026-08-03", "title": "...", "labels": ["...", "..."]}
      with one label per segment, in order. The label of a sub-agent's segment is written without
      the sub-agent's name, which is put in front of it here. A run is only written if every day
      of it is there and fits its segments; otherwise it keeps its rule-based text. Other keys on
      a line are ignored. The day's display_summary, which the viewer does not show, is left as
      the rules wrote it.
      --keep writes the text back out as one file per run, with each segment's range of trace
      entries added as "events". A later apply from those files refuses a run whose segments
      have moved, so text is never put on a trace it was not written for.

The 2026 Q3 text is kept in scripts/futuresim_q3_summary_text/ and applied by
build_futuresim_q3_trace_data.sh.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_futuresim_trace_summaries as rules  # noqa: E402

SOURCE = {
    "created_by": "scripts/futuresim_trace_summary_text.py",
    "created_for": "trace_visualization_summary_overlay",
    "text": (
        "Day titles and segment labels were written by a language model from a digest of each day. "
        "Segment ranges, counts, forecasts and the day's display_summary come from "
        "scripts/build_futuresim_trace_summaries.py."
    ),
}
MAX_CHARS = {"title": 90, "label": 90}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    digest = commands.add_parser("digest")
    digest.add_argument("--data-dir", type=Path, required=True)
    digest.add_argument("--market-csv", type=Path, required=True, help="The questions' titles.")
    digest.add_argument("--out", type=Path, required=True)
    digest.add_argument("--days-per-file", type=int, default=33)
    apply = commands.add_parser("apply")
    apply.add_argument("--data-dir", type=Path, required=True)
    apply.add_argument("--text", type=Path, required=True)
    apply.add_argument("--keep", type=Path)
    args = parser.parse_args()
    data = args.data_dir.resolve()
    if args.command == "digest":
        TITLES.update({qid: row["title"] for qid, row in rules.load_market_truth(args.market_csv).items() if row["title"]})
        write_digests(data, args.out, args.days_per_file)
    else:
        sys.exit(apply_text(data, args.text, args.keep))


def summary_files(data):
    index = json.loads((data / "summaries" / "index.json").read_text())
    return [data / row["path"] for row in index["runs"]]


# ---------------------------------------------------------------------------------------------
# digest


def write_digests(data, out, days_per_file):
    out.mkdir(parents=True, exist_ok=True)
    for path in summary_files(data):
        summary = json.loads(path.read_text())
        run = summary["run"]
        days = summary["days"]
        parts = [days[i:i + days_per_file] for i in range(0, len(days), days_per_file)]
        for number, part in enumerate(parts, 1):
            lines = [
                f"RUN {run['agent_name']} {run['seed_label']} ({run['harness_name'] or run['harness']}), "
                f"days {part[0]['date']} to {part[-1]['date']} of {len(days)} days starting {days[0]['date']}",
                "",
            ]
            for day in part:
                lines.extend(day_digest(data, day, first=day is days[0]))
            target = out / f"{path.stem}.part{number}.txt"
            target.write_text("\n".join(lines) + "\n")
            segments = sum(len(day["segments"]) for day in part)
            print(f"{target.name}: {len(part)} days, {segments} segments, {target.stat().st_size:,} bytes")


def day_digest(data, day, first):
    trace = rules.read_trace(data / day["trace_path"])
    events = [event for event in trace.get("events", []) if rules.should_show_event(event)]
    stats = day["stats"]
    searches = sum(count_of(segment, "news searches") for segment in day["segments"])
    # A submission to an id that is not in the market counts as a forecast but not as a question.
    stray = stats.get("unscored_update_count", 0)
    head = [
        f"{stats.get('forecast_count', 0)} forecasts on {stats.get('benchmark_update_count', 0)} questions"
        + (f" and {stray} ids that are not in the market" if stray else ""),
        f"{searches} searches",
        f"{stats.get('tool_call_count', 0)} tool calls",
        f"{len(day['segments'])} segments",
    ]
    if first:
        head.append("first day of the run")
    lines = [f"=== {day['date']} | " + " | ".join(head)]
    for segment in day["segments"]:
        chunk = [event for event in events if segment["event_idx_start"] <= event["idx"] <= segment["event_idx_end"]]
        lines.extend(segment_digest(segment, chunk))
    lines.append("")
    return lines


def count_of(segment, what):
    for fact in segment.get("notable_facts", []):
        if fact.endswith(what):
            return int(fact.split()[0])
    return 0


def segment_digest(segment, events):
    who = f'sub-agent "{segment["subagent"]}"' if segment.get("subagent") else "main agent"
    facts = ", ".join(segment.get("notable_facts", [])) or "no searches or forecasts"
    lines = [f"[{segment['id'][-3:]}] {who} | {segment['action_count']} entries | {facts}"]

    queries, work, commands = [], Counter(), 0
    for event in events:
        for block in rules.tool_blocks(event):
            kind = rules.tool_kind(block.get("name"))
            data = block.get("input") if isinstance(block.get("input"), dict) else {}
            if kind == "search_news":
                queries.append(one_line(data.get("query"), 90))
            elif kind not in {"submit_forecasts", "next_day"}:
                note = call_note(block.get("name"), data)
                work[note] += 1
                commands += not note
    queries = list(dict.fromkeys(query for query in queries if query))
    if queries:
        lines.append("  searches: " + " | ".join(spread(queries, 6)) + more(queries, 6))

    forecasts = list(segment_forecasts(events))
    if forecasts:
        lines.append("  forecasts: " + " | ".join(spread(forecasts, 6)) + more(forecasts, 6))

    notes = [note for note in work if note]
    if notes or commands:
        shell = [f"{commands} shell commands"] if commands else []
        lines.append("  other work: " + " | ".join(spread(notes, 4) + shell) + more(notes, 4))

    said = [one_line(text, 240) for text in segment.get("model_messages", [])]
    said = [text for text in said if text]
    for text in dict.fromkeys(said[:1] + said[-1:]):
        lines.append(f"  says: {text}")
    return lines


def segment_forecasts(events):
    """'Question title (Leading outcome 0.43 -> 0.62)' for each forecast the segment submits."""
    for example in rules.forecast_examples(events, TITLES):
        outcomes = example["outcomes"]
        if not outcomes:
            continue
        top = max(outcomes, key=outcomes.get)
        before = example.get("previous_outcomes", {}).get(top)
        move = f"{before:.2f} -> {outcomes[top]:.2f}" if before is not None else f"{outcomes[top]:.2f}"
        yield f"{one_line(example['question_title'], 100)} ({one_line(top, 40)} {move})"


def call_note(name, data):
    """A few words on a tool call that is neither a search nor a forecast, or '' for a bare shell command."""
    tool = rules.pretty_tool_name(name)
    if isinstance(data.get("files"), list):
        paths = [Path(str(item.get("path", ""))).name for item in data["files"] if isinstance(item, dict)]
        return f"{tool}: {', '.join(paths[:3])}"
    for key in ("description", "file_path", "path", "name", "agent_type", "target"):
        value = data.get(key)
        if isinstance(value, str) and value.strip():
            text = Path(value).name if key in {"file_path", "path"} else value
            return f"{tool}: {one_line(text, 80)}"
    return "" if "command" in data else tool


def one_line(text, limit):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def spread(items, count):
    """Up to `count` of the items, taken evenly from first to last."""
    if len(items) <= count:
        return items
    return [items[round(i * (len(items) - 1) / (count - 1))] for i in range(count)]


def more(items, count):
    return f" (+{len(items) - count} more)" if len(items) > count else ""


# Question titles by id, from the market file.
TITLES = {}


# ---------------------------------------------------------------------------------------------
# apply


def apply_text(data, text_dir, keep_dir=None):
    failed = 0
    if keep_dir:
        keep_dir.mkdir(parents=True, exist_ok=True)
    for path in summary_files(data):
        summary = json.loads(path.read_text())
        written = {}
        problems = []
        for source in sorted(text_dir.glob(f"{path.stem}*.jsonl")):
            for number, line in enumerate(source.read_text().splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as error:
                    problems.append(f"{source.name}:{number}: not JSON ({error})")
                    continue
                if row.get("date") in written:
                    problems.append(f"{source.name}:{number}: {row.get('date')} is there twice")
                written[row.get("date")] = row
        for day in summary["days"]:
            problems.extend(day_problems(day, written.get(day["date"])))
        if problems:
            failed += 1
            print(f"NOT WRITTEN {path.name}: {len(problems)} problems")
            for problem in problems[:12]:
                print("   ", problem)
            continue
        for day in summary["days"]:
            row = written[day["date"]]
            day["title"] = clean(row["title"])
            for segment, label in zip(day["segments"], row["labels"]):
                label = clean(label)
                segment["label"] = f"Sub-agent {segment['subagent']}: {label}" if segment.get("subagent") else label[0].upper() + label[1:]
        summary["source"] = SOURCE
        path.write_text(json.dumps(summary, indent=2) + "\n")
        print(f"written {path.name}: {len(summary['days'])} days")
        if keep_dir:
            lines = [
                json.dumps({
                    "date": day["date"],
                    "title": clean(written[day["date"]]["title"]),
                    "labels": [clean(label) for label in written[day["date"]]["labels"]],
                    "events": segment_ranges(day),
                }, ensure_ascii=False)
                for day in summary["days"]
            ]
            (keep_dir / f"{path.stem}.jsonl").write_text("\n".join(lines) + "\n")
    return 1 if failed else 0


def day_problems(day, row):
    date = day["date"]
    if row is None:
        return [f"{date}: no line for this day"]
    problems = text_problems(f"{date} title", row.get("title"), MAX_CHARS["title"])
    labels = row.get("labels")
    if not isinstance(labels, list) or len(labels) != len(day["segments"]):
        count = len(labels) if isinstance(labels, list) else "no"
        return problems + [f"{date}: {count} labels for {len(day['segments'])} segments"]
    if "events" in row and row["events"] != segment_ranges(day):
        return problems + [f"{date}: the segments have moved since the text was written"]
    for segment, label in zip(day["segments"], labels):
        problems.extend(text_problems(segment["id"], label, MAX_CHARS["label"]))
        if isinstance(label, str) and re.match(r"sub-?agent\b", label.strip(), re.I):
            problems.append(f"{segment['id']}: the label names the sub-agent itself: {label!r}")
    return problems


def segment_ranges(day):
    return [[segment["event_idx_start"], segment["event_idx_end"]] for segment in day["segments"]]


def text_problems(where, text, limit):
    if not isinstance(text, str) or not text.strip():
        return [f"{where}: missing"]
    if len(clean(text)) > limit:
        return [f"{where}: {len(clean(text))} characters, the limit is {limit}"]
    return []


def clean(text):
    return re.sub(r"\s+", " ", text).strip()


if __name__ == "__main__":
    main()
