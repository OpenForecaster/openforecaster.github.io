# Forecasting Strategy & Scoring Insights

## The Metric
- Score per question-day = Brier Skill Score = 1 - Σ_i (p_i - y_i)^2, summed ONLY over submitted outcomes.
- TW-score per question = average daily score ×100, SUMMED across all 330 questions.
- **No active prediction on a day → score 0 for that day.**

## Key strategic implications (derived from proper-scoring analysis)
1. **ALWAYS predict on every question every day.** Zero (no prediction) is the worst outcome; even a low-confidence honest guess has expected score > 0.8.
2. **Report honestly (p_i = true belief).** The rule is proper: honest reporting maximizes expected score. Deviating (over/under-confidence) lowers EV.
3. **Expected score formula for honest report = 1 - C + P**, where C = total true prob mass on my guess set, P = Σ c_i^2.
   - Very uncertain (C small, ~0.1-0.2): expected score ~0.87-0.92 (being wrong with low mass is cheap).
   - Moderately confident (C~0.5): expected ~0.75 — the WORST regime.
   - Very confident (C~0.9): expected ~0.9+.
   - => Research is most valuable where I can move C from ~0.5 to higher, OR confirm a strong favorite.
4. When truly can't guess the specific answer: put modest mass (~0.15-0.25) on best 1-2 guesses. Don't spread thin over many — concentration raises P.

## *** LESSONS CONFIRMED (through Day 18, TW +140.85, 41 resolved) ***
1. **Diversify with low-mass 2nd/3rd/4th guesses (up to 5 outcomes).** Repeatedly hit by hedging: Carrick 0.05, PKK 0.045, UAE 0.15, DHS 0.059, Rubio 0.07, Parchin 0.06, ICE 0.03. The answer is often a non-obvious 2nd-choice. Always include plausible alternatives at low mass.
2. **EXACT NAME SPELLING MATTERS.** Lost Thai PM (had "Natthaphong Ruangchan", truth "Natthaphong Ruengpanyawut") — right person, wrong surname. Verify exact spellings of people/places.
3. **Don't overcommit even on "obvious" answers.** Nipah=West Bengal (not Kerala, my 0.55 → -11.61); Somalia severed w/UAE (not Ethiopia, my 0.42 → -18.38); Deloitte FML=Liverpool (not Man City despite 10-yr reign, my 0.55 → -19.25). Cap single-outcome mass ~0.30-0.35 even when confident; the scenario often subverts the obvious.
4. **Research resolving-soon questions for big +TW wins:** Algeria/DRC AFCON (+45), Nigeria SF (+33), USA FIFA (+32), SDF Syria (+22), Bangladesh Sri Lanka (+24), DHS (+15), UAE (+15), Iran-BRICS (+19). Live sports draws/brackets & current news are gold.
5. **Low-mass-wrong is cheap** (-2 to -5); **high-mass-wrong is costly** (-11 to -18). **right-with-mass is big +** (+15 to +45). Net: honest mass + diversification + research.

## *** CRITICAL SCORING DISCOVERY (Day 8, after first 5 resolutions) ***
The harness's per-question Brier is shown as NEGATIVE (e.g. measles -0.17 = -Σp_i²), and TW-score accumulates as NEGATIVE for wrong predictions; abstain (no prediction) = 0. Implication: **overconfidence when wrong is very costly; Σp² is penalized.** First 5 resolutions: I went 0/5 (all missed: Rosenior, Fedorov, Mint Hill, Liensberger, South Carolina) with masses 0.25-0.45 → TW -36.8.
- **FIX: keep probability mass LOW and honest.** My true belief for speculative answers is ~0.05-0.12/candidate, NOT 0.2-0.45. Recalibrated all 312 active Qs to ~0.45× original (median total mass 0.40→0.18).
- Robust logic: with low hit rate, low mass is near-optimal whether scoring is -Σp² (minimize loss) or 1-Σp² (Brier; low mass when wrong → ~1.0, honest mass proper). Overconfidence is the enemy.
- Keep higher mass ONLY where genuine research signal exists (protected set: 883856 Sarvarov, 459037/703511 AFCON bracket, 946810 Grammy, 951896 AO, 348570/221278/291796/783773/666021/318661/398988/325000).
- Hit rate is ~0% on pure speculation → lower mass = less damage. For future questions, default to 2-3 guesses at 0.04-0.08 each (total ~0.12-0.20).

## Tactical priorities
- Coverage first: get a prediction on ALL 330 questions day 1.
- Prioritize soonest-resolving (Jan) questions for depth, but don't neglect later ones (they have more total days).
- News corpus only goes to ~2025-12-24. Questions describe Jan-Mar 2026 events — many unguessable; rely on current trends + forward-looking articles.
- Submit ≤5 outcomes, no placeholders, probs sum ≤1.0.

## Daily routine
1. Check market.csv for changes / resolutions.
2. Search news for updates on soon-resolving questions.
3. Update predictions where new evidence; ensure full coverage.
4. Log lessons to MEMORY.md.
