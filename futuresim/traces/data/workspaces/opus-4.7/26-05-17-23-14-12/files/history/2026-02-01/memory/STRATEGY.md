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
- **#1 TW DRAIN = concentrated Day-1 prior w/o evidence on speculative who/where Qs.** It accrues negative weight over the WHOLE question life. Fix: Day-1 cap top ≤0.22-0.25, list 5 broad plausible names/places, wide residual. Only spike to a favorite AFTER hard confirming news (then it scores big, e.g. AO Alcaraz +40, Grammy BadBunny +25, CL structural 50/50s +18/+16).
- **Structural/constraint reasoning wins big**: when a Q is constrained by rules (draw pairings, brackets, scheduled events), compute the real distribution (often ~.49/.49 or near-certain) — scored ~+0.5 Brier each.
- **Location Qs w/ niche qualifier**: match the qualifier precisely (coal "miners" → Pavlohrad/Ternivka basin, NOT famous iron-ore Kryvyi Rih). Don't anchor on the famous big city.
- **Event-not-yet-happened "which X" Qs**: keep Σp modest so void/no-event resolution → only small −Σp² loss.
- **Don't over-think on the last day** (956334: Day-1 instinct BF was right; last-day switch to Mali nearly lost it). Trust earlier calibrated reasoning unless NEW evidence.
- Get breaking-cluster facts EARLY (AFCON Senegal, CL standings) — late corrections only earn ~1 day weight.
