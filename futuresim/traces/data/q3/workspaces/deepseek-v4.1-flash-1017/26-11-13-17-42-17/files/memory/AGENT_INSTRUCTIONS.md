# Research Agent Instructions — Forecasting Simulation

## Context
- Today is **2026-06-24** in a simulated world. You are forecasting events that resolve between July and September 2026.
- Your batch file lists the questions. Each has full title, background, resolution criteria, answer type, resolution date.
- **Evidence sources**: use `mcp__forecast__search_news` (hybrid semantic+keyword search over a date-capped web index; always pass to_date="2026-06-24"). You can also grep the local corpus: `/agent/workspace/articles/2026/06/24/articles.jsonl` (3078 news articles from 2026-06-24; each line is JSON with title/source/content).
- The search index contains simulated 2026 news, Wikipedia snapshots, and real historical pages. Prefer recent (June 2026) sources. Wikipedia pages can be very informative for schedules, standings, and lists.

## Your task per question
1. Run 2-5 targeted searches (use the exact names/terms from the question). Check for: current standings/rankings, schedules, seeded brackets, recent form, official announcements, odds/favorites, expert predictions.
2. Determine the most likely outcome(s). Think about base rates and current evidence.
3. Produce a probability distribution over **up to 5 real outcomes** that sum to ≤ 1.0. Do NOT use placeholders ("Unknown", "TBD", "Other", "N/A", "No one").
4. Use the **exact answer format** requested (e.g., full NBA team name "Cleveland Cavaliers", full person name, full country name, month name "August").

## Calibration guidance (important for scoring)
- Scoring is Brier skill: being confident and right pays; being confident and wrong costs a lot. A well-spread 5-outcome guess earns little; a well-supported favorite at 0.7-0.9 with a couple of backups earns much more when correct.
- If a clear, well-evidenced favorite exists (e.g., standings leader, incumbent, defending champion, heavy odds favorite), assign 0.6-0.9 and spread the rest over 2-4 plausible alternatives.
- If evidence is thin, spread more evenly over the 3-5 most plausible candidates.
- Include a 0.02-0.10 sliver for a surprise candidate only if it doesn't dilute the favorite too much.
- For "which X will..." questions where the same few names recur (e.g., F1 drivers, top tennis players), use recent rankings/results to rank.
- For conditional questions ("If A happens, which B..."), answer the most likely B given A; if the condition is uncertain, still give your best distribution over B answers (the question's resolution may be void otherwise, which we cannot predict).
- For "which month" answers, give the month name(s).
- For yes/no-like or "if any" questions, name the specific most-likely entity; do not answer "none".

## Output format
Write a JSON file to `/agent/workspace/memory/results/<BATCHNAME>.json` (exact batch name from the filename without .txt), containing a list:
```json
[
  {"qid": "123456", "outcomes": {"Most Likely Answer": 0.7, "Second Answer": 0.2, "Third Answer": 0.1}, "rationale": "One sentence with key evidence."},
  ...
]
```
- outcomes: 1-5 entries, probabilities sum ≤ 1.0 (sum to ~1.0 preferably).
- Every qid in the batch file must appear exactly once.
- Also return the same JSON (or a compact summary) as your final message.

## Rules
- NEVER submit forecasts yourself via mcp__forecast__submit_forecasts — only write the JSON file and return it. The orchestrator submits.
- Work efficiently: cap ~4 searches per question. Prioritize questions with the earliest resolution dates.
- If search returns nothing useful, rely on general knowledge, schedules, rankings, and base rates — still produce a distribution.
- Double-check that outcome names are real, specific, and correctly spelled.
