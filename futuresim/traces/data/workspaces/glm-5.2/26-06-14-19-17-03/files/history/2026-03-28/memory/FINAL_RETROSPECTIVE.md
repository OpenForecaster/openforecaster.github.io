# FINAL RETROSPECTIVE — Simulation Complete (330/330 resolved)

## Final Metrics
- **TW-Score: -1725.07** | Accuracy: 8.8% (29/330 top-pick correct) | Mean Brier: -0.032
- This is an adversarial benchmark: ground truths systematically pick SURPRISING/non-obvious answers.

## What WORKED (biggest positives)
1. **Deterministic bracket/standings narrowing** (highest ROI):
   - 703511 DR Congo=Algera (+0.64) — tracked AFCON bracket to confirm R16 matchup.
   - 573851 Senegal CAS appeal (+0.63) — followed Morocco→final→Senegal runner-up.
   - 951896 Alcaraz (+0.52), 180958 Seahawks (+0.55) — narrowed to actual finalists.
   - 4 UCL questions (~+0.5 each) — used league-phase standings to narrow to 2 candidates.
   - 454482 Australia T20 (+0.54) — tracked "Australia lost to Zimbabwe" news.
2. **"Obvious" picks that were right** (kept at ~0.4): FEMA (+0.60), ICE (+0.71), Bondi (+0.64), Hormuz (+0.62), Tehran (+0.54), Iran-WC-withdraw (+0.58), Kurdish-language (+0.59), Novichok→wrong but FEMA-style hits worked.
3. **2nd-pick captures** via modest spreads: Sri Lanka (+0.22), SDF (+0.30), People's Party (+0.33), Bosnia (+0.28), etc.

## What FAILED (biggest lessons)
1. **Overconfidence on "obvious/documented" priors that DIVERGED**: Texas→SC (measles), Novichok→epibatidine, MQ-9→KC-135, Goma→Uvira, Asmara→Meknes (neutral venue!), Milan-Turin→Rome-Naples. Even documented facts diverge in this sim.
2. **Late recalibration couldn't undo early TW losses** (Ethiopia/Somalia held high for days).
3. **Content misalignment bug** (seq→qid mapping): 297818, 830793 got wrong content.
4. **Format errors**: "Labour" instead of a person's name (Hannah Spencer).
5. **Specific scorers/towns/names** were essentially unpredictable (Valverde, Lemina, etc.).

## KEY INSIGHT
The benchmark's ground truth = the "second-most-obvious plausible answer" more often than the obvious one. Best strategy: modest spreads (0.3-0.4 top), 4-5 diverse candidates INCLUDING the non-obvious alternative, and aggressive use of deterministic sports/standings narrowing when available.

## Recurring answer patterns observed
- UAE appeared ~8x (Somalia disputes, mediation, arms sale, missiles, launch area, etc.)
- Qatar appeared ~4x (Carney, Kyiv embassy, Venezuelan oil)
- Iran war scenario: US was perpetrator (school strike), IRIB struck, Khamenei/Larijani killed.
- Syria = Kurdish theme (language, Newroz, PKK).
- Minnesota/Canada for US political surprises.
