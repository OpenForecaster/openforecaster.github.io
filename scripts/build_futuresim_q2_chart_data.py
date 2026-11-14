#!/usr/bin/env python3
"""Build the data behind the interactive FutureSim 2026 Q2 leaderboard chart.

The numbers come from the same question-level hierarchical bootstrap that draws
the paper/website PNGs (``main_fig_plot.aggregate_by_group`` in the forecast-sim
analysis code), so the interactive chart shows the same means and +-1 std
bands as ``futuresim/figures/q2/*.png``.

Usage:
    python scripts/build_futuresim_q2_chart_data.py \
        --analysis-src /path/to/forecast-sim/analysis/src \
        --runs-dir /fast/sgoel/forecasting/current_sim/Q2results
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

DEFAULT_ANALYSIS_SRC = Path("/lustre/home/nchandak/forecast-sim/analysis/src")
DEFAULT_RUNS_DIR = Path("/fast/sgoel/forecasting/current_sim/Q2results")
DEFAULT_OUTPUT = Path("futuresim/data/q2_results.json")

START_DATE = "2026-04-01"
END_DATE = "2026-06-28"
RESOLUTION_MONTHS = {4, 5, 6}

# (bootstrap label, display name, slug, vendor, harness, color, run dirs).
# Bootstrap labels match the forecast-sim plotting scripts so the RNG streams
# (seeded from label + metric) and therefore the std bands are identical.
MODELS = [
    (
        "gpt-5.6-sol (Codex)", "GPT 5.6 Sol", "gpt-5.6-sol", "openai", "Codex", "#007F66",
        [f"codex_aljazeera2026Q2v38_gpt56sol_max_r{i:02d}" for i in range(3)],
    ),
    (
        "gpt-5.5 (Codex)", "GPT 5.5", "gpt-5.5", "openai", "Codex", "#00A67E",
        [f"codex_aljazeera2026Q2v38_gpt55_xhigh_r{i:02d}" for i in range(3)],
    ),
    (
        "claude-opus-5 (Claude Code)", "Opus 5", "opus-5", "anthropic", "Claude Code", "#C15F3C",
        [f"claude_code_aljazeera2026Q2v38_opus5_v1_r{i:02d}" for i in range(2)],
    ),
    (
        "claude-fable-5 (Claude Code)", "Fable 5", "fable-5", "anthropic", "Claude Code", "#9C3017",
        [
            "claude_code_aljazeera2026Q2v38_fable5_cont01_r00_restart",
            "claude_code_aljazeera2026Q2v38_fable5_retry_r01",
            "claude_code_aljazeera2026Q2v38_fable5_r02",
        ],
    ),
    (
        "glm-5.2 (Claude Code)", "GLM 5.2", "glm-5.2", "zhipu", "Claude Code", "#4A4A4A",
        [f"claude_code_aljazeera2026Q2v38_glm52_r{i:02d}" for i in range(5)],
    ),
    (
        "deepseek-v4-flash-0731 (Claude Code)", "DeepSeek V4 Flash 0731", "deepseek-v4-flash-0731",
        "deepseek", "Claude Code", "#6BA4D6",
        [f"claude_code_aljazeera2026Q2v38_deepseek_v4flash0731_v3_openrouter_r{i:02d}" for i in (1, 2, 3)],
    ),
]

METRICS = {"accuracy": ("accuracy", 3), "brier": ("avg_brier", 5)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--analysis-src", type=Path, default=DEFAULT_ANALYSIS_SRC)
    parser.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    sys.path.insert(0, str(args.analysis_src))
    import pandas as pd
    from main_fig_plot import GroupSpec, aggregate_by_group, collect_runs_for_group, hh_any

    runs = []
    seeds_by_label = {}
    for label, name, *_rest, run_dirs in MODELS:
        spec = GroupSpec(label=label, scaffold="", model_id="", run_dirs=run_dirs, hh_predicate=hh_any)
        seeds = collect_runs_for_group(args.runs_dir, spec, end_date=END_DATE)
        if len(seeds) != len(run_dirs):
            raise SystemExit(f"{name}: expected {len(run_dirs)} completed seeds, found {len(seeds)}")
        seeds_by_label[label] = seeds
        runs.extend(seeds)

    grouped = {
        key: aggregate_by_group(runs, metric, START_DATE, resolution_months=RESOLUTION_MONTHS)
        for key, (metric, _digits) in METRICS.items()
    }

    dates = None
    models = []
    for label, name, slug, vendor, harness, color, _run_dirs in MODELS:
        entry = {
            "id": slug,
            "name": name,
            "vendor": vendor,
            "harness": harness,
            "color": color,
            "seeds": len(seeds_by_label[label]),
        }
        for key, (_metric, digits) in METRICS.items():
            model_dates, mean, std, _n = grouped[key][label]
            iso = [pd.Timestamp(d).date().isoformat() for d in model_dates]
            if dates is None:
                dates = iso
            elif iso != dates:
                raise SystemExit(f"{name}: dates differ from the other models")
            entry[key] = {
                "mean": [round(float(v), digits) for v in mean],
                "std": [round(float(v), digits) for v in std],
            }
        models.append(entry)

    output = {
        "version": 1,
        "created_at_utc": datetime.now(UTC).isoformat(timespec="seconds"),
        "simulation": "FutureSim 2026 Q2",
        "method": (
            "Mean over seeds of the daily score on questions resolving in April-June 2026. "
            "Std is a question-level hierarchical bootstrap (questions resampled, then one seed per question)."
        ),
        "dates": dates,
        "models": models,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Wrote {args.output} ({len(models)} models x {len(dates)} days)")
    for model in models:
        print(
            f"  {model['name']:<24} seeds={model['seeds']} "
            f"final acc={model['accuracy']['mean'][-1]:.2f}% +-{model['accuracy']['std'][-1]:.2f} "
            f"brier={model['brier']['mean'][-1]:+.4f} +-{model['brier']['std'][-1]:.4f}"
        )


if __name__ == "__main__":
    main()
