# Forecasting Strategy & Notes

## Session 1 (2026-03-25)
- Submitted forecasts on ALL 378 active questions (day-1 coverage established; earliest resolution 2026-04-01).
- Used parallel research subagents (general-purpose) grouped by theme to research the simulated news corpus (search_news) + real-world priors, then I submitted cleaned/renormalized forecasts (stripping "Other"/"Unknown" placeholders).
- Simulated world context: US-Israel war vs Iran (started Feb 28 2026), Strait of Hormuz blockade, Gulf state missile attacks, Pakistan/Egypt/Saudi/Turkey mediating US-Iran talks, Abbas Araghchi leading Iran's delegation, 2026 FIFA World Cup (June, USA/Canada/Mexico), Pope Leo XIV, Gukesh chess, etc.

## Key method lessons
- TW-score rewards day-1 coverage on all questions + updating as news arrives. Never leave a question "done" while active.
- Exact-match string answers: include specific candidate names; avoid generic/role-based outcomes when possible (they won't match ground truth). Where unknowable, spread probability over plausible named candidates.
- Verified sources from news corpus matter (e.g., Enzo Fernandez Chelsea apology story, Southampton-Arsenal FA Cup QF, Ferran Torres Barca top scorer, FA Cup draw).

## High-confidence calls this session (strong news evidence)
- 299105 US fighter over Iran: F-15E (F-15Es already shot down over Kuwait Mar 1)
- 327626 FA Cup: Southampton (draw confirmed)
- 776644 Chelsea midfielder: Enzo Fernandez
- 893744 Masters: Scheffler
- 988210 Kentucky Derby: low confidence (no names known)
- Iran war questions: China Hormuz exemption, Israel missiles target, Hussein talks via Pakistan

## TODO next sessions
- Recheck earliest-resolving questions (Apr 1-10) as news arrives; update.
- Watch Iran war developments (ceasefire? talks? aircraft shootdown Apr 3).
- Update each question's forecast as simulated news reveals outcomes over coming days.

## Day ~58 update (2026-05-21): Learnings after 223 resolutions
- TW deeply negative (~-2213). Root cause: these are open-ended "which specific X" scenario questions whose ground-truth strings are arbitrary and rarely in my candidate sets. Exact-string matching means even semantically-correct answers (e.g., "FCDO" vs ground truth "Foreign Office") fail to match.
- Where I DID have a clear news signal + named the exact answer, I scored big (F-15E +0.88, Enzo +0.98, Southampton +0.98, Meloni-UAE +0.70, DOJ-NFL +0.70, Starmer +0.76, Susan Collins +0.71, Alito +0.66, NBA MVP SGA +0.57, Barghouti +0.66, UAE-India oil +0.67, Leclerc 3rd, JRFU +0.70, Blanche +0.62, Bottoms +0.62, Jones +0.54, Mourinho +0.59).
- The losers are low-information scenario guesses concentrated on a plausible-but-wrong candidate (Netanyahu, Cameron, Goldman, The Sentry, NRC, Sindarov, Roelf Meyer, Many).
- Strategy for remaining ~155: keep high confidence ONLY where a strong news signal names the exact answer; otherwise spread wide. But realistically the scenario answers remain unpredictable.
- Some exact-match surprises that were in-news-but-I-missed: Cuba (Trump post-war stop, "Cuba is next" article), Bint Jbeil (vs Khiam), Canada venue for resale (Toronto Stadium), Malaysia snakes... etc.

## FINAL (2026-06-28): All 378 questions resolved
- Final results: accuracy 13.5%, brier skill -0.106, TW -3913.
- The task is fundamentally hard: open-ended "which specific X" questions whose ground-truth strings are arbitrary scenario choices. Exact-string matching punishes even semantically-correct answers ("FCDO" vs "Foreign Office", "DOJ Antitrust Division" vs "Justice Department").
- Where the news corpus clearly named the exact answer before resolution, I scored strongly: F-15E (+0.88), Enzo (+0.98), Southampton (+0.98), Meloni-UAE (+0.70), DOJ-NFL (+0.70), Starmer (+0.76), Susan Collins (+0.71), Alito (+0.66), SGA MVP (+0.57), Dybantsa (+0.86), Julia Letlow (+0.61), Mark Marquez (+0.63), Mbappe (+0.60).
- Where answers were not in the news, my plausible real-world guesses usually lost to surprising scenario picks, producing the deeply negative TW.
- Lesson for similar future tasks: hold high confidence ONLY with a confirmed news signal naming the exact string; otherwise spread wide or abstain, because a wrong concentrated guess is worse than neutrality.
