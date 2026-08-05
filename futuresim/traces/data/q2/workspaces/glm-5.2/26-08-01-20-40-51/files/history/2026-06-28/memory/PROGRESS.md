# Forecasting Progress Log

## Day 1: 2026-03-25 (sim)
- Submitted predictions for 375 of 378 questions.
- ABSTAINED on 3 (zero basis, negative EV to guess randomly):
  - 625905 (idx 329) — person released re Mousa al-Omar complaint
  - 186080 (idx 342) — person returned to US for $3.7bn Medicare fraud
  - 666275 (idx 378) — defeats Cameron Norrie Wimbledon R1 (draw-dependent, random)
  - Revisit these on future days once news articles accumulate.
- Strategy: calibrated 2-5 candidate distributions summing ~1.0; concentrated on best guess when confident (e.g., Pulisic captain 0.60, Hamas tunnels 0.80, Orbán PM 0.74), spread when uncertain.
- Coverage by month: April 111/111, May 149/149, June 115/118.

## Key calibration insight (IMPORTANT for future days)
Brier Skill = 1 - Σ(p_i - y_i)^2 with implicit "other" category = (1-Σp) penalized when truth not in list.
- EV of an even 5-way spread (0.20 each) is POSITIVE only if collective P(truth in list) > 0.50.
- So: only predict when candidates are genuinely informed (sports rosters, known officials, plausible geography).
- For truly unknowable specific names (random individuals, draw-dependent matchups): ABSTAIN (0) beats a random guess (~ -0.2).
- When right, concentration raises score; when wrong, concentration lowers it. Concentrate only on confident picks.

## Priority for future days
1. As April/May articles accumulate, REFINE the earliest-resolving questions (April) with real evidence.
2. Fill the 3 abstentions if evidence appears.
3. Re-check sports rosters/lineups as match days approach (injuries change scorers).
4. Watch the US-Iran ceasefire timeline — many questions depend on it (talks leader, Hormuz exemption, missile targets, seized ships).
5. Questions to revisit with news: FA Cup QF opponent (327626), Candidates chess (284263), specific officials appointed.

## Day 2: 2026-03-26 (sim) — refinements from ~10k new articles
- 597530 (Hormuz exemption): Araghchi named allowed nations = India, Pakistan, Iraq, China, Russia. Reweighted to China/India/Pakistan/Russia/Iraq.
- 583783 (Iran talks leader): Araghchi CONFIRMED leading Iran side → raised to 0.55. US envoys = Witkoff + Kushner; Oman mediates (Geneva); Asim Munir (PAK army chief, now Field Marshal) = key US-Iran link.
- 727712 (PAK visit Tehran): raised Asim Munir (key link) vs Shehbaz.
- 487623 (8pm market closing, fuel crisis): Bangladesh + Sri Lanka most active on energy closures → favored Bangladesh/Sri Lanka. (Nepal = cylinder rationing; Pakistan also relevant.)
- 430728 (16 nationals killed RU-UA): Nepal's govt publicly discusses Nepalis killed fighting for Russia → raised Nepal.
- US 15-point ceasefire plan via Pakistan; Iran missiles hitting Israel + Gulf states; Khamenei killed in Feb 28 strikes.

## FINAL RESULTS (all 378 resolved)
- Final TW-Score: -1022.19. Accuracy (top pick): 14.6%. Mean Brier skill: -0.017.
- Peak TW was ~+558 (late April) when knowable questions dominated; deep slide through May/June as unpredictable sim-specifics resolved.
- Biggest single wins (high-confidence + evidence): Marcos +77.9, Southampton +51-96, DOJ +60.9, Brazil-forest +68.3, Sindarov +0.89 daily, Blanche +0.61, Mbappe +51.2, El Capitan +27.6, Tesla +28.8, UK-tanker +51.8, Telegram +49.4, Wang Yi +48.2.
- Biggest losses: overconfident near-misses (Hamas 0.80 → truth "Qassam Brigades" -68; Pulisic 0.60 → "Tim Ream" -43; Boston-Celtics 0.78 → Philly -22).

## KEY LESSONS (for future runs)
1. Find definitive info EARLY and act on it (TW is time-weighted; late fixes only partially help). Best sources: live sports leaderboards/fields, current-official changes (Bondi fired→Blanche), opponent draws (Southampton).
2. Beware STRING/SPECIFICITY matching: "Sevastopol"≠"Sevastopol Bay", "Hamas"≠"Qassam Brigades", "Turkey"≠"Turkiye", "Windows 12"≠"Windows", "Faleh al-Fayyadh"≠"Fayyad". Use the most official/precise entity name.
3. Don't over-concentrate (>0.6) on "obvious" picks in this sim — upsets are common (Orbán lost, Pulisic not captain, Al-Dawsari not Saudi scorer, Boston knocked out). Cap favorites ~0.40-0.50; keep 4-5 candidates.
4. For truly unknowable random-name questions (a specific person with zero basis), ABSTAIN (0) beats a random 5-way spread (~ -0.2). The 3 abstentions (Norrie opponent, Medicare-fraud name, Mousa al-Omar detainee) correctly scored 0.
5. Once a fact is revealed (e.g., Ghalibaf led Iran's talks), propagate it to ALL related questions immediately (missed applying Ghalibaf to the framework-signer question).
6. Sports "first goal scorer" answers are frequently non-obvious (defenders/midfielders, subs) — a 5-forward list catches ~40%; consider adding defensive/rotational options for minnow teams.

## LESSONS LEARNED (resolutions so far: Manado, F-15E, Enzo Fernández, Southampton, Lewandowski, Iraq, Jordan, UAE)
- TW-score is TIME-WEIGHTED: holding a WRONG spread for many days then correcting late still yields negative TW (FA Cup: -7.95 despite last-day fix to Southampton at 0.82). => Find definitive info EARLY; for sports, the opponent/draw is knowable well before the match — pin it high ASAP.
- Correct picks where truth was my #1: F-15E (+0.60), Southampton (+0.96 daily), Lewandowski (+0.40), UAE-Meloni (+0.41). Spread candidates where truth was #2-3: Manado (+0.19), Enzo (+0.26).
- MISS: 281-missile target = JORDAN (I had Israel/UAE, no Jordan). Lesson: Iran targets ALL US-base-host states including Jordan (large US troop presence). Always include Jordan in Iran-missile-target candidate sets. => updated 879060 to include Israel+Jordan.
- MISS-near: Hormuz exemption = Iraq (I had Iraq at 0.12, last of the 5 named countries). The "named countries" were India/Pakistan/Iraq/China/Russia — Iraq was correct.
- STRATEGY VALIDATED: informed spread candidates + early monitoring = strongly positive cumulative TW (150.91 after 8 Qs).
- Efficient monitoring: grep articles/JSONL by keyword (semantic search returns historical noise for future events). Article dirs may rotate — use search tool when files unavailable.

## World-state facts (see WORLD_STATE.md)
US-Iran war since Feb 28 2026; Hormuz blocked; Khamenei dead; Hezbollah re-engaged Mar 2; Israel DM Katz; Pentagon Hegseth; Trump POTUS; Iran FM Araghchi; Pakistan facilitating US-Iran talks.
