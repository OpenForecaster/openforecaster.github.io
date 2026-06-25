#!/usr/bin/env python3
"""Build bootstrapped FutureSim leaderboard data for the static website."""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path
from statistics import mean
from typing import Any

import numpy as np

DATA_DIR = Path("futuresim/traces/data")
FINAL_RUNS = Path("/fast/sgoel/forecasting/current_sim/final_runs_v37")
BOOTSTRAP_SAMPLES = 1000


def main() -> None:
    manifest = json.loads((DATA_DIR / "manifest.json").read_text(encoding="utf-8"))
    run_vectors = []
    warnings = []
    for run in manifest["runs"]:
        original = find_original_run_dir(run)
        if not original:
            raise SystemExit(f"Could not find original run dir for {run['agent_slug']} {run['run_id']}")
        vectors, run_warnings = build_run_vectors(run, original)
        warnings.extend(run_warnings)
        run_vectors.append((run, vectors))

    models = []
    for agent_slug in sorted({run["agent_slug"] for run, _ in run_vectors}):
        items = [(run, vectors) for run, vectors in run_vectors if run["agent_slug"] == agent_slug]
        agent_name = items[0][0]["agent_name"]
        dates = sorted(set.intersection(*(set(vectors) for _, vectors in items)))
        points = []
        for date in dates:
            brier_vectors = [vectors[date]["brier"] for _, vectors in items]
            acc_vectors = [vectors[date]["accuracy"] for _, vectors in items]
            brier_means = [vectors[date]["brier_mean"] for _, vectors in items]
            acc_means = [vectors[date]["accuracy_mean"] for _, vectors in items]
            question_count = min(len(values) for values in brier_vectors)
            points.append(
                {
                    "date": date,
                    "brier_skill_score_mean": round(mean(brier_means), 6),
                    "brier_skill_score_std": round(bootstrap_std(brier_vectors, question_count, f"{agent_slug}:{date}:brier"), 6),
                    "top1_accuracy_mean": round(mean(acc_means) * 100.0, 4),
                    "top1_accuracy_std": round(bootstrap_std(acc_vectors, question_count, f"{agent_slug}:{date}:accuracy") * 100.0, 4),
                    "seed_count": len(items),
                    "question_count": question_count,
                }
            )
        models.append(
            {
                "agent_slug": agent_slug,
                "agent_name": agent_name,
                "seed_count": len(items),
                "points": points,
            }
        )

    output = {
        "version": 1,
        "created_at_utc": datetime.now(UTC).isoformat(),
        "method": (
            "Means are the official daily_metrics.csv means averaged over official seeds. "
            "Std is precomputed by bootstrapping both seeds and question IDs from per-run daily question score vectors."
        ),
        "bootstrap_samples": BOOTSTRAP_SAMPLES,
        "models": models,
        "warnings": warnings,
    }
    (DATA_DIR / "leaderboard.json").write_text(json.dumps(output, indent=2), encoding="utf-8")
    print(f"Wrote {DATA_DIR / 'leaderboard.json'} with {len(models)} models")
    if warnings:
        print(f"{len(warnings)} reconstruction warnings retained in leaderboard.json")


def build_run_vectors(run: dict[str, Any], original: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    market_path = original / "market.csv"
    matcher_path = original / "matcher_cache.json"
    predictions_dir = next(original.glob("agents/*/predictions"), None)
    if not market_path.exists() or not matcher_path.exists() or not predictions_dir:
        raise SystemExit(f"Missing market/matcher/predictions in {original}")

    questions = {row["qid"]: row for row in csv.DictReader(market_path.open(encoding="utf-8"))}
    qids = list(questions)
    matcher_cache = json.loads(matcher_path.read_text(encoding="utf-8"))
    metrics = {row["date"]: row for row in run.get("metrics", [])}
    predictions: dict[str, dict[str, float]] = {}
    vectors = {}
    warnings = []

    for day in run.get("days", []):
        date = day["date"]
        path = predictions_dir / f"{date}.json"
        if path.exists():
            for record in json.loads(path.read_text(encoding="utf-8")):
                qid = str(record.get("question_id") or "")
                outcomes = record.get("outcomes") if isinstance(record.get("outcomes"), dict) else {}
                if qid and outcomes:
                    predictions[qid] = {str(key): float(value) for key, value in outcomes.items()}

        brier = []
        accuracy = []
        for qid in qids:
            outcomes = predictions.get(qid)
            if outcomes:
                brier.append(score_brier(outcomes, questions[qid], matcher_cache))
                accuracy.append(1.0 if score_top1(outcomes, questions[qid], matcher_cache) else 0.0)
            else:
                brier.append(0.0)
                accuracy.append(0.0)

        metric = metrics.get(date)
        if not metric:
            continue
        target_brier = float(metric["brier_skill_score"])
        target_accuracy = float(metric["top1_accuracy"]) / 100.0
        brier_delta = target_brier - mean(brier)
        accuracy_delta = target_accuracy - mean(accuracy)
        if abs(brier_delta) > 0.005 or abs(accuracy_delta) > 0.005:
            warnings.append(
                {
                    "agent_slug": run["agent_slug"],
                    "run_id": run["run_id"],
                    "date": date,
                    "brier_delta": round(brier_delta, 6),
                    "accuracy_delta": round(accuracy_delta, 6),
                }
            )

        vectors[date] = {
            "brier": [value + brier_delta for value in brier],
            "accuracy": [value + accuracy_delta for value in accuracy],
            "brier_mean": target_brier,
            "accuracy_mean": target_accuracy,
        }
    return vectors, warnings


def score_brier(outcomes: dict[str, float], question: dict[str, str], matcher_cache: dict[str, bool]) -> float:
    matched = next((outcome for outcome in outcomes if is_match(outcome, question, matcher_cache)), None)
    brier = sum((prob - (1.0 if outcome == matched else 0.0)) ** 2 for outcome, prob in outcomes.items())
    if matched is None:
        brier += 1.0
    return 1.0 - brier


def score_top1(outcomes: dict[str, float], question: dict[str, str], matcher_cache: dict[str, bool]) -> bool:
    if not outcomes:
        return False
    top = max(outcomes.items(), key=lambda item: item[1])[0]
    return is_match(top, question, matcher_cache)


def is_match(outcome: str, question: dict[str, str], matcher_cache: dict[str, bool]) -> bool:
    truth = question["ground_truth"]
    if outcome == truth or compact(outcome) == compact(truth):
        return True
    key = json.dumps(
        [
            str(outcome).lower().strip(),
            str(truth).lower().strip(),
            str(question["qid"]).lower().strip(),
            str(question["title"]).lower().strip(),
        ],
        ensure_ascii=False,
    )
    return bool(matcher_cache.get(key, False))


def compact(value: str) -> str:
    return str(value or "").lower().replace(" ", "").strip()


def bootstrap_std(vectors: list[list[float]], question_count: int, seed: str) -> float:
    if not vectors or question_count == 0:
        return 0.0
    arr = np.asarray([values[:question_count] for values in vectors], dtype=float)
    rng_seed = int.from_bytes(hashlib.sha256(seed.encode("utf-8")).digest()[:8], "little")
    rng = np.random.default_rng(rng_seed)
    seed_idx = rng.integers(0, arr.shape[0], size=(BOOTSTRAP_SAMPLES, arr.shape[0]))
    question_idx = rng.integers(0, question_count, size=(BOOTSTRAP_SAMPLES, question_count))
    draws = arr[seed_idx[:, :, None], question_idx[:, None, :]].mean(axis=(1, 2))
    return float(draws.std(ddof=1)) if BOOTSTRAP_SAMPLES > 1 else 0.0


def find_original_run_dir(run: dict[str, Any]) -> Path | None:
    from_stdout = original_dir_from_stdout(run)
    if from_stdout and from_stdout.exists():
        return from_stdout

    tokens = model_tokens(run)
    candidates = [path for path in FINAL_RUNS.glob(f"*/{run['run_id']}") if path.is_dir()]
    for candidate in candidates:
        text = str(candidate).lower()
        if any(token in text for token in tokens):
            return candidate
    return candidates[0] if len(candidates) == 1 else None


def original_dir_from_stdout(run: dict[str, Any]) -> Path | None:
    copied = Path("/fast/sgoel/forecasting/current_sim/official_runs_complete") / run["agent_slug"] / run["run_id"]
    stdout = next(copied.glob(f"agents/*/{run['source_filename']}"), None)
    if not stdout:
        return None
    with stdout.open(encoding="utf-8", errors="ignore") as handle:
        for index, line in enumerate(handle):
            if index > 2000:
                break
            if not line.strip():
                continue
            try:
                raw = json.loads(line)
            except json.JSONDecodeError:
                continue
            cwd = find_cwd(raw)
            if cwd:
                root = cwd.split("/agents/")[0]
                return Path(root.replace("/lustre/fast/fast/", "/fast/"))
    return None


def find_cwd(value: Any) -> str:
    if isinstance(value, dict):
        cwd = value.get("cwd")
        if isinstance(cwd, str) and cwd:
            return cwd
        for item in value.values():
            found = find_cwd(item)
            if found:
                return found
    elif isinstance(value, list):
        for item in value:
            found = find_cwd(item)
            if found:
                return found
    return ""


def model_tokens(run: dict[str, Any]) -> list[str]:
    slug = run["agent_slug"]
    return {
        "ds-v4-pro": ["deepseek", "ds-v4"],
        "qwen-3.6-plus": ["qwen36plus", "qwen"],
        "gpt-5.5": ["gpt55"],
        "glm-5.1": ["glm51"],
        "glm-5.2": ["glm52"],
        "opus-4.6": ["opus"],
        "opus-4.7": ["opus47"],
        "opus-4.8": ["opus48"],
        "fable-5": ["fable5"],
    }.get(slug, [slug.replace("-", "")])


if __name__ == "__main__":
    main()
