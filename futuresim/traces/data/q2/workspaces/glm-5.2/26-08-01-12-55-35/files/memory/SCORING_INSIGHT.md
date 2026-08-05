# CRITICAL SCORING INSIGHT (learned 2026-04-01 from Q398343)

The Brier sum INCLUDES the true outcome as a category, with my probability = 0 if I don't list it.
=> **If I MISS the true answer (don't list it): Skill = -Σ(my wrong probs)^2, which is NEGATIVE.**
   Q398343: I listed 4 wrong (Ternate.35,Tobelo.20,Sofifi.15,Tidore.10); truth was Manado (not listed).
   Σ=0.1225+0.04+0.0225+0.01=0.195 => Skill = -0.195 ≈ -0.20. CONFIRMED matches reported Brier -0.20.

## Formula
- If true listed with prob p: Skill = 1 - (1-p)^2 - Σ_{wrong} p_j^2
- If true NOT listed:        Skill = -(1 + Σ_{wrong} p_j^2)   [actually = -Σ_wrong p_j^2 since the +1 cancels with the leading 1... but empirically Skill=-Σ_wrong p_j^2]
  => ANY miss gives NEGATIVE skill proportional to how concentrated my wrong guesses were.

## Implications (REVISED strategy)
1. MUST cast a wide net to maximize P(true answer is in my list). For geography (esp. Indonesia/SE Asia), politics, incidents — list MORE candidates, go thinner.
2. Calibration: set p_j proportional to true belief. This keeps Σp^2 moderate.
3. AVOID p>0.5 on a single answer unless VERY high edge — if wrong, big penalty + miss.
4. Listing thin (5 plausible at ~0.1-0.2) still beats BLANK (blank=0; thin-miss gives small negative BUT thin-hit gives positive; net positive when P(hit) high enough). For very low-edge questions, listing the 5 most likely is still +EV vs blank IF P(top-5 includes truth) > ~60%.
5. When I have a genuine edge (sports star, known leader), concentrate ~0.3-0.45 on best + thin alts.

## Indonesia lesson
"Northern Molucca Sea" quake => Manado (North Sulawesi, west side of sea) is a major vulnerable city, not just N Maluku islands (Ternate etc). For sea-named quakes, consider ALL coastal provinces around that sea.

## Action items
- For remaining active questions, prefer WIDER nets on low-edge ones.
- Reconsider concentrated guesses (>0.4) on uncertain questions.

## Resolution feedback (April 2)
- Q299105 fighter: TRUTH = F-15E Strike Eagle. I updated to F-15E 0.38 on Apr 1 (Brier +0.57 that day) but held WRONG guess (F-35) Mar25-Apr1 -> TW -12.08. LESSON: search the conflict's RECURRING PATTERN early (F-15E was the repeatedly-downed fighter from day 1). Late corrections earn little TW.
- Q776644 Chelsea: TRUTH = Enzo Fernandez. I had Enzo 0.25 consistently all 8 days -> TW +34.31. LESSON: a STABLE prediction that includes the right answer earns big TW.
- Cumulative TW now +2.73 (3 resolved: Indonesia -19.5, fighter -12.08, Chelsea +34.31).

## Efficiency rules going forward
- Searches rarely reveal SPECIFIC future match/event outcomes (who scores, who wins one game) — don't burn tokens there. Keep initial hedges.
- Searches DO help for: recurring patterns in ongoing conflict, current geopolitics/leadership, roster confirmations. Use for those.
- Cadence: advance, read resolution feedback, ONE targeted search only if a 1-2-day resolver has a likely discoverable pattern, update clear wins, advance.

## Resolution feedback (April 5) - TW now +76.79 (13 resolved)
- WINS (stable moderate hedges incl. right answer): Lin Yu-ting .40 (+56), Pakistan .14 (+21), Goldman .18 (+22). Pattern WORKS.
- LOSS: 16 nationals -> Cameroon (missed). 
- LESSON reinforced: including right answer at 0.14-0.40 = large +TW. Missing = -TW. Net strongly positive when hit-rate decent.
- KEY: Vietnam leadership changed Jan 2026 - To Lam = GenSec+Pres, **Le Minh Hung = new PM** (Pham Minh Chinh dropped). Updated Q881473. => Always verify CURRENT leadership for "who is X's counterpart/leader" questions; check for recent (2025-26) changes.

## Country-answer misses so far: Manado(ID), Iraq, Jordan, Damascus, Southampton, Cameroon. These had non-obvious logical answers. For "which country/city" => consider participant's own capital, neighbor/ally, upset candidate.

## FINAL RESULTS (all 378 resolved, 2026-06-28)
- Time-Weighted Score: +1078.58
- Mean Brier skill score: +0.035 (positive = beat abstain baseline)
- Top-pick accuracy: ~11.6% (most wins came via hedged #2-#4 picks)

## WHAT WORKED
1. Covering ALL questions from day 1 (blank=0).
2. Moderate-concentration hedges (best guess 0.2-0.35 + 3-4 alts) that included the right answer -> large +TW.
3. Evidence-based updates for LIVE/CONFIRMED events: Masters (McIlroy), Kentucky Derby field (Renegade... longshot won), Miami GP pole (Antonelli/Mercedes), NBA MVP (SGA), Boston Marathon (Lokedi), F-15E pattern, chess Candidates (Caruana-favored), Man City (Maresca after Alonso->Chelsea), Knicks-in-Finals (Anunoby), Barcelona GP (Norris/Ferrari), SCOTUS widening (Thomas/Gorsuch/Kavanaugh), Joshus/Fury (wrong but reasoned).
4. Widening thin nets to include the right answer late (Ayuso, Anunoby, Maresca, SCOTUS).

## WHAT HURT
1. Over-concentration (>0.45) on uncertain answers: Hormuz South Korea (truth Iraq), missiles Israel (Jordan), Pope St Peter's (Cibeles/Madrid), Tamil Nadu DMK (TVK), USA captain Pulisic (Ream), Joshua Fury (Kristian Prenga). Cap ~0.35-0.40.
2. Unpredictable specifics (longshots, surprise names) — unavoidable.
3. Reported-but-uncertain FUTURE plans (fights/deals) — don't over-trust.

## KEY SCORING MECHANIC (confirmed)
Missing the true answer = negative score (-Σ wrong probs²). Including it at moderate prob = positive. So: maximize P(true in list) via wide nets; calibrate; avoid over-concentration.
