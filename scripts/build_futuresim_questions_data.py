#!/usr/bin/env python3
"""Build the data behind the FutureSim "Questions" page (futuresim/questions/).

The page previews 50 of the 252 questions in the 2026 Q3 set and shows, for
each one, how every leaderboard agent's forecast moved over the simulation.

Two things are curated by hand and live in this file:

* ``DOMAIN_QIDS`` files every one of the 252 questions under a topic; the
  topics roll up into the six categories the page filters by.
* ``PREVIEW_QIDS`` is the 50-question preview: widely followed events with an
  unambiguous answer, spread over the topics of each category, with a mix of
  questions the agents got right and wrong. It is deliberately not
  proportional to the full set, which is mostly sport (147 of 252): the
  preview shows 13 sport questions so that the other categories get room.
  The script prints how far the preview's accuracy is from the full set's.

Everything else is computed from the same runs as the Q3 leaderboard
(``clean_runs_Q3v8``, see build_futuresim_q3_chart_data.py), with the scoring
rules of forecast-sim's ``analysis/src/main_fig_plot.py``:

* the forecast in force on a day is the latest one submitted on or before it
  (and never after the question's resolution date);
* an outcome counts as the answer if it is the ground-truth string or the
  run's answer matcher judged it equivalent (``matcher_cache.json``);
* Brier skill score = 1 - sum((p - y)^2), with a further -1 if the answer
  was not listed at all. No forecast scores 0.

Usage:
    python scripts/build_futuresim_questions_data.py \
        --questions /fast/nchandak/datasets/OpenForesight/aljazeera2026Q3v8-00000-of-00001.parquet \
        --runs-dir /is/cluster/fast/sgoel/forecasting/current_sim/clean_runs_Q3v8
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import unicodedata
from collections import Counter
from datetime import UTC, date, datetime
from pathlib import Path

import pandas as pd

DEFAULT_QUESTIONS = Path("/fast/nchandak/datasets/OpenForesight/aljazeera2026Q3v8-00000-of-00001.parquet")
DEFAULT_RUNS_DIR = Path("/is/cluster/fast/sgoel/forecasting/current_sim/clean_runs_Q3v8")
DEFAULT_OUTPUT = Path("futuresim/questions/data/q3_questions.json")
DEFAULT_LEADERBOARD = Path("futuresim/data/q3_results.json")

SPLIT = "aljazeera2026Q3v8"
SIM_START = date(2026, 6, 24)
SIM_END = date(2026, 9, 30)
PREVIEW_SIZE = 50
MAX_OUTCOMES = 5

# (display name, slug, vendor, harness, color, run dirs) - the Q3 leaderboard
# line-up, in leaderboard order. Keep in sync with build_futuresim_q3_chart_data.py.
MODELS = [
    (
        "GPT 6.1 Sol", "gpt-6.1-sol", "openai", "Codex", "#00BF8F",
        [f"codex_aljazeera2026Q3v8_gpt61sol_max_exa_r{i:02d}" for i in range(2)],
    ),
    (
        "Opus 5.5", "opus-5.5", "anthropic", "Claude Code", "#B5462A",
        [f"claude_code_aljazeera2026Q3v8_opus55_exa_r{i:02d}" for i in range(2)],
    ),
    (
        "DeepSeek V4.1 Flash 1017", "deepseek-v4.1-flash-1017", "deepseek", "Claude Code", "#2456A8",
        [f"claude_code_aljazeera2026Q3v8_deepseek_v41flash1017_openrouter_exa_r{i:02d}" for i in range(3)],
    ),
    (
        "GLM 5.3 Flash", "glm-5.3-flash", "zhipu", "Claude Code", "#0A0A0A",
        [f"claude_code_aljazeera2026Q3v8_glm53flash_exa_r{i:02d}" for i in (0, 1, 2, 3, 5)],
    ),
    (
        "Muse Wonder Full 1.0", "muse-wonder-full-1.0", "meta", "Muse", "#3182F4",
        [f"muse_aljazeera2026Q3v8_wonderfull_max_exa_r{i:02d}" for i in range(2)],
    ),
]

# (id, label, icon). The categories the page filters by, in display order.
# The icon is the id of a topic whose icon stands for the whole category.
CATEGORIES = [
    ("geopolitics", "Geopolitics", "geopolitics"),
    ("politics", "Politics & law", "politics"),
    ("economy", "Economy & business", "economy"),
    ("science", "Science & environment", "scitech"),
    ("culture", "Arts & entertainment", "culture"),
    ("sport", "Sport", "othersports"),
]

# (id, label, category). The topic each question is filed under; the id is
# also the name of its icon in futuresim/questions/icons.svg.
DOMAINS = [
    ("geopolitics", "Geopolitics", "geopolitics"),
    ("politics", "Elections & government", "politics"),
    ("law", "Courts & justice", "politics"),
    ("economy", "Economy & business", "economy"),
    ("environment", "Climate, disasters & health", "science"),
    ("scitech", "Technology & space", "science"),
    ("culture", "Arts & entertainment", "culture"),
    ("football", "Football", "sport"),
    ("tennis", "Tennis", "sport"),
    ("motorsport", "Motorsport", "sport"),
    ("cricket", "Cricket", "sport"),
    ("athletics", "Athletics & Olympic sports", "sport"),
    ("othersports", "US leagues, combat & golf", "sport"),
]

# Every question in the set, assigned by reading it.
DOMAIN_QIDS = {
    "geopolitics": """
        659176 666563 425213 249565 126882 339902 107175 971524 238968 709570 576510 817209
        202511 251083 112235 422179 246629 916964 461239 874244 834692 921981 712131 790870
        508136 759359 174389 101639 56802 88025 870914
    """,
    "politics": """
        754639 76066 107473 362674 927657 415011 481741 716751 883794 874628 685197 49405
        882554 720221 844962 845687 970733 764491 846721 720892 120116 673971 408396 581343
        660356 934953 81247 935351 335239
    """,
    "economy": """
        263626 279946 329053 605397 942650 687277 565579 205592 299105
    """,
    "law": """
        213487 946660 984539 903565 880660 25611 423956 788295 76365 138739 342722
    """,
    "environment": """
        604201 764544 633052 446236 66613 442417 872064 149811 683823 737715 772343 903529
        224345 490094
    """,
    "scitech": """
        803035 731076 154739 133827 48050
    """,
    "culture": """
        33659 964047 52657 216881 440552 873349
    """,
    "football": """
        935518 524604 199448 457239 439898 592683 201629 241292 581542
        26225 617889 696503 108618 810891 243962 918938 459381 160265 770763 225772 248237
        767460 974146 222955 388162 623398 588637 162316 450664 876325 20480 127253 72574 875467
        619176 517488 628038 754377 311120 541001 279786 616886 163032 72132 97251 277370
        53266 79046 591807 568969 284913 546622 5814 487575 816232 753240 729308 297571
        564365 173061 158157 815451 889545
    """,
    "tennis": """
        985440 846335 742225 356778 443143 229258 277746 418046 855662 260735 372528 772246
        408930 608158 891014
    """,
    "motorsport": """
        747581 897546 556116 475441 918398 594916 259947 669987 668636 48458 447470 315568 187330
    """,
    "cricket": """
        258607 799550 562262 131869 179451 988210 920782 356699 971366 540490
    """,
    "athletics": """
        906651 970163 449245 22056 354508 2260 409386 936021 261941 30434 653425 518392
        784475 686508 695205
        45561 777991 985937 292136 67348 224082 300850 832291 190556 996188 259249 556932
        700005 574485 944956 24813
    """,
    "othersports": """
        344207 177324 902592 607314 981188 805635
        674079 113668 40115 425800 574553 723378
        32938 992842 969395
    """,
}

# The 50-question preview, one line per category in CATEGORIES order.
PREVIEW_QIDS = """
    249565 238968 834692 112235 921981 56802 817209 870914 174389 339902
    754639 76066 883794 120116 81247 935351 970733 581343 76365 880660 903565
    329053 205592 279946 942650 605397
    66613 772343 903529 149811 48050 133827 803035
    216881 873349 52657 964047
    241292 201629 810891 616886 97251 846335 891014 668636 258607 24813 686508 981188 40115
""".split()


# ---------------------------------------------------------------------------
# Scoring - mirrors forecast-sim analysis/src/main_fig_plot.py
# ---------------------------------------------------------------------------

def as_float(value, default: float = 0.0) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError):
        return default
    return default if x != x else x


def matcher_normalize(text) -> str:
    return str(text or "").strip().lower()


def score_normalize(text) -> str:
    return str(text or "").lower().replace(" ", "").strip()


def load_matcher_cache(run_path: Path) -> dict[tuple[str, ...], bool]:
    cache_path = run_path / "matcher_cache.json"
    if not cache_path.is_file():
        return {}
    raw = json.loads(cache_path.read_text(encoding="utf-8"))
    cache: dict[tuple[str, ...], bool] = {}
    for key, value in raw.items():
        try:
            parts = json.loads(str(key))
            if isinstance(parts, list):
                cache[tuple(str(x) for x in parts)] = bool(value)
                continue
        except json.JSONDecodeError:
            pass
        legacy = str(key).split("|||")
        if len(legacy) in (3, 4):
            cache[tuple(legacy)] = bool(value)
    return cache


def is_equivalent(predicted, truth, qid, title, cache) -> bool:
    pred_norm = matcher_normalize(predicted)
    truth_norm = matcher_normalize(truth)
    if pred_norm == truth_norm:
        return True
    key = (pred_norm, truth_norm, str(qid), matcher_normalize(title))
    if key in cache:
        return cache[key]
    if key[:3] in cache:
        return cache[key[:3]]
    return score_normalize(predicted) == score_normalize(truth)


def matched_outcome(outcomes: dict, truth, qid, title, cache):
    """The listed outcome that counts as the answer, or None."""
    if truth in outcomes:
        return truth
    for outcome in outcomes:
        if is_equivalent(outcome, truth, qid, title, cache):
            return outcome
    return None


def brier_skill(outcomes: dict | None, matched) -> float:
    if not outcomes:
        return 0.0
    brier = sum((as_float(p) - (1.0 if o == matched else 0.0)) ** 2 for o, p in outcomes.items())
    if matched is None:
        brier += 1.0
    return 1.0 - brier


def top_choice_correct(outcomes: dict | None, truth, qid, title, cache) -> bool:
    if not outcomes:
        return False
    best, best_p = None, -1.0
    for outcome, prob in outcomes.items():
        p = as_float(prob)
        if p > best_p:
            best, best_p = outcome, p
    return best is not None and is_equivalent(best, truth, qid, title, cache)


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

def run_path(runs_dir: Path, name: str) -> Path:
    subs = [p for p in (runs_dir / name).iterdir() if p.is_dir()]
    if len(subs) != 1:
        raise SystemExit(f"expected exactly one timestamp folder in {runs_dir / name}, found {len(subs)}")
    return subs[0]


def load_run(path: Path) -> dict:
    csv.field_size_limit(10**9)
    with (path / "market.csv").open(encoding="utf-8", newline="") as f:
        market = {str(r["qid"]): r for r in csv.DictReader(f)}
    predictions: dict[str, list[tuple[date, dict]]] = {}
    resolved_brier: dict[str, float] = {}
    with (path / "actions.jsonl").open(encoding="utf-8") as f:
        for line in f:
            row = json.loads(line)
            qid = str(row.get("question_id"))
            if row.get("type") == "prediction":
                day = date.fromisoformat(str(row["sim_date"])[:10])
                outcomes = {str(k): as_float(v) for k, v in (row.get("outcomes") or {}).items()}
                predictions.setdefault(qid, []).append((day, outcomes))
            elif row.get("type") == "resolution":
                raw = row.get("raw_brier") or {}
                if raw:
                    resolved_brier[qid] = as_float(next(iter(raw.values())))
    for preds in predictions.values():
        preds.sort(key=lambda x: x[0])  # stable: the last forecast of a day wins
    return {
        "market": market,
        "predictions": predictions,
        "resolved_brier": resolved_brier,
        "cache": load_matcher_cache(path),
    }


def forecast_as_of(preds: list[tuple[date, dict]], day: date) -> dict | None:
    latest = None
    for d, outcomes in preds:
        if d <= day:
            latest = outcomes
        else:
            break
    return latest


# ---------------------------------------------------------------------------
# Text
# ---------------------------------------------------------------------------

def clean_text(text) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", "", str(text or "")))
    return re.sub(r"\s+", " ", text).strip()


def typeset(text: str) -> str:
    """Typographic apostrophes and quotation marks for text shown on the page.

    The source mixes straight and curly marks; the page should read one way."""
    text = re.sub(r"(?<=\w)'(?=\w)", "\u2019", text)                    # Women's, d'Ivoire
    text = re.sub(r"(?<=[sS])'(?=\s|$|[.,;:?!)])", "\u2019", text)       # the players' union
    text = re.sub(r"(?<![\w.,;:?!)])'(?=\S)", "\u2018", text)           # opening single quote
    text = text.replace("'", "\u2019")
    text = re.sub(r'(?<![\w.,;:?!)\u2019\u201d])"(?=\S)', "\u201c", text)  # opening double quote
    return text.replace('"', "\u201d")


RELATED_STORIES = re.compile(r"Recommended Stories\s*list of \d+ items.*?end of list", re.S)


def answer_only_in_related_stories(row) -> bool:
    """True when the source article names the answer only in its "Recommended Stories" list.

    A few questions were written from a headline in that list, so the article itself is
    about something else. The page says so next to the source link."""
    def plain(text) -> str:
        decomposed = unicodedata.normalize("NFKD", str(text))
        stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
        return " ".join(re.sub(r"[^a-z0-9 ]+", " ", stripped.lower()).split())

    answer = plain(row.answer)
    tokens = [w for w in answer.split() if len(w) > 3] or answer.split()

    def names(text) -> bool:
        words = plain(text)
        return answer in words or any(w in words.split() for w in tokens)

    own = " ".join([RELATED_STORIES.sub(" ", str(row.article_maintext)), str(row.article_title),
                    str(row.article_description)])
    return names(row.article_maintext) and not names(own)


def parse_criteria(raw: str) -> list[list[str]]:
    """``<li><b>Label</b>: text</li>`` items as [label, text] pairs."""
    items = []
    for body in re.findall(r"<li>(.*?)</li>", str(raw or ""), flags=re.S):
        m = re.match(r"\s*<b>(.*?)</b>\s*:?\s*(.*)", body, flags=re.S)
        if m:
            items.append([typeset(clean_text(m.group(1))), typeset(clean_text(m.group(2)))])
        elif clean_text(body):
            items.append(["", typeset(clean_text(body))])
    return items


def merge_key(text: str) -> str:
    """Key used to merge spelling variants of the same outcome across seeds."""
    decomposed = unicodedata.normalize("NFKD", str(text))
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", stripped.lower())


def answer_kind(answer_type: str) -> str:
    m = re.search(r"\((.*?)\)", str(answer_type or ""))
    return m.group(1) if m else str(answer_type or "")


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def day_index(d: date) -> int:
    return (d - SIM_START).days


def build_series(question: dict, runs: list[dict]) -> tuple[dict, dict]:
    """Seed-averaged forecast history of one model on one question.

    Returns (series, labels) where series holds one entry per day on which any
    seed changed its forecast, and labels maps merge key -> display label.
    """
    qid, title, truth = question["qid"], question["title"], question["answer"]
    resolves = question["resolves"]
    n = len(runs)

    per_seed = []
    for run in runs:
        preds = [(d, o) for d, o in run["predictions"].get(qid, []) if d <= resolves]
        per_seed.append(preds)
    days = sorted({d for preds in per_seed for d, _ in preds})

    labels: dict[str, str] = {}
    label_votes: dict[str, Counter] = {}
    series = {"d": [], "p": [], "lo": [], "hi": [], "b": [], "a": [], "o": []}

    for day in days:
        p_seed, b_seed, a_seed = [], [], []
        merged: Counter = Counter()
        for run, preds in zip(runs, per_seed):
            outcomes = forecast_as_of(preds, day)
            if not outcomes:
                p_seed.append(0.0)
                b_seed.append(0.0)
                a_seed.append(0.0)
                continue
            matched = matched_outcome(outcomes, truth, qid, title, run["cache"])
            p_seed.append(as_float(outcomes[matched]) if matched is not None else 0.0)
            score = brier_skill(outcomes, matched)
            if day == resolves and qid in run["resolved_brier"]:
                score = run["resolved_brier"][qid]
            b_seed.append(score)
            a_seed.append(1.0 if top_choice_correct(outcomes, truth, qid, title, run["cache"]) else 0.0)
            for outcome, prob in outcomes.items():
                key = "" if outcome == matched else merge_key(outcome)
                if key:
                    label_votes.setdefault(key, Counter())[outcome.strip()] += 1
                merged[key] += as_float(prob) / n
        series["d"].append(day_index(day))
        series["p"].append(round(sum(p_seed) / n, 4))
        series["lo"].append(round(min(p_seed), 4))
        series["hi"].append(round(max(p_seed), 4))
        series["b"].append(round(sum(b_seed) / n, 4))
        series["a"].append(round(sum(a_seed) / n, 4))
        ranked = sorted(merged.items(), key=lambda kv: (-kv[1], kv[0]))
        top = [kv for kv in ranked if kv[1] > 0][:MAX_OUTCOMES]
        if merged.get("", 0) > 0 and all(k != "" for k, _ in top):
            top[-1] = ("", merged[""])
        series["o"].append([[k, round(v, 3)] for k, v in top])

    for key, votes in label_votes.items():
        labels[key] = votes.most_common(1)[0][0]
    series["n"] = round(sum(len({d for d, _ in preds}) for preds in per_seed) / n, 1)
    return series, labels


def final_scores(question: dict, runs: list[dict]) -> tuple[float, float, float]:
    """(top-1 accuracy, Brier skill, p(answer)) at resolution, averaged over seeds."""
    qid, title, truth = question["qid"], question["title"], question["answer"]
    acc = brier = prob = 0.0
    for run in runs:
        outcomes = forecast_as_of(run["predictions"].get(qid, []), question["resolves"])
        matched = matched_outcome(outcomes, truth, qid, title, run["cache"]) if outcomes else None
        acc += 1.0 if top_choice_correct(outcomes, truth, qid, title, run["cache"]) else 0.0
        brier += run["resolved_brier"].get(qid, brier_skill(outcomes, matched))
        prob += as_float(outcomes[matched]) if matched is not None else 0.0
    n = len(runs)
    return acc / n, brier / n, prob / n


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS)
    parser.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--leaderboard", type=Path, default=DEFAULT_LEADERBOARD,
                        help="Q3 leaderboard JSON, only used to cross-check the scoring.")
    args = parser.parse_args()

    df = pd.read_parquet(args.questions)
    df["qid"] = df["qid"].astype(str)

    domain_of: dict[str, str] = {}
    for dom, blob in DOMAIN_QIDS.items():
        for qid in blob.split():
            if qid in domain_of:
                raise SystemExit(f"question {qid} is in both {domain_of[qid]} and {dom}")
            domain_of[qid] = dom
    if set(domain_of) != set(df["qid"]):
        raise SystemExit(
            f"domain map does not cover the set: missing {sorted(set(df['qid']) - set(domain_of))}, "
            f"extra {sorted(set(domain_of) - set(df['qid']))}"
        )

    category_of = {dom: category for dom, _label, category in DOMAINS}
    if set(category_of) != set(DOMAIN_QIDS) or set(category_of.values()) != {c for c, _l, _i in CATEGORIES}:
        raise SystemExit("DOMAINS, DOMAIN_QIDS and CATEGORIES do not line up")
    if len(set(PREVIEW_QIDS)) != PREVIEW_SIZE or len(PREVIEW_QIDS) != PREVIEW_SIZE:
        raise SystemExit(f"the preview should be {PREVIEW_SIZE} distinct questions, got {len(set(PREVIEW_QIDS))}")
    if not set(PREVIEW_QIDS) <= set(domain_of):
        raise SystemExit(f"preview questions not in the set: {sorted(set(PREVIEW_QIDS) - set(domain_of))}")
    totals = Counter(category_of[dom] for dom in domain_of.values())
    picked = Counter(category_of[domain_of[q]] for q in PREVIEW_QIDS)

    questions: dict[str, dict] = {}
    for row in df.itertuples(index=False):
        questions[row.qid] = {
            "qid": row.qid,
            "title": clean_text(row.question_title),
            "answer": str(row.answer),
            "resolves": date.fromisoformat(str(row.resolution_date)[:10]),
            "row": row,
        }

    print("loading runs ...")
    model_runs = []
    for name, slug, vendor, harness, color, run_dirs in MODELS:
        runs = [load_run(run_path(args.runs_dir, d)) for d in run_dirs]
        for run in runs:
            for qid, q in questions.items():
                m = run["market"][qid]
                if str(m["ground_truth"]) != q["answer"] or str(m["resolution_date"])[:10] != q["resolves"].isoformat():
                    raise SystemExit(f"{slug}: market.csv disagrees with the question set on {qid}")
                q["title_run"] = m["title"]
        model_runs.append((name, slug, vendor, harness, color, runs))
    # The matcher cache is keyed on the title as the run saw it.
    for q in questions.values():
        q["title"], q["title_display"] = q.pop("title_run"), q["title"]

    # Cross-check against the leaderboard and measure how representative the preview is.
    leaderboard = {}
    if args.leaderboard.is_file():
        for m in json.loads(args.leaderboard.read_text(encoding="utf-8"))["models"]:
            leaderboard[m["id"]] = (m["accuracy"]["mean"][-1], m["brier"]["mean"][-1])
    print(f"\n{'model':28s} {'top-1 all':>9s} {'preview':>8s} {'brier all':>10s} {'preview':>8s}   leaderboard")
    finals: dict[str, dict[str, tuple[float, float, float]]] = {}
    for name, slug, *_rest, runs in model_runs:
        finals[slug] = {qid: final_scores(q, runs) for qid, q in questions.items()}
        acc_all = sum(v[0] for v in finals[slug].values()) / len(questions)
        bri_all = sum(v[1] for v in finals[slug].values()) / len(questions)
        acc_pre = sum(finals[slug][q][0] for q in PREVIEW_QIDS) / PREVIEW_SIZE
        bri_pre = sum(finals[slug][q][1] for q in PREVIEW_QIDS) / PREVIEW_SIZE
        ref = leaderboard.get(slug)
        note = f"{ref[0]:.1f}% / {ref[1]:.3f}" if ref else "n/a"
        print(f"{name:28s} {100 * acc_all:8.1f}% {100 * acc_pre:7.1f}% {bri_all:10.3f} {bri_pre:8.3f}   {note}")
        if ref and (abs(100 * acc_all - ref[0]) > 0.05 or abs(bri_all - ref[1]) > 0.0005):
            raise SystemExit(f"{slug}: scores do not reproduce the leaderboard")

    print(f"\n{'category':24s} {'full set':>8s} {'preview':>8s}")
    for category, label, _icon in CATEGORIES:
        print(f"{label:24s} {totals[category]:8d} {picked[category]:8d}")

    out_questions = []
    for qid in PREVIEW_QIDS:
        q = questions[qid]
        row = q["row"]
        labels: dict[str, str] = {}
        series_by_model = {}
        for _name, slug, *_rest, runs in model_runs:
            series, model_labels = build_series(q, runs)
            for key, label in model_labels.items():
                labels.setdefault(key, label)
            series_by_model[slug] = series
        # Outcome labels become a table; index 0 is always the answer.
        table = [q["answer"]]
        index = {"": 0}
        for series in series_by_model.values():
            for day in series["o"]:
                for pair in day:
                    if pair[0] not in index:
                        index[pair[0]] = len(table)
                        table.append(labels[pair[0]])
                    pair[0] = index[pair[0]]
        out_questions.append({
            "id": qid,
            "category": category_of[domain_of[qid]],
            "topic": domain_of[qid],
            "title": typeset(q["title_display"]),
            "answer": typeset(q["answer"]),
            "answer_kind": answer_kind(row.answer_type),
            "background": typeset(clean_text(row.background)),
            "criteria": parse_criteria(row.resolution_criteria),
            "resolves": q["resolves"].isoformat(),
            "article": {
                "title": typeset(clean_text(row.article_title)),
                "url": str(row.url),
                "date": str(row.article_publish_date)[:10],
                **({"related_only": True} if answer_only_in_related_stories(row) else {}),
            },
            "final": {
                slug: {"p": round(finals[slug][qid][2], 4), "a": round(finals[slug][qid][0], 4),
                       "b": round(finals[slug][qid][1], 4)}
                for _n, slug, *_r in model_runs
            },
            "labels": [typeset(label) for label in table],
            "series": series_by_model,
        })

    output = {
        "version": 2,
        "created_at_utc": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "simulation": "FutureSim 2026 Q3",
        "split": SPLIT,
        "sim_start": SIM_START.isoformat(),
        "sim_end": SIM_END.isoformat(),
        "total_questions": len(questions),
        "categories": [
            {"id": category, "label": label, "icon": icon, "total": totals[category], "preview": picked[category]}
            for category, label, icon in CATEGORIES
        ],
        "topics": [
            {"id": dom, "label": label, "category": category}
            for dom, label, category in DOMAINS
        ],
        "models": [
            {"id": slug, "name": name, "vendor": vendor, "harness": harness, "color": color, "seeds": len(runs)}
            for name, slug, vendor, harness, color, runs in model_runs
        ],
        "questions": out_questions,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"\nwrote {args.output} ({args.output.stat().st_size / 1024:.0f} KB, {len(out_questions)} questions)")


if __name__ == "__main__":
    main()
