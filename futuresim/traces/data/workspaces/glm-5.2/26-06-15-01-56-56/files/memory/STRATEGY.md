# Forecasting Strategy & Scoring Notes

## Task
- 330 open-ended (string) questions, all resolving Jan 1 – Mar 28, 2026.
- News corpus grows 1 day at a time (call next_day). Today = 2025-12-24, only Dec 24 articles exist.
- Questions describe specific future events; many reference incidents that haven't happened yet.
- Goal: MAXIMIZE TW-score = sum over days of (daily Brier skill * 100 / total_q_days). Early predictions weighted heavily.

## Scoring model (best inference)
- Brier Skill = 1 - Σ_i (p_i - y_i)^2. Max 5 outcomes. Real answers only.
- Robust strategy: identify top 1-3 most likely answers; put ~50-70% on favorite; ~30-50% across 2-4 alternatives. Sums ~1.0.
- A prediction on every active question every day beats blank (0 score).
- UPDATE daily as news arrives — esp. for questions resolving soon.

## Workflow
- master_predictions.csv: qid, res_date, my_answer(s)+probs, confidence, notes.
- Each day: scan new articles, update predictions where news changes the picture.
- Prioritize by (a) soonest resolution, (b) where new info most changes odds.

## Lessons (fill in as we learn)
