# Forecasting guide — Day 2026-06-24

Score: Brier Skill = 1 - sum(p_i - y_i)^2 over submitted outcomes (+ implicit 1 if true answer unlisted).
TW-score sums daily scores. Every question MUST get a submission today.

## Calibration rules
- Submit 3-5 REAL named outcomes per question (never Other/Unknown/TBD). Max 5.
- Probabilities sum <= 1.0. Scale total mass to confidence:
  - Near-certain favorite (odds-on, single dominant): top 0.55-0.75, total ~0.9
  - Clear favorite among few: top 0.35-0.5, total 0.8-0.95
  - Open field, plausible top-5 covers ~50%: top 0.15-0.25, total 0.5-0.7
  - Very open / speculative (transfers, one-off events): top 0.08-0.15, total 0.3-0.5. Do NOT inflate: a miss costs sum(p^2).
  - Conditional questions ("If X leaves/traded..."): forecast the conditional destination distribution at moderate mass (total 0.4-0.6) since question may void if condition fails — still submit best destinations.
- Exact string matters loosely (grader likely fuzzy-matches names); use full canonical names: full person name, full club/team name, country common name, full month name. Match the "Accepted Answer Format" in resolution criteria exactly.
- For two-team finals / head-to-head style answers use the format implied (e.g. two countries: give pairs like "Nigeria and Morocco" — check criteria).

## Evidence (in priority order)
1. `articles/2026/06/24/articles.jsonl` — grep it first (free). Use python/grep for keywords per question.
2. `mcp__forecast__search_news` — date-capped web search. Budget ~35 searches per batch. Spend on near-term/uncertain questions; use betting-odds/favorites queries for sports ("X odds favourite"), official announcements for politics.
3. Base rates / prior knowledge for far-future questions (defending champions, rankings, incumbents).

Today is 2026-06-24 in-simulation. The 2026 FIFA World Cup and ICC Women's T20 World Cup are IN PROGRESS — search current standings/results, do not rely on pre-tournament priors alone. Wimbledon 2026 starts ~June 29. F1 2026 season in progress (new regs) — check current standings/form.

## Submission
- Call `mcp__forecast__submit_forecasts(question_id, outcomes)` once per question, question_id = qid string.
- ALSO write every forecast to `memory/batches/forecasts_batch_NN.json` as a list of {"question_id":..., "outcomes":{...}, "rationale":"one line"} BEFORE/AFTER submitting, so work survives if submission fails.
- If submit tool is unavailable to you, still write the JSON file completely and report that.
- Do NOT call next_day.
