# Context: Al Jazeera 2026 Q2 Forecasting Market (378 questions)

## Date / state
- Sim "today" started 2026-03-25. Questions resolve 2026-04-01 → 2026-06-28.
- Day 1 (2026-03-25): submitted calibrated predictions on ALL 378 questions. predictions_today.json has the master set.
- Update daily as new articles arrive in articles/YYYY/MM/DD/.

## Key real-world backdrop (from news search, as of 2026-03)
- **US-Iran WAR active** since Feb 28, 2026 ("Operation True Promise 4"). US+Israel vs Iran.
  - ~700 missiles + 3,600 drones fired by mid-March. Strait of Hormuz tensions. Qatar (Al Udeid) & Dubai targeted.
  - Many questions assume an April 2026 ceasefire + US-Iran talks (mediator Oman; Iran FM Abbas Araghchi leads delegation).
  - Iran negotiator: Araghchi (FM) primary, Ali Bagheri Kani deputy.
- **2026 FIFA World Cup**: June 11 – July 19, 2026, USA/Canada/Mexico. 48 teams, 12 groups. Opens Mexico City (Azteca), final MetLife NJ. Group letter refs in questions (A=Mexico, etc).
- **F1 2026**: new regs. Lineups: McLaren(Norris/Piastri), Mercedes(Russell/Antonelli), Red Bull(Verstappen/Hadjar), Ferrari(Leclerc/Hamilton). Cadillac joins. McLaren likely strong.
- **NBA 2025-26**: MVP favorites SGA (Gilgeous-Alexander, Thunder), Jokic, Doncic, Giannis. OKC Thunder strong (SGA). Draft 2026 #1: AJ Dybantsa favorite.
- F1 calendar from search: Miami May 2-4, Spain May 30-Jun1, Canada Jun13-15, Austria Jun27-29. (Note: questions' GP dates sometimes differ — sim may use own calendar.)

## High-confidence anchors I used (verify with later news)
- USA WC captain: Pulisic. GK: Matt Turner.
- Syria FM: Asaad al-Shibani. Iran FM: Abbas Araghchi.
- Golgi/leadership for many is genuinely uncertain in 2026 — treat hedges as reasonable.

## Scoring reminder (see STRATEGY.md)
- Submit on EVERY question every day (blank=0, hedged guess≈+0.8 even if wrong).
- Cap single-outcome conf ~0.3-0.5. Spread 3-5 outcomes. Leave residual (sum<1).
- Daily priority: (1) maintain coverage, (2) update questions where new articles reveal evidence, especially earliest-resolving ones.

## Process notes
- make_preds.py builds the dict P; predictions_today.json is the exported clean version.
- Submit via mcp__forecast__submit_forecasts (one qid per call, ~35-70 parallel per turn).

## 2026-03-26 daily scan notes
- **Q597530 (Hormuz exemption country) -> UPDATED to South Korea 0.55.** Strong evidence: Iran envoy calls South Korea "non-hostile country," signals conditional vessel access. Big win vs original China guess.
- **Q368203 (Hungary PM) -> Orban 0.50.** Orban governing; Tisza/Magyar in opposition.
- US-Iran: ceasefire plan "reviewed" by Iran; Trump urging action. Oman mediates; Araghchi leads Iran side; US envoys Witkoff(+Kushner). Supports Oman(Q384398), Araghchi(Q583783,Q502300).
- Chess Candidates 2026 underway (challenges Gukesh, Q284263). "Old guard" -> watch Ding Liren/Caruana/Nakamura.
- F1: Norris says "McLaren best car" -> supports McLaren/Norris. NBA: OKC Thunder & Celtics strong -> supports Thunder(SGA). India fuel crisis emerging -> watch Q487623 (8pm closing, maybe India).
- Spain to face Peru in final WC warm-up (Mexico) -> Q812233 opponent Peru.
- Senegal AFCON title stripped -> Morocco (CAS pending). Context only.

## IMPORTANT: cwd note
- Bash working dir PERSISTS between calls. Use ABSOLUTE paths or `cd <abs>` to avoid drift after cd into articles/.
