# Forecasting Strategy & Key Insights

## META-INSIGHT (most important)
- Questions are derived from REAL Al Jazeera Q1 2026 news articles. The events described
  in the questions almost certainly HAPPEN (the benchmark turns a real future article into
  a question). So my job is to predict the SPECIFIC ANSWER (which city/person/team/etc.),
  not whether the premise event occurs.
- Even speculative-sounding clusters (Iran-Israel war Feb-Mar 2026) likely reflect real
  reported events. As of Dec 24 2025: June 2025 saw a 12-day Israel-Iran war; Netanyahu
  expected to ask Trump for help with FRESH strikes. So a new escalation in Q1 2026 is
  plausible/likely per the question set.

## SCORING MODEL (proper scoring rule)
- Brier Skill Score = 1 - Σ(p_i - y_i)^2 over outcomes. Abstain = 0.
- Reporting TRUE calibrated probabilities maximizes expected score. Expected score ≈ q^2
  where q = P(my top guess correct) if single guess.
- ALWAYS predict (never abstain) — calibrated prediction ≥ 0 in expectation.
- List up to 5 top candidates with their TRUE marginal probs. Do NOT inflate to sum=1;
  leave leftover mass for "the field" (unlisted answers).
- Time-weighting: early predictions cover more days → dominate score. For Feb/Mar questions,
  the many "blind" days (before event reported) dominate, so getting the EARLY prediction
  well-calibrated matters most. Update to ~near-certainty once news reports the answer.

## WORKFLOW
1. Triage all 330 Qs by cluster/urgency. (memory/all_titles.txt has all titles)
2. Research clusters via news search (1 search informs many Qs).
3. Submit best-guess predictions on ALL questions ASAP (coverage = score).
4. Each day: read new articles, update predictions where news reveals/clarifies answers.

## CLUSTERS (approx counts)
- Sports: AFCON 2025 (Morocco), AusOpen 2026, T20 WC 2026, UCL R16/playoff, Super Bowl LX,
  Winter Olympics Milano-Cortina, F1, IPL, NBA, boxing/MMA.
- Iran-Israel war scenario (~40 Qs, Feb-Mar 2026): missile strikes, schools, oil, US troops.
- Ukraine-Russia: ministers, peace talks, attacks.
- Elections: Bangladesh (Feb 12), Portugal pres, Nepal PM, Bulgaria pres.
- US politics: immigration/ICE, Epstein, prediction-market bills, appointments.
- Incidents: fires, crashes, attacks, weather.

## CALIBRATION NOTES
- (to be updated as questions resolve)
