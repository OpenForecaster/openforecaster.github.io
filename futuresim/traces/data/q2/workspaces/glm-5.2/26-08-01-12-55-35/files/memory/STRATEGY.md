# Forecasting Strategy — Al Jazeera 2026 Q2 (378 questions)

## Date context
- Simulation "today": 2026-03-25. Articles available up to 2026-03-25.
- Questions resolve 2026-04-01 through 2026-06-28. All in the FUTURE relative to available news.
- So most answer-relevant events haven't been reported yet; lean on general knowledge + reasoning + trend extrapolation. Some events (ongoing conflicts, scheduled sports/politics) can be informed by current news.

## Scoring insight (CRITICAL)
- Brier Skill Score = 1 - Σ(p_i - y_i)^2 over SUBMITTED outcomes only (max 5).
- Blank prediction on a day = 0 score that day.
- A calibrated guess almost ALWAYS beats blank: even if wrong & answer not in list, score ≈ 1 - Σp_i^2 ≈ 0.8+ when spread thin.
- Expected score with best guess prob p=q (true belief): ≈ 1 - q(1-q), always ≥ 0.75.
- CONCLUSION: Submit on EVERY question. Avoid p>~0.6 on any single guess unless very confident. Spread remaining prob on alternatives. Keep Σp_i^2 low for downside protection.
- Downside risk: putting high prob (p>0.7) on a WRONG answer → negative score. So cap confidence.

## Per-question approach
- Put main guess at probability = calibrated confidence (usually 0.15-0.45).
- Fill 2-4 alternatives at lower probabilities.
- Leave residual unassigned (sum < 1) — this is the implicit "none of these" and protects when wrong.

## Workflow
- Process in resolution-date order (earliest first — lock in days, get feedback soonest).
- Update daily as new articles arrive.
- Track reasoning in per-topic notes.
