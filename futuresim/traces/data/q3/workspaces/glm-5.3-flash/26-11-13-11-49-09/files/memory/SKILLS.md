# FINAL RESULTS (252 questions, all resolved)

- **TW-Score: 1625.25** | Accuracy: 26.6% (67/252 top-pick hits) | Brier: 0.108
- Trajectory: Day-1 baseline + daily refinement near resolution dates compounded to ~1600.

# FINAL LESSONS (ranked by impact)

## 1. Day-1 full coverage is mandatory — but FIRST prediction accuracy dominates TW
TW weights each day held; a wrong day-1 pick accrues negative weight for weeks (e.g. Michigan cyclospora cost -7 TW despite hitting on update; mile WR El Guerrouj cost -40). Invest most day-1 effort in the soonest-resolving questions; accept diffuse priors on far-future ones.

## 2. Update aggressively as events resolve (hits came in waves)
Best days: Alcaraz-return day (+215), UFC 330 day (+104), final-stretch days (+50-60 each). When a tournament/card/election produces facts, immediately re-score every dependent question.

## 3. String exactness matters ("Nuseirat" ≠ "Nuseirat refugee camp"; "Government" ≠ "Federal government"; "Tiangong" ≠ "Tiangong Ultra"; "Drapatiy" ≠ "Drapatyi")
Write outcomes the way a grader would: full names (Rumesh Tharanga Pathirage), simple sector names, complete club/camp names.

## 4. This sim's recurring wildcards (world-specific priors!)
- **Philadelphia 76ers**: destination for NBA stars (Jaylen Brown trade AND LeBron signing!)
- **Trabzonspor / Turkish entities**: Salah (football), Super Cup host, Golden Global Bank, Liverpool shirt sponsor (Turkish Airlines)
- **Florida & Texas**: MAGA-aligned wildcard states (ChatGPT lawsuit, MAGA Inc ads)
- **Saudi clubs / Al-Hilal**: Villa fire-sale (Watkins, Martinelli), Gulf moves
- **Morocco/Malaysia breakout**: WAFCON Cameroon+Malawi final; Malaysian squash sweep at Asiad
- **Pathirage (Sri Lanka)**: world-lead form carried through CWG+Ultimate+Asiad javelin — when someone has a massive lead/streak, prior on the streak continuing
- **Yu Zidi (China)**: teenage swimming prodigy won 200 IM AND 400 IM
- **On (Swiss brand)**: even shoe sponsors can be wildcarded (Mbappé)
- **African/Asian nations join space/Artemis accords** (Ivory Coast 75th)

## 5. Structural priors that worked
- Betting odds (normalized) for pre-event winners (Sinner 0.55→hit; Puripol 0.15; Hamilton KC-pole logic)
- Power-streak continuation: Marc Márquez (Sachsenring master + pole → hit), Scheffler, Antonelli (Monza, Madrid), Norris (Hungary pole→win), Russell (Baku pole→win), Palou (Freedom 250 pole→hit)
- Champions/holders defending at home venues (Qin Haiyang SB, France WC, Dern/Islam UFC, Ri Song Gum, Ledecky-type)
- Successor-mirrors-predecessor (Fleming after McCullum) — worked for others' misses
- Cabinet/coalition "amplia convocatoria" includes ex-rivals (Carlos Espá as Peru FM)
- Fed dissents come in multi-vote sets (Hammack+Kashkari+Logan); Golden Ball goes to winning-team pivot (Rodri)

## 6. Misses that taught the most
- Never-zero-mass credible movers: 76ers (×2!), Trabzonspor, Bengals of the world
- Bracket-venue mapping (Miami vs KC QF) — verify geography against live reporting
- Econ under war/tariffs: Vietnam top deficit (China collapsed); Oil&gas Iran decline
- Asian Games squash/pong/robot/monsoon (Assam) obscure outcomes need at least 1-2% on local breakouts
- Norway king death within 2 days of "very serious" news — royal health questions flip fast

## 7. Workflow that scaled to 252 questions
Compact dump → grep local corpus (free) → 2-search batches on biggest gaps → submit in batches of 4-6 → nightly "resolve tomorrow" scan → morning refinements. Memory files cross-day.
