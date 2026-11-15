# Daily log

## 2026-06-24 (day 1)
- Read 252 questions; built 19 topical batches; spawned 19 research sub-agents (general-purpose) to research + submit all.
- Search budget allotted ~1,075 across agents.
- Session 1 lost (agents killed when turn ended). Session 2: re-ran 19 foreground agents; all 252 forecasts submitted + notes (memory/research/). ~708 searches used; ~1,845 left.
- Built scan_articles.py + keywords.json, record.py, world_state.md.
- Priorities for 06-25..07-01: Jaylen Brown trade (07-01), Russian official at Khamenei funeral (Kremlin ~07-01/02), Palestinian FA restart (07-01), Trey Alexander (07-04), cyclospora (07-04/16), Women's T20 WC semis (07-02/03), British GP (07-05), UK by-election leader (07-07), Moldova PM (07-08), Dugan sentencing (07-08), WC R32 results (06-28..07-03) -> rerun memory/research/wc_sim.py.

## 2026-06-25 (day 2)
- Verified all 252 day-1 predictions recorded (predictions/2026-06-24.json).
- Updates: 258607 Women's T20 (India must beat Aus Jun 28; Aus .52 Eng .23 Ind .09 SA .08 WI .06); 112235 Golan (Colombia up to .16: De la Espriella inaugurated Aug 7 ~ res Aug 10).
- News: Celtics "hunting a big man" for Brown (Shams: active talks, not close). Khamenei funeral Jul 4-9 (lying in state Jul 4-5, procession Jul 6, Qom Jul 7, Najaf/Karbala Jul 8, Mashhad burial Jul 9); Pakistan PM + Munir expected; Modi invited.
- Cyclospora: 145 domestic cases in 17 states (as of Jun 16), no state breakdown.
- WC results Jun 24-25: Mexico 3-0 Czechia, South Africa 1-0 South Korea, Brazil 3-0 Scotland, Morocco 4-2 Haiti, Ecuador 2-1 Germany (Germany still top E), Ivory Coast beat Curacao (Pepe 2). Plan: full wc_sim rerun on Jun 28 with official bracket.
- Searches used today: 3 (1,844 left).

## 2026-06-26 (day 3)
- Wimbledon draw: Sinner & Djokovic same (top) half (proj SF); bottom half Zverev(2), Shelton(4), de Minaur(5), Fritz(6). Serena Williams wildcard (v Maya Joint). Andreeva = RG 2026 champion. Swiatek same half as Rybakina.
  -> 985440 first finalist: Sinner .24 Zverev .17 Fritz .11 Shelton .09 Djokovic .08; 742225 champion: Sinner .50 Djokovic .12 Zverev .10 Fritz .06 Shelton .045.
- Elliot Anderson -> Man City agreed £116m (up to £130m) -> 875467 Anderson .87.
- WC: France 4-1 Norway (Dembele hat-trick, 4 goals; France top I, Norway 2nd); Australia 0-0 Paraguay (Aus through). Deschamps leaves after WC.
  -> 201629 Golden Boot: Messi .33 Mbappe .24 Dembele .12 Haaland .10 Kane .08; 581542 Golden Ball add Dembele .09.
- Searches used today: 1 (1,843 left).

## 2026-06-27 (day 4)
- US–Iran: Iranian drone hit ships in Hormuz (Ever Lovely Jun 25, Kiku Jun 27); US struck Iran Jun 26 & 27 (Sirik, Qeshm; minelayer capabilities); IRGC hit US sites in Gulf. MoU (Jun 17) ceasefire strained. ~80 mines remain in Hormuz TSS; Pakistan coordinating nav warnings; Iran must clear mines within 30 days per MoU. Israel–Lebanon–US framework agreement signed Jun 26.
- Europe deadly heat wave (relevant: wildfire emergency 149811, nuclear drought 683823/772343).
- Women's T20: Ireland beat WI (WI semi hopes dented) -> 258607 Aus .53 Eng .25 Ind .09 SA .08 WI .03.
- MotoGP Assen: Aprilia dominant (Martin pole, Bezzecchi leads champ by 9 over Martin; Trackhouse Fernandez/Ogura 1-2 sprint); Marquez 7th on grid, 6th sprint. -> revisit 897546 (German GP, Marquez .47) after Assen race Jun 28.
- WC Jun 26-27: Spain 1-0 Uruguay (Spain top H), England beat Panama (top L), Senegal 5-0 Iraq, Cape Verde into R32 v Argentina. TODO Jun 28: full bracket + wc_sim rerun.
- Searches: 0 today (1,843 left).

## 2026-06-28 (day 5)
- WC R32 bracket set -> new scripts/wc_ko.py + wc_boot.py; updated 199448, 457239, 935518, 439898, 592683, 241292, 201629 (Messi .52), 581542 (Messi .28).
- Women's T20: India out; SFs Aus v WI (Jun 30), Eng v SA (Jul 2) -> 258607 Aus .52 Eng .30 SA .12 WI .05; 799550 Wyatt-Hodge .17 (top scorer) etc.
- F1 Austria: Russell won, Verstappen 2nd, Antonelli 3rd; standings Ant 171 Rus 131 Ham 125 -> 556116 Russell .62 Ham .30; 747581 British GP Ant .30 Rus .29 Ver .12 Ham .11 Lec .06; added Verstappen to later races.
- Stokes retiring (after NZ series) -> 971366 replace Stokes w/ Fisher.
- Res-date heuristic: lowered None in 709570 (ASEAN .45), 903565, 423956, 880660, 339902, 712131.
- Searches: 1 (1,842 left).

## 2026-06-29 (day 6)
- Portland acquired Ja Morant (less likely Brown dest); Celtics asking ~4 firsts -> 344207 Hou .27 Atl .17 Cle .11 NOP .06 Por .04.
- India lost T20I series 2-0 in Ireland -> 562262 England .55 India .43 (5 T20Is from Jul 1).
- Wimbledon D1: Sinner beat Kecmanovic in 5 (fall, bloodied); Draper & Raducanu withdrew. Sabalenka through.
- WC R32: Brazil beat Japan (Martinelli 90+); Canada beat SA. Ireland v Israel NL match in Serbia (neutral).
- Searches: 0 (1,842 left).

## 2026-06-30 (day 7)
- Light article day (53). Paraguay beat Germany on pens (1-1) in R32; Brazil beat Japan. wc_ko RESULTS updated (M73 Canada, M76 Brazil, M74 Paraguay) -> updated 199448 (France .48), 935518, 439898, 592683, 241292 (France .195).
- US heat wave; Colorado wildfire smoke.

## 2026-07-01 (day 8) — first resolutions
- RESOLVED: 344207 JB -> 76ers (miss, -0.12); 619176 Palestinian FA -> September (hit, +0.52); 659176 Russian official -> Dmitry Medvedev (miss, -0.28).
- Cyclospora: Michigan outbreak 174 cases Jun 22-30 -> 633052 Michigan .78.
- LeBron leaving Lakers (GSW/CLE/MIA pitches) -> 981188 GSW .36 CLE .26 MIA .12 SAS .05 DEN .05.
- WC R32: Morocco beat NED (pens), Norway beat CIV 2-1, France 3-0 SWE (Mbappe 6 = Messi 6), MEX 2-0 ECU, ENG 2-1 DRC (Kane 5), Haaland 5. Updated WC Qs; Golden Boot Mbappe .36 Messi .33 Kane .12 Haaland .10.
- Warsh (Jul 1): inflation risks down; "good family fight" at July meeting -> supports hold+hawkish dissents (942650 unchanged).
- Ebola spread to Haut-Uele -> 490094 tweak. Forest hired Glasner -> 72132, 5814 tweaks. Serhii K. indicted (Nord Stream).
- England-India 1st T20I abandoned (rain).

## 2026-07-02 (day 9)
- Women's T20: Aus beat WI by 8 wkts (SF1); Perry quad scare; Eng v SA SF2 Jul 2 -> 258607 Aus .60 Eng .28 SA .11; 799550 Gardner .18 Wyatt-Hodge .13 Perry .10 Mooney .09 Litchfield .05.
- WC R32: USA 2-0 BIH (Balogun red), Belgium 3-2 Senegal aet, Spain 3-0 Austria (Oyarzabal 2 -> 5). Updated 935518, 592683, 241292, 201629.
- Fixed noisy keywords (Bavi, Noul, Dolphin, by-election).

## 2026-07-03 (day 10)
- Moldova PM Munteanu resigned Jul 3; Sandu consultations next week (no names) -> 76066 spread (Popsoi .12 Spatari .11 Popescu .10 Gherasimov .10 Gavrilita .07).
- Women's T20 final Aus v Eng (Lord's Jul 5); Eng beat SA by 40 (Sciver-Brunt 75, Knight 58) -> 258607 Aus .58 Eng .42; 799550 Gardner .20 Wyatt-Hodge .15 Sciver-Brunt .13 Mooney .12 Perry .09.
- Silverstone sprint weekend; Hamilton fastest FP1 (Antonelli 2, Leclerc 3, Russell 4) -> 747581 Ant .28 Ham .20 Rus .20 Lec .10 Ver .08; 556116 Rus .55 Ham .37.
- WC R32: Portugal beat Croatia (R16 v Spain), Switzerland 2-0 Algeria, Egypt beat Australia (pens). Remaining: ARG-CPV, COL-GHA (Jul 3).
- Wildfires: Portugal (Vouzela), France (Pyrenees-Orientales, 3,000 evacuated), Spain (Costa Brava) -> 149811 N.Macedonia .40 Portugal .10.
- Tunisia WC players clenbuterol (contaminated Mexican meat).

## 2026-07-04 (day 11)
- RESOLVED: 177324 Trey Alexander -> Utah Jazz (miss -0.20); 633052 cyclospora -> Michigan (+0.93 final; TW +8).
- Bavi super typhoon: Marianas ~Jul 6, then W-WNW toward Taiwan (closest Jul 10-11; models diverge Ryukyu vs Taiwan) -> 66613 Fujian .45 Zhejiang .30; 446236 Fujian .38 Zhejiang .36.
- British GP: Antonelli won sprint + pole (Leclerc P2, Hamilton P3, Russell P4) -> 747581 Ant .45; standings Ant +43 over Rus, +47 over Ham -> 556116 Rus .50 Ham .45.
- Wimbledon W: Swiatek (Eala), Rybakina (Mertens), Andreeva (R2 Krejcikova), Anisimova (Keys) out -> 846335 Sabalenka .30 Keys .10 Bencic .08 Pegula .07 Noskova .07.
- Eng-Ind T20: M1 abandoned, Eng won M2 (Bethell 76*) -> 562262 Eng .76 (res Jul 9 hint).
- WC Jul 3-4: ARG beat CPV 3-2 aet (Messi 7 goals), COL 1-0 GHA; R16: Morocco 3-0 Canada (QF Boston v FRA/PAR winner). Messi GB .50.

## 2026-07-05 (day 12)
- RESOLVED: 258607 -> Australia (+), 747581 British GP -> Leclerc (Antonelli .45 from pole; small +), 799550 POT -> Beth Mooney (.12).
- Wimbledon W: Osaka beat Sabalenka; QFs Osaka-Muchova, Pegula-Gauff; bottom R16 Mon (Keys-Noskova, Paolini-Eala, Kostyuk-Krueger, Bouzkova-Mertens) -> 846335 Gauff .14 Pegula .14 Muchova .13 Osaka .13 Keys .10.
- Wimbledon M: Sinner (beat Mochizuki) & Djokovic (beat Safiullin) in QFs; FAA through.
- WC R16: France 1-0 Paraguay (Mbappe pen; Mbappe 7G/2A leads Messi 7G/0A on assists) -> Boston QF France v Morocco (Jul 9). Updated 199448 (Fra .68), 935518, 241292 (Fra .27), 592683, 201629 (Mbappe .50 Messi .35), 581542.
- wc_boot.py now has assists tiebreak weights (TB dict).
- Norway 2-1 Brazil (Haaland 7G; QF Miami Jul 11 v MEX/ENG). McMorrow suspended MI Senate campaign -> 883794 El-Sayed .58 Stevens .41. Babar Azam Pakistan Test captain again.

## 2026-07-06 (day 13)
- Bavi hit Rota (Jul 6); CMA: brush N Taiwan Jul 10-11, landfall Zhejiang-Fujian border Jul 11-12 or direct Zhejiang -> 66613 Zhe .57 Fuj .36; 446236 Zhe .62 Fuj .28. (Chinese-language search very useful.)
- WC R16: England 3-2 Mexico (10 men, Kane pen -> 6), Spain beat Portugal (late; Ronaldo's last WC). Remaining R16: USA-BEL (Jul 6), ARG-EGY, SUI-COL (Jul 7). Updated 935518 (Fra .42 Esp .39), 439898 (Eng .37 Arg .30 Nor .17), 592683, 241292 (Fra .26 Esp .225 Eng .19), 201629.
- Samson dropped from Zimbabwe T20I squad -> 131869 Abhishek .30 Sooryavanshi .28.
- Restore Britain rising vs Reform (supports Lowe for 754639). Maine Dems call on Platner to drop out (720892 context). Hamas announced Gaza govt resignation. Khamenei body in Qom Jul 7.

## 2026-07-07 (day 14)
- RESOLVED: 263626 trade deficit -> Vietnam (+0.10); 754639 UK leader -> Nigel Farage (miss -0.29; I had Lowe .60).
- Moldova: Osmochescu (deputy PM, ex-IFC) acting PM from Jul 8 -> 76066 Osmochescu .25 + PAS names.
- Eng 2-0 India after 3rd T20I (India biggest T20I defeat) -> 562262 Eng .88.
- Bavi CMA Jul 7: landfall most likely central-south Zhejiang to N Fujian night of Jul 11 (or N Zhejiang / pass north) -> 66613 Zhe .62 Fuj .30; 446236 Zhe .65 Fuj .25 Sha .07.
- Wimbledon: Sinner SF (beat Struff); W SF1 Gauff v Muchova (beat Pegula/Osaka); QFs Kostyuk-Paolini, Noskova-Mertens; M QFs Zverev-Fritz (Fritz 10-5 H2H), Cobolli-Fery, Djokovic-FAA. Updated 846335, 742225, 985440.
- WC R16 complete: BEL 4-1 USA, ARG 3-2 EGY (Messi 8G), SUI beat COL (pens). QFs: FRA-MAR (Bos Jul 9), ESP-BEL (LA Jul 10), ENG-NOR (Mia Jul 11), ARG-SUI (KC Jul 11). Updated all WC Qs.

## 2026-07-08 (day 15)
- RESOLVED: 213487 Dugan -> Monetary fine (miss-ish -0.24); 76066 Moldova -> Vasile Tofan (miss -0.09).
- Wimbledon SFs: M Sinner v Djokovic (Djokovic beat FAA in 5h), Zverev v Fery (UK wildcard; Zverev beat Fritz, Fery beat Cobolli). W Gauff v Muchova, Kostyuk v Noskova. First-SF order unknown: Brit SFs (Murray) historically 2nd -> ~55% Sinner-Djokovic first.
- SK hynix ADR multiple times oversubscribed -> 279946 SK Hynix .86.
- Emmy noms (Jul 8): Drama: Diplomat, Gilded Age, Knight of Seven Kingdoms, Paradise, The Pitt (25), Pluribus (18), Slow Horses, Your Friends & Neighbors. Comedy: Abbott, The Bear, Hacks (24), Margo's Got Money Troubles, Nobody Wants This, OMITB, Shrinking, Widow's Bay (19). Lead Actress Drama: Coon, Infiniti, Russell, Seehorn, Zendaya. Updated 873349, 216881, 440552.
- Fed minutes: some officials considered June hike (supports hawkish dissents 942650). Germany offers to minesweep Hormuz. Trump struck Iran again (~Jul 8).
- Calibration review (after misses): trimmed 764544 (Central Sulawesi .75->.45; res-date Aug15<Aug17 hints new deadly quake), 882554 (Electoral .72->.65), 623398 (Como .55->.45), 126882 (Aerial bombs .52->.47). Pattern: generated questions often resolve to SURPRISING names (Farage, Medvedev, 76ers, Utah, Tofan, fine) -> keep judgment-based tops <=0.4-0.45 and diversify.
- Jul 9: Bavi landfall forecast Fuqing (FJ) to Wenling (ZJ) evening Jul 11; national IV response for ZJ+FJ. W final Muchova v Noskova (Jul 11). M SF order: Fery-Zverev first (1:30pm), then Sinner-Djokovic -> 985440 Zverev .78 Fery .21. France 2-0 Morocco (Mbappe 8G = Messi 8G; Mbappe ankle knock).

## 2026-07-10 (day 17)
- RESOLVED: 446236 -> Zhejiang (+); 985440 -> Zverev (+). TW +291.7.
- Bavi: Reuters Jul 10 landfall ~Wenzhou (Zhejiang) late Sat/early Sun; 17k evacuated in ZJ -> 66613 Zhe .72.
- Wimbledon: Sinner beat Djokovic; Zverev beat Fery -> final Sinner v Zverev (Jul 12) -> 742225 Sinner .72.
- WC: Spain beat Belgium (Merino) -> SF1 France v Spain (Jul 14). Updated 935518 (.52/.48), 592683, 241292.
- MLB ASG: Ohtani out (knee) -> 607314 Schwarber .06 etc. Scheffler missed Scottish Open cut; McIlroy co-leads.
- MotoGP Assen (Jun 28): Ogura won, R.Fernandez 2, Martin 3 (Aprilia sweep); Bezzecchi crashed; Marquez 6th; Martin leads. -> 897546 Marquez .30, 259947 Aprilia up.
- Jul 11: Marquez pole+sprint win Sachsenring -> 897546 Marquez .56. Argentina beat Switzerland (KC QF resolved). ENG-NOR result pending.
- Jul 11: NK Premier Pak Thae Song visited Beijing Jul 10-12 (treaty 65th; met Xi, Li Qiang, Cai Qi) -> 666563 tweak (+Liu Haixing). TN-9: Taylor endorsed by Jim Jordan -> 362674 Taylor .78. No news on Hochul NY data-centre bill.

## 2026-07-12 (day 19)
- RESOLVED: 742225 -> Sinner (+), 897546 -> Marc Marquez (+). TW +551.7.
- WC QFs done: England 2-1 Norway aet (Bellingham 2; now 6G), Argentina 3-1 Switzerland aet (Messi assist; 8G 1A). SFs: France v Spain (Dallas Jul 14), Argentina v England (Atlanta Jul 15). GB: Mbappe 8G/2A, Messi 8G/1A, Haaland 7 (out), Kane 6, Bellingham 6.
- FIXED BUG in scripts/wc_boot.py (was double-counting already-played matches). Corrected GB: Mbappe .60 Messi .36 -> submitted Mbappe .56 (ankle) Messi .38.
- Updated 201629, 581542 (Messi .30 Mbappe .29 Bellingham .14), 439898 (Arg .51 Eng .49), 592683, 241292.
- McGregor injured (knee) at UFC 329. Ryu Hae-ran 60 at Evian.
- TdF: Merlier won st7 & st8; Kooij st5, Pedersen st4, VdP st9; Pogacar yellow -> 24813 Merlier .30.
- Rogers: Arsenal close on personal terms; Villa ask £130m (could rival Anderson record) -> 26225 Arsenal .76; 875467 Anderson .70 Rogers .15.
- Bruno Guimaraes: verbally agreed Arsenal terms; Arsenal formal bid coming (NUFC £75-90m) -> 108618 Arsenal .62. Tonali sold to Spurs £100m (< Anderson £116m).
- Transfer re-research agent (36 searches): Diomande -> PSG .70 (verbal terms); Enzo: Real ruled out -> City .30; Barcola -> Liverpool .45; Ferran -> PSG .68 (terms to 2031); Hadjam -> Como .82 (verbal agreement); Watkins -> Fenerbahce .45; Bouaddi City .23 Arsenal .18; Konsa Arsenal .27; Marmoush Atletico .25; Salah Al-Ittihad .30 Al-Ahli .27; Rodri summer move unlikely (total .21); Savinho Spurs .72; E. Martinez Juve .72; Jesus Everton .27; Vozinha Inter Miami .38; Fabinho spread.
- 875467: Anderson .62, Rogers .14, Barcola .12.
- Sweep agent Jul 17-31 Qs (41 searches): ECB removed McCullum Jul 12 -> 988210 Flower .47; LeBron -> CLE .46 MIA .15 PHI .15 GSW .11 (Kalshi ~50% CLE); 605397 Spain .55 (Trump ordered trade cut off at NATO Jul 8; South Korea .12); 415011 Gonzalez-Olaechea .40 (leaked list); 872064 Himachal .30 Maharashtra .17; 149811 N.Mac .42 (decision date may be Jun 30!) Portugal .18; 126882 bombs .42 rockets .40; 45561 Eng .52 Can .42; 918398 Istanbul .27 Portimao .26 Bahrain .18; 942650 hike odds fell to 20-25% after +57k June jobs; 683823 Romania .55 (Cernavoda thresholds published).
- MIDDLE EAST ESCALATION ~Jul 11-12: Iran closed Hormuz; US struck Iran again; missiles/drones at Bahrain, Qatar, UAE. TODO: sweep August Middle East Qs (817209, 246629, 916964, 56802, 461239, 508136, 790870, 101639).
- Searches left ~1,738.

## 2026-07-13 (day 20)
- RESOLVED: 362674 TN-9 -> Brent Taylor (+0.94). TW +648.7.
- Sarah Khalifa trial adjourned again Jul 9 (forensic testimony; no verdict).
- Sweep Aug 1-15 (42 searches): 481741 July .55 (WH 2,000 arrests/day standard); 687277 Leisure & hospitality .27; 311120 Qatar .42 Morocco .16 USA .13; 883794 El-Sayed .50 Stevens .49 (Politico poll 41-42); 805635 Braves .20 Dodgers .18 Rays .12; 517488 Gtech .45 Stamford Bridge .17; 246629 Bahrain .36 UAE .22 Kuwait .20; 685197 Poonch div .35 (polling still single day Jul 27 — phases TBD); 882554 Electoral .60 (Venezuela twin quakes Jun 24 killed 4,561; talks frozen). US reimposed naval blockade of Iran Jul 13; Iran struck Kuwait, Bahrain, Qatar, Oman, Jordan Jul 8-12.
- Searches left ~1,695.

## 2026-07-14 (day 21)
- RESOLVED: 607314 MLB ASG MVP -> Cody Bellinger (unlisted); 666563 -> Wang Huning (.05); 803035 -> New York (+0.97); 935518 SF1 -> Spain (+0.46). TW +768.6.
- WC SF1: Spain 2-0 France (Oyarzabal pen 22', Porro 58'). Final Jul 19 Spain v ARG/ENG; France in 3rd place match Jul 18. -> 241292 Spain .53; 592683 France .56; 201629 Messi .50 Mbappe .44; 581542 Yamal .28 Messi .28 Bellingham .16.
- Pogacar won TdF stage 10 (Bastille Day). Spain Almeria wildfire Jul 9 killed 13.
- Final referee: SF refs Barton (FRA-ESP) & Elfath (ARG-ENG); remaining pool listed; English/Argentine refs excluded -> 524604 Faghani .50.

## 2026-07-15 (day 22)
- RESOLVED: 24813 TdF st11 -> Waerenskjold (.06); 439898 SF2 -> Argentina. TW +800.5.
- Argentina 2-1 England (Gordon; Enzo 85', Lautaro 90+2'). Final Spain v Argentina (Jul 19 NJ); 3rd place France v England (Jul 18 Miami).
- GB: Mbappe 8G/2A (one game: 3rd place) vs Messi 8G (final). Poisson calc -> Mbappe .64 Messi .33. Golden Ball Messi .40 Yamal .28. Champion Spain .55. 3rd France .55.

## 2026-07-16 (day 23)
- RESOLVED: 524604 final referee -> Slavko Vincic (+0.12).
- Ukraine: Zelensky dismissed DefMin Fedorov Jul 15 after feud with Syrskyi (Zelensky backed Syrskyi); protests; Khmara acting DefMin; PM Koretskyi. Fedorov says Zelensky hasn't fully chosen side. 249565 unchanged (Budanov .24 ...).
- Open R1: Brown & Im 66, DeChambeau 67, Scheffler 68 -> 32938 tweak. Kerr attempting mile WR at London Jul 18 (new Brooks shoes).

## 2026-07-17 (day 24)
- RESOLVED: 329053 -> APPLE (Nvidia .88: -0.72 big miss); 32938 -> Lucas Herbert (unlisted); 425213 -> Nuseirat refugee camp (.07). TW +741.5.
- Status-quo review: 120116 Harald V .60 / Haakon VIII .38 (accession clause hint); 846721 Bonilla .72 Rocha .12; 729308 Nike .55 Adidas .15; 906651 El Guerrouj .78 Kerr .17. TODO: research 508136 Mayun control (could change w/ Red Sea escalation).
- F1 after British GP (Leclerc won; Antonelli DNS-score): Ant 179, Rus 154, Ham 147. Spa FP1: Verstappen, Hamilton, Leclerc. -> 556116 Rus .60 Ham .36.

## 2026-07-18 (day 25)
- RESOLVED: 26225 Rogers -> Chelsea £117m (miss -0.41); 592683 3rd -> England (+0.39); 674079 -> du Plessis (+0.85); 906651 mile WR -> Josh Kerr 3:42.66 (miss -0.30). TW +773.3.
- 875467: Anderson .45 vs Rogers .38 (Rogers £117m > Anderson £116m base but Anderson up to £130m).
- Newsworthiness trims: Norway Haakon VIII .50/Harald .48; Sinaloa Bonilla .60; Mbappe Nike .45; Ledecky .62; Yu Zidi .70; Ohashi .62; transfers w/ reported deals trimmed to ~.6; primaries trimmed slightly.
- 3rd place: England 6-4 France (Saka hat-trick); Mbappe 2 -> 10 goals (WC all-time record 22). -> 201629 Mbappe .95; 581542 Messi .38 Yamal .22 Mbappe .15.

## 2026-07-19 (day 26)
- RESOLVED: 201629 GB -> Mbappe (+1.00); 241292 WC -> Spain (+0.59); 556116 F1 2nd after BEL -> Hamilton (.36, +0.23); 581542 Golden Ball -> Rodri (.07, -0.08); 927657 Syria NSB -> Anas Khattab (+0.45). TW +918.1 (44 resolved).
- Belgian GP: Antonelli won, Leclerc 2nd, Verstappen 3rd, Hamilton 4th (5s pen), Russell DNF lap 1 (collision w/ Hamilton). Standings: Antonelli leads Hamilton by 45.
- Updates: 249565 Drapatyi .48 Hnatov .15 (FT: Zelensky interviewing C-in-C candidates, met Drapatyi/Horbatiuk/Apostol Jul 19); 594916 Ant .33; 475441 Ant .25; 442417 Guangdong .42 (Haishen dissipated; SCS disturbances); 872064 HP .25 J&K .24 MH .20 (Poonch floods 18 dead); 131869 Abhishek .28 Sooryavanshi .20 Iyer .14; 149811 N.Mac .38 Spain .13; 605397 Spain .45 S.Korea .20 (Coupang 'discrimination'); 988210 FLOWER OUT -> Langer .40 Fleming .24 Trott .10; 339902 Iraq .44 Yemen .34 None .10 (war re-escalated, Houthis entered war Jul 14).
- LESSON: scan --max 2 hid the Flower-withdrawal news on 07-17; broadened keywords for 988210/249565/442417/415011. Read more hits for questions due within 10 days.
- TODO: sweep Aug Middle East Qs (817209, 916964, 461239, 508136, 246629, 790870, 101639, 56802) given war re-escalation.
- Searches left ~1,656.

## 2026-07-20 (day 27)
- RESOLVED: 605397 Section 338 -> Canada (.06, -0.13). TW 923.1.
- Updates: 249565 Drapatyi .47 Biletsky .11 (Zelensky met 6 candidates Jul 20; protest deadline Jul 24); 981188 CLE .46 MIA .18 PHI .17 (Charania: no timetable, East focus); 107175 Saudi .36 (Houthis declared maritime embargo on Saudi Jul 20); 683823 Romania .68 (Danube lowest in 30 yrs).
- Sweep agents (43 searches) updated 23 Qs due Jul 29-Aug 12: 604201 Oman .88 (Reuters Jul 17 spill off Hallaniyat); 772343 Romania .66; 946660 Life .36 Death .30 (trial adjourned to Aug 4); 443143 Pegula .20 (top seed DC); 356778 Fritz/Shelton/FAA ~.12; 449245 Pathirage .38; 970163 Pathirage .27; 920782 WI .52; 72574 Fiorentina .48; 202511 Russia .36 China .24; 709570 ASEAN .45 None .35; 422179 Next Vision .38; 992842 Cam Young .12; 737715 composite prefecture labels (Taizhou .15, Wenzhou .12).
- Searches left ~1,610.

## 2026-07-21 (day 28)
- RESOLVED: 249565 -> Drapatyi (+0.70); 442417 -> Guangdong (+0.60). TW 989.2.
- Updates: 872064 HP .62 (HP minister: 66 July rain deaths, official).
- Sweep agents (57 searches) updated 34 Qs due Aug 13-Sep 5: 541001 Nashville .86; 874244 Witkoff .64; 40115 Makhachev .74; 113668 Dern .60; 777991 G.Walsh .43 Douglass .36; 855662 Cincinnati .48 US Open .42; 591807 Renard .27 (Queiroz quit Jul 5); 163032 Beye .30 Vieira .20 (Thiaw fired Jul 11); 720221 Elijah .47 Mills .46; 673971 Texas .45; 224345 Indonesia .65; 565579 Net exports .60; 970733 Ferrara .30 Overton .27 Vacirca .27; 964047 Netherlands .38; 461239 Oman .25; 903529 Pennsylvania .30; 279786 Arsenal .52; 616886 Morocco .27 Nigeria .26; 921981 Erdogan .45.
- NOTE: Lindsey Graham died Jul 11 (SC special primary Aug 11, runoff Aug 25). record.py patched for atomic writes after concurrent-write corruption (verified fc == log).
- Searches left ~1,548.

## 2026-07-22 (day 29)
- RESOLVED: 872064 -> Assam (.03, -0.35). TW 988.9.
- Updates: 981188 MIAMI .55 (Heat accidentally posted 'LeBron James Introductory Press Conference' Jul 27; BetOnline Miami fav); 339902 Yemen .45 Iraq .33 (Houthis struck Saudi tankers; Bab al-Mandeb effectively shut); 107175 Saudi .38 US .24; 238968 Grynspan .42 Grossi .36 (first straw poll Jul 30, 6 candidates); 594916 Ant .31 Ham/Lec/Rus .14.

## 2026-07-23 (day 30)
- RESOLVED: 131869 -> Sooryavanshi (+0.24); 149811 -> Spain (+0.09). TW 1010.0.
- Updates: 339902 Yemen .60 (Trump: 'major military punishment' for Houthis); 107175 Saudi .33 US .30; 942650 trio .18 / full-hike list .18 (FedWatch July hike 38%); 617889 Colo-Colo .30 Inter Miami .12 (Colo-Colo offer then Mele pivot, Mele collapsed Jul 22). LeBron: DraftKings Miami -200, CLE +225 (kept MIA .55).
- LESSON: local corpus is English-only; for transfers near resolution search in Spanish/Portuguese/etc. (missed Vozinha-Colo-Colo saga for 5 days).

## 2026-07-24 (day 31)
- RESOLVED: 126882 Aerial bombs (+0.50); 45561 Canada (+0.39); 617889 Colo-Colo (+0.49); 981188 76ers (-0.18). TW 1071.0.
- Updates: 918398 Sepang .30 Portimao .30 (Malaysia feasibility study); 475441 Lec .31 Ham .29 / 594916 Lec .30 Ham .28 (Ferrari dominated FP1/FP2); 696503 PSG .42 Real .30 (Real €100m bid); 243962 Rodri Real .45 (was .10); 222955 Bouaddi City .40.
- Transfer sweep agent (26 searches): 810891 Salah BESIKTAS .72 (terms agreed, agent fee cut Jul 24); 875467 Rogers .76 (Al Jazeera: £117m surpasses Anderson £116m); 108618 Bruno Arsenal .70; 459381 Spence Inter .40 Everton .25; 225772 Savinho Spurs .85; 623398 Hadjam Como .85; 162316 Barcola Liverpool .52; 450664 Martinez Juve .72; 918938 Ferran PSG .66; 160265 Watkins Fener .50; 770763 Konsa Arsenal .50; 248237 Baleba Utd .26 Gala .19.
- Searches left ~1,510.

## 2026-07-25 (day 32)
- RESOLVED: 475441 FP3 -> Norris (.10); 918398 -> Sepang (.30). TW 1048.2.
- Updates: 594916 Norris .36 Leclerc .28 (Norris pole; Ham/Ant 3-place pens); 415011 Carlos Pareja .45 (Leiva leaked cabinet; PCM Galarreta); 179451 Alzarri out -> Seales .22 Shamar .22 Roach .14 Warrican .12 Bishop .06.

## 2026-07-26 (day 33)
- RESOLVED: 594916 Hungary -> Norris (+0.49); 696503 Diomande -> Real Madrid (+0.32; TW -47.9). TW 988.4.
- Updates: F1 future races rebalanced (669987 Dutch Ant .20 Nor .17; 668636 Monza Ant .25; 48458 Madrid Ant .22; 447470 Baku Ant .24); 339902 None .45 Yemen .30 Iraq .17 (US paused strikes Jul 24-26); 107175 Saudi .40.

## 2026-07-27 (day 34)
- RESOLVED: 179451 -> Justin Greaves (unlisted); 415011 -> Carlos Espa (.06). TW 962.3.
- Updates: 988210 Fleming .32 Dawson .27 Trott .13 (Langer NOT in running; Trescothick interim); 971524 Thailand .45 Malaysia .38; 449245 Pathirage .33 Chopra .20; 970163 Pathirage .25 Chopra .20.

## 2026-07-28 (day 35)
- RESOLVED: 339902 -> Iraq (+0.02 last day; TW +58). TW 1020.5.
- Updates: 920782 WI .58 (won 1st Test by 90); 883794 Stevens .55 El-Sayed .44 (Detroit News 48-41); 683823 Romania .65 Bulgaria .10.

## 2026-07-29 (day 36)
- RESOLVED: 107175 Saudi (+0.59); 942650 H,K,L (+0.28); 971524 Malaysia (+0.41); 988210 Fleming (+0.44). TW 1103.2.
- Updates: 683823 Romania .95 (both Cernavoda reactors shut by Jul 30); 772343 Romania .35 Hungary .25 Bulgaria .22 (window Aug 1-13 after Romania's Jul 29 announcement).

## 2026-07-30 (day 37)
- RESOLVED: 238968 Grynspan (+0.52); 970163 Pathirage (+0.36); 683823 -> HUNGARY (Romania .95: -0.88). TW 1179.1.
- Updates: 772343 Romania .45 Hungary .35 (Romania 2nd reactor stayed online Jul 30; Paks full shutdown Jul 30-Aug 2); 449245 Pathirage .35 Peters .20 Chopra .17.

## 2026-07-31 (day 38)
- RESOLVED: 108618 Arsenal (+0.91); 449245 Pathirage (+0.50). TW 1269.0.
- Updates: 883794 El-Sayed .60 (Emerson +15); 737715 Wenzhou .25 Taizhou .18 Ningde .14 (Dolphin EC/GFS S.Zhejiang/N.Fujian Aug 8-9); 805635 Rays .17 Dodgers .17.
- Updates: 992842 Young .20 Cantlay .16 (R2 co-leaders); 356778 Fritz .26; 443143 Pegula .36 Osaka .20.

## 2026-08-01 (day 39)
- RESOLVED: 805635 Skubal -> Dodgers (+0.24). TW 1298.1.
- Updates: 992842 Riley .33 Brennan .20 (R3 leaders); 443143 Pegula .58 Eala .42 (final); 356778 Fritz .37 Jodar .23 Nakashima .22 Tabilo .17.
- 810891 Salah -> TRABZONSPOR .55 (Besiktas shelved Jul 27; Trabzonspor hijack Aug 1). LESSON reinforced: re-check transfer Qs in local language 2-3 days before resolution.

## 2026-08-02 (day 40)
- RESOLVED: 481741 July (+0.72); 992842 Thorbjornsen (unlisted). TW 1324.1.
- Updates: 685197 Poonch div .86 (EC schedule confirmed); 243962 Rodri Real .78 (club talks, personal terms); 222955 Bouaddi City .75.

## 2026-08-03 (day 41) [next_day returned a parse error but the sim advanced]
- RESOLVED: 356778 Fritz (.37); 443143 Eala (.42); 709570 ICRC (.04).
- Updates: 817209 Oman .62 (Hormuz compromise: exit via Omani side; Oman agreed); 810891 Trabzonspor .75 (offer accepted per Turkish journalists; signing Aug 5).

## 2026-08-04 (day 42)
- RESOLVED: 33659 Edinburgh (unlisted); 576510 Mahdi Adam (unlisted); 716751 Hamilton (+0.92); 810891 Trabzonspor (+0.78); 817209 Oman (+0.72); 946660 Death penalty (+0.36). TW 1499.1.
- Updates: 737715 Ningbo .20 Taizhou .14 Shanghai .12 Zhoushan .10 (CMA: landfall ~Aug 9 Yangtze estuary-Zhejiang or recurve north Aug 10-11). Ferran: Flick 'depends on Ferran', PSG linked (kept .66).

## 2026-08-05 (day 43)
- RESOLVED: 883794 El-Sayed (+0.69); 920782 Pakistan (+0.16). TW 1592.5.
- Updates: 772343 Romania .55 Hungary .35 (Romania Unit 2 expected shut ~Aug 10-13; Paks shut Aug 2). Parker suspension lifted (723378 details pending).

## 2026-08-06 (day 44)
- RESOLVED: 202511 Thailand (.13); 243962 Rodri -> BARCELONA (.02!); 723378 'His nutritionist' (unlisted wording); 874628 TN-5 -> Hatcher (upset). TW 1562.7.
- HIJACK RULE applied: 918938 PSG .62; 225772 Spurs .62; 222955 City .62; 623398 Como .68; 450664 Juve .60; 875467 Rogers .70.

## 2026-08-07 (day 45)
- RESOLVED: 685197 -> 'Bagh and Haveli' (-0.74; Poonch/Sudhnoti postponed); 687277 Government (+0.14). TW 1553.7.
- Updates: 737715 Wenzhou .30 Ningde .25 (CMA: landfall Aug 9-10 Zhejiang-N.Fujian); 259947 Martin .22 M.Marquez .18 Ogura .14.

## 2026-08-08 (day 46)
- RESOLVED: 251083 Bristol (+0.11); 72574 West Ham (unlisted); 737715 Yuhuan (composite label failed). TW 1535.4.
- Updates: label fixes 996188 'YUUKI', 25611 split Bajinya/Brown; 259947 Martin .33 (pole) Ogura .15.

## 2026-08-09 (day 47)
- RESOLVED: 259947 Raul Fernandez (.12). TW 1531.9.
- Updates: 229258 Rybakina/Gauff .20 Swiatek .18 (Sabalenka/Pegula out); 628038 Mor-Alg .25; 616886 Morocco .33 Algeria .19; 754377 Phase One .78 (Miami lost to Monterrey).
- Sweep agents (61 searches) refreshed 44 Qs due Aug 19-Sep 15 (Emmys: The Pitt .80, Seehorn .77, Hacks .56; 880660 Mendonca .72; 518392 London .63; 261941 Yan Ziyi .62; 408930 Shelton .41 Fritz .35; 891014 Sinner; etc.).
- Tennis: Alcaraz withdrew Cincy (Aug 4); Sinner withdrew Cincy (Aug 9, knee) -> 855662 US Open .55; 891014 Sinner .40; 277746/418046 removed Sinner/Alcaraz.
- Searches left ~1,412.

## 2026-08-10 (day 48)
- RESOLVED: 112235 Colombia (+0.23). TW 1554.7.
- Updates: 628038 Mor-Alg .34 Mor-Mal .28; 616886 Morocco .38 (Nigeria out); 772343 Romania .65 (Unit 2 shutdown expected ~Aug 10-11).

## 2026-08-11 (day 49)
- RESOLVED: 49405 Marques (+0.97); 517488 Stamford Bridge (+0.23); 772343 Romania (+0.80); 918938 PSG (+0.85). TW 1796.8.
- Updates: 229258 Swiatek .27 Gauff .20 Rybakina .18; 459381 Inter .70 (Spence deal agreed); 882554 Judicial .47 Electoral .43.

## 2026-08-12 (day 50)
- RESOLVED: 422179 NextVision (+0.59); 459381 Inter (+0.91); 604201 Oman (+0.98); 628038 Cameroon-Malawi (.16); 754377 'Group stage' (Phase One not credited, -0.62); 882554 Judiciary (+0.53). TW 1853.6.
- Updates: synonym hedges 565579 External demand .45/Net exports .15; 408396 +Green card holder; 916964 +Ansarallah; 229258 Rybakina .29 Svitolina .25 Gauff .24 Swiatek .22 (SFs).

## 2026-08-13 (day 51)
- RESOLVED: 229258 Swiatek (.22); 311120 'Türkiye' ('Turkey' not credited, -0.34). TW 1830.4.
- Updates: Türkiye variants (834692, 174389, 56802); 356699 Mominul .35 Tanzid .30 (Ban 96-1 day 1); 616886 Cameroon .52 Malawi .46 (final).

## 2026-08-14 (day 52)
- RESOLVED: 356699 Tanzid Hasan (.30). TW 1815.8.
- Updates: 764544 East Nusa Tenggara .72 (+NTT .08) (M7.7 Flores Aug 15); 777991 Walsh .40 Douglass .30 Harris .20; 985937 Ledecky .60 Pallister .32.

## 2026-08-15 (day 53)
- RESOLVED: 113668 Dern; 277746 Tirante (unlisted); 40115 Makhachev; 541001 Nashville; 764544 E. Nusa Tenggara; 777991 Douglass; 985937 Pallister. TW 2039.7.
- Updates: 969395 Scheffler .56 (R3 lead by 2); 770763 Konsa Arsenal .15 (Villa refused; Arsenal to Quansah).

## 2026-08-16 (day 54)
- RESOLVED: 279786 Arsenal; 616886 Cameroon; 969395 Scheffler. TW 2110.9.
- Updates: 720221 Elijah .62 Mills .33 (new poll).
- Updates: 163032 Vieira .80 (Senegal coach reports).

## 2026-08-17 (day 55)
- RESOLVED: 163032 Vieira (+0.96); 292136 England (+0.55); 565579 Net exports (+0.01). TW 2268.2.

## 2026-08-18 (day 56) [prior next_day errored; harness synced on 2nd call]
- RESOLVED: 160265 Al Hilal (miss); 246629 UAE (.22); 418046 Nakashima (unlisted); 720221 Elijah (+0.75); 844962 Fedorov (.14); 845687 NIXON (Vindman .83 miss); 970733 Overton (.27); 984539 Shifa (.40). TW 2363.4.
- Updates: 846721 Rocha Moya .50 / Bonilla .47 (return door opened).

## 2026-08-19 (day 57)
- RESOLVED: 770763 Arsenal (.15 after over-cut); 903565 Zhuravlev (.13). TW 2416.0.
- Updates: 248237 Baleba Man Utd .62 (bid + personal terms).
- Updates: 767460 Marmoush Spurs .55 (new double-deal talks); 225772 Savinho Spurs .68.

## 2026-08-20 (day 58)
- RESOLVED: 225772 Spurs (+0.89); 764491 Wahab (+0.86); 846721 Rocha Moya (+0.53); 855662 US Open (+0.60); 916964 Hezbollah (+0.10). TW 2632.9.
- Updates: 260735 Pegula .22 Rybakina .20 Swiatek .18 Gauff .18; 372528 Fritz .20 Cobolli .14 Musetti .13 Paul .13 Fils .12; 874244 Witkoff .55.

## 2026-08-21 (day 59)
- RESOLVED: 248237 Man Utd (+0.85); 767460 Spurs (+0.78). TW 2686.9.
- 08-21 updates: 891014 (Sinner WD) Alcaraz .22; 461239 Lincoln (Duqm stop Jul 7 pre-Aug1; heading home) Singapore .28 US .17 Thailand .12; 669987 Antonelli .28; 260735 Swiatek .38 Pegula .22 Gauff .16 Bejlek .14; 372528 Fils .25 Nakashima .24 Cobolli .23 (Fritz out); 48050 Flash .21/Lightning .18 (Honor label split) Bolt .17; 974146 Fabinho free agent: Flu .10; 720892 Rogers .55; 22056 DS .45 W .43; 354508 Alfred .40 MJW .35; 222955 City .75; 120116 Harald V .87 (hospitalised, regent; undo meta-trim); 277370 UCL .90 (3-0 1st leg); 874244 Witkoff .55 (+Cook); 964047 NL .55; 903529 PA .45 OH .13; 772246 E/V .12 T/Z .10 None .08; 388162 ALLAN -> MAN CITY .77; 623398 Porto .35 Como .30; 450664 (Juve collapsed) Gala .12 Juve .10; 588637 Villa .60; 162316 Liverpool .70; 876325 City .72; 875467 Rogers .48 Barcola .22 Enzo .20; 127253 Everton .35 Napoli .15 Ipswich .10; 20480 Napoli .30 Roma .10; 591807 Queiroz .40 Ofei .30 (Renard -> CIV).
- 08-21: launched 4 sweep subagents (84 stale questions; brief memory/SWEEP_BRIEF_0821.md). record.py now uses flock.
- 08-21 SWEEP done (4 agents, ~150 searches; 61 resubmits). Big moves: 668636 Monza Antonelli grid penalty -> Russell .23; 335239 Raam #2 -> Yoav Segalovitz .65 (Maariv prelim deal); 205592 FAO -> Sugar .65; 408396 LPR .72; 216881 Hacks/Widow's Bay .47/.47; 81247 Berlin -> Die Linke .40 CDU .34 (Wegner withdrew); 935351 Morocco PM Chaouki .30 Baraka .27 El Mansouri .23; 788295 Wael Nawar .68 (only hunger striker); 574553 Tsarukyan .70 (v Ruffy); 425800 Van .49 Pantoja .46; 784475 Agnes Ngetich .40; 996188 label -> 'Yuki Kurihara' .78 (legal name; format = full name); 315568 Alonso .64; 261941 Yan Ziyi .72; 971366 Tongue .23 Robinson .22; 729308 Nike .48 On .15/On Running .08 (Nike deal expired Jul 31); 53266 Bruno .72 (Kalshi 83c); 138739 None .55.
- Searches left after 08-21: ~1,160.

## 2026-08-22 (day 60)
- RESOLVED: 187330 Palou (+0.41); 48050 Tiangong Ultra (-0.02); 720892 Rogers (+0.78); 72132 Leeds (+0.26); 97251 Hull (-0.25); 974146 Trabzonspor (-0.02). TW 2797.8.
- 08-22 updates: 669987 Norris pole -> Norris .40 Russell .26 Antonelli .15; 372528 Fils .55 (final v Nakashima/Tiafoe); 260735 Pegula .50 Gauff .34 Bejlek .15; 222955 City .82 (medical imminent). Mixed doubles field changed (Rybakina/Draper out -> Pegula/Fritz; WCs Serena/Alcaraz, Muchova/Mensik, Navarro/Paul; Shnaider partner TBA) - draw pending. Allan-City meeting Sat; Villa going for Jackson (Watkins->Hilal pending).

## 2026-08-23 (day 61)
- RESOLVED: 22056 DS (+0.51); 222955 City (+0.97); 260735 Gauff (+0.29); 354508 MJW (+0.40); 372528 Fils (+0.70); 669987 Norris (+0.54). TW 2920.2.
- 08-23 updates: 772246 draw -> Fernandez/Tiafoe .45 (R1), Eala/FAA .14, Svitolina/Monfils .13 (QF); 623398 Porto .38 Como .22 Genoa .08. Allan: Palmeiras want EUR40m fixed, City ~35m, Allan played Sun (no deal yet). Swiatek WD mixed (rest, not injury).
- 08-23: 874244 Witkoff .38 (TASS: visit postponed past Aug). 

## 2026-08-24 (day 62)
- RESOLVED: 388162 City (+0.94); 461239 Thailand (+0.11); 623398 BRIGHTON (-0.20, TW -48); 964047 Netherlands (+0.77). TW 2899.5.
- 08-24 updates: 120116 Harald V .80 / Haakon VIII .19 (deteriorated, bacteremia); 921981 Erdogan .38 Modi .30 (Putin hopes to meet Modi at SCO); 20480 Martinelli -> Al-Hilal .50 (final stage). Watkins->Hilal close (then Villa->Jackson). Barcola: LFC bids EUR100m, 115m rejected; GBP111-128m may suffice. Jesus: Everton early talks (GBP20m ask).

## 2026-08-25 (day 63)
- RESOLVED: 277370 Europa League (-0.62); 53266 Bruno (+0.89); 772246 Patten/Siniakova (-0.25); 874244 Ratcliffe (-0.16); 903529 Pennsylvania (+0.67). TW 3000.5.
- 08-25 updates: 588637 Villa .70; 876325 City .80; 875467 Rogers .48 Enzo .30 Barcola .15. Putin-Modi meeting planned at SCO (921981 kept Erdogan .38 Modi .30).

## 2026-08-26 (day 64)
- RESOLVED: 588637 Villa (+0.91); 834692 Egypt (+0.25). TW 3024.9.
- 08-26 updates: 120116 Harald V .86 (stable); 162316 Liverpool .86 (verbal agreement >GBP110m); 875467 Rogers .42 Barcola .28 Enzo .25.
- 08-26: 335239 Segalovitz .55 Taha .35 (primaries put Taha #2; Abbas may reserve #2 for Segalovitz).

## 2026-08-27 (day 65)
- RESOLVED: 162316 Liverpool (+0.98); 450664 CHELSEA (-0.03, TW -40); 876325 City (+0.96). TW 3069.3.
- 08-27 updates: 875467 Enzo .47 Barcola .30 Rogers .18 (Enzo->City ~EUR140m/GBP120m; Barcola EUR116m+addons to 140m); US Open draws -> 891014 Alcaraz .24 Zverev .19 Djokovic .13; 408930 Fritz .28 Shelton .27; 608158 Sabalenka .22 Gauff .15 Swiatek .13. Muchova/Mensik won mixed.
- 08-27 LATE: 120116 Norway -> Haakon VIII .52 (King very serious, family gathered).

## 2026-08-28 (day 66)
- RESOLVED: 120116 Haakon VIII (+0.64); 921981 Erdogan (+0.36). TW 3135.9.
- 08-28 updates: 335239 Segalovitz .66 (joint declaration imminent); 20480 Al-Hilal .88 (Martinelli green light, medical this weekend).
- 08-28: 729308 Nike .38 On .28/On Running .12 (trivial-Q rule); 508136 Mayun: Yemeni govt .36 Houthis .22 NRF .14 coalition .14 (Houthi attacks escalating).

## 2026-08-29 (day 67)
- RESOLVED: 20480 Al-Hilal (+0.98); 2260 Gobena (-0.06); 409386 Jepchirchir (+0.41). TW 3150.0.
- 08-29 updates: 875467 Barcola .45 Enzo .38 Rogers .13 (AJ: Barcola up to GBP123m); 79046 Arsenal .61 D .23 Villa .16 (odds).

## 2026-08-30 (day 68)
- RESOLVED: 127253 Barcelona (-0.15). TW 3137.0.
- 08-30 updates: 591807 Ofei .50 Queiroz .30 (GFA to appoint Ofei - exclusive); 224345 Malaysia .48 Indonesia .42 (Sarawak hazardous); 673971 Texas .50 Michigan .14. Bessent: another bank to be sanctioned this week (790870 unchanged, no name).

## 2026-08-31 (day 69)
- RESOLVED: 335239 "Yoav Segalovich" (my Segalovitz .66 NOT credited; -0.51); 79046 Arsenal (+0.77). TW 3177.3.
- 08-31 updates: 788295 split Naouar .35 / Nawar .33 (name-variant v2); 875467 Barcola .68 (official GBP123m, AP "most expensive of window") Enzo .27.

## 2026-09-01 (day 70)
- RESOLVED: 875467 Enzo Fernandez (+0.00; TW -43). TW 3134.1.
- 09-01: no changes (MAGA Inc still no buy; Ghana/Gaza plan no news).

## 2026-09-02 (day 71)
- RESOLVED: 591807 Queiroz (+0.26); 712131 Ben-Gvir (+0.14). TW 3179.3.
- 09-02: 284913 Barca .66 RM .30 (MD3 table, GD tiebreak).

## 2026-09-03 (day 72)
- No resolutions.
- 09-03: no changes (bank not yet named; Ebola Ituri epicentre, Beni 868).

## 2026-09-04 (day 73)
- RESOLVED: 205592 Sugar (+0.84); 224345 Malaysia (+0.55); 568969 Troy Parrott (-0.04); 790870 Golden Global Bank (-0.01). TW 3230.2.
- 09-04: 668636 Russell .28 Leclerc .20 (FP). MAGA Inc-linked nonprofit ran first national ad (Trump-focused) - 673971 unchanged Texas .50.

## 2026-09-05 (day 74)
- RESOLVED: 673971 Texas (+0.71). TW 3275.3.
- 09-05 updates: 668636 Russell .38 (Gasly pole, Russell P2); 284913 Barca .88 (RM lost at Betis).
- 09-05 US Open: 891014 Alcaraz .38 Zverev .22 (Djokovic R1 loss, FAA/deMinaur/Musetti/Fritz out); 408930 Tiafoe .26 Shelton .25 Michelsen .17; 608158 Sabalenka .25. Sweep2 launched (3 agents, 63 Qs).
- 09-05 SWEEP2 done (3 agents, ~100 searches, 39 resubmits). Big moves: 653425 Bednarek .42 (Lyles season over); 936021 Balew .26; 30434 Pathirage .50; 695205 Pathirage .80 (Chopra out); 816232 Camp Nou .78; 581343 Koja .58; 81247 CDU .55; 425800 Pantoja .48/Van .47; 88025 Netherlands .42; 935351 El Mansouri .38 (Chouki/Chaouki split); 759359 Odesa .35; 971366 Robinson .32; 52657 NAZA .12; 880660 Mendonca .62 None .33; 56802 Pakistan .50.

## 2026-09-06 (day 75)
- RESOLVED: 284913 Barcelona (+0.98); 490094 North Kivu (+0.42); 668636 Antonelli (-0.20). TW 3413.4.
- 09-06 US Open: 891014 Alcaraz .42; 608158 Sabalenka .28; 408930 Tiafoe/Shelton .26.

## 2026-09-07 (day 76)
- No resolutions.
- 09-07 US Open: 408930 Tiafoe .46 Michelsen .28 Shelton .16; 891014 Alcaraz .40 Zverev .20; 608158 Sabalenka .22 Rybakina .17 (Swiatek out to Zheng).

## 2026-09-08 (day 77)
- RESOLVED: 546622 Turkish Airlines (-0.01); 880660 Mendonca (+0.75). TW 3492.3.
- 09-08 US Open: 891014 Alcaraz .38 Zverev .25; 408930 Tiafoe .48 Michelsen .30 Shelton .17; 608158 Gauff .11.

## 2026-09-09 (day 78)
- RESOLVED: 408396 Permanent residency (+0.91); 971366 Tongue (+0.25). TW 3594.6.
- 09-09 US Open: Shelton beat Alcaraz! 891014 Zverev .34 Shelton .25 Tiafoe .19 Khachanov .16; 408930 Shelton .54 Tiafoe .45; 608158 Sabalenka .34 Rybakina .27 Gauff .22 Pegula .16.

## 2026-09-10 (day 79)
- RESOLVED: 508136 Houthis (+0.22); 759359 Kyiv (+0.59). TW 3622.5.
- 09-10: 891014 Zverev .38 Shelton .25 Tiafoe .19 Khachanov .14. NAZA (Venice) 25-min record ovation.
- 09-10 FIXES from Budapest final entry lists: 936021 Ingebrigtsen .25 (Balew not entered); 653425 Bednarek .45 (+Levell, Taylor out); 261941 Yan .76 (Angulo out); 30434 Pathirage .50.

## 2026-09-11 (day 80)
- RESOLVED: 342722 Kherbouch (+0.72); 408930 Shelton (+0.59); 936021 Ingebrigtsen (+0.39). TW 3751.2.
- 09-11: 891014 Zverev .55 Shelton .44 (final); 608158 Sabalenka .53 Rybakina .46 (final).

## 2026-09-12 (day 81)
- RESOLVED: 261941 Kitaguchi (-0.45); 52657 NAZA (+0.19); 5814 Forest (+0.28); 608158 Rybakina (+0.43). TW 3760.3.
- 09-12: 48458 Norris .38 Antonelli .27 (Norris pole at Madring).
- 09-12: 653425 Bednarek .50 (won 100m); 581343 Koja .63.

## 2026-09-13 (day 82)
- RESOLVED: 174389 UAE (+0.12); 30434 Pathirage (+0.71); 48458 Antonelli (+0.30); 487575 City (+0.55); 581343 Koja (+0.73); 653425 Bednarek (+0.72); 891014 Zverev (+0.60). TW 3943.3.
- 09-13: Emmys final odds: 216881 Widows Bay .66 Hacks .32; 873349 Pitt .90; 440552 Seehorn .82.

## 2026-09-14 (day 83)
- RESOLVED: 216881 Widows Bay (+0.78); 440552 Seehorn (+0.95); 816232 Camp Nou (+0.91); 870914 US (+0.62); 873349 The Pitt (+0.98). TW 4241.3.
- 09-14: 81247 Linke .40 CDU .38 AfD .15 (Infratest Linke 21 CDU 20).

## 2026-09-15 (day 84)
- RESOLVED: 518392 Nairobi (+0.06). TW 4232.8.
- 09-15: 934953 Tillis .30 McConnell .18 (Kremlev-Don Jr wedding story; GOP largely silent).

## 2026-09-16 (day 85)
- RESOLVED: 101639 Yemen (+0.75); 56802 China (+0.05); 753240 Inter Miami (+0.61). TW 4382.3.

## 2026-09-17 (day 86)
- RESOLVED: 660356 Aniviye (+0.66). TW 4448.5.
- 09-17: no changes (El Hammamy in Qatar final; 574485 kept Orfi .63).

## 2026-09-18 (day 87)
- RESOLVED: 574485 Orfi (+0.74); 729308 On (+0.26); 934953 John Curtis (-0.16). TW 4467.3.
- 09-18 updates: 425800 Van .54 Pantoja .44 (odds -130/-140); 574553 Tsarukyan .73; 67348 China .70 Iran .29 (SF: JPN bt CHN 97-77, KOR bt IRN 77-51 -> bronze CHN v IRN Sep 20);
  297571 RM .43 D .27 ATM .30 (Opta 46.6/25.1/28.3); 784475 Ngetich .44 (Taye apparently out; Ftaw Zeray in); 788295 AJ spelling "Wael Naouar" .56 (+Nawar .12);
  423956 MIKLÓS SESZTÁK .72 (Volánbusz hűtlen kezelés case; NNI: immunity-holder involved; Galgóczy: immunity lifted in 1-2 wks) — found via HU-language search!;
  731076 None .35 (Djibouti 72nd Sep 14, Albania 73rd Sep 21); 540490 +None .15; 447470 Antonelli .32 (8 wins; Russell no Baku penalty; Leclerc penalty);
  76365 +Tenth Circuit .12 (Sep 8 inj-pending-appeal denial); 154739 Texas .35 (TikTok liable Sep 10, remedies trial Oct) Arkansas .30 None .10;
  88025 Netherlands .62 (Israel weighing more measures; ban effective Sep 22); 889545 Korea .36 Uzbek .15 Japan .12 Saudi .10 Iran .06 (China bt PRK 2-1).
- LESSON: native-language searches (HU) uncovered decisive info missed by EN searches for weeks. Apply to other non-English questions.

## 2026-09-19 (day 88)
- RESOLVED: 425800 Van (+0.59); 574553 Tsarukyan (+0.86). TW 4578.3.
- 09-19: 81247 Linke .45 CDU .40 AfD .11 (final polls Linke +1-2). No other changes (Madrid derby kept; Alvarez to play some part).

## 2026-09-20 (day 89)
- RESOLVED: 297571 Atlético (+0.25); 299105 "Oil and gas" (+0.67, label "Oil and gas extraction" credited); 67348 IRAN (+0.01, China .70 lost bronze game); 784475 Ngetich (+0.65); 81247 "The Left" (+0.52). TW 4721.7.
- 09-20: 224082 Yu Yiting .52 Yu Zidi .44 (Yu Zidi 200fly GR 2:05.08); 300850 Yu Zidi .69; 889545 Korea .32 Uzbek .22 Saudi .16 Japan .14 Thai .05 (China 0-0 Iran, through).

## 2026-09-21 (day 90)
- RESOLVED: 224082 YU ZIDI (+0.42; had Yu Yiting .52); 25611 VINCENT BROWN (+0.09; alias split Bajinya .17 / Brown .10 — CPS used legal UK name). TW 4774.4.
- 09-21: 300850 Yu Zidi .86 (won 200IM 2:06.10); 190556 Ohashi .50 Dong .33 (100br dead heat 58.64); 695205 Pathirage .74 (won Ultimate Champs 91.09; javelins broken in transit). DOSB vote Sat Sep 26 (Berlin+, KölnRheinRuhr, München; 144 votes, abs. majority).

## 2026-09-22 (day 91)
- RESOLVED: 423956 BALÁZS HANKÓ (-0.54; I had Seszták .72 — over-concentrated on one probe; Hankó was in my Aug list at .05 then dropped). TW 4766.7.
- 09-22: 832291 Ri .83 (China absent 49kg); 315568 Alonso .56 (WEC option); 133827 FL .32 Iowa .22; 788295 Naouar .55 Henchiri .20 (all 4 striking; Henchiri needs surgery; AJ spelling Ghassen); 731076 None .42 (Albania 73rd Sep 21).

## 2026-09-23 (day 92)
- RESOLVED: 300850 Yu Zidi (+0.97); 788295 Wael Naouar (+0.74); 832291 Ri Song Gum (+0.96). TW 4974.5.
- 09-23: 944956 Munich .62 R-R .36 (Berlin withdrew; eval cttee ranked Munich & R-R highly); 686508 Puripol .58 Xie .12 Koike .09 Tada .08 (fixed entries); 556932 label split Satomi Kaido .22 / Watanabe .08.

## 2026-09-24 (day 93)
- RESOLVED: 190556 Ohashi (+0.63); 564365 João Félix (+0.02); 731076 IVORY COAST (-0.18; had None .42). TW 5058.6.
- 09-24: 889545 Korea .58 Vietnam .19 Thailand .15 (China B1, QF v Thailand Sep 26, SF v W(KOR/VIE) Sep 30); 158157 Ire .36 D .30 Isr .34 (both lost MD1); 447470 Antonelli .28 Russell .17 (FP1 Russell P1, Antonelli hydraulics); 935351 El Mansouri .62 Lekjaa .26 (PAM 97 seats 1st).

## 2026-09-25 (day 94)
- RESOLVED: 154739 ALABAMA (-0.23; unlisted); 686508 Puripol (+0.79); 76365 Sixth Circuit (+0.33). TW 5116.1.
- 09-25: squash SFs set (556932 Siva .61; 700005 Ng .38 Abhay .32 Zaman .16 Irfan .12); 447470 Russell .46 (pole by 0.84s; Antonelli P16); 173061 Eng .32 D .29 Spa .39 (odds); 815451 Belgium .57 France .41 (BEL leads on win/draw).

## 2026-09-26 (day 95)
- RESOLVED: 173061 Spain (+0.44); 447470 Russell (+0.68); 540490 KOHLI (+0.22); 944956 Munich (+0.73); 996188 Kurihara (+0.95). TW 5279.4.
- 09-26: squash finals Siva .72 v Anahat; Ng .57 v Abhay; 259249 QF .73 (Sindhu v Chen Yufei QF Sep 27); 138739 None .85 (TN SC denied stay Sep 23); 158157 kept (odds Isr 2.80 D 3.20 Ire 2.40; Irish turmoil).

## 2026-09-27 (day 96)
- RESOLVED: 158157 Ireland (+0.38); 259249 Quarterfinals (+0.89); 556932 Sivasangari (+0.85); 700005 Ng Eain Yow (+0.64); 88025 Netherlands (+0.84). TW 5518.2.
- 09-27: 815451 France .51 Belgium .48 (odds FRA -115; BEL leads on draw); 315568 Alonso .60; 935351 El Mansouri .80 (Alayam24 exclusive: King receives her Sep 28).

## 2026-09-28 (day 97)
- RESOLVED: 133827 Florida (+0.47); 695205 Pathirage (+0.92); 815451 France (+0.53). TW 5717.0.

## 2026-09-29 (day 98)
- RESOLVED: 315568 Alonso (+0.82); 935351 El Mansouri (+0.97). TW 5809.8. Active: 889545 (China v Korea SF Sep 30), 138739 (Pike Sep 30).
- 09-29: 138739 None .97 (SCOTUS denied stay Sep 29); 889545 Korea .84.

## 2026-09-30 (day 99)
- RESOLVED: 138739 SIXTH CIRCUIT granted day-of stay (-0.92; had None .97); 889545 South Korea (+0.97). TW 5836.1. ALL 252 RESOLVED. Final: acc 50.8%, BSS 0.367, TW 5836.12.
