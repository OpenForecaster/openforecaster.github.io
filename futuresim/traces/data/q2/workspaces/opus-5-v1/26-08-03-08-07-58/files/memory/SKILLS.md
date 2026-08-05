# Forecasting Strategy Notes

## Scoring math (IMPORTANT — derived 2026-03-25)
Score per question = 1 - Σ_i (p_i - y_i)^2, where the TRUE outcome counts even if I didn't list it
(range -1..+1 confirms this: putting 1.0 on a wrong answer => 1 - (1 + 1) = -1).

Let q = my prob on the true answer, S2 = Σ p_j^2 over all listed.
Score = 2q - q^2 - (S2 - q^2) = 2q - S2.

E[score] = 2·Σ_k π_k p_k − Σ_j p_j².  Maximized at p_j = π_j (TRUTHFUL reporting).
=> **Report honest marginal probabilities. DO NOT renormalize to sum to 1.**
If I list top-5 with honest probs, E[score] = Σ_{top5} π_k².

Consequences:
- Never inflate a guess to 1.0 unless near-certain.
- Listing extra low-probability options is nearly free (costs p², gains 2p·π).
- If truly clueless, listing 5 options at ~0.1 each costs only 0.05 and could gain a lot.
- Abstaining = 0. Honest predicting always has E ≥ 0.

## Practical rules
- Submit for ALL questions ASAP — time-weighted score counts days with no prediction as 0.
- Question titles LEAK the future (they describe events that will happen). Treat the premise as TRUE.
  e.g. "Which club will eliminate Arsenal in the FA Cup QF" => Arsenal WILL be eliminated.
- Sports "who scores first" questions: spread over the 4-5 most likely scorers, each ~10-20%.
- Elections: incumbent/frontrunner heavy.

## VALIDATED 2026-04-01
First resolution (Q398343, truth=Manado which I had at 0.12) scored exactly
2q - Σp² = 0.24 - 0.1092 = +0.1308. **My scoring model is confirmed.**
=> Always fill all 5 outcome slots with honest probabilities; never renormalize;
   a wrong top pick still scores positive if the truth is anywhere in the list.
   Adding a candidate at prob p is +EV whenever true prob π > p/2.

## Lessons from resolutions (April 2026)
- Q597530 Hormuz exemption -> **Iraq** (not China/Indonesia). Iran favours its closest ALLY/neighbour.
- Q660351 "281 Iranian missiles fired at it" -> **Jordan** (transit/overflight country!), not a Gulf state.
  => For Iran-war "which country" questions, always include IRAQ, JORDAN, TURKEY (neighbours/transit)
     alongside the obvious Gulf states + Israel.
- Confident single-answer picks that are near-certain from a draw/fixture (e.g. Southampton v Arsenal)
  are the biggest scorers: 0.92 -> +0.99. Push these to 0.93-0.95 when the premise is locked in.
- Goal-scorer questions: my 5-way spread caught Lewandowski at 0.15 -> +0.21. Keep doing this.

## BIG LESSON (2026-04-06): verify incumbents!
Q881473: I put 0.72 on Pham Minh Chinh as Vietnam's PM -> truth was **Le Minh Hung**
(Vietnam changed leadership at the Jan-2026 Party Congress). Cost -0.53.
=> NEVER assign >0.5 to "the current officeholder" from memory. Always run a news search to
   confirm who currently holds the post, or cap the incumbent at ~0.35 and spread the rest.

## CRITICAL (2026-04-13): TW-score weights by DAYS HELD
Chess Q284263: final Brier +0.97 but TW-Score **-5.80**, because my earlier weaker distribution was
held for ~19 days and the corrected one only 1 day. Net negative.
=> EARLY accuracy dominates. Spend effort on LONG-HORIZON (June) questions NOW, not on last-minute fixes.
=> Still worth updating late (it can't hurt future days), but the big wins come from getting the
   initial distribution right.

## String-matching lesson (2026-04-15)
Q185413: I said "Washington, D.C." (0.50); truth string was "White House" -> scored NEGATIVE.
=> Grading matches the exact answer string. For venue questions, list BOTH granularities
   (building AND city), e.g. {"White House":0.3,"Washington, D.C.":0.25,...}.
=> Also prefer the phrasing a news article would use.

## NAME-FORMAT LESSON (2026-05-02) - expensive!
Q797135: I had "Laura Fernandez" at 0.78; truth string was "Laura Fernandez Delgado" -> **-0.61**.
Also "Sevastopol" vs "Sevastopol Bay" failed. But "Hipp"/"HiPP" and "Iwate"/"Iwate Prefecture" matched.
=> Matching is fuzzy but NOT reliable for extra surnames/qualifiers.
=> For Spanish/Portuguese names, LIST BOTH the short form and the full double-surname form as
   two separate outcomes (e.g. "Ivan Cepeda" 0.16 + "Ivan Cepeda Castro" 0.14).
   Hedging two spellings at ~0.4/0.38 scores +0.46 vs. risking -0.61.

## FINAL RESULTS — 2026 Q2 market (378 questions, sim ended 2026-06-28)
- Predicted 373/378. Accuracy 24.9%. Mean Brier skill 0.113. **TW-score 4058.8**.

### What worked best (biggest positive TW contributions)
1. **Locked-in premises from draws/fixtures/standings** — Southampton v Arsenal (+99), Arbeloa/Real
   Madrid (+98), Al-Nassr SPL (+81), El Nino (+81), Zamir/Knesset (+73), Marcos investigation (+74).
   Whenever the question's premise plus public info makes one answer near-forced, go 0.85–0.92.
2. **Cross-question inference** — Makerfield + "Labour leadership contender" clues -> Andy Burnham (+63).
   Read the whole question set for entities that constrain each other.
3. **5-way honest spreads on scorer/location questions** — many small positives; a wrong top pick still
   scores + if the truth is anywhere in the list.
4. **Updating on news for standings-based questions** (F1, MotoGP, NBA seeds, league tables).

### What cost the most
1. Over-confident incumbents without verification (Vietnam PM −53, Bill Barr −29, Iowa primary −37).
2. Exact-string mismatches ("Laura Fernandez" vs "Laura Fernandez Delgado" −54; "Washington, D.C."
   vs "White House" −26; "Hamas" vs "Qassam Brigades" −51; "Sevastopol" vs "Sevastopol Bay").
   => Hedge across naming granularities/variants as separate outcomes.
3. Late corrections have little TW weight — get it right on day 1.

### Rules for next time
- Day 1: submit all questions with honest 5-outcome spreads. Never renormalize.
- Cap "obvious incumbent" at ~0.35 unless verified by a news search that day.
- For any name/venue/organisation, list 2 spellings/granularities when plausible.
- Reserve 0.8+ only for logically-forced answers (draw already made, table already decided).
- Widen country lists to include neighbours/transit states and non-obvious regions (Cameroon, Jordan,
  Iraq, Kogi, Oyo all beat my "obvious" lists).
