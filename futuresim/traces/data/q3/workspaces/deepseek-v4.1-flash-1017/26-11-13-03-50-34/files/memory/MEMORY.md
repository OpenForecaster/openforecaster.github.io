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

## Corrections logged 2026-06-24 (post-submission research)
- **Jaylen Brown (344207)**: Giannis was traded to MIAMI (not Boston); Boston's offer of Brown+2 firsts rejected. Brown likely stays; if traded, destination unknown — updated spread to Brooklyn/Houston/Detroit/Miami/San Antonio.
- **Women's T20 World Cup (258607/799550)**: Final is July 5 at Lord's; semifinals June 30 (SF1) & July 2 (SF2) at The Oval. Group stage ends June 28 (Australia v India at Lord's).
- **SK Hynix (279946)**: Confirmed $29.4B Nasdaq ADR listing, pricing ~July 9, trading July 10 → would beat Alibaba's $25B foreign-issuer US IPO record.
- **Alcaraz (855662 etc.)**: Out of Wimbledon; return earliest Canada Masters (Aug 2). Sinner dominant #1.

## Day 2 (2026-06-25) notes
- World Cup: Brazil won Group C (beat Scotland 3-0); Morocco 2nd (4-2 Haiti). Mexico won Group A 3-0 over Czechia; South Africa beat South Korea to take 2nd in A. Germany won Group E despite losing 2-1 to Ecuador; Ivory Coast 2nd (Pepe brace); Ecuador advances as 3rd. Group F final June 25 (Japan-Sweden, Tunisia-Netherlands); Group G final June 25 (Egypt-Iran, NZ-Belgium). Group I June 26 (Norway-France). Group H June 26 (Uruguay-Spain). Groups J/K/L June 27.
  - Confirmed R16: M89 (Jul 4, Philadelphia) = Germany vs France (likely). Boston QF M97 = France/Germany vs W90 (Canada vs Netherlands/Japan/Morocco).
- F1 Austrian GP June 28 odds: Antonelli +200, Hamilton +300, Russell +300, Leclerc +700, Verstappen +850, Norris +900. Antonelli leads championship 156, Hamilton 115, Russell 106, Leclerc 75.
- Wimbledon: Sinner #1 seed, Zverev #2, Auger-Aliassime #3, Shelton #4, de Minaur #5, Fritz #6, Djokovic #7, Medvedev #8. Draw June 26. Women: Sabalenka #1, Rybakina #2, Swiatek #3.
- Women's T20 WC: England qualified (beat WI); SF1 June 30, SF2 July 2, Final July 5. Australia likely Group A winner.
- UFC 330 confirmed: Makhachev vs Machado Garry (welterweight), Dern vs Robertson (strawweight), Aug 15 Philadelphia.
- MLB All-Star: Ohtani & Ernie Clement won Phase 1 fan vote; ASG July 14 Citizens Bank Park.
- Jaylen Brown: Rockets and Pelicans held trade talks with Boston; Celtics want a big man (Trey Murphy III interest); Minnesota traded for LaMelo Ball. Brown hasn't requested trade.
- Khamenei funeral: Iran hasn't released foreign dignitary list; Pakistan PM Sharif confirmed attending; Russia expected to send delegation (Volodin precedent from Raisi).
- FDA: shortlist includes Heidi Overton, John Crowley, Jeff Vacirca, Kyle Diamantas, Sharpless; RBC expects Diamantas through midterms.
- UN SG: first straw poll late July; field Grossi/Grynspan/Bachelet/Espinosa/Sall.
- Cornyn lost Texas GOP Senate primary to Paxton; Cassidy lost Louisiana primary. El-Sayed rising in Michigan.
- Iran attacked Singapore-flagged ship in Hormuz June 25 (first since MoU); IMO paused evacuation; oil ~$75 Brent.
- Updates submitted 6/25: 659176, 344207, 457239, 754639, 742225, 985440, 199448, 935518, 439898, 720892, 934953, 970733.

## Day 3 (2026-06-26) notes
- **US launched retaliatory strikes on Iran** (missile/drone storage sites) after IRGC drone attack on Singapore-flagged cargo ship June 25; ceasefire fragile; Iran insists on control of Hormuz; IMO paused evacuations. Oil ~$75 Brent.
- **FOMC (942650)**: New Chair Kevin Warsh. June 16-17 unanimous hold at 3.50-3.75%; May PCE 4.1% (core 3.4%); 9/18 dots show hikes; market ~30% July hike, ~80% Sept hike. 2026 voters: Warsh, Williams, Barr, Bowman, Cook, Hammack, Jefferson, Kashkari, Logan, Paulson, Powell, Waller. Updated 942650: None 0.55 + possible hawk dissenters.
- **Wimbledon draw**: Sinner & Djokovic same half (SF); Zverev other half with Shelton/Fritz. Sinner R1 Kecmanovic. Women: Sabalenka #1. Serena Williams returns vs Maya Joint. Updated 985440.
- **World Cup**: France won Group I (4-1 Norway, Dembele hat-trick); Netherlands won Group F (3-1 Tunisia); Japan 2nd (1-1 Sweden); Australia 2nd Group D (0-0 Paraguay); Turkey beat USA 3-2 (dead rubber). Group G/H finals late June 26.
  - Confirmed R32: Jun 28 South Africa-Canada (M73); Jun 29 Brazil-Japan (M76), Germany-3rd (M74, Boston), Netherlands-Morocco (M75); Jun 30 Ivory Coast-Norway (M78), France-3rd (M77, NY/NJ), Mexico-3rd (M79); Jul 1 England-3rd (M80), Egypt-3rd (M82), USA-3rd (M81); Jul 2 Spain-Austria (M84), Portugal-Ghana (M83), Switzerland-3rd (M85); Jul 3 Australia-Iran (M86), Argentina-Uruguay (M87), Colombia-3rd (M88).
  - Golden Boot: Messi 5 (odds +170), Mbappe 4 (+225), Haaland 4 (+750), Vinicius +800, Kane +850. Updated 201629/581542.
- **Venezuela earthquakes** (Jun 24, M7.2 & 7.5): 164+ dead; Delcy Rodríguez acting president; post-Maduro talks (Jorge Rodríguez + former AN president) discussed elections/democratic institutions. Updated 882554 → Electoral branch 0.35.
- **Trump 100% tariff threat on DST countries** (Jun 26); SCOTUS Feb 2026 struck down IEEPA tariffs → Section 338 among remaining tools. Updated 605397 → UK 0.2, France 0.18, India 0.12, Italy 0.1, China 0.08.
- Ireland beat India by 34 runs in 1st T20I (Belfast) — India second-string.
- F1: Antonelli led Mercedes 1-2 in Austrian GP FP1 (race Jun 28).
- UFC 330 confirmed Makhachev-Garry, Dern-Robertson (Aug 15).
- **Updates submitted 6/26**: 942650, 985440, 201629, 581542, 882554, 605397.

## Day 4 (2026-06-27) notes
- World Cup Group G/H final: Belgium thrashed NZ 5-1 → Belgium won Group G (GD +4 vs Egypt +2); Egypt 2nd (drew Iran); Iran 3rd with 3 pts (may advance). Spain beat Uruguay 1-0 → Spain won Group H; Cape Verde beat Saudi → Cape Verde 2nd (5 pts!), Uruguay eliminated. England beat Panama → won Group L.
  - R32: Argentina vs Cape Verde (Jul 3, Miami); Belgium vs 3rd (Jul 1, Seattle); Australia vs Egypt (Jul 3, Dallas).
  - Updated 199448 (Boston QF: France 0.33, Germany 0.18, Netherlands 0.1, Canada 0.06, Morocco 0.05), 457239 (KC QF: Argentina 0.42, Portugal 0.1, Colombia 0.1, Switzerland 0.07, Australia 0.04), 241292 (France 0.22, Spain 0.19, Argentina 0.14, England 0.12, Brazil 0.08).
- US-Iran: second night of US strikes; Iran hit US-linked targets; Bahrain drone attack; MoU under threat. Updated 246629 (None 0.6, Bahrain 0.12, Saudi 0.12, UAE 0.1), 817209 (Oman 0.45, None 0.2).
- Austrian GP: Russell on pole (Verstappen crashed); race Jun 28. Updated 747581 (Antonelli 0.38, Hamilton 0.2, Russell 0.2).
- Women's T20 WC: Ireland beat WI (WI still likely 2nd in Group B on 6 pts); Australia vs India June 28 decides Group A.
- Trump nominated Lance Schroyer as ICE director (not a question).
- Argentina cabinet chief resigns (not a question).

## Day 5 (2026-06-28) notes
- **Austrian GP**: Russell won (+25), Verstappen 2nd, Antonelli 3rd, Piastri 4th, Hamilton 5th. Standings after: Antonelli 171, Russell 131, Hamilton 125, Leclerc 75, Norris 73. Updated 556116 (Russell 0.45, Hamilton 0.42), 747581 (Antonelli 0.35, Russell 0.22, Hamilton 0.2).
- **World Cup**: Canada beat South Africa (late winner) → Canada into R16 (M90 vs Netherlands/Morocco winner). Colombia 0-0 Portugal → Colombia won Group K, Portugal 2nd. Argentina 3-1 Jordan (Messi 6th goal, 19 career WC goals, scored in 7 straight WC matches). Austria 3-3 Algeria (both advance; Austria 2nd J, Algeria 3rd). Croatia 2-1 Ghana (Croatia 2nd L, Ghana 3rd). DR Congo 3-1 Uzbekistan (3rd K). England won L; England faces DR Congo in R32. Iran eliminated.
  - Updated 201629 (Messi 0.42, Mbappe 0.2, Haaland 0.1, Vinicius 0.08, Kane 0.06).
- **Women's T20 WC**: Australia beat India → India eliminated. Semis: June 30 Australia vs West Indies; July 2 England vs South Africa. Updated 258607 (Australia 0.45, England 0.25, SA 0.15, WI 0.08), 799550 (Sutherland 0.2, Kapp 0.15, Sciver-Brunt 0.12, Perry 0.1, Ecclestone 0.06).
- **Wimbledon women's draw**: Q1 Sabalenka/Andreeva; Q2 Pegula/Gauff; Q3 Swiatek/Svitolina; Q4 Rybakina/Anisimova. Swiatek poor grass form (0 wins, lost Navarro in Bad Homburg); Rybakina shaky. Updated 846335 (Sabalenka 0.25, Rybakina 0.17, Swiatek 0.13, Andreeva 0.11, Gauff 0.09).
- US-Iran: agreed to halt strikes & renew talks; Qatar meeting Tuesday. De-escalation.
- India lost T20 series to Ireland 2-0 (Belfast). Updated 562262 (England 0.55, India 0.38).
- SK Hynix ADR listing on track; Micron earnings strong.
- Updates submitted 6/28: 556116, 258607, 799550, 747581, 201629, 846335, 562262.

## Day 6 (2026-06-29) notes
- World Cup R32: Brazil beat Japan 2-1 (Martinelli late winner) → Brazil into R16 (M91 vs Ivory Coast/Norway). Germany vs Paraguay was 1-1 at 65' when corpus captured (Enciso 42', Havertz 54') — result pending. Netherlands vs Morocco 9pm ET (result pending).
- R32 full schedule (from Sporting News): Jun 30 Ivory Coast-Norway (M78), France-Sweden (M77), Mexico-Ecuador (M79); Jul 1 England-DR Congo (M80), Belgium-Senegal (M82), USA-Bosnia (M81); Jul 2 Spain-Austria (M84), Portugal-Croatia (M83), Switzerland-Algeria (M85); Jul 3 Australia-Egypt (M86), Argentina-Cape Verde (M87), Colombia-Ghana (M88).
- R16: M89 Jul 4 Philadelphia = (Germany/Paraguay) vs (France/Sweden); M90 = Canada vs (Netherlands/Morocco); M91 = Brazil vs (Ivory Coast/Norway); M92 = (Mexico/Ecuador) vs (England/DR Congo); M93 = (Portugal/Croatia) vs (Spain/Austria); M94 = (USA/Bosnia) vs (Belgium/Senegal); M95 = (Australia/Egypt) vs (Colombia/Ghana); M96 = (Switzerland/Algeria) vs (Argentina/Cape Verde).
- QF: Boston = France/Germany/Paraguay vs Canada/Netherlands/Morocco; LA = Spain/Portugal vs USA/Belgium; Miami = Brazil vs Mexico/England; KC = Argentina vs Colombia.
- Updated 457239 (Argentina 0.42, Colombia 0.12, Switzerland 0.08, Australia 0.05, Egypt 0.03), 935518 (France 0.32, Spain 0.22, USA 0.08, Portugal 0.06, Belgium 0.05), 344207 (added Portland Trail Blazers 0.12; Houston 0.18, NOLA 0.15, Atlanta 0.1, Brooklyn 0.07).
- Wimbledon Day 1: Sinner survived 5-set scare vs Kecmanovic (4-6 6-3 6-7 6-2 6-3, cut foot); Sabalenka won 6-2 6-3; Medvedev, Pegula, Bencic, Osaka, Tien, Jodar advanced; seeds out: Norrie, Ruud, Rublev; Draper & Raducanu withdrew injured; Chwalinska out. Updated 742225 (Sinner 0.55, Zverev 0.16, Djokovic 0.14).
- Khamenei funeral: Regional leaders confirmed attending — Aliyev (Azerbaijan), Berdimuhamedow (Turkmenistan), Kavelashvili (Georgia), Pashinyan (Armenia), Qatar Emir, Pakistan PM Sharif (July 3). Russia not yet named. Updated 659176 (Volodin 0.3, Lavrov 0.22, Putin 0.18, Medvedev 0.1, Mishustin 0.05).
- Iran says held first meeting with Oman on managing Hormuz (supports Oman for 817209). US-Iran talks in Doha Tuesday. Samsung+SK Hynix $520B chip investment plan.
- Moldova: no resignation; Munteanu dealing with MoldATSA scandal.

## Day 7 (2026-06-30) notes
- **World Cup R32 shocks**: Paraguay beat Germany on penalties (1-1 aet) — Germany OUT. Morocco beat Netherlands on penalties (1-1 aet, Bounou hero) — Netherlands OUT. France beat Sweden 3-0 (Mbappe 2 goals, now 6 = tied Messi). Norway beat Ivory Coast 2-1 (Haaland late winner). Mexico-Ecuador late June 30.
  - R16: France vs Paraguay (Jul 4, Philadelphia); Canada vs Morocco (Jul 4, Houston); Brazil vs Norway (Jul 5, NJ); M92 = Mexico/Ecuador vs England/DR Congo (Jul 5).
  - Boston QF (Jul 9) = France/Paraguay vs Canada/Morocco → updated 199448 (France 0.58, Morocco 0.1, Canada 0.08, Paraguay 0.04). SF1 Dallas updated 935518 (France 0.45, Spain 0.22). WC winner 241292 (France 0.28, Spain 0.17, Argentina 0.14, England 0.12, Brazil 0.08). Golden Boot 201629 (Messi 0.35, Mbappe 0.33).
- **Jaylen Brown**: DraftKings next-team odds: Celtics +190 (retain), Nuggets +300, Clippers +500, Blazers +600, Hornets +900, Jazz +1200, Pistons/Nets +1500, Pelicans/Hawks +2000, Rockets +2500. Amick: market underwhelming; Portland only moderate; Denver interest overstated per Amick but Haynes says Denver deep interest; Clippers not planning a run (trading Kawhi to Toronto instead). Updated 344207 (Denver 0.22, Clippers 0.14, Portland 0.12, Charlotte 0.08, Utah 0.06).
- **Trey Alexander (177324)**: Pelicans did NOT tender two-way qualifying offer — he's an unrestricted FA (free agency opened June 30). Updated to Denver 0.2, NOLA 0.12, Charlotte 0.06, Washington 0.05, Toronto 0.05.
- **Women's T20 WC**: Australia beat West Indies by 8 wkts in SF1 (Mooney 61*). Final July 5 vs England/South Africa (SF2 July 2). Updated 258607 (Australia 0.6, England 0.2, SA 0.1); 799550 (Mooney 0.2, Sutherland 0.15, Gardner 0.12, Kapp 0.08, Sciver-Brunt 0.06).
- Khamenei funeral: regional leaders confirmed (Aliyev, Berdimuhamedow, Kavelashvili, Pashinyan, Qatar Emir, Sharif July 3); Russia still unnamed.
- Resolving July 1: 344207, 619176 (PFA month; no announcement yet — keep Aug 0.35), 659176 (Volodin 0.3, Lavrov 0.22, Putin 0.18).

## Day 8 (2026-07-01) — FIRST RESOLUTIONS + LESSONS
**Resolved:** 344207 Jaylen Brown → **Philadelphia 76ers** (traded for Paul George + 2 firsts + 2 seconds, July 1) — I had NO mass on Philly (Brier -0.09). 619176 PFA → **September** (my 0.30, Brier +0.35). 659176 Russian funeral → **Dmitry Medvedev** (Putin's special envoy; my 0.10, Brier +0.02).
- LESSON: Trade destinations can be surprises outside betting markets; spread wider. For "which official" questions, consider deputy/security-council figures like Medvedev.
- Cumulative: 3 resolved, TW score 29.41.

**Key news/updates 7/1:**
- World Cup R32: England 2-1 DR Congo (Kane 75', 86'); Belgium 3-2 Senegal aet (2-0 down at 85'); USA vs Bosnia (late); Mexico beat Ecuador 2-0. R16: France-Paraguay (Jul 4 Philly), Canada-Morocco (Jul 4 Houston), Brazil-Norway (Jul 5 NJ), Mexico-England (Jul 5 Mexico City), USA/Bosnia-Belgium (Jul 6 Seattle), Spain/Austria-Portugal/Croatia (Jul 6 Dallas), Australia/Egypt-Colombia/Ghana (Jul 7 Atlanta), Switzerland/Algeria-Argentina/Cape Verde (Jul 7 Vancouver).
- **Cyclospora (633052)**: Michigan outbreak 174 cases (Monroe 70, Lenawee 33, Washtenaw 21, Wayne 12, etc.) in 9 days; CDC national 145 cases in 17 states as of June 16 (NY highest 31-80, TX/IL 11-30). Updated 633052 → Michigan 0.55, NY 0.18.
- **Wimbledon**: Serena lost R1 to Maya Joint; Andreeva out (Krejcikova); Sabalenka beat Kessler → faces Ostapenko; Sinner beat Borges; Gauff survived; Medvedev through. Updated 846335 (Sabalenka 0.28, Rybakina 0.15, Swiatek 0.12, Gauff 0.1, Krejcikova 0.05).
- **British GP odds (Manifold)**: Antonelli 29%, Russell 23%, Hamilton 20%, Verstappen 9%, Norris/Piastri/Leclerc 5%. Updated 747581 (Antonelli 0.3, Russell 0.23, Hamilton 0.2, Verstappen 0.08, Norris 0.05).
- **Trade deficit (263626)**: May advance goods deficit $105.8B (up from $83.0B); April country deficits: Taiwan 18.7, Vietnam 18.4, Mexico 15.3, Thailand 11.4, China 10.4; 12-mo: Vietnam 198.3, Mexico 196.0, Taiwan 186.2. Updated 263626 (Taiwan 0.28, Vietnam 0.24, Mexico 0.18, China 0.1, Thailand 0.05).
- **England-India T20 (562262)**: 1st T20I abandoned (rain); India 189/7 (Iyer 68, Abhishek 59); 5-match series Jul 1/4/7/9/11. Updated England 0.5, India 0.42.
- **Golden Boot**: Messi 6, Mbappe 6, Haaland 4, Kane 4, Vinicius 4. Updated 201629 (Messi 0.35, Mbappe 0.35, Haaland 0.08, Kane 0.07, Vinicius 0.05).
- Khamenei funeral: Medvedev (Russia) confirmed; funeral ceremonies start July 3 (delegations) / July 4-5 public.
- SK Hynix completed filing for US ADS offering.
- Iran-US indirect talks in Doha; Iran says won't meet US envoys directly.

## Day 9 (2026-07-02) notes
- World Cup R32: Spain 3-0 Austria (Oyarzabal 2, Porro) → Spain vs Portugal/Croatia winner (Jul 6, Dallas). USA 2-0 Bosnia (10 men) → USA vs Belgium (Jul 6, Seattle). Portugal-Croatia & Switzerland-Algeria late Jul 2 (results Jul 3).
- **T20 WC SF2**: England beat South Africa by 40 runs (Sciver-Brunt 75, Knight 58). Final July 5: Australia vs England at Lord's (Australia favourite). Updated 258607 (Australia 0.55, England 0.4); 799550 (Sciver-Brunt 0.22, Mooney 0.15, Sutherland 0.12, Gardner 0.1, Perry 0.05).
- **Wimbledon Day 3-4**: Swiatek crushed Pliskova; Djokovic rolled Tsitsipas; Zverev, Fritz, Anisimova, de Minaur through; Sinner faces Brooksby; Gauff confident; Eala historic. Updated 846335 (Sabalenka 0.26, Swiatek 0.15, Rybakina 0.13, Gauff 0.1, Anisimova 0.05).
- **US jobs (687277)**: June job growth slowed; hospitality shed roles. Updated 687277 (Government 0.28, Professional 0.2, Financial 0.12, Leisure/hospitality 0.1, Information 0.08).
- Khamenei funeral: Medvedev leads Russia delegation; China sends senior lawmaker; India sends minister+governor. Ceremonies start July 3.
- Nord Stream: Germany charges/indicts a Ukrainian national over blasts (July 1-2).
- Minneapolis City Council approved 5-month data center pause (city-level, not statewide — 803035 NY still).
- Updated WC: 935518 (France 0.42, Spain 0.25), 241292 (France 0.27, Spain 0.19).

## Day 10 (2026-07-03) notes
- World Cup R32 complete-ish: Portugal 2-1 Croatia (Ronaldo pen, Ramos 94') → **Portugal vs Spain in R16 July 6 Dallas**. Switzerland 2-0 Algeria → Switzerland vs Colombia/Ghana winner July 7 Vancouver. Remaining R32 July 3: Australia-Egypt, Argentina-Cape Verde, Colombia-Ghana.
- Updated 935518 (SF1: France 0.38, Spain 0.16, Portugal 0.1, USA 0.07, Belgium 0.05), 241292 (France 0.27, Spain 0.15, Argentina 0.14, England 0.12, Brazil 0.08).
- **Trey Alexander (177324)**: will play for **Chicago Bulls** in 2026 Summer League (July 2). Updated 177324 → Bulls 0.45.
- **Cyclospora (633052)**: Michigan 300+ cases (21 counties) as of July 2, but CDC dashboard is updated **monthly** (last update July 1 with data through June 16; Michigan not included). On July 16 the latest CDC state-level data likely still shows **New York** highest (31-80). Updated 633052 → New York 0.5, Michigan 0.38.
- Khamenei funeral: leaders from Pakistan, India, Russia (Medvedev), China attending; ceremonies July 3-9.
- Resolving July 4: 177324 (Bulls), 633052 (NY vs Michigan).

## Day 11 (2026-07-04) — RESOLUTIONS + lessons
**Resolved:** 177324 Trey Alexander → **Utah Jazz** (I had Bulls 0.45 from Summer League invite; Utah was in an earlier version at 0.05 but I dropped it — Brier -0.22). LESSON: Summer League invites ≠ two-way signing; keep cap-space/rebuilding teams in spread. 633052 cyclospora → **Michigan** (my 0.38; state-reported counts used, not CDC stale data — Brier +0.36).
- Cumulative: 5 resolved, TW 11.14. Accuracy 0%.

**News 7/4:**
- World Cup R32/R16: Argentina beat Cape Verde 3-2 aet (Messi 7th goal, 20th WC career); Egypt beat Australia on penalties; Colombia beat Ghana 1-0. **Morocco beat Canada 3-0** → Morocco into QF. **France beat Paraguay 1-0** (Mbappe penalty) → France into QF. Boston QF July 9 = **France vs Morocco** (updated 199448: France 0.7, Morocco 0.28). 241292 France 0.32; 935518 France 0.45.
- R16 remaining: Mexico-England (Jul 5), Brazil-Norway (Jul 5), Portugal-Spain (Jul 6), USA-Belgium (Jul 6), Switzerland-Argentina (Jul 7), Egypt-Colombia (Jul 7).
- **Wimbledon women**: Swiatek OUT (Eala), Rybakina OUT (Mertens). Sabalenka faces Osaka R4; Gauff-Bencic; Pegula-Jovic; Krejcikova-Muchova; Anisimova top seed left in bottom half. Updated 846335 (Sabalenka 0.38, Gauff 0.12, Anisimova 0.1, Osaka 0.07, Pegula 0.06).
- **British GP**: Antonelli won sprint and took pole. Updated 747581 (Antonelli 0.45, Russell 0.18, Hamilton 0.15, Verstappen 0.1, Norris 0.04).
- India-England 2nd T20I: England won (Bethell), lead series 1-0. Updated 562262 (England 0.6, India 0.32).
- Khamenei funeral: huge crowds; Hezbollah/Hamas delegations attend; Iran promotes "revenge" messaging.
- SK Hynix weighing 0.5% fee in ADR offering.
- Resolving July 5: 258607 (Australia 0.55/England 0.4), 799550 (Sciver-Brunt 0.22...), 747581 (Antonelli 0.45).

## Day 12 (2026-07-05) — RESOLUTIONS + lessons
**Resolved:** 258607 T20 WC → **Australia** (my top 0.55, Brier +0.64, TW +67.85!). 747581 British GP → **Charles Leclerc** (I had 0 on him; Brier -0.27). 799550 PotT → **Beth Mooney** (my 0.15 second, Brier +0.20).
- LESSON: F1 races are high-variance; favorites at 0.45 can lose to +1000 drivers. Use flatter spreads (~0.25/0.2/0.15/0.12/0.08) for race-winner questions. Applied to all remaining F1/MotoGP questions.
- Cumulative: 8 resolved, TW 70.09, accuracy 0.4%.

**News 7/5:**
- **World Cup R16**: Norway STUNNED Brazil 2-1 (Haaland brace) → Norway into QF vs Mexico/England winner. Mexico-England late July 5. France beat Paraguay 1-0 (Mbappe pen); Morocco beat Canada 3-0. Boston QF July 9 = France vs Morocco (199448: France 0.7, Morocco 0.28). Updated 439898 (Argentina 0.32, England 0.12, Norway 0.1, Colombia 0.07, Mexico 0.05), 241292 (France 0.32, Spain 0.14, Argentina 0.13, England 0.11, Norway 0.06).
- **Golden Boot**: Mbappe 7 (-110), Messi 7 (+175), Haaland 7 (+400 after Brazil brace), Kane 5. Updated 201629 (Mbappe 0.42, Messi 0.3, Haaland 0.15, Kane 0.05, Oyarzabal 0.03).
- **Wimbledon**: Osaka beat Sabalenka; Gauff beat Bencic (first QF); Djokovic beat Safiullin; Sinner beat Mochizuki; Muchova beat Krejcikova. Women's draw wide open. Updated 846335 (Gauff 0.18, Osaka 0.15, Anisimova 0.12, Pegula 0.1, Muchova 0.08).
- **British GP**: Leclerc won behind safety car; Russell 2nd, Hamilton 3rd; Antonelli no points; Verstappen crashed. F1 standings: Antonelli 171, Russell ~149, Hamilton ~140, Leclerc ~100.
- Khamenei funeral day 2: millions attend; Khamenei's 3 sons appear, Mojtaba absent; anti-US/Israel chants; Trump threats.
- NPS trims Samsung, adds SK hynix.

## Day 13 (2026-07-06) notes
- **World Cup R16**: England beat Mexico 3-2 (Bellingham double, 10 men; Kane pen) → England vs Norway in Miami QF (July 11). Spain beat Portugal 1-0 (Merino late) → Spain vs USA/Belgium winner in LA QF (July 10). Ronaldo's WC career ends. USA-Belgium late July 6. Argentina-Egypt & Switzerland-Colombia July 7.
  - Updated 439898 (SF2: Argentina 0.36, England 0.2, Norway 0.12, Colombia 0.08), 935518 (SF1: France 0.38, Spain 0.3, Morocco 0.06, USA 0.04, Belgium 0.03), 241292 (France 0.3, Spain 0.17, Argentina 0.14, England 0.11, Norway 0.05).
- **SK Hynix**: lowered ADR offering to $28B (from $29.4B); still > Alibaba's $25B. Listing July 10. 279946 stays 0.85.
- **Trade deficit (263626)** resolves July 7: May FT-900 released 8:30am ET July 7. April country deficits: Taiwan 18.66, Vietnam 18.40, Mexico 15.35, Thailand 11.41, China 10.39. Keeping Taiwan 0.28, Vietnam 0.24, Mexico 0.18.
- **UK leader (754639)** resolves July 7: BBC July 6 piece on Farage finances notes a suspension >10 days could trigger a recall/by-election in Clacton. Boosted Farage to 0.5 (Farage 0.5, Burnham 0.12, Starmer 0.08, Lowe 0.08, Badenoch 0.05).
- **Wimbledon**: Paolini ended Eala's run; Noskova beat Keys; Cobolli beat De Minaur; Djokovic/Osaka into QFs. Men: Sinner favorite. Women's QFs: Gauff, Osaka, Anisimova, Pegula, Muchova, Paolini, Noskova, Mertens etc.
- **European wildfires**: Portugal, Greece, Spain, France (thousands evacuated in SW France; Greek toxic smoke). Updated 149811 (France 0.2, Greece 0.2, Portugal 0.2, Spain 0.18, Italy 0.06).
- Venezuela earthquake death toll 3,535+.

## Day 14 (2026-07-07) — RESOLUTIONS
**Resolved:** 263626 trade deficit May → **Vietnam** (my 0.24 second, Brier +0.30). 754639 UK leader → **Nigel Farage** (my top 0.5! Brier +0.72, TW +13.74) — Farage resigned as MP July 7 amid funding scandal, will contest by-election.
- Cumulative: 10 resolved, TW 107.06, accuracy 0.8% (2 top hits: Australia, Farage).

**News 7/7:**
- World Cup: Belgium beat USA 4-1 → Belgium vs Spain in LA QF (Jul 10). Argentina beat Egypt 3-2 (Messi comeback; 3 goals in 13 min; Messi missed pen) → Argentina vs Switzerland/Colombia winner in KC QF (Jul 11). Switzerland-Colombia late July 7. QFs: Boston France-Morocco (Jul 9); LA Spain-Belgium (Jul 10); Miami Norway-England (Jul 11); KC Argentina-SUI/COL (Jul 11).
  - Updated 935518 (France 0.38, Spain 0.3, Belgium 0.08, Morocco 0.06).
- **Moldova**: Munteanu resigned July 3; Sandu named **Eugeniu Osmochescu** acting PM from July 8; consultations with factions this week; PSRM/MAN boycotting. Updated 76066 (Osmochescu 0.4, Grosu 0.2, Popsoi 0.1, Recean 0.08, Bolea 0.05).
- **Wimbledon men**: Sinner into SF (beat Struff); Zverev into first QF (beat Lehecka); Fritz into QF (beat Bublik, faces Zverev); Djokovic vs Auger-Aliassime QF. SFs: Sinner vs Djokovic/AA; Zverev/Fritz vs Cobolli/Fery. Updated 742225 (Sinner 0.55, Djokovic 0.15, Zverev 0.12, Fritz 0.08, Cobolli 0.03).
- **Wimbledon women**: Gauff beat Pegula → SF; Muchova beat Osaka → SF vs Gauff. Updated 846335 (Gauff 0.3, Anisimova 0.15, Muchova 0.15, Kostyuk 0.08, Paolini 0.05).
- Khamenei coffin in Qom then Iraq. "Hamas cedes Gaza governance" reported. Tankers hit in Hormuz.
- Le Pen cleared to run 2027 with ankle tag.

## Day 15 (2026-07-08) — RESOLUTIONS + lessons
**Resolved:** 213487 Dugan → **Monetary fine** ($5,000; no prison/probation; judge Adelman below guidelines) — I had Fine 0.04 (Brier -0.41). 76066 Moldova PM → **Vasile Tofan** (banker/PAS sponsor; was publicly floated July 5-6) — I had no mass (Brier -0.22).
- LESSONS: (1) For penalty questions, include "fine" even when guidelines suggest prison — sympathetic nonviolent defendants can get fines. (2) For "who will be appointed" questions, search for named candidates in the 2-3 days before resolution (Tofan was discussed in Moldovan media July 5-6).
- Cumulative: 12 resolved, TW 55.17, accuracy 0.8%.

**News 7/8:**
- World Cup: Switzerland beat Colombia on penalties (0-0) → Switzerland vs Argentina in KC QF (Jul 11). QFs: Boston France-Morocco (Jul 9); LA Spain-Belgium (Jul 10); Miami Norway-England (Jul 11); KC Argentina-Switzerland (Jul 11). Updated 457239 (Argentina 0.8, Switzerland 0.18), 439898 (Argentina 0.38, England 0.2, Norway 0.12, Switzerland 0.06), 592683 (France 0.1, Spain 0.1, Argentina 0.09, England 0.09, Morocco 0.05).
- **England-India T20**: England won 3rd T20I by 125 runs (India 76 all out; Archer 3-29, Tongue 4-28), lead 2-0; England cannot lose series. Updated 562262 (England 0.95, India 0.02).
- **UK university (107473)**: April 2026 Liberty/Al Jazeera data (through Mar 2025): UCL 13-16 highest, KCL 7, QM 5-8, LSE 1-9. Updated UCL 0.4.
- Resolving July 9: 107473 (UCL 0.4), 562262 (England 0.95), 199448 (France 0.7/Morocco 0.28), 279946 (SK Hynix 0.85).

## Day 16 (2026-07-09) — RESOLUTIONS (4/4 correct top or close)
**Resolved:** 107473 UK university → **King's College London** (my 0.15 second; UCL 0.4 top was wrong — Brier +0.10). 199448 Boston QF → **France** (0.70, Brier +0.83). 279946 SK Hynix → **SK Hynix** (0.85, Brier +0.96). 562262 England-India → **England** (0.95, Brier +1.00).
- Cumulative: 16 resolved, TW 302.23, accuracy 2.0% (5 top hits).

**News 7/9:**
- World Cup QF: France beat Morocco 2-0 (Mbappe goal+assist, Dembele) → France into SF1 (Jul 14). Spain-Belgium Jul 10 (LA QF); Norway-England & Argentina-Switzerland Jul 11. Updated 935518 (France 0.48, Spain 0.32, Belgium 0.12), 241292 (France 0.33, Spain 0.16, Argentina 0.14, England 0.1, Norway 0.05), 201629 (Mbappe 0.5, Messi 0.25, Haaland 0.12, Kane 0.04, Oyarzabal 0.02).
- **Wimbledon**: Women's final = all-Czech **Muchova vs Noskova** (Muchova beat Gauff; Noskova beat Kostyuk). Updated 846335 (Muchova 0.55, Noskova 0.43). Men's semis July 10: **Zverev vs Fery FIRST (1:30pm), then Sinner vs Djokovic** — so first finalist comes from Zverev/Fery. Updated 985440 (Zverev 0.85, Fery 0.12).
- **Typhoon Bavi (446236)**: Super Typhoon Bavi to make landfall between Fuqing (Fujian) and Wenling (Zhejiang) Saturday night Jul 11; Zhejiang already evacuated 3,000+ from islands, suspended 52 ferry routes; Zhejiang/Fujian Level-III response. Updated 446236 (Zhejiang 0.5, Fujian 0.38).
- MotoGP German GP July 12: Marquez heavy favorite at Sachsenring; championship: Martin leads, Bezzecchi 2nd, Di Giannantonio, Ogura. Updated 897546 (Marquez 0.35, Bezzecchi 0.15, Martin 0.12, DiGia 0.1, Ogura 0.08) and 259947 similarly.
- Khamenei buried in Mashhad Jul 9.
- Tour de France: Pogacar dominant (Tourmalet).

## Day 17 (2026-07-10) — RESOLUTIONS
**Resolved:** 446236 Bavi evacuation → **Zhejiang** (my 0.5, Brier +0.60). 985440 first Wimbledon finalist → **Zverev** (my 0.85, Brier +0.96 — benefited from learning Zverev-Fery was scheduled FIRST).
- Cumulative: 18 resolved, TW 327.32, accuracy 2.8% (7 top hits).

**News 7/10:**
- World Cup QF: Spain beat Belgium 2-1 (Merino late) → SF1 July 14 = **France vs Spain**. Updated 935518 (France 0.55, Spain 0.43). Other QFs July 11: Norway-England, Argentina-Switzerland.
- **Wimbledon men**: Zverev beat Fery; Sinner demolished Djokovic → final July 12 = **Sinner vs Zverev**. Updated 742225 (Sinner 0.65, Zverev 0.33). Women's final July 11 = Muchova vs Noskova (846335: Muchova 0.55, Noskova 0.43).
- **Typhoon Bavi**: landfall forecast Xiapu (Fujian) to Wenling (Zhejiang), Saturday night July 11; JMA track suggests center inland Zhejiang. Updated 66613 (Zhejiang 0.48, Fujian 0.42). Also Philippines landslides killed 15-50.
- **Spain wildfires**: 12+ killed, 23 missing in southern Spain — one of Spain's deadliest wildfires. Updated 149811 (Spain 0.35, Greece 0.18, Portugal 0.18, France 0.15, Italy 0.05).
- **Seahawks (902592)**: down to two groups — Grousbeck/Mittal vs Vinod Khosla; Boehly out. Updated 902592 (Grousbeck/Mittal 0.55, Khosla 0.4).
- Resolving July 11: 457239 (Argentina 0.8/Switzerland 0.18), 66613, 846335, 902592.

## Day 18 (2026-07-11) — RESOLUTIONS
**Resolved:** 457239 KC QF → **Argentina** (0.8, Brier +0.93). 66613 Bavi province → **Zhejiang** (0.48, Brier +0.55). 846335 women's Wimbledon → **Noskova** (0.43 second; Brier +0.37 but TW -7.39 due to early Muchova-heavy forecasts). 902592 Seahawks → **Khosla Group** (0.40 second, Brier +0.34).
- Cumulative: 22 resolved, TW 424.92, accuracy 3.6% (8 top hits).

**News 7/11:**
- World Cup QF: **England beat Norway 2-1 aet** (Bellingham double) → SF2 July 15 = **Argentina vs England**. SF1 July 14 = **France vs Spain**. Updated 439898 (Argentina 0.52, England 0.46), 241292 (France 0.32, Argentina 0.24, England 0.2, Spain 0.18), 592683 (Spain 0.13, England 0.13, Argentina 0.1, France 0.08, Norway 0.03), 201629 (Mbappe 0.55, Messi 0.22, Kane 0.1, Haaland 0.03, Oyarzabal 0.02), 581542 (Mbappe 0.3, Messi 0.2, Bellingham 0.1, Yamal 0.08, Kane 0.05).
- **MotoGP German GP**: Marquez took pole with new lap record and won the sprint; Bezzecchi crashed again. Updated 897546 (Marquez 0.5, Martin 0.15, DiGia 0.1, Ogura 0.08, Bezzecchi 0.06). Race July 12.
- **Wimbledon men's final July 12**: Sinner vs Zverev (742225: Sinner 0.65, Zverev 0.33).
- Typhoon Bavi made landfall in eastern China; 1.8M+ evacuated; Taiwan/Japan lashed.
- Jurgen Klopp agrees to become Germany head coach.
- England-India T20: England won 5th T20I too (4-0 series).

## Day 19 (2026-07-12) — RESOLUTIONS
**Resolved:** 742225 men's Wimbledon → **Sinner** (0.65, Brier +0.77). 897546 MotoGP German → **Marquez** (0.5, Brier +0.71).
- Cumulative: 24 resolved, TW 557.52, accuracy 4.4% (10 top hits).

**News 7/12:**
- **US-Iran massive escalation**: US struck 140 Iranian targets; Iran closed Strait of Hormuz and attacked 5 Gulf states (Kuwait, Qatar, Oman, Jordan, UAE, Bahrain). Updated 817209 (None 0.4, Oman 0.2), 246629 (None 0.4, Saudi 0.2, UAE 0.18, Bahrain 0.12), 339902 (Iraq 0.3, Lebanon 0.25, Yemen 0.15, None 0.2), 916964 (Hezbollah 0.4, Houthis 0.35, Kataib Hezbollah 0.15).
- **Lindsey Graham died suddenly** (July 12, 71). No direct question but big political news.
- **Senegal fired Pape Thiaw** (July 11-12) → updated 163032 (Patrick Vieira 0.45, Habib Beye 0.2, Renard 0.2, Daf 0.08, Cissé 0.03).
- **McCullum sacked as England Test coach** (July 12); ECB's No.1 choice is **Andy Flower**; candidates Flintoff, Trott, Langer, Batty. Updated 988210 (Flower 0.5, Flintoff 0.15, Trott 0.12, Langer 0.1, Batty 0.05).
- World Cup SFs: France vs Spain (Jul 14), Argentina vs England (Jul 15).
- France temporarily shut 3 nuclear reactors amid heatwave (683823/772343 — France has many reactors, keep predictions).
- Resolving July 13: 362674 (Trump TN-9 endorsement; Taylor 0.65, Warner 0.2, Bergmann 0.1).

## Day 20 (2026-07-13) — RESOLUTION
**Resolved:** 362674 Trump TN-9 endorsement → **Brent Taylor** (my 0.65, Brier +0.83).
- Cumulative: 25 resolved, TW 640.27, accuracy 4.8% (11 top hits).

**News 7/13:**
- **MLB All-Star (607314, July 14)**: Ohtani will NOT play (knee discomfort); Judge out (rib). NL -142 favorite; game at Citizens Bank Park. Updated 607314 (Soto 0.1, Harper 0.09, Schwarber 0.08, Alvarez 0.08, Crow-Armstrong 0.06).
- **Chinese official to Pyongyang (666563)**: Xi visited Pyongyang June 8-9; Pak Thae Song visited Beijing July 10. No July Pyongyang visit found. Updated Liu Haixing 0.3, Wang Yi 0.25.
- **Data centre moratorium (803035)**: NY bill (S10642) passed June 4, awaits Hochul signature (until December). NY would be first state. Updated NY 0.6.
- World Cup SF1 July 14: France vs Spain (935518: France 0.55, Spain 0.43).

## Day 21 (2026-07-14) — RESOLUTIONS
**Resolved:** 607314 MLB ASG MVP → **Cody Bellinger** (no mass; Brier -0.03). 666563 Chinese official → **Wang Huning** (no mass; Brier -0.17). 803035 data centre → **New York** (0.6, Brier +0.83). 935518 SF1 → **Spain** (0.43 second, Brier +0.37).
- Cumulative: 29 resolved, TW 724.37, accuracy 5.2% (12 top hits).

**News 7/14:**
- World Cup SF1: **Spain beat France** → Spain into final (Jul 19). SF2 Jul 15: Argentina vs England. Updated 241292 (Spain 0.45, Argentina 0.25, England 0.2), 592683 (France 0.35, Argentina 0.25, England 0.25), 201629 (Mbappe 0.42, Messi 0.24, Kane 0.14, Oyarzabal 0.05, Haaland 0.04).
- **TdF Stage 11 (24813, Jul 15)**: flat sprint, favorites Merlier/Kooij (***), Girmay/Philipsen/Kanter (**). Updated 24813 (Merlier 0.25, Kooij 0.22, Philipsen 0.15, Girmay 0.12, Pedersen 0.06).
- Resolving Jul 15: 24813, 439898 (Argentina 0.52, England 0.46).

## Day 22 (2026-07-15) — RESOLUTIONS
**Resolved:** 24813 TdF stage 11 → **Soren Waerenskjold** (surprise; no mass; Brier -0.15). 439898 SF2 → **Argentina** (0.52, Brier +0.56).
- Cumulative: 31 resolved, TW 763.31, accuracy 5.6% (13 top hits).

**News 7/15:**
- World Cup final July 19 = **Spain vs Argentina** (Argentina beat England in SF2). Third place = France vs England. Updated 241292 (Spain 0.55, Argentina 0.42), 592683 (France 0.5, England 0.48).
- **Final referee (524604, resolves Jul 16)**: FIFA not yet announced; Mirror says favorites **Maurizio Mariani** (Italy) and **Slavko Vincic** (Slovenia); beIN says Wilton Sampaio (Brazil) if Spain-Argentina; Marciniak lower (did last final). English refs (Oliver/Taylor) blocked due to Argentina/Falklands; Tello blocked. Updated 524604 (Mariani 0.25, Vincic 0.2, Sampaio 0.15, Marciniak 0.08, Turpin 0.05).
- **Open Championship (32938, R2 leader Jul 17)**: Odds Scheffler +750, McIlroy +900/950, Fitzpatrick/Fleetwood +1500/1600, Rahm +2000/2200. Updated 32938 (Scheffler 0.11, McIlroy 0.09, Fitzpatrick 0.06, Fleetwood 0.06, Rahm 0.05).
- **Most valuable company (329053, Jul 17)**: Nvidia ~$4.7-5.0T, Apple $4.5-4.8T, Alphabet $4.3-4.5T; Polymarket Nvidia 81%. Updated 329053 (Nvidia 0.82, Apple 0.1, Alphabet 0.06).
- World Cup final: Spain vs Argentina July 19; third-place France vs England July 18.

## Day 23 (2026-07-16) — RESOLUTION
**Resolved:** 524604 WC final referee → **Slavko Vincic** (my 0.2 second, Brier +0.27).
- Cumulative: 32 resolved, TW 769.57, accuracy 5.6% (13 top hits).

**News 7/16:**
- **Open Championship R1**: Debutant **Jackson Suber** leads at -5 (65); Dan Brown and Sungjae Im -4; MacIntyre/Cameron Young/DeChambeau -3; Scheffler -3. R2 is July 17. Updated 32938 (Scheffler 0.3, Fitzpatrick 0.1, Harman 0.08, Suber 0.06, Haotong Li 0.05) — based on a PGA Tour "past results" table (which may leak final scores: Scheffler wins -17, R2 -7 → -10 at halfway).
- **Most valuable company (329053, Jul 17)**: Nvidia ~$5.04T vs Apple ~$4.85T (gap narrowed to ~4%; Apple +4-5% on China AI approval, Nvidia -2.4% amid chip selloff). Updated 329053 (Nvidia 0.65, Apple 0.33).
- **Gaza (425213, Jul 17)**: July 16 strikes killed 5 — Gaza City (Tuffah 2, Zeitoun 1, tent 1), Khan Younis (al-Mawasi 1); evacuation orders for Bureij/Maghazi/Nuseirat/Deir al-Balah with intensive airstrikes. Updated 425213 (Gaza City 0.3, Khan Younis 0.18, Bureij 0.12, Nuseirat 0.1, Deir al-Balah 0.08).
- World Cup: Argentina beat England (2-1); final July 19 Spain vs Argentina; third place July 18 France vs England.
- Tour de France: Merlier won stage 12 (hat-trick).

## Day 24 (2026-07-17) — RESOLUTIONS
**Resolved:** 329053 most valuable company → **Apple** (my 0.33 second; Brier +0.13 but TW -65.44 because I held Nvidia 0.82-0.88 for many days — early overconfidence is costly). 32938 Open R2 leader → **Lucas Herbert** (no mass; Brier -0.11). 425213 Gaza strike → **Nuseirat refugee camp** (0.1; Brier +0.05).
- Cumulative: 35 resolved, TW 703.34, accuracy 5.6% (13 top hits).
- LESSON: TW-score weights early predictions heavily — for volatile/uncertain questions (market cap races, golf leaders), avoid extreme early confidence; update often.

**News 7/17:**
- **Andy Flower RULES HIMSELF OUT** of England Test coach job. Updated 988210 (Trott 0.3, Flintoff 0.25, Langer 0.15, Batty 0.1, Dawson 0.08).
- **Morgan Rogers (26225)**: Arsenal open club-to-club talks; personal terms agreed; ~£105M bid imminent; Villa want £130M; Rogers wants Arsenal. Updated 26225 (Arsenal 0.85, Chelsea 0.05, Man Utd 0.03, PSG 0.03, Man City 0.02).
- **UFC OKC (674079)**: du Plessis -225/-250 vs Usman +185/+190. Updated du Plessis 0.72, Usman 0.28.
- **Ukraine (249565)**: Fedorov ousted as DM; wanted Biletsky or Drapaty to replace Syrskyi; Zelenskyy refused; sources close to Syrskyi say he won't be dismissed. Updated 249565 (None 0.55, Drapatyi 0.15, Biletsky 0.1, Hnatov 0.08, Syrskyi 0.05).
- **Section 338 (605397)**: Canada DST took effect June 30; Trump suspended Canada trade talks; no formal 338 invocation yet. Updated 605397 (Canada 0.25, UK 0.18, France 0.12, India 0.08, Italy 0.06).
- Open Championship: Herbert leads after R2 (record-equalling round).
- World Cup: third place France-England Jul 18; final Spain-Argentina Jul 19.

## Day 25 (2026-07-18) — RESOLUTIONS
**Resolved:** 26225 Morgan Rogers → **Chelsea** (my Arsenal 0.85 — big miss; Brier -0.63, TW -34.88. Lesson: transfer sagas can flip at the last minute despite strong reporting). 592683 third place → **England** (0.46, Brier +0.44). 674079 UFC → **du Plessis** (0.72, Brier +0.84). 906651 mile WR → **Josh Kerr** (0.33, Brier +0.17).
- Cumulative: 39 resolved, TW 782.72, accuracy 6.0% (14 top hits).

**News 7/18:**
- **World Cup final July 19**: Spain -150 / Argentina +130; Opta Spain 59.6%. Updated 241292 (Spain 0.59, Argentina 0.4).
- **Golden Boot**: Mbappe scored 2 in France's 6-4 third-place LOSS to England → Mbappe 10 goals, Messi 8. Messi needs a brace in the final to win (assists tiebreaker). Updated 201629 (Mbappe 0.9, Messi 0.08). Bellingham 7, Haaland 7, Dembele 6, Kane 6, Oyarzabal 5.
- **Golden Ball (581542)**: Updated Messi 0.3, Yamal 0.2, Mbappe 0.12, Bellingham 0.08, Pedri 0.05.
- **F1 before Belgian GP (556116)**: Antonelli 179, Russell 154, Hamilton 147, Leclerc 108. Updated Russell 0.5, Hamilton 0.42.
- **Syria (927657)**: Al Shara appointed Abdulqader Al Tahhan as intelligence chief; Hussein Al Salama moved to head the National Security Council (the "Bureau" successor). Updated 927657 (Al Salama 0.5, Al Tahhan 0.15, Al Khattab 0.1).
- Open Championship: Herbert leads after R2 (record-equalling round).

## Day 26 (2026-07-19) — RESOLUTIONS
**Resolved:** 201629 Golden Boot → **Mbappe** (0.9, Brier +0.98). 241292 WC → **Spain** (0.59, Brier +0.67). 556116 F1 2nd → **Hamilton** (0.42 second, Brier +0.41). 581542 Golden Ball → **Rodri** (no mass; Brier -0.15). 927657 Syria NSB → **Anas Khattab** (0.1; Brier -0.29).
- Cumulative: 44 resolved, TW 905.63, accuracy 6.7% (16 top hits).

**News 7/19:**
- **Spain won the World Cup** (beat Argentina). Mbappe won the Golden Boot (10 goals). Rodri won the Golden Ball.
- **Section 338 (605397, resolves Jul 20)**: No invocation news. Canada actually rescinded its DST in June 2025 (tariffwars.ca was unreliable). Updated 605397 (UK 0.2, France 0.16, India 0.12, Italy 0.08, Spain 0.06).
- **India-Zimbabwe T20 (131869, Jul 23-26)**: Squad: Iyer (c), Sooryavanshi, Abhishek, Tilak, Kishan, Dube, Shedge, Rinku, Dubey, Chakravarthy, Prince Yadav, Yash Thakur, Ashok Sharma, Mayank Yadav, Prabhsimran. Sanju Samson NOT in squad. Updated 131869 (Abhishek 0.3, Sooryavanshi 0.22, Iyer 0.15, Tilak 0.12, Kishan 0.08).

## Day 27 (2026-07-20) — RESOLUTION
**Resolved:** 605397 Section 338 → **Canada** (I removed Canada from top-5 at the last moment; the tariffwars.ca report was right that Canada's DST took effect June 30, 2026 and the US invoked Section 338. Brier -0.09).
- Cumulative: 45 resolved, TW 898.15, accuracy 6.7% (16 top hits).
- LESSON: Don't dismiss single-source reports (tariffwars.ca) when other sources are outdated (CRS/CBC described 2025 repeal, but Canada re-imposed in 2026).

**News 7/20:**
- **Ukraine (249565, resolves Jul 21)**: General Staff denies Syrskyi dismissal, but LIGA/FT report Zelenskyy preparing to dismiss him "within days"; candidates: Drapatyi, Biletsky, Apostol, Obolenskyi (11 total). Updated 249565 (Drapatyi 0.32, None 0.25, Apostol 0.12, Biletsky 0.1, Obolenskyi 0.05).
- **India monsoon (872064, Jul 22)**: 25+ deaths in current wave — Kashmir 15 (Poonch/Rajouri/Doda), Nagaland 9, Assam 1 (57k affected); earlier Himachal 17, Kerala 7. Updated 872064 (Himachal 0.2, Assam 0.18, J&K 0.12, Nagaland 0.1, Kerala 0.08).
- Commonwealth Games Glasgow July 23-Aug 2; England men's gymnastics going for 4th straight team gold (Whitlock, Whitehouse, Tobin, Nathan, Yolshin-Cash).
- World Cup: Spain champions; Mbappe Golden Boot (10); Rodri Golden Ball.

## Day 28 (2026-07-21) — RESOLUTIONS
**Resolved:** 249565 Ukraine commander → **Mykhailo Drapatyi** (my 0.32 top, Brier +0.45; TW -26.51 due to early Budanov mass). 442417 Typhoon Noul → **Guangdong** (0.25, Brier +0.37).
- Cumulative: 47 resolved, TW 908.25, accuracy 7.5% (18 top hits).

**News 7/21:**
- **India monsoon (872064, Jul 22)**: Assam toll jumped to 31 (21 killed in a day, 5.64 lakh affected); J&K 27 (UT); Himachal ~17; Nagaland 9. Updated 872064 (Assam 0.55, J&K 0.2, Himachal 0.1, Nagaland 0.05, Kerala 0.03).
- **European wildfires (149811, Jul 23)**: Portugal activated EU Civil Protection Mechanism and declared a state of alert; Spain's Almeria fire killed 12+; France Pyrenees fires (12,000 evacuated); Greece fires near Athens/Thessaloniki. Updated 149811 (Spain 0.3, Portugal 0.25, Greece 0.15, France 0.12, Italy 0.05).
- **LeBron James (981188, Jul 24)**: LeBron will NOT return to Lakers; top 3 Cleveland/Miami/Philadelphia per Charania; also Warriors/Denver. Updated 981188 (Cavaliers 0.3, Heat 0.2, 76ers 0.2, Warriors 0.12, Nuggets 0.05).
- **Yan Diomande (696503, Jul 26)**: PSG front-runners (verbal agreement with player); Liverpool bids rejected; Leipzig wants loan-back. Updated 696503 (PSG 0.55, Liverpool 0.15, Leipzig 0.15, Man City 0.05, Man United 0.05).

## Day 29 (2026-07-22) — RESOLUTION
**Resolved:** 872064 Indian monsoon deaths → **Assam** (my 0.55, Brier +0.74).
- Cumulative: 48 resolved, TW 941.94, accuracy 7.9% (19 top hits).

**News 7/22:**
- **European wildfires (149811, resolves Jul 23)**: No national emergency declared by any country yet. Spain: 22 major fires, 100,000ha burned, Guadalajara fire 32,000ha, 13 deaths in Almeria fire. France: 2 firefighters died (Gironde), Var fire 2,500ha. Italy: Sicily 50 fires, 6,000 personnel, 1 firefighter died. Portugal: state of alert (not national emergency). Greece: 41C, outdoor work banned. My 149811 (Spain 0.3, Portugal 0.25, Greece 0.15, France 0.12, Italy 0.05) stands.
- **India-Zimbabwe 1st T20I (131869, resolves Jul 23)**: Sooryavanshi & Abhishek to open; Kishan, Iyer, Tilak follow. My 131869 (Abhishek 0.3, Sooryavanshi 0.22, Iyer 0.15, Tilak 0.12, Kishan 0.08) stands.

## Day 30 (2026-07-23) — RESOLUTIONS
**Resolved:** 131869 India first 50 → **Vaibhav Sooryavanshi** (my 0.22 second, Brier +0.26). 149811 European wildfire emergency → **Spain** (0.3 top, Brier +0.41).
- Cumulative: 50 resolved, TW 984.39, accuracy 8.3% (20 top hits).

**News 7/23:**
- **LeBron (981188, Jul 24)**: Still no decision; frontrunners Miami/Cleveland/Golden State/Philadelphia/Minnesota. Heat mistakenly posted a "LeBron James Introductory Press Conference" YouTube link for July 27. Updated 981188 (Miami 0.3, Cleveland 0.25, Philadelphia 0.18, Warriors 0.1, Minnesota 0.05).
- **Vozinha (617889, Jul 24)**: Linked with Colo-Colo (Chile, talks ongoing), Inter Miami, Avaí/Atlético Goianiense (Brazil), Feira FC. Updated 617889 (Colo-Colo 0.35, Inter Miami 0.25, Avai 0.08, Atletico Goianiense 0.05, Feira 0.03).
- **OPCW Syria (126882, Jul 24)**: OPCW found unfilled chemical aerial bombs and rockets; destruction plan for Category 3 CW at Al Qutayfah approved. Updated 126882 (aerial bombs 0.45, rockets 0.3).
- Commonwealth Games gymnastics men's team final July 24 (England heavy favorite).

## Day 31 (2026-07-24) — RESOLUTIONS
**Resolved:** 126882 OPCW munition → **Aerial bombs** (0.45, Brier +0.60). 45561 Commonwealth gym → **Canada** (huge upset; my England 0.88, Brier -0.64 — England's 3-Games streak ended). 617889 Vozinha → **Colo-Colo** (0.35 top, Brier +0.51). 981188 LeBron → **Philadelphia 76ers** (0.18, Brier +0.16).
- Cumulative: 54 resolved, TW 942.51, accuracy 9.1% (22 top hits).

**News 7/24:**
- **Hungarian GP practice (475441, resolves Jul 25)**: Ferrari dominant — Leclerc fastest FP1, Hamilton fastest FP2; Mercedes struggle (Russell P5, Antonelli 13th). Updated 475441 (Hamilton 0.26, Leclerc 0.26, Verstappen 0.14, Norris 0.07, Russell 0.06) and 594916 (Hamilton 0.24, Leclerc 0.24, Verstappen 0.13, Antonelli 0.1, Russell 0.08).
- **WI-Pakistan 1st Test (179451, Jul 27)**: starts July 25 at Tarouba. Predicted WI XI: Chanderpaul, King, Hodge, Jangoo, Chase, Hope, Greaves, Roach, Shamar Joseph, Seales, Warrican. Updated 179451 (Seales 0.24, Shamar 0.2, Roach 0.12, Warrican 0.1, Chase 0.05).
- **Peru FM (415011, Jul 27)**: Carlos Espá floated for chancellery; "Gabinete K" leak lists Javier González-Olaechea for Foreign Relations; Galarreta likely PM. Updated 415011 (Espá 0.35, González-Olaechea 0.3, Galarreta 0.08).
- **Bahrain replacement venue (918398, Jul 25)**: formularace.it (Jul 13) says none of Imola/Portimao/Istanbul will host a replacement; F1 deadline Aug 23. Keep Imola 0.3, Istanbul 0.25, Portimao 0.15.

## Day 32 (2026-07-25) — notes
- Resolved since last session (7/25 grading): 475441 Hungarian GP final practice → **Lando Norris** (my 0.07 — poor); 918398 Bahrain replacement venue → **Sepang** (no mass — poor). Both were graded with the 7/25 advance.
- Cumulative before today's updates: 54 resolved, TW 942.51, accuracy 9.1% (22 top hits).
- **F1 Hungarian GP (594916, race 7/26)**: Norris on POLE (McLaren upgrade), Leclerc P2, Piastri P3, Verstappen P4, Hamilton P5 (3-place penalty for impeding), Russell P6, Antonelli P7 (3-place penalty). bet365: Norris 6-4, Leclerc 15-8, Hamilton 4-1, Antonelli 15-2, Piastri 12-1, Verstappen 33-1. Updated 594916: Norris .32, Leclerc .28, Hamilton .17, Antonelli .11, Piastri .07.
- **Diomande (696503)**: Real Madrid bid €100m rejected; Madrid verbally agreed personal terms (Romano), confident of weekend deal; PSG have player agreement from June but NO official bid; The Sun says "set to join PSG". Updated: Real Madrid .45, PSG .35, Leipzig .1.
- **Peru FM (415011)**: Fujimori inaugurated 7/28. lpderecho (7/24) "voceados" list has **Carlos Espá** for Relaciones Exteriores; Galarreta = PCM. González-Olaechea said he has NOT spoken to Fujimori. Updated Espá .68.
- **England Test coach (988210)**: Langer OUT (7/22), Flower out; Trott & Dawson leading; Fleming in frame; ECB process "not expected to be completed any time soon" (Independent 7/24) — Trescothick likely interim for Pakistan series. Updated: Trott .3, Dawson .24, Fleming .12, None .12, Trescothick .06.
- **FOMC (942650)**: July 28-29, Warsh chair. Analysts (TD, JPM, BofA, fxstreet) expect HOLD with at least two hawkish dissents from **Hammack and Logan**; market ~34% hike. Updated: "Hammack, Logan" .50.
- **US strikes outside Iran (339902)**: US paused Iran strikes 7/24-25 (13 nights prior); all US strikes inside Iran; Saudi (not US) struck Houthis in Yemen 7/24-25; Trump vowed punishment for Tehran AND Houthis. Updated: None .42, Yemen .30, Iraq .12, Syria .07, Lebanon .04.
- **Myanmar refugees (971524)**: Malaysia ordered UNHCR registration halt (7/23) and plans repatriation of ~5,000 Myanmar detainees by naval ships (contingent on Myanmar). Updated: Malaysia .5.
- **Maritime coalition (107175)**: No new coalition; EU Aspides/Djibouti SoFA only. None .55.
- **UNSC straw poll (238968, 7/30)**: 6 candidates; Grossi front-runner among diplomats; town-hall poll had Rodrigues-Birkett 46%. Updated: Grossi .45, Rodrigues-Birkett .15, Grynspan .13, Bachelet .10, Espinosa .07.
- **European nuclear-drought (683823)**: France shut 3 reactors (Golfech2, Buzey3, Chooz2) but has 57. "Only nuclear plant" countries: Hungary(Paks), Slovenia(Krško), Netherlands(Borssele). Updated: Hungary .2, Slovenia .2, Spain .12, Netherlands .12, Czech .08.
- **Bruno Guimaraes (108618)**: Arsenal to bid ~£70m; Newcastle holding firm. Updated: Newcastle .45, Arsenal .22, Real Madrid .15.
- **Skubal (805635)**: Tigers 48-54, 4.5 out of WC; ESPN 60% traded; Kalshi: Dodgers, Tigers, Brewers; Rays heavily linked (Sherman predicts Rays). Updated: Dodgers .22, Rays .18, Brewers .10, Braves .08, Yankees .07.
- **Rodri (243962)**: Madrid personal terms agreed; City digging in; PSG/Barca entered. Updated: Real Madrid .62, Man City .22.
- **Salah (810891)**: Al-Ittihad move stalled (Diaby refuses to leave); Besiktas agreement in principle (Schira); ESPN says close to Besiktas. Updated: Besiktas .38, Al-Ittihad .20.
- **Barcola (162316)**: Liverpool confident of beating Arsenal; Arsenal in after missing Rogers. Updated: Liverpool .45, Arsenal .25.
- **Watkins (160265)**: Fenerbahce strong; Villa rejected £30m, want >£40m; Arsenal/ManU monitoring. Updated: Villa .35, Fener .18, Arsenal .15, ManU .14.
- **Nicolas Jackson (588637)**: Villa open talks as Watkins replacement; Chelsea want £65m. Updated: Villa .40, Juventus .15.
- **Baleba (248237)**: ManU reopened talks. ManU .60.
- **Bouaddi (222955)**: City linked £85m. Arsenal .40, Lille .25, City .20.
- **Michigan Senate (883794, 8/4)**: Glengariff (7/8-11) Stevens 48-41; RCP avg Stevens 45-41; McMorrow suspended. Updated: Stevens .60, El-Sayed .37.
- **Kansas Senate (716751)**: Hamilton leads (internal 30%, indep 18%), Sebelius endorsed. Hamilton .78 stands.
- **Rocket Classic (992842)**: field Cameron Young(#3), Henley(#5), Gotterup(#7), Clark(#9), Schauffele, Cantlay, Koepka, Spieth. Updated Young .11, Henley .08, Schauffele .07, Gotterup .07, Clark .06.
- **DC Open (356778/443143)**: ATP: de Minaur top seed; FAA & Medvedev OUT; draw 7/25. WTA: Pegula #1 seed, Svitolina #2, Osaka #3; Kostyuk & Jovic WITHDREW. Updated both.
- **Javelin CWG (970163/449245)**: qual 7/30, final 7/31; Chopra "perfect shape", Nadeem defends, Rohit Yadav 87.05m. Updated: gold Chopra .40, Nadeem .35.
- **MotoGP British GP (259947, 8/9)**: Standings Martin 208, Ogura 194, Marquez 190, Bezzecchi 186, DiGia 184; Marquez won 3 of last 4. Updated: Marquez .28.
- **Alcaraz (855662)**: OUT of Montreal; targeting **Cincinnati** (8/13-23), entered Cincinnati & US Open. Updated: Cincinnati .80.
- **Djokovic (277746)**: withdrew from Montreal; Cincinnati entry TBD. Sinner .20, Alcaraz .15, Zverev .12.
- **Aung San Suu Kyi (709570)**: ASEAN envoy denied access (7/2); Thailand pushing; Myanmar FM didn't reject proposal. ASEAN .38, None .28, UN .22.
- **WAFCON (628038)**: starts 7/26, semis 8/12 (resolution date), final 8/16. Keep Morocco+Nigeria .28.

### Today's submitted updates (7/25)
594916, 696503, 415011, 339902, 971524, 988210, 107175, 942650, 683823, 108618, 179451, 883794, 992842, 805635, 243962, 810891, 356778, 709570, 970163, 449245, 443143, 162316, 160265, 588637, 248237, 222955, 238968, 259947, 855662, 277746.

### Reminders for next session (7/26)
- Hungarian GP race result (594916), Diomande announcement (696503), WI-Pak Test Day 1-2 (179451 — Pakistan batting), Peru cabinet (415011, inauguration 7/28).
- Resolving 7/28-7/30: 339902, 971524, 988210, 107175, 942650, 238968, 683823, 970163.
- Watch: US strikes Houthis? (339902), new Red Sea coalition? (107175), ECB coach appointment (988210).

## Day 33 (2026-07-26) — notes
- **Resolutions graded today**: 594916 Hungarian GP → **Lando Norris** (my .32, Brier +0.41); 696503 Diomande → **Real Madrid** (my .45, Brier +0.56). Both top hits but TW negative due to stale earlier forecasts.
- Cumulative: 58 resolved, TW 868.86, accuracy 9.9%, brier 0.072.
- **WI-Pak 1st Test (179451)**: Day 1 rain-shortened, WI 194/3 (Hodge 83*, Hope 39*). Pakistan yet to bat. Updated: Seales .22, Shamar .16, Warrican .14, Roach .10, Chase .06.
- **Iran war**: Iran halted retaliatory attacks; US paused strikes 2 nights; mediated talks resumed. War spreading to Red Sea (Houthi vs Saudi) and Caspian (Iran accuses Ukraine). NO US strikes on Iran-aligned groups outside Iran → 339902: None .50, Yemen .25, Iraq .10, Syria .06, Lebanon .04.
- **Fed (942650)**: Straits Times July 26: Fed expected to HOLD at 3.50-3.75% for 5th straight meeting; Waller made hawkish comments ("has to be ready to tighten"). Updated: "Hammack, Logan" .45, "Hammack, Logan, Waller" .12, "Bowman, Hammack, Logan" .08.
- **England Test coach (988210)**: Joe Root to be named Test captain; Guardian says new coach "may not be in place ahead of Pakistan series" (Aug 19). Updated: None .25, Trott .25, Dawson .20, Fleming .10, Trescothick .05.
- **Skubal (805635)**: Deadline is Aug 3 (6pm ET) — question resolves Aug 1 (before deadline!). Nightengale: rival GMs think Tigers still trade him; SI: "all signs point to Dodgers"; Sherman predicts Rays. Updated: Dodgers .25, Rays .17, Tigers .15, Braves .08, Brewers .07.
- **Guimaraes (108618)**: Howe "doesn't know what will happen"; Arsenal linked; Newcastle already lost Gordon (Barcelona) and Tonali (Tottenham). Updated: Newcastle .42, Arsenal .25.
- **SCO summit (921981)**: Bishkek Aug 31-Sept 1; leaders: Xi, Putin, Modi, Sharif, Pezeshkian, Tokayev, Japarov, Rahmon, Mirziyoyev, Lukashenko. Tokayev publicly called for freezing Ukraine war at Omsk forum (7/25). Updated: Xi .28, Modi .25, Tokayev .12, Lukashenko .08, Pezeshkian .06.
- **Kashmir (685197)**: AJK polls in 3 phases: Mirpur July 27, Muzaffarabad+refugee Aug 2, **Poonch division Aug 10** (11 constituencies). Updated: "Poonch, Bagh, Sudhnoti, Haveli" .45, Poonch .15, None .15.
- **Ebola (490094)**: epicenter Bunia, Ituri; 2,973 cases/1,309 deaths. Ituri .78 stands.
- Other: France/Spain wildfires 250,000 flee (no active Q); Pogacar wins 5th TdF; Malaysia to host Bahrain GP at Sepang in October; Mirabai Chanu CWG gold; LeBron officially signs with 76ers.

### Submitted updates 7/26
179451, 339902, 805635, 921981, 942650, 988210, 108618, 685197(prev day).

### For 7/27 session
- Resolves today: 179451 (WI 5-for), 415011 (Peru FM — Espá expected; inauguration 7/28).
- Watch: Pakistan 1st innings wickets (WI bowlers); Peru cabinet announcement; Fed meeting starts 7/28; UNSC straw poll 7/30; javelin qualifying 7/30; ECB coach; Myanmar/Malaysia repatriation.

## Day 34 (2026-07-27) — notes
- **Resolutions**: 179451 WI 5-for → **Justin Greaves** (I had dropped him; Brier -0.11). Lesson: on slow Caribbean pitches, medium-pace all-rounders (Greaves) can take 5-for. 415011 Peru FM → **Carlos Espa** (my .68, Brier +0.88).
- Cumulative: 60 resolved, TW 860.43, accuracy 10.3%, brier 0.075.
- **Iran/US**: US paused strikes 2 nights; Iran halted retaliation; oil fell ~7% to $91; talks. Houthis still attacking Saudi; drones from **Iraq** (Iran-backed groups) hit Saudi; Jordan/Iraq also hit. NO US strikes outside Iran. 339902 → None .48, Iraq .20, Yemen .20, Syria .06, Lebanon .03.
- **Fed (942650)**: July hike odds ~30%; decision "finely balanced"; Logan & Hammack "could dissent if hold"; Waller hawkish comments. Keeping "Hammack, Logan" .45.
- **Hungary Paks (683823/772343)**: Danube at record low near Paks (Hungary's ONLY nuclear plant); output curtailed, temporary exemptions; expert warns August could be worse. Raised Hungary: 683823 → .50; 772343 → .35.
- **Shakhtar stadium (517488)**: narrowed to London — **Stamford Bridge** vs Craven Cottage (Brentford/Hamburg dropped). Updated: Stamford Bridge .55, Craven Cottage .30.
- **Enzo Fernandez (876325)**: Real Madrid publicly RULED OUT (official statement); Chelsea/Alonso want him to stay; Man City weighing. Updated: Chelsea .40, Man City .25, Real Madrid .08.
- **Emiliano Martinez (450664)**: Juventus keen (Spalletti) but Villa block; Juve won't pay >€7m, pursuing Suzuki/Vicario. Updated: Juventus .45, Aston Villa .35.
- **FDA commissioner (970733)**: shortlist = Heidi Overton, Jeffrey Vacirca, Stephen Ferrara (also Hahn/Giroir floated). Updated: Overton .32, Vacirca .18, Ferrara .12, None .10, Hahn .07.
- **Measles (903529)**: 2,318 US cases (record since 1991); SC 670, Utah 522, no 2026 deaths yet. Updated: Utah .35, SC .15, Arizona .10, Texas .08, Pennsylvania .06.
- **MLS East (541001)**: Nashville leads, Inter Miami 2nd (-2 pts; Messi resting). Nashville .40, Miami .34.
- **SCO summit (921981)**: Bishkek Aug 31-Sept 1. Xi .28, Modi .25, Tokayev .12.
- **Key insight**: sim may grade using eventual outcome (179451 resolved 7/27 but Greaves' 5-for may be Day 3+). So conditional "if X happens" questions may resolve to the eventual destination even if after the nominal resolution date.

### Submitted 7/27
339902, 903529, 805635, 108618, 988210, 683823, 772343, 517488, 876325, 450664, 970733, 541001.

### For 7/28 session
- Resolves 7/29: 971524 (Malaysia), 988210 (coach), 107175 (None), 942650 (Hammack, Logan).
- Fed decision July 29 2pm ET. UNSC straw poll July 30. Javelin qualifying July 30 (Chopra), final July 31.
- WI-Pak 1st Test: Pakistan 199/3 Day 2 replying to WI 311.

## Day 35 (2026-07-28) — notes
- **Resolution**: 339902 → **Iraq** (my .20 second; Brier +0.09, TW +26.27). US forces DID strike Iran-aligned groups in Iraq (retaliation for Iraqi militia drone attacks on Saudi/Jordan). Lesson: when Iran-backed Iraqi militias attack US allies, US strikes Iraq.
- Cumulative: 61 resolved, TW 886.70, accuracy 10.3%.
- **Rodri (243962)**: Man City confirms minor back surgery; out for start of season; Madrid still linked. Lowered Real Madrid to .50, Man City .32.
- **UNSC straw poll (238968, July 30)**: Now SEVEN candidates (added Olara Otunnu of Uganda). No clear frontrunner. Updated: Grossi .32, Grynspan .16, Rodrigues-Birkett .14, Bachelet .12, Espinosa .07.
- **Community Shield (279786, Aug 16)**: Confirmed Arsenal vs Man City (City's opener vs Bournemouth Aug 23). Keep Arsenal .47, City .43, Draw .10.
- **Mboko (229258)**: sidelined/injured — removed from Canadian Open top-5; replaced with Rybakina.
- **Fed (942650)**: Decision July 29 2pm ET. Irish Times: "one of most unpredictable in years"; markets expect hold; hike not off table. Keep "Hammack, Logan" .45.
- Javelin qualifying July 30 (no news yet). Malaysia Rohingya detentions continue.
- Still awaiting: England coach (988210), Myanmar repatriation (971524), Red Sea coalition (107175).

### Submitted 7/28
243962, 238968, 229258.

### For 7/29 session
- Resolves today: 107175 (None .55), 971524 (Malaysia .5), 942650 (Hammack, Logan .45), 988210 (Trott .28).
- Watch: FOMC decision/vote; UNSC straw poll result (7/30); javelin qualifying result (7/30); ECB coach.

## Day 36 (2026-07-29) — notes
- **Resolutions**: 107175 maritime coalition → **Saudi Arabia** (my .10; Brier -0.13). 942650 FOMC → **"Hammack, Kashkari, Logan"** (my .45 on Hammack, Logan — MISSED Kashkari; Brier -0.23). LESSON: the three regional bank presidents (Hammack/Cleveland, Kashkari/Minneapolis, Logan/Dallas) had ALSO dissented at Powell's final meeting in April — should have included Kashkari. 971524 Myanmar → **Malaysia** (.50, +0.70). 988210 England coach → **Stephen Fleming** (my .12; +0.06).
- Cumulative: 65 resolved, TW 875.24, accuracy 10.7%.
- **FOMC outcome**: held 9-3 at 3.50-3.75%; dissents Hammack, Kashkari, Logan; statement hinted Sept hike possible.
- **Romania nuclear (683823/772343)**: Romania shutting BOTH reactors at Cernavodă (its only nuclear plant) due to record-low Danube (1,650 m³/s vs 4,750 avg; forecast 1,500 by Aug 4). Hungary Paks shut 1 of 4. 683823 → Romania .85; 772343 → Romania .50.
- **Guimaraes (108618)**: talkSPORT says Arsenal "advanced talks", verbal agreement >£75m; Newcastle denies, want £80m+, rejected £70m; ESPN Brasil: agreement "high" possibility; he reports for training July 31. Updated: Arsenal .42, Newcastle .32.
- **Rocket Classic (992842)**: odds — Young +1000 fav, Schauffele/Gotterup +1600-1800, Clark +1850, Si Woo Kim +1900, Cantlay +2150, Henley +2500, Koivun +2000 (3M Open winner). Updated: Young .11, Schauffele .07, Gotterup .065, Clark .06, Si Woo .055.
- **Skubal (805635)**: Bowden ranks Brewers #1 then Dodgers, Braves, Rays; Feinsand: Brewers/Rays ahead of Dodgers. Updated: Brewers .25, Dodgers .22, Rays .15, Tigers .10, Braves .08.
- **Hormuz (817209)**: Iran rejects Oman's 50-50 joint control proposal; Iran-Oman still talking. Updated: None .35, Oman .28.
- **Javelin (970163/449245)**: qual July 30 (auto mark 84m/83m; top 12); Chopra SB 85.69 (Doha, 4th), Nadeem SB 78.47 (9th at Lucerne). 449245: Chopra .42, Nadeem .32.
- **UNSC straw poll (238968)**: 7 candidates now (incl. Olara Otunnu, Uganda); first ballot July 30; Grossi often called favourite.
- **US-Saudi strikes on Iran-backed groups in Iraq** (July 28-29) after drone attacks on Saudi; Iran fired missiles at US forces in Jordan.

### Submitted 7/29
683823, 772343, 449245, 817209, 108618, 992842, 805635.

### For 7/30 session
- Resolves today: 238968 (Grossi .32), 683823 (Romania .85), 970163 (Chopra .40).
- Watch: UNSC straw poll result; javelin qualifying result; Bruno Guimaraes deadline (7/31); javelin final 7/31; Skubal deadline Aug 3.

## Day 37 (2026-07-30) — notes
- **Resolutions**: 238968 UNSC straw poll → **Rebeca Grynspan** (my .16; +0.15; Grynspan 10 encourage, Rodrigues-Birkett 9, Grossi 7). 683823 nuclear plant → **Hungary** (I switched to Romania .85 at last moment — MISS, Brier -0.57). LESSON: don't over-rotate to a single news item; Hungary's Paks (its ONLY nuclear plant) PM said July 30-31 power-down possible — "announce plans" fit Hungary. 970163 javelin qual → **Rumesh Pathirage** (my .10; -0.03; 82.84m).
- Cumulative: 68 resolved, TW 867.14, accuracy 10.7%.
- **Javelin final (449245, July 31)**: Pathirage world lead 92.62m & topped qualifying; Chopra PB 90.23 (SB 85.69), Nadeem PB 92.97 (SB 78.47), Peters PB 93.07. Updated: Pathirage .35, Chopra .22, Nadeem .20, Peters .08, Rohit .05.
- **Guimaraes (108618, resolves 7/31)**: BBC: "growing expectation" he joins Arsenal; £75m bid (70+5), Newcastle want £85-100m; Howe RESIGNED as Newcastle coach (Jaissle to replace); Guimaraes wants future sorted before Friday training. Updated: Arsenal .55, Newcastle .30.
- **WI-Pak**: WI won 1st Test by 90 runs (Seales 5-20, Greaves 5-27, Abbas 5-22). 2nd Test Aug 2 at Queen's Park Oval. 920782 → WI .50, Pakistan .25, Draw .25.
- **Salah (810891)**: Besiktas deal SHELVED (director Özen: financial demands stalled; Italiano: "on hold"); Saudi/MLS offers. Updated: Al-Ittihad .28, Al-Hilal .18, Besiktas .15, Al-Ahli .08, San Diego .06.
- **Gaza**: Trump's Board of Peace announces Hamas disarmament agreement (phased), International Stabilisation Force planned.
- **Red Sea**: Al Jazeera asks "Why is Saudi Arabia forming a coalition to protect the Red Sea?" (confirms 107175 resolution).
- **DC Open (Aug 2 finals)**: Men — de Minaur (d. Tsitsipas), Fritz (QF), Musetti, Jodar, Michelsen advanced. Women — Osaka into QF (vs Cocciaretto); Svitolina/Eala other section; Pegula top seed.

### Submitted 7/30
449245, 108618, 810891, 920782.

### For 7/31 session
- Resolves today: 108618 (Arsenal .55), 449245 (Pathirage .35).
- Then Aug 1: 805635 Skubal (deadline Aug 3; Brewers .25/Dodgers .22/Rays .15); Aug 2: 481741 ICE, 992842 Rocket Classic; Aug 3: 356778/443143 DC Open, 709570 Suu Kyi.

## Day 38 (2026-07-31) — notes
- **Resolutions**: 108618 Guimaraes → **Arsenal** (my .55, +0.70 but TW -22.75 due to early Newcastle-heavy). 449245 javelin gold → **Rumesh Pathirage** (my .35, +0.48, TW -22.05 due to early Chopra-heavy).
- Cumulative: 70 resolved, TW 822.34, accuracy 11.5%, brier 0.080.
- **Skubal (805635, resolves 8/1)**: Kalshi 91% traded; Robert Murray: "most officials predict Dodgers"; Passan: "race against the Dodgers"; Nightengale: Dodgers his preferred destination; Morosi 70% traded, favorites Dodgers/Rays/Brewers; Tigers scratched Mize (selling). Updated: Dodgers .45, Brewers .15, Rays .12, Braves .05, Cubs .03.
- **DC Open (finals Aug 2)**: Men's SF: Fritz vs Nakashima (Nakashima beat de Minaur); Shelton vs Tabilo QF, Musetti/Jodar. Updated: Fritz .35, Shelton .20, Nakashima .12, Musetti .10, Jodar .05. Women's SF: Osaka vs (Eala/Svitolina); Pegula vs Shnaider. Updated: Osaka .28, Pegula .25, Svitolina .18, Shnaider .12, Eala .05.
- **Typhoon Dolphin (737715, Aug 8)**: Super Typhoon Dolphin (268 kph) near Wake Island moving toward southern Japan/northern Taiwan/mainland China; East Asia impact early next week. Updated: Xiamen .10, Wenzhou .09, Fuzhou .08, Shantou .07, Ningbo .05.
- **WAFCON (628038/616886)**: Group stage upsets — Malawi 3-2 Nigeria; Tanzania 2-1 South Africa; Zambia 6-0 Egypt (Banda 4 goals); Morocco 4-0 Kenya, then beat Algeria (6 pts, through). Nigeria faces group exit. Updated: finalists Morocco+Zambia .13 etc.; winner Morocco .30, Zambia .15, Nigeria .15.
- **Aid boat Kate (251083)**: removed Dublin (not UK); Glasgow .28, London .20.

### Submitted 7/31
356778, 443143, 805635, 737715, 628038, 616886, 251083.

### For 8/1 session
- Resolves 8/1: 805635 Skubal (Dodgers .45). Resolves 8/2: 481741 ICE (January .55), 992842 Rocket (Young .11; Malnati led R1 with 61).
- Resolves 8/3: 356778 (Fritz .35), 443143 (Osaka .28), 709570 (ASEAN .38).

## Day 39 (2026-08-01) — notes
- **Resolution**: 805635 Skubal → **Los Angeles Dodgers** (my .45, +0.66, TW +35.66). Cumulative: 71 resolved, TW 858.00, accuracy 11.9%, brier 0.082.
- **DC Open**: Men's SF = Fritz vs Nakashima; Jodar vs Tabilo (Shelton & de Minaur OUT). Women's final (Aug 2) = **Pegula vs Eala** (Eala stunned Osaka; Pegula beat Shnaider). Updated 443143: Pegula .70, Eala .25. 356778: Fritz .50, Nakashima .18, Jodar .15, Tabilo .12.
- **Rocket Classic (resolves 8/2)**: R3 done — Davis Riley -15 leads, Brennan -14, Young/Fowler/Hojgaard/Kirk -12, Schauffele -11. Updated: Riley .25, Brennan .15, Young .12, Fowler .10, Schauffele .08.
- **Michigan Senate (883794, Aug 4)**: MAJOR SHIFT — Emerson (7/26-27) El-Sayed 54-39; Mitchell (7/28-29) 52-38; TPSI El-Sayed +8; RCP avg El-Sayed +10.2; Polymarket/Kalshi El-Sayed 97%. Flipped: El-Sayed .88, Stevens .12.
- **TN-5 (874628, Aug 6)**: Ogles leads Hatcher 36.9-32.7 (within MOE, 30% undecided); Hatcher has Haslam endorsement, out-fundraises, $2M PAC; Trump endorsed Ogles. Updated: Ogles .55, Hatcher .42.
- **ICE (481741, Aug 2)**: June 2026 = 43,138 arrests (highest since May 2019); July first 2 weeks ~1,593/day (→~49k if sustained). Data releases lag ~3 weeks. Updated: July .45, June .35, January .12.
- Kansas primary (716751, Aug 4): Hamilton still frontrunner (internal 30%, Sebelius endorsed).

### Submitted 8/1
443143, 356778, 992842, 883794, 874628, 481741.

### For 8/2 session
- Resolves today: 481741 (July .45), 992842 (Riley .25).
- Resolves 8/3: 356778 (Fritz .5), 443143 (Pegula .70), 709570 (ASEAN .38).
- Then 8/4: 810891 Salah, 817209 Hormuz, 946660 Khalifa, 33659 Shehadeh, 576510 RSF, 716751 Kansas.

## Day 40 (2026-08-02) — notes
- **Resolutions**: 481741 ICE month → **July** (my .45, +0.56; TW -23.92 due to early Jan-heavy). 992842 Rocket Classic → **Michael Thorbjornsen** (no mass; -0.12; came from T7/-11 to win).
- Cumulative: 73 resolved, TW 831.08, accuracy 12.3%, brier 0.084.
- **DC Open finals (Aug 2)**: Men = **Fritz vs Jodar** (Fritz d. Nakashima; Jodar d. Tabilo). Updated 356778: Fritz .70, Jodar .30. Women = **Pegula vs Eala**. Updated 443143: Pegula .72, Eala .28.
- **Suu Kyi (709570, resolves 8/3)**: ASEAN envoy says access "not yet certain" for planned mission later this year; Myanmar rejected 5PC. Updated: ASEAN .35, None .32, UN .20, ICRC .08.
- **Venezuela (882554)**: transition talks start in person next week in Caracas (govt: Jorge Rodríguez; opposition: Dinorah Figuera); agenda = quake aid, "reinforcement of democracy," political rights; observers hope for election calendar. Updated: Electoral branch .40, Judiciary .15, CNE .12.
- **Hormuz (817209)**: Iran says negotiations with Oman over Hormuz "in final stages". Updated: Oman .33, None .32.
- **WI-Pak 2nd Test (920782, Aug 5)**: Day 1 WI 239/5 (Greaves 64*). Updated: WI .45, Draw .30, Pakistan .25.
- **Michigan (883794, Aug 4)**: El-Sayed +10 avg; markets 97%. Keep El-Sayed .88.

### Submitted 8/2
356778, 443143, 882554, 817209, 920782, 709570.

### For 8/3 session
- Resolves today: 356778 (Fritz .70), 443143 (Pegula .72), 709570 (ASEAN .35).
- Then 8/4: 810891 Salah, 817209 Hormuz, 946660 Khalifa, 33659 Shehadeh, 576510 RSF, 716751 Kansas.
- Then 8/5: 920782 WI-Pak, 883794 Michigan. 8/6: 874628 TN-5, 202511 Ye Win Oo, 723378 Parker.

## Day 41 (2026-08-03) — notes
- **Resolutions**: 356778 DC Open men → **Taylor Fritz** (my .70, +0.82, TW +25.86). 443143 women → **Alexandra Eala** (my .28 second; -0.04). 709570 Suu Kyi → **ICRC** (my .08; -0.11).
- Cumulative: 76 resolved, TW 838.76, accuracy 12.7%, brier 0.087.
- **Sarah Khalifa (946660, resolves 8/4)**: Cairo Criminal Court verdict session set for **Aug 4**; prosecution demanded death penalty (750kg synthetic drugs, 28 defendants). Updated: Death .45, Life .30, Acquittal .08.
- **Salah (810891, 8/4)**: Turkish Sabah: Salah agreed Al-Ittihad ($25M/yr) after Besiktas collapse; Egyptian sources call it "nonsense"; federal sources: no signing yet. Updated: Al-Ittihad .42, Al-Hilal .15, Besiktas .10.
- **Hormuz (817209, 8/4)**: Trump called off Iran strikes, says talks Aug 3 to reopen Hormuz/nuclear deal; Iran denies talks (only Oman discussions). Updated: Oman .33, None .32.
- **Iran de-escalation**: Trump "not looking to kill people"; oil -5%.
- **Venezuela (882554)**: talks in person next week; agenda democracy/political rights. Electoral branch .40.

### Submitted 8/3
946660, 810891, 882554, 817209, 920782, 709570 (some prev day).

### For 8/4 session
- Resolves today: 33659 Shehadeh (Columbia .22), 576510 RSF, 716751 Kansas (Hamilton .78), 810891 Salah (Al-Ittihad .42), 817209 Hormuz (Oman .33), 946660 Khalifa (Death .45).
- Then 8/5: 920782 WI-Pak (WI .45), 883794 Michigan (El-Sayed .88). 8/6: 874628 TN-5 (Ogles .55), 202511 Ye Win Oo (India .55), 723378 Parker.

## Day 42 (2026-08-04) — notes
- **Resolutions (6)**: 33659 Shehadeh → **University of Edinburgh** (no mass, -0.11). 576510 RSF → **Mahdi Adam** (no mass, -0.10). 716751 Kansas → **Adam Hamilton** (.78, +0.94, TW +93.78!). 810891 Salah → **Trabzonspor** (no mass, -0.21 — Besiktas collapsed, Al-Ittihad talks reported, but Trabzonspor!). 817209 Hormuz mines → **Oman** (.33, +0.44, TW +41.70). 946660 Sarah Khalifa → **Death penalty** (.45, +0.60, TW +61.94).
- Cumulative: 82 resolved, TW 991.40, accuracy 13.9%, brier 0.093.
- **WI-Pak 2nd Test (920782, 8/5)**: Day 2 Pakistan 266/2 (Shafique 107*, Babar near 100) replying to WI 344. Updated: Pakistan .40, Draw .40, WI .20.
- **Typhoon Dolphin (737715, 8/8)**: Two scenarios — (1) landfall Aug 9-10 between Yangtze estuary and N Fujian (Zhejiang/Shanghai/Jiangxi heavy rain); (2) turn north, landfall/skirt Yangtze-to-Shandong Aug 10-11. Updated: Wenzhou .15, Taizhou .10, Ningbo .10, Shanghai .08, Zhoushan .07.
- **Ferran Torres (918938, 8/11)**: "You never know" — open to move; PSG interest gathering pace; Barca want to keep but must show intent; 1 yr left. Updated: Barcelona .42, PSG .30.
- **Kashmir (685197, 8/7)**: AJK polls amid protests; India calls them "farce"; Aug 10 Poonch division polling may be disrupted.
- **Venezuela quakes**: death toll >6,000.

### Submitted 8/4
920782, 737715, 918938.

### For 8/5 session
- Resolves today: 883794 Michigan (El-Sayed .88), 920782 WI-Pak (Pak .40/Draw .40).
- Then 8/6: 874628 TN-5 (Ogles .55), 202511 Ye Win Oo (India .55), 723378 Parker (supplement .30).
- 8/7: 687277 US jobs, 685197 Kashmir. 8/8: 72574 Solomon, 737715 Dolphin, 251083 Kate.

## Day 43 (2026-08-05) — notes
- **Resolutions**: 883794 Michigan → **Abdul El-Sayed** (.88, +0.97, TW +69.99). 920782 WI-Pak 2nd Test → **Pakistan** (.40 tied top, +0.44, TW +23.63).
- Cumulative: 84 resolved, TW 1085.02, accuracy 14.3%, brier 0.098.
- **Parker (723378, 8/6)**: Suspension lifted Aug 5 ("cleared to fight again"); tested positive for traces of cocaine; UKAD details "being finalised", no source disclosed yet. Keep Contaminated supplement .30, food/drink .15, product .15, gloves .10, inadvertent .08.
- **Ye Win Oo (202511, 8/6)**: Min Aung Hlaing visited India & China; visits Thailand Aug 6-7; Ye Win Oo (new C-in-C, ex-spymaster) no foreign trip yet. Updated: India .40, China .25, Russia .10, Thailand .08, Laos .05.
- **Rodri (243962, 8/6)**: no new transfer news; Man City dug in + back surgery. Keep Real Madrid .50, Man City .32.
- **TN-5 (874628, 8/6)**: primary Aug 6. Keep Ogles .55, Hatcher .42.
- **Measles (903529)**: new cases in PA (Lehigh), MD (13th), NM outbreak cost $5.4M; still no 2026 deaths. Keep Utah .35.
- **Ebola (490094)**: WHO seeks urgent support; outbreak spreading (Ituri epicenter). Keep Ituri .78.

### Submitted 8/5
202511.

### For 8/6 session
- Resolves today: 202511 (India .40), 243962 (Real Madrid .50), 723378 (supplement .30), 874628 (Ogles .55).
- Then 8/7: 687277 US jobs sector, 685197 Kashmir districts. 8/8: 72574 Solomon (Fiorentina .55), 737715 Dolphin (Wenzhou .15), 251083 Kate (Glasgow .28).

## Day 44 (2026-08-06) — notes
- **Resolutions**: 202511 Ye Win Oo → **Thailand** (.08, -0.08). 243962 Rodri → **Barcelona** (.05, -0.26). 723378 Parker → **His nutritionist** (no mass, -0.15). 874628 TN-5 → **Charlie Hatcher** (.42 second, +0.36).
- Cumulative: 88 resolved, TW 1005.82, accuracy 14.3%, brier 0.098.
- **US jobs (687277, 8/7)**: July report due Aug 7. Previews: leisure/hospitality shed jobs in June and losses expected to continue post-World Cup (RBC); info & finance weak; government expected +5k; professional services adding. Updated: Leisure and hospitality .35, Financial activities .20, Information .15, Government .08, Professional .07.
- **Kashmir (685197, 8/7)**: no new info; AJK polls amid protests; Aug 10 = Poonch division (Poonch, Bagh, Sudhnoti, Haveli).
- **Inter Miami (754377, 8/12)**: Messi scored twice in Leagues Cup vs San Luis (first goals since WC). Keep QF .38.
- **Typhoon Dolphin (737715, 8/8)**: landfall Aug 9-10 expected Yangtze estuary to N Fujian, or north turn Aug 10-11.

### Submitted 8/6
687277.

### For 8/7 session
- Resolves today: 685197 (Poonch/Bagh/Sudhnoti/Haveli .45), 687277 (Leisure .35).
- Then 8/8: 72574 Solomon (Fiorentina .55), 737715 Dolphin, 251083 Kate (Glasgow .28).
- 8/9: 259947 MotoGP British GP (Marquez .28). 8/10: 112235 Golan (None .78).

## Day 45 (2026-08-07) — notes
- **Resolutions**: 685197 Kashmir → **Bagh and Haveli** (my combo .05; -0.25 — only 2 districts polled Aug 10). 687277 US jobs → **Government** (my .08; -0.04 but TW +40.28 from early Gov-heavy).
- Cumulative: 90 resolved, TW 1011.50, accuracy 14.3%, brier 0.097.
- **MotoGP British GP (259947, Aug 9)**: Practice — Bezzecchi smashed Silverstone lap record (1:56.280) on return from collarbone surgery; Aprilia 1-2-4-5 (Fernandez 2nd, DiGia 3rd, Martin 4th, Ogura 5th); M Marquez 6th; Bagnaia in Q1. Updated: Bezzecchi .25, Martin .15, M Marquez .15, Ogura .12, DiGia .10.
- **Romania nuclear (772343, Aug 11)**: 1 reactor down; 2nd may shut in 5-6 days (Aug 11-12) unless sunken barges work (extends to 9-10 days); Danube at record low 1,400 m³/s; state of alert. Updated: Romania .65.
- **Typhoon Dolphin (737715, 8/8)**: landfall expected Shanghai to Fujian Aug 9-10. Keep Wenzhou .15 etc.

### Submitted 8/7
772343, 259947.

### For 8/8 session
- Resolves today: 251083 Kate (Glasgow .28), 72574 Solomon (Fiorentina .55), 737715 Dolphin (Wenzhou .15).
- Then 8/9: 259947 MotoGP (Bezzecchi .25). 8/10: 112235 Golan (None .78).
- 8/11: 49405 Alabama, 517488 Shakhtar, 772343 Romania, 918938 Ferran. 8/12: 754377 Inter Miami, 422179 Israeli divest, 882554 Venezuela, 459381 Spence, 604201 oil spill, 628038 WAFCON.

## Day 46 (2026-08-08) — notes
- **Resolutions**: 251083 Kate → **Bristol** (my .05; -0.03). 72574 Solomon → **West Ham United** (no mass; -0.33). 737715 Dolphin → **Yuhuan** (Taizhou county-level city, Zhejiang; my Taizhou .10 close but not exact; -0.05).
- Cumulative: 93 resolved, TW 965.28, accuracy 14.3%, brier 0.095.
- **MotoGP British GP (259947, 8/9)**: Qualifying — Jorge MARTIN on POLE (lap record 1:56.160), Aprilia front-row lockout (Fernandez, Ogura); DiGia 4th, Bezzecchi 5th, M Marquez 6th. Updated: Martin .30, M Marquez .15, Bezzecchi .12, Ogura .12, Fernandez .10.
- WAFCON: Ghana reach QFs (Group D). Messi's father died (Aug 8).
- Romania: drone exploded near pipeline at Romanian border (Bulgaria).

### Submitted 8/8
259947.

### For 8/9 session
- Resolves today: 259947 MotoGP (Martin .30).
- Then 8/10: 112235 Golan (None .78). 8/11: 49405 Alabama (Marques .62), 517488 Shakhtar (Stamford Bridge .55), 772343 Romania (.65), 918938 Ferran (Barcelona .42).
- 8/12: 754377 Inter Miami (QF .38), 422179 divest (Elbit .2), 882554 Venezuela (Electoral .40), 459381 Spence (Tottenham .45), 604201 oil spill (Yemen .28), 628038 WAFCON (Morocco+Zambia .13).

## Day 47 (2026-08-09) — notes
- **Resolution**: 259947 MotoGP British GP → **Raul Fernandez** (my .10; +0.05, TW -14.11 — Martin on pole but Fernandez won).
- Cumulative: 94 resolved, TW 951.17, accuracy 14.3%, brier 0.095.
- **WAFCON (628038/616886)**: QFs — Morocco 2-1 South Africa; Algeria 2-1 Ivory Coast (both to semis + 2027 WC). Semis Aug 12: Morocco vs (Nigeria/Cameroon); Algeria vs (Ghana/Malawi). Updated 628038: Morocco+Algeria .18, Morocco+Nigeria .14, Morocco+Ghana .12. 616886: Morocco .40, Algeria .15, Nigeria .12.
- **Inter Miami (754377, 8/12)**: Lost 2-1 to Monterrey (Messi in Argentina after father's death); 3 pts, one group match left vs León Wed; "chances of advancing appear bleak". Updated: Phase One .50, QF .25, SF .13, Final .07.
- **Alabama 2nd (49405, Aug 11)**: Rhett Marques likely frontrunner (Trump, Sen. Britt endorsements); 6 candidates, no runoff. Keep Marques .62.
- **Shakhtar (517488, Aug 11)**: Arda Turan confirmed London home games; stadium (Stamford Bridge/Craven Cottage/Gtech) not finalized. Keep Stamford .55, Craven Cottage .30.

### Submitted 8/9
754377, 628038, 616886.

### For 8/10 session
- Resolves today: 112235 Golan (None by end of 2026 .78).
- Then 8/11: 49405 Alabama, 517488 Shakhtar, 772343 Romania (.65), 918938 Ferran (Barcelona .42).
- 8/12: 754377 Inter Miami (Phase One .50), 422179 divest (Elbit .20), 882554 Venezuela (Electoral .40), 459381 Spence (Tottenham .45), 604201 oil spill (Yemen .28), 628038 WAFCON (Morocco+Algeria .18).

## Day 48 (2026-08-10) — notes
- **Resolution**: 112235 Golan → **Colombia** (no mass; -0.62, TW -62.16). Surprise — Colombia recognized Israeli Golan sovereignty.
- Cumulative: 95 resolved, TW 889.01, accuracy 14.3%, brier 0.093.
- **WAFCON (628038/616886)**: Nigeria ELIMINATED (Cameroon beat them); Malawi also to semis. Semis Aug 12: **Morocco vs Cameroon; Algeria vs Malawi**. Updated 628038: Morocco+Algeria .40, Morocco+Malawi .22, Cameroon+Algeria .22, Cameroon+Malawi .12. 616886: Morocco .45, Algeria .18, Cameroon .15, Malawi .10.
- **Romania (772343, 8/11)**: Reactor 2 still running; 4 barges raised Danube ~8cm → at least 9 days (to ~Aug 18); CNCAN: could shut in 3-4 days if level keeps falling; forecast shows levels falling until Aug 16. Keep Romania .65.
- **Shakhtar (517488, 8/11)**: no stadium decision yet. Keep Stamford .55, Craven .30.
- **Ferran (918938, 8/11)**: no news. Keep Barcelona .42, PSG .30.
- **Alabama (49405, 8/11)**: primary tomorrow; Marques frontrunner (Trump/Britt). Keep .62.

### Submitted 8/10
628038, 616886.

### For 8/11 session
- Resolves today: 49405 Alabama (Marques .62), 517488 Shakhtar (Stamford .55), 772343 Romania (.65), 918938 Ferran (Barcelona .42).
- Then 8/12: 754377 Inter Miami (Phase One .50), 422179 divest (Elbit .20), 882554 Venezuela (Electoral .40), 459381 Spence (Tottenham .45), 604201 oil spill (Yemen .28), 628038 WAFCON (Morocco+Algeria .40).

## Day 49 (2026-08-11) — notes
- **Resolutions (4, all correct)**: 49405 Alabama → **Rhett Marques** (.62, +0.80, TW +80.42). 517488 Shakhtar → **Stamford Bridge** (.55, +0.71). 772343 Romania → **Romania** (.65, +0.86). 918938 Ferran → **PSG** (.30 second, +0.32).
- Cumulative: 99 resolved, TW 1014.90, accuracy 15.5%, brier 0.103.
- **Oil spill (604201, 8/12)**: Caroline Bezengi spill is off OMAN (Hallaniyat Islands, Dhofar), within 7km of Oman's mainland coast, spreading toward it. Updated: Oman .85, Yemen .06, Somalia .03, Djibouti .02, Egypt .02.
- **Djed Spence (459381, 8/12)**: Inter Milan closing in (~€30m + bonuses, "on his way" to San Siro; Gazzetta/talkSPORT). Updated: Inter Milan .85.
- **Venezuela (882554, 8/12)**: talks began Aug 6; agenda = quake aid, political rights (Oct), TSJ reinstitutionalization (Nov), CNE/electoral calendar (Dec); session permanent until Aug 12. Updated: Electoral branch .42, CNE .15, Judiciary .13.
- **Inter Miami (754377, 8/12)**: final Phase One match vs León (which has won both). Messi in Argentina. Keep Phase One .50.

### Submitted 8/11
604201, 459381, 628038, 616886, 882554.

### For 8/12 session
- Resolves today: 422179 (Elbit .20), 459381 (Inter .85), 604201 (Oman .85), 628038 (Morocco+Algeria .40), 754377 (Phase One .50), 882554 (Electoral .42).
- Then 8/13: 229258 Canadian Open women (Sabalenka .20), 311120 Spanish Super Cup host (Qatar .72). 8/14: 356699 Bangladesh Test century.
- 8/15: 541001 MLS East, 292136 Hockey, 764544 Indonesia quake, 113668 UFC strawweight, 277746 Djokovic, 777991/985937 Pan Pac swimming, 40115 UFC welterweight, 279786 Community Shield.

## Day 50 (2026-08-12) — notes
- **Resolutions (6)**: 422179 divest → **NextVision Stabilized Systems** (my .12; +0.15). 459381 Spence → **Inter Milan** (.85, +0.97, TW -28.88). 604201 oil spill → **Oman** (.85, +0.97, TW -11.66). 628038 WAFCON → **Cameroon, Malawi** (my .12; -0.03). 754377 Inter Miami → **Group stage** (Phase One .50; +0.67). 882554 Venezuela → **Judiciary** (my .13; +0.04).
- Cumulative: 105 resolved, TW 1002.06, accuracy 16.7%, brier 0.114.
- **Canadian Open (229258, 8/13)**: Semifinals Aug 12 = Swiatek vs Svitolina; Gauff vs Rybakina. Sabalenka OUT (R16). Final Thursday Aug 13. Updated: Swiatek .30, Rybakina .25, Gauff .22, Svitolina .18.
- **Spanish Super Cup (311120, 8/13)**: Qatar .72 stands.
- Note: next batch of resolutions 8/13-8/16: 229258, 311120, 356699 (BD Test century), 541001 MLS, 292136 Hockey, 764544 Indonesia quake, 113668 UFC, 277746 Djokovic, 777991/985937 Pan Pac, 40115 UFC, 279786 Community Shield, 616886 WAFCON, 565579 Japan GDP, 969395 St Jude.

### Submitted 8/12
229258.

### For 8/13 session
- Resolves today: 229258 (Swiatek .30), 311120 (Qatar .72).
- Watch: Community Shield (Arsenal vs Man City, Aug 16), WAFCON final (Aug 16), UFC 330 (Aug 15), Pan Pac swimming, St Jude Championship.

## Day 51 (2026-08-13) — notes
- **Resolutions**: 229258 Canadian Open → **Iga Swiatek** (.30, +0.37, TW +19.21). 311120 Spanish Super Cup → **Türkiye** (no mass; -0.56, TW -55.72 — Qatar was wrong).
- Cumulative: 107 resolved, TW 965.54, accuracy 17.1%, brier 0.114.
- **Bangladesh-Australia 1st Test (356699, 8/14)**: Darwin Day 1 — Australia 198 all out (Hasan Mahmud 6-55); Bangladesh 96/1 (Mominul 35*, Tanzid 32*). Updated: Mominul .25, Tanzid .15, Shanto .15, Mushfiqur .12, Litton .10.
- **WAFCON (616886, 8/16)**: Final = **Cameroon vs Malawi** (Malawi shocked Algeria; Cameroon beat Morocco). Updated: Cameroon .55, Malawi .40.
- Community Shield Aug 16: Arsenal vs Man City (Guimaraes made Arsenal debut). Keep Arsenal .47, City .43.
- UFC 330 (Aug 15): Makhachev vs Machado Garry; Dern vs Robertson. Keep.

### Submitted 8/13
356699, 616886.

### For 8/14 session
- Resolves today: 356699 (Mominul .25).
- 8/15: 541001 MLS East, 292136 Hockey Pool D, 764544 Indonesia quake, 113668 UFC strawweight (Dern .75), 277746 Djokovic, 777991/985937 Pan Pac, 40115 UFC welterweight (Makhachev .78).
- 8/16: 279786 Community Shield, 616886 WAFCON (Cameroon .55), 969395 St Jude.

## Day 52 (2026-08-14) — notes
- **Resolution**: 356699 BD Test century → **Tanzid Hasan** (my .15; +0.17).
- Cumulative: 108 resolved, TW 956.70, accuracy 17.1%, brier 0.114.
- **Indonesia quake (764544, 8/15)**: M7.7 struck off Flores (East Nusa Tenggara) Aug 14-15, tsunami up to 0.94m, USGS Yellow alert. Updated: Central Sulawesi .30, East Nusa Tenggara .30, West Sumatra .05, Aceh .05, North Sumatra .05.
- **UFC 330 (8/15)**: DraftKings — Makhachev -360 vs Garry +285; Dern -218 vs Robertson +180. Updated: Makhachev .77, Dern .68.
- **Pan Pac (8/15)**: Ledecky won 1500 (15:36.09); Pallister 2nd; Meg Harris won 100 free; Gretchen Walsh won 50 fly (CR 24.65). Keep 50 free spread (Walsh .26, Douglass .26), 800 free (Ledecky .44, Pallister .38).
- WAFCON final Aug 16: Cameroon vs Malawi (616886: Cameroon .55, Malawi .40).

### Submitted 8/14
764544, 40115, 113668.

### For 8/15 session
- Resolves today: 113668 (Dern .68), 277746 (Djokovic), 40115 (Makhachev .77), 541001 (Nashville .40), 764544 (C.Sulawesi .30/ENT .30), 777991 (Walsh .26), 985937 (Ledecky .44).
- 8/16: 279786 Community Shield (Arsenal .47), 616886 WAFCON (Cameroon .55), 969395 St Jude.

## Day 53 (2026-08-15) — notes
- **Resolutions (7)**: 113668 UFC strawweight → **Dern** (.68, +0.80, TW +87.35). 277746 Djokovic → **Thiago Tirante** (no mass). 40115 UFC WW → **Makhachev** (.77, +0.89, TW +90.30). 541001 MLS East → **Nashville** (.40, +0.51). 764544 Indonesia quake → **East Nusa Tenggara** (.30, +0.41). 777991 50m free → **Kate Douglass** (.26, +0.36). 985937 800m free → **Lani Pallister** (.38, +0.42).
- Cumulative: 115 resolved, TW 1229.72, accuracy 18.3%, brier 0.127.
- **St Jude (969395, 8/16)**: Scheffler leads at -11 (61 in R2), 3 shots over Im Sung-jae and Hovland; Aberg -7. Updated: Scheffler .45, Im .12, Hovland .12, Aberg .08, Spieth .05.
- **Community Shield (279786, 8/16)**: Arsenal vs Man City; Rice/Saka/Zubimendi available. Keep Arsenal .47, City .43, Draw .10.
- **WAFCON final (616886, 8/16)**: Cameroon vs Malawi. Keep Cameroon .55, Malawi .40.

### Submitted 8/15
969395.

### For 8/16 session
- Resolves today: 279786 (Arsenal .47), 616886 (Cameroon .55), 969395 (Scheffler .45).
- 8/17: 292136 Hockey Pool D (India .45), 565579 Japan GDP. 8/18: 418046 Medvedev, 970733 FDA, 844962 Ukraine, 984539 Imran Khan, 160265 Watkins, 720221 FL Mills, 246629 Gulf embargo, 845687 FL Dem (Vindman .88).

## Day 54 (2026-08-16) — notes
- **Resolutions (3, all top hits)**: 279786 Community Shield → **Arsenal** (.47, +0.52). 616886 WAFCON → **Cameroon** (.55, +0.64). 969395 St Jude → **Scheffler** (.45, +0.66).
- Cumulative: 118 resolved, TW 1295.31, accuracy 19.4%, brier 0.135.
- **Senegal coach (163032, 8/17)**: Multiple reports — **Patrick Vieira** to be named, 4-year contract agreed, presentation expected Tue Aug 18. Updated: Vieira .85.
- **Hockey World Cup Pool D (292136, 8/17)**: After MD1 — England 3pts (+3), India 3pts (+2), Wales 0, Pakistan 0. India vs England Aug 17. Updated: India .45, England .40, Pakistan .10.
- **Japan GDP (565579, 8/17)**: External demand .40, Private consumption .30 stands.

### Submitted 8/16
163032, 292136.

### For 8/17 session
- Resolves today: 163032 (Vieira .85), 292136 (India .45/England .40), 565579 (External demand .40).
- 8/18: 418046 Medvedev (Sinner .22), 970733 FDA (Overton .32), 844962 Ukraine (Poroshenko .25), 984539 Imran Khan (PIMS .35), 160265 Watkins (Villa .35), 720221 FL Mills (.45/.45), 246629 Gulf embargo (None .40), 845687 FL Dem (Vindman .88).

## Day 55 (2026-08-17) — notes
- **Resolutions (3)**: 163032 Senegal → **Patrick Vieira** (.85, +0.97, TW +17.15). 292136 Hockey Pool D → **England** (.40, +0.43). 565579 Japan GDP → **Net exports** (.40, +0.53).
- Cumulative: 121 resolved, TW 1400.88, accuracy 20.2%, brier 0.142.
- **Medvedev Cincinnati (418046, 8/18)**: Medvedev beat Trungelliti; next faces **Brandon Nakashima** (R3). Updated: Nakashima .30, Sinner .15, Alcaraz .12, Zverev .10, Fritz .05.
- **Djokovic Cincinnati (277746)**: resolved earlier — lost to Thiago Tirante.
- **Iran/Gulf (246629, 8/18)**: Trump threatens to strike Oman if it "gets in way" of Iran deal; two Iranian drones hit Iraqi Kurdistan PM's office. Keep None .40 for embargo.
- **FDA (970733, 8/18)**: no US nomination news. Keep Overton .32.
- **Imran Khan (984539, 8/18)**: no news. Keep PIMS .35.
- **FL primaries (720221/845687, 8/18)**: primary Aug 18. Keep Mills .45/Elijah .45; Vindman .88.
- **Ukraine elections (844962, 8/18)**: no news. Keep Poroshenko .25, Zelensky .22, Kuleba .18.

### Submitted 8/17
418046.

### For 8/18 session
- Resolves today: 160265 Watkins, 970733 FDA, 246629 Gulf embargo, 984539 Imran Khan, 418046 Medvedev, 720221 FL Mills, 844962 Ukraine elections, 845687 FL Dem.
- Then 8/19: 770763 Konsa (Villa .70), 903565 Nord Stream (None .68). 8/20: 764491 CA-14 (Wahab .80), 846721 Sinaloa (Bonilla .90), 916964 proxy (Hezbollah .40), 225772 Savinho (Tottenham .80), 855662 Alcaraz (Cincinnati .80), 248237 Baleba (ManU .60).

## Day 56 (2026-08-18) — notes
- **Resolutions (8)**: 160265 Watkins → **Al Hilal** (no mass; -0.20). 246629 Gulf embargo → **UAE** (.18, +0.11). 418046 Medvedev → **Nakashima** (.30, +0.46). 720221 FL Mills → **Ryan Elijah** (.45, +0.49). 844962 Ukraine → **Mykhailo Fedorov** (no mass; -0.16). 845687 FL Dem → **Angie Nixon** (.09; -0.60 — Vindman lost!). 970733 FDA → **Heidi Overton** (.32, +0.48). 984539 Imran Khan → **Shifa International** (.30, +0.36).
- Cumulative: 129 resolved, TW 1397.55, accuracy 21.0%, brier 0.146.
- 770763 Konsa (8/19): no news; keep Aston Villa .70.
- 903565 Nord Stream (8/19): keep None .68.
- Tottenham GK Vicario joined Juventus on loan (not a question).

### For 8/19 session
- Resolves today: 770763 (Villa .70), 903565 (None .68).
- 8/20: 764491 CA-14 (Wahab .80), 846721 Sinaloa (Bonilla .90), 916964 proxy (Hezbollah .40), 225772 Savinho (Tottenham .80), 855662 Alcaraz (Cincinnati .80), 248237 Baleba (ManU .60).
- 8/21: 767460 Marmoush (Villa .32/Barca .25/City .25). 8/22: 48050 robot (Shandian .42), 187330 IndyCar pole, 720892 AIPAC, 72132 Forest, 97251 ManUtd, 974146 Fabinho.

## Day 57 (2026-08-19) — notes
- **Resolutions**: 770763 Konsa → **Arsenal** (I had Villa .70; -0.51, TW -51.50). 903565 Nord Stream → **Volodymyr Zhuravlev** (my .12; -0.33).
- Cumulative: 131 resolved, TW 1313.48, accuracy 21.0%, brier 0.143.
- **Alcaraz (855662, 8/20)**: WITHDREW from Cincinnati; training in Murcia with Rune, testing wrist before US Open decision (final decision expected soon; on US Open entry list). Updated: US Open .65, None .15, Cincinnati .05, Shanghai .05.
- **Savinho (225772, 8/20)**: Tottenham in daily talks; £85m offer matching City's ask; medical booked; Savinho wants move. Updated: Tottenham .90.
- **Marmoush (767460, 8/21)**: Tottenham working on double deal (Savinho + Marmoush); City prepared to let both leave. Updated: Tottenham .45, Man City .20, Villa .15, Barca .10.
- **CA-14 (764491, 8/20)**: Wahab .80 stands. **Sinaloa (846721, 8/20)**: Bonilla .90 stands. **Proxy (916964, 8/20)**: Hezbollah .40, Houthis .35 stands.
- Community Shield result: Arsenal beat Man City 3-0 (Cardiff).

### Submitted 8/19
855662, 225772, 767460.

### For 8/20 session
- Resolves today: 225772 (Tottenham .90), 764491 (Wahab .80), 855662 (US Open .65), 846721 (Bonilla .90), 916964 (Hezbollah .40).
- 8/21: 767460 Marmoush (Tottenham .45), 248237 Baleba (ManU .60).
- 8/22: 48050 robot (Shandian .42), 187330 IndyCar pole (Palou .20), 720892 AIPAC (Moody .20), 72132 Forest (.46), 97251 ManUtd (.50), 974146 Fabinho (Palmeiras .28).

## Day 58 (2026-08-20) — notes
- **Resolutions (5)**: 225772 Savinho → **Tottenham** (.90, +0.98, TW +93.58). 764491 CA-14 → **Aisha Wahab** (.80, +0.93, TW +92.72). 846721 Sinaloa → **Ruben Rocha Moya** (my .08; -0.66, TW -65.64 — Bonilla was interim but Rocha returned). 855662 Alcaraz → **US Open** (.65, +0.85). 916964 proxy → **Hezbollah** (.40, +0.49, TW +51.32).
- Cumulative: 136 resolved, TW 1448.47, accuracy 22.6%, brier 0.153.
- **Baleba (248237, 8/21)**: ManU closing in; £60m+£5m bid; club agreement expected soon; player pushing. Updated: Man United .85.
- **Marmoush (767460, 8/21)**: Tottenham in double-deal talks (Savinho+Marmoush); Marmoush green light; City want £150m, Spurs £140m. Updated: Tottenham .65.
- Arsenal beat City 3-0 in Community Shield (Cardiff).

### Submitted 8/20
248237, 767460.

### For 8/21 session
- Resolves today: 248237 (ManU .85), 767460 (Tottenham .65).
- 8/22: 48050 robot (Shandian .42), 187330 IndyCar pole, 720892 AIPAC, 72132 Forest, 97251 ManUtd, 974146 Fabinho, 222955 Bouaddi.
- 8/23: 22056 400mH, 354508 100m, 260735/372528 Cincinnati, 669987 Dutch GP.

## Day 59 (2026-08-21) — notes
- **Resolutions**: 248237 Baleba → **Man United** (.85, +0.96, TW +73.49). 767460 Marmoush → **Tottenham** (.65, +0.83).
- Cumulative: 138 resolved, TW 1523.95, accuracy 23.4%, brier 0.160.
- **PL fixtures confirmed (Aug 22)**: Hull City vs Man United (97251: ManU .50, Draw .27, Hull .23); Nottingham Forest vs Leeds (72132: Forest .46, Draw .27, Leeds .27).
- **Robot race (48050, 8/22)**: Honor's "Flash"/Shandian targets 100m WR (~10s in testing; won robot half-marathon in April). Updated: Shandian .50.
- **IndyCar Freedom 250 (187330, 8/22)**: 25 drivers, 1.7-mile DC street circuit; Palou leads championship by 133; 5 poles in recent streak. Keep Palou .20, Kirkwood .20.
- **AIPAC (720892, 8/22)**: AIPAC weighing tens of millions to back Mike Rogers (MI GOP) vs El-Sayed. Question = which GOP Senate candidate ASKED AIPAC not to campaign. Updated: Rogers .30, Moody .15, Paxton .12.
- **Fabinho (974146, 8/22)**: left Al-Ittihad (free agent); PRIORITY is Europe (not Brazil); Fluminense only Brazilian club with contact; Palmeiras ruled out; MLS/Asia possible. Updated: Fluminense .25, Palmeiras .12, Flamengo .12, Inter Miami .10.
- Arsenal beat Coventry 3-0 (PL opener Aug 21).

### Submitted 8/21
48050, 97251, 72132, 720892, 974146.

### For 8/22 session
- Resolves today: 187330 (Palou .20), 48050 (Shandian .50), 97251 (ManU .50), 720892 (Rogers .30), 72132 (Forest .46), 974146 (Fluminense .25).
- 8/23: 22056 400mH (dos Santos .22), 354508 women's 100m, 260735/372528 Cincinnati winners, 669987 Dutch GP (Antonelli .28), 222955 Bouaddi (Arsenal .40).

## Day 60 (2026-08-22) — notes
- **Resolutions (6)**: 187330 IndyCar pole → **Alex Palou** (.20, +0.31). 48050 robot → **Tiangong Ultra** (no mass; -0.08). 720892 AIPAC → **Mike Rogers** (.30, +0.46). 72132 Forest opener → **Leeds United** (.27, +0.18). 97251 ManUtd opener → **Hull City** (.23, +0.08). 974146 Fabinho → **Trabzonspor** (no mass; -0.11).
- Cumulative: 144 resolved, TW 1579.41, accuracy 24.2%, brier 0.163.
- **Dutch GP (669987, 8/23)**: Norris took POLE at Zandvoort (surged past Russell and Antonelli). Updated: Norris .45, Russell .15, Antonelli .13, Verstappen .10, Piastri .05.
- **Cincinnati men (372528, 8/23)**: Nakashima beat Fritz (into SF); Alcaraz out (withdrew), Djokovic out (Tirante), Medvedev out (Nakashima). Updated: Sinner .40, Zverev .20, Nakashima .15.
- **Cincinnati women (260735, 8/23)**: Bejlek beat Keys (into SF); Sabalenka through. Updated: Sabalenka .25, Swiatek .18, Gauff .15, Rybakina .10, Bejlek .10.
- **Silesia DL (22056/354508, 8/23)**: no news; keep spreads.
- **Bouaddi (222955, 8/23)**: keep Arsenal .40, Lille .25, Man City .20.
- Serena Williams to play US Open mixed doubles with Alcaraz (not a question).

### Submitted 8/22
669987, 372528, 260735.

### For 8/23 session
- Resolves today: 22056 (dos Santos .22), 222955 (Arsenal .40), 260735 (Sabalenka .25), 354508 (Jefferson-Wooden .18), 372528 (Sinner .40), 669987 (Norris .45).
- Then 8/24: 461239 USS Lincoln port (Oman .30), 964047 Eurovision (Netherlands .40), 388162 Allan Elias (Napoli .35), 623398 Hadjam (Como .40/Young Boys .40).
- 8/25: 53266 PFA (Bruno Fernandes .92), 277370 Celtic (CL .62), 772246 Djokovic/Sabalenka mixed doubles, 874244 Witkoff Moscow, 903529 measles (Utah .35), 588637 Jackson.

## Day 61 (2026-08-23) — notes
- **Resolutions (6)**: 22056 400mH → **Alison Dos Santos** (.22, +0.32). 222955 Bouaddi → **Manchester City** (.20 second; +0.13). 260735 Cincinnati W → **Coco Gauff** (.15; +0.16). 354508 100m → **Melissa Jefferson-Wooden** (.18, +0.27). 372528 Cincinnati M → **Arthur Fils** (no mass; -0.23). 669987 Dutch GP → **Lando Norris** (.45, +0.65).
- Cumulative: 150 resolved, TW 1605.38, accuracy 25.4%, brier 0.169.
- **USS Lincoln (461239, 8/24)**: Lincoln left Middle East (Aug 20-21), heading to San Diego via 7th Fleet (4-5 week journey); made brief Guam stop in Dec and Oman resupply. Updated: United States .25, Japan .20, Singapore .12, Oman .10, Philippines .08.
- **Eurovision (964047, 8/24)**: Netherlands reportedly RETURNING to Eurovision 2027 (De Telegraaf); 2026 boycotters were Spain, Ireland, Netherlands, Slovenia, Iceland. Updated: Spain .30, Ireland .20, Slovenia .15, Iceland .12, Netherlands .10.
- **Allan Elias (388162, 8/24)**: keep Napoli .35, Palmeiras .30. **Hadjam (623398, 8/24)**: keep Como .40, Young Boys .40.

### Submitted 8/23
461239, 964047.

### For 8/24 session
- Resolves today: 388162 (Napoli .35), 461239 (US .25), 623398 (Como .40), 964047 (Spain .30).
- 8/25: 53266 PFA (Bruno Fernandes .92), 277370 Celtic (CL .62), 772246 Djokovic/Sabalenka mixed doubles, 874244 Witkoff Moscow (.40), 903529 measles (Utah .35), 588637 Jackson (Villa .40).
- 8/26: 834692 Xi Middle East (Saudi .30/UAE .30), 248237 done.

## Day 62 (2026-08-24) — notes
- **Resolutions (4)**: 388162 Allan Elias → **Manchester City** (no mass; -0.25). 461239 USS Lincoln → **Thailand** (no mass; -0.13). 623398 Hadjam → **Brighton** (no mass; -0.34). 964047 Eurovision → **Netherlands** (my .10; +0.02, TW +52.66).
- Cumulative: 154 resolved, TW 1577.17, accuracy 25.4%, brier 0.166.
- **Celtic (277370, 8/25)**: Celtic beat LASK 3-0 in CL playoff 1st leg; 2nd leg Aug 25 in Linz; "will reach league phase barring a collapse". Updated: Champions League .90.
- **PFA (53266, 8/25)**: no news; Bruno Fernandes .92 stands.
- **Measles (903529, 8/25)**: no 2026 death yet; Utah .35 stands.
- **Witkoff/Moscow (874244, 8/25)**: no direct news; Witkoff .40 stands.
- **Djokovic/Sabalenka mixed doubles (772246, 8/25)**: Serena/Alcaraz playing mixed doubles; keep spread.
- Cincinnati: Gauff beat Pegula (W); Fils won (M).

### Submitted 8/24
277370.

### For 8/25 session
- Resolves today: 277370 (CL .90), 53266 (Fernandes .92), 772246 (spread), 903529 (Utah .35), 874244 (Witkoff .40).
- 8/26: 834692 Xi Middle East (Saudi .30/UAE .30), 162316 Barcola (Liverpool .45), 876325 Enzo (Chelsea .40), 450664 Martinez (Juventus .45), 921981 SCO (Xi .28), 2260 Sydney Marathon M, 409386 Sydney Marathon W, 20480 Martinelli.

## Day 63 (2026-08-25) — notes
- **Resolutions (5)**: 277370 Celtic → **Europa League** (my CL .90; -0.62 but TW +21.75 from early Europa mass — Celtic LOST to LASK in 2nd leg!). 53266 PFA → **Bruno Fernandes** (.92, +0.99, TW +99.21). 772246 mixed doubles → **Patten and Siniakova** (no mass). 874244 Witkoff → **John Ratcliff** (US spy chief, no mass; -0.28). 903529 measles → **Pennsylvania** (my .06; -0.04).
- Cumulative: 159 resolved, TW 1656.47, accuracy 25.8%, brier 0.166.
- **Nicolas Jackson (588637, 8/26)**: Villa closing in on £65m permanent move (daily contact; Emery reunion); Jackson also agreed Atletico (Marca) but Atletico wants loan, Chelsea wants permanent. Updated: Villa .70, Atletico .15, Chelsea .08.
- **Xi Middle East (834692, 8/26)**: no Middle East news (Xi may visit India for BRICS in Sept). Keep Saudi .30, UAE .30.
- Confirmed: John Ratcliffe (DNI) visited Moscow (not Witkoff/Rubio).

### Submitted 8/25
588637.

### For 8/26 session
- Resolves today: 588637 (Villa .70), 834692 (Saudi .30/UAE .30).
- 8/27: 162316 Barcola (Liverpool .45), 876325 Enzo (Chelsea .40), 450664 Martinez (Juventus .45), 921981 SCO (Xi .28), 2260/409386 Sydney Marathon, 20480 Martinelli.
- 8/28: 120116 Norway monarch (Harald V .93), 248237 done.
- 8/29: 20480 Martinelli, 335239 Raam slate.

## Day 64 (2026-08-26) — notes
- **Resolutions**: 588637 Jackson → **Aston Villa** (.70, +0.88, TW +21.44). 834692 Xi Middle East → **Egypt** (my .12; +0.03).
- Cumulative: 161 resolved, TW 1681.19, accuracy 26.2%, brier 0.170.
- **Barcola (162316, 8/27)**: Liverpool struck verbal agreement with PSG (>£110m; Plateau); medical next; Romano cautious but "here we go" imminent. Updated: Liverpool .80.
- **Emiliano Martinez (450664, 8/27)**: CHELSEA contacted Martinez reps; Juventus deal collapsed (finger injury) and signed Vicario; Villa signed Zion Suzuki (Martinez available). Updated: Chelsea .40, Aston Villa .35, Besiktas .06.
- **Enzo (876325, 8/27)**: no news; Chelsea .40, Man City .25 stands.
- Man City signed Bouaddi (€100m); Newcastle signed Gonzalez from City.

### Submitted 8/26
162316, 450664.

### For 8/27 session
- Resolves today: 162316 (Liverpool .80), 450664 (Chelsea .40), 876325 (Chelsea .40).
- 8/28: 921981 SCO (Xi .28), 120116 Norway (Harald V .93), 2260/409386 Sydney Marathon, 20480 Martinelli.
- 8/29: 20480, 335239 Raam.

## Day 65 (2026-08-27) — notes
- **Resolutions (3, all top hits)**: 162316 Barcola → **Liverpool** (.80, +0.95, TW +56.28). 450664 Martinez → **Chelsea** (.40, +0.51). 876325 Enzo → **Manchester City** (.25 second, +0.27).
- Cumulative: 164 resolved, TW 1686.70, accuracy 27.0%, brier 0.176.
- **SCO summit (921981, 8/28)**: CONFIRMED — "PM Modi to hold bilateral talks with Putin on sidelines of SCO summit in Bishkek". Updated: Modi .75.
- **Norway monarch (120116, 8/28)**: King Harald V (89) in "extremely serious" condition (haemolytic anaemia, hospital since Aug 17); family gathered, engagements cancelled; Haakon acting regent. Updated: Haakon VIII .50, Harald V .48.
- CIA director Ratcliffe met Russian spy chief in Moscow (confirmed).

### Submitted 8/27
921981, 120116.

### For 8/28 session
- Resolves today: 120116 (Haakon .50), 921981 (Modi .75).
- 8/29: 2260/409386 Sydney Marathon, 20480 Martinelli, 335239 Raam.
- 8/30: 127253 Gabriel Jesus. 8/31: 79046 Villa-Arsenal, 335239.
- 9/1: 875467 PL top transfer fee. 9/2: 591807 Ghana coach, 712131 Gaza plan.

## Day 66 (2026-08-28) — notes
- **Resolutions**: 120116 Norway → **Haakon VIII** (.50, +0.52, TW -74.80). 921981 SCO → **Recep Tayyip Erdogan** (no mass; -0.58 — not Modi!).
- Cumulative: 166 resolved, TW 1592.79, accuracy 27.4%, brier 0.176.
- **Martinelli (20480, 8/29)**: Al-Hilal booked medical; agreement in principle €20M/yr to 2030; Arsenal to get €60M; announcement over weekend. Updated: Al-Hilal .90.
- **Sydney Marathon (2260/409386, 8/29)**: Men — Sisay Lemma (2:01:48 PB) fastest, Simbu (world champ), Kiplagat, Ngetich, Kiros (defending), Ramakongoana, Gebrhiwet (debut). Women — Peres Jepchirchir (2:14:43) headlines; Sifan Hassan NOT defending. Updated: Lemma .20, Simbu .15, Kiros .12; Jepchirchir .30, Cheptai .12.

### Submitted 8/28
20480, 2260, 409386.

### For 8/29 session
- Resolves today: 20480 (Al-Hilal .90), 2260 (Lemma .20), 409386 (Jepchirchir .30), 335239 Raam.
- 8/30: 127253 Gabriel Jesus (Everton .34). 8/31: 79046 Villa-Arsenal.
- 9/1: 875467 PL top transfer fee.

## Day 67 (2026-08-29) — notes
- **Resolutions**: 20480 Martinelli → **Al-Hilal** (.90, +0.99). 2260 Sydney M → **Addisu Gobena** (no mass; -0.09). 409386 Sydney W → **Peres Jepchirchir** (.30, +0.48).
- Cumulative: 169 resolved, TW 1576.06, accuracy 28.2%, brier 0.182.
- **Gabriel Jesus (127253, 8/30)**: Everton most likely (contact made; Arsenal want £18-20m; salary obstacle); Napoli key target but need to offload; Atletico offered (Alvarez link); Ipswich also. Updated: Everton .40, Napoli .20, Atletico .15, Ipswich .08, Palmeiras .05.
- Arsenal signings: Barcola to Liverpool done; Martinelli to Al-Hilal; Alvarez saga ongoing.

### Submitted 8/29
127253.

### For 8/30 session
- Resolves today: 127253 (Everton .40).
- 8/31: 79046 Villa-Arsenal (Villa .40, Arsenal .31, Draw .29).
- 9/1: 875467 PL top transfer fee.
- 9/2: 591807 Ghana coach (Renard .30), 712131 Gaza plan (Katz .30).
- Transfer deadline Sept 1 — many questions resolve around then.

## Day 68 (2026-08-30) — notes
- **Resolution**: 127253 Gabriel Jesus → **Barcelona** (no mass; -0.23 — surprise late move).
- Cumulative: 170 resolved, TW 1558.20, accuracy 28.2%, brier 0.181.
- **Villa-Arsenal (79046, 8/31)**: Watkins joined Al-Hilal; Villa lost 4-0 to Brighton in opener; Arsenal 3-0 Coventry + 3-0 Community Shield. Updated: Arsenal .50, Villa .27, Draw .23.
- **Raam slate (335239, 8/31)**: no news; keep Saadi .20 etc.
- Chelsea signed Emiliano Martinez from Villa (confirms 450664).

### Submitted 8/30
79046.

### For 8/31 session
- Resolves today: 335239 (Saadi .20), 79046 (Arsenal .50).
- 9/1: 875467 PL top transfer fee. 9/2: 591807 Ghana coach, 712131 Gaza plan.
- 9/4: 205592 FAO, 224345 haze, 568969 Betis-Madrid, 790870 bank. 9/5: 673971 MAGA ad.

## Day 69 (2026-08-31) — notes
- **Resolutions**: 335239 Raam → **Yoav Segalovich** (no mass; -0.07). 79046 Villa-Arsenal → **Arsenal** (.50, +0.62, TW +28.49).
- Cumulative: 172 resolved, TW 1579.41, accuracy 28.6%, brier 0.183.
- **PL top fee (875467, 9/1)**: Barcola to Liverpool £106m initial/£123m with add-ons (~€140m) — AP calls it "most expensive transfer of summer window"; Enzo to Man City ~€140m ($160.5m) "almost done"; Morgan Rogers £117m; Elliot Anderson £116m; Diomande £115.7m. Updated: Barcola .55, Enzo .40, Rogers .03.
- Gabriel Jesus → Barcelona (surprise); Watkins → Al-Hilal; Martinez → Chelsea; Martinelli → Al-Hilal.

### Submitted 8/31
875467.

### For 9/1 session
- Resolves today: 875467 (Barcola .55).
- 9/2: 591807 Ghana coach (Renard .30), 712131 Gaza plan (Katz .30).
- 9/4: 205592 FAO, 224345 haze, 568969 Betis-Madrid, 790870 bank.
- Remaining 80 questions through Sept 30.

## Day 70 (2026-09-01) — notes
- **Resolution**: 875467 PL top fee → **Enzo Fernandez** (Man City, ~€140m; my .40 second; +0.34, TW +20.62 — beat Barcola's £123m with add-ons).
- Cumulative: 173 resolved, TW 1600.03, accuracy 28.6%, brier 0.184.
- **Ghana coach (591807, 9/2)**: Queiroz out (contract expired, no extension); GFA pres: coach "99% in place, already working"; reports say **Desmond Ofei** (current assistant, ex-U20) to be appointed. Updated: Ofei .65, Renard .15, Queiroz .08.
- **Gaza plan (712131, 9/2)**: keep Katz .30, Smotrich .25, None .20. Smotrich/Feiglin joint election run announced.

### Submitted 9/1
591807.

### For 9/2 session
- Resolves today: 591807 (Ofei .65), 712131 (Katz .30).
- 9/4: 205592 FAO commodity, 224345 haze emergency, 568969 Betis-Madrid first goal, 790870 Treasury bank.
- 9/5: 673971 MAGA ad state. 9/6: 284913 La Liga leader, 490094 DRC Ebola, 668636 Italian GP.

## Day 71 (2026-09-02) — notes
- **Resolutions**: 591807 Ghana → **Carlos Queiroz** (my .08; -0.29 but TW +24.09 from early Queiroz mass — GFA reversed course and kept him). 712131 Gaza plan → **Itamar Ben-Gvir** (my .15; -0.22).
- Cumulative: 175 resolved, TW 1602.38, accuracy 28.6%, brier 0.182.
- **Haze (224345, 9/4)**: Haze hitting Sarawak (Malaysia), Singapore; dry September; water reserves low. Updated: Malaysia .40, Indonesia .40, Singapore .08.
- **Italian GP (668636, 9/6)**: Antonelli has grid penalty — starting from BACK of grid. Will update after qualifying (Sept 5).
- **Ebola (490094, 9/6)**: Ituri epicenter; schools resumed; WHO warns. Keep Ituri .78.
- Xi visited Egypt (confirms 834692).

### Submitted 9/2
224345.

### For 9/3 session
- Nothing resolves 9/3.
- 9/4: 205592 FAO, 224345 haze, 568969 Betis-Madrid first goal, 790870 Treasury bank.
- 9/5: 673971 MAGA ad. 9/6: 284913 La Liga, 490094 Ebola, 668636 Italian GP.

## Day 72 (2026-09-03) — notes
- No resolutions today. Cumulative: 175 resolved, TW 1602.38, accuracy 28.6%, brier 0.182.
- **Treasury bank (790870, 9/4)**: Bessent: "probably announce a bank sanction this week, and another next week" (Operation Economic Outcast); earlier limited an Egyptian bank's UAE ops; also targeting airline leasing cos tied to IRGC. Updated: Bank Melli .20, Bank Saderat .15, Bank Sepah .12, Bank Tejarat .10, Bank Mellat .08.
- **Betis-Madrid (568969, 9/4)**: Mbappe hat-trick vs Sociedad Aug 26. Updated: Mbappe .30, Vinicius .16.
- **Haze (224345, 9/4)**: Sarawak cloud seeding; no emergency declared yet; Malaysia .40/Indonesia .40.
- **FAO (205592, 9/4)**: no news; keep Oils .18 etc.
- Italian GP (668636, 9/6): Antonelli has grid penalty (back of grid).

### Submitted 9/3
790870, 568969.

### For 9/4 session
- Resolves today: 205592, 224345, 790870, 568969.
- 9/5: 673971 MAGA ad state. 9/6: 284913 La Liga leader, 490094 Ebola, 668636 Italian GP.

## Day 73 (2026-09-04) — notes
- **Resolutions (4)**: 205592 FAO → **Sugar** (.16, +0.18). 224345 haze → **Malaysia** (.40, +0.47). 568969 Betis-Madrid → **Troy Parrott** (no mass; -0.13). 790870 Treasury bank → **Golden Global Bank** (no mass; -0.09).
- Cumulative: 179 resolved, TW 1607.01, accuracy 28.6%, brier 0.184.
- **Italian GP (668636, 9/6)**: FP1 Ferrari 1-2 (Leclerc, Hamilton); FP2 Russell fastest (1:22.559) from Leclerc (+0.120), Antonelli 3rd (+0.141) but starts BACK of grid (engine penalties); Norris 4th; Verstappen expects pain. Updated: Russell .28, Leclerc .22, Hamilton .15, Norris .12, Antonelli .10.
- **La Liga (284913, 9/6)**: Betis beat Real Madrid (Mbappe missed pen) — Real's first defeat. Barcelona likely leads. Keep Barcelona .32.
- **Ebola (490094, 9/6)**: new case in rebel-held eastern DRC after outbreak declared over; Ituri epicenter. Keep Ituri .78.
- **MAGA ad (673971, 9/5)**: no news; keep North Carolina .30.

### Submitted 9/4
668636.

### For 9/5 session
- Resolves today: 673971 (NC .30).
- 9/6: 284913 (Barcelona .32), 490094 (Ituri .78), 668636 (Russell .28).

## Day 74 (2026-09-05) — notes
- **Resolution**: 673971 MAGA ad → **Texas** (no mass; -0.17).
- Cumulative: 180 resolved, TW 1589.76, accuracy 28.6%, brier 0.183.
- **Italian GP (668636, 9/6)**: Qualifying — **Pierre Gasly (Alpine) took shock POLE** ahead of Russell; Antonelli played team game (starts back). Updated: Russell .30, Gasly .20, Leclerc .15, Norris .12, Hamilton .10.
- La Liga: Betis beat Real Madrid (Mbappe missed pen) — Real's first defeat. 284913 (Barcelona .32) stands.
- Ebola (490094): Ituri .78 stands.

### Submitted 9/5
668636.

### For 9/6 session
- Resolves today: 284913 (Barcelona .32), 490094 (Ituri .78), 668636 (Russell .30/Gasly .20).
- 9/8: 546622 Liverpool sponsor, 880660 Brazil SC justice. 9/9: 408396 census status, 971366 England bowler.

## Day 75 (2026-09-06) — notes
- **Resolutions**: 284913 La Liga → **Barcelona** (.32, +0.43, TW +42.90). 490094 Ebola → **North Kivu** (my .12; -0.39, TW -38.68). 668636 Italian GP → **Kimi Antonelli** (my .10; -0.18 — won from back of grid!).
- Cumulative: 183 resolved, TW 1578.70, accuracy 29.0%, brier 0.183.
- **US Open men (408930, 9/11)**: Fritz OUT (Cerundolo); Shelton, Tiafoe, Paul, Michelsen, Tien remain. Updated: Shelton .50, Tiafoe .15, Paul .12, Michelsen .08, Tien .05.
- Remaining 69 questions resolve Sept 8-30. Key upcoming: 546622 Liverpool sponsor (9/8), 880660 Brazil SC (9/8), 408396 census status (9/9), 971366 England bowler (9/9), 508136 Mayun Island (9/10), 759359 Ukraine strikes (9/10).

### Submitted 9/6
408930.

### For 9/7 session
- Nothing resolves 9/7. Prepare for 9/8-9/13 batch (US Open finals, Venice, Emmys).

## Day 76 (2026-09-07) — notes
- No resolutions. Cumulative: 183 resolved, TW 1578.70, accuracy 29.0%, brier 0.183.
- Reviewed remaining 69 questions (Sept 8-30). Key ones:
  - 546622 Liverpool sponsor (9/8): SC .12, Riyadh Air .10, Emirates .08.
  - 880660 Brazil SC (9/8): None .70 (Brazil court crisis in news; Bolsonaro son rallies).
  - 971366 England bowler (9/9): Tongue .20, Atkinson .18, Archer .14.
  - 759359 Ukraine city (9/10): Kyiv .45.
  - 408396 census status (9/9): LPR .55.
  - 408930 US player (9/11): Shelton .50 (Fritz out).
  - 508136 Mayun Island (9/10): Houthis .40.
  - US Open finals (9/12-13): Sabalenka .28; Sinner .40.
  - Emmys (9/14): Hacks .62; The Pitt .58; Rhea Seehorn .60.
  - 48458 Spanish GP (9/13): Antonelli .25.
  - 870914 space weapons (9/14): Russia .55.

### For 9/8 session
- Resolves today: 546622, 880660.

## Day 77 (2026-09-08) — notes
- **Resolutions**: 546622 Liverpool sponsor → **Turkish Airlines** (no mass; -0.04). 880660 Brazil SC → **Andre Mendonca** (my .10; -0.31).
- Cumulative: 185 resolved, TW 1543.24, accuracy 29.0%, brier 0.181.
- **England bowler (971366, 9/9)**: 3rd Test at Edgbaston starts Sept 9. Carse OUT (police probe); attack = Archer, Robinson, Tongue, Atkinson; Tongue 13 wkts @12.46 in series; Robinson 8-35 in 2nd Test. Updated: Tongue .28, Robinson .22, Atkinson .18, Archer .15, Baker .05.
- **Census status (408396, 9/9)**: no news; LPR .55 stands.

### Submitted 9/8
971366.

### For 9/9 session
- Resolves today: 408396 (LPR .55), 971366 (Tongue .28).
- 9/10: 508136 Mayun (Houthis .40), 759359 Ukraine city (Kyiv .45).
- 9/11: 408930 US player (Shelton .50), 342722 Donnarumma (Kherbouch .60), 936021 5000m (Yihune .20).

## Day 78 (2026-09-09) — notes
- **Resolutions**: 408396 census → **Permanent residency** (my LPR .55 matched; +0.75, TW +75.00). 971366 England bowler → **Josh Tongue** (.28, +0.38, TW +29.27).
- Cumulative: 187 resolved, TW 1647.51, accuracy 29.8%, brier 0.186.
- **Mayun Island (508136, 9/10)**: Houthis vs Saudi-backed forces fighting on Yemen's west coast; 30+ Saudi strikes. Keep Houthis .40, Yemeni govt .30.
- **Ukraine city (759359, 9/10)**: keep Kyiv .45.

### For 9/10 session
- Resolves today: 508136, 759359.
- 9/11: 408930 (Shelton .50), 342722 (Kherbouch .60), 936021 (Yihune .20).
- 9/12: 261941 (Yan .30), 52657 (Venice), 608158 (Sabalenka .28), 5814 (Villa .44).

## Day 79 (2026-09-10) — notes
- **Resolutions (2, both top hits)**: 508136 Mayun Island → **Houthis** (.40, +0.50, TW +50.00). 759359 Ukraine → **Kyiv** (.45, +0.61, TW +61.50).
- Cumulative: 189 resolved, TW 1759.01, accuracy 30.6%, brier 0.190.
- **US player (408930, 9/11)**: Shelton AND Tiafoe both in US Open SEMIS (Alcaraz OUT!). Updated: Shelton .50, Tiafoe .45.
- **5000m (936021, 9/11)**: Ultimate Championship starts; no start list news. Keep Yihune .20.
- **Donnarumma (342722, 9/11)**: keep Kherbouch .60.

### For 9/11 session
- Resolves today: 342722, 408930, 936021.
- 9/12: 261941 (Yan .30), 52657 (Venice), 608158 (Sabalenka .28), 5814 (Villa .44).
- 9/13: 581343 Okinawa (Tamaki .68), 174389 venue (US .45), 30434 javelin (Tharanga .22), 487575 derby (City .45), 653425 200m (Tebogo/Lyles .28), 891014 US Open men (Sinner .40), 48458 Spanish GP (Antonelli .25).

## Day 80 (2026-09-11) — notes
- **Resolutions (3)**: 342722 Donnarumma → **Ilyas Kherbouch** (.60, +0.81, TW +80.82). 408930 US player → **Ben Shelton** (.50, +0.55, TW +44.30). 936021 5000m → **Jakob Ingebrigtsen** (no mass; -0.08).
- Cumulative: 192 resolved, TW 1876.39, accuracy 31.3%, brier 0.195.
- **US Open W (608158, 9/12)**: Final = **Sabalenka vs Rybakina** (Rybakina beat Gauff; Sabalenka beat Pegula). Updated: Sabalenka .55, Rybakina .45.
- **Villa-Forest (5814, 9/12)**: Villa lost 4-0 to Brighton, sold Watkins. Updated: Villa .38, Forest .34, Draw .28.
- Venice: Gaza doc 'NAZA' got 25-min ovation. 52657 (Special Jury) no specific news.

### Submitted 9/11
608158, 5814.

### For 9/12 session
- Resolves today: 261941 (Yan .30), 52657 (Venice), 5814, 608158.
- 9/13: 581343 Okinawa (Tamaki .68), 174389 venue (US .45), 30434 javelin (Tharanga .22), 487575 derby (City .45), 653425 200m, 891014 US Open men (Sinner .40), 48458 Spanish GP (Antonelli .25).

## Day 81 (2026-09-12) — notes
- **Resolutions (4)**: 261941 javelin → **Haruka Kitaguchi** (.16, +0.17). 52657 Venice → **NAZA** (no mass; -0.04). 5814 Villa-Forest → **Nottingham Forest** (.34, +0.34). 608158 US Open W → **Rybakina** (.45, +0.39).
- Cumulative: 196 resolved, TW 1914.19, accuracy 31.3%, brier 0.199.
- **Spanish GP (48458, 9/13)**: Norris took POLE from Antonelli. Updated: Norris .45, Antonelli .18, Russell .12.
- **US Open M (891014, 9/13)**: Final = **Shelton vs Zverev** (Sinner & Alcaraz OUT). Updated: Shelton .55, Zverev .45.
- Manchester derby (487575): City .45, United .28, Draw .27.
- Okinawa (581343): Tamaki .68. 200m (653425): Tebogo/Lyles .28 each. Javelin (30434): Tharanga .22.

### Submitted 9/12
48458, 891014.

### For 9/13 session
- Resolves today: 174389, 30434, 487575, 48458, 653425, 581343, 891014.
- 9/14: Emmys (216881 Hacks .62, 873349 The Pitt .58, 440552 Seehorn .60), 816232 CL final stadium (Camp Nou .58), 870914 space weapons (Russia .55).

## Day 82 (2026-09-13) — notes
- **Resolutions (7)**: 174389 venue → **UAE** (my .10; -0.10). 30434 javelin → **Rumesh Tharanga Pathirage** (.22, +0.34). 48458 Spanish GP → **Kimi Antonelli** (my .18; -0.27). 487575 derby → **Man City** (.45, +0.55, TW +54.62). 581343 Okinawa → **Genta Koja** (my .27; +0.00). 653425 200m → **Bednarek** (my .10; +0.03). 891014 US Open → **Zverev** (.45, +0.39).
- Cumulative: 203 resolved, TW 1982.31, accuracy 32.1%, brier 0.202.
- Emmys (9/14): Hacks .62, The Pitt .58, Seehorn .60 stands.
- CL final stadium (816232): Camp Nou .58. Space weapons (870914): Russia .55.

### For 9/14 session
- Resolves today: 216881, 440552, 816232, 870914, 873349.
- 9/15: 518392 2029 World Athletics (London .42). 9/16: 753240 Campeones (Inter Miami .42), 101639 UNGA (Gaza .35), 56802 Iran-Houthis (US .30).

## Day 83 (2026-09-14) — notes
- **Resolutions (5)**: 216881 Comedy Emmy → **Widow's Bay** (no mass; -0.42). 440552 Lead Actress → **Rhea Seehorn** (.60, +0.79, TW +79.38). 816232 CL final → **Camp Nou** (.58, +0.71, TW +70.80). 870914 space weapons → **United States** (my .12; -0.12). 873349 Drama Emmy → **The Pitt** (.58, +0.74, TW +73.78).
- Cumulative: 208 resolved, TW 2152.44, accuracy 33.3%, brier 0.209.
- 518392 (2029 World Athletics host, 9/15): London .42 stands; no news.

### For 9/15 session
- Resolves today: 518392 (London .42).
- 9/16: 753240 Campeones (Inter Miami .42), 101639 UNGA (Gaza .35), 56802 Iran-Houthis (US .30).
- 9/17: 660356 Nigeria official (None .65).

## Day 84 (2026-09-15) — notes
- **Resolution**: 518392 2029 World Athletics → **Nairobi** (my .12; -0.02).
- Cumulative: 209 resolved, TW 2150.10, accuracy 33.3%, brier 0.209.
- **UNGA appeal (101639, 9/16)**: UN urging foreign investigators' access to Gaza; hundreds of bodies from rubble; war crimes concerns. Updated: Gaza .50, Sudan .20, Afghanistan .10.
- **Iran-Houthis (56802, 9/16)**: Houthi missile/drone attacks injure 13 in S Saudi; Riyadh vows firm response. Keep US .30, China .25.
- **Campeones Cup (753240, 9/16)**: Inter Miami new manager 'Kily' Gonzalez; keep Inter Miami .42.

### Submitted 9/15
101639.

### For 9/16 session
- Resolves today: 101639 (Gaza .50), 56802 (US .30), 753240 (Inter Miami .42).
- 9/17: 660356 Nigeria official (None .65). 9/18: 934953 GOP senator (Tillis .25), 574485 PSA (El Hammamy .72), 729308 Mbappe sponsor (Nike .52).

## Day 85 (2026-09-16) — notes
- **Resolutions (3)**: 101639 UNGA → **Yemen** (my .08; -0.15). 56802 Iran-Houthis → **China** (.25, +0.32, TW +32.47). 753240 Campeones → **Inter Miami** (.42, +0.55, TW +54.84).
- Cumulative: 212 resolved, TW 2235.67, accuracy 33.7%, brier 0.212.
- 660356 Nigeria official (9/17): None .65 stands; no news.

### For 9/17 session
- Resolves today: 660356 (None .65).
- 9/18: 934953 GOP senator (Tillis .25), 574485 PSA squash (El Hammamy .72), 729308 Mbappe sponsor (Nike .52).
- 9/19: 425800 UFC flyweight (Van .68), 574553 UFC lightweight (Pimblett .20).

## Day 86 (2026-09-17) — notes
- **Resolution**: 660356 Nigeria → **Suberu Siyaka Aniviye** (no mass; -0.43).
- Cumulative: 213 resolved, TW 2192.42, accuracy 33.7%, brier 0.210.
- 574485 PSA (9/18): El Hammamy .72 stands. 729308 Mbappe sponsor (9/18): Nike .52. 934953 GOP senator (9/18): Tillis .25.

### For 9/18 session
- Resolves today: 574485, 729308, 934953.
- 9/19: 425800 UFC flyweight (Van .68), 574553 UFC lightweight (Pimblett .20).
- 9/20: 81247 Berlin (CDU .60), 67348 basketball (Japan .30), 784475 half marathon, 299105 Iran GDP (Oil .55), 297571 Madrid derby (Real .44).

## Day 87 (2026-09-18) — notes
- **Resolutions**: 574485 PSA → **Amina Orfi** (my .20; -0.16). 729308 Mbappe sponsor → **On** (no mass; -0.32). 934953 GOP senator → **John Curtis** (no mass; -0.13).
- Cumulative: 216 resolved, TW 2131.10, accuracy 33.7%, brier 0.208.
- **UFC 331 (9/19)**: 425800 flyweight = Van (-130/-140) vs Pantoja (+110/+115) → Van .58, Pantoja .42. 574553 co-main = **Tsarukyan (-305) vs Ruffy (+240)** (NOT Pimblett!) → Tsarukyan .70, Ruffy .30.

### Submitted 9/18
425800, 574553.

### For 9/19 session
- Resolves today: 425800 (Van .58), 574553 (Tsarukyan .70).
- 9/20: 81247 Berlin (CDU .60), 67348 basketball (Japan .30), 784475 half marathon, 299105 Iran GDP (Oil .55), 297571 Madrid derby (Real .44).

## Day 88 (2026-09-19) — notes
- **Resolutions (2)**: 425800 UFC flyweight → **Joshua Van** (.58, +0.65, TW +79.35). 574553 UFC lightweight → **Arman Tsarukyan** (.70, +0.82, TW +11.93).
- Cumulative: 218 resolved, TW 2222.38, accuracy 34.5%, brier 0.214.
- **Basketball bronze (67348, 9/20)**: S. Korea reached men's FINAL (so not bronze); Iran lost to Korea. Updated: Iran .30, Japan .20, Philippines .20, China .15, Chinese Taipei .10.
- **Berlin (81247, 9/20)**: AfD surge in eastern Germany. Updated: CDU .50, AfD .20, SPD .10, Linke .08, Greens .05.
- **Madrid derby (297571, 9/20)**: Mourinho's Real lacking control; lost to Betis recently. Updated: Real .38, Atletico .33, Draw .29.
- 299105 Iran GDP (Oil .55), 784475 half marathon stand.

### Submitted 9/19
67348, 81247, 297571.

### For 9/20 session
- Resolves today: 297571, 81247, 299105, 784475, 67348.
- 9/21: 224082 200m IM (Yu Yiting .80), 25611 Rwanda suspect (Mutabaruka/Munyaneza .25 each).
- 9/22: 423956 Hungary immunity (No immunity .40).

## Day 89 (2026-09-20) — notes
- **Resolutions (5)**: 297571 Madrid derby → **Atletico Madrid** (.33, +0.32, TW +21.09). 299105 Iran GDP → **Oil and gas** (my Oil .55; -0.34). 67348 basketball → **Iran** (.30, +0.40). 784475 half marathon → **Ngetich** (.12, +0.19). 81247 Berlin → **The Left** (my .08; -0.15).
- Cumulative: 223 resolved, TW 2209.32, accuracy 34.9%, brier 0.215.
- **200m IM (224082, 9/21)**: Yu Zidi (13) won 200 fly in Asian Games record 2:05.08; scheduled for 3 individual events. Updated: Yu Yiting .55, Yu Zidi .35.
- 25611 Rwanda suspect (9/21): keep Mutabaruka .25, Munyaneza .25.

### Submitted 9/20
224082.

### For 9/21 session
- Resolves today: 224082 (Yu Yiting .55), 25611 (Rwanda).
- 9/22: 423956 Hungary immunity (No immunity .40).
- 9/23: 300850 400m IM (Yu Zidi .68), 832291 weightlifting (Huang .35), 788295 Tunisia activist.

## Day 90 (2026-09-21) — notes
- **Resolutions**: 224082 200m IM → **Yu Zidi** (.35, +0.27, TW -41.01). 25611 Rwanda → **Vincent Brown** (my .15 for Bajinya; -0.17).
- Cumulative: 225 resolved, TW 2151.12, accuracy 34.9%, brier 0.216.
- 423956 Hungary immunity (9/22): No immunity .40 stands; no news.

### For 9/22 session
- Resolves today: 423956 (No immunity .40).
- 9/23: 300850 400m IM (Yu Zidi .68), 832291 weightlifting (Huang .35), 788295 Tunisia activist.
- 9/24: 731076 Artemis (Colombia .08), 190556 breaststroke (Qin .45), 564365 Portugal goal (Ronaldo .24).

## Day 91 (2026-09-22) — notes
- **Resolution**: 423956 Hungary immunity → **Balazs Hanko** (no mass; -0.19).
- Cumulative: 226 resolved, TW 2131.68, accuracy 34.9%, brier 0.215.
- 300850 400m IM (9/23): Yu Zidi .68 stands (won 200 fly & 200 IM).
- 788295 Tunisia activist (9/23), 832291 weightlifting (9/23): keep.

### For 9/23 session
- Resolves today: 300850, 788295, 832291.
- 9/24: 731076 Artemis (Colombia .08), 190556 breaststroke (Qin .45), 564365 Portugal goal (Ronaldo .24).

## Day 92 (2026-09-23) — notes
- **Resolutions (3)**: 300850 400m IM → **Yu Zidi** (.68, +0.84, TW +84.42). 788295 Tunisia → **Wael Naouar** (.15, +0.25, TW +24.62). 832291 weightlifting → **Ri Song Gum** (my .12; +0.07).
- Cumulative: 229 resolved, TW 2247.50, accuracy 35.7%, brier 0.220.
- **Portugal goal (564365, 9/24)**: Ronaldo continues international career, eyes 1000 goals. Updated: Ronaldo .28, Bruno .12.
- 190556 breaststroke (9/24): Qin .45, Ohashi .40. 731076 Artemis (9/24): keep Colombia .08.

### Submitted 9/23
564365.

### For 9/24 session
- Resolves today: 190556, 564365, 731076.
- 9/25: 76365 court (Fourth Circuit .30), 154739 TikTok (California .25), 686508 100m (Boonson .40).

## Day 93 (2026-09-24) — notes
- **Resolutions (3)**: 190556 breaststroke → **Shin Ohashi** (.40, +0.43, TW +42.50). 564365 Portugal → **Joao Felix** (no mass; -0.10). 731076 Artemis → **Ivory Coast** (no mass; -0.02).
- Cumulative: 232 resolved, TW 2279.05, accuracy 35.7%, brier 0.221.
- 154739 TikTok (9/25): California .25 stands. 76365 court (9/25): Fourth Circuit .30. 686508 100m (9/25): Boonson .40.

### For 9/25 session
- Resolves today: 154739, 76365, 686508.
- 9/26: 996188 Puyo Puyo (Yo Kim .40), 173061 England-Spain (Spain .47), 447470 Azerbaijan GP (Antonelli .25), 540490 Kohli (.35), 944956 DOSB (Munich .45).

## Day 94 (2026-09-25) — notes
- **Resolutions (3)**: 154739 TikTok → **Alabama** (no mass; -0.12). 686508 100m → **Puripol Boonson** (.40, +0.58, TW +58.50). 76365 court → **Sixth Circuit** (.20, +0.25, TW +24.67).
- Cumulative: 235 resolved, TW 2350.64, accuracy 36.1%, brier 0.224.
- **Azerbaijan GP (447470, 9/26)**: Russell took POLE; Antonelli crashed in qualifying ("stupid" crash). Updated: Russell .40, Leclerc .12, Verstappen .10, Norris .10, Antonelli .08.
- 173061 England-Spain (Spain .47), 540490 Kohli (.35), 944956 DOSB (Munich .45), 996188 Puyo Puyo (Yo Kim .40) stand.

### Submitted 9/25
447470.

### For 9/26 session
- Resolves today: 173061, 447470, 540490, 944956, 996188.
- 9/27: 259249 Sindhu (QF .35), 556932 squash W (Anahat .30), 158157 Ireland-Israel (Ireland .42), 700005 squash M (Ng .30), 88025 Ramallah (Norway .25).

## Day 95 (2026-09-26) — notes
- **Resolutions (5)**: 173061 England-Spain → **Spain** (.47, +0.58, TW +57.82). 447470 Azerbaijan GP → **Russell** (.40, +0.60). 540490 Kohli → **Virat Kohli** (.35, +0.48). 944956 DOSB → **Munich** (.45, +0.56). 996188 Puyo Puyo → **Yuki Kurihara** (no mass; -0.22).
- Cumulative: 240 resolved, TW 2508.63, accuracy 37.7%, brier 0.231.
- **Squash W (556932, 9/27)**: Anahat Singh into final (beat world No.6). Updated: Anahat .60, Watanabe .15, Sivasangari .10.
- 158157 Ireland-Israel (Ireland .42), 259249 Sindhu (QF .35), 700005 squash M (Ng .30), 88025 Ramallah (Norway .25) stand.

### Submitted 9/26
556932.

### For 9/27 session
- Resolves today: 158157, 259249, 556932, 88025, 700005.
- 9/28: 815451 Nations League A1 (France .60), 133827 ChatGPT state (Florida .45), 695205 javelin Asian Games (Nadeem .42).
- 9/29: 315568 Aston Martin (Alonso .45), 935351 Morocco PM.
- 9/30: 889545 China football, 138739 Christa Pike.

## Day 96 (2026-09-27) — notes
- **Resolutions (5)**: 158157 Ireland-Israel → **Ireland** (.42, +0.49, TW +49.46). 259249 Sindhu → **Quarterfinals** (.35, +0.44). 556932 squash W → **Sivasangari** (my .10; -0.20 but TW +38.13). 700005 squash M → **Ng Eain Yow** (.30, +0.42). 88025 Ramallah → **Netherlands** (no mass; -0.14).
- Cumulative: 245 resolved, TW 2668.22, accuracy 38.9%, brier 0.236.
- ONLY 7 QUESTIONS LEFT.
- 133827 ChatGPT state (9/28): Florida .45 stands. 695205 javelin (9/28): Nadeem .42, Chopra .38. 815451 Nations League A1 (9/28): France .60.

### For 9/28 session
- Resolves today: 133827, 695205, 815451.
- 9/29: 315568 Aston Martin (Alonso .45), 935351 Morocco PM (Akhannouch .30/Chaouki .30).
- 9/30: 889545 China football, 138739 Christa Pike (Tennessee SC .45).

## Day 97 (2026-09-28) — notes
- **Resolutions (3)**: 133827 ChatGPT → **Florida** (.45, +0.66, TW +66.01). 695205 javelin → **Rumesh Pathirage** (my .05; -0.23). 815451 Nations League → **France** (.60, +0.78, TW +78.22).
- Cumulative: 248 resolved, TW 2789.54, accuracy 39.7%, brier 0.240.
- ONLY 4 QUESTIONS LEFT.
- 315568 Aston Martin (9/29): Alonso .45. 935351 Morocco PM (9/29): Akhannouch .30/Chaouki .30.

### For 9/29 session
- Resolves today: 315568, 935351.
- 9/30: 889545 China football (South Korea .30), 138739 Christa Pike (Tennessee SC .45).

## Day 98 (2026-09-29) — notes
- **Resolutions (2)**: 315568 Aston Martin → **Fernando Alonso** (.45, +0.66, TW +65.62). 935351 Morocco PM → **El Mansouri** (my .08; -0.04).
- Cumulative: 250 resolved, TW 2850.83, accuracy 40.1%, brier 0.243.
- ONLY 2 QUESTIONS LEFT (both resolve 9/30):
  - **138739 Christa Pike stay**: Execution set for Sept 30; no stay reported yet. Updated: Tennessee SC .35, No court .30, U.S. Supreme Court .25, Davidson Chancery .05, Sixth Circuit .05.
  - **889545 China football**: Men's semifinal = **South Korea vs China** (Sept 30); winner plays Japan/Uzbekistan in final Oct 3. Updated: South Korea .60, Japan .15, Uzbekistan .12.

### Submitted 9/29
889545, 138739.

### For 9/30 session
- Final day: 138739, 889545 resolve.

## FINAL SESSION SUMMARY (2026-09-30) — ALL 252 QUESTIONS RESOLVED
- **Final resolutions**: 138739 Christa Pike → **Sixth Circuit** (my .05; -0.18, TW -30.62). 889545 China football → **South Korea** (.60, +0.80, TW +41.70).
- **FINAL SCORE: 252 predictions, 252 resolved, accuracy 40.5%, Brier Skill Score 0.245, Time-Weighted Score 2861.91.**
- Progress: started at TW ~29 (day 8) → 2862 final. Big gains came from: (1) updating early when news arrived (F1 qualifying, transfer sagas), (2) nailing high-confidence picks (England-India T20 +66, SK Hynix +96, PFA +99, BTS... ), (3) hedging with 5 outcomes on uncertain fields.

### Key lessons across 98 simulated days
1. **TW-score weights early predictions heavily** — the opening-day forecast carries the most weight. Being wrong early (Nvidia .82 on most-valuable-company, Muchova .55 on Wimbledon, Chopra-heavy javelin) cost far more than late corrections could recover.
2. **Late news beats early analysis** for sports/transfers: use qualifying results, injury reports, grid penalties, polls 1-2 days before resolution.
3. **Transfers can flip at the last minute** (Rogers→Chelsea, Jackson→Villa not Everton, Jesus→Barcelona, Salah→Trabzonspor, Fabinho→Trabzonspor). Keep 3-4 plausible clubs, never 0.85+ on a transfer unless the medical is booked.
4. **"If X happens" questions**: the sim grades to the eventual outcome even if after the nominal date; current club can be the answer if no move.
5. **F1 races are high variance**: use flatter spreads; pole-sitter ~40-45%, but backmarker-team shocks happen (Gasly pole, Antonelli win from back).
6. **FOMC dissent questions**: include all regional bank presidents who dissented at the previous meeting (Kashkari was missed).
7. **"Only nuclear plant" questions**: match the exact phrasing to the country's plant count (Hungary/Paks fit "announce plans"; Romania/Cernavodă fit "complete shutdown").
8. **Soccer/football winner markets**: bookmaker odds normalized are the best prior; upset rate in single matches ~25-30%.
9. **Political primaries**: late polling shifts matter (Michigan El-Sayed +10 flip); prediction markets (Polymarket/Kalshi) are strong signals.
10. **Geopolitical questions**: the sim's world escalated Iran war through 2026; US struck Iraq (not Yemen) for proxy retaliation; Oman mediated Hormuz.
