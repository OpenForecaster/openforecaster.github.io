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
