# Forecasting Progress Log

## Day 1: 2026-03-25 (sim)
- Submitted predictions for 375 of 378 questions.
- ABSTAINED on 3 (zero basis, negative EV to guess randomly):
  - 625905 (idx 329) — person released re Mousa al-Omar complaint
  - 186080 (idx 342) — person returned to US for $3.7bn Medicare fraud
  - 666275 (idx 378) — defeats Cameron Norrie Wimbledon R1 (draw-dependent, random)
  - Revisit these on future days once news articles accumulate.
- Strategy: calibrated 2-5 candidate distributions summing ~1.0; concentrated on best guess when confident (e.g., Pulisic captain 0.60, Hamas tunnels 0.80, Orbán PM 0.74), spread when uncertain.
- Coverage by month: April 111/111, May 149/149, June 115/118.

## Key calibration insight (IMPORTANT for future days)
Brier Skill = 1 - Σ(p_i - y_i)^2 with implicit "other" category = (1-Σp) penalized when truth not in list.
- EV of an even 5-way spread (0.20 each) is POSITIVE only if collective P(truth in list) > 0.50.
- So: only predict when candidates are genuinely informed (sports rosters, known officials, plausible geography).
- For truly unknowable specific names (random individuals, draw-dependent matchups): ABSTAIN (0) beats a random guess (~ -0.2).
- When right, concentration raises score; when wrong, concentration lowers it. Concentrate only on confident picks.

## Priority for future days
1. As April/May articles accumulate, REFINE the earliest-resolving questions (April) with real evidence.
2. Fill the 3 abstentions if evidence appears.
3. Re-check sports rosters/lineups as match days approach (injuries change scorers).
4. Watch the US-Iran ceasefire timeline — many questions depend on it (talks leader, Hormuz exemption, missile targets, seized ships).
5. Questions to revisit with news: FA Cup QF opponent (327626), Candidates chess (284263), specific officials appointed.

## World-state facts (see WORLD_STATE.md)
US-Iran war since Feb 28 2026; Hormuz blocked; Khamenei dead; Hezbollah re-engaged Mar 2; Israel DM Katz; Pentagon Hegseth; Trump POTUS; Iran FM Araghchi; Pakistan facilitating US-Iran talks.
