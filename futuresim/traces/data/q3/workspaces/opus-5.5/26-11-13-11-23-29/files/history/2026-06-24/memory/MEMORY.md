# MEMORY / PLAN (forecasting run)

## Setup facts
- Sim start date: 2026-06-24. 252 questions, all resolve 2026-07-01 .. 2026-09-30 (column resolution_date; criteria may give later true date).
- Search budget: 3000 total (incl. subagents). Plan: ~850 on day 1 initial research, then ~15-25/day updates.
- Local free resource: articles/YYYY/MM/DD/articles.jsonl (grep it before spending searches).
- Scoring: per question 1 - sum_i (p_i - y_i)^2 incl. true outcome. Unlisted true answer => score = -sum p_i^2.
  Expected score with honest p = sum p_i^2 >= 0, so ALWAYS submit, be calibrated.
- No prediction on a day => 0 for that day. Submit everything on day 1.

## Workflow
- memory/questions_dump.txt : all questions (sorted by res date).
- memory/batches/batch_XX_questions.txt : per-topic batches (19 batches) -> subagents research+submit.
- memory/batches/batch_XX_forecasts.json : subagent outputs (outcomes, rationale, next_info).
- memory/batches/batch_XX_notes.md : evidence notes.
- Daily: check articles for new day, update questions whose events are imminent / news-driven.

## Lessons / calibration notes
(append below)
