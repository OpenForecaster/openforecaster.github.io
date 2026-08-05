# Forecasting Memory — Al Jazeera 2026 Q2 simulation

## Sim date: 2026-03-25 (articles to this date). 378 open-ended questions, resolve Apr-Jun 2026.

## Day 1 (2026-03-25) — COMPLETE
- Submitted forecasts for ALL 378 questions (stored in forecasts.py / forecasts.json).
- All qids covered, all valid (≤5 outcomes, sum ≤1.0, mean sum 0.55).

## World state (from Mar 25 articles)
- **US-Iran war** "Operation Epic Fury" since Feb 28 2026 (US+Israel vs Iran).
  - Ali Khamenei killed → son **Mojtaba Khamenei** new supreme leader. Iran FM = **Abbas Araghchi**.
  - Mediators: **Pakistan (FM/Field Marshal Asim Munir)**, Turkey (FM Hakan Fidan), Oman.
  - Trump 15-pt ceasefire plan via Pakistan (Mar 25). Strait of Hormuz mined/closed; US destroyed 16 minelayers.
  - Gulf states (UAE) intercepting Iranian fire; Israel + Gulf struck. 2000+ killed, oil surging.
  - Bangladesh PM = **Tarique Rahman**.
- **Ukraine-Russia**: Ukraine drone-strikes Russian ports (Primorsk, Ust-Luga); new RU offensive; US wants Ukraine to cede Donbas; UK boarding shadow-fleet tankers; Merz (DE) says Ukraine doesn't need Taurus.
- **Football**: Salah leaving Liverpool. Mbappe (Real) torn knee. Arsenal top EPL by 7pts (quadruple). Real Madrid mgr = Xabi Alonso. CL L16: PSG-Chelsea, RMA-ManCity, Newcastle-Barca, Atletico-Spurs, Leverkusen-Arsenal, Atalanta-Bayern. Chelsea: Maresca left Jan 2026 → Liam Rosenior. Guardiola deal to 2027 (Maresca linked successor).
- **F1 2026**: Mercedes dominant (Antonelli maiden win + Russell 1-2s; Verstappen/Red Bull). Japanese GP = race 3.
- **Tennis**: Alcaraz (won AO+Qatar, 17-0, then slumped), Sinner #2, Gauff #4.
- **NBA**: Wembanyama/Spurs surging (MVP leader, 54-18). Giannis/Bucks tanking (no deadline trade, may shut down). Knicks strong (7 straight).
- **Tech**: Anthropic suing DoD re Claude use. OpenAI shutting Sora.

## Scoring reminder
Score = 1 − Σ(pᵢ−yᵢ)² − (y_missing)². Missing the true answer costs full +1 to squared error (−1 worst). → Always include best guess; concentrate when confident, spread when uncertain. TW-score is time-weighted+summed; no prediction = 0 that day.

## Per-cluster approach used
- Sports specific scorers → top 3-5 team scorers, spread.
- "Which city/state/country" unpredictable → geographic plausibility spread.
- Diplomacy/appointments → most plausible named official, spread.
- Tech → naming-convention reasoning.

## TODO for future days
- Re-read new articles each day; refine forecasts as events unfold (especially Apr-resolving questions).
- Watch for: FA Cup QF draw/result, CL results, US-Iran ceasefire specifics, election polls.
- Many name-based forecasts are low-confidence (spread thin) — refine as news identifies specific people.
- Predictions/ dir gets a file after each next_day — verify harness recorded my submissions.

## Day 2 (2026-03-26) refinements
- **Steve Witkoff** = US special envoy presenting 15-point Iran ceasefire plan. Updated 390748, 487686, 481741 → Witkoff up.
- Iran Hormuz "friendly nations" reprieve: **India** (big reprieve), **Malaysia** (passage granted), **South Korea** (coordination), China (Cosco resumes). Updated 597530 → India/Malaysia/China/SK.
- **US deploys uncrewed drone boats** in Iran conflict. Updated 965659 → unmanned surface vessel/drone boat.
- Trump pauses Iran energy strikes; pushes deadline to **April 6**. Iran rejects plan, offers counterproposal.
- **IRGC Navy Cmdr Alireza Tangsiri** killed by Israel (Hormuz blockade overseer).
- Israel took Iran FM **Araghchi** + Speaker Ghalibaf off hit list at Pakistan's request → confirms Pakistan mediation (Asim Munir).
- UAE deaths from Iran attacks = 11; UAE engaging 15 ballistic missiles. (supports UAE as missile target)
- **JD Vance** may travel to Pakistan for Iran talks.
- Djibouti: Guelleh (IOG) 6th term April 2026; opposition Daher Ahmed Farah / Omar Ali Ewado. Updated 85884.
- PSG (CL), Carlo Ancelotti = Brazil mgr, F1 Japanese GP race 3, AIADMK lists TN candidates.
- No questions resolve until April. FA Cup QFs ~March 28-30 (not yet played).

## Day 3 (2026-03-27) refinements
- **Slovenia**: dead-heat. GS (Golob) 29 seats/40 w/ allies vs SDS (Janša) 28/43 w/ allies; 46 needed. Updated 287636 → Golob 0.42, Janša 0.38 (toss-up).
- F1 Japanese GP: Mercedes (Russell/Antonelli) set practice pace (race Mar 29). Reinforces Mercedes-dominant F1 spreads.
- Miami Open: Sabalenka + Sinner chasing Sunshine Double (strong). Djokovic withdrew Monte-Carlo.
- Tiger Woods OUT of Masters (injury). Confirms golf spread (no Woods).
- Carlo Ancelotti = Brazil manager (870813 Brazil forward context).
- Kash Patel emails hacked by Iran-linked Handala group (48174 lawsuit context).
- IPL 2026 underway (RCB defending, Kohli); PSL 2026 underway (new dew rules). PCB.
- Bangladesh PM Tarique Rahman (confirmed, India ties strained).
- Slovenia done. Indonesia M7.4 quake NOT yet occurred (future event) — geographic spread stands.

## Day 4 (2026-03-28) refinements (concrete signals)
- **F1**: Antonelli POLE in Japan, Mercedes 1-2 (Russell P2); Verstappen P11 ("undriveable" Red Bull). Updated 188803, 221686, 665320, 66287 → Antonelli/Russell/Mercedes up, Verstappen/Red Bull down.
- **Tennis**: Sabalenka beat Gauff in Miami final (Sunshine Double). Updated 720539, 802784 → Sabalenka up.
- **Football**: Barcelona's Raphinha OUT for CL quarters (injury). Updated 350996, 993293 → Lewandowski/Yamal/Torres up, Raphinha dropped.
- Pakistan hosting talks w/ Saudi, Turkey, Egypt on Iran war.
- Pope Leo in Monaco (pro-poor theme) — encyclical may be poverty/economy themed (268214).
- David Sacks slams Anthropic "ruthless" amid Pentagon clash.
- MS Dhoni out IPL start (calf); RCB beat SRH in IPL opener (Kohli/Duffy); IPL 2026 underway.
- Luka Doncic suspension row (MVP at stake, 65-game rule) — keep Wembanyama MVP leader.
- Ilia Malinin 3rd straight worlds figure skating.

## Day 5 (2026-03-29) refinements
- **F1**: Antonelli WINS Japanese GP → youngest championship leader (19). Verstappen P8, mulling retirement; Red Bull uncompetitive. Updated 188803 (Antonelli 0.34), 519536 Austrian (Russell/Antonelli up, Verstappen down to 0.16).
- **MotoGP**: Bezzecchi wins US GP, "perfect start to season" → 2026 MotoGP leader. Updated 310636 (Bezzecchi 0.30), 562636 Czech (Bezzecchi 0.26).
- FA Cup QF results (weekend Mar 28-30) NOT yet found for Arsenal — QF opponent/result TBD. 327626 spread stands; NOTE Arsenal very strong (quadruple chase) so premise (Arsenal eliminated in QF) may fail ~40%.
- IPL 2026: RCB beat SRH opener; Dhoni out (calf).
- Verstappen retirement talk = Red Bull 2026 weak; Mercedes/McLaren era.

## STATUS: All 378 forecasted (day 1) + ~25 refinements through day 5. Future sessions: keep scanning new articles, refine as events resolve. Watch: FA Cup QF (327626), CL QF (PSG/Barca/Arsenal paths), US-Iran ceasefire (Witkoff/Araghchi), earliest resolves Apr 1 (Indonesia quake 398343).

## Day 6 (2026-03-30) refinements
- **Tottenham close in on Roberto De Zerbi as manager** → removed De Zerbi from Chelsea (385416): now Frank/Iraola/Potter/Glasner/McKenna.
- SpaceX IPO retail push (E*Trade); OpenAI kills Sora; Anthropic eating enterprise. Pope Leo anti-war Palm Sunday msg (encyclical likely peace theme). DeepSeek 7hr outage.
- Iran FM rejects US ceasefire; Trump threatens civilian infra. India/China tankers transiting Hormuz (reinforces 597530).
- FA Cup QF results STILL not in sim articles — likely early-April event. 327626 spread stands.
- NCAA Final Four: UConn, Illinois, Arizona, Michigan.
- France beat Colombia 3-1 (friendly). Zelensky Easter ceasefire call w/ Russia.

## Day 7 (2026-03-31)
- **398343 (Indonesia quake city) resolves TOMORROW Apr 1.** No quake news yet (event imminent). Forecast current: Ternate .24, Tobelo .18, Bitung .14, Manado .12, Tidore .10 — geographically sound (North Maluku, near Ternate/Tobelo per historical epicenters).
- Artemis II moon mission launching (crew incl Reid Wiseman cmdr) — context for 657924 (Artemis III cmdr).
- Rand Paul 50-50 on prez run. Iran exiled crown prince (Pahlavi) urges US stay course.
- Mar 31 articles sparse/local — little actionable. FA Cup QF still not in sim news.

## Day 8 (2026-04-01)
- RESOLVED 398343 → Truth Manado (I had .12, 4th). Brier +0.11, TW +10.60. Lesson in CALIBRATION.md: broad geographic spreads incl. largest regional city.
- 299105 (US fighter over Iran): F-15E Strike Eagle is Epic Fury workhorse (3 downed Mar1, 2-seat) → boosted to .52.
- 776644 (Chelsea mid apologize): Neto apologized Mar 12 → added .22; removed Jackson (forward).
- Both resolve Apr 2. Cumulative TW: 10.60.

## Day 9 (2026-04-02) — Resolutions: 299105 +0.71 (F-15E, research boost paid off huge!), 776644 +0.11 (Enzo). Cumulative TW 72.06.
- 5 resolve Apr 3: 327626 (Arsenal FA Cup — no result found, spread stands; risk Arsenal won QF), 597530 (Hormuz exempt — India/Malaysia/China/SK), 350996 (Barca-Atletico — Lewandowski/Yamal, Raphinha out), 660351 (281 missiles — Israel/UAE), 77558 (Meloni after Qatar — UAE/Saudi/Oman).
- No Apr article files crawled yet. Kept all 5 as calibrated spreads.

## Day 10 (2026-04-03) TW 89.29 (8 resolved). Misses: Southampton/Iraq/Jordan (not in lists). 
- LESSON: broaden MidEast "which country" beyond GCC+Israel → incl Iraq, Jordan, Syria, Kuwait, Egypt.
- Updated 632512 (Saudi cities), 879060 (added Jordan to missile pairs).
- 632512 resolves Apr 4. Next: Apr 5 batch (225146 Taiwan boxer, 430728, 487623, 578115).
