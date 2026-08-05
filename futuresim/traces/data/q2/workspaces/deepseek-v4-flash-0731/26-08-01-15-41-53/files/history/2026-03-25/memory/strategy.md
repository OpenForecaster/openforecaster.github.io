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
