# Forecasting Memory — Al Jazeera Q1 2026 Market

## SIM SETUP
- Sim date starts **2025-12-24**. 330 questions, all open-ended string answers, resolve Jan–Mar 2026.
- Articles in articles/YYYY/MM/DD/. New ones appear daily as sim advances.
- Predictions PERSIST across days until I change them. So: predict ALL questions ASAP (time-weighted), refine daily.

## SCORING MODEL (critical)
- BSS = 1 - Σ(p_i - y_i)² over outcomes; TRUE outcome ALWAYS counted (range -1..+1).
- If true answer in my list: 1 - Σ(p_i-y_i)². If NOT in list: score = -Σp_i² (mild if probs low).
- Proper scoring → report calibrated probs. Leave unallocated mass for "other" (don't force sum=1).
- For unpredictable specific-event Qs: list 2-4 plausible candidates at LOW/modest probs to cap downside.
- Strategy: high-confidence Qs → strong dist now. Unknowable Qs → low-conf guess now, sharpen when article appears near resolution.

## WORLD MODEL as of 2025-12-24
### Iran/Israel: NO active war, but RISING risk. Netanyahu (Dec20-22) pushing Trump for fresh strikes on Iran (ballistic missile rebuild, nuclear reconstruction). IRGC missile drills alarm Israel. June 2025 "12-day war" already happened (Op Midnight Hammer, US bombed Iran nuclear sites). => Large Iran-war Q cluster (HIMARS, Tehran strikes, Gulf refineries, US troops killed, Israeli town missile deaths) is SPECULATIVE round-2; meaningful prob but NOT certain. Modest confidence, sharpen as news arrives.
### Venezuela: Maduro under max US pressure (Caribbean buildup, strikes on boats ~80+ killed, tanker seizures, $50M bounty, family sanctions Dec19). Machado (Nobel) = US favorite; Edmundo González = claimed election winner. No transition yet. Q651727 interim president: if Maduro falls → González or Machado.
### Ukraine-Russia: ACTIVE peace talks Miami/Florida Dec20-22 (Witkoff, Kushner, Umerov, Dmitriev). Trilateral proposed. Possible deal momentum.
### NFL (SB LX Feb 8 @ Levi's): AFC seeds: 1 Denver(12-3),2 NE Patriots(12-3),3 Jax(11-4),4 Pittsburgh,5 LAChargers(11-4),6 Buffalo(11-4),7 Houston. NFC: 1 Seattle(12-3),2 Chicago(10-4),3 Philadelphia(9-5),4 TampaBay,5 LA Rams(11-4),6 SF49ers(10-4),7 GreenBay. Mahomes torn ACL, Chiefs OUT. Playoffs: WC Jan10-12, Div Jan17-18, Conf Champ Jan25, SB Feb8.
  - NFC QBs: Seattle=Sam Darnold, Rams=Stafford, Eagles=Hurts, Packers=Love, Bears=Caleb Williams, 49ers=Purdy, Bucs=Mayfield.
### AFCON 2025 (Morocco): Groups A Morocco/Mali/Zambia/Comoros; B Egypt/SA/Angola/Zim; C Nigeria/Tunisia/Uganda/Tanzania; D Senegal/DRCongo/Benin/Botswana; E Algeria/BurkinaFaso/EqGuinea/Sudan; F IvoryCoast/Cameroon/Gabon/Mozambique. Group stage ends Dec31, R16 Jan3, final Jan18 Rabat. Q799398 BG implies FINAL = Morocco vs Senegal (so Senegal wins their half).
### Bangladesh election Feb12 2026: BNP frontrunner (most seats), Jamaat-e-Islami 2nd, NCP 3rd. Awami League BANNED. Nominations Dec29, campaign from Jan22. => Q304287 main opposition likely Jamaat-e-Islami.
### Grammys Feb1 2026: AOTY nominees: Bad Bunny(DTMF), Clipse, Bieber(Swag), Kendrick(GNX), Lady Gaga(Mayhem), Leon Thomas(Mutt), Sabrina Carpenter(Man's Best Friend), Tyler(Chromakopia). Kendrick frontrunner(9 noms), Gaga 2nd, Bad Bunny strong.
### Chelsea: Maresca under pressure but "committed", contract to 2029. No appointment likely by Jan31 (Q165622 may void / low conf).

## TODO / OPEN
- Oscars 2026 (Jan22 noms): need frontrunners. Q886103 says a film gets RECORD 16 noms (all-time record is 14!) — distinctive.
- Men's UCL league phase standings + playoff draw (~late Jan) for 85609/35131/55999/261538.
- Tennis AO "who faces X round Y" — draw out ~Jan 8; unknowable now, sharpen post-draw.

## MORE FACTS (Dec 24 research)
### Oscars 98th (noms Jan22): "One Battle After Another"(PTA) = frontrunner, led Golden Globes. Others: Hamnet(Zhao), Sinners(Coogler), Frankenstein(del Toro), Sentimental Value(Trier), Marty Supreme, Wicked:For Good. Q876347 most-noms film, Q886103 its director (likely PTA).
### AFCON results thru Dec24: A: Morocco 2-0 Comoros. B: SA 2-1 Angola, Egypt 2-1 Zim. C: Nigeria 2-1 Tanzania, Tunisia 3-1 Uganda. D: DRCongo 1-0 Benin, Senegal 3-0 Botswana. Morocco fav(11/4), Senegal/Algeria/Egypt next, IvoryCoast holders(6/1). Nigeria DIDN'T qualify for World Cup (lost to DRC on pens). Q343689 implies Morocco QF vs Cameroon Jan9; Q799398 BG implies FINAL Morocco vs Senegal.
### Ukraine govt: Yermak (chief of staff) resigned Nov28 - NOT yet replaced. DefMin=Denys Shmyhal (ex-PM). PM=Yulia Svyrydenko. Chief-of-staff candidates: Fedorov, Shmyhal, Kyslytsia, Palisa. Energy+justice min vacant. Corruption scandal (Energoatom $100M).
### PROCESS: bulk-submitting all 330 today w/ calibrated probs. Unpredictable specific-event Qs => 2-4 low-prob candidates (total<0.4) to cap downside. Refine daily as articles drop near each resolution date.

## DAY 1 (Dec 24) COMPLETE: 292/330 predicted. 38 unpredicted (see TO_REVISIT.md).
HIGH-CONF ANCHORS: 951896 Sinner AO; 348570 ManCity Deloitte; 304287 Jamaat opp; 14689 Canada school shoot; 652747 Novichok; 207522 Sulawesi; 924864 Pakistan Board of Peace; 459?/799398 Morocco-Senegal AFCON final.
DAILY ROUTINE: (1) check articles/ new date for resolved/near events, (2) update soonest-resolving Qs, (3) add TO_REVISIT items as draws/news drop, (4) refine war-cluster if Iran war materializes.
NOTE on scoring assumption: treating void/unresolved as ~neutral (excluded), so war-cluster conditional favorites at moderate (0.2-0.4) are safe upside. Keep per-Q individual probs <=0.5 to bound downside if specific detail wrong.

## DAY 2 (Dec 25):
- Venezuela: White House -> ECONOMIC "quarantine" of oil for ~2 months; "late Jan economic calamity" expected. Military focus paused. => regime change by Jan 2 LESS likely. Trimmed 651727. USS Gerald Ford + 10 escorts in Caribbean ("biggest armada ever in S.America" - confirms 279531=Caribbean).
- Chelsea: Maresca firmly in place, no Jan transfers, "in love with squad" => 165622 likely voids.
- Iran: US-Iran clashing at UN over nuclear talks; no new war. Israeli spy (Iran) arrested in Rishon LeZion.
- AFCON: no new results (next games Dec26). Hold predictions.
- No other near-term updates needed. Most predictions persist.

## DAY 3 (Dec 26):
- Syria: Homs mosque blast (Wadi al-Dahab, Alawite area) 8 dead, claimed by Saraya Ansar al-Sunna. Watch Syria instability Qs.
- Ukraine: 20-pt peace plan (from 28). Zelensky to meet Trump "before New Year". Russia strikes continue (Odesa 8 dead). Russian general killed by car bomb in Moscow (Dec). Watch talks-location Qs (48762/655453/575662) - no venue named yet.
- No direct resolutions today. Held all predictions.

## DAY 4 (Dec 27):
- AFCON Group D: Senegal 1-1 DRCongo. Senegal top (4pts, better GD), DRCongo 2nd (4pts). Final games Dec30: Senegal-Benin, Botswana-DRCongo. DRCongo likely 2D -> R16 vs 1E (Algeria/BurkinaFaso winner of Grp E). Updated 703511 (Algeria top eliminator).
- Group A: Morocco beat Mali 8pm Dec26 (check). Egypt-SA played.
- REFINE AFCON knockout Qs again Dec31 when bracket fully set.

## DAY 8 (Dec 31): AFCON R16 SET
- R16: Senegal(1D) v Sudan Jan3 Tangier; Egypt(1B) v Benin Jan5 Agadir; DRCongo(2D) v ALGERIA(1E) Jan6; Nigeria(1C) won grp perfect. Morocco(1A) v 3rd-place C/D/E Jan4.
- 703511 SHARPENED: DRCongo's R16 foe = Algeria (winner maybe faces Nigeria QF). Set Algeria 0.48, Nigeria 0.20.
- 459037 Morocco SF opp: refine after QFs (Jan9-10). Final assumed Morocco-Senegal (opposite halves).
- Anthony Joshua injured in DEADLY car crash in Nigeria (Dec30) -> threatens Fury-Joshua (465445), moderated AJ 0.40->0.28.
- Tomorrow Jan1 resolves: 165622(Chelsea-likely void),227432(UA defmin),628026(Charlotte),892867(Austrian skier),93950(measles). Predictions in place.
- NEXT MILESTONES: Jan3 R16 starts; Jan8 AO draw (tennis Qs); Jan9-10 AFCON QFs.

## DAY 9 (Jan 1) — FIRST RESULTS & LESSONS
Resolved: Chelsea->Liam Rosenior (I missed, -0.50, low alloc saved me). UA defmin->Fedorov (had 0.08, +12.70). Charlotte->Mint Hill (miss -1.63). Austrian skier->Katharina Liensberger [FEMALE!] (had men, -1.65). Measles->South Carolina (had #1 @0.18, +27.66). Cumulative TW=36.58.
KEY LESSONS:
1. TW-score per Q ≈ BSS×100 (if held full duration). BSS=1-Σ(p_i-y_i)².
2. **UNDER-CONFIDENT on favorites**: SC@0.18 gave BSS .28; SC@0.40 would give .59. When I have a genuine edge, put 0.35-0.55 on top pick, not 0.15-0.20. Spreading thin wastes points.
3. Downside of confident-wrong is bounded (~ -Σp²). Asymmetry favors confidence when I have real signal.
4. Don't assume gender/category (skier was female). Read Q carefully.
5. Void-likely Qs CAN resolve (Chelsea appointed Rosenior). But low-alloc still correct hedge.
ACTION: when updating/refining, push favorites higher where justified. Keep spreads only for true toss-ups.

## DAY 9 (Jan1) cont:
- Venezuela ESCALATING: "Trump bombs Venezuelan land for first time" headline; warns land ops "very soon". Maduro releasing prisoners (conciliatory), still in power. Watch 935533(Starlink->Venezuela?), 75613, 279531(Caribbean confirmed).
- Greenland: Denmark summoned US amb over envoy Jeff Landry(LA gov); still buying US P-8 planes. Dispute hot. Hold 630728/269293/621718.
- Bumped 207522 Sulawesi 0.62, 924864 Pakistan 0.58 (high-conviction, applying confidence lesson).
- T20 WC = India+SriLanka co-host confirmed. Pakistan in Grp A (India/USA/Namibia/Netherlands); P-I match Feb15 Colombo.

## DAY 10 (Jan 2) — RESULTS + AFCON FULL BRACKET
RESOLVED: Bangladesh->Sri Lanka (had 0.60, +82.31 HUGE). Venezuela interim->Delcy Rodriguez (VP, had 0.05, +5.74). Cumulative TW=124.63.
- Maduro STILL president Jan2 (releasing prisoners, "open to US talks"). Regime-change cluster NOT resolved; Venezuela Qs mostly hold (Maduro stays near-term).
### AFCON R16 (full bracket traced):
R16: Senegal-Sudan(J3); Mali-Tunisia(J3); Morocco-Tanzania(J4); SouthAfrica-Cameroon(J4); Egypt-Benin(J5); Nigeria-Mozambique(J5); Algeria-DRCongo(J6); IvoryCoast-BurkinaFaso(J6).
QF(J9-10): QF1=(Mali/Tunisia)v(Senegal/Sudan); QF2=(SA/Cameroon)v(Morocco/Tanzania); QF3=(Algeria/DRCongo)v(Nigeria/Mozambique); QF4=(Egypt/Benin)v(IvoryCoast/BurkinaFaso).
SF1=QF1wXQF4w; SF2=QF3wXQF2w. **MOROCCO in SF2; its SF opp=QF3 winner (Algeria/DRCongo/Nigeria/Mozambique ONLY).** Final=SF1 v SF2 (assumed Senegal v Morocco).
- 459037 Morocco SF opp FIXED: Nigeria.36/Algeria.26/DRCongo.16/Mozambique.06 (old had wrong-half teams!).
- 703511 DRC eliminator FIXED: Algeria.50/Nigeria.23/Morocco.11/Mozambique.04/Senegal.03.
- 343689 Morocco QF=Cameroon confirmed (needs Morocco bt Tanzania, Cameroon bt SA). Calf-injury player still unknown; hold low.
- REFINE after R16(J3-6) & QF(J9-10) results.
- Bumped Oscars: 876347 OBAA 0.50, 886103 PTA 0.52.

## DAY 11 (Jan 3) — RESULTS + VENEZUELA WAR
RESOLVED: Starlink->Venezuela (had #1 0.18, +30.32). Morocco injury->Ounahi (missed, -2.25). Cumulative TW=152.70.
- **US STRIKES INSIDE VENEZUELA (Jan3)**: Trump "US will run Venezuela until safe transition". Maduro likely removed/fled (explains Delcy Rodriguez interim). UN/Russia/EU condemn. ~500 UK nationals sheltering. Western-Hemisphere war scenario LIVE. Watch Venezuela cluster.
- Greenland: Danish PM Frederiksen defiant NY speech, summoned US amb over envoy Landry. Hold 630728(Trump/Rubio).
- LESSON reinforced 3x: my correct #1 picks under-weighted (0.18->+30). Amplify confident favorites. Bumped 951896 Sinner 0.48.
- Iran cluster: still conditional; US focus may be on Venezuela now, but Netanyahu still pushing Iran strikes. Hold.

## DAY 12 (Jan 5) — BIG DAY, TW=379.58 (+228 today)
RESOLVED: Syria Aleppo->SDF(0.32,+57.9); Iran complex->Parchin(0.22,+33.5); Greenland->Rubio(0.27,+33.8); DRCongo->Algeria(0.50 post-bracket,+40.9); BritishMPs WC->US(0.50,+71.0); ImmigrationState->MINNESOTA(missed,-9.4).
KEY MISS LESSON: I'd researched "Trump crackdown on Somali communities in Minnesota" Day1 but predicted Louisiana/CA for 915183. **CROSS-REFERENCE my own MEMORY/research notes when predicting!**
WINS confirm: confident favorites + bracket/structural analysis = big TW. 
- AFCON QF1=Senegal v Mali (J9). Senegal favored -> consistent w/ Morocco-Senegal final.
- Yemen: Saudi bombed Mukalla; Saudi-UAE fallout over STC offensive in Hadramout. al-Alimi appeals for Riyadh forum (watch 797906).
- 278197 Minneapolis woman shooting: nudged CBP up (Bovino Border Patrol leads MN surge); ICE 0.33/CBP 0.30.

## DAY 13 (Jan 6) — TW=513.75
RESOLVED: Minneapolis->ICE(0.33,+49.3); Qatar->Board of Peace(0.62,+84.9!). 
- **MADURO CAPTURED** Jan3 op, held in NYC, federal charges. Delcy Rodriguez acting pres. US to "run Venezuela" + tap oil. Regime change DONE.
- 269293 Greenland venue->State Dept bump (confirmed they're meeting Rubio). 
- 765155 added Caracas (Venezuela war = possible "regional conflict" w/ embassy evac).
- 822586 Carney-after-Beijing: NO confirmation Carney doing China trip (Irish PM Martin & S.Korea Lee are visiting Beijing, not Carney). May void; hold low.
- Greenland dispute HOT: Stephen Miller "Greenland should be part of US"; EU joint statement against.

## DAY 14 (Jan 7) — TW=562.78
RESOLVED: Greenland venue->White House (my late switch to StateDept was WRONG but held WhiteHouse 0.4 ~13d, TW saved +58.0). Carney->Qatar(miss -7.6). NATO->Arctic Sentry(miss -1.4).
LESSON: don't over-correct a sound prior w/o strong evidence (WhiteHouse switch was a mistake).
- AO 2026: Jan18-Feb1. MAIN DRAW ~Jan15 (NOT out yet). Tennis-opp Qs (2176/980781/793465/464874/922844/679570/789844/286957/287417/400561) -> predict ~Jan15.
- Brisbane Intl ongoing: Sabalenka cruising (beat Bucsa 6-0 6-1, R3 vs Ostapenko/Cirstea), on track to meet Keys in QF. 891998 final opp still unclear (Navarro is in Auckland not Brisbane).
- Madison Keys = defending AO champ (beat Sabalenka 2025 final).
- NEXT: AFCON QF J9-10 -> refine 459037; AO draw ~J15 -> tennis cluster.

## DAY 16 (Jan 9) — TW=643.07
RESOLVED: Morocco SF->Nigeria(0.36 bracket-fix,+30.6); TradeDeficit->Taiwan(0.18,+27.1); Grok->Indonesia(in list,+8.5); Yemen body->Supreme Military Committee(miss,-2.4); Brisbane final->Marta Kostyuk(miss,-4.6).
- **AFCON SF (Jan14)**: Morocco v Nigeria; Senegal v (IvoryCoast/Egypt - play Jan10). Final Jan18. 799398(Morocco-Senegal final, Hakimi pen miss) needs Morocco bt Nigeria + Senegal bt IvC/Egy. Hold Hakimi 0.35.
- **AO MAIN DRAW = THU JAN 15** 2:30pm local. Predict tennis cluster THEN: 2176,980781,793465,464874,922844,679570,789844,286957,287417,400561. Tournament Jan18-Feb1.
  Seeds: M: 1 Alcaraz,2 Sinner,3 Zverev,4 Djokovic,5 Auger-Aliassime. W: 1 Sabalenka,2 Swiatek,3 Gauff,4 Anisimova,5 Rybakina.
  951896 champ: hold Sinner 0.48 (2x defending champ, hardcourt) / Alcaraz 0.31 (#1 seed).
- Semenyo signed Man City from Bournemouth ($87m).

## DAY 17 (Jan 10) — FIRST NEG DAY, TW=622.42 (-20)
RESOLVED: Nipah->WEST BENGAL (I had Kerala 0.70!!, -33.6); IranProvince->ISFAHAN (I had Sistan 0.40, -19.3); ThaiPM->Natthaphong(0.22,+32.2).
**KEY CALIBRATION RULE (refined)**: 
- HIGH confidence (0.5-0.65) ONLY with CURRENT/specific evidence (Bangladesh->SriLanka, Board of Peace, current polls, bracket logic).
- MODERATE (<=0.45) for BASE-RATE-only favorites (Nipah-usually-Kerala, protests-usually-Sistan). The specific event often differs from historical norm! Kerala 0.70 & Sistan 0.40 were base-rate bets w/o current confirmation = overconfident.
- Trimmed 348570 ManCity 0.52, 207522 Sulawesi 0.55 (base-rate-ish).

## DAY 19 (Jan 12) — TW=720.33. ***EXACT-MATCH LESSON***
RESOLVED: UA opposition->Tymoshenko(had 0.08,+9.0); proIsrael->"Betar US" but I wrote "Betar"(0.35)=> SCORED AS MISS -14.3 (exact-string mismatch! would've been +56 if matched); Atletico->RealBetis(#1@0.12,+19.1).
***CRITICAL: USE PRECISE/CANONICAL ANSWER STRINGS.*** "Betar"!="Betar US". For orgs include suffix (US/Worldwide); people use FULL names; teams use common full name. When unsure of exact form, can list 2 variants but better to pick canonical. Cost ~70 pts on Betar.
- Tennis cluster (Jan15 draw): use FULL player names (e.g. "Carlos Alcaraz", "Jannik Sinner").
- Upcoming: AFCON SF Jan14 (Morocco-Nigeria, Senegal-?); AO draw Jan15; 279531 armada=Caribbean 0.6 (confident, resolves Jan14).

## DAY 20 (Jan 13) — TW=744.09
RESOLVED: SEAsia visa->Thailand(co-#1 0.36,+46.1); ICE NE->Maine(miss -14); Gaza head->Ali Shaath(miss low); Massie->Qatar(miss low); Gaza body->"Palestinian national committee"(miss low).
- AFCON SF Jan14: Senegal v Egypt (Tangier); Morocco v Nigeria (Rabat). Final Jan18.
  - 799398 (Morocco-Senegal final, Hakimi stoppage-pen miss): WAIT for SF results Jan14. If Morocco-Senegal final confirmed -> BUMP Hakimi to ~0.5 (conditional-on-resolution: he's the taker; void if final differs). Currently 0.35.
- Carrick = Man Utd interim REST OF SEASON (confirms 16281 frame). Xabi Alonso SACKED by Real Madrid, Arbeloa in.
- **TOMORROW-ish AO DRAW Jan15**: predict tennis cluster w/ FULL names. Seeds: M 1-Alcaraz 2-Sinner 3-Zverev 4-Djokovic; W 1-Sabalenka 2-Swiatek 3-Gauff 4-Anisimova 5-Rybakina.

## DAY 21 (Jan 14) — TW=707.16 (-37 day). ***IRAN WAR ACTIVATING***
RESOLVED: "big armada"->MIDDLE EAST (I had Caribbean 0.60! -37 OVERCONFIDENCE on anchored guess); basketball->"Chinese Basketball Association"(had "China", naming miss -5.3); UN food->Somalia(in list +5.4); migrant worker->El Hacen Diarra(skipped); Venus beaten by->Olga Danilovic(skipped).
***IRAN WAR IMMINENT (Jan14)***: Trump "Iranians keep protesting, help is on the way"; US evac Al Udeid(Qatar)+most ME bases; tankers->Iran; USS Gerald Ford repositioning Caribbean->ME. Iran protests ongoing (Isfahan casualties). IRAN-CLUSTER (~40 Qs) NOW LIKELY TO RESOLVE not void. My conditional favorites live: Tehran(city strikes), Qatar/Al Udeid & Iraq(US bases), TelAviv(Israel hits), Saudi/UAE(Gulf refineries), IRIB(broadcaster), ATACMS(HIMARS).
- AFCON: Senegal in FINAL (beat Egypt 1-0 Mane). Morocco-Nigeria SF pending. 799398: update tomorrow if Morocco reaches final (then bump Hakimi; note Brahim Diaz=top scorer 5 goals, possible pen taker).
- AO DRAW: still ~Jan15. Predict tennis cluster TOMORROW w/ full names.
- OVERCONFIDENCE TALLY: armada(-37), Nipah(-34), Dnipro/Oreshnik(-14). All were anchored/base-rate bets at 0.4-0.6 w/o specific current confirmation. RULE: cap at 0.45 unless CURRENT-SPECIFIC evidence.

## DAY 22 (Jan 15) — TW=718.40
RESOLVED: SyriaLang->Kurdish(0.32,+47.5!); Governor->Tim Walz(in list +10.5); SyriaFestival->"Newroz"(I had "Nowruz"-exact-match miss -7.3); Guehi->ManCity(I had Liverpool 0.40, -19.9); UAplanes->Czech Republic(I had Sweden 0.40, -19.6).
### AFCON FINAL = MOROCCO vs SENEGAL (Sun Jan18 Rabat)! Morocco beat Nigeria 4-2 pens (En-Nesyri decider, Bono saved 2). 3rd place Nigeria-Egypt Jan16.
- 799398 updated: Hakimi 0.40/En-Nesyri 0.18/Brahim Diaz 0.13 (penalty taker if Morocco gets stoppage-pen & misses).
### AO 2026 DRAW (out Jan15, tourney Jan18-Feb1):
- Men R1: Alcaraz v Adam Walton; Sinner v Hugo Gaston; Djokovic v Pedro Martinez. Halves: Sinner+Djokovic top; Alcaraz+Zverev+DeMinaur bottom. Projected Alcaraz R4 v Davidovich Fokina(14). Sinner R3 v Fonseca(28).
- Women R1: Sabalenka v Rakotomanga(WC); Swiatek v qualifier; Gauff v Rakhimova; Keys v Oliynykova. Halves: Sabalenka+Gauff+Venus top; Swiatek+Anisimova+Pegula+Keys+Rybakina+Osaka bottom. Raducanu(28) projected Sabalenka R3. Keys proj R4 v Pegula(6) -> Anisimova(4). Swiatek proj R4 v Osaka.
- Submitted: 464874 Raducanu 0.32; 789844 Davidovich Fokina 0.30; 286957 Keys-elim Pegula0.18/Anisimova0.14/Swiatek0.12.
- STILL TODO (refine as tourney plays): 2176 Alcaraz R2, 980781 Sinner R2, 679570 Osaka R3, 922844 Sonmez R3, 287417 Sabalenka QF, 400561 debutante-vs-Sabalenka.
- 951896 champ Sinner 0.48/Alcaraz 0.31 hold.

## DAY 23 (Jan 16) — TW=731.09
RESOLVED: SDF assault->Raqqa(#3 0.12,+13.8); Karachi fire->Gul Plaza(miss low); UDP->Malinowski & Indonesia plane(skipped).
- **505500 Portugal STALE FIX**: Jan14 poll Ventura 24%/Seguro 23%/Cotrim deFigueiredo 19%/Gouveia eMelo ONLY 14%(faded!). Election Sun Jan18, runoff Feb8. Ventura makes runoff; 2nd spot=Seguro or Cotrim. Updated: Seguro 0.35/Cotrim 0.22/GouveiaeMelo 0.13. (LESSON: recheck "frontrunner" assumptions w/ CURRENT polls before resolution!)
- **IRAN WAR IMMINENT**: Trump may strike "within 24h", "surgical regime removal"; US/UK evac ME bases, UK closed Tehran embassy; 2500+ protest deaths. Iran cluster resolving soon - MONITOR daily, update as specific strikes named.
- Myanmar: USDP (military party) winning election (3-phase, final Jan25). 243685 Myanmar panel - watch.
- AFCON final Morocco-Senegal Sun Jan18. AO starts Jan18.

## DAY 24 (Jan 17) — TW=776.66 (+45 day!)
RESOLVED: Bangladesh party->NCP(0.25,+40.5); Portugal->Seguro(updated 0.35,+17.1 - STALE-FIX WIN!); AFCON pen->Brahim Diaz(diversified 0.13,+1.9); Pakistan boycott->Bangladesh(miss low); Spain train town->Adamuz/dest->Huelva(miss); Alcaraz R2->Hanfmann(skipped).
- IRAN: Trump signaled OFF-RAMP (said Iran killings "stopped, no executions") - full strike PAUSED not launched. June2025 12-day war was PAST. New standoff may/may not escalate. Iran cluster stays conditional (void=neutral). Monitor.
- VALIDATION: stale-fix on Portugal = ~36pt swing. ALWAYS recheck favorites vs current data pre-resolution.
- Tomorrow Jan18: AFCON FINAL Morocco-Senegal; AO R1 starts; 37248 Bulgaria(Iotova 0.3); 551676 al-Shaddadi; 904367 Syria city.

## DAY 25 (Jan 18) — TW=857.25 (+80 day!)
RESOLVED: Bulgaria->Iliana Iotova(VP succession 0.30,+50); al-Shaddadi base->"Syrian army"(my "Syrian government forces" 0.30 MATCHED,+40 - note semantic fuzzy-match works sometimes); Syria city->al-Shaddadi(missed, was the OTHER Q's entity -9.3).
- LESSON: cross-ref entities across questions (al-Shaddadi base Q + al-Shaddadi city A).
- Matching is SEMI-fuzzy: "Syrian government forces"≈"Syrian army" OK, but "Betar"≠"Betar US", "Nowruz"≠"Newroz" failed. Still use canonical/precise forms.
- UPCOMING: AO R1 thru Jan20; tennis R3/QF resolve Jan20-24 (464874 Raducanu 0.32 done; 287417 Sabalenka QF + 679570 Osaka R3 + 922844 Sonmez R3 TODO when draws clearer). Oscar noms ~Jan22 (876347 OBAA 0.50, 886103 PTA 0.52). Jan21: 348570 Deloitte, 48762/655453 Ukraine talks city/mediator, 944348 TikTok CEO.

## DAY 26 (Jan 20) — TW=880.21
RESOLVED: BoardOfPeace->PAKISTAN(0.58,+78.3!); oldest paintings->Muna island(I had Sulawesi 0.55, -37!); Sabalenka R3->Potapova(#2 0.12,+2.1); Greenland deal->Mark Rutte/NATO(miss -9.9); Sonmez R3->Putintseva(skipped).
***OVERCONFIDENCE PATTERN CONFIRMED (4th time ~-35ea): Sulawesi(-37), Nipah(-34), armada(-37), all BASE-RATE/anchored favorites @0.5-0.7.*** vs WINS = CURRENT-EVIDENCE favorites (Pakistan/BoardOfPeace +78, Bangladesh-SriLanka +82, Bulgaria-Iotova +50, Thai poll +58).
**HARD RULE: base-rate/historical/anchored favorite => CAP 0.40. Current-specific-evidence favorite => OK 0.5-0.65.** "which island/city" wants SPECIFIC name not region.
- Hold most; apply discipline to NEW preds. Upcoming Jan21-22: Oscars(876347 OBAA 0.50/886103 PTA 0.52 - current-evidence OK); 348570 Deloitte ManCity ~0.5(base-rate-ish, watch); 48762/655453 Ukraine talks city/mediator; 944348 TikTok CEO.

## DAY 27 (Jan 21) — TW=910.43 (NFL update)
- NFL Conf Champs Jan25: AFC=Patriots@Broncos(Stidham for injured Nix); NFC=Rams@Seahawks(Seattle crushed SF 41-6, Rams beat Bears OT). All others OUT.
- 694686 NFC QB updated: Sam Darnold 0.52 / Matthew Stafford 0.46 (CERTAIN one of these - current evidence).
- 180958 SB winner updated: Patriots 0.28/Seahawks 0.27/Rams 0.23/Broncos 0.14.
- Oscars: most noms = SINNERS (Coogler), not OBAA frontrunner. Diversification saved me. 876347/886103 resolved.
- Watch: Jan24 286957 Keys-elim & 287417 Sabalenka QF (AO progressing); Jan25 conf champs; Feb1 Grammys; Feb8 SB.

## DAY 28-29 (Jan22-23) — TW=1016 (crossed 1000!)
RESOLVED: Crans-Montana->Italy(in list +11); MilanOlympics agency->ICE(0.40,+60); UkraineTalks Feb4->Abu Dhabi(bumped 0.30,+34); CAwildfire->FEMA(in list +6); Alcaraz R4->Tommy Paul(miss low); UFC HoF->Dominick Cruz(miss low).
- NFL conf champs Jan25: 694686 Darnold0.52/Stafford0.46; 180958 Pats0.28/Seahawks0.27/Rams0.23/Broncos0.14 SET.
- Routine working well. Stay efficient. Next deep-dives: Grammys Feb1, SuperBowl Feb8, WinterOlympics Feb6-22, T20WC Feb7+, Iran-war escalation.

## DAY 33-34 (Jan26-27) — TW=1016.74
RESOLVED: SuperBowl=Patriots vs Seahawks(Pats beat Broncos 10-7 snow). 180958 updated Seattle 0.53/Pats 0.47 (2-team certainty). UN nuke mtg->Netherlands(3rd party! I had Russia/Ukraine 0.65, -21 overconfidence). Fury->Makhmudov(miss); AusLeader->Herzog(in list +16); BisanOwda->TikTok(diversification saved, Instagram 0.40 wrong but TikTok 0.12 hit +4).
- LESSON: "which country/platform does X" - obvious party often WRONG; diversify, cap obvious favorite <=0.40.
- **UCL PLAYOFF DRAW = FRI JAN 30** (league phase ends Jan28). Predict 35131(Juve elim)/55999(Benfica opp)/85609(RealMadrid opp)/261538(Newcastle leg1 city) AFTER draw ~Jan30-31. NOTE: RealMadrid(3rd) & Newcastle(7th) currently TOP-8 => may get BYE => those Qs VOID. Benfica(29th) likely eliminated => 55999 voids.
- Grammys Feb1: 946810 AOTY toss-up Kendrick0.28/BadBunny0.24/Gaga0.18 hold. BadBunny=SuperBowl halftime.

## DAY 36-37 (Jan29-30) — TW=1121
RESOLVED: Epstein CommerceSec->Howard Lutnick(0.35,+55.5!); USskier->Lindsey Vonn(0.18,+28.9!); UCL playoffs (35131/55999/85609/261538) resolved Jan29 - I'd DEFERRED & scored 0 (RealMadrid<->Benfica drawn, Newcastle->Baku, Juve->Galatasaray). LESSON: don't defer draw-Qs past the actual draw; predict day-of.
- ***CRITICAL Q951896 SAVE***: Djokovic BEAT Sinner in SF! AO FINAL = ALCARAZ vs DJOKOVIC (Feb1). Updated Alcaraz 0.62/Djokovic 0.36 (was Sinner 0.48 - would've been disaster). LESSON: ALWAYS verify bracket/matchup before final-day resolution.
- 946810 Grammy AOTY (Feb1): expert forecasts favor BAD BUNNY (1st all-Spanish AOTY). Updated BadBunny 0.32/Kendrick 0.27/Gaga 0.16.
- Feb1-2 also: 102687 NorwegianPM corruption(Solberg 0.40), 453736 Libya killed(Saif Gaddafi 0.45), 220862 ManCity LeagueCup opp, 955662 Brazil bus state.

## DAY 47-48 (Feb11-12) — TW=1530.83 (halfway, strong!)
RESOLVED: Bangladesh oppo->Jamaat(0.52 held from Day1,+71.4!); Carrier->USS Gerald R Ford(0.18,+28.1); FrenchCity->Lyon(in list +9.3); Tractor->Shabab Al-Ahli(miss low).
LESSON CONFIRMED: early structural picks (Jamaat, Board of Peace, etc.) HELD to resolution = max BSS×100. 
- **T20 WC** (Feb7-Mar8, India+SriLanka; Bangladesh OUT->Scotland): GrpA India&Pakistan(both 2-0, clash Feb15 Colombo) +USA/Neth/Namibia. GrpB Australia/SriLanka/Ireland/Zim/Oman. GrpC WestIndies LEADING/England STRUGGLING(lost to WI)/Nepal/Italy/Scotland. GrpD NZ/SouthAfrica/Afghanistan(0-2 likely OUT)/Canada/UAE. Top2 each ->Super8.
- 454482 (former champ fails Super8): updated England 0.30 (struggling). 190197 light update.
- T20 Qs to watch: 307616(Pak Super8 opener Feb17), 992626(Grp1 1st Feb22), 333107(SA semi opp Feb27), 156/?.
- IRAN: talks in Oman going "very good", de-escalation; war cluster less likely near-term. 415069 Oman/489902 Muscat well-placed.

## DAY 49 (Feb13) — TW=1494.83. ***OVERCONFIDENCE AUDIT***
RESOLVED: Navalny toxin->EPIBATIDINE (I had Novichok 0.60! -36). Rail pair->Rome-Naples(skipped).
***BIGGEST SYSTEMATIC ERROR = overconfidence on OBVIOUS/KNOWN/BASE-RATE answers @0.55-0.70: Novichok(-36), Sulawesi(-37), Nipah-Kerala(-34), armada-Caribbean(-37). ~-144 total. If capped @0.40 would've saved ~84pts.***
HARD RULE going forward: top pick <=0.45 UNLESS current-specific-evidence (poll/bracket/cross-Q/confirmed-fact). "Obvious because of history/prior-event" != certain. Diversify always.
- Most overconfident bets already resolved; just avoid NEW ones. Remaining active mostly <=0.45 (good).
- Upcoming: India-Pak T20 Feb15; 454482 England 0.30; Olympics medals (162065 Italy 30 medals Feb21, 221278 hockey Canada Feb21).

## DAYS 58-62 (Feb19-25) — TW=1594.77 (~58% resolved)
KEY WINS: Italy 30 medals(bumped 0.48,+56); USA hockey(2-team sizing,+31); Barca de Jong(+20); Brazil flood MinasGerais(+17); UK mosque Manchester(+15); Columbia univ(+19); Crete(+28).
KEY LOSSES (overconfidence/single-answer): Lebanon cmd ctr->HAMAS(I had Hezbollah 0.55 NO ALTS, -30!); Navalny->epibatidine(Novichok 0.60,-36); SA capt->Maharaj(Markram 0.40,-18). => DIVERSIFY ALWAYS, cap obvious @0.45.
### IRAN WAR TIMING: Trump "15-day deadline" (~Feb22 -> ~Mar9). Massive buildup (2 carriers+Ford, jets to Israel, Khamenei threats). NOT erupted yet (Vienna/Oman talks ongoing). => Feb27-28 Iran-war Qs likely VOID; MARCH Iran-war Qs may ACTIVATE if deadline passes. Conditional favorites hold (Tehran/TelAviv/AlUdeid-Qatar/IRIB/ATACMS).
- CL R16 DRAW Fri Feb27: Newcastle vs Barcelona-or-Chelsea (915784 0.45/0.45). Arsenal vs Leverkusen-or-Bayern region. Inter OUT (Bodo/Glimt upset).
- Ship names need prefix: IRIS(Iran)/USS/HMS. Diplomatic talks venues: include Vienna/Austria.

## DAY 65 (Feb27) — TW=1712 (+109 day!). ***IRAN WAR ERUPTED (joint US-Israeli strikes)***
RESOLVED: city explosions->TEHRAN(0.40,+62!); Iran can't WC->IRAN(0.50,+74!); Trump talks collapsed->Geneva(in list,+11); BUT specific-incident cities MISSED: boys'school->Qazvin, girls'school->Minab (Tehran wrong for small incidents); SA T20 semi->New Zealand; airspace->Qatari.
### IRAN WAR FACTS (for cluster, ~25 Qs resolving now-March):
- US strikes from ISRAEL(F-22s)+JORDAN. **SAUDI & UAE REFUSED airspace/bases (neutral)** -> Iran may SPARE them. Iraq US presence REDUCED (Al Asad transferred).
- US bases in Iran range: Al Udeid(QATAR,CENTCOM HQ-prime target), NSA Bahrain(5th Fleet), Kuwait(Arifjan/AliAlSalem), PrinceSultan(Saudi), AlDhafra(UAE), Muwaffaq Salti(Jordan).
- Carriers: USS Abraham Lincoln(Arabian Sea), USS Gerald Ford(incoming).
- Updated 70713/169286 US-base: QATAR top, Iraq down.
- PATTERN: Tehran=favorite for MAJOR strikes; SMALL incidents (schools/hospitals) in OTHER cities (Qazvin,Minab) - keep Tehran ~0.30 + DIVERSIFY for specific-incident Qs.
- Remaining Iran Qs hold conditional favorites: 13213 TelAviv, 354370 ATACMS, 994042 IRIB, 214539 Kharg, 863162 Saudi/UAE(maybe spared-reconsider), 297818 AbuDhabi.

## DAYS 66-67 (Feb28-Mar1) — TW=1843 (+141 day!). IRAN WAR "Operation Epic Fury"
- US+Israel struck Iran leadership: KHAMENEI KILLED, DefMin Nasirzadeh, IRGC Pakpour killed. 24 provinces, 201+ dead, 2 schools(Minab/Qazvin). Iran retaliated vs Israel+Gulf. ABU DHABI/Dubai hit. KUWAIT friendly-fired 3 US F-15s + US troops killed there. Gulf energy strike=Ras Laffan(Qatar LNG).
- BIG WINS (Day-1 conditional favorites HELD): IRIB(0.40,+62!); AWS->Bahrain(+39); Taliban->Rawalpindi(+34); fruit->S.Africa(+32); HIMARS->PrSM(+16); Kuwait base(+7).
- Updated: 864964 Khamenei0.46, 297818 AbuDhabi0.48, 863162 UAE up, 887402 Kuwait0.42(F-15 friendly fire), 169286 Kuwait/Qatar.
- REMAINING Iran Qs (March): 214539 Kharg(island), 779990 Saudi city, 560679 ADNOC/AbuDhabi, 58520 Katz/Netanyahu, 669234 central Israel, 79608 Iran city, 668257 IRGC spox, 26340 UAE desalination, 679215 ship, 765155 capital evac.
- LESSON: read Q carefully (971319 "Gulf energy strike"=Ras Laffan not Tel Aviv - I misread as Israel).

## SIMULATION COMPLETE (Mar 28) — ALL 330 RESOLVED. FINAL TW-SCORE = 1834.08
- accuracy 18.2%, brier skill 0.064. Predicted 298/330 (32 skipped unguessable). Peak TW ~1965 (early Mar), drifted to 1834 in lottery-heavy endgame.
### TOP WINS (current-evidence favorites held early): Bangladesh->SriLanka +82; Pakistan BoardOfPeace +78; Iran can't WC +74; Bangladesh oppo Jamaat +71; Saif Gaddafi killed +69; Canada school shooting +80(cross-Q); IRIB +62; Tehran explosions +62; SuperBowl Seattle +30; measles SC +28...
### BIGGEST LOSSES (overconfidence on obvious/base-rate, single-answer): Hezbollah cmd ctr -25 & -30 (Hamas/Jama'a); Navalny Novichok -36(epibatidine); Sulawesi -37(Muna); Nipah Kerala -34(WBengal); armada Caribbean -37(MiddleEast); Latvia drone Russia -24(Ukraine).
### KEY LESSONS (for future sims):
1. Current-evidence favorite -> bet 0.5-0.65. Base-rate/obvious/anchored -> CAP 0.40, ALWAYS diversify 3-5 outcomes (never single-answer!).
2. Cross-question entity inference = huge (+69, +80). Link same-event Qs.
3. Exact strings: prefixes (IRIS/USS), full org names (Betar US), regional spellings (Newroz). 
4. Predict EARLY & hold (TW = BSS x days held). Late correct preds get low TW.
5. "Obvious party" often WRONG (US not Israeli embassy; Hamas not Hezbollah; Ukraine not Russia; Macron not Trump). Diversify obvious.
6. Read Q carefully (which country/region/who specifically).
7. Conditional/scenario clusters (Iran war): void=neutral, so conditional favorites are safe upside. Iran war DID erupt Feb28 -> cluster paid off big.
