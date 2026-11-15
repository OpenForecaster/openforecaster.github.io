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

## Day 1 submission summary (all 252 covered)
- Strongest conviction: Sinner Wimbledon 0.55 (Alcaraz out); Ledecky 800 free 0.50; Qin Haiyang 200br 0.45; Mbappe Nike sponsor 0.75; Alibaba IPO record 0.82; Nvidia most valuable 0.55; Hamilton 2nd in champs 0.48; Akhannouch Morocco PM 0.42; Milstein? no. others: China trade deficit 0.68; Alb El-Sayed MI 0.42/0.38 split.
- Key uncertainty flagged: Moldova successor, UK leader resignation, Donnarumma defendants, Algeria/Austria J-group order, proxy designation, PaK districts (guess), Puyo Puyo players (weak), Q199448 bracket guess.

## Day 2 (2026-06-25) notes
- WC groups updated: A final: MEX 9, RSA 4 (2nd!), KOR 3, CZE 1. C final: BRA 7 (+6), MAR 7 (+3), SCO 3rd. B final: SUI 7, CAN 4 (+5, 2nd), BIH 4 (-1, 3rd — strong best-3rd candidate for M81 vs USA).
- Group E: GER clinched; CIV runner-up likely. F: NED/JPN 4pts, SWE 3. G final Jun 26: EGY-Iran, NZ-BEL. H final Jun 26: URU-Spain, CPV-KSA. I final Jun 26: NOR-FRA (draw gives FRA top), SEN-IRQ. J/K/L finals Jun 27.
- Bracket after updates: M73 RSA v CAN (CAN ~65%); M89 FRA/GER; M90 CAN/NED/MOR; M91 BRA; M92 MEX/ENG; M93 ESP; M94 USA/BEL; M95 ARG; M96 SUI/POR.
- QFs: Boston= FRA/GER v CAN/NED/MOR (FRA 0.24, GER 0.21); KC= BRA v ENG (BRA 0.34, ENG 0.29); LA= ESP v USA/BEL; MIA= ARG v POR/SUI.
- T20: India beat BAN (Shafali 53*); IND/AUS/ENG/WI still semis favorites.
- England-India T20I series Jul 1-11 (5 matches, Durham/MANC/Trent Bridge/Bristol/Southampton). ENG squad: Brook (c), Buttler, Salt, Bethell, Archer, Rashid, Coles. IND world #1 T20. Updated IND 0.54/ENG 0.42.
- Pakistan tour ENG: 3 Tests Aug 19-23 (Headingley), Aug 27-31 (Lord's), Sep 9-13 (Edgbaston) → Q971366 = 3rd Test Edgbaston Sep 9.
- Wimbledon: Sinner dominant 2026 (won first 5 Masters 1000s) but lost early RG to J.M. Cerúndolo; Mouratoglou calls him huge favourite; Zverev RG champ (grass unproven). Sinner 0.55 stands.
- Bagnaia → Aprilia 2027+ (4-year deal). Not relevant to 2026 races.
- Salah/Moldova: no news yet.

## Day 3 (2026-06-26) notes
- WIMBLEDON DRAW: Men top half: Sinner v Medvedev QF, FAA v Djokovic QF, SF Sinner v Djok/FAA. Bottom: Zverev v Fritz QF (Fritz won last 7 H2H incl Halle SF; Draper R1 for Fritz), Shelton v de Minaur QF; Tiafoe won Halle. Sinner lost RG 2R (physical). Serena v Maya Joint R1.
- Women QFs: Sabalenka-Andreeva, Pegula-Gauff, Svitolina-Swiatek, Anisimova-Rybakina. Sabalenka lost RG QF; Berlin SF: Pegula BEAT Sabalenka. Rybakina won AO 2026. Swiatek 0 grass wins, lost Berlin opener to Navarro. Serena in Swiatek's Q3.
- Updated: Sinner 0.48/0.28-first-finalist; women: Rybakina 0.22, Sabalenka 0.22, Pegula 0.13, Swiatek 0.12, Gauff 0.10.
- IRAN DE-ESCALATION: US-Iran MoU signed; Hormuz reopening (Aramco Ras Tanura resumed after 4-month halt; Korean vessels exiting); Trump unfreezing Iranian assets for farm goods; Israel-Lebanon talks extended. Adjusted down: Q339902 strikes (0.46 total), Q246629 embargo (0.61), Q605397 338 (China 0.35).
- Group E final: Germany 1-0 Ecuador (GER top 9? actually GER 9pts w/ 3 wins: 7-1,2-1,1-0); THREE through from B (SUI,CAN,BIH), E (GER,CIV,ECU), F (NED 7, JPN 5, SWE 4). USA "reality check" (lost to Turkey but USA top D). Norway secured qualification in I (in-form; SEN?).
- Venezuela: twin earthquakes, hundreds trapped (Jun 25-26) — may affect govt-opposition talks timeline (Q882554).
- Egypt-Iran tonight decides G; Uruguay-Spain, CPV-KSA tonight decide H; J/K/L finals Jun 27.

## Day 4 (2026-06-27) notes
- Group I FINAL: FRA 9 (Dembélé hat-trick 4-1 v NOR), NORWAY 6 (2nd! beat SEN 3-2, IRQ 4-1), SEN 3 (+4 GD, 3rd, likely best-3rd), IRQ 0. Norway → M78 v CIV.
- Group G final: BEL 5-1 NZ → Belgium tops (5pts, +6); EGY 2nd (1-1 v Iran); IRN 3rd (3pts, 0GD); NZ out.
- Group H final: ESP 1-0 URU (Muslera howler, Baena goal) → Spain top (7); CPV 2nd (3 draws, 3pts) → meets ARG (M86)! KSA 3rd 2pts. URU out (highest-ranked out).
- Group L: ENG top (7: 4-2 CRO, 0-0 GHA, 2-0 PAN — Bellingham+Kane). GHA 2nd likely (4pts); CRO must win v GHA tonight.
- Group K tonight: COL v POR (COL 6pts leads; POR 4). COD v UZB. Portugal likely RU unless loses.
- Spain → M84 v ALG/AUT (runner-up J) in LA Jul 2. Argentina → M86 v CPV.
- T20: Ireland shocked WI (first ever WT20 win, 22nd attempt; Orla Prendergast 63*) — WI unlikely to advance. ENG B1 (4-0?), likely ENG v IND SF2; AUS v B2 SF1. AUS still final favorite.
- India men reigning T20 WC champs; Abhishek Sharma opener; Vaibhav Sooryavanshi teen sensation (debut watch).
- Vozinha: 40yo Cape Verde GK hero (held Spain 0-0). Q617889 destination still open.

## Day 5 (2026-06-28) notes — FULL BRACKET SET
- Group J: ARG 9 top (Messi 6 goals this WC, 19 career). AUT-ALG 3-3 → BOTH through; ALG 3rd (4pts), AUT runner-up → M84: Spain v Austria (LA Jul 2).
- Group K: COL 7 top (0-0 POR), POR 5 RU, COD 3rd (4pts, beat UZB 3-1). M83: POR v CRO (Toronto Jul 2).
- Group L: ENG 7, CRO 6 RU (beat PAN + GHA 2-1), GHA 4 3rd → M87: Colombia v Ghana (Vancouver Jul 3). M80: England v DR Congo (Atlanta Jul 1).
- R32 pairings: M73 RSA-CAN; M74 GER-3rd(Sweden?); M75 NED-MAR; M76 BRA-JPN; M77 FRA-3rd; M78 CIV-NOR; M79 MEX-3rd(Senegal/Ecuador?); M80 ENG-COD; M81 USA-3rd(ALG/BIH?); M82 BEL-3rd; M83 POR-CRO; M84 ESP-AUT; M85 SUI-3rd; M86 ARG-CPV; M87 COL-GHA; M88 AUS-EGY.
- QF distributions updated: Boston FRA .25/GER .16; KC BRA .32/ENG .27; LA ESP .36/USA .13/BEL .11/POR .10; MIA ARG .24/SUI .10/COL .10.
- F1: Russell WON Austrian GP (2nd win of season; career 7th; Mercedes 7 wins in 8 rounds!). Standings: Antonelli 171, Russell 131, Hamilton ~121 (5th at Austrian GP). Updated Q556116: Russell 0.50 2nd-in-standings; Q747581 British GP: Antonelli 0.28, Russell 0.20, Hamilton 0.14, Verstappen 0.09.
- Scotland coach Steve Clarke RESIGNED after group-stage exit (relevance: minor).
- "door open to Messi vs Ronaldo final" narrative (ARG M86, POR M83→M93 path).

## Day 6 (2026-06-29) notes
- Canada beat RSA 1-0 → first R16 team (Marsch). M90 Jul 4 Houston: CAN v NED/MAR winner.
- Ja Morant TRADED to Portland (Blazers) — complicates Jaylen Brown-to-POR. Updated Q344207: HOU .22, ATL .18, POR .08. Resolution Jul 1!
- Wimbledon Day 1: Sinner & Sabalenka won R1 ("answered doubters").
- Gaza "ceasefire" exists (fragile) — strikes continue but fewer.
- Tonight Jun 29: NED-MAR (Monterrey), BRA-JPN (Houston).

## Day 7 (2026-06-30) notes
- R32 Jun 29 results: PAR beat GER 4-3 pens (Enciso 42', Havertz 54', VAR overturned Tah header); MAR beat NED 3-2 pens (Gakpo 72', Diop 91', Bounou save, Saibari winner); BRA 2-1 JPN (Sano 29', Casemiro 56', Martinelli 95'); NOR beat CIV (M78) → BRA v NOR M91 Jul 5 MetLife.
- M77 Jun 30: FRA v SWE. W89 = FRA/PAR. M90 = CAN v MAR (Jul 4 Houston).
- Boston QF updated: FRA .30, PAR .14, CAN .12, MAR .11. KC: BRA .36, ENG .28, MEX .13.
- Tomorrow Jul 1 resolutions: Q344207 Brown (no agreement news yet), Q619176 PFA month (keep Aug/Sep), Q659176 Kremlin funeral attendee (no news; Medvedev .30/Lavrov .27 keep).
- France-Sweden tonight; also USA? M81 Jul 1 (USA v best-3rd = ?), M80 ENG-COD Jul 1, M82 BEL-3rd Jul 1, M79 MEX-3rd Jul 1.

## Day 8 (2026-07-01) notes + SCOREBOARD
- RESOLVED Jul 1: Brown→Philadelphia 76ers (MISS — not in dist; lesson: cast wider net incl. draft-night rebuild partners). PFA→September (my #2, 0.25). Kremlin→Medvedev ✓ (top pick, Brier +0.40).
- Cumulative TW: 58.34 (×100 scale of brier skill). Accuracy 0.4% (1/252).
- France 3-0 Sweden (Mbappé 2 → 6 goals, ties Messi for lead; Barcola 1). M89: FRA v PAR Jul 4 Philly. Mbappé now tied with Messi for Golden Boot → both 0.16-0.17.
- T20: SF2 Jul 2 = ENG v SOUTH AFRICA (India OUT — SA 2nd in Group A!). Updated: AUS .44, ENG .18, SA .16; PoT: Mooney .20, Kapp .14, Sciver-Brunt .10.
- Cyclospora: MICHIGAN sudden outbreak Jun 22-30 (investigated) → updated Michigan .30, Texas .28, Florida .20.
- England-India men's T20I series started Jul 1 (Brook leads).
- Wimbledon R2 ongoing: Zverev v Royer, Swiatek v Pliskova, Anisimova v Kenin.

## Day 9 (2026-07-02) notes
- Spain 3-0 AUT (Oyarzabal x2) → 34 games unbeaten, M93 v POR/CRO Jul 6 Dallas.
- ENG 2-1 COD (Kane 2 late) — labored, Bellingham booked. USA 2-0 BIH (ten men, Freese saves). BEL stunned SEN in ET (M82) → M94: USA v BEL Seattle Jul 6.
- Senegal → M82 (lost to BEL). Mexico likely won M79 (3rd = Ecuador/Saudi?) → M92: ENG v MEX Jul 5 Azteca.
- R16 schedule: M89 FRA-PAR Jul 4 Philly; M90 CAN-MAR Jul 4 Houston; M91 BRA-NOR Jul 5 MetLife; M92 ENG-MEX Jul 5 Azteca; M93 POR/CRO-ESP Jul 6 Dallas; M94 USA-BEL Jul 6 Seattle; M95 ARG-CPV/AUS-EGY winner Jul 7 Atlanta; M96 SUI/ALG-COL/GHA Jul 7 Vancouver.
- QFs updated: Boston FRA .33/PAR .15; KC BRA .38/ENG .28/MEX .12; SF1 FRA .20/ESP .17; SF2 BRA .20/ARG .15/ENG .14; Winner ESP .16/FRA .15/BRA .12/ARG .12/ENG .10.
- Wimbledon R2: Sinner gritty 7-6 7-6 v Borges; Sabalenka through; Swiatek demolished Pliskova.
- India men won T20 WC ~Feb 2026 (Samson 97*/89s referenced).

## Day 10 (2026-07-03) notes
- POR 2-1 CRO (Ronaldo pen 68, Ramos 90+4) → M93: ESP v POR Jul 6. SUI 2-0 ALG (Embolo, Ndoye) → M96 v COL/GHA. EGY beat AUS 4-2 pens (Ashour 13', Hany OG) → M95: ARG v EGY Jul 7 Atlanta.
- T20 FINAL set: England v Australia at Lord's Jul 5 (ENG beat SA by 40; Sciver-Brunt 75(47), Knight 58). Updated: AUS .56/ENG .40; PoT: Mooney .24, Sciver-Brunt .22, Healy .12.
- Updated SF2: BRA .22/ARG .17/ENG .13; Winner: ESP .17/FRA .15/BRA .13/ARG .12/ENG .10.
- Tomorrow resolves: Q177324 Trey Alexander (no news — may void), Q633052 cyclospora (Michigan .30/Texas .28/Florida .20 stand).
- Jul 4: M89 FRA-PAR, M90 CAN-MAR. Jul 5: BRA-NOR, ENG-MEX + T20 final + F1 British GP.

## Day 11 (2026-07-04) notes + SCOREBOARD
- RESOLVED Jul 4: Trey Alexander→Utah Jazz (MISS; had DEN .15 — two-way signings unpredictable, spread wider). Cyclospora→Michigan ✓ top pick (+0.39 brier) but TW -7.15 (early Texas-heavy days dragged; lesson: FIRST prediction accuracy matters most).
- Cumulative TW: 46.96 (5 resolved: Medvedev ✓, September ✓2nd, Brown ✗, Alexander ✗, Michigan ✓).
- MAR 3-0 CAN (Ounahi x2, Rahimi; Saibari injured — Bayern-bound) → Boston QF = MAR v FRA/PAR. Updated Q199448: FRA .46/MAR .42/PAR .09.
- Wimbledon: EALA stunned Swiatek 7-6(9) 6-2 (R3, first Filipino in Wimbledon L16). Updated women: Rybakina .24, Sabalenka .26, Pegula .12, Gauff .10, Andreeva .08.
- British GP: Antonelli POLE + sprint win; Russell crashed in quali, P4. Updated Q747581: Antonelli .42, Hamilton .18, Russell .10.
- Tonight Jul 4: FRA-PAR; T20 final (AUS v ENG) tonight at Lord's; Jul 5: BRA-NOR, ENG-MEX, British GP race.

## Day 12 (2026-07-05) notes + SCOREBOARD
- RESOLVED Jul 5: T20→Australia ✓ (0.56, +0.65); PoT→Mooney ✓ (0.24, +0.34); British GP→CHARLES LECLERC ✗ (-0.23) — lesson: when quali hints say rival is fast ("too fast for Ferrari"), price them in!
- Cumulative TW: 124.79 (8 resolved; 4 top-pick hits). Accuracy 1.6%.
- R16: NOR 2-1 BRA!!! (Haaland 79' 90', Neymar 90+10 pen; Nyland heroics) — Brazil OUT. FRA 1-0 PAR (Mbappé 70' pen → 7 goals, WC lead).
- Boston QF = FRA v MAR (Jul 9 9pm): FRA .60/MAR .37. KC QF = NOR v ENG/MEX: ENG .42/NOR .20/MEX .14.
- Wildfires: Portugal (massive 3-day blaze, Spain/Italy sending help) + Greece (Thessaloniki) burning — watch Q149811 (national emergency by Jul 25).
- Tonight Jul 5-6: ENG-MEX (altitude), ESP-POR Mon 8pm, USA-BEL Tue 1am (Jul 7), ARG-EGY Tue, COL-GHA done? (M87 Jul 3: check).
- Wimbledon R4: Gauff beat Bencic → first Wimbledon QF; Eala v Paolini; Fritz v Bublik.

## Day 13 (2026-07-06) notes
- ENG 3-2 MEX (Bellingham, Kane; England down a man in 2nd half!) → KC QF = ENG v NOR (updated ENG .58/NOR .30). Balogun red-card ban reprieved after Trump intervention (FIFA uproar).
- Wildfires rage across southern Europe (Portugal massive, Greece Thessaloniki, French Pyrenees near TdF; record heatwave) — Q149811 emergency watch.
- Mbappé 7 goals (Golden Boot lead); Messi 6. Ronaldo confirmed last WC before Spain clash.
- Resolve tomorrow: Q263626 (keep China .68), Q754639 (no UK news; keep).

## Day 14 (2026-07-07) notes + SCOREBOARD
- RESOLVED Jul 7: May trade deficit→VIETNAM (✗ China .68 — tariff world shifted trade; lesson: war/tariff scenarios change econ baselines). UK leader→FARAGE ✓ top pick (+0.27).
- Cumulative TW: 120.41 (10 resolved, 5 top-pick hits). Accuracy 2.0%.
- R16: ESP 1-0 POR (Merino 91'); BEL 4-1 USA (CDK x2, Balogun played w/ suspended ban); ARG 3-2 EGY (2-0 down, Messi missed pen then late equalizer — epic); COL 1-0 GHA.
- QFs: LA = ESP v BEL Jul 10; MIA = ARG v SUI/COL Jul 11; KC = ENG v NOR Jul 11?; Boston = FRA v MAR Jul 9. M96 SUI v COL Jul 7.
- Wimbledon: Sinner into SF (beat Struff — so Medvedev out earlier); Zverev first Wimbledon QF (beat Lehecka after curfew); Gauff SF (beat Pegula 6-4 6-3 6-3); Osaka out.
- MOLDOVA: Sandu named Eugen OSMOCESCU acting PM — updated Q76066 Osmochescu .30 (acting→elected plausible).
- Dugan sentencing Jul 8 (Probation .55 stands). Tomorrow resolves: Q213487, Q76066.

## Day 15 (2026-07-08) notes + SCOREBOARD
- RESOLVED Jul 8: Dugan→Monetary fine (✗ had Fine #2 .12, Probation .55 top). Moldova→Vasile Tofan (✗ unknown PAS figure).
- Cumulative TW: 99.17 (12 resolved, 5 hits). TW dipped from early-day wrong predictions — top-pick accuracy is critical.
- England 201 beat India, 125-run humiliation (India's heaviest T20I defeat) → likely 3-0. Updated Q562262: ENG .92/IND .06. LESSON: don't flip to away "world #1" over home form + squad news.
- Wimbledon SFs set: Sinner v Djokovic (5h QF vs FAA, calf injury); Zverev v British wildcard Arthur FERY (fairytale SF). Updated: title Sinner .50/Zverev .24; first-finalist Sinner .34/Zverev .30.
- Tonight Jul 9: Boston QF FRA v MAR (Q199448 resolves). Tomorrow resolves: Q107473 (no news; keep UCL .15), Q279946 (Alibaba .82).

## Day 16 (2026-07-09) notes + SCOREBOARD
- RESOLVED Jul 9: KCL won UK univ question (✗). FRANCE beat Morocco ✓✓ (0.60, +0.70). IPO record→SK HYNIX (✗✗ — Korean chipmaker did record US IPO in AI-boom world; watch mega chip offerings!). England-India series→England ✓✓ (0.92, +0.99).
- Cumulative TW: 114.98 (16 resolved, 7 top-pick hits). Accuracy 2.8%.
- Super Typhoon Bavi (~200km/h, strongest since 2024): hit Guam, now SE of Taiwan → mainland landfall likely FUJIAN (updated .42/.38). Maysak flooding killed 39 in S. China (Guangxi); Korean Chungcheong flooding.
- Wimbledon SFs: Sinner v Djokovic; Zverev v wildcard Fery (Fery destroyed Cobolli 6-4 7-6 6-0; world #114). Women: Kostyuk v Noskova SF! (upsets: Rybakina/Anisimova or Svitolina out; Eala/Paolini out?).
- Tonight Jul 9-10: men's SFs → Q985440 resolves tomorrow (Sinner .30/Zverev .32/Djokovic .10/Fery .05).
- Q446236 (Bavi evacuations) resolves tomorrow — Fujian .38.

## Day 17 (2026-07-10) notes + SCOREBOARD
- RESOLVED Jul 10: Bavi evacuations→ZHEJIANG (✗ Fujian .38; Zhejiang .10; TW +9.05 net positive). First Wimbledon finalist→ZVEREV ✓✓ (0.32, +0.43).
- Cumulative TW: 134.45 (18 resolved, 9 top-pick hits). Accuracy 3.2%.
- Wimbledon: Sinner 6-4 6-4 6-4 Djokovic (clinical); Zverev ended Fery-tale → FINAL: SINNER v ZVEREV (updated .62/.33). Women's final: ALL-CZECH Muchova v Noskova!! (Muchova won one SF; Noskova beat Kostyuk) — resubmitted Muchova .52/Noskova .48. (Sabalenka/Gauff/Rybakina all OUT — huge draw chaos; lesson: in wide-open slams, keep QF losers in distribution!)
- Bavi: pounding Taiwan Fri/Sat then "smashing into China" → landfall Sat Jul 11. Zhejiang evacuated most → landfall likely ZHEJIANG (updated .40/Fujian .32).
- France cruised past Morocco → SF1 Dallas Jul 14: FRA v ESP/BEL. LA QF ESP-BEL Jul 10 tonight. England-Norway Jul 11 night US. Miami QF ARG v SUI/COL Jul 11.
- Tomorrow resolves: Q457239 (ENG .58/NOR .30 — game may be after resolution; keep), Q66613 (Zhejiang .40), Q846335 (Muchova .52), Q902592 (Seahawks; no news — keep).

## Day 18 (2026-07-11) notes + SCOREBOARD
- RESOLVED Jul 11: KC QF→ARGENTINA (✗✗ my KC=England mapping was WRONG — England-Norway was the MIAMI QF! KC = ARG v SWITZERLAND (SUI beat COL). Lesson: verify venue-team mapping against live articles before final QF predictions). Bavi→Zhejiang ✓✓ (0.40, +0.52). Wimbledon women→NOSKOVA ✓ (0.48, +0.46). Seahawks→Khosla (✗ #3 @0.14).
- Cumulative TW: 90.98 (22 resolved, 11 hits). TW dipped — Argentina zero-mass miss.
- Spain beat Belgium (Yamal MOTM, 0 tournament goals) → SF1 Dallas Jul 14: FRA v ESP (updated ESP .52/FRA .45). SF2 Atlanta Jul 15: ARG v ENG/NOR winner (updated ARG .40/ENG .34/NOR .14). Miami QF = ENG v NOR (tonight Jul 11).
- MotoGP: Martin now championship LEADER (Márquez -32). German GP: Márquez POLE (lap record) + sprint win, 12x Sachsenring winner, Bezzecchi crashed again → updated Márquez .55.
- Wembanyama: 5yr/$252M Spurs. UFC 329: McGregor v Holloway at 170.5 (mid-July).
- TdF: heatwave; Evenepoel 3rd overall (-23s); Pogačar won stage 3; Del Toro won stage 2 & may lead. Stage 11 ~Jul 14 (resolves Jul 15) — Pogačar .24 stands.
- Tomorrow Jul 12: Wimbledon men's final (Sinner .62/Zverev .33 — final TODAY 11am; check result), MotoGP German GP (Márquez .55).

## Day 19 (2026-07-12) notes + SCOREBOARD
- RESOLVED Jul 12: Wimbledon men→SINNER ✓✓ (0.62, +0.75). MotoGP German→MÁRQUEZ ✓✓ (0.55, +0.77).
- Cumulative TW: 211.98 (24 resolved, 13 hits). Accuracy 4.4%.
- England 2-1 Norway (Bellingham OG-fortune? + 93' winner; 6 goals = Kane). SF2 = ENG v ARG Jul 15. Goals: Mbappé 8, Messi 8, Haaland 7 (OUT), Bellingham 6, Kane 6. Updated GB: Mbappé .28/Messi .26; Golden Ball: Mbappé .18/Yamal .14/Messi .15.
- Lindsey Graham DIED (sudden illness). Skubal 5-5 3.06, Tigers losing → Phillies .20 lead for Skubal sweepstakes (deadline Jul 31).
- TdF: stage 9 shortened (heatwave), van der Poel won; Pogačar vocal about heat. Stage 11 ~Jul 14: Pogačar .26/vdPoel .10.

## Day 20 (2026-07-13) notes + SCOREBOARD
- RESOLVED Jul 13: TN-9 Trump endorsement→Brent Taylor ✓✓ (0.45, +0.62).
- Cumulative TW: 273.89 (25 resolved, 14 hits). Accuracy 4.8%.
- SF1 FRA-ESP Tue Jul 14 8pm (French favourites per media; Spain unbeaten) — resolves tomorrow. SF2 ENG-ARG Wed Jul 15.
- Xi Jinping VISITED PYONGYANG IN JUNE; NK PM Pak Song Ho visited China (met Xi/Li Qiang, treaty anniversary). Updated Q666563: Zhao Leji .30/Wang Yi .25.
- MLB ASG at Citizens Bank Park; McGonigle (DET rookie) debut; Rangers lead AL West.
- Tomorrow resolves: Q607314 (ASG MVP — keep), Q666563 (Zhao Leji .30), Q803035 (moratorium — Dec 31 window, keep), Q935518 (ESP .50/FRA .46).

## Day 21 (2026-07-14) notes + SCOREBOARD
- RESOLVED Jul 14: ASG MVP→Cody Bellinger (✗). Pyongyang→Wang Huning (✗ — CPPCC chairman, classic Jo Yong Won counterpart; include CPPCC/NPC next time). Data center moratorium→NEW YORK ✓✓ (0.15, +0.18). SF1→SPAIN ✓✓ (0.50, +0.54).
- Cumulative TW: 302.95 (29 resolved, 16 hits). Accuracy 5.2%.
- WORLD CUP FINAL: SPAIN v (ENG/ARG) Jul 19. SF2 tonight Jul 15 (Q439898 resolves tomorrow: ARG .40/ENG .34/NOR .14).
- TdF: Pogačar WON stage 10 (solo, Bastille Day), leads Vingegaard by 3.5min! Stage 11 Jul 15 → updated Pogačar .28. France: Fontainebleau fire 17k ha + shutting 3 NPPs → France .30 for national-emergency question.

## Day 22 (2026-07-15) notes + SCOREBOARD
- RESOLVED Jul 15: TdF stage 11→Soren Waerenskjold (✗ NOR sprinter). SF2→ARGENTINA ✓✓ (0.40, +0.50).
- Cumulative TW: 323.19 (31 resolved, 18 hits). Accuracy 5.6%.
- FINAL SET: SPAIN v ARGENTINA Jul 19 MetLife. Updated: winner ESP .54/ARG .42; Golden Boot Messi .48 (8 goals, can add)/Mbappé .32 (8, out); Golden Ball Messi .26/Yamal .26; 3rd place FRA .55/ENG .42 (Jul 18).
- Tomorrow: Q524604 final referee (searching for appointment).

## Day 23 (2026-07-16) notes + SCOREBOARD
- RESOLVED Jul 16: Final referee→Slavko Vincic (✗ — Slovenian elite neutral; include Vinčić-class refs in FIFA appointments).
- Cumulative TW: 314.52 (32 resolved, 18 hits).
- SPACEX IPO'd — largest in US history (~$75B raise June 11?, $1.8T cap). NVIDIA still likely most valuable (Q329053 resolves tomorrow; keep NVDA .55).
- Open R1: Brown & Sung-jae Im 66, Scheffler solid. Q32938 (leader after R2) resolves tomorrow: Scheffler .20/McIlroy .12/Im .10.
- Gaza: strikes continue despite Oct 2025 ceasefire (1100+ killed since); Nuseirat hit → updated Q425213 Nuseirat .22/Gaza City .26.
- Final Jul 19: Spain v Argentina. 3rd place Jul 18: France v England.

## Day 24 (2026-07-17) notes + SCOREBOARD
- RESOLVED Jul 17: Most valuable→APPLE (✗ NVDA dipped/Apple surged). Open R2 leader→Lucas Herbert (✗ random). Gaza→"Nuseirat refugee camp" — I had "Nuseirat" 0.22: STRING MISMATCH = miss. LESSON: use full expected answer strings ("X refugee camp", full club names).
- Cumulative TW: 275.82 (35 resolved, 18 hits).
- SpaceX $1.8T post-IPO; NVDA still #1? Apple took most-valuable on Jul 17 — volatile.
- London DL Sat: Hodgkinson/Kerr/Duplantis/Alfred/Bol. Mile WR question: updated Kerr .18/El Guerrouj .58 (max 5 outcomes error — resubmitted correctly).
- 3rd place France v England Sat night; UFC 330? OKC card Sat; Final Sun: Spain v Argentina.

## Day 25 (2026-07-18) notes + SCOREBOARD
- RESOLVED Jul 18: Rogers→Chelsea ✓ (2nd, +0.15). 3rd place→England ✓ (2nd, +0.36). UFC OKC→Dricus du Plessis (✗ champ DDP fought there! Lesson: title-champ main events → include champion). Mile WR→Josh Kerr set it! (✗ El Guerrouj .58 top — TW -39.8; the WR did fall in London).
- Cumulative TW: 255.65 (39 resolved, 22 hits).
- Belgian GP: Antonelli POLE (+0.3s over Verstappen!), Norris P3. Updated Q556116: Russell .52/Hamilton .30 (2nd place post-Belgian; resolves Jul 19).
- Final Jul 19: Spain v Argentina (ESP .54/ARG .42; GB: Mbappé .28/Messi .26; Ball: Messi .26/Yamal .26).
- Tomorrow resolves: Q201629, Q241292, Q556116, Q581542, Q927657.

## Day 26 (2026-07-19) notes + SCOREBOARD
- RESOLVED Jul 19: WORLD CUP→SPAIN ✓✓ (0.54, +0.61). Golden Boot→Mbappe ✓ (2nd, +0.30; tiebreak over Messi's 8). 2nd F1→Hamilton ✓ (2nd, +0.23 — big Belgian GP). Golden Ball→RODRI (✗ winning team's holding midfielder — like 2010/2018 pattern; include team pivot next time). Syria NSB→Anas Khattab ✓✓ (0.18, +0.30).
- Cumulative TW: 369.76 (44 resolved, 26 hits). Accuracy 6.3%.
- Skubal: Tigers surging (7-0 W, 9 Ks) — may not trade him. Final: Spain beat Argentina (worst final in history per Ken Early, 0-0-ish? Rodri involved).

## Day 27 (2026-07-20) notes + SCOREBOARD
- RESOLVED Jul 20: Section 338→CANADA (✓ 2nd, 0.13, +0.09 — digital services tax retaliation).
- Cumulative TW: 379.13 (45 resolved, 27 hits). Accuracy 6.3%.
- Ukraine: protests demand Syrskyi + DM Fedorov dismissal; navy & air-assault chiefs BACKED Syrskyi; Zelensky meeting commanders. Updated Q249565: Zaluzhnyi .22, Skibiuk/Niezh? — actually submitted: Drapatiy .14, Neizhpapa .10, Hnatov .10, Budanov .08.
- No Typhoon Noul news yet (resolves tomorrow — likely void or late landfall).

## Day 28 (2026-07-21) notes + SCOREBOARD
- RESOLVED Jul 21: Syrskii successor→Mykhailo Drapatyi (✓ 2nd choice 0.14; note spelling "Drapatyi"!). Typhoon Noul→Guangdong ✓✓ (0.26, +0.40).
- Cumulative TW: 405.96 (47 resolved, 28 hits). Accuracy 6.7%.
- Monsoon: 25+ killed in N/NE India Monday. LeBron: "not rushed" — decision may slip past Jul 24 resolution → trimmed Lakers to .52.
- Anthony Taylor retired from elite refereeing.

## Day 29 (2026-07-22) notes + SCOREBOARD
- RESOLVED Jul 22: Monsoon→ASSAM (✗ NE India floods; lesson: Assam/Bihar perennial monsoon-death leaders alongside Himachal).
- Cumulative TW: 387.58 (48 resolved, 28 hits).
- Spain's worst fires (Guadalajara largest, Bedar 13 dead), France 2 firefighters killed. Updated Q149811: Spain .30/France .22 (resolves tomorrow).
- India-Zim T20Is start Thu Jul 23 Harare; Shreyas Iyer captains (India lost twice to Ireland recently!). Abhishek Sharma .28 stands for first fifty.

## Day 30 (2026-07-23) notes + SCOREBOARD
- RESOLVED Jul 23: India first fifty→Vaibhav Sooryavanshi (✗ the 14yo debuted and fiftied immediately — hyped debutants deliver). Europe wildfire→SPAIN ✓✓ (0.30, +0.41).
- Cumulative TW: 390.00 (50 resolved, 29 hits). Accuracy 7.1%.
- Vozinha won WC Golden Glove + Team of Tournament (Cape Verde R32 run). CWG Glasgow opened Jul 23. LeBron still "not rushed" (resolution Jul 24 likely void/slip).

## Day 31 (2026-07-24) notes + SCOREBOARD
- RESOLVED Jul 24: OPCW→Aerial bombs (✗ had "Aerial bomb" .08 — plural mismatch again). CWG gym team→Canada ✓ (2nd, +0.13). Vozinha→Colo-Colo (✗ Chile!). LeBron→PHILADELPHIA 76ERS (✗✗ zero mass — AGAIN like Jaylen Brown! THE 76ERS ARE THIS WORLD'S AGGRESSIVE STAR-SUITOR: bought Brown + signed LeBron).
- Cumulative TW: 355.60 (54 resolved, 30 hits).
- Bahrain replacement: SEPANG leads candidates (slot between Baku Sep 26 & Singapore); Portimão returning 2027. Updated Sepang .34.
- Hungary FP1: Leclerc fastest +0.5s! Updated FP3: Leclerc .26; race: Antonelli .26/Leclerc .22.

## Day 32 (2026-07-25) notes + SCOREBOARD
- RESOLVED Jul 25: FP3→Norris (net +0.03). Bahrain replacement→SEPANG ✓✓ (0.34, +0.53).
- Cumulative TW: 372.14 (56 resolved, 31 hits). Accuracy 7.5%.
- Hungarian GP: NORRIS POLE (upgraded McLaren; Mercedes quali domination ended); Hamilton P2 → demoted 3 (impeding Piastri) = P5. Stella says Ferrari still favourites. Race Jul 26: Norris .24/Ham .18/Lec .16.
- Diomande: Real Madrid €100M bid REJECTED (Leipzig want more); Arsenal radar (also chasing Vinícius!, Álvarez, Barcola). Updated: Real Madrid .30/Arsenal .14. Arsenal signed Tzolis £34M.

## Day 33 (2026-07-26) notes + SCOREBOARD
- RESOLVED Jul 26: Hungarian GP→NORRIS ✓✓ (0.24, +0.34, pole→win). Diomande→Real Madrid ✓✓ (0.30, +0.48).
- Cumulative TW: 373.63 (58 resolved, 33 hits). Accuracy 8.3%.
- WI-Pak 1st Test Tarouba/Brian Lara Stadium: rain Day 1, WI 194/3 (Hodge 83*). Spin-friendly → updated Warrican .18/Motie .16.
- India routed by Zimbabwe (Laxman message) — India's T20 slide continues.

## Day 34 (2026-07-27) notes + SCOREBOARD
- RESOLVED Jul 27: WI 5fer→Justin Greaves (✗ part-timer). Peru FM→Carlos Espa (✗ ex-presidential-rival in coalition cabinet — LESSON: "amplia convocatoria" cabinets include defeated rivals from the first round!).
- Cumulative TW: 358.10 (60 resolved, 33 hits).
- US-IRAN TRUCE since Saturday (13 nights of renewed strikes over Hormuz blockade ended); Houthis attacked Saudi Red Sea oil installations; Yemen PM (IRGY) blames Iran. Q339902 (US strikes Jul 22-29) resolves tomorrow — my Yemen .15 stands.

## Day 35 (2026-07-28) notes + SCOREBOARD
- RESOLVED Jul 28: US strikes→Iraq ✓ (2nd choice 0.12, +0.19).
- Cumulative TW: 377.23 (61 resolved, 34 hits).
- Saudi-led coalition striking Houthis in Hodeidah (shipping attacks response). Updated Q107175: US .30/Saudi .25. England coach: ten Doeschate .16 (left India staff). Q971524: Malaysia .36 (Rohingya pressure).

## Day 36 (2026-07-29) notes + SCOREBOARD
- RESOLVED Jul 29: Coalition→Saudi Arabia ✓ (2nd, 0.25, +0.32). FOMC dissents→Hammack+Kashkari+Logan (partial: Hammack .20/Logan .03 yes, Kashkari missing — multi-answer sets are hard). Myanmar repatriation→MALAYSIA ✓✓ (0.36, +0.50). England coach→Stephen Fleming (✗ McCullum's NZ network — LESSON: successors mirror predecessor's network/compatriots!).
- Cumulative TW: 408.85 (65 resolved, 36 hits). Accuracy 8.7%.
- ROMANIA shut both Cernavodă reactors (Danube drought) Jul 29 → updated Q683823 Romania .45 (only-NPP by Aug 2) + Q772343 Romania .40 (whole-fleet Aug 1-13; announced Jul 29 — timing risk).
- Neeraj Chopra AT the CWG (Glasgow return); javelin quali Jul 30 10:30am. UNSG straw poll happened (details murky) — Bachelet .30 stands.

## Day 37 (2026-07-30) notes + SCOREBOARD
- RESOLVED Jul 30: UNSG straw poll→Grynspan ✓ (0.14, +0.12). Nuclear→HUNGARY/Paks (✗ Romania .45 wrong — Paks shut before Aug 2). CWG jav quali→Rumesh Pathirage (✗ Sri Lankan world lead!).
- Cumulative TW: 430.02 (68 resolved, 36 hits).
- NEWCASTLE CHAOS: Eddie Howe LEFT (eve of season); Isak/Tonali sold; Gordon→Barcelona rumor; Al-Ahli boss touted as replacement → updated Bruno: Al-Ahli .14/Real Madrid .14/Al-Hilal .12 (resolves tomorrow).
- CWG jav final Fri: Pathirage (WORLD LEAD) v Nadeem (champ) v Chopra → updated Pathirage .18/Chopra .22/Nadeem .20 (resolves tomorrow).

## Day 38 (2026-07-31) notes + SCOREBOARD
- RESOLVED Jul 31: Bruno→Arsenal (✗ for this Q; I'd put Arsenal on Diomande). CWG jav gold→Rumesh THARANGA Pathirage ✓ (0.18; full-name string mattered).
- Cumulative TW: 408.98 (70 resolved, 36 hits).
- SKUBAL: Rays = LEADING contender (payroll flexibility, McClanahan injury makes them more aggressive). Updated: Rays .18/Phillies dropped. Deadline TODAY Jul 31; resolves tomorrow.

## Day 39 (2026-08-01) notes + SCOREBOARD
- RESOLVED Aug 1: Skubal→DODGERS ✓ (2nd, 0.14, +0.21).
- Cumulative TW: 432.89 (71 resolved, 37 hits).
- Rocket Classic: Cameron Young 61 (-10) co-leads R2; Sunday rain delays. Updated: Young .18/Scheffler .13.

## Day 40 (2026-08-02) notes + SCOREBOARD
- RESOLVED Aug 2: ICE month→JULY ✓✓ (0.28, +0.37). Rocket Classic→Michael Thorbjornsen (✗ surprise chaser won; PGA events w/o Scheffler = random winners).
- Cumulative TW: 465.49 (73 resolved, 38 hits). Accuracy 9.1%.

## Day 41 (2026-08-03) notes + SCOREBOARD
- RESOLVED Aug 3: DC Open men→Fritz ✓ (0.12, +0.17). DC Open women→ALEXANDRA EALA (✗ — SIM BREAKOUT STAR: beat Swiatek at Wimbledon, now WTA title. Include Eala in Montreal/Cincinnati/US Open women!). Suu Kyi→ICRC ✓✓ (0.28, +0.40).
- Cumulative TW: 516.09 (76 resolved, 39 hits). Accuracy 9.5%.
- Trump-Iran talks Aug 3 (deal to reopen Hormuz; attack called off). Salah still unsigned (Q810891 resolves tomorrow — likely void). Kansas primary TODAY (Hamilton .62).

## Day 42 (2026-08-04) notes + SCOREBOARD
- RESOLVED Aug 4: Kansas→ADAM HAMILTON ✓✓✓ (0.62, +84 TW!!). Hormuz mines→Oman ✓ (2nd, +0.27). Khalifa→Death penalty ✓ (3rd, +0.10). Salah→TRABZONSPOR (✗ wild card — Turkish club). Shehadeh→Edinburgh (✗). RSF→Mahdi Adam (✗).
- Cumulative TW: 604.52 (82 resolved, 42 hits). Accuracy 9.9%.
- Updated US Open women: Eala .10 in.

## Day 43 (2026-08-05) notes + SCOREBOARD
- RESOLVED Aug 5: Michigan→El-Sayed ✓✓ (0.42, +0.51). WI-Pak 2nd Test→Pakistan ✓ (2nd, +0.26 — not a draw!).
- Cumulative TW: 681.71 (84 resolved, 44 hits). Accuracy 10.3%.
- Myanmar: Min Aung Hlaing now PRESIDENT (since Apr 10), visiting Thailand Aug 6-7 (2nd ASEAN visit after Laos); Ye Win Oo is military chief → updated Russia .30/China .28/Thailand .18.
- Parker CLEARED (provisional suspension lifted; details pending) — Q723378 may void.

## Day 44 (2026-08-06) notes + SCOREBOARD
- RESOLVED Aug 6: Ye Win Oo→Thailand ✓ (3rd, 0.18, +0.15). Rodri→Barcelona ✓ (3rd, 0.10, +0.13). Parker→"His nutritionist" (✗ doping explanations cite support persons). TN-5→Charlie Hatcher (✗ unknown beat Van Epps).
- Cumulative TW: 653.23 (88 resolved, 46 hits).

## Day 45 (2026-08-07) notes + SCOREBOARD
- RESOLVED Aug 7: PaK polling→"Bagh and Haveli" (✗ — answer was a 2-district set). Jobs→"Government" (✗ I wrote "Federal government" — STRING MISMATCH AGAIN).
- Cumulative TW: 609.96 (90 resolved, 46 hits).
- Typhoon Dolphin: landfall China's EASTERN coast Sun-Mon → updated: Wenzhou .22/Ningbo .18/Taizhou .16/Fuzhou .12/Zhoushan .10.

## Day 46 (2026-08-08) notes + SCOREBOARD
- RESOLVED Aug 8: Boat Kate→Bristol (✗). Solomon→West Ham (✗). Dolphin→YUHUAN (✗ Taizhou .16 — Yuhuan is a county-level city of Taizhou; granularity lesson).
- Cumulative TW: 585.22 (93 resolved, 46 hits).
- MotoGP Silverstone: Martin POLE (lap record, Aprilia front-row lockout) → updated Martin .30/Márquez .22/Bezzecchi .18 (resolves tomorrow).

## Day 47 (2026-08-09) notes + SCOREBOARD
- RESOLVED Aug 9: MotoGP British→Raul Fernandez (✗ the OTHER Aprilia won after lockout).
- Cumulative TW: 571.54 (94 resolved, 46 hits).

## Day 48 (2026-08-10) notes + SCOREBOARD
- RESOLVED Aug 10: Golan→Colombia (✗ unexpected recogniser).
- Cumulative TW: 562.61 (95 resolved, 46 hits).
- Tomorrow: AL-2 primary (Dobson .26 stands), Shakhtar stadium (Lublin .22), Romania fleet shutdown (.40), Ferran Torres (Al-Hilal .15).

## Day 49 (2026-08-11) notes + SCOREBOARD
- RESOLVED Aug 11: AL-2→Rhett Marques (✗). Shakhtar→STAMFORD BRIDGE (✗ wild — CL homes at Chelsea). Romania fleet shutdown ✓✓ (0.40, +0.20). Ferran Torres→PSG (✗).
- Cumulative TW: 560.62 (99 resolved, 47 hits).

## Day 50 (2026-08-12) notes + SCOREBOARD
- RESOLVED Aug 12: Divest→NextVision Stabilized Systems (✗ niche drone co). Spence→Inter Milan (✗). Oil spill→Oman (✗). WAFCON finalists→CAMEROON & MALAWI (✗✗ total shock). Inter Miami→Group stage ✓ (+0.06). Venezuela talks→Judiciary ✓✓ (0.28, +0.36).
- Cumulative TW: 548.91 (105 resolved, 49 hits). Accuracy 11.1%.
- Canadian Open: Rybakina (AO/Wimbledon champ) beat Osaka; SF v Gauff → updated Rybakina .30/Gauff .22 (resolves tomorrow).

## Day 51 (2026-08-13) notes + SCOREBOARD
- RESOLVED Aug 13: Canadian Open→Swiatek ✓ (0.08; net +19 TW). Super Cup→Türkiye (✗).
- Cumulative TW: 533.84 (107 resolved, 50 hits).
- Bangladesh dominating at Darwin: AUS 198 (Hasan Mahmud 6-55), BAN 96/1 (Mominul 35*, Tanzid 32*) → updated first-century: Mominul .30/Tanzid .26 (resolves tomorrow).

## Day 52 (2026-08-14) notes + SCOREBOARD
- RESOLVED Aug 14: Bangladesh century→Tanzid Hasan ✓ (2nd, 0.26).
- Cumulative TW: 525.72 (108 resolved, 51 hits).
- UFC 330 (Philadelphia, Aug 15): Islam Makhachev (NEW WW champ) v Ian Machado Garry; Mackenzie Dern defends SW. Updated both: Islam .62/Garry .30; Dern .60/Zhang .15.
- Indonesia: 7.7 quake OFF Indonesia (no details on province).

## Day 53 (2026-08-15) notes + SCOREBOARD
- RESOLVED Aug 15: UFC330→Dern ✓✓ (0.60, +0.80!) & Islam ✓✓ (0.62, +0.76!). Djokovic beater→Tirante (✗). MLS East→NASHVILLE (✗). Indonesia→East Nusa Tenggara (✗, 7.7 off NTT). 50 free→Douglass ✓ (2nd). 800 free→Lani Pallister (✗ AUS).
- Cumulative TW: 583.13 (115 resolved, 54 hits). Accuracy 11.9%.
- COMMUNITY SHIELD: Arsenal (PL CHAMPIONS 2025-26!) v Man City, Cardiff Sun → updated Arsenal .52/City .44 (resolves tomorrow). WAFCON final → resubmitted Cameroon .52/Malawi .45 (resolves tomorrow). St Jude: Lowry ~50th; Scheffler .24 stands.

## Day 54 (2026-08-16) notes + SCOREBOARD
- RESOLVED Aug 16: Community Shield→ARSENAL ✓✓ (0.52, +0.58, +22TW). WAFCON→CAMEROON ✓✓ (0.52, +0.57). St Jude→SCHEFFLER ✓✓ (0.24, +0.40, +39.77TW).
- Cumulative TW: 624.46 (118 resolved, 60 hits). Accuracy 13.1%.

## Day 55 (2026-08-17) notes + SCOREBOARD
- RESOLVED Aug 17: Senegal coach→Patrick Vieira (✗ big-name return). Hockey Pool D→England (✗). Japan GDP→Net exports ✓ (2nd, 0.30, +0.37).
- Cumulative TW: 643.82 (121 resolved, 61 hits). Accuracy 13.1%.
- Cory Mills has Trump's full endorsement but scandals may sink him Tue → trimmed Mills to .45.

## Day 56 (2026-08-18) notes + SCOREBOARD
- RESOLVED Aug 18: UAE embargo Iran ✓ (2nd, 0.18, +0.27). Imran Khan→Shifa ✓✓ (0.25, +0.36). Watkins→Al Hilal (✗ Villa fire-sale to Saudi). Mills→Ryan Elijah (✗ unknown challenger won — my trim helped). FL Sen Dem→Angie Nixon (✗). FDA→Heidi Overton (✗). Ukraine call→Fedorov (✗ the embattled DM!). Medvedev beater→Nakashima (✗).
- Cumulative TW: 637.34 (129 resolved, 62 hits). Accuracy 13.5%.

## Day 57 (2026-08-19) notes + SCOREBOARD
- RESOLVED Aug 19: Konsa→Arsenal (✗ Arsenal on Villa buying spree). Nord Stream→Volodymyr Zhuravlev (✗).
- Cumulative TW: 628.98 (131 resolved, 62 hits).
- No news found for tomorrow's five (Savinho, CA-14, Alcaraz return, Sinaloa, proxy designation) — priors stand.

## Day 58 (2026-08-20) notes + SCOREBOARD
- RESOLVED Aug 20: FIVE HITS! Savinho→Tottenham ✓ (0.20); CA-14→Wahab ✓✓ (0.55, +75TW); Sinaloa→Rocha Moya ✓✓ (0.30); Alcaraz return→US OPEN ✓✓ (0.35 — he returns AT the US Open!); proxy→Hezbollah ✓ (0.15).
- Cumulative TW: 842.95 (+215 in one day!). 136 resolved, 68 hits. Accuracy 15.1%.
- Updated US Open men's: Alcaraz .22/Sinner .30.

## Day 59 (2026-08-21) notes + SCOREBOARD
- RESOLVED Aug 21: Baleba→Man United ✓✓ (0.30, +0.48, +48TW). Marmoush→Tottenham ✓ (0.06 tail hit!).
- Cumulative TW: 899.17 (+56!). 138 resolved, 70 hits. Accuracy 15.5%.
- Robot Games (2nd, Beijing): 2,056 robots, 51 events; humanoid crashed during 100m speed test. PL opener opponents not found — priors stand.

## Day 60 (2026-08-22) notes + SCOREBOARD
- RESOLVED Aug 22: Freedom 250 pole→ALEX PALOU ✓✓ (0.25, +0.38, +38TW). Robot 100m→"Tiangong Ultra" (had "Tiangong" .20 — STRING lesson again). AIPAC→Mike Rogers (✗ — should've considered MI Senate race GOPer). Forest lost to Leeds; Man Utd LOST to Hull City (✗✗). Fabinho→Trabzonspor (✗ — same club as Salah! Trabzonspor = destination club this sim).
- Cumulative TW: 897.03 (144 resolved, 71 hits). Accuracy 15.9%.
- Djokovic OUT of Cincinnati (lost to Tirante) → updated Cincinnati men's: Sinner .32/Zverev .12 (resolves tomorrow with women's Cincinnati + Dutch GP + Silesia).

## Day 61 (2026-08-23) notes + SCOREBOARD
- RESOLVED Aug 23: 400h→dos Santos ✓ (3rd). Bouaddi→Man City (✗). Cincinnati women→GAUFF ✓ (3rd, +13.5TW). 100m Silesia→Jefferson-Wooden ✓✓ (0.22, +33TW!). Cincinnati men→ARTHUR FILS (✗ young French star won). Dutch GP→Norris ✓ (0.10, +0.07).
- Cumulative TW: 938.48 (+41!). 150 resolved, 78 hits. Accuracy 16.3%.

## Day 62 (2026-08-24) notes + SCOREBOARD
- RESOLVED Aug 24: Allan Elias→Man City (✗). USS Lincoln→Thailand (✗ — carrier now Indo-Pacific post-Iran-war). Hadjam→Brighton (✗). Eurovision boycott→Netherlands ✓ (0.10, +0.10).
- Cumulative TW: 924.88 (154 resolved, 79 hits).
- Measles: MARYLAND outbreak (31 cases, 4 counties incl St. Mary's) → updated Maryland .35 (resolves tomorrow).

## Day 63 (2026-08-25) notes + SCOREBOARD
- RESOLVED Aug 25: Celtic→Europa League ✓✓ (0.45, +0.53, +53TW). PFA→Bruno Fernandes (✗). Mixed doubles→Patten/Siniakova elimination (✗ they played). CBS Moscow→Ratcliffe ✓ (0.08). Measles death→Pennsylvania (✗).
- Cumulative TW: 947.61 (159 resolved, 80 hits). Accuracy 16.7%.
- Xi: visiting WASHINGTON late Sep (first in a decade); BRICS New Delhi Sep 12-13 likely. No ME visit yet → Q834692 may void.

## Day 64 (2026-08-26) notes + SCOREBOARD
- RESOLVED Aug 26: Jackson→Aston Villa ✓ (0.07, +0.07). Xi ME→Egypt ✓ (3rd, 0.15, +0.11).
- Cumulative TW: 965.98 (161 resolved, 82 hits).
- Man City: MARESCA replaced Pep (end of last season); signed Bouaddi €100M (Lille); retain interest in ENZO → updated Enzo: Man City .30 (resolves tomorrow).

## Day 65 (2026-08-27) notes + SCOREBOARD
- RESOLVED Aug 27: Barcola→Liverpool (✗). Emi Martinez→Chelsea (✗!). Enzo→Man City ✓✓ (0.30, +0.48).
- Cumulative TW: 951.09 (164 resolved, 83 hits).
- KING HARALD (89) in "VERY SERIOUS" condition in hospital (announced Thursday Aug 27) → updated Harald .62/Haakon .36 (resolves tomorrow Aug 29!).
- CIA Director Ratcliffe visited Moscow (met Putin re NATO concerns; Kyiv drone waves changed NATO-risk calculus).

## Day 66 (2026-08-28) notes + SCOREBOARD
- RESOLVED Aug 28: King Harald DIED → Haakon VIII (my Haakon .36 right direction, Harald .62 top wrong). SCO counterpart→Erdogan (✗).
- Cumulative TW: 923.34 (166 resolved, 83 hits).

## Day 67 (2026-08-29) notes + SCOREBOARD
- RESOLVED Aug 29: Martinelli→AL-HILAL ✓✓ (0.10 top, +0.17, +16.5TW — Villa-style Saudi moves recurring). Sydney men→Addisu Gobena (✗); women→Peres Jepchirchir (✗).
- Cumulative TW: 933.25 (169 resolved, 84 hits). Accuracy 17.5%.

## Day 68 (2026-08-30) notes + SCOREBOARD
- RESOLVED Aug 30: Gabriel Jesus→Barcelona (✗ surprise).
- Cumulative TW: 929.01 (170 resolved, 84 hits).

## Day 69 (2026-08-31) notes + SCOREBOARD
- RESOLVED Aug 31: Raam #2→Yoav Segalovich (✗ ex-Shin Bet on Arab slate). Villa-Arsenal→Arsenal ✓✓ (0.42, +0.51, +51TW).
- Cumulative TW: 970.79 (172 resolved, 85 hits). Accuracy 17.9%.
- Window closed: Bouaddi €100M→City likely record fee → updated Q875467: Bouaddi .38/Rogers .18/Baleba .14 (resolves tomorrow).

## Day 70 (2026-09-01) notes + SCOREBOARD
- RESOLVED Sep 1: Highest PL fee→ENZO FERNANDEZ (✗ — I knew Enzo→City but didn't link to fee Q! Lesson: after resolving "which club" Qs, check related "fee/stage/etc" Qs).
- Cumulative TW: 965.97 (173 resolved, 85 hits).

## Day 71 (2026-09-02) notes + SCOREBOARD
- RESOLVED Sep 2: Ghana coach→Carlos Queiroz (✗ — Queiroz again, he's the journeyman pick everywhere). Gaza plan→BEN-GVIR ✓✓ (0.30, +0.41, +41TW).
- Cumulative TW: 1001.04 (175 resolved, 86 hits). Accuracy 18.3%.

## Day 72 (2026-09-03) notes
- Haze: severe Indonesian smoke since Aug 21 (Sumatra/Kalimantan); experts say 2015-repeat unlikely → Indonesia .55 stands (Q224345 resolves tomorrow).
- Iran: sanctions era continues; 72% of US voters support force/sanctions to reopen Hormuz.

## Day 73 (2026-09-04) notes + SCOREBOARD
- RESOLVED Sep 4: FAO→Sugar ✓ (0.15, +0.10). Haze→Malaysia ✓ (2nd). Betis opener→Troy Parrott (✗ Betis striker! — consider opposition strikers, not just Madrid stars). Bank→Golden Global Bank (✗ TURKISH bank — Turkey theme recurring: Salah-Trabzonspor, Super Cup-Türkiye, Golden Global).
- Cumulative TW: 984.26 (179 resolved, 87 hits).

## Day 74 (2026-09-05) notes + SCOREBOARD
- RESOLVED Sep 5: MAGA Inc→Texas (✗ — Senate race push).
- Cumulative TW: 968.44 (180 resolved, 87 hits).
- Italian GP (Monza) today: boosted Leclerc .16 (tifosi) — resolves tomorrow.

## Day 75 (2026-09-06) notes + SCOREBOARD
- RESOLVED Sep 6: La Liga leader→Barcelona ✓✓ (0.28, +0.33, +33TW). Ebola→North Kivu ✓ (2nd, +0.08). Italian GP→ANTONELLI ✓✓ (0.26, +0.39, +41TW — Monza win for the home hero!).
- Cumulative TW: 1051.13 (183 resolved, 91 hits). Accuracy 18.7%.

## Day 76 (2026-09-07) notes
- No news on Liverpool sponsor or STF/Rodrigues (resolve tomorrow) — priors stand (Standard Chartered .25; de Moraes .30).

## Day 77 (2026-09-08) notes + SCOREBOARD
- RESOLVED Sep 8: Liverpool sponsor→TURKISH AIRLINES (✗ — Turkey AGAIN: Super Cup, Salah-Trabzonspor, Golden Global Bank, now this. TURKISH ENTITIES are this sim's wildcard sponsor!). STF→André Mendonça (✗ newest justice).
- Cumulative TW: 1022.66 (185 resolved, 92 hits).

## Day 78 (2026-09-09) notes + SCOREBOARD
- RESOLVED Sep 9: Census→Permanent residency (✓2nd, net ~flat). England bowler→Josh Tongue (✗).
- Cumulative TW: 1010.23 (187 resolved, 92 hits).

## Day 79 (2026-09-10) notes + SCOREBOARD
- RESOLVED Sep 10: Mayun→Houthis ✓✓ (0.55, +0.74, +74TW!). Kyiv fuel strikes ✓✓ (0.28, +0.41, +41TW!).
- Cumulative TW: 1126.12 (189 resolved, 94 hits). Accuracy 19.4%.
- US Open: Shelton BEAT Alcaraz (defending champ); Tiafoe 2-set comeback into SFs; Zverev v Khachanov other SF. Updated Q408930: Shelton .34/Tiafoe .30 (resolves tomorrow).

## Day 80 (2026-09-11) notes + SCOREBOARD
- RESOLVED Sep 11: Donnarumma trial→Ilyas Kherbouch (✗). Furthest American→SHELTON ✓✓ (0.34, +0.46, +29.75TW). 5000m→INGEBRIGTSEN ✓✓ (0.40, +0.60, +60.5TW!).
- Cumulative TW: 1210.04 (192 resolved, 97 hits). Accuracy 20.2%.
- US Open women's final: SABALENKA v RYBAKINA (threepeat bid) → resubmitted Sabalenka .52/Rybakina .44. Venice: NAZA record ovation → NAZA .24 (resolves tomorrow). Also FIFA rebuked Morocco's 2030-final claim (Spain/Portugal hosts!).

## Day 81 (2026-09-12) notes + SCOREBOARD
- RESOLVED Sep 12: Women's javelin→Kitaguchi ✓ (2nd, 0.18, +0.24). Venice→NAZA ✓✓ (0.24, +0.40). Villa-Forest→FOREST ✓✓ (0.35, +0.40, +39.75TW). US Open women→RYBAKINA ✓ (0.44 2nd; Sabalenka threepeat failed).
- Cumulative TW: 1263.21 (196 resolved, 101 hits). Accuracy 21.0%.
- Updated: derby City .38/United .24; US Open men's Sinner .40/Zverev .22; Spanish GP Antonelli .24/Norris .16.

## Day 82 (2026-09-13) notes + SCOREBOARD
- RESOLVED Sep 13: Talks venue→UAE (✗). Javelin→Pathirage AGAIN (✗ world-lead form carried). Spanish GP→ANTONELLI ✓✓ (0.24, +0.35, +41TW). Derby→Man City ✓✓ (0.38, +0.47, +35TW). Okinawa→Genta Koja (✗). 200m→Kenneth Bednarek (✗ classic silver-guy upset). US Open men→ZVEREV ✓ (0.22 2nd; 1st major!).
- Cumulative TW: 1281.85 (203 resolved, 107 hits). Accuracy 21.8%.
- Emmys ceremony Sep 13/14 — check tomorrow's articles for winners before resolution.

## Day 83 (2026-09-14) notes + SCOREBOARD
- RESOLVED Sep 14: Comedy→Widow's Bay (✗ new show). Lead Actress→Rhea Seehorn (✗ Pluribus star!). 2029 CL final→Camp Nou ✓ (3rd, +0.10). Orbit weapons→UNITED STATES ✓ (3rd, 0.20, +0.17). Drama→THE PITT ✓ (3rd, 0.14, +0.16).
- Cumulative TW: 1306.40 (208 resolved, 110 hits). Accuracy 21.8%.

## Day 84 (2026-09-15) notes + SCOREBOARD
- RESOLVED Sep 15: 2029 WAC→NAIROBI ✓ (0.08, +0.10, +10.5TW).
- Cumulative TW: 1316.88 (209 resolved, 111 hits).
- Yemen: 100k+ displaced (Houthi offensive + Saudi strikes); Gulf states condemning → updated UNGA appeal: Sudan .22/Yemen .20.

## Day 85 (2026-09-16) notes + SCOREBOARD
- RESOLVED Sep 16: UNGA appeal→YEMEN ✓ (2nd, 0.20, +0.27). Iran-Houthis ask→CHINA ✓ (3rd, 0.15, +0.15). Campeones Cup→INTER MIAMI ✓✓ (0.42, +0.60, +60TW!).
- Cumulative TW: 1397.84 (212 resolved, 114 hits). Accuracy 22.2%.

## Day 86 (2026-09-17) notes + SCOREBOARD
- RESOLVED Sep 17: Nigeria suspension→Suberu Siyaka Aniviye (✗ specific official name).
- Cumulative TW: 1383.26 (213 resolved, 114 hits).

## Day 87 (2026-09-18) notes + SCOREBOARD
- RESOLVED Sep 18: PSA #1→AMINA ORFI ✓ (0.15, +0.15, +15TW — young star took #1). Mbappé sponsor→ON (✗✗ Swiss running brand!). Trump Jr probe→John Curtis ✓✓ (0.15, +0.18, +17.8TW).
- Cumulative TW: 1358.62 (216 resolved, 116 hits).

## Day 88 (2026-09-19) notes + SCOREBOARD
- RESOLVED Sep 19: UFC 331 flyweight→Joshua Van ✓ (0.12 tied-2nd — Van dethroned Pantoja!). Lightweight→ARMAN TSARUKYAN ✓✓ (0.18 top, +0.27, +27TW).
- Cumulative TW: 1387.53 (218 resolved, 118 hits). Accuracy 22.6%.

## Day 89 (2026-09-20) notes + SCOREBOARD
- RESOLVED Sep 20: Madrid derby→ATLÉTICO (✗ — they won the derby). Iran GDP→Oil&gas ✓ (0.15, +0.08). Basketball bronze→Iran (✗). Copenhagen half→Agnes Ngetich (✗). Berlin→THE LEFT (✗ CDU .38 wrong; Left won Berlin!).
- Cumulative TW: 1396.47 (223 resolved, 119 hits). Accuracy 22.6%.

## Day 90 (2026-09-21) notes + SCOREBOARD
- RESOLVED Sep 21: 200 IM Asian Games→YU ZIDI ✓✓ (0.20, +0.31, +31TW!). Rwanda→Vincent Brown (✗).
- Cumulative TW: 1422.78 (225 resolved, 120 hits). Accuracy 23.0%.

## Day 91 (2026-09-22) notes + SCOREBOARD
- RESOLVED Sep 22: Hungary immunity→Balázs Hankó (✗ research minister).
- Cumulative TW: 1412.65 (226 resolved, 121 hits).
- Yu Zidi won 200 IM at Asian Games → boosted 400 IM: Yu Zidi .32 (resolves tomorrow).

## Day 92 (2026-09-23) notes + SCOREBOARD
- RESOLVED Sep 23: 400 IM→YU ZIDI ✓✓ (0.32, +0.50, +35TW — double gold!). Tunisia activist→Wael Naouar (✗). 49kg→RI SONG GUM ✓✓ (0.25, +0.37, +37TW — DPRK lifters deliver).
- Cumulative TW: 1479.79 (229 resolved, 123 hits). Accuracy 23.8%.

## Day 93 (2026-09-24) notes + SCOREBOARD
- RESOLVED Sep 24: 200 breast→Shin Ohashi (✗ Japan's next-gen). Portugal goal→João Félix (✗). Artemis 75th→Ivory Coast (✗ — African nations joining; consider CAF countries for space accords).
- Cumulative TW: 1446.03 (232 resolved, 125 hits).

## Day 94 (2026-09-25) notes + SCOREBOARD
- RESOLVED Sep 25: TikTok→Alabama (✗). Asian Games 100m→PURIPOL BOONSON ✓✓ (0.15, +0.25, +25.4TW — Thai teen delivered). Kalshi→Sixth Circuit (✗).
- Cumulative TW: 1447.90 (235 resolved, 126 hits). Accuracy 24.2%.
- Baku: Antonelli CRASHED out in Q1 (championship leader, "stupid"); RUSSELL POLE → updated Q447470: Russell .34 (resolves tomorrow).

## Day 95 (2026-09-26) notes + SCOREBOARD
- RESOLVED Sep 26: England-Spain→SPAIN ✓ (2nd, 0.32, +0.31, +31TW — Spain won at Wembley). Azerbaijan GP→RUSSELL ✓✓ (0.34, +0.50 — pole→win). Kohli "last WC" ✓✓ (0.25, +0.39, +38.9TW). DOSB→Munich ✓ (2nd, +0.26). Puyo Puyo→Yuki Kurihara (✗).
- Cumulative TW: 1553.01 (240 resolved, 129 hits). Accuracy 25.0%.

## Day 96 (2026-09-27) notes + SCOREBOARD
- RESOLVED Sep 27: Ireland beat Israel ✓✓ (0.42, +0.51, +51TW!). Sindhu→QF ✓✓ (0.30, +0.40, +40.5TW). Squash women→Sivasangari, men→Eain Yow Ng (✗✗ MALAYSIAN sweep — considered Malaysia in nothing). Ramallah→Netherlands (✗).
- Cumulative TW: 1602.92 (245 resolved, 131 hits). Accuracy 25.8%.

## Day 97 (2026-09-28) notes + SCOREBOARD
- RESOLVED Sep 28: ChatGPT halt→Florida (✗ Florida again — the sim's wildcard US state, like Texas). Javelin→Pathirage 3rd straight (✗ — world-lead streak should have dominated priors after CWG+Ultimate). UNL A1→France (✗ — France in A1, my group mapping wrong).
- Cumulative TW: 1541.03 (248 resolved, 131 hits).
- Morocco: ruling coalition dominated last week's election → Akhannouch .42 stands.

## Day 98 (2026-09-29) notes + SCOREBOARD
- RESOLVED Sep 29: Aston Martin 2027→FERNANDO ALONSO ✓✓ (0.25, +0.41, +40.8TW — Alonso stays!). Morocco PM→El Mansouri (✗ new name).
- Cumulative TW: 1561.53 (250 resolved, 133 hits). Accuracy 26.2%.
- FINAL 2: Q138739 Pike stay court + Q889545 China Asiad football eliminator — resolve tomorrow.

## FINAL SESSION RESULTS (2026-09-30)
- ALL 252 questions resolved and predicted.
- FINAL: TW-Score 1625.25 | Accuracy 26.6% (67/252) | Brier skill 0.108
- Last-day hits: Pike stay→Sixth Circuit ✓ (2nd, 0.25, +27.9TW); China Asiad→South Korea ✓✓ (0.25, +0.36, +35.9TW).
- Full lessons in memory/SKILLS.md.
