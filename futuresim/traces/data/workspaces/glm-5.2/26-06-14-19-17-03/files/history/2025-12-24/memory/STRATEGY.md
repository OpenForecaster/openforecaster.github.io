# Forecasting Strategy & Key Insights

## Market structure
- 330 string-answer questions, all resolve Q1 2026 (Jan-Mar). Simulation date: 2025-12-24.
- This is the "Al Jazeera Q1 2026" market. Questions are scenario-generated from a simulated future timeline.
- News corpus is REAL news capped at 2025-12-24. Helps with current events (AFCON, politics) but NOT with fictional future events.

## Overarching narrative (key to ~150 questions)
A **US-Israel war on Iran** erupts ~late Feb 2026. Cluster of questions (#200-330) reference:
- Strikes on Iranian cities (Tehran, Isfahan, Natanz, etc.), schools, hospitals
- Gulf state impacts (Saudi Arabia, UAE, Qatar, Bahrain, Kuwait)
- Strait of Hormuz, oil facilities, refineries
- Iran retaliatory missile strikes on Israel, Basij, IRGC
- Diplomatic fallout, peace talks, World Cup venue changes

## Scoring math (CRITICAL)
E[Brier score for a question] = 2·Σ(q_i·p_i) - Σ(p_i²)
where q_i = TRUE prob of my listed candidate i, p_i = my reported prob.
- Optimal: report honest probabilities (p_i = q_i) → E[score] = Σq_i² > 0.
- OVERCONFIDENCE is the killer: p=1 when q=0.1 → E=-0.8.
- Weak calibrated spread (p=0.1 each x5) beats abstention (0) iff my top-5 collectively capture >25% true prob.
- **Abstain on truly random/uninformed questions (expected negative). Forecast everywhere I have ANY basis, with HONEST modest probabilities.**

## TW-score incentives
- Early forecasts carry more weight (cover more days). ACT NOW.
- 0 score for un-predicted questions each day. Cover breadth.
- Update as new info arrives each day.

## Clusters & priority
1. SPORTS (high edge): AFCON 2025 (NOW), AusOpen, T20 WC, UCL playoffs, Winter Olympics, IPL, F1, boxing.
2. POLITICS/appts: Chelsea mgr, Trump cabinet, Syria transition, Thailand/Bangladesh elections.
3. IRAN WAR scenario: reason from priors (Gulf states, cities, waterways).
4. RANDOM incidents: abstain or weak regional guess.

## Per-question notes go in RESEARCH.md
