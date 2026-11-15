# Forecasting Memory — main log

## Setup
- 252 active questions in market.csv, resolving 2026-07-01 → 2026-09-30.
- Update cadence: daily. First resolutions: 2026-07-01 (344207 Jaylen Brown trade, 619176 Palestinian FA month, 659176 Khamenei funeral Russian official).
- Scoring: Brier Skill per outcome = 1 - Σ(p_i - y_i)², TW-score = sum over days/questions. Days without an active prediction count 0 → predict EVERY question EVERY day starting at open.
- **KEY MATH**: unassigned probability mass (sum < 1.0) is a valid hedge: if truth is outside my listed outcomes, penalty = Σp_i² < 1. Mass on a placeholder outcome ("Another country") is strictly worse — it always contributes p². Never submit placeholders; leave tail unassigned instead.
- None-case convention in this market's criteria: literal string "None" (see qid 903565 criteria). Multi-name answers: alphabetical, comma-separated (628038), or joined by "and" (685197).

## World state (SIMULATED — diverges from real history; verified via corpus/search 2026-06-24)
- Khamenei KILLED 2026-02-28; state funeral scheduled ~July 5-9 (HT article). New Iranian leadership unknown — VERIFY.
- US–Iran war happened in 2026, ended via interim ceasefire/MoU; Senate passed war-powers resolution 50-48 requiring approval for further action. CENTCOM clearing IRGC-laid Hormuz mines.
- Maduro REMOVED in Venezuela; first govt-opposition talks June 19 (Jorge Rodríguez vs Figuera); roadmap targets new National Electoral Council by end-2026.
- UK: Starmer RESIGNED as PM/leader June 2026; Burnham set to enter No 10 ~Jul 18. Starmer hasn't said if he'll vacate Holborn & St Pancras seat.
- Peru: Fujimori won runoff; inauguration July 28.
- Premier League 2025-26: Arsenal champions (85 pts), City 2nd (78, Guardiola gone; Mourinho now at Real Madrid), United 3rd (71, Michael Carrick manager), Forest 16th (Vitor Pereira). Man Utd open 2026-27 away at Hull City; Forest host Leeds Aug 22; Villa host Arsenal Aug 31.
- FIFA WC 2026 LIVE (48 teams): as of Jun 24, MD2 done; 7 through, 5 out. Groups known: Switzerland won B (Canada 2nd → LA side), Mexico group A? (unverified), England Group L (beat Croatia 4-2, drew Ghana), Colombia beat Congo. Iran plays Egypt game. Germany NOT verified as through (agent assumed E winner — VERIFY). Messi: 5 goals (all Argentina's) leads scoring; Mbappé 4, Haaland 4, Kane/Ronaldo 2.
- F1 2026: Kimi Antonelli leads (156 pts, 5 wins), Mercedes on every pole; Hamilton 90 (first Ferrari win Barcelona), Russell 88, Leclerc 75; Norris reigning champ but weak McLaren; Verstappen P7 with exit-clause rumors. Bahrain GP is being REPLACED (Imola favored per reporting); new Madrid ("Madring") GP debuts Sep 13.
- MotoGP 2026: Marc Marquez (Ducati) winning streak; Bezzecchi (Aprilia) leads points ~180.
- Tennis: Sinner world #1 & dominant (Alcaraz OUT with wrist injury since ~spring; return targeted North American hard swing — Cincinnati most cited). Zverev RG 2026 champ; Andreeva RG 2026 women's champ; Sabalenka #1 WTA; Rybakina AO 2026 champ; Djokovic (38-39) rusty, lost RG 3R to Fonseca; Musetti out.
- Golf: Scheffler dominant world #1. MLB: Schwarber leading HRs; Judge rib bruise. Tigers bad → Skubal trade chatter (Braves "sleeper", Dodgers).
- NBA: LeBron free agent, Lakers pole position; Giannis trade chatter w/ Celtics (Brown for Giannis scenario); Skubal→Braves per Nightengale.
- Economics: Fed rate 3.50-3.75%, Chair Kevin WARSH; inflation 4.2%; June hold 12-0. SpaceX IPO'd June 2026 $75bn (US firm). Nvidia most valuable company. US-China trade war: 10% across-board Feb 2026 tariff; China still largest bilateral deficit ($202B in 2025).
- Ukraine: Zelensky intends to replace commander Syrskii with Budanov (May TASS-sourced reports). England: McCullum STAYS through 2027 WC (ECB confirmed Mar 23) — so qid 988210 likely "None"/no successor.
- WNBA/UFC: Makhachev moved to welterweight, champ, fights Garry at UFC 330; Dern strawweight champ vs Robertson; UFC 331 card unknown (Joshua Van flyweight champ); Gaethje unified LW title upset of Topuria at "UFC Freedom 250" June 14.
- DRC Ebola: 17th outbreak declared May 15 2026, Bundibugyo strain, epicenter Ituri.
- Measles 2026: zero deaths as of mid-June; Utah epicenter (484+ cases), SC largest outbreak (997).
- Eurovision: 2026 boycotters Spain/Ireland/Netherlands/Iceland/Slovenia.
- SCO summit 2026: Bishkek Aug 31-Sep 1.
- Asian Games 2026: Aichi-Nagoya, Sep 19-Oct 4. WAFCON in Morocco Jul 26-Aug 16. CWG Glasgow Jul 23-Aug 2(? verify). Hockey WC Belgium/Netherlands Aug 15-30, Pool D = England/India/Pakistan/Wales.
- PFA PPOTY 2025-26 already reported: Bruno Fernandes (record assists, FWA award).

## Submission conventions that worked
- Agents: give strict JSON output + make them submit themselves (worked; 252/252 covered on day 1) BUT audit afterwards: 48 questions had "Another/Other X" placeholder mass (dead weight) — cleaned via resubmission. Next time: ban placeholders harder AND require sum ≤ 1.0 with tolerated undersum.
- For wide-open questions (major R2 leader, "first state to...", lottery-ish), leave 20-35% unassigned as out-of-list hedge.

## Daily workflow
1. Read market.csv for newly opened questions + approaching resolution_dates (due within ~3 days get deep re-check).
2. Grep articles/<date>/articles.jsonl (new days appear after next_day) + search_news for live topics: WC bracket (esp. after Jun 27), Wimbledon draw (Jun 29), July appointments/announcements, transfer confirmations.
3. Update predictions on ANY new evidence; each overwrite re-weights accrual from that day.
4. Re-verify these agent-sourced conclusions that matter most: WC group winners/bracket→venue mapping (questions 199448, 457239, 935518, 439898, 592683, 241292); Golden Boot leaders (201629); Wimbledon fields (985440/846335/742225).

## Files
- memory/clusters/*.json — question clusters given to research agents.
- memory/corrections_0624.json — placeholder-fix resubmissions.
- memory/question_notes.md — per-question key rationales for near-term questions.

## Day 2 log (2026-06-25) — verified updates
- WC BRACKET VERIFIED (agent cross-checked FIFA/CBS/worldcuply): TOP half → Boston QF Jul 9 (M97: groups A-F pool) + LA QF Jul 10 (W-H/RU-J, RU-K/RU-L, W-D, W-G) → Dallas SF Jul 14 (M101). BOTTOM half → Miami QF Jul 11 (W-I/RU-I/RU-E, W-A, W-L) + KC QF Jul 11 (W-J/RU-H, RU-D/RU-G, W-B, W-K) → Atlanta SF Jul 15 (M102). 3rd place Miami Jul 18; final MetLife Jul 19.
- CONFIRMED group results: A: Mexico 9pts, South Africa 2nd (Korea OUT). B: Switzerland 7, Canada 4, Bosnia 3rd-qualified, Qatar out. C: BRAZIL 7 (1st on tiebreak), Morocco 7 (2nd), Scotland out. D: USA won (Turkey out; Paraguay-Australia decides 2nd). E: Germany won (Ecuador 3rd-qualified). F (finishes Jun 26): NED 4, JPN 4, SWE 3, Tunisia out. G (Jun 27): Egypt 4, Iran 2, Belgium 2, NZ 1. H: Spain 4 (through w/ draw vs Uruguay), Uruguay 2, Cape Verde 2, Saudi 1. I (Jun 26 decider): France 6 AND Norway 6 — winner tops I, BOTH land in Miami half, collide again in R16 M91. J: Argentina 6 (1st), Austria 3, Algeria 3. K: Colombia 6 (1st), Portugal 4 (2nd), DRC 1, Uzb 0. L (Jun 27): England 4, Ghana 4, Croatia 3, Panama out.
- Golden Boot after MD3-partial: Messi 5 (18 career WC goals, passed Klose), Mbappé 4, Haaland 4, Vinicius 4, Undav/Saibari/Cunha/J.David/Manzambi 3, Kane 2, Ronaldo 2.
- GIANNIS TRADED TO MIAMI HEAT (draft night, Shams) → Brown-for-Giannis framework dead. Boston in "active trade talks with multiple teams with a sense of purpose" per Shams. New 344207: no-trade .44/GSW .20/DAL .14/Bucks .14/Heat .08.
- F1: Hamilton WON Austrian GP (momentum) → Silverstone Hamilton .25/Norris .25/Antonelli .20. Season: Antonelli leads 156 pts.
- Iran de-escalation confirmed: framework/MoU signed, oil pre-war levels, Hormuz traffic rebounding, Rubio Gulf tour selling deal, Senate REJECTED war-powers restriction Jun 25. But: Iran struck a commercial ship in Hormuz Jun 25; IRGC rejects new route. 339902 None .70→.80; 107175 None .78→.84.
- Lakers re-signed Reaves 4yr/$185M max. LeBron FA opens ~Jun 30.
- Venezuela: TWIN EARTHQUAKES Jun 24-25, 32+ killed, airport closed, state of emergency (no direct market question; context).
- US Supreme Court allows mass deportation of some Haitians/Syrians (TPS).
- Sinner Wimbledon fitness questions (RG 2R exit, medical tests) but reports full fitness; won 5 Masters titles this season, defending champ. Djokovic rusty (lost RG 3R to Fonseca). Alcaraz OUT (wrist), targeting hard swing return.
- Tomorrow priorities: WC group finales (Jun 26-27: F/G/H/I/J/L deciders) → full R32 bracket known by Jun 28; Wimbledon draw ~Jun 29 (starts Jun 29); Women's T20 WC semifinals Jun 30/Jul 2; Jul 1 resolutions (344207, 619176, 659176).
