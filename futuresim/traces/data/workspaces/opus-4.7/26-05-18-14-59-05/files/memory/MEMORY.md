# FORECASTING MEMORY

## SETUP
- Sim start: 2025-12-24. 330 questions, all string-type, resolve 2026-01-01..2026-03-28.
- Daily updates. TW-score = sum over questions of (sum daily BSS*100)/active_days. Predict EVERY question EVERY day.
- BSS = 1 - SSE over outcomes. Abstain=0. Calibrated tiny probs on unknowable ≈ 0 (safe). Overconfidence = negative.
- Strategy: predict all 330 each day; refine near-term (resolving <10d) with fresh news; base-rate the rest.
- Workspace path: .../minimalHarness_claude-opus-4-7_001/workspace

## SCORING NOTES
- If true outcome unpredicted: score = -(sum of my p_i^2). Small probs => small loss.
- If predicted at p and true: gain ~1-(1-p)^2. Report calibrated probs; cover top 3-5; leave mass implicit when unsure.
- Many "Who/Which X will [dramatic event]" Qs: event may NOT happen by date -> resolves no-answer -> any guess slightly negative. Keep sums modest (0.4-0.7) for speculative.

## MACRO CONTEXT (as of 2025-12-24)
- VENEZUELA: Trump huge military buildup in Caribbean (carrier, troops), boat strikes, blockade, sanctions on Maduro family Dec 19. Trump says land strikes "coming soon". Regime change pressure. Machado (opposition, fled) backs US. Citgo license extended to Feb 3.
- UKRAINE: Yermak (chief of staff) sacked early Dec over $100M Energoatom corruption scandal. Defence Min = Denys Shmyhal. US peace plan talks ongoing (US envoys to Moscow). Successor candidates for roles: Fedorov, Shmyhal, Kyslytsya, Pavlo Palisa.
- GREENLAND: Trump-Denmark dispute ongoing/escalating into Jan 2026 (talks, NATO Arctic).
- MEASLES: SC (Spartanburg ~138), Arizona (176), Utah (115). Q asks which state hits 185 by Jan 2026 -> Arizona most likely (176 and growing), then South Carolina.
- NYE PLOT: FBI foiled "Operation Midnight Sun" Turtle Island Liberation Front, LA/Orange County (NOT Charlotte NC). Q628026 asks town outside Charlotte NC -> may be different/unclear; LA-area plot is the big one.
- AFCON 2025: Morocco hosts, Dec 21 2025 - Jan 18 2026 final in Rabat. Groups: A: Morocco,Mali,Zambia,Comoros; B: Egypt,SA,Angola,Zimbabwe; C: Nigeria,Tunisia,Uganda,Tanzania; D: Senegal,DR Congo,Benin,Botswana; E: Algeria,BurkinaFaso,EqGuinea,Sudan; F: IvoryCoast,Cameroon,Gabon,Mozambique. KO from Jan 3. Final Jan 18 = Morocco vs Senegal (per Q799398).
- IRAN: Major US-Israel-Iran WAR erupts ~Feb 2026 (huge Q cluster). Protests in Iran late Dec/Jan. Possible supreme leader vacancy/interim council Feb. Strikes on Iranian cities, Gulf spillover Feb-Mar.
- AUS OPEN 2026: Melbourne, ~Jan 12-Feb 1. Men top: Sinner(1), Alcaraz(2/3). Women: Sabalenka(1). Defending W champ Madison Keys. Defending M champ Sinner.
- ELECTIONS: Bangladesh Feb 12; Thailand Feb 8 (snap); Portugal pres Jan (Ventura far-right in runoff); Nepal PM Mar 27; Bulgaria first female head of state by Feb 11.
- Chelsea: Maresca under pressure (rift w/ hierarchy) but contract to 2029, insists staying as of Dec 19. Man Utd: interim coach Michael Carrick from ~late Jan 2026 (Amorim out).

## WORKFLOW (each day)
1. Read MEMORY.md + preds.py. Call next_day already advanced date.
2. Check market.csv resolution_date column for Qs resolving in next ~10 days -> prioritize.
3. Search news (from_date= last ~3 days) for those Qs + any breaking macro news.
4. Update preds.py + re-submit ONLY changed qids (re-submitting overwrites; weight accrues from that day).
   - Also: questions whose start_date passed may now have real news -> refine.
5. Submit. Then next_day.
NOTE: Don't need to resubmit unchanged ones every day? Actually TW-score uses last active prediction (it persists). Re-submitting only matters when changing. A submitted prediction stays active until overwritten. So focus daily effort on NEW info / near-term Qs.

## DAY 1 (2025-12-24): submitted all 330 baseline preds. File: memory/preds.py, memory/submit_order.json.

## HIGH-PRIORITY TO REFINE (as news arrives)
- AFCON: group results finalize Dec 31; R16 Jan 3-6; QF Jan 9-10... wait QF Jan 14? final Jan 18 Morocco likely. Qs: 343689,703511,459037,799398,573851.
- Aus Open draw ~Jan 8-9: refine 2176,980781,789844,287417,464874,679570,922844,286957,793465,400561,891998,951896.
- Portugal pres 1st round mid-Jan: 505500 (Ventura runoff opp).
- Thailand polls late Jan: 787699,934187. Bangladesh election Feb 12: 304287,22203,223607.
- Oscars noms ~Jan 22: 876347 (One Battle After Another strong),886103.
- Super Bowl LX Feb 8; NFC champ QB 694686; winner 180958. NFL playoffs Jan 10+.
- CL knockout draw late Jan (Q85609,35131,55999,915784,167989 etc).
- Venezuela: watch for Maduro fall -> 651727. NYE plot 628026 (search Charlotte NC specifically).
- Chelsea 165622 (Maresca staying as of Dec19 - low prob new coach).
- Grammys Feb 1 (946810 - research nominees).

## KEY RESOLVED/UPDATED LOG
- 2025-12-24: baseline all 330.
- GREENLAND UPDATE (Dec 24): Trump named Jeff Landry (Louisiana Gov) special envoy to Greenland. Denmark FM Lars Lokke Rasmussen summoning US ambassador. Relevant: 269293, 630728 (maybe add Jeff Landry/Trump), 621718 (Frederiksen/Nielsen), 85534, 822586.
- AFCON groups (as of Dec 29): Nigeria won Group C (qual, top). Egypt won Group B (qual). Senegal & DRC both 4pts Group D (final Dec 30 Senegal v Benin, DRC v Botswana - DRC likely beats winless Botswana to advance). Morocco 4pts top Group A. Ivory Coast Group F. R16 Jan 3-6. Refine 459037/703511 once bracket set.
## RESOLVED RESULTS (learnings)
- 165622 Chelsea coach -> Liam Rosenior (TW -1.69, low spread limited loss). Lesson: appointments resolve to surprise names; keep spreads.
- 227432 Ukraine DefMin -> Mykhailo Fedorov (I had 0.04, TW -2.37). He was a listed candidate; should've weighted higher (he's a top Zelensky ally/DPM).
- 628026 Charlotte NYE -> Mint Hill (a real Charlotte suburb plot existed; my search missed it). TW -1.02.
- 892867 Austrian skier -> Katharina Liensberger (female slalom skier; I had speed men). TW -4.09.
- 93950 measles -> South Carolina (I had 0.55!). TW +61.78. BIG WIN.
- NET: cumulative TW 52.61. One confident-correct >> many tiny-negatives. STRATEGY VALIDATED: low spreads on speculative limit loss; invest to NAIL knowable ones early (weight accrues per day held).

## 2026-01-01: Trump began bombing Venezuelan LAND (Al Jazeera). Maduro still in power, releasing prisoners (conciliatory). Q651727 trimmed (no interim pres by Jan2). T20 WC 2026 Feb7-Mar8 India+SL; India-Pak Feb15 Colombo neutral -> 468637 Sri Lanka stays 0.55.

## 2025-12-25: scanned. No material change. NYE plot = California "Operation Midnight Sun" (TILF), NOT Charlotte NC -> Q628026 likely no valid Charlotte answer, keep low spread. Venezuela: Maduro still in power, escalation continues. AFCON openers done (Egypt, SA, Senegal, DR Congo, Nigeria, Tunisia, Algeria, Ivory Coast winning starts). Predictions persist; only resubmit on material change. Next deep refinement: ~Dec 31 (AFCON groups final) & Jan 8 (AO draw).

## 2026-01-02 results: Bangladesh->Sri Lanka (TW +74.66!), Venezuela interim->Delcy Rodriguez (had 0.06, TW +12.46). Cumulative TW 139.72. LESSON: always include the establishment/obvious fallback answer (VP, incumbent, co-host) even at low prob - huge payoff if it hits. Maduro still around Jan2 (offering US talks) despite Delcy interim resolution. AFCON R16: Morocco v Tanzania Jan4; QF Jan9-10. Hakimi ANKLE (not calf) returning; El Kaabi is Morocco star. 935533 Starlink->Venezuela 0.55 (crisis fit).

## 2026-01-03: TW 220.82 (Starlink VEN +73.69, Ounahi +7.41). US STRIKES INSIDE Venezuela; Trump "US will run Venezuela until safe transition" - major. Ukraine reshuffle: Budanov->chief of staff, Fedorov->DefMin(confirmed), Shmyhal->energy min/1stDPM. AFCON R16: Algeria v DR Congo Jan6 -> 703511 Algeria 0.5. Morocco SF path opp from {Nigeria,Algeria,DRC,Mozambique} -> 459037 updated. Aleppo ISIS suicide bombing -> 369962 ISIS 0.5. 709715 lowered (candidates reshuffled away).

## 2026-01-04: TW 218.56. 709715->Chrystia Freeland (Canadian, surprise; low spread saved). MADURO CAPTURED Jan3 by US military, held in NYC, US to "run Venezuela"+tap oil. Greenland tensions escalating (Katie Miller "SOON"). Jan5 resolvers updated: 915183 Minnesota 0.38 (massive MN Somali fraud op), 814175 US 0.55. 369962 ISIS, 703511 Algeria, 630728 Trump - kept.

## 2026-01-05: TW 333.31 (Parchin +42.76, US-WC +29.61, SDF-Aleppo +23.70, MN +7.02, Rubio +7.12, Algeria +4.55). LESSON: correct EARLY (TW accrues/day); 2nd-choice at ~0.18 still scores + when top wrong. Jan6 resolvers: 278197 CBP/ICE 0.34/0.32 (Minneapolis = Bovino CBP/BorderPatrol-led), 857643 Board of Peace 0.6. UPCOMING: AO draw ~Jan8-9 (12+ tennis Qs), AFCON QF Jan9-10/SF Jan14/final Jan18, Portugal pres ~Jan18.

## 2026-01-06: TW 471.00 (ICE Minneapolis +59.07, BoardOfPeace +78.61). LESSON: don't tinker away from strong baseline w/o strong signal (my CBP shift was slightly off, ICE baseline was right - still won). Jan7 resolvers 269293/822586/85534 left as-is (Washington 0.5 / Carney spread / Arctic mission low - no new signal, avoid over-tinker). Greenland: Denmark/GL requested Rubio meeting; Trump says Greenland decision "~2 months". NEXT: AO draw ~Jan8-9 -> refine tennis Qs.

## 2026-01-07: TW 429.48 (down: 269293 "White House" not "Washington" -27.44; Carney->Qatar -11; Arctic Sentry -3). KEY LESSON: location/venue Qs resolve to EXACT string - hedge variants (White House/Washington/State Dept) & don't put 0.5 on one phrasing. Jan8: 812287 rebalanced (Ford in Caribbean not ME -> Nimitz/Vinson/GeorgeWashington), 787699 People's Party 0.55. Carney trip = Beijing then QATAR (note for any other Carney Qs). NEXT: AO 2026 draw imminent (~Jan8-9).

## 2026-01-08: TW 440.91. AO 2026 = Jan 18-Feb 1 (NOT Jan 12!). Brisbane Intl: Sabalenka cruising, faces Keys in QF (so Keys NOT final opp). Swiatek/Gauff at United Cup not Brisbane. AFCON QF set: Jan9 Mali-Senegal, Cameroon-Morocco; Jan10 Algeria-Nigeria, Egypt-IvoryCoast. Morocco SF opp = Algeria/Nigeria winner (459037 -> Nigeria .38/Algeria .36, ~26% Morocco-out). Grok CSAM scandal: India/Malaysia/Brazil/EU probing, none banned yet (45659 spread India/Brazil/Malaysia/France). Yemen: PLC vs STC, "National Shield"/"Homeland Shield" forces (797906 updated). Qatar recurring answer. NEXT: AO main draw ~Jan15-16 -> refine ~10 tennis Qs then.

## 2026-01-09: TW 445.29 (Nigeria SF +29.86, Taiwan deficit +7.08; losses: Indonesia Grok, Yemen "Supreme Military Committee", Kostyuk Brisbane). Iran nationwide anti-Khamenei protests (econ collapse, rial 1.4M/$, 27+ killed). Jan10: 291796 Kerala 0.78 (Nipah=Kerala base rate), 69214 -> Sistan-Bal/Chaharmahal-Bakhtiari(Lordegan 30 wounded)/Kermanshah, 934187 Natthaphong Ruengpanyawut 0.42 (PP consistently tops Thai PM polls). NOTE name-spelling risk (use common news transliteration). NEXT: AO main draw ~Jan15.

## 2026-01-10: TW 368.55 (BIG DROP: Nipah->WestBengal not Kerala -49 [overconfident 0.78 prior!]; Iran province->Isfahan -15; Thai PM right name but baseline had wrong spelling -> net -12). CALIBRATION RULE: cap base-rate priors at ~0.6 (not 0.78+) unless near-certain; get name SPELLING right from day1. Jan11: Amorim SACKED Jan5, Fletcher interim, Solskjaer/Carrick in talks ->474377 Fletcher .32/Solskjaer .26/Carrick .24. Syria army vs SDF Aleppo (Sheikh Maqsoud) -> 138247/756891 SDF .52/.55. Israel recognized Somaliland+Saar visit -> 783773 add Israel .22. House passed CJS/Interior/Energy minibus.

## 2026-01-11: TW 401.57 (recovered). Carrick Man Utd derby +73.82 (long baseline hold WON despite my Jan10 reduction - DON'T 2nd-guess good baselines!). UAE was answer for BOTH Somalia Qs (over-anchored Ethiopia). Syria Kurdish force resolved as "PKK"/"Kurdistan Workers' Party" NOT "SDF" (entity-label specificity). 80352->DHS not Interior (ICE funding fight). Jan12 resolvers (117844 Poroshenko 0.5 / 359260 Betar / 98159 Atletico CdR) - no new signal, left as-is. Chelsea's Rosenior 1st game (confirms 165622). Atletico lost Supercopa SF to Real Madrid.

## 2026-01-12: TW 399.84. 117844->Tymoshenko (had Poroshenko 0.5, Tym 0.12 #2 softened). 359260->"Betar US" (had "Betar" - STRING again!). 98159->Real Betis (flat spread #2 +17). RULE: use precise official names; when 2 string-forms plausible, split prob across both. Jan13: 214384 NY 0.45 ("Operation Salvo" NYC), 806810 "Technocratic Committee" 0.3+variant. Gaza: Board of Peace dir = Mladenov; technocratic committee names NOT yet announced (71 may be unanswerable). NEXT: AO main draw ~Jan15.

## 2026-01-13: TW 401.41. 756639->Thailand +40 (2-candidate cluster both covered=reliable win pattern). 214384->Maine (NY 0.45 bump backfired -18; "which state" keeps surprising-> cap <=0.3). 75613->Qatar AGAIN (Qatar = recurring answer for Gulf/mediator/host Qs!). AO draw THU Jan15 (seeds: M Alcaraz1 Sinner2 Zverev3 Djokovic4; W Sabalenka1 Swiatek2 Anisimova3 Gauff4 Rybakina5 Pegula6 Keys7). Venus WC, struggling (lost Hobart/Auckland R1). 736847->Somalia bump (US cut all Somalia aid Jan8, WFP crisis). 279531 Caribbean 0.6 (US armada Venezuela, strong). NEXT: post-AO-draw Jan15 refine tennis Qs (2176,980781,789844,287417,464874,679570,922844,286957,793465,400561,951896).

## 2026-01-14: TW 389.65 (Caribbean armada -39.8 -> "big armada" was MIDDLE EAST not Caribbean! confirms RULE: cap geo/region guesses <=0.4). CBA basketball +24.8 (flat spread won). Jan15: 406433 Guehi spread (City wants Jan, LFC summer, open race), 599463 Pritzker 0.38 (MN/IL DOJ sanctuary list, lawsuits), 972999 Sweden 0.35, 172391 Christmas 0.35 lowered. 579233 Arabic 0.82 kept (locked fact). AO DRAW = Jan15 (tomorrow) -> next session research draw for tennis Qs: 2176,980781,789844,287417,464874,679570,922844,286957,400561,951896.

## 2026-01-15: TW CRASHED 389->259 (-130!). 579233 Syria language Arabic 0.82 -> KURDISH (-57!!). 172391 Syria festival -> "Newroz" (had "Nowruz" -spelling). 406433 Guehi->Man City (#2).
### *** BIGGEST STRATEGIC LESSON ***: These Qs are GENERATED FROM SURPRISING NEWS. The answer is the NEWSWORTHY TWIST, NOT the boring default. "Why would Syria 'declare' Arabic (already official)? -> because they declared KURDISH." NEVER assign >0.55 from prior/default reasoning; only >0.6 with DIRECT news confirmation of the actual outcome. Default-reasoning baselines are systematically biased wrong.
### AO 2026 draw (Jan15): R1: Sinner-Gaston, Alcaraz-Walton, Djokovic-PedroMartinez, Sabalenka-Rakotomanga(WC), Swiatek-qualifier, Gauff-Rakhimova, Keys-Oliynykova, Venus-Danilovic. Djokovic+Sinner same half; Alcaraz+Zverev same half. Keys(9) bottom half proj R4 vs Pegula(6) then Anisimova(4). Raducanu projected Sabalenka R3 (->464874 Raducanu 0.38). Starts Jan18, W final Jan31, M final Feb1.
### Syria: SDF left Aleppo (Sheikh Maqsoud); army closed military zone E. Aleppo (Maskana/Deir Hafer); 974205 Manbij 0.28. Q138247/756891 had resolved to PKK.

## 2026-01-16: TW 285.83 (recovered; Raqqa#2 +19.9, IndoAirTransport#3 +13.9 - SPREAD WIDE works). Jan17: 505500 Portugal Seguro 0.45 (poll: Ventura24 Seguro23 Cotrim19; runoff = Ventura+Seguro likely), 486189 Bangladesh 0.4 (India-Bangla cricket war; Pak boycotts India for Bangla), 77915/744407 LOWERED (no Spain train collision in news - likely unanswerable; reduce downside). AFCON FINAL Jan18: Morocco vs Senegal in Rabat (Morocco beat Nigeria pens, Senegal beat Egypt 1-0 Mane). 3rd place Nigeria-Egypt Jan17. T20WC: Bangladesh WON'T play in India, boycotts; venues uncertain. NEXT: AO matches Jan18+ (tennis Qs).

## 2026-01-17: TW 287.36. Spain train collision DID happen (Adamuz, train to Huelva) - lesson: events DO occur, don't gut to ~0; keep calibrated spread. 505500 Seguro +46 (poll-driven). Jan18: 904367 Aleppo 0.42/Deir Hafer 0.3 (army "full control" Aleppo + Deir Hafer/Maskana, 34 towns), 551676 Syrian govt forces 0.34 (SDF withdrawing E Euphrates per Mar10 deal). Syria recognised Kurdish language (confirms 579233 Kurdish). AFCON final Jan18 Morocco-Senegal. Daily-loop ongoing; ~70 days left to ~Mar28.

## 2026-01-18: TW 308.39 (+al-Shaddadi 551676 +38: "Syrian government forces"~="Syrian army" SEMANTIC MATCH worked!; but matching inconsistent - Nowroz/Newroz, SDF/PKK failed). 904367 also = al-Shaddadi (2 Qs same event). Bulgaria 37248 -> Iliana Iotova (VP became head of state) - PATTERN: "first female head of state"/"interim leader" = sitting VP/deputy (cf Delcy Rodriguez VEN, Iotova BG). AO day1: Alcaraz/Sabalenka/Zverev/Paolini won; Kostyuk OUT, Alexandrova OUT (Sonmez upset). Sinner/Keys start Jan20. WC: Trump travel ban hits Senegal/IvoryCoast/Iran/Haiti fans; FIFA ticket-price fury (England FA criticized). 377358/980781 left (no firm signal).

## 2026-01-19: TW 291.17. 377358 -> "KNVB" (had Netherlands 0.06; answer_type=organization -> use FA name/acronym NOT country!). RULE: match answer_type exactly (org->org name, name->person). Trump escalated Greenland: 10% tariff Feb1 on Den/Nor/Swe/Fra/Ger/UK/NL/Fin, 25% Jun1 until purchase; no framework yet. Board of Peace: Pak+India+many invited; Hungary/Vietnam ACCEPTED; 924864 Pakistan 0.48 (likely only S.Asian to JOIN). 207522 lowered Sulawesi 0.42 (no cave-paint news, calibration). AO: Sabalenka R2 vs Pavlyuchenkova/Bai; Kostyuk/Alexandrova/Cobolli out; Vondrousova withdrew.

## 2026-01-20: TW 292.78. 924864 Pakistan Board of Peace +71.6 (research win). 207522->Muna island (had Sulawesi; -40, baseline 0.62 held 25d dominated). 621718 Greenland framework->Mark Rutte (NATO!) surprise. Audited 28 hi-conf actives; trimmed speculative (14689/789042/465445/789988/348570). Jan21: 48762 Davos 0.5 + 655453 Switzerland 0.55 (US-UKR talks moved Miami->Davos WEF), 110472 Scotland 0.46 (ICC: Scotland replaces Bangladesh if pulls out, ultimatum Jan21), 273948 lowered (no NZ landslide news). PATTERN: research-driven updates on structured Qs = wins; stale "obvious" baselines = big losses.

## 2026-01-21: TW 338.35 (+46! 48762/655453 baseline UAE/Abu Dhabi held 27d = +34/+34; my Jan20 Davos override was WRONG, baseline saved it). KEY: sound structural baselines (UAE/Abu Dhabi=ME mediator) RIGHT - don't override w/ ambiguous partial news (Davos was separate US-UKR bilateral). 110472 Scotland correct but late switch=TW-1. 348570->Liverpool (Man City overconf). Oscars most noms->Sinners (not OBAA). Crans-Montana: 40 dead mostly teens, owners FRENCH (Moretti). Jan22 663866/789844 left (no signal; R4 not set). 8 days to AO finals Jan31. T20WC Feb7.

## 2026-01-22: TW 341.38. 663866->Italy (#5 0.08 +5.5, spread works). Jan23: 575662 Abu Dhabi 0.45 (Zelensky: trilateral in UAE/Emirates Jan23-24; 2nd round Feb4 likely UAE too), 243746 OMB0.3/DOJ0.22 (CA fraud=DOJ/Essayli/Bondi prosecutors), 24182 Poirier 0.2 (retired 2025, prime UFC HOF). 789042 ICE kept. UAE/Abu Dhabi = the trilateral venue (confirmed). Witkoff-Putin Moscow Thu; deal "90-95%". AO 4th rnd ~Jan25; W final Jan31 M Feb1.

## 2026-01-23: TW 433.66 (+92! ICE 789042 +71 baseline held since day1; Abu Dhabi 575662 +30). FORMULA CONFIRMED: sound structural baseline held consistently = huge TW. Jan24: 694686 NFC SB QB = Darnold(SEA) 0.5/Stafford(LAR) 0.46 (NFC champ=Seahawks v Rams Jan25, locked 2-option). 287417 Sabalenka QF=Andreeva 0.22. 286957 Keys elim=Pegula0.22/Anisimova0.18 (Keys struggling, bottom half). AFC champ=Patriots@Broncos(Stidham starting, Nix injured). SB LX Feb8 Levi's.

## 2026-01-24: TW 468.65 (Keys->Pegula +7, NFC QB Darnold +33). Jan25: 110125 Melbourne 0.4 (Invasion Day hub, monuments vandalized), 238071 N.Kordofan 0.26 (Sudan war now in Kordofan, El Fasher already fell), 267761 EU 0.2 (15% deal countries; Greenland 10->25 separate). Sudan: RSF takes Darfur, sieges Kordofan (al-Obeid/North Kordofan threatened). AO QF underway; SB LX Feb8 SEA/LAR v NE/DEN.
## 2026-01-25: TW 434.72 (Perth -21, Trikala -16: city Qs keep surprising-> cap 0.3). Jan26: 976773 Ukraine 0.34/Russia 0.3 (Chernobyl power loss, ZNPP threat, IAEA active). Trilateral talks Abu Dhabi ongoing; ZNPP/territory sticking points.
## 2026-01-26: TW 409.47 (976773->Netherlands; 3rd-party initiator pattern: 'which country requests/proposes' often a non-involved middle power - spread to NL/Norway/etc). Jan27: 465445 Makhmudov 0.34 (Fury Apr=WARM-UP not Joshua/Usyk!), 988168 Instagram 0.42. Pattern lesson logged.
## 2026-01-27: TW 361 (Joshua-baseline drag on Fury; Herzog not Netanyahu; TikTok). Jan28: 430936 Jonglei 0.6 (SSudan fighting epicenter, 180k->growing), 956334 Mali 0.28. Israel leader Australia=Herzog (910937 resolved). Board of Peace members: Israel/Egypt/Azerbaijan/Bahrain/UAE/Belarus/Morocco/Hungary/Vietnam joined.

## 2026-01-28 — CL playoff structural correction (Jan 29/30 resolvers)
Confirmed final UCL league-phase standings (Independent, Jan 28):
Seeded 9-16: 9 Real Madrid, 10 Inter, 11 PSG, 12 Newcastle, 13 Juventus, 14 Atletico, 15 Atalanta, 16 Bayer Leverkusen
Unseeded 17-24: 17 Dortmund, 18 Olympiacos, 19 Club Brugge, 20 Galatasaray, 21 Monaco, 22 Qarabag, 23 Bodo/Glimt, 24 Benfica
Bracket pairs (FIXED): 9/10 vs 23/24; 11/12 vs 21/22; 13/14 vs 19/20; 15/16 vs 17/18. Seeded host SECOND leg (first leg away). No country/rematch protection.
- 85609 Real Madrid(9) opp = Bodo/Glimt OR Benfica → 0.48/0.48 (resolves at draw Jan 30). Old wrong pred (Man City/Juve) FIXED.
- 55999 Benfica(24) opp first leg = Real Madrid OR Inter → RM 0.48 / Inter Milan 0.44. Old wrong pred FIXED.
- 261538 Newcastle(12) seeded→first leg AWAY at 21/22 city = Monaco OR Baku (Qarabag play in Baku) → 0.46/0.44. Old "Newcastle upon Tyne 0.28" was WRONG (seeded host 2nd leg).
- 35131 Juventus(13) plays Brugge OR Gala; only those 2 can eliminate; if Juve advances may resolve "Juventus" → Juventus 0.42, Brugge 0.24, Gala 0.24.
- 176447 Epstein/Commerce Sec: NO news links Lutnick/Ross to Dec 2012 island visit. Speculative; kept Lutnick 0.34 / Ross 0.30.
- 1877 Crans-Montana women DH is Fri Jan 30 (not yet raced). Low base rate of US airlift; spread Vonn 0.13/Johnson 0.10/Wiles 0.08/Macuga 0.06/Wright 0.04.
LESSON: For UCL knockout questions, ALWAYS apply the fixed bracket-pair structure + seeded-host-2nd-leg rule. Two-option 50/50 structural plays yield solid +BSS vs catastrophic old geo guesses.

## 2026-01-29 (TW 484.02, 117 resolved)
RESULTS Jan 28→29: All 6 CL/Epstein/ski Qs scored +Brier. 176447 Lutnick correct (+71.87 TW, baseline held long=huge). 1877 Vonn correct (+27.25). 85609 Benfica correct (+14.72). 261538 Baku (2nd pick, +Brier but -8.26 TW from old wrong baseline held long). 35131 Galatasaray (+0.19). 55999 Real Madrid correct (+0.53). Structural CL 50/50 plays validated.
- 316535 (Cummins T20 replacement, res Jan30/31): No announcement yet. Updated to new-call-up quicks: Abbott 0.22, J.Richardson 0.17, S.Johnson 0.13, Beardman 0.10, Starc 0.08. (Removed Ellis/Bartlett—already in 15.)
- 951896 (AO men's, res ~Feb1): SEMIS are FRI Jan30 (not Jan28). QFs done Wed: Sinner bt Shelton; Djokovic adv (Musetti retired); Alcaraz bt deMinaur; Zverev bt Tien. SF: Alcaraz-Zverev, Sinner-Djokovic. Final Feb1. Sinner clear fav (def champ, 19-match AO streak, beat Djok last 5). → Sinner 0.55, Alcaraz 0.29, Zverev 0.10, Djokovic 0.05.
- 946810 (Grammy AOTY, ceremony Feb1): **BIG FIX** — old baseline had Taylor Swift & Billie Eilish who are NOT nominated (wasted 0.34 mass!). Real nominees: Bad Bunny, Bieber, S.Carpenter, Clipse, Lady Gaga, K.Lamar, Leon Thomas, Tyler. AP leans Lady Gaga (narrative) vs Bad Bunny (zeitgeist/streaming/historic) vs Kendrick. → Bad Bunny 0.32, Lady Gaga 0.27, Kendrick 0.19, Carpenter 0.09, Tyler 0.06.
- 391811 (Ukraine miners' bus drone, Dnipropetrovsk, res Feb1): No specific incident reported yet. Weighted Marhanets/Nikopol (front-line mining towns) → Marhanets 0.22, Nikopol 0.18, Kryvyi Rih 0.18, Pavlohrad 0.14, Dnipro 0.06.
- 562701 (Balochistan town secured, res Feb4): no specific news; kept spread, revisit.
**LESSON: For ALL award/election/bracket questions, VERIFY the actual eligible candidate/nominee list before trusting baseline. Audit other award-type baselines for ineligible-name errors.**

## 2026-01-30 (TW 474.62, 118 resolved)
RESULT: 316535 → Ben Dwarshuis (unforeseeable left-arm call-up I didn't list). Brier -0.11, TW -9.41. Wide 5-name spread (sum 0.70) limited the loss. Squad call-ups w/o direct news = inherently low-hit; keep wide.
- 951896 AO: **MAJOR SWING** — SF Fri Jan30: Djokovic BEAT Sinner (5 sets); Alcaraz beat Zverev (5h27m, cramps). Final = Alcaraz vs Djokovic (Sinner OUT). Was Sinner 0.55 → would've been catastrophic. Updated to locked 2-outcome: Alcaraz 0.56, Djokovic 0.44 (Alcaraz younger/No.1/beat Djok 2025 USO final; offset by his marathon-SF fatigue vs Djok's AO mastery+beat Sinner).
- 562701 Balochistan: Jan30 AJ: 41 fighters killed — 30 in Harnai dist, 11 in Panjgur dist (Jan 29 raids). No clear single "3-day battle/town secured by police" yet. Updated spread: Panjgur 0.18, Kalat 0.15, Mastung 0.14, Harnai 0.12, Khuzdar 0.10.
- 391811 (miners' bus drone, res Feb1): still no specific incident reported; kept Marhanets 0.22/Nikopol 0.18/KryvyiRih 0.18/Pavlohrad 0.14/Dnipro 0.06.
- 946810 Grammy AOTY (Feb1 ceremony): unchanged BadBunny 0.32/Gaga 0.27/Kendrick 0.19/Carpenter 0.09/Tyler 0.06.
**LESSON REINFORCED: Re-check EVERY near-term resolver with newest news daily. Sports brackets can fully invert in 24h (Sinner→out). Never treat a 'sharpened' pred as done while active.**

## 2026-01-31 (TW 497.69, 122 resolved)
RESULTS: 391811 → Ternivka (small DTEK coal town nr Pavlohrad; not listed) Brier -0.14. 562701 → Nushki (obscure Balochistan border town; not listed) Brier -0.10. 946810 → **Bad Bunny ✓** (top pick 0.32) Brier +0.42 TW+9.96. 951896 → **Alcaraz ✓** (top pick 0.56) Brier +0.61 TW+34.66. Day net strongly +.
PATTERN: Obscure single-town/location Qs (Ternivka, Nushki, Muna, Kurdish earlier) keep costing small negatives — answer is usually a NOT-obvious small place. For these, spread wider/flatter (more candidates ~0.10-0.14 each, lower top) to cap downside; do not concentrate.
- 102687 Norway ex-PM corruption (res by Feb28): No news naming any ex-PM. Norway corruption news = PetroNor/Congo (not a PM). Solberg still only realistic (2023 Finnes share scandal). Kept Solberg 0.46/Stoltenberg 0.15/Bondevik 0.05.
- 449104 US minerals stockpile name (res by Feb29): Shaheen-Young bill proposes independent reserve body; no official WH name yet. Added "Strategic Resilience Reserve" 0.18 (likely bill name) + generic variants. Wide/low — may not resolve.

## 2026-02-01 (TW 464.29, 124 resolved) — HARDENED RULE
RESULTS: 102687 → Thorbjorn Jagland (ex-PM 1996-97; NOT Solberg). Solberg@0.46 held ~13d → Brier -0.24, TW **-27.81** (big). 449104 → "Project Vault" (unguessable codename) Brier -0.08 (wide spread saved it).
**RECURRING #1 LOSS SOURCE = overconfidence on "obvious" candidate for speculative string Qs w/ no confirming news. Subverted every time: Arabic→Kurdish, Caribbean→MidEast, Kerala→WBengal, Sulawesi→Muna, Solberg→Jagland.**
HARD RULE NOW (apply + audit actives):
 1. Speculative string Q (no DIRECT news naming the answer) + big answer space → TOP candidate ≤0.30, others flat 0.10-0.18, total allocated ≤0.70. Flat 5×0.14 vs unlisted truth = BSS≈-0.10; one@0.5 = BSS≈-0.30. Flatness caps downside ~3x.
 2. Concentrate (>0.45) ONLY when news directly confirms the specific answer, or it's a locked small option set (≤3 known options, e.g. set sports final).
 3. Re-audit any active pred with a single name >0.4 lacking confirming news; flatten it.

## 2026-02-01 cont (7 Qs resolve Feb2)
NEW TECHNIQUE: cross-question structural inference. 426743 asks WHERE Saif al-Islam Gaddafi will be BURIED → presupposes his death → 453736 ("who killed in Libya") almost certainly = Saif al-Islam Gaddafi even without a direct news hit. Set him 0.52 (clear fav, not extreme—no direct news). 976004 (probe forensic site): flat Tripoli .20/Zintan .16/Benghazi .14/Sabha .12/Zawiya .06 (Zintan = where Saif historically held).
- 220862 Man City L.Cup final opp: could NOT find Carabao Cup semi info in 4 searches → flat Arsenal .18/Liverpool .15/Newcastle .15/Chelsea .13/Spurs .10.
- 243685 Myanmar 5-member panel name: flat naming spread.
- 955662 Brazil bus crash state: no crash yet; flat MG .20/Bahia .15/SP .13/Parana .11/Pern .10.
- 995305 market fire city: no fire yet; flat Karachi .15/Lagos .10/Bangkok .09/Manila .08/Dhaka .07.
- 492629 Harden trade: no trade news; low/spread (sum .28) — may not resolve.
NOTE: NBA trade deadline Feb 5; CL playoff draw done (Newcastle→Qarabag, RM→Benfica, Juventus→Galatasaray confirms earlier 35131 Gala correct, 85609 Benfica correct, 261538 Baku correct).

## 2026-02-02 (TW 506.25, 131 resolved) — KEY WINS + MATH REFINEMENT
RESULTS: 453736 → **Saif al-Islam Gaddafi ✓ (0.52)** Brier+0.75 TW**+62.24** (cross-Q inference = top technique). 220862 → Arsenal ✓ (flat top 0.18) +0.26/+13.20. 976004 → Zintan ✓ (2nd 0.16) +0.22 (TW-8.70, old baseline). Unguessables w/ flat spread = small losses: 243685 Union Consultative Council -0.06, 492629 Darius Garland -0.02, 995305 Tehran -0.05, 955662 Alagoas -0.10.
**MATH: if truth is UNLISTED, BSS ≈ -Σp_i². Equal 5-spread summing S → loss = S²/5. S=0.7→-0.098; S=0.5→-0.05; S=0.4→-0.032.**
REFINED RULE: For no-signal obscure location/name Qs (low chance truth is in my list ~15-25%), cap TOTAL allocated ≤0.45-0.55 (5 thin outcomes), NOT 0.65-0.70. Saves ~0.04-0.05 Brier each when (usually) truth is unlisted, costs little when it is listed. Reserve higher totals only when I have real signal or a confirmed/locked answer.
TOP TECHNIQUES RANKED: (1) cross-question structural inference; (2) confirmed-news concentration; (3) locked small-option-set (sports finals/brackets); (4) flat thin spreads to cap downside on unguessables.

## 2026-02-02 cont (4 Qs res Feb3)
- 57193 SCOTUS map: DOJ urging SCOTUS to BLOCK California (Newsom Prop50) map → question = does SCOTUS reject GOP suit & let CA keep. CA is clearly THE state at issue. Raised California 0.58 (cond. on resolving to a state, ~CA; uncertainty = ruling direction/void). Tx .08/NC .06/IL .05/UT .04.
- 426743 Saif burial: confirmed killed. Strong tribal-geo prior: Qadhadhfa→Sirte; loyalist stronghold→Bani Walid. Two-town concentration justified: Sirte .30/BaniWalid .28/Sabha .10/Zintan .06/Tripoli .05.
- 336425 E.Ukraine market shelling: no event yet; Kostiantynivka = historic Donetsk market-strike city (real signal) .26; Kramatorsk .12/Pokrovsk .09/Sloviansk .07/Druzhkivka .05. (Dropped Kherson—wrong oblast; criteria=Donetsk authorities.)
- 579252 Saleh Mohammadi (19yo wrestler, real case, imminent execution per US State Dept Jan29): sentencing city unknown → Tehran .24 (Revolutionary Courts)/Mashhad .14/Karaj .10/Shiraz .08/Isfahan .06.

## 2026-02-03 (TW 577.82, 135 resolved) — strong day
RESULTS: 57193 → **California ✓ (0.58)** Brier+0.81 TW**+62.62**. 426743 → **Bani Walid ✓ (0.28, tribal-geo reasoning)** Brier+0.38 TW+32.45. 336425 → Druzhkivka (had 0.05, 5th — Brier ~0.00, incl. tail saved it). 579252 → Qom (unlisted) Brier-0.10.
KEY: including a 5th thin tail outcome turned a likely -0.05 into 0.00 (Druzhkivka). ALWAYS include 5 outcomes incl. a plausible tail.
- 180958 Super Bowl LX: LOCKED — New England Patriots vs Seattle Seahawks (Feb 8). Near-even; slight Seattle lean (#1 seed, explosive O, 41-6 & 31-27 wins) vs NE (elite D, Vrabel, 10-7). → Seattle 0.52 / NE 0.48.
- 883856 Moscow officer shot: speculative, no event. Removed STALE Kirillov (assassinated Dec2024 historically). Low flat: Gerasimov.06/Belousov.04/Alaudinov.03/Yevkurov.03/Surovikin.03 (total .19).
- 198725 Narges Mohammadi exile city: no news; kept flat Zahedan.16/Zabol.14/BandarAbbas.10/Birjand.08/Tabriz.06.
- 456284 WaPo publisher: Lewis still embattled-but-in-post Jan29, no successor named; speculative—kept low.
- 534224 Olympic W-downhill silver country (Games open Feb6): kept Switz.26/Italy.22/Austria.16/US.12/Ger.06.

## 2026-02-04 (TW 577.82, 135 resolved; no Feb3→4 resolutions)
- 976004 confirmed Zintan via Feb4 AJ (Saif killed in Zintan, forensics sent there) — already scored +.
- 883856 (Moscow officer shot, res Feb5): still NO such shooting in news → keep low flat spread (.19 total). No-signal speculative.
- 456284 (WaPo publisher post-Lewis, res Feb6): Feb4 — massive layoffs; Lewis "absent from staff calls, not present much"; Exec Editor **Matt Murray** repeatedly cited as the one running paper/addressing staff (Don Graham praised Murray). Raised Matt Murray 0.30 (de facto leader; but title is "publisher"≠exec editor & Lewis not formally stepped aside → kept moderate). Winnett.07/Barr.04/Graham.04/Bezos.03.
- 198725 (Narges Mohammadi exile city, res Feb6): no news of her new sentence → kept flat Zahedan.16/Zabol.14/BandarAbbas.10/Birjand.08/Tabriz.06.

## 2026-02-05 (TW 577.05, 136 resolved)
RESULT: 883856 → Vladimir Alekseyev (GRU deputy, unguessable). Brier -0.01, TW **-0.77** ONLY — validates: no-signal speculative w/ low total (0.19) ≈ near-zero loss. KEEP THIS DISCIPLINE.
- 198725 (Narges Mohammadi exile city, res Feb6): still no news of her new sentence; kept flat (no churn).
- 456284 (WaPo publisher, res Feb6): Feb5 — Murray still titled EXEC EDITOR; Lewis NOT formally stepped aside, no successor publisher named. Question may void/not resolve. Kept Murray 0.30 + low spread (hedge both ways).

## 2026-02-06 (TW 569.08, 138 resolved)
RESULTS: 198725 → Khosf (tiny S.Khorasan exile town, unguessable; Iranian internal exile = ultra-remote) Brier-0.07. 456284 → Jeff D'Onofrio (ex-Disney; Murray was a TRAP—exec editor≠publisher) Brier-0.10 TW-1.45 (cap at 0.30 limited it).
LESSON: role/title mismatch trap — if Q asks for role X and the prominent news figure holds role Y, cap that figure ≤0.20 (don't treat as strong signal). 
- 180958 Super Bowl LX (game Feb8): Seahawks confirmed **4.5-pt betting favourites** + ex-QB consensus → sharpened Seattle 0.63 / NE 0.37 (market-implied).
- 534224 W-downhill silver country (race Sun Feb8): Vonn (USA) top-3 in ALL 5 DH WC this season (strong); Goggia (ITA) home fav; SUI deep. Reweighted Italy .23/Switz .22/USA .19/Austria .15/Ger .06.

## 2026-02-07 (TW 590.18, 140 resolved)
RESULTS: 180958 → **Seattle Seahawks ✓ (0.63, betting-line calibrated)** Brier+0.73 TW+25.07. 534224 → Germany (silver; I had 0.06 tail) Brier-0.04 — tail inclusion again limited loss.
TECHNIQUE CONFIRMED: calibrate locked 2-team sports to betting spread (4.5pt≈63%). Keep including a plausible 5th tail.
- 318661 Colombia resume talks: EGC/Gulf Clan Doha talks SUSPENDED Feb4 (group-side, over Petro targeting their leader Chiquito Malo; Def Min confirmed target). Resumption uncertain but ALL active peace-talk news = EGC. Weighted EGC variants combined ~.52 (GulfClan .24/ClanDelGolfo .16/Gaitanist .12) + ELN .18 hedge.
- 398988 Lebanese group Israel abducted official: strong structural prior Hezbollah (Israel S.Lebanon raids overwhelmingly vs Hezbollah). Hezbollah 0.55/Amal .12/Hamas .07/PIJ .04.
- 538697 country 8000 Gaza troops by June: Indonesia most vocal on large Gaza contribution → Indonesia 0.42/Azer .13/Egypt .10/Pak .09/Tur .07.
- 630740 Lebanese building collapse ≥15: no event in news (collapses were India); Beirut prior (dense/old/war-damaged) 0.30 + Tripoli .15/Sidon .09/Tyre .08/Nabatieh .05.

## 2026-02-08 (TW 640.95, 144 resolved) — HARD CEILING RULE
RESULTS: 538697 → **Indonesia ✓ (0.42)** Brier+0.62 TW**+53.59**. 630740 → **Tripoli** (had .15, 2nd) +0.17 TW+24.98. 318661 → **Gulf Clan ✓ (.24 top)** +0.35 (TW~0, old baseline drag). 398988 → al-Jamaa al-Islamiya (NOT Hezbollah!) — Hezbollah@0.55 → Brier **-0.32 TW-27.70**.
**THE #1 RECURRING LOSS, AGAIN: overconfident "obvious/structural" ACTOR on identity Q w/o DIRECT confirming news. Hezbollah felt 'obvious' (Israel raids S.Lebanon=Hezbollah) but truth = obscure Sunni group al-Jamaa al-Islamiya. Same as Solberg→Jagland, Arabic→Kurdish, Sulawesi→Muna.**
HARD CEILING (non-negotiable): For "who/which-group/which-person was killed/abducted/named/appointed" identity Qs WITHOUT a news item directly naming that specific answer: TOP ≤0.35, spread rest flat. EV math: concentrating 0.35→0.55 gains ~+0.15 if right but loses ~ -0.19 if wrong; these priors are subverted ≥40% → net negative. Only exceed 0.35 with (a) direct news naming it, (b) cross-question structural lock, or (c) ≤3-option locked set.
Cross-Q inference (453736) & locked sports (180958) & confirmed-policy (538697 Indonesia) remain the big winners. Stay disciplined.

## 2026-02-08 cont (5 Qs res Feb9) — applied hard ceiling
- 14689 school mass shooting country: US base-rate dominance (~80-90% of school mass shootings) → US 0.46 (justified base-rate, not subverted-actor). +small spread.
- 312764 Egypt planning min: no reshuffle news; incumbent Al-Mashat capped 0.33 (hard ceiling) + flat.
- 487245 country tension re Trump late-Feb address: Venezuela hottest (Jan US military action) → Venezuela 0.30/Iran 0.22/China .12/Russia .10/Colombia .07.
- 527803 Canada school shooting town: very rare event, no news → LOW total 0.40 flat (likely won't occur/resolve).
- 745180 Cyclone Gezani comparison: no Gezani news; Madagascar-landfall → Freddy .28/Batsirai .20/Idai .20/Enawo .08/Gombe .06.

## 2026-02-09 (TW 637.37, 149 resolved) — CROSS-QUESTION LINKING (critical)
RESULTS: 487245 → **Iran ✓** TW**+59.97** (baseline Iran 0.42 held long = big; my late Venezuela switch was slightly wrong but low-weight — DON'T 2nd-guess sound long baselines late). 14689 → **Canada** (had US 0.46) Brier-0.22 TW-22.59. 312764 → Ahmed Rostom (unguessable) -17.98. 745180 → Geralda (1994 Madagascar benchmark cyclone, omitted) -17.04. 527803 → Tumbler Ridge (low flat, -5.95).
**HUGE MISS: 14689 ("country of secondary-school mass shooting") + 527803 ("town of deadly school shooting IN CANADA") = SAME EVENT. 527803's existence was DIRECT evidence 14689=Canada, not US. I treated them independently.**
RULE: EVERY day, scan ALL active questions for CLUSTERS that reference the same event/topic. If Q-B presupposes a specific fact (country/person/place), use it to set Q-A. This is the SAME technique that won +62 on Saif Gaddafi (453736←426743). Systematically cross-reference. Build cluster map for near-term resolvers.
ALSO: historical-analog Qs → include the canonical region-specific benchmark (Madagascar cyclones: Geralda 1994, Gafilo 2004, in addition to Freddy/Batsirai/Idai).

## 2026-02-09 cont (clusters scanned; next res Feb11-13)
- 901381 Italy rail cables: DIRECT NEWS — sabotage Feb7, "fire targeted the line between **Bologna and Venice**", cables severed in Bologna. Concentrated "Bologna and Venice" 0.55 (exception a: direct news) + Milan-Bologna .18 (knock-on).
- 304287 Bangladesh main opposition: Feb8 survey BNP 34.7% vs Jamaat 33.6% (tight); NCP in Jamaat alliance. If BNP governs (modal) → main opp = Jamaat. Jamaat-e-Islami 0.40 / BNP 0.22 / NCP .13 / Jatiya .10 / AL .03.
- 652747 Navalny toxin: established fact = Novichok (2020 OPCW). Strong factual base (not subverted-actor) → Novichok 0.66 + nerve-agent variants.
- 739916 2nd carrier ME: Lincoln already there ("massive armada" vs Iran); no 2nd carrier named → Ford 0.28 (newest/surge) flat ≤ceiling.
TODO next days: 795774 (French far-right activist killed, Macron-Meloni, res Feb12 — flatten if no event), 613203 (Tractor FC AFC, res Feb11 — flat, no draw). Watch clusters: T20 WC (190197/307616/454482), Pak-Afghan strikes (26859/493481), Bangladesh cabinet (22203), Olympics (162065/221278/207951).

## 2026-02-11 (TW 632.26, 150 resolved)
RESULT: 613203 → Shabab Al-Ahli (had 0.08 tail) Brier +0.09 (tail saved it; TW -5.11 old-baseline drag). Confirms: always 5 outcomes incl. realistic tail.
- 304287 Bangladesh (vote Feb12): consensus = BNP wins govt, Jamaat best-ever but won't govern → Jamaat = main opposition (modal). Bumped Jamaat-e-Islami 0.45 (well-grounded election forecast, not wild guess) / BNP 0.22 / NCP .12 / Jatiya .08 / AL .02.
- 795774 French far-right activist killed/Macron-Meloni: NO such event in news (Meloni news = anti-Olympics protesters Milan, unrelated). Speculative non-event → flattened/lowered total 0.50 (Paris .18...).
- 739916 2nd carrier: Feb10 buildup = Lincoln + destroyers only, NO 2nd carrier named. Kept Ford 0.28 flat (no change).
Cross-cluster note: Saif Gaddafi killed in Zintan by 4-man commando; timing ~48h after US-brokered Paris meeting Saddam Haftar/Dbeibah — relevant to any Libya follow-on Qs.

## 2026-02-12 (TW 740.80, 153 resolved) — BIG +108 DAY
RESULTS: 304287 → **Jamaat-e-Islami ✓ (0.45)** Brier+0.63 TW**+49.04**. 739916 → **Gerald R. Ford ✓ (0.28)** Brier+0.42 TW+38.25 (sound prior held long). 795774 → Lyon (had .12, 2nd, flattened) Brier+0.18 TW+21.25 (lowered-but-listed still won).
Validated: well-grounded election/structural forecasts + sound priors held long + always-list-5 = compounding gains. TW 632→740.
- 652747 Navalny: established Novichok; no change (0.66). Res Feb13.
- 901381 Italy rail: anarchists claimed it; Reuters "fire targeted line between Bologna and Venice"; no change (Bologna and Venice 0.55). Res Feb13.

## 2026-02-13 (TW 683.67, 155 resolved) — BOTH "EXCEPTION" CONCENTRATIONS FAILED
RESULTS: 652747 → **epibatidine** NOT Novichok (had 0.66) Brier**-0.45** TW**-44.56**. 901381 → **Rome and Naples** NOT Bologna-Venice (had 0.55) Brier-0.34 TW-12.57.
**Both hard-ceiling EXCEPTIONS backfired same day:**
 - 652747: "established fact" (2020 Novichok) ≠ NOVEL 2026 scenario finding. Q asked what 5 govts find NOW in tissue → scenario can invent anything (epibatidine). Historical fact ≠ new-finding answer.
 - 901381: "direct news" — I matched the WRONG incident. News = Bologna sabotage; Q's "HSR section investigated for burned cables" = Rome–Naples (Italy's flagship HSR). Conflated a related-but-different event.
TIGHTENED RULE (supersedes prior exceptions):
 (a) "Established/historical fact" is NOT confirming news when the Q asks about a NEW finding/announcement/event in-scenario. Treat as speculative → cap ≤0.45.
 (b) "Direct news" concentration >0.50 ONLY if the article explicitly answers THIS Q's exact incident/framing (same event, same entities). Any ambiguity about incident-match → cap ≤0.40.
 (c) Default hard ceiling 0.35 for identity/specific-fact Qs stands; 0.45 max even with strong priors; >0.55 ONLY with an article literally stating the answer to the exact question.
Net still strong (cum TW 683). Discipline > occasional big hits. Stop over-concentrating.

## 2026-02-13 cont (T20 cluster, next res Feb15)
T20 WC 2026 (Feb7–Mar8): GrpA India/Pak/USA/Neth/Namibia; GrpB Aus/SL/Ire/Zim/Oman; GrpC Eng/WI/Nepal/Italy/Scot; GrpD NZ/SA/Afg/Can/UAE. Top2/grp→Super8. Afghanistan 0-2 likely out. Pak beat Neth, played USA Feb10.
- 190197 team Pak defeats to clinch Super8 berth: FIXED (had wrong non-GrpA teams Ireland/Oman). → Namibia 0.32 / USA 0.26 / Neth 0.16 / India 0.07.
- 454482 former champ to miss Super8: spread Pakistan .24/SL .22/WI .18/Eng .16/Aus .06 (Eng&WI both strong in weak GrpC→both likely advance; Pak USA-upset risk). CROSS-LINK: if Pak qualifies→454482≠Pak & 190197 resolves.
- 778783 Sudan market drone ≥28: heavy RSF strikes N.Kordofan/El Obeid → El Obeid 0.24 flat.
- 580089 NW Pakistan motorcycle bomb district: no news; kept flat Bannu/DIKhan/Bajaur/Peshawar/Tank.

## 2026-02-14 (TW 683.67, 155 resolved; no Feb13→14 res)
- 190197: Pak beat Neth+USA (4pts/2g); India tops GrpA on NRR; Pak-India Sun. Process-of-elim: clinching win = vs **Namibia** (weak, unplayed). → Namibia 0.46/India .18/USA .16/Neth .08 (structural, capped 0.46).
- 580089 NW Pak motorcycle bomb police stn: DI Khan = hottest (5 police killed there Feb11) → DIKhan 0.22/Bannu .16/Bajaur .12/Tank .10/Peshawar .09 flat.
- 778783 Sudan market drone ≥28: RSF strikes heavy in Kordofan; UN says markets hit in N/S Kordofan → El Obeid 0.22/Kadugli .12/Kosti .12/Dalanj .10/Sennar .08 flat.

## 2026-02-15 (TW 710.83, 158 res) — 7 Qs res Feb16
RESULTS: 190197→Namibia✓(0.46)+13.98. 580089→Bannu(.16,2nd)+23.99. 778783→Sodari(unlisted N.Kordofan town)-10.81. Cum 710.
- 548734 storm France: DIRECT — "Storm Nils" hit France/Spain/Portugal Feb11-13, "unusually strong", 900k power out, flooding. → Storm Nils 0.60 (direct-news exact match).
- 207951 broadcaster removed Israel-bobsleigh segment: RAI/RaiSport mired in Olympics commentary fiasco (Petrecca gaffes) BUT not confirmed = Israel-bobsleigh incident → NOT direct match → RAI 0.30 capped / BBC .22 / Eurosport .12 / NBC .10 / NRK .06.
- 454482 former T20 champ to miss Super8: WI qualified (drop). India safe. Eng shaky (lost WI, barely beat Nepal) → England 0.27 / SL .22 / Pak .20 / Aus .08 / WI .02.
- 22203 Bangladesh only-woman cabinet min: BNP landslide (209 seats), cabinet sworn Feb17; only 7 women MPs (6 BNP). No list yet → flat low BNP-women (Rumeen Farhana .13...) total .43.
- 456938 Rousey / 876124 StPetersburg blast / 903473 Vinicius-Benfica: kept low/flat (speculative, no news).

## 2026-02-16 (TW 672.69, 165 res) — TEMPORAL-FRAMING TRAP (3rd time)
RESULTS: 876124 → **Sertolovo ✓ (0.05 tail!)** +7.75 (tails win AGAIN — always include 5). 207951→RTS(Swiss, not RAI; contextual-signal trap) -16.56. 454482→Australia(.08; surprise collapse) -14.62 old-drag. 548734→Storm **Pedro** NOT Nils (had 0.60) Brier-0.37 (only TW-3.71, 1-day weight = lucky). 22203/456938/903473 → unlisted, low-flat limited losses (-2 to -6).
**TEMPORAL-FRAMING TRAP (Navalho, Italy-rail, now Storm Nils = 3rd):** Q with prospective framing ("poised to / will batter / by [future date]") + news describing a PAST event → that news is NOT a confirming match. The answer is a FUTURE/different item (Pedro, not Nils). 
RULE: Before concentrating on "direct news", check TENSE/TIME match. Past-event news ≠ future-framed Q. If mismatch → speculative, cap ≤0.35. Only >0.5 if news explicitly answers the exact Q with matching time-frame.
Net: still cum 672 (strong vs 0 baseline). Stop over-concentrating; tails + flat spreads are reliably net-positive; big concentrated bets only on truly locked/confirmed-same-frame facts.

## 2026-02-16 cont (res Feb17: 307616, 479547)
- 307616 Pak Super8 opener opp: Qualified=India,WI,SA; Pak needs beat Namibia. A1(India)&A2(Pak) go to SEPARATE Super8 groups → India CANNOT face Pak (was my 0.26 top — FIXED, dropped India). Pak plays all in Colombo. Spread SA 0.24/Eng .18/SL .16/Aus .12/WI .10.
- 479547 Iranian frigate sunk off Sri Lanka: no news; heavy US-Iran maritime escalation (US boarding tankers Indian Ocean). Flat over Iran frigates: Alborz .22/Jamaran .20/Dena .16/Alvand .12/Bayandor .06 (kept).

## 2026-02-17 (TW 661.82, 167 res) — STRING-MATCH loss
RESULTS: 307616→New Zealand (NZ=D2 seed in Pak's Super8 grp; not listed) Brier-0.14 TW+2.34. 479547→**IRIS Dena** — I had "Dena" 0.16 but string≠"IRIS Dena" → scored as MISS -0.13/-13.20. **STRING-MATCH FAILURE (recurring: Washington/WhiteHouse, Newroz, SDF/PKK).**
RULE: For named ships/people/orgs with standard prefixes/titles, INCLUDE BOTH bare & prefixed variants among the 5 outcomes (e.g., "IRIS Dena" AND "Dena"; "HMS X"/"X"; full official name AND common short). Diacritics & prefixes cost real points. When answer_type hints format, mirror it.

## 2026-02-17 cont (res Feb18: 207254,485328,943026)
- 943026 AI tool Dutch court bars (sexual imagery): MASSIVE Grok deepfake scandal (EU/Ireland/Brazil/Indonesia/UK/France crackdowns) → Grok favored 0.38; but civil nudify rulings classically target apps → Clothoff 0.22 hedge; SD .10/MJ .06/DeepNude .05.
- 485328 Dem SOTU response: no announcement; Wes Moore prominent (Trump snub, only Black gov) → Moore .16/Beshear .13/Whitmer .12/Jeffries .09/Slotkin .05 flat.
- 207254 US office France-US row reposted comments: no clear specific news; Trump/WH notorious reposts + embassy plausible → US Embassy France .30/WH .20/State .16/OVP .08/NATO .04.

## 2026-02-18 (TW 684.43, 170 res)
RESULTS: 943026 → **Grok ✓ (0.38)** Brier+0.55 TW**+46.01** (dominant-context signal + capped 0.38 = ideal). 207254→Bureau of Counterterrorism (unguessable) -17.62. 485328→Abigail Spanberger (newly-elected VA gov; not listed) -5.78. NOTE: for "who gives party response/role" consider RECENTLY-ELECTED swing-state officials.
- 325000 group Israel says ran Lebanon command centre: base rate Israel→Hezbollah high, but Feb15 news shows Israel ALSO attributing PIJ in Lebanon → moderated Hezbollah 0.58 (not 0.66; respects 398988 burn) / PIJ .14 / Hamas .10 / Amal .04.
- 434350 SA T20 capt NZ tour: Markram = incumbent T20 capt, in form (86 v NZ); post-WC rotation risk → Markram 0.42 / vdDussen .12 / Ferreira .08 / Miller .07 / Stubbs .06.

## 2026-02-19 (TW 641.01, 172 res) — ENFORCE 0.35 CAP, NO MORE EXCEPTIONS
RESULTS: 325000→**Hamas** NOT Hezbollah (had Hez 0.58) Brier-0.17 TW**-24.67**. 434350→**Keshav Maharaj** NOT Markram (had 0.42) Brier-0.21 TW-18.75. Day -43.
**DEFINITIVE PATTERN (now ~6+ instances): over-concentrating an "obvious" incumbent/dominant ACTOR on a future-announcement identity Q WITHOUT direct news = systematic loss. Subverted: Solberg→Jagland, Hezbollah→alJamaa, Hezbollah→Hamas, Markram→Maharaj, Murray→D'Onofrio, Lutnick(early). Resolvers favor NON-obvious answers.**
ABSOLUTE RULE GOING FWD: identity/who/which-actor Q resolved by a FUTURE announcement & no article naming the exact answer → TOP ≤0.33, ≥4 outcomes, spread flat. NO exceptions for "base rate"/"incumbent"/"dominant context"/"established fact about a NEW finding". Concentrate >0.45 ONLY: (1) article explicitly states THIS answer w/ matching timeframe, (2) cross-Q structural lock, (3) locked ≤3-option set / set sports final, (4) betting-line 2-way.
Net still +641 cum (avg ~+3.7/resolved). Winners = flat spreads, tails, cross-Q inference, locked sports, confirmed-news. Drain = obvious-actor over-concentration. DISCIPLINE.

## 2026-02-20 (TW 660.86, 174 res) — 6 res Feb21
RESULTS: 26859→"Nangarhar and Paktika" (PLURAL combined string; I had singles) Brier-0.12. 59953→**Crete ✓ (0.22)** +31.73. PLURAL answer_type lesson: include combined "X and Y" options.
- 221278 men's hockey gold: **CONFIRMED — "United States earn gold, revenge OT win over Canada" (Straits Times Feb20), Switzerland bronze.** Concentrated US 0.90 (confirmed-result direct news, exact match).
- 73075 ambassador France summons re Quentin Deranque: CROSS-Q LOCK — Deranque=Lyon far-right activist (795774); confirmed Macron-Meloni row Feb19-20, Italy PM office statement. → Italy 0.62 (cross-Q + direct-news of the specific row; capped 0.62 as 'summon' action not yet explicit).
- 162065 country 30 medals new record: Italy host at 26 (Feb19), Norway 34 (not record for them). Italy ~30 = new natl record. Italy 0.32 (capped, "exactly 30" risky) / Neth .14 / Fra .12 / Swi .10 / Swe .06.
- 493481 country condemns Pak strikes on Afghan: strikes confirmed (26859). Afghanistan obvious condemner but cap → Afghanistan 0.34 / Iran .16 / Qatar .12 / Tur .08 / Saudi .07.
- 109135 (Ukr double-tap city) & 489825 (Iran Kurdish alliance acronym): kept flat/low (speculative).

## 2026-02-21 (TW 668.55, 180 res)
RESULTS: 221278→**US ✓ (0.90 confirmed-result)** Brier+0.99 TW+27.90. 162065→**Italy ✓ (0.32 host-overperf)** +32.48. 489825→CPFIK (unguessable; low total .24) only -2.00. 109135→Lviv (flat, -8.88). 493481→**India** NOT Afghanistan (had .34; obvious-victim subverted AGAIN; cap saved half) -13.69. 73075→**Charles Kushner** (US amb!) NOT Italy (had .62 cross-Q to Italy) Brier-0.40 TW-28.13.
LESSONS: (1) 73075 cross-Q inference FAILED — France summoned US amb (Kushner) over US figures' comments, not Meloni/Italy. Cross-Q lock must verify WHICH thread; & answer_type="name" → give PERSON name not country (format mismatch compounded loss). (2) "obvious victim condemns" subverted→India; 0.34 cap limited damage — KEEP CAPPING. (3) Confirmed-result (US hockey 0.90) & host-overperf (Italy) & low-total-unguessable = reliable winners.
RULE ADD: Always match answer_type format (name→person; country→country; acronym→letters). Re-read answer_type before finalizing.

## 2026-02-21 cont (res Feb22: 992626)
- 992626 Group1 Super8 first place by Feb25: Group1 = **India, South Africa, West Indies, Zimbabwe** (Group2=Eng/NZ/Pak/SL). My old pred had Australia/England/NZ — ALL WRONG (not in Grp1). Fixed: India 0.45 (strongest, hosts Grp1 in India=low rain) / SA 0.30 / WI 0.15 / Zim 0.04. Australia eliminated in group stage (biggest shock).

## 2026-02-23 (TW 676.98, 183 res)
RESULT: 648994→Border Patrol Police (NOT Royal Thai Army; obvious-org subverted again; 0.34 cap held loss to -17). 654360→**Minas Gerais ✓ (0.30, base-rate, long hold)** Brier+0.42 TW**+42.99**.
- 392014 DRC mass graves city: no specific news; M23 epicentre → Goma 0.30/Bukavu .20/Beni .14/Bunia .10 (flat, kept).
- 632535 Spain final WC warm-up opp: no news (France-Brazil Mar26 noted, not Spain); flat/low kept.
- 726747 UK mosque axe tarawih city: no incident yet (Ramadan ~Feb18+); London 0.30/Bham .18/Man .12/Bradford .08/Leeds .06 flat.
All 3 speculative no-info → flat per cap rule, no resubmit needed.

## 2026-02-24 (TW 663.06, 186 res)
RESULTS: 392014→Uvira (S.Kivu, unlisted) -15.96. 632535→Peru (Spain warmup; low-flat) -4.72. 726747→**Manchester ✓ (0.12 in list)** Brier+0.07 TW+6.76.
- 415069 / 489902 US-Iran talks venue (LINKED): DIRECT NEWS — Oman confirmed talks in **GENEVA** (2nd round Feb19 at Oman's Geneva embassy, Oman-mediated). Next round Mar2 likely continues Geneva. → 415069 Switzerland 0.50/Oman .22; 489902 Geneva 0.50/Muscat .22 (capped 0.50; "next round" could move).
- 812182 Barca midfielder ~6wk hamstring: no news; Dani Olmo & Pedri both hamstring-prone → 0.24 each /deJong .16/Gavi .10/Fermin .08 (flat per cap).
- 422164 (univ ICE misrep) & 811321 (Turkish migrant-boat province): no info; kept low/flat.

## 2026-02-25 (TW 648.94, 191 res) — TEMPORAL-FRAMING TRAP #4 + FLAT-SPREAD WINS
RESULTS: 415069→**Austria** (had Switzerland 0.50) -23.09. 489902→**Vienna** (had Geneva 0.50) -21.32. BOTH = temporal-framing trap #4 (talks venue ROTATES Muscat→AbuDhabi→Geneva→Vienna; I concentrated on CURRENT venue for a NEXT-round Q). vs flat-spread WINS: 422164→Columbia (had .08) **+12.56**, 812182→de Jong (had .16) **+16.40**, 811321→Antalya (.08 tail) +1.32.
**DECISION: The data over ~191 resolutions is unambiguous. Flat 4-5 spreads (top ≤0.30-0.35) net consistently POSITIVE; concentrations >0.45 on "obvious/current/incumbent" without literal-exact-confirmed news net NEGATIVE. From now: HARD cap 0.35 on ALL speculative/identity/future-event Qs. Concentrate >0.45 ONLY for: locked sports result already played (confirmed score), cross-Q lock VERIFIED to same thread, betting-line 2-way, or article literally stating the exact answer to the exact (same-timeframe) question.**
"Next round/edition of rotating thing" (talks, summits) → NEVER assume continuity; spread across rotation set, top ≤0.30.

## 2026-02-25 cont (5 res Feb26)
- 915784 Newcastle UCL R16 host: DIRECT NEWS — Newcastle (beat Qarabag 9-3) "will play **Barcelona or Chelsea**" (draw Feb27). Near-locked 2-opt → Barcelona 0.47 / Chelsea 0.47 / hedge .04.
- 55315 Gorton&Denton by-election (Thu Feb26): 3-way cliffhanger — Green Hannah Spencer 33%, Reform Matt Goodwin 29%, Labour Angeliki Stogia 26% (Omnisis). FIXED (old pred had outgoing Gwynne/"Reform candidate"). → Spencer 0.34/Goodwin 0.31/Stogia 0.28 (genuine tossup, slight Green edge).
- 661416 Russian ship drone vs French carrier: no match; Yantar (recurring NATO-spy-ship) ~0.22 flat/low.
- 131819 (cross-border strike on clinic) & 412823 (senator vs prediction mkts): no info; flat/low per cap.

## 2026-02-26 (TW 690.94, 196 res) — BIG +42 day. 7 res Feb27
RESULTS recap: 131819→Kabul✓(.16)+25.36, 412823→Chris Murphy✓(.08 TAIL)+10.92, 55315→Hannah Spencer✓(.34), 915784→Barcelona✓(.47 2-opt)+11.88, 661416→Zhigulevsk(low-flat)-5. Flat+tails+2-opt = strong.
CLUSTER: US+Israel strikes on Iran imminent (~Feb28; Rubio→Israel Feb28; Reuters "sliding to military conflict"; talks Geneva Feb26). 
- 58660 city explosions during strikes: Tehran 0.40 (very high base-rate, capital primary target, 2025 precedent).
- 209948 airspace must reopen: Iranian airspace 0.40 (dominant — Iran=conflict zone).
- 443306 where final talks collapsed: venue ROTATES (Muscat/Rome/Geneva/Vienna); latest=Geneva Feb26 → Geneva 0.32/Vienna .18/Muscat .16 (no over-concentrate, rotation lesson).
- 739634 country can't play WC: Iran 0.45 (war scenario) / Israel 0.18 (ban pressure) — moderated per cap.
- 434027/815035 Iran city school strike: Tehran ~0.28-0.30 flat per cap.
- 333107 SA T20 SF1 opp: SA=Grp1 winner→plays Grp2 runner-up; England qualified(likely Grp2 #1→other SF). FIXED (old had Australia-eliminated). NZ .26/SL .24/Pak .18/Eng .16/India .06.

## 2026-02-27 (TW 823.38, 203 res) — 11 res Feb28 (Iran-war cluster)
Context: US F-22s to Israel; "potential wartime mission"; strikes ~Feb27-28 (confirmed by Feb27 resolutions). Applied caps + scenario reasoning:
- 354370 HIMARS missile: ATACMS 0.46 (domain-dominant). 70713 US troops base country: Qatar 0.34 (Al Udeid, 2025 precedent; Iraq dropped—US left Al Asad). 768218 Hezbollah avenging: Nasrallah 0.34. 13213 Israeli town 9 deaths: TelAviv 0.28 flat. 59501 Gulf country >half Iran migrants: UAE 0.32 (Dubai expat hub). 
- 172888/635419 Iran interim council: highly speculative; Mojtaba Khamenei .18 / Jannati .26 (Guardian Council secy) low-flat.
- 599755 Tehran hospital: Milad .18 flat. 917339 conflict phrasing: spread Iran-Israel war .30/US-Iran .24 (string-phrasing risk). 80868 WB village: flat. 468437 women's capt: negligible (unguessable).

## 2026-02-28 (TW 809.64, 214 res) — tails win again; phrasing loss
RESULTS: 59501→UAE✓(.32)+29.15. Tails WON: 172888→Arafi(.07)+6.65, 468437→Z.Ghanbari(.04!)+7.59, 354370→PrSM(.22 2nd)+9.66, 70713→Kuwait(.14)+7.78. Losses: 917339→"US-Israel war" (had Iran-Israel/US-Iran, NOT exact phrasing) **-23.33**; 768218→Ali Khamenei (had Nasrallah; KHAMENEI KILLED in strikes!) -13.56; 13213 Beit Shemesh / 599755 Gandhi Hosp / 80868 Abu Falah / 635419 Arafi(unlisted) — small losses.
SCENARIO UPDATE: **Khamenei apparently KILLED in US-Israel strikes; Iran interim leadership (Alireza Arafi on council)**. US-Israel war on Iran ongoing.
LESSONS: (1) ALWAYS 5 outcomes incl. 0.04-0.07 tails — even 0.04 on truth beats unlisted (468437 proof). (2) Conflict/event-NAMING Qs: include actor-combination phrasings ("US-Israel war","US-Iran war","Iran-Israel war") — string match matters. (3) Track scenario state across cluster (Khamenei dead changes Iran-leadership Qs).

## 2026-02-28 cont (7 res Mar1) — Khamenei KILLED confirmed
Scenario: US-Israel struck 24 Iran provinces Sat Feb28, Khamenei killed (Trump "correct story"), Iran retaliating Israel+US bases, Hormuz at risk, Israel struck 2 Iran schools (80+ dead).
- 246419 AWS region disrupted: Bahrain 0.44 (primary AWS ME region, 5th-Fleet drone zone) / UAE .28 / Israel .12 (~2-3 option factual).
- 994042 broadcaster Israel struck: IRIB 0.45 (June2025 precedent + regime-decapitation scenario) / PressTV .14 / Al-Manar .12.
- 560525 country friendly-fire 3 US F-15s: flat Saudi .22/Israel .20/UAE .16/Iraq .12/Qatar .10.
- 971319 Iranian-missile damage site: flat TelAviv .20/Abqaiq .16/AlUdeid .12.
- 453556 Germany evac flights country: UAE .26/Qatar .20/Iran .16 flat.
- 232393 fruit exporter losses: SAfrica .22/Iran .16/Turkey .14 flat. 414228 Taliban target city: Rawalpindi .24/Peshawar .20 flat.

## 2026-03-01 (TW 973.40, 221 res) — +164 day; 4 res Mar2
RESULTS: 246419→Bahrain✓(.44)**+69**, 994042→IRIB✓(.45 precedent)**+56**, 232393→SAfrica✓(.22 baseline)+35, 414228→Rawalpindi✓(.24 baseline)+34. Losses small: 560525 Kuwait F-15 -17.58, 971319 RasLaffan -10.66, 453556 Oman -2.24. Cluster+precedent+held-baseline = compounding wins.
Scenario: Iran missiles hit Gulf — Abu Dhabi (1 killed), Bahrain (5th Fleet center hit), Kuwait airbase runway, Qatar/Doha, Saudi (Riyadh+east). 
- 297818 UAE oil emirate: Abu Dhabi 0.36 (main oil)/Fujairah .26 (storage hub).
- 584240 country Pak brings to Iran talks: Saudi .30/US .24 flat.
- 656436 country Trump threatens trade cutoff: Turkey .20 (vocal critic)/China .16 flat.
- 759458 Iran hospital-babies city: Tehran 0.34 (high base rate) flat.

## 2026-03-02 (TW 1006.25, 225 res) — crossed 1000; 6 res Mar3
RESULTS: 297818→Fujairah(.26 2nd)+26.74, 584240→US(.24 2nd)+34.54, 656436→Spain(unguessable)-12.22, 759458→Bushehr(unlisted)-16.21. Net +33.
- 68828 CEO $30bn: DIRECT NEWS — OpenAI round: SoftBank & Nvidia EACH $30bn. → Son 0.40 / Huang 0.26 (both exactly $30bn; Son more vocal).
- 803012 House Oversight subpoena re DOJ/Epstein: Bondi central (perjury/coverup accusations) → Bondi 0.36 (cap) / Blanche .14 / Patel .12.
- 937255 waterway ship ablaze: Strait of Hormuz 0.38 (Iran-war epicenter).
- 16281 Carrick 1st defeat: unbeaten 7-8 (19/21 pts); no fixture info → flat Liv/City .16/Ars .14/Che .12/Spurs .08.
- 157054 senator removes protester: Mullin 0.20 (physical-confrontation history) flat. 768526 country wants UA drone help: flat Saudi .20/UAE .16/Poland .14.

## 2026-03-03 (TW 1112.31, 231 res) — +106 day; 8 res Mar4
RESULTS: 803012→Bondi✓(.36)+51.48, 937255→Hormuz✓(.38)+48.11, 768526→US✓(.12,baseline held)+25.42, 68828→Huang(.26 2nd)+0.27Brier, 157054 Sheehy/16281 Newcastle (flat,-7/-9).
War: Khamenei confirmed killed; Aramco Ras Tanura refinery shut after strike; US Embassy Kuwait hit; Israel mobilizing 100k for Lebanon.
- 863162 Gulf country oil refinery hit: **Saudi (Ras Tanura Aramco confirmed)** 0.48.
- 765155 capital homes near US Embassy evac: **Kuwait City 0.34** (US Embassy Kuwait hit Mar2).
- 779990 Saudi city projectile: Ras Tanura 0.26 flat.
- 869392 co-sponsor w/Merkley anti-prediction-mkt bill: CROSS-Q → Chris Murphy 0.28 (he's THE anti-pred-mkt senator, 412823).
- 887402 military blamed for Iran school strike: moderated flat Israel .34/US .26/Iran .24 (DoD deflection uncertain; cap).
- 943634/281710/641254: flat/low.

## 2026-03-05 (TW 1136.20, 241 res) — 3 res Mar6
RESULT: 483759→**Middle East ✓ (0.32)** Brier+0.47 TW+44.09 (scenario-grounded+held). 871156→Michigan (unlisted) -11.80.
- 758920 Nepal PM (vote Mar5, sworn Mar27): Balen Shah front-runner but parliamentary/coalition → Balen .26/Thapa .20/Oli .16/Karki .12 flat.
- 681301 S.Lebanon strike district: Israel heavy Lebanon war; Tyre district house hit → Tyre .26/Nabatieh .20/BintJbeil .16 flat.
- 893235 country US PREVIOUSLY accused of school attack: CROSS-Q (887402=US military responsible) → US deflected to Iran → Iran 0.42/Israel .22.

## 2026-03-06 (TW 1224.65, 244 res) — clean sweep +88; 4 res Mar7
RESULTS: 681301→Tyre✓(.26)+34.27, 758920→Balen Shah✓(.26)+8.16, 893235→Iran✓(.42 cross-Q)+46.01. Disciplined approach compounding (BSS .077, acc 18.8%).
- 338215/830793 Oslo embassy bomb (LINKED): no news; scenario→Israeli embassy/Israel ~0.40-0.42 (kept, capped, no churn).
- 276362 Beirut coastal hotel-room strike: Ain al-Mreisseh .20/Raouche .18 (hotel-corniche area) flat.
- 578870 Beirut apartment ≥4 killed: Dahieh 0.32 (most-struck S.suburbs) flat.
STATUS: 86 active, ~21 days. Strategy stable & strongly net-positive. Keep: cap ≤0.42 (≤0.50 only direct-news/locked), flat 5-spreads w/tails, scenario+cross-Q grounding, hold sound baselines.

## 2026-03-07 (TW 1260.93, 248 res) — cap discipline validated
RESULTS: 276362→Raouche✓(.18 2nd)+23.44. 338215→US embassy / 830793→US (had Israel .40/.42 top BUT US .18 2nd) → BOTH +TW (+15.12/+13.48) despite wrong top — CAP DISCIPLINE converts wrong-obvious into net positive. 578870→Raouche (both Beirut strikes = Raouche; missed cross-link) -15.76.
LESSON: cross-link same-day same-topic Qs (276362 hotel & 578870 apartment both Beirut→both Raouche).
- 271330 Australia missiles→country: Ukraine 0.36 (long-standing aid recipient).
- 179817 SL coach: Jayasuriya resigned, SLC seeking FOREIGN coach (names unknown) → low-flat Hathurusingha .14/Nawaz .12 (total .49, speculative).
- 304016 airline suspends 2026 outlook: EU carriers worst-hit (Lufthansa/IAG/AF-KLM) → flat.
- 309487 Ukr region retaken: flat Kharkiv .22/Sumy .16.

## 2026-03-08 (TW 1215.16, 252 res) — rough batch (4 unguessable -46); 4 res Mar9
- 932855 China WAsianCup QF: DIRECT — Matildas play "North Korea OR China" at Perth Mar14 → Australia 0.46.
- 399040 Iran move WC matches country: FFIRI noncommittal/boycott talk; if move→Mexico/Canada co-hosts → Mexico .30/Canada .26 flat.
- 605397 Iraqi group US strike: Kataib Hezbollah 0.30 cap.
- 935869 Liverpool UCL R16 1st-leg only-goal scorer: opponent/result unknown → Salah .18 low-flat.
NOTE: continuing strong cumulative (1215, ~+4.8/resolved). Some unguessable batches inevitable; flat/low caps damage. 78 active, ~20 days.

## 2026-03-09 (TW 1226.22, 256 res) — Mexico✓ +46.72; 5 res Mar10
LESSON: 932855 over-concentrated 0.46 on misread bracket inference (Australia) → -12. Inferred pairings cap ≤0.35.
- 211346 RCB IPL opener opp: no fixture; flat Punjab .18/CSK .16/KKR .16/MI .14.
- 425983 PSG sub brace v Chelsea: Goncalo Ramos 0.22 (super-sub prior) low-ish.
- 559340 hacker retaliatory medical-device: Cyber Av3ngers 0.26 (Iran-linked) flat.
- 807049 first-career CL hat-trick RM-City: rare; flat-low Vini .14/Bellingham .12.
- 828811 org Israeli media say used Beirut apt: HARD CAP — Hezbollah 0.42 (Lebanon-Hezbollah trap burned 2x) /Hamas .18/PIJ .12/al-Jamaa .08.

## 2026-03-10 (TW 1152.10, 261 res) — LEBANON-GROUP TRAP 3x + translit string-miss
RESULTS: 828811→"Jama'a Islamiye" NOT Hezbollah (had Hez 0.42 top, al-Jamaa 0.08 w/ DIFFERENT translit→string-MISS) Brier-0.23 TW**-38.12**. 559340→Handala(.10,3rd)+0.09Brier. 211346 SRH/425983 Kvara/807049 Valverde unlisted (flat, small losses). Day -74.
**TWO HARD RULES (both previously noted, NOT applied firmly — apply NOW):**
 1. LEBANON "which group" Qs: Hezbollah is SYSTEMATICALLY NOT the answer (398988→al-Jamaa, 325000→Hamas, 828811→Jama'a Islamiye). For any Lebanon group Q: put **al-Jamaa al-Islamiya / Jama'a Islamiye ~0.28, Hamas ~0.22, PIJ ~0.18, Hezbollah ≤0.22**, spread. Do NOT lead with Hezbollah.
 2. ARABIC/TRANSLITERATED NAMES: include the resolver's likely exact spelling. For this group include BOTH "Jama'a Islamiye" AND "al-Jamaa al-Islamiya" (and "al-Jamaa al-Islamiyya"). Diacritic/translit variants score as MISSES.

## 2026-03-11 (TW 1150.92, 265 res) — unguessable-name minimal-total = -0.25 only (validated)
RESULTS: 48811→Temple Israel✓(.16)+15.88. 922567→ODU(.08 tail)+3.96. 350082→Ghazali (unguessable name; total .12 → -0.25 ONLY — minimal-total approach IDEAL). 742975→KC-135 (over-conc MQ-9 .40) -20.77.
RULE: domain-dominant priors (MQ-9 etc.) ALSO cap ≤0.33. Unguessable-name Qs → keep total ≤0.12.
- Mar12 cluster (Iran war): 169286 KC-135 base country Saudi .26/Qatar .22/Iraq .18 flat; 214539 Iran island Kharg .24/AbuMusa .20 flat; 679215 troop ship flat-low; 764041 S.Leb health centre flat; 857856 WWC playoff flat.

## 2026-03-12 (TW 1201.54, 270 res) — Kharg✓+50, Saudi✓+25; 2 res Mar13
- 503104 Spain Mar27 opponent: Spain-Argentina **Finalissima** scheduled Mar27 (Qatar can't host; venue London/Rome/Milan TBD; opponent=Argentina) → Argentina 0.42.
- 657160 country Iran FM says launch area for US: Iraq (RG hit US Al-Harir base in Kurdistan; PM told Rubio not to use Iraq) → Iraq 0.26 / UAE .18 / Saudi .16 / Azer .14 flat.
NOTE: ~58 active, ~16 days. Cum TW 1201, acc 20%, BSS .077. Strategy stable.

## 2026-03-14 (TW 1206.89, 276 res) — Germany✓+35.93; 2 res Mar15
- 506444 team beats SK to reach WAsianCup final: bracket — SF1=China v Australia; SF2=(SK/Uzb) v (Japan/Phi). Japan dominant (3W 17GF 0GA) → Japan 0.50 (FIXED; old had Australia 0.50 = wrong side of bracket).
- 529060 missile Ukr destroyed pre-launch (late-Mar record attack): Iskander 0.30 flat (speculative future).
STATUS: cum 1206.89, acc 20.3%, BSS .078, 276/330 res, 54 active, ~14 days left. Strategy: scenario/cross-Q/bracket-grounded moderate (≤0.42) + flat 5-spreads w/tails; net strongly +.

## 2026-03-15 (TW 1214.59, 278 res) — Japan✓; 7 res Mar16
Mostly speculative/no-signal batch; applied caps/flat: 167989 Arsenal QF (no bracket→flat RM .22/PSG .18); 58520 Israeli official flat Netanyahu/Katz; 669234 TelAviv .28; 573851 AFCON appeal flat Senegal .20; 293527 agency-director-quit CIA .30 (Munshi=commission advisor, not match); 274734 bill-name low total; 219636 Mexico refinery flat.
STATUS: cum 1214.59, acc 20.6%, BSS .080, 278/330 res, 52 active, ~13 days.

## 2026-03-16/17 (TW 1252.95, 288 res) — caps limiting losses
864964→Ali Larijani NOT Khamenei (scenario-dominant subverted; 0.42 cap→only -5.81). 405816 Beit Awwa/676065 Bernie(.08 tail) unguessable small losses.
Mar18 batch: 666706 Chuck Norris hosp state Texas 0.42 (residence prior, no death confirmed); 512785 $8.4bn F-16 sale UAE .24 (UAE flies F-16; Saudi=F-15); 398208 AI server smuggle Malaysia .24; 388689 Lin Yu-ting WBoxing .32; 724111 Iran Basij Zahedan .22; 739439 Los Mayos low-total.
STATUS: cum 1252.95, acc 20.9%, 288/330 res, 42 active, ~11 days. Strategy stable; caps converting subversions into small losses, flat-spread 2nd-picks into wins.

## 2026-03-18 (TW 1231.05, 294 res) — residence-prior subverted too
666706→Hawaii NOT Texas (had 0.42 residence prior) Brier-0.21 TW**-27.84**. 512785→UAE✓(.24)+22.95. 398208→Taiwan(.10 tail)+7.39. 739439→unguessable (total .16) only -0.53.
**FINAL DISCIPLINE for remaining ~36 Qs: cap TOP ≤0.33 for ALL identity/location/specific Qs UNLESS (a) confirmed-result/official-announcement direct news, (b) hard cross-Q lock, (c) locked ≤3-option set. NO residence/incumbent/scenario-dominant exceptions (all subverted: Texas, Khamenei, MQ-9, Hezbollah×3). Unguessable names → total ≤0.15. Always 5 outcomes incl tails.**

## 2026-03-19/20 (TW 1219.72, 303 res) — unguessable batch
217580 East Darfur/427993 Kenya/974962 Meknes all unlisted (-7 to -13 each, flat capped). cum 1219.72, acc 21.2%, 303/330 res, 27 active, ~8 days.
- 774274 N.Israel Hezbollah strike: Nahariya hit Mar16 (residential bldg); Kiryat Shmona perennial target → Nahariya 0.26 / Kiryat Shmona 0.26 flat.

=== DAY 2026-03-22 (resolvers for 2026-03-23) ===
262505 Dennis Coyle release facilitating country: NO release confirmed; US blacklisted Afghanistan 3/9, Pak bombed Kabul 3/16-18 (tensions HIGH). Qatar = dominant historical Taliban-US mediator (Glezmann, Corbett, Frerichs all Qatar). Pred Qatar 0.48 / UAE 0.14 / Saudi 0.07 / Turkey 0.05 / Pak 0.04. Risk: may not resolve (no release).
698278 IPL Bolt Ventures: STRUCTURAL FIX — baseline (Punjab/SRH/KKR) was WRONG. All news: Blitzer/BOLT due diligence ONLY on Royal Challengers Bengaluru + Rajasthan Royals. RCB=Diageo non-core sale ($1.8B, heavy competition Poonawalla/Pai/Blackstone/KKR/Glazer); RR=Badale-owned. Near-even RR 0.34/RCB 0.33 + small tails. Risk: deal may not close by 3/31.
494140 IQAir most polluted COUNTRY 2025: report not out. Hist #1: 2022 Chad, 2023 Bangladesh, 2024 Chad. Pred Chad 0.32/Bangladesh 0.30/Pakistan 0.20/India 0.08/DRC 0.05.
757107 IQAir most polluted CITY 2025: report not out. 2024 #1 = Byrnihat (India); Lahore/Delhi consistent. Pred Byrnihat 0.30/Lahore 0.18/Delhi 0.16/N'Djamena 0.08/Dhaka 0.06 (left room for other small Indian town).
912807 Lukashenko first official visit wk ending 3/31: no specific trip found; Russia overwhelming base rate but capped (incumbent-prior trap, narrow window, may not travel). Russia 0.40/China 0.15/NK 0.07/Iran 0.05/UAE 0.03.
LESSON reinforced: always check baseline against news for structural validity on near-term resolvers (698278 caught wrong candidate set).

=== DAY 2026-03-23 ===
RESULTS 3/22->23: 262505 Coyle->UAE (had Qatar0.48/UAE0.14) Brier+0.02 TW+0.42 (tail saved); 494140 IQAir country->Pakistan (had 0.20 3rd) Brier+0.16 TW+19.51 (flat-spread win); 698278 IPL->RCB (had RR0.34/RCB0.33) Brier+0.43 TW-8.89 (wrong-baseline drag, fix limited damage); 757107 IQAir city->LONI (UNLISTED! had Byrnihat0.30) Brier-0.16 TW-14.14; 912807 Lukashenko->NORTH KOREA (had Russia0.40/NK0.07) Brier-0.05 TW+0.02 (Russia cap CRUCIAL - NK tail saved). Cum TW 1195.16.
LESSON: IQAir most-polluted-CITY is wildly unpredictable rotating obscure towns (Byrnihat'24, Loni'25, Begusarai'23) - keep total LOW (~0.55) many tails. Incumbent-cap on Lukashenko (Russia 0.40 not 0.65) saved ~big negative when truth=NK. Tails repeatedly net-positive.
SUBMITTED (resolve 3/24-25):
200605 Australia 6mo visitor ban: ABC/Greens "clearly aimed at Iran" (war, Iranian asylum). Iran 0.55/Leb0.08/Isr0.06/Iraq0.05/Qatar0.04.
240291 Latvia drone from Russian airspace: geographic prior strong->Russia 0.60/Belarus0.14/Ukr0.12/Iran0.03.
534802 Italy WC playoff FINAL opponent: bracket CONFIRMED Path A = Italy v N.Ireland (Bergamo 3/26) + Wales v Bosnia. Final opp = Wales/Bosnia winner if Italy beats NI(~80%). Wales0.42/Bosnia0.38/NI0.05/Italy0.03/Swe0.02.
34927 Kosovo hosts in playoff final: Path C Turkey v Romania + Slovakia v Kosovo. Kosovo final opp=Turkey/Romania winner. Turkey0.42/Rom0.18/Svk0.06/Bih0.04/NMk0.03 (void risk if Kosovo loses semi ~55%).
390530 Trump 10-day pause from whom: news=5day postpone after "talks w/ Tehran"; Qatar OUT as mediator(pro-war), Oman now sole GCC mediator. Iran0.40/Oman0.12/Qatar0.10/Rus0.07/Isr0.06.
953884 Navy search aid boats to Cuba: NO specific news; spread Cuba0.24/Mex0.24/US0.22/Hon0.05/Spain0.04.
CROSS-Q NOTE: Football playoff bracket locked - reuse for any other playoff Qs. Path A:Italy/NI,Wales/Bosnia. Path C:Turkey/Rom,Slovakia/Kosovo. Path D:Denmark/NMacedonia,Czech/Ireland(Prague 3/26).

=== DAY 2026-03-24 ===
RESULTS 3/23->24: 200605 Australia ban->IRAN ✓ (had 0.55) Brier+0.78 TW+61.39 BIG WIN (confident directional). 240291 Latvia drone->UKRAINE (had Russia0.60/Ukr0.12) Brier-0.15 TW-29.21 - geographic prior SUBVERTED again (drone entered FROM Russian airspace but was Ukrainian stray). Cum TW 1227.35.
LESSON: Even "obvious" geographic attribution caps must stay <=0.55; surprise-truth keeps happening (Lukashenko->NK, Latvia drone->Ukraine, Coyle->UAE). Confident calls only when news explicitly confirms direction (Australia/Iran worked because ABC said so).
UPDATES (resolve 3/25): 534802 Italy final opp: bracket confirmed, Wales hosts Bosnia (Cardiff). Wales0.44/Bosnia0.36/NI0.05/Ita0.03/Swe0.02. 390530 Trump pause: it's 5-DAY not 10, Trump cited "top person in Iran", analysts cite Pakistan/Egypt/Turkey mediators, Qatar OUT. Iran0.38/Oman0.10/Turkey0.09/Pak0.08/Egypt0.07. 34927 Kosovo host: Path C Slovakia v Kosovo + Turkey v Romania - kept Turkey0.42/Rom0.18/Svk0.06/Bih0.04/NMk0.03. 953884 aid boats Cuba: no news, kept Cuba0.24/Mex0.24/US0.22/Hon0.05/Spain0.04.
STRUCTURAL FIX: 489669 England defender - removed Colwill/TAA (NOT in squad). Squad def: Burn,Guehi,Hall,Konsa,Livramento,Maguire,O'Reilly,Quansah(inj->White),Spence,Stones,Tomori. England v Uruguay 3/27 Wembley, v Japan 3/31. Compound event (score only goal + concede stoppage pen) low prob -> Maguire0.16/Guehi0.14/Stones0.12/Konsa0.07/Tomori0.05 (total 0.54, void-likely).

=== DAY 2026-03-25 ===
RESULTS 3/24->25: 34927 Kosovo host->"Turkiye" (I had "Turkey" 0.42 - STRING MISMATCH, NOT matched!) Brier-0.21 TW-6.38. 390530 Trump pause->"Iran's government" (I had "Iran" 0.38 - STRING MISMATCH, NOT matched!) Brier-0.17 TW-14.10. 534802 Italy->Bosnia&Herzegovina (had Bosnia 0.36 2nd) Brier+0.39 TW-6.01. 953884 aid boats->Mexico (had Mexico0.24 tied-top) Brier+0.31 TW+13.09. Cum TW 1213.95.
*** CRITICAL LESSON - STRING VARIANTS ***: Grader does EXACT match, no normalization. "Turkey"!="Turkiye"; "Iran"!="Iran's government". COST ~20 TW this round. NEW RULE: when answer could have spelling/format variants, SUBMIT MULTIPLE VARIANT OUTCOMES splitting the probability:
 - Turkey questions (esp UEFA/FIFA): include BOTH "Turkiye" AND "Turkey".
 - answer_type "string (government)": include BOTH bare country AND "<Country>'s government"/"Government of <Country>".
 - Transliterations: include common variants.
This hedges exact-match risk at low cost.
UPDATES (resolve 3/26): 79608 Iran city 6 killed 3 houses: heavy Tehran residential strike reporting -> Tehran0.30/Isfahan0.13/Tabriz0.10/Kermanshah0.09/Ahvaz0.08. 489669 England def vs Uruguay (3/27 Wembley, squad split): compound event low-prob, kept Maguire0.16/Guehi0.14/Stones0.12/Konsa0.07/Tomori0.05. 659262 Israeli PL footballer firing in S.Lebanon: NO id news, UNGUESSABLE -> kept minimal total (Solomon0.05/Zahavi0.04) to minimize downside.

=== DAY 2026-03-26 ===
RESULTS 3/25->26: 489669 England def->Ben White (late squad add, I omitted) Brier-0.07 TW-10.40. 659262 Israeli footballer->Menashe Zalka (unguessable; my minimal-total Solomon0.05/Zahavi0.04) Brier-0.00 TW-0.41 *** minimal-total strategy VINDICATED on unguessable ***. 79608 Iran city->Qom (had Tehran0.30, no Qom) Brier-0.13 TW-10.83. Cum TW 1192.31.
LESSON: minimal-total (Σp≈0.09) on truly-unguessable specific-identity Qs = only -0.41 vs moderate-total spreads = -10 to -14. For large-answer-space Qs with NO strong signal, KEEP TOTAL LOW (~0.3-0.5). Also: include late squad additions (Ben White).
SUBMITTED (resolve 3/27): 795856 town 3 journalists killed S.Lebanon: Tyre repeatedly hit incl during AJ report -> Tyre0.28/Nabatieh0.12/BintJbeil0.09/Sidon0.08/Naqoura0.06 (total 0.63). 560679 Abu Dhabi company damage: UAE hit by Iran missiles (Al Shawamekh debris,161 injured), no co. claim yet -> ADNOC0.36/EGA0.14/Borouge0.12/Mubadala0.07/TAQA0.05. 177801 armed group claims attacks before S.Israel missile strike: flat Houthis0.25/Hamas0.20/Hezb0.18/PIJ0.12/IRI0.07. 320138 app recruited Paris bank bomber: Telegram strong prior -> Telegram0.44/Signal0.16/WA0.10/TikTok0.10/Snap0.06.

=== DAY 2026-03-27 ===
RESULTS 3/26->27: 177801 armed group->Houthis ✓ (had 0.25 top) Brier+0.35 TW+36.14 WIN. 320138 Paris app->Snapchat (had Telegram0.44/Snap0.06) Brier-0.12 TW-25.65 (thematic prior subverted again). 560679 Abu Dhabi co->Emirates Global Aluminium (had EGA0.14 2nd) Brier+0.11 TW+15.23 (spread win). 795856 town->Jezzine (had Tyre0.28, no Jezzine) Brier-0.11 TW-8.31. Cum TW 1209.73.
LESSON: thematic priors (Telegram-recruitment, ADNOC-AbuDhabi) keep getting subverted -> cap such priors <=0.35, spread more. Flat-spread-with-tails consistently wins (Houthis, EGA). Location Qs w/ huge answer space keep missing (Qom, Jezzine) - keep total moderate (~0.6) not high.
SUBMITTED (resolve 3/28, FINAL 3 Qs): 144312 who says worship-all-religions Jerusalem post Palm Sunday(Mar29): Pope most likely -> Pope Leo XIV0.36/Guterres0.10/Pizzaballa0.09/KingAbdullahII0.07/Macron0.05. 26340 country Iranian raid kills power+water plant worker: Gulf desal cluster UAE0.28/Saudi0.24/Bahrain0.16/Kuwait0.10/Qatar0.08 (used full "United Arab Emirates" - grader used full name in qid262505). 267975 Sudan state aid cutoff: El Fasher/N.Darfur siege prototypical -> NorthDarfur0.30/EastDarfur0.15(AlDaein hosp attack)/SKordofan0.10/WestDarfur0.08/NKordofan0.07.

=== DAY 2026-03-28 — SIMULATION COMPLETE ===
RESULTS 3/27->28 (final 3): 144312 worship Jerusalem->Emmanuel Macron (had Macron0.05 tail, Pope0.36) Brier-0.06 TW+1.92 (tail+spread kept TW positive). 26340 country->Kuwait (had Kuwait0.10 4th) Brier+0.02 TW+7.70 (flat-spread captured it). 267975 Sudan->White Nile State (had NorthDarfur0.30, unlisted) Brier-0.13 TW-13.48.
*** FINAL: 330/330 resolved, 0 active. Accuracy 21.8% | BSS 0.082 | TW-SCORE 1205.87 ***
KEY VALIDATED STRATEGIES (for future runs):
1. Flat-spread-with-tails on multi-candidate Qs: repeatedly net-positive (Houthis+36, EGA+15, Kuwait+7.7, IQAir-Pakistan+19). Tails at 0.05-0.15 catch 2nd/3rd/unlisted-adjacent truths and limit downside.
2. Minimal-total (Σp~0.09) on TRULY unguessable specific-identity Qs = near-zero loss (Israeli footballer -0.41 vs moderate-spread -10/-14). USE THIS for unknowable person/obscure-place Qs.
3. Confident concentration ONLY when news explicitly confirms direction (Australia/Iran +61). Otherwise cap top <=0.35-0.45.
4. Incumbent/geographic/thematic priors GET SUBVERTED constantly (Lukashenko->NK, Latvia drone->Ukraine, Telegram->Snapchat, Pope->Macron, ADNOC->EGA, NorthDarfur->WhiteNile). Cap them, never >0.55 w/o confirmation.
5. STRING EXACT-MATCH is unforgiving: "Turkey"!="Turkiye", "Iran"!="Iran's government". For variant-prone answers, submit BOTH spellings as separate outcomes.
6. Structural baseline check on near-term resolvers caught wrong candidate sets (IPL teams, football paths, England squad) — always validate against current news before a Q resolves.
7. Cross-Q inference (football bracket reused across 34927/534802) and same-topic clustering = reliable edge.
8. Large-answer-space location Qs (Iranian city, Lebanese town, Sudan state) are very low-hit; keep total ~0.5-0.65, never high.
NET TRAJECTORY: recovered from disaster low ~259 to final 1205.87 via disciplined caps + flat spreads + tails.
