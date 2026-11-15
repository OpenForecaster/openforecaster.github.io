# Forecasting Memory — Simulated 2026 World

## Scoring mechanics (important)
- Brier Skill Score = 1 − Σ(p_i − y_i)² summed over ALL outcomes (unlisted true outcome counts as p=0 → −1 term). Range [−1, +1].
- Therefore: submit CALIBRATED probabilities for your top ≤5 outcomes; probability mass on outcomes that might be true is rewarded, and unlisted true answers are heavily penalized. Do NOT use uniform 0.2 spreads on huge fields; put the bulk on the most likely answer(s) but include plausible alternatives.
- TW-score is summed across all questions; every question should have an active prediction every day (0 if absent). Update daily when evidence changes.

## World state as of 2026-06-24 (simulated)
- **Iran war**: US-Israel strikes began Feb 28, 2026; Supreme Leader Ali Khamenei killed (assassinated). His son Mojtaba Khamenei became Supreme Leader (Mar 8). US-Iran MoU signed ~June 17, 60-day negotiation window; 60-day oil waiver (OFAC June 22). Khamenei state funeral July 4–9 (Tehran, Qom, Mashhad).
- **World Cup 2026** (US/Canada/Mexico): group stage ends ~June 27. Round of 32 June 28–July 3; R16 July 4–7; QFs July 9–11 (Boston M97, LA M98, Miami M99, KC M100); SFs Dallas July 14 (M101), Atlanta July 15 (M102); 3rd place Miami July 18; Final MetLife July 19.
  - Group winners/leaders as of June 24: A Mexico (won), B Switzerland (won, Canada 2nd), C Brazil/Morocco (final games June 24-25), D USA (won), E Germany (won), F Netherlands/Japan, G Egypt, H Spain, I France (Norway also 6pts, play June 26), J Argentina (won), K Colombia (Portugal 2nd), L England/Ghana.
  - R16 bracket: M89 = W74(Germany) vs W77(France/Norway) → so France–Germany likely meet in R16 in Philadelphia July 4! M90 = W73(A2/B2) vs W75(F1 vs C2). Boston QF = France/Germany vs Netherlands/Canada. M98 LA QF: Spain/USA/Portugal/England half. M100 KC QF: Argentina vs Colombia/Portugal/Switzerland. SF1 Dallas: France/Germany/Spain/USA; SF2 Atlanta: Argentina/Brazil/England.
  - Betting: France +400/+470 favourite, Spain +450/+500, England +550/+650, Brazil +850.
  - Golden Boot: Messi 5 goals (all-time WC record 18), Mbappe 4.
- **F1 2026**: Kimi Antonelli (Mercedes) championship leader, 5 straight wins, ~156 pts; Mercedes dominant (6 wins); Hamilton won Spain for Ferrari, 2nd in points; Russell 3rd. Austrian GP June 28 (round 8). British GP July 5.
- **Tennis**: Alcaraz out (right wrist tenosynovitis since April 14; withdrew from RG, Queen's, Wimbledon; return earliest North American swing, Canada Masters Aug 2). Sinner world #1, dominant (6 straight Masters). Wimbledon June 29–July 13 (women's final July 11, men's July 12). Sabalenka/Rybakina/Swiatek top women.
- **Cricket**: Women's T20 WC in England; England qualified for semis (beat WI June 24); Australia strong in Group A; final ~June 28 at Lord's. England–India men's T20 series July 2026.
- **MotoGP 2026**: Marc Marquez won last two races; Bezzecchi leads championship (~180 pts).
- **Other**: SK Hynix filed June 24 for $29.4B Nasdaq ADR listing (trading July 10) — would break Alibaba's foreign-issuer US IPO record. SpaceX did an $85.7B IPO in June 2026 (US firm, irrelevant to foreign record). Nvidia ~$5T most valuable. UK: Starmer announced resignation as Labour leader June 22; Burnham won Makerfield by-election; leadership nominations July 9-16. Moldova PM Munteanu still in post June 24 (question premise says he resigns later). Utah = US measles epicenter (482 cases in 2026); no 2026 measles deaths as of June 11. Sinaloa interim governor: Yeraldine Bonilla Valverde (since May 2, indefinite). US-Iran: Rubio reassuring Gulf allies.
- **NBA**: Celtics discussed Jaylen Brown trade to Milwaukee for Giannis (offer rejected; Miami likely got Giannis). LeBron expected to stay Lakers.

## Workflow
- 15 research agents (batches memory/batches/B01..B15.txt) produced JSON in memory/research/agent_results.json; corrections applied → memory/research/final_forecasts.json.
- All 252 forecasts submitted 2026-06-24.
- Helper: `python3 memory/search_corpus.py "kw1" "kw2" --max 20 --ctx 350` searches 3,078 articles dated 2026-06-24.
- Web: `mcp__forecast__search_news` returns historical + current simulated news (great for schedules, standings, official announcements).

## Tomorrow (2026-06-25) checklist
- Check resolutions: Women's T20 WC semifinals/final; World Cup group finales (Groups C, E, F, G, H, I, J, K, L); Austrian GP practice.
- Update: 258607/799550 (T20 WC), World Cup QF/SF/F questions with confirmed bracket, 754639 (UK leader), 76066 (Moldova), 659176 (Russian funeral delegation announcements expected closer to July 4).
- New articles will appear in articles/2026/06/25/.

## Lessons
- Agent research can be wrong on conditional/bracket questions (e.g., initially put USA in Boston QF; correct bracket has France/Germany there). Verify with official schedules.
- Answer-format questions with "if any" allow "None" as a legitimate outcome.
