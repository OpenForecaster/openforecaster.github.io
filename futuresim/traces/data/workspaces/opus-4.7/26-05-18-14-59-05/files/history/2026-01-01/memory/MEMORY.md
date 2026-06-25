# FORECASTING MEMORY

## SETUP
- Sim start: 2025-12-24. 330 questions, all string-type, resolve 2026-01-01..2026-03-28.
- Daily updates. TW-score = sum over questions of (sum daily BSS*100)/active_days. Predict EVERY question EVERY day.
- BSS = 1 - SSE over outcomes. Abstain=0. Calibrated tiny probs on unknowable ≈ 0 (safe). Overconfidence = negative.
- Strategy: predict all 330 each day; refine near-term (resolving <10d) with fresh news; base-rate the rest.
- Workspace path: .../minimalHarness_claude-opus-4-7_001/workspace

## SCORING NOTES
- If true outcome unpredicted: score = -(sum of my p_i^2). Small probs => small loss.
- If predicted at p and true: gain ~1-(1-p)^2. Report calibrated probs; cover top 3-5; leave mass implicit when unsure.
- Many "Who/Which X will [dramatic event]" Qs: event may NOT happen by date -> resolves no-answer -> any guess slightly negative. Keep sums modest (0.4-0.7) for speculative.

## MACRO CONTEXT (as of 2025-12-24)
- VENEZUELA: Trump huge military buildup in Caribbean (carrier, troops), boat strikes, blockade, sanctions on Maduro family Dec 19. Trump says land strikes "coming soon". Regime change pressure. Machado (opposition, fled) backs US. Citgo license extended to Feb 3.
- UKRAINE: Yermak (chief of staff) sacked early Dec over $100M Energoatom corruption scandal. Defence Min = Denys Shmyhal. US peace plan talks ongoing (US envoys to Moscow). Successor candidates for roles: Fedorov, Shmyhal, Kyslytsya, Pavlo Palisa.
- GREENLAND: Trump-Denmark dispute ongoing/escalating into Jan 2026 (talks, NATO Arctic).
- MEASLES: SC (Spartanburg ~138), Arizona (176), Utah (115). Q asks which state hits 185 by Jan 2026 -> Arizona most likely (176 and growing), then South Carolina.
- NYE PLOT: FBI foiled "Operation Midnight Sun" Turtle Island Liberation Front, LA/Orange County (NOT Charlotte NC). Q628026 asks town outside Charlotte NC -> may be different/unclear; LA-area plot is the big one.
- AFCON 2025: Morocco hosts, Dec 21 2025 - Jan 18 2026 final in Rabat. Groups: A: Morocco,Mali,Zambia,Comoros; B: Egypt,SA,Angola,Zimbabwe; C: Nigeria,Tunisia,Uganda,Tanzania; D: Senegal,DR Congo,Benin,Botswana; E: Algeria,BurkinaFaso,EqGuinea,Sudan; F: IvoryCoast,Cameroon,Gabon,Mozambique. KO from Jan 3. Final Jan 18 = Morocco vs Senegal (per Q799398).
- IRAN: Major US-Israel-Iran WAR erupts ~Feb 2026 (huge Q cluster). Protests in Iran late Dec/Jan. Possible supreme leader vacancy/interim council Feb. Strikes on Iranian cities, Gulf spillover Feb-Mar.
- AUS OPEN 2026: Melbourne, ~Jan 12-Feb 1. Men top: Sinner(1), Alcaraz(2/3). Women: Sabalenka(1). Defending W champ Madison Keys. Defending M champ Sinner.
- ELECTIONS: Bangladesh Feb 12; Thailand Feb 8 (snap); Portugal pres Jan (Ventura far-right in runoff); Nepal PM Mar 27; Bulgaria first female head of state by Feb 11.
- Chelsea: Maresca under pressure (rift w/ hierarchy) but contract to 2029, insists staying as of Dec 19. Man Utd: interim coach Michael Carrick from ~late Jan 2026 (Amorim out).

## WORKFLOW (each day)
1. Read MEMORY.md + preds.py. Call next_day already advanced date.
2. Check market.csv resolution_date column for Qs resolving in next ~10 days -> prioritize.
3. Search news (from_date= last ~3 days) for those Qs + any breaking macro news.
4. Update preds.py + re-submit ONLY changed qids (re-submitting overwrites; weight accrues from that day).
   - Also: questions whose start_date passed may now have real news -> refine.
5. Submit. Then next_day.
NOTE: Don't need to resubmit unchanged ones every day? Actually TW-score uses last active prediction (it persists). Re-submitting only matters when changing. A submitted prediction stays active until overwritten. So focus daily effort on NEW info / near-term Qs.

## DAY 1 (2025-12-24): submitted all 330 baseline preds. File: memory/preds.py, memory/submit_order.json.

## HIGH-PRIORITY TO REFINE (as news arrives)
- AFCON: group results finalize Dec 31; R16 Jan 3-6; QF Jan 9-10... wait QF Jan 14? final Jan 18 Morocco likely. Qs: 343689,703511,459037,799398,573851.
- Aus Open draw ~Jan 8-9: refine 2176,980781,789844,287417,464874,679570,922844,286957,793465,400561,891998,951896.
- Portugal pres 1st round mid-Jan: 505500 (Ventura runoff opp).
- Thailand polls late Jan: 787699,934187. Bangladesh election Feb 12: 304287,22203,223607.
- Oscars noms ~Jan 22: 876347 (One Battle After Another strong),886103.
- Super Bowl LX Feb 8; NFC champ QB 694686; winner 180958. NFL playoffs Jan 10+.
- CL knockout draw late Jan (Q85609,35131,55999,915784,167989 etc).
- Venezuela: watch for Maduro fall -> 651727. NYE plot 628026 (search Charlotte NC specifically).
- Chelsea 165622 (Maresca staying as of Dec19 - low prob new coach).
- Grammys Feb 1 (946810 - research nominees).

## KEY RESOLVED/UPDATED LOG
- 2025-12-24: baseline all 330.
- GREENLAND UPDATE (Dec 24): Trump named Jeff Landry (Louisiana Gov) special envoy to Greenland. Denmark FM Lars Lokke Rasmussen summoning US ambassador. Relevant: 269293, 630728 (maybe add Jeff Landry/Trump), 621718 (Frederiksen/Nielsen), 85534, 822586.
- AFCON groups (as of Dec 29): Nigeria won Group C (qual, top). Egypt won Group B (qual). Senegal & DRC both 4pts Group D (final Dec 30 Senegal v Benin, DRC v Botswana - DRC likely beats winless Botswana to advance). Morocco 4pts top Group A. Ivory Coast Group F. R16 Jan 3-6. Refine 459037/703511 once bracket set.
## RESOLVED RESULTS (learnings)
- 165622 Chelsea coach -> Liam Rosenior (TW -1.69, low spread limited loss). Lesson: appointments resolve to surprise names; keep spreads.
- 227432 Ukraine DefMin -> Mykhailo Fedorov (I had 0.04, TW -2.37). He was a listed candidate; should've weighted higher (he's a top Zelensky ally/DPM).
- 628026 Charlotte NYE -> Mint Hill (a real Charlotte suburb plot existed; my search missed it). TW -1.02.
- 892867 Austrian skier -> Katharina Liensberger (female slalom skier; I had speed men). TW -4.09.
- 93950 measles -> South Carolina (I had 0.55!). TW +61.78. BIG WIN.
- NET: cumulative TW 52.61. One confident-correct >> many tiny-negatives. STRATEGY VALIDATED: low spreads on speculative limit loss; invest to NAIL knowable ones early (weight accrues per day held).

## 2026-01-01: Trump began bombing Venezuelan LAND (Al Jazeera). Maduro still in power, releasing prisoners (conciliatory). Q651727 trimmed (no interim pres by Jan2). T20 WC 2026 Feb7-Mar8 India+SL; India-Pak Feb15 Colombo neutral -> 468637 Sri Lanka stays 0.55.

## 2025-12-25: scanned. No material change. NYE plot = California "Operation Midnight Sun" (TILF), NOT Charlotte NC -> Q628026 likely no valid Charlotte answer, keep low spread. Venezuela: Maduro still in power, escalation continues. AFCON openers done (Egypt, SA, Senegal, DR Congo, Nigeria, Tunisia, Algeria, Ivory Coast winning starts). Predictions persist; only resubmit on material change. Next deep refinement: ~Dec 31 (AFCON groups final) & Jan 8 (AO draw).
