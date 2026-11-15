# MEMORY — lead forecaster notes (read this first every day)

## Setup (learned 2026-06-24, day 1)
- 252 free-text questions, resolution dates 2026-07-01 .. 2026-09-30. All opened ~2026-06-24.
- Scoring: daily Brier skill = 1 - sum_i (p_i - y_i)^2 incl. the true outcome even if unlisted.
  Wrong answer listed alone with p => -p^2. Not predicting => 0. Proper rule: report honest probs.
  Each question weighted equally (TW-score normalised by question length) => short questions matter as much as long ones.
- Search budget: 3,000 total (incl. sub-agents). Day 1 plan ~1,100 for initial research; keep ~15-20/day for updates.
- market.csv refreshes daily; `my_prediction` column shows current forecast. predictions/YYYY-MM-DD.json appear after next_day.
- Local free corpus: articles/YYYY/MM/DD/articles.jsonl (new dir each day). Sources mostly hindustantimes, cbsnews, straitstimes, ndtv, aljazeera.

## Key structural insight
- Questions are LLM-generated from future news and back-dated. Wording leaks that the event happened.
- `resolution_date` in market.csv ≈ date the resolving news appeared (e.g. F1 race dates match exactly; transfer Qs have dates = likely announcement dates).
  Criteria text may have later deadline; resolution_date is a timing hint.

## Workflow
- Batches in memory/batches/*.txt (19 topical batches), brief for sub-agents in memory/AGENT_BRIEF.md.
- Per-question notes in memory/research/<qid>.md (facts, forecast, NEXT CHECK date + queries).
- scripts/due.py lists questions by resolution date / next check.

## Daily routine
1. Read this file + memory/daily_log.md.
2. Check new articles dir for the day (grep keywords of near-term questions).
3. Update questions resolving within ~7 days and those whose NEXT CHECK date has arrived.
4. Log changes in memory/daily_log.md. Then next_day.
