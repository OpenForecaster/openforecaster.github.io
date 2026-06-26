# FINAL OUTCOME — Simulation Complete (all 330 questions resolved)

## Result
- **Time-Weighted Score: +585.54** (strongly positive; "abstain everything" = 0)
- Accuracy (top-guess exact match): 8.2% — low because answers are hyper-specific (exact towns, people, missile names), but Brier skill/TW strongly positive via hedging.
- Brier Skill Score (mean): 0.026

## What worked (the winning strategy)
1. **Day-1 full coverage:** predicted all 330 immediately → no zero-days.
2. **Scoring discovery (Day 8):** harness penalizes Σp² when wrong; overconfidence is costly. Recalibrated all speculative predictions to honest low mass (~0.05-0.12/outcome). This flipped the trajectory from negative (-36) to positive.
3. **Diversification:** low-mass 2nd/3rd/4th guesses captured many wins (Carrick, UAE, PKK, DHS, Rubio, Parchin, Alcaraz 0.34, USA hockey 0.26, PrSM, Kharg, Fujairah, etc.). The right answer was very often a non-obvious 2nd choice.
4. **Research on live events:** AFCON bracket (Algeria→+45, Nigeria SF→+33), Super Bowl (Seahawks), Carabao Cup (Arsenal→+14), Sarvarov, Grammy nominees, Oscar/Sinners context, hockey finalists (Canada/USA), Fury-Makhmudov, SDF/Syria, Israel WC exclusion, etc. Each researched bet was worth +10 to +45.
5. **Cap overcommits at ~0.30-0.40:** big losses came from >0.40 on "obvious" answers that were wrong (Man City Deloitte→Liverpool, Hezbollah, Ethiopia/Somalia, Kerala/Nipah, Sarvarov→Alekseyev).
6. **Scenario mapping:** the question set encodes a coherent US/Israel-Iran war (Jan-Mar 2026) + Israel-Lebanon + Sudan + sports calendars. Betting the scenario's logic (Iran withdraws from WC, Tehran/Isfahan struck, Strait of Hormuz, Gulf refineries, SDF/al-Jamaa in Lebanon) paid off.

## Key misses / lessons
- Exact name SPELLING matters (Thai PM: had "Ruangchan", truth "Ruengpanyawut").
- Answer GRANULARITY (Washington D.C. vs "White House"; city vs specific venue).
- Recurring scenario entities: al-Jamaa al-Islamiya (Lebanese group), "Board of Peace", Kharg Island, PrSM, UAE as Gulf target. Hindsight: hedge these more.
- Research EARLY (playoff brackets, draws) — late updates only score the final day; early correct bets compound across all active days.

## Tooling notes for future runs
- work/preds.json = current predictions; work/preds.py = generator; memory/STRATEGY.md + MEMORY.md = full reasoning log.
- News corpus reaches ~current sim date; AO 2026 match results were NOT indexed (only 2023-24), limiting tennis research. Olympics/T20/soccer/geo were researchable.
