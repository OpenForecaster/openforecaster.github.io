# Forecasting Strategy

## Setup
- 330 questions, all open-ended string answers, NO options provided. Q1 2026 Al Jazeera set.
- Today = 2025-12-24 (sim). Resolution dates 2026-01-01 .. 2026-03-28.
- Article DB current as of sim date. Search news + read articles/YYYY/MM/DD/articles.jsonl.

## Scoring insight
- TW-score per question ≈ daily_BSS*100, normalized by question lifetime. PREDICT EVERYTHING ASAP — every day without a prediction = 0 for that question.
- BSS = 1 - Σ(p_i - y_i)^2. If true answer NOT in my listed outcomes → penalty includes (0-1)^2=1 term. So always cover plausible answers.
- Proper scoring: list up to 5 plausible specific answers with CALIBRATED probs; residual (1-Σp) = implicit "other/none" mass. Don't over-concentrate unless confident.
- Expected BSS for single true-prob-π outcome listed at q: 2πq - q², maximized at q=π → max π². Listing more plausible outcomes raises expected score.

## Workflow
1. Calibrate world model via news on big clusters (Iran/Israel/US war, Ukraine peace talks, AFCON, AusOpen, T20 WC, Winter Olympics, CL, politics).
2. Batch first-pass predictions for ALL 330, prioritizing soonest resolution.
3. Iterate daily on new info; re-submit to overwrite (accrues weight from that day).

## Key clusters (by theme)
- IRAN WAR scenario: ~80 Qs presupposing US-Israel war on Iran (strikes, bases, casualties). Need to assess if war is real as of Dec 2025.
- Ukraine-Russia peace talks (locations, mediators, ministers).
- Sports: AFCON 2025 (Jan), Australian Open 2026 (Jan), T20 World Cup 2026 (Feb-Mar), Champions League playoffs/R16 (Feb-Mar), Winter Olympics Milano Cortina (Feb), Super Bowl LX (Feb 7), IPL 2026 (Mar), Grammys/Oscars (Jan-Feb).
- Politics: Bangladesh election (Feb 12), Thailand election (Feb 8), US (Epstein, immigration, prediction-market bills), Greenland dispute, Venezuela.

## Lessons learned
- (update daily)
