# Forecasting Tournament — Persistent Memory

## Simulation state
- Sim date: **2026-06-24** (Day 1). 252 active questions, all resolved by 2026-09-30.
- All 252 have an initial forecast submitted on Day 1 (2026-06-24). predictions/2026-06-24.json.
- Key fictional/sim events: Khamenei assassinated 2026-02-28 (funeral July 4-9, Mashhad); Mojtaba Khamenei is new Supreme Leader; Iran war ongoing; Maduro removed from Venezuela; Starmer resigned as UK Labour leader 2026-06-22 (Burnham returned via Makerfield by-election, frontrunner); Kevin Warsh Fed chair since 2026-05-22; Powell out; 2026 World Cup ongoing in US/Mexico/Canada; Alcaraz out of Wimbledon (wrist).

## Scoring strategy
- Score = Brier skill per day: E[score] ≈ Σ p_i² over listed outcomes if q=p. So ALWAYS list the true top-5 candidates with honest probabilities; adding a candidate with true prob p adds ~p² to expected score.
- Unlisted true outcome → big penalty. Never use placeholder outcomes; use exact names.
- Update forecasts as new info arrives — TW score accrues daily; each new submission overwrites prior and accrues weight from that day.
- For "if any" questions, "None" is a legitimate outcome.
- For conditional questions ("If X leaves..."), answer the likely destination if the event occurs; question may void if condition fails (then it doesn't count).

## Key verified facts (as of 2026-06-24)
### F1 2026 (new regs)
- Standings after 7 rounds (Barcelona): Antonelli 156 (Mercedes, 5 wins: China, Japan, Miami, Canada, Monaco), Hamilton 115 (Ferrari, won Barcelona), Russell 106 (won Australia), Leclerc 75, Norris 73, Piastri 68, Verstappen 55.
- Mercedes dominant (6 wins in 7). Bahrain + Saudi GPs cancelled (Iran conflict). Races: British GP July 5 (Silverstone), Belgian July 19, Hungarian July 26, Dutch Aug 23, Italian Sep 6, Spanish Sep 13 (Madrid), Azerbaijan Sep 26.
- Per-race priors: Antonelli ~0.40-0.44, Hamilton ~0.20, Russell ~0.15, Norris ~0.09, Verstappen ~0.07.
### MotoGP 2026
- Bezzecchi 180, Martin 172, Marquez 140 (5 wins) after ~10 rounds. Marquez strong at Sachsenring.
### Tennis
- Wimbledon June 29-July 12; draw June 26. Alcaraz OUT (wrist). Men: Sinner -175 (~64%), Djokovic +500, Zverev +900 (won 2026 French Open). Women: Sabalenka +300, Rybakina +400, Swiatek +500 (defending), Gauff +600, Andreeva +800 (won 2026 French Open). Serena Williams singles wildcard (+3500).
### FIFA World Cup 2026 bracket (verified FIFA/CBS)
- R32: Jun 28-Jul 3. R16 Jul 4-7. QF: Jul 9 Boston (M97=W89vW90), Jul 10 LA (M98=W93vW94), Jul 11 Miami (M99=W91vW92), Jul 11 KC (M100=W95vW96). SF: Jul 14 Dallas (W97vW98), Jul 15 Atlanta (W99vW100). 3rd place Jul 18 Miami. Final Jul 19 NJ.
- Paths: Boston QF ← 1E(Germany)/1I(France) side + 1F(Neth)/2C(Brazil?) side. LA QF ← 1H(Spain)/1D(USA)/1G(Belgium). Miami QF ← 1C(Brazil)/1L(England)/1A(Mexico). KC QF ← 1J(Argentina)/1K(Portugal)/1B(Switzerland).
- Bookmaker win odds (June 19-23): France ~17-20%, Spain ~15-17%, England ~11-12%, Brazil ~8-10%, Portugal ~8-10%, Argentina ~8-9%, Germany ~6-7%.
- Group stage results so far: Spain 0-0 Cape Verde; France 3-1 Senegal; USA 4-1 Paraguay, 2-0 Australia; Canada 6-0 Qatar but lost 1-2 Switzerland (SUI won Group B, CAN 2nd); Morocco 1-0 Scotland (Boston); Brazil 1-1 Morocco.
- Golden Boot odds: Mbappe 6/4, Messi 13/8, Haaland 5/1, Kane 6/1. Messi 5 goals (all Argentina's) after 2 games; Mbappe 4.
### Fed (July 29 FOMC)
- Chair Kevin Warsh (since May 22). April 29 meeting 8-4: Miran wanted cut; Hammack/Kashkari/Logan opposed easing bias. June 16-17 unanimous hold. July hike odds ~18-34%. Hawks: Hammack, Kashkari, Logan.
### UK politics
- Starmer resigned as PM/Labour leader June 22; leadership nominations July 9-16; new leader by Sept 1. Burnham frontrunner (won Makerfield June 18, 54.8%).
### Others
- SK Hynix filed June 24 for $29.4B Nasdaq ADR listing July 10 (largest ADR ever, beats Alibaba $21.8B).
- Seahawks sale: bidders Grousbeck/Mittal (letter of interest), Khosla, Boehly (weighing), Zuckerberg (rumored); NFL approval possibly August.
- Nvidia ~$5.1T most valuable (Alphabet $4.5T, Apple $4.4T).
- NY passed 1-yr data-center moratorium June 4 (awaiting Hochul signature).
- Women's T20 World Cup (England, June-July 2026): Australia favorite ~1.63, 3-0 in group; England & WI 3-0; India lost to South Africa.
- England-India T20I series: July 1, 4, 7, 9, 11 in England. India reigning men's T20 WC champs (beat England in semi by 7 runs).
- LeBron: Lakers most likely (0.67); Warriors threat.

## Per-question notes (selected)
- 279946 SK Hynix 0.82 (verified filing).
- 225772 Savinho→Spurs 0.85 (verified "effectively formalised").
- 26225 Morgan Rogers→Arsenal 0.85 (personal terms agreed, multiple sources; fee £100m still to settle).
- 876325 Enzo→Real Madrid 0.82 (personal terms in principle; Chelsea want £120-140m; some sources say no agreement yet — monitor).
- 311120 Qatar hosts 2027 Spanish Super Cup 0.90 (RFEF president confirmed).
- 76066 Moldova PM: Munteanu still active (June 24); question may void; Recean 0.30 if not.
- 754639 UK party leader resign MP: unclear; low confidence spread.
- 619176 PFA month: no decision yet; September 0.40 modal.
- 126882 OPCW Syria: 54 aerial bombs + 25 rockets found May 2026; answer likely "aerial bombs" (0.45).

## Update triggers / to-dos
- **June 25-27**: WC group stage ends → update WC QF/SF/final forecasts (199448, 457239, 935518, 439898, 592683, 241292, 201629, 581542) based on actual bracket.
- **June 26**: Wimbledon draw → update 985440 (first finalist; check Sinner/Djokovic halves), 742225, 846335.
- **June 28-July 3**: WC R32 results → refine.
- **July 1-11**: England-India T20 series (562262) — update after each match.
- **July 5**: British GP (747581); **July 12**: MotoGP German GP (897546).
- **July 9-11**: WC QFs; **July 14-15** semis; **July 19** final.
- Watch for: Kremlin announcement on Khamenei funeral delegation (659176) ~July 1-4; Hannah Dugan sentencing July 8 (213487); SK Hynix pricing July 10 (279946); FOMC July 28-29 (942650); Seahawks sale approval (902592); Fed July meeting.
- Resubmit/refine when agents' key claims (e.g., transfer agreements) get confirmed or contradicted in news.

## Agent cluster research files (Day 1)
- scripts/cluster_*.json contain question lists per topic. Research summaries embedded in session transcripts; key numbers captured above and in per-question submissions.

## Day 1 (2026-06-24) late-session updates
- 279946 SK Hynix → 0.82 (SEC F-1 filed 6/24; $29.4B Nasdaq ADR listing July 10; beats Alibaba $21.8B if completed).
- 659176 Khamenei funeral Russian official: Volodin 0.45, Putin 0.20 (Iran Intl: "lower-level Russian delegation expected"; Raisi 2024 precedent Volodin).
- 902592 Seahawks: Grousbeck/Mittal 0.33, Boehly 0.16, Khosla 0.15, Zuckerberg 0.08.
- 803035 NY data center moratorium: bill passed June 4, awaiting Hochul (has until Dec); NY 0.62.
- 213487 Dugan sentencing July 8: felony §1505, max 5 yrs, first-time offender, Judge Adelman (Clinton appointee); Prison 0.50, Probation 0.28.
- 258607 Women's T20 WC: Australia 4-0 Q, England 4-0 Q; India 2-1 at risk (needs win vs BAN/AUS; SA/BAN contenders). Updated Australia 0.50, England 0.22, India 0.11.
- 799550 POTM: Sciver-Brunt 0.22, Sutherland 0.20, Ecclestone 0.12.
- 344207 Jaylen Brown: Giannis traded to Heat 6/22; Celtics listening to Brown offers; Houston & Atlanta frontrunners, Portland/Cleveland/New Orleans in mix. Updated Houston 0.28, Atlanta 0.20, Portland 0.12, Cleveland 0.10, NOP 0.04.
- 263626 trade deficit: April goods deficits Taiwan $19.3B, Vietnam $19.3B, Mexico $14.8B, China $12.0B (May data out July 7). Current: Taiwan 0.44/Vietnam 0.32/Mexico 0.18/China 0.04.
- 362674 TN-9: Brent Taylor self-funded $1M; endorsed by Blackburn, Hagerty, Burchett, Scalise; Trump not yet endorsed as of 6/24. Taylor 0.78.
- 633052 cyclospora: Texas highest baseline (400+ cases 2024); Texas 0.40.
- 619176 PFA month: no decision as of 6/24; Sept 0.40 modal.
- 754639 UK party leader: Starmer resigned Labour leader 6/22 (not MP resignation); Burnham won Makerfield 6/18. No clear candidate for "resign as MP + by-election July 1-9". Spread Farage/Starmer/Davey ~0.08-0.12.

## Reminder for Day 2
- WC group stage final results (June 24-27) → check bracket seeds for QF paths.
- Wimbledon draw June 26 → Sinner/Djokovic half placement for 985440.
- Check for new news on: Khamenei funeral delegation, Seahawks bids, Moldova PM, UK leadership.
- Format fixes applied Day 1: 120116 → "Harald V"; 628038 → "Morocco, Nigeria" (alphabetical comma format); 685197 → district names joined by "and"; 772246 → surnames joined by "and".
- End of Day 1: 252/252 predictions active. Mean max prob 0.41; 25 questions ≥0.70, 24 questions <0.20.

## Day 2 (2026-06-25) updates
### World Cup (group stage nearly done)
- Group A: Mexico 1st (9pts), South Africa 2nd (beat South Korea 1-0). 2A=South Africa.
- Group B: Switzerland 1st, Canada 2nd. Group C: Brazil 1st (7), Morocco 2nd (7). 1C=Brazil, 2C=Morocco.
- Group D: USA 1st (6pts, +5). 2D = Australia or Paraguay (final June 25: Turkey-USA, Paraguay-Australia).
- Group E: Germany 1st despite losing 1-2 to Ecuador; Ivory Coast 2nd (6pts). Ecuador 3rd 4pts.
- Group F: Netherlands 4 (+4), Japan 4 (+4), Sweden 3 (0) before final MD3 June 25 (Japan-Sweden, Tunisia-Netherlands).
- Group G: Egypt 4 (+2), Iran 2, Belgium 2, NZ 1 (final MD3: Egypt-Iran, Belgium-NZ).
- Group H: Spain 4 (+4), Uruguay 2, Cape Verde 2, Saudi 1.
- Group I: France 6 (+5), Norway 6 (+4); France-Norway June 26 for top spot (France needs draw).
- Group J: Argentina 6 (+5) 1st, Austria 3, Algeria 3. 2J=Austria likely.
- Group K: Colombia 6 (+3) 1st, Portugal 4 (+5); Colombia-Portugal MD3 (Colombia tops if avoids defeat).
- Group L: England 4 (+2), Ghana 4 (+1), Croatia 3; England likely 1L.
- Boston QF (M97) = W89 (1E Germany vs 1I France/Norway in R16!) vs W90 (2A/2B winner vs 1F/2C Morocco). Updated: France 0.33, Netherlands 0.12, Germany 0.11, Morocco 0.05, Norway 0.04.
- KC QF (M100) = Argentina/2H vs (1K Colombia/Portugal vs 1B Switzerland). Updated: Argentina 0.33, Portugal 0.12, Colombia 0.11, Switzerland 0.08, Uruguay 0.04.
- SF Dallas (M101) = Boston vs LA (Spain/USA/Egypt/Belgium). Updated: France 0.27, Spain 0.26, Germany 0.09, Netherlands 0.06, USA 0.04.
- Golden Boot: Messi has 5 goals in 2 games (2 vs Austria), Mbappe 4. Updated Messi 0.31, Mbappe 0.30.
### Other key updates
- US-Iran preliminary peace deal signed ~June 19; oil back to pre-war (~$72 Brent); Hormuz traffic normalizing; Rubio reassures GCC in Bahrain. → 339902 None up to 0.30; 107175 None 0.45; 817209 Oman 0.60.
- Core PCE 4.1% y/y May (core 3.4%, highest since 2023). Market: ~30% July hike, ~80% Sept hike. Fed July 29 question: None 0.38, Hammack/Kashkari/Logan 0.10.
- Wimbledon: draw June 26. Men's seeds: 1 Sinner, 2 Zverev, 3 Auger-Aliassime, 4 Shelton, 5 de Minaur, 6 Fritz, 7 Djokovic, 8 Medvedev. Draper injured/outside top100 (not a contender). Women: 1 Sabalenka, 2 Rybakina, 3 Swiatek, 4 Pegula, 5 Andreeva, 6 Anisimova, 7 Gauff. Mboko out (knee).
- LeBron: free agency June 30; Lakers frontrunners but no commitment; Warriors + Cavs (sign-and-trade Jarrett Allen buzz). Updated Lakers 0.62, Cavs 0.10, Warriors 0.10, Knicks 0.04.
- Minneapolis council passed 5-month data center pause (city-level, not state; NY still frontrunner for statewide).
- Venezuela earthquakes (7.5/7.2, 164+ dead) — watch for effects.
- DRC Ebola outbreak >1000 cases; first case in France June 24.
- Typhoon Mekkhala passing Taiwan toward Japan (not Bavi/Noul/Dolphin).
- PFA Gaza: recovery plan ongoing; Ramadan tournament Feb 2026, U19 "hope" tournament April 2026; formal league resumption announcement could come July-Aug.

## To-do Day 3
- Check WC Group D/F final results (2D, 1F/2F) → refine QF forecasts.
- Wimbledon draw (June 26) → check Sinner/Djokovic halves for 985440.
- Watch for Khamenei funeral delegation announcement (659176), Russia/Ukraine, Moldova.
- Check June 26 articles for transfer updates.

## Day 3 (2026-06-26) updates
### Wimbledon draw (June 26)
- MEN: Sinner & Djokovic SAME top half (Djokovic seeded to meet FAA in QF, Sinner in SF). Zverev bottom half with Shelton SF, Fritz QF. Fritz vs Draper R1. Updated 985440: Sinner 0.50, Djokovic 0.13, Zverev 0.12, FAA 0.07, Shelton 0.04. 742225: Sinner 0.48, Zverev 0.13, Djokovic 0.11, Shelton 0.05, Fritz 0.04.
- WOMEN: Top half Sabalenka(1)/Andreeva(5)/Pegula(4)/Gauff(7); bottom Swiatek(3)/Svitolina(8)/Anisimova(6)/Rybakina(2). QFs: Sabalenka-Andreeva, Pegula-Gauff, Svitolina-Swiatek, Anisimova-Rybakina. Updated 846335: Sabalenka 0.20, Rybakina 0.17, Swiatek 0.14, Andreeva 0.11, Gauff 0.09.
- Alcaraz return: Montreal (Canadian Open) most realistic per June 25 Puntodebreak; Los Cabos/DC improbable. Updated 855662: Canadian Open 0.40, DC Open 0.25, Los Cabos 0.12, Cincinnati 0.10, US Open 0.05.
### World Cup (June 26)
- France 4-1 Norway (Dembélé hat-trick; Norway rested Haaland). France 1I, Norway 2I.
- Japan 1-1 Sweden → Netherlands 1F (7pts), Japan 2F (5), Sweden 3rd (4). R32: Netherlands vs Morocco (M75), Brazil vs Japan (M76).
- Group D final: Australia 0-0 Paraguay → USA 1st, Australia 2D. Turkey beat USA 3-2 (dead rubber).
- 199448 Boston QF: France 0.34, Germany 0.12, Netherlands 0.11, Morocco 0.05, Canada 0.03 (Norway removed — now Miami path).
- 241292: France 0.18, Spain 0.15, England 0.12, Argentina 0.09, Brazil 0.08.
- Golden Boot: Messi 5; Mbappe/Haaland/Vinicius/Dembélé 4. Updated 201629: Messi 0.27, Mbappe 0.25, Vinicius 0.11, Haaland 0.10, Dembele 0.08. 581542: Mbappe 0.18, Messi 0.16, Dembele 0.08, Vinicius 0.07, Olise 0.05.
### Markets
- Kospi crash -5.8% June 26 (chip sell-off; SK Hynix -8.4%; Apple price hikes). SK Hynix ADR offering July 10 at risk of repricing/delay → 279946: SK Hynix 0.68, Alibaba 0.28.
- 329053: Nvidia 0.75, Alphabet 0.18, Apple 0.04.
- US-Iran 60-day ceasefire/framework; talks in Switzerland; Hormuz normalizing. Dollar strong on Fed hike bets.
### Group G/H finals (June 26 night, results June 27): Egypt-Iran, Belgium-NZ, Spain-Uruguay, Cape Verde-Saudi.

## Day 4 (2026-06-27) updates
### World Cup final group standings & R32 bracket
- Group G: Belgium 1st (5pts +4, beat NZ 5-1), Egypt 2nd (5pts +2, drew Iran 1-1), Iran 3rd (3).
- Group H: Spain 1st (7), Cape Verde 2nd (3, 3 draws — smallest nation ever in knockouts), Uruguay OUT (2), Saudi OUT (2).
- Group L: England 1st (7, beat Panama 2-0; Bellingham, Kane). 2L = Croatia or Ghana (Croatia-Ghana played June 27; BBC snippet suggests Croatia 3-1 Ghana → Croatia 2L).
- Group K: Colombia vs Portugal June 27 night (Colombia tops with draw; Portugal tops with win).
- Group J: Argentina vs Jordan, Austria vs Algeria June 27 night.
- CONFIRMED R32: M73 South Africa-Canada (Jun 28); M74 Germany-Paraguay (Jun 29 Boston); M75 Netherlands-Morocco (Jun 29/30 Monterrey); M76 Brazil-Japan (Jun 29 Houston); M77 France vs 3rd C/D/F/G/H (Jun 30 NY); M78 Ivory Coast-Norway (Jun 30 Dallas); M79 Mexico vs 3rd (Jun 30 Mexico City); M80 England vs 3rd (Jul 1 Atlanta); M81 USA-Bosnia (Jul 1 SF); M82 Belgium vs 3rd (Jul 1 Seattle); M83 2K-2L (Jul 2 Toronto); M84 Spain-Austria (Jul 2 LA); M85 Switzerland vs 3rd (Jul 2 Vancouver); M86 Argentina-Cape Verde (Jul 3 Miami); M87 1K vs 3rd (Jul 3 KC); M88 Australia-Egypt (Jul 3 Dallas).
- Argentina's path: Cape Verde → Australia/Egypt → KC QF vs Switzerland/(Colombia/Portugal). Very favorable.
- Updated: 457239 Argentina 0.44, Colombia 0.10, Portugal 0.09, Switzerland 0.09, Egypt 0.04.
- 439898: Argentina 0.24, Brazil 0.16, England 0.15, Portugal 0.07, Mexico 0.03.
- 241292: France 0.18, Spain 0.15, Argentina 0.11, England 0.11, Brazil 0.08.
- 592683: France 0.12, Spain 0.12, Argentina 0.10, England 0.08, Brazil 0.07.
- Kane scored vs Panama; tied Lineker at 10 career WC goals. Kane tournament goals ~3.
### Other
- No news yet on Kremlin funeral delegation (funeral July 4-9); no transfer updates; no Seahawks/Moldova updates.
- Typhoons Higos & Mekkhala passed Japan (not Bavi/Noul/Dolphin).

## Day 5 (2026-06-28) updates
### World Cup group stage COMPLETE
- Group K: Colombia 1st (7pts; 0-0 vs Portugal), Portugal 2nd (5), DR Congo 3rd (4, through). Group L: England 1st (7), Croatia 2nd (6), Ghana 3rd (4, through). Group J: Argentina 3 wins (beat Jordan 3-1; Messi scored 6th goal off bench). Austria/Algeria 2nd/3rd TBD (played June 27 late).
- R32: M80 England-DR Congo (Jul 1); M83 Portugal-Croatia (Jul 2 Toronto); M87 Colombia vs 3rd D/E/I/J/L (Jul 3 KC); M86 Argentina-Cape Verde (Jul 3 Miami); M84 Spain-Austria (Jul 2 LA); M88 Australia-Egypt (Jul 3 Dallas); M85 Switzerland vs 3rd E/F/G/I/J (Jul 2 Vancouver); M82 Belgium vs 3rd (Jul 1 Seattle); M79 Mexico vs 3rd (Jun 30 Mexico City); M77 France vs 3rd (Jun 30 NY); M78 Ivory Coast-Norway (Jun 30 Dallas); M76 Brazil-Japan (Jun 29 Houston); M75 Netherlands-Morocco (Jun 29/30); M74 Germany-Paraguay (Jun 29 Boston); M73 South Africa-Canada (Jun 28 LA).
- KC QF (M100) = (Argentina/Cape Verde vs Australia/Egypt) vs (Switzerland/3rd vs Colombia/3rd). Portugal now in LA path.
- Updated 457239: Argentina 0.46, Colombia 0.12, Switzerland 0.10, Egypt 0.04, Australia 0.03.
- Messi 6 goals (Golden Boot leader). Updated 201629: Messi 0.32, Mbappe 0.22, Vinicius 0.10, Haaland 0.09, Dembele 0.07. 581542: Messi 0.20, Mbappe 0.17.
- 241292: France 0.17, Spain 0.14, Argentina 0.13, England 0.11, Brazil 0.08.
### Middle East REVERSAL
- Iran-US MoU jeopardized: US struck Iran 2 days near Hormuz (Sirik, Bandar-e Lengeh, Qeshm); Iran attacked Bahrain & Kuwait; Israel resumed Lebanon strikes. → 339902: Iraq 0.50, Yemen 0.20, None 0.20. 246629: Bahrain 0.30, UAE 0.25, Saudi 0.15. 107175: None 0.35, US 0.15, Saudi 0.15. 817209: Oman 0.45.
- 942650 (Fed): None 0.32 (higher oil → more hike pressure). 461239: Oman 0.20, Bahrain 0.18, Japan 0.15.
### Tennis
- Wimbledon starts June 29. European heatwave (40°C+) — Sinner & Djokovic both struggle in heat. Adjusted 742225: Sinner 0.45, Zverev 0.14, Djokovic 0.11. 985440: Sinner 0.47, Djokovic 0.13, Zverev 0.13.
- Tour de France 2026 Grand Départ Barcelona July 4.

## Day 6 (2026-06-29) updates
### Wimbledon Day 1
- Sinner survived 5-set scare vs Kecmanovic (4-6 6-3 6-7(6) 6-2 6-3), bloodied foot, slip; looked vulnerable. Djokovic beat Wu in 4 sets; next Tsitsipas. Sabalenka cruised 6-2 6-3. Andreeva, Pegula, Gauff, Osaka, Muchova, Bencic advanced. Fernandez lost to Janice Tjen. Chwalinska lost.
- Updated 742225: Sinner 0.42, Zverev 0.15, Djokovic 0.12, Shelton 0.05, Fritz 0.04. 985440: Sinner 0.44, Zverev 0.14, Djokovic 0.14, FAA 0.07, Shelton 0.04. 846335: Sabalenka 0.23, Rybakina 0.16, Swiatek 0.14, Andreeva 0.11, Gauff 0.09.
### World Cup R32
- South Africa 0-1 Canada (June 28): Canada advances to face Netherlands/Morocco winner in R16 (M90). Boston QF path: France/Germany vs Canada/Netherlands/Morocco.
- R32 odds: Brazil -140 vs Japan; Germany -255 vs Paraguay; Netherlands +110 vs Morocco.
### NBA
- Jaylen Brown: Houston NOT in mix; Portland Blazers frontrunners (Kalshi 21%, double any other); Atlanta still trying; also Toronto, Denver, Brooklyn, Charlotte, Clippers. Updated 344207: Portland 0.35, Atlanta 0.15, Charlotte 0.08, Toronto 0.06, Denver 0.05.
### Seahawks
- First-round bids due June 29 (Bloomberg). Bidders: Grousbeck/Mittal, Khosla, Boehly. Sale expected before Sept 9 season opener; NFL approval possibly August. Keep 902592: Grousbeck/Mittal 0.33, Boehly 0.16, Khosla 0.15, Zuckerberg 0.08.
### Khamenei funeral
- Regional leaders confirmed/expected: Aliyev (Azerbaijan), Berdimuhamedow (Turkmenistan), Kavelashvili (Georgia), Pashinyan (Armenia), Qatar Emir, Pakistan PM Sharif (July 3), Afghanistan PM Akhund. NO Russia announcement yet. Funeral July 4-9 (Tehran Mosalla farewell July 4-5, Qom July 7, Najaf/Karbala July 8, Mashhad burial July 9).
- Keep 659176: Volodin 0.45, Putin 0.20, Lavrov 0.10, Peskov 0.06, Mishustin 0.05.
### Other
- Supreme Court 5-4 blocked Trump's attempt to fire Fed's Lisa Cook (June 29) — Cook remains.
- Enzo Maresca confirmed Man City manager (not Enzo Fernandez transfer).
- Iran-US: tanker struck in Hormuz, worst escalation since MoU; Israel strikes southern Syria near Golan.
- PFA: professional league still suspended; officials hope for scaled-down league after summer break (autumn).
- SK Hynix: Korea announced massive AI/chip investments June 29; Kospi volatile.

## Day 7 (2026-06-30) updates
### World Cup R32 upsets (huge)
- Germany 1-1 Paraguay (Paraguay win 4-3 pens) — GERMANY OUT.
- Netherlands 1-1 Morocco (Morocco win 3-2 pens) — NETHERLANDS OUT.
- Brazil 2-1 Japan (Martinelli 95'). Canada 1-0 South Africa (June 28).
- R16: Morocco vs Canada (Jul 6 Houston); Paraguay vs France/Sweden winner (Jul 4 Philadelphia); Brazil vs Norway/Ivory Coast (Jul 5 NJ).
- Boston QF (M97): France vs Morocco most likely. Updated 199448: France 0.40, Morocco 0.18, Canada 0.09, Paraguay 0.05, Sweden 0.02.
- 241292: France 0.19, Spain 0.15, Argentina 0.13, England 0.12, Brazil 0.09.
- 935518 (SF Dallas): France 0.30, Spain 0.27, Morocco 0.06, USA 0.04, Belgium 0.03.
### Wimbledon Day 2
- Ben Shelton OUT (lost to qualifier Otto Virtanen in 5 sets). Zverev survived Blockx in 4 tight sets. Fritz won (Draper withdrew). De Minaur, Bublik, Khachanov, Mensik advanced. Women: Swiatek, Rybakina advanced; Svitolina OUT (lost to Snigur).
- Updated 742225: Sinner 0.42, Zverev 0.17, Djokovic 0.12, Fritz 0.05, de Minaur 0.04. 985440: Sinner 0.45, Zverev 0.16, Djokovic 0.14, FAA 0.07, Fritz 0.04.
### Khamenei funeral (July 4-9)
- 90+ countries ready to attend; 30+ formal delegation requests. Regional leaders: Aliyev, Berdimuhamedow, Kavelashvili, Pashinyan, Qatar Emir, Pakistan PM (July 3), Afghanistan PM. No Russia announcement yet.
- Updated 659176: Volodin 0.42, Putin 0.22, Lavrov 0.10, Medvedev 0.06, Shoigu 0.04.
### Questions resolving July 1
- 344207 Jaylen Brown: Portland 0.35 (frontrunner), Atlanta 0.15, Charlotte 0.08, Toronto 0.06, Denver 0.05.
- 619176 PFA month: September 0.40, October 0.20, August 0.15, November 0.10, December 0.05.
- 659176: as above.
### Day 7 additional
- Women's T20 WC: India ELIMINATED (lost to Australia by 6 wkts, June 29). South Africa beat Bangladesh to advance. Semis: England vs South Africa; Australia vs West Indies (June 30). Final July 5.
- Updated 258607: Australia 0.55, England 0.23, South Africa 0.12, West Indies 0.08. 799550: Sciver-Brunt 0.24, Sutherland 0.20, Ecclestone 0.12, Gardner 0.09, Kapp 0.06.
- No SK Hynix pricing news; no Khamenei Russia announcement yet.

## Day 8 (2026-07-01) — FIRST RESOLUTIONS + lessons
### Resolved
- 344207 Jaylen Brown → **Philadelphia 76ers** (truth). My top: Portland 0.35. MISS. Brier -0.16. Lesson: NBA trade reporting favorites often wrong; spread wider (include more teams).
- 619176 PFA month → **September** (truth). My top: September 0.40. HIT. Brier +0.56, TW +56.5.
- 659176 Russian official → **Dmitry Medvedev** (truth). My top: Volodin 0.42; Medvedev was 5th at 0.06. MISS. Brier -0.12 (earlier forecast -0.255 before update). Lesson: for "which official" fields, spread more evenly; precedent (Volodin for Raisi) was misleading.
- Cumulative after 3: accuracy 0.4% (1/3), brier skill 0.001, TW score 17.81.
### Key updates July 1
- World Cup: France 3-0 Sweden (Mbappe brace, 6 goals); Norway 2-1 Ivory Coast (Haaland 5th goal); Mexico 2-0 Ecuador. R16: France-Paraguay (Jul 4 Philadelphia); Morocco-Canada (Jul 6 Houston); Brazil-Norway (Jul 5 NJ); Mexico vs England/DRC winner (Jul 5 Mexico City).
- Boston QF (M97, Jul 9) = France/Paraguay vs Morocco/Canada. Updated 199448: France 0.53, Morocco 0.25, Canada 0.12, Paraguay 0.08.
- 935518 (SF Dallas): France 0.33, Spain 0.29, Morocco 0.08, USA 0.04, Belgium 0.03.
- Golden Boot: Messi 6, Mbappe 6, Haaland 5. Updated 201629: Mbappe 0.30, Messi 0.28, Haaland 0.10, Vinicius 0.07, Dembele 0.05. 581542: Mbappe 0.22, Messi 0.18, Dembele 0.07, Vinicius 0.06, Olise 0.05.
- Wimbledon Day 3: Djokovic crushed Tsitsipas 6-3 6-4 6-2 (strong); Sinner beat Borges 7-6 7-6 6-4; FAA beat Prizmic; **Krejcikova beat Andreeva (OUT)**; Serena lost R1 to Maya Joint. Updated 742225: Sinner 0.42, Zverev 0.17, Djokovic 0.14, Fritz 0.05, de Minaur 0.04. 985440: Sinner 0.45, Djokovic 0.16, Zverev 0.16, FAA 0.07, Fritz 0.04. 846335: Sabalenka 0.24, Rybakina 0.18, Swiatek 0.16, Gauff 0.10, Osaka 0.05.
- Cyclospora: Michigan 174 cases June 22-30 (big outbreak). Updated 633052: Texas 0.32, Michigan 0.28, Ohio 0.08, NY 0.06, PA 0.04.
- Fed: Warsh at Sintra July 1 said "inflation risks have come down" → July hike odds down. Updated 942650: None 0.40, HKK 0.10.
- SK Hynix: Korea June exports +70.9% (chips +199.5%); AI boom intact. Keep 0.68.
- Khamenei funeral: Medvedev confirmed as Putin's special envoy (Iran ambassador, July 1).
### Upcoming resolutions
- Jul 4: 177324 (Trey Alexander two-way), 633052 (cyclospora)
- Jul 5: 258607 (Women's T20 WC final), 747581 (British GP), 799550 (POTM)
- Jul 7: 263626 (trade deficit May), 754639 (UK party leader)
- Jul 8: 213487 (Dugan sentencing), 76066 (Moldova PM)
- Jul 9: 107473 (UK university), 279946 (SK Hynix), 562262 (Eng-Ind T20)
- Jul 10: 446236 (Bavi evacuations), 985440 (Wimbledon first finalist)
- Jul 11: 457239 (KC QF), 66613 (Bavi landfall), 846335 (women's Wimbledon), 902592 (Seahawks)
- Jul 12: 742225 (men's Wimbledon), 897546 (MotoGP German GP)

## Day 9 (2026-07-02) updates
### World Cup R32
- England 2-1 DR Congo (Kane brace); Belgium 3-2 Senegal AET (Tielemans 125' pen); USA 2-0 Bosnia (Balogun red card).
- R16: England-Mexico (Jul 5 Mexico City); Belgium-USA (Jul 6 Seattle); Brazil-Norway (Jul 5 NJ); France-Paraguay (Jul 4 Philadelphia); Morocco-Canada (Jul 6 Houston).
- Jul 2: Spain-Austria, Portugal-Croatia, Switzerland-Algeria. Jul 3: Argentina-Cape Verde, Colombia-Ghana, Australia-Egypt.
### Wimbledon Day 4
- Zverev crushed Royer 6-1 6-3 7-6 (strong, open bottom half). Fritz, de Minaur, Cobolli, Bublik, Lehecka, Dimitrov advanced. Women: Rybakina crushed McNally, Swiatek crushed Pliskova, Anisimova, Keys, Kostyuk, Paolini, Navarro advanced; Shnaider out.
- Updated 742225: Sinner 0.40, Zverev 0.20, Djokovic 0.14, Fritz 0.05, de Minaur 0.04. 846335: Sabalenka 0.23, Rybakina 0.19, Swiatek 0.17, Gauff 0.10, Osaka 0.05.
### Women's T20 WC
- Final: Australia vs England (July 5, Lord's). Australia beat WI by 8 wkts; England beat SA by 40 runs (Sciver-Brunt 75, Knight 58).
- Updated 258607: Australia 0.58, England 0.42. 799550: Sciver-Brunt 0.25, Gardner 0.16, Mooney 0.12, Sutherland 0.10, Ecclestone 0.08.
### Cricket other
- England-India 1st T20 abandoned (rain; India 189-7). Series 0-0 with 4 matches left. Updated 562262: India 0.47, England 0.44, Drawn 0.06.
- Ben Stokes retired from international cricket (Test loss to NZ). Updated 971366: Tongue 0.22, Atkinson 0.20, Archer 0.18, Bashir 0.10, Robinson 0.06. 988210: McCullum 0.45, Trott 0.12.
### Iran-US
- Doha talks "positive progress"; communication channel established; talks pause during funeral (Jul 4-9), resume after. Iran to impose Hormuz transit fees after 60-day grace; Hormuz under "exclusive responsibility of Iran and Oman". Updated 817209: Oman 0.55.
### Moldova
- Munteanu very active July 1-2 (reorganizing PPA, state enterprise cleanup) — NOT resigning. 76066 likely void.

## Day 10 (2026-07-03) updates
### World Cup R32 (July 2 results)
- Spain 3-0 Austria (Oyarzabal brace, 4 goals); Portugal 2-1 Croatia (Ronaldo pen, Ramos 94'); Switzerland 2-0 Algeria.
- R16 (July 6 Dallas): SPAIN vs PORTUGAL (Iberian derby!). USA-Belgium (July 6 Seattle). Switzerland vs Colombia/Ghana (July 7 Vancouver).
- July 3 R32: Australia-Egypt, Argentina-Cape Verde, Colombia-Ghana.
- Updated 935518 (SF Dallas): France 0.32, Spain 0.24, Portugal 0.10, Morocco 0.08, USA 0.04.
- Updated 241292: France 0.20, Spain 0.13, Argentina 0.13, England 0.11, Brazil 0.09.
### Trey Alexander (177324, resolves July 4)
- Released by Pelicans (was on two-way); will play for Chicago Bulls in Summer League. Updated: Bulls 0.35, Pelicans 0.15, Denver 0.05, Orlando 0.04, Spurs 0.03.
### F1 British GP (July 5)
- Antonelli leads championship 171 pts after 8 rounds (5 wins). Russell WON Austria (round 8) and is 2nd. Hamilton 3rd (won Barcelona).
- British GP odds: Antonelli +175, Russell +200, Hamilton +450, Verstappen +650. Sprint qualifying: HAMILTON TOOK SPRINT POLE (0.011s over Antonelli); topped practice.
- Updated 747581: Antonelli 0.28, Russell 0.25, Hamilton 0.22, Verstappen 0.10, Leclerc 0.05.
- Updated 556116 (2nd in standings after Belgian GP): Russell 0.50, Hamilton 0.30, Antonelli 0.10. 594916 (Hungarian GP): Antonelli 0.30, Russell 0.24, Hamilton 0.20. 475441 (Hungarian FP): Antonelli 0.24, Russell 0.20, Hamilton 0.18.
### SK Hynix (279946, resolves July 10)
- Registration amended/resubmitted; offering size $29.47B unchanged; pricing not finalized (market-dependent). New antitrust class action risk factor. Keep 0.68.
### Other
- Khamenei funeral starts July 4; US-Iran talks resume after July 9.
- Tour de France starts July 4 (Barcelona).

## Day 11 (2026-07-04) updates
### Resolutions
- 177324 Trey Alexander → **Utah Jazz** (truth). My top: Bulls 0.35. MISS (Jazz unlisted). Brier -0.15, TW -26.38. Lesson: NBA two-way contracts are a 30-team lottery; spread wider.
- 633052 cyclospora → **Michigan** (truth). My 2nd pick at 0.28. HIT-ish. Brier +0.37, TW +15.05.
- Cumulative after 5: accuracy 0.4% (1/5), brier skill 0.002, TW 6.47.
### World Cup R32 COMPLETE
- Egypt 1-1 Australia (Egypt 4-2 pens); Argentina 3-2 Cape Verde AET (Messi 20th WC goal); Colombia 1-0 Ghana.
- R16: Canada-Morocco (Jul 4 Houston), Paraguay-France (Jul 5 Philadelphia), Brazil-Norway (Jul 6 NJ), Mexico-England (Jul 6 Mexico City), Portugal-Spain (Jul 7 Dallas), USA-Belgium (Jul 7 Seattle), Argentina-Egypt (Jul 7), Switzerland-Colombia (Jul 8 Vancouver).
- KC QF (M100) field is exactly Argentina/Egypt/Switzerland/Colombia. Updated 457239: Argentina 0.57, Switzerland 0.15, Colombia 0.15, Egypt 0.05.
### British GP (July 5)
- Antonelli WON the sprint and took POLE for the GP (1:28.111; Leclerc P2, Hamilton P3, Russell P4). Antonelli leads championship by 43 pts over Russell. Updated 747581: Antonelli 0.45, Hamilton 0.15, Leclerc 0.14, Russell 0.12, Verstappen 0.07.
### Resolving July 5
- 258607 (Women's T20 final Australia vs England): Australia 0.58, England 0.42.
- 799550 (POTM): Sciver-Brunt 0.25, Gardner 0.16, Mooney 0.12, Sutherland 0.10, Ecclestone 0.08.
- 747581: as above.

## Day 12 (2026-07-05) updates
### Resolutions
- 258607 Women's T20 WC → **Australia** (truth). My 0.58 top. Brier +0.65, TW +68.14. 
- 747581 British GP → **Charles Leclerc** (truth, from P3 on grid!). My Leclerc 0.14 (3rd). Brier +0.02, TW -21.39 (earlier forecast had him 0.05). Lesson: F1 polesitter ≠ winner; spread top teams more.
- 799550 POTM → **Beth Mooney** (truth). My Mooney 0.12 (3rd). Brier +0.12, TW -5.25.
- Cumulative after 8: accuracy 0.8% (2/8), brier skill 0.005, TW 47.96.
### World Cup R16 (July 4)
- Morocco 3-0 Canada; France 1-0 Paraguay (Mbappe pen, 7th goal of tournament).
- BOSTON QF (July 9) CONFIRMED: FRANCE vs MOROCCO. Updated 199448: France 0.62, Morocco 0.38.
- R16 July 5: Brazil-Norway; Mexico-England. July 6: Portugal-Spain; USA-Belgium. July 7: Argentina-Egypt; Switzerland-Colombia.
- Updated 935518 (SF Dallas): France 0.33, Spain 0.18, Morocco 0.15, Portugal 0.12, USA 0.05.
- Updated 439898 (SF Atlanta): Argentina 0.27, Brazil 0.17, England 0.15, Switzerland 0.07, Colombia 0.06.
- Updated 241292: France 0.23, Argentina 0.14, Spain 0.12, England 0.10, Brazil 0.09.
- Golden Boot: Messi 7, Mbappe 7. Updated 201629: Mbappe 0.32, Messi 0.30, Haaland 0.08, Vinicius 0.06, Dembele 0.04.
### Cricket
- England won 2nd T20 vs India by 4 wkts (Bethell 76*); series England 1-0 (1 abandoned). Updated 562262: England 0.60, India 0.35, Drawn 0.05.

## Day 13 (2026-07-06) updates
### World Cup R16 upsets
- NORWAY 2-1 BRAZIL (Haaland brace 79'/90'; Nyland saved Bruno pen) — Brazil OUT. Neymar retired from Brazil duty.
- ENGLAND 3-2 MEXICO (Bellingham brace, Kane pen; Quansah red) — Mexico OUT.
- MIAMI QF (July 11): ENGLAND vs NORWAY. July 6 R16: Portugal-Spain; USA-Belgium. July 7: Argentina-Egypt; Switzerland-Colombia.
- Updated 439898 (SF Atlanta): Argentina 0.25, England 0.25, Norway 0.13, Switzerland 0.06, Colombia 0.05.
- Updated 241292: France 0.25, Argentina 0.15, England 0.13, Spain 0.12, Portugal 0.08.
- Golden Boot: Messi 7, Mbappe 7, Haaland 7, Kane 6. Updated 201629: Mbappe 0.28, Messi 0.27, Haaland 0.20, Kane 0.09, Vinicius 0.03.
- Updated 592683: France 0.12, Spain 0.11, Argentina 0.10, England 0.09, Portugal 0.06.
### SK Hynix (279946, resolves July 10)
- Offering revised down to $28.14B (43.14T won) from $29.47B; oversubscribed; subscription closes July 8; pricing/trading July 10. Baillie Gifford/Coatue/Situational Awareness interested in up to $7B. Updated: SK Hynix 0.85, Alibaba 0.14.
### Resolving July 7
- 263626 trade deficit May: Taiwan 0.44, Vietnam 0.32, Mexico 0.18, China 0.04 (May data out July 7).
- 754639 UK party leader: no news; Farage 0.12, Starmer 0.08, Davey 0.08, Badenoch 0.05, Burnham 0.05.

## Day 14 (2026-07-07) updates
### Resolutions
- 263626 trade deficit May → **Vietnam** (truth). My 2nd pick at 0.32. Brier +0.31, TW +31.00.
- 754639 UK party leader → **Nigel Farage** (truth). My TOP pick at 0.12! Brier +0.21, TW +20.78.
- Cumulative after 10: accuracy 1.2% (3/10 top-1), brier skill 0.007, TW 99.74.
### World Cup R16 (July 6)
- SPAIN 1-0 PORTUGAL (Merino 90+1') — Ronaldo's WC career ends. BELGIUM 4-1 USA (De Ketelaere brace).
- LA QF (July 10): SPAIN vs BELGIUM. Boston QF (July 9): France vs Morocco. Miami QF (July 11): England vs Norway. KC QF: Argentina/Egypt vs Switzerland/Colombia (July 7 R16).
- Updated 935518 (SF Dallas): France 0.36, Spain 0.30, Morocco 0.17, Belgium 0.15.
- Updated 241292: France 0.26, Argentina 0.15, England 0.13, Spain 0.13, Morocco 0.06.
- Updated 592683: France 0.12, Spain 0.11, Argentina 0.10, England 0.09, Morocco 0.06.
### Moldova (76066, resolves July 8)
- Munteanu RESIGNED July 3 (MoldATSA corruption scandal). Sandu appointed Eugeniu Osmochescu acting PM from July 8. Parliament consultations ongoing; PAS has 55/101 majority. Opposition (PSRM, MAN) boycotting, demanding early elections.
- Updated 76066: Igor Grosu 0.28, Osmochescu 0.25, Recean 0.15, Popsoi 0.08, Nicu Popescu 0.06.
### Other
- 213487 Dugan sentencing July 8: Prison 0.50, Probation 0.28, Home detention 0.10, Fine 0.05.

## Day 15 (2026-07-08) updates
### Resolutions
- 213487 Dugan → **Monetary fine** (truth)! Extremely lenient sentence (Judge Adelman). My Fine 0.05 (4th). Brier -0.24, TW -24.09. Lesson: political-case federal sentencings can be non-custodial; don't over-weight "prison".
- 76066 Moldova → **Vasile Tofan** (truth). Not in my list (Grosu/Osmochescu/Recean). Brier -0.17, TW -16.49. Lesson: parliamentary PM picks can be outsiders; spread wider.
- Cumulative after 12: accuracy 1.2% (3/12), brier skill 0.006, TW 59.17.
### World Cup R16 complete
- Argentina 3-2 Egypt (Messi 8th goal, Enzo 90+3 winner); Switzerland 0-0 Colombia (SUI 4-3 pens).
- QF: Boston (Jul 9) France-Morocco; LA (Jul 10) Spain-Belgium; Miami (Jul 11) England-Norway; KC (Jul 11) Argentina-Switzerland.
- Updated 457239 (KC QF): Argentina 0.70, Switzerland 0.30.
### Cricket
- England won 3rd T20 vs India by 125 runs (India 76 all out; Tongue 4-28, Archer 3-29). England leads 2-0, 2 to play. Updated 562262: England 0.85, India 0.08, Drawn 0.07.
### Wimbledon (QF stage)
- Men: Sinner beat Struff; Djokovic beat FAA in 5h15m epic (7-6 3-6 6-3 6-7 7-6); Zverev beat Lehecka, plays Fritz in QF. SF: Sinner vs Djokovic (Friday Jul 10). Updated 742225: Sinner 0.40, Zverev 0.20, Djokovic 0.16, Fritz 0.07, Cobolli 0.03. 985440: Sinner 0.50, Djokovic 0.22, Zverev 0.12, Fritz 0.04.
- Women: SABALENKA OUT (lost to Osaka, who lost to Muchova). Gauff beat Pegula; Muchova beat Osaka. SF: Gauff vs Muchova; Swiatek vs Rybakina projected. Updated 846335: Swiatek 0.32, Rybakina 0.28, Gauff 0.22, Muchova 0.13.
### Typhoon Bavi
- Formed July 2; hit Guam; heading toward northern Taiwan and eastern mainland China by weekend (Jul 10-11). Expected to make landfall on eastern coast (Zhejiang/Fujian). Updated 66613: Zhejiang 0.35, Fujian 0.30, Jiangsu 0.08, Guangdong 0.07, Shanghai 0.05. 446236: Zhejiang 0.38, Fujian 0.30.
### Tour de France
- Stage 5 first bunch sprint: Olav Kooij WON (Kanter 2nd, Merlier 3rd, Philipsen 5th). Updated 24813 (stage 11): Kooij 0.26, Merlier 0.22, Philipsen 0.18, Kanter 0.07, Pedersen 0.05.
### Seahawks
- Bids due ~June 29-July 6; Khosla, Grousbeck/Mittal, Boehly in mix; no winner yet. Keep 902592 as is.

## Day 16 (2026-07-09) updates — ALL FOUR HITS!
### Resolutions (all correct top-1)
- 107473 UK university → **King's College London**. My 0.25 top. Brier +0.36, TW +35.87.
- 199448 Boston QF → **France** (beat Morocco). My 0.62. Brier +0.71, TW +62.35.
- 279946 SK Hynix → **SK Hynix**. My 0.85. Brier +0.96, TW +86.41.
- 562262 Eng-Ind T20 → **England** (led 2-0, series won). My 0.85. Brier +0.97, TW +54.76.
- Cumulative after 16: accuracy 2.8% (7/16 top-1), brier skill 0.017, TW 298.55.
### Wimbledon semifinals (July 10)
- MEN: Order of play — **Zverev vs Arthur Fery FIRST** (1:30pm), then Sinner vs Djokovic. So first finalist is almost certainly Zverev. Updated 985440: Zverev 0.85, Fery 0.06, Sinner 0.05, Djokovic 0.03.
- Updated 742225 (champion): Zverev 0.44, Sinner 0.36, Djokovic 0.18, Fery 0.02.
- WOMEN: Semifinals are Gauff vs Muchova and Noskova vs Kostyuk. SWIATEK AND RYBAKINA BOTH OUT! Updated 846335: Gauff 0.45, Muchova 0.24, Noskova 0.18, Kostyuk 0.13.
### Typhoon Bavi
- Landfall expected evening July 11 between Fuqing (Fujian) and Wenling (Zhejiang), after grazing northern Taiwan. Zhejiang activated Level-III response, evacuated 3,000+; national HQ dispatched 50,000 relief items to Zhejiang/Fujian. Updated 66613: Zhejiang 0.42, Fujian 0.42, Jiangsu 0.06. 446236: Zhejiang 0.45, Fujian 0.38.

## Day 17 (2026-07-10) updates
### Resolutions
- 446236 Bavi evacuations → **Zhejiang**. My 0.45 top. Brier +0.55, TW +38.71.
- 985440 Wimbledon first finalist → **Zverev**. My 0.85. Brier +0.97, TW +8.29.
- Cumulative after 18: accuracy 3.6% (9/18 top-1), brier skill 0.023, TW 345.55.
### Wimbledon
- Women's SF: MUCHOVA beat Gauff 6-2 1-6 7-6(10) (saved match point); NOSKOVA beat Kostyuk 6-4 6-4. Final (July 11): Muchova vs Noskova (all-Czech). Updated 846335: Muchova 0.55, Noskova 0.45.
- Men's SF July 10: Zverev vs Fery FIRST, then Sinner vs Djokovic. Results July 11.
### Seahawks (902592, resolves July 11)
- Down to TWO groups: Grousbeck/Mittal (frontrunner) and Khosla. Boehly OUT; Apostolopoulos OUT. Decision could come before Sept 9 opener. Updated: Grousbeck/Mittal 0.60, Khosla 0.38, Ballmer 0.02.
### Typhoon Bavi (66613, resolves July 11)
- Landfall evening July 11 between Fuqing (Fujian) and Wenling (Zhejiang) after grazing N Taiwan. Keep Zhejiang 0.42, Fujian 0.42.
### World Cup
- KC QF July 11: Argentina vs Switzerland. Keep Argentina 0.70, Switzerland 0.30.
- Other QFs: LA Spain-Belgium July 10 (result July 11); Miami England-Norway July 11.

## Day 18 (2026-07-11) updates
### Resolutions
- 457239 KC QF → **Argentina** (beat Switzerland). My 0.70. Brier +0.82, TW +69.46. HIT.
- 66613 Bavi landfall → **Zhejiang**. My 0.42 (tied top). Brier +0.48, TW +40.42. HIT.
- 846335 Women's Wimbledon → **Noskova** (beat Muchova in final). My Muchova 0.55/Noskova 0.45. Brier +0.39, TW -8.79 (earlier forecasts hurt).
- 902592 Seahawks → **Khosla Group**. My Grousbeck/Mittal 0.60. Brier -0.50, TW -18.58. MISS.
- Cumulative after 22: accuracy 4.0% (11/22 top-1), brier skill 0.028, TW 428.05.
### Wimbledon men's final (July 12)
- Sinner beat Djokovic 6-4 6-4 6-4; Zverev beat Fery 7-6 6-2 6-4. Final: Sinner vs Zverev. Updated 742225: Sinner 0.65, Zverev 0.35.
### MotoGP German GP (July 12)
- Marquez is Sachsenring king (12 career wins there) but recovering from injury (P7 at Assen). Martin leads championship; Bezzecchi crashed at Assen but will race; Ogura won Assen. Updated 897546: Marquez 0.40, Martin 0.18, Bezzecchi 0.15, Ogura 0.10, Acosta 0.08.
### World Cup QF results
- France 2-0 Morocco; Spain 2-1 Belgium (Merino 88'); England 2-1 Norway (Bellingham brace).
- SF1 (Dallas July 14): FRANCE vs SPAIN. Updated 935518: France 0.52, Spain 0.48.
- SF2 (Atlanta July 15): ENGLAND vs (Argentina/Switzerland, playing July 11). Updated 439898: England 0.48, Argentina 0.37, Switzerland 0.14.
- Updated 241292: France 0.29, Spain 0.25, England 0.22, Argentina 0.18, Switzerland 0.02.
- Updated 592683 (3rd place): France 0.14, Spain 0.14, England 0.12, Argentina 0.10, Switzerland 0.03.
- Golden Ball 581542: Mbappe 0.25, Messi 0.18, Bellingham 0.10, Yamal 0.08, Kane 0.06.
- Golden Boot 201629: Messi 0.34, Mbappe 0.33, Kane 0.12, Bellingham 0.05, Alvarez 0.03.

## Day 19 (2026-07-12) updates
### Resolutions
- 742225 Men's Wimbledon → **Sinner** (beat Zverev in final). My 0.65. Brier +0.76, TW +60.26. HIT.
- 897546 MotoGP German GP → **Marc Marquez**. My 0.40. Brier +0.57, TW +61.43. HIT.
- Cumulative after 24: accuracy 4.8% (13/24 top-1), brier skill 0.033, TW 549.74.
### World Cup QF: Argentina 3-1 Switzerland (AET)
- SF2 (Atlanta July 15): ENGLAND vs ARGENTINA confirmed. Updated 439898: England 0.52, Argentina 0.48.
- Updated 241292: France 0.28, Spain 0.25, England 0.24, Argentina 0.23.
- Updated 592683 (3rd place): Spain 0.26, Argentina 0.26, France 0.24, England 0.24.
- Golden Boot: Messi 8, Mbappe 8. Updated 201629: Mbappe 0.35, Messi 0.35, Kane 0.10, Bellingham 0.05, Alvarez 0.03.
### MLB All-Star (607314, July 14)
- Rosters: Ohtani (NL DH, leading vote-getter), Alvarez (AL DH), Judge INJURED (won't play), Guerrero Jr. won't play. Updated: Ohtani 0.18, Alvarez 0.15, Soto 0.09, Witt 0.08, Harper 0.07.
### Other
- 362674 TN-9 Trump endorsement: no endorsement as of July 10; Taylor has Jim Jordan, Blackburn, Hagerty, Scalise. Keep Taylor 0.78, Warner 0.14.
- 803035 NY data center moratorium: Hochul still hasn't signed as of July 9-10. Keep NY 0.62.
- 666563 China-DPRK: no news of Jo Yong Won talks with Chinese official in early July. Keep Zhao Leji 0.30.

## Day 20 (2026-07-13) updates
### Resolution
- 362674 TN-9 Trump endorsement → **Brent Taylor**. My 0.78. Brier +0.93, TW +93.20. HIT.
- Cumulative after 25: accuracy 5.2% (14/25 top-1), brier skill 0.037, TW 642.94.
### Open Championship (July 16-19, Royal Birkdale)
- Odds: Scheffler +750, McIlroy +850, Fleetwood +1800, Rahm +2000, Fitzpatrick +2000, Schauffele +2200. Scheffler missed cut at Scottish Open; McIlroy T7. Updated 32938 (leader after R2): Scheffler 0.12, McIlroy 0.12, Fleetwood 0.06, Rahm 0.05, Fitzpatrick 0.05.
### Resolving July 14
- 607314 MLB ASG MVP: Ohtani 0.18, Alvarez 0.15, Soto 0.09, Witt 0.08, Harper 0.07 (Judge injured/out).
- 666563 China-Jo Yong Won: Zhao Leji 0.30 (no news of talks).
- 803035 data centre moratorium: NY 0.62 (Hochul hasn't signed).
- 935518 SF Dallas: France 0.52, Spain 0.48.
### Resolving July 15
- 24813 TdF stage 11: Kooij 0.26, Merlier 0.22, Philipsen 0.18.
- 439898 SF Atlanta: England 0.52, Argentina 0.48.

## Day 21 (2026-07-14) updates
### Resolutions
- 607314 MLB ASG MVP → **Cody Bellinger**. Not listed. Brier -0.07, TW -6.85. Miss.
- 666563 China-Jo Yong Won → **Wang Huning**. My 0.10 (4th). Brier +0.04, TW +4.31.
- 803035 data centre moratorium → **New York**. My 0.62. Brier +0.84, TW +84.15. HIT.
- 935518 SF Dallas → **Spain** (beat France). My 0.48. Brier +0.46, TW +34.86.
- Cumulative after 29: accuracy 5.6% (16/29 top-1), brier skill 0.042, TW 759.40.
### Tour de France
- Sprint stages: Stage 5 Kooij won; Stage 7 Merlier; Stage 8 Merlier (back-to-back). Merlier is the form sprinter. Updated 24813 (stage 11, July 15): Merlier 0.35, Kooij 0.22, Philipsen 0.14, Girmay 0.07, Pedersen 0.05.
- GC: Pogacar leads Vingegaard by 2:42.
### Resolving July 15
- 439898 SF Atlanta: England 0.52, Argentina 0.48.

## Day 22 (2026-07-15) updates
### Resolutions
- 24813 TdF stage 11 → **Soren Waerenskjold**. Not listed. Brier -0.20, TW -15.57. Miss.
- 439898 SF Atlanta → **Argentina** (beat England 2-1). My 0.48. Brier +0.46, TW +37.28.
- Cumulative after 31: accuracy 5.6% (16/31 top-1), brier skill 0.043, TW 781.12.
### World Cup final & 3rd place
- FINAL (July 19): SPAIN vs ARGENTINA. Odds: Spain -156/-175 (~60%), Argentina +125/+134. Kalshi: Spain 58%. Updated 241292: Spain 0.60, Argentina 0.40.
- THIRD PLACE (July 18): FRANCE vs ENGLAND. Updated 592683: France 0.55, England 0.45.
- Golden Boot: Messi 8, Mbappe 8 (Mbappe done; Messi has final + likely tiebreak edge). Updated 201629: Messi 0.65, Mbappe 0.22, Kane 0.05, Bellingham 0.03, Alvarez 0.02.
- Golden Ball: Updated 581542: Messi 0.35, Yamal 0.15, Pedri 0.08, Mbappe 0.07, Bellingham 0.04.
### Referee (524604, resolves July 16)
- FIFA announcement expected July 16. Mirror favorites: Maurizio Mariani (Italy) and Slavko Vincic (Slovenia); Marciniak lower (did 2022 final). English refs OUT (conflict rules). Elfath (USA) also mentioned. Updated: Mariani 0.28, Vincic 0.24, Elfath 0.12, Marciniak 0.08, Barton 0.06.

## Day 23 (2026-07-16) updates
### Resolution
- 524604 Referee → **Slavko Vincic**. My 0.24 (2nd). Brier +0.32, TW +9.54.
- Cumulative after 32: accuracy 5.6% (16/32 top-1), brier skill 0.044, TW 790.65.
### Resolving July 17
- 329053 most valuable company: Nvidia $4.73T vs Apple $4.59T vs Alphabet ~$4.5T (July 10 data; gap narrowed). Updated: Nvidia 0.60, Alphabet 0.20, Apple 0.15, Microsoft 0.04, Amazon 0.01.
- 32938 Open R2 leader: keep Scheffler 0.12, McIlroy 0.12, Fleetwood 0.06, Rahm 0.05, Fitzpatrick 0.05.
- 425213 Gaza deadliest strike July 17: recent strikes in Deir al-Balah, Gaza City, Khan Younis. Updated: Gaza City 0.27, Khan Younis 0.25, Deir al-Balah 0.18, Jabalia 0.08, Rafah 0.07.
### Upcoming
- July 18: 26225 (Rogers→Arsenal?), 592683 (3rd place France-England), 674079 (UFC du Plessis-Usman), 906651 (mile WR London DL).
- July 19: 201629, 241292 (final Spain-Argentina), 556116 (F1 2nd after Belgian GP), 581542, 927657.
- July 20: 605397 (Section 338).

## Day 24 (2026-07-17) updates
### Resolutions (all misses)
- 329053 most valuable company → **Apple** (overtook Nvidia). My Nvidia 0.60. Brier -0.12, TW -50.34. Lesson: market-cap gaps of 3% are too close for 0.60 confidence.
- 32938 Open R2 leader → **Lucas Herbert**. Not listed. Brier -0.04, TW -4.52. Lottery.
- 425213 Gaza deadliest strike → **Nuseirat refugee camp**. Not listed. Brier -0.18, TW -17.98. Lesson: include refugee camps (Nuseirat, Bureij, Maghazi) in Gaza locality lists.
- Cumulative after 35: accuracy 5.6% (16/35 top-1), brier skill 0.043, TW 717.81.
### Resolving July 18
- 26225 Morgan Rogers: Arsenal preparing first bid ~£105m (Villa want £130m); personal terms finalized; Rogers wants Arsenal. Keep Arsenal 0.85.
- 592683 3rd place: France 0.55, England 0.45.
- 674079 UFC: du Plessis 0.72, Usman 0.26.
- 906651 Mile WR: Josh Kerr's dedicated record attempt (Project 222, pacemakers, ideal conditions, 3:42 target) confirmed for July 18. PB 3:45.34 vs record 3:43.13. Updated: Kerr 0.45, El Guerrouj 0.53, Nuguse 0.02.

## Day 25 (2026-07-18) updates
### Resolutions
- 26225 Morgan Rogers → **CHELSEA** (not Arsenal!). My 0.85 Arsenal. Brier -0.65, TW -64.70. Big miss — "done deal" reporting flipped.
- 592683 3rd place → **England** (beat France). My 0.45. Brier +0.39, TW +16.80.
- 674079 UFC → **du Plessis**. My 0.72. Brier +0.85, TW +85.40. HIT.
- 906651 Mile WR → **Josh Kerr** (broke El Guerrouj's record!). My 0.45. Brier +0.42, TW +24.99.
- Cumulative after 39: accuracy 6.0% (17/39 top-1), brier skill 0.047, TW 780.31.
### Resolving July 19
- 241292 WC final: Spain 0.60, Argentina 0.40.
- 201629 Golden Boot: Messi 0.65, Mbappe 0.22.
- 581542 Golden Ball: Messi 0.35, Yamal 0.15.
- 556116 F1 2nd after Belgian GP: standings Antonelli 179, Russell 154, Hamilton 147. Updated: Russell 0.55, Hamilton 0.35, Antonelli 0.06, Norris 0.02, Leclerc 0.02.
- 927657 Syria NSB: Al-Salama appointed head of National Security (Al-Tahhan to General Intelligence). Updated: Al-Salama 0.65, Al-Tahhan 0.12, Khattab 0.08, Arnaout 0.05, Al-Soufi 0.03.

## Day 26 (2026-07-19) updates
### Resolutions
- 201629 Golden Boot → **Kylian Mbappe** (not Messi; tie at 8 goals, Mbappe won tiebreak). My Messi 0.65. Brier -0.03, TW +31.09.
- 241292 World Cup → **SPAIN** (beat Argentina in final). My 0.60. Brier +0.68, TW +27.02. HIT.
- 556116 F1 2nd after Belgian GP → **Lewis Hamilton**. My 0.35 (2nd). Brier +0.27, TW +37.36.
- 581542 Golden Ball → **Rodri** (Spain). Not listed. Brier -0.16, TW -10.22. Miss.
- 927657 Syria NSB → **Anas Khattab**. My 0.08 (3rd) but TW +42.54 (earlier forecast had Khattab 0.35).
- Cumulative after 44: accuracy 6.3% (18/44 top-1), brier skill 0.049, TW 908.10.
### Ukraine commander (249565, resolves July 21)
- Defense Minister Fedorov dismissed; nationwide protests; FT: Zelensky considering dismissing Syrsky. Possible successors: Drapatyi (leading), Hnatov, Skybiuk, Brovdi; corps commanders interviewed. Ukrainska Pravda: no appointment discussion yet; LIGA: Zelensky chose Syrsky for now (front collapse risk). Updated: Drapatyi 0.35, Budanov 0.18, Hnatov 0.12, Skybiuk 0.06, Brovdi 0.04.
### Section 338 (605397, resolves July 20)
- No news. Keep India 0.14, Brazil 0.12, China 0.12, Mexico 0.10, Vietnam 0.05.

## Day 27 (2026-07-20) updates
### LeBron (981188, resolves July 24)
- CERTAIN: LeBron plays a 24th season but NOT for the Lakers. Shortlist: Cavaliers, Warriors, Heat, 76ers, Nuggets, Timberwolves. Narrowed to 3: Cavaliers, Heat, 76ers; Warriors dark horse. Decision "imminent" (July 16-18). Updated: Cavaliers 0.35, 76ers 0.25, Heat 0.18, Warriors 0.12, Nuggets 0.05.
### Typhoon Bavi aftermath
- Bavi made landfall at Yuhuan, Zhejiang (July 11, 23:20), second landfall Wenzhou. My 66613 Zhejiang resolved correctly.
### Typhoon Noul (442417, resolves July 21)
- No news; not yet formed. Keep Fujian 0.27, Guangdong 0.26, Zhejiang 0.22.

## Day 28 (2026-07-20) updates
### Resolution
- 605397 Section 338 → **Canada**. Not listed. Brier -0.06, TW -6.09. Miss (US-Canada trade tension was an obvious candidate).
- Cumulative after 45: accuracy 6.3% (18/45 top-1), brier skill 0.049, TW 902.01.
### Ukraine commander (249565, resolves July 21)
- Drapatyi now THE leading candidate (Bloomberg/UP/FT; protesters chant his name; met Zelensky twice). Syrsky could be fired within days; 11 candidates considered. Others: Apostol (Syrsky's preferred), Horbatiuk, Biletsky, Prokopenko. Budanov now Head of President's Office (not candidate). Updated: Drapatyi 0.55, Apostol 0.12, Horbatiuk 0.08, Biletsky 0.06, Prokopenko 0.04.
### Typhoon Noul (442417, resolves July 21)
- Not yet formed/no news. Keep Fujian 0.27, Guangdong 0.26, Zhejiang 0.22.

## Day 29 (2026-07-21) updates
### Resolutions
- 249565 Ukraine commander → **Mykhailo Drapatyi**. My 0.55. Brier +0.77, TW -3.13 (earlier forecasts had him 0.12).
- 442417 Typhoon Noul → **Guangdong**. My 0.26 (2nd). Brier +0.32, TW +31.86.
- Cumulative after 47: accuracy 6.7% (19/47 top-1), brier skill 0.053, TW 930.74.
### India monsoon floods (872064, resolves July 22)
- Current: J&K 15 dead (Poonch/Rajouri), Nagaland 9, Kerala 7, Assam 6+ (3.63 lakh affected, worsening), Gujarat 17 (Surat), Uttarakhand 2. IMD: active monsoon in north/east/NE for 6-7 more days. Updated 872064: Assam 0.28, Kerala 0.15, J&K 0.12, Maharashtra 0.12, Himachal 0.08.

## Day 30 (2026-07-22) updates
### Resolution
- 872064 India floods → **Assam**. My 0.28. Brier +0.42, TW +40.58. HIT.
- Cumulative after 48: accuracy 7.1% (20/48 top-1), brier skill 0.055, TW 971.31.
### European wildfires (149811, resolves July 23)
- Portugal declared "state of alert" July 3-6 (wildfire risk); activated EU mechanism. Spain: Almeria fire killed 12+ (July 9-11). France/Greece major fires; EU pre-positioned record crews. Updated: Portugal 0.32, Spain 0.28, Greece 0.15, Italy 0.09, France 0.07.
### India-Zimbabwe T20 (131869, resolves July 23)
- No news yet. Keep Abhishek Sharma 0.30, Sooryavanshi 0.15, Iyer 0.12.

## Day 31 (2026-07-23) updates
### Resolutions
- 131869 India half-century → **Vaibhav Sooryavanshi**. My 0.15 (2nd). Brier +0.15, TW +15.31.
- 149811 European wildfire emergency → **Spain**. My 0.28 (2nd). Brier +0.34, TW +35.30.
- Cumulative after 50: accuracy 7.1% (20/50 top-1), brier skill 0.057, TW 1021.93.
### LeBron (981188, resolves July 24)
- Still undecided as of July 23. Kalshi: Heat 46%, Cavs 27%, Warriors 17%, 76ers 8%. Heat planned (erroneous?) July 27 intro presser. Decision expected before end of July. Updated: Heat 0.42, Cavs 0.28, Warriors 0.15, 76ers 0.10, Nuggets 0.03.
### Resolving July 24
- 126882 OPCW: Aerial bombs 0.45, Rockets 0.30.
- 45561 Commonwealth gymnastics: England 0.75.
- 617889 Vozinha: Athletic MG 0.20, Ceara 0.10, Chaves 0.10.

## Day 32 (2026-07-24) updates
### Resolutions
- 126882 OPCW → **Aerial bombs**. My 0.45. Brier +0.60, TW +59.82. HIT.
- 45561 Commonwealth gymnastics → **Canada** (England 0.75 favorite lost). Brier -0.42, TW -41.63. Miss.
- 617889 Vozinha → **Colo-Colo**. Not listed. Brier -0.07, TW -7.28. Miss.
- 981188 LeBron → **Philadelphia 76ers**! My 0.10 (4th; Heat were favorites). Brier -0.09, TW -30.79. Miss.
- Cumulative after 54: accuracy 7.5% (21/54 top-1), brier skill 0.057, TW 1002.05.
### F1
- Belgian GP (July 19): **Antonelli WON** (Russell out). Hungarian GP July 26.
- Updated 475441 (Hungarian FP): Antonelli 0.28, Russell 0.20, Hamilton 0.17, Verstappen 0.08, Leclerc 0.06.
- 918398 Bahrain replacement: **Sepang (Malaysia)** leading candidate; Suzuka, Portimao also mentioned. Decision expected before August break. Updated: Sepang 0.45, Portimao 0.15, Suzuka 0.10, Bahrain 0.10, Imola 0.05.

## Day 33 (2026-07-25) updates
### Resolutions
- 475441 Hungarian FP → **Lando Norris**. Not in top-5. Brier -0.16, TW -8.26. Miss.
- 918398 Bahrain replacement → **Sepang**. My 0.45. Brier +0.65, TW -9.26 (earlier had Sepang unlisted). HIT.
- Cumulative after 56: accuracy 7.9% (22/56 top-1), brier skill 0.059, TW 984.53.
### Hungarian GP (594916, resolves July 26)
- Qualifying: NORRIS POLE (1:17.207); Hamilton P2 but 3-place penalty → P5; Leclerc P2; Piastri P3; Verstappen P4; Antonelli P4 but 3-place penalty → P7; Russell P8. McLaren upgrade package working. Updated: Norris 0.35, Leclerc 0.17, Hamilton 0.14, Piastri 0.12, Verstappen 0.08.
### Diomande (696503, resolves July 26)
- Liverpool's $115M offer rejected; Diomande CHOSE PSG (personal terms to 2031); PSG no formal bid yet; Real Madrid bid $101M+$12M rejected; Leipzig want €120M. Updated: PSG 0.55, Liverpool 0.15, Real Madrid 0.12, Arsenal 0.08, Man City 0.05.

## Day 34 (2026-07-26) updates
### Resolutions
- 594916 Hungarian GP → **Lando Norris** (pole → win). My 0.35. Brier +0.51, TW -13.80 (earlier forecasts had Norris low).
- 696503 Diomande → **Real Madrid** (not PSG!). My PSG 0.55. Brier -0.11, TW -40.55. Miss — "chose PSG" reporting flipped.
- Cumulative after 58: accuracy 8.3% (23/58 top-1), brier skill 0.060, TW 930.18.
### Resolving July 27
- 179451 WI bowler five-for 1st Test Tarouba (started July 25): predicted WI XI: Chanderpaul, King, Hodge, Jangoo, Chase, Hope, Greaves, Roach, Shamar Joseph, Seales, Warrican. Updated: Seales 0.28, Shamar Joseph 0.22, Warrican 0.14, Roach 0.08, Greaves 0.04.
- 415011 Peru FM: Fujimori's first cabinet sworn in July 28. Rumored (voiced, not confirmed) FM: **Carlos Espá**. Current FM Carlos Pareja handling transition. Updated: Espá 0.40, Pareja 0.20, de Zela 0.10.

## Day 35 (2026-07-27) updates
### Resolutions
- 179451 WI bowler five-for → **Justin Greaves** (my 5th pick 0.04). Brier -0.07, TW -16.23. Miss.
- 415011 Peru FM → **Carlos Espá**. My 0.40. Brier +0.58, TW -15.92 (earlier unlisted). HIT.
- Cumulative after 60: accuracy 8.7% (24/60 top-1), brier skill 0.062, TW 898.03.
### Middle East
- US has conducted 13 nights of strikes on IRAN itself (not proxies); US-Iran war appears to pause July 27 for talks. Houthis attacked Saudi tankers, threatened Bab el-Mandeb closure; Saudi-led coalition vowed to protect shipping. EU bolstered Aspides (Djibouti SOFA).
- Updated 339902 (US strikes outside Iran July 22-29): None 0.35, Yemen 0.32, Iraq 0.27, Syria 0.04.
- Updated 107175 (new maritime coalition by Aug 1): None 0.32, US 0.20, Saudi 0.18, Egypt 0.10, France 0.05.

## Day 36 (2026-07-28) updates
### Resolution
- 339902 US strikes → **Iraq**. My 0.27 (3rd). Brier +0.24, TW +64.41 (earlier had Iraq 0.55). 
- Cumulative after 61: accuracy 8.7% (24/61 top-1), brier skill 0.063, TW 962.44.
### Resolving July 29
- 942650 FOMC: market 68.5% hold / 31.5% hike; Citadel expects hike; Warsh wants "family fight". Keep None 0.40, HKK 0.10, HK 0.06, KL 0.05, K 0.04.
- 971524 Myanmar refugees: Bangladesh established national repatriation committee. Keep Bangladesh 0.55.
- 107175 maritime coalition: keep None 0.32, US 0.20, Saudi 0.18.
- 988210 England Test coach: keep McCullum 0.45.

## Day 37 (2026-07-29) updates
### Resolutions
- 107175 maritime coalition → **Saudi Arabia**. My 0.18 (3rd). Brier +0.17, TW +11.43.
- 942650 FOMC → **"Hammack, Kashkari, Logan"** (exact match!). My 0.10 (2nd). Brier +0.02, TW +2.89. (Fed held; three hawks dissented for hike.)
- 971524 Myanmar refugees → **Malaysia**. My 0.12 (3rd). Brier -0.14, TW -14.19. Miss.
- 988210 England coach → **Stephen Fleming**. Not listed. Brier -0.23, TW -23.82. Miss.
- Cumulative after 65: accuracy 8.7% (24/65 top-1), brier skill 0.063, TW 938.76.
### Resolving July 30
- 238968 UN SG straw poll: candidates Grossi, Bachelet, Grynspan, Espinosa, Rodrigues-Birkett, Sall, Otunnu. Grossi most-mentioned frontrunner. Updated: Grossi 0.45, Grynspan 0.25, Rodrigues-Birkett 0.12, Bachelet 0.08, Sall 0.04.
- 970163 CWG javelin qualification: field has Pathirage (92.62 SB), Chopra (85.69), Rohit Yadav (87.05), Peters (86.38), Walcott, Nadeem (78.47). Updated: Pathirage 0.42, Chopra 0.20, Rohit Yadav 0.08, Peters 0.06, Walcott 0.05.
- 683823 nuclear shutdown drought: ROMANIA Cernavodă reactor offline (its only NPP; 2nd may follow); Hungary Paks output cut (only NPP); Slovenia Krško full power; France 3 plants temp shutdown. Updated: Romania 0.45, Hungary 0.15, Slovenia 0.10, France 0.08, Spain 0.05.

## Day 38 (2026-07-30) updates
### Resolutions
- 238968 UN SG straw poll → **Rebeca Grynspan**. My 0.25 (2nd). Brier +0.21, TW +22.30.
- 683823 nuclear shutdown → **Hungary** (Paks, its only NPP, output cut). My 0.15 (2nd). Brier +0.06, TW -15.21.
- 970163 CWG javelin qual → **Pathirage**. My 0.42. Brier +0.61, TW +47.98. HIT.
- Cumulative after 68: accuracy 9.1% (25/68 top-1), brier skill 0.066, TW 993.84.
### Resolving July 31
- 108618 Bruno Guimaraes: Arsenal close to agreeing ~£70m+ deal; personal terms agreed; Guimaraes wants Arsenal. Updated: Arsenal 0.75, Newcastle 0.10, Man City 0.06, Man Utd 0.04, Chelsea 0.03.
- 449245 CWG javelin final (July 31): qual standings Pathirage 82.84, Peters 81.29, Smit 80.64, East 80.38, Chopra 79.61, Nadeem 78.63. Updated: Pathirage 0.45, Chopra 0.28, Peters 0.08, Nadeem 0.05, Walcott 0.03.

## Day 39 (2026-07-31) updates
### Resolutions
- 108618 Bruno Guimaraes → **Arsenal**. My 0.75. Brier +0.92, TW +41.90. HIT.
- 449245 CWG javelin → **Pathirage**. My 0.45. Brier +0.61, TW +51.12. HIT.
- Cumulative after 70: accuracy 9.9% (27/70 top-1), brier skill 0.072, TW 1086.85.
### Resolving Aug 1
- 805635 Skubal trade (deadline Aug 3): Passan says WILL be traded; DODGERS favorites; Brewers/Rays next; Braves/Cubs. Updated: Dodgers 0.45, Brewers 0.20, Rays 0.12, Braves 0.08, Cubs 0.05.
- 481741 ICE arrests month: no news; keep January 0.62, February 0.12, March 0.08.

## Day 40 (2026-08-01) updates
### Resolution
- 805635 Skubal → **Dodgers**. My 0.45. Brier +0.63, TW +16.77. HIT.
- Cumulative after 71: accuracy 10.3% (28/71 top-1), brier skill 0.075, TW 1103.63.
### Resolving Aug 2
- 481741 ICE arrests: keep January 0.62.
- 992842 Rocket Classic: R3 leaders Cameron Young (-10), Michael Brennan, Davis Riley, Rickie Fowler T4. Updated: Young 0.28, Riley 0.18, Brennan 0.15, Fowler 0.10, Bhatia 0.04.
- 356778 DC Open men (Aug 2): top seeds de Minaur, Shelton, Fritz, Musetti, Tien, Tiafoe, Mensik, Fils. Updated: de Minaur 0.20, Fritz 0.16, Shelton 0.15, Tiafoe 0.06, Mensik 0.05.
- 443143 DC Open women: seeds Pegula, Svitolina, Osaka, Shnaider, Kalinskaya, Keys, Fernandez, Navarro. Updated: Pegula 0.25, Svitolina 0.18, Osaka 0.15, Keys 0.08, Shnaider 0.06.

## Day 41 (2026-08-02) updates
### Resolutions
- 481741 ICE arrests → **July** (not January). My January 0.62. Brier -0.35, TW -34.77. Miss.
- 992842 Rocket Classic → **Michael Thorbjornsen**. Not listed. Brier -0.14, TW -2.81. Miss.
- Cumulative after 73: accuracy 10.3% (28/73 top-1), brier skill 0.073, TW 1066.05.
### Resolving Aug 3
- 356778 DC Open men: SFs Fritz vs Nakashima; Tabilo vs Jodar (de Minaur, Shelton, Musetti all out). Updated: Fritz 0.45, Nakashima 0.20, Tabilo 0.18, Jodar 0.12.
- 443143 DC Open women: Final PEGULA vs EALA (Eala beat Osaka and Svitolina). Updated: Pegula 0.65, Eala 0.35.
- 709570 Aung San Suu Kyi: Myanmar DENIED ASEAN envoy access (2nd refusal); Thailand pressing. Updated: No org 0.30, ASEAN 0.28, ICRC 0.18, UN 0.15.

## Day 42 (2026-08-03) updates
### Resolutions
- 356778 DC Open men → **Fritz**. My 0.45. Brier +0.61, TW +27.03. HIT.
- 443143 DC Open women → **Eala** (beat Pegula). My 0.35 (2nd). Brier +0.15, TW -6.07.
- 709570 Aung San Suu Kyi → **ICRC**. My 0.18 (3rd). Brier +0.14, TW +20.33.
- Cumulative after 76: accuracy 10.7% (29/76 top-1), brier skill 0.076, TW 1107.34.
### Resolving Aug 4
- 810891 Salah: Al-Ittihad deal imminent ($25M/yr; Besiktas talks collapsed). Updated: Al-Ittihad 0.65, Fenerbahce 0.08, Besiktas 0.08, San Diego FC 0.08, Al Qadsiah 0.03.
- 716751 Kansas Dem Senate primary (Aug 4): Hamilton 30% internal poll (Davis 13, Taylor 10, Schmidt 5). Keep Hamilton 0.80.
- 33659 Shehadeh archive: low info; keep Columbia 0.15, Oxford 0.15.
- 576510 RSF commander: low info; keep Ali Yagoub 0.25.
- 817209 Hormuz mines: keep Oman 0.55.
- 946660 Sarah Khalifa: trial ongoing; prosecution demands death; court could go life or death. Keep Life 0.45, Death 0.25.

## Day 43 (2026-08-04) updates
### Resolutions
- 33659 Shehadeh archive → **University of Edinburgh**. Not listed. Brier -0.07, TW -7.50.
- 576510 RSF commander → **Mahdi Adam**. Not listed. Brier -0.10, TW -10.50.
- 716751 Kansas Dem Senate → **Adam Hamilton**. My 0.80. Brier +0.94, TW +94.40. HIT.
- 810891 Salah → **Trabzonspor** (not Al-Ittihad!). My 0.65. Brier -0.44, TW -19.21. Miss.
- 817209 Hormuz mines → **Oman**. My 0.55. Brier +0.78, TW +77.66. HIT.
- 946660 Sarah Khalifa → **Death penalty**. My 0.25 (2nd). Brier +0.21, TW +21.50.
- Cumulative after 82: accuracy 11.5% (32/82 top-1), brier skill 0.082, TW 1263.69.
### Resolving Aug 5
- 883794 Michigan Dem Senate primary (Aug 4): El-Sayed leads 52-38 (Mitchell), 54-39 (Emerson), 54.8-45.2 (TPSI); markets 97%. Updated: El-Sayed 0.90, Stevens 0.08.
- 920782 WI-Pak 2nd Test (Queen's Park Oval): WI won 1st Test by 90 runs (Seales 5-20); WI unbeaten in last 6 Tests at venue. Updated: West Indies 0.55, Pakistan 0.32, Draw 0.13.

## Day 44 (2026-08-05) updates
### Resolutions
- 883794 Michigan Dem Senate → **El-Sayed**. My 0.90. Brier +0.98, TW +88.16. HIT.
- 920782 WI-Pak 2nd Test → **Pakistan** (levelled series). My 0.32 (2nd). Brier +0.22, TW +42.25.
- Cumulative after 84: accuracy 11.9% (33/84 top-1), brier skill 0.086, TW 1394.10.
### Resolving Aug 6
- 243962 Rodri: Real Madrid deal "effectively in place," final formalities; expected within week. Updated: Real Madrid 0.85, Bayern 0.03, Atletico 0.02, Barcelona 0.02.
- 874628 TN-5 GOP primary: Ogles leads Hatcher 36.9-32.7 (within MOE), 30%+ undecided; Hatcher has Haslam endorsement, more cash, $2M PAC. Trump endorsed Ogles. Updated: Ogles 0.55, Hatcher 0.45.
- 202511 Ye Win Oo: no news; keep India 0.35.
- 723378 Parker: no news; keep contaminated supplement 0.25.

## Day 45 (2026-08-06) updates
### Resolutions
- 202511 Ye Win Oo → **Thailand**. My 0.10 (4th). Brier -0.01, TW -0.50.
- 243962 Rodri → **BARCELONA** (not Real Madrid!). My 0.85. Brier -0.68, TW -22.69. Big miss.
- 723378 Parker → **His nutritionist**. Not listed. Brier -0.13, TW -13.25.
- 874628 TN-5 → **Charlie Hatcher** (beat Ogles). My 0.45 (2nd). Brier +0.39, TW -63.19.
- Cumulative after 88: accuracy 11.9% (33/88 top-1), brier skill 0.085, TW 1294.46.
### Resolving Aug 7
- 685197 AJK Aug 10 polling: Poonch division = Rawalakot, Sudhnoti, Bagh, Haveli districts (+ LA-24). Updated: "Rawalakot, Sudhnoti, Bagh and Haveli" 0.55, "Rawalakot and Sudhnoti" 0.10, "Bagh and Haveli" 0.08.
- 687277 July jobs sector: ADP shows leisure/hospitality -11k, trade/transport -8k, mining -6k; financial +10k, prof +9k. Updated: Leisure 0.28, Trade 0.22, Financial 0.12, Professional 0.10, Government 0.08.

## Day 46 (2026-08-07) updates
### Resolutions
- 685197 AJK Aug 10 → **"Bagh and Haveli"** (subset). My 0.08 (3rd). Brier -0.17, TW -22.86.
- 687277 July jobs sector → **Government**. My 0.08 (5th). Brier +0.00, TW +21.10 (earlier had 0.17).
- Cumulative after 90: accuracy 11.9% (33/90 top-1), brier skill 0.084, TW 1292.70.
### Resolving Aug 8
- 251083 aid boat Kate: keep London 0.30, Bristol 0.20, Southampton 0.20.
- 72574 Solomon: agent wants permanent exit from Spurs; Fiorentina declined €10M option; West Ham held talks; Leeds/Hull interested; Spurs value €10M. Updated: West Ham 0.30, Fiorentina 0.20, Leeds 0.18, Hull City 0.07, Crystal Palace 0.05.
- 737715 Typhoon Dolphin: forecast landfall between southern Zhejiang and northern Fujian (Wenzhou reference), Aug 9 afternoon-Aug 10 morning. Updated: Wenzhou 0.30, Taizhou 0.18, Fuzhou 0.15, Ningde 0.10, Fuding 0.05.

## Day 47 (2026-08-08) updates
### Resolutions
- 251083 aid boat Kate → **Bristol**. My 0.20 (2nd). Brier +0.21, TW +21.00.
- 72574 Solomon → **West Ham**. My 0.30 top. Brier +0.43, TW -22.02 (earlier unlisted).
- 737715 Typhoon Dolphin → **Yuhuan** (Taizhou county-level city). Not listed. Brier -0.16, TW -7.98.
- Cumulative after 93: accuracy 12.3% (34/93 top-1), brier skill 0.086, TW 1283.71.
### Resolving Aug 9
- 259947 MotoGP British GP: standings Martin 208, Ogura 194, Marquez 190, Bezzecchi 186, Di Giannantonio 184. Silverstone: 11 different winners in last 11 editions; Marquez only won there in 2014 (weak track); Bezzecchi won 2025 but returning from collarbone/knee surgery (13 pts in last 4 rounds); Aprilia favored. Updated: Martin 0.24, Bezzecchi 0.18, Ogura 0.15, Marquez 0.13, Di Giannantonio 0.08.

## Day 48 (2026-08-09) updates
### Resolution
- 259947 MotoGP British GP → **Raul Fernandez** (11th different winner in 11 Silverstone editions). Not listed. Brier -0.14, TW -20.20.
- Cumulative after 94: accuracy 12.3% (34/94 top-1), brier skill 0.085, TW 1263.50.
### Resolving Aug 10
- 112235 Golan recognition: no news. Keep Argentina 0.30, Paraguay 0.20, Honduras 0.15, Guatemala 0.10, Czechia 0.05.
### Aug 11
- 49405 Alabama 2nd GOP special primary: 6 candidates, no runoff, Marques frontrunner (Trump, Britt endorsements). Keep Marques 0.80.

## Day 49 (2026-08-10) updates
### Resolution
- 112235 Golan → **Colombia**. Not listed. Brier -0.17, TW -16.50.
- Cumulative after 95: accuracy 12.3% (34/95 top-1), brier skill 0.085, TW 1247.00.
### Resolving Aug 11
- 49405 Alabama 2nd: keep Marques 0.80.
- 517488 Shakhtar stadium: coach Arda Turan confirmed London home matches; negotiated with Chelsea, Fulham, Brentford; Gtech leading. Updated: Gtech 0.50, Craven Cottage 0.20, Stamford Bridge 0.15, Veltins 0.07.
- 918938 Ferran Torres: chose PSG; personal terms agreed; Barça-PSG €50M deal closing, official expected next week. Updated: PSG 0.85, Atletico 0.05, Arsenal 0.04, Chelsea 0.03.
- 772343 complete drought nuclear shutdown Aug 1-13: Romania Cernavodă reactor offline (No.1; No.2 may follow). Updated: Romania 0.45, France 0.20, Slovenia 0.10, Spain 0.08, Hungary 0.06.

## Day 50 (2026-08-11) updates
### Resolutions
- 49405 Alabama 2nd → **Rhett Marques**. My 0.80. Brier +0.95, TW +94.84. HIT.
- 517488 Shakhtar stadium → **Stamford Bridge** (not Gtech). My 0.15 (3rd). Brier -0.02, TW -34.00.
- 772343 drought nuclear shutdown → **Romania**. My 0.45. Brier +0.64, TW -16.43 (earlier had Romania 0.1).
- 918938 Ferran Torres → **PSG**. My 0.85. Brier +0.97, TW +26.30. HIT.
- Cumulative after 99: accuracy 13.5% (37/99 top-1), brier skill 0.095, TW 1317.71.
### Resolving Aug 12
- 422179 divest Israeli company: keep Elbit 0.40.
- 459381 Spence: INTER MILAN talks advanced, €30M+bonus deal close. Updated: Inter 0.80, Juventus 0.07.
- 604201 oil spill: Caroline Bezengi leaking off OMAN (Dhofar, Hallaniyat Islands; slick 7km from coast, reached Qibliyah Island). Updated: Oman 0.85.
- 628038 WAFCON finalists: SFs Morocco-Cameroon and Algeria-Ghana/Malawi. Updated: "Morocco, Algeria" 0.40, "Cameroon, Algeria" 0.22, "Morocco, Ghana" 0.18.
- 754377 Inter Miami Leagues Cup: lost 2-1 to Monterrey in group (1-1-0); beat Atletico San Luis 4-2. Keep Quarterfinals 0.33.
- 882554 Venezuela branch overhaul: agenda covers CNE (electoral) and TSJ (judicial). Updated: Electoral 0.60, Judicial 0.30.

## Day 51 (2026-08-12) updates
### Resolutions
- 422179 divest → **NextVision Stabilized Systems**. Not listed. Brier -0.21, TW -21.00.
- 459381 Spence → **Inter Milan**. My 0.80. Brier +0.95, TW -19.90.
- 604201 oil spill → **Oman**. My 0.85. Brier +0.97, TW -18.10.
- 628038 WAFCON → **Cameroon, Malawi** (Malawi giant-killers!). Not listed. Brier -0.25, TW -17.09.
- 754377 Inter Miami → **Group stage**. My Phase One 0.24 (2nd). Brier -0.24, TW -24.30.
- 882554 Venezuela → **Judiciary**. My Judicial 0.30 (2nd). Brier +0.14, TW -26.11.
- Cumulative after 105: accuracy 14.3% (40/105 top-1), brier skill 0.100, TW 1191.21.
### Resolving Aug 13
- 229258 Canadian Open women: Sabalenka OUT (R16); SFs Gauff-Rybakina and Swiatek-Svitolina. Updated: Rybakina 0.30, Gauff 0.30, Swiatek 0.20, Svitolina 0.20.
- 311120 Spanish Super Cup 2027 host: MIAMI leading candidate; Istanbul 2nd; Qatar 3rd; RFEF decision Aug 13. Updated: United States 0.60, Turkey 0.20, Qatar 0.15.

## Day 52 (2026-08-13) updates
### Resolutions
- 229258 Canadian Open women → **Swiatek**. My 0.20 (3rd). Brier +0.14, TW +11.45.
- 311120 Spanish Super Cup → **Türkiye**. My Turkey 0.20 (2nd). Brier -0.42, TW -80.64 (June forecast had Qatar 0.9).
- Cumulative after 107: accuracy 14.3% (40/107 top-1), brier skill 0.099, TW 1122.02.
### Resolving Aug 14
- 356699 Bangladesh first Test century in Australia: 1st Test Darwin, Day 1: Bangladesh 96-1 (Mominul 35*, Tanzid Hasan 32*; Mahmud 6-55 bowled AUS out for 198). Updated: Mominul 0.40, Tanzid Hasan 0.18, Shanto 0.10, Litton 0.08, Mushfiqur 0.06.

## Day 53 (2026-08-14) updates
### Resolution
- 356699 Bangladesh century in Australia → **Tanzid Hasan**. My 0.18 (2nd). Brier +0.15, TW -8.48.
- Cumulative after 108: accuracy 14.3% (40/108 top-1), brier skill 0.100, TW 1113.54.
### Resolving Aug 15
- 113668 UFC 330 strawweight: Dern 0.74, Robertson 0.25.
- 40115 UFC 330 welterweight: Makhachev 0.86, Garry 0.13.
- 277746 Djokovic Cincinnati defeater: Djokovic #3 seed; path Tirante → Landaluce/Arnaldi → Mensik/Darderi → de Minaur/Lecheka → Zverev SF. Sinner/Alcaraz absent. Updated: Zverev 0.20, Tirante 0.15, Landaluce 0.10, Mensik 0.08, de Minaur 0.08.
- 541001 MLS East leader Aug 19: Nashville 40, Miami 38, NE 30, Chicago 29 (Aug 2). Nashville hosts Miami Aug 15. Updated: Nashville 0.50, Miami 0.35, Chicago 0.06.
- 764544 Indonesia earthquake province: keep Central Sulawesi 0.35.
- 777991 Pan Pacific 50m free: keep Douglass 0.45, Walsh 0.35.
- 985937 Pan Pacific 800m free: keep Ledecky 0.55, McIntosh 0.35.

## Day 54 (2026-08-15) updates
### Resolutions
- 113668 UFC Dern → **Dern**. My 0.74. Brier +0.87, TW +86.99. HIT.
- 277746 Djokovic Cincinnati → **Thiago Tirante**. My 0.15 (2nd). Brier +0.21, TW -8.11.
- 40115 UFC Makhachev → **Makhachev**. My 0.86. Brier +0.96, TW +96.35. HIT.
- 541001 MLS East → **Nashville**. My 0.50. Brier +0.62, TW +53.24. HIT.
- 764544 Indonesia quake → **East Nusa Tenggara**. Not listed. Brier -0.16, TW -15.97.
- 777991 50m free → **Douglass**. My 0.45. Brier +0.57, TW +56.91. HIT.
- 985937 800m free → **Lani Pallister**. Not listed. Brier -0.43, TW -42.75.
- Cumulative after 115: accuracy 15.9% (44/115 top-1), brier skill 0.110, TW 1340.21.
### Resolving Aug 16
- 279786 Community Shield (Aug 16): Arsenal vs Man City. Keep Arsenal 0.50, City 0.40.
- 616886 WAFCON winner: final Cameroon vs Malawi. Updated: Cameroon 0.60, Malawi 0.40.
- 969395 St Jude: Scheffler leads by 2 (13 under; Burns & Im 11 under) into final round. Updated: Scheffler 0.60, Burns 0.13, Im 0.12.

## Day 55 (2026-08-16) updates
### Resolutions
- 279786 Community Shield → **Arsenal**. My 0.50. Brier +0.59, TW +59.00. HIT.
- 616886 WAFCON → **Cameroon**. My 0.60. Brier +0.68, TW -16.71.
- 969395 St Jude → **Scheffler**. My 0.60. Brier +0.81, TW +42.71. HIT.
- Cumulative after 118: accuracy 17.1% (47/118 top-1), brier skill 0.118, TW 1425.21.
### Resolving Aug 17
- 163032 Senegal coach: keep Renard 0.15, Cissé 0.12.
- 292136 Hockey Pool D: after MD1 England 3pts (+3), India 3 (+2), Wales 0, Pakistan 0; India-Pak Aug 19. Updated: England 0.50, India 0.38, Pakistan 0.07.
- 565579 Japan GDP component: consensus GDP +0.6% q/q; private consumption +0.5% (~0.28 pt); net exports +0.3 pt; business investment +0.4%. Updated: Net exports 0.45, Private consumption 0.40, Business investment 0.08, Government 0.04.

## Day 56 (2026-08-17) updates
### Resolutions
- 163032 Senegal coach → **Patrick Vieira**. Not listed. Brier -0.05, TW -5.19.
- 292136 Hockey Pool D → **England**. My 0.50. Brier +0.60, TW +67.36. HIT.
- 565579 Japan GDP → **Net exports**. My 0.45. Brier +0.53, TW +2.41. HIT.
- Cumulative after 121: accuracy 17.9% (49/121 top-1), brier skill 0.123, TW 1489.79.
### Resolving Aug 18
- 160265 Ollie Watkins: keep Newcastle 0.35, Milan 0.25.
- 970733 FDA commissioner: keep Overton 0.40.
- 246629 Gulf embargo Iran: keep UAE 0.30, Bahrain 0.20.
- 984539 Imran Khan hospital: SC hears petition Aug 18; PTI demands Shifa; jail says PIMS treatment sufficient. Keep Shifa 0.60, PIMS 0.20.
- 418046 Medvedev Cincinnati defeater: beat Trungelliti R2; faces Nakashima R3; then de Minaur/Lehecka QF; Zverev SF. Sinner/Alcaraz absent. Updated: Nakashima 0.20, Zverev 0.18, de Minaur 0.08, Fritz 0.06, Shelton 0.05.
- 720221 Cory Mills: keep Mills 0.80.
- 844962 Ukraine wartime elections: Kuleba explicitly called for both elections during war (Aug 16 interview; also April). Keep Kuleba 0.40.
- 845687 Florida Dem Senate: keep Vindman 0.90.

## Day 57 (2026-08-18) updates
### Resolutions
- 160265 Ollie Watkins → **Al Hilal**. Not listed. Brier -0.20, TW -19.55.
- 246629 Gulf embargo → **UAE**. My 0.25 (2nd). Brier +0.31, TW +32.29.
- 418046 Medvedev defeater → **Nakashima**. My 0.20 top. Brier +0.32, TW -4.56.
- 720221 Cory Mills → **Ryan Elijah**. My 0.15 (2nd). Brier -0.36, TW -36.25.
- 844962 Ukraine elections → **Mykhailo Fedorov**. Not listed. Brier -0.24, TW -23.75.
- 845687 Florida Dem Senate → **Angie Nixon** (not Vindman!). My 0.90. Brier -0.66, TW -65.64.
- 970733 FDA → **Heidi Overton**. My 0.40. Brier +0.57, TW +56.92. HIT.
- 984539 Imran Khan → **Shifa International**. My 0.62. Brier +0.82, TW +81.91. HIT.
- Cumulative after 129: accuracy 19.0% (51/129 top-1), brier skill 0.125, TW 1511.16.
### Resolving Aug 19
- 770763 Konsa: Arsenal (reignited interest, Saliba injured) and Liverpool frontrunners; Villa want £60M. Updated: Arsenal 0.38, Liverpool 0.32, Tottenham 0.04, Man City 0.04.
- 903565 Nord Stream arrest: Kuznetsov already in custody (charges filed July 1); Zhuravlov extradition refused. Keep None 0.62.

## Day 58 (2026-08-19) updates
### Resolutions
- 770763 Konsa → **Arsenal**. My 0.38 top. Brier +0.51, TW -5.37.
- 903565 Nord Stream → **Volodymyr Zhuravlev**. My 0.10 (3rd). Brier -0.21, TW -21.13.
- Cumulative after 131: accuracy 19.4% (52/131 top-1), brier skill 0.126, TW 1484.66.
### Resolving Aug 20
- 225772 Savinho: keep Spurs 0.85.
- 764491 CA-14 special: Wahab leads 51.0-49.0 in early results (more ballots Aug 21/26/28). Updated: Wahab 0.75, Hernandez 0.25.
- 855662 Alcaraz return: withdrew from Cincinnati (Aug 4); skipped Canada/DC/Los Cabos; training with Rune, US Open decision pending. Updated: US Open 0.60, Winston-Salem 0.20, No return confirmed 0.10.
- 846721 Sinaloa governor: keep Bonilla 0.82.
- 916964 Iranian proxy: keep Kataib Hezbollah 0.25.

## Day 59 (2026-08-20) updates
### Resolutions
- 225772 Savinho → **Tottenham**. My 0.85. Brier +0.97, TW +97.10. HIT.
- 764491 CA-14 → **Wahab**. My 0.75. Brier +0.88, TW +77.05. HIT.
- 846721 Sinaloa → **Rubén Rocha Moya** (returned!). My 0.15 (2nd). Brier -0.39, TW -39.49.
- 855662 Alcaraz → **US Open**. My 0.60. Brier +0.79, TW -13.09.
- 916964 Iranian proxy → **Hezbollah**. My 0.20 (2nd). Brier +0.28, TW +27.67.
- Cumulative after 136: accuracy 20.6% (56/136 top-1), brier skill 0.136, TW 1633.90.
### Resolving Aug 21
- 248237 Baleba: Man Utd £65M bid, deal expected ~£70M, "matter of hours"; player wants United. Updated: Man Utd 0.90.
- 767460 Marmoush: Tottenham in talks for £140M double deal (Savinho+Marmoush); Marmoush keen; personal terms discussed. Updated: Tottenham 0.75, Barcelona 0.07.

## Day 60 (2026-08-21) updates
### Resolutions
- 248237 Baleba → **Man United**. My 0.90. Brier +0.99, TW +85.20. HIT.
- 767460 Marmoush → **Tottenham**. My 0.75. Brier +0.93, TW +23.87. HIT.
- Cumulative after 138: accuracy 21.4% (58/138 top-1), brier skill 0.144, TW 1742.97.
### Resolving Aug 22
- 187330 Freedom 250 pole: Palou leads title by 133 pts; Honda won all 5 street races. Updated: Palou 0.28, Kirkwood 0.12, O'Ward 0.08, Newgarden 0.07, Dixon 0.06.
- 48050 robot 100m: now fully autonomous; Unitree H1 hit 10 m/s. Keep Tiangong Ultra 0.33, Unitree H1 0.33.
- 97251 Man Utd opener at Hull: keep United 0.55.
- 720892 AIPAC candidate: keep Rogers 0.20.
- 72132 Forest-Leeds: keep Forest 0.45.
- 974146 Fabinho: keep Fenerbahce 0.35.

## Day 61 (2026-08-22) updates
### Resolutions
- 187330 Freedom 250 pole → **Palou**. My 0.28. Brier +0.45, TW +38.89. HIT.
- 48050 robot 100m → **Tiangong Ultra**. My 0.35. Brier +0.45, TW +45.25. HIT.
- 720892 AIPAC → **Mike Rogers**. My 0.20 top. Brier +0.31, TW +31.11. HIT.
- 72132 Forest-Leeds → **Leeds**. My 0.28 (2nd). Brier +0.21, TW +20.62.
- 97251 Man Utd opener → **Hull City**. My 0.20 (3rd). Brier -0.01, TW -0.50.
- 974146 Fabinho → **Trabzonspor**. Not listed. Brier -0.18, TW -18.33.
- Cumulative after 144: accuracy 22.6% (61/144 top-1), brier skill 0.149, TW 1860.01.
### Resolving Aug 23
- 22056 400mH Silesia: keep dos Santos 0.63, Warholm 0.31.
- 222955 Bouaddi: MAN CITY advanced talks, ~£85M bid; Rodri sold to Barcelona. Updated: Man City 0.75, Arsenal 0.10.
- 260735 Cincinnati women: SFs Pegula-Swiatek, Bejlek-Gauff; Sabalenka OUT, Rybakina retired. Updated: Swiatek 0.40, Gauff 0.30, Pegula 0.17, Bejlek 0.13.
- 354508 women's 100m Silesia: keep Jefferson-Wooden 0.48, Alfred 0.38.
- 372528 Cincinnati men: SFs Cobolli-Fils, Nakashima-Tiafoe (Zverev, FAA, Medvedev, Fritz all out). Updated: Nakashima 0.30, Tiafoe 0.25, Cobolli 0.25, Fils 0.20.
- 669987 Dutch GP: keep Antonelli 0.42, Hamilton 0.21.

## Day 62 (2026-08-23) updates
### Resolutions
- 22056 400mH → **dos Santos**. My 0.63. Brier +0.77, TW +76.57. HIT.
- 222955 Bouaddi → **Man City**. My 0.75. Brier +0.92, TW -38.41.
- 260735 Cincinnati women → **Gauff**. My 0.30 (2nd). Brier +0.30, TW +10.87.
- 354508 100m → **Jefferson-Wooden**. My 0.48. Brier +0.58, TW +58.11. HIT.
- 372528 Cincinnati men → **Arthur Fils**. My 0.20 (4th). Brier +0.14, TW -12.81.
- 669987 Dutch GP → **Norris**. My 0.09 (4th). Brier -0.08, TW -7.91.
- Cumulative after 150: accuracy 23.8% (66/150 top-1), brier skill 0.159, TW 1946.44.
### Resolving Aug 24
- 388162 Allan Elias: MAN CITY closing in, €40M deal, personal terms agreed. Updated: Man City 0.80.
- 461239 USS Abraham Lincoln: keep Oman 0.20, Bahrain 0.18, Japan 0.15.
- 623398 Hadjam: keep Como 0.50.
- 964047 Eurovision boycott: Netherlands RETURNING (De Telegraaf); 2026 boycotters were NL, Spain, Slovenia, Ireland, Iceland. Updated: Ireland 0.30, Spain 0.20, Slovenia 0.10, Iceland 0.08.

## Day 63 (2026-08-24) updates
### Resolutions
- 388162 Allan Elias → **Man City**. My 0.80. Brier +0.95, TW -9.83.
- 461239 USS Abraham Lincoln → **Thailand**. Not listed. Brier -0.11, TW -10.78.
- 623398 Hadjam → **Brighton**. Not listed. Brier -0.27, TW -26.99.
- 964047 Eurovision → **Netherlands** (announced boycott despite return reports). My 0.06 (5th). Brier -0.03, TW +20.74.
- Cumulative after 154: accuracy 24.2% (68/154 top-1), brier skill 0.161, TW 1919.58.
### Resolving Aug 25
- 277370 Celtic: won CL playoff 1st leg 3-0 vs LASK; 2nd leg Aug 26. Updated: Champions League 0.87, Europa League 0.13.
- 53266 PFA Player: keep Bruno Fernandes 0.62.
- 772246 Djokovic/Sabalenka mixed doubles: they ARE playing (top seeds); R1 vs Fernandez/Tiafoe Aug 25; Medvedev/Swiatek/Rybakina withdrew. Updated: None 0.25, "Fernandez and Tiafoe" 0.20, "Eala and Auger-Aliassime" 0.08, "Pegula and Fritz" 0.08.
- 903529 measles death state: keep Texas 0.35.
- 874244 Trump official Moscow: keep Witkoff 0.55.

## Day 64 (2026-08-25) updates
### Resolutions
- 277370 Celtic → **Europa League** (LASK overturned 0-3!). My 0.87 CL. Brier -0.51, TW +69.14.
- 53266 PFA → **Bruno Fernandes**. My 0.62. Brier +0.81, TW +81.34. HIT.
- 772246 mixed doubles → **Patten and Siniakova**. Not listed. Brier -0.12, TW -2.56.
- 874244 Moscow → **John Ratcliffe**. Not listed. Brier -0.35, TW -35.05.
- 903529 measles → **Pennsylvania**. Not listed. Brier -0.20, TW -19.50.
- Cumulative after 159: accuracy 24.6% (69/159 top-1), brier skill 0.160, TW 2012.95.
### Resolving Aug 26
- 588637 Nicolas Jackson: Aston Villa closing in on £65M deal; daily contact; Watkins to Al-Hilal. Updated: Aston Villa 0.80, Atletico 0.08.
- 834692 Xi Middle East visit: keep Saudi Arabia 0.35.

## Day 65 (2026-08-26) updates
### Resolutions
- 588637 Jackson → **Aston Villa**. My 0.80. Brier +0.95, TW +41.29. HIT.
- 834692 Xi → **Egypt**. My 0.15 (3rd). Brier +0.10, TW +10.37.
- Cumulative after 161: accuracy 25.0% (71/161 top-1), brier skill 0.164, TW 2064.61.
### Resolving Aug 27
- 162316 Barcola: Liverpool personal terms agreed; verbal agreement with PSG >£110M; deal "done" pending medical. Updated: Liverpool 0.85, Arsenal 0.08.
- 450664 Emiliano Martinez: keep Juventus 0.72.
- 876325 Enzo Fernandez: Real Madrid denied interest; Man City intend to bid; Chelsea working on him staying; "Manchester or Madrid, not Barcelona". Updated: Man City 0.55, Real Madrid 0.20, PSG 0.05.

## Day 66 (2026-08-27) updates
### Resolutions
- 162316 Barcola → **Liverpool**. My 0.85. Brier +0.97, TW -15.71.
- 450664 Emiliano Martinez → **Chelsea**. My 0.02 (5th). Brier -0.50, TW -50.47.
- 876325 Enzo → **Man City**. My 0.55. Brier +0.75, TW -60.22.
- Cumulative after 164: accuracy 25.8% (72/164 top-1), brier skill 0.169, TW 1938.21.
### Resolving Aug 28
- 120116 Norway monarch Aug 29: King Harald V in "extremely serious" condition (haemolytic anaemia, hospitalized >1 week); Haakon serving as regent. Updated: Harald V 0.65, Haakon VIII 0.35.
- 921981 SCO summit Putin counterpart: Putin plans to meet MODI at Bishkek SCO (Aug 31-Sep 1); Kremlin schedule TBD. Updated: Modi 0.35, Erdogan 0.30, Lukashenko 0.05, Xi 0.05.

## Day 67 (2026-08-28) updates
### Resolutions
- 120116 Norway → **Haakon VIII** (King Harald died). My 0.35 (2nd). Brier +0.15, TW -79.02.
- 921981 SCO → **Erdogan**. My 0.30 (2nd). Brier +0.38, TW +73.32.
- Cumulative after 166: accuracy 25.8% (72/166 top-1), brier skill 0.171, TW 1932.51.
### Resolving Aug 29
- 20480 Martinelli: AL-HILAL medical booked, £56M, announcement over weekend. Updated: Al-Hilal 0.90.
- 2260 Sydney Marathon men: field Lemma (2:01:48), Simbu (2:02:47, world champ), Kiplagat, Ngetich, Kiros (defending). No Sawe/Kiplimo/Kejelcha. Updated: Lemma 0.30, Simbu 0.25, Kiplagat 0.12, Ngetich 0.10, Kiros 0.07.
- 409386 Sydney Marathon women: Jepchirchir favorite; also Cheptai, Shauri, Cheruiyot. Updated: Jepchirchir 0.45, Cheptai 0.15, Shauri 0.10, Cheruiyot 0.05.

## Day 68 (2026-08-29) updates
### Resolutions
- 20480 Martinelli → **Al-Hilal**. My 0.90. Brier +0.99, TW -18.09.
- 2260 Sydney Marathon men → **Addisu Gobena**. Not in top-5. Brier -0.18, TW -5.50.
- 409386 Sydney Marathon women → **Jepchirchir**. My 0.45. Brier +0.66, TW +20.38. HIT.
- Cumulative after 169: accuracy 26.6% (74/169 top-1), brier skill 0.177, TW 1929.30.
### Resolving Aug 30
- 127253 Gabriel Jesus: training away from Arsenal group; Everton and Napoli interest; could stay. Updated: Everton 0.35, Palmeiras 0.22, Napoli 0.15, AC Milan 0.06.

## Day 69 (2026-08-30) updates
### Resolution
- 127253 Gabriel Jesus → **Barcelona**. Not listed. Brier -0.20, TW -22.64.
- Cumulative after 170: accuracy 26.6% (74/170 top-1), brier skill 0.176, TW 1906.66.
### Resolving Aug 31
- 335239 Raam 2nd candidate: list announced Aug 22: 1. Abbas, 2. WALID TAHA, 3. al-Huashla, 4. Khatib-Yasin, 5. Hajirat. Updated: Walid Taha 0.90.
- 79046 Villa-Arsenal: Arsenal 8/15 favorites (~65%); Villa in crisis (lost 4-0 Brighton, sold Rogers/Konsa/Martinez/Watkins); Arsenal won CS 3-0, Coventry 3-0. Updated: Arsenal 0.65, Draw 0.20, Villa 0.15.

## Day 70 (2026-08-31) updates
### Resolutions
- 335239 Raam 2nd → **Yoav Segalovich** (independent joined slate!). Not listed. Brier -0.81, TW -5.16.
- 79046 Villa-Arsenal → **Arsenal**. My 0.65. Brier +0.82, TW +56.14. HIT.
- Cumulative after 172: accuracy 27.0% (75/172 top-1), brier skill 0.176, TW 1957.64.
### Resolving Sept 1
- 875467 highest PL transfer fee summer 2026: Morgan Rogers £117M (Chelsea) > Elliot Anderson £116M (Man City) > Barcola £106M (Liverpool) > Tonali £92.5M. Updated: Rogers 0.88, Anderson 0.10.

## Day 71 (2026-09-01) updates
### Resolution
- 875467 highest PL fee → **Enzo Fernandez** (deadline-day Man City move >£117M). Not listed. Brier -0.78, TW -24.88.
- Cumulative after 173: accuracy 27.0% (75/173 top-1), brier skill 0.173, TW 1932.76.
### Resolving Sept 2
- 591807 Ghana coach: GFA says coach "99% in place"; Tom Saintfiet reported frontrunner (former Mali coach); Desmond Ofei also mentioned. Updated: Saintfiet 0.55, Ofei 0.15, Renard 0.06.
- 712131 Israeli Gaza plan: "voluntary migration" plan stalled; no host countries; Trump moved away; resurfacing before elections. Updated: None 0.35, Katz 0.22, Gamliel 0.12, Ben-Gvir 0.08.

## Day 72 (2026-09-02) — MAJOR REFRESH of all 77 active Sept questions
All 77 active questions had stale 2026-06-24 forecasts. Resubmitted all 77 today using agent research (8 parallel research agents + direct searches).

### Key facts / context as of Sept 2, 2026
- **F1 2026**: Antonelli leads 242 pts, 59 ahead of Russell and Hamilton. Norris won last 2 races (Hungary, Zandvoort). Italian GP Sept 6: Antonelli takes full power-unit penalty → starts near back. Bookmakers: Norris ~6/4 fav, Russell 9/4, Ferraris 7/1, Antonelli 10/1. Spanish GP Sept 13 Madrid: Russell penalty-free (Mercedes ruled out Madrid); Baku Sept 26 likely Russell penalty. Aston Martin 2027: Alonso expected to stay/announce at Spanish GP (0.82).
- **Mbappe sponsor**: Nike deal expired July 31, 2026, not renewed; On (Swiss) repeatedly named as likely new principal sponsor; Nike has 6-month matching right; no official announcement by Sept 2.
- **La Liga**: after MD3, Barcelona 9 pts +10 GD, Real Madrid 9 pts +8. Betis-Real Madrid Fri Sept 4 at La Cartuja (Mourinho Real Madrid coach; Mbappe 4 goals). Valencia-Barcelona actual MD4 is Sept 6 (question says Sept 20 — data conflict; res date Sept 6). Madrid derby Atlético (home) v Real Sept 20.
- **F1 driver market**: Aston Martin seat = Alonso.
- **US Open 2026**: Djokovic lost R1 to Navone; Sinner withdrew (knee); Alcaraz returned from 4-month wrist layoff and won R1; Zverev #1 seed, French Open champ. Americans: Shelton (8), Fritz (9), Tiafoe (11), Tien (14); Nakashima lost R2 to Michelsen. Women: Sabalenka ~23%, Gauff ~20% (Cincinnati champ), Swiatek ~15%.
- **Ebola DRC**: 6,186 cases/3,007 deaths as of Aug 31; Ituri 81.9% of cases (epicenter); North Kivu 868 cases, 67.9% CFR, new health zones; 6 provinces affected. WHO mid-Sept assessment.
- **Haze**: Sarawak API peak 476 (Aug 31), 408/407 Sept 1; emergency threshold 500; cloud seeding Sept 3-5. Indonesia: Central Kalimantan provincial "tanggap darurat" Aug 31-Sept 29; Gunung Mas regency tanggap darurat Sept 1-30; East Kalimantan siaga darurat. Philippines school closures only. No national emergency anywhere by Sept 2.
- **Treasury/Iran**: Operation Economic Outcast launched Aug 24. Aug 28: FinCEN proposed rule vs Banque Misr UAE (not OFAC designation); OFAC sanctioned Bank Melli Dubai manager Reza Taeedi + Kameng Trading Ltd. Bessent Sept 1: "probably announce a bank sanction this week, and one the week after"; no name given. Iran International: 15 foreign banks (7 Chinese) used by Iran; only 2 targeted in August.
- **MAGA Inc**: Sept 2 began ~$1M NATIONAL TV ads (nonprofit arm Securing American Greatness), Trump-focused; first public event Michigan (Vance, Aug 31); $828k spent on SC runoff (Darlene Graham). No state-specific general-election ad buy yet.
- **Brazil**: PF report (ordered by Mendonça) revealed Banco Master's Vorcaro messages to Moraes citing "protection" from Andrei Rodrigues/Gonet. Opposition demands Rodrigues suspension/impeachment of Moraes; STF plenary to decide next steps. No suspension order as of Sept 2.
- **Census 2030**: Leaked June 25 draft rule (OMB review, not yet published as of Aug 20) counts only "lawful permanent residents, approved asylees, approved refugees"; excludes other noncitizens from apportionment. Citizenship question also pushed.
- **England cricket**: 3rd Test v Pakistan at Edgbaston Sept 9-13. Squad: Root(c), Archer, Atkinson, Baker, Bashir, Brook, Cook, Cox, Duckett, Gay, Lawrence, Pope, Robinson, Smith, Tongue. Carse omitted (arrest), Fisher dropped. Pakistan dropped 7 players, 5 uncapped. Robinson in form (8-35 at Lord's, 23 wkts at 8.3 avg). Archer/Atkinson/Tongue may be rested for Sri Lanka white-ball series.
- **Ukraine**: Massive Russian strikes on Odesa Sept 1-2; gas station destroyed in Odesa Sept 2; Kharkiv petrol station hit Aug 28 and two more in Kharkiv region Aug 29. Question window Sept 1-11 needs strikes on 2 separate days; Odesa best candidate.
- **Yemen**: Houthi/Sana'a forces attacking Tareq Saleh-held islands in southern Red Sea; "near-complete termination" of Saleh presence (pro-Houthi source, Sept 1); Hanish/Zuqar government-held, Houthi boat attacks repelled. Mayun/Perim status unclear.
- **Emmy 2026** (Sept 14): Rhea Seehorn (Pluribus) ~72-77% for Drama Actress; The Pitt ~85% Drama Series; Comedy Series close: Widow's Bay ~50% vs Hacks ~42%.
- **Venice**: festival opened Sept 2; awards Sept 12; Special Jury Prize wide open; buzz: "Mr. Nelson, Did You Kill People?" (Tsukamoto), "A Bit of Light" (Asgari), "DAU".
- **Athletics Ultimate Championship** (Budapest Sept 11-13): 5000m Ingebrigtsen/Hocker/Yihune; men's javelin Pathirage (world lead 92.62) with Chopra OUT; women's javelin Yan Ziyi (71.74); men's 200m Bednarek/Tebogo/Dambile, Lyles weak.
- **Asian Games** (Aichi-Nagoya Sept 2026): swimming Yu Yiting/Yu Zidi dominant; men's javelin Pathirage fav with Nadeem 2nd (Chopra out); men's 100m Boonson 9.99 season best.
- **Tennis/other**: US Open men Alcaraz 27-28% market, Zverev 20%.
- **UFC 331** (Sept 19): Van vs Pantoja pick-em (~50/47); co-main Tsarukyan vs Ruffy (Oliveira withdrew) Tsarukyan ~78%.
- **PSA**: Hania El Hammamy #1 (2109 pts) ahead of Amina Orfi (1986).
- **Berlin election Sept 20**: BerlinTrend CDU 21, Linke 19, Grüne 18, AfD 18, SPD 11; Civey Linke 20, CDU 19. Coin flip CDU/Linke.
- **UEFA 2029 CL final**: Camp Nou vs Wembley; UEFA ExCo decision ~Sept 15; Camp Nou favored.
- **World Athletics 2029**: Nairobi vs London vs Rome; announcement ~Sept 15-20.
- **DOSB**: Munich/Berlin/Rhine-Ruhr decision Sept 26.
- **Okinawa governor Sept 13**: Tamaki (incumbent) vs Genta Koja (LDP); polls level, Koja momentum, 29/41 mayors back Koja. Toss-up.
- **Donnarumma trial Sept 10-11**: 3 defendants — Ilyas Kherbouch ("Ganito", alleged mastermind, escaped Villepinte in March), Khyan M. (second commander), unnamed executor. Minors already sentenced 4 and 3 years.
- **Morocco election Sept 23**: PM appointed from largest party; Chaouki (RNI), Baraka (Istiqlal), Lekjaa (PAM) contenders.
- **Tunisia hunger strike**: Wael Naouar on hunger strike since Aug 16 (day 16 Sept 1); others detained.
- **Christa Pike execution Sept 30**: stay likely requested; no stay yet.
- **Artemis Accords**: 71 signatories after Türkiye (Aug 31); 75th by Sept 27 unlikely (None 0.5).
- **Kalshi**: Ninth Circuit ruled 3-0 Aug 28 that Nevada can regulate Kalshi; Third Circuit ruled opposite April 6; NJ petitioned SCOTUS Sept 2; next circuit ruling unclear.

### Predictions submitted Day 72 (all 77)
Top-confidence: 315568 Alonso 0.82; 873349 The Pitt 0.85; 880660 None 0.85; 440552 Seehorn 0.72; 574485 El Hammamy 0.80; 540490 None 0.70; 574553 Tsarukyan 0.78; 101639 Sudan 0.78; 832291 Ri Song-gum 0.30 (low); 695205 Pathirage 0.60.
Low-confidence/unresearched: 790870 bank (spread), 546622 Liverpool sponsor (no name), 52657 Venice, 996188 Puyo Puyo, 660356 Nigeria official, 299105 Iran GDP sector.

### To-do Day 73
- Check Sept 3-4 news for: bank sanction name (790870), haze emergency (224345), FAO August release (205592), Betis-RM result (568969), MAGA state buy (673971).
- Check Italian GP practice/qualifying Sept 4-5 (668636).
- Check England XI for 3rd Test (971366).
- Update any resolved questions' neighbors.

## Day 73 (2026-09-03) updates
- Cumulative after Day 72 resolutions: accuracy 27.0%, brier 0.172, TW 1963.83. (591807 Ghana → Queiroz, my 0.04 -0.25; 712131 Gaza plan → Ben-Gvir, my 0.08 -0.04.)
- **Haze**: Sarawak API peak 475 (Serian) Sept 3, 7 areas >300; emergency threshold 500; cloud seeding started Sept 3-5; governor says API could hit 800. No emergency yet. Indonesia: Central Kalimantan tanggap darurat (Aug 31-Sept 29), Gunung Mas regency tanggap darurat (Sept 1-30), East Kalimantan siaga darurat. Updated 224345: Indonesia 0.52, Malaysia 0.25, None 0.10, Philippines 0.06, Singapore 0.04.
- **Bank sanctions**: No new bank named as of Sept 3. FinCEN Banque Misr rule published in Federal Register Sept 1 (proposed, not OFAC designation; comment period to Oct 1). Bessent Sept 2: more bank sanctions could come this week; also airlines/digital assets. IBTimes: Chinese banks may not be targeted; no major Chinese bank named. Updated 790870: Banque Misr 0.28, None 0.25, Emirates NBD 0.08, Bank of China 0.06, Bank of Kunlun 0.04.
- **MAGA Inc**: First buy is $1M NATIONAL TV ads starting Sept 3 (Securing American Greatness), no state-specific buy. Updated 673971: Texas 0.25, Michigan 0.15, None 0.15, Pennsylvania 0.10, NC 0.08.
- **Italian GP**: Norris fav (Sisal 2.75), Russell 4.00, Leclerc 5.00, Hamilton 6.00; Antonelli starts back (PU penalty), will tow Russell in qualifying; Ferrari ADUO2 engine upgrade. Updated 668636: Norris 0.30, Russell 0.22, Leclerc 0.15, Hamilton 0.13, Antonelli 0.08.
- **Ebola**: Africa CDC Sept 3: weekly cases peaked 537 (Aug 10), dipped to 464/479; Ituri cases -12% over 3 weeks; North Kivu cases more than doubled, deaths +98%, CFR 67.7%; Haut-Uélé cases nearly tripled; Bas-Uélé new. Updated 490094: North Kivu 0.38, Ituri 0.32, Haut-Uele 0.14, Bas-Uele 0.05, Tshopo 0.03.
- **Ukraine fuel**: Odesa gas station destroyed Sept 2; another Ukrnafta gas station hit near Sychavka (Odesa region) night Sept 3. Updated 759359: Odesa 0.55, Kyiv 0.12, Poltava 0.08, Sumy 0.06, Kharkiv 0.05.
- **US Open**: Shelton, Fritz, Tiafoe, Paul, Alcaraz, Zverev, Medvedev advance; Nakashima out (Michelsen), Musetti out, FAA out (Khachanov), Rublev out. Tien vs Monfils pending. Updated 408930: Shelton 0.33, Fritz 0.22, Tiafoe 0.15, Tien 0.11, Paul 0.05. 891014: Alcaraz 0.28, Zverev 0.18, Medvedev 0.08, Shelton 0.07, Fritz 0.06. 608158: Sabalenka 0.24, Gauff 0.20, Swiatek 0.15, Pegula 0.09, Andreeva 0.06.
- **Venice**: Wild Horse Nine rave reviews + 13-min ovation; Bucking Fastard (Herzog) polarizing B+; Ink opened. Updated 52657: Wild Horse Nine 0.15, Bucking Fastard 0.12, Mr. Nelson 0.12, Bunker 0.08, Primetime 0.05.
- **Berlin**: BerlinTrend Sept 2: CDU 21, Linke 19, Grüne 18, AfD 18, SPD 11. Updated 81247: CDU 0.40, Linke 0.30, AfD 0.12, Grüne 0.07, SPD 0.03.
- **UEFA 2029 final**: Camp Nou favored over Wembley; UEFA ExCo votes Sept 15 in Thessaloniki. Updated 816232: Camp Nou 0.70, Wembley 0.26.
- **Okinawa**: Dead heat; LDP poll shows Koja closing; 29/41 mayors back Koja; 50% undecided; Ishin supporters lean Tamaki. Keep Koja 0.47/Tamaki 0.46.
- **Brazil STF**: Crisis intensifying; Moraes asks Fachin to investigate Mendonça; ministers in wait mode; no Rodrigues suspension. Keep None 0.85.
- **5000m**: Ingebrigtsen confirmed for 5000m and 1500m in Budapest. Keep 0.30.
- **Census**: Rule still unpublished as of Sept 3; DAO 216-26 noise-infusion ban complicates. Keep LPR 0.42.

### To-do Day 74 (Sept 4)
- 4 questions resolve Sept 4: 205592 (FAO Aug), 224345 (haze emergency), 790870 (bank), 568969 (Betis-RM scorer). Check results.
- Italian GP practice Sept 4; Betis-RM match Sept 4 21:00 CEST.
- Check MAGA state buy (673971 resolves Sept 5).

## Day 74 (2026-09-04) updates
- Resolutions Sept 4: 205592 FAO → **Sugar** (my 0.40, Brier +0.52); 224345 haze → **Malaysia** (my 0.25 2nd, +0.15); 568969 Betis-RM scorer → **Troy Parrott** (not listed, -0.11; Parrott came on 68' and scored 81'; Cucho started but Parrott scored); 790870 bank → **Golden Global Bank** (not listed, -0.15). Cumulative: accuracy 27.4%, brier 0.173, TW 1999.12.
- **MAGA Inc (673971, resolves Sept 5)**: MS NOW Sept 4: MAGA Inc. reached arrangement with Musk this week — America PAC handles Texas (Paxton), MAGA Inc. spends in **North Carolina** for Michael Whatley. Neither on air yet. Also Trump says $400-500M allocation. Updated: North Carolina 0.50, Texas 0.12, Michigan 0.08, None 0.08, Pennsylvania 0.05.
- **Italian GP (668636, Sept 6)**: FP1 Ferrari 1-2 (Leclerc 1:23.008, Hamilton +0.173, Russell +0.304). FP2 Russell fastest 1:22.559, Leclerc +0.120, Antonelli +0.141, Norris +0.384, Hamilton +0.457. McLaren says not in contention. Updated: Russell 0.30, Leclerc 0.24, Hamilton 0.14, Norris 0.12, Antonelli 0.08. Qualifying Sept 5.
- **La Liga (284913, Sept 6)**: Real Betis 1-0 Real Madrid (Parrott 81', Mbappe missed pen). Real stay 9 pts, GD +7. Barcelona play Valencia Sept 6; Barcelona 9 pts +10 GD. Barcelona almost certainly top unless heavy loss. Updated: Barcelona 0.85, Real 0.08, Atletico 0.05.
- **Ebola (490094, Sept 6)**: Africa CDC Sept 3-4: plateau, weekly cases 464-479 (peak 537 Aug 10); Ituri -12% over 3 weeks; North Kivu cases doubled, deaths +98%, CFR 67.7%; Haut-Uélé nearly tripled. Keep North Kivu 0.38, Ituri 0.32, Haut-Uele 0.14.
- **US Open**: Alcaraz d. Wu 6-3 6-4 6-1 (R4 vs Tommy Paul); Medvedev d. Rinderknech; Zverev d. Halys in 5 sets; Fritz d. Bellucci 6-0 6-1 6-1; Tien d. Monfils 6-3 6-4 6-3; De Minaur lost to van de Zandschulp; FAA out to Khachanov. Updated 891014: Alcaraz 0.32, Zverev 0.15, Medvedev 0.09, Shelton 0.07, Fritz 0.06.
- **Yemen (508136)**: Houthis launched major ground offensive toward Bab al-Mandab/Mokha Sept 3-4; 129 killed; they do not yet control territory bordering the strait. Updated: Yemeni government 0.30, Houthis 0.28, UAE 0.12, Saudi 0.12, STC 0.08.
- **Liverpool sponsor**: No new sponsor; Amazon "extremely slim" per Wyness; Emirates hijack failed. Keep Standard Chartered 0.28.
- **Villa**: Villa poor start (0 wins/0 goals in first 2; lost 0-1 Arsenal Aug 31; play Hull Sept 5). Sept 12 Villa-Forest forecast may shift after weekend.

### To-do Day 75 (Sept 5)
- 673971 resolves Sept 5 (MAGA state).
- Italian GP qualifying Sept 5; race Sept 6.
- Barcelona-Valencia Sept 6.
- Check WHO Ebola mid-Sept statement (Sept 10-16 window).
- Check England XI for Edgbaston Test (Sept 9).

## Day 75 (2026-09-05) updates
- Resolution Sept 5: 673971 MAGA → **Texas** (my 0.12 2nd after switching to NC 0.50; Brier -0.04). Lesson: don't over-weight one late article; the "first ad buy" was Texas. Cumulative: accuracy 27.4%, brier 0.173, TW 1990.44.
- **Italian GP (668636, Sept 6)**: Qualifying — **Gasly on pole** 1:21.786 (first career pole), Russell P2 +0.060, Piastri P3, Leclerc P4, Hamilton P5; Antonelli P7 but starts back (penalty); Norris P9. Race Sept 6. Updated: Russell 0.27, Gasly 0.15, Leclerc 0.15, Piastri 0.12, Hamilton 0.11.
- **La Liga (284913, Sept 6)**: Real Betis 1-0 Real Madrid (Sept 4). Real 9 pts +7 GD. Barcelona 9 pts +10 GD play Valencia Sept 6 (Valencia 17th, 1 pt). Barcelona top unless 4+ goal loss. Updated: Barcelona 0.90, Real 0.05, Atletico 0.04.
- **Ebola (490094, Sept 6)**: Sept 4: 92 new cases (Ituri 60, North Kivu 25, Haut-Uélé 5, Tshopo 2); 6,436 cases/3,095 deaths as of Sept 3; Ituri 81.4% of cases. Updated: North Kivu 0.38, Ituri 0.30, Haut-Uele 0.15, Bas-Uele 0.05, Tshopo 0.03.
- **Yemen (508136)**: Houthis took areas in western Taiz; government counteroffensive recaptured Hays district; Houthis do not control Bab al-Mandab coast. Updated: Yemeni government 0.32, Houthis 0.26, UAE 0.12, Saudi 0.12, STC 0.08.
- **Brazil (880660)**: PF report says Mendonça considered suspending Andrei Rodrigues; no order; Fachin takes over crisis. Updated: None 0.82, Mendonca 0.08, Moraes 0.03, Fachin 0.03, Gilmar 0.02.
- **Ukraine fuel (759359)**: Odesa region gas stations hit Sept 2 and Sept 3; Dnipro service station hit Sept 5 (1 killed); Hostomel (Kyiv region) gas station Sept 4. Keep Odesa 0.55, Kyiv 0.12, Poltava 0.08, Sumy 0.06, Kharkiv 0.05.
- **Villa-Forest (5814)**: Villa drew 0-0 at Hull Sept 5 — still 0 goals in 3 PL games (L, L, D). Updated: Villa 0.40, Draw 0.28, Forest 0.32.
- **Venice (52657)**: Primetime strong reviews (93% RT, 9-min ovation); Wild Horse Nine raves; Bucking Fastard mixed 70% RT; Mr. Nelson panned (D+). Updated: Primetime 0.18, Wild Horse Nine 0.15, Bunker 0.10, Bucking Fastard 0.08, The Echo Chamber 0.05.
- **US Open**: Fritz OUT (Cerundolo comeback from 2 sets down); Cobolli out; Shelton d. Shapovalov (R4 vs Tsitsipas); Tiafoe d. Vacherot (R4 vs Medvedev); Paul d. Bublik (R4 vs Alcaraz); Michelsen R4; Tien vs Mensik pending; Anisimova out (Potapova); Andreeva R4 vs Potapova. Updated 408930: Shelton 0.40, Tiafoe 0.20, Paul 0.10, Tien 0.10, Michelsen 0.06. Updated 891014: Alcaraz 0.30, Zverev 0.22, Medvedev 0.10, Shelton 0.08, Tiafoe 0.05.
- **Manchester derby (487575)**: Sept 13 at Old Trafford; City won first 2, Enzo Fernandez signed; United lost to Hull, beat Ipswich 5-2. Keep City 0.46, Draw 0.27, United 0.27.
- **Okinawa**: Dead heat, Koja momentum; keep Koja 0.47/Tamaki 0.46.
- **Berlin**: CDU 21, Linke 19 per BerlinTrend; keep CDU 0.40/Linke 0.30.
- **UEFA 2029**: Camp Nou favored; keep 0.70.
- **5000m**: Ingebrigtsen confirmed; no startlist. Keep 0.30.

### To-do Day 76 (Sept 6)
- 3 resolve Sept 6: 284913, 490094, 668636.
- Check Liverpool sponsor (546622, Sept 8), Brazil (880660, Sept 8), England XI (971366, Sept 9), census rule (408396, Sept 9).
- US Open R4 Sept 6-7: Shelton-Tsitsipas, Tiafoe-Medvedev, Paul-Alcaraz, Tien/Mensik.

## Day 76 (2026-09-06) updates
- Resolutions Sept 6: 284913 La Liga → **Barcelona** (0.90, +0.99); 490094 Ebola → **North Kivu** (0.38, +0.50); 668636 Italian GP → **Kimi Antonelli** (won from 19th! my 0.08 unlisted, -0.14). Cumulative: accuracy 28.2%, brier 0.179, TW 2136.85.
- **US Open men**: Alcaraz d. Paul 6-4 6-3 6-4 (QF vs Shelton/Tsitsipas winner); Tiafoe d. Medvedev 7-6(1) 6-4 7-6(6) (QF vs Michelsen); Michelsen d. Etcheverry (QF); Fritz OUT (Cerundolo), Cobolli OUT (Blockx), Medvedev OUT. Shelton vs Tsitsipas Sunday night. Updated 408930: Shelton 0.38, Tiafoe 0.26, Michelsen 0.16, Tien 0.05, Fritz 0.02. Updated 891014: Alcaraz 0.35, Zverev 0.20, Shelton 0.10, Tiafoe 0.08, Tsitsipas 0.05.
- **US Open women**: R16: Sabalenka d. Townsend; Noskova d. Kostyuk (QF Sabalenka-Noskova); Pegula vs Cirstea, Navarro vs Kalinskaya, Andreeva vs Potapova, Gauff vs Jovic, Swiatek vs Zheng, Rybakina vs Osaka. Updated 608158: Sabalenka 0.24, Gauff 0.18, Swiatek 0.15, Pegula 0.09, Andreeva 0.07.
- **Ukraine fuel (759359)**: Ukrnafta gas stations hit 4x in 24h (Kyiv region Sept 5, Zaporizhzhia x2 Sept 5-6, Dnipropetrovsk region Sept 6); Dnipro service station Sept 5 (2 dead); Odesa region Sept 2-3. Updated: Odesa 0.50, Kyiv 0.15, Dnipro 0.12, Poltava 0.06, Sumy 0.05.
- **Okinawa**: Dead heat; 6 candidates but Koja/Tamaki de facto head-to-head; Okinawa Times/Asahi poll due Sept 6-7; LDP internal poll had Tamaki 45.5-41.1 mid-Aug but Koja closing. Keep Koja 0.48, Tamaki 0.45.
- **Spanish GP (48458, Sept 13)**: Antonelli won Monza from 19th; Russell P2; Verstappen P3; Leclerc crashed; Hamilton P6. Madrid new circuit. Updated: Antonelli 0.26, Russell 0.24, Norris 0.14, Leclerc 0.09, Hamilton 0.09.
- **Brazil (880660)**: Fachin delays cases to Sept 14/22; no Rodrigues suspension; Mendonça considered it. Keep None 0.82.
- **Liverpool sponsor (546622)**: Still no replacement; Standard Chartered placeholder. Keep 0.28.
- **England (971366)**: No XI yet; Trescothick wants strongest side. Keep Robinson 0.25, Archer 0.19, Atkinson 0.16, Tongue 0.14, Cook 0.07.
- **Census (408396)**: No formal rule published as of Sept 6. Keep LPR 0.42.
- **Donnarumma (342722)**: Trial Sept 10-11; Le Figaro says two commanders "Kiki" and "Ganito" (Kherbouch). Keep Kherbouch 0.62, Khyan M. 0.25, Bakary B. 0.05.
- **5000m (936021)**: No startlist yet; Ingebrigtsen confirmed. Keep 0.30.

### To-do Day 77 (Sept 7)
- No resolutions Sept 7. Check England XI, Donnarumma trial preview, US Open QFs, Okinawa poll.
- Sept 8: 880660, 546622. Sept 9: 971366, 408396.

## Day 77 (2026-09-07) updates
- **England XI (971366, Sept 9)**: Predicted XI: Duckett, Gay, Cox, Root, Brook, Lawrence, Smith, Atkinson, Robinson, Archer, Tongue (all four seamers play, no Bashir/Cook). Updated: Robinson 0.27, Archer 0.24, Atkinson 0.20, Tongue 0.19.
- **US Open (408930, Sept 11)**: Shelton d. Tsitsipas 6-2 6-3 6-4 → QF vs Alcaraz. Tiafoe d. Medvedev → QF vs Michelsen. Three Americans in QF; Tiafoe/Michelsen guaranteed an American semifinalist, Shelton faces Alcaraz. Updated: Tiafoe 0.42, Michelsen 0.38, Shelton 0.16.
- **US Open men (891014, Sept 13)**: QFs: Alcaraz-Shelton, Tiafoe-Michelsen; Zverev in QF. Updated: Alcaraz 0.38, Zverev 0.20, Shelton 0.10, Tiafoe 0.08, Michelsen 0.06.
- **Okinawa (581343, Sept 13)**: Asahi/Okinawa Times/QAB poll: Koja slightly ahead, Tamaki chasing hard, ~40% undecided. Yomiuri: Koja ahead, ~20% undecided. Kyodo/Mainichi: dead heat. Updated: Koja 0.52, Tamaki 0.42.
- **Venice (52657, Sept 12)**: Golden Lion odds: NAZA 4/5, Wild Horse Nine 5/1, Possible Love 11/2, Woman Unknown 12/1, Bunker 16/1, A Bit of Light 25/1, Primetime 40/1, Bucking Fastard 50/1, Echo Chamber 50/1. Special Jury Prize updated: Wild Horse Nine 0.18, Bunker 0.12, Possible Love 0.10, A Bit of Light 0.07, Primetime 0.05.
- **Athletics startlists (Sept 11-13)**: Men's javelin: Pathirage 92.62, Weber 90.40, Thompson 87.59, Wegner 87.47, Peters 86.93, Walcott 83.99, Yego 82.22, Nadeem 78.63. Updated 30434: Pathirage 0.45, Weber 0.15, Peters 0.15, Walcott 0.06, Nadeem 0.05.
  Women's javelin: Yan Ziyi 71.74, Ruiz 67.34, Vilagos 67.22, Kitaguchi 67.38, Borge 66.50. Updated 261941: Yan 0.42, Kitaguchi 0.20, Ruiz 0.10, Vilagos 0.08, Borge 0.05.
  Men's 5000m: Ntakarutimana 12:46.73, Kemboi 12:47.29, Yihune 12:47.62, Mehary 12:47.78, Blanks 12:47.98, Young 12:48.12, Wolfe 12:49.45, Fisher 12:49.61, Ingebrigtsen 13:15.29 (returning), Hocker no SB. Updated 936021: Yihune 0.18, Ingebrigtsen 0.16, Ntakarutimana 0.14, Hocker 0.12, Fisher 0.08.
  Men's 200m: Bednarek 19.57 SB, Dambile 19.74, Levell 19.64, Tebogo entered; Lyles injured/out. Updated 653425: Bednarek 0.32, Tebogo 0.20, Dambile 0.16, Levell 0.08, Charamba 0.05.
- **Spanish GP (48458, Sept 13)**: Madrid new circuit; Antonelli won Monza from 19th. Updated: Antonelli 0.26, Russell 0.24, Norris 0.14, Leclerc 0.09, Hamilton 0.09.
- **Brazil (880660, Sept 8)**: No suspension; Andrei strengthened with Lula; Fachin handling. Keep None 0.82.
- **Liverpool sponsor (546622, Sept 8)**: No new sponsor; Standard Chartered placeholder. Keep 0.28.

### To-do Day 78 (Sept 8)
- 2 resolve Sept 8: 546622, 880660.
- Sept 9: 971366 (England bowler), 408396 (census).
- Sept 10: 759359 (Ukraine fuel), 508136 (Mayun).
- Sept 11: 408930 (US Open US), 342722 (Donnarumma), 936021 (5000m).
- Check US Open QFs Sept 8-9, Venice awards Sept 12, athletics Sept 11-13.

## Day 78 (2026-09-08) updates
- Resolutions Sept 8: 546622 Liverpool sponsor → **Turkish Airlines** (not listed; my Standard Chartered 0.28, Brier -0.09); 880660 Brazil → **Andre Mendonça** (my 0.08 2nd, Brier -0.52; Mendonça ordered Rodrigues suspension despite no prior formal order). Cumulative: accuracy 28.2%, brier 0.176, TW 2081.40.
- **US Open (408930, Sept 11)**: Tiafoe beat Michelsen 5-7 3-6 7-5 6-3 7-6(6) → Tiafoe in SF. Shelton vs Alcaraz QF Tuesday night (result unknown). Updated: Tiafoe 0.72, Shelton 0.25, Michelsen 0.02.
- **US Open men (891014, Sept 13)**: Tiafoe in SF; Alcaraz/Shelton QF; Zverev in QF. Keep Alcaraz 0.38, Zverev 0.20, Shelton 0.10, Tiafoe 0.08, Michelsen 0.06.
- **Donnarumma (342722, Sept 11)**: Trial Sept 10-11; defendants Ilyas Kherbouch ("Ganito") and Khyan Mamouni ("Kiki") are the alleged masterminds; third defendant unnamed. Updated: Kherbouch 0.60, Khyan Mamouni 0.27, Bakary B. 0.05.
- **Ukraine fuel (759359, Sept 10)**: Kharkiv hit 3 gas stations on Sept 8 (one day); Odesa region gas stations Sept 2-3; Kyiv region Sept 4-5 and Kyiv city gas station Sept 8; Dnipro service station Sept 5 + gas station complex Sept 6; Zaporizhzhia 2 gas stations Sept 5-6. Updated: Odesa 0.42, Kyiv 0.25, Dnipro 0.12, Kharkiv 0.10, Poltava 0.04.
- **Mayun (508136, Sept 10)**: Houthis attacking Saudi oil sites; government counteroffensive; no specific Mayun control news. Keep Yemeni government 0.32, Houthis 0.26, UAE 0.12, Saudi 0.12, STC 0.08.
- **Census (408396, Sept 9)**: No formal rule found in Sept 8 corpus; a govinfo FR PDF dated Sept 8 exists but unreadable. Keep LPR 0.42, US citizenship 0.14, legal permanent resident 0.12, approved asylee 0.05, approved refugee 0.05.
- **England (971366, Sept 9)**: Predicted XI all four seamers (Robinson, Archer, Atkinson, Tongue). Updated: Robinson 0.27, Archer 0.24, Atkinson 0.20, Tongue 0.19.

### To-do Day 79 (Sept 9)
- 2 resolve Sept 9: 408396, 971366.
- Sept 10: 759359, 508136.
- Sept 11: 408930, 342722, 936021.
- Check US Open QF Alcaraz-Shelton result, women's QFs, Donnarumma verdict, 5000m result.

## Day 79 (2026-09-09) updates
- Resolutions Sept 9: 408396 census → **Permanent residency** (my "Lawful permanent resident" 0.42, Brier +0.62); 971366 England bowler → **Josh Tongue** (my 0.19 4th, Brier +0.17). Cumulative: accuracy 28.6%, brier 0.179, TW 2158.74.
- **US Open men (408930, Sept 11; 891014, Sept 13)**: Shelton UPSET Alcaraz 6-7(5) 6-1 6-3 1-6 7-6(10-7) at 3:33am → all-American SF Shelton vs Tiafoe (Friday Sept 11). Zverev in other half. Updated 408930: Shelton 0.55, Tiafoe 0.43. Updated 891014: Zverev 0.40, Shelton 0.30, Tiafoe 0.20, Tien 0.04, Mensik 0.03.
- **US Open women (608158, Sept 12)**: QFs: Sabalenka d. Noskova; Pegula d. Navarro; Gauff d. Andreeva; Rybakina d. Zheng (Rybakina new world #1). SFs: Sabalenka-Pegula, Gauff-Rybakina. Updated: Sabalenka 0.34, Rybakina 0.25, Gauff 0.24, Pegula 0.17.
- **Ukraine fuel (759359, Sept 10)**: Kharkiv gas stations hit Sept 8 (3 stations) AND Sept 9 (Kyivskyi district + Marshall station overnight); Odesa region Sept 2-3; Kyiv region Sept 4-5 and Kyiv city gas station Sept 8; Dnipro Sept 5-6; Zaporizhzhia Sept 5-6; Poltava 7 facilities; Sumy 4-5; Mykolaiv 4-5. Russia plans 20+ gas stations in Kyiv. Updated: Odesa 0.40, Kyiv 0.25, Kharkiv 0.15, Dnipro 0.08, Poltava 0.05.
- **Mayun (508136, Sept 10)**: Houthis pushing toward Bab al-Mandab; government counteroffensive; no direct Mayun control report. Keep Yemeni government 0.32, Houthis 0.26, UAE 0.12, Saudi 0.12, STC 0.08.
- **Donnarumma (342722, Sept 11)**: Trial Sept 10-11; Kherbouch transferred to Meaux prison due to new escape plan; co-defendant Khyan Mamouni ("Kiki"). Keep Kherbouch 0.60, Mamouni 0.27, Bakary B. 0.05.

### To-do Day 80 (Sept 10)
- 2 resolve Sept 10: 508136, 759359.
- Sept 11: 408930, 342722, 936021.
- Check Donnarumma trial verdict, 5000m final result, US Open SF Shelton-Tiafoe, Venice awards Sept 12.

## Day 80 (2026-09-10) updates
- Resolutions Sept 10: 508136 Mayun → **Houthis** (my 0.26 2nd, +0.31); 759359 Ukraine fuel → **Kyiv** (my 0.25 2nd, +0.25). Cumulative: accuracy 28.6%, brier 0.182, TW 2167.13.
- **Donnarumma (342722, Sept 11)**: Trial Day 1 chaotic; defendants: Ilyas Kherbouch ("Ganito", 21, 11+ convictions), Khyan Mamouni ("Kiki", 22, also implicated in Vitaa/Lapix home-jackings), Moktar Diop (24, present at burglary, admitted participation without violence). Up to 20 years. Verdict Friday Sept 11. Updated: Kherbouch 0.58, Mamouni 0.28, Diop 0.08.
- **US Open SF (408930, Sept 11; 891014, Sept 13)**: Shelton -300 to -349 vs Tiafoe +240/+269 (~73-75% Shelton); Zverev -486 vs Khachanov +357. Futures: Zverev +120 (~45%), Shelton +150 (~40%), Tiafoe +700 (~12%), Khachanov +1600 (~6%). Updated 408930: Shelton 0.73, Tiafoe 0.26. Updated 891014: Zverev 0.47, Shelton 0.34, Tiafoe 0.11, Khachanov 0.07.
- **5000m (936021, Sept 11)**: Ingebrigtsen 100% focused on 5000m; final Friday 20:36. Updated: Ingebrigtsen 0.20, Yihune 0.17, Ntakarutimana 0.13, Hocker 0.11, Fisher 0.07.
- **Venice (52657, Sept 12)**: Corriere: Golden Lion race between Possible Love (critics 4.55) and Wild Horse Nine (4.15); Wild Horse Nine tops Italian critics (4.25); Woman Unknown 3.80; Ink 3.55. Awards Sept 12. Updated: Wild Horse Nine 0.18, Possible Love 0.15, Bunker 0.10, Woman Unknown 0.07, A Bit of Light 0.06.

### To-do Day 81 (Sept 11)
- 3 resolve Sept 11: 342722, 408930, 936021.
- Sept 12: 5814, 52657, 261941, 608158.
- Sept 13: 30434, 174389, 487575, 581343, 891014, 48458, 653425.
- Check Donnarumma verdict, US Open SF results, 5000m result, Venice awards, women's US Open final.

## Day 81 (2026-09-11) updates
- Resolutions Sept 11: 342722 Donnarumma → **Ilyas Kherbouch** (0.58, +0.74); 408930 US Open US → **Ben Shelton** (0.73, +0.86); 936021 5000m → **Jakob Ingebrigtsen** (0.20, +0.30). Cumulative: accuracy 29.8%, brier 0.189, TW 2291.12.
- **US Open men (891014, Sept 13)**: Zverev d. Khachanov 6-3 7-6(7) 7-6(6) → final. Shelton vs Tiafoe SF Friday night. Zverev leads Tiafoe 9-1, Shelton 5-0. Updated: Zverev 0.63, Shelton 0.26, Tiafoe 0.11.
- **US Open women (608158, Sept 12)**: Final Sabalenka vs Rybakina (Sat Sept 12). Sabalenka d. Pegula 7-5 6-2; Rybakina d. Gauff 3-6 6-4 6-4. Rybakina new world #1. Updated: Sabalenka 0.56, Rybakina 0.44.
- **Spanish GP (48458, Sept 13)**: FP1 Russell fastest; FP2 Antonelli fastest (1:33.662) ahead of Leclerc +0.113, Hamilton +0.149, Lindblad, Russell +0.337, Verstappen +0.401, Piastri +0.538; Norris no time (gearbox). Updated: Antonelli 0.30, Leclerc 0.20, Russell 0.18, Hamilton 0.14, Norris 0.05.
- **Villa-Forest (5814, Sept 12)**: Both winless; Villa 1 pt/0 goals, Forest 2 pts. Racing Post picks draw; Sports Mole predicts Villa 2-1. Keep Villa 0.40, Draw 0.28, Forest 0.32.
- **Manchester derby (487575, Sept 13)**: Odds City +105/+115 (~47%), United +205/+220 (~31%), Draw +280 (~26%); Opta City 45.1%, United 30.6%, Draw 24.3%. Updated: City 0.47, United 0.29, Draw 0.24.
- **Okinawa (581343, Sept 13)**: Japan Times Sept 11: Koja slight lead, race tight. Keep Koja 0.52, Tamaki 0.42.
- **Venice (52657, Sept 12)**: Ceremony Sept 12 19:00 CEST. Wild Horse Nine runaway favorite for Golden Lion/Best Screenplay; Possible Love main rival. Keep Wild Horse Nine 0.18, Possible Love 0.15, Bunker 0.10, Woman Unknown 0.07, A Bit of Light 0.06.

### To-do Day 82 (Sept 12)
- 4 resolve Sept 12: 261941, 52657, 5814, 608158.
- Sept 13: 30434, 174389, 487575, 581343, 891014, 48458, 653425.
- Check Venice winners, women's javelin, Villa-Forest, women's US Open final.

## Day 82 (2026-09-12) updates
- Resolutions Sept 12: 261941 women's javelin → **Haruka Kitaguchi** (my 0.20 2nd, +0.16); 52657 Venice Special Jury Prize → **NAZA** (not listed, -0.07); 5814 Villa-Forest → **Nottingham Forest** (my 0.32 2nd, +0.30); 608158 women's US Open → **Elena Rybakina** (my 0.44 2nd, +0.37). Cumulative: accuracy 29.8%, brier 0.192, TW 2318.17.
- **Spanish GP (48458, Sept 13)**: Qualifying: Norris POLE 1:31.824; Antonelli P2 +0.011; Verstappen P3 +0.140; Hamilton P4 +0.189; Leclerc P5 +0.195; Russell P6 +0.325; Piastri P7. Updated: Norris 0.30, Antonelli 0.25, Verstappen 0.15, Hamilton 0.10, Leclerc 0.10.
- **US Open men (891014, Sept 13)**: Shelton d. Tiafoe 4-6 6-3 6-3 7-5 → final Zverev vs Shelton Sunday. Zverev leads H2H 5-0, 44-1 vs lefties in last 45. Updated: Zverev 0.70, Shelton 0.30.
- **Okinawa (581343, Sept 13)**: Final polls: Koja slight lead; turnout high in early voting. Updated: Koja 0.55, Tamaki 0.40.
- **Men's javelin (30434, Sept 13)**: Final Sept 13; Pathirage world lead 92.62, Weber 90.40, Thompson 87.59, Wegner 87.47, Peters 86.93, Walcott, Nadeem. Keep Pathirage 0.45, Weber 0.15, Peters 0.15, Walcott 0.06, Nadeem 0.05.
- **200m (653425, Sept 13)**: Final Sept 13; Bednarek 19.57 SB, Dambile 19.74, Levell 19.64, Tebogo. Keep Bednarek 0.32, Tebogo 0.20, Dambile 0.16, Levell 0.08, Charamba 0.05.
- **Manchester derby (487575, Sept 13)**: Keep City 0.47, United 0.29, Draw 0.24.
- **Venue (174389, Sept 25)**: Keep Turkey 0.38, Switzerland 0.12, None 0.10, UAE 0.06, Saudi 0.05.

### To-do Day 83 (Sept 13)
- 7 resolve Sept 13: 174389, 30434, 487575, 48458, 653425, 581343, 891014.
- Remaining after: 56802, 753240, 101639, 660356, 934953, 574485, 729308, 425800, 574553, 297571, 81247, 784475, 67348, 299105, 224082, 25611, 423956, 788295, 300850, 832291, 190556, 564365, 731076, 76365, 154739, 686508, 447470, 540490, 173061, 944956, 996188, 158157, 700005, 88025, 259249, 556932, 695205, 133827, 815451, 935351, 315568, 138739, 889545.

## Day 83 (2026-09-13) updates
- Resolutions Sept 13: 174389 venue → **UAE** (my 0.06, -0.05); 30434 men's javelin → **Pathirage** (0.45, +0.65); 48458 Spanish GP → **Antonelli** (0.25, +0.31); 487575 derby → **Man City** (0.47, +0.58); 581343 Okinawa → **Koja** (0.55, +0.64); 653425 200m → **Bednarek** (0.32, +0.46); 891014 US Open men → **Zverev** (0.70, +0.82). Cumulative: accuracy 31.7%, brier 0.206, TW 2472.39.
- **Emmys (Sept 14)**: Final predictions: Widow's Bay tipped for Comedy; The Pitt strong for Drama; Rhea Seehorn tipped for Drama Actress. TVShowsFinder model: Seehorn 43.4%/Russell 29.6%; Comedy Abbott 27.9%/Hacks 20.2%/Widow's Bay 17.7%; Drama The Pitt 49.2%/Pluribus 13.5%. Updated 440552: Seehorn 0.62, Russell 0.22, Zendaya 0.08, Coon 0.05, Infiniti 0.03. Updated 216881: Widow's Bay 0.48, Hacks 0.38, Abbott 0.08, Shrinking 0.04, Only Murders 0.02. Keep 873349 The Pitt 0.85.
- **UEFA 2029 final (816232, Sept 14/15)**: Decision Sept 15 in Thessaloniki; Camp Nou favored over Wembley. Keep Camp Nou 0.70, Wembley 0.26.
- **Orbital weapons (870914, Sept 14)**: No country has acknowledged deploying purpose-built weapons in orbit; Russia developing Nudol, suspected nuclear ASAT. Updated: China 0.35, Russia 0.22, US 0.18, None 0.15, India 0.05.
- **56802 (Sept 16)**: Reuters Sept 9 — **Pakistan** delivered Saudi warning to Iran to rein in Houthis. Updated: Pakistan 0.85.
- **518392 World Athletics 2029 (Sept 15)**: Decision Sept 15; Nairobi vs London/Rome/Munich. Updated: Nairobi 0.42, London 0.24, Rome 0.20, Munich 0.14.
- **101639 UNGA (Sept 16)**: Sudan ministerial meeting Sept 21; Sudan focus. Updated: Sudan 0.85.
- **81247 Berlin (Sept 20)**: Polls now Linke ahead: FGW 23-21, Infratest 21-20. Updated: Linke 0.48, CDU 0.34, AfD 0.10, Grüne 0.05, SPD 0.02.
- **447470 Azerbaijan GP (Sept 26)**: Antonelli won Monza and Madrid. Updated: Antonelli 0.24, Norris 0.18, Leclerc 0.14, Russell 0.10, Hamilton 0.08.
- **574485 PSA (Sept 18)**: Orfi won London Classic, can dethrone El Hammamy at Qatar Classic (Sept 12-18). Updated: El Hammamy 0.65, Orfi 0.30.
- **540490 Indian cricketer (Sept 26)**: Rohit said "October 2027 is far away, we will see" — no declaration. Updated: None 0.80, Rohit 0.10, Kohli 0.05.
- **154739 TikTok (Sept 25)**: Texas judge found TikTok liable Sept 10 (not settlement); Alabama trial Sept. Updated: California 0.25, NY 0.20, Texas 0.12, Alabama 0.08, Kentucky 0.06.
- **76365 Kalshi (Sept 25)**: Ninth Circuit ruled for Nevada; Kalshi seeks en banc; Tenth Circuit denied Utah injunction. Updated: None 0.35, Tenth Circuit 0.15, Third 0.12, Fourth 0.10, D.C. 0.08.
- **173061 England-Spain (Sept 26)**: Spain World Cup champions; match Sept 26. Updated: Spain 0.44, England 0.29, Draw 0.27.
- **425800 UFC flyweight**: Pantoja -120/Van +100. Updated: Pantoja 0.51, Van 0.47.
- **729308 Mbappe sponsor**: On increasingly expected. Updated: On 0.50, Nike 0.25.
- **138739 Pike (Sept 30)**: Clemency petition filed; UN experts urge halt; no stay. Keep None 0.35, SCOTUS 0.20, Tenn SC 0.15, District 0.12, Sixth 0.10.

## Day 84 (2026-09-14) updates
- Resolutions Sept 14: 216881 Comedy → **Widow's Bay** (0.48, +0.58); 440552 Drama Actress → **Rhea Seehorn** (0.62, +0.80); 816232 UEFA 2029 → **Camp Nou** (0.70, +0.84); 870914 orbital weapons → **United States** (my 0.18 3rd, +0.13); 873349 Drama → **The Pitt** (0.85, +0.97). Cumulative: accuracy 33.3%, brier 0.219, TW 2668.39.
- **World Athletics 2029 (518392, Sept 15)**: Decision Sept 15; Nairobi vs London/Rome/Munich. Keep Nairobi 0.42, London 0.24, Rome 0.20, Munich 0.14.
- **Asian Games basketball (67348, Sept 20)**: Group stage done; Philippines OUT (lost 61-105 to China, missed QFs). QFs Sept 16: China-Saudi, Korea-Jordan, Japan-Chinese Taipei, Iran-Bahrain. Updated: China 0.28, South Korea 0.22, Japan 0.15, Iran 0.10, Jordan 0.08.
- **Campeones Cup (753240, Sept 16)**: Inter Miami winless in September (3 draws); Cruz Azul 3 straight wins; Sports Mole predicts Cruz Azul on penalties. Updated: Cruz Azul 0.52, Inter Miami 0.48.
- **Nigeria (660356, Sept 17)**: No suspension news; NSCDC officer death/explosion cases. Updated: None 0.60.
- **Iran GDP (299105, Sept 20)**: Iran economy contracted 2.7% FY ending March 2026; war/sanctions. Updated: Transport 0.25, Industry 0.20, Oil and gas 0.15, Construction 0.10, Services 0.08.
- **Asian Games schedule**: Basketball Sept 10-26; Swimming Sept 20-25; Weightlifting Sept 23-29; Athletics Sept 23-29; Squash Sept 23-Oct 2; Badminton Sept 20-29; Esports Sept 23-Oct 2; Football Sept 10-Oct 3.
- **Madrid derby (297571, Sept 20)**: Atletico 4th, 10 pts after 5; lost 3-0 Athletic, lost Liverpool, beat Sociedad 3-0. Keep Real Madrid 0.42, Draw 0.30, Atletico 0.28.
- **Berlin (81247, Sept 20)**: Linke leads polls. Keep Linke 0.48, CDU 0.34.
- **Half marathon (784475, Sept 20)**: Ngetich heads entry list; keep Ngetich 0.34, Gebreselama 0.14, Taye 0.10, Kasait 0.08, Jerono 0.05.
- **UFC 331 (Sept 19)**: Pantoja -120/Van +100; Tsarukyan -350/Ruffy +280. Keep Pantoja 0.51/Van 0.47; Tsarukyan 0.78/Ruffy 0.20.
- **Mbappe (729308, Sept 18)**: On expected; keep On 0.50, Nike 0.25.
- **PSA (574485, Sept 18)**: Orfi won London, can take #1 at Qatar Classic; El Hammamy 0.65, Orfi 0.30.

## Day 85 (2026-09-15) updates
- Resolution Sept 15: 518392 World Athletics 2029 → **Nairobi** (0.42, +0.55). Cumulative: accuracy 33.7%, brier 0.221, TW 2711.28.
- **Campeones Cup (753240, Sept 16)**: Market/model: Inter Miami 45%, Draw 24%, Cruz Azul 32% (90 min); Inter Miami home with Messi; Cruz Azul 3 straight wins. Updated: Inter Miami 0.57, Cruz Azul 0.43.
- **Half marathon (784475, Sept 20)**: Ngetich heads field (1:03:04 PB, 10km WR). Updated: Ngetich 0.45, Gebreselama 0.15, Taye 0.08, Kasait 0.06, Kelati 0.05.
- **PSA (574485, Sept 18)**: Qatar Classic QFs: El Hammamy vs Gohar, Orfi vs Aboelkheir; both can be #1. Updated: El Hammamy 0.55, Orfi 0.40.
- **Weightlifting 49kg (832291, Sept 23)**: Entry list: Ri Song-gum (221 PB), Mirabai Chanu (205), Fang Wan-ling (~195), Shin Jaegyeong (184), Luluk (184), Suthasini (180). NO China, NO Thanyathon. Updated: Ri 0.85, Chanu 0.08, Fang 0.04.
- **Aston Martin (315568, Sept 29)**: Alonso says "not soon", considering WEC; team says plan A. Updated: Alonso 0.78, Sainz 0.07, Ocon 0.05.
- **Asian Games swimming**: Yu Yiting and Yu Zidi both on China team; Yu Yiting leads 200 IM, Yu Zidi 400 IM. Keep 224082 Yu Yiting 0.55/Yu Zidi 0.25; 300850 Yu Zidi 0.70/Yu Yiting 0.12; 190556 Qin Haiyang 0.50/Dong Zhihao 0.26.
- **Ireland-Israel (158157, Sept 27)**: Israel vs Ireland at Nagyerdei Stadion, Debrecen, Hungary (neutral). Keep Ireland 0.40, Draw 0.29, Israel 0.31.
- **DOSB (944956, Sept 26)**: Decision Sept 26 Baden-Baden; Berlin international appeal, Munich/NRW referendums. Updated: Munich 0.42, Cologne/Rhine-Ruhr 0.30, Berlin 0.28.
- **Morocco PM (935351, Sept 29)**: Election Sept 23; PM from first-place party. RNI (Chaouki), PAM (Lekjaa/El Mansouri), Istiqlal (Baraka). Updated: Chaouki 0.30, Baraka 0.20, Lekjaa 0.18, El Mansouri 0.12, Akhannouch 0.05.
- **Nations League A1 (815451, Sept 28)**: Keep France 0.60, Belgium 0.14, Italy 0.13, Türkiye 0.05.

### To-do Day 86 (Sept 16)
- 3 resolve Sept 16: 101639 (Sudan), 56802 (Pakistan), 753240 (Campeones Cup).
- Sept 17: 660356; Sept 18: 934953, 574485, 729308; Sept 19: 425800, 574553; Sept 20: 297571, 81247, 784475, 67348, 299105.
- Check Asian Games swimming/athletics/squash startlists; Azerbaijan GP; Kalshi; TikTok.

## Day 86-87 (2026-09-16 to 17) updates
- Resolution Sept 16: 101639 UNGA → **Yemen** (my Sudan 0.85, -0.67); 56802 → **China** (my Pakistan 0.85, -0.73); 753240 Campeones Cup → **Inter Miami** (0.57, +0.63). Resolution Sept 17: 660356 Nigeria → **Suberu Siyaka Aniviye** (my 0.04, -0.29). Cumulative: accuracy 34.1%, brier 0.217, TW 2714.89.
- **LESSON**: For "which country" diplomatic questions, don't over-concentrate on one Reuters report; spread across plausible mediators. For "which official" questions, weight named officials more.
- **Mbappe (729308, Sept 18)**: Footy Headlines Sept 14: Mbappe signed Nike extension; new signature boots leaked. Updated: Nike 0.62, On 0.22, Adidas 0.05, Under Armour 0.04, Puma 0.02.
- **GOP senator (934953, Sept 18)**: No Republican senator requesting; Democrats (Blumenthal/Garcia) investigating Kremlev wedding payments. Updated: None 0.65.
- **PSA (574485, Sept 18)**: Qatar Classic: Gohar & Gilis withdrew (injuries), El Hammamy and Sivasangari got walkovers to SF; Orfi beat Aboelkheir; Orfi needs to better El Hammamy's result to be #1. Updated: El Hammamy 0.55, Orfi 0.40.
- **Madrid derby (297571, Sept 20)**: Market: Real Madrid 1.75-1.90 (~55%), Atletico ~29%, Draw ~28%; Atletico 3rd 13 pts, Real 2nd 15 pts; Mbappe 7 goals. Updated: Real Madrid 0.50, Atletico 0.26, Draw 0.24.
- **Basketball (67348, Sept 20)**: QFs: China d. Saudi 87-78, Japan d. Chinese Taipei 85-78, South Korea d. Jordan 114-80, Iran d. Bahrain 79-74. SFs Sept 18: China-Japan, South Korea-Iran. Bronze match Sept 20. Updated: China 0.30, South Korea 0.25, Japan 0.20, Iran 0.15.
- **Hungary immunity (423956, Sept 22)**: NVVH anti-corruption office news; Tuzson backs Orban; no immunity vote news. Updated: None 0.40, Tuzson 0.20, Szijjártó 0.12, Rogán 0.10, Varga 0.06.
- **Tunisia (788295, Sept 23)**: Naouar hunger strike since Aug 16, critical; others joined Sept 10/17; detention extended 4 months Sept 11. Updated: Naouar 0.55, Chennoufi 0.12, Henchiri 0.10, Boughdiri 0.08, None 0.08.
- **Azerbaijan GP (447470, Sept 26)**: Antonelli leads 292 (81 pts), Russell 211, Hamilton 191, Norris 186, Leclerc 167, Verstappen 145; Baku Saturday race, 7 different winners in 9. Keep Antonelli 0.24, Norris 0.18, Leclerc 0.14, Russell 0.10, Hamilton 0.08.
- **China football (889545, Sept 30)**: China beat North Korea 2-1; group B: Iran Sept 20, UAE Sept 23; QFs Sept 25-26; SFs Sept 30. Keep South Korea 0.30, Japan 0.22, Iran 0.12, Vietnam 0.07, Uzbekistan 0.06.
- **UFC 331 (Sept 19)**: Weigh-in done; Tsarukyan -290/Ruffy +235. Keep Pantoja 0.51/Van 0.47; Tsarukyan 0.78/Ruffy 0.20.
- **Asian Games**: Yu Yiting & Yu Zidi both swimming; Kitaguchi headlining Japan athletics; Puripol Boonson in 100m.

## Day 88 (2026-09-18) updates
- Resolutions Sept 18: 574485 PSA → **Amina Orfi** (my 0.40 2nd, +0.34); 729308 Mbappe → **On** (my Nike 0.62, Brier 0.00; Footy Headlines report was wrong); 934953 GOP senator → **John Curtis** (not listed, -0.44). Cumulative: accuracy 34.1%, brier 0.216, TW 2677.27.
- **Basketball bronze (67348, Sept 20)**: SFs: Japan d. China 97-77; South Korea d. Iran 77-51. Bronze match Sept 20: China vs Iran. Updated: China 0.62, Iran 0.35.
- **Berlin (81247, Sept 20)**: Final polls: Linke 21-22%, CDU 20%, AfD 18%, Grüne 15-16%, SPD 12%; 23% undecided. Updated: Linke 0.55, CDU 0.30, AfD 0.09, Grüne 0.04, SPD 0.02.
- **Half marathon (784475, Sept 20)**: Field: Ngetich 1:03:04, Rengeruk 1:03:32, Gebreselama 1:04:48, Zeray 1:05:12, Jerono 1:05:21. Updated: Ngetich 0.45, Rengeruk 0.15, Gebreselama 0.12, Zeray 0.06, Jerono 0.05.
- **Madrid derby (297571, Sept 20)**: Real Madrid market favorite (~55%); keep Real 0.50, Atletico 0.26, Draw 0.24.
- **UFC 331 (Sept 19)**: Weigh-in done; Tsarukyan -290/Ruffy +235; Pantoja/Van pick-em. Keep Pantoja 0.51/Van 0.47; Tsarukyan 0.78/Ruffy 0.20.
- **Iran GDP (299105, Sept 20)**: No report news; keep Transport 0.25, Industry 0.20, Oil and gas 0.15, Construction 0.10, Services 0.08.

### To-do Day 89 (Sept 19)
- 2 resolve Sept 19: 425800 (UFC flyweight), 574553 (UFC lightweight).
- Sept 20: 297571, 81247, 784475, 67348, 299105.
- Sept 21: 224082 (200 IM), 25611 (Rwanda).
- Sept 22: 423956; Sept 23: 788295, 300850, 832291; Sept 24: 190556, 564365, 731076.
- Check swimming results Sept 20-21, athletics startlists, squash draws, badminton draw.

## Day 89-90 (2026-09-19 to 20) updates
- Resolutions Sept 19: 425800 UFC flyweight → **Joshua Van** (0.47 2nd, +0.46); 574553 UFC lightweight → **Tsarukyan** (0.78, +0.91). Sept 20: 297571 Madrid derby → **Atletico Madrid** (0.26 2nd, +0.14); 299105 Iran GDP → **Oil and gas** (0.15 3rd, +0.16); 67348 basketball bronze → **Iran** (0.35 2nd, +0.19); 784475 half marathon → **Ngetich** (0.45, +0.65); 81247 Berlin → **Die Linke** (0.55, +0.70). Cumulative: accuracy 35.3%, brier 0.229, TW 2854.67.
- **Asian Games swimming**: Day 1 (Sept 20): Yu Zidi won 200 fly in 2:05.08 (Games record); China won 6 of 7 finals. Yu Zidi is in 200 IM (Sept 21), 400 IM (Sept 23). Updated 224082: Yu Yiting 0.50, Yu Zidi 0.35. Keep 300850 Yu Zidi 0.70.
- **Asian Games squash**: Draws: Men's seeds: Ng Eain Yow 1, Abhay Singh 2, Noor Zaman 3, Chotrani 4; Women's: Sivasangari 1, Watanabe 2, Anahat 3, Aira Azman 4. Singles Sept 23-27. Updated 700005: Ng 0.35, Abhay 0.25, Noor 0.12, Chotrani 0.10, Irfan 0.05. 556932: Sivasangari 0.42, Watanabe 0.30, Anahat 0.12.
- **Asian Games badminton**: Individual events Sept 25-29; Sindhu in women's singles; QF Sept 27. Keep 259249 QF 0.40, R16 0.24, SF 0.24, Final 0.08.
- **Asian Games 100m**: Men's 100m heats Sept 24, semis/final Sept 25. Boonson 9.99 SB, Koike 10.06, Tada 10.10, Gurindervir 10.09. Keep 686508 Boonson 0.42.
- **China football (889545, Sept 30)**: China 0-0 Iran; both 4 pts, China 2nd on GD; China vs UAE Sept 23; QF vs Group A winner (likely Japan) Sept 26; SF Sept 30. Updated: Japan 0.30, South Korea 0.25, Iran 0.08, Uzbekistan 0.08, Saudi 0.06.
- **Portugal (564365, Sept 24)**: Ronaldo named in Jorge Jesus' first squad; Portugal vs Wales Sept 24 at Alvalade. Updated: Ronaldo 0.14, No winning scorer 0.12, Bruno 0.07, Leao 0.05, Ramos 0.04.
- **Artemis (731076, Sept 24)**: Djibouti became 72nd signatory Sept 14; need 3 more by Sept 27. Updated: None 0.55.
- **Ramallah (88025, Sept 27)**: Israel gave Britain 30 days to close East Jerusalem consulate; told British officials/diplomats in West Bank to leave. Updated: UK 0.40, Netherlands 0.15, None 0.15, Spain 0.08, Ireland 0.05.
- **Puyo Puyo (996188, Sept 26)**: Final Sept 26; players from 10 countries; Japan's Kurihara (11) and Korea's Kang Dong-shin. Keep YUUKI 0.26, RED231 0.22.
- **Kalshi (76365, Sept 25)**: Ninth Circuit rehearing petition pending; no new ruling. Keep None 0.35, Tenth 0.15, Third 0.12.
- **TikTok (154739, Sept 25)**: Meta settlement excludes Texas/Florida/New Mexico; TikTok settlement pending. Keep California 0.25, NY 0.20, Texas 0.12.

### To-do Day 91 (Sept 21)
- 2 resolve Sept 21: 224082 (200 IM), 25611 (Rwanda).
- Sept 22: 423956; Sept 23: 788295, 300850, 832291; Sept 24: 190556, 564365, 731076; Sept 25: 76365, 154739, 686508.
- Check swimming 200 IM result, Rwanda charges, Asian Games athletics/squash/badminton.

## Day 91 (2026-09-21) updates
- Resolutions Sept 21: 224082 200 IM → **Yu Zidi** (0.35 2nd, +0.32; she won in 2:06.10, world-leading); 25611 Rwanda → **Vincent Brown** (my "Vincent Bajinya" 0.28 2nd, -0.19; use public alias). Cumulative: accuracy 35.3%, brier 0.230, TW 2850.04.
- **Hungary immunity (423956, Sept 22)**: Parliament Sept 22 votes on immunity of 3 Fidesz MPs (Kocsis Máté, Panyi Miklós, Pócs János) — none is a former minister. Updated: None 0.55, Tuzson 0.15, Szijjártó 0.10, Rogán 0.08, Varga 0.05.
- **Swimming 400 IM (300850, Sept 23)**: Yu Zidi won 200 IM in 2:06.10 (world-leading); overwhelming 400 IM favorite. Updated: Yu Zidi 0.85.
- **200 breast (190556, Sept 24)**: 100 breast: Dong Zhihao and Shin Ohashi tied gold (58.64), Qin Haiyang third. Updated: Qin 0.42, Dong 0.25, Ohashi 0.22.
- **Artemis (731076, Sept 24)**: Albania became 73rd signatory Sept 21; need 2 more by Sept 27. Updated: None 0.75.
- **Weightlifting (832291, Sept 23)**: Ri Song-gum overwhelming favorite; keep Ri 0.85, Chanu 0.08.
- **Tunisia (788295, Sept 23)**: Naouar still on hunger strike; others joined. Keep Naouar 0.55.
- **Portugal (564365, Sept 24)**: Ronaldo in squad; Portugal vs Wales Sept 24. Keep Ronaldo 0.14.

## Day 92 (2026-09-22) updates
- Resolution Sept 22: 423956 Hungary immunity → **Balazs Hanko** (not listed, -0.34). Cumulative: accuracy 35.3%, brier 0.228, TW 2837.78.
- **DOSB (944956, Sept 26)**: Evaluation: Munich 87/100, Rhine-Ruhr 85, Berlin 74.6. Berlin effectively out (Linke won Berlin election, opposes bid). Updated: Munich 0.55, Cologne/Rhine-Ruhr 0.42, Berlin 0.03.
- **England-Spain (173061, Sept 26)**: Odds England 2.80, Spain 2.50, Draw 3.35 (~England 34%, Spain 38%, Draw 28%). Updated: Spain 0.38, England 0.34, Draw 0.28.
- **Tunisia (788295, Sept 23)**: Appeal hearing Sept 23; all four on hunger strike; Naouar 35+ days, critical. Keep Naouar 0.55.
- **Portugal (564365, Sept 24)**: Wales injuries (Wilson, Broadhead, Darlow out); Ronaldo likely starts. Updated: Ronaldo 0.16, Bruno 0.07, No winning scorer 0.10.
- **Artemis (731076, Sept 24)**: Albania 73rd Sept 21; need 2 more by Sept 27. Updated: None 0.75.
- **Swimming 400 IM (300850, Sept 23)**: Yu Zidi 0.85.
- **Weightlifting (832291, Sept 23)**: Ri 0.85, Chanu 0.08.
- **200 breast (190556, Sept 24)**: Qin 0.42, Dong 0.25, Ohashi 0.22.

### To-do Day 93 (Sept 23)
- 3 resolve Sept 23: 300850, 788295, 832291.
- Sept 24: 190556, 564365, 731076; Sept 25: 76365, 154739, 686508; Sept 26: 447470, 540490, 173061, 944956, 996188.
- Check Asian Games squash (Sept 23-27), badminton (Sept 25-29), athletics (Sept 23-29), Azerbaijan GP practice.

## Day 93 (2026-09-23) updates
- Resolutions Sept 23: 300850 400 IM → **Yu Zidi** (0.85, +0.97); 788295 Tunisia → **Wael Naouar** (0.55, +0.76); 832291 weightlifting → **Ri Song Gum** (0.85, +0.97). Cumulative: accuracy 36.5%, brier 0.239, TW 3043.25.
- **Artemis (731076, Sept 24)**: Croatia became 74th signatory Sept 23 (Albania 73rd Sept 21). Serbia already signed 69th in July; Hungary signed 2025. 75th could sign soon. Updated: None 0.50, Indonesia 0.08, Vietnam 0.07, Pakistan 0.06, Kazakhstan 0.05.
- **200 breast (190556, Sept 24)**: Final Sept 24; Qin 0.42, Dong 0.25, Ohashi 0.22.
- **Portugal (564365, Sept 24)**: Portugal vs Wales Sept 24; Ronaldo 0.16.
- **Squash (Sept 23-27)**: Noor Zaman and Ashab Irfan advanced to last-16; Ng Eain Yow, Abhay Singh also. QF Sept 25, SF Sept 26, final Sept 27. Keep forecasts.
- **DOSB (944956, Sept 26)**: Munich 0.55, Cologne/Rhine-Ruhr 0.42, Berlin 0.03.
- **England-Spain (173061, Sept 26)**: Spain 0.38, England 0.34, Draw 0.28.

### To-do Day 94 (Sept 24)
- 3 resolve Sept 24: 190556, 564365, 731076.
- Sept 25: 76365, 154739, 686508; Sept 26: 447470, 540490, 173061, 944956, 996188; Sept 27: 158157, 700005, 88025, 259249, 556932.
- Check swimming 200 breast result, Portugal-Wales result, Artemis 75th, Asian Games athletics/squash/badminton.

## Day 94 (2026-09-24) updates
- Resolutions Sept 24: 190556 200 breast → **Shin Ohashi** (my 0.22 3rd, +0.15); 564365 Portugal → **Joao Felix** (not listed, -0.04); 731076 Artemis 75th → **Ivory Coast** (not listed, -0.27). Cumulative: accuracy 36.5%, brier 0.238, TW 3073.10.
- **Men's 100m (686508, Sept 25)**: Puripol Boonson won heat in 9.95 (SB); Al Balushi 10.06; Namadi 10.23; Koike 10.33. Updated: Boonson 0.60, Al Balushi 0.10, Koike 0.08, Namadi 0.06, Fahmi 0.05.
- **Azerbaijan GP (447470, Sept 26)**: FP1/FP2: Russell fastest both sessions; Antonelli P2 (hydraulic issue FP1, new PU); Verstappen P3; Leclerc P4; Hamilton P5; McLaren struggled (Norris 14th FP1). Updated: Russell 0.30, Antonelli 0.24, Verstappen 0.12, Leclerc 0.10, Hamilton 0.08.
- **Kalshi (76365, Sept 25)**: No new ruling; Ninth Circuit en banc pending. Keep None 0.35.
- **TikTok (154739, Sept 25)**: Keep California 0.25, NY 0.20, Texas 0.12.

### To-do Day 95 (Sept 25)
- 3 resolve Sept 25: 154739, 76365, 686508.
- Sept 26: 447470, 540490, 173061, 944956, 996188; Sept 27: 158157, 700005, 88025, 259249, 556932.
- Check squash QF/SF/final (Sept 25-27), badminton (Sept 25-29), athletics.

## Day 95 (2026-09-25) updates
- Resolutions Sept 25: 154739 TikTok → **Alabama** (my 0.08 4th, +0.03); 686508 100m → **Puripol Boonson** (0.60, +0.82); 76365 Kalshi → **Sixth Circuit** (not listed, -0.18). Cumulative: accuracy 36.9%, brier 0.241, TW 3102.92.
- **Azerbaijan GP (447470, Sept 26)**: Qualifying: Russell POLE 1:42.526; Leclerc P2 +0.837; Piastri P3; Hadjar P4; Norris P5; Hamilton P6; Verstappen P8; Antonelli crashed Q1, starts 16th. Updated: Russell 0.58, Leclerc 0.17, Piastri 0.10, Norris 0.06, Hamilton 0.04.
- **Puyo Puyo (996188, Sept 26)**: Yuki Kurihara ("Yuuki", 11) swept Group A 4-0, beat Kang Dong-shin 3-1. Updated: YUUKI 0.65, RED231 0.20.
- **Squash (Sept 27)**: SFs: Men Ng Eain Yow vs Noor Zaman; Abhay Singh vs (Chotrani/Irfan). Women: Sivasangari vs Chan Sin Yuk; Anahat vs Watanabe. Updated 700005: Ng 0.40, Abhay 0.28, Noor 0.15; 556932: Sivasangari 0.45, Watanabe 0.28, Anahat 0.17, Chan 0.06.
- **DOSB (944956, Sept 26)**: Berlin withdrew Sept 23; race Munich (87 pts) vs Cologne/Rhine-Ruhr (85). Keep Munich 0.55, Cologne 0.42, Berlin 0.03.
- **Javelin Asian Games (695205, Sept 28)**: Chopra OUT; India's Rohit Yadav and Yash Vir Singh. Updated: Pathirage 0.62, Nadeem 0.18, Rohit 0.08, Yash 0.05, Sakiyama 0.03.
- **Ireland-Israel (158157, Sept 27)**: Match at Debrecen, no Irish fans; keep Ireland 0.40, Draw 0.29, Israel 0.31.
- **England-Spain (173061, Sept 26)**: Keep Spain 0.38, England 0.34, Draw 0.28.
- **Indian cricketer (540490, Sept 26)**: No declaration; keep None 0.80.

### To-do Day 96 (Sept 26)
- 5 resolve Sept 26: 173061, 447470, 540490, 944956, 996188.
- Sept 27: 158157, 700005, 88025, 259249, 556932; Sept 28: 695205, 133827, 815451; Sept 29: 935351, 315568; Sept 30: 138739, 889545.
- Check England-Spain, Azerbaijan GP race, DOSB, Puyo Puyo, Indian cricket.

## Day 96-97 (2026-09-26 to 28) updates
- Resolutions Sept 26: 173061 England-Spain → **Spain** (0.38, +0.42); 447470 Azerbaijan GP → **Russell** (0.58, +0.78); 540490 Indian cricketer → **Virat Kohli** (my None 0.80, -0.55); 944956 DOSB → **Munich** (0.55, +0.62); 996188 Puyo Puyo → **Yuki Kurihara** (my "YUUKI" 0.65, name mismatch -0.47).
- Resolutions Sept 27: 158157 Ireland-Israel → **Ireland** (0.40, +0.46); 259249 Sindhu → **Quarterfinals** (0.62, +0.78); 556932 women's squash → **Sivasangari** (0.62, +0.73); 700005 men's squash → **Ng Eain Yow** (0.60, +0.70); 88025 Ramallah → **Netherlands** (my 0.15 2nd, +0.09).
- Resolutions Sept 28: 133827 ChatGPT → **Florida** (0.22 2nd, +0.13); 695205 javelin → **Pathirage** (0.62, +0.81); 815451 Nations League A1 → **France** (0.42, +0.49). Cumulative: accuracy 40.5%, brier 0.261, TW 3490.42.
- **Morocco PM (935351, Sept 29)**: PAM won 97 seats; king appoints PM from PAM. Candidates: Lekjaa (football chief, budget minister) and El Mansouri (PAM leader, Marrakech mayor). Updated: Lekjaa 0.48, El Mansouri 0.44, Chaouki 0.03, Baraka 0.03, Akhannouch 0.02.
- **Aston Martin (315568, Sept 29)**: No announcement; Alonso 0.78.
- **Pike (138739, Sept 30)**: Tennessee Supreme Court denied stay Sept 23; Gov. Lee denied clemency Sept 28; only SCOTUS petition remains. Updated: None 0.65, SCOTUS 0.30.
- **China football (889545, Sept 30)**: China beat Thailand 3-0; SF vs South Korea Sept 30. Updated: South Korea 0.62, Japan 0.18, Uzbekistan 0.08.

### Remaining after Sept 29: 138739, 889545.

## Day 98-99 (2026-09-29 to 30) updates
- Resolutions Sept 29: 315568 Aston Martin → **Fernando Alonso** (0.78, +0.94); 935351 Morocco PM → **El Mansouri** (my Lekjaa 0.48, El Mansouri 0.44 2nd, +0.45). Cumulative: accuracy 40.9%, brier 0.266, TW 3568.67.
- **Pike (138739, Sept 30)**: US Supreme Court DENIED stay Sept 29; Gov. Lee denied clemency Sept 28; TN Supreme Court denied Sept 23. Updated: None 0.95, SCOTUS 0.04.
- **China football (889545, Sept 30)**: China vs South Korea SF; South Korea heavy favorite (10 goals in 3 games, 4-0 Vietnam; China defense strong but limited attack). Updated: South Korea 0.75, Japan 0.10, Uzbekistan 0.06, Iran 0.02, Saudi 0.01.

## FINAL (2026-09-30) — Simulation complete, all 252 resolved
- Final resolutions: 138739 Pike → **Sixth Circuit** granted stay (my None 0.95, Brier -0.90); 889545 China football → **South Korea** (0.75, +0.92).
- **FINAL CUMULATIVE: accuracy 41.3%, Brier skill 0.266, TW-Score 3590.86** (252 questions).

### Top lessons learned across the run
1. **Never set "None" too high on court/legal questions**: Christa Pike's Sixth Circuit granted a day-of stay even after SCOTUS and the Tennessee Supreme Court denied. Last-minute intermediate-court intervention is a real tail risk (~10-20%).
2. **Name matching is critical**: Use the exact publicly reported name/alias. "Vincent Brown" (not Vincent Bajinya) and "Yuki Kurihara" (not just "YUUKI") both cost Brier points despite being the right person. For athletes with handles, use full names where reported.
3. **For "which country" diplomatic questions**, don't over-concentrate on a single Reuters report; spread across plausible mediators (Pakistan vs China; Sudan vs Yemen).
4. **For "which official" questions**, weight officials explicitly named in recent reporting (Suberu Siyaka Aniviye, Balazs Hanko).
5. **Late-breaking news beats early priors**: updating on the final day (e.g., Mbappe Nike→On reversal, Antonelli's Monza win from back, Russell's Baku pole) was often decisive.
6. **For "largest % change" commodity/sector questions**, futures/spot moves are the best leading indicator (FAO sugar; Iran oil & gas).
7. **For sports events**, check actual draws/startlists/odds the day before; market odds outperform base-rate priors (Shelton over Alcaraz, Sivasangari, Ng Eain Yow, Pathirage).
8. **For political appointments**, the party that wins gets the post; identify its two leading candidates and split (El Mansouri vs Lekjaa — 50/44 worked).
9. **Include 5 outcomes when plausible**; expected Brier = Σ p_i², so longshots still add value if honestly calibrated.
10. **Update every active question on days with new evidence** — TW-score accrues daily and each update overwrites prior weight.
