# Forecasting Memory

## Current Simulation
- Sim date: 2026-03-25 (day 1). Questions resolve Apr-Jun 2026. Update cadence: daily.
- 378 questions, all string-answer (specific names/locations/countries).
- DAY 1 COMPLETE: submitted predictions for ALL 378 questions (coverage = priority).

## Strategy that worked
- COVERAGE IS KING: 0 score if no active prediction. Day-1 coverage maximizes time-weighted score.
- For uncertain string questions: list 4-5 plausible options at 0.10-0.35 each. Math: missing right answer entirely → score ≈ -(sum of p_i^2) ≈ -0.1 to -0.15 (small downside); including right answer at p → +0.4 to +0.6 upside. Spread caps downside, broadens upside.
- Listing MORE options reduces downside and raises P(include correct). Max 5 outcomes per q.

## CRITICAL LESSON (qid mismatch)
- I keep a handwritten qid→topic map in notes; it had at least 1 ERROR: I thought 407333=West Bank camp, but 407333=Real Madrid Betis goal. West Bank camp = 702685. FIXED both. ALWAYS verify qid→title against market.csv when using notes; the dump (index#) is the source of truth.

## Key Context (from 2026-03-25 articles)
### Iran-US War (started Feb 28, 2026)
- 15-pt ceasefire plan via Pakistan; army chief Asim Munir key mediator. US envoys Witkoff/Kushner; VP Vance, SecState Rubio. Iran lead = FM Abbas Araghchi. Hormuz disrupted. Iran firing at Israel + Gulf states.

### FIFA WC 2026 groups (draw Dec 2025; USA/CAN/MEX hosts; 48 teams)
- A: Mex,SAfrica,SKorea,EuroPlayoffD | B: Can,EuroPlayoffA,Qatar,Sui | C: Brazil,Morocco,Haiti,Scotland
- D: USA,Paraguay,Australia,EuroPlayoffC | E: Germany,Curacao,IvoryCoast,Ecuador
- F: Ned,Japan,EuroPlayoffB(Sweden?),Tunisia | G: Belgium,Egypt,Iran,NZ | H: Spain,CapeVerde,Saudi,Uruguay
- I: France,Senegal,FIFAPlayoff2,Norway | J: Argentina,Algeria,Austria,Jordan
- K: Portugal,FIFAPlayoff1,Uzbekistan,Colombia | L: England,Croatia,Ghana,Panama
- Opener: Mexico vs South Africa June 11 Mexico City. Some q's reference friendlies (Nigeria, Iraq vs WC teams).

## Calibration notes
- "Who scores X goal" → spread among 4-5 star attackers, top ~0.25-0.35.
- F1 2026: lean McLaren (Norris/Piastri) + Verstappen.
- NBA 2025-26: SGA/Jokic top MVP; Celtics strong in East.

## TODO next days
- As events resolve/articles arrive, sharpen the questions with real outcomes.
- Re-verify qid mappings whenever using notes.
