#!/usr/bin/env python3
import argparse
import csv
import json
import os
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "futuresim/traces/data"
SUMMARY_DIR = DATA / "summaries"
DEFAULT_MARKET_CSV = Path("/fast/sgoel/forecasting/current_sim/official_runs_complete/gpt-5.5/26-06-01-14-27-01/market.csv")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    manifest = json.loads((DATA / "manifest.json").read_text())
    market = load_market_truth()
    SUMMARY_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    for run in manifest["runs"]:
        out = SUMMARY_DIR / f"{run['agent_slug']}__{run['run_id']}.json"
        if out.exists() and not args.overwrite and not created_by_this_script(out):
            written.append((run, out, "existing"))
            continue
        summary = summarize_run(run)
        out.write_text(json.dumps(summary, indent=2) + "\n")
        written.append((run, out, "written"))

    postprocess_summary_files(manifest, market)
    index = {
        "runs": [
            {"agent_slug": run["agent_slug"], "run_id": run["run_id"], "path": f"summaries/{run['agent_slug']}__{run['run_id']}.json"}
            for run in manifest["runs"]
            if (SUMMARY_DIR / f"{run['agent_slug']}__{run['run_id']}.json").exists()
        ]
    }
    (SUMMARY_DIR / "index.json").write_text(json.dumps(index, indent=2) + "\n")
    for run, out, status in written:
        print(status, run["agent_slug"], run["seed_label"], out.relative_to(ROOT))


def summarize_run(run):
    title_by_qid = build_question_title_index(run)
    metric_stats = run_metric_stats(run)
    days = []
    for day_meta in sorted(run.get("days", []), key=lambda row: row["date"]):
        trace = json.loads((DATA / day_meta["path"]).read_text())
        if len(title_by_qid) < 250:
            add_titles(title_by_qid, trace_text(trace))
        visible = [event for event in trace.get("events", []) if should_show_event(event)]
        segments = [summarize_segment(day_meta["date"], i, chunk, title_by_qid) for i, chunk in enumerate(segment_events(visible), 1)]
        stats = {
            "event_count_in_shard": len(trace.get("events", [])),
            "action_count": len(visible),
            "tool_call_count": day_meta.get("tool_call_count", 0),
            "forecast_count": day_meta.get("forecast_count", 0),
            **metric_stats.get(day_meta["date"], {}),
            "truncated": bool(trace.get("truncated")),
        }
        days.append({
            "date": day_meta["date"],
            "trace_path": day_meta["path"],
            "title": day_title(run, day_meta, stats, segments),
            "display_summary": day_summary(run, stats, segments),
            "stats": stats,
            "segments": segments,
        })

    return {
        "schema": "futuresim.trace_summary.v1",
        "source": {
            "created_by": "scripts/build_futuresim_trace_summaries.py",
            "created_for": "trace_visualization_summary_overlay",
        },
        "status": "complete",
        "run": {key: run.get(key, "") for key in ["agent_name", "agent_slug", "model", "harness", "harness_name", "seed_label", "run_id", "run_label", "source_filename"]},
        "linking_contract": {
            "day_trace_path": "days[].trace_path is relative to trace_data_base",
            "segment_event_range": "segments[].event_idx_start and segments[].event_idx_end refer to day.events[].idx in the trace shard",
            "segment_grouping": "Segments are consecutive visible action sequences, split around day transitions and roughly 60 visible actions.",
            "ui_behavior": "The visualizer renders each segment summary first, then expands all trace events whose idx is within the segment range.",
        },
        "days": days,
    }


def should_show_event(event):
    if event.get("kind") == "tool_result":
        return False
    blocks = event.get("blocks", [])
    if event.get("kind") == "user" and blocks and all(block.get("type") == "tool_result" for block in blocks):
        return False
    return bool(event.get("preview") or any(
        block.get("type") == "tool_use"
        or block.get("type") == "compaction"
        or (block.get("type") == "text" and str(block.get("text") or "").strip())
        for block in blocks
    ))


def segment_events(events, target=55):
    chunk = []
    for event in events:
        chunk.append(event)
        if len(chunk) >= target or any(is_next_day_tool(block.get("name")) for block in tool_blocks(event)):
            yield chunk
            chunk = []
    if chunk:
        yield chunk


def summarize_segment(date, index, events, title_by_qid):
    tool_names = [block.get("name") or "tool" for event in events for block in tool_blocks(event)]
    counts = Counter(tool_kind(name) for name in tool_names)
    forecasts = forecast_examples(events, title_by_qid)
    label = segment_label(counts, forecasts, events)
    facts = []
    for name, label_text in [("search_news", "news searches"), ("submit_forecasts", "forecast submissions"), ("next_day", "day advance calls"), ("compaction", "context compactions")]:
        if counts.get(name):
            facts.append(f"{counts[name]} {label_text}")

    return {
        "id": f"{date}-s{index:02d}",
        "event_idx_start": events[0]["idx"],
        "event_idx_end": events[-1]["idx"],
        "label": label,
        "summary": segment_summary(counts, forecasts, events),
        "action_count": len(events),
        "tools": unique_pretty_tools(tool_names, events),
        "notable_facts": facts,
        "representative_event_idxs": representative_idxs(events),
        **({"question_scope": {"count": counts["submit_forecasts"], "mode": "forecast submissions"}} if counts.get("submit_forecasts") else {}),
        **({"representative_forecasts": forecasts[:5]} if forecasts else {}),
    }


def segment_label(counts, forecasts, events):
    if counts.get("submit_forecasts") and counts.get("search_news"):
        return "Research and forecast updates"
    if counts.get("submit_forecasts"):
        return "Forecast submissions"
    if counts.get("search_news"):
        return "News research"
    if counts.get("next_day"):
        return "Save state and advance day"
    if counts.get("compaction"):
        return "Context compaction"
    if any(tool_blocks(event) for event in events):
        return "Workspace and tool work"
    return "Agent reasoning"


def segment_summary(counts, forecasts, events):
    parts = []
    if counts.get("submit_forecasts"):
        parts.append(f"Submitted {counts['submit_forecasts']} forecast update(s)")
    if counts.get("search_news"):
        parts.append(f"ran {counts['search_news']} news search(es)")
    workspace = sum(counts[name] for name in counts if name not in {"submit_forecasts", "search_news", "next_day", "compaction"})
    if workspace:
        parts.append(f"used {workspace} workspace/tool action(s)")
    if counts.get("next_day"):
        parts.append("advanced the simulation day")
    if counts.get("compaction"):
        parts.append(f"recorded {counts['compaction']} context compaction event(s)")
    if not parts:
        text_events = sum(1 for event in events if any(block.get("type") == "text" for block in event.get("blocks", [])))
        parts.append(f"Recorded {text_events or len(events)} agent reasoning/action event(s)")
    summary = "; ".join(parts)
    if forecasts:
        summary += ". Representative forecasts are listed below."
    return sentence(summary)


def day_title(run, day_meta, stats, segments):
    if stats["forecast_count"]:
        return f"{day_meta['date']}: {stats['forecast_count']} forecast updates"
    if stats["action_count"]:
        return f"{day_meta['date']}: {stats['action_count']} visible actions"
    return f"{day_meta['date']}: No recorded actions"


def day_summary(run, stats, segments):
    if not stats["action_count"]:
        return "The trace shard contains no visible actions for this simulation day."
    bits = []
    if stats["forecast_count"]:
        bits.append(f"{run['agent_name']} submitted {stats['forecast_count']} forecast update(s)")
    tool_counts = Counter()
    for segment in segments:
        for fact in segment.get("notable_facts", []):
            if "news searches" in fact:
                tool_counts["search"] += int(fact.split()[0])
    if tool_counts["search"]:
        bits.append(f"Ran {tool_counts['search']} news search(es)")
    if not bits:
        bits.append(f"{run['agent_name']} recorded {stats['action_count']} visible action(s)")
    return sentence(". ".join(bits))


def postprocess_summary_files(manifest, market):
    for run in manifest["runs"]:
        path = SUMMARY_DIR / f"{run['agent_slug']}__{run['run_id']}.json"
        if not path.exists():
            continue
        payload = json.loads(path.read_text())
        metric_stats = run_metric_stats(run)
        update_stats = run_update_stats(run, market)
        changed = False
        for day in payload.get("days", []):
            cleaned = clean_transition_phrase(day.get("display_summary", ""))
            if cleaned != day.get("display_summary", ""):
                day["display_summary"] = cleaned
                changed = True
            stats = day.setdefault("stats", {})
            before = dict(stats)
            stats.update(metric_stats.get(day.get("date"), {}))
            stats.update(update_stats.get(day.get("date"), {}))
            changed = changed or stats != before
        if changed:
            path.write_text(json.dumps(payload, indent=2) + "\n")


def run_metric_stats(run):
    metric_by_date = {row["date"]: row for row in run.get("metrics", [])}
    stats_by_date = {}
    previous = None
    for day_meta in sorted(run.get("days", []), key=lambda row: row["date"]):
        metric = metric_by_date.get(day_meta["date"], {})
        brier = number_or_none(metric.get("brier_skill_score"))
        top1 = number_or_none(metric.get("top1_accuracy"))
        stats_by_date[day_meta["date"]] = {
            "brier_skill_score": brier,
            "top1_accuracy_percent": top1,
            "brier_skill_score_delta": metric_delta(brier, previous["brier"]) if previous else None,
            "top1_accuracy_delta": metric_delta(top1, previous["top1"]) if previous else None,
        }
        previous = {"brier": brier, "top1": top1}
    return stats_by_date


def metric_delta(current, previous):
    if current is None or previous is None:
        return None
    return round(current - previous, 6)


def number_or_none(value):
    return float(value) if is_number(value) else None


def clean_transition_phrase(text):
    text = re.sub(r"\s*The trace includes a next-day transition\.?", "", str(text or "")).strip()
    text = re.sub(r"\s{2,}", " ", text)
    return text


def load_market_truth():
    candidates = []
    if os.environ.get("FSIM_MARKET_CSV"):
        candidates.append(Path(os.environ["FSIM_MARKET_CSV"]))
    candidates.extend([DATA / "market.csv", DEFAULT_MARKET_CSV])

    for path in candidates:
        if not path.exists():
            continue
        with path.open(encoding="utf-8") as handle:
            return {
                canonical_qid(row.get("qid")): {
                    "title": row.get("title", ""),
                    "ground_truth": str(row.get("ground_truth") or "").strip(),
                }
                for row in csv.DictReader(handle)
                if canonical_qid(row.get("qid"))
            }
    return {}


def run_update_stats(run, market):
    last_predictions = {}
    stats_by_date = {}
    for day_meta in sorted(run.get("days", []), key=lambda row: row["date"]):
        trace = json.loads((DATA / day_meta["path"]).read_text())
        today = final_day_predictions(trace)
        scored = []
        unscored = 0
        for qid, outcomes in today.items():
            truth = market.get(qid, {}).get("ground_truth", "")
            if not truth:
                unscored += 1
                continue
            before = last_predictions.get(qid)
            scored.append({
                "brier_before": brier_skill(before, truth),
                "brier_after": brier_skill(outcomes, truth),
                "top1_before": top1_correct(before, truth),
                "top1_after": top1_correct(outcomes, truth),
            })
        last_predictions.update(today)
        stats_by_date[day_meta["date"]] = summarize_update_scores(today, scored, unscored)
    return stats_by_date


def summarize_update_scores(today, scored, unscored):
    out = {
        "updated_question_count": len(today),
        "benchmark_update_count": len(scored),
        "unscored_update_count": unscored,
        "brier_update_delta": None,
        "top1_update_delta": None,
    }
    if not scored:
        return out

    brier_before = mean(item["brier_before"] for item in scored)
    brier_after = mean(item["brier_after"] for item in scored)
    top1_before = mean(item["top1_before"] for item in scored)
    top1_after = mean(item["top1_after"] for item in scored)
    out.update({
        "brier_update_before": round(brier_before, 6),
        "brier_update_after": round(brier_after, 6),
        "brier_update_delta": round(brier_after - brier_before, 6),
        "top1_update_before_percent": round(top1_before * 100.0, 6),
        "top1_update_after_percent": round(top1_after * 100.0, 6),
        "top1_update_delta": round((top1_after - top1_before) * 100.0, 6),
    })
    return out


def final_day_predictions(trace):
    predictions = {}
    for event in trace.get("events", []):
        for block in tool_blocks(event):
            if tool_kind(block.get("name")) != "submit_forecasts":
                continue
            input_data = block.get("input") if isinstance(block.get("input"), dict) else {}
            qid = canonical_qid(input_data.get("question_id") or input_data.get("qid"))
            outcomes = clean_outcomes(input_data.get("outcomes"))
            if qid and outcomes:
                predictions[qid] = outcomes
    return predictions


def clean_outcomes(outcomes):
    if not isinstance(outcomes, dict):
        return {}
    cleaned = {}
    for name, value in outcomes.items():
        if is_number(value):
            cleaned[str(name)] = float(value)
    return cleaned


def canonical_qid(value):
    qid = str(value or "").strip()
    if re.fullmatch(r"[qQ]\d+", qid):
        return qid[1:]
    return qid


def brier_skill(outcomes, truth):
    if not outcomes or not truth:
        return 0.0
    matched = None
    truth_norm = normalize_outcome(truth)
    for outcome in outcomes:
        if outcome == truth or normalize_outcome(outcome) == truth_norm:
            matched = outcome
            break

    brier = 0.0
    for outcome, prob in outcomes.items():
        target = 1.0 if outcome == matched else 0.0
        brier += (prob - target) ** 2
    if matched is None:
        brier += 1.0
    return 1.0 - brier


def top1_correct(outcomes, truth):
    if not outcomes or not truth:
        return 0.0
    best = max(outcomes.items(), key=lambda item: item[1])[0]
    return 1.0 if normalize_outcome(best) == normalize_outcome(truth) else 0.0


def normalize_outcome(value):
    return str(value or "").lower().replace(" ", "").strip()


def mean(values):
    items = list(values)
    return sum(items) / len(items) if items else 0.0


def forecast_examples(events, title_by_qid):
    examples = []
    for event in events:
        for block in tool_blocks(event):
            if tool_kind(block.get("name")) != "submit_forecasts":
                continue
            input_data = block.get("input") if isinstance(block.get("input"), dict) else {}
            qid = str(input_data.get("question_id") or input_data.get("qid") or "")
            outcomes = input_data.get("outcomes") if isinstance(input_data.get("outcomes"), dict) else {}
            top = sorted(((str(k), float(v)) for k, v in outcomes.items() if is_number(v)), key=lambda item: item[1], reverse=True)[:2]
            examples.append({
                "question_id": qid,
                "question_title": title_by_qid.get(qid, f"Question {qid}" if qid else "Forecast question"),
                "event_idx": event["idx"],
                "summary": "Top outcomes: " + ", ".join(f"{name} {value:.2f}" for name, value in top) + "." if top else "Forecast submitted.",
            })
    return examples


def build_question_title_index(run):
    index = {}
    workspace = DATA / "workspaces" / run["agent_slug"] / run["run_id"] / "files"
    if workspace.exists():
        for path in workspace.rglob("*"):
            if path.is_file() and path.suffix.lower() in {".txt", ".md", ".json", ".csv"} and path.stat().st_size < 2_000_000:
                add_titles(index, path.read_text(errors="ignore"))
    return index


def trace_text(trace):
    chunks = []
    for event in trace.get("events", []):
        if event.get("preview"):
            chunks.append(str(event["preview"]))
        for block in event.get("blocks", []):
            for key in ["text", "content", "output", "result"]:
                value = block.get(key)
                if isinstance(value, str):
                    chunks.append(value)
                elif value is not None:
                    chunks.append(json.dumps(value)[:20000])
    return "\n".join(chunks)


def add_titles(index, text):
    patterns = [
        re.compile(r"^\s*\[?(\d{5,})\]?\s*(?:\([^)]*\))?\s*[-|:]\s*(.{20,240})$", re.M),
        re.compile(r"^\s*Q(?:uestion)?\s+(\d{5,})\s*[:|-]?\s*(.{20,240})$", re.M | re.I),
        re.compile(r"^\s*(\d{3,})\s+(\d{5,})\s*\|\s*(.{20,240})$", re.M),
        re.compile(r"^\s*(\d{5,})\s*\|\s*(.{20,240})$", re.M),
        re.compile(r'"qid"\s*:\s*"(\d{5,})".{0,500}?"title"\s*:\s*"([^"]{20,240})"', re.S),
        re.compile(r'"title"\s*:\s*"([^"]{20,240})".{0,500}?"qid"\s*:\s*"(\d{5,})"', re.S),
    ]
    for pattern in patterns[:2]:
        for qid, title in pattern.findall(text):
            clean = clean_title(title)
            if clean:
                index.setdefault(qid, clean)
    for _, qid, title in patterns[2].findall(text):
        clean = clean_title(title)
        if clean:
            index.setdefault(qid, clean)
    for qid, title in patterns[3].findall(text):
        clean = clean_title(title)
        if clean:
            index.setdefault(qid, clean)
    for match in patterns[4].findall(text):
        qid, title = match
        clean = clean_title(title)
        if clean:
            index.setdefault(qid, clean)
    for title, qid in patterns[5].findall(text):
        clean = clean_title(title)
        if clean:
            index.setdefault(qid, clean)


def clean_title(title):
    title = re.sub(r"\\s+", " ", str(title)).strip().strip(",")
    if len(title) > 220:
        title = title[:217] + "..."
    return title if len(title) >= 12 else ""


def tool_blocks(event):
    return [block for block in event.get("blocks", []) if block.get("type") == "tool_use"]


def unique_pretty_tools(tool_names, events):
    names = [pretty_tool_name(name) for name in tool_names]
    if any(any(block.get("type") == "compaction" for block in event.get("blocks", [])) for event in events):
        names.append("Context Compaction")
    return list(dict.fromkeys(names))[:8]


def representative_idxs(events):
    picks = [events[0]["idx"], events[len(events) // 2]["idx"], events[-1]["idx"]]
    return list(dict.fromkeys(picks))


def tool_kind(name):
    value = str(name or "")
    lower = value.lower()
    if "submit_forecasts" in lower:
        return "submit_forecasts"
    if "search_news" in lower:
        return "search_news"
    if "next_day" in lower:
        return "next_day"
    return value or "tool"


def is_next_day_tool(name):
    return tool_kind(name) == "next_day"


def pretty_tool_name(name):
    value = str(name or "tool")
    value = re.sub(r"^mcp__forecast__", "", value)
    value = value.replace("_", " ")
    return " ".join(word[:1].upper() + word[1:] for word in value.split())


def is_number(value):
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def sentence(text):
    text = str(text).strip()
    if not text:
        return ""
    text = text[0].upper() + text[1:]
    return text if text.endswith((".", "!", "?")) else text + "."


def created_by_this_script(path):
    try:
        return json.loads(path.read_text()).get("source", {}).get("created_by") == "scripts/build_futuresim_trace_summaries.py"
    except Exception:
        return False


if __name__ == "__main__":
    main()
