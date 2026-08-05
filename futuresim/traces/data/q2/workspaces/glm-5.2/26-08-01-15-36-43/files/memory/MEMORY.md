# MEMORY — Forecasting Sim

## Status
- 2026-03-25: Submitted calibrated priors on ALL 378 questions. Sim date starts here.
- Real-world run date is 2026-08-01 but SIM date = 2026-03-25 (articles only exist for 2026-03-25).

## Key Strategy
1. ALWAYS have a forecast on every question (abstain=0; low-conf wrong ≈0.97-0.99 >> 0).
2. Report CALIBRATED beliefs (Brier is proper scoring). Don't overcommit — spread mass when unsure.
3. Daily loop: advance day → scan new articles → when an event in a question is REPORTED, lock in the actual answer at high confidence (~0.9) for huge score.
4. Earliest-resolving (April) questions carry most remaining daily weight → refine those first.

## Scoring math reminder
- Brier Skill = 1 - Σ(p_i - y_i)^2. Report true probabilities p=q to maximize EV.
- Right with p: score=1-(1-p)^2. Wrong with p: score=1-p^2. Symmetric; calibrated is optimal.

## The big scenario (US-Iran war, started 2026-02-28)
- US+Israel vs Iran. Khamenei killed; successor Mojtaba Khamenei.
- Strait of Hormuz blocked. Pakistan (Asim Munir) + Turkey (Fidan) mediating.
- Trump 15-pt ceasefire plan via Pakistan (Mar 25).
- Iran FM = Abbas Araghchi. Many questions reference this war.
- Israel ground ops in S.Lebanon, focus on Khiam.

## Refinement priorities (high-confidence-able via news once reported)
- qid 829924 (S.Lebanon town surrounded) — watch for Khiam confirmation.
- qid 660351 (country hit by 281 Iranian missiles) — Israel likely.
- qid 583783/502300 (Iran delegation leader) — Araghchi.
- All sports "first goal" q's — read match reports on the day after the match.
- Elections (Tamil Nadu DMK, West Bengal TMC, Slovenia Golob, Hungary Orban) — incumbents favored.

## Lessons
- Wrote priors to /home/user/memory/ first; the REAL persistent workspace is the lustre .../workspace/memory/. Use WS variable / absolute paths. predictions/ is a symlink (read-only, auto-recorded).
- Keep a submitted-qid checklist (memory/submitted.txt) and diff vs market.csv to catch gaps (caught 12 missing on first pass).
- Watch for answer-format nuances: some q's want TWO countries (e.g. qid 879060, 787625, 388712, 105885) — format "X and Y".

## Updates by sim-day
### 2026-03-26 (after advancing)
- Ruben Amorim SACKED as Man Utd manager (Jan 2026); Michael Carrick interim, revived team (top 3, 23pts/10). → qid 600383 updated to Carrick 0.40.
- Thomas Tuchel = England men's manager (named 35-man squad; England vs Uruguay 3/27, Japan 3/31).
- Kylian Mbappe at Real Madrid, returning from knee injury (sub last 2 games). → qid 407333 (Real Madrid goal vs Betis) Mbappe still good.
- Rodri (Man City) hinting Real Madrid move. Man City CF options: Haaland primary.
- CL final May 30 at Puskas Arena, Budapest. CL SF 1st leg Apr 28/29.
- US-Iran: Iran's 5-pt counterproposal (incl Hormuz sovereignty). No ceasefire yet. Araghchi FM. Iran naval chief Tangsiri killed by Israel (Bandar Abbas). → keep Araghchi for qid 583783/502300.
- APPROACH: March 26-31 mostly "dead" (April events not yet). Advance efficiently; focus deep research when events resolve.

### 2026-03-27
- US-Iran: Chief US negotiator = **Steve Witkoff**. Key US advisers: Rubio (SecState), JD Vance, Witkoff, Jared Kushner.
- Mediator trio = **Pakistan (lead, FM Ishaq Dar), Turkey, Egypt**. → qid 793188 updated (tour last stop: Egypt/Turkey).
- Iran lead negotiators = FM **Abbas Araghchi** + Speaker **Mohammad Ghalibaf** (both taken off Israel kill list). → qid 583783 Araghchi 0.48; qid 481741 Rubio/Witkoff.
- Iran President = **Masoud Pezeshkian**. Supreme Leader = Mojtaba Khamenei (unseen since ascending).
- US-Israel campaign = "Operation Epic Fury". Iran naval chief Tangsiri killed (Bandar Abbas).
- Iran counterproposal expected ~Mar 27 via interlocutors.
- WC playoff Path A final: Bosnia vs Italy (Wales eliminated). 
- Indonesia M7.4 quake NOT yet happened (resolves Apr 1).

### 2026-03-28
- **Iran exempted PAKISTAN** from Hormuz transit (20 Pakistani-flagged vessels, 2/day). → qid 597530 updated: Pakistan 0.52.
- Iran hardening Hormuz sovereignty in domestic law (red line). Kharg Island (90% oil exports) = Iranian existential red line; strike would trigger surge on Qatar Ras Laffan, Saudi Eastern Province, UAE Ruwais.
- Kuwait airport hit by Iranian drones; UAE (Abu Dhabi/Kezad) missile debris; Houthis launching at Israel.
- ~2000 vessels stranded; oil >$100/bbl.
- WSL: Man City women cruising to title (Miedema). Not a question.
- Indonesia quake still NOT happened. FA Cup Arsenal QF not yet played.

### 2026-03-29 (Irish Times sport guide = fixture goldmine)
FA Cup QF (wknd Apr 4-5): Man City v Liverpool; **Chelsea v Port Vale**; **Southampton v Arsenal**; West Ham v Leeds.
→ qid 327626 (Arsenal eliminated by?) = Southampton (Arsenal's QF opponent) updated 0.52.
Atletico Madrid v Barcelona (La Liga, Sat Apr 4) → confirms qid 350996 fixture.
Masters week ~Apr 9-12 (Texas Open Apr 2 precedes; Augusta Women's Amateur Apr 2-3).
Friendlies: England v Japan (Mar 31), USA v Portugal (Apr 1), Croatia v Brazil (Apr 1), Czech v Denmark WCQ (Mar 31).
Indonesia quake still NOT happened (resolves Apr 1). Meloni tour not yet clear.

## !!! CRITICAL SCORING LESSON (learned 2026-04-01, qid 398343) !!!
- Indonesia quake first-fatality city = MANADO (I had Ternate/Tobelo/Sofifi/Tidore). Brier -0.12, TW -11.77.
- THE BRIER INCLUDES THE TRUE ANSWER AS IMPLICIT p=0 OUTCOME. So if WRONG (true not in your list):
  score = 1 - [ (0-1)^2 for true answer + sum of your listed p_i^2 ] = -sum(p_i^2). NEGATIVE.
- WRONG confident guess (p=0.5) -> score -0.25. Held full question life -> TW ~ -25. VERY costly.
- WRONG diffuse guess (p=0.05 x4) -> score -0.01. Cheap.
- RIGHT confident (p=0.9) -> score +0.99. Great.
- => STRATEGY: (1) For pure guesses, allocate LOW total (~0.10-0.15 across best candidates) to cap downside.
  (2) Include the MOST PROMINENT candidate (capital/largest city, top contender) — I missed Manado.
  (3) Ramp to high confidence (0.7-0.9) ONLY when news confirms the actual answer.
  (4) Proper scoring: optimal p = true belief q. Don't over-allocate on unknowables.
- ACTION: Lower egregious over-allocations on pure-guess May/June questions opportunistically during daily passes.

### 2026-04-01
- Iran WC Group G = Belgium, Egypt, New Zealand (LA & Seattle). Iran beat Costa Rica 5-0 friendly. Sardar Azmoun OMITTED from Iran squad (expelled, disloyalty).
- Europe pushes back: France blocked Israel arms transit airspace; Italy denied Sigonella landing; Spain closed airspace. UK King Charles state visit US late April.
- UAE willing to join fight to open Hormuz. Trump: deal "irrelevant"; strikes on Isfahan/Farokhshar steel+pharma. Germany Pres Steinmeier: war illegal.
- Applied scoring lesson: lowered allocations on 8 unknowable pure-guess questions (801535,978710,773935,456839,655455,523555,356699,699330) to cap downside.
- qid 398343 resolved Manado (lost). 299105 & 776644 resolve tomorrow.

## RESOLUTION TRACKER (lessons)
- 299105 fighter F-15E CORRECT (+45.5). 776644 Chelsea Enzo (had 0.15, +15.7).
- 327626 Arsenal elim = Southampton CORRECT (+39). Framing logic (QF opponent) works.
- 350996 Barca goal = Lewandowski CORRECT (+38). Top-striker prior works.
- 77558 Meloni after Qatar = UAE CORRECT (+30).
- 597530 Hormuz exempt = IRAQ (I over-raised Pakistan to 0.72 -> -27). LESSON: news "Pakistan ships allowed" ≠ question "country exempt from ALL restrictions". Don't raise confidence on partial/tangential news. Iraq (Iran ally/neighbor) was the answer.
- 660351 281 missiles target = JORDAN (I had Israel 0.5 -> -29). LESSON: sim picks surprising specific answers; geographic defaults can miss. Spread/keep modest on "which country" incident qs.
- NET after 8 resolved: TW +99.82. Being right+confident pays huge (+38-45). Over-raising on partial news is costly.

## CALIBRATION RULES (refined)
- Raise to 0.6-0.9 ONLY when news DIRECTLY states the exact answer to the exact question.
- Otherwise keep priors modest; don't chase partial news into overconfidence.
- For "which country/location" incident qs with a specific number, the answer may be non-obvious — keep spread, cap downside.

### 2026-04-06 (big news dump 11.5k articles)
- US-Iran: "Islamabad Accord" ceasefire framework via Pakistan (Asim Munir mediating). Two-tier: immediate ceasefire + comprehensive, reopen Hormuz. Final in-person talks Islamabad. Araghchi = Iran lead (talks to Witkoff/Vance). → qid 583783 bumped Araghchi 0.60.
- Masters (Apr 9-12): Scheffler 6-1 (won '22,'24; even-yr trend), McIlroy defending champ 12-1 (back issue), Rahm 9-1, DeChambeau 12-1. No Woods(DUI)/Mickelson. My qid 893744 prior well-calibrated.
- Lebanon: expanding ground offensive; strikes on Tyre/Maaraka(killed 5)/Masnaa crossing. Khiam still focal. Pres Joseph Aoun, PM Salam.
- Resolved: Haftar=The Sentry; BCB=Tamim Iqbal; Roberts-Smith=NSW(+35.6); Japan-Vietnam counterpart=Le Minh Hung.

## Progress through 2026-04-15 (51 resolved, TW +295.87)
- STRATEGY VALIDATED: moderate spreads (0.15-0.25 across 3-5 candidates) consistently profitable — 2nd/3rd-choice hits (DOJ, ICRC, Ayuso, Maguire, Foreign Office, Albanese, Boko Haram) carry days even when top wrong.
- Sim often picks NON-OBVIOUS answers (WADA=India not China; missiles=Jordan; Hormuz=Iraq; chess=Sindarov; Spurs scorer=Mukiele defender). Spreading hedges this.
- Be PRECISE with names: "White House" not "Washington" (qid 185413 lost -7 for near-miss). "Justice Department" works for DOJ.
- Wins (~+25-35): when a candidate hits at 0.20-0.30. Losses (~-5 to -13): unknowable specifics, bounded by modest allocation.
- Keep doing: daily news scan for resolvable events (elections, matches, confirmed appointments), spread candidates, lock high-conf only on direct news.

### 2026-04-22 (TW +538.95, 75 resolved)
- F1 2026 NEW ERA: Mercedes dominant (won all 3 races). **Kimi Antonelli = championship leader** (won China+Japan, 2 in a row), George Russell 2nd (won Australia opener, -9pts). Verstappen/Red Bull struggling (hinted at quitting). McLaren not dominant. → Updated ALL F1 qids (Miami pole/winner, Canadian GP leader, Barcelona constructor, Austrian GP) to Antonelli/Russell/Mercedes top.
- Kentucky Derby field not covered in corpus; kept weak prior.
- Wins this stretch: Haaland(+51), Starmer(+42), DC Patel(+46), Lokedi(+19, researched), Yamal(+26), California(+26).
- Crossed TW +500. Strategy (spreads + timely research) strongly positive.

### Resumed 2026-05-23 (was interrupted May 15-23; sim auto-advanced, my last preds held). 231 resolved, 147 active. Cumulative TW ~+1151 (pre-interruption).
- Chelsea manager = Xabi Alonso (resolved; I had Maresca - missed).
- Mohamed SALAH leaving Liverpool (final match 5/24). Arne Slot manager, Liverpool 5th (no CL). Man Utd (Carrick) got CL qualification.
- IPL playoffs: RCB 1st, GT 2nd, SRH in eliminator (vs RR per q195361). SRH explosive (255 vs RCB, Head/Klaasen/Kishan).
- French Open: Sinner runaway fav (29-match streak, 5 Masters). Alcaraz OUT (wrist). Djokovic undercooked.
- Still strong: ~+1151 TW. Continue daily catches on World Cup (June), French Open, NBA Finals, F1.

### 2026-05-30 (TW +1441, 259 resolved, 119 active)
- US WC captain = Tim Ream (surprise; not Pulisic/Adams). Turner = GK1 (+47 researched).
- US Group D: Paraguay (6/12), Australia (6/19 Seattle), Turkiye (6/25 LA). Coach Pochettino.
- French Open: Sinner heavy fav (Alcaraz/Fils OUT). Gauff beaten by Potapova. Medvedev R1 upset by Walton.
- Remaining ~119 mostly World Cup (June) "who scores first goal" — random among forwards, keep modest spreads, catch match results day-after.
- Chelsea=Xabi Alonso. Salah left Liverpool.

## ========== FINAL RESULT (all 378 resolved) ==========
- Final TW-Score: +1835.84 | accuracy 15.1% | mean Brier skill +0.058
- Started 2026-03-25, finished 2026-06-28. Strategy delivered strongly positive score throughout.

## WHAT WORKED (lessons for future sims)
1. Cover EVERY question immediately with a calibrated prior (abstain=0 is the worst).
2. Moderate SPREADS (0.15-0.30 across 3-5 candidates) are the single biggest lever — 2nd/3rd-choice hits (DOJ, ICRC, Ayuso, Zaporizhzhia, Karachi, PNL, etc.) carried many days even when the top pick missed.
3. Daily news refinement: when an event resolves/occurs, ramp the confirmed answer to high confidence (0.4-0.6+) — big wins (Haaland +51, Clark +41 at end, Mbappe +52, Turner +47, Mindanao +31, F-15E +45, Wang Yi +48, Diaz-Canel +47, Marquez +44).
4. The Brier INCLUDES the unlisted true answer as implicit p=0 → wrong forecasts score -sum(p^2). Keep allocations LOW on pure unknowables to cap downside (Derby longshot bounded to -3.4).
5. Don't over-raise on PARTIAL/tangential news (Hormuz=Iraq not Pakistan; missiles=Jordan not Israel). Only raise when news states the EXACT answer to the EXACT question.
6. "Obvious incumbent" priors can miss (Hungary=Magyar not Orban; Iraq PM=al-Zaidi not Sudani; NBA Draft=Dybantsa not Flagg; Farrer=One Nation). Keep some hedge.
7. F1 2026 = Mercedes era (Antonelli/Russell dominant). NBA = Knicks over Spurs. Chelsea=Xabi Alonso. Salah left Liverpool.
