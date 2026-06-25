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
