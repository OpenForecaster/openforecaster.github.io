# Daily Log & Forward Plan

## Day 1: 2025-12-24
- Read all 330 questions (memory/questions_overview.txt). Forecasts in forecasts_master.json.
- Submitted forecasts on 327/330 questions. Abstained on 3 unknowable-name questions:
  521564 (migrant worker name), 672298 (UDP NJ primary target), 350082 (Michigan synagogue assailant).
  Rationale: q≈0 for any name guess → E[Brier]=−Σp² < 0, worse than abstain(0).
- Dispatched 7 research subagents (tennis/Olympics, football, cricket, US-pol/elections, Iran-war ME, disasters, gaps).

## KEY BUG FIXED
- Some submissions used SEQUENCE numbers (#N) instead of QID. The seq→qid map in questions_overview.txt
  (format "#N [date] QID (type)") was used to fix all keys. ALWAYS submit by QID (the big number), never #N.

## Scenario understanding (crucial for ~150 Qs)
- Simulated US-ISRAEL WAR ON IRAN erupts ~late Feb 2026. Cluster Qs #200-330 reference it.
- Recurring answers: Gulf countries (Saudi/UAE/Qatar/Bahrain/Kuwait), Iranian cities (Tehran/Isfahan),
  Strait of Hormuz, Lebanese districts (Nabatieh/Tyre/Dahiyeh), Israeli towns (Tel Aviv/Bat Yam/Kiryat Shmona).
- AFCON 2025 happening NOW in Morocco (Dec 21-Jan 18). Groups known. Bracket forming.
- Syria: interim Pres Ahmed al-Sharaa; FM Assaad al-Shaibani; Def Min Murhaf Abu Qasra.

## HIGH-CONFIDENCE anchors (my best edges)
- 836984 Oreshnik city = Dnipro (0.80); 264/742975 aircraft = MQ-9 Reaper (0.78)
- 238071 Sudan siege = North Darfur (0.78); 392014 Congo = Goma (0.80)
- 652747 Navalny toxin = Novichok (0.82); 783773/666021 Somalia = Ethiopia (0.80/0.75)
- 291796 Nipah = Kerala (0.82); 93950 measles = Texas (0.60)
- 630728 Greenland meeting = Trump (0.80); 974962 Eritrea host = Asmara (0.82)

## Tomorrow's priorities (2025-12-25)
1. Re-submit ALL forecasts (they persist? check predictions/ dir) — if they carry over, skip; else re-submit.
   Actually: next_day() just advances date; forecasts stay active until I update. Confirm via my_prediction column.
2. Refine AFCON Qs as bracket firms up (search news): 703511, 459037, 799398, 573851.
3. Research resolvable-soon questions (Jan 1-10) more deeply: 165622 Chelsea mgr, 892867 Austrian skier,
   227432 Ukraine def min, 651727 Venezuela interim pres, 93950 measles.
4. Sharpen Oscar/Grammy (876347/946810/886103) — nominees firming up.
5. Reconsider weak guesses; tighten calibration where news gives signal.

## Calibration note
- Kept probabilities modest (top guess usually 0.2-0.45) reflecting genuine uncertainty on scenario Qs.
- For outcome-space-huge questions (specific towns), spread 4 guesses ~0.1-0.3.

## Day 2: 2025-12-25
- Confirmed all 327 forecasts persisted and still active.
- AFCON bracket still early (matchday 1-2); can't sharpen 703511/459037/799398/573851 yet.
- Chelsea: Maresca stable on 5-yr deal, no sack news -> kept spread.
- Oscar search returned 97th-ceremony data only; kept PTA "One Battle After Another" bet.
- No decisive new evidence -> did NOT churn. Update promptly when events resolve (AFCON R16 Jan 3-6).

## Day 3: 2025-12-26
- 327 forecasts still active. AFCON matchday-2 games TODAY (results not yet in article corpus).
- Learned: Maria Corina Machado won 2025 Nobel Peace Prize (Oct 2025) -> bumped 651727 Machado 0.22->0.30 (Gonzalez 0.6->0.5).
- Tomorrow: check AFCON Dec 26 results (Morocco v Mali, Egypt v SA) to sharpen bracket Qs.

## Day 4: 2025-12-27
- 327 forecasts active. AFCON matchday-2 results not surfacing in corpus yet (article still shows thru Dec 23).
- Bracket can't sharpen until R16 (Jan 3-6). No decisive new info -> no churn.
- Plan: when R16 bracket firms up (Jan 3-6), update 703511/459037/799398/573851. Also research Oscar/Grammy/election nominees deeper on a fresh-context day.

## Day 5: 2025-12-28
- AFCON standings thru MD2-3 (from article corpus):
  A: Morocco 4(W,D) QUAL-WON, Mali 2, Zambia 2, Comoros 1. [MD3: Comoros-Mali, Zambia-Morocco]
  B: Egypt 6 WON, South Africa 3, Angola 1, Zimbabwe 1. [MD3: Angola-Egypt, Zimbabwe-SA]
  C: Nigeria 6 WON, Tunisia 3, Uganda 1, Tanzania 1. [MD3: Tanzania-Tunisia, Uganda-Nigeria]
  D: Senegal 4(+3), DR Congo 4(+1), Benin 3, Botswana 0. [MD3: Benin-Senegal, Botswana-DRC]
  E: Algeria 6 WON, Sudan 3, Burkina Faso ~3, Eq Guinea 0. [MD3: EqG-Algeria, Sudan-BF]
  F: Ivory Coast 4(+1), Cameroon 4(+1), Mozambique 3, Gabon 0. [MD3: Gabon-IC, Moz-Cameroon]
- R16 bracket key: R16-7 = 1E(Algeria) v 2D(DR Congo). => Updated 703511 Algeria=0.38 (top candidate to knock DRC out).
- Groups won: Morocco(A), Egypt(B), Nigeria(C), Algeria(E). D & F undecided (Senegal/IC leading).
- Next: after MD3 (Dec 31) & R16 (Jan 3-6), firm up 459037(Morocco SF opp), 799398(penalty), 573851(CAS appeal).

## Day 6: 2025-12-29
- AFCON MD3 partial: Morocco 3-0 Zambia (WON Group A, 9pts perfect). Mali 0-0 Comoros (Mali 2nd). Egypt 0-0 Angola (Egypt won B, 7pts). SA 3-2 Zimbabwe (SA 2nd, 6pts).
- Morocco dominant -> strengthens 799398(final penalty)/459037(SF) premises. Updated 799398: Hakimi 0.3 top (primary penalty taker).
- Groups C/D/E/F MD3 Dec 30-31. R16 Jan 3-6 will firm bracket. Conserve context for Jan event-driven updates.

## Day 7: 2025-12-30
- AFCON MD3 final (Groups C,D): Nigeria 3-1 Uganda (won C, 9pts). Tanzania 1-1 Tunisia (both qualify; Tanzania 1st-ever KO). Senegal 3-0 Benin (won D). DR Congo 3-0 Botswana (2nd, 7pts) -> CONFIRMED R16 vs Algeria.
- CONFIRMED R16 bracket (Jan 3-6):
  R16-1: Senegal(1D) v 3rd(B/E/F); R16-2: Mali(2A) v Tunisia(2C); R16-3: Morocco(1A) v 3rd(C/D/E);
  R16-4: SouthAfrica(2B) v 2F; R16-5: Egypt(1B) v 3rd(A/C/D); R16-6: Nigeria(1C) v 3rd(A/B/F);
  R16-7: Algeria(1E) v DR Congo(2D); R16-8: 1F v 2E.
- Morocco SF path: QF2(R16-3/R16-4 winners) -> SF1 vs W(QF1)= Senegal or Mali/Tunisia.
- Updated 703511 Algeria=0.42 (R16 opp confirmed); 459037 Senegal=0.32 (Morocco's likely SF opp via bracket).
- Groups E/F finish Dec 31. R16 Jan 3-6. Then refine knockout-resolved Qs.

## Day 8: 2025-12-31
- 5 Qs resolve 2026-01-01: 165622(Chelsea), 227432(Ukraine def min), 628026(Charlotte NYE), 892867(Austrian skier), 93950(measles).
- 93950: Texas measles (Gaines Co) confirmed dominant -> bumped Texas 0.6->0.68.
- 628026: no Charlotte-specific NYE plot in real news (LA/Detroit/NOLA only) -> kept Charlotte-suburb spread.
- Others: no decisive new signal, kept spreads.
- NEXT: after next_day, check if ground_truth revealed for resolved Qs -> calibrate learning.

## Day 9: 2026-01-01 — CALIBRATION CRISIS (5 Qs resolved)
RESOLVED TRUTHS vs my picks:
- 165622 Chelsea = LIAM ROSENIOR (I had Maresca/Potter/Tuchel/Mancini). Brier -0.11
- 227432 Ukraine def min = MYKHAILO FEDOROV (I had Umerov 0.55). Brier -0.32
- 628026 Charlotte = MINT HILL (I had Concord/Gastonia/etc). Brier -0.11
- 892867 Austrian skier = KATHARINA LIENSPERGER (WOMAN; I only listed men!). Brier -0.10
- 93950 measles = SOUTH CAROLINA (I had Texas 0.68!). Brier -0.48 (worst)
Cumulative TW: -105.06 over 5 Qs (mean -21/Q).

### CRITICAL LESSONS
1. **Benchmark picks SURPRISING/non-obvious answers.** "Obvious" real-world priors are systematically WRONG (Texas measles->SC, Umerov->Fedorov, male skiers->woman).
2. **OVERCONFIDENCE = severe penalty.** p=0.68 on wrong Texas gave -0.48. Keep top p <= 0.5-0.6 for uncertain scenario Qs.
3. **BROADEN candidates beyond obvious**: include women for gendered-neutral Qs, less-prominent politicians, surprising picks.
4. **Real-world priors unreliable**: simulated timeline has own outbreaks/events diverging from reality.

### ACTIONS TAKEN
- Recalibrated 11 high-p (>0.6) forecasts down to 0.5-0.66 with broader spreads.
- Reduced concentration on 468637, 651727 (resolve Jan 2).

### FORWARD RULE
- Cap top prob ~0.45-0.55 for scenario/uncertain Qs. Only exceed for definitional facts (capitals, documented toxins).
- When a question seems "obvious," deliberately add 1-2 non-obvious alternatives.

## Day 9 cont. — AFCON FULL R16 BRACKET (confirmed after group stage):
E: Algeria 9(WON), Burkina Faso 6(2nd), Sudan 3(3rd), EqGuinea 0.
F: Ivory Coast 7(WON), Cameroon 6(2nd), Mozambique 3(3rd), Gabon 0.
R16: [1]Senegal v 3rd(B/E/F) [2]Mali v Tunisia [3]Morocco v 3rd(C/D/E) [4]South Africa v Cameroon
    [5]Egypt v 3rd(A/C/D) [6]Nigeria v 3rd(A/B/F) [7]Algeria v DR Congo [8]Ivory Coast v Burkina Faso
- Group winners: Morocco(A), Egypt(B), Nigeria(C), Senegal(D), Algeria(E), Ivory Coast(F).
- 703511 (Algeria v DRC) and 459037 (Morocco SF vs Senegal-path) well positioned.
- Next event-driven update: R16 results Jan 3-6, QF Jan 9-10.

## Day 10: 2026-01-02
- 468637 Bangladesh ICC = Sri Lanka (I had 0.22 2nd) -> Brier +0.22! SPREADING WORKS. TW +27.59.
- 651727 Venezuela = DELCY RODRIGUEZ (Maduro regime figure, not opposition!). I assumed opposition. Lesson: consider regime-side candidates for "interim president."
- Cumulative TW -112.33 over 7 Qs.
- Broadened 343689 (Morocco injury: added Rahimi/Diaz) and 935533 (Starlink: spread Gaza/Ukraine/Yemen/Iran/Lebanon) before Jan 3 resolve.
- R16 starts Jan 3 (Senegal game). Watch for bracket results to update 703511/459037/799398/573851.

## Day 11: 2026-01-03
- 343689 Morocco calf = Azzedine Ounahi (missed, Brier -0.05 - spread kept it small). 935533 Starlink = VENEZUELA (surprise! Venezuela subplot x2: Delcy Rodriguez + Starlink). Cum TW -137.92.
- Updated 709715 (resolves Jan 4): Svyrydenko 0.2, Fedorov 0.15 (timeline likes tech figures).
- AFCON R16 Jan 3: Senegal 3-1 Sudan; Mali bt Tunisia on pens. => QF: Senegal v Mali. Winner = Morocco's SF opp.
- Updated 459037: Senegal 0.5 (favored over Mali in QF), Mali 0.2.
- Morocco R16 (vs 3rd-place) Jan 4. Algeria v DR Congo Jan 6 (key for 703511).
- VENEZUELA SUBPLOT insight: simulated timeline has Venezuela events (interim pres Delcy Rodriguez, Starlink to Venezuela). Watch for more.

## Day 12: 2026-01-04
- 709715 Ukraine econ adviser = CHRYSTIA FREELAND (Canadian! cross-national surprise). Brier -0.08 (spread helped). Cum TW -141.15.
- 6 Qs resolve Jan 5: 369962, 915183, 433526, 630728, 703511, 814175. All already calibrated (top 0.28-0.6). No churn.
- AFCON R16 Jan 4: Morocco 1-0 Tanzania; Cameroon 2-1 South Africa. => QF: Morocco v Cameroon (Jan 9). Confirms 343689 premise.
- Morocco SF path confirmed: beat Cameroon QF -> face Senegal/Mali winner. 459037 (Senegal 0.5) solid.
- Next: QF Jan 9-10 (Morocco-Cameroon, Senegal-Mali, Algeria-DRC already Jan 6) -> refine 703511/799398/573851.

## Day 13: 2026-01-05 — BIG LEARNING BATCH (6 Qs)
POSITIVES (event-driven research pays!):
- 703511 DR Congo = Algeria (+0.64, +44.75) <- bracket research CORRECT & well-calibrated.
- 369962 Syria Aleppo = SDF (+0.30) <- had SDF as 2nd pick (0.24).
SURPRISES (timeline picks non-obvious):
- 433526 Iran complex = PARCHIN (not Natanz/Fordow). -0.22
- 630728 Greenland meeting = MARCO RUBIO (SoS, not Trump!). -0.17
- 814175 WC exclude = UNITED STATES (not Israel!). -0.21
- 915183 ICE op = MINNESOTA (not CA/TX). -0.16
Cum TW -165.46 over 16 Qs.

### MICRO-LESSONS (apply forward)
- "Meeting with senior US officials" -> Rubio (SecState), NOT Trump.
- Geographic Qs: timeline favors NON-obvious states (Minnesota, South Carolina). Add 1-2 long-shot US states.
- Iran military sites: Parchin (not just Natanz/Fordow).
- "Exclude from World Cup": could be US (Trump backlash).
- EVENT-DRIVEN sports research (bracket tracking) = highest ROI. Continue for AusOpen, UCL, T20, Olympics.

## Day 14: 2026-01-06
- 278197 Minneapolis = ICE. 857643 Qatar peace body = "Board of Peace" (fictional name in timeline; also q924864). Cum TW -190.84.
- AFCON QF (Jan 9-10) SET: Senegal-Mali, Morocco-Cameroon, Egypt-Nigeria, Algeria-Ivory Coast.
  Algeria 1-0 DRC(AET); Nigeria 4-0 Mozambique; Ivory Coast 3-0 BF; Egypt advanced.
- SF1 = W(Senegal/Mali) v W(Morocco/Cameroon); SF2 = W(Egypt/Nigeria) v W(Algeria/IC).
- Updated 573851 (CAS appeal/losing finalist): Algeria/Nigeria/Egypt/IC (SF2 teams).
- 3 Qs resolve Jan 7: 269293(Washington DC for Greenland talks), 822586(Carney), 85534(NATO mission name-guess). All moderate.
- HIGH-VALUE upcoming: AusOpen starts Jan 6! Track draw/results for tennis Qs (2176,980781,793465,951896 etc).

## Day 15: 2026-01-06 (cont)
- Searched AusOpen 2026 draw: NOT YET OUT (draw ~Jan 8-9, matches ~Jan 12). Tennis Qs can't sharpen until then. Revisit after draw.
- Updated 573851 (CAS appeal) to SF2 teams per bracket.
- 3 Qs resolve Jan 7: 269293(Greenland talks loc=Washington DC), 822586(Carney), 85534(NATO mission name). Moderate.
- STRATEGY: conserve context. Each day do 1-2 targeted checks. Deep research only when deterministic info drops (AusOpen draw Jan 8-9, AFCON QF Jan 9-10/SF Jan 14/final Jan 18).
- ONGOING: track AFCON QF results Jan 9-10 to confirm Morocco SF opponent (459037 Senegal 0.5).

## Day 16: 2026-01-07
- 269293 Greenland talks = White House (specific building, not "Washington DC"). 822586 Carney = Qatar. 85534 NATO = Arctic Sentry (close to my Arctic Guardian). Cum TW -225.91.
- Broadened 812287 (carrier): Carl Vinson 0.35 (was 0.5).
- 5 resolve Jan 8: 423343(Jenin), 567250, 787699(Thai poll), 812287(done), 836984(Dnipro 0.5).
- LESSON: location Qs may want specific BUILDING (White House) not city.
- NEXT high-value: AFCON QF Jan 9-10 (Morocco-Cameroon, Senegal-Mali) -> confirm 459037. AusOpen draw ~Jan 8-9.

## Day 17: 2026-01-08
- Resolutions: 423343=East Jerusalem, 567250=Qatar(-0.05 good spread), 787699=People's Party(+0.33! had 2nd), 812287=USS Abraham Lincoln, 836984=LVIV(not Dnipro!). Cum TW -295.63.
- KEY LESSON: candidate SET must include right answer. Oreshnik=LVIV, carrier=LINCOLN — I missed both. Use all 5 slots, include less-obvious.
- Broadened 45659 (Grok ban) to 5 options. Brisbane 2026 final not in corpus -> kept Rybakina 0.32.
- 5 resolve Jan 9: 45659(done), 459037(Senegal 0.5, game today), 46876, 797906, 891998.
- NEXT: AFCON QF results (Senegal-Mali today) -> confirms 459037. Then SF Jan 14, final Jan 18 (799398/573851).

## Day 18: 2026-01-09 (resumed)
- Last batch (31 resolved, cum TW -373.55): 45659=Indonesia, 459037=NIGEDIA(! Morocco SF opp=Nigeria not Senegal), 46876=Taiwan, 797906=Supreme Military Committee, 891998=Marta Kostyuk.
- AFCON QF Jan 9: Senegal 1-0 Mali; Morocco 2-0 Cameroon. => SFs: Morocco v Nigeria, Senegal v (Algeria/IC winner Jan 10).
- Lesson: my bracket-half reasoning was wrong (Nigeria in Morocco's SF). Sim timeline diverges.
- Updated: 934187 (Pita 0.3, People's Party momentum), 69214 (Sistan 0.5 + Tehran/Kurdistan), 573851 (Senegal 0.24 - SF1 winner is losing finalist).
- 3 resolve Jan 10: 291796(Kerala 0.66), 69214(done), 934187(done).
- PENDING: 799398(final penalty - Hakimi 0.3), AFCON SF Jan 14, final Jan 18. AusOpen R1 starting ~Jan 12.

## Day 19: 2026-01-10 — BRUTAL LESSON
Resolutions: 291796 Nipah=WEST BENGAL (not Kerala!), 69214 Iran=ISFAHAN (not Sistan!), 934187 Thai PM=NATTHAPHONG (not Pita!). Even STRONG base-rate priors WRONG. Cum TW -471.90 over 34 Qs.
### META-PATTERN (ground truths deliberately pick LESS-OBVIOUS plausible alternative):
- Geo: West Bengal/Kerala, Isfahan/Sistan, SC/Texas, Minnesota/CA, Lviv/Dnipro, Taiwan/China.
- People: Natthaphong/Pita, Rosenior, Freeland, Liensberger (woman).
- Recurring: Qatar appears often (Carney, Kyiv embassy, mediator).
- I score POSITIVE when my 2nd pick is right (Sri Lanka, SDF, People's Party, Algeria).
### STRATEGY REVISION
- For "obvious" answer, make it 2nd (0.2-0.3); lead with or co-lead the plausible alternative.
- Cap tops at 0.35-0.45. Spread 4-5 diverse options.
- Reduced 783773/666021 (Ethiopia 0.4), 474377 (Amorim 0.34) before Jan 11.

## Day 19 cont: recalibrated ~22 high-p (>0.45) forecasts down to ~0.4 cap with broader spreads.
Covered: 974962,652747,742975,901381,887402,392014,238071,176447,994042,972999,579233,789042,863162,841822,803012,486189,415069,398988,304287,240291,207522,120805.
NOTE: forecasts_master.json is STALE; submitted forecasts are authoritative.
7 Qs resolve Jan 11: 118127,138247,474377(done),783773(done),666021(done),80352,756891.

## Day 20: 2026-01-11
- Positives: 118127 BRICS=Iran (had 2nd, +0.23), 80352 cabinet=DHS (+0.59!). Recalibration WORKS going forward.
- BUT 666021/783773 = UAE (not Ethiopia): TW -43/-41 because EARLY days locked high-Ethiopia losses before I recalibrated. Late recalib can't undo past weight.
### SOLID PATTERNS (apply to remaining similar Qs):
- Syria rebel/reinforcement groups = PKK (138247 & 756891 both PKK).
- Somalia antagonist = UAE (both Somalia Qs = UAE, not Ethiopia).
- Qatar = recurring mediator/location.
- Man Utd caretaker = Michael Carrick (474377).
- Cum TW -523.66 over 41 Qs.
- 3 resolve Jan 12: 117844, 359260, 98159 (all modest spreads, no churn).

## Day 21: 2026-01-12
- 117844 Ukraine opp = Tymoshenko (+0.17, had top). 359260=Betar US, 98159=Real Betis (missed). Cum TW -520.82 (stabilizing).
- Split 756639 Philippines/Thailand more evenly (0.4/0.3).
- 5 resolve Jan 13: 214384,71,756639(done),75613,806810 (all modest).
- LESSON: cum TW stabilizing now that forecasts calibrated ~0.4. Keep course.

## Day 22: 2026-01-13
- 214384 NE ICE=Maine, 71 Pal committee=Ali Shaath, 75613 Venezuela oil=QATAR(! recurring), 756639=Thailand(+0.35 split worked), 806810=Pal national committee. Cum TW -554.55.
- QATAR now confirmed answer ~4x (Carney, Kyiv embassy, peace body, Venezuelan oil). Elevate Qatar in financial/diplomatic Qs.
- AO 2026 draw/R1 not in corpus yet. Tennis Qs kept as spreads.
- 5 resolve Jan 14: 279531,39911,521564(abstain),736847,793465 (all modest).
- STRATEGY: minimal daily churn; deep-dive only when deterministic sports results appear (AO rounds, AFCON SF Jan 14/final Jan 18).

## Day 23: 2026-01-14
- 279531 armada=Middle East(+0.27), 39911=CBA, 736847=Somalia, 793465=Olga Danilovic, 521564=El Hacen Diarra(abstained). Cum TW -566.63.
- AFCON SF1: Senegal 1-0 Egypt (Mane) -> Senegal in FINAL Jan 18. SF2 Morocco v Nigeria (result pending Jan 15).
- CONFIRMED: Man Utd caretaker = Michael Carrick (474377 truth).
- Updated 573851 (CAS appeal): Senegal 0.32 (confirmed finalist), removed eliminated Algeria/IC/Egypt.
- 5 resolve Jan 15: 172391,406433,579233,599463,972999 (modest).
- AFCON final Jan 18. After final: 799398(penalty), 573851(CAS) resolve. Nigeria T20 WC relocation also recurring.

## Day 24: 2026-01-15
- 579233 Kurdish +0.59 (+75.21!) - recalib kept Kurdish top, paid off. 172391=Newroz(Kurdish holiday), 406433=Man City, 599463=Tim Walz(Minnesota again), 972999=Czech Republic. Cum TW -567.30.
- PATTERNS: Kurdish theme (Syria lang+holiday+PKK). Minnesota recurring (ICE+Walz). Less-obvious picks (Czech for planes).
- AFCON: Morocco bt Nigeria on pens (4-2) -> FINAL: Morocco v Senegal (Jan 18).
- Updated 573851: Senegal 0.4 (likely runner-up/loser appealing). 799398 (Hakimi) confirmed valid (Morocco in final).
- 4 resolve Jan 16: 672298(abstain),841822,942671,974205.
- AFCON final Jan 18 -> 799398, 573851 resolve. Then track AusOpen deep rounds, T20 WC (Feb).

## Day 25: 2026-01-16
- 672298 UDP NJ=Tom Malinowski(abstained=0, fine). 841822=Indonesia Air Transport, 942671=Gul Plaza, 974205=Raqqa(+0.26 2nd pick!). Cum TW -585.19.
- DETERMINISTIC AO 2026 (from draw/corpus): Alcaraz R2=ADAM WALTON (updated 2176=0.72). Sinner R1=Gaston, R3(pot)=Fonseca. Real Madrid sacked Alonso->Arbeloa (Copa exit to Albacete).
- 7 resolve Jan 17: 2176(done Walton),223607,486189,505500,744407,77915,799398(Hakimi, final Jan 18).
- NEXT: AO R3/R4 results as they come (789844 Alcaraz R4, 922844/464874/679570 women R3). AFCON final Jan 18 (799398/573851).

## Day 26: 2026-01-17
- 2176 Alcaraz R2=HANFMANN not Walton! My 0.72 overconfidence -> -0.52 (article said Walton but timeline diverged). LESSON: NEVER >0.5 even on "confirmed" news.
- 223607=National Citizen Party(BD), 486189=Bangladesh(had 3rd), 505500=Seguro, 744407=Adamuz, 77915=Huelva, 799398=Brahim Diaz(had 4th 0.08). Cum TW -663.59.
- 3 resolve Jan 18: 37248(Bulgaria-low conf),551676(SDF),904367(NE Syria city).
- GOING FORWARD: cap ALL tops at 0.5 max, even deterministic-looking. Keep 3-4 alternatives.

## Day 27: 2026-01-18
- 37248 Bulgaria=Iliana Iotova(-0.04 good spread). 551676 al-Shaddadi base=SYRIAN ARMY(+0.28, 2nd pick). 904367=al-Shaddadi(city). Cum TW -656.03.
- NE Syria theme = SYRIAN ARMY asserting control (not SDF).
- AFCON final today (Morocco v Senegal) -> 799398/573851 will finalize.
- 2 resolve Jan 19: 377358(Iran WC), 980781(Sinner R2 - kept spread, couldn't confirm).

## Day 28: 2026-01-19
- 377358 football assoc=KNVB(Netherlands). 980781 Sinner R2=James Duckworth (low spread -> only -3.99, no-overconfidence works). Cum TW -667.62.
- 5 resolve Jan 20: 207522,464874,621718,924864,922844 (modest spreads, no churn).
- Trajectory ~-9/Q. Keep modest spreads, capture deterministic sports results when cleanly verifiable.

## Day 29: 2026-01-20
- 924864 Board of Peace=Pakistan(+0.31, top). 207522=Muna island(near Sulawesi), 621718 Greenland deal=Mark Rutte(NATO!), tennis R3s missed but low-spread (-0.04). Cum TW -687.97.
- 98th Oscar noms NOT in corpus (only historical). 876347/886103 kept as PTA guess.
- 10 resolve Jan 21: 110472,273948,348570,400561,876347,48762,886103,655453,944348,679570 (modest).
- Trajectory stable ~-9/Q. Modest spreads limiting damage.

## Day 30: 2026-01-21
- 348570 Deloitte=Liverpool(+0.11 3rd pick). 48762 3-way talks=Abu Dhabi, 655453 mediate=UAE(had 0.06-too low!). 876347 Oscar=Sinners(had 0.06 4th), 886103=Ryan Coogler. Cum TW -792.12.
- UAE PATTERN STRONG: mediation(Abu Dhabi talks), Somalia disputes. Elevate UAE in diplomatic Qs.
- AO LESSON: "beat X to reach R3" => X was R2 opp. Read round carefully. Confirmed Alcaraz R2=Hanfmann.
- 2 resolve Jan 22: 663866, 789844(Alcaraz R4-not found, kept spread).

## Day 31: 2026-01-22
- 663866 Crans-Montana=Italy(+0.23 2nd). 789844 Alcaraz R4=Tommy Paul(-0.05 low spread). Cum TW -774.37.
- Updated 575662 (peace talks): added Abu Dhabi 0.26 (UAE mediation pattern).
- 4 resolve Jan 23: 24182,243746(FEMA),789042(ICE),575662(done).

## Day 32: 2026-01-23 — BIG POSITIVES
- 243746=FEMA(+0.60), 789042=ICE(+0.71), 575662=Abu Dhabi(+0.34 Brier, -21 TW due to late add). 24182=Dominick Cruz. Cum TW JUMPED to -670.81 (from -774)!
- LESSON CONFIRMED: "obvious" picks at ~0.4 give big positives when right (FEMA, ICE). UAE/Abu Dhabi pattern pays.
- 3 resolve Jan 24: 286957(Keys),287417(Sabalenka QF),694686(NFC QB). Results not in corpus yet (matches in progress). Kept spreads.
- Trajectory improving. Keep ~0.4 caps + patterns.

## Day 33: 2026-01-24
- 286957=Pegula, 287417=Iva Jovic, 694686=Sam Darnold (all missed, low-spread kept small). Cum TW -702.01.
- 5 resolve Jan 25: 110125,238071(N.Darfur 0.45),267761,320820,9493 (modest).
- Continuing efficient advance. ~231 Qs left, trajectory ~-7/Q.

## Day 34: 2026-01-25
- 5 missed: 110125=Perth(Australia!),238071=South Kordofan,267761=South Korea,320820=Jordan,9493=Trikala. Cum TW -781.65.
- All "less-obvious plausible." No exploitable meta-pattern. Modest spreads limiting damage (~-7.5/Q).
- 1 resolve Jan 26: 976773 (UN nuclear meeting, modest spread).
- Continuing efficient advance through remaining ~226 Qs.

## Day 35: 2026-01-26
- 976773=Netherlands. Cum TW -798.69. 105 resolved, 225 active.
- 3 resolve Jan 27: 465445(Fury opp),910937,988168 (modest).

## Day 36: 2026-01-27
- 988168 Owda platform=TikTok(+0.28 2nd). 465445=Makhmudov,910937=Isaac Herzog. Cum TW -790.50. 108 resolved.
- 3 resolve Jan 28: 430936,789988,956334 (modest).

## Day 37: 2026-01-28 — UCL REFINEMENT
- 430936=Jonglei(+0.16 3rd), 956334=Burkina Faso(+0.51!), 789988=Modi. Cum TW -736.38.
- UCL league phase final standings known (Jan 28). Playoff pairings FIXED by rank:
  9/10(Real/Inter) v 23/24(Bodo-Glimt/Benfica); 11/12(PSG/Newcastle) v 21/22(Monaco/Qarabag);
  13/14(Juve/Atletico) v 19/20(Club Brugge/Galatasaray); 15/16(Atalanta/Leverkusen) v 17/18(Dortmund/Olympiacos).
- NARROWED 4 Qs to 2 candidates each (~0.5/0.45): 85609(Benfica/Bodo-Glimt), 55999(Real/Inter), 35131(Club Brugge/Galatasaray), 261538(Monaco/Baku).
- Draw Jan 30 -> these resolve with one of my 2 candidates. Potential +2.0 Brier.
- 6 resolve Jan 29: above 4 + 176447(Lutnick),1877(skier).

## Day 38: 2026-01-29 — ALL 4 UCL HITS!
- 176447=Lutnick(+0.65). 261538=Baku(+0.45), 35131=Galatasaray(+0.44), 55999=Real Madrid(+0.55), 85609=Benfica(+0.55). 1877=Lindsey Vonn(-0.05). Cum TW -684.98 (big jump from -736). Accuracy 3.6%, Brier -0.007.
- BRACKET-NARROWING STRATEGY VALIDATED: standings/draw constraints -> narrow to 2 candidates -> ~+0.5 Brier each. HIGHEST-VALUE technique.
- 1 resolve Jan 30: 316535(Cummins replacement, moderate).
- APPLY to remaining tournament Qs (T20 WC groups Feb, Europa/Conference leagues, AFC) where bracket known.

## Day 39: 2026-01-30
- 316535 Cummins replacement=Ben Dwarshuis(-0.26, too concentrated on Ellis). Cum TW -710.98.
- AO men's final: Alcaraz(beat Zverev 5h27m SF) v (Sinner/Djokovic). Narrowed 951896: Alcaraz 0.44, Sinner 0.4, Djokovic 0.08.
- 4 resolve Jan 31: 391811,562701,946810(Grammy Lamar),951896(done).
- AO women's final Jan 31; men's final Feb 1.

## Day 40: 2026-01-31
- 951896 AO men's=ALCARAZ(+0.52, finalist-narrowing worked!). 946810 Grammy=Bad Bunny(surprise). 391811=Ternivka,562701=Nushki. Cum TW -727.85. 122 resolved.
- 2 resolve Feb 1: 102687(Norwegian PM),449104(minerals stockpile) - modest.
- T20 World Cup starts ~mid Feb (India/Sri Lanka). Watch for group draw to narrow cricket Qs.

## Day 41: 2026-02-01
- 102687=Thorbjorn Jagland, 449104=Project Vault(fictional). Cum TW -761.37. 124 resolved, 206 active.
- 7 resolve Feb 2: 220862(League Cup opp-not confirmed),492629,243685,955662,453736,976004,995305 (mostly modest).

## Day 42: 2026-02-02
- 220862 League Cup=Arsenal(+0.47, +46 TW). Others missed (Union Consultative Council, Saif al-Islam Gaddafi-killed, Darius Garland, Alagoas, Zintan, Tehran market fire). Cum TW -783.27. 131 resolved.
- Libya cluster: Saif al-Islam Gaddafi killed (453736), buried somewhere (426743 resolves Feb 3).
- 4 resolve Feb 3: 336425,426743(Gaddafi burial),57193,579252 (modest).

## Day 43: 2026-02-03
- 426743 Gaddafi burial=Bani Walid(+0.16 3rd). 336425=Druzhkivka,57193=California,579252=Qom. Cum TW -821.47. 135 resolved.
- DETERMINISTIC: Super Bowl LX = Seahawks(Darnold) v Patriots(Maye), Feb 8. Narrowed 180958: Seahawks 0.5, Patriots 0.45.
- Bad Bunny = SB halftime + Grammy AOTY (connection).
- Watch: Winter Olympics Feb 6-22 (downhill 534224), Iran war scenario Feb-Mar, T20 WC groups (narrow cricket).

## Day 44: 2026-02-04
- CONTEXT: June 2025 US-Israel Iran war is REAL (Trump bombed Fordow/Natanz/Esfahan; Op Rising Lion; IRGC chief Hossein Salami killed; Iran struck Tel Aviv/Jerusalem/Haifa). Feb-Mar 2026 Qs = further escalation.
- For "Iran avenging killing" Qs (864964/286): Salami possibly relevant. Keep spreads.
- 1 resolve Feb 5: 883856(Russian general, modest spread).
- Watch Feb-Mar for Iran war scenario events unfolding in corpus.

## Day 45: 2026-02-05
- 883856=Alekseyev(-0.04 low spread). Cum TW -824.99. 136 resolved, 194 active.
- 2 resolve Feb 6: 198725,456284 (modest). Winter Olympics opens Feb 6.

## Day 46: 2026-02-06
- 198725=Khosf, 456284=Jeff D'Onofrio (missed). Cum TW -843.95. 138 resolved.
- 2 resolve Feb 7: 180958(SB Seahawks/Patriots narrowed), 534224(downhill silver).

## Day 47: 2026-02-07
- 180958 SB=Seattle Seahawks(+0.55 Brier, narrowing worked). 534224=Germany. Cum TW -865.25. 140 resolved, 190 active.
- 4 resolve Feb 8: 318661(Colombia ELN),398988,538697,630740 (modest).
- Olympics ongoing; Iran war scenario events should appear late Feb.

## Day 48: 2026-02-08
- 318661 Colombia=Gulf Clan(+0.07 3rd), 630740 Lebanon collapse=Tripoli(+0.48, +48 TW!). 398988=al-Jamaa al-Islamiya, 538697=Indonesia. Cum TW -850.34. 144 resolved.
- 5 resolve Feb 9: 14689(US school shooting-strong prior),312764,487245,527803,745180.

## Day 49: 2026-02-09
- 487245=Iran(+0.44). 14689 school shooting=CANADA(not US!), 745180 cyclone=Geralda. Cum TW -866.31. 149 resolved.
- T20 WC 2026 CONTEXT: Bangladesh EXPELLED (Scotland replaced). Pakistan refuses to play India. Groups: A(Ind,Pak,USA,Neth,Nam) B(Aus,SL,Ire,Zim,Oman) C(Eng,WI,Nep,Ital,Scot) D(NZ,SA,Afg,Can,UAE). Started Feb 7.
- Updated 190197 (Pak beats Namibia/Neth/USA), 454482 (former champ fails: WI/Pakistan-boycott/SL/Eng).
- Watch T20 group results to narrow Super Eight Qs.

## Day 50: 2026-02-10
- T20 WC early: Pakistan bt Netherlands+USA (winning). England struggling (close vs Nepal). WI bt Scotland. Group C tight (Eng/WI/Scot - only 2 advance).
- Updated 190197 (Namibia clincher 0.38), 454482 (WI 0.24/England 0.2 struggling).
- 1 resolve Feb 11: 613203 (AFC ACL playoff).

## Day 51: 2026-02-11
- 613203=Shabab Al-Ahli. Cum TW -872.32. 150 resolved (halfway), 180 active.
- 3 resolve Feb 12: 304287(BNP),739916(Truman),795774 (modest).

## Day 52: 2026-02-12
- 739916 carrier=Gerald R Ford(+0.16 3rd). 304287=Jamaat(had 3rd). 795774=Lyon. Cum TW -863.35. 153 resolved.
- 2 resolve Feb 13: 652747(Novichok 0.55-strong), 901381(Milan-Turin 0.45-strong). Should be positive.

## Day 53: 2026-02-13
- 652747 Navalny=epibatidine(NOT Novichok!), 901381 HSR=Rome-Naples. Both strong-prior MISSES (-39/-25 TW). Cum TW -928.15. 155 resolved.
- BRUTAL: even documented facts diverge. Reduced 605397(Kataib),354370(ATACMS) to 0.38.
- No resolve Feb 14. Watch Iran war cluster (late Feb) + T20 Super Eight.

## Day 54: 2026-02-14
- 3 resolve Feb 15: 190197(Namibia clincher),580089,778783 (modest).

## Day 55: 2026-02-15
- 190197=Namibia(+0.55 Brier, T20 narrowing worked!). 580089=Bannu,778783=Sodari. Cum TW -957.25. 158 resolved.
- T20: Australia LOST to Zimbabwe (former champ struggling!). WI already qualified. England 2nd Group C.
- Updated 454482: Australia 0.36 (failing former champ).
- 7 resolve Feb 16: 207951,22203,454482(done),456938,548734,876124,903473.

## Day 56: 2026-02-16
- 454482=Australia(+0.54! T20 narrowing worked). Others missed, low-spread kept small. Cum TW -982.08. 165 resolved, 165 active (halfway). Accuracy 5.8%.
- 2 resolve Feb 17: 307616,479547 (modest).
- Strategy working: deterministic narrowing (sports) = big positives; modest spreads limit surprise losses.

## Day 57: 2026-02-17
- 307616 NZ(+0.36), 479547 IRIS Dena(+0.23). Cum TW -922.57 (improved). 167 resolved. Accuracy 6.4%.
- 3 resolve Feb 18: 207254,485328,943026 (modest).

## Day 58: 2026-02-18
- 3 missed (Bureau of Counterterrorism, Spanberger, Grok-Dutch court). Cum TW -967.69. 170 resolved.
- Grok recurring (Indonesia ban + Dutch court). 
- 2 resolve Feb 19: 325000(Hezbollah),434350(Markram). T20 Super Eight starts Feb 21.

## Day 59: 2026-02-19
- 325000=Hamas(+0.33 2nd). 434350=Maharaj. Cum TW -952.29. 172 resolved.
- 2 resolve Feb 20: 26859,59953 (modest). T20 Super Eight Feb 21.

## Day 60: 2026-02-20
- 59953=Crete(+0.10 3rd). 26859=Nangarhar+Paktika. Cum TW -959.45. 174 resolved.
- 6 resolve Feb 21: 109135,162065,221278(Canada hockey 0.42),489825,493481,73075.

## Day 61: 2026-02-21
- 221278 hockey=USA(+0.23 2nd). Others: Italy(host 30 medals), India(condemns Pak), Charles Kushner(FR ambassador), Lviv, CPFIK. Cum TW -995.54. 180 resolved.
- 1 resolve Feb 22: 992626 (T20). Super Eight underway.

## Day 62: 2026-02-22
- 992626 Super Eight Grp1 leader=West Indies. Cum TW -1008.26. 181 resolved, 149 active.
- 2 resolve Feb 23: 648994,654360 (modest).

## Day 63: 2026-02-23
- 654360=Minas Gerais(+0.15 3rd). 648994=Border Patrol Police. Cum TW -1000.26. 183 resolved.
- 3 resolve Feb 24: 392014(Goma 0.5),632535,726747.

## Day 64: 2026-02-24
- 726447=Manchester(+0.14 3rd). 392014=Uvira(Goma prior WRONG again). 632535=Peru. Cum TW -1025. 186 resolved.
- 5 resolve Feb 25: 415069(Oman 0.4),422164,812182,489902,811321.

## Day 65: 2026-02-25
- 422164 Columbia(+0.39!), 812182 Frenkie de Jong(+0.15). 415069=Austria(Vienna-US/Iran talks, classic JCPOA venue-missed). 489902=Vienna, 811321=Antalya. Cum TW -1030.74. 191 resolved.
- LESSON: US-Iran talks -> Vienna/Austria (historic JCPOA venue).
- 5 resolve Feb 26: 131819,412823,55315(Labour 0.5),661416,915784.

## Day 66: 2026-02-26
- 55315=Hannah Spencer (I put "Labour" - FORMAT ERROR, "who"=person name not party!). Others: Kabul, Chris Murphy, Zhigulevsk, Barcelona. Cum TW -1082.76. 196 resolved.
- LESSON: "who will be elected/appointed" -> person NAME, not party/org.
- 7 resolve Feb 27: 209948,434027,333107,815035,443306,58660,739634 (Iran-war modest).

## Day 67: 2026-02-27
- 58660 Tehran(+0.54), 739634 Iran(+0.58), 443306 Geneva(+0.12). Misses: Qatari airspace, NZ SF, Qazvin, Minab. Cum TW -1037.36 (improved ~45). 203 resolved. Accuracy 7.3%.
- Iran war scenario peaking (Feb 28 strikes). 11 resolve Feb 28 (modest spreads).

## Day 68: 2026-02-28
- 354370 PrSM(+0.20 recalib), 59501 UAE(+0.22). Misses: Beit Shemesh, Arafi(x2), Gandhi Hosp, Kuwait base, Khamenei-avenged, US-Israel war. Cum TW -1092.67. 214 resolved.
- Iran war: Khamenei killed, US troops Kuwait, PrSM missile, UAE gets most missiles.
- 7 resolve Mar 1: 232393,246419,414228,560525,453556,971319,994042.

## Day 69: 2026-03-01
- 2nd-pick wins: 232393 South Africa(+0.23), 246419 Bahrain(+0.27), 453556 Oman(+0.06). 994042=IRIB(Israel struck IRAN's broadcaster, not AlJazeera). 560525=Kuwait(F15),971319=Ras Laffan(Qatar gas). Cum TW -1104.84. 221 resolved.
- LESSON: Iran war broadcaster = IRIB (Iran state TV), not Al Jazeera.
- 4 resolve Mar 2: 297818,584240,656436,759458 (modest).

## Day 70: 2026-03-02
- 297818 content misalign (Ukraine forecast vs UAE emirate question=Fujairah). 584240=US,656436=Spain,759458=Bushehr. Cum TW -1163.56. 225 resolved.
- 6 resolve Mar 3: 157054,16281(Carrick defeat club),803012(Bondi),68828(Nadella),937255(Hormuz),768526.

## Day 71: 2026-03-03
- 803012 Bondi(+0.61!), 937255 Hormuz(+0.62!). Misses: Jensen Huang(Nvidia/OpenAI), US(Zelenskyy drones), Tim Sheehy, Newcastle. Cum TW -1088.94 (big improvement). 231 resolved. Accuracy 7.9%.
- 8 resolve Mar 4: 281710(Homan),869392,641254,943634,887402(IAF),779990,765155,863162(Saudi).

## Day 72: 2026-03-04
- 765155 Doha(+0.05). 887402=US military (school strike by US not Israel!), others missed (Mullin, Al-Kharj, Bahrain refinery, Klobuchar, Parand). Cum TW -1158.59. 239 resolved.
- 2 resolve Mar 5: 483759,871156 (modest).

## Day 73: 2026-03-05
- 483759 Middle East(+0.30). 871156=Michigan. Cum TW -1139.43. 241 resolved.
- 3 resolve Mar 6: 681301(Nabatieh),758920(Oli),893235(Israel).

## Day 74: 2026-03-06
- 681301 Tyre(+0.27 2nd), 893235 Iran(+0.19 2nd). 758920=Balendra Shah(Nepal rapper-mayor). Cum TW -1110.55. 244 resolved.
- 4 resolve Mar 7: 276362,338215,830793,578870 (modest).

## Day 75: 2026-03-07
- 276362 Raouche(+0.23 2nd), 338215 US embassy(+0.26 2nd). 830793 content misalign (Mexico forecast vs Oslo embassy question). Cum TW -1095.15. 248 resolved.
- 4 resolve Mar 8: 179817,304016,271330,309487 (modest).

## Day 76: 2026-03-08
- 4 missed (Gary Kirsten, UAE-missiles, Air NZ, Dnipropetrovsk). Cum TW -1154.51. 252 resolved, 78 active.
- 4 resolve Mar 9: 399040(Qatar),605397(Kataib),932855,935869.

## Day 77: 2026-03-09
- 4 missed (Mexico WC move, Kataib Imam Ali, Taiwan, Lemina). Cum TW -1221.35. 256 resolved, 74 active.
- 5 resolve Mar 10: 211346(KKR),425983,559340,807049(Mbappe),828811.

## Day 78: 2026-03-10
- 5 missed (Sunrisers, Kvaratskhelia, Handala, Valverde, Jama'a Islamiye). Cum TW -1294.16. 261 resolved, 69 active.
- 4 resolve Mar 11: 350082(abstain),48811,742975(MQ-9),922567.

## Day 79: 2026-03-11
- 48811 Temple Israel(+0.13 3rd). 350082 abstain=correct. 742975=KC-135(NOT MQ-9!), 922567=Old Dominion. Cum TW -1325.42. 265 resolved.
- 5 resolve Mar 12: 169286(Qatar KC135 base),214539,857856,679215,764041.

## Day 80: 2026-03-12
- 5 missed (Saudi base, Kharg island, USS Tripoli, Burj Qalaouiyah, North Korea). Cum TW -1396.31. 270 resolved, 60 active.
- 2 resolve Mar 13: 503104,657160 (modest).

## Day 81: 2026-03-13
- 657160 UAE(+0.05 3rd). 503104=Serbia. Cum TW -1398.80. 272 resolved, 58 active.
- 4 resolve Mar 14: 196640,369030,581686,833672 (modest).

## Day 82: 2026-03-14
- 4 missed (AlJazeera network, McLaren, Emergency NGO, Germany-Hormuz). Cum TW -1445.37. 276 resolved, 54 active.
- 2 resolve Mar 15: 506444(Japan),529060(Kinzhal).

## Day 83: 2026-03-15
- 506444 Japan(+0.45!), 529060 Zircon(+0.29 2nd). Cum TW -1371.77 (improved ~74). 278 resolved. Accuracy 8.5%.
- 7 resolve Mar 16: 167989,219636,274734,669234,573851(Senegal CAS),293527,58520.

## Day 84: 2026-03-16
- 573851 Senegal CAS(+0.63!! AFCON-final tracking paid off huge), 58520 Katz(+0.32 2nd). Misses: Sporting, Olmeca, BETS OFF, NCTC, Ramat Gan. Cum TW -1339.50 (improved ~85). 285 resolved. Accuracy 8.8%.
- Updated 864964 (Iran avenging -> Khamenei 0.3, since Khamenei killed).
- 3 resolve Mar 17: 405816,676065,864964(done).

## Day 85: 2026-03-17
- 864964=Larijani(Khamenei update missed). 405816=Beit Awwa, 676065=Bernie Sanders. Cum TW -1369.74. 288 resolved, 42 active.
- 6 resolve Mar 18: 388689,398208,666706(Texas),739439,512785(Taiwan),724111.

## Day 86: 2026-03-18
- 388689 Asian Boxing(+0.14 3rd), 512785 UAE arms(+0.07 3rd). Misses: Taiwan, Hawaii(Norris), Tabriz, Torres. Cum TW -1409.42. 294 resolved, 36 active.
- 6 resolve Mar 19: 144493,244043,757234,50504,655411,668257.

## Day 87: 2026-03-19
- 244043 Old City(+0.21 2nd). Misses: Costa Rica, Bank of America, US-SriLanka, Naini, Iranian Red Crescent. Cum TW -1449.30. 300 resolved, 30 active.
- 3 resolve Mar 20: 217580(N.Darfur),427993,974962(Asmara).

## Day 88: 2026-03-20
- 974962=Meknes(Morocco neutral venue, NOT Asmara! -36.62 costly). 217580=East Darfur, 427993=Kenya. Cum TW -1520.68. 303 resolved, 27 active.
- LESSON: "host" in qualifying can = neutral venue (war disruptions). Even definitional assumptions fail.
- 1 resolve Mar 21: 774274 (Kiryat Shmona).

## Day 89: 2026-03-21
- 774274=Misgav Am. Cum TW -1537.08. 304 resolved, 26 active.
- 5 resolve Mar 22: 120805(Oman),581783,554489,718848,740952 (modest).

## Day 90: 2026-03-22
- 5 missed (Pakistan intermediaries, Montreal, AlJazeera, Khiam, Colombian AF). Cum TW -1585.85. 309 resolved, 21 active.
- 5 resolve Mar 23: 262505,698278,494140,757107,912807(Russia).

## Day 91: 2026-03-23
- 494140 Pakistan IQAir(+0.20 3rd). Misses: UAE(Coyle), RCB, Loni, North Korea(Lukashenko). Cum TW -1627.05. 314 resolved, 16 active.
- 2 resolve Mar 24: 200605,240291 (modest).

## Day 92: 2026-03-24
- 200605 Iran(+0.27 2nd). 240291=Ukraine. Cum TW -1622.42. 316 resolved, 14 active.
- 4 resolve Mar 25: 34927,390530,534802,953884 (modest).

## Day 93: 2026-03-25
- 534802 Bosnia(+0.28 2nd). Misses: Turkiye, Iran-govt, Mexico. Cum TW -1621.46. 320 resolved, 10 active.
- 3 resolve Mar 26: 489669,79608,659262 (modest).

## Day 94: 2026-03-26
- 3 missed (Ben White, Zalka, Qom). Cum TW -1642.19. 323 resolved, 7 active.
- 4 resolve Mar 27: 177801,320138(Telegram),795856,560679(ADNOC).

## Day 95: 2026-03-27
- 560679 EGA(+0.07 3rd). Misses: Houthis, Snapchat, Jezzine. Cum TW -1676.31. 327 resolved, 3 active (FINAL 3).
- 3 resolve Mar 28: 144312(Pope Leo),26340(UAE),267975(N.Darfur).
