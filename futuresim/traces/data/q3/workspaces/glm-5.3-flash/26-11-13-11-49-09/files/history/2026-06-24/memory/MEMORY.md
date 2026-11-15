# Forecasting Memory

## Session log
- Day 1 (2026-06-24): Initial pass. Read all 252 questions. Submitted ~85 predictions.

## Key world facts (simulated 2026)
- Iran war ongoing: Khamenei assassinated Feb 28, 2026 by US-Israeli strikes. State funeral July 4-9, 2026 (postponed from March). Succession unresolved in March.
- Maduro removed Jan 2026 (Venezuela); government-opposition talks ongoing.
- Giannis traded to Miami Heat (June 22, 2026).
- LeBron FA 2026: Lakers favorite (not committed), Warriors main threat.
- Moldova PM Munteanu (since Nov 2025) resigned → successor TBD (I guessed Grosu 0.2).
- Kansas Dem Senate primary: Adam Hamilton (pastor) leads (Polymarket 71%). Other names: Patrick Schmidt, Christy Davis, Sharice Davids, Sandy Spidel Neumann.
- TN-9: new redrawn R-friendly district; Brent Taylor (self-funded $1M, Blackburn/Hagerty/Scalise endorsements) vs Todd Warner (MAGA farmer, state rep). Primary Aug 6.
- TN redistricting mid-cycle; Steve Cohen's TN-9 replaced.
- Michigan Senate Dem primary: Abdul El-Sayed vs Mallory McMorrow (both running; El-Sayed progressive/Mamdani-backed).
- NYC: Mamdani mayor; DSA wave vs AIPAC-funded incumbents (Goldman lost primary, Espaillat lost to Avila Chevalier).
- T20 Women's WC (England, Jun 12-Jul 5): Australia dominant (NRR +4.39), England/WI from group B, India/SA from A. Wyatt-Hodge 100.
- WC groups final-ish: A: MEX, KOR; B: SUI (won), CAN; C: BRA, MAR; D: USA, (TUR out); E: GER, CUW(!); F: NED likely (SWE led mid), JPN; G: BEL, EGY (Iran 3rd); H: ESP, CPV(!), KSA, URU; I: FRA, SEN (NOR out); J: ARG, ALG/AUT; K: POR, COD, UZB, COL; L: ENG, CRO.
- Bracket: QF Boston Jul 9 = {GER/FRA} v {CAN/NED/MAR}; LA Jul 10 = ESP v {USA/BEL}; KC Jul 11 = {BRA/SEN} v {MEX/ENG}; Miami Jul 11 = {ARG} v {SUI/POR}. SF1 Jul 14 Dallas, SF2 Jul 15 Atlanta. Final Jul 19 MetLife.
- F1 2026: Antonelli (Mercedes) leads 156, Hamilton 115, Russell 106, Leclerc 75, Norris 73, Piastri 68, Verstappen 55 after 7 races. Zverev won RG 2026; Sinner won AO 2026. Alcaraz OUT of Wimbledon (wrist injury, April).
- Wimbledon Jun 29-Jul 12: Men: Sinner -210 (~55-65% with Alcaraz out), Djokovic +650, Zverev +950, Mensik +2000, Fritz +2200. Women: Sabalenka +300, Rybakina +400, Swiatek +500, Gauff +600, Andreeva +800. Serena Williams wild card (+3500).
- MotoGP 2026: Bezzecchi (Aprilia) 180 leads, Martin 172, Diggia 157, Mar Márquez 140 (3 wins in last 4, 100th win at Balaton Jun 7), Ogura 134, Acosta 132, Bagnaia 127.
- Salah left Liverpool (end of 25-26). Al-Ittihad $200M offer; Saudi likeliest. Benzema left Al-Ittihad Feb; Al-Hilal sold by PIF. Griezmann → Orlando City; De Bruyne → Napoli (2025).
- Open 2026 at Royal Birkdale Jul 16-19: Scheffler +550, McIlroy +650, Fleetwood +1400, Schauffele/Rahm +1800. McIlroy won 2026 Masters (2nd straight); US Open winner? (Scheffler came up short in all 3 majors).
- England Test coach question: McCullum successor TBD.
- Seahawks: Paul Allen estate sale — buyer TBD (Q902592, resolves Jul 11).

## Lessons / strategy
- Predict on day 1 for ALL questions (TW-score weights early days); use ≤5 outcomes, leave ~0.1-0.25 implicit tail mass.
- Conditional "if X leaves" questions: predict top-5 destinations with ~0.5-0.6 total mass, condition partially on the event happening (P(event)~0.5-0.7 for active rumors).
- For void-able questions, total allocated mass ≈ P(condition occurs) × P(outcome|occurs).
- Local articles corpus (articles/YYYY/MM/DD/articles.jsonl) greppable — sources: Hindustan Times, CBS, Straits Times, Al Jazeera, NDTV, Irish Times, Daily Beast, Korea Herald, Khaleej Times...
- search_news max_results ≤7; use to_date=none (capped at today).
