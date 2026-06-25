# MEMORY / LESSONS

## Day 1 (2025-12-24) done: all 330 questions have first-pass predictions.

## CRITICAL LESSON
- VERIFY qid ↔ question title before submitting. I transposed 117844 (Ukraine opposition leader) vs 118127 (Ramaphosa BRICS drills) — caught & fixed. Use memory/q_detail.txt (qid headers from market.csv) as source of truth; submit qid straight from that file.

## Scoring model (derived)
- Expected BSS per Q = 2·Σ(π_k·p_k) − Σ(p_i²); maximized when p_k = true prob. List top ≤5 likely answers, leave residual = P(other/none). Don't overconcentrate on guesses; calibrate.
- No prediction = 0 that day. A confidently-wrong pred can go negative. For unknowable name Qs keep total prob low (~0.05–0.15) to bound downside.

## Revisit priorities (update as info arrives — earlier resubmissions accrue more weight)
- AFCON 2025 (Morocco): group results land Dec 24-31; R16 Jan3-6; QF Jan9-10; SF Jan14; final Jan18. Qs: 703511(DRC out), 459037(Morocco SF opp), 343689/799398(Morocco players), 573851(AFCON appeal). Update as bracket forms.
- Australian Open 2026: draw ~Jan 8-9; many opponent Qs (2176,980781,464874,922844,679570,789844,287417,286957,793465,400561,891998 Brisbane). Update once draw out & per round.
- Champions League: league phase ends ~late Jan, KO playoff draw then; R16 draw later. Qs 85609,55999,35131,261538,915784,167989,425983,807049,935869,16281,474377.
- CL/Grammys/Oscars: Grammy AOTY Feb1 (946810); Oscar noms Jan22 (876347,886103). Refine nominee lists via news.
- Venezuela (651727,487245): monitor Maduro/US escalation daily — fast-moving.
- Iran-war cluster (~70 Qs Feb-Mar): NO new war as of Dec24 (June 2025 war ended; Netanyahu mulling strikes). These are conditional. Monitor whether a new US/Israel-Iran war actually starts; if not, many resolve to no listed answer (kept probs modest). If war starts, refine city/base/casualty guesses.
- Ukraine peace talks venues (48762,655453,575662): talks in Florida; trilateral proposed. Watch for announced host city/country.
- Soonest resolving (Jan 1-8): 165622,227432,628026,892867,93950,468637,651727,343689,935533,709715,369962,433526,630728,703511,814175,915183,278197,857643,269293,822586,85534,423343,567250,787699,812287,836984 — refine these first each day.

## Key world state (see FACTS.md)
- Greenland: Trump named Jeff Landry US envoy (Dec21); Denmark furious. 
- Bangladesh: BNP (Tarique Rahman) frontrunner, election Feb12; Awami League banned.
- Measles: South Carolina ~138 & rising, Arizona 176, Utah 115 (Q93950 wants exactly 185).
- NYE plot was LA (Turtle Island Lib Front), NOT Charlotte NC (Q628026 premise likely off → kept low).
- FBI NYE/ICE: Minneapolis ICE/CBP surge ongoing.

## Workflow for subsequent days
1. Read new articles/ for the new date; search news on revisit-priority clusters.
2. Re-submit improved forecasts (overwrites; accrues weight from that day).
3. Prioritize soonest-resolving + highest-info-gain questions.
4. Keep this file + FACTS.md updated.

## Day 2 (2025-12-25) notes
- Predictions persist across days until overwritten — only resubmit when evidence shifts (saves effort; existing forecast keeps accruing).
- Venezuela: White House ordered 2-month economic "quarantine" of oil, de-emphasizing imminent land strikes/regime change. Lowered 651727 named probs (residual ~0.77 = no swearing-in by Jan31). 487245 (country re US address) Venezuela still strong.
- Ukraine: 20-pt peace plan; "Peace Council chaired by Trump"; Zelensky-Witkoff-Kushner Xmas call; Umerov = NSDC adviser (not new DM). 227432 hold (Shmyhal). Watch trilateral host city (48762/655453/575662).
- AFCON Grp standings forming: Grp D Senegal & DR Congo 3pts; Grp C Tunisia top, Nigeria 3pts; Grp B Egypt & SA 3pts. No bracket yet — hold AFCON Qs.
- T20 WC 2026 confirmed Feb7-Mar8 India+SL. NZ group: SA, Afghanistan, Canada, UAE. No Bangladesh venue-move news yet (468637 hold Sri Lanka).
- No measles count update past SC138/AZ176 — hold 93950.

## Day 3 (2025-12-26) notes
- Syria/Aleppo: active Syrian army vs SDF clashes (SANA names SDF attacking near Sheihan/Lairmoun roundabouts; Turkey wants SDF dismantled; integration deadline end-2025). Raised SDF: 369962→SDF.62, 756891→SDF.50, 138247→"Syrian Democratic Forces".45, 974205 (Manbij/Kobani/Aleppo), 904367→Aleppo.25. Monitor SDF integration / al-Shaddadi (551676).
- AFCON: Egypt won Grp B (beat SA 1-0, Salah pen), tops group. Grp D (Senegal/DRC) plays Dec27. Hold AFCON bracket Qs.
- Chelsea: Maresca still in job (touchline ban), 12/1 next sacked; no appointment. 165622 hold low.
- Greenland: Landry envoy "dialogue not conquest"; no specific meeting counterpart named yet. Hold 630728/269293.
## Day 4 (2025-12-27): AFCON Grp D Senegal 1-1 DRC; both 4pts; DRC plays Botswana(0pts) Dec30 → DRC likely advances. 703511 hold (bracket TBD ~Jan1). Venezuela: prisoner releases, pressure continues, no transition. No updates submitted.

## Day 5 (2025-12-28) — KEY STRATEGIC INSIGHT
- Questions resolve on the resolution_date COLUMN (harness uses it). Many texts say "by Jan 31" but resolution_date is early Jan → they likely resolve as "event not yet occurred / no listed answer". For such premise-unlikely-by-resolution Qs, KEEP TOTAL PROBABILITY LOW (BSS = -Σp² when true answer unlisted; minimize Σp²).
- Trimmed Jan-1-resolving void-likely Qs: 165622 (Chelsea, no appt), 227432 (Ukraine DM, no nomination), 628026 (Charlotte plot — was LA not NC), 892867 (Austrian skier — only Swiss crashed; Schwarz fine, Kriechmayr DNF race not ruled out).
- Going forward: for each soon-resolving Q, ask "will the asked event plausibly have a valid answer BY resolution_date?" If no → minimize Σp². If yes → calibrate normally.
- Ukraine: NABU/SAPO raided Parliament Dec27, MPs in graft probe (energy $100M Mindich scheme; Yermak resigned earlier). 117844 (opposition leader charged) — not clearly Poroshenko yet; hold/monitor.
- Measles: no new exact count; hold 93950 (SC.40/AZ.30 ish).
## Day 6 (2025-12-29): Iran Pezeshkian 'total war' rhetoric (economic siege, NOT new kinetic war). Netanyahu-Trump Mar-a-Lago meeting ~this week re Iran strikes; analysts say Trump unlikely to back new war (prioritizing Venezuela). Iran-war cluster still conditional — hold modest. AFCON Grp B: Egypt 1st, SA 2nd, Angola 3rd(anxious), Zimbabwe out. DRC v Botswana Dec30 (DRC likely advances). Bracket ~Jan1 → then update 703511/459037. No forecast shifts submitted.

## Day 7 (2025-12-30)
- AFCON: Senegal won Grp D; DR Congo 2nd → DRC plays ALGERIA in R16 (~Jan6); winner may face Nigeria QF. Updated 703511→Algeria .52/Nigeria .12. Benin 3rd→faces Egypt R16. Senegal faces Grp E 3rd (BurkinaFaso/Sudan) in Tangier. 459037 (Morocco SF opp) hold pending full bracket Jan1.
- Trump-Netanyahu Mar-a-Lago: Trump conditional threat ("could support another major strike IF Iran rebuilds"); not imminent; Netanyahu "not seeking confrontation". Iran-war cluster still conditional — hold.
- Venezuela: Trump says US struck a "big facility" in Venezuela (Dec29 escalation). Nudged 651727 named probs up slightly (total .26).
- Anthony Joshua injured in deadly car crash in Nigeria → lowered 465445 Joshua .40→.25 (Fury opponent less likely Joshua). Verify severity later.
## Day 8 (2025-12-31): Finalized Jan-1 resolvers. 93950 measles: US total 2065; no state at exactly 185 reported; rebalanced AZ.34/SC.30 (AZ ~176 Dec16 closer to 185). 892867 trimmed (no Austrian alpine ruled out — only Swiss). 227432 trimmed (no DM nomination). 165622/628026 already minimal. Note: Σp²-minimization for void-likely resolvers.

## Day 9 (2026-01-01) — RESULTS & LESSONS
- Jan1 resolved: Chelsea→Liam Rosenior (appointment DID happen; I trimmed→Brier ~0, TW -0.83). Ukraine DM→Mykhailo Fedorov (TW -5.58, accrued over 8 days). Charlotte→Mint Hill. Austrian skier→Katharina Liensberger (a real answer! she WAS ruled out — I had only male speed skiers, missed; but trimmed so small loss). Measles→South Carolina (I had SC .30 → Brier +0.39, TW +56.26 — huge, dominated).
- LESSON: cumulative TW=48.4. Holding a good early pred on an eventually-correct Q = big TW. Bad early pred held long = negative (Ukraine DM). Measles win >> all losses.
- LESSON: appointment/injury Qs DO resolve to real answers even at early res_date. But surprise names (Rosenior/Fedorov/Liensberger) are ~unpredictable; trimming kept losses ~0 — acceptable. Keep a BROADER candidate list (incl. dark horses) at low-moderate prob rather than 2-3 names.
- LESSON: don't over-concentrate on premise-uncertain soon-resolvers (fixed Bangladesh 468637 0.62→0.28; Venezuela 651727 trimmed).
- AFCON R16 bracket (Jan3-6): Senegal-Sudan, Mali-Tunisia, Morocco-Tanzania, SA-Cameroon, Egypt-Benin, Nigeria-Mozambique, Algeria-DRC, IvoryCoast-BurkinaFaso. QF3=(Alg/DRC w)v(Nig/Moz w); SF2=Morocco-half vs QF3 winner. Fixed 459037→Nigeria/Algeria/DRC/Moz (was wrongly Egypt/Senegal). 703511 Algeria .52 stays (Alg=DRC R16 opp Jan6).

## Day 10 (2026-01-02) — RESULTS & BIG LESSON
- Bangladesh venue→Sri Lanka (I had .28 after trimming from .62; Brier +0.47, TW +78.93). Venezuela interim pres→Delcy Rodriguez (I had Delcy .05 earlier for 8 days then DROPPED her in Jan-1 trim! still TW +7.21 from early days). Cumulative TW=134.5.
- BIG LESSON: My aggressive pre-resolution trimming HURT. Both resolved to REAL answers (not void). Bangladesh would've scored more at 0.62; Venezuela I removed the eventual winner. => Trust well-reasoned initial signals; keep BROAD calibrated distributions incl. dark horses; do NOT slash plausible candidates to zero right before resolution unless strong evidence of void. Many "by [later date]" Qs DO resolve to real answers on res_date.
- Revised policy: only minimize Σp² when (a) premise clearly cannot be determined by res_date, AND (b) no base-rate reason it resolves to a listed answer. Otherwise keep calibrated spread (incl. a 4th/5th dark-horse).
- 343689 (Morocco calf injury, res Jan3): QF not even set by Jan3, no injury news → keep minimal (~.15). 935533 (free Starlink, res Jan3): no announcement found → modest trim Venezuela .10.

## Day 11 (2026-01-03)
- Results: 343689 Morocco calf→Azzedine Ounahi (not in my list; small loss -1.24; injury Qs DO resolve to real player → list 5+ incl. midfielders). 935533 Starlink→Venezuela (had .10; +27.27; trim again cost a bit). Cum TW=160.5, rising.
- Ukraine reshuffle confirmed: Shmyhal→energy min/1st dep PM; Fedorov→defence min (227432 already resolved Fedorov); Budanov→chief of staff. No "economic development adviser" named → 709715 (res Jan4) likely void; kept low ~.14 (no candidate signal; not churning).
- Ukraine peace deal "90% ready" (Zelensky Dec31). Watch peace-talks venue Qs 48762/655453/575662.
- POLICY HOLDING: stop over-trimming; keep calibrated broad distributions; trust early signals; only change on real new evidence.

## Day 12 (2026-01-04) — MADURO CAPTURED
- HUGE: US military operation Jan 3 captured Maduro+wife (held NYC, federal charges). Trump says US will "run" Venezuela indefinitely + tap oil. (651727 already resolved Delcy Rodriguez.) Future Venezuela Qs: 487245 raised Venezuela .42. Watch 75613 (Massie oil proceeds), 487245.
- 709715 resolved → Chrystia Freeland (Canada ex-DPM) as Ukraine econ adviser. Surprise int'l figure. Cum TW 159.8.
- Syria: govt-SDF merger talks FAILED (no tangible results), SDF still main unintegrated force; ISIL resurgent (Aleppo suicide bombing, UK/France strike Palmyra, US killed 25 ISIL). 369962→SDF .55/ISIL .18.
- Greenland: escalation (Katie Miller "SOON" post; Denmark PM urges Trump stop threatening). 630728 hold Trump/Rubio/Landry.
- 814175 (UK MPs exclude from WC hosting): only US/Can/Mex host → US dominant; kept .62 (strong thematic, Q created anticipating; don't over-trim per lesson).
- Jan5 resolvers: 369962,915183,433526,630728,703511,814175 — finalized.

## Day 13 (2026-01-05) — BIG RESULTS, cum TW=395.8
- Resolved: 369962 SDF (+79.66), 814175 US (+90.39, GLAD didn't over-trim!), 703511 Algeria (+41.65), 630728 Rubio (+21.51, had .18), 433526 Parchin (+17.26, had .18 2nd), 915183 Minnesota (MISS -14.53; I had LA/IL/CA/NC; Minneapolis surge was the answer — should've connected to 278197 Minneapolis cluster!).
- LESSON CONFIRMED: trust strong thematic signals, keep confident probs, DON'T over-trim. Cross-reference related questions (Minneapolis ICE/CBP surge relevant to 915183 AND 278197).
- 278197 (Minneapolis woman fatal shooting agency, res Jan6): Minneapolis "Metro Surge" led by Border Patrol cmdr Bovino (CBP). Rebalanced → Border Patrol .30/ICE .28/CBP .22.
- 857643 Qatar peace body → "Board of Peace" .68 held (strong, well-reasoned; Qatar central Gaza mediator).

## Day 14 (2026-01-06) cum TW=543.4
- 278197→ICE (had ICE .28 2nd; +58). 857643→Board of Peace (had .68; +89). Strategy working: confident well-reasoned preds held long = big TW.
- Jan7 resolvers: 269293 (Greenland talks venue — Denmark/GL asked to meet Rubio but Rubio hasn't agreed; kept Washington .40/StateDept .18). 822586 (Carney post-Beijing — NO evidence of Carney China trip; trimmed moderate). 85534 (NATO Arctic mission name — no named mission; trimmed hard, unpredictable name).
- Greenland: Trump hinted decision "in ~2 months" (after Venezuela). EU/6-nation solidarity statement. Rubio confirmed as requested counterpart.

## Day 15 (2026-01-07) cum TW=570.1
- 269293→White House (had .12; +15). 822586→Qatar (missed, trim limited loss -9.8). 85534→Arctic Sentry (had top .07 after trim; +21 — trim cost some upside again).
- REFINED POLICY: keep confident on well-reasoned TOP picks (don't trim those); only trim premise-uncertain Qs with NO signal & high Σp².
- Jan8 resolvers: 787699 People's Party .66 HELD (strong Thai poll signal). 423343/567250 held (frequent-event base rates, reasonable spreads). 812287 (carrier SCS→ME) & 836984 (Oreshnik) TRIMMED — no signal, focus is Venezuela not ME, high void risk.
- Context: Maduro captured; US pursuing Russia-flagged tanker Marinera in N Atlantic. Ukraine peace "90%", Paris "coalition of willing" Jan 6. Yemen: Saudi-UAE/STC clashes, Socotra tourists stranded.

## Day 16 (2026-01-08) cum TW=616
- Resolved: 787699 People's Party (+86, strong signal held). 423343→East Jerusalem (miss -8). 567250→Qatar embassy (miss -6). 812287→USS Abraham Lincoln (miss, trim limited -12). 836984→Lviv (miss, trim limited -14). Pattern: specific city/entity = often surprise; broad spread/trim caps loss; big thematic favorites win huge.
- AFCON QF: Jan9 Mali-Senegal, Cameroon-Morocco; Jan10 Algeria-Nigeria, Egypt-IvoryCoast. Morocco SF opp = winner(Algeria v Nigeria). Fixed 459037→Nigeria .34/Algeria .31 only.
- Grok CSAM scandal: India(MeitY)/France/Malaysia pressuring X; no formal ban yet. 45659→India .16 top.
- Yemen: National Shield Forces (Saudi-backed) retook Hadramout/Mahra from STC; PLC expelled STC leader. 797906 added National Shield Forces .14.
- 46876 trimmed (annual trade report not out by Jan9 → void risk).

## Day 17 (2026-01-09) cum TW=665
- 45659→Indonesia (had .05; +5). 459037→Nigeria (had .34 after bracket-fix; +28). 46876→Taiwan (had .10; +24). 797906→"Supreme Military Committee" (had "Supreme Military Council" .06 near-miss; -3). 891998→Marta Kostyuk (miss -4).
- Iran nationwide protests (25+ provinces, ~36+ killed, rial collapse, anti-Khamenei). Hotspots: Ilam(Abdanan/Malekshahi), Sistan-Baluchestan(Jaish al-Adl), Chaharmahal&Bakhtiari(Lordegan), Kermanshah, Khorasan Razavi(Chenaran). 69214 added Ilam .22.
- Thailand: Natthaphong (People's Party) consistently tops polls; Anutin incumbent w/ nationalism. 934187→Natthaphong .45.
- Note Iran protest cluster relevant to many Iran Qs — instability rising (not war, internal unrest).

## Day 18 (2026-01-10) cum TW=655.7 (Nipah cost -51)
- KEY CALIBRATION LESSON: 291796 Nipah→West Bengal (I had Kerala .78 = overconfident on historical prior; held 17 days → -51 TW). CAP single-outcome confidence ~0.60-0.70 for "which X" Qs unless near-locked (confirmed news/scheduled). Strong priors can break; long-held overconfident wrong pred = big neg.
- 934187→Natthaphong (had .45; +58). 69214→Isfahan (surprise, not in list; -16).
- Man Utd: Amorim SACKED Jan5; Darren Fletcher interim (→474377 Fletcher .74 for Jan17 derby).
- Syria: army shelling SDF in Aleppo Sheikh Maqsoud/Ashrafieh, 100k+ fled, curfew, 22+ killed. 138247→"Syrian Democratic Forces" .62; 756891→SDF .65.
- Yemen STC announced dissolution (Riyadh talks) but split/Aden rallies; UAE withdrew forces. al-Zubaidi fled to UAE via Somaliland.

## Day 19 (2026-01-11) cum TW=670.6
- 783773→UAE (had UAE .35 top; +50.9 big win). 118127→Iran (miss -18). 138247→PKK/756891→PKK (Syrian intel frames SDF threat as "PKK"/"Kurdistan Workers' Party" — LESSON: for Syria-govt-attribution Qs, weight PKK high, not just SDF). 474377→Carrick (had Fletcher .74 overconfident -5.5; interim flipped). 666021→UAE (had Ethiopia .45; +small). 80352→DHS (miss -9.5).
- LESSON: For "what will [Syrian/Turkish/govt] SAY" attribution Qs, use THEIR framing (PKK not SDF). Keep top-pick ≤~0.55 unless locked.
- Jan12 resolvers: 117844 (Ukr opp leader bribery — no name yet; Poroshenko trimmed .25). 359260 (Betar NY winddown — well-reasoned .38, hold). 98159 (Atletico Copa QF — no draw info, hold spread).
- Spanish Super Cup: Real Madrid beat Atletico; Barca beat Bilbao 5-0; final Barca v RM Jan 11 Jeddah.

## Day 20 (2026-01-12) cum TW=707.7
- 117844→Tymoshenko (had .10 2nd; +12). 359260→Betar US (had Betar .40/BetarUS .12; +5). 98159→Real Betis (had top .12; +20). Moderate broad dists working well.
- Jan13 resolvers: 214384→NY raised .38 (Noem NYC focus + Mamdani clash; NOT Minnesota=Midwest). 806810→"Technocratic Committee" .30 (consistent media term; Board of Peace=oversight, Mladenov dir-gen). 756639→Philippines .25/Thailand .18 trimmed (no evidence either visa-paused; calibration). 71/75613 held.
- Context: Minneapolis ICE surge huge (Renee Good killed by agent Jonathan Ross; 2000 agents; MN lawsuit; Walz not seeking reelection). Gaza: Hamas to dissolve govt when technocratic cmte takes over; Mladenov=Board of Peace DG. Venezuela: Maduro in NY court; Trump EO shields VZ oil revenue in US Treasury; $100bn US oil rebuild; Switzerland/UK froze VZ gold/assets.

## Day 21 (2026-01-13) cum TW=708.5
- 214384→Maine (miss -18, surprise). 71→Ali Shaath (miss, low -2.5). 75613→Qatar (miss -8). 756639→Thailand (had .18 2nd; +33). 806810→"Palestinian national committee" (had Technocratic Cmte .30; -4 near-concept).
- AO 2026 DRAW IS JAN 15 (after many AO Qs' res dates!). 793465 (Venus R1 opp) res Jan14 < draw Jan15 → void; trimmed tiny. Watch: AO seeds known (Sabalenka1/Swiatek2 W; Alcaraz1/Sinner2 M; Djokovic4). Venus=wildcard, lost Auckland+Hobart R1.
- 521564 migrant-worker custody death→ likely Renee Nicole Good (ICE agent shot MN mother, nationwide protests). Set .30/.26 across name renderings.
- 736847 UN food-aid halt: US SUSPENDED all aid to Somalia (WFP warehouse demolished, 4.4M crisis hunger). Raised Somalia .30.
- 279531 Caribbean .60 hold (US armada vs Venezuela).

## Day 22 (2026-01-14) cum TW=671.8
- 279531 "big armada"→Middle East (had Caribbean .62; -40 OVERCONFIDENCE BURN #2, held 21d). 736847→Somalia (had .30 top after raise; +6). 521564→El Hacen Diarra (not Renee Good; -0.8). 793465→Danilovic (trimmed, -0.4 minimal — good). 39911→Chinese Basketball Assoc (low, -2).
- REINFORCED RULE: cap "which X" top prob ≤0.50-0.55 unless locked by confirmed fact/schedule. Overconfident wrong held-long = -40/-50 (Nipah, armada). Asymmetric: downside >> upside.
- Oreshnik DID hit Lviv (resolved earlier as Lviv — I missed). Context: UK Project Nightfall missiles; coalition-of-willing troop prep; Russia claims Ukr drone attack on Putin residence.
- Jan15: 406433 Guehi→Man City .30 (only Jan pursuer; others summer/free). 599463 gov DOJ→Walz .28/Pritzker .22 (MN epicenter, DHS alleges Walz released criminal aliens). 972999 trimmed Sweden .20. 579233 Arabic .62. 172391 lowered.

## Day 23 (2026-01-15) cum TW=590 (-81 day! overconfidence carnage)
- 579233 Syria language→KURDISH not Arabic (had Arabic .62, held .75→.62 ~22d; -46). 172391→Newroz (-16). 972999→Czech Rep (-20). 406433→Man City CORRECT but TW -17 (held Liverpool .40 21d, switched late — late correction can't beat long-held wrong!). 599463→Walz (+17).
- ***GOVERNING RULE (firm): TW sums daily BSS over the WHOLE question life. Day-1 pred held longest = most weight. A wrong top-pick @0.6 held 20d ≈ -40; @0.45 ≈ -20; @0.30-spread ≈ -10. Catastrophic -40/-50s (Nipah, armada, Syria-lang) dominate. => For speculative "which X/who/where" Qs, keep top ≤0.40-0.45 with 4-5 spread from DAY 1. Reserve >0.55 ONLY for confirmed-news/locked-schedule/structural-near-certainty.***
- Did overconfidence SWEEP: trimmed 13 active preds with top≥0.55 (war-conditional ones→.42-.45; strong-pattern→.50-.62). Repeat sweep periodically.
- Syria attribution confirmed: SANA says "Kurdistan Workers' Party (PKK)" for Maskana/Deir Hafer. 974205→Deir Hafer .34 (Syrian offensive looming there, humanitarian corridor, SDF told withdraw E of Euphrates).

## Day 24 (2026-01-16) cum TW=592.8
- Jan16 resolvers all low-conf misses (small loss) + 974205 Raqqa (had Deir Hafer .34 but broad spread → +10 net). Validates: broad capped spreads = stable, small losses, occasional positive even when top wrong.
- AO 2026 draw OUT (Jan15): Alcaraz R1 v Adam Walton; Sinner R1 v Hugo Gaston; Djokovic same half as Sinner. Venus R1 v Olga Danilovic; Gauff could face Venus R2. Use for AO opponent Qs as rounds play (Jan18+).
- 505500 Portugal: 1st round Jan18; polls Ventura24/Seguro23/Cotrim19/MarquesMendes14/GouveiaeMelo14 — updated to Seguro .30 top (was outdated Gouveia .45).
- Bangladesh election FIRM Feb12 (Yunus). Portugal/AO Qs with res before event likely void → keep minimal.

## Day 25 (2026-01-17) cum TW=635.4 (+43, recovery validated)
- 223607→NCP (+24, had .18 in spread). 505500→Seguro (+15, updated right). 486189→Bangladesh (+0.2). Spain train/Alcaraz R2/Morocco penalty: minimized correctly (~0/+6). Capped-spread strategy WORKING.
- Syria: army took Aleppo city neighbs + east-Aleppo towns; announced FULL CONTROL of Deir Hafer & Maskana (Jan17, SDF withdrew under int'l deal). 904367→Deir Hafer .40. 551676 al-Shaddadi→Syrian Army .42 (momentum). Syria decree formally recognised Kurdish language (confirms 579233).
- Bulgaria: snap election coming, Radev (male) stays president, caretaker cabinet. 37248 (female head of state) → void-likely, trimmed Iotova .08.

## Day 26 (2026-01-18) cum TW=710.1 (+75, NEW HIGH)
- 37248→Iliana Iotova (had her listed .08/earlier .22; +38 — KEEPING right answer LISTED even low = big TW vs omitting). 551676 al-Shaddadi→Syrian army (had .42 top; +48). 904367→al-Shaddadi (had Deir Hafer .40, missed; -12 — SHOULD cross-ref: al-Shaddadi was the answer to BOTH 551676 & 904367).
- LESSONS: (1) always LIST the plausible answer even at low prob (huge asymmetric TW upside). (2) cross-reference related Qs (same event answers multiple). (3) calibrated 0.42 favorite = big win, low risk — keep this band.
- 980781 Sinner R2: Sinner R1 is Tue Jan20 (after res Jan19) → void; minimized. 377358 NFF .30 hold (Norway classic boycott-petition case).
- AO day1: Alcaraz beat (R2 v Hanfmann), Zverev d. Diallo, Paolini through; Kostyuk OUT, Alexandrova OUT (Sonmez). Sinner/Keys/Djokovic/Swiatek start Tue Jan20.

## Day 27 (2026-01-19) cum TW=697.8
- 377358→KNVB Netherlands (had NFF .30; -12; Dutch fans' petition, not Norway). 980781→Duckworth (minimized -0.2).
- Board of Peace: Hungary & Vietnam ACCEPTED; India/Australia/Jordan/Greece/Cyprus/Pakistan invited. 924864 South Asian→Pakistan .48 hold (Pakistan-Trump close; India also invited). 806810/857643 cluster context.
- Greenland: US-Danish "high-level working group" (Vance+Rasmussen); Trump threatens tariffs on 8 EU nations; Rubio drafting purchase proposal; no deal. 621718 trimmed (no framework imminent).
- AO: Sabalenka R2 v Pavlyuchenkova/Bai; Sonmez(qualifier) upset Alexandrova. 464874/922844 minimized (R3 not set by res Jan20).

## Day 28 (2026-01-20) cum TW=734.1 (+36, NEW HIGH)
- 924864→Pakistan (had .48 top; +77 BIG). 207522→Muna island (had Sulawesi .42-.60 26d; -36 — prior-only guess held long = burn). 621718→Mark Rutte (NATO SG; missed, low -4.6). Sabalenka/Sonmez R3 minimized ~0.
- HEURISTIC: high conf only with SPECIFIC current evidence, not just historical prior. Prior-only "which X" → keep top ≤0.25-0.30.
- Ukraine talks: Miami→continuing in DAVOS (WEF, Trump attending; US-Ukraine may sign there). 48762→Davos .45; 655453→Switzerland .40.
- Oscars noms Jan22: One Battle After Another = frontrunner. 876347→OBAA .35/Sinners .25.
- Deloitte WOMEN's Money League: Arsenal top. Men's (348570) not out yet — hold ManCity .56.

## Day 29 (2026-01-21) cum TW=859 (+125 HUGE; multi-resolve day)
- 48762→Abu Dhabi (NOT Davos; my LATE Davos switch wrong BUT original Abu Dhabi .22 held 28d → net +32!). 655453→UAE (orig UAE .25 held long → +36 despite late Switzerland switch). LESSON: trust well-reasoned ORIGINAL geopolitical calls; don't over-react to interim planning news (Davos was a planned venue, actual 3-way=Abu Dhabi/UAE). Late single-news swings cost ≤1 day; long-held originals dominate.
- 876347→Sinners (had .25 2nd; +36). 886103→Coogler/Sinners (had .16 2nd; +32). 400561→Mboko (had .06 top; +11). 110472→Scotland (had .04 listed; +5). 348570→Liverpool (had ManCity .56; -24 prior burn).
- 663866 Crans-Montana: 6 Italian victims, Italy ambassador/Rome prosecutor very engaged → added Italy .40 top (was missing!). LESSON: identify most-engaged party from news.
- Cumulative climbing strongly; capped-spread + trust-original strategy validated.

## Day 30 (2026-01-22) cum TW=851.5
- 663866→Italy (added Italy .40 only 1 day pre-res; +0.62 Brier but TW -7 since 27 prior days had no Italy). CONFIRMS: Day-1 pred dominates TW; late fixes ~1 day only. Get originals right.
- Ukraine: trilateral US-Ukraine-Russia in ABU DHABI Jan23-24 (Witkoff/Kushner→Putin Moscow then Abu Dhabi mil-to-mil + prosperity pkg). 575662 (2nd round Feb4)→Abu Dhabi .42.
- 789042 Milan Olympics US agency→ICE .42 (trimmed from .50 per calib; global anti-ICE wave but actual Olympic security=Secret Service/DSS).
- 243746 CA wildfire funds→OMB .25/DOJ .20 (Bondi/Essayli CA fraud task force + $10B pause).

## Day 31 (2026-01-23) cum TW=946.7 (+95, ~950)
- 575662→Abu Dhabi (had .42, orig .22; +35). 789042→ICE (had .42, orig .50 held ~30d; +72 BIG). 24182→Dominick Cruz (had Poirier; -8). 243746→FEMA (had .08 listed; -3).
- NFC Champ: Seahawks(14-3, #1, beat 49ers 41-6) v Rams Jan25. 694686→Darnold .52/Stafford .42 (near-locked binary, only 2 left — higher conf justified).
- AO: Keys→R3 (still in), Sabalenka→R4 v Mboko. 286957/287417 unknowable specific opponents resolving pre-determination → keep minimal.
- Validated: well-reasoned favorites held LONG = huge TW (ICE +72, Abu Dhabi, Pakistan, al-Shaddadi). Strategy strong; ~950 TW at 96/330 resolved.

## Day 32 (2026-01-24) cum TW=973.6 (~974)
- 694686→Darnold (had .52; +28; Seahawks won NFC). 286957/287417 unknowable→minimized ~0. Strategy solid.
- Gaza body = "National Committee for Gaza Management (NGAC)" met in Cairo (context; 806810/71 resolved).
- Jan25: 110125 trimmed (Australia Day=Jan26 > res Jan25, only Melbourne vandalism so far). 238071→South Kordofan .22 (RSF besieging S.Kordofan; al-Obeid=N.Kordofan drone-hit). 267761 added France .16 (Trump France 25% threat).
- TACO context: Trump withdrew Greenland EU tariffs; threatens Canada 100% (China deal), France 25%.
## Day 33 (2026-01-25) cum TW=996.5 (~1000). 110125→Perth(-11). 238071→South Kordofan(had .22 top after upd;+18). 267761→S.Korea(.10 listed;+12). 320820→Jordan(.08 listed;+6). 9493→Trikala(min;-1.6). 'list plausible low-prob answers' keeps yielding + even when not top. 976773 Ukraine .38/Russia .22 hold (Zaporizhzhia/Chernobyl crisis; Ukraine natural IAEA requester).

## Day 34 (sim 2026-01-26) — cum TW ~974.34
- RESULT: 976773 Netherlands miss -22 (pattern: Western country requesters keep burning me; should weight EU/NL/UK higher generically).
- 465445 (Fury comeback opponent, res 1/27): manager named Arslanbek Makhmudov "top three/four", announcement "imminent"; Fury wants Usyk/Wardley LATER → comeback = tune-up vs lesser. Updated: Makhmudov .30 / Smakici .08 / Joshua .07 / Miller .05.
- 988168 (res 1/27): HELD Bisan Owda→Instagram ~0.46-0.50 (Meta pro-Palestine suppression history, well-reasoned).
- 910937 (res 1/27): HELD Netanyahu .18 / Modi .10 / Prabowo .07 (foreign leader Australia visit charges; no decisive new evidence).
- Lesson reinforced: don't over-churn well-reasoned favorites without new info; but DO update when manager/official source shifts the base rate (465445).

## Day 35 (sim 2026-01-27) — cum TW 953.18 (-21 from Jan26: TikTok miss -15, Fury partial -9.83, Herzog +3.67)
- LESSON: 988168 Bisan Owda → TikTok (not Instagram). Over-anchored Meta-suppression narrative. Bisan huge on TikTok; should've weighted TikTok ~equal. Don't tunnel on one platform/narrative.
- LESSON: 910937 Herzog won at 0.05 → +3.67 TW. Spreading to 4th outcome paid off. Keep covering plausible long-shots.
- Submitted Jan28 resolvers: 430936 Jonglei 0.80 (UNMISS 180k displaced + "operation enduring peace" imminent, 3 counties evacuating — strong); 956334 Mali 0.45 (Mali junta already dissolved all parties 2025, standing example fits literal RC); 789988 Orban 0.18/Modi 0.15 (no signal; Board of Peace context).
- Submitted Jan29-31: 951896 AO Sinner 0.45/Alcaraz 0.42 (both in semis region, Sinner 2x champ+18 streak but heat-cramp issues, Alcaraz #1 1st AO SF); 946810 Grammy BadBunny .27/Gaga .24/Kendrick .22 (AP: Gaga most likely, BadBunny deserving, Kendrick 9 noms); 316535 Cummins NOT replaced — still in squad, joins game 3-4 → low conf Abbott .15; 391811 KryvyiRih .45 (THE mining city, hit Jan23&27); 176447 Ross .38 trim (no Epstein doc surfaced).
- KEY FACT: AFCON 2026 OVER — SENEGAL beat Morocco 1-0 (final Jan 18), Pape Gueye ET winner, Brahim Diaz missed Morocco penalty. Big controversy: Senegal walkout, fan invasion, Morocco/CAF bias claims, CAF "appropriate action" pending. SF: Egypt, Morocco, Nigeria, Senegal. Updated 573851 (CAS appeal) Morocco .30/Senegal .26.
- KEY FACT: Ukraine — security agreement "100% ready" (Zelensky) but US ties it to Donbas concessions; NO deal signed. Trilateral talks Abu Dhabi (Jan 23-24), next round ~Feb 1 Abu Dhabi. Davos bilateral US-Ukraine finalized. Venue=Abu Dhabi for Ukraine talk Qs.
- CL playoff draw = Fri Jan 30 Nyon; final league games Wed Jan 28. 85609(RM opp)/261538(Newcastle 1st-leg city) unpredictable pre-draw — UPDATE Jan 30 post-draw. Newcastle if in playoff plays 1st leg AWAY (top-half seeded). Top-8 finishers get bye (Q may void).

## Day 36 (sim 2026-01-28) — cum TW 1025.48 (+72 big day: 789988 Modi +33, 956334 BF +37, 430936 Jonglei +2.25)
- LESSON: 956334 truth = Burkina Faso (NEW dissolution by Traoré junta), NOT Mali. My Jan-27 over-think (Mali standing example) was WRONG; Day-1 instinct BF 0.25 was RIGHT (saved by TW from Day-1 weight). RULE: when BG frames "watching whether [junta] will take [extraordinary future step]", favor a NEW action by the most hardline junta, not a historical standing example. Don't over-think last-day.
- LESSON: 430936 Jonglei correct but TW only +2.25 (held wrong Upper Nile 0.4 from Day1; corrected only last day). Reinforces: get breaking-cluster facts EARLY.
- CL DRAW STRUCTURE LOCKED (final standings Jan28): Seeded 9-16 [RM,Inter,PSG,Newcastle,Juve,Atletico,Atalanta,Leverkusen]; Unseeded 17-24 [Dortmund,Olympiacos,Brugge,Galatasaray,Monaco,Qarabag,Bodo/Glimt,Benfica]. Pairs: 9/10↔23/24, 11/12↔21/22, 13/14↔19/20, 15/16↔17/18. Seeded play 2nd leg HOME (1st leg at unseeded venue). Submitted: 85609 RM opp = Benfica/BodoGlimt .49/.49; 55999 Benfica opp = RealMadrid/Inter .49/.49; 261538 Newcastle 1st-leg city = Monaco/Baku .46/.46; 35131 Juve eliminated-by = Gala .20/Brugge .18 (Juve seeded, likely advances, big residual).
- 176447 trimmed Ross .22 (Epstein files delayed/blown deadline, no Commerce-Sec Dec2012 island doc surfaced; Bondi redactions unfinished).
- 57193 California .46 (SCOTUS map Q: framing "reject GOP lawsuit, let state keep map" = CA Prop50; lower court upheld 2-1; GOP+DOJ emergency app pending — timing/direction risk).
- 102687 Solberg trimmed .24 (no current Norway ex-PM corruption signal; Norway news = PetroNor/Congo bribes, not a PM).
- 220862 ManCity beat Newcastle 2-0 in Carabao SF 1st leg → City likely in final; removed Newcastle, cut "No final" to .08, spread Arsenal/Liv/Tot/Che (other SF unknown).
- WATCH: Libya cluster — 453736 (who killed in Libya, res 2/3), 426743 (Saif al-Islam burial town, starts 1/31 res 2/3), 976004 (forensics location, res 2/2). No confirming kill news yet; recheck near Jan 31.

## Day 37 (sim 2026-01-29) — cum TW 1074.95 (+49: CL structural plays 85609 +18, 55999 +16.5, 1877 Vonn +20.7; 261538/35131 correct-top but ~0 TW; 176447 Lutnick -3.7)
- BIG LESSON: structural/constraint reasoning (CL draw pairing rules) → calibrated 50/50s scored ~+0.50 Brier each. When a Q is constrained to 2 outcomes by rules, submit ~.49/.49. Apply same to future bracket/draw Qs.
- LESSON: 176447 truth Lutnick (current Commerce Sec) not Ross. Anchored wrong on "older 1st-term" prior. For "which X official" Qs split more evenly across plausible holders.
- 1877 Vonn airlifted (truth) — comeback veteran crash-risk instinct correct, +20.7.
- 951896 AO updated: SF Fri 1/30 Alcaraz-Zverev & Djokovic-Sinner. Sinner eased past Shelton; Djokovic lucky (Musetti retired injured, was 2 sets down), 38yo struggling. → Sinner .43/Alcaraz .40/Zverev .09/Djokovic .06 (removed out Musetti/Shelton).
- 316535 Cummins NOT replaced (still in squad, joins game 3-4); no replacement named → trimmed to Abbott .10/Beardman .07/Bartlett .05/Dwarshuis .04 (minimize void downside).
- KEY FACT T20 WC 2026 (Feb7-Mar8, India+SriLanka): BANGLADESH REFUSED to travel → SCOTLAND replaced them. Group A: India,Pakistan,Namibia,Netherlands,USA. Group C: England,Italy(debut),Nepal,Scotland,WestIndies. India open vs USA Feb7 Wankhede Mumbai; defending champs (SKY captain). WI captain Shai Hope.
- Feb5-6 spec Qs (883856 Moscow officer shot, 198725 Mohammadi exile city, 456284 WaPo publisher) — held, no info, low spreads OK.

## Day 38 (sim 2026-01-30) — cum TW 1079.95 (+5: 316535 Dwarshuis listed @.04 → +5; low-spread coverage of long-shots keeps paying)
- 951896 AO FINAL = ALCARAZ vs DJOKOVIC. Djokovic BEAT Sinner in 5 sets (oldest AO finalist, Open era); Alcaraz beat Zverev in 5h27m marathon (longest Melbourne SF, thigh cramps). Sinner OUT. → 2-outcome: Alcaraz .66 / Djokovic .32 (Alcaraz #1/22yo/beat Djoko 2025 USO; Djoko 38 but Melbourne king + just beat Sinner; both had grueling 5-set SFs).
- 946810 Grammy: Independent (1/30) explicitly tips BAD BUNNY for AOTY; AP says Gaga "most likely" / BadBunny "deserving"; Kendrick 9 noms (rap won AOTY only 2x ever). → BadBunny .32/Gaga .24/Kendrick .20/Sabrina .09/Tyler .06. Ceremony Sun Feb 1, Crypto.com LA.
- 562701 Balochistan: Jan30 — Pak military killed 41 fighters in raids at HARNAI (30) & PANJGUR (11) districts, "sanitisation ongoing". Boosted Panjgur .20/Harnai .16/Kalat .10/Mastung .08/Turbat .06.
- 391811 held Kryvyi Rih .45 (no specific miners-bus attack yet; KR = dominant Dnipropetrovsk mining city). Risk: event may not occur by 1/31.
- Ukraine: Russia struck Kharkiv passenger train (5 killed, Zelensky "terrorism"); Kherson "human safari" civilian drone attacks; trilateral Abu Dhabi talks continue (next Sunday). Energy infra hammered.

## Day 39 (sim 2026-01-31) — cum TW 1124.90 (+45: AO Alcaraz +39.8, Grammy BadBunny +25.4; offsets 391811 Ternivka -14.7, 562701 Nushki -5.5)
- BIG LESSON (location Qs): 391811 truth=Ternivka NOT Kryvyi Rih. "miners" = COAL (Pavlohrad/Ternivka/Western Donbas basin), NOT iron-ore Kryvyi Rih. RULE: for "which city/town will [specific industrial/niche incident] happen" where event hasn't occurred yet, CAP top ≤0.32 and spread 5 wide incl. smaller specific towns. Don't anchor on the famous big city.
- 562701 truth=Nushki (Balochistan). Unpredictable specific town; spread didn't cover. Same lesson.
- WINS: AO final correctly updated to Alcaraz .66 (beat Djokovic); Grammy BadBunny .32 (Independent tip). Updating to clear favorite when bracket/news resolves = high TW.
- 102687 Norway ex-PM corruption: STILL zero signal (only PetroNor/Congo bribes case, execs not a PM). Trimmed Solberg .13/Stolt .04/Bond .03 to minimize void-downside (likely no PM identified by Feb1).
- 449104 US minerals stockpile name: no official name announced (bipartisan $2.5B bill, Trump stakes in USA Rare Earth/MP Materials). Held low spread.
- Libya cluster (453736 killed res2/2, 426743 Saif burial res2/3, 976004 forensics res2/2): NO confirming Saif/Libya killing news yet despite 426743 starting 1/31. Hold spreads; recheck Feb1.
- TO CHECK Feb1: 492629 James Harden→Clippers trade (NBA deadline Feb5), 243685 Myanmar 5-member panel name, 955662 Brazil bus-crash state, 995305 market-fire city, 336425 E-Ukraine market shelling city.

## Day 40 (sim 2026-02-01) — cum TW 1110.69 (-14: 102687 Norway→Jagland -12.3 [never listed him], 449104 "Project Vault" -1.9)
- CRITICAL RECURRING LESSON: concentrated Day-1 prior w/o evidence on "which person/place" Qs = big TW drain over question life (Jagland -12, Solberg held high all run; Nipah, Kryvyi Rih, Syria-Arabic earlier). FIX now applied: for speculative who/where Qs, Day-1 cap top ≤0.22-0.25, list 5 broad plausible, accept wide residual. Updating to favorite only AFTER hard news.
- 955662 Brazil bus crash: no event yet; rebalanced toward NE Brazil pilgrimage states Bahia .16/Pernambuco .13/MinasGerais .12/Ceara .07/SaoPaulo .06 (was over-concentrated MG .22).
- Held (no news, low spreads OK to limit void-downside): 453736 Libya killed (Saif .22), 976004 Libya forensics, 243685 Myanmar 5-panel (forms Mar-Apr, won't be named by Feb2), 492629 Harden→Clippers (no trade; deadline Feb5), 995305 market fire city, 220862 Carabao (other SF unknown; ManCity beat Newcastle 2-0 1st leg).
- FACTS: Myanmar election — USDP (military) swept; parliament elects president MARCH, new govt APRIL; Min Aung Hlaing expected president. ASEAN won't recognize. ManCity finished 8th in CL (direct to last-16, no playoff) via Benfica beating Real Madrid 4-2.
- NBA deadline Feb 5: Giannis trade rumors (Knicks/Towns), no Harden trade reported. Paul George suspended 25 games (drug policy).

## Day 41 (sim 2026-02-02) — cum TW 1178.18 (+67 huge: Libya Saif killed +38.8, Carabao Arsenal +24.8, Libya forensics Zintan +17.7; offsets Brazil Alagoas -10.1)
- KEY NUANCE on the concentration lesson: Saif al-Islam .22 held from Day1 → +38.8 (correct well-reasoned prior pays HUGE via TW). Discriminator: concentrate when there's a STRUCTURAL/logical reason for the favorite (Saif=dominant Libya figure; Zintan=where he was detained); spread when it's a vague prior w/o basis (Solberg/Jagland). 
- 220862 Carabao = Arsenal (my Day1+ top) +24.8.
- 955662 Brazil = Alagoas (didn't list; held MG .22 Day1) -10.1 → reinforces spread-wide on location Qs.
- Updated Feb3 resolvers: 336425 → rebalanced to DONETSK-region cities (BG says Donetsk): Kostiantynivka .25 (history of market strikes)/Kramatorsk .13/Sloviansk .09/Pokrovsk .06/Druzhkivka .05; removed Kherson (wrong region). 426743 Saif burial → BaniWalid .26 (Warfalla loyalist bastion)/Sirte .22 (Qadhadhfa home)/Zintan .10/Sabha .07/Tripoli .05. 579252 widened Tehran .20/Shiraz .13/Karaj .10/Mashhad .08/Isfahan .06.
- 57193 SCOTUS map: HOLD California .46 (justified structural fav — specific pending GOP/DOJ suit vs CA Prop50 fits Q exactly; lower court upheld 2-1). Not a vague prior.
- FACTS: DTEK miners bus drone strike = city of DNIPRO, ≥12 miners killed (Feb2) [391811 already resolved Ternivka]. Trump claimed Putin agreed temp halt on city strikes (cold weather) — Russia kept striking (Zaporizhzhia maternity hosp, Dnipro). Iran: wrestler Saleh Mohammadi imminent execution, US State Dept campaigning; >30 athletes shot in crackdown.

## Day 42 (sim 2026-02-03) — cum TW 1236.77 (+58: SCOTUS California +62.6 [justified structural fav held early], Saif burial BaniWalid +13.8; offsets 336425 Druzhkivka -10.3, 579252 Qom -7.6)
- REFINED RULE (validated): TW swings dominated by early/Day-1 concentrated pick. Concentrate+hold-early ONLY w/ CONCRETE specific reason (pending case fits Q exactly=CA +62; unique dominant figure=Saif +38; draw constraint). For weak/generic "one of many similar" (Kostiantynivka among fortress-belt towns; Tehran among Iran cities) → spread evenly cap ≤0.22.
- 336425 truth Druzhkivka (had it @.05 but held Kostiantynivka .22-.25 Day1→ -10.3). 579252 truth Qom (didn't list; religious/judiciary city — should've included). Both = generic-prior overconcentration drain.
- SUPER BOWL LX SET: New England Patriots vs Seattle Seahawks, Feb 8 Levi's Stadium. NE beat Broncos 10-7 (AFC, snow, Drake Maye, elite D); SEA beat Rams 31-27 (NFC, Sam Darnold 3TD, #1 seed, blew out 49ers 41-6). 180958 → Seattle .53/NE .45 (even, slight SEA edge #1 seed+offense). Bad Bunny halftime; Trump skipping.
- 534224 Olympic women's DH silver country → Switzerland .20/Italy .20(home)/Austria .15/US .11(Vonn airlifted 1/30)/Norway .07 (single medal, wide spread).
- 318661 Colombia peace talks → ELN .24/EMC .18/SegundaMarquetalia .14/ClanGolfo .08 (Total Peace collapsed; no specific resumption; spread). 538697 HOLD Indonesia .38 (Prabowo big Gaza-troop pledges; justified). 398988 HOLD Hezbollah .48 (THE S.Lebanon group; justified structural).
- FACTS: ISF Gaza — Pakistan pledged 3,500 troops; Mladenov = Board of Peace High Rep for Gaza; NCAG technocratic Gaza govt; Rafah crossing limited reopening (~150/day pedestrians). Trump-Petro met/meeting at White House (US-Colombia tensions de-escalating).

## Day 43 (sim 2026-02-04) — cum TW 1236.77 (no resolvers Feb3→4)
- 883856 Russian officer shot Moscow (res Feb5): no such event; HOLD low spread (Gurulyov/Alaudinov/Surovikin .03/.03/.02; void→ -0.002 negligible).
- 456284 WaPo publisher (res Feb6): Will Lewis absent from staff calls/"not present much"; Matt Murray (exec editor) de-facto running paper, praised "strong stand-up editor" by Don Graham; Bezos gutting ⅓ staff. → Murray .26/Lewis .07/Baron .04/DonGraham .03 (concrete reason to concentrate Murray; caveat publisher≠editor & Lewis may not formally step aside by Feb6).
- 198725 Narges Mohammadi exile city (res Feb6): no new exile sentence reported; trimmed Zabol .10/Tabas .08/Zahedan .06/BandarAbbas .05 (remote-exile towns; reduce void downside).
- Pre-positioned Feb9: 14689 US school-shooting country .50 (justified base-rate fav, hold); 487245 Venezuela .42 (US-tension fav, hold); 527803 Canada school-shooting town low spread; 745180 cyclone Gezani→Freddy .22/Batsirai .20/Idai .16 (starts Feb5, recheck); 312764 Egypt planning min Rania Al-Mashat .33 (hold).
- FACTS: WaPo mass layoffs (⅓ staff, sports/book sections axed) at Bezos behest; Lewis sidelined, Murray exec editor leading. Iran: >3,000 dead in unrest (Tehran's own admission); Oscar co-writer Mahmoudian arrested; AO/Oscars context. Sergei Ivanov dismissed as Putin special rep (still Security Council).

## Day 44 (sim 2026-02-05) — cum TW 1236.55 (-0.22: 883856 Alekseyev, didn't list but low spread → negligible. VALIDATES low-spread for no-signal speculative event Qs.)
- 456284 WaPo: still NO formal "Lewis steps aside"/publisher successor named; Murray (exec editor) running everything but publisher≠editor + void risk if Lewis hasn't stepped aside by Feb6. Trimmed Murray .22/Lewis .06/Baron .03/Graham .03.
- 198725 Mohammadi exile: no new sentence reported; HOLD trimmed spread (void-likely, small downside).
- WINTER OLYMPICS open Feb 6 (Milano-Cortina, →Feb 22). Upcoming Olympic Qs: 534224 women's DH silver country (res Feb7-8, done: Swiss/Italy .20 each); 877 country w/30 medals natl record (res Feb22); 882 men's ice hockey gold (res Feb22); 792 broadcaster Israel-bobsleigh segment (res Feb17); 772 high-speed rail burned cables cities (res Feb14). PRIORITIZE Olympic medal Qs as events occur Feb7+.
- Super Bowl LX Feb 8 (Seattle .53/NE .45). ~20 resolvers Feb7-15 — heavy week ahead.

## Day 45 (sim 2026-02-06) — cum TW 1232.46 (-4: 198725 Mohammadi→Khosf -3.4 [her HISTORICAL exile town, should've known], 456284 D'Onofrio -0.7 [publisher≠editor instinct right, trim limited loss])
- LESSON: recurring named figures → check HISTORICAL pattern (Mohammadi previously exiled to Khosf). LESSON validated: trimming a shaky concentrated pick (Murray .32→.22) limits loss when wrong (-0.7 not -4).
- 180958 Super Bowl: SEATTLE "firm favourites" (AlJazeera), expert edge to Darnold; NE QB Drake Maye RIGHT SHOULDER injury (ProFootballDoc concerned), struggled in playoffs; Darnold hot (41-6, 346/3TD). → boosted Seattle .60/NE .38.
- 534224 women's DH (Sun Feb8 Cortina): Goggia (ITA, home, fav course), strong Swiss team (Gut-Behrami/Suter/Blanc), Austria underdogs, Vonn (USA,41,torn ACL wk ago — training only, won't medal). → Swiss .20/Italy .20/Austria .13/US .11/Germany .07 (swapped Norway→Germany; Norway not women's-DH power).
- Olympics opened Feb6 Cortina. Men's DH Sat Feb7 Bormio/Stelvio (Odermatt/Paris favs). Watch medal Qs.

## Day 46 (sim 2026-02-07) — cum TW 1245.04 (+13: SuperBowl Seattle +23.7; offsets women's DH silver Germany -11.2 [had Germany only .07, added late])
- LESSON: Olympic single-medal country Qs = dark-horse risk (Germany silver). Spread VERY wide (top ≤0.18), include Germany/Czechia/France/Canada/Norway. Day-1 narrow spread drains TW over ~3wk life.
- 318661 Colombia: EGC/Gulf Clan SUSPENDED Doha talks (Petro targeted their leader Chiquito Malo at Trump WH meeting). "Major dialogue in doubt"=EGC. Resumption by Feb8 uncertain (leader now a target). → spread Gulf Clan .20/ELN .18/EMC .15/SegundaMarquetalia .10 (used "Gulf Clan" not "Clan del Golfo" = AJ common English name).
- 398988 HOLD Hezbollah .46 (THE S.Lebanon group Israel raids; justified structural; Israel hit Kfar Tibnit/Ain Qana/Ansariyeh). 538697 Indonesia .35 trim (Prabowo big pledges; void risk). 630740 trimmed Beirut .14/Tripoli .10 (no Lebanon collapse; collapses all in India - void likely).
- FACTS: Colombia — Petro at Trump WH Feb3, named 3 kingpin targets (Chiquito Malo/EGC, Iván Mordisco, Pablito); EGC suspended Doha peace talks. Hezbollah replaced security chief Wafiq Safa (→Hussein Abdullah); Lebanon army done phase-1 Hezbollah disarmament S of Litani. Gaza ceasefire violated daily (>525 Palestinians killed); AJ investigation on Israel-backed Gaza militias (Strike Force Against Terror/Hussam al-Astal).

## Day 47 (sim 2026-02-08) — cum TW 1299.06 (+54: Gaza/Indonesia +53.7 [justified fav held Day1!], Lebanon collapse Tripoli +23.6, Colombia GulfClan +4.2; offset 398988 al-Jamaa al-Islamiya -27.4)
- BIG LESSON: 398988 truth = al-Jamaa al-Islamiya, NOT Hezbollah. "Hezbollah=THE S.Lebanon group" felt justified but was a CATEGORY DEFAULT, not event-specific evidence. Multiple armed groups exist (Hezbollah/Amal/Hamas/al-Jamaa al-Islamiya/PFLP). Held .46 from Day1 → -27. RULE: "obvious" group/person favorites w/o SPECIFIC current evidence of THAT entity in THAT event → cap ≤0.38, spread more, list 5.
- CONTRAST: 538697 Indonesia .35 (Prabowo's SPECIFIC repeated public 20k-troop Gaza pledges) = grounded → +53.7. Discriminator = specific evidence for THIS entity vs category assumption.
- 487245 added Colombia (Petro-Trump drug drama) → Venezuela .40/Iran .15/China .08/Colombia .07/Russia .06.
- 312764 Egypt planning min: no reshuffle reported; trimmed Al-Mashat .30 (incumbent, justified) /ElSaid .08 (void risk).
- HOLD: 14689 US school-shooting country .48 (base-rate fav); 527803 Canada town low spread (void likely); 745180 cyclone Gezani Freddy .22/Batsirai .18/Idai .16 (no Gezani news yet).
- FACTS: Yemen new govt — PM Shaya Mohsen al-Zindani (also FM); Maryland elementary accidental discharge (non-fatal); Philippines Tropical Storm Penha (5 dead Mindanao).

## Day 48 (sim 2026-02-09) — cum TW 1263.29 (-36 DOWN day: 14689 school-shooting→Canada -25.7 [held US .50 base-rate Day1!], 312764 Egypt→Ahmed Rostom -12.1, 745180 cyclone→Geralda(1994) -12; offset 487245 Iran +14.7 [wide spread covered])
- PATTERN CRYSTALLIZED: Day-1 concentrated picks on speculative who/where/which (US base-rate, incumbent, recent-cyclone, Hezbollah-category) = systematic TW drain when specific event lands elsewhere. Even base-rate/incumbent/obvious favorites must be capped & spread unless SPECIFIC current evidence.
- ACTION: ran high-concentration sweep of ACTIVE preds (top≥0.40). Trimmed: 304287 Bangladesh Jamaat .42/BNP .20/NCP .14 (BNP frontrunner 33-35%, Jamaat 30-34% resurgent, AL banned; BNP govt→Jamaat opp OR Jamaat govt→BNP opp); 456938 Rousey removed "Not announced" placeholder→Cyborg .22; 325000 Hezbollah .58→.50 (Israeli-army attribution more Hezbollah-reliable than 398988's self-claim, but post-lesson trim); 221278 hockey Canada .36/USA .28 (both elite, was .42).
- 652747 Novichok .62 KEPT (justified: Navalny established Novichok poisoning, conclusive toxin finding→Novichok). 434350 Markram .45 KEEP (SA T20I captain). 415069/489902 Oman/Muscat US-Iran venue KEEP (historical mediator). 506444 Australia KEEP (>>S.Korea women's football).
- TODO: continue sweep on remaining flagged active top≥0.40 (mostly Iran-war cluster: 739634,58660,209948,200605,584240,742975,59501; + 240291 Russia,320138 Telegram,271330 Ukraine,262505/297818/246419 Gulf) by res date.
- FACTS: Bangladesh election Feb12 (AL banned; BNP frontrunner Tarique Rahman/Khaleda Zia; Jamaat Shafiqur Rahman; NCP Nahid Islam weak). Canada school shooting = Tumbler Ridge BC. Cyclone = Geralda comparison.

## Day 49 (sim 2026-02-10) — cum TW 1263.29 (no resolvers 2/9→10)
- SWEEP insight: most remaining flagged top≥0.40 are IRAN-WAR CLUSTER (739634,58660,209948,200605,584240,59501,742975,994042,246419,297818,271330...) — Question Start Dates Feb19–Mar15 (NOT started yet), presuppose US-Israel-Iran war that has NOT happened (June2025 war ended). NOT urgent; handle as they approach start/res + per war news. Concentrated "if-war-then-X" picks (Iran/Tehran/Oman) are pattern-based; keep but watch for war actually starting.
- Non-war flagged (keep, justified, not urgent): 240291 Latvia-drone→Russia .55; 506444 Australia>>S.Korea; 262505 Qatar hostage-mediator; 666706 Texas (Chuck Norris, starts 3/9, presuppositional).
- 613203 Tractor FC: Iran's Tractor already qualified to ACL Elite last-16 (W region w/ AlHilal,AlAhli,AlWahda). Opponent = bracket-dependent, unknown pre-draw. Low spread AlWahda .10/AlHilal .09/AlAhli .08/ShababAlAhli .07/Sharjah .06.
- Next resolvers: 304287 Bangladesh (Feb12), 739916/795774 (Feb12), 652747 Navalny/Novichok (Feb13), 901381 (Feb13).

## Day 50 (sim 2026-02-11) — cum TW 1261.80 (-1.5: 613203 Tractor→ShababAlAhli, had .07, low spread limited loss)
- 304287 Bangladesh (res2/12): BNP "widely expected to win"/Khaleda Zia DIED (sympathy)/Tarique returned; Jamaat "strong challenge, may surprise, best-ever". → Jamaat-e-Islami .45 (main opp if BNP govts)/BNP .22/NCP .12/Jatiya .05.
- 795774 trimmed Paris .12 (no France far-right killing/Macron-Meloni dispute; France news=Le Pen trial; void-likely).
- 739916 carrier: held Ford .22/Nimitz .14 spread (no 2nd carrier named; "by end March" window).
- ⚠️ ESCALATION WATCH: US-Iran tensions PEAK. "Iran strike looms" — US armada (USS Abraham Lincoln+3 destroyers+F-15E+F-35) Arabian Sea; US shot down Iranian Shahed-139 drone near Lincoln (Feb3); IRGC harassed US tanker Stena Imperative (Strait of Hormuz). Trump considering "major strike on Iran"; Araghchi defiant. NO war yet (buildup+skirmish). IF strike/war starts → ~70 Iran-war-cluster Qs activate (start dates Feb19-Mar). MONITOR DAILY; update cluster fast if war begins.
- FACTS: Le Pen appeal trial — prosecutors seek 5yr office ban (not immediate); verdict ~summer; Bardella backup for 2027.

## Day 51 (sim 2026-02-12) — cum TW 1364.02 (+102 HUGE: Bangladesh Jamaat +59.5, Ford carrier +30.4, Lyon +12.3)
- VALIDATED: news-grounded favorites held consistently = big TW (Jamaat per polls, Ford per US-surge-carrier doctrine). Wide spread covering true answer at low p (Lyon .06) still nets positive when event occurs.
- 901381 BIG CORRECTION: Olympics rail sabotage = cables SEVERED on BOLOGNA–VENICE line (+ Pesaro cabin fire, Bologna). None of my old options had it! → Bologna and Venice .58/Bologna and Milan .16/Bologna and Florence .08. (Lesson: when a specific event is reported, REPLACE generic option set with the actual named entities.)
- 652747 Navalny toxin KEPT Novichok .58 (justified: established 2020 Novichok poisoning precedent; ~85% if resolves). Void risk (no 5-govt finding reported yet).
- ESCALATION WATCH continues: US-Iran buildup, no war yet. Monitor.

## Day 52 (sim 2026-02-13) — cum TW 1314.89 (-49: Navalny→epibatidine(exotic frog toxin!) -43.2 [Novichok .58 = "precedent" overconfidence, NOT confirmed], 901381→Rome-Naples -5.9 [over-pivoted to Bologna-Venice on 1 report])
- RULE HARDENED in STRATEGY.md: cap top ≤0.45 on ANY speculative who/where/which/what unless SPECIFIC current outcome already reported. ≥0.50 ONLY if essentially confirmed (set matchup/clear polls/draw constraint/scheduled fact). "Established precedent" ≠ confirmation.
- Applied: re-swept active top≥0.46 → trimmed 325000 Hezbollah .50→.42, 415069 Oman .50→.44, 739634 Iran .50→.45, 828811 Hezbollah .55→.45, 240291 Russia .55→.50. (506444 Australia .46 kept — strong-fav 2-team matchup, borderline OK.)
- LESSON: 901381 — found Bologna sabotage news, pivoted .58 there, but Q resolved on a DIFFERENT incident (Rome-Naples cables). Don't assume the news incident I found = the one the Q means; keep ≤0.45 spread when multiple incidents possible.
- Net trajectory still strong (1315, was 953 on Jan26). Over-concentration on unconfirmed = the one persistent leak; now hard-capped.

## Day 53 (sim 2026-02-14) — cum TW 1314.89 (no resolvers 2/13→14)
- Feb15 resolvers updated (all event-not-confirmed → hardened rule, cap ~0.26 wide spread):
  - 190197 Pakistan T20 clinch-win opponent: FIXED options (old had Ireland/UAE — wrong, not Group A). Group A=India/Pak/USA/Neth/Namibia. → Namibia .22/USA .16/India .10/Neth .10.
  - 580089 NW Pakistan moto-bomb district: Dera Ismail Khan epicenter (5 police killed Feb11) → DIKhan .24/Bannu .16/NWaziristan .10.
  - 778783 Sudan market drone town: KORDOFAN epicenter (RSF drones, 90+ killed late Jan-Feb6, mosque/WFP hits) → El Obeid .26 (N.Kordofan capital, besieged)/Kadugli .12.
- FACTS: T20 WC groups — A:India,Pak,USA,Neth,Namibia; B:Aus,SL,Ire,Zim,Oman; C:Eng,WI,Nepal,Italy,Scotland; D:NZ,SA,Afg,Canada,UAE. Pak beat Neth opener; Pak-India Feb15 Colombo. India defending champs. Sudan civil war expanding Darfur→Kordofan (RSF vs SAF drones). Islamabad Shia mosque suicide bombing 31+ killed.

## Day 54 (sim 2026-02-15) — cum TW 1345.90 (+31: 190197 Namibia +12.3, 580089 Bannu +25.3 [had .16, wide spread held early=big TW], 778783 Sodari -6.6 [capped, small loss]). HARDENED RULE VALIDATED — wide capped spreads turn would-be disasters into small losses + capture long-shot hits.
- 454482 former-champ-miss-Super8: WI ALREADY QUALIFIED (won Grp C) — removed; Pakistan beat Namibia→likely qualified, lowered. → England .28 (lost to WI, Grp C w/ dominant WI)/SriLanka .22/Pak .12/Aus .10.
- 548734 storm: STORM NILS confirmed battering France/Spain (850k no power, deaths, "unusually strong", officials commenting) → Nils .48/Marta .14. (News-confirmed → justified ~.48.)
- 207951 Olympics broadcaster Israel-bobsleigh: RaiSport(RAI) in active commentary-scandal (journalists striking) → RAI .20/BBC .15/NRK .10 (no specific confirmation; capped).
- HELD low-spread: 22203 Bangladesh woman minister, 456938 Rousey/Cyborg .22, 876124 St Petersburg blast, 903473 Vinicius racism (all speculative, minimal downside).
- FACTS: T20WC — WI won Grp C (3-0, beat Scotland/England/Nepal); Nepal/Namibia eliminated; India crushed Pakistan by 61 (Feb15 Colombo, no handshakes). Olympics: Breezy Johnson (USA) won downhill GOLD; medals cracking (ribbon defect fixed); Ukraine skeleton Heraskevych DQ'd (memorial helmet). Storm cluster Iberia: Nils/Marta/Leonardo/Kristin.

## Day 55 (sim 2026-02-16) — cum TW 1325.81 (-20: Rousey→Gina Carano -19.1 [legacy rival, missed; Cyborg .22 held], others small via low spreads; Sertolovo +11.2 @.06 wide-spread hit!)
- LESSON: "comeback/return opponent" Qs → include the NOSTALGIC LEGACY RIVAL (Carano for Rousey). 548734 "poised to batter" = FUTURE storm (Pedro) not current (Nils) — confirmed reading.
- 307616 BIG FIX: T20 Super8 PRE-SEEDED. Group Y = England(Y1),NZ(Y2),Pakistan(Y3),SriLanka(Y4); Group X = India,Aus/Zim,SA,WI. Pakistan opener opponent ∈ {SL,NZ,Eng} ONLY (old options had India/Aus/SA = Group X, impossible). → SL .34/NZ .33/Eng .28 (constrained 3-way, justified concentration).
- 479547 Iran frigate sunk off SL: hypothetical, no event (naval news=US boarding tankers Veronica III/Aquila II). Trimmed to .08/.06/.05/.03 (min void downside).
- FACTS: T20WC qualified S8 = India, West Indies, South Africa (+more). Australia in REAL danger of group-stage exit (Zimbabwe upset). Pakistan needs to beat Namibia (likely) to be Y3. India S8 opener vs SA Feb22 Ahmedabad. US Navy: Gerald R Ford = Caribbean/4th Fleet (not ME!); Truxtun-Supply collision Caribbean.

## Day 56 (sim 2026-02-17) — cum TW 1331.26 (+5: 307616 NZ +8.7 [structural group fix], 479547 Dena -3.3 [over-trimmed; event DID happen, Dena @.05])
- LESSON: don't over-trim speculative events to near-zero — 479547 IRIS Dena actually sank; I had Dena .05 (trimmed too hard). Balance: cap top low BUT keep ~5 plausible at ≥0.05 each so a hit still scores.
- 943026 AI tool Dutch court = GROK .52 (xAI/X Grok = THE global controversy: Ireland DPC probe, Brazil/France/UK/Indonesia bans, 3M sexualized images; Dutch case clearly about Grok). Justified strong fav (THE entity in worldwide litigation for this exact issue). Clothoff .18 backup.
- 207254 France-US row office: State Dept anti-Europe-censorship push (Rubio/Vance Munich, DSA "Orwellian") → DRL .22/StateDept .16/WH .10 (no specific incident confirmed; capped spread).
- 485328 Dem SOTU response: no announcement; wide spread Wes Moore .13/Beshear .11/Whitmer .07/Jeffries .07/Slotkin .05.
- FACTS: Grok deepfake scandal huge (xAI). Rubio Munich speech (Reagan-esque, anti-EU-censorship/climate/migration). T20WC NZ = Pakistan's S8 opener.

## Day 57 (sim 2026-02-18) — cum TW 1367.50 (+36: Grok AI-tool +47.3 [news-grounded strong fav validated]; offsets 207254 Bureau-of-Counterterrorism -7.3, 485328 Spanberger -3.8 [both unlisted but capped/wide=small loss])
- VALIDATED again: concentrate ONLY when news-confirmed/near-deterministic (Grok=THE global deepfake-litigation entity → +47). Capped/wide spreads keep misses small (-7,-4).
- 325000 Israel-army-names-group at Lebanon command centre → Hezbollah .45 (Israel consistently attributes Lebanon infra/warehouse strikes to Hezbollah; "command centre"=organized=Hezbollah; recent PIJ vehicle strike near Syria border → PIJ .08). Capped .45 (398988 -27 lesson: group self-claim vs Israeli-attribution differ; latter more Hezbollah-reliable).
- 434350 SA NZ-tour captain → Markram .45 (clear incumbent T20I captain, 86* vs NZ; capped per rule, squad maybe not announced).
- FACTS: Israel near-daily Lebanon strikes (10,000+ since 2024 truce per UN; Hezbollah warehouses; PIJ Majdal Anjar). SA reached/near T20 S8 (Markram 86* vs NZ, 3-0 Grp D). Trump pardoned 5 ex-NFL players. Olympics curling cheating row.

## Day 58 (sim 2026-02-19) — cum TW 1317.19 (-50: 325000 Israel→HAMAS -27.2 [3rd Hezbollah-category disaster!], 434350 SA capt→Keshav Maharaj -23.1 [incumbent-Markram assumption failed, SA rotated])
- ABSOLUTE RULE now in STRATEGY.md: speculative who/which/what (group/person/team chosen by an actor, NOT yet reported) → top ≤0.35, spread ~flat 5. Israeli attribution = multi-way. "Incumbent retained" NOT safe.
- DID FULL SWEEP: capped ~22 active concentrated picks (mostly Iran-war cluster) to ≤0.35: 415069 Oman .35, 489902 Muscat .35, 209948 .34, 58660 Tehran .33, 739634 Iran .35, 59501 Qatar .33, 246419 Bahrain .35, 994042 IRIB .35, 584240 US .33, 297818 AbuDhabi .34, 338215 IsraeliEmb .33, 830793 Israel .34, 271330 Ukraine .35, 807049/425983 "No player" .33-.34, 828811 Hezbollah .34, 742975 MQ-9 .34, 666706 Texas .34, 262505 Qatar .35, 200605 Iran .33, 240291 Russia .42, 320138 Telegram .35. Kept 506444 Australia .45 (genuine sports heavy-fav vs S.Korea, not selection-speculation).
- 26859 Afghan provinces (held wide: Paktika.16/Khost.14/Kunar.12; Saudi-mediated PAK-AFG de-escalation, soldiers freed Feb17); 59953 Greek migrant island → Crete.18/Gavdos.15/Lesbos.12/Chios.10 (Chios Feb3 wreck pre-window; no new yet).
- FACTS: PAK-AFG: Saudi-mediated thaw, Taliban freed 3 PAK soldiers Feb17; Bajaur checkpoint VBIED 11+ killed; ISIS claimed Islamabad mosque bombing. NO new Iran war yet (still buildup).

## Day 59 (sim 2026-02-20) — cum TW 1338.95 (+22: 59953 Greek island=Crete +29.8 [wide spread, Crete top from Day1, southern-Libya-route reasoning]; 26859 Nangarhar+Paktika combo -8 [exact-combo format hard])
- VALIDATED: wide calibrated spread w/ right modest top held early = +30 (Crete). Strategy sound.
- 221278 hockey: Reuters/StraitsTimes report "USA earn gold, OT win over Canada", Switzerland bronze → near-CONFIRMED → USA .75/Canada .18 (justified high, news-reported result).
- 162065 30-medals-record: Norway leads 34 (not their record), USA 26, ITALY 26 (host, old Italian WO record ~20) → Italy .42 (clear record-territory candidate; news-grounded).
- 73075 ambassador France summons re Quentin Deranque (Lyon killing): Macron-Meloni ACTIVE CLASH (Meloni TV interview Red Brigades) → Italian amb Emanuela D'Alessandro .30/Kushner(US) .16.
- 493481 HELD Afghanistan .35 capped (Pakistan DID strike Nangarhar+Paktika per 26859; Afghanistan likely "strongly condemns"; phrase attribution varies).
- FACTS: Olympics close Feb22; Norway top (34), USA/Italy 26. USA men's hockey GOLD (OT vs Canada), Switzerland bronze. USA women's hockey gold (OT vs Canada). France-Italy row over Lyon far-right killing (Quentin Deranque). France not joining Board of Peace (wants Gaza-recentre); EU Commissioner Suica attended.

## Day 60 (sim 2026-02-21) — cum TW 1437.55 (+99 HUGE: Italy 30-medals +47.8, Kushner ambassador +49.9 [Day1 .30 held!], USA hockey +26; offsets India-condemns-Pakistan -15.3, Lviv -8.9)
- VALIDATED: news-confirmed/near-deterministic → concentrate big (Italy record, USA hockey). 73075 Kushner: Day1 .30 weighting paid +50 even though last-day I wrongly made D'Alessandro top — Day-1 weight dominates. 493481 India (not Afghanistan) -15: capped spread limited vs -27.
- 992626 STRUCTURAL FIX: T20 S8 Group 1 = India/SA/WI/Zimbabwe ONLY (old options had Australia[eliminated]/England/NZ[Group2]). India "clear favourites" defending champ 4-0 home → India .48/SA .34/WI .12/Zim .03 (constrained 4-team, India news-grounded fav).
- TW trajectory: 953(Jan26)→1317(Feb19 low)→1437(Feb21). 180/330 resolved. Strategy solid: concentrate only on confirmed/structural; wide-cap on speculative.
- FACTS: T20 S8 G1=India,SA,WI,Zimbabwe; G2=Eng,NZ,Pak,SL. India-SA Feb22 Ahmedabad (both stormed groups; India tournament fav, Abhishek Sharma 3 ducks). Australia ELIMINATED group stage (biggest shock). Olympics closed Feb22 (Norway top ~34, Italy record ~30).

## Day 61 (sim 2026-02-22) — cum TW 1425.75 (-12: 992626 Group1 1st = West Indies, not India [-11.8]. India .48 too concentrated for "1st by early DATE" — noisy standings ≠ tournament fav.)
- LESSON: "which team leads/1st by [specific early date]" = volatile (few matches); spread near-flat among 2-3 contenders, DON'T concentrate on overall favorite. WI won Grp C, was a real contender — undervalued at .12.
- 648994 Thai ammo site (no event reported): held RoyalThaiArmy .28/Police .16/ArmedForces .10 (capped, speculative).
- 654360 Brazil SE flood deaths (no Brazil flood news; all Europe storms): held MinasGerais .28/SaoPaulo .20/Rio .16/EspiritoSanto .10 (MG most flood-prone SE state; capped wide).
- FACTS: Lviv bombs = police officer killed +24 injured (terrorist act, homemade IEDs at shop break-in scene — matches 109135 Lviv). Storm Pedro battering France (35+ days rain record, Bordeaux emergency). Sertolovo HQ explosion 3 dead (876124 resolved).

## Day 62 (sim 2026-02-23) — cum TW 1452.27 (+26: 654360 Brazil flood = Minas Gerais +39.8 [well-reasoned modest fav .28 held Day1!]; 648994 Thai site = Border Patrol Police -13.2 [unlisted specific force])
- VALIDATED again: well-reasoned modest favorite (MG = most flood-prone SE Brazil, .28) held from Day1 → +40. Core winning pattern.
- Feb24 resolvers (all speculative-not-confirmed, held wide/capped per rule): 392014 Congo mass graves → Goma .25 (M23 epicenter); 726747 UK mosque axe → London .22 (largest Muslim pop; only UK mosque news = Bristol bacon, not axe); 632535 Spain WC warmup → low spread (just started 2/23, no announcement).
- FACTS: DRC — M23 holds Goma+Bukavu, famine (10M hunger), 300 farmers killed N of Goma. UK: Bristol mosque bacon hate-crime. Australia Lakemba mosque threat letters. Storm Pedro France floods (35-day rain record).
- TW trajectory healthy: 1452 (183/330 resolved). ~147 active remain (res through Mar 28).

## Day 63 (sim 2026-02-24) — cum TW 1464.00 (+12: 726747 UK mosque axe = Manchester +14.2 [had .12, wide spread held Day1]; 392014 Uvira ~0 [had .06, wide-spread protected]; Spain/Peru -2.5)
- VALIDATED: wide-spread (Manchester .12) still nets +14 when event occurs & answer listed. Uvira at .06 → ~0 (no concentration loss). Wide-cap strategy robust.
- 415069/489902 US-Iran talks venue: CONFIRMED GENEVA/Switzerland (Oman FM Albusaidi: "Geneva this Thursday"; Feb17 & Feb26 rounds both Geneva). → 415069 Switzerland .48 / 489902 Geneva .50 (news-confirmed venue → justified concentration).
- 812182 Barca midfielder hamstring: no Barca news (injuries=Loftus-Cheek jaw/Davies Bayern/Cucurella Chelsea). Held Olmo .22/Pedri .18 capped.
- 422164 university / 811321 Turkish migrant province: speculative, held wide low.
- FACTS: US-Iran — Geneva talks (Witkoff/Kushner vs Araghchi), Oman-mediated, "guiding principles" reached, Iran to submit written proposal; Trump "considering strikes"; US 2nd carrier en route, full forces by mid-March; Rubio→Netanyahu Feb28. NO war yet but escalating. Loftus-Cheek (Eng) broken jaw, months out.

## Day 64 (sim 2026-02-25) — cum TW 1432.72 (-31: 415069 Switz→Austria -27.7, 489902 Geneva→Vienna -12.5 [next-round venue ROTATED]; +422164 Columbia +9.3, +812182 deJong +9.9 [wide spreads listed answers])
- 915784 STRUCTURAL FIX: Newcastle beat Qarabag 9-3, plays BARCELONA or CHELSEA R16 (per Reuters; draw Fri 2/27). Old options PSG/Bayern/Inter all wrong → Barca .49/Chelsea .49 (clean 50/50, like prior CL structural +0.5 plays).
- 55315 FIX: Gorton&Denton NOT safe Labour — 3-way (Omnisis: Green 20/Reform 17/Labour 15, 27% undecided; Labour blocked Burnham). Old names (Western/Khan) wrong. → Goodwin(Reform) .34/Spencer(Green) .32/Stogia(Labour) .26.
- 412823 prediction-mkt-ban senator: no "ASAP" senator named (news=CFTC defending, 23-sen letter to Selig). Held Murphy .18/Merkley .16 wide.
- 661416 Yantar .18 / 131819 wide held (speculative).
- FACTS: CL R16 — Newcastle vs Barca/Chelsea; Bodo/Glimt KO'd Inter (5-2 agg!); Atletico beat Brugge; Leverkusen vs Bayern/Arsenal. Prediction markets: CFTC (Selig) defends Kalshi/Polymarket vs state bans; Trump admin backing them. Iran-US: venues rotating Oman→Geneva→Vienna(IAEA).

## Day 65 (sim 2026-02-26) — cum TW 1472.45 (+40: 412823 Murphy +28.2 [Day1 modest-top correct], 131819 Kabul +16.3 [wide-spread listed], 55315 Spencer +0.15 [late fix salvaged from neg], 915784 Barca correct +0.50 Brier but TW -1.3 late])
- 333107 FIX: T20 semis are CROSS-group (G1-1 vs G2-2, G2-1 vs G1-2). SA (G1 leader) opponent ∈ GROUP 2 {Eng,NZ,Pak,SL} ONLY. Old options India/Australia IMPOSSIBLE (India=same group; Aus eliminated). → NZ .26/SL .22/Eng .22/Pak .12.
- IRAN WAR STILL NOT STARTED (Feb26): heavy escalation — F-22 Raptors to Israeli bases (1st ever), Ford carrier at Crete en route, "highly kinetic campaign" ready, Trump "15 days to deal or unfortunate"; Saudi/UAE deny airspace. NO strikes yet. War-cluster Qs (209948,434027,815035,443306,58660 res 2/27-28) held capped ≤0.34 → likely VOID (no event) = small loss. 739634 Iran .35 held.
- FACTS: T20WC — England 1st into semis (beat Pakistan); SA top Group1 (beat India by 76 & WI by 9wkt, Markram 82*); WI also strong; India reeling (lost to SA, NRR -3.80, must-win). T20 semis ~Mar4-5, final Mar8.

## Day 66 (sim 2026-02-27) — cum TW 1584.39 (+112 HUGE: 58660 Tehran-explosions +60.4, 739634 Iran-cant-play-WC +72.1 [war started → Day1 capped Iran/Tehran .33-.35 paid massive!], 443306 Geneva +10.6, 333107 NZ +9.4; offsets 209948 Qatari-airspace -20, 815035 Minab -12, 434027 Qazvin -8.5)
- ⚡ IRAN WAR HAS BEGUN: US-Israeli joint strikes on Iran (confirmed via 443306 "talks collapsed in Geneva before joint US-Israeli strikes" + 58660 Tehran explosions + 739634 Iran out of WC all resolved TRUE). War-cluster Qs now LIVE events, not void.
- KEY VALIDATION: capped ~0.33 Tehran/Iran picks (per hardened rule) held from Day1 → +60/+72 because war happened & Tehran/Iran = correct dominant answers. The rule (cap but keep reasonable favorite) WINS big when the presupposed event occurs.
- War-cluster Feb28 updates (war-pattern, capped): 70713 US-troops-killed country = Qatar .30/Iraq .22 (Al Udeid CENTCOM HQ prime target, hit June2025); 59501 Gulf-most-hit = Qatar .37 (Al Udeid); 13213 Israeli town = Tel Aviv .26/Beersheba .16. HELD capped: 172888/635419 Iran council (Jannati ~.20), 354370 ATACMS .35, 768218 Nasrallah .30, 599755 hospital low, 80868 W.Bank village wide, 917339 conflict-name spread.
- WAR FACTS: Strikes ~Feb27. June 2025 precedent (12-day war, Op Midnight Hammer): Iran→Al Udeid Qatar; Israel hit Tehran/Fordow/Natanz/Isfahan; Iran missiles→Tel Aviv/BatYam/Beersheba/Haifa. US bases in range: AlUdeid(Qatar/CENTCOM), NSA Bahrain(5th Fleet), Camp Arifjan/Ali Al Salem(Kuwait), Prince Sultan(Saudi), Al Dhafra(UAE), Muwaffaq Salti(Jordan). Al Asad(Iraq) transferred to Iraqi control. F-22s at Israeli bases. Khamenei health/whereabouts speculation (Bayt shadow apparatus runs regime even if he's "eliminated"; son Mojtaba key). MEK clashed near Khamenei Tehran compound.

## Day 67 (sim 2026-02-28) — cum TW 1561.98 (-22: PrSM +19.5, Ghanbari@.03 +5.75, Kuwait@.10 +5, UAE@.12 +3.8 [wide-spread coverage pays]; offsets Beit Shemesh -10.5, Khamenei/Hezbollah -10.4, conflict-name -16.7)
- KHAMENEI DEAD (targeted in strikes; Hezbollah avenging him). Iran interim council member = Ayatollah Alireza Arafi (seminary head — unguessable). War specifics keep resolving to SURPRISE answers (Beit Shemesh, Minab, Qazvin, Arafi×2, Abu Falah, Gandhi Hosp) → keep capped wide, accept ~-5 to -16 modest losses, occasional low-prob hits net + (PrSM/Kuwait/UAE/Ghanbari).
- WAR DETAILS (Sat Feb28): US "Op Epic Fury" + Israel struck Tehran(Khamenei home), Isfahan(nuclear), Qom, Karaj, Kermanshah, Lorestan, Tabriz. US used TLAMs to suppress air defense. Iran retaliated: missiles at Israel + US bases UAE/Bahrain(5th Fleet HQ hit)/Qatar; Saudi confirms Riyadh+Eastern Province hit. Airspace closed Iran/Iraq/Kuwait/UAE/Bahrain/Jordan/Qatar/Saudi. Dubai airport 700 cancellations.
- Mar1 war updates: 994042 IRIB .42 (Israel targets state TV, precedent); 246419 AWS UAE .36/Bahrain .34; 453556 Germany evac UAE .26; 971319 energy Abqaiq .20 (Saudi E.Province hit). Held 560525/232393/414228 wide.

## Day 68 (sim 2026-03-01) — cum TW 1718.07 (+156 HUGE: IRIB +68.5, Bahrain-AWS +52.9, Rawalpindi +27.8, SAfrica-fruit +24.4; offsets Kuwait-F15E -11.6, RasLaffan -7)
- War-pattern favorites held from Day1 paying massive (IRIB=Israel-targets-state-TV; SAfrica citrus; Rawalpindi mil-HQ). Wide-cap strategy peak performance. TW 953(Jan26)→1718(Mar1). 221/330 resolved.
- Mar2 war updates: 656436 country Trump threatens re base-access → Saudi .30/UAE .22 (BOTH publicly refused airspace; MBS Jan statement; old Turkey-top was wrong); 297818 UAE oil emirate → Abu Dhabi .38 (ADNOC/Ruwais, AD hit); 584240 Pakistan-bring-to-talks → US .35 (main belligerent); 759458 Iran hospital city → Tehran .40 (dominant strike target, Gandhi Hosp precedent).
- WAR FACTS Mar1: Khamenei CONFIRMED KILLED ("assassination" of 86yo). Iran hit Abu Dhabi (1 civ dead debris), Dubai (Palm Jumeirah/Burj Al Arab fire, DXB airport damaged 4 injured), Doha, Manama, Riyadh, Eastern Province, Amman, Kuwait. UAE closed Tehran embassy. MBS privately urged strike but publicly refused airspace (WaPo). Trump ran war from Mar-a-Lago. Oman still mediating (Albusaidi-Vance "peace within reach"). Vienna technical talks were planned Mar2.

## Day 69 (sim 2026-03-02) — cum TW 1749.39 (+31: 584240 US +58.8 [Day1 fav held]; offsets 759458 Bushehr -14.3 [over-conc Tehran .40], 656436 Spain -10.3, 297818 Fujairah -2.9)
- LESSON: even mid-war "Iranian city" specifics surprise (Bushehr hospital, not Tehran). Cap "Tehran" ~0.32 not 0.40 for Iran-city Qs; spread incl. Bushehr/Bandar Abbas/Kermanshah.
- Mar3 updates: 68828 OpenAI $30bn CEO → Masayoshi Son .36 (SoftBank $30bn, vocal, IPO end-2026; Microsoft did NOT participate so Nadella dropped; Nvidia/Huang also $30bn .16); 937255 ship-ablaze waterway → Strait of Hormuz .32 (war chokepoint); 803012 Epstein-DOJ subpoena → Bondi .32 (AG perjury-accused over files).
- HELD: 157054 Mullin .25 (physical-confrontation history), 768526 Israel .25, 16281 "No team" .15.
- FACTS: OpenAI closed $110bn round (Amazon $50bn, SoftBank $30bn, Nvidia $30bn; Microsoft did NOT participate; IPO ~end-2026; val $730bn pre). Epstein: Bondi accused of perjury/coverup (Dems want special counsel); Clintons deposed Feb26-27 (Comer/Oversight). War ongoing.

## Day 70 (sim 2026-03-03) — cum TW 1839.91 (+90: Bondi-subpoena +48.2, Hormuz-ship +40.4, US-drone-help +12.7; offsets Sheehy -8.5, Carrick -5)
- TW 953(Jan26)→1840(Mar3). 231/330 resolved. News-grounded/war-pattern Day1 favorites = consistent big TW.
- Mar4 updates: 863162 Gulf refinery hit = SAUDI .55 (CONFIRMED Ras Tanura Aramco hit by Shahed drones Mar2); 779990 Saudi city = Riyadh .30 (US Embassy Riyadh hit, Diplomatic Qtr); 765155 embassy-evac capital → Riyadh .22/KuwaitCity .18/Baghdad .18 (Riyadh+Kuwait embassies HIT); 869392 Merkley co-sponsor = Chris Murphy .28 (THE pred-mkt crusader, won 412823); 281710 Noem-replacement trimmed Homan .14 (Noem STILL DHS sec, testifying Mar3 — likely void).
- WAR FACTS Mar3: Iran hit US Embassies Riyadh(2 drones, fire), Kuwait City, Dubai consulate. Saudi Ras Tanura refinery hit (Aramco shut). Qatar Ras Laffan+Mesaieed LNG halted (QatarEnergy). 3 US jets crashed Kuwait (friendly fire — matches 560525 Kuwait!). UAE endured 800 projectiles, considering strikes on Iran. Hezbollah fired missiles at Israel (52+ killed Lebanon, Israel ground troops S Lebanon). Israel/Pal 11 killed. Ronaldo left Saudi.

## Day 71 (sim 2026-03-04) — cum TW 1800.36 (-40: war specifics surprised again — 765155 Doha -12.5, 887402 US-military -17.6, 779990 Al-Kharj -7.7, 869392 Klobuchar -8; 863162 Bahrain +16.3 [Day1 weighting saved it despite wrong last-day Saudi .55])
- LESSON: "US DoD investigation identifies responsibility" → US self-probes often ADMIT US fault; weight investigating party's own military higher (887402=US military, I had .12). 765155 Doha (Qatar=Al Udeid warzone) — embassy-evac was Doha not Riyadh/Baghdad.
- LESSON reinforced: 863162 — last-day pivot to Saudi .55 was WRONG (Bahrain), but Day1 Bahrain-weighting still netted +16. Confirms: don't trust single-news-report last-day pivots on multi-candidate war Qs; Day-1 spread weight dominates. (Mirrors 956334/Mali earlier.)
- 483759 Trump region "would've been taken over" → HELD Middle East .30 (war-context). 871156 tornado state → HELD wide Texas/Miss/Ark/Mo/Kan (no outbreak confirmed yet).
- WAR FACTS: Noem REPLACED by Markwayne Mullin (DHS sec). US DoD blamed US military for southern Iran school strike. Bahrain refinery (Bapco/Sitra) hit. Trump cartel coalition = "Americas Counter-Cartel Coalition". 91 active, mostly war + late-March sports/politics.

## Day 72 (sim 2026-03-05) — cum TW 1839.52 (+39: 483759 Trump-region Middle East +47.6 [war-context Day1 fav]; 871156 tornado Michigan -8.4)
- 758920 Nepal PM FIX: election held Mar5; Balendra Shah(Balen, Kathmandu mayor) = FRONT-RUNNER → Balen .30/Gagan Thapa .16/Oli .14/Karki .08 (Karki was INTERIM, old pred wrongly had her top). Coalition formation unpredictable → capped .30.
- 681301 S.Lebanon district held Nabatieh .20/Tyre .16 (war-pattern wide). 893235 held Iran .32 (US initially blamed Iran for school strike before admitting own fault per 887402).
- FACTS: Nepal Gen-Z revolt (Sept2025) ousted Oli; Karki interim PM; election Mar5 (275 seats); Balen Shah front-runner, Gagan Thapa(NC), Oli contenders. Iran war ongoing. 89 active (war + late-Mar sports: CL R16, T20 final, IPL, Oscars).

## Day 73 (sim 2026-03-06) — cum TW 1929.89 (+90: 893235 Iran +46, 681301 Tyre +26.7, 758920 Balen +17.7. No losses.)
- TW 953(Jan26)→1930(Mar6). 244/330 resolved. War + news-grounded favorites = sustained huge gains.
- 578870 Beirut apt strike → Haret Hreik .26 (Israel issued displacement orders for Haret Hreik, striking Dahieh); 276362 coastal hotel → added Hazmieh .22 (confirmed Comfort Hotel strike Hazmieh/Baabda, though Q says "coastal"). 338215/830793 Oslo embassy HELD Israel .33 (no Oslo blast yet; war-pattern fav if occurs; capped).
- WAR FACTS: Hezbollah opened fire on Israel (Mar2) to avenge KHAMENEI's killing. Israel striking Beirut (Comfort Hotel Hazmieh, Haret Hreik displacement orders, S.suburbs), Baalbek (4 killed), 16 S.Lebanon towns evac. 50+ killed Lebanon since Mar2 escalation. Israel troops into S Lebanon. Tehran police stations/IRGC bases bombed (mass casualties). NYPD/US on alert for retaliation.

## Day 74 (sim 2026-03-07) — cum TW 1940.78 (+11: Oslo embassy=US (had US .14 both Qs) +7.2/+3.7, 276362 Raouche@.07 +7.5; 578870 Raouche miss -7.5)
- LESSON: BOTH Beirut Qs resolved RAOUCHE (coastal hotel + apartment ≥4). Oslo embassy = US (not Israel) — in Iran war US is ALSO prime target (US embassies hit globally), not just Israel. Don't default "Israel" for all war-attack-target Qs.
- 179817 Sri Lanka coach FIX: Jayasuriya RESIGNED (T20 WC failure); SLC negotiating FOREIGN coaches (unnamed) → Tom Moody .18/Bayliss .14/Arthur .10 (dropped Jayasuriya .30→.04). 271330 HELD Australia→Ukraine .35 (established missile aid). 309487 HELD Sumy/Kharkiv wide. 304016 HELD Wizz Air .22 (most Gulf-exposed).
- FACTS: T20WC — Pakistan KO'd (failed defending 147 vs SL); NZ + India + SA + England semis (India-England Wankhede semi). Ukraine peace talks postponed (were Abu Dhabi, now no venue — Iran war disrupted). Zelensky pro-US-strike; Iran war diverting US Patriots from Ukraine (PURL delays). Ukraine offered Gulf drone-interceptor swap.

## Day 75 (sim 2026-03-08) — cum TW 1891.64 (-49 all 4 missed: 271330 Australia→UAE -19.6 [war overrode hist Ukraine pattern], 179817 Kirsten -11, 309487 Dnipropetrovsk -10.5, 304016 AirNZ -8)
- LESSON: dominant current event (Iran war) OVERRIDES strong historical patterns. 271330: Australia→Ukraine missiles (historical) WRONG; war→Australia→UAE (Gulf ally under attack). Weight war-context branch higher even vs strong prior.
- 399040 Iran WC venue: Iran games all in US (LA/Seattle) — can't play US; → Mexico .32/Canada .30/Qatar .10 (even, no Iran statement yet). 935869 Liverpool R16 scorer trimmed (spec: needs 1-0, opp unknown, Liverpool poor form 5th PL). 605397 HELD Kataib Hezbollah .28. 932855 HELD wide.
- FACTS: 555+ killed Iran, 10 Israel, 3 US soldiers KIA, 38 other-nations. WC: Iran Grp G (Belgium/Egypt/NZ), all games US West Coast. CL R16: Man City vs Real Madrid, PSG vs Chelsea headline; Newcastle-Barca. Liverpool 5th PL, poor form (lost Wolves), barely CL spot. T20WC semis: India-England Wankhede.

## Day 76 (sim 2026-03-09) — cum TW 1903.67 (+12: 399040 Mexico +38.6; offsets 605397 Kataib Imam Ali -13.4, 932855 Taiwan -8, 935869 Lemina -5.2)
- 211346 RCB IPL opener opp: no fixture confirmed; RCB defending champs host opener Chinnaswamy. Wide: PunjabKings .16(2025-final rematch)/KKR .15/CSK .14/MI .13. 425983/807049 HELD "No player" .33-.34 (sub-brace/first-career-hat-trick rare→no-player most likely). 828811 HELD Hezbollah .34 capped (central Beirut=Dahieh). 559340 HELD CyberAv3ngers .20 wide.
- FACTS: India WON T20 World Cup (SKY captain; beat England? — SKY "led India to T20 WC glory"). RCB 2025 champs (beat Punjab final). CSK revamped. IPL 2026 starts ~mid-March. Iran war continues. 74 active (war winding-down Qs + late-Mar sports: CL R16, IPL, Oscars Mar15, AFCON-CAS).

## Day 77 (sim 2026-03-10) — cum TW 1863.27 (-40: 828811 al-Jamaa -28 [4TH Hezbollah-category disaster! cumulative Hezbollah-default ≈ -110], 425983 Kvara-sub-brace -17, 807049 Valverde-hat-trick -20; offsets 559340 Handala +17.2, 211346 SRH@.08 +7.3)
- LESSON FINAL: Hezbollah-category default = ~-110 cumulative (398988,325000,828811). Israeli "which group" attribution → answer keeps being al-Jamaa al-Islamiya/Hamas. SWEPT remaining active: NO Hezbollah/Hamas ≥0.3 left. Good.
- LESSON: CL R16 marquee matches DO produce sub-braces/hat-tricks (Kvara, Valverde) — "No player" .33 too high for high-profile knockouts; but specific scorer unpredictable. Inherent variance, accept.
- Mar11 HELD: 350082/48811 Michigan/Detroit synagogue (NO such event reported — Liege/Toronto/Bondi instead; ultra-low spreads, void-likely tiny loss); 742975 MQ-9 Reaper .34 (justified war-pattern, most-lost US aircraft); 922567 Virginia univ terror wide.
- FACTS: Antisemitic incidents global (Liege synagogue blast, Toronto synagogue shootings, Brooklyn Chabad, Bondi Beach trial Naveed Akram 15 killed). India won T20 WC. ~69 active: war-tail + late-Mar (CL R16 2nd legs, IPL, Oscars Mar15, AFCON CAS appeal Mar16, Eritrea-Eswatini Mar20).

## Day 78 (sim 2026-03-11) — cum TW 1849.95 (-13: 48811 Temple Israel@.05 +9.2 [wide-spread hit again]; 742975 KC-135 -17 [had MQ-9], 922567 ODU -5.4, 350082 ultra-low ~0)
- 169286 KC-135 base country: wide Qatar .26/Iraq .18/Saudi .16/UAE .14 (war-base specifics keep surprising; 742975=KC-135 W.Iraq). 679215 troop ship → added USS George HW Bush .20 (3rd carrier deploying; ~3500 ambiguous, also amphibs Bataan/IwoJima). HELD 214539 Iran-island wide, 857856/764041 spec wide.
- WAR FACTS Mar11: Minab school strike = US TOMAHAWK hit IRGC naval base beside school (175 dead; Trump denied, blamed Iran). US destroyed 30+ Iran warships, IRIS Shahid Bagheri drone-carrier ablaze; B-2s hit 200 targets deep Iran; Iran ballistic attacks down 90%. Iran hit Kuwait airport fuel tanks/2 border guards killed, Bahrain desalination/Bapco, Sharjah, Jebel Ali Port, Prince Sultan AB (Saudi intercepted 3 ballistic). 16 killed Gulf states. 3rd US carrier USS George HW Bush deploying (Ford+Lincoln there). France Charles de Gaulle CSG (Netherlands HNLMS Evertsen escort) defending Cyprus.

## Day 79 (sim 2026-03-12) — cum TW 1871.93 (+22: 169286 Saudi@.16 +16, 214539 Kharg@.16 +22.3 [wide-spread listed answers keep paying]; 679215 USS Tripoli -7.5, 764041 BurjQalaouiyah -4, 857856 NKorea -4.8)
- Wide-spread war strategy robust: listed answers at .16 → +16/+22; misses capped -4 to -7. Net positive even on "hard" war specifics.
- 657160 Iran-FM launch-area country → Azerbaijan .22/Iraq .20 (Iran's classic accusation targets; capped wide). 503104 Spain friendly HELD wide low (no fixture; Spain warmup=Peru earlier per 632535).
- Upcoming hi-value: 573851 AFCON CAS appeal (Mar16, Morocco .30/Senegal .26 set earlier), 506444 Australia w-AsianCup (Mar15, Aus .45). 60 active, war-tail + late-Mar.

## Day 80 (sim 2026-03-13) — cum TW 1881.02 (+9: 657160 UAE@.10 +11; 503104 Serbia -2)
- Mar14 HELD (all speculative, wide spreads OK): 196640 news-net first-face died 73 (CNN .25 — Ernie Anastos died 82 but he's NYC-local not network-first-face, no match; hold), 369030 F1 DNS Cadillac .08 wide, 581686 SOS Mediterranee .22, 833672 Hormuz-refusal Germany .22 wide.
- Pattern stable: wide-spread war/event coverage nets small positives; TW 1881, 272/330 resolved, 58 active. Loop efficient — most remaining are speculative-event Qs (capped wide per rule) + a few structural late-March (CL R16 2nd legs, IPL, Oscars Mar15, AFCON-CAS Mar16, Eritrea-Eswatini Mar20, T20-related).

## Day 81 (sim 2026-03-14) — cum TW 1891.54 (+11: 833672 Germany +33 [justified fav held Day1]; 196640 AlJazeera -10.5 [LESSON: this is an AJ question set — include Al Jazeera for "news network" Qs!], 581686 Emergency -10.5)
- META-LESSON: AJ-authored set → "which news network/outlet" Qs: weight AL JAZEERA prominently (196640=AJ).
- 506444 HELD Australia .46 (vs S.Korea AFC w-semi; strong fav but knockout variance, capped). 529060 HELD Iskander .25/Kinzhal .20 wide (Russia record air attack missile, speculative).
- TW 1892, 276/330 resolved, 54 active. Stable wide-spread strategy.

## Day 82 (sim 2026-03-15) — cum TW 1854.02 (-38: 506444 Japan -24.5 [Q premise said Australia-SKorea semi but actual=Japan beat SKorea; over-trusted premise/over-conc Aus .46], 529060 Zircon -13)
- LESSON: don't over-trust a Q's stated premise/background ("Australia and SKorea set to play") — brackets/premises shift; cap even premise-based picks, spread alternatives.
- Mar16 HELD wide (no new info): 167989 Arsenal QF opp (drew Leverkusen 1-1, bracket unclear; added Bodo/Glimt — 5-win streak surging); 573851 AFCON-CAS Morocco .28/Senegal .26 (no appeal news); 669234 Tel Aviv .25; 58520 Katz .30/Netanyahu .25; 293527 CIA .30; 219636/274734 spec low.
- FACTS: CL R16 1st legs — RM battered Man City (Valverde hat-trick), PSG beat Chelsea, Bodo/Glimt beat Sporting 3-0 (5 straight), Arsenal 1-1 Leverkusen (Havertz 89' pen, 2nd leg Mar17 London). Iran WC withdrawal threat → FIFA pondering replacement (Iraq/UAE candidates; Iraq in intercontinental playoff Mexico Mar31). Angola cancelled Iran/Jordan friendlies (ME conflict).

## Day 83 (sim 2026-03-16) — cum TW 1935.68 (+82: Katz +44.1 [justified fav Day1], Senegal-AFCON-CAS +32.8 [two-horse held Day1], Olmeca@.10 +12.4, RamatGan@.10 +9.7; offsets NCTC -11.6, Arsenal -4.9)
- 864964 Iran-strikes-avenging → Ali Khamenei .45 (JUSTIFIED concentration: Khamenei killed in US-Israeli strikes = THE Iran casus belli, multiply confirmed via 768218/893235). Was wrongly only .12.
- 676065 MN No-Kings senator HELD Tina Smith .28/Klobuchar .25 (both MN senators). 405816 WBank salon strike HELD Tulkarem/Jenin wide.
- TW 1936, 285/330 resolved, 45 active. Strong endgame. Wide-spread + justified-favorite-held-Day1 = winning combo continues.

## Day 84 (sim 2026-03-17) — cum TW 1929.73 (-6: 676065 Bernie@.10 +3.75; 864964 Ali Larijani -3.65 [Khamenei boost wrong but late→only 1-day weight, limited damage — validates "late boosts low-impact"], 405816 BeitAwwa -6)
- 666706 Chuck Norris hospitalized-state: NO death/hosp news (deaths=Anastos/Culpepper/Clark) → trimmed Texas .34→.22 (void-likely, reduce downside; if dies, Texas=his ranch).
- 512785 $8.4bn arms sale: no news; rebalanced toward F-16 operators Saudi/UAE/Egypt/Bahrain/Turkey wide.
- HELD: 724111 Zahedan .22 (Baloch checkpoint-attack zone), 388689/398208/739439 spec wide.
- FACTS: Khamenei killed Feb28 (confirmed). Ukraine sent drone-defense teams to Qatar/UAE/Saudi/Jordan-US-base (Zelensky wants $35-50bn tech/$ deal; Trump declined US help). Iran proxies/Iraq militias active. 42 active, war-tail + final-week (Oscars done? IPL, Eritrea-Eswatini Mar20-25, WC playoffs Mar31).

## Day 85 (sim 2026-03-18) — cum TW 1918.54 (-11: 398208 Taiwan@.10 +10.4, 512785 UAE@.16 +13.2 [wide-spread/F16-rebalance]; offsets 666706 Chuck Norris→Hawaii -22.5 [Day1 Texas .45 conc drained, late trim too late], 724111 Tabriz -8.8)
- FINAL LESSON CONFIRMED: Day-1 concentration on presupposed-event "where" Qs (Texas/Chuck Norris) = TW drain; late trims only ~1-day weight. Should've capped ≤0.25 from Day1 on all speculative who/where.
- Mar19 HELD (speculative, wide/capped per rule): 668257 Ramezan Sharif .30 (IRGC spokesman), 50504 BNP Paribas .25, 757234 White Helmets/Lebanese CD wide, 144493 Ecuador .22, 244043 Jerusalem wide, 655411 India .20.
- TW 1918, 294/330 resolved, 36 active. Endgame stable; wide-spread strategy holding well. Session: 953(Jan26)→1918(Mar18).

## Day 86 (sim 2026-03-19) — cum TW 1924.64 (+6: 244043 Jerusalem Old City@.10 +16.2, 668257 Naini@.12 +13.2, 655411 US-Mattala@.08 +5.9; offsets 144493 CostaRica -11.2, 50504 BankofAmerica -10.6, 757234 IranianRedCrescent -7.5)
- Wide-spread continues netting +: listed answers at .08-.12 → +6 to +16; misses capped -7 to -11.
- 217580 Sudan hospital state → North Darfur .22 (El Fasher RSF-siege epicenter). 974962 Eritrea-Eswatini venue → Asmara .26 trim (Q hints alternate-venue; Eritrea stadium issues). 427993 HELD Syria .20 (post-Assad mass graves).
- KEY FACT: CAF Appeal Board STRIPPED Senegal of AFCON 2025 title, AWARDED to Morocco (Mar17, Senegal "forfeited" final via walkout → 3-0). Senegal→CAS Lausanne appeal + corruption-probe demand. (573851 already resolved Senegal correctly.)
- TW 1924, 300/330 resolved, 30 active. Final 10 days.

## Day 87 (sim 2026-03-20) — cum TW 1894.24 (-30: all 3 missed unlisted — 217580 EastDarfur -10.5, 427993 Kenya -9.6, 974962 Meknes -10.2 [Eritrea played "home" in Morocco neutral venue, as Q hinted])
- Late-stage speculative location Qs keep resolving to unlisted surprises; wide spreads cap losses ~-10 each.
- 774274 (only Mar21 resolver) HELD Kiryat Shmona .22/Metula .14 (classic Hezbollah N.Israel rocket targets; war-pattern wide, capped).
- TW 1894, 303/330 resolved, 27 active. ~8 days left (res through Mar28). Remaining mostly speculative war-tail + a few late sports/politics.

## Day 88 (sim 2026-03-21) — cum TW 1885.00 (-9: 774274 Misgav Am [small border kibbutz] -9.2, wide spread limited)
- 120805 Trump 15-pt plan intermediary → Oman .40 (JUSTIFIED: Oman = THE consistent US-Iran mediator all war, FM Albusaidi repeatedly). Others HELD wide (581783 BBC .30, 718848 S.Leb town wide, 740952 Brazilian AF .18, 554489 NY-flight low spec).
- TW 1885, 304/330 resolved, 26 active. ~7 days left. Stable.

## Day 89 (sim 2026-03-22) — cum TW 1882.94 (-2: Khiam@.10 +15.6, ColombianAF@.12 +16.2; offsets 120805 Pakistan -19.2 [over-conc Oman; war shifted mediator to Pakistan, see 584240], 581783 Al Jazeera -13.6 [AGAIN missed AJ for "which news org" — AJ-authored set!])
- REPEAT LESSON (cost again): "which news org/network/journalists" → INCLUDE AL JAZEERA prominently (AJ-authored set: 196640, 581783 both AJ). War mediators shift (Pakistan not Oman for 120805).
- Mar23 HELD (historical-pattern/justified, IQAir report not out): 494140 Chad .30/Bangladesh .26 (IQAir perennial); 757107 Byrnihat .28 (IQAir 2024 #1 city); 262505 Qatar .35 (Taliban-mediation); 912807 Lukashenko→Russia .30; 698278 IPL/Blitzer Punjab .12 wide.
- TW 1883, 309/330 resolved, 21 active. 6 days left.

## Day 90 (sim 2026-03-23) — cum TW 1872.97 (-10: 494140 Pakistan@.18 +15.9 [wide spread paid], 262505 UAE@.13 +4.6; 757107 Loni -14.2, 912807 NKorea -12.9 [Lukashenko→NKorea surprise])
- Mar24 HELD justified favorites: 200605 Iran .33 (Australia visitor ban, war-epicenter); 240291 Russia .42 (drone FROM Russian airspace → Russia near-automatic link; structural).
- TW 1873, 314/330 resolved, 16 active. 5 days left (Mar24-28). Endgame: hold well-calibrated, advance efficiently.

## Day 91 (sim 2026-03-24) — cum TW 1904.54 (+32: 200605 Iran +57.9 [war-context justified fav held Day1]; 240291 Latvia drone→Ukraine -26.3 ["structural Russia-from-Russian-airspace" WRONG — strayed Ukrainian drone; even structural reasoning fails])
- 34927 Kosovo WC-playoff-final opp STRUCTURAL FIX: Path C = Slovakia-Kosovo(semi) + Türkiye-Romania(semi). If Kosovo advances, final opp=Türkiye/Romania ONLY (old had Slovakia=their semi foe, wrong). → Turkey .42/Romania .30.
- 534802 Italy playoff-final opp → Wales .22/Bosnia .18 (Path A; Italy likely vs N.Ireland semi, final vs Wales/Bosnia winner). 390530/953884 HELD speculative wide.
- TW 1905, 316/330 resolved, 14 active. 4 days left.

## Day 92 (sim 2026-03-25) — cum TW 1939.28 (+35: 953884 Mexico-navy +32.7, 534802 Bosnia +15.2; 34927 "Turkiye" spelling vs my "Turkey" -3 [SPELLING MISMATCH cost a win!], 390530 "Iran's government" vs "Iran" -10 [FORMAT mismatch])
- LESSON (endgame): EXACT string/spelling matters — "Turkiye" not "Turkey", "Iran's government" not "Iran". Match official/likely-reported wording.
- Mar26 HELD: 489669 Eng defender (Guehi .14 wide spec double-condition), 79608 Tehran .26 (war-pattern, trimmed per Iran-city-surprise lesson), 659262 ultra-low spec.
- TW 1939, 320/330 resolved, 10 active. 3 days left (Mar26-28).

## Day 93 (sim 2026-03-26) — cum TW 1924.34 (-15: all 3 missed capped — 489669 Ben White -4.8, 79608 Qom -10.1 [Iran-city surprise again], 659262 ultra-low ~0)
- 177801 SOUTHERN-Israel attack group → Houthis .24/Hamas .20 (southern=Houthis/Gaza, NOT Hezbollah[northern]; per Hezbollah-category lesson kept Hezbollah .08). 320138 HELD Telegram .35 (extremist-recruit app); 560679 HELD ADNOC .35 (AD dominant industrial co); 795856 HELD Hasbaya .20 (2024 journalist-strike precedent).
- TW 1924, 323/330 resolved, 7 active. 2 days left (Mar27-28). Session arc: 953(Jan26)→1924(Mar26).

## Day 94 (sim 2026-03-27) — cum TW 1938.97 (+15: 177801 Houthis +26.9 [lesson-applied rebalance: southern-Israel=Houthis not Hezbollah], 560679 EGA@.10 +5; 320138 Snapchat -9.8 [Telegram-prior failed], 795856 Jezzine -7.4)
- FINAL 3 (Mar28): 144312 Pope Leo XIV .40 (THE figure for Jerusalem all-religions/Palm Sunday — justified); 26340 Gulf power+water plant → UAE/Saudi .20 each/Bahrain .16 wide (war-pattern); 267975 Sudan aid-cutoff state → North Darfur .22 wide (El Fasher epicenter).
- SESSION COMPLETE arc: TW 953 (Jan26 low) → 1939 (Mar27), 327/330 resolved. Net huge gain via: news-grounded/structural favorites held from Day1 (+big TW), wide-capped spreads on speculative (limit losses, capture low-prob hits). Main persistent leak fixed mid-run: over-concentration on unconfirmed who/where (esp. Hezbollah-category ~-110).

## SIMULATION COMPLETE (sim 2026-03-28) — FINAL
- ALL 330/330 resolved. FINAL: accuracy 20.9%, mean Brier-skill 0.082, **TW-SCORE = 1936.73** (vs 0 = abstain; max 33000). Strongly positive.
- Last day: 26340 Kuwait@.12 +10.5; 144312 Macron (had Pope .40) -2.9 [late boost=low weight, lucky]; 267975 White Nile unlisted -9.9.
- TW arc this session: ~953 (Jan26 low, post early over-confidence) → 1937 (Mar28 final). Recovered + grew strongly.

### KEY WINNING PATTERNS (for future runs)
1. Wide 5-outcome spreads, top capped ~0.25-0.35, on speculative who/where/which-event Qs whose specific outcome ISN'T confirmed. Listed long-shots at .08-.16 still net +10..+50 TW when they hit; misses capped -5..-12.
2. Concentrate (0.45-0.75) ONLY when outcome is news-confirmed/near-deterministic OR structurally forced (set bracket/draw, decided polls, scheduled fact, unique dominant figure with specific evidence). These produced the biggest wins (+40..+72): Bangladesh Jamaat, IRIB, Indonesia-Gaza, CA SCOTUS, Saif, Tehran/Iran war-pattern, US-Pakistan, Bondi, Hormuz, AO Alcaraz, Grammy BadBunny.
3. Get breaking-cluster facts EARLY (war start, AFCON result, CL standings) — Day-1 weight dominates TW; late corrections only ~1 day.
4. When a presupposed event (Iran war) DOES occur, the held capped-favorites (Tehran/Iran/Qatar) pay massively.

### KEY LEAKS (avoid next time)
- #1 leak: Day-1 over-concentration on unconfirmed who/where (Hezbollah-category ~-110 over 3-4 Qs; Kryvyi Rih, Jagland, US-school-shooting, Novichok/epibatidine -43, Markram, Oman-venue). FIX: hard cap ≤0.35 unless confirmed/structural.
- "Which news org/network" in this AJ-authored set → ALWAYS include AL JAZEERA (missed twice: 196640, 581783).
- War context OVERRIDES historical patterns (Australia→UAE not Ukraine; mediator Pakistan not Oman).
- "Next/future venue/round" rotates — don't extrapolate the confirmed instance.
- Exact spelling/format matters ("Türkiye"≠"Turkey", "Iran's government"≠"Iran").
- Don't over-trust a Q's stated premise/background; brackets shift.
