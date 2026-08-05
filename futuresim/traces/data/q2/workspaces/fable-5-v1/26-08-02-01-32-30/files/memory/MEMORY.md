# Forecasting Memory — aljazeera2026Q2 simulation

## Setup
- Sim start: 2026-03-25. Questions resolve 2026-04-01 → 2026-06-30. 378 questions, all string-answer.
- Articles: Al Jazeera corpus, new day folder appears after next_day(). Search tool = hybrid semantic+keyword, 5 chunks.
- Scoring: Brier Skill Score, time-weighted. OPTIMAL: report calibrated probabilities on up-to-5 candidates. Any calibrated forecast has positive EV (= Σq_i² approx). ALWAYS forecast something plausible.
- Overconfidence costs: p=0.5 on a q=0.2 event loses vs p=0.2. Be calibrated.
- Questions are generated FROM future news articles (Al Jazeera). The "Question Start Date" ≈ date of source article. When sim reaches that date, search for the article to get near-certain answer, then update to high probability.

## KEY STRATEGY
1. Each day: check questions whose "Question Start Date" just passed → source article likely in corpus now → search & lock in answer at 0.85-0.97.
2. Early low-info: spread 2-5 calibrated candidates.
3. Track per-question state in memory/qnotes.md (qid, current answer, confidence, next check date).
4. Question titles contain hints (e.g., "281 missiles fired at [country]" — neighboring Gulf state).


## FINAL RETROSPECTIVE (2026-06-28)
FINAL: TW-Score 3803.28 across 378 questions (max theoretical 37,800). Accuracy 22.5%, mean BSS 0.116. ~+10 TW/question average.

WHAT WORKED (keep doing):
1. Day-1 full coverage with calibrated spreads (any calibrated forecast = positive EV; TW rewards early).
2. Daily search for source articles as question start-dates arrive; lock in 0.6-0.9 when confirmed (Southampton +99, Carrick +80 path, Enzo +80, Magyar +76, Marcos +67, Mojtaba +64, Starmer +60+62, Windows +59, Zamir +74, Baumann +70, Pena +71, India/WADA +60).
3. Hedging 2nd/3rd candidates saved dozens of misses (Collins +33, Ghalibaf +18, Ayuso +28, El Capitan +28, Russell +34).
4. Domain base rates for sports scorers (star ~0.15-0.3): Haaland +49, Mbappe +49, Salah, Lewandowski +21.
5. Meta-pattern detection: ANTI-INCUMBENT WAVE in this world (Magyar, TVK, BJP-WB, One Nation, Lahn, Platner +53, de la Espriella +37, Janeese George). Apply world-level regime priors across questions.
6. Propagating officeholder changes across all pending questions (Blanche +39 after the -21 lesson).

WHAT COST (avoid):
1. Stale training priors on officeholders (Vietnam PM -61, Germany UNSC -52, Feenstra -26).
2. Matcher strictness: 'Hamas' vs 'Qassam Brigades' -64; 'Fayyadh' vs 'Fayyad' -13; 'Laura Fernandez' vs full name -22. USE the most granular, commonly-printed form.
3. Over-concentration without source confirmation (Hormuz exemption China 0.45 vs truth Iraq -24; NATO mission Ukraine 0.6 vs Hormuz -37; AJ opponent Fury 0.55 vs journeyman -17).
4. Not re-weighting a proven 'channel person' (Ghalibaf signer -27 after he'd been the interlocutor all along).
5. Question-cluster hints under-used early (Jordan overflight -30; arms-to-Sudan -32).

## DAY LOG
- 2026-05-03: SHOCKS: TVK won Tamil Nadu (-38); BJP won West Bengal (+1 thanks to late hedge). PATTERN in this world: strong anti-incumbent waves (Hungary, TN, WB, Iraq dark-horse PM, NZ Luxon wobbling). Lean challenger in remaining elections. Sixers beat Celtics (Embiid returned). Peshawar Zalmi won PSL. Mercedes Miami 1-2 (Antonelli pole->+41, Mercedes +73). Matcher inconsistency: 'Laura Fernandez' missed vs 'Laura Fernandez Delgado' but 'John Mahama' matched 'John Dramani Mahama' - USE FULLEST NAMES.
- 2026-04-24: LESSON REINFORCED: propagate officeholder changes across ALL pending questions immediately (Blanche=acting AG missed on 846721, -21). Bondi OUT as AG. Iraq PM watch: al-Badri (7/12). Peru runoff: Keiko vs Roberto Sanchez. Hawks traded Trae Young for CJ McCollum in Jan; Kuminga on Hawks. Wolves up 2-1->G4 W (+46). Claude Mythos announced Apr 7 (Project Glasswing).
- 2026-04-06 (Day res): WINS: The Sentry +55, Tamim Iqbal +28, NSW +51. MISS: Vietnam PM = Le Minh Hung (NOT Pham Minh Chinh) -61 at 0.78. BIG LESSON: NEVER >0.6 on 'current officeholder' from training memory alone - many leaders changed in 2025-26 (Vietnam PM, Bangladesh PM=Tarique Rahman, Iran leader=Mojtaba). VERIFY VIA NEWS FIRST. TW=401.
TO VERIFY before their resolution: IDF chief (585196 Eyal Zamir?), Iraq PM (523557 Sudani?), Philippine Senate pres (138890 Sotto?), DC mayor (923435 Bowser?), Union Berlin coach, USMNT GK, Ghana coach, ADF chief (356778), BP chair, ICE director (529979 Todd Lyons still?), CJP=Cockroach Janta Party?? (740282 - what is this?), Hamas leader (Meshaal vs al-Hayya).
- 2026-04-03 (Day 8 res): WINS: Southampton +99, Lewandowski +21, Meloni->UAE +40, F-15E +27, Enzo +80, Manado +44. MISSES: Hormuz exemption = IRAQ (not China; was in Araghchi's 5-list - LESSON: with an official candidate list, spread evenly, don't over-weight the 'obvious' pick). 281 missiles = JORDAN (overflight/interception path to Israel, not the intended target - LESSON: 'fired at it' can mean transit country). TW=256.93 (8 resolved).
- 2026-03-27 (Day 3): Mojtaba Khamenei = new Supreme Leader (confirmed). Araghchi Mar 25: Hormuz passage for friendly nations incl China, Russia, India, Iraq, Pakistan; COSCO ships turned back Mar 27 anyway; Thai tanker passed; Tehran Toll Booth route. Trump: Iran letting 10 tankers out. Qatar North Field gas plant damaged by Iranian attacks. Asian Cup draw postponed (was Apr 11 Riyadh); ACL Elite Jeddah Apr 13-26 on. Hamas disarm plan: tunnels destroyed in stages (494514 Hamas 0.8). Tiger Woods DUI (out of Masters). Hodgson interim Bristol City.
- 2026-03-26 (Day 2): Enzo Fernandez confirmed (776644→0.6). Candidates field: Caruana, Nakamura, Giri, Pragg, Bluebaum, Sindarov, Wei Yi, Esipenko (starts Mar 28 Cyprus). Ghalibaf rumored US interlocutor (583783 adjusted). Chelsea out of UCL (PSG 8-2 agg); Chalobah injured ~6wks. Trump 15-pt plan delivered via Pakistan; Istanbul possible venue too; Iran wants Vance. Ghalibaf warns of island-occupation plan (669987 Abu Musa thesis ok). Kompany=Bayern coach; Bayern vs Real Madrid in UCL QF. Kane 31 goals. Mbappe knee fine, France friendlies vs Brazil/Colombia in US in late March. No Molucca quake yet — WATCH DAILY until ~Apr 1.
- 2026-03-25 (Day 1): Submitted forecasts on 368/378 questions. Skipped (revisit): 988210 Derby (late Apr), 654858 Syria ag min, 247231 SL monk, 76517 Dynasty, 625905 Syria release, 559024/217220/720539 French Open draws (~May 21), 666275 Wimbledon draw (~Jun 26), 186080 Medicare fraud name.
- Key high-confidence: 327626 Southampton (FA Cup QF draw confirmed), 190217 Hakimi, 881473 Pham Minh Chinh, 916578 Germany UNSC, 583783 Araghchi.

## WORLD STATE (as learned, update daily)
- Iran: Khamenei KILLED Feb 28 at war start. Interim council: Pezeshkian + Mohseni-Ejei + Alireza Arafi. Assembly of Experts to pick successor; Mojtaba Khamenei touted. Ghalibaf parliament speaker.
- NBA East: Tatum RETURNED Mar 6 (Achilles). Celtics strong. Hawks 9th (Mar 11), Trae Young traded away? (NAW+Dyson Daniels on Hawks). Sixers: Embiid/Maxey in and out. Knicks-Hawks R1 implies Hawks 7/8 via play-in vs Knicks 1/2.
- Hamas choosing new chief: Meshaal vs Khalil al-Hayya (Feb).
- F1: Mercedes dominant (Russell > Antonelli by 4 pts after China). McLaren/Red Bull struggling. Bahrain+Saudi GPs CANCELLED (war). Japan GP ~Mar 29 next.
- Tonga M7.6 quake Mar 24 (deep, no tsunami).
- (2026-03-25) US/Israel-Iran war ongoing since ~March 2026. First ceasefire expected April (by May 7). Pakistan mediates US-Iran talks. Strait of Hormuz restricted.
- Gaza: ceasefire w/ Hamas in place but strikes continue. Israel ground op in southern Lebanon (April) & strikes into May.
- 2026 WC groups (from questions): A: Mexico, South Africa, Czechia; B: Canada, Qatar; C: Morocco, Scotland; D: USA, Paraguay (LA, June 12); F: Netherlands (+ Japan?? no - Japan in AFC Asian Cup Q); G: Egypt; H: Sweden, Tunisia, Saudi Arabia, Uruguay; I: France, Senegal, Iraq; K: Portugal, Colombia, Uzbekistan; L: England. Opening match June 11: Mexico–South Africa (Azteca). WC opening ceremony LA June 12: Katy Perry + rapper.
- UCL semifinal: PSG vs Bayern (2nd leg May 6 in Munich). 
- El Clasico May 10 (Real hosts Barca?). Real Madrid presidential election early June 2026 (Perez contested).
- Man City: Guardiola leaving end of season. Man Utd: interim manager. Chelsea: next permanent manager TBD by May 17.
- Hungary: parliamentary election ~April 2026; new PM elected by May 13.
- Peru: presidential election April 12, 2026; Keiko Fujimori in runoff (per Q).
- Colombia: presidential first round May 31, 2026.
- Iraq: president names PM-designate by Apr 27.
- Kosovo: early parliamentary election ~June 7.
- Philippines Senate leadership vote May 2026.
- Trump visits Beijing mid-May 2026 for trade talks.
- Modi 5-nation trip May incl. Netherlands + next country.
- Pope Leo XIV: first encyclical by May 25; June 6-12 trip to Spain + Canary Islands.
