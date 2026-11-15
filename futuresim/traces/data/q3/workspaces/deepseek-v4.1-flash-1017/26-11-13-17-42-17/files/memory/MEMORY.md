# MEMORY — Forecasting Simulation (started 2026-06-24)

## Strategy / workflow
- 252 active questions, all resolve July–Sept 2026. TW-score rewards having a prediction on every question every day; never leave a qid without a prediction.
- Workflow each day:
  1. Read market.csv, check for newly resolved questions (is_resolved) and any new questions.
  2. Update forecasts for questions resolving soonest / with fresh news (search_news, to_date=today).
  3. Spawn research subagents for batches needing re-research; submit updates.
  4. Save results to memory/results/<batch>.json and note lessons here.
- Batch files in memory/batches/; agent instructions in memory/AGENT_INSTRUCTIONS.md; results in memory/results/.
- Submit via mcp__forecast__submit_forecasts (one qid per call). Max 5 outcomes; probabilities ≤ 1.0.

## World state as of 2026-06-24 (key facts learned)
- **NBA**: 2026 Finals: Knicks beat Spurs 4-1 (June 13); Finals MVP Jalen Brunson. Giannis traded to Heat (June 22); Celtics offered Jaylen Brown + 2 firsts for Giannis (declined). NBA draft June 23-24. LeBron is UFA; Lakers favored.
- **FIFA World Cup 2026** (June 11–July 19): group stage ending June 24-26. Group winners so far: Mexico (A), Switzerland (B), USA (D), Germany (E). France, Norway advanced (I); Argentina (J); Colombia (K). Favorites per odds: France +375, Spain/England +550, Argentina +650, Brazil +900. Messi 5 goals, Mbappe/Haaland 4.
- **F1 2026**: Kimi Antonelli (Mercedes) leads 156 pts, 5 wins in 7 races; Hamilton 115, Russell 106, Leclerc 75, Norris 73, Piastri 68, Verstappen 55. Bahrain & Saudi GPs cancelled (Iran war); replacement venue TBD. MotoGP: Bezzecchi leads 180, Martin 172.
- **Tennis 2026**: Alcaraz won AO (beat Djokovic), Rybakina won women's AO; Zverev won RG (beat Cobolli), Andreeva won women's RG. Sinner #1 ATP; Alcaraz out with wrist injury (since mid-April, missing grass season). Wimbledon June 29–July 12: Sinner heavy favorite; women's open (Sabalenka #1 seed, Rybakina #2, Swiatek defending).
- **Cricket**: Women's T20 WC (England, June 12–July 5): Australia 4-0, England strong; final July 5 Lord's. England-India T20 series in July: India favored.
- **UK politics**: Starmer resigned as Labour leader/PM June 22; Labour leadership process starts July 9; Burnham (won Makerfield June 18) frontrunner. Badenoch strengthened (Tories won Aberdeen South June 18). Farage under Standards investigation over £5m gift (may face suspension/recall). SNP: Swinney FM.
- **Iran/Geopolitics**: Khamenei assassinated Feb 28, 2026 (US-Israeli strike); state funeral July 4-9 (Tehran/Qom/Mashhad). US-Iran MoU/ceasefire fragile. Gulf states hit by Iranian attacks. Venezuela: Maduro removed; US-backed talks began June 18-19.
- **Fed**: June 17 FOMC held 12-0, hawkish dot plot; July 29 meeting. Dissenters: Logan, Miran, Hammack, Kashkari mentioned.
- **Weather**: Typhoons Bavi/Noul/Dolphin not yet formed as of June 24 (base rates only).
- **Dugan**: sentencing July 8 (Judge Adelman, ED Wis.); max 5 yrs; probation/prison possible.
- **Other**: NY passed first statewide data-center moratorium (June 4, awaiting Hochul); Switzerland Beznau nuclear output halved June 23 due to Aare temp (drought); largest US IPO by foreign firm still Alibaba; Nvidia ~$5T most valuable.

## Lessons / calibration notes
- Search tool has rich simulated 2026 corpus including Wikipedia snapshots; very useful for schedules/standings.
- Subagents (general-purpose) can use mcp__forecast__search_news and write JSON results — efficient for batches of ~10-15 questions.
- Watch for conditional questions ("If X leaves...") — question may resolve void; still predict the most likely real outcome.
- Answer naming should follow the resolution criteria (full names, full team names).
- Re-check questions daily as events (World Cup, WT20, Wimbledon) resolve — update probabilities with results.

## Questions to watch (earliest resolutions)
- Jul 1: 344207 (Jaylen Brown trade), 619176 (PFA restart month), 659176 (Russian official at Khamenei funeral)
- Jul 4: 177324 (Trey Alexander two-way), 633052 (cyclospora state)
- Jul 5: 258607/799550 (WT20 winner/POTM), 747581 (British GP)
- Jul 7: 263626 (US trade deficit country), 754639 (UK party leader by-election)
- Jul 8: 213487 (Dugan sentence), 76066 (Moldova PM)
- Jul 9: 107473 (UK university), 199448 (WC Boston QF), 279946 (IPO record), 562262 (England-India T20)
- Jul 10: 446236 (Bavi evacuations), 985440 (Wimbledon first finalist)

## CALIBRATION RULES (distilled 2026-08-28, after 166 resolutions)
Scoring recap: Brier = 1 - sum over SUBMITTED outcomes of (p_i - y_i)^2; an unlisted correct answer counts as p=0,y=1. Reporting true beliefs is optimal; when wrong the penalty is sum(p_i^2). TW-score sums daily Brier across all questions.

HARD RULES learned the hard way:
1. NEVER 0.95+ on an elderly public figure's survival/health without checking the last 48h of news. Cap at ~0.90 same-week, ~0.85 multi-week. (Harald V died/abdicated before Aug 29 — I had .97.)
2. Re-read the EXACT resolution criteria before finalising any high-confidence number. 921981 asked for Putin's counterpart for talks *on the Ukraine war* — the answer was mediator Erdogan, not an SCO head of state.
3. For "next port call"/deployment questions, include the whole plausible theatre: Gulf states AND Southeast/East Asia (Thailand, Singapore, Japan, Philippines, South Korea) AND home ports.
4. For transfers: ALWAYS include Al Hilal / Al-Nassr / Al-Ittihad for PL players late-20s with reduced roles (Watkins and Martinelli both went to Al Hilal and I missed both initially). Also weight "no deal yet" heavily when the question resolves BEFORE deadline day — verbal agreements routinely slip.
5. For tournaments: re-check at the semifinal stage. Pre-tournament lists are often 4-for-4 wrong by then (Cincinnati men and women both).
6. For US primaries: cap the money/national-profile favourite at ~0.65-0.70 (Vindman .78 lost to Nixon).
7. For "which armed group will the US designate as an Iranian proxy": always include Hezbollah.
8. For "first X to call for Y" political questions: consider the digitally-active ministers, not just the famous opposition figures (Ukraine: Fedorov, not Kuleba).
9. When a question may resolve VOID before the underlying event completes, moderate concentration to ~0.6-0.75 (Savinho de-concentration from .88 to .72 gained +97 TW).
10. Use 5 outcomes when a research list contains a plausible dark horse — dropping Mike Rogers from the AIPAC list cost a miss.
