# Forecasting Tournament — Persistent Memory

## Simulation state
- Sim date: **2026-06-24** (Day 1). 252 active questions, all resolved by 2026-09-30.
- All 252 have an initial forecast submitted on Day 1 (2026-06-24). predictions/2026-06-24.json.
- Key fictional/sim events: Khamenei assassinated 2026-02-28 (funeral July 4-9, Mashhad); Mojtaba Khamenei is new Supreme Leader; Iran war ongoing; Maduro removed from Venezuela; Starmer resigned as UK Labour leader 2026-06-22 (Burnham returned via Makerfield by-election, frontrunner); Kevin Warsh Fed chair since 2026-05-22; Powell out; 2026 World Cup ongoing in US/Mexico/Canada; Alcaraz out of Wimbledon (wrist).

## Scoring strategy
- Score = Brier skill per day: E[score] ≈ Σ p_i² over listed outcomes if q=p. So ALWAYS list the true top-5 candidates with honest probabilities; adding a candidate with true prob p adds ~p² to expected score.
- Unlisted true outcome → big penalty. Never use placeholder outcomes; use exact names.
- Update forecasts as new info arrives — TW score accrues daily; each new submission overwrites prior and accrues weight from that day.
- For "if any" questions, "None" is a legitimate outcome.
- For conditional questions ("If X leaves..."), answer the likely destination if the event occurs; question may void if condition fails (then it doesn't count).

## Key verified facts (as of 2026-06-24)
### F1 2026 (new regs)
- Standings after 7 rounds (Barcelona): Antonelli 156 (Mercedes, 5 wins: China, Japan, Miami, Canada, Monaco), Hamilton 115 (Ferrari, won Barcelona), Russell 106 (won Australia), Leclerc 75, Norris 73, Piastri 68, Verstappen 55.
- Mercedes dominant (6 wins in 7). Bahrain + Saudi GPs cancelled (Iran conflict). Races: British GP July 5 (Silverstone), Belgian July 19, Hungarian July 26, Dutch Aug 23, Italian Sep 6, Spanish Sep 13 (Madrid), Azerbaijan Sep 26.
- Per-race priors: Antonelli ~0.40-0.44, Hamilton ~0.20, Russell ~0.15, Norris ~0.09, Verstappen ~0.07.
### MotoGP 2026
- Bezzecchi 180, Martin 172, Marquez 140 (5 wins) after ~10 rounds. Marquez strong at Sachsenring.
### Tennis
- Wimbledon June 29-July 12; draw June 26. Alcaraz OUT (wrist). Men: Sinner -175 (~64%), Djokovic +500, Zverev +900 (won 2026 French Open). Women: Sabalenka +300, Rybakina +400, Swiatek +500 (defending), Gauff +600, Andreeva +800 (won 2026 French Open). Serena Williams singles wildcard (+3500).
### FIFA World Cup 2026 bracket (verified FIFA/CBS)
- R32: Jun 28-Jul 3. R16 Jul 4-7. QF: Jul 9 Boston (M97=W89vW90), Jul 10 LA (M98=W93vW94), Jul 11 Miami (M99=W91vW92), Jul 11 KC (M100=W95vW96). SF: Jul 14 Dallas (W97vW98), Jul 15 Atlanta (W99vW100). 3rd place Jul 18 Miami. Final Jul 19 NJ.
- Paths: Boston QF ← 1E(Germany)/1I(France) side + 1F(Neth)/2C(Brazil?) side. LA QF ← 1H(Spain)/1D(USA)/1G(Belgium). Miami QF ← 1C(Brazil)/1L(England)/1A(Mexico). KC QF ← 1J(Argentina)/1K(Portugal)/1B(Switzerland).
- Bookmaker win odds (June 19-23): France ~17-20%, Spain ~15-17%, England ~11-12%, Brazil ~8-10%, Portugal ~8-10%, Argentina ~8-9%, Germany ~6-7%.
- Group stage results so far: Spain 0-0 Cape Verde; France 3-1 Senegal; USA 4-1 Paraguay, 2-0 Australia; Canada 6-0 Qatar but lost 1-2 Switzerland (SUI won Group B, CAN 2nd); Morocco 1-0 Scotland (Boston); Brazil 1-1 Morocco.
- Golden Boot odds: Mbappe 6/4, Messi 13/8, Haaland 5/1, Kane 6/1. Messi 5 goals (all Argentina's) after 2 games; Mbappe 4.
### Fed (July 29 FOMC)
- Chair Kevin Warsh (since May 22). April 29 meeting 8-4: Miran wanted cut; Hammack/Kashkari/Logan opposed easing bias. June 16-17 unanimous hold. July hike odds ~18-34%. Hawks: Hammack, Kashkari, Logan.
### UK politics
- Starmer resigned as PM/Labour leader June 22; leadership nominations July 9-16; new leader by Sept 1. Burnham frontrunner (won Makerfield June 18, 54.8%).
### Others
- SK Hynix filed June 24 for $29.4B Nasdaq ADR listing July 10 (largest ADR ever, beats Alibaba $21.8B).
- Seahawks sale: bidders Grousbeck/Mittal (letter of interest), Khosla, Boehly (weighing), Zuckerberg (rumored); NFL approval possibly August.
- Nvidia ~$5.1T most valuable (Alphabet $4.5T, Apple $4.4T).
- NY passed 1-yr data-center moratorium June 4 (awaiting Hochul signature).
- Women's T20 World Cup (England, June-July 2026): Australia favorite ~1.63, 3-0 in group; England & WI 3-0; India lost to South Africa.
- England-India T20I series: July 1, 4, 7, 9, 11 in England. India reigning men's T20 WC champs (beat England in semi by 7 runs).
- LeBron: Lakers most likely (0.67); Warriors threat.

## Per-question notes (selected)
- 279946 SK Hynix 0.82 (verified filing).
- 225772 Savinho→Spurs 0.85 (verified "effectively formalised").
- 26225 Morgan Rogers→Arsenal 0.85 (personal terms agreed, multiple sources; fee £100m still to settle).
- 876325 Enzo→Real Madrid 0.82 (personal terms in principle; Chelsea want £120-140m; some sources say no agreement yet — monitor).
- 311120 Qatar hosts 2027 Spanish Super Cup 0.90 (RFEF president confirmed).
- 76066 Moldova PM: Munteanu still active (June 24); question may void; Recean 0.30 if not.
- 754639 UK party leader resign MP: unclear; low confidence spread.
- 619176 PFA month: no decision yet; September 0.40 modal.
- 126882 OPCW Syria: 54 aerial bombs + 25 rockets found May 2026; answer likely "aerial bombs" (0.45).

## Update triggers / to-dos
- **June 25-27**: WC group stage ends → update WC QF/SF/final forecasts (199448, 457239, 935518, 439898, 592683, 241292, 201629, 581542) based on actual bracket.
- **June 26**: Wimbledon draw → update 985440 (first finalist; check Sinner/Djokovic halves), 742225, 846335.
- **June 28-July 3**: WC R32 results → refine.
- **July 1-11**: England-India T20 series (562262) — update after each match.
- **July 5**: British GP (747581); **July 12**: MotoGP German GP (897546).
- **July 9-11**: WC QFs; **July 14-15** semis; **July 19** final.
- Watch for: Kremlin announcement on Khamenei funeral delegation (659176) ~July 1-4; Hannah Dugan sentencing July 8 (213487); SK Hynix pricing July 10 (279946); FOMC July 28-29 (942650); Seahawks sale approval (902592); Fed July meeting.
- Resubmit/refine when agents' key claims (e.g., transfer agreements) get confirmed or contradicted in news.

## Agent cluster research files (Day 1)
- scripts/cluster_*.json contain question lists per topic. Research summaries embedded in session transcripts; key numbers captured above and in per-question submissions.
