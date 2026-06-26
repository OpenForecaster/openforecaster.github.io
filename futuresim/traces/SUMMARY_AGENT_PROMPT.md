# FutureSim Trace Summary Worker Prompt

You are summarizing one official FutureSim run for the trace visualizer.

## Repository Context

- Work in `/lustre/home/sgoel/forecast-sim/openforecaster.github.io`.
- Trace manifest: `futuresim/traces/data/manifest.json`.
- Trace shards are relative to `futuresim/traces/data/`, for example `runs/<agent_slug>/<run_id>/<date>.json`.
- Summary output directory: `futuresim/traces/data/summaries/`.
- The visualizer loads one run-level sidecar at `summaries/<agent_slug>__<run_id>.json`.
- Only edit your assigned output file. Do not modify viewer code, raw shards, manifests, workspace exports, or another worker's summary file.

## Assigned Output

Create or update exactly one file:

```text
futuresim/traces/data/summaries/<agent_slug>__<run_id>.json
```

The file must summarize every day in the assigned run, in chronological order. Each day is one object inside the run-level file.

## Product Decision

The summary file owns the meaningful grouping. The UI should not split giant action dumps with arbitrary batches.

Each day must contain short, logical, consecutive action segments. A segment is one collapsible event row. Opening it reveals the existing raw trace visualization for the exact event-index range in that segment.

Do not club hundreds of actions together. Day 0 often contains an initial all-market forecast dump; split it by market order, resolution window, topic cluster, checkpoint, or another human-readable boundary. For forecast submission runs, prefer 25-60 visible actions per segment and avoid segments above 80 visible actions unless genuinely unavoidable.

## Linking Contract

- `segments[].event_idx_start` and `segments[].event_idx_end` refer to raw `day.events[].idx` values, not array offsets.
- Segment ranges must be chronological, consecutive action sequences.
- Ranges may include hidden `tool_result` events; the UI filters those.
- `representative_event_idxs` must point to important visible events inside the segment range.
- `representative_forecasts[].event_idx`, when present, must point to a forecast submission event.

## Required JSON Shape

Use strict JSON:

```json
{
  "schema": "futuresim.trace_summary.v1",
  "source": {
    "created_by": "codex-subagent",
    "created_for": "trace_visualization_summary_overlay"
  },
  "status": "complete",
  "run": {
    "agent_name": "",
    "agent_slug": "",
    "model": "",
    "harness": "",
    "harness_name": "",
    "seed_label": "",
    "run_id": "",
    "run_label": "",
    "source_filename": ""
  },
  "linking_contract": {
    "day_trace_path": "days[].trace_path is relative to trace_data_base",
    "segment_event_range": "segments[].event_idx_start and segments[].event_idx_end refer to day.events[].idx in the trace shard",
    "segment_grouping": "Segments are short logical, consecutive action sequences. Large forecast dumps should be split by market order, resolution window, topic cluster, checkpoint, or another human-readable boundary instead of represented as one large segment.",
    "ui_behavior": "A visualizer can render each segment summary at the top of the day, then expand/highlight all trace events whose idx is within the segment range."
  },
  "days": []
}
```

Each day object:

```json
{
  "date": "YYYY-MM-DD",
  "trace_path": "runs/<agent_slug>/<run_id>/<date>.json",
  "title": "Short day title.",
  "display_summary": "One to three sentences summarizing what the agent did that day.",
  "stats": {
    "event_count_in_shard": 0,
    "action_count": 0,
    "tool_call_count": 0,
    "forecast_count": 0,
    "brier_skill_score": null,
    "top1_accuracy_percent": null,
    "truncated": false
  },
  "segments": []
}
```

Each segment object:

```json
{
  "id": "YYYY-MM-DD-s01",
  "event_idx_start": 0,
  "event_idx_end": 0,
  "label": "Short segment label",
  "summary": "One or two sentences describing the consecutive action sequence.",
  "action_count": 0,
  "tools": ["exec_command"],
  "notable_facts": [],
  "representative_event_idxs": []
}
```

Optional segment fields:

- `question_scope` for forecast blocks, with fields such as `count`, `mode`, and `topic`.
- `representative_forecasts` for forecast-heavy segments, with 3-5 useful examples:

```json
{
  "question_id": "123456",
  "question_title": "Human-readable market question title when recoverable.",
  "event_idx": 42,
  "summary": "Question topic: top outcome 0.35, second outcome 0.15."
}
```

## Summarization Rules

1. Read run metadata from `manifest.json` and each raw day shard.
2. Identify visible actions: assistant reasoning, relevant user instructions, tool calls, compactions, forecast submissions, next-day calls, and workspace/memory updates. Ignore standalone tool-result events except as evidence for the preceding tool call.
3. Walk each day chronologically and create short consecutive segments.
4. For each segment, capture what the agent did, why it mattered, and which tools or forecast submissions were involved.
5. For search/news segments, summarize the search topics and facts used.
6. For bash/workspace segments, summarize inspected files, market scans, memory writes, and scripts run.
7. For forecast segments, summarize the question cluster and include representative forecasts rather than listing every submission.
   For each representative forecast, include `question_title` when it is recoverable from market scans, workspace question files, or trace output. Do not use a bare qid as the only human-facing label when a title is available.
8. For day-advance and handoff segments, state the memory/workspace changes and next-day transition.
9. Write the day-level `title` and `display_summary` after segmenting the day.

## Quality Rules

- Summarize the agent's observed actions and beliefs, not external truth.
- Do not invent evidence, outcomes, or question text not present in trace/tool/workspace data.
- Use absolute simulation dates.
- Keep summaries factual and concise.
- Preserve uncertainty when the trace was uncertain.
- Keep segment labels specific; avoid generic repeated labels when the trace gives enough context.
- Make forecast segment topics match the actual representative forecasts.
- Use ASCII punctuation.

## Validation

Run:

```bash
jq empty futuresim/traces/data/summaries/<agent_slug>__<run_id>.json
```

Also check that every segment range maps to visible raw actions and that `action_count` matches those visible actions. Report:

- output file path
- days summarized
- max segment action count
- any segment above 80 visible actions and why
- validation result

## Coordination

- You are not alone in the codebase.
- Only edit your assigned output file.
- Do not revert or reformat unrelated files.
- Do not spawn subagents.
