# Forecasting Memory — updated 2026-03-26

## STATE
- 378 questions, all predicted as of 2026-03-26 EXCEPT abstentions listed in WATCHLIST.md.
- 360 predictions made 2026-03-25 (prior session, no notes saved); 12 new ones + 1 update made 2026-03-26.
- Full prediction dump: memory/predictions_review.txt (regenerate each day from market.csv).

## WORLD CONTEXT SNAPSHOT (as of 2026-03-26)
- **US-Israel war on Iran**: started ~Feb 27/28 2026. 7,800+ targets struck. Iran retaliates on Israel + Gulf (UAE/Bahrain/Kuwait/Qatar host US bases; UAE hit repeatedly, Kuwait airport fuel tank fire). Strait of Hormuz restricted by Iran (India denies needing permission; S.Korea pressured). US proposed 15-point peace plan ~Mar 24; Iran REJECTED it, offered own conditions; ceasefire talks "heating up", market optimism. Lebanon: Israel ground op in south Lebanon, plans to "occupy swathe", Lebanon expelled Iran ambassador; Iran wants Lebanon in ceasefire. Several questions presuppose: first ceasefire in April; US-Iran talks in April (likely Araghchi leads); US fighter shot down Apr 3 over southern Iran.
- **Venezuela**: US invaded Jan 3 2026, captured Maduro + wife → NY narco-terrorism trial ongoing (pretrial Mar 26). Interim President = Delcy Rodríguez (chavista). Machado (Nobel laureate) returning "in coming weeks"; US-Venezuela oil trade reopening per Machado/Trump. Future: major Caracas earthquake ~June 20-26 (per hidden-event Qs 30914, 105885).
- **Australia**: Sussan Ley ousted as Lib leader Feb 13 by Angus Taylor (34-17), resigned as MP → Farrer by-election ~May. Lib party at historic lows; One Nation surging (2nd in SA state election Mar 21, 22% vote). 
- **Bangladesh**: BNP-alliance won Feb election (212/350); parliament met Mar 12; speaker Hafiz Uddin Ahmad. Fuel rationing due to Iran war oil spike.
- **F1 2026**: Mercedes dominant (Russell won Australia; Antonelli won China Mar 15, both 1-2s). Russell leads WDC by 4 pts over Antonelli. McLaren (champs 2025: Norris WDC) both DNS China. Verstappen/Red Bull poor. Hamilton now Ferrari (1st podium China). Bahrain+Saudi GPs cancelled, Qatar MotoGP postponed (war).
- **Football**: WC2026 draw (Dec 5): Grp K = Portugal, Colombia, Uzbekistan, playoff; Grp F = Netherlands, Japan, Tunisia, playoff; Grp A Mexico/SK/SAf; D USA/Aus/Paraguay; final Jul 19 MetLife. Playoffs Mar 31 (Italy in). Chelsea: Rosenior replaced Maresca Jan 2026; lost 8-2 agg to PSG UCL R16; 6th in PL. Arsenal lost Carabao final to Man City (O'Reilly x2). Everton (Moyes) 7th surging.
- **Syria**: al-Sharaa consolidating; Kurds granted citizenship Jan; UNSC lifted HTS sanctions Feb 27; new currency Jan (2 zeros dropped). Cabinet (Mar 2025): agriculture = Amjad Badr (Druze/Suwayda). First reshuffle expected by May 2026 (Q654858).
- **Hungary**: election ~Apr 12; my pred: Magyar 0.6 / Orban 0.3 for PM elected by May 13.
- **Japan PM**: female (Takaichi presumably) — Q881473 assumes visit to Hanoi; Vietnam PM = Pham Minh Chinh (pred 0.75).

## SCORING INSIGHTS (critical)
- BSS = 1 - Σ(p_i - y_i)². Missing true outcome costs the full 1.0; abstaining scores 0/day.
- Optimal: honest probabilities. Adding a guess with subjective prob q at p=q gains ~q² expected. Wrong small guesses cost only p². So ALWAYS include plausible candidates at honest probs; never inflate.
- TW-score: earlier predictions weigh more (active more days). Submit ASAP on new questions; update immediately when news reveals answers.
- Hidden-event questions (generated from FUTURE articles): answer usually appears in corpus 0-3 days before resolution date. CHECK DAILY questions resolving within ~7 days via targeted search — this is the biggest score lever. When an article reveals the answer, submit at 0.85-0.97.
- ~1/day update cadence. Corpus = daily crawl incl. Al Jazeera, Reuters wires, CBS, Straits Times, Khaleej Times, Korea Herald, HT, Irish Times, etc.

## DAY LOG
- 3/27: Iran: Khamenei KILLED Feb 28 (war trigger); new Supreme Leader = Mojtaba Khamenei. Iran rejected 15-pt plan (wants Hormuz sovereignty, Lebanon in deal, reparations); Pakistan = preferred talks venue (Islamabad); Araghchi+Qalibaf off Israel hit-list (negotiators). Trump extended pause on Iran ENERGY strikes to Apr 6 8pm. Deaths: 1500+ Iran, 1100 Lebanon, 16 Israel, 13 US. Qatar's giant gas plant damaged. Asian Cup draw (was Apr 11 Riyadh) postponed; Doha DL May 8 in doubt. Zelensky in Gulf NOW: Saudi deal signed 3/27, UAE/Qatar next → updated 632512 to Riyadh .30/Damascus .22. Hungary: Median poll Tisza +23 → Magyar .68. FA Cup QF = Southampton v Arsenal (Apr 4-5) → Southampton .90. WC playoffs: Italy-Bosnia & Kosovo-Türkiye finals 3/31; Jamaica beat NC (faces DR Congo, winner → Grp K); Bolivia-Iraq for Grp I. Sri Lanka jailing fuel hoarders → 487623 SL up to .12. Maduro motion to dismiss DENIED, in Brooklyn jail.

## DAILY ROUTINE
1. Read market.csv; find questions with my_prediction empty (new) → research + predict same day.
2. List questions with resolution_date within 7-10 days (script: memory/near_term.py) → targeted news search each; update where news reveals/informs.
3. Check WATCHLIST.md scheduled checks for today.
4. Skim new articles (articles/YYYY/MM/DD/) headlines for major world shifts (war status, elections).
5. Update this file's context snapshot; call next_day.
