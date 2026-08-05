# Forecasting Strategy

## Date
Sim date: 2026-03-25. Articles available to 2026-03-25. Questions resolve Apr-Jun 2026.

## Scoring (confirmed)
Score = 1 - Σ_i (p_i - y_i)^2 - (y_missing)^2
- y_missing = 1 if true answer NOT in my listed outcomes (p=0 implicit).
- Confirmed by: single wrong outcome at p=1.0 → 1 - 1 - 1 = -1 (matches stated -1 lower bound).
- IMPLICATION: Always include best guess. Missing the truth costs full +1 to squared error.
- Concentrate probability when confident; spread across top candidates when uncertain.

## Key tactics
- For open-ended "which city/country/name": list top 3-5 candidates, weight by likelihood.
- Spread thin (5x0.2) beats confident-wrong when high uncertainty.
- TW-score is time-weighted & summed: get EVERY question covered ASAP (no prediction = 0 that day).
- Max 5 outcomes/question, probs sum ≤ 1.0.

## Clusters (by theme)
- US-Iran war (huge): Strait of Hormuz, ceasefires, talks, strikes
- Israel/Gaza/Lebanon/Iran
- Ukraine-Russia
- Sports: FA Cup, NBA/Finals/Draft, F1, tennis (French Open, Wimbledon), golf (Masters, US Open), boxing, chess, MotoGP, IPL, Kentucky Derby, Eurovision, soccer leagues, World Cup prep
- Elections: UK Labour, Australia, Hungary, Slovenia, Colombia, Peru, Djibouti, Kosovo, India states (Bengal, Tamil Nadu), US primaries (gubernatorial, Senate, House), DC mayor
- Tech: Anthropic Claude model, DeepSeek, supercomputers TOP500, Nvidia, SpaceX IPO
- Natural disasters / incidents (hard, spread probability)
- Diplomacy / appointments
