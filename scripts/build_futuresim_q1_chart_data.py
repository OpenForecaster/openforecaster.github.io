#!/usr/bin/env python3
"""Build the data behind the interactive FutureSim 2026 Q1 leaderboard chart.

Converts the published Q1 leaderboard (``futuresim/traces/data/leaderboard.json``,
written by ``scripts/build_futuresim_leaderboard_data.py``) into the compact
schema that ``assets/futuresim-leaderboard.js`` reads, the same schema as
``futuresim/data/q2_results.json``. No new numbers are computed here.

Usage:
    python scripts/build_futuresim_q1_chart_data.py
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = REPO_ROOT / "futuresim" / "traces" / "data" / "leaderboard.json"
DEFAULT_OUTPUT = REPO_ROOT / "futuresim" / "data" / "q1_results.json"

# (leaderboard agent_slug, chart id, vendor, harness, color), in legend order.
# Colors are the paper's per-model colors (forecast-sim analysis/src/plot_config.py),
# except Opus 4.7: its paper color #8E4124 is indistinguishable from Fable 5's
# #9C3017 when both are on one chart, so it takes the lighter shade of the same
# family here.
MODELS = [
    ("gpt-5.5", "gpt-5.5", "openai", "Codex", "#00A67E"),
    ("fable-5", "fable-5", "anthropic", "Claude Code", "#9C3017"),
    ("opus-4.8", "opus-4.8", "anthropic", "Claude Code", "#5B2914"),
    ("opus-4.7", "opus-4.7", "anthropic", "Claude Code", "#E0866A"),
    ("opus-4.6", "opus-4.6", "anthropic", "Claude Code", "#C15F3C"),
    ("glm-5.2", "glm-5.2", "zhipu", "Claude Code", "#4A4A4A"),
    ("glm-5.1", "glm-5.1", "zhipu", "Claude Code", "#6E6E6E"),
    ("ds-v4-pro", "deepseek-v4-pro", "deepseek", "Claude Code", "#2B6CB4"),
    ("qwen-3.6-plus", "qwen-3.6-plus", "qwen", "OpenCode", "#5B43D4"),
]

# chart key -> (leaderboard field prefix, decimals kept)
METRICS = {"accuracy": ("top1_accuracy", 3), "brier": ("brier_skill_score", 5)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    source = json.loads(args.source.read_text(encoding="utf-8"))
    by_slug = {model["agent_slug"]: model for model in source["models"]}
    unlisted = sorted(set(by_slug) - {slug for slug, *_ in MODELS})
    if unlisted:
        raise SystemExit(f"Leaderboard agents missing from MODELS: {', '.join(unlisted)}")

    dates = None
    models = []
    for slug, chart_id, vendor, harness, color in MODELS:
        if slug not in by_slug:
            raise SystemExit(f"{slug}: not in {args.source}")
        agent = by_slug[slug]
        points = agent["points"]
        agent_dates = [point["date"] for point in points]
        if dates is None:
            dates = agent_dates
        elif agent_dates != dates:
            raise SystemExit(f"{slug}: dates differ from the other models")
        entry = {
            "id": chart_id,
            "name": agent["agent_name"],
            "vendor": vendor,
            "harness": harness,
            "color": color,
            "seeds": agent["seed_count"],
        }
        for key, (field, digits) in METRICS.items():
            entry[key] = {
                "mean": [round(float(point[f"{field}_mean"]), digits) for point in points],
                "std": [round(float(point[f"{field}_std"]), digits) for point in points],
            }
        models.append(entry)

    output = {
        "version": 1,
        "created_at_utc": source["created_at_utc"],
        "simulation": "FutureSim 2026 Q1",
        "method": source["method"],
        "dates": dates,
        "models": models,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Wrote {args.output} ({len(models)} models x {len(dates)} days)")
    for model in models:
        print(
            f"  {model['name']:<16} seeds={model['seeds']} "
            f"final acc={model['accuracy']['mean'][-1]:.2f}% +-{model['accuracy']['std'][-1]:.2f} "
            f"brier={model['brier']['mean'][-1]:+.4f} +-{model['brier']['std'][-1]:.4f}"
        )


if __name__ == "__main__":
    main()
