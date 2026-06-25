# MEMORY — Forecasting Session Notes

## KEY ESTABLISHED FACTS (as of 2025-12-24)
- **US/Israel-Iran war ONGOING since mid-2025.** Al Jazeera (2025-06-23): Israel struck Iran a day before 6th round of Iran-US talks; "US bombed three key nuclear facilities in Iran." → March-2026 questions describe an ESCALATING regional war (strikes on Iranian cities/hospitals/oil, Iranian retaliation on Israel/Tel Aviv, Gulf oil facilities hit, F-15s shot down, HIMARS, Strait of Hormuz). Treat the war arc as the base scenario. Questions: many "which Iranian city/hospital/facility hit" — I leaned Tehran/Isfahan/Natanz/Fordow/Tabriz.
- **AFCON 2025** (Morocco, Dec 21 2025–Jan 18 2026). Groups: A=Morocco,Mali,Zambia,Comoros | B=Egypt,SouthAfrica,Angola,Zimbabwe | C=Nigeria,Tunisia,Uganda,Tanzania | D=Senegal,DR Congo,Benin,Botswana | E=Algeria,Burkina Faso,EqGuinea,Sudan | F=Ivory Coast,Cameroon,Gabon,Mozambique. R16 Jan 3-6, QF Jan 9-10, SF Jan 14, Final Jan 18 (Rabat). Some Qs presume Morocco-QF-vs-Cameroon & Morocco-vs-Senegal final.
- **Grammys 2026** (Feb 1). AOTY noms: Kendrick Lamar(GNX, 9 noms, frontrunner), Lady Gaga(Mayhem), Sabrina Carpenter, Bad Bunny, Tyler/Clipse/Justin Bieber/Leon Thomas. → Kendrick ~0.46.
- **Oscars 98th** (March 2026, noms late Jan 2026, 2025 films). Weak data. A Q presumes a film gets record 16 noms — suspicious/uncertain. Low confidence spread.
- **Syria**: Assad fell Dec 8 2024. Interim Pres Ahmed al-Sharaa (ex-HTS). Govt formed Mar 2025: FM Assaad al-Shaibani, Def Murhaf Abu Qasra, Interior Anas Khattab, +Hind Kabawat, Raed al-Saleh(White Helmets). SDF deal signed. Qs: national holiday, national language (guessed Kurdish/Syriac), armed-group ops near Aleppo (SDF/SNA/PKK).
- **Ukraine**: Rustem Umerov = defence minister (since Sep 2023). Mid-2025 reshuffle talk: Umerov maybe → ambassador Washington; Svyrydenko PM. Zelensky questions → Umerov may stay or be replaced.
- **Thailand** snap election Feb 8 2026. NIDA poll Qs → Pheu Thai party-list lead; PM pref → Paetongtarn Shinawatra (Pita/People's Party 2nd).
- **Chelsea**: Enzo Maresca (5-yr deal, Jun 2024) still coach. "Next permanent" Q implies possible sacking — low conf.
- **Man Utd**: Ruben Amorim (appointed late 2024) → derby Jan 17.
- **Trump Commerce Sec**: Howard Lutnick. (Epstein correspondence Q → Lutnick.)

## CALIBRATION / STRATEGY
- 330 open-ended string Qs, resolve Jan 1–Mar 28 2026. News arrives 1 day/call via next_day.
- Many Qs presume a specific event (e.g. "Morocco vs Senegal final", "film with 16 noms", "Karachi biggest fire"). Treat premise as likely-true in sim, pick most likely specific.
- Approach: ~0.20-0.46 on favorite, spread across 4 alts, sums ≤1.0.
- TW-score weights earliest days most → getting all 330 in on Day 1 (done) is max-value.
- Daily: scan new articles, update resolving-soon Qs and Qs where news changes odds.

## DAY-1 SUBMISSIONS
- final_preds.json holds all 330 (also preds_day1.py / preds_day1b.py in /workspace).
- predictions/2025-12-24.json should appear after next_day.

## HIGH-CONFIDENCE PICKS (my best edges)
- 946810 Grammy AOTY = Kendrick Lamar
- 176447 Epstein/Commerce Sec = Howard Lutnick
- 291796 Nipah = Kerala
- 68828 OpenAI $30bn = Satya Nadella
- 946810, 180958 (SB: Detroit Lions lean), 994042 (Al Jazeera HQ struck)
- 787699 Pheu Thai; 934187 Paetongtarn; 666021 Ethiopia; 783773 Ethiopia
- 320138 Telegram (recruitment app); 988168 Instagram (ban)

## TODO NEXT DAYS
- Re-search Oscars 2026 most-nominated film once precursor data arrives (late Dec/Jan).
- Watch AFCON results (daily) to sharpen QF/SF/final + injury/penalty Qs.
- Update Australia Open tennis Qs once draw posted (mid-Jan) & results.
- Track the Iran-war arc: specific cities/facilities named in articles.
- Champions League playoff draw (Jan 30) → Real Madrid/Benfica/Juventus/Newcastle Qs.

## DAY 2 (2025-12-25) updates
- 165622 Chelsea: Maresca under "intense scrutiny" (Sky Sports Dec 15) - cryptic comments, Carragher says he won't last. Updated to favor replacements: De Zerbi 0.20, McKenna 0.17, Thomas Frank 0.16, Potter 0.15, Maresca 0.14. (Chelsea won Conf League + Club World Cup 2025, in UCL 25-26, lost to Atalanta - has credit, so not a lock to be sacked.)
- AFCON Dec-24 results not yet in news; bracket still as expected. Re-check daily for Morocco/injury/penalty Qs.

## DAY 3 (2025-12-26)
- AFCON matchday-2 underway (Morocco v Mali etc Dec 26). Dec-24 scores still not in search results. Bracket not set until ~Jan 6 — defer AFCON-injury/SF/penalty updates until R16/QF known.
- Measles (93950): Texas outbreak already >185 by mid-2025 (grew to ~750). "Exactly 185" likely a different state, but no data on which. Kept Texas lead but low confidence; revisit if a state-level 2025-26 outbreak story appears.
- No decisive evidence shifts today; keeping baseline. Strategy: on quiet days, keep predictions & advance; update when specific events resolve (AFCON bracket Jan 6, UCL draw Jan 30, tennis draws mid-Jan, Iran incidents).

## DAY 5 (2025-12-28)
- BREAKING: Israel recognized Somaliland (Dec 26-28); Somalia + African bodies condemn; Somalia demands Israel withdraw recognition. → Updated:
  - 783773 (Somalia says who supports separatist regions) → ISRAEL 0.58
  - 666021 (Somalia severs all agreements with) → ISRAEL 0.55
- AFCON: Senegal drew DR Congo (Mane equalizer); Nigeria & Algeria reached knockouts; Mozambique first-ever win. Group stage winding down; bracket set ~Jan 6.
- Also: US/Trump airstrikes on ISIS in Nigeria (Christmas Day); Trump-Zelenskyy meeting upcoming.

## DAY 6 (2025-12-29)
- Nepal: "former rapper" + Gen-Z alliance running for PM in upcoming elections (q758920 resolves Mar 27). Identify the candidate later; traditional leaders (Oli/Deuba/Dahal) may be challenged. Revisit closer to date.
- US struck a "drug boat facility" inside Venezuela (Trump, Dec 29) — rising US-Venezuela tension; could make interim-president scenario (651727) more likely but not resolved. Keep González/Machado.
- Measles exposure at Newark airport (NJ) — not the 185-case state.
- No Charlotte NYE attack yet (NYE is Dec 31).

## DAY 7 (2025-12-30)
- Oreshnik missiles deployed to Belarus & entered active service (Putin). Raises stakes for 836984 but no city named.
- Anthony Joshua: friends killed in fatal car crash; AJ himself apparently OK. Wild card for Fury opponent (465445) — keep Joshua lead.
- No Charlotte NYE attack reported yet (NYE Dec 31).

## DAY 8 (2025-12-31) — 5 Qs resolve tomorrow Jan 1
- 165622 Chelsea: Maresca still in charge Dec 31 (2-2 Bournemouth, "pressure rises") but not sacked. Kept replacement-favored spread (De Zerbi/McKenna/Frank/Potter/Maresca).
- 628026 Charlotte: foiled NYE plot was LA (Turtle Island Liberation Front), NOT Charlotte. No Charlotte plot reported. Kept Concord/Gastonia/Huntersville spread.
- 892867 Austrian skier: crashes so far are SWISS (Gisin, Suter, Gut-Behrami). No Austrian crash reported. Kept Schwarz/Kriechmayr/Feller.
- 227432 Ukraine def min: no reshuffle news. Kept Umerov lead.
- 93950 measles: airport exposures only; no state at 185. Kept Texas lead (sim likely uses canonical Texas outbreak).

## *** CRITICAL SCORING INSIGHT (learned from first 5 resolutions, 2026-01-01) ***
The 5 resolved Qs ALL MISSED (truths: Rosenior, Fedorov, Mint Hill, K.Liensberger, S.Carolina).
Brier = 1 - Σ(p_i - y_i)^2 where the TRUE (unlisted) answer contributes (0-1)^2 = 1.
=> If I MISS the truth: Brier = -Σ(my probs^2). Always NEGATIVE.
=> My v1 forecasts (sum ~0.85, concentrated) gave ~-0.15 per miss.
=> OPTIMAL total mass to put on my 5 outcomes ≈ q = P(my set contains truth).
   For unknowable specifics, q ~ 0.15-0.20 => put ONLY ~0.16 total mass (each ~0.03-0.06).
   For genuine edges (Kendrick, Kerala, Israel/Somalia, Lutnick/Ross), concentrate.
==> RECENTERED: Tier C (guessing) -> sum ~0.16; Tier B (mild) -> ~0.35; Tier A -> concentrated.
   This converts -0.15 misses into -0.03 misses. v2 forecasts now live on all 325 active Qs.

## Also learned: the SIM picks LESS-OBVIOUS answers (Rosenior not De Zerbi; Fedorov not Umerov; Mint Hill not Concord; female skier Liensberger; S.Carolina not Texas). So:
  - Don't restrict to obvious category (skiers: include WOMEN; coaches: consider less-famous names).
  - "Exactly N" number clues point to non-obvious cases (S.Carolina for 185, not Texas).
  - Outcome sets likely DON'T contain truth for most Qs -> thinning is correct.

## Resolved truths so far: Chelsea=Rosenior, UkraineDefMin=Fedorov, Charlotte=Mint Hill, AustrianSkier=Katharina Liensberger, Measles=South Carolina.

## PROGRESS (through 2026-01-07): Cumulative TW = +65.94 (climbing from -78 low).
Resolved hits: Rubio(Greenland)+51, Board of Peace+41, SDF(Syria)+30, State Dept/WhiteHouse+40, Parchin+15, Bangladesh+13, Morocco injury+9, Algeria+6, ICE+0.22.
Misses all ~-0.01 (thinning working): USA-WC, Minnesota, Carney-Qatar, Arctic Sentry, Venezuela, Starlink, Freeland, Charlotte, measles, etc.
STRATEGY CONFIRMED: concentrate Tier A/B on real edges; thin Tier C to ~0.16. Keep multiple plausible options even when favoring one (White House as 2nd pick saved +40).
Sim patterns: picks non-obvious/cross-national/regime-internal answers; "exactly N" clues → non-canonical; female skiers; Venezuela/Minnesota/USA-WC surprises.

## DAY ~15 (2026-01-09): BIG — Iran nationwide uprising/protests (Pahlavi: regime "collapsing"; protesters taking cities; 45+ dead; internet blackout; Khamenei defiant; Trump/Graham threats). Relevant to many Iran Qs (69214 province, March-war cluster). Track.
- AFCON bracket confirmed: QF = Mali-Senegal, Cameroon-Morocco, Algeria-Nigeria, Egypt-IvoryCoast. Morocco SF = vs Nigeria (Nigeria won Algeria QF). Final premise Morocco-Senegal.
- Bracket logic = strong tool for tournament Qs.

## DAY ~17 (2026-01-11): TW=+55.97.
- Somalia Qs BOTH = UAE (not Israel!). UAE backs Somaliland too (Berbera port). I over-concentrated Israel 0.45 -> -0.14 & -0.11. LESSON: hedge alternatives even w/ strong signal (Israel AND UAE both plausible). 
- Nipah=West Bengal (not Kerala) earlier. PATTERN: sim subverts strong expectations. => CAP favorites at ~0.20-0.25 max. Trimmed Kendrick 0.44->0.26, ManCity 0.36->0.24, Nadella 0.34->0.22, Ross 0.32->0.22.
- Hits this batch: Iran(BRICS)+18.9, ManUtd Carrick(2nd)+4, Syria PKK(3rd/4th)+8.8/+8.9. Keeping alt options saves scores.
- Iran nationwide uprising continues. AFCON: Morocco beat Cameroon, SF vs Nigeria (Nigeria won QF). 

## DAY ~25 (2026-01-31): TW=+165.31. 122 resolved.
- Alcaraz AO (concentrated on 2 finalists) +20.83. Lutnick/Epstein +36.54 earlier. Burkina Faso +17. 
- *** GRAMMY = BAD BUNNY (not Kendrick!) *** Even my strongest real-world frontrunner was subverted. -12.05. DEFINITIVE: the SIM DEVIATES from real-world likelihood. Do NOT concentrate on "obvious/real-world frontrunner." 
- NEW RULE going forward: thin everything aggressively; ONLY concentrate on (a) genuine 2-way structural/definitional questions (Lutnick/Ross; SB Patriots/Seahawks), (b) bracket-determined matchups (2 finalists). Everything else: thin ~0.10-0.15.
- Remaining concentrated OK: 180958 (Patriots/Seahawks = actual 2 SB reps, legitimate 2-way).

## FINAL (2026-03-28): ALL 330 RESOLVED. TW = +475.30 (simulation complete).
- Coverage: ground truth was in my option set 30.3% of the time (100/330). Top-pick correct 8.2% (27/330).
- Trajectory: started -78 (over-concentrated v1) -> recalibrated to thin -> climbed to +475.
- KEY WINNING STRATEGY (validated across 330 questions):
  1. The Brier penalty for missing the true answer = -Σ(prob²). So THIN low-confidence forecasts (total mass ~0.12-0.16 over 5 options). Caps miss damage at ~-0.03.
  2. This sim SUBVERTS real-world frontrunners (~70% of "obvious" picks were wrong: Grammy=Badbunny not Kendrick, Nipah=W.Bengal not Kerala, Navalny=epibatidine not Novichok, Somalia=UAE not Israel). NEVER concentrate on "obvious/real-world likely."
  3. CONCENTRATE only on: (a) genuine 2-way definitional (Commerce Sec = Ross or Lutnick; SB = 2 actual reps), (b) bracket-determined (2 tournament finalists), (c) directly-named breaking news (capped ~0.15-0.20, since even these sometimes fail).
  4. KEEP MULTIPLE plausible alternatives — many hits came from 2nd-5th picks (Lutnick 2nd +36, Rubio 1st +51, Hamas 2nd +11, US-military 2nd +19, Jensen Huang added late +saved, etc.).
  5. Watch for miscategorization (read question carefully: "Gulf energy" ≠ Israeli cities; skier ≠ Gulf; AI tool ≠ country; player name ≠ country).
  6. Exact name precision matters (Betar/Betar US, Nowruz/Newroz, Yotova/Iotova, Dena/IRIS Dena) — use full official forms when known; thinning keeps these cheap when wrong.
- The recalibration on day ~9 (after first 5 misses revealed the scoring) was THE pivotal decision, worth hundreds of TW points.
