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
