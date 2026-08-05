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

## DAY LOG
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
