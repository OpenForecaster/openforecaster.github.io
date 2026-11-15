# Forecasting memory

## Day 1 — 2026-06-24
- Submitted forecasts for all 252 active questions (7 parallel batch agents, 36 each, ~132 search_news calls total of 3000 budget).
- All questions are open-ended strings, no options list. Exact canonical naming matters; used full names per criteria.
- Calibration: top prob capped by field size; sums often <1. Overconfidence scores negative under Brier Skill, abstaining = 0.
- Batch files: memory/batches/batch1.md .. batch7.md (sorted by resolution date, Jul-Sep 2026).

## Strategy
- Every day: check new articles/ + refreshed market.csv; update ONLY questions where news materially changes the favorite (esp. resolving within 7 days + World Cup/Wimbledon/F1 brackets as they narrow). Raise probabilities as tournaments converge.
- Prioritize near-term: Jul 1-19 cluster (World Cup knockouts, Wimbledon finals, ICC Women's T20 WC final Jul 5, British GP Jul 5).
- Watch void/conditional phrasing: "if any" / "None" outcomes were submitted where criteria allows an explicit no-qualifier string — verify exact ground-truth phrasing when resolutions start appearing.

## Lowest-confidence Day-1 picks (revisit first)
- 754639 UK party leader resigns as MP; 107473 UK university investigations; 76066 Moldova PM successor (incumbent still in post Jun 24).
- Typhoons Bavi/Noul/Dolphin landfall provinces (climatology only, no 2026 track yet).
- 617889 Vozinha next club; 415011 Peru foreign minister; 927657 Syria NSB head; 942650 FOMC surnames (exact-string risk).
- 546622 Liverpool shirt sponsor; 52657 Venice Special Jury film; 660356 Nigeria suspended official; 934953 GOP senator; 870914 orbital weapons country.
- 996188 Puyo Puyo (gamertags vs real names); 574553 UFC 331 co-main (card unannounced).

## Key Jun-24 anchors found via search
- 2026 F1: Antonelli leads standings (156) ahead of Hamilton 115, Russell 106 — Mercedes-dominant season.
- World Cup: Messi 5 goals, Mbappe/Haaland 4 (Jun 24); favourites France/Spain/Argentina/England.
- Wimbledon: Alcaraz out injured (wrist); Sinner clear men's favourite; Sabalenka top women's seed.
- Nvidia most valuable company ~$4.9-5.1tn; Alibaba still largest foreign-firm US IPO record.

## Day 2 — 2026-06-25
- No resolutions; all 252 still covered. Updated 5 only: Golden Boot (Vinicius Jr 4 goals in), Women's T20 winner + Player of Tournament (England in SF, Wyatt-Hodge starring, India beat Bangladesh), Khamenei funeral Russian (Putin trimmed; funeral Jul 4-9), Boston QF (Germany trimmed after Ecuador loss, still group winners).
- Typhoon Bavi: no 2026 storm exists yet (search returns 2020 Bavi only) — climatology picks stand.
- Search budget: ~2825 remaining.

## Day 3 — 2026-06-26
- No resolutions. France beat Norway 4-1 (Dembele hat-trick) to top Group I; Haaland benched/rotated. Updated Golden Boot (Dembele in, Haaland trimmed), Boston QF (France up).
- Wimbledon odds (ESPN Jun 26): Sinner -165, Djokovic +600, Zverev +900; raised Sinner to 0.48 title / 0.42 first-finalist. Women's top: Sabalenka +350 — aligned.
- Spain v Uruguay result pending at scan time — check Jun 27 for SF1/Kansas City paths. Women's T20: Aus v India Jun 28 decisive for India SF.

## Day 4 — 2026-06-27
- WC groups: Spain top H (Uruguay OUT), England top group (Kane scored v Panama), France top I. Messi rested/bench v Jordan. Portugal v Colombia result pending at scan.
- Women's T20: Ireland upset WI but England beat NZ → SFs England + West Indies (Group B); Australia + likely India (Group A; SA needs huge NRR swing Jun 28).
- F1 Austria: Russell pole, Verstappen crash → Russell nudged up for British GP.
- Watch Jun 28: Aus v India + SA v Bangladesh (final SF spot), WC R32 begins, Austrian GP race, Wimbledon starts Jun 29.

## Day 5 — 2026-06-28
- Women's T20 SFs set: Australia, South Africa (India OUT, lost to Aus), England, West Indies. Final ~Jul 5.
- WC: Colombia top K (Portugal 2nd), Argentina top J (Messi scored as sub v Jordan → 6 goals), Canada first into R16. R32 running Jun 28-Jul 3; update QF/SF/winner as bracket thins.
- F1 post-Austria: Antonelli 171, Russell 131, Hamilton 125 (Russell won Austria). British GP Jul 5.
- Wimbledon starts Jun 29: watch early upsets (Sinner/Sabalenka paths).

## Day 6 — 2026-06-29
- Wimbledon D1: Sinner 5-set scare + fall vs Kecmanovic (won) → trimmed 0.48→0.44. Sabalenka comfortable. Raducanu withdrew (not in our outs).
- WC R32: Canada, Brazil (2-1 Japan) into R16. Netherlands-Morocco pending. No WC forecast changes.
- Next resolutions: Jul 1 (Jaylen Brown destination qid 344207 resolves by Jul 31 window actually — check criteria dates; market resolution_date Jul 1 for 344207/619176/659176).

## Day 7 — 2026-06-30
- WC R32 shocks: Germany OUT (Paraguay pens), Netherlands OUT (Morocco pens). France 3-0 Sweden, Norway 2-1 Ivory Coast, Brazil 2-1 Japan, Canada 1-0 South Africa.
- Boston QF pool now France/Paraguay/Canada/Morocco → France 0.50. R16: France-Paraguay (Philadelphia), Canada-Morocco (Houston), Brazil-Norway.
- Articles harvest Jun 30 only 53 lines — lean on search_news for scores/scorers. Confirm Mbappe/Haaland R32 goals Jun 31->Jul 1 before Golden Boot update.
- Jul 1: first resolution_dates (344207 Brown, 619176 PFA month, 659176 Russian official) — check if market resolves them then or at criteria deadline.

## Day 8 — 2026-07-01 (first resolutions)
- 344207 Brown → Philadelphia 76ers (miss, ~-0.09). 619176 → September (hit @0.24, ~+0.39). 659176 → Dmitry Medvedev (miss, ~-0.11). Capped-prob strategy validated: misses cheap.
- GT format: plain full names ("Philadelphia 76ers", "September", "Dmitry Medvedev") — matches our style.
- Golden Boot: Messi 6, Mbappe 6 (2 v Sweden), Haaland ~5, Kane 4 (brace v DRC), Vinicius 4.
- Bracket halves (Sporting News): SF1 half = France/Spain/Portugal/Belgium/USA/Canada/Morocco/Paraguay/Croatia...; Atlanta SF half = Argentina/England/Brazil/Mexico/Colombia/Norway/Switzerland... Fixed Atlanta SF (Portugal removed).
- Next: Jul 4-5 resolutions (Trey Alexander, cyclospora, Women's T20 final Jul 5, British GP Jul 5). Khamenei funeral starts Jul 4.

## Day 9 — 2026-07-02
- Women's T20 final Sun Jul 5 Lord's: Australia (beat WI SF) v England (beat SA SF, Sciver-Brunt 75). Priced Aus 0.52 / Eng 0.42.
- WC: Spain routed Austria (Oyarzabal 2), USA 2-0 Bosnia (Balogun red, suspended v Belgium). Portugal-Croatia + Switzerland-Algeria pending overnight.
- Wimbledon: Sinner/Sabalenka/Swiatek/Fritz into R3. British GP weekend starts Jul 3 (FP) — check Russell/Antonelli pace before Jul 5 race.
- Jul 4 resolutions incoming: Trey Alexander (177324), cyclospora state (633052, data as of Jul 16 per criteria but resolution_date Jul 4 — watch).

## Day 10 — 2026-07-03
- WC R32 done bar Argentina-Cape Verde + Colombia-Ghana (live/pending): Portugal 2-1 Croatia (R16 v Spain), Switzerland 2-0 Algeria, Egypt pens Australia (R16 v Argentina/Cape Verde winner).
- KC QF fixed: Portugal was wrongly in that pool (SF1 half) → Argentina/Colombia/Switzerland/Egypt.
- Silverstone Sprint weekend FP1: Hamilton P1, Antonelli P2, Leclerc P3, Russell P4 → British GP Hamilton 0.22. Update again after qualifying Jul 4.
- Jul 4: Khamenei funeral begins; Tour de France starts; WC R16 France-Paraguay + Canada-Morocco; Wimbledon R3/R16.

## Day 11 — 2026-07-04
- Resolved: Trey Alexander → Utah Jazz (miss ~-0.08); cyclospora state → Michigan (miss ~-0.09). Score so far: 5 resolved, 1 hit.
- Wimbledon women: Swiatek + Rybakina OUT R3 → Sabalenka 0.34.
- Silverstone: Antonelli sprint win + pole → British GP Antonelli 0.34 (race Jul 5).
- WC: Morocco 3-0 Canada (Boston QF v France/Paraguay winner; France-Paraguay live Jul 4, Tchouameni injured). Argentina 3-2 AET Cape Verde (Messi 7th goal, shaky). Colombia 1-0 Ghana.
- Jul 5: Women's T20 final Aus v Eng, British GP — both resolve. France result overnight → update Boston QF/SF1 Jul 5.

## Day 12 — 2026-07-05
- Resolved hits: Australia T20 @0.52 (+0.59), Mooney POT @0.14 (+0.20), Leclerc British GP @0.07 (-0.05 net; Antonelli 0.34 overweight on sprint/pole — lesson: cap F1 single-race tops ~0.25).
- WC: France 1-0 Paraguay (Mbappe pen, 7 goals = Messi), Norway 2-1 Brazil (Haaland brace, ~7 goals), Brazil OUT. Boston QF = France v Morocco Jul 9.
- Wimbledon: Sabalenka OUT (Osaka); Sinner + Djokovic into QFs. Women's now Gauff fav 0.22.
- F1: Leclerc won Silverstone (safety car finish), Russell P2, Hamilton P3, Antonelli no score → Russell extends 2nd-place cushion.
- R16 remaining Jul 6-7: Spain-Portugal, USA-Belgium, Argentina-Egypt, Switzerland-Colombia, England-Mexico. Update SF1/SF2/KC after.

## Day 13 — 2026-07-06
- Spain 1-0 Portugal (Merino 90+') — Ronaldo's last WC. SF1 repriced France/Spain co-favs 0.30.
- USA-Belgium playing Jul 6 eve (Balogun ban overturned by FIFA after Trump intervention — controversy).
- Jul 7 resolutions: trade deficit May (263626), UK leader by-election (754639, no news; Lowe/Farage stand), Hannah Dugan sentencing Jul 8 (213487), Moldova PM (76066, Jul 8).
- Wimbledon QFs Jul 7-8; R16 WC Jul 7: Argentina-Egypt, Switzerland-Colombia, England-Mexico.

## Day 14 — 2026-07-07
- Resolved hits: Vietnam largest trade deficit @0.29 (+0.36), Farage resigns as MP @0.10 (+0.16). Tally: 10 resolved, 6 hits (counting Leclerc), all misses cheap.
- Belgium 4-1 USA → QF v Spain. Wimbledon SFs: Gauff v Muchova (women), Sinner into men's SF.
- Jul 8: Dugan sentencing + Moldova PM resolutions; WC R16 finish (Arg-Egy, Sui-Col, Eng-Mex) Jul 7 eve US time → check Jul 8; WC QFs Jul 9-11 (Boston Thu, KC Sat).

## Day 15 — 2026-07-08
- Resolved: Dugan GT 'Monetary fine' vs our 'Fine' (possible exact-string miss — prefer fuller formal phrasings from criteria for penalty/status answers); Moldova PM Vasile Tofan (miss).
- WC QFs set: France-Morocco (Boston Jul 9), Spain-Belgium, Argentina-Switzerland (KC Jul 11), England-Norway. Messi leads Golden Boot.
- Wimbledon SFs: Sinner-Djokovic, Zverev-Fery (wildcard); women Gauff-Muchova, Kostyuk-Noskova (Andreeva out).
- Jul 9 resolutions: Boston QF (199448), UK university (107473), largest foreign IPO (279946 Alibaba 0.62), Eng-Ind T20 series (562262 — rain-hit, check).

## Day 16 — 2026-07-09
- Resolved: France Boston QF @0.60 (+0.74), England T20 series @0.36 (+0.40), King's College London (miss; GT uses curly apostrophe King’s), SK Hynix largest foreign US IPO (miss @Alibaba 0.62 → -0.38, worst yet: avoid >0.55 single-outcome on "record holds" with pending events).
- Typhoon Bavi: super typhoon, mainland landfall Sat Jul 11 Fuqing(Fujian)-Wenling(Zhejiang) stretch. Both Bavi qs now ~40/40 Fujian/Zhejiang.
- Wimbledon women's final Sat: Muchova v Noskova. Men's SFs Fri Jul 10: Sinner-Djokovic, Zverev-Fery.
- WC QFs: Spain-Belgium Jul 10, England-Norway + Argentina-Switzerland Jul 11. SFs Jul 14/15, 3rd place Jul 18, final Jul 19.

## Day 17 — 2026-07-10
- Resolved hits: Zhejiang most Bavi evacuations @0.40 (+0.50), Zverev first Wimbledon finalist @0.22 (+0.22). Tally 18 resolved.
- Spain 2-1 Belgium (Merino late winner again) → SF1 France v Spain Jul 14 priced 47/45.
- Wimbledon finals: women Muchova-Noskova Sat Jul 11; men Sinner-Zverev Sun Jul 12 (Sinner demolished Djokovic in SF).
- Jul 11: Bavi mainland landfall (66613), KC QF Argentina-Switzerland (457239), England-Norway QF, Seahawks ownership (902592), Wimbledon women's title (846335).

## Day 18 — 2026-07-11
- Resolved: Argentina KC QF @0.62 (+0.77), Zhejiang Bavi first mainland @0.40 (+0.46). GT short-forms: 'Noskova' (we: Linda Noskova 0.40) + 'Khosla Group' (we: Khosla family 0.11) — if grader is exact-match both score as misses; majority of GTs are full names so keep full-name style, but prefer criteria's literal phrasing where given.
- WC SFs: France-Spain (Jul 14), Argentina vs England/Norway winner (Jul 15 Atlanta). Final Jul 19.
- Resolutions Jul 12: Wimbledon men (742225 Sinner 0.62), MotoGP German GP (897546 Marc Marquez 0.28 top).

## Day 19 — 2026-07-12
- Resolved hits: Sinner Wimbledon @0.62 (+0.75), Marc Marquez German GP @0.28 (+0.44). 24 resolved.
- England 2-1 AET Norway (Bellingham x2) → SF Argentina-England Jul 15 Atlanta. Haaland out (goals frozen).
- McCullum SACKED as England Test coach Jul 12 (keeps white-ball). Successor (988210, resolves Jul 29): Flower fav. NOTE related: Stokes retired as captain late June; Brook fav captain (no market q).
- Jul 13-14: Trump TN-09 endorsement (362674 resolves Jul 13), MLB All-Star MVP Jul 14 (607314), SF1 France-Spain Jul 14, Tour de France stage 11 Jul 15 (24813).

## Day 20 — 2026-07-13
- Resolved hit: Brent Taylor Trump endorsement @0.28 (+0.48). 25 resolved.
- Tour sprint tally: Merlier 2 wins, Kooij 1, Philipsen 0 → Stage 11 (Jul 15, flat Vichy-Nevers) Merlier 0.24.
- Jul 14 resolutions: SF1 France-Spain, MLB ASG MVP, Jo Yong Won talks, NY data-centre moratorium (Hochul signature unconfirmed in headlines — risk).

## Day 21 — 2026-07-14
- Resolved: Spain SF1 @0.45 (+0.48), NY data-centre moratorium @0.42 (+0.65); misses Bellinger ASG MVP, Wang Huning (cheap). 29 resolved.
- Spain 2-0 France → final Jul 19 v Argentina/England (SF Jul 15 Atlanta, ref Ismail Elfath).
- Jul 15-17 watch: Tour stage 11, Atlanta SF, WC final referee (524604, Jul 16), most valuable company Jul 17 (329053 Nvidia), Open Championship R2 leader Jul 17 (32938), Gaza locality Jul 17 (425213, near-lottery).

## Day 22 — 2026-07-15
- Resolved: Argentina Atlanta SF @0.50 (+0.57); Tour stage 11 Waerenskjold upset (miss -0.11). 31 resolved.
- Final Jul 19 Spain-Argentina (priced 52/40); 3rd place Jul 18 France-England (48/38).
- Jul 16-17: WC final referee announcement, Nvidia market-cap check, Open Championship (starts Jul 16 at Royal Birkdale? R2 leader Jul 17), Morgan Rogers transfer (26225 resolves Jul 18), UFC Oklahoma Jul 18 (674079 Du Plessis-Usman), mile WR London DL Jul 18 (906651 El Guerrouj 0.72).

## Day 23 — 2026-07-16
- Resolved: WC final referee Slavko Vincic (miss, cheap). 32 resolved.
- Market cap Jul 15: Nvidia $5.1T > Apple $4.6T > Alphabet $4.4T → Nvidia 0.70 for Jul 17.
- Open R1: Brown/Im lead, Scheffler lurking, McIlroy cut battle → R2 leader Scheffler 0.16.
- Jul 17-19 cluster: Open R2, Gaza locality (lottery), 3rd-place playoff, Morgan Rogers, UFC OKC, London DL mile WR, WC final + Golden Boot/Ball (Jul 19), F1 Belgian GP weekend (556116 2nd place), Syria NSB (927657).

## Day 24 — 2026-07-17
- Resolved: Apple most valuable (Nvidia 0.70 → net -0.20 despite Apple cover; snapshot gaps <10% are near coin-flips — cap ~0.55), Lucas Herbert Open R2 leader (miss), Nuseirat Gaza (miss). 35 resolved.
- Belgian FP1: Verstappen P1, Hamilton P2 → Russell 2nd-place trimmed 0.50→0.46.
- Jul 18: 3rd-place France-England, Rogers transfer deadline, UFC OKC (Du Plessis 0.60), London DL mile. Jul 19: WC final Spain-Argentina + Golden Boot/Ball + Belgian GP.

## Day 25 — 2026-07-18
- Resolved: Rogers→Chelsea @0.17 (+0.20), England 3rd place 6-4 @0.38 (+0.39), Du Plessis @0.60 (GT 'Dricus du Plessis' case differs from ours — grader tolerance unknown), Josh Kerr mile WR (miss @El Guerrouj 0.72 → -0.53 worst; heavily-trailed home WR attempt underpriced). 39 resolved.
- Mbappe broke all-time WC scoring record (22) in 3rd-place game → likely leads Golden Boot into final; Messi needs final goals.
- Belgian GP: Antonelli pole, Hamilton FP3 crash → Russell 0.52 for 2nd-in-standings.
- Jul 19: WC final Spain-Argentina, Golden Boot/Ball, Belgian GP (556116), Syria NSB (927657).

## Day 26 — 2026-07-19
- Resolved: Spain WC @0.52 (+0.61), Mbappe Golden Boot @0.45 (+0.57), Hamilton 2nd @0.30 (+0.19, Russell DNF Spa), Khattab Syria @0.12 (+0.16); Rodri Golden Ball miss (skipped over name fear — GT short forms common: 'Rodri', 'Noskova'). 44 resolved.
- LeBron LEFT Lakers; finalists Cavs/Heat/76ers (981188 repriced). Open won by Ryan Fox (no market q on winner, only R2 leader).
- Next cluster Jul 20-26: Section 338, Syrskii successor, Noul, monsoon state, India 50 v Zimbabwe, wildfire emergency, Commonwealth gymnastics, OPCW munition, Vozinha club (post-WC heroics may move him), LeBron, Hungarian GP weekend.

## Day 27 — 2026-07-20
- Resolved: Section 338 first target Canada (miss, -0.10). 45 resolved.
- Syrskii: Zelensky interviewing replacements amid protests; Drapatyi frontrunner (249565 updated; Budanov is now chief of staff, not CinC candidate).
- Typhoon names: Haishen next, then Noul (unused) — Noul question (442417) may void if no July formation; Dolphin after that (737715 Aug).
- Jul 23-24: India-Zimbabwe T20 first 50 (check India squad Jul 22), Commonwealth Games start (gymnastics, javelin), Vozinha, LeBron decision imminent.

## Day 28 — 2026-07-21
- Resolved hits: Drapatyi @0.35 (+0.55, updated day before), Noul Guangdong @0.28 (+0.44). 47 resolved.
- India Zim squad: Iyer(c), openers Abhishek + 15yo Sooryavanshi; no Suryakumar/Samson/Gill → 131869 rebuilt.
- Vozinha: Colo-Colo deal collapsing (Romano), Inter Miami + Brazil interest; still unsigned Jul 21.
- Commonwealth Games Glasgow start Jul 23: men's team gymnastics (45561 England 0.45), javelin qual/gold Jul 30-31 — check startlists Jul 22-23.

## Day 29 — 2026-07-22
- Resolved hit: Assam monsoon deaths @0.20 (+0.32). 48 resolved. LeBron still undecided (Heat teaser was accidental post).
- Jul 23: India-Zimbabwe 1st T20I (131869), wildfire emergency window closes Jul 25 (market date Jul 23).
- Jul 24-26: OPCW munition, CWG gymnastics, Vozinha, LeBron, Bahrain GP replacement venue, Hungarian GP (FP3 Jul 25, race Jul 26), Diomande.

## Day 30 — 2026-07-23
- Resolved hits: Sooryavanshi first India 50 @0.20 (+0.26), Spain wildfire emergency @0.20 (+0.30). 50 resolved of 252.
- Jul 24-27: OPCW, CWG gymnastics, Vozinha (still unsigned?), LeBron, Bahrain replacement venue, Hungarian GP, Diomande, Peru FM (Fujimori inauguration Jul 28), WI 5-fer v Pakistan Tarouba.

## Day 31 — 2026-07-24
- Resolved: Vozinha→Colo-Colo @0.18, LeBron→76ers @0.20, Canada CWG gymnastics @0.15 (small +), OPCW GT 'Aerial bombs' plural vs our singular (tolerance unknown). 54 resolved.
- String-matching risk list: 'Monetary fine' vs Fine, 'Noskova', 'Rodri', 'Dricus du Plessis' case, 'Aerial bombs' plural, King’s curly apostrophe. If grader exact-matches, several right-answer forecasts score as misses — nothing more to do beyond using criteria phrasing.
- Hungary FP1 Leclerc fastest → Leclerc up in FP3/race. Bahrain replacement: Malaysia/Sepang now in frame.

## Day 32 — 2026-07-25
- Resolved: FP3 Hungary Norris (miss after dropping him Jul 24), Bahrain replacement GT 'Sepang' short form. 56 resolved.
- Hungary grid: Norris pole, Leclerc P2, Antonelli P3, Piastri P4, Hamilton P5 (penalty). Race priced Norris 0.30.
- Jul 26-29: Hungarian GP, Diomande, Peru FM + WI 5-fer (Test starts Jul 27 Tarouba), US strike country window (339902), Red Sea coalition (107175), FOMC Jul 29 (942650), McCullum successor (988210 Jul 29).

## Day 33 — 2026-07-26
- Resolved: Norris Hungarian GP @0.30 (+0.44), Diomande→Real Madrid @0.04 (~flat). 58 resolved.
- FOMC Jul 29: consensus hold + Hammack/Logan hawkish dissents (Warsh chairing; hike prob rose to ~34% per FedWatch late). 942650 updated.
- Jul 27: WI-Pakistan Test Tarouba starts (179451), Peru FM (415011 — Fujimori inauguration Jul 28, cabinet then).

## Day 34 — 2026-07-27
- Resolved misses (cheap): Justin Greaves WI 5-fer, Carlos Espa Peru FM. 60 resolved.
- Jul 28-30 cluster: US strike country (339902 window Jul 22-29), FOMC + McCullum successor + Red Sea coalition + Myanmar repatriation (Jul 29), UN straw poll + nuclear shutdown + CWG javelin qual (Jul 30), CWG javelin gold Jul 31.

## Day 35 — 2026-07-28
- Resolved hit: Iraq US strike country @0.25 (+0.31). 61 resolved.
- Jul 29: FOMC dissents (942650), McCullum successor (988210 Flower fav), Red Sea coalition (107175 US 0.22), Thailand Myanmar repatriation (971524).
- Jul 30-31: UN SG straw poll (238968 Grossi 0.38), nuclear drought shutdown (683823), CWG javelin (970163 qual + 449245 gold; Pathirage fav), Bruno Guimaraes (108618 Man Utd 0.24).

## Day 36 — 2026-07-29
- Resolved: FOMC 'Hammack, Kashkari, Logan' exact-string hit @0.10, Saudi Red Sea coalition @0.10, Malaysia repatriation @0.08; Stephen Fleming England coach (miss). 65 resolved.
- Aug transfer window heats up: many club-signing qs resolve Aug (window closes Sep 1) — check Romano-type news weekly per player cluster (batch files 3-5).
- Skubal "possible farewell" start Jul 28 → trade likely by Jul 31 deadline.

## Day 37 — 2026-07-30
- Resolved: Grynspan UN straw poll @0.12, Hungary nuclear drought @0.14 (+0.24), Pathirage javelin qual (GT short form 'Rumesh Pathirage'). 68 resolved.
- NAME-FORM RULE: when a related question's GT reveals the short form for a person, mirror it in sibling questions (done for 449245; also Asian Games javelin 695205 has 'Rumesh Tharanga Pathirage' 0.28 — switch it too next touch).
- Aug 1-4: Skubal deadline, ICE month, Rocket Classic golf, DC Open tennis, Salah club, Kansas/Michigan Senate primaries Aug 4-5.

## Day 38 — 2026-07-31
- Resolved: Guimaraes→Arsenal @0.05 (~flat), Pathirage CWG gold — GT full name 'Rumesh Tharanga Pathirage' (qual GT was short). VERDICT: GT name forms inconsistent; stick to full canonical names, stop chasing variants. 70 resolved.
- Aug: 182 questions left, mostly transfers (window closes Sep 1), US primaries, tennis/golf weekly events, Asian Games late Sep. Strategy: twice-weekly transfer-news sweep + event-eve checks for sports.

## Day 39 — 2026-08-01
- Resolved hit: Skubal→Dodgers @0.24 (+0.40). 71 resolved.
- In-progress repricing works: Rocket Classic (Riley leads R3), DC Open SFs (Fritz/Nakashima, Tabilo/Jodar; Pegula/Shnaider, Osaka/Eala). Shelton + de Minaur OUT in DC.
- Aug 4-5 primaries: Kansas Dem Senate (716751), Michigan Dem Senate (883794 El-Sayed fav), TN-05 GOP (874628 Ogles), Alabama-02 GOP Aug 11. Check polls Aug 3.

## Day 40 — 2026-08-02
- Resolved misses: ICE highest month July, Thorbjornsen Rocket Classic. 73 resolved.
- DC finals Aug 2: Fritz-Jodar (62/30), Pegula-Eala (58/34). Eala is breakout story of summer (beat Swiatek at Wimbledon, Osaka+Svitolina in DC) — remember for Canadian/Cincinnati/US Open draws.

## Day 41 — 2026-08-03
- Resolved: Fritz DC @0.62 (+0.77), Eala DC @0.34 (+0.23), ICRC Suu Kyi access (GT 'ICRC' short form). 76 resolved.
- Michigan Dem primary Aug 4: El-Sayed +10-15 in late polls, prediction markets ~97% → raised to 0.75.
- Aug 4-6: Kansas Dem, Salah next club (check), Sarah Khalifa sentence, TN-05 Ogles, WI-Pak 2nd Test, Rodri transfer, Parker UKAD.

## Day 42 — 2026-08-04
- Resolved hits: Adam Hamilton KS Dem @0.18, Oman Hormuz mines @0.24, 'Death penalty' Khalifa @0.28. Salah→Trabzonspor (had Fenerbahce/Galatasaray, right league wrong club). 82 resolved.
- Aug 5-9: Michigan primary result, WI-Pak 2nd Test, TN-05, jobs data sector (687277 Aug 7), MotoGP British (259947 Aug 9 Bezzecchi fav), Dolphin landfall city (737715 Aug 8 — check storm), AJK polling districts (685197), Kate boat city (251083).

## Day 43 — 2026-08-05
- Resolved hits: El-Sayed Michigan @0.75 (+0.90, best yet — late poll check paid), Pakistan 2nd Test @0.34 (+0.44). 84 resolved.
- Dolphin: super typhoon heading for Zhejiang/Yangtze coast ~Aug 9-10 → city list rebuilt (Wenzhou/Taizhou/Ningbo/Shanghai).
- Pattern: biggest gains come from checking REAL odds/polls/leaderboards 1-3 days before resolution. Keep doing event-eve checks for Aug sports (Canadian/Cincy tennis, St Jude golf, UFC 330, MotoGP, hockey WC pools, Pan Pacs swimming).

## Day 44 — 2026-08-06
- Resolved: Thailand Ye Win Oo @0.20, Hatcher TN-05 @0.30 (beat our fav Ogles, still +); Rodri→Barcelona, Parker 'His nutritionist'. 88 resolved.
- MotoGP standings: Martin 208, Ogura 194, M Marquez 190, Bezzecchi 186 (injured, collarbone), Di Giannantonio 184. British GP odds fav M Marquez 5/2 → repriced.

## Day 45 — 2026-08-07
- Resolved: Government sector jobs @0.19 hit; AJK districts miss (tiny). 90 resolved.
- Dolphin landfall Aug 9-10 Fuzhou–Taizhou coast; HKO points near Taizhou → Taizhou 0.20 top.
- Aug 8-12: Kate boat, Solomon, MotoGP, Golan recognition, Alabama-02 primary, Shakhtar stadium, nuclear shutdown #2, Ferran Torres, Inter Miami Leagues Cup, Canadian Open tennis, Women's Afcon.

## Day 46 — 2026-08-08
- Resolved: Bristol Kate @0.07 small hit; Solomon→West Ham miss; Dolphin GT 'Yuhuan' (county under Taizhou — granularity loss). 93 resolved.
- MotoGP: Aprilia 1-2-3 sprint (Martin/Ogura/Bezzecchi), M Marquez P9 struggling → Sunday Martin 0.32.

## Day 47 — 2026-08-09
- Resolved: Raul Fernandez British GP @0.07 (~flat). 94 resolved.
- WAFCON SFs Aug 12: Morocco-Cameroon, Algeria-Malawi (Nigeria + South Africa OUT in QFs; Malawi = giant-killers with Chawinga sisters). Final ~Aug 16.
- Canadian Open (Toronto, final Aug 13): Noskova out early; top seeds Sabalenka/Rybakina/Gauff/Swiatek alive at R32.

## Day 48 — 2026-08-10
- Resolved: Colombia Golan recognition (miss cheap). 95 resolved, 157 to go.
- Aug 11-13: Alabama-02 Marques, Shakhtar stadium, nuclear shutdown #2 (Slovenia 0.14 top), Ferran Torres, WAFCON SFs, Canadian Open final Aug 13, Spanish Super Cup host (Qatar 0.52).

## Day 49 — 2026-08-11
- Resolved hits: Marques AL-02 @0.34 (+0.54), Ferran Torres→PSG @0.12, Romania nuclear shutdown @0.05. Shakhtar→Stamford Bridge (wild miss). 99 resolved.
- Canadian Open SFs: Swiatek-Svitolina + Rybakina/Gauff/Osaka side; Sabalenka out before SF.

## Day 50 — 2026-08-12
- Resolved: NextVision @0.14, Cameroon+Malawi final pair @0.12; Inter Miami group-stage exit (miss, -0.12), Spence→Inter Milan (had Juventus), 'Judiciary' variant. 105 resolved.
- WAFCON final Aug 16: Cameroon (beat Nigeria, Morocco) v Malawi (Chawingas) → 48/40.
- Aug 13-16: Canadian Open final, Spanish Super Cup host (Qatar 0.52), Bangladesh Test century in Aus, UFC 330 (Dern 0.55, Makhachev 0.60), Pan Pacs swimming (Ledecky 0.65 800FR), Community Shield Arsenal-City, St Jude golf, Cincinnati tennis starts.

## Day 51 — 2026-08-13
- Resolved: Swiatek Canadian Open @0.30 (+0.42); Spanish Super Cup host Türkiye (miss @Qatar 0.52, -0.32). 107 resolved.
- Cincinnati (men+ women) Aug 14-23: check Djokovic/Medvedev draw paths + Alcaraz return status (855662) Aug 14-15. Sinner/Alcaraz entries?
- Aug 15-16: UFC 330, Pan Pacs, Community Shield, WAFCON final, St Jude, MLS East leader Aug 19 snapshot (541001 Nashville/Miami).

## Day 52 — 2026-08-14
- Resolved: Tanzid Hasan Bangladesh century (miss). 108 resolved.
- Cincinnati: Sinner (knee) + Alcaraz (wrist) OUT → men's title/conqueror markets rebuilt (Zverev top seed, Djokovic 3, Medvedev 4, Fritz 6). Alcaraz return → US Open.
- Aug 15-16: UFC 330, Pan Pacs (Douglass/Walsh 50FR; Ledecky 800FR), Community Shield, WAFCON final, St Jude R3 check Aug 15.

## Day 53 — 2026-08-15
- Resolved hits: Dern @0.55 (+0.71), Makhachev @0.60 (+0.79), Douglass 50FR @0.30 (+0.45, set WR in heats). Misses: Ledecky 800FR @0.65 (-0.43, Pallister won 400+800 — era change), Djokovic lost Cincy R2 to Tirante, Indonesia quake. 115 resolved.
- Scheffler leads St Jude after 61 → 0.30. Cincy: Zverev fav with Djokovic out.
- Aug 16: WAFCON final, Community Shield, St Jude.

## Day 54 — 2026-08-16
- Resolved hits x3: Arsenal Community Shield @0.38 (+0.51), Cameroon WAFCON @0.48 (+0.57), Scheffler St Jude @0.30 (+0.50). 118 resolved, 134 left.
- Aug 17-23: Senegal coach, Hockey WC Pool D, Japan GDP component, FDA nominee (Overton 0.25), Cory Mills primary, Florida Dem Senate (Vindman 0.60), transfer cluster, Cincinnati finals Aug 23, Dutch GP Aug 23, Silesia DL Aug 23.

## Day 55 — 2026-08-17
- Resolved: England Hockey Pool D @0.35 (+0.47), Japan GDP net exports @0.20; Patrick Vieira Senegal coach (miss). 121 resolved.

## Day 56 — 2026-08-18
- Resolved hits: UAE embargo @0.20, Elijah FL primary @0.30, Overton FDA @0.25, Shifa Hospital @0.30. Vindman 0.60 lost to Nixon (cover @0.15 kept it near flat). 129 resolved.
- NOTE club spelling: GT 'Al Hilal' (no hyphen) vs our usual 'Al-Hilal' elsewhere — inconsistency stands.
- Aug 19-23: Konsa/Savinho/Baleba/Marmoush transfers, CA-14 Wahab 0.60, Sinaloa governor, Freedom 250 pole (Palou 0.30), PL opening weekend, Dutch GP, Cincinnati finals, Silesia DL.

## Day 57 — 2026-08-19
- Resolved misses: Konsa→Arsenal, Nord Stream arrest Zhuravlev (None @0.50 → -0.25; cap "none" outcomes ~0.35 unless base rate overwhelming). 131 resolved.

## Day 58 — 2026-08-20
- Resolved hits: Savinho→Spurs @0.45 (+0.70), Wahab CA-14 @0.60 (+0.80), Alcaraz US Open return @0.34 (+0.56), Hezbollah @0.06. 136 resolved.
- Aug 21-23: Baleba/Marmoush/Fabinho transfers, Freedom 250 pole, Robot Games 100m, PL openers (Forest/Man Utd), Dutch GP, Cincinnati finals (men Zverev fav; women 260735 check SFs Aug 22), Silesia DL (Warholm/dos Santos; Jefferson-Wooden/Alfred).

## Day 59 — 2026-08-21
- Resolved hits: Baleba→Man Utd @0.25 (+0.43), Marmoush→Spurs @0.10. 138 resolved.
- Cincinnati carnage: Zverev/FAA/Djokovic/de Minaur/Sabalenka/Rybakina(ret) all out. Men QFs Fritz-Nakashima, Paul-Cobolli, Fils in SF; women SF Pegula-Swiatek + Gauff/Kostyuk/Bejlek/Keys side.
- Sabalenka slump (RG QF, Wim R4, Toronto R4, Cincy R4) — fade for US Open pricing late Aug.

## Day 60 — 2026-08-22
- Resolved hits: Palou Freedom 250 pole @0.30 (+0.48), Tiangong Ultra robot 100m @0.32 (+0.51), Leeds beat Forest @0.18. Hull beat Man Utd (cover). 144 resolved.
- Trabzonspor signed BOTH Salah and Fabinho — Turkish club was the summer's spender; note for remaining transfer qs with Turkish links.
- Dutch GP: Norris pole → 0.34. Cincy finals Aug 23; Silesia DL Aug 23.

## Day 61 — 2026-08-23
- Resolved hits x5: dos Santos 400H @0.32, Jefferson-Wooden 100m @0.25, Gauff Cincy @0.18, Fils Cincy @0.14, Norris Dutch GP @0.34 (+0.49). Bouaddi→Man City miss. 150 resolved, 102 left.
- Remaining profile: ~30 transfers (window ends Sep 1), US Open tennis, Asian Games (Sep), F1 Italy/Spain/Azerbaijan, Emmys/Venice, nations league, misc specific-news lottery tickets.

## Day 62 — 2026-08-24
- Resolved: Allan Elias→Man City, Lincoln port Thailand, Hadjam→Brighton (GT short 'Brighton'), Netherlands Eurovision boycott @0.06 cover. 154 resolved, 98 left.
- Aug 25: Celtic UEFA comp (UCL 0.55/UEL 0.38 — playoff 2nd leg), PFA Player of Year (Fernandes 0.30/Rice 0.27), measles death state, Witkoff Moscow.

## Day 63 — 2026-08-25
- Resolved: Bruno Fernandes PFA @0.30 (+0.42); Celtic→Europa League (our UCL 0.55 too high — playoff coin flips cap ~0.4), Ratcliffe Moscow, Pennsylvania measles, Patten/Siniakova mixed. 159 resolved, 93 left.

## Day 64 — 2026-08-26
- Resolved: Jackson→Villa @0.04 cover, Xi first ME visit Egypt (miss). 161 resolved, 91 left.
- Aug 27-31: Barcola/Martinez/Enzo transfers, Harald V (0.75), SCO Putin counterpart, Martinelli, Sydney Marathon (check elite fields Aug 28), Gabriel Jesus, Raam No.2, Villa-Arsenal Aug 31.

## Day 65 — 2026-08-27
- Resolved: Barcola→Liverpool @0.22 (+0.37); Martinez→Chelsea, Enzo→Man City (rumour-tops at 0.32 both wrong). 164 resolved.
- Sydney Marathon Aug 30 (market date Aug 29): Lemma/Simbu men; Jepchirchir women (Hassan absent, Sawe absent despite 1:59:30 London WR in April!).

## Day 66 — 2026-08-28
- Resolved: Haakon VIII Norway monarch (Harald V @0.75 → -0.45), Erdogan Putin SCO counterpart @0.15. 166 resolved, 86 left (all September).

## Day 67 — 2026-08-29
- Resolved: Jepchirchir Sydney @0.30 (+0.48); Gobena men's upset, Martinelli→Al-Hilal. 169 resolved, 83 left.
- US Open Aug 30: Sinner OUT (knee), Alcaraz returns as fav (~30% mkt), Zverev #2. Women: Sabalenka fav despite slump; Gauff form player; Rybakina Achilles doubt.

## Day 68 — 2026-08-30
- Resolved: Gabriel Jesus→Barcelona (miss). 170 resolved, 82 left (all September).
- September watchlist: US Open (to Sep 13), Italian GP Sep 6, Spanish GP Sep 13, Azerbaijan Sep 26, Emmys Sep 14, Venice Sep 12, Asian Games Sep 19-30 cluster, Nations League late Sep, Morocco PM Sep 29, Christa Pike Sep 30.

## Day 69 — 2026-08-31
- Resolved: Arsenal beat Villa @0.42 (+0.55); Segalovich Raam (miss). 172 resolved, 80 left.
- Biggest PL fee: Rogers→Chelsea ~£117m/$160m vs Barcola→Liverpool £123m w/add-ons vs Anderson→City £116m — source-dependent; split 30/28/20.
- US Open underway; check surviving seeds ~Sep 5 (R16) and Sep 9 (SF).

## Day 70 — 2026-09-01
- Resolved: Enzo Fernandez highest PL fee (cover @0.08). 173 resolved, 79 left.

## Day 71 — 2026-09-02
- Resolved: Queiroz Ghana @0.18 (+0.32); Ben-Gvir Gaza plan (None 0.45 cushioned). 175 resolved.

## Day 72 — 2026-09-03
- No resolutions. US Open top seeds into R3 (Alcaraz, Sabalenka, Gauff, Swiatek, Zverev; Jodar OUT to lucky loser Bu).
- Monza: Antonelli grid penalty → Norris 0.22 fav for Italian GP Sep 6.

## Day 73 — 2026-09-04
- Resolved: FAO Sugar @0.22 (+0.32); Malaysia haze, Troy Parrott opener, Golden Global Bank misses. 179 resolved, 73 left.

## Day 74 — 2026-09-05
- Resolved: MAGA Inc Texas @0.06 cover. 180 resolved.
- Monza: Gasly maiden pole (Alpine), Russell P2, Leclerc P3, Antonelli back-of-grid (engine), Norris P8 → race Russell 0.20.
- US Open: Fritz OUT R3 (Cerundolo), Anisimova out; favorites alive into R16.

## Day 75 — 2026-09-06
- Resolved: Barcelona La Liga leaders @0.30, North Kivu Ebola @0.20; Antonelli won Monza from back of grid (we'd faded him post-penalty). 183 resolved, 69 left.

## Day 76 — 2026-09-07
- No resolutions. US Open QFs: Zheng stunned Swiatek; Rybakina (fit again) beat Osaka; Alcaraz cruising, faces Shelton QF.

## Day 77 — 2026-09-08
- Resolved: Liverpool sponsor Turkish Airlines (miss), Mendonca Brazil (None 0.55 → -0.30). 185 resolved, 67 left.
- US Open QFs Sep 9-10; finals Sep 12-13. World Athletics Ultimate Champs Sep 11-13 (5000m, javelins, 200m).

## Day 78 — 2026-09-09
- Resolved: 'Permanent residency' census (variant of our lawful permanent residence), Tongue most wickets @0.12 cover. 187 resolved.
- USO SFs: Shelton d. Alcaraz (3:33am finish), Tiafoe also SF; women Sabalenka-Pegula + Rybakina (new No.1)-Gauff.

## Day 79 — 2026-09-10
- Resolved: Kyiv fuel-station strikes @0.25 hit; Mayun Houthis cover. 189 resolved, 63 left.
- USO men's SFs: Shelton-Tiafoe, Zverev-Khachanov (Djokovic out QF). Women's final Sat, men's Sun.
- Sep 11-13: World Athletics Ultimate Champs Budapest (5000m Ingebrigtsen/Hocker, javelins, Lyles 200m), Venice prizes Sep 12, Villa-Forest, Spanish GP Sep 13.

## Day 80 — 2026-09-11
- Resolved hits x3: Kherbouch sentence @0.35 (+0.58), Shelton furthest US @0.52 (+0.64), Ingebrigtsen 5000m @0.30 (+0.46). 192 resolved, 60 left.
- USO finals: Sabalenka-Rybakina (50/42), Zverev-Shelton (52/38).

## Day 81 — 2026-09-12
- Resolved hits: Kitaguchi javelin @0.25 (+0.40), Rybakina US Open @0.42 (+0.41), Forest @0.18. Venice NAZA (unknowable). 196 resolved, 56 left.
- Madrid GP: Norris pole by 0.011 over Antonelli → Norris 0.32.
- Sep 13: USO men's final Zverev-Shelton, Spanish GP, Ultimate Champs day 3 (men javelin, 200m), Manchester derby, Okinawa gov election.

## Day 82 — 2026-09-13
- Resolved hits: Zverev US Open @0.52 (+0.63), Man City derby @0.35 (+0.48), Koja Okinawa @0.30, UAE venue @0.16, Bednarek 200m @0.10 (name variant). Pathirage won Ultimate javelin too (omitted from our list — fixed for Asian Games). 203 resolved, 49 left.
- Antonelli won Madrid (GT short 'Kimi Antonelli').

## Day 83 — 2026-09-14
- Resolved hits: Seehorn @0.45 (+0.67), The Pitt @0.45 (+0.65); Widow's Bay comedy upset. 208 resolved, 44 left.
- Remaining: Asian Games cluster (Sep 19-30), Nations League, UFC 331, Azerbaijan GP, Berlin election, Morocco PM, Christa Pike, misc specifics.

## Day 84 — 2026-09-15
- Resolved: Nairobi 2029 Worlds @0.18. 209 resolved, 43 left.
- UFC 331 Sep 19: Van-Pantoja 2 (Van -130), Tsarukyan-Ruffy co-main → priced.

## Day 85 — 2026-09-16
- Resolved: China Houthis ask @0.32 (+0.50), Inter Miami Campeones @0.40 (GT 'Inter Miami' short), Yemen UNGA appeal cover. 212 resolved, 40 left.

## Day 86 — 2026-09-17
- Resolved: Aniviye Nigeria suspension exact hit @0.12. 213 resolved, 39 left.
- Asian Games Nagoya start Sep 19: verify entries for Yu Yiting/Yu Zidi (IMs), Qin Haiyang (breast), Ri Song-gum (49kg), squash Sivasangari/Ng, Sindhu, 100m Boonson/Sani Brown, basketball bronze, China football.

## Day 87 — 2026-09-18
- Resolved: Orfi PSA No.1 @0.30 (+0.30); Mbappe sponsor 'On' (Nike 0.70 → -0.50). 216 resolved, 36 left.
- Asian Games open Sep 19: China swim roster confirmed (Yu Yiting, Yu Zidi, Qin Haiyang in).

## Day 88 — 2026-09-19
- Resolved hits: Van @0.52 (+0.61), Tsarukyan @0.62 (+0.78). 218 resolved, 34 left.
- Berlin Sep 20: Linke 22 / CDU 20 / AfD 18 final FGW poll → flipped to Linke 0.34.

## Day 89 — 2026-09-20
- Resolved: Atletico derby (accent variant), Oil and gas Iran, Iran basketball bronze @0.08, Ngetich half marathon @0.10, Berlin 'The Left' GT vs our 'Die Linke'. 223 resolved, 29 left.

## Day 90 — 2026-09-21
- Resolved: Yu Zidi 200IM @0.20 cover (+0.17); Vincent Brown (Bajinya alias) Rwanda charge. 225 resolved, 27 left.

## Day 91 — 2026-09-22
- Resolved: Hanko Hungary immunity (miss). 226 resolved, 26 left.

## Day 92 — 2026-09-23
- Resolved: Yu Zidi 400IM @0.42 (+0.62), Ri Song Gum 49kg @0.30 (hyphen variant), Naouar hunger strike (spelling variant). 229 resolved, 23 left.

## Day 93 — 2026-09-24
- Resolved: Ohashi upset Qin (0.50 → -0.28), Joao Felix winner, Ivory Coast Artemis. 232 resolved, 20 left.
- Finale week: Baku GP qualifying Sep 26, Nations League Sep 24-29, Asian Games athletics/squash/football, DOSB Sep 26, Morocco PM + Aston Martin Sep 29, Pike Sep 30.

## Day 94 — 2026-09-25
- Resolved: Boonson 100m @0.20 (+0.32); Alabama TikTok, Kalshi Sixth Circuit short-form. 235 resolved, 17 left.
- DOSB vote Sep 26: Berlin withdrew post-Linke win; Munich (eval 87.0) v Köln-Rhein-Ruhr (85.0) → Munich 0.48.
- England-Spain NL is Sep 26 (market title says Sep 19).

## Day 95 — 2026-09-26
- Resolved hits: Spain beat England @0.32, Munich DOSB @0.48 (+0.60), Kohli cover. 240 resolved, 12 left.
- A1: Belgium 2-0 in Italy, France 1-0 in Turkey (Mbappe injured, Zidane coaching France now). MD2 Belgium-France Sep 28 → Belgium 0.42 to lead.

## Day 96 — 2026-09-27
- Resolved hits: Ireland beat Israel @0.38 (+0.51), Sivasangari squash @0.30 (+0.46), Sindhu QF + Ng squash (name variants), Netherlands Ramallah miss. 245 resolved, 7 left.
- Morocco: PAM won election (97 seats); PM = Mansouri (leader) vs Lekjaa → 52/30.
- Last 7: ChatGPT state, javelin, A1 leader, Alonso, Morocco PM, China football, Pike stay.

## Day 97 — 2026-09-28
- Resolved: France lead A1 @0.36 (+0.41), Pathirage Asian javelin (name variant), Florida ChatGPT. 248 resolved, 4 left.
- China U23 in Asian Games SF v South Korea Sep 30 → Korea 0.62 to end bid.

## Day 98 — 2026-09-29
- Resolved hits: Alonso stays @0.42 (+0.65), El Mansouri Morocco PM @0.52 (GT short 'El Mansouri'). 250 resolved, 2 left.

## Day 99 — 2026-09-30 FINAL
- Last two: South Korea ended China bid @0.62 hit; Sixth Circuit granted Pike stay (cover @0.08). All 252 resolved.
- Search budget used: ~215 of 3000.
