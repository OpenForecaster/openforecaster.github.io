#!/usr/bin/env python3
"""Build the data behind the interactive FutureSim 2026 Q3 leaderboard chart.

The numbers come from the same question-level hierarchical bootstrap that draws
the paper/website PNGs (``main_fig_plot.aggregate_by_group`` in the forecast-sim
analysis code, as called by ``q3_v8_main_fig.py``), so the interactive chart
shows the same means and +-1 std bands as ``futuresim/figures/q3/*.png``.

The runs are the stitched, one-folder-per-seed copies in ``clean_runs_Q3v8``
(sim days 2026-06-24 to 2026-09-30, plotted from 2026-07-01 like the figure).
DeepSeek V4.1 Flash (the undated snapshot) is left out: only the 1017 snapshot
is shown, as in the Q3 main figure.

Usage:
    python scripts/build_futuresim_q3_chart_data.py \
        --analysis-src /path/to/forecast-sim/analysis/src \
        --runs-dir /is/cluster/fast/sgoel/forecasting/current_sim/clean_runs_Q3v8
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import UTC, datetime
from pathlib import Path

DEFAULT_ANALYSIS_SRC = Path("/lustre/home/nchandak/forecast-sim/analysis/src")
DEFAULT_RUNS_DIR = Path("/is/cluster/fast/sgoel/forecasting/current_sim/clean_runs_Q3v8")
DEFAULT_OUTPUT = Path("futuresim/data/q3_results.json")

START_DATE = "2026-07-01"
END_DATE = "2026-09-30"
RESOLUTION_MONTHS = {7, 8, 9}

# (bootstrap label, display name, slug, vendor, harness, color, run dirs).
# Bootstrap labels match q3_v8_main_fig.py so the RNG streams (seeded from
# label + metric) and therefore the std bands are identical. Colors are the
# paper's per-model colors (forecast-sim analysis/src/plot_config.py).
MODELS = [
    (
        "gpt-6.1-sol (Codex)", "GPT 6.1 Sol", "gpt-6.1-sol", "openai", "Codex", "#00BF8F",
        [f"codex_aljazeera2026Q3v8_gpt61sol_max_exa_r{i:02d}" for i in range(2)],
    ),
    (
        "claude-opus-5-5 (Claude Code)", "Opus 5.5", "opus-5.5", "anthropic", "Claude Code", "#B5462A",
        [f"claude_code_aljazeera2026Q3v8_opus55_exa_r{i:02d}" for i in range(2)],
    ),
    (
        "deepseek-v4.1-flash-1017 (Claude Code)", "DeepSeek V4.1 Flash 1017", "deepseek-v4.1-flash-1017",
        "deepseek", "Claude Code", "#2456A8",
        [f"claude_code_aljazeera2026Q3v8_deepseek_v41flash1017_openrouter_exa_r{i:02d}" for i in range(3)],
    ),
    (
        # r04 was stopped partway and is not in clean_runs_Q3v8.
        "glm-5.3-flash (Claude Code)", "GLM 5.3 Flash", "glm-5.3-flash", "zhipu", "Claude Code", "#0A0A0A",
        [f"claude_code_aljazeera2026Q3v8_glm53flash_exa_r{i:02d}" for i in (0, 1, 2, 3, 5)],
    ),
    (
        "muse-wonder-full-1.0 (Muse)", "Muse Wonder Full 1.0", "muse-wonder-full-1.0", "meta", "Muse", "#3182F4",
        [f"muse_aljazeera2026Q3v8_wonderfull_max_exa_r{i:02d}" for i in range(2)],
    ),
    (
        "gemini-4-carbon (Antigravity)", "Gemini 4 Carbon", "gemini-4-carbon", "google", "Antigravity", "#966AB5",
        [f"agy_aljazeera2026Q3v8_gemini4carbon_high_exa_r{i:02d}" for i in range(2)],
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
        "simulation": "FutureSim 2026 Q3",
        "method": (
            "Mean over seeds of the daily score on questions resolving in July-September 2026. "
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
