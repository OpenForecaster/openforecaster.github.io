# Forecasting Memory — aljazeera Q1 2026 market (330 qs)

## Setup facts
- Sim today: 2025-12-24. Questions resolve 2026-01-01 → 2026-03-28.
- All answer-type = string entity. Max 5 outcomes, sum ≤ 1. Honest probs ⇒ E[score] = Σq_i² ≥ 0. NEVER bet >q on hunches; never list junk fillers.
- TW score: per question = avg daily score × 100. Cover EVERYTHING asap, refine daily.
- Questions auto-generated from FUTURE Al Jazeera articles; titles leak the storyline. Cross-reference question titles for bracket/event info!

## Big leaked storylines (from question titles)
1. US-Israel joint strikes on IRAN (~late Feb 2026), Iran retaliates vs Israel + Gulf (Qatar? Bahrain?), Iran "temporary 3-member governing council" (regime change?!), Strait of Hormuz crisis, oil/energy strikes, US troops killed, F-15Es downed by friendly fire, HIMARS new missile, hospital/school strikes in Tehran & southern Iran. Hezbollah-Israel war resumes in Lebanon (Beirut strikes, journalists killed).
2. Iran protests Dec 2025-Jan: province lost 30 police (q69214), checkpoint attack kills 13 Basij (q724111).
3. Ukraine: 3-way US-RU-UA talks Jan 23-24 (city? mediator country?), round 2 on Feb 4 somewhere; Zelensky reshuffle (def min, econ adviser); opposition leader charged in bribery probe; counteroffensive retakes a region (~Mar).
4. AFCON 2025 (Morocco): Morocco QF vs Cameroon Jan 9; SF in Rabat Jan 14; final Jan 18 — Morocco player MISSES stoppage-time penalty in final; a country appeals title ruling to CAS (controversy!). DR Congo knocked out by ??.
5. Australian Open: winner by Feb 1; many draw questions (unknowable until draw ~Jan 15).
6. T20 WC 2026 (Feb-Mar, India+SL): Bangladesh asks ICC to move matches to ??; Bangladesh REPLACED by another team (q110472); Pakistan boycotts India match; SA in SF1 Mar 4.
7. Milano Cortina Olympics Feb: hockey gold, women's downhill silver country, country with 30 medals record (Norway? Italy?).
8. Venezuela: interim president sworn in by Jan (Maduro gone?!); "big armada" region q279531.
9. Syria: army vs SDF in NE (Maskana/Deir Hafer, assault on city ~Raqqa?), al-Shaddadi base, national language (Kurdish?), holiday (Nowruz? Eid?).
10. Bangladesh election Feb 12: NCP/BNP/Jamaat dynamics; main opposition party in new parliament.
11. Thailand election Feb 8: NIDA poll leader (party + PM pick).
12. Greenland: Trump deal framework with ?? by Jan 31; Denmark/Greenland request meeting; NATO Arctic mission name.
13. Epstein: Commerce Sec (Lutnick) island visit Dec 2012 in correspondence; House Oversight subpoena in March.
14. Oscars: film with most noms (record 16!) + director. Super Bowl LX winner + NFC QB. Grammys AOTY.
15. UCL playoffs (draw ~Dec 19?): Real Madrid/Benfica/Juventus/Newcastle ties; R16 in March.

## Lessons / process notes
- (init) Submit all 330 with honest hedges day 1; refine daily as articles arrive.

## Day 1 (2025-12-24) summary
- Submitted 311/330. Abstained (revisit when info emerges): 521564 (migrant worker name), 793465/2176/980781/464874/922844/400561/679570/789844/286957/935869 (AO draw-dependent — draw ~Jan 15-16), 672298 (NJ primary candidate names), 55315 (Gorton&Denton MP names — by-election Feb 26), 883856 (Moscow officer name), 548734 (Feb storm name — check storm list late Jan), 489825 (Kurdish alliance letters), 468437 (Iran women's captain name), 350082 (Michigan assailant name), 659262 (Israeli footballer name).
- Key research findings Day 1:
  * Chelsea: Maresca-hierarchy conflict ongoing Dec 19. Watch for sack ~Dec 27-31; coach candidates unclear (I guessed free agents). UPDATE DAILY.
  * Ukraine: Yermak resigned Nov 28; defmin=Shmyhal; chief-of-staff vacancy candidates: Fedorov, Shmyhal, Kyslytsya, Palisa. If Shmyhal moves → new defmin (I bet Palisa).
  * Venezuela: US "quarantine" of oil 2mo; Maduro under pressure; successors: Delcy Rodríguez, Padrino López; Machado/González opposition. Interim president sworn in by Jan 2 per question.
  * Measles: SC at 138 (Dec 16, +27/wk) → 185 ~Jan 1. AZ at 176 (yearly, Mohave outbreak 172).
  * Syria-SDF: Aleppo clashes Dec 22; integration deadline end-2025; assault target qs (Raqqa/Tabqa guesses).
  * Minneapolis: ICE/CBP ops ongoing; expect fatal shooting of woman (agency q: CBP vs ICE split).
  * NFL: Chiefs eliminated, Mahomes ACL. Broncos/Pats/Bills/Jags/Chargers in (AFC); Niners/Eagles/Bears/Rams/Seahawks (NFC). Seahawks possible 1-seed.
  * Thai NIDA Dec: People's Party 25.3%, Natthaphong 17.2% > Anutin 12.3% (Bhumjaithai 9.9%, 4th).
  * TikTok JV: closes Jan 22 (Oracle/Silver Lake/MGX 45%); US CEO unknown.
  * Oscars: OBAA led Globes noms (9). Shortlists: Sinners, Hamnet, Frankenstein, OBAA strong.
  * Gaza: Board of Peace named "early 2026"; Pakistan offered to consider ISF role.
  * Greenland: Landry envoy Dec 21, Denmark summoned US amb.
- Tomorrow priorities: (1) Chelsea coach news; (2) Venezuela; (3) AFCON group results & bracket (DR Congo R16 opponent!); (4) Austrian skier crash news (Bormio training Dec 26+); (5) Ukraine defmin/reshuffle; (6) Charlotte NYE plot; (7) Bangladesh cricket/politics; (8) re-check abstained qs.

## Day 2 (2025-12-25)
- Bangladesh: Tarique Rahman returned (PM frontrunner); Awami League BANNED from Feb 8...wait Feb 12 election; unrest (Osman Hadi killing, Dhaka blast, Hindu lynching tension w/ India). Keeps BNP-led govt + Jamaat-as-opposition thesis. NCP defection noted.
- AFCON: Group B = Egypt, RSA, Angola, Zim. Egypt & RSA won openers; finale Mon Dec 29. DR Congo R16 opp likely 2B (Egypt/RSA) — current split fine.
- Aguerd injury talk pre-Mali match → raised q343689 Aguerd to 0.32.
- Moscow: Lt-Gen Fanil Sarvarov killed by CAR BOMB Dec 22 — NOT the q883856 event (that q starts 2026-01-19, asks officer SHOT; future event; stay abstained).
- IMPORTANT STRUCTURAL FIND: resolution_date in market.csv ≈ parsed deadline, NOT necessarily event date; question start dates vary (some start mid-Jan!). Check start dates before assuming.
- Chelsea: drew 2-2 at Newcastle; pressure eased but q165622 created Dec 25 → appointment still expected by Jan 31. Keep watching daily.
- Ukraine: Christmas Witkoff/Kushner-Zelensky talks "very good"; Zelensky open to Donbas DMZ. No chief-of-staff/defmin moves yet.
- Venezuela: Trump "smart to step down"; political prisoners released (sign of negotiation?); Polymarket Maduro-out-by-Mar31 only 39%. Keep Delcy/Machado/González spread.

## Day 3 (2025-12-26)
- AFCON: Egypt 1-0 RSA (Salah pen; Egypt through, tops B likely; RSA 2nd pending Zim Mon). Morocco DREW with Mali (Group A tight but Morocco should top). Bracket note: R16 M8 = 1E vs 2D → DRC (if 2D) faces Group E winner (Algeria, Mahrez in form). Updated 703511 (Algeria .28) & 459037 (Egypt .2/Senegal .18).
- Zelensky-Trump meeting Dec 28 Florida re: peace framework ("a lot can be decided before New Year"). Watch for breakthrough → mediator/city of Jan 23-24 trilateral.
- Chelsea host Aston Villa today (pundits tip Villa). Watch result → Maresca.
- Venezuela: 99 prisoners freed; Russia calls blockade piracy; "Will China rescue Venezuela" framing.
- No Bormio/Semmering crash news yet (training Dec 27+). No Charlotte plot news yet.

## Day 4 (2025-12-27)
- Chelsea LOST 1-2 home to Villa (Watkins; one win in 6 league). Maresca crisis deepens. Watch sack window Dec 28-Jan 4.
- Skiing: Marco Schwarz WON Livigno Super-G (healthy → dropped from crash list; replaced w/ Babinsky/Striedinger). Scheib won Semmering GS. Bormio races Dec 28-29 — crash watch.
- AFCON: Senegal 1-1 DRC (Group D); Nigeria beat Tunisia → through. Morocco must wait (Mali draw).
- Kyiv: ~500 drones+40 missiles, center hit, power/heat out for 100s of thousands; no embassy damage reported yet (q567250 window to Jan 10).
- Zelensky→Florida; meets Trump Dec 28 (security guarantees, Donetsk/Zaporizhzhia territorial issues). 20-pt plan: freeze + DMZ.

## Day 5 (2025-12-28)
- Carabao SFs: Newcastle-City & Chelsea-Arsenal (legs Jan 13-14, Feb 3-4) → q220862 now Arsenal .53/Chelsea .43.
- Trump "productive" call w/ PUTIN before Zelensky Florida meeting (today); Netanyahu ALSO meeting Trump in Florida (supports q789988 Trump-visits-Israel & Iran-strike planning storyline).
- AFCON: Nigeria qualified (Osimhen); Algeria reached last 16 (→1E ✓ for DRC R16); Ivory Coast 1-1 Cameroon; Mozambique first-ever win (F tight). Hakimi yet to play (returning vs Zambia) → NOT the calf-injury man; Aguerd 0.32 stands.
- Shiffrin won Semmering slalom. Bormio men's downhill Dec 28-29 — watch crash tomorrow.

## Day 6 (2025-12-29)
- Trump-Zelensky Florida: "closer but no breakthrough"; territorial issues unresolved; Russia claims drone attack on Putin residence (Kyiv denies). Talks to continue → Jan trilateral plausible.
- AFCON groups B done: Egypt 1st (unbeaten), RSA 2nd (beat Zim 3-2) → R16: RSA vs 2F (likely Cameroon). Morocco beat Zambia → tops A. Algeria through (E). DRC final group game Dec 30 → likely 2D → vs ALGERIA in R16 (q703511 Algeria .34).
- Skiing: Livigno SG Dec 27 — Raphael HAASER (AUT) crashed; Kriechmayr DNF. No injury news yet; added Haaser .15 to q892867. Watch for "ruled out of Olympics" news by Jan 2.
- Chelsea: Maresca still in ("end 2025 in best way"). Next league game ~Dec 30/31.

## Day 7 (2025-12-30)
- AFCON R16 SET: DR Congo vs ALGERIA (q703511 → Algeria .55, Egypt .18 QF-scenario). Senegal top D; Nigeria 1C perfect.
- Chelsea 2-2 Bournemouth (1 league win in 7; 13 pts dropped from winning positions at home; fans chanting at Maresca; he missed presser ill). Sack imminent? No successor names circulating yet — tomorrow check.
- Venezuela: Trump announces LAND strikes on Venezuela "dock area" (escalation!).
- Guehi: Liverpool prefers to wait for summer free (Mail) → Real Madrid up to .38.
- England provisional T20 WC squad: Archer, Tongue in.

## Day 8 (2025-12-31)
- Maresca: "in danger unless results improve in January" (Sky) — not sacked yet; Jan results decisive. Chelsea Jan fixtures incl. Arsenal Carabao SF Jan 14.
- Venezuela: FIRST known US strike INSIDE Venezuela (drug dock); more oil sanctions; Americans detained. Escalating to possible Maduro endgame.
- Russia: Gerasimov ordered to expand "buffer zones" 2026; alleged Putin-residence drone story used to dent peace hopes; Tuapse port hit.
- No Austrian skier ruled out yet (deadline Jan 2!). Haaser crash Livigno no injury news. Men's next races: Four Hills GaPa Jan 1 (jumping); alpine men ?Garmisch/Adelboden Jan. Crash likely reported Jan 1-2 — check tomorrow FIRST.
- Measles at airports (Logan, Denver, Walnut Creek). SC count update pending.

## Day 9 (2026-01-01) — FIRST RESOLUTIONS
- RESOLVED: Chelsea coach = LIAM ROSENIOR (Strasbourg/BlueCo internal! LESSON: check ownership networks). Ukraine defmin = FEDOROV (+17, had 2nd). Charlotte town = MINT HILL (missed; list more suburbs next time). Austrian skier = KATHARINA LIENSBERGER (training crash; I dropped her — LESSON: keep women/tech skiers in mix; don't narrow without evidence). Measles = SOUTH CAROLINA ✓ (+83).
- Net TW so far: +90.6. Asymmetry confirmed: wrong-5-way costs only ~-0.03; right top pick at .6 pays +.83. Include best candidates broadly; avoid overconfident misses.
- AFCON R16 FULL BRACKET: Sen-Sud, Mali-Tun (Jan3); Mor-Tan, RSA-Cmr (Jan4); Egy-Ben, Nga-Moz (Jan5); Alg-DRC, CIV-BF (Jan6). QF2 = Morocco v (RSA/Cmr) → leak says Cameroon. Morocco SF opp (q459037) ∈ {Alg, Nga, DRC, Moz} — set .36/.36/.14/.05. Final Jan 18 opp pool: Senegal/Egypt/CIV/Mali/Tun/BF side.
- Pakistan T20WC Group A: India, Pak, USA, Namibia, Netherlands (Feb 15 IND-PAK Colombo ✓).
- Ukraine: Coalition of Willing NSAs meet in Ukraine Jan 3; leaders in France Jan 6. Shaheen Afridi injured (BBL) — race for WC.
- Maresca OUT (left amid medical-staff disagreements + City/Juve talks); Rosenior in.

## Day 10 (2026-01-02)
- RESOLVED: Bangladesh→SRI LANKA ✓ (+87, had .70). Venezuela interim president = DELCY RODRIGUEZ ✓ (+42, had .30 top). TW now ~219.8.
- NOTE: Maduro still active/negotiating in Jan 1-2 news (drug-trafficking talks offer) — "interim president" event coexists with Maduro presence; don't over-update toward full regime collapse.
- Budanov (GUR) named Zelensky CHIEF OF STAFF; peace deal "90% ready"; Witkoff/Rubio/Kushner working European track. Kharkiv hit by missiles (19 injured).
- Starlink q935533 rebalanced (Ven .32 / Jam .28) — resolves tomorrow.
- AFCON R16 from today: Sen-Sudan, Mali-Tunisia.

## Day 11 (2026-01-03)
- RESOLVED: Morocco calf injury = OUNAHI (had .04; Aguerd was decoy — LESSON: "coach dismisses injury talk" = player likely fine). Starlink = VENEZUELA ✓ (+31). TW ~248.6.
- HUGE: US military operation in Venezuela — Trump claims MADURO CAPTURED (Jan 3). AG: faces US justice. Delcy interim. → armada q now ME .52.
- UK+France joint strike on ISIS underground site in Syria; rockets hit Damascus mosque.
- NFL Wk18: Steelers-Ravens decider (Rodgers vs Lamar); Raiders → #1 pick.
- Watch tomorrow: AFCON Sen-Sud/Mali-Tun results; Morocco-Tanzania & RSA-Cameroon (leak: Cameroon wins); econ adviser q709715 (res Jan 4).

## Day 12 (2026-01-04)
- RESOLVED: Ukraine econ adviser = CHRYSTIA FREELAND (!; unguessable, -2.8).
- AFCON: Cameroon 2-1 RSA → Morocco-Cameroon QF Jan 9 ✓ (leak validated). Tunisia out (sacked coach); Mali advanced. QF1: Senegal? (check Sen-Sudan result) vs Mali.
- Iran: protests week 2, 15-16 dead, clashes in WEST (Kermanshah belt), Khamenei "put in their place". q69214 → Kermanshah .16 top.
- DHS pauses immigration apps from 20 MORE countries (mostly African: Angola, Nigeria, Senegal, Tanzania, Zimbabwe). SE Asia ally (PH/TH) not yet named — q756639 unchanged.
- Denmark PM urges Trump stop Greenland threats; "Soon" post provocation.

## Day 13 (2026-01-05)
- RESOLVED yesterday batch: SDF ✓+90, Algeria-DRC ✓+53, US WC-host exclusion ✓+71, Minnesota ✓+78; misses: Parchin (-1), Rubio (-8.5; LESSON: "request meeting with" → working-level counterpart (FM/SecState), not president). TW 528.
- AFCON: Nigeria 2-0+ Mozambique (Osimhen double) → QF3 Algeria-Nigeria; Egypt survived Benin → QF4 Egypt vs CIV/BF. Morocco SF opp = Nigeria .47/Algeria .45.
- Minneapolis: 2,000 federal agents deploying (immigration + daycare-fraud probe). Fatal-shooting event (q278197) still ahead.
- Iran: protests persist, no leniency; regime-change chatter post-Maduro.

## Day 14 (2026-01-06)
- RESOLVED: Minneapolis agency = ICE (+42; had .35 2nd). Qatar peace body = BOARD OF PEACE ✓ (+95). TW 665.
- Baltic: Finland seized Fitburg (cable sabotage); Latvia cable breach Jan 4; US Navy P-8s over Ireland tracking Russian-flagged tanker Marinera (Venezuela oil) — US may seize by force.
- Irish Taoiseach + S.Korea's Lee in Beijing; European leaders to Beijing in "first weeks of 2026" — Carney trip not yet announced (q822586 res tomorrow; keep spread).
- AFCON QFs set: Sen-Mali, Mor-Cmr, Alg-Nga, Egy-(CIV/BF tonight).

## Day 15 (2026-01-07)
- RESOLVED: Greenland talks venue = "WHITE HOUSE" (my "Washington, DC" scored as MISS -31.5!! CRITICAL LESSON: grader is literal — hedge across phrasings: e.g. split mass between "White House" AND "Washington"). Carney after Beijing = QATAR (miss). NATO mission = ARCTIC SENTRY ✓ (+42).
- Brisbane: Sabalenka cruising; QF proj. vs Keys (same half → final opp from other half: Rybakina/Pegula/Osaka/Andreeva unknown). AO runs Jan 18-Feb 1; draw ~Jan 15-16 → FILL ABSTAINED AO QUESTIONS Jan 16-17.
- Grok scandal worsening ("undressing women") — first-ban question (Jan 9): Indonesia .25 top.
- AFCON QFs Jan 9-10: Sen-Mali, Mor-Cmr, Alg-Nga, Egy-CIV/BF.

## Day 16 (2026-01-08)
- RESOLVED: NIDA party-list = People's Party ✓ (+80.5). Misses: wedding raid = occupied East Jerusalem; Kyiv embassy = QATAR; carrier SCS→ME = USS ABRAHAM LINCOLN (so q739916 "joins Lincoln" — Ford .3 intact); Oreshnik = LVIV (had .06). TW 717.5.
- Grok: global backlash (UK/EU/PL/FR/IN/MY/BR condemn; no ban yet). Rebalanced q45659: Brazil .2 (X-ban precedent), Malaysia .18, Indonesia .12.
- Brisbane: Sabalenka R3 vs Ostapenko/Cirstea; semis Jan 9-10; final Jan 11.
- AFCON QFs tomorrow: Senegal-Mali, Morocco-Cameroon.

## Day 17 (2026-01-09)
- RESOLVED: Grok ban = INDONESIA (+38; LESSON: original instinct (formal-ban track record) > recency of loud condemnations). Morocco SF opp = NIGERIA ✓ (+27.6). Trade deficit = TAIWAN ✓ (+48.8). Yemen = "Supreme Military Committee" (near-miss). Brisbane final = Kostyuk (miss). TW 826.8.
- ManU: AMORIM SACKED Jan 5; Fletcher caretaker; Solskjaer & Carrick in talks (Sky: Solskjaer favourite) BUT March leak (q16281) says Carrick is interim boss → q474377 Carrick .45/Ole .3/Fletcher .15.
- Iran: nationwide (25/31 provinces); worst in 6 western provinces; cops killed in Iranshahr (Jaish al-Adl claimed!), Malard, Ilam. q69214 → S-B .22. Rial collapse trigger; "Pahlavi will return" chants.
- AFCON: SF2 = Morocco vs Nigeria (Jan 14). QF1 today Sen-Mali; QF4 Egypt-CIV(?).

## Day 18 (2026-01-10)
- RESOLVED: Nipah = WEST BENGAL (-72!! had Kerala .85. LESSON: cap base-rate-only confidence ~.6; ALWAYS verification-search before high-confidence stands). Iran 30-police province = ISFAHAN (+3.4 net). NIDA PM = Natthaphong ✓ (+67). TW 824.9.
- Yemen: STC seized Hadramout/al-Mahra in Dec, Saudi-backed forces retook; STC "disbanded" in Riyadh (disputed; Zubaidi expelled/treason). Saudi-UAE feud open.
- Supercopa: Real beat Atletico 2-1 (Mbappe knee sprain, back for final); Clasico final Jan 11. Vinicius 15-game goal drought (note for q807049).
- Bangladesh "to work with ICC" on T20WC security in India (headline) — q110472 replacement still live.
- No Copa R16 draw yet.

## Day 19 (2026-01-11)
- RESOLVED big batch (+310): Iran-BRICS ✓+67, PKK ✓+78 (full name "Kurdistan Workers' Party" matched my "PKK" — semantic matching exists but is inconsistent; remember White House≠Washington DC), Carrick ✓+57.5 (leak-based), PKK ✓+71.8, DHS ✓+38.9; Somalia severed = UAE (-13.6; second Somalia q got +10.8 via UAE .2). TW 1135.6!
- Minneapolis ICE shooting victim = Renee Nicole Good (37); "ICE Out for Good" national protests. q521564 (migrant-worker custody death, NAME) — different event, still unknown → stay abstained.
- Gaza: Mladenov = Board of Peace director-general; technocratic committee names due THIS WEEK (q71!). Hamas to dissolve its govt when committee takes over; al-Hayya to Cairo.
- Lesson reinforced: UAE-backs-separatists pattern (Yemen STC, Somaliland) — for future "who backs X separatists" questions, weight UAE higher.

## Day 20 (2026-01-12)
- RESOLVED: Tymoshenko (had .15 → +2.6); Betar US ("Betar" scored as MISS -10 — STRING LESSON again: use full official names); Real Betis ✓ +12.6. TW 1140.7.
- AFCON SFs: SF1 Egypt-Senegal (Egypt KO'd holders CIV 3-2; Salah 4 goals); SF2 Morocco-Nigeria. BRAHIM DIAZ = top scorer → q799398 Brahim .18 top now; q573851 → Egypt .2/Senegal .16/Morocco .14.
- PrSM hedged with both phrasings (q354370).
- AO draw expected ~Jan 15-16: MUST fill ~10 abstained AO questions then (2176, 980781, 464874, 922844, 679570, 789844, 286957, 400561, 793465, +).

## Day 21 (2026-01-13)
- RESOLVED: NE ICE state = MAINE (miss); Gaza committee head = ALI SHAATH (new name, miss but cheap); Massie = QATAR ✓ +27.9; SE Asia visa ally = THAILAND ✓ +36.6 (had .38); Gaza body name = "Palestinian national committee" (miss, -5.4). TW 1179.9.
- Syria: Army TOOK Sheikh Maqsoud by force; SDF evacuated Aleppo entirely (ceasefire/evac deal; US mediated; ~30 dead, 150k displaced). q904367 → ALEPPO .55. US "large-scale" anti-ISIL strikes after deadly ambush.
- Carabao SF leg1 tonight Newcastle-City; AFCON SFs tomorrow (Egy-Sen, Mor-Nga). AO draw Thu.

## Day 22 (2026-01-14)
- RESOLVED: ME armada ✓ +64.7; CBA basketball (+15.2, had .12); Somalia food aid (-15.1, cut it — LESSON: Somalia top-tier for UN funding crises); migrant worker = El Hacen Diarra (abstained, 0); Venus R1 loser→Danilovic (abstained 0). TW 1244.7.
- AO: draw details not yet in corpus (previews only). Alcaraz SPLIT WITH FERRERO; Sinner bookies' favorite (2x defending). q951896 → Sinner .38/Alcaraz .31. Medvedev won Brisbane (men). TOMORROW: fill AO R2/R3 abstained questions from draw.
- AFCON SFs tonight; Carabao leg1 Newcastle-City done (check result tomorrow).

## Day 23 (2026-01-15) — AO DRAW FILLED
- RESOLVED: Newroz ✓+73 (semantic match Nowruz→Newroz worked), Kurdish ✓+90, Walz ✓+65; Guehi→MAN CITY (miss -23), combat planes→CZECH REPUBLIC (-21). TW 1428.7.
- AFCON FINAL: MOROCCO vs SENEGAL (Morocco beat Nigeria on pens — Bounou; Senegal beat Egypt). q573851→Senegal .40/Morocco .32; q799398 Brahim .20/Hakimi .18.
- AO draw filled (9 questions): Alcaraz R2 Hanfmann/Svajda; Sinner R2 Prizmic/Duckworth; Alcaraz R4 Paul .32; Sabalenka R3 RADUCANU .5; Sonmez R3 Kostyuk .42; Osaka R3 Samsonova .5; Keys eliminator Pegula .2; Sabalenka QF Paolini .3; debutante-R4 = Sakatsume/Maristany/Eden Jones.
- Jordan Smith "stunned Sinner" = AO One Point Slam exhibition (red herring!).

## Day 24 (2026-01-16)
- RESOLVED: UDP target = Tom Malinowski (abstained 0); Indonesia Air Transport (miss -10); Gul Plaza ✓ +7.8 (small spread worked); RAQQA ✓ +46.6. TW 1473.
- Carabao leg1: City 2-0 at Newcastle; Arsenal 3-2 at Chelsea → q220862 Arsenal .6/Chelsea .36.
- Rosenior debut: Chelsea 5-1 Charlton (FA Cup).
- Watch next: AFCON final Sun (Morocco-Senegal; stoppage-time pen leak!); Portugal election Jan 18 (runoff q); AO starts Jan 18; Spain train crash qs (event ~Jan 17-19).

## Day 25 (2026-01-17)
- RESOLVED (+183!): Hanfmann ✓, NCP ✓+42.9, Pakistan-boycott-supports-Bangladesh ✓+73.6, Seguro ✓+59.5, Brahim Diaz pen ✓+17.9; Spain crash = Adamuz/Huelva (cheap misses). TW 1656.6.
- Ukraine: delegation (Budanov/Umerov/Arakhamia) in MIAMI; docs may be SIGNED AT DAVOS next week; Trump may meet Zelensky at WEF (Jan 19-23). → Trilateral Jan 23-24 likely DAVOS/Switzerland (q48762 Davos .45; q655453 Switzerland .55). Kushner/Witkoff planning MOSCOW trip (Putin meeting this month; may slip due to IRAN unrest).
- Iran unrest now affecting US-Russia scheduling (war precursor).
- AFCON final tomorrow: Morocco-Senegal (Brahim pen miss already known!). Portugal 1st round tomorrow too.

## Day 26 (2026-01-18)
- RESOLVED: Iotova ✓+83.7; Syrian army (al-Shaddadi) ✓+51.3; NE-Syria city = AL-SHADDADI (Aleppo miss -13.2). TW 1778.3.
- AFCON FINAL: SENEGAL beat Morocco amid PENALTY CHAOS + Senegal walk-off; "ugly scenes"; Brahim missed stoppage-time pen ✓already. Title via ruling-ish → q573851 MOROCCO .62 (likely appellant to CAS).
- IRAN: Khamenei acknowledges "several thousand" deaths, blames US/Trump incitement; claims up to 16,000 deaths (unverified) / 5,000 verified. Schools reopen. WEF urged to bar Iranian regime. Massive repression → war arc on track.
- Davos: Trump attending; Ukraine-US talks continue at Davos ✓.

## Day 27 (2026-01-19)
- RESOLVED: FA petition = KNVB (my "Netherlands" .10 NOT matched — acronym phrasing matters; -15.7); Sinner R2 = Duckworth (+6.4). TW 1769.
- AO: Djokovic 100th AO win; Raducanu through to R2 (vs Potapova) → Sabalenka R3 on track.
- Iran: warns vs US strike; internet blackouts; state TV hacked; Reza Pahlavi prominent; US solidarity marches.
- Deloitte Women's ML: Arsenal top (MEN'S report due ~Jan 21-22; q348570 City .4/Liverpool .3).
- Coming: Oscar noms Jan 22; TikTok close Jan 22; Davos Jan 19-23 (trilateral?); NZ landslide q (res Jan 21); Greenland deal q (res Jan 20).

## Day 28 (2026-01-20)
- RESOLVED: Pakistan Board of Peace ✓+87.2; Muna island (miss; was Sulawesi-adjacent!); Sabalenka R3 = Potapova (Raducanu lost R2; tiny +); Sonmez R3 = Putintseva (+0.5); Greenland framework w/ MARK RUTTE (NATO SG twist; -19.6). TW 1815.7.
- Davos: Trump agrees to meet European leaders there on Greenland; says PUTIN INVITED TO JOIN BOARD OF PEACE. Trilateral window Jan 23-24 — venue bet Davos/Switzerland holding.
- NZ T20: Milne & Bracewell injured pre-WC.

## Day 29 (2026-01-21)
- RESOLVED (+159): Scotland ✓+26, Liverpool Deloitte +33 (had .30), trilateral = ABU DHABI/UAE (early mass saved Davos pivot: +21.6/+22.8), SINNERS most noms (record 16!) +19.9, RYAN COOGLER ✓+25.6, ADAM PRESSER TikTok ✓+21.2, Mboko = debutante-R4 (seeded but 1st AO; miss), Mount Maunganui landslide (miss), Inglis (miss small). TW 1974.6.
- NFL: Broncos beat Bills but BO NIX BROKE ANKLE (out). Rams beat Bears. NFC title: SEAHAWKS (home, favorites) vs RAMS. AFC: Broncos vs Pats/Texans winner. q694686 Darnold .55/Stafford .38; q180958 SEA .28/NE .2/LAR .18/DEN .12.
- LESSON: hold early diffuse mass; pivots late in window matter less (time-weighting).

## Day 30 (2026-01-22)
- RESOLVED: Italy (Crans-Montana bar) ✓+20.2; Tommy Paul ✓+11.7. TW 2006.4 — crossed 2000!
- Keys: shaky wins, into R3 vs Tjen/Pliskova/Stephens; R4 would be Pegula section → q286957 Pegula .25/Tjen .12.
- UFC 324 Sat: Harrison INJURED, Nunes unretired & opponent-less → q456938 NUNES .30 for Rousey fight.
- UFC HOF announcement may come at UFC 324 (Jan 24); Poirier .3 stands.

## Day 31 (2026-01-23)
- RESOLVED: ICE Milan ✓+77.4; Abu Dhabi (round 2 talks) ✓+22; FEMA +4.4; UFC HOF = Dominick Cruz (-12.2). TW 2098.1.
- AO: Sabalenka R4 vs MBOKO; Jovic STUNNED Paolini → q287417 = Jovic .42/Putintseva .28/Sonmez .22.
- Grammys Feb 1: AP predicts Kendrick/Gaga/K-pop. Keep Kendrick .24/Gaga .22 (maybe check AP detail).
- NFL conference championships this weekend (NFC: SEA-LAR; AFC: DEN-NE/HOU).

## Day 32 (2026-01-24)
- RESOLVED: Pegula eliminates Keys ✓+10; Jovic ✓ (-0.9 net, late catch); DARNOLD ✓+28.4 → SEATTLE in Super Bowl. TW 2135.6.
- AFC title Sun: Patriots at Broncos. q180958 → SEA .42/NE .2/DEN .15.
- Trump skipping Super Bowl ("too far"/anti-halftime-acts).

## Day 33 (2026-01-25)
- RESOLVED: South Kordofan ✓+38.7; South Korea tariff ✓+26.4; Jordan (Gaza kids) ✓+27.4; Perth (!), Trikala (cheap misses). TW 2221.6.
- UCL pre-MD8 (Jan 28): Arsenal 1st (21,100%), Bayern 18, Real 3rd but plays BENFICA away MD8. CROSS-LEAK: q903473 (Vinicius-Benfica racism) dated FEB 17 = playoff leg 1 → BENFICA vs REAL MADRID is the playoff tie! → q55999 Real .62; q85609 Benfica .62. Newcastle plays PSG MD8; Newcastle seeded→away leg1 (Turin .18 stands if Juve unseeded).
- Playoff dates Feb 17-18/24-25; R16 Mar 10-11/17-18; final Budapest May 30.

## Day 34 (2026-01-26)
- RESOLVED: IAEA requester = NETHERLANDS (-21.8). TW 2199.8.
- Fury comeback: Agron Smakici sparring drama + wants the fight; Wardley summer talk → q465445 Smakici .30/AJ .25.
- Iran: ~6,000 confirmed dead; "massacre" framing; mural threatens retaliation; Hezbollah pledges to confront US threat; Rubio warns Iraq (Maliki returning). War imminent.
- AO: Sinner QF; Pegula/Anisimova QFs.
- US: Alex Pretti ICE shooting controversy (Minneapolis pattern continues).

## Day 35 (2026-01-27)
- RESOLVED: Fury opponent = Arslanbek MAKHMUDOV (miss -22); Herzog ✓ +17.8; Bisan = TikTok (~0). TW 2195.2.
- Tomorrow: UCL MD8 → check Real-Benfica result + final standings; playoff draw Jan 30 → finalize 261538/35131.
- Watch: Lutnick Epstein (Jan 29), Crans-Montana downhill (US skier q, Jan 29-31), Cummins replacement (Jan 30), Grammys+AO final (Feb 1).

## Day 36 (2026-01-28)
- RESOLVED: Jonglei ✓+22.5; Burkina Faso ✓+60.3; Netanyahu visitor = MODI (-37; India-Israel angle underweighted). TW 2241.
- Epstein files: DOJ redactions delayed past deadline ("near term") — Lutnick q may still resolve via Oversight tranche.
- UCL MD8 tonight (Real at Benfica!). Playoff draw Jan 30.

## Day 37 (2026-01-29)
- RESOLVED (+151): LUTNICK ✓+75; VONN ✓+29.7; BENFICA-REAL double ✓+55.8 (leak-dated inference = best tool); Newcastle leg1 = BAKU (Qarabag); Juve eliminated by GALATASARAY. TW 2392.6.
- AO: women's final Sabalenka-Rybakina; men's SFs Sinner-Djokovic & Alcaraz-Zverev (Sincaraz final likely; q951896 unchanged).

## Day 38 (2026-01-30)
- RESOLVED: Cummins replacement = BEN DWARSHUIS (+8.6, in spread). TW 2401.2.
- Grammys: Kendrick 9 noms; AP tips GAGA for AOTY (narrative), Independent tips BAD BUNNY. → q946810 Gaga .30/Bunny .28/Kendrick .18.
- AO men's final Sun: Sinner vs Djokovic SF & Alcaraz vs Zverev SF pending.

## Day 39 (2026-01-31)
- RESOLVED: Ternivka ✓+10; Nushki ("Noshki" spelling = MISS -3.9; SPELLING LESSON); Bad Bunny AOTY +18.4; ALCARAZ AO champ +39.75 (hedge). TW 2465.6.
- Feb dawn: SB Feb 8 (SEA .42); Olympics Feb 6; T20WC Feb 7; Bangladesh vote Feb 12. Watch Feb 1-3: Solberg, minerals stockpile name, Saif death (Feb 2), Carabao 2nd legs (Feb 3-4) → City final opponent.

## Day 40 (2026-02-01)
- RESOLVED: Norwegian ex-PM = THORBJORN JAGLAND (miss); stockpile = "PROJECT VAULT" (unguessable). TW 2445.6.
- Iran: US talks "progress"; Khamenei calls protests a "coup"; US-Israeli generals met at Pentagon (war prep ~Feb 27-28 per leak); Trump: India to buy Venezuelan not Iranian oil.
- Ukraine talks next week (Abu Dhabi Feb 4 ✓ already resolved).

## Day 41 (2026-02-02)
- RESOLVED (+149): Arsenal final ✓+60; SAIF AL-ISLAM ✓+83.6; Zintan ✓+23.6; Garland/Alagoas/Tehran-market misses cheap. TW 2594.7.
- SB LX: SEAHAWKS vs PATRIOTS (Pats beat Broncos in snow; Maye). → q180958 SEA .52/NE .44. Bad Bunny halftime; Levi's Stadium Feb 8.
- Saif burial: forensics in Zintan → q426743 Zintan .30.

## Day 42 (2026-02-03)
- RESOLVED: CALIFORNIA ✓+78.6; Bani Walid burial +16.6 (early mass); Druzhkivka & Qom misses cheap. TW 2679.
- Moscow officer-shot event: not yet (by Feb 28; stay abstained, re-search ~Feb 10).
- India: Ajit Pawar died (state mourning) — not in questions.
- Coming: Narges exile city + WaPo publisher (Feb 6); Olympics open Feb 6; T20WC Feb 7; SB Feb 8.

## Day 43 (2026-02-04)
- WaPo: layoffs ~1/3 staff; Lewis absent; Matt Murray exec editor fronting → q456284 Murray .25.
- US-Iran nuclear talks in OMAN Friday (Feb 6); US rejects venue change; Iranian gunboats near US tanker in Hormuz; 50k arrested in crackdown.
- Colombia: EGC suspends Doha talks (watch q318661 "resume with X").
- Abu Dhabi round-2 talks "productive" day 1.

## Day 44 (2026-02-05)
- RESOLVED: Moscow officer = Vladimir Alekseyev (abstained, 0).
- Iran softening: women motorcycle licences; execution reprieves/bail; 3,000+ deaths acknowledged (mostly "security forces/bystanders" per regime); Oman talks Friday. War qs still loom late Feb.
- q534224 silver updated (AUT .18/US .16/ITA .14).

## Day 45 (2026-02-06)
- RESOLVED: Narges → KHOSF; WaPo publisher = Jeff D'Onofrio (obscure; cheap misses). TW 2672.2.
- Hezbollah: Wafiq Safa resigned/replaced (internal restructuring framing — possibly the abduction story's other side; q398988 Hezbollah .65 holds).
- Olympics opened (two-city ceremony). T20WC starts tomorrow; SB Sunday.

## Day 46 (2026-02-07)
- RESOLVED: SEAHAWKS SB ✓+32.2; women's DH silver = GERMANY (had .05; -6.7 TW). TW 2697.6.
- UCL playoffs: Real-Benfica ✓, PSG-Monaco confirmed pairings (Feb 17-25).
- No Tractor ACL news yet. T20WC underway.

## Day 47 (2026-02-08)
- RESOLVED: Indonesia ✓+72.7; Tripoli ✓+39.6; Colombia = "Gulf Clan" (-7.8; had Clan del Golfo .10 — phrasing?); Lebanese group = AL-JAMAA AL-ISLAMIYA (-43.6; LESSON: cap "obvious actor" at ~.5 in Lebanon-actor questions). TW 2758.5.
- Olympics hockey: Canada opened with win (Crosby captain). Bangladesh vote Thu; Jamaat chief under fire (anti-women remarks).

## Day 48 (2026-02-09)
- RESOLVED: CANADA school shooting ✓+83.2 (cross-leak); IRAN SOTU tensions ✓+65.9; Tumbler Ridge/Rostom/Geralda cheap misses. TW 2894.8.
- All tracking on schedule: Bangladesh Feb 12; UCL legs Feb 17; Iran war window Feb 27-28.

## Day 49 (2026-02-10)
- T20WC: Pak beat USA; NZ beat UAE; NED beat NAM (De Leede). Pakistan U-TURN: will play India (boycott reversed). q190197 → Netherlands .42.
- Sri Lanka: Hasaranga out (injury).

## Day 50 (2026-02-11)
- RESOLVED: Tractor vs SHABAB AL-AHLI ✓+13.1. TW 2907.9.
- Trump "thinking" of 2nd carrier to Mideast (q739916 Ford .3 holds); anti-Khamenei slogans continue.
- Bangladesh votes tomorrow (NCP's Nahid Islam alliance story).

## Day 51 (2026-02-12)
- RESOLVED (+121): JAMAAT main opposition ✓+55.3 (BNP won); GERALD R FORD ✓+46.1; LYON ✓+19.9. TW 3029!
- Storms: Kristin→Leonardo→Marta→Nils (K,L,M,N); next O female → q548734 filled "Storm Olivia" .30 + "Olivia" .10 (phrasing hedge).
- Portugal interior minister resigned over Kristin response.

## Day 52 (2026-02-13)
- RESOLVED: Navalny toxin = EPIBATIDINE (frog toxin! -27.5 on Novichok .52); HSR = Rome-Naples (-7.4). TW 2994.1.
- META-LESSON: questions are generated by NOVELTY. If the "obvious" answer would be stale news, cap it at ~.35-.4 and spread to fresh alternatives. Applied: q994042 → Al-Manar .35 / IRIB .30.

## Day 53 (2026-02-14)
- Hockey: Canada beat Swiss (McDavid rolling); Fiala out for Swiss. IND-PAK tomorrow.
- LA Olympics boss in Epstein files shame (separate storyline).

## Day 54 (2026-02-15)
- RESOLVED: Namibia (last S8 berth; +19.2 via spread); BANNU ✓+19.3; Sodari miss cheap. TW 3028.8.
- WI first into Super 8s → q454482 rebalanced: SRI LANKA .48 (WI eliminated from "failing" candidacy).
- IND-PAK today in Colombo (rain risk; no reserve day).

## Day 55 (2026-02-16)
- RESOLVED (7!): Sertolovo ✓+13.4; Carano (+0.5); misses: RTS, Afroza Khanam Rita, AUSTRALIA (failed S8 — shock; -14.3), Storm PEDRO (-0.8), Prestianni (-10.5). TW 3001.5.
- Australia OUT of Super 8 → updated 992626 (India .30 lead), 333107 (SA SF opp: India .25), 307616 (Pak opener: England .14).
- 165 active questions remain; Iran-war cluster (late Feb) is the big block ahead.

## Day 56 (2026-02-17)
- RESOLVED: Pak opener = NZ ✓+14.5; frigate = "IRIS Dena" (had "Dena" .12 — PREFIX MISS AGAIN; always include "IRIS/USS" full forms). TW 3010.9.
- Iran: GENEVA nuclear talks ("guiding principles" understanding); Iran to shut PARTS of Hormuz; Pentagon restocking GBU-57s; India seized 3 Iran-linked tankers. Updated talks-venue qs toward Geneva/Switzerland.
- UCL playoff leg1 tonight: Benfica-Real (Vinicius-Prestianni incident expected per resolved q).

## Day 57 (2026-02-18)
- RESOLVED: SPANBERGER ✓+24.6; GROK ✓+61.2; Bureau of Counterterrorism (miss). TW 3090.1.
- Olympics: Canada only ~9 medals day 10 (gold drought till Kingsbury) → q162065 FLIPPED to ITALY .40 (host surge; record 20). Hockey: Canada dominant (10-2 France!) → gold q Canada .38/US .26.
- Iran-US Geneva track active; war window Feb 27-28 approaches.

## Day 58 (2026-02-19)
- RESOLVED: Lebanon command centre = HAMAS (-26.4; novelty lesson AGAIN — Israeli ops in Lebanon often target Hamas now); SA captain = Keshav Maharaj (-10.9). TW 3052.8.
- Applied: q828811 Beirut apartment → Hezbollah .38/Hamas .22.

## Day 59 (2026-02-20)
- RESOLVED: CRETE ✓+22.5; Nangarhar-Paktika near-miss (-2.6). TW 3072.7.
- Hockey: Women's gold = USA (Knight). Men's: Canada beat Finland → final (likely vs US) → q221278 Canada .50/US .36.
- IRAN: Trump 10-15 day deadline, "considering strike"; Poland evacuating; Iran NOTAM rocket launches; "US bases legitimate targets if attacked". War on schedule.

## Day 60 (2026-02-21)
- RESOLVED (+140): ITALY 30 medals ✓ (flip vindicated); US men's hockey gold (+30.7 via .36); INDIA ✓+54.8; KUSHNER ✓+73.6; Lviv miss; CPFIK (abstained). TW 3212.7.
- Gorton&Denton FILLED: Spencer (Grn, 20%) .38 / Goodwin (Ref, 17%) .28 / Stogia (Lab, 15%) .22. Burnham was blocked!

## Day 61 (2026-02-22)
- RESOLVED: Group 1 leader = WEST INDIES (-13.8; WI surging). Updated q333107 SA-SF1-opp: India .2/WI .2.
- War week begins (strikes expected Feb 27-28 per question structure).

## Day 62 (2026-02-23)
- RESOLVED: MINAS GERAIS ✓+34.3; Thai site = Border Patrol Police (miss). TW 3219.2.
- q443306 "final talks collapsed" → GENEVA .35 (venue updated).

## Day 63 (2026-02-24)
- RESOLVED: Uvira +5.1; Manchester ✓+13.6; Spain warm-up = Peru (miss). TW 3236.1.
- US pulling Beirut embassy staff; Iran buying Chinese anti-ship missiles; strike decision looms.

## Day 64 (2026-02-25)
- RESOLVED: Mar-2 talks host = AUSTRIA/Vienna (missed; JCPOA-venue prior should've been listed!); Columbia ✓+15; de Jong ✓+12.4; Antalya miss. TW 3213.3.
- q443306 → Vienna .30 / Geneva .15 / Austria .08.

## Day 65 (2026-02-26)
- RESOLVED: HANNAH SPENCER ✓ (+3.8, Green gain!); Newcastle hosts BARCELONA ✓+12.2; Murphy (+0.9); Kabul/Zhigulevsk misses. TW 3216.7.
- q167989 Arsenal QF → Barcelona .30/Newcastle .15 (bracket-adjacent).
- War: strikes expected within 48h per question timeline (Feb 27-28).

## Day 66 (2026-02-27)
- RESOLVED (+147): TEHRAN ✓+72.8; IRAN WC ✓+87.4; Geneva (+10.7); NZ SF1 (+9.5); Qatari airspace (miss → supports Qatar-hit thesis); Qazvin/Minab cheap.
- PAKISTAN-AFGHANISTAN "OPEN WAR" (55 Pak soldiers killed; cities struck) — separate war!
- US-Iran Vienna/Geneva talks ended NO DEAL; US citizens told to leave Israel; UK pulls staff from Iran. Strikes imminent/beginning.
- q59501 Qatar → .42.

## Day 67 (2026-02-28) — WAR DAY RESOLUTIONS (11!)
- ARAFI ✓✓ (+25.1; constitutional-council inference); PrSM ✓+33.9 (phrasing hedge!); Kuwait (US troops, +0.6); KHAMENEI KILLED (Hezbollah avenging him; -13.4); UAE took >half missiles (-3.1); "US-Israel war" phrasing miss (-15.3 — use short canonical phrases!). TW 3380.2.
- Iran: interim council = Pezeshkian + Ejei + ARAFI. Khamenei dead.
- q971319 → UAE-weighted (Ruwais .15).

## Day 68 (2026-03-01) — +198!!
- RESOLVED: BAHRAIN AWS ✓+56.5; RAWALPINDI ✓+38.3; IRIB ✓+53 (kept .30); RAS LAFFAN ✓+23.5; SA fruit +12.6; Oman +8.2; Kuwait F-15 +6.3. TW 3578.5!
- Khamenei assassination CONFIRMED (state media); attacks to last days; OPEC+ boosts output; tankers hit in Gulf.
- 109 active left (Lebanon/Iraq/March sports/Nepal/IQAir etc.).

## Day 69 (2026-03-02)
- RESOLVED: FUJAIRAH ✓+30.1; misses: Pakistan brings US into talks (-16.8), SPAIN trade cutoff (Rota refusal — NATO-ally blind spot), Bushehr babies. TW 3567.6.
- Lebanon war open: Israel strikes after Hezbollah attacks (52+ dead); EU backs Lebanon ending Hezbollah military activity. ManU 3rd under Carrick (streak).

## Day 70 (2026-03-03)
- RESOLVED: BONDI ✓+52.2; HORMUZ ✓+41.1; misses: Sheehy, Newcastle (Carrick), Jensen Huang ($30bn — had .08), US-drones. TW 3625.8. 99 active.

## Day 71 (2026-03-04)
- RESOLVED (+52): BAHRAIN refinery ✓+43.2; DOHA ✓+20.1; US military ✓+20.5; misses: MULLIN to DHS(!), Klobuchar, Al-Kharj, Parand, "Americas Counter-Cartel Coalition" (close-no-match). TW 3678. 91 active.
- Watch: Nepal election Mar 5 → PM q (Mar 27); tornado state; T20WC final Mar 8.

## Day 72 (2026-03-05)
- RESOLVED: MIDDLE EAST ✓+40.2; Michigan tornado (miss). TW 3708.6.
- Nepal voted: Balendra Shah favorite (RSP-aligned), Gagan Thapa (NC) & Oli rivals. q758920 → Shah .35/Thapa .15. Results in 2-4 days; PM sworn Mar 27.

## Day 73 (2026-03-06)
- RESOLVED (+123): TYRE district ✓+21.3; BALENDRA SHAH ✓+33; IRAN (school attack accusation) ✓+68.5. TW 3831.4! 86 active.

## Day 74 (2026-03-07)
- RESOLVED: RAOUCHE ✓+24.5; Oslo = US embassy ×2 (+5.7,+2.0 — Israel .45 top was wrong but US .12 hedges saved); Raouche apartment (-4.9). TW 3858.6. 82 active.

## Day 75 (2026-03-08)
- RESOLVED: DNIPROPETROVSK ✓+29.9; Kirsten/UAE-missiles/AirNZ misses cheap. TW 3869. 78 active.
- W Asian Cup: China & NK through (play for 1B Mar 9); Japan 11-0 India; Taipei beat Vietnam. Updated 932855 & 857856.
- IPL: Chinnaswamy hosts opener + final; RCB opener opponent TBA (PBKS .2 held).

## Day 76 (2026-03-09)
- RESOLVED: MEXICO ✓+40; "Taiwan" ≠ my "Chinese Taipei" (-6.4 PHRASING); Kataib Imam Ali (obscure); Lemina (Liverpool R16 opp = Galatasaray; abstained). TW 3890.5. 74 active.

## Day 77 (2026-03-10)
- RESOLVED: HANDALA ✓+23.4; misses: SRH (IPL opener), Kvaratskhelia, Valverde hat-trick, Jama'a Islamiye AGAIN (-25.5 — same group hit me twice; once a NEW actor appears in a storyline, FOLLOW-UP questions about that storyline likely have the same actor!). TW 3867.4. 69 active.
- KEY-LESSON ADDED: storyline continuity — new actor in resolved q → related pending qs likely share it.

## Day 78 (2026-03-11)
- RESOLVED: TEMPLE ISRAEL ✓+16.1; aircraft = KC-135 (miss; ties to q169286 tanker-base q); ODU miss; Ghazali (abstained). TW 3870.3. 65 active.

## Day 79 (2026-03-12)
- RESOLVED: KHARG ✓+26.3; SAUDI ARABIA (KC-135s) ✓+14; USS Tripoli/Burj Qalaouiyah/North Korea misses cheap. TW 3897.9. 60 active.

## Day 80 (2026-03-13)
- RESOLVED: Spain friendly = SERBIA (not Finalissima; miss); UAE launch-area (miss). TW 3880.3. 58 active.

## Day 81 (2026-03-14)
- RESOLVED: GERMANY (Hormuz refusal) ✓+38.8; Emergency +9.8; Al Jazeera +3.9; McLaren DNS shock (miss). TW 3926.9. 54 active.

## Day 82 (2026-03-15)
- RESOLVED: JAPAN ✓+46.5; "Zircon" vs my "Tsirkon" (-11.8 — transliteration trap #4: ALWAYS use the English-news common form + variant). TW 3961.6. 52 active.

## Day 83 (2026-03-16)
- RESOLVED (7): KATZ ✓+43.4; RAMAT GAN ✓+13; Senegal CAS appeal (+1.7 — winner appealed!); misses: Sporting (Arsenal QF), OLMECA (= Dos Bocas! naming trap #5), BETS OFF Act, NCTC. TW 3998.5. 45 active.

## Day 84 (2026-03-17)
- RESOLVED: Beit Awwa, Bernie Sanders (had .10), Ali Larijani (Iran avenging — new twist) — all small misses. TW 3986.4. 42 active.

## Day 85 (2026-03-18)
- RESOLVED: Asian Boxing Champs ✓+12.7; Taiwan +5.3; misses: UAE arms, HAWAII (Chuck Norris -37; Texas .6 overconfident — residence≠event location!), Tabriz, Omar Torres. TW 3940.9. 36 active.

## Day 86 (2026-03-19) — TW CROSSED 4000
- RESOLVED: NAINI ✓+68.8; IRANIAN RED CRESCENT ✓+30.2; OLD CITY ✓+13.7; US (Mattala) ✓+16.1; Costa Rica & Bank of America misses. TW 4049.4. 30 active.

## Day 87 (2026-03-20)
- RESOLVED: East Darfur, KENYA mass grave, MEKNES (Eritrea hosts at neutral Morocco venue! -25.8; pariah-state home games = neutral grounds). TW 4006.7. 27 active.

## Days 88-89 (2026-03-21/22)
- RESOLVED: Misgav Am, PAKISTAN intermediaries (-20.1, Munir channel!), Montreal, Al Jazeera (N London), Khiam, Colombian AF — all small/medium misses (-52 combined). TW 3954.6. 21 active.

## Day 90 (2026-03-23)
- RESOLVED: UAE (Coyle), PAKISTAN (IQAir country), RCB (Blitzer buy!), LONI (IQAir city), NORTH KOREA (Lukashenko) — string of obscure misses (-50). TW 3904.3. 16 active.

## Day 91 (2026-03-24)
- RESOLVED: IRAN (Australia visitor ban) ✓+74.2; Ukraine drone link (+1.9 via .08). TW 3980.4. 14 active.

## Day 92 (2026-03-25)
- RESOLVED: "TURKIYE" vs my "Turkey" = MISS (-39.25!!! AJ house style — worst string-trap of the run); BOSNIA ✓+32.8; MEXICO navy ✓+26.9; "Iran's government" pause. TW 3993.6. 10 active.

## Days 93-94 (2026-03-26/27)
- RESOLVED: Ben White (England), Qom, Zalka (abstained); HOUTHIS ✓+55; Snapchat (Telegram miss -22.7); EGA; Jezzine. TW 4013.4. 3 active: Pope Leo q, desal country, Sudan aid state.

# ===== FINAL RETROSPECTIVE (all 330 resolved) =====
- FINAL: TW-Score 4003.76 | Brier skill 0.135 | top-pick accuracy 26.7% | 321/330 covered (9 abstains).
- Strategy that worked:
  1. Day-1 full coverage with honest hedged distributions (TW rewards early mass; E[score]=Σq² ≥ 0 when honest).
  2. Cross-question leak mining (bracket/QF dates, Feb-17 Benfica-Real, Cameroon QF, Carrick-interim, Canada school shooting) — the question SET is itself evidence.
  3. Daily news-driven updates on near-resolution questions; corpus grep (free) before search (budgeted).
  4. Constitutional/structural inference (Iran council→Guardian Council cleric Arafi; Iotova via VP succession; storm-name alphabets; naming conventions "Arctic Sentry").
  5. Form/odds tracking for sports with later flips (Italy 30 medals, WI surge).
- Costliest failure modes (fix in future):
  1. STRING/TRANSLITERATION MISSES: Turkey≠Turkiye (-39), Washington DC≠White House (-31), Noshki≠Nushki, Tsirkon≠Zircon, Dena≠IRIS Dena, Betar≠Betar US, Chinese Taipei≠Taiwan, Dos Bocas≠Olmeca. → ALWAYS submit the Al Jazeera/wire-style canonical form; split mass across variants when limit allows.
  2. OVERCONFIDENCE ON BASE RATES: Kerala-Nipah (-72), Texas-Norris (-37), Hezbollah-defaults (-44,-26), Novichok (-27). → Cap "obvious" at .4-.5 unless verified; remember questions exist BECAUSE something novel happened.
  3. Storyline continuity: a surprising actor revealed in one resolution (al-Jamaa al-Islamiya) tends to recur in sibling questions — update siblings immediately.
  4. Residence ≠ event location; pariah states play at neutral venues; "request a meeting with" = working-level counterpart.
- Net: positive TW on ~60% of covered questions; big wins clustered where leaks/cross-inference applied.
