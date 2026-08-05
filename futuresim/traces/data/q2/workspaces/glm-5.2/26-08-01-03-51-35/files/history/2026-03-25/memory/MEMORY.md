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
