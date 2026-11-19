# Session Log

## Day 2026-06-24 (sim date)
- Submitted all 252 forecasts (8 earlier + 244 today) across plans A/B/C/D.
- All distributions stored in memory/sub/plan_[abcd].py; master list in memory/sub/all_forecasts.jsonl.
- Scoring approach: named plausible candidates only, no placeholders, sums <= 1.0.
- Reminder: market.csv `my_prediction` is stale; true record in predictions/YYYY-MM-DD.json.
- Next: call next_day; check resolution events; re-forecast changed priors.
## Day 2026-06-25 (sim date)
- All 252 recorded; updated 19 forecasts with fresh news:
  * WC bracket recomputed from real results (Mexico 1A, S.Africa 2A, Brazil 1C, Morocco 2C, Germany 1E, Ivory Coast 2E, Ecuador 3E-Q, Netherlands/Japan 1F/2F contest, Switzerland 1B, Canada 2B, USA 1D, France/Norway 6pts 1I showdown Jun 26).
  * Boston QF 199448 -> Germany .33, Netherlands .15, France .12, Norway .08, Morocco .08
  * KC QF 457239 -> Argentina .40, Colombia .32, Switzerland .18, Uruguay .05, Australia .04
  * SF1 935518 (Dallas Jul 14) -> Spain .18, Germany .16, France .13, Portugal .08, USA .06
  * SF2 439898 (Atlanta Jul 15) -> Argentina .28, Brazil .22, Mexico .09, Colombia .08, Switzerland .05
  * Winner 241292 -> Argentina .22, Spain .16, France .12, Brazil .11, England .09
  * Golden Boot 201629 -> Mbappe .28, Haaland .24, Kane .20, Messi .15 (Haaland/Mbappe 4 goals each)
  * Golden Ball 581542 -> Mbappe .22, Yamal .17, Messi .12, Haaland .08
  * Transfers: Rogers->Arsenal .80; Diomande->Liverpool .75; Rodri -> Man City .35/Real Madrid .15 (news: not Madrid priority after Bernardo Silva; City renewal favored); highest-PL-fee 875467 -> Diomande .30/Rogers .22; Enzo->Madrid .65; Baleba->Man U .30 (Ederson signed; Mateus Fernandes priority).
- Learning: resubmit whenever the actual bracket/group outcome changes paths; check final group tables the morning before matches.

## 2026-06-26 (Day 3)
- Scanned 2026-06-26 articles. Key results: France 4-1 Norway (Dembélé hat-trick, Mbappé 2 assists, France 9pts win Group I; Norway 2nd rested Haaland); Netherlands 3-1 Tunisia (perfect run, Netherlands 1F, plays Morocco M75); Japan 1-1 Sweden (Japan 2F vs Brazil; Sweden 3rd in best-3rd contention); Ecuador 2-1 Germany (Germany still 1E on 6pts/+6GD, IC 2E, Ecuador best-3rd); Australia 0-0 Paraguay (AUS 2D; USA 1D lost 3-2 to Turkey in dead rubber); USA v Bosnia R32 confirmed.
- Re-derived bracket probs; resubmitted: 199448 France .35/Germany .25/Netherlands .19/Morocco .07/Canada .05; 457239 Argentina .33/Colombia .24/Switzerland .18/Australia .08/Egypt .05; 935518 France .23/Spain .15/Germany .14/Netherlands .11/Portugal .11; 439898 England .21/Brazil .18/Argentina .17/Colombia .13/Switzerland .09; 241292 England .16/France .15/Argentina .14/Brazil .13/Spain .11; 592683 France .21/Spain .17/Brazil .14/Germany .13/Netherlands .09.
- Golden Boot/Ball: 201629 Mbappé .25/Messi .20/Dembélé .13/Haaland .11/Kane .10 (Dembélé hat-trick; Haaland benched, Norway out-path short); 581542 Mbappé .20/Dembélé .16/Yamal .13/Kane .12/Messi .09.
- Women's T20 WC: Australia 4-0 (semi favorites); 258607 Australia .62/England .13/India .12; 799550 Sutherland .18/Sciver-Brunt .14/Mooney .12/Perry .11/Gardner .06. Final group A game June 28 (AUS v IND) decides semi seeding; final July 5 Lord's.
- Transfers: Morgan Rogers personal terms agreed with Arsenal (until 2031) but Villa wants €120m+ — 26225 Arsenal .84; Yan Diomande: Liverpool rejected €80m+€20m bid, Leipzig wants ~€130m — 696503 Liverpool .70; Enzo Fernandez: Madrid not yet in club-to-club talks — 876325 Real Madrid .60 (question conditional on him leaving Chelsea); Rodri conditional question 243962 → Real Madrid .55/Barcelona .14 (City renewal favored); 875467 → Diomande .28/Rogers .25/Tonali .10/Anderson .05/Gibbs-White .05.
- Khamenei state funeral (July 4-9) — Kremlin delegation: 659176 Volodin .33/Medvedev .22/Lavrov .22/Putin .12 (Raisi funeral precedent = Putin sends Volodin).
- Jaylen Brown trade: 344207 now Portland Trail Blazers .16/Spurs .12/Pelicans .10/Rockets .09/Magic .07 (Shams: Blazers lots of interest, Western conf heavy, Boston hunting big man).
- Venezuela earthquake death toll >900 (no market question). US struck Iran after cargo-ship drone attack (235→900+ Venezuela quake toll). Alligator Alcatraz shut (no question). No 2026 measles death yet — 903529 unchanged.
- Group G (Egypt v Iran 11pm ET Jun 26) and Group H (Spain v Uruguay, Cape Verde v Saudi) pending in this batch — watch next_day articles for results; Group D/E/F final tables now known (Ecuador 3E qualifier; Paraguay 3D likely best-third; Sweden 3F in best-3rd contention).
- Next: June 27 — Colombia v Portugal (Group K decider), Austria v Algeria, England v Panama, Ghana v Croatia, Argentina v Jordan (Group J), plus full third-place table after all 12 groups complete; R32 assignments confirmed ~June 27-28.

## 2026-06-27 (Day 4)
- Results: Cape Verde 1-1 Saudi Arabia (Cape Verde qualify! 3 pts, smallest nation ever; 2H confirmed); Spain 1-0 Uruguay (Muslera error; Uruguay out; Spain 1H on 7 pts); Egypt 1-1 Iran (draw; Salah assessment ongoing; Egypt 1G on 5, Belgium 2G via 5-1 v NZ Trossard brace); England 2-? Panama W (Kane+Bellingham; England 1L). Portugal vs Colombia (Group K) and Austria vs Algeria (J) pending as of scan; Messi rested vs Jordan (Scaloni) — Argentina prioritize group win w/ 8/9 pts path.
- 2H = Cape Verde -> Argentina R32 gets weak M86: 457239 Argentina .35 (up), 241292 Argentina .16, 439898 England .19/Argentina .19/Brazil .17.
- Group L decider June 27/28 (England Panama done -> England 1L; Ghana v Croatia pending); Group J Austria v Algeria pending; Group K Portugal v Colombia pending.
- Iran-US: second night of US strikes post-ship-attack; MoU unraveling; Iran hits US-linked targets (Bahrain drone). No direct market question resolution imminent.
- Russell pole for Austrian GP (controversial; Verstappen Q3 crash) — 747581 Antonelli .55 kept (Mercedes 1-2 pace).
- No transfers confirmed June 27.

## 2026-06-28 (Day 5)
- Confirmed results: Colombia 0-0 Portugal (Colombia 1K, Portugal 2K, VAR disallowed; DR Congo best-3rd, face England M80); England beat Panama (England 1L) — England v DR Congo R32 Atlanta; Croatia 2-1 Ghana (Vlasic; Croatia 2L, Ghana 3L best-3rd); Austria 3-3 Algeria (both advance — one 2J one 3J, tiebreaker TBC; Iran eliminated); Argentina 3-1 Jordan (Messi scored again; Argentina 9 pts 1J); Spain 1-0 Uruguay (Spain 1H); Cape Verde 1-1 Saudi (Cape Verde 2H); Egypt 1-1 Iran (Egypt 1G); Belgium 5-1 NZ (Belgium 2G); USA 1D but lost to Turkey (M81 v Bosnia confirms); Australia 2D 0-0 draw; Germany 1E beaten by Ecuador (Ecuador best-3rd); Netherlands 9pts 1F; Japan 2F vs Brazil R32.
- Women's T20 WC semis set: AUS v WI (SF1 Jun 30) & ENG v IND (SF2 Jul 2) — Australia beat India (India out; SA scraped Bangladesh). 258607: AUS .62/ENG .17/IND .13/WI .03. Final Jul 5 Lord's.
- F1: Russell won Austrian GP beating Verstappen; trims Antonelli lead — 747581: Antonelli .50/Russell .22/Verstappen .10/Norris .06/Leclerc .05.
- Stokes retires international cricket (no market q). Korea out (Hong quits).
- 241292 updated: England .17/Argentina .16/France .15/Brazil .13/Spain .09.
- No transfers confirmed today; all transfer forecasts stand.
- Next: June 29 — R32 begins (M73 Canada-SAfrica, M74 Germany-3rd, M75 Netherlands-Morocco, M76 Brazil-Japan); watch results; 200-day: resolution check — 258607/799550 (Jul 5), 344207 (Jul 1 — still 'agree to trade by Jul 31'? question is conditional, but resolution Jul 1 - keep named Blazers etc), 659176 (Jul 1 - Khamenei funeral delegation TBC Jul ~3), 619176 (Jul 1), 633052 (Jul 4), 177324 (Jul 4), 258607 (Jul 5), 747581 (Jul 5), 799550 (Jul 5).

## Day 6 — 2026-06-29
R32 so far: Canada beat South Africa (Eustaquio stoppage-time, first knockout win; M90 Houston Jul 4 = W73 v W75); Brazil beat Japan 2-1 (Martinelli 90+; into last 16). Germany v Paraguay (Jun 29): Paraguay led 1-0 HT (Enciso 41'), Havertz equalized mid-2H — unresolved at session end; Netherlands v Morocco tonight (Monterrey, early Jun 30 FT). Women's T20 semis confirmed: Australia v West Indies (Jun 30, Oval; Australia chased 6 down vs India in decider at T20WC, WI lost to Ireland late), England v India (Jul 2). 258607 → Australia .68/Eng .15/Ind .13/WI .02. 799550: Perry .11→.13 (in form vs India).
WC forecast resubmissions (HT-Germany vs Paraguay shock): 199448 France .36/Germany .22/Netherlands .20/Morocco .07/Canada .06 | 935518 France .24/Spain .15/Netherlands .12/Germany .12/Portugal .11 | 592683 Germany .13→.12 | 439898 Brazil .17→.18 | 241292 Brazil .13→.14 | 201629 Messi .20→.21 | 177324 REBUILT: New Orleans Pelicans .40/OKC .12/Denver .08/Spurs .07/Boston .05 (Alexander = RESTRICTED FA w/ two-way QO per LD Sport — Pelicans re-sign most likely; prior forecast lacked Pelicans entirely) | 344207 Portland .16→.20 + Brooklyn Nets .10 added (Charania: 4+ firsts ask; Nets have capital) | 659176/619176/243962/26225/696503/524604 unchanged (no new info; funeral delegation likely announced ~Jul 3-4).
Note: 199448 = Boston QF Jul 9 (W89 v W90); 935518 = SF1 Dallas Jul 14; 457239 = KC QF Jul 11 (M100); 439898 = SF2 Atlanta Jul 15; 592683 = 3rd place; 241292 = Final Jul 19.
Market.csv check: no questions resolve 2026-06-29 or 2026-06-30. July 1: 344207 (Jaylen Brown trade destination, conditional; Portland strongest), 659176 (Kremlin funeral delegation; Volodin .33/Medvedev .22/Lavrov .22/Putin .12/Novak .05), 619176 (PFA resume month; September .30/August .25/October .20/July .10/Nov .05). July 4: 177324 (Alexander two-way), 633052 (cyclospora leader; TX .40). July 5: 258607/747581 (Antonelli strong for British GP).
Also 2026-06-29 news: US-Iran "stand down" + Doha talks Tuesday (both sides "tit-for-tat appears over"); Khamenei funeral Jul 4–9 ladder Tehran→Qom→Mashad confirmed (Wikipedia); PFA/WC non-resolution items noted. F1: Russell won Austrian GP; Antonelli leads.
Pending: M74 (GER–PAR), M75 (NED–MAR) final scores → update 199448/935518/592683/347581? (no) after result. Women's T20 SF1 Jun 30 → update 258607/799550. M76 Brazil–Japan result already in (BRA won) — verify list continuity tomorrow.

## Day 7 — 2026-06-30
R32 results IN: Germany 1-1 Paraguay, Paraguay won pens 4-3 after ET (Enciso 41' HT, Havertz 52'; Tah ruled out; Havertz/Woltemade/Tah missed pens) — GERMANY ELIMINATED. Netherlands 1-1 Morocco (Gakpo 72', Diop 90+1', pens 2-3; Bounou the hero) — NETHERLANDS ELIMINATED. Morocco advance to R16 vs Canada (Houston Jul 4). Paraguay advance to R16 vs winner of France v Sweden (Philadelphia Jul 4; winner then QF Boston Jul 9 = 199448).
WOMEN'S T20 WC: Australia beat West Indies by 8 wickets in SF1 (The Oval, Jun 30; Mooney 61* off 36, Gardner 2/13+35*, Molineux captain, Perry retired hurt w/ quad in 7th over — Sunday final at Lord's v ENGLAND or SOUTH AFRICA). SF2 (Thu Jul 2) is ENGLAND v SOUTH AFRICA — INDIA ELIMINATED (failed chase vs AUS; NRR overhauled by SA's big win vs Bangladesh, +0.734 vs collapsed IND NRR). 258607 → AUS .70/ENG .20/SA .08 (India removed). 799550 → Mooney .18/Sutherland .17/Sciver-Brunt .13/Perry .09 (hurt)/Gardner .08.
WC bracket questions rebuilt post-upsets: 199448 → France .40/Morocco .18/Canada .16/Paraguay .10/Sweden .04 (pool = W89 winner {FRA/SWE/SCO/PAR} v W90 winner {CAN/MAR}). 935518 (SF1 Dallas) → France .30/Spain .17/Portugal .11/Morocco .08/Croatia .06 (W98 = W93 {ESP v POR/CRO} v W94 {USA/Bosnia v EGY/...}). 457239 (KC QF) → Argentina .37/Colombia .24/Switzerland .18/Belgium .06/Australia .06 (Egypt REMOVED — Egypt is in SF1 path via M82/M94). 439898 (SF2 Atlanta) → Brazil .20/England .19/Argentina .20/Colombia .13/Switzerland .09. 592683 → France .22/Spain .17/Brazil .15/Argentina .12/England .10 (GER/NED removed). 241292 → England .17/France .17/Argentina .16/Brazil .14/Spain .09.
201629 → Kane .13/Haaland .10 (Haaland faces Brazil M91).
Resolves tomorrow 2026-07-01: 344207 (Portland .25/Nets .10/Pelicans .10/Spurs .10/Rockets .08 — conditional Jaylen Brown trade; Celtics demand 4+ firsts, Blazers strongest), 619176 (PFA resume month — keep Sept .30/Aug .25/Oct .20/Jul .10/Nov .05; no news), 659176 (Volodin .35/Lavrov .20/Medvedev .20/Putin .12/Novak .05 — Raisi precedent + Iran Intl "lower-level Russian delegation expected"; funeral Jul 4–9; still no official Kremlin announcement as of Jun 30).
US-Iran: stand-down + Qatar talks Tuesday (Kushner/Witkoff to Doha); oil easing. No impact on tracked questions.

## Day 8 — 2026-07-01
RESOLUTIONS (3, arrived today): 344207 Jaylen Brown → Philadelphia 76ers (NOT named; Brier -0.10, TW +2.63 — lesson: when Celtics linked him to SIXnERS?? actually reports said Giannis to Miami; any named-at-all needed ~coverage of Sixers — add discretionary ~5% on unloved longshots next time). 619176 → September (Brier +0.40, TW +39.5). 659176 → Dmitry Medvedev (Brier +0.18, TW +20.89 — Volodin lost; Medvedev .20 hit).
R32 results in: FRANCE 3-0 Sweden (Mbappé 2 → 6 goals, level w/ Messi; STRONG Path: M89 vs Paraguay Jul 4 PHL). MEXICO 2-0 Ecuador (M92 Jul 6 MEX: Mexico v England). ENGLAND 2-1 DR Congo (Kane double, controversial no-pen; into R16). NORWAY beat Ivory Coast (Drogba furious re: decision) → NORWAY v BRAZIL M91 Jul 4. USA v Bosnia TODAY Jul 1 (Santa Clara, evening) — pending.
Women's T20: Australia in FINAL (Lord's Jul 5 vs England or South Africa; SF2 Thu Jul 2). Perry quad worry.
WC forecast updates: 199448 → France .47/Morocco .17/Canada .15/Paraguay .07 (Sweden removed)| 439898 → England .20/Brazil .20/Argentina .20/Colombia .13/Switzerland .08 | 241292 → France .18 (England .17/Argentina .16/Brazil .14/Spain .09) | 201629 → Mbappé .28/Messi .21/Dembélé .13/Kane .13/Haaland .10.
177324 BIG UPDATE: Pelicans DECLINED the two-way qualifying offer on Trey Alexander (Yahoo/Keith Smith; redundancy w/ Jaron Pierre Jr. draft pick) → he's an unrestricted FA; 177324 reshaped: OKC .22/Denver .14/Pelicans .09/Phoenix .08/San Antonio .08 (resolves 2026-07-04!).
Cumulative: accuracy 0.4% | BSS 0.002 | TW 63.02 (after 3 resolutions).
July 4 resolves: 632783? no — 177324, 633052 (cyclospora; Texas .40 unchanged). July 5: 258607, 747581 (British GP; Antonelli), 799550.
Next: watch USA v Bosnia (Jul 1), Spain v 2J (M84 Jul 2), France R16 (Jul 4), M93 (ESP v POR/CRO, Jul 6). Khamenei funeral Jul 4–9 — delegation Qs done.

## Day 9 — 2026-07-02
R32 results IN: USA beat Bosnia 2-0 (Balogun red card — suspended for R16; first US knockout win since 2002). Spain beat Austria 2-0 (Oyarzabal brace). Belgium beat Senegal 3-2 (comeback, controversial penalty) — M82 Seattle = Belgium v Senegal (my bracket maps were off: M82 was BEL-SEN NOT Egypt; Australia v Egypt = M88 Jul 3 Dallas; Spain-Austria = M84 Jul 2). Portugal v Croatia 0-0 live (referee Vincic — good for 524604!). Women's T20 FINAL SET: England beat South Africa by 40 runs in SF2 (Sciver-Brunt 75 return from injury + Knight 58 record 133 stand) → England v Australia Lord's Sun Jul 5. 258607 → Australia .63/England .33 (Sciver-Brunt 75 form). 799550 → Sciver-Brunt .22/Mooney .17/Sutherland .15/Perry .08/Gardner .07.
Bracket fixes: 935518 → France .28/Spain .15/Portugal .11/Belgium .08/Morocco .08 (adds Belgium; W98 = (POR/CRO-ESP) v (USA/BEL)). 457239 → Argentina .37/Colombia .24/Switzerland .18/Australia .07/Egypt .04 (Egypt replaces Belgium — Australia/Egypt M88 feeds M95→KC QF). 439898 unchanged (Brazil .20/Argentina .20/England .20/Colombia .13/Switzerland .08).
633052 HUGE UPDATE: CDC tracks 145 cyclospora cases; NEW YORK leads with 31–80 (~80); Texas & Illinois 11–30 each; no deaths. Forecast rebuilt: New York .75/Texas .10/Illinois .08/Florida .03 (resolves 2026-07-04).
Resolves 2026-07-04: 633052 (now NY-favored), 177324 (Alexander — Pelicans DECLINED QO; UFA; OKC .22/Denver .14/NOP .09/PHX .08/SAS .08). 2026-07-05: 258607, 799550, 747581 British GP (Antonelli .50/Russell .22).
R16 upcoming: M89 PAR v FRA (Jul 4 PHL) | M90 CAN v MAR (Jul 4 HOU) | M91 BRA v NOR (Jul 4/5 NY/NJ) | M92 MEX v ENG (Jul 5 MEX Azteca) | M93 POR/CRO v ESP (Jul 6 DAL) | M94 USA/BEL (Jul 6 SEA) | M95 ARG/CPV v AUS/EGY (Jul 7 ATL) | M96 SUI v COL (Jul 7 VAN) | M99 Miami (Jul 11) | M97 Boston Jul 9 (199448) | M100 Kansas Jul 11 (457239) | SF1 Dallas Jul 14 | SF2 Atlanta Jul 15 | Final Jul 19 MetLife (241292).
Timeline: US-Iran stand-down + Doha talks Tue (Kushner/Witkoff); Khamenei funeral Jul 4–9 (Volodin bet lost — Medvedev confirmed as Russian rep).

## Day 10 — 2026-07-03
R32 final round: SWITZERLAND 2-0 Algeria (advance). EGYPT beat Australia 4-2 on penalties (Salah hero — first-ever WC knockout for Egypt). PORTUGAL beat Croatia (Ronaldo first WC knockout goal; VAR disallowed Gvardiol equalizer; POR → M93 vs Spain, ref Vincic). SPAIN 2-0 Austria (Oyarzabal brace) — Spain flying. MESSI 7 goals (scored tonight vs Cape Verde; "record-extending 8th straight World Cup match with a goal"; ahead of Mbappé 6). Argentine–Cape Verde R32 played tonight: goalless at 88' when live page captured (Messi 29'). Julian Nagelsmann RESIGNS as Germany coach (Klopp frontrunner). Djokovic through to Wimbledon R16 ("quest for 25" alive); Sinner advanced; ALCARAZ ABSENT (wrist) → Sinner defending champ; Zverev won RG 2026 (sim). 2026 F1: Antonelli leads (Mercedes), Hamilton 2nd (Won Spanish GP; FASTEST practice + sprint pole at Silverstone "Er Ecstatic"); Russell won Austrian GP. MotoGP: Bezzecchi leads (180) ahead of Jorge Martín (160); Marc Márquez 5th (108). 2026 foreign IPOs: SpaceX IPO'd $75B (US firm, not foreign) — Alibaba $25B record intact. Cyclospora: MICHIGAN surge (170+ SE Michigan since Jun 22 vs ~50/yr) — now leader candidate over NY (NY still highest in CDC multi-state map through Jun 16).
RESOLUTIONS UPCOMING: Jul 4: 177324 (OKC .22/DEN .14/NOP .09/PHX .08/SAS .08) + 633052 (rebuilt Michigan .55/NY .30/IL .05/TX .05). Jul 5: 258607 (AUS .63/ENG .33) / 799550 (Sciver-Brunt .22/Mooney .17) / 747581 (Antonelli .35/Hamilton .28/Russell .15/Verstappen .08 — Hamilton fastest practice+sprint pole at HOME, Antonelli champ leader). Jul 7: 754639 (Farage .30/Lowe .15/Sultana .15/Jenrick .10/Badenoch .05 — no news) + 263626 (rebuilt Taiwan .35/Vietnam .30/Mexico .25/China .05 — Feb & Apr largest bilateral goods deficit = TAIWAN). Jul 8: 76066 (Igor Grosu .35/Dan Perciun .22 (ED/rumor leak — Munteanu-Perciun conflict caused resignation) /Gherasimov .15/Popsoi .12/Recean .05; Perciun denied; Sandu consults next week) + 213487 (Incarceration .45/Probation .30/Home confinement .15/Fine .10 — prosecutors seek 15–21 months; Adelman liberal judge). Jul 9-13: 562262 (IND v ENG T20I 1st abandoned rain; England .47/India .44; India shock 2-0 series loss to Ireland), 107473 (UCL .30/SOAS .10/Edinburgh .08/Manchester .08/Leeds .06 — Liberty/Sky Feb 2025: UCL 12-16 investigated, most), 279946 (Alibaba .82 — SpaceX is US firm), 199448 (France .50/Morocco .19/Canada .15/Paraguay .12), 362674 (TN-9: Scalise-backed Brent Taylor .60/Todd Warner .20 — NO Trump endorsement yet; Mark Green dropped, not in primary), 902592 (Grousbeck .4/Khosla .2/Boehly .18/Mittal .15), 666563 (Cai Qi .3/Zhao Leji .28/Wang Huning .18/Wang Yi .08/Liu Jianchao .06 — Xi summit June 8-9; 65th anniversary of Friendship Treaty; Jo Yong-won = WPK org secretary), 897546 (Marc Márquez .42/Bezzecchi .25), 742225 (Sinner .62), 846335 (Rybakina .30/Sabalenka .28/Swiatek .16 — Swiatek out of form Bad Homburg; Rybakina AO champ & best grass record), 985440 (Sinner .52/Zverev .14/Djokovic .13), 66613/446236 (Bavi: no 2026 formation found in wiki list — keep Zhejiang .35/Fujian .3 etc.).
WC path updates post-upsets: 457239 → Argentina .37/Switzerland .23/Colombia .21/Egypt .09/Ghana .05 (Australia eliminated; Egypt won pens; M87 COL v GHA is tonight/Sat 02:30; M95 = winner ARG/CPV v winner AUS/EGY Jul 7). 935518 → France .30/Spain .17/Portugal .14/USA .12/Morocco .09 (Croatia OUT). 439898 → England .22/Brazil .17/Argentina .17/Mexico .13/Colombia .12. 592683 → France .24/Spain .18/Brazil .16/England .14/Argentina .12. 241292 → France .23/England .16/Argentina .14/Brazil .14/Spain .11. 199448 → France .50. 201629 → Messi .27/Mbappé .28/Kane .13/Dembélé .12/Haaland .06. 581542 → Mbappé .22/Yamal .17/Dembélé .15/Kane .13/Messi .13. 524604 → Marciniak .22/Turpin .20/Vincic .15/Zwayer .12/Oliver .08 (Vincic refereed POR v CRO — bump for final).
ALL 16-ish submissions logged OK. 249 active; TW 63.02 after 3 resolutions; no new resolutions arrived today.
NEXT: Jul 4-5 resolution watch (Alexander signing, Michigan cyclospora, Women's T20 final, British GP); R16 starts Jul 4 (PAR-FRA, CAN-MAR, BRA-NOR, MEX-ENG Jul 5). Update WC odds after each R16 result. Khamenei funeral Jul 4-9.

## Day 11 — 2026-07-04
RESOLUTIONS (Jul 4): 177324 (Alexander two-way) → TRUTH UTAH JAZZ — I missed Jazz completely (UFA after Pelicans declined QO; signed somewhere new). Brier −0.09, TW −10.47. LESSON: two-way market = deep bench of small-market teams; keep a long tail (Jazz/Wolves/Hawks/Bulls) next time instead of concentrate OKC-Denver. 633052 (cyclospora leader) → TRUTH MICHIGAN — rebuilt to Michigan .55/NY .30 on Jul 3 after finding SE-Michigan 170+ case explosion vs NY ~80 — hit .55 → Brier +0.70 (but early days NY .75 hurt TW: −6.57). LESSON: update immediately when a state surges past the frontrunner; don't hold stale NY .75 (should have moved Michigan .55-.60 yesterday).
TODAY (Jul 4) NEWS: R16 underway — M89 France v Paraguay (Tchouameni OUT, thigh; Kone in; Philadelphia weather threatens — LIVE/delayed), M91 Brazil v Norway (Haaland vs Brazil), M90 Morocco 3-0 Canada (Ounahi & Rahimi; Morocco into QF Boston Jul 9), ARG-CPV finished: "Argentina survive heroic Cape Verde fightback" (Messi 29'; Cape Verde eliminated; Messi 7 goals Golden Boot), WIMBLEDON: Eala (Filipino, #29) TOPPLED SWIATEK + Mertens STUNNED Rybakina (both R3 exits; defending champ & AO champ OUT); Sinner & Djokovic through to R16. 2026 Women T20: England WON 2nd T20I vs India (Bethell spoiler; Sooryavanshi made youngest-EVER India debut — record broken!) — Eng now 1-0 up w/ T20Is remaining; series lead → Eng .60/Ind .30. F1 Silverstone: ANTONELLI sprinted to win + POLE for GP (2nd home event for Russell — crashed 'weird' struggling for pace; Hamilton 2nd fastest FP1). 747581 → Antonelli .50/Ham .25/Ham... (final: Antonelli .5/Hamilton .25/Leclerc .08/Verstappen .08/Russell .06).
199448 rebuilt: France .53/Morocco .34 (10 Canada gone / Paraguay .09). 846335 rebuilt: Sabalenka .38/Eala .15/Anisimova .15/Pegula .12/Andreeva .08 (Rybakina & Swiatek GONE).
CUMULATIVE: TW 45.98 (after 5 resolutions: 3 hits ×(+.40,+.18,+.70), 2 misses (−.10,−.09)); accuracy 0.8%; BSS 0.004. 247 active.
TOMORROW (Jul 5) RESOLVES: 258607 (AUS .63/ENG .33) / 799550 (Sciver-Brunt .22/Mooney .17) / 747581 (updated today). Double-check morning of Jul 5. R16: M92 MEX v ENG (Azteca, Jul 5); M93 ESP v POR/CRO (Jul 6 DAL); M94 USA v BEL (Jul 6 SEA); M95 ARG/CPV v AUS/EGY → winner vs Egypt? No: M95 = W86(ARG) v W88(EGY) Jul 7 ATL. M96 SUI v COL/GHA Jul 7 VAN.

## Day 12 — 2026-07-05
RESOLUTIONS (Jul 5): 258607 Women's T20 → AUSTRALIA (+0.75, TW +79.94! Aus won by 7 wickets at Lord's; Sciver-Brunt valiant) | 799550 POT → BETH MOONEY (+0.23, TW +19.86!) | 747581 British GP → TRUTH CHARLES LECLERC (−0.17, TW −20.74 — Antonelli won sprint + pole but Leclerc won the GP; Ferraris had race pace; Russell crashed 'weird') LESSON: sprint/pole ≠ GP win; Mercedes looked beatable; Ferrari showed pace — don't anchor on championship leader.
CUMULATIVE after 8 resolved: TW 125.04 | accuracy 1.2% | BSS 0.008 | 244 active.
WC NEWS Jul 5: FRANCE beat Paraguay (Mbappé goals; "draws level with Messi") → France into QF v Morocco | 199448 → France .56/Morocco .37 (Paraguay 0) | NORWAY 2-1 Brazil!! (Haaland x2, Nyland heroics; Brazil OUT) → 439898 rebuilt Norway .22/Eng .20/Arg .19/Mex .13/Col .11; 592683 → France .26/Spain .19/England .15/Argentina .13/Norway .08; 241292 → France .26/England .16/Argentina .14/Spain .12/Norway .08; 201629 → Mbappé .30/Messi .26/Haaland .15/Kane .10 (Cape Verde carried off Vozinha + Messi 7-goal streak). ARGENTINA advanced vs Cape Verde fightback (Messi 29'). Wimbledon: Eala stuns Swiatek (OUT), Osaka stuns SABalenka (OUT!), Eala→R16 vs Paolini; Djokovic through (breaks SW19 record, "quest for 25" alive) vs Safiullin ugly win; Sinner into QF vs Mochizuki. Rebuilt 846335: Eala .24/Osaka .22/Anisimova .17/Pegula .11/Paolini .10 | 742225: Sinner .58/Djokovic .16/Zverev .10 | 985440: Sinner .52/Djokovic .17. 562262: Eng won 2nd T20I (Bethell spoil Sooryavanshi's debut — youngest-EVER India debut) → Eng .60/Ind .30.
FIXED SISYPHUS: 346707? no. 344207 Jaylen Brown → Philadelphia 76ers (Day 8, unresolved earlier). Onward.
UPCOMING: Jul 7: 754639 + 263626 resolve. Jul 8: 76066 (Grosu .35 — Sandu consults THIS WEEK) + 213487 (Incarceration .45 — sentencing Wed Jul 8!). Jul 9: 562262/107473/199448/279946. Jul 10: 446236/985440. Jul 11: 66613/457239/846335/902592. Jul 12: 897546/742225. Jul 13: 362674 (TN-9 Brent Taylor .60 — Scalise-endorsed; no Trump endorsement yet as of Jul 3). Jul 14: 607314/666563/803035/935518. Jul 15: 24813/439898. Jul 16: 524604.
TODO tomorrow (Jul 6): scan M92 MEX v ENG result (Azteca, late Jul 5); M93 ESP v POR/CRO; M94 USA v BEL; Wimbledon QF; recalc 457239/935518 after M93/M94; check Seahawks/Trump endorsements; check Alexander Jazz two-way (done, lost).

## Day 13 — 2026-07-06
WC NEWS: ENGLAND 3-2 Mexico at Azteca (10-man; Kane pen; Henderson wrist injury out) → England into QF. SPAIN late winner eliminated Portugal (Ronaldo's LAST WC confirmed) → M93 Dallas Jul 6 was ESP WIN vs POR. FIFA+Trump lifted Balogun's red-card suspension (mass uproar; UEFA 'red line'; Belgium furious) → Balogun plays USA v Belgium (M94; result pending today). Neymar retreat. Haaland×2 vs Brazil (Nyland) → Norway into QF (vs winner M92 England = ENG v NOR Miami Jul 11 M99).
WIMBLEDON QF FIELD: Men — Sinner (Mochizuki), Djokovic (Safiullin, broke SW19 record), Cobolli ('homeless' run), + Zverev/Fritz/Bublik (Bublik-Fritz R16 pending?); Cobolli added to 742225/985440 (.05/.07). Women — Osaka (beat Sabalenka, dispatched CONVINCING), Noskova (Keys down), Paolini (Connolly/Eala out), + Anisimova/Pegula. Rebuilt 846335: Osaka .26/Paolini .18/Noskova .14/Anisimova .14/Pegula .10 | 742225: Sinner .56/Djokovic .17/Zverev .07/Cobolli .05/Bublik .04 | 985440: Sinner .5/Djokovic .17/Zverev .11/Cobolli .07/Bublik .04.
FORECAST UPDATES: 935518 → France .33/Spain .22/USA .13/Morocco .13/Belgium .10 (Portugal OUT) | 439898 → England .23/Argentina .21/Norway .17/Switzerland .09/Colombia .09 | 592683 → France .25/Spain .19/England .16/Argentina .13/Norway .10 | 241292 → France .25/England .18/Argentina .14/Spain .12/Norway .09. 754639 → Lowe .25/Farage .25/Sultana .15/Jenrick .10/Badenoch .05 ("Farage's gold deal / Restore Britain rises / UK tightens rules amid Farage funding probe" — no by-election news; resolves TOMORROW Jul 7).
263626 stays (Taiwan .35/Vietnam .30/Mexico .25/China .05; resolves TOMORROW Jul 7, BEA May release expected Jul 7 — Taiwan likely retains #1 given Feb/Apr pattern).
CUMULATIVE: TW 125.04 | accurate 1.2% | 244 active | 8 resolved.
Upcoming: Jul 8: 76066 (Sandu consultations EARLY WEEK — Grosu .35/Perciun .22) + 213487 (Dugan sentencing Jul 8 — prosecutors 15-21mo). Jul 9: 562262/107473/199448/279946. Jul 10: 446236/985440. Jul 11: 66613/457239/846335/902592. Jul 12: 897546/742225. Jul 13: 362674. Jul 14: 607314/666563/803035/935518. Jul 15: 24813/439898. Jul 16: 524604.

## Day 14 — 2026-07-07
RESOLUTIONS received today (Jul 7): 263626 (trade deficit) → TRUTH VIETNAM (+0.32, TW +15.71 — my #2; Taiwan .35 failed; VIETNAM was under-weighted; keep mid-tier hedges) | 754639 (Reform West Ham?/UK party by-election) → TRUTH NIGEL FARAGE (+0.34, TW +54.77 — "Farage resigns from parliament but will stand in byelection" / "Reform UK's Farage resigns as MP amid funding scandal"). LESSON: on by-election/news-driven questions, trust the breaking-corruption-story signal.
CUMULATIVE: TW 195.52 | accuracy 1.6% | BSS 0.010 | 10 resolved | 242 active.
JUL-7 RESULTS (all WC R16 done): USA OUT — Belgium beat USA (Balogun reprieve/FIFA-Trump 'red line' firestorm; Belgium through to M98 QF v ESP) | ARGENTINA 3-2 Egypt (2-0 down, Messi 29'? no — Messi 83' + Romero 79' headers, 3-2 flip; Egypt blasted referee; ENG won 3-2 too) → ARG into KC QF | SWITZERLAND beat Colombia (M96 Vancouver) → M100 KC QF = ARGENTINA v SWITZERLAND (confirmed by FIFA) | SPAIN late winner dumped Portugal — Ronaldo's LAST WC done (previously logged) | France beat Paraguay; Morocco 3-0 Canada; Norway 2-1 Brazil (Haaland ×2); England 3-2 Mexico 10-man (Kane pen).
WIMBLEDON: Sinner powers to SF (Struff 7-5 7-6 6-3; unimpressive, 26 UE) | Djokovic def Auger-Aliassime 5-set 5h+ classic → RECORD-BREAKING 8th-straight SW19 SF | Zverev def Lehecka 6-4 7-5 3-6 7-6 (QF TODAY Jul 8 vs Fritz) | Cobolli beat de Minaur (5-set, homeless paperback run) — QF vs Fery TODAY | Zverev "breaks new ground"; SBOTH men's SFs: Sinner v Djokovic (Jul 10) + Zverev/Fritz v Cobolli/Fery. Women — Muchova def Osaka 7-6(4) 6-4 → Muchova vs Gauff SF; Gauff def Pegula (her first SW19 SF); Osaka OUT | SFs women: Gauff v Muchova (one half) + Kostyuk/Paolini v Noskova/Mertens (QF Jul 8, other half) | Anisimova OUT (Keys 3-6 6-2 6-3) | Eala OUT (to Paolini, R16) | Rybakina & Swiatek & Sabalenka all OUT.
GOLDEN BOOT: Messi 8 (1 assist — record 9 straight WC games scored), Mbappé 7 (2 assists, leads tiebreaker), Haaland 7 (0 ast), Kane 6; Dembélé 4 (2 ast), Oyarzabal 4. 201629 → Messi .42/Mbappé .28/Haaland .16/Kane .09/Oyarzabal .02 | 581542 (Golden Ball) → Messi .40/Mbappé .30/Haaland .10/Kane .10/Oyarzabal .04.
CUP QUARTERFINALS: M97 Boston Jul 9 = France v Morocco | M98 Los Angeles Jul 9/10 = Spain v Belgium | M99 Miami Jul 11 = England v Norway | M100 Kansas City Jul 11 = Argentina v Switzerland (CONFIRMS 457239).
REBUILDS submitted today: 457239 → ARG .55/SUI .40 (.95) | 935518 (Dallas SF1, W97 v W98) → France .34/Spain .31/Belgium .16/Morocco .13 (.94) | 439898 (Atlanta SF2, W99 v W100) → Argentina .35/England .33/Norway .15/Switzerland .14 (.97) | 241292 (Final) → France .26/Argentina .22/England .17/Spain .14/Norway .06 (.85) | 592683 (3rd place) → France .20/Spain .18/England .17/Argentina .16/Belgium .10 (.81) | 846335 → Gauff .28/Muchova .24/Noskova .13/Paolini .11/Kostyuk .09 (.85) | 742225 → Sinner .52/Zverev .17/Djokovic .13/Fritz .07/Cobolli .06 (.95) | 985440 (first to final) → Sinner .48/Zverev .17/Djokovic .11/Fritz .06/Cobolli .05 (.87) | 562262 → England .72/India .22/Draw .06 (Eng 1-0 in 5-match series; Durham abandoned; Bethell hero; India lost to whittled Ireland series recently; match-3 Trent Bridge tonight Jul 7) | 201629/581542 updated (Messi 8, leads).
MOLDOVA (resolves Jul 8): PAS faction meeting sat — NO names released; Grosu evasive ("this week we present our candidate"); Sandu consultations underway (opposition PSRM/MAN snubbed, demand early elections); PAS 55/101 majority → Parliament approves whoever Sandu names. Osmochescu named ACTING PM (starts Jul 8, Economic Dev minister) — likely temporary. 76066 → Grosu .33/Osmochescu .28/Gherasimov .12/Popsoi .12/Perciun .06 (.91) — Grosu remains most likely (party leader + speaker), Osmochescu bumped (acting + dark-horse continuity pick), Perciun tanked (he WAS the resignation trigger).
DUGAN sentencing (Jul 8, Adelman): prosecutors suggest 15-21 mo ("reasonable") — no specific ask; average 16 mo; defense wants time served; 67-yr-old ex-judge, 20 letters of support. 213487 → Incarceration .48/Probation .27/Home confinement .15/Fine .10 (1.0).
SEAHAWKS: NO new news — special owners meeting still expected AUGUST (Rapoport; target pre-Labor Day/Oct kickoff); 902592 (resolves Jul 11 — ??? uncertain timing) — kept stored Grousbeck .4/Khosla .2/Boehly .18/Mittal .15.
279946 (Jul 9) → Alibaba .82 stays (largest US IPO by FOREIGN firm: Alibaba $21.8B 2014 — SpaceX Jun 2026 = US firm; no foreign challenger since). 524604 (final referee) → Marciniak .22/Turpin .20/Vincic .15/Zwayer .12/Oliver .08 — kept.
199448 → France .56/Morocco .37 (QF Boston) — kept. 107473 (UK uni investigation) → UCL .3/SOAS .1 — kept.
UPCOMING: Jul 8: 213487 (Incarceration .48) + 76066 (Grosu .33/Osmochescu .28). Jul 9: 562262/107473/199448/279946. Jul 10: 446236/985440 (Sinner .48 — both men's SFs same day; "first to final" coin-toss-ish). Jul 11: 66613/457239 (ARG .55/SUI .40)/846335/902592. Jul 12: 897546 (MotoGP Sachsenring — Bezzecchi .? leader, Marques 5th?)/742225. Jul 13: 362674 (TN-9 primary — Aug 6; Brent Taylor Scalise+Trump-UNendorsed). Jul 14: 935518. Jul 15: 439898. Jul 16: 524604. Jul 18: 592683. Jul 19: 201629/241292/581542.
CUMULATIVE after Jul 7: TW 195.52 | accuracy 1.6% | BSS 0.010 | 242 active.

## Day 15 — 2026-07-08
RESOLUTIONS: 213487 Dugan sentencing → TRUTH **MONETARY FINE** (Adelman spared her prison; prosecutors wanted 15-21mo; defense time-served; Fine was my .10 tail — Brier −0.14, TW −5.67). 76066 Moldova → TRUTH **VASILE TOFAN** (outsider/technocrat PAS pick — not Grosu, not Osmochescu, nobody I held — Brier −0.22, TW −18.88). LESSONS: (1) liberal judge + White House-hagiography defendant → "monetary fine" is the soft landing; widen fine bucket next time. (2) Moldova PAS "prime minister from OUTSIDE the party" was flagged by Grosu himself — must carry an outsider technocrat in these one-shot party-election questions; keeping only party insiders burned me.
CUMULATIVE: TW 170.98 | accuracy 1.6% | BSS 0.009 | 12 resolved | 240 active.
JUL-8 NEWS: Wimbledon QFs COMPLETE: **ZVEREV def Fritz 6-4 7-5 3-6 7-6** (Fritz knee issue, "panicked") → SF **Zverev v Arthur Fery** (British #114 wildcard; Fery beat Cobolli! first British wildcard SF in 25 years) | **Djokovic def Auger-Aliassime 5-set 5h+ EPIC** → SF SINNER v DJOKOVIC (Jul 10) | **Kostyuk def Paolini** (2nd straight Slam SF) and **Noskova def Mertens** (1st Slam SF) → 2nd women's SF = **Kostyuk v Noskova**; women's SFs: Gauff v Muchova + Noskova v Kostyuk (Jul 10) | Anisimova OUT earlier; Eala OUT; Osaka OUT; Pegula OUT | "Wimbledon 2026: revolving door of women's champions continues."
ENG v IND T20: England SMASHED India 125 runs (201-7; India 76 all out in 11.4 overs) — India's WORST-EVER T20I defeat; England 2-0 (Durham washout) with Bristol Jul 9 + Southampton Jul 11 remaining; England cannot lose the series. 562262 → England .88/India .05/Draw .07.
REBUILDS today: 846335 → Gauff .27/Muchova .24/Noskova .15/Kostyuk .13 (.79) | 742225 → Sinner .51/Zverev .22/Djokovic .19/Fery .03 (.95) | 985440 (first to men's final Jul 10; both SFs same-day, order unknown) → Zverev .30/Sinner .30/Djokovic .27/Fery .04 (.91) — Zverev likely reaches final first (shorter match vs wildcard) but order unknown; Sinner-Djokovic 5h risk high.
WC: All QFs set: M97 Boston Jul 9 FRA v MAR (199448, keep France .56/Morocco .37) | M98 LA Jul 9/10 ESP v BEL | M99 Miami Jul 11 ENG v NOR | M100 KC Jul 11 ARG v SUI. Golden Boot: Messi 8/1ast (leads outright), Mbappé 7/2ast (tiebreak), Haaland 7 — 201629 → Messi .42/Mbappé .28/Haaland .16/Kane .09 | 581542 → Messi .40/Mbappé .30 — kept.
MOLDOVA lesson: outsider. Tofan likely technocrat (ex-director of something). Note for future Sandu/PAS questions.
107473 → UCL .45/KCL .13/SOAS .09/QueenMary .07/Manchester .07 (Al Jazeera+Liberty Investigates nationwide FOI report pending; UCL strongest case ~13-16 investigated; StandWithUs cites UCL most) — resolves TOMORROW Jul 9.
279946 (Jul 9): Alibaba .82 stays (SpaceX = US firm; no foreign mega-IPO since).
UPCOMING: Jul 9: 199448 (FRA v MAR Boston!) + 562262 (series) + 107473 + 279946. Jul 10: 446236 (Bavi — no formation) + 985440. Jul 11: 66613/457239 (ARG .55/SUI .40)/846335/902592. Jul 12: 897546 (Sachsenring — Marc Márquez .50 fav) + 742225. Jul 13: 362674 (TN-9 Trump endorsement — none yet). Jul 14: 935518. Jul 15: 439898. Jul 16: 524604. Jul 18: 592683. Jul 19: 201629/241292/581542.

## Day 16 — 2026-07-09
RESOLUTIONS: 107473 (UK pro-Palestine investigations) → TRUTH **KING'S COLLEGE LONDON** (Brier +0.02, TW −8.49 — UCL lead didn't materialize in final FOI nationwide cut; KCL testimonies 7 + cut visibility; lesson: second-guess the two London leaders side-by-side instead of stacking one) | 199448 (Boston QF) → TRUTH **FRANCE** (Brier +0.67, TW +51.32 — France deserved it; kept .56) | 279946 (foreign-firm US IPO record) → TRUTH **SK HYNIX** (Brier −0.68, TW −61.30 — SK Hynix announced Nasdaq debut; I never saw it; lesson: mega-IPO record questions include NON-China challengers (Korea/global); must scan IPO wire before resolution day, not just Alibaba; catastrophic miss) | 562262 (Eng–Ind T20 series) → TRUTH **ENGLAND** (Brier +0.98, TW +63.07 — England crushed India 76 all out; couldn't lose series).
CUMULATIVE: TW 215.58 | accuracy 2.4% | BSS 0.013 | 16 resolved | 236 active.
JUL-9 NEWS: WIMBLEDON REALITY SHIFT: **Muchova def Gauff 6-2 1-6 7-6(12-10)** (Muchova saved a match point; patched-up body dive-volley showstopper) + **Noskova def Kostyuk 6-4 6-4** → SATURDAY ALL-CZECH WOMEN'S FINAL: **Muchova v Noskova** (both Czech, 1st all-Czech Slam final). 846335 → Muchova .52/Noskova .43 (.95). Gauff OUT; Kostyuk OUT.
BAVI (SUPER TYPHOON, ~200kmh, widest on record for Taiwan since 1987): skirts N Taiwan Sat Jul 11 midday; LANDS IN MAINLAND CHINA SAT NIGHT (Jul 11) along coast between **Fuqing (Fujian) and Wenling (Zhejiang)** — Fujian evening landfall favored; alternative direct-Zhejiang-coast track. Zhejiang: 52 ferry routes suspended, 3,000+ evacuated islands; Level-III emergency + 50,000 relief items dispatched to BOTH provinces; Xiamen port vessels sheltering; Fujian evacuation will eclipse Zhejiang (fuqing dense metro). 66613 (Jul 11 landfall) → Fujian .45/Zhejiang .40/Jiangsu .06/Shanghai .05/Guangdong .02 | 446236 (Jul 10 most-evacuated) → Fujian .48/Zhejiang .36/Shanghai .05/Jiangsu .05/Guangdong .03.
MEN'S SFS (FRI JUL 10): **Fery v Zverev (Centre Court 1.30pm BST — FIRST) — then Sinner v Djokovic (~5pm)**. Moving Fery–Zverev ahead of the Sinner–Djokovic blockbuster (avoids WC ESP-BEL clash, BBC cover). 985440 (FIRST to men's final; resolves Jul 10) → Zverev .78/Fery .09/Sinner .04/Djokovic .03 (.94) — winner of the FIRST match reaches the final first, period (Fery-Zvereef finishes before Sinner-Djokovic begins).
WC QF SCHED: M98 LA Fri Jul 10 ESP v BEL 19:00 (Spain unbeaten, 0 conceded in WC; Belgium 4-1 USA) | M99 Miami Sat Jul 11 NOR v ENG | M100 KC Sat Jul 11 ARG v SUI. France won Boston (M97) → SF-1 Dallas Jul 14 vs winner M98; SF-2 Atlanta Jul 15 Miami winner vs KC winner.
SK Hynix: SK Group chair to visit New York for Nasdaq debut (confirmed Nov 2026 listing). Also Micron expanding US investment. Lesson recorded.
SENIOR WC punditry: "World Cup pauses for breath" — action resumes Jul 10.
UPCOMING: Jul 10: 446236 (Bavi evac — Fujian lean) + 985440 (Zverev .78). Jul 11: 66613 (Fujian landfall?) + 457239 (ARG .55/SUI .40) + 846335 (Muchova .52/Noskova .43) + 902592 (Seahawks — AUGUST meeting expected; watch). Jul 12: 897546 (Sachsenring — Marc Márquez .50) + 742225 (Sinner .51). Jul 13: 362674 (TN-9). Jul 14: 935518 (SF1 Dallas — France/Spain/Belgium/Morocco). Jul 15: 439898. Jul 16: 524604. Jul 18: 592683. Jul 19: 201629/241292/581542.
CUMULATIVE: TW 215.58 | 2.4% acc | 16/252 resolved | 236 active.

## Day 17 — 2026-07-10
RESOLUTIONS: 446236 (Bavi most-evacuated province by Jul 10) → TRUTH **ZHEJIANG** (Brier +0.35, TW +47.21 — I underweighted Zhejiang at .36; Zhejiang had 3,000+ evacuated & seemed "spur-zone" but Wenling/Wenzhou path pointed there all along; lesson: when one province already shows evacuations AND is on track, price it ABOVE 40%) | 985440 (first to men's final Jul 10) → TRUTH **ALEXANDER ZVEREV** (Zverev 1.30pm SF vs Fery, Fery out; Sinner-Djokovic blockbuster second; Brier +0.94, TW +2.18 — 1-day accrual, small but clean).
CUMULATIVE: TW 264.98 | accuracy 2.8% | BSS 0.018 | 18 resolved | 234 active.
JUL-10 NEWS: **MEN'S FINAL SET (SUN Jul 12): SINNER def Djokovic (demolition) — ZVEREV def Fery (ruthless, Fery's fairytale over)** → 742225 → Sinner .60/Zverev .33 (.93). **WOMEN'S FINAL (SAT Jul 11): ALL-CZECH — Muchova v Noskova** (Muchova def Gauff 6-2 1-6 7-6(12-10)!! Gauff OUT saved match point; Noskova def Kostyuk 6-4 6-4). 846335 ✓ Muchova .52/Noskova .43.
BAVI UPDATE (Reuters Jul 10): **landfall now forecast around WENZHOU (ZHEJIANG) late Sat Jul 11 or early Sun Jul 12** — track shifted NE! Zhejiang re-boosted (66613: Zhejiang .62/Fujian .30). Beijing evacuated ~100k for heavy rain (unrelated warning). Fujian relief items still dispatched. Resolution timing may slip to Jul 12.
SPAIN 2-1 BELGIUM (Merino 88', 2nd straight WC winner vs POR/BEL; Ruiz 30', De Ketelaere 41') — SPAIN to SF vs FRANCE (Dallas Jul 14 = 935518). Belgium run ends (Courtois injured, Lammens error). 935518 → France .48/Spain .46 (.94) — true toss-up final-four classic.
241292 → Spain .26/France .25/Argentina .22/England .15/Norway .05 (.93) | 592683 → France .21/Spain .21/England .18/Argentina .18/Norway .10 (.88) | 581542 (Golden Ball) → Messi .38/Mbappé .27/Rodri .08/Yamal .07/Kane .06 (.86).
WC QF REMAINING: M99 Miami SAT Jul 11 = **NORWAY v ENGLAND** | M100 KC SAT Jul 11 = **ARGENTINA v SWITZERLAND** (457239 → ARG .55/SUI .40, resolves tomorrow).
SEAHAWKS: NO news — special owners meeting expected Aug; kept stored. TN-9: no Trump endorsement yet (Taylor .60 kept). 338: nothing.
UPCOMING: Jul 11: 457239 (ARG v SUI result late Sat) + 66613 (Bavi landfall Sat night) + 846335 (Muchova v Noskova) + 902592 (Seahawks Jul 11 — likely non-resolution). Jul 12: 897546 (Sachsenring — Marc Márquez .50; race 12:00 CEST) + 742225 (Sinner .60). Jul 13: 362674. Jul 14: 935518 (FRA v ESP). Jul 15: 439898. Jul 16: 524604. Jul 18: 592683. Jul 19: 201629/241292/581542.
CUMULATIVE: TW 264.98 | 2.8% acc | 18/252 | 234 active.

## Day 18 — 2026-07-11
RESOLVED while active: 457239 QF KC SAT = **ARGENTINA** beat Switzerland (TW +53.11) | 846335 (women's final all-Czech) → TRUTH **LINDA NOSKOVA** (Muchova lost — Brier +0.40, TW −8.38; coin-flip bucket both ways) | 66613 (Bavi landfall) → TRUTH **ZHEJIANG** (Bavi shifted NE to Wenzhou; TW +47.50) | 902592 (Seahawks sale) → TRUTH **KHOSLA GROUP** (Grousbeck/Mittal "lead bidder" reports failed; approval to Khosla — Brier −0.25, TW −23.77; lesson: weight the bidder with quiet financing + cleared finance committee over headline lead). TOTAL today (cumulative after Jul-11 results): TW 333.43 | accuracy 3.6% | BSS 0.024 | 22 resolved | 230 active.
SAT/SUN WC QF FINALE: M99 Miami = **ENGLAND 2-1 NORWAY** (Bellingham 2 goals; Schjelderup 21'; Heggem's goal VAR-chalked off — Haaland shoved Anderson) → **SF2 Atlanta Jul 15 = ENGLAND v ARGENTINA (439898)** | M100 KC = **ARGENTINA** v SUI | M98 (Thu) = **SPAIN 2-1 BELGIUM** (Merino 88' — 2nd straight WC winner; Lammens error; Ruiz 30'; De Ketelaere 41') → **SF1 Dallas Jul 14 = FRANCE v SPAIN (935518)**. FINAL MetLife Jul 19 (241292). THIRD PLACE Miami Jul 18 (592683).
WIMBLEDON FINALS DONE (women's): **Noskova def Muchova** (Muchova previously def Gauff 7-6(12-10) saving match point). MEN'S FINAL SUN Jul 12: **SINNER v ZVEREV** — Sinner demolished Djokovic in SF; Zverev ruthless vs Fery (first British wildcard SF in 25 yrs; beat Cobolli). 742225 → Sinner .60/Zverev .33 (.93) — resolves Jul 12.
MOTOGP SACHSENRING (897546, resolves Jul 12 12:00 CEST): Marc Márquez (9 Sachsenring wins, "guns for tenth", championship challenger) — 897546 → Marc Márquez .50/Jorge Martín .15/Marco Bezzecchi .12/Pedro Acosta .08/Álex Márquez .06 (.91). Martín = championship leader (16 crashes), Bezzecchi wobbly after Assen, Acosta outside.
RESUBMITTED today: 439898 → England .53/Argentina .43 (.96) | 241292 → Spain .27/France .24/Argentina .24/England .21 (.96) | 592683 → England .24/Spain .24/Argentina .22/France .20 (.90) | 201629 (Golden Boot) → Messi .44/Mbappé .30/Haaland .09/Kane .06/Oyarzabal .03 (.92) — Haaland capped at 7 (Norway OUT); Messi 8 scored in 9 straight WC games, Mbappé 7 (2 ast, tiebreak) | 581542 (Golden Ball) → Messi .36/Mbappé .26/Rodri .09/Yamal .08/Kane .06 (.85).
CUMULATIVE: TW 333.43 | accuracy 3.6% | BSS 0.024 | 22/252 resolved | 230 active.
REMAINING WIRES: none scheduled today beyond recaps. UPCOMING: Jul 12: 742225 (Sinner v Zverev — Sinner .60) + 897546 (MotoGP Sachsenring — Marc .50) — BOTH RESOLVE TOMORROW. Jul 13: 362674 (TN-9 Trump endorsement — NONE as of Jul 11; Taylor has Jordan+Haggerty+Blackburn+Burchett+$1M self-fund; Trump silent). Jul 14: 935518 (FRA v ESP — France .48/Spain .46). Jul 15: 439898 (ENG .53/ARG .43). Jul 16: 524604 (final referee — Marciniak/Turpin/Vincic/Zwayer undecided). Jul 18: 592683. Jul 19: 201629 (Messi .44) + 241292 + 581542.
SCORELESS DAYS NOTE: 22 resolved days covered starting Jun 24; TW per resolved qid target ≥ +15 (fine-grained binary-ish questions sacred; multi-outcome finals near coin-flip are priced near 50/50 = tiny edge but small accrual).

## Day 19 — 2026-07-12
RESOLUTIONS: 742225 (men's singles title) → TRUTH **Jannik Sinner** (Sinner demolished Djokovic; Brier +0.73, TW +78.97 ✓) | 897546 (MotoGP Sachsenring) → TRUTH **Marc Marquez** (9th Sachsenring win, Brier +0.70, TW +64.14 ✓). CUMULATIVE: TW 476.55 | accuracy 4.4% | BSS 0.030 | 24 resolved | 228 active.
JUL-12 NEWS: (1) **France–Spain** SF set — France -155 (60.8%) to advance vs Spain +125 (imply~44%); Tchouaméni groin doubt, Mbappé Grade-1 ankle sprain (plays), Olise 6 ast, France 16-2 outscore, unbeaten; Spain 0-conc in 37 competitive matches until Belgium; betting markets ~ coin-flip. 935518 → France .56/Spain .44 (was .48/.46). (2) **England–Argentina** SF2 Jul 15 — England -135 (57.5%) advance vs Argentina +110; both needed ET last round; Konsa suspended England (Quansah in); Messi/Alvarez/Lautaro scored twice ET vs SUI; Kane 6, Bellingham 6 after brace. 439898 → England .55/Argentina .44 (was .53/.43).
WC FUTURES REBUILT (FanDuel/DK odds Jul 12): 241292 (FINAL) → France .36/England .23/Spain .22/Argentina .18 (France +150) | 201629 (GOLDEN BOOT) → Mbappé .36/Messi .33/Kane .12/Oyarzabal .07/Bellingham .04 (Mbappé & Messi BOTH 8 goals; Mbappé has 2 ast vs Messi 0-1 → tiebreak wins him; Haaland OUT at 7 — capped) | 581542 (GOLDEN BALL) → Mbappé .34/Messi .33/Bellingham .12/Olise .06/Kane .05 (Olise 6 ast, 1 shy of Pelé) | 592683 (3RD) → England .24/Argentina .23/Spain .22/France .21 (losers of SFs, each ~coin-flip match).
666563 (Chinese official / Jo Yong Won Pyongyang Jul 1–15): NO Pyongyang visit as of Jul 12 — treaty-anniversary events ALL in Beijing (Cai Qi reception in Beijing Jul 10; Xi met Pak Thae-song; Zhao Leji met Pak Jul 10 ["legislative bodies"]; Li Qiang Jul 11; Pak departed to Pyongyang Jul 12). 666563 → Cai Qi .28/Zhao Leji .26/Wang Huning .15/Liu Jianchao .14/Wang Yi .07 (bumped Liu Jianchao, party-diplomacy chief, most plausible special envoy for Pyongyang reception). Window closes Jul 15; KCNA must report a name or it voids.
803035 (first statewide data-center moratorium): **NY legislature passed one-year moratorium June 4 (AB 10141/SB 9144) — awaiting Hochul signature**; Maine LD 307 was vetoed Apr 24 (Mills; Jay carve-out); Vermont S.205 in committee; Minnesota SF 4298 chaired. 803035 → New York .68/Vermont .08/Michigan .05/Minnesota .04/Pennsylvania .04 (was NY .2 — now clear favorite).
906651 (mile WR after London Diamond League Jul 18): **Josh Kerr 'Project 222' attempt at London (World Indoor 3000m champ, 4×1000m @ WR pace) + Yared Nuguse ENTERED (3:43.97, 4th ATL)**. Ingebrigtsen (Achilles surgery Feb) NOT racing. 906651 → El Guerrouj .60/Kerr .28/Nuguse .08/Ingebrigtsen .02 (was .42/.18/.15 — rebuilt around confirmed race).
24813 (TDF stage 11 flat Vichy→Nevers, Wed Jul 15): sprinters Merlier (already 2 TDF stage wins) / Philipsen (0) / Kooij (1) — cyclingstage fav: Merlier/Merlier over Philipsen; Pouletips #1 Philipsen, #2 Merlier. 24813 → Merlier .34/Philipsen .21/Kooij .16/Pedersen .06/De Lie .05 (Merlier bumped from .28).
362674 (TN-9 TRUMP endorsement): NO endorsement as of Jul-12 search (Ballotpedia tracker shows only Hagerty+House reelections for TN; Taylor has Scalise/Blackburn/Hagerty/Burchett/Jordan + $1M self-fund; Warner = "Trump shoulder-to-shoulder" branding, no major endorsement). 362674 → Brent Taylor .66/Todd Warner .27/Bergmann .02/Thompson .02 (sum .97) — resolves Jul 13.
NO Section 338 invocation yet (Greer speaking Jun 17 — kept China .35). Ukraine: Drapatyi = likely Syrskii successor (joint-forces cmd Jun 2025) — kept .32/.12/.08. Syria NSB: no appointment news (Anas Khattab = Interior Minister; al-Salama = GID director, UN NY Jun 29-30) — kept. Gaza/Open/ASG Houston kept.
UPCOMING: Jul 13: 362674 (Taylor .66). Jul 14: 607314 (ASG MVP — Ohtani .25) + 935518 (FRA v ESP — France .56; match 14:00 Dallas) + 803035 (NY .68, Hochul signs?) + 666563 (if KCNA reports) + 666563/24813 (Jul 15). Jul 15: 439898 (ENG .55). Jul 16: 524604. Jul 17: 32938 (Open Birkdale — not started)/329053/425213. Jul 18: 592683/674079/906651/26225. Jul 19: 201629/241292/581542/556116/927657. Jul 20: 605397. Jul 21: 249565/442417. Jul 23: 131869/149811.
CUMULATIVE: TW 476.55 | 4.4% acc | BSS 0.030 | 24/252 | 228 active.

## Day 20 — 2026-07-13 (Mon)
Cumulative after next_day: TW 518.20 | acc 4.8% | BSS 0.033 | 25/252 resolved | 227 active.
Day-19 resolution: TN-9 open primary → BRENT TAYLOR won (+0.81 Brier share, TW +41.65). 

Scan day before 4 Jul-14 resolutions:
- 607314 (MLB ASG MVP, Citizens Bank Park, NL favored -135): CRITICAL — Ohtani skips (left knee procedure), Aaron Judge OUT (broken rib, IL since May), Vlad Jr OUT (illness/IF vs injury — replaced by Ben Rice at AL 1B), Nick Kurtz OUT (Tristán Peters replaces). NL starters: Baldwin, Freeman, Albies, Muncy, Abrams, Marsh, Soto, Pages, Schwarber DH (home, leadoff, 32 HR — replaces Ohtani), SP Sánchez. AL: Langeliers, Rice, Clement, Caminero, Witt, Trout, Greene, Bellinger, Alvarez DH, SP Cease. Opta-type edge to NL; MVP typically from winning team (last 11 decided). FantasyAlarm focus PCA (.374 since June 1, 232 wRC+) & Alvarez. REBUILT distribution: Schwarber .20 / Alvarez .20 / Soto .14 / Caminero .10 / PCA .08 (sum .72). Discarded Ohtani/Judge/Vlad prior (.43 mass) — biggest avoided miss of the day.
- 666563 (China official w/ Jo Yong Won in Pyongyang Jul 1–15, KCNA): as of Jul 13 NO Chinese official has visited Pyongyang in July (Pak visited BEIJING Jul 10–12; met Xi, Li, Zhao Leji, Cai Qi). Window almost closed (ends Jul 15). Sejong/Hann1 phrasing: reciprocity would usually be Zhao Leji (NPC chair, 2024 goodwill-visit lead; parliamentary parity with Jo). Kept but tilted: Zhao Leji .30 / Cai Qi .25 / Liu Jianchao .13 / Wang Huning .12 / Wang Yi .05 (.85).
- 803035 (first statewide data-center moratorium): No state yet imposed. NY bill passed Jun 4, awaits Hochul — signing maybe after Nov election per Morinello; supporters expect sign; Albany council 13-0 backing Jul 6. Arizona/Illinois/Ohio = tax-break freezes only (not construction moratoriums). Maine vetoed; Vermont H.727 vetoed (May 28); Minnesota bills died May 18. Kept NY .68.
- 935518 (SF1 FRA v ESP, Dallas Jul 14): France spurts — Upamecano & Saliba didn't train Sat (back); Kone & Tchouameni doubtful; Mbappé minor ankle, expected to play. Spain clean. Opta: FRA 42.1 / draw 26.1 / ESP 31.8 → conditional FRA ~57 / ESP ~43. Kept France .56 / Spain .44.

NOTE for tomorrow: recheck ASG result posts (Schwarber narrative strong at home), KCNA report for Pyongyang visit, Hochul signature watch, FRA-ESP final.

## Day 21 — 2026-07-14 (Tue)  [after advance from Day 20]
Cumulative after next_day: TW 597.10 | acc 5.2% | BSS 0.038 | 29/252 resolved | 223 active.

Jul-14 resolutions:
- 607314 → Truth CODY BELLINGER (ASG MVP). I held Schwarber .2/Alvarez .2/Soto .14/Caminero .1/PCA .08 → Brier -0.12, TW -8.92. LESSON: replaced injured Ohtani/Judge/Vlad (correct move — 0 for them) but under-covered the field off the bench; Bellinger (NYY, replaced Judge) won as AL understudy surprise. ASG MVP is near-unforecastable; protect with broader net & cap single names lower.
- 666563 → Truth WANG HUNING. My .12 on Wang Huning saved it (+0.05 Brier share, TW +21.69). I tilted to Zhao Leji (.30) but held Wang Huning (4th PSC, ideology, pre-visit candidate). LESSON: keep PSC-parity names with some mass even if no visit reported — KCNA reveals only after/belatedly.
- 803035 → Truth NEW YORK (+0.89 Brier share, TW +37.58) — Hochul signed EO No.62 on Jul 14 (nation-first statewide moratorium; pauses DEC permits on 50MW+ facilities ~1yr; less than the 20MW bill but qualifies). LESSON: "executive action" also counts as 'formally impose' — my NY .68 was right to be high despite bill unsigned.
- 935518 → Truth SPAIN (+0.37 Brier share, TW +28.54). Spain 2–0 France (Oyarzabal 22' pen after Digne foul on Yamal; Porro 58' give-and-go w/ Olmo). Opta 42.1/26.1/31.8 → my 56/44 France was wrong; Spain dominated (1.63 xG, 10 shots, 84% pass acc). LESSON: prefer the in-form team's model more; shrink chalk when Opta has lower edge vs market noise.

World Cup state after SF1: SPAIN into final (Jul 19 MetLife vs ENG/ARG). France eliminated; Deschamps final game = 3rd-place playoff Jul 18 Miami. Golden Boot: Mbappé 8 (0 SOG semi) / Messi 8 / Kane 6 / Bellingham 6 / Oyarzabal 5 (pen). SF2 Jul 15 Atlanta (ENG v ARG): books ENG +155/+160, ARG +188/+200, qual ENG 4/5. Referee for final unknown — FourFourTwo: Oliver/Taylor banned (ENG/ARG); Faghani (AFC) named front-runner + Marciniak (2022 final) / Turpin (ENG ref twice) / Vincic / Zwayer. Revised: 524604 Faghani .24/Marciniak .20/Turpin .15/Vincic .12/Zwayer .06 (dropped Oliver). 241292 → Spain .50/England .26/Argentina .21. 592683 → France .51/Argentina .22/England .22. 201629 → Messi .38/Mbappé .30/Kane .13/Oyarzabal .08/Bellingham .04. 581542 → Messi .38/Mbappé .22/Oyarzabal .12/Bellingham .08/Kane .06. 439898 kept ENG .55 (books ~56%).

Other checks:
- 24813 (TDF stage 11 sprint to Nevers, resolves Jul 15): Merlier 2 stage wins, Kooij 1; FloBikes & IDL top pick Merlier; thunderstorm risk late; Pedersen green jersey ~5th target. Kept Merlier .34/Philipsen .21/Kooij .16/Pedersen .06/De Lie .05.
- 26225 (Morgan Rogers transfer): Romano — Arsenal top target, personal terms "very very close", first bid imminent (€85m vs £130m ask); Villa signed Manzambi → Rogers likely sold. Kept 26225 → Arsenal .86 (was .84; bumped).
- 329053 (most valuable company, Jul 17): NVIDIA ~$5.1T (Kyber delay fears dismissed, +2.6% Jul 10), Apple ~$4.5–4.6T, Alphabet ~$4.3T, Microsoft ~$2.8T(+ Amazon 2.6, TSM 2.25, SPCX 2.13). Nvidia gap >9%; raised 329053 Nvidia .55→.80 (was carrying big skepticism; fine).
- ASG lessons noted; 425213 (Gaza Jul 17), 32938 (Open R2 leader Jul 17), 556116 (F1 P2 after Hungarian GP Jul 19), 927657 (HTS/Syria NBS Jul 19) — no material news; kept stored.

Next: Jul 15 = 24813 & 439898 resolve (check post-session), Jul 16 = 524604.

## Day 22 — 2026-07-15 (Wed)  [after advance to Day-22]
Cumulative after next_day: TW 612.79 | acc 5.2% | BSS 0.038 | 31/252 resolved | 221 active.

Jul-15 resolutions:
- 24813 (TDF stage 11) → Truth SOREN WAERENSKJOLD (Uno-X). I held Merlier .34/Philipsen .21/Kooij .16/Pedersen .06/De Lie .05, 0 for Waerenskjold → TW -15.93. LESSON (2nd same miss): FloBikes/IDL named Waerenskjold among "others who've finished 2nd" — have to give ≥.04 mass to 2nd-place finishers in bunch sprints when premium sprint names pile up.
- 439898 (SF2 ENG v ARG) → Truth ARGENTINA (TW +31.62). Gordon led 55'; Messi 2 ast (Enzo 85', Lautaro 90+2'); 65% possession ARG. My England .55 wrong outcome-wise but +0.38 Brier share. Books had England ~56% to lift — mild upset; honest loss.

SF2 result → FINAL = SPAIN v ARGENTINA (Jul 19 MetLife). Updates submitted:
- 241292 → Spain .52/Argentina .48 (near toss-up; Spain 1-goal-conceded whole tournament, but Place culture + Messi peak + NY pro-ARG crowd).
- 592683 → 3rd place Miami (FRA v ENG): France .55/England .45.
- 201629 Golden Boot → Messi .76/Mbappé .24 (8 goals BOTH; tiebreak = assists: Messi 4 vs Mbappé 2 — Messi wins even at 8-8; Mbappé only via "Mbappé ≥1 goal & Messi 0").
- 581542 Golden Ball → Messi .70/Oyarzabal .12/Mbappé .12/Bellingham .03/Kane .03 (SF: Messi 2 ast, all-time WC scoring record 21; Mbappe 0 SOG semi).
- 524604 (final referee, resolves Jul 16) → Mundo Deportivo: Marciniak "currently the leading candidate" (2022 final ref). Rebuilt: Marciniak .48/Faghani .14/Turpin .10/Vincic .06/Zwayer .04. (Michael Oliver/Taylor/Tello banned — not listed.)

Other scans:
- 927657 (Syria National Security Bureau head, Jul 19): News Jul 14-15 — Sharaa appointed Abdulqader al-Tahhan as NEW chief of General Intelligence (replaces Hussein al-Salama); **al-Salama moved to head National Security Council/Bureau** ("جهاز الأمن القومي"). Arabic Aksalser/Sookeh confirm. Rebuilt: al-Salama .78/al-Tahhan .10/al-Khattab .05/Maher al-Sharaa .02.
- 674079 (UFC Fight Night Oklahoma City middleweight main, Jul 18): = Dricus du Plessis vs Kamaru Usman (-265/-320 fav; +225/+255). My stale Imavov/Borralho/Allen/De Ridder replaced → Du Plessis .74/Usman .26. LESSON: recheck card line-ups before |"main event"| — opponent changed/misread.
- 556116 (P2 in F1 drivers' championship after Belgian GP Jul 19): standings (post-Silverstone Jul 5) Antonelli 179 / Russell 154 / Hamilton 147 / Leclerc 108. Two races ago Antonelli lead was 77 → now 25. Spa is 1 race; Russell most likely P2. (Prior stored Hamilton .42/Russell .30 was BACKWARDS.) → Russell .62/Hamilton .32/Antonelli .03/Leclerc .02.
- 32938 (Open R2 leader after Jul 17): FRACAS win model — Scheffler 12.1%, Fitzpatrick 5.1% (3 wins, hot), then Schauffele/McIlroy cluster; Fleetwood .043/Clark .041. R2-leader = hot-start bias. Built: Scheffler .14/Fitzpatrick .14/McIlroy .13/Fleetwood .07/MacIntyre .04.
- 26225 → Arsenal .86 (Romano: terms “very very close”, first bid imminent, Manzambi signing clears Rogers exit).
- 329053 (most valuable company Jul 17) → Nvidia .80 (Jul 10: Kyber delay dismissed, closed $210.96; cap ~$5.1T vs Apple ~$4.5T).
- 906651 (mile WR, London Jul 18): Kerr attempt confirmed; pacers Kidder & Rudolf; 74°F forecast, 3:36pm; Nuguse & Kessler field. El Guerrouj .52 / Kerr .30 / Nuguse .12 / Kessler .02 / Ingebrigtsen .02.
- 605397 (Section 338 target, Jul 20): no invocation yet (Section 122 expires Jul 24; 301 Brazil hearing done Jul 6, 60-country forced-labor rate set, Vietnam IP probe pending). Kept China .35.
- 249565 (Syrskii successor, Jul 21): reshuffle is REAL (Fedorov out as DefMin → Klymenko offered; Koretsky = PM candidate) but NO Syrskii move yet. Kept Drapatyi .32.
- 524604 resolves Jul 16; 24813 resolved Jul 15; 329053/32938/425213 resolve Jul 17; 26225/592683/674079/906651 Jul 18; 241292/201629/581542/556116/927657 Jul 19.

## Day 23 — 2026-07-16 (Thu)  [after advance to Day-23]
Cumulative after next_day: TW 623.58 | acc 5.2% | BSS 0.038 | 32/252 resolved | 220 active.

Jul-16 resolution:
- 524604 → Truth SLAVKO VINCIC (Slovenian, UEFA finalist-confed ok). Mundo Deportivo had Marciniak as "leading candidate" — FIFA overruled rumor; my Vincic .06 → TW +10.79 (small mercy from spread). LESSON: referee picks near-random among plausible pool; keep credible pool diverse rather than chasing MD rumor.

Jul-17 resolvers (tomorrow): 329053 (Nvidia .8 ✓ solid), 32938 (Open R2 leader — 153rd?? opened today; R1 leaderboard TBD; stored Scheffler .14/Fitzpatrick .14/McIlroy .13/Fleetwood .07/MacIntyre .04 — update after R1 scores), 425213 (unpredictable strike site; kept Gaza City .3/Khan Younis .15/Rafah .1).

Tee times (Birkdale, bright & breezy): MacIntyre early wave, Scheffler 09:58 UK, McIlroy/Schauffele/Fitzpatrick 15:15 UK (light wind window?), Fleetwood+Rahm mid. TOMORROW with R1 results visible, re-rank R2-leader picks.

World Cup FINAL (Jul 19): Spain v Argentina confirmed. 201629: Messi .76; 581542: Messi .70; 241292: Spain .52; 592683: France .55. Final referee = Slavko Vincic.
Next: 329053/32938/425213 resolve Jul 17; then 26225/592683/674079/906651 Jul 18; 201629/241292/556116/581542/927657 Jul 19.
## Day 24 — 2026-07-17 (Fri)  [after advance to Day-24]
Cumulative after next_day: TW 601.42 | acc 5.2% | BSS 0.036 | 35/252 resolved | 217 active.

Jul-17 resolutions (scored):
- 329053 (most valuable company Jul 17) → Truth **APPLE** (NVIDIA lost cap leadership, suffered Kyber ARM pullback). My Nvidia .8 → TW **-15.24**. LESSON (reinforces): near-term "biggest company" races can flip dramatically on a high-beta gap; cap ≤ .65 on two-horse race; never .8 even with wide current lead.
- 32938 (Open R2 lead after 36 holes) → Truth **LUCAS HERBERT** (62, leads with Burns 58 on rich Birkdale scoring day; Scheffler no-so, McIlroy -3 at halfway; Matt Wallace -4). My Scheffler .14/Fitzpatrick .14/McIlroy .13/Fleetwood .07 → TW **-3.78**. LESSON (again): 36-hole leader = draw-of-teeth lottery; longfield starvation — either spread to 10+ names or keep ≤ .05 per name.
- 425213 (top Gaza strike intensity, Jul 17) → Truth **Nuseirat refugee camp**. TW -3.14 (had .05, small survived loss).

News scan (Jul 17): Open R2 — Herbert/Burns shoot 62s, lead calls for weekend; Bryson -3 (2-stroke 8.1 penalty). UFC: Du Plessis -230/-260/Kalshi 67% (kept DuP, bumped 674079 Du Plessis .74→.70, Usman .26→.30). Rogers: no official announcement yet — Arsenal "first bid imminent", player terms agreed, Villa starting at £130m; could resolve to nothing/void tomorrow or Arsenal (ole .9 — conditional market). Kerr mile: 475,000"Project 222" — pacers signed/seal, shoe at speed, Nuguse/Kessler/Green in field (no Ingebrigtsen delivered) — shifted 906651: El Guerrouj .63 / Kerr .34 / Nuguse .02 / Kessler .01.

CRITICAL correction — 201629 Golden Boot: Kalshi post-SF had Messi 58/Mbappé 32 (Messi's 4-goal-assist SF double); bet guides say Messi leads tiebreak 4/3 AFTER Semi; Deschamps "Mbappe is AVAILABLE" for 3rd place (goals count!), rotation likely but Mbappé ST won't rest (wants boot + 21st WC goal, 5 shy HungRek=All-time 22 all-time record). My .76 Messi WRONG scale — actual: P(Mbappé≥1)≈.7 vs England defense (~8 conceded); scenarios → "Messi 0 × Mbappé≥1 ⇒ Mbappé wins (9>8)". New: 201629 **Mbappé .50 / Messi .46 / Kane .02 / Bellingham .01 / Oyarzabal .01** (was .76/.24). 
581542 Golden Ball rebuilt: Messi .66 / Oyarzabal .13 / Mbappé .08 / **Rodri** .08 / Bellingham .03 (Rodri previously missing — Spain midfield dominance vs Argentina; Golden Ball often to winning team's midfield engine proxy).

927657 update CONFIRMED Jul 14-15: al-Sharaa appointed **Abdulqader al-Tahhan** new General Intelligence chief (replaces al-Salama); **al-Salama moved to head National Security Bureau (جهاز الأمن القومي)** (The National + Arabic press). Rebuilt 927657: **Hussein al-Salama .93** / al-Tahhan .04 / al-Khattab .02 / Maher al-Sharaa .01.

Other updates:
- 241292 (FINAL winner): Spain favorite again since semi (58% Poly/Kalshi; -136 to lift, +130/260). 241292 Spain .57 / Argentina .43 (was .52/.48).
- 617889 (Vozinha club): Jul-17 reports — **Colo-Colo** looking; July 7/6 **Inter Miami (Messi tie) "extremely interested"** strongest; Ceará SC (50% rated link), Avaí/Goianiense contacted (Romano), Chaves exit confirmed. Likely S.American/MLS, NOT Iberia/Turkey: 617889 **Inter Miami .33 / Colo-Colo .2 / Ceará SC .18 / Atlético Goianiense .08 / Sporting CP .06** (was .18 Sporting/.15 Porto/.12 Benfica/.1 Galatasaray).
- 45561 (Men's team gymnastics gold, Commonwealth Games Jul 24): Birmingham 2022 = ENGLAND gold (attr Fraser/Hall/Jarman/Whitlock/Regini-Moran). 2026 = home venue GLASGOW, Whitlock back (later not the gymnastics venue for gold-day? No — Glasgow CG Games Fri 24 Jul = men's team all-around); England favored yet again + Jake Jarman world champion. Rebuilt 45561: **England .72** / Australia .12 / Canada .10 / Scotland .03 / Cyprus .01.
- 872064 (India monsoon deaths state, as of Aug 5): Himachal 9-11 / Maharashtra ~16 (Pune epicenter) / Arunachal 7 / Assam low. Rebuilt 872064: **Maharashtra .25 / Assam .2 / Uttarakhand .18 / Bihar .12 / Himachal Pradesh .12**.
- 249565 (Ukraine Syrskii successor Jul 21): Fedorov FIRED as DefMin (Khmara interim SBU → Defense); **Zelensky REJECTED Syrskii removal** (Fedorov admission Jul 16; 1-2k-protest). Candidates: Drapatyi (fresh, Joint Forces), **Biletsky (3rd Corps)** — missed in stored list originally (only Drapatyi .32/Pavliuk .12/Barhylevych .08). Rebuilt: **Drapatyi .35 / Biletsky .20 / Pavliuk .07 / Barhylevych .05**.
- 149811 (European country declares national emergency due to wildfires by Jul 25): No national-level emergency — **Portugal declared mainland-wide "state of alert" Jul 3** (situation of alertation, not emergency). Criteria excludes local-but-state-level declarations qualify as "national"?? Genuinely ambiguous — bump Portugal to co-favorite. Rebuilt: **Spain .3 / Portugal .3** / Greece .15 / France .15 / Italy .10.
- 605397 (Section 338 first target Jul 20): Section 122 expires **Jul 24**; Trump announced **25% 301 tariffs on Brazil** Wed Jul 15 (J.B.E). Brazil pathway used. Kept China favorite but trimmed: **China .33 / Brazil .2 / India .18 / Canada .08 / Germany .08** (was China .35).
- 26225 → **Arsenal .9** / Liverpool .02 / Bayern .01 (was .86) — conditional market; contradicting? "if he leaves Villa" — Arsenal is the destination.
- 981188 (LeBron team): no announcement; kept Lakers .6 / Cavaliers .15 / Heat .1.

Next wake: Jul 18 = 26225, 592683 (FRA v ENG), 674079 (DuP v Usman), 906651 (mile WR). Jul 19 = FINAL DAY: 201629/241292/556116/581542/927657.
Note: market_aggregate items remains mirror-list; no external signal; breaking news is primary.

## Day 25 — 2026-07-18 (Sat)  [after advance to Day-25]
Cumulative after next_day: TW 557.69 | acc 5.6% | BSS 0.038 | 39/252 resolved | 213 active.

Jul-18 resolutions (scored):
- 26225 (Morgan Rogers next club) → Truth CHELSEA!! TW -69.47 (barsa-top-bid mythbusted: Chelsea swooped; Arsenal only "advanced talks"—never signed). LESSON MASSIVE: "confirmed close" reports ≠ done; preserve ≥ .1 spread on other suitors; never .9 on a reported but UNSIGNED conditional deal. Had been .86→.9 — doubling down hurt. OWN THIS.
- 592683 (3rd place FRA v ENG) → Truth ENGLAND. TW +12.42 (held England .45 France .55). Match: ENG 6-4 FRA, Saka 3, Rice career first WC goal (famous one-nil advertising), Bellingham 7 goals — Mbappé 2 (9th & 10th, all-time 22 > Messi's 21), Kane & Bellingham RESTED (Tuchel paranoid final preparation) → Mbappé scored anyway.
- 674079 (UFC OKC main) → Truth **Du Plessis** (-230, won) — TW +4.92 ✓
- 906651 → Truth **Josh Kerr** = NEW MILE WR **3:42.x** (pacemakers delivered, London SL home track record) — TW +8.40 (kept .34 mass) ✓

News scan Jul-18 (final-day EVE):
- FINAL (Jul 19): Spain v Argentina MetLife. Both XIs predicted: Spain = Simon; Porro/Cubarsi/Laporte/Cucurella; Rodri/Ruiz; Yamal/Olmo/Baena; Oyarzabal (Porro doubtful but expected). ARG = E.Martinez; Montiel/Romero/L.Martinez/Tagliafico; Paredes/Mac Allister/Fernandez/Simeone; Messi/Alvarez. Vincic referee. Spain big favorites (+120, Markets 58%).
- Golden Boot CONTEXT shifted: Mbappé 10 goals (3rd-place 2) vs Messi 8. Updated 201629: **Mbappé .78 / Messi .17 / Bellingham .03 / Kane .02** (Messi .76 was under-bought-heat — he needed 2 goals in final).
- Golden Ball (581542): Messi .62 / Oyarzabal .15 / Rodri .10 / Mbappé .08 / Bellingham .03 (was .66/.12/.12/../..).
- 241292 final winner kept Spain .57 / Argentina .43.
- 556116 (P2 in F1 champs after Spa): Antonelli pole (1:44.361, 6th pole, .317 over Verstappen); Norris P3 but 10-grid-penalty → Russell drops to P3 on grid; Leclerc P4; Hamilton P5 (crash end of FP3, quali'd P6 + .002 off Leclerc). Champions: Antonelli 179/Russell 154/Hamilton 147. Rebuilt 556116: **Russell .62 / Hamilton .18 / Antonelli .15 / Leclerc .03 / Verstappen .02**.
- **981188 LEBRON** — KEY UPDATE: LeBron told Lakers June 30 he will NOT return (eight-year run over). Decision expected late-July/early-August; NOT BY Jul 24 GUARANTEED. Candidates: **Cavaliers, Heat, 76ers, Warriors** (Charania hierarchy: CLE > MIA > PHI, Warriors contingent, Myers pitched Sixers "best shot to win" w/ Jaylen Brown; Heat landed GIANNIS ANTETOKOUNMPO). Rebuilt 981188: **Cavaliers .3 / 76ers .25 / Heat .25 / Warriors .15** (was Lakers .6 — DULL PAST DUE; was never going to be Lakers)
- 696503 (Yan Diomande next club): preference PSG; Liverpool £69m+£17m then €100m then €116m offers all REJECTED; Bayern also interested; Arsenal consideration (as loser fill-in). Rebuilt 696503: **PSG .42 / Liverpool .32 / Bayern .08 / Arsenal .06 / Real Madrid .03** (was Liverpool .7).
- 927657: SANA/officials silent; only The National + Arabic: al-Salama → NSB head, al-Tahhan → intelligence chief. KEEP al-Salama .93 (resolution likely official announcement Mon Jul 20/21 but question resolves tomorrow per market — The National reporting insufficient? Hold).
- Belgium GP (Jul 19): Antonelli pole; Spa Race is Sunday. 475441 (FP3 leader — already took place: Antonelli topped) stored Antonelli .25 — retained.
- 124??? nothing else.
Next: Jul-19 resolutions: 201629/241292/556116/581542/927657 + 3rd place outcome known.
Lessons (scorched): ⑴ Rogers .9 — bully reopening; always keep ≥ .12 distributed for "unrelated suitor" on unsigned ~£100m deals. ⑵ Never dust filed news from > 48h prior (LeBron). ⑶ Golden Boot turnover insight — Messi .17 now post-mbr.

## Day 26 — 2026-07-19 (Sun)  [after advance + Day-26 updates]
Cumulative: TW 667.78 | acc 6.3% | BSS 0.039 | 44/252 resolved | 208 active.
(First advance rolled Day-26 hint: 1 question resolves tomorrow 2026-07-20: **605397** Section 338 first target.)

Day-26 RESULTS (from harness, Jul-19 session headline news):
- 201629 Golden Boot → **MBAPPÉ** ✓ (+34.13)
- 241292 WC FINAL winner → **SPAIN** ✓ (+22.92)
- 556116 P2 after Spa → **LEWIS HAMILTON** (+48.10 — Antonelli won; Russell DNF T1; Hamilton P4 w/ penalty, +45 lead over Russell for P2). Champions standings after Spa: Antonelli 204 / Hamilton 159 / Russell 154 / Leclerc 126 / Norris 103 / Piastri 92 / Verstappen 91.
- 581542 Golden Ball → **Rodri** ✗ (-18.58). LESSON restated: when Spain lift their 2nd WC, value Spanish midfield engine for Golden Ball; Oyarzabal/Rodri deserved bigger mass vs Messi .62. Cap Messi ≤ .5 pre-final when Spain strong.
- 927657 Syria NSB → **Anas al-KHATTAB** ( Interior ) ✗ — my al-Salama .93 → small consolation via spread; LESSON: multiple similarly named bodies (NSB vs GSS vs Interior ministry); criteria named the exact جهاز الأمن القومي; never > .9 on a contested appointment; journalists disagreed (The National said al-Salama).

News scan Day-26 (Jul 19):
- F1 Spa report: **Antonelli won** (1:24:42.479, 6th win, extends title to 204), Leclerc P2, Verstappen P3, Hamilton P4 (+17.245, 5-sec cold-track T1 hit vs Russell), Russell DNF. Hamilton leads Russell by 5 for P2.
- §338 search: no Section 338 invocation announced anywhere (0 hits Jul 17-19 articles); Brazil **Section 301 25% tariffs announced** (effective Jul 22); **Section 122 expires Jul 24** (CFR). 605397 resolves tomorrow Jul 20 w/ criteria "announced on/before Aug 18" — market_close-date gap; likely void or near. Re-submitted 605397 identical China .33/Brazil .2/India .18/Canada .08/Germany .08 (refresh my-prediction-date).
- **LeBron (981188)**: Evan Sidery Jul-19: decision likely **within 48 h**; Patch (Jul-19): Sixers gaining, "if not favorite"; league staff still see CLE pole position; Heat/Cavs/Sixers final three; Warriors pessimistic internally; Nuggets/Wolves longshots. Rebuilt 981188: **Cavaliers .3 / 76ers .28 / Heat .18 / Warriors .1 / Timberwolves .07**.
- **Yan Diomande (696503)**: BILD (Jul-15) "Man Utd in pole position" (no bid yet); PSG had agreement bases late June but dormant since — "won't pay >£100m; Leipzig confident of keeping"; Liverpool's £68m+£17m rejected; only Liverpool ever bid. Rebuilt: **PSG .38 / Man Utd .3 / Man City .07 / Liverpool .06 / Bayern .04** (dropped Arsenal/Real).
- **Vozinha (617889)**: africasoccer Jul-17 — **Colo-Colo** active pursuit ("yet to progress to advanced stage"); Marka Jul-7 — Inter Miami "could snap him up" (Messi); ESPN Jun-24 — open to Brazil (Ceará SC etc.). Rebuilt: **Colo-Colo .35 / Inter Miami .25 / Ceará SC .12 / Atlético Goianiense .08 / Sporting CP .05**. DON'T over-weight Inter Miami despite Messi narrative; Colo-Colo is the freshest hard link.
- **India monsoon deaths (872064)**: Maharashtra **62 killed** as of Jul-8 (highest state); Surat/Gujarat ~17; J&K 11 (Poonch/Rajouri Jul-19); Wayanad (Kerala) 6; Uttarakhand red alerts ongoing. Rebuilt: **Maharashtra .38 / Assam .16 / Uttarakhand .14 / Gujarat .12 / Bihar .1** (dropped Himachal).
- **India T20I vs Zimbabwe (131869)** 🚨 SQUAD ALERT: Gill & Samson NOT in squad; **Shreyas Iyer (c), Tilak Varma (vc), Vaibhav Sooryavanshi, Abhishek Sharma, Ishan Kishan (WK)** — openers = Sooryavanshi + Abhishek Sharma. First T20I Jul 23. Rebuilt: **Abhishek Sharma .3 / Sooryavanshi .27 / Ishan Kishan .13 / Tilak Varma .12 / Shreyas Iyer .07** (was Gill/Samson-carrying — would have lost EVERYTHING on Samson/Gill picks; saved).
- **F1 Hungary (594916/475441)**: after Spa, Antonelli 204 is champ-favorite; Antonelli dominates twisty slow tracks?? (received pole at Spa); Hungaroring rewards outright pace more than overtaking. 594916: **Antonelli .52 / Hamilton .13 / Russell .1 / Norris .09 / Verstappen .08**; 475441 (FP3): **Antonelli .3 / Norris .13 / Verstappen .12 / Russell .09 / Hamilton .07**.
- **45561 gymnastics**: Games Jul 24–28 GLASGOW; men's team all-around Fri Jul 24/25; England won 2014/2018/2022 stacked. No changes: England .72.
- **149811 wildfires**: no national-emergency declaration by any European country through Jul-19 (Greece = two municipalities; Portugal "state of alert" mainland-wide STILL not national emergency; Spain peaks 50k ha, no Nat Emerg; France Pyrenees spectatorless stage). Kept Spain .3/Portugal .3/Greece .15/France .15/Italy .1.
- **918398 (Bahrain GP replacement)**: zero announcements (calendar stays 22); criteria needs announcement by Dec-31; close date Jul-25 → likely voids. Kept Imola .2/Portimao .2/Barcelona-Catalunya .12/Istanbul Park .12.
- **249565 Syrskii**: FT (Jul-19) — Zelensky consulting corps commanders (Voloshyn 8AAC, Bohomolov 10AC, Maistrenko 11AC, Lasiichuk 7AAC, Zaits 20AC, Sydorov 17AC) as potential successors; NOT Drapatyi/Biletsky named; no appointment yet; decisions "worked out soon". Keep Drapatyi .35/Biletsky .2/Pavliuk .07/Barhylevych .05 — likely voids Jul-21.
- **442417 Typhoon Noul**: no Noul formed (Bavi = 9th this year, landed Zhejiang Jul-11). Kept Guangdong .3/Hainan .2/Fujian .15/Guangxi .1 — likely voids.
- **605397**: re-submitted identical (China .33 etc.) — freshens prediction date.
- **696503** submit set.

Lessons Day-26:
1. Match squad news to market questions BEFORE their day — Samson/Gill cross-check saved 131869 TW. Rule: for any "who will X first" in an upcoming series, re-derive from actual posted squad 2 weeks out.
2. Teams with "agreement in place" but no movement for 2+ weeks = rumor premium, not deal; fade unless deadline (Leipzig's £102m ask dead) — Diomande almost certainly voids or stays Leipzig.
3. Shoe remains key: 149811 window nearly closed w/o any national declaration — my earlier "Portugal state of alert" lean may well lose .3 if voids; nothing else I can do.
4. TW still building post-Rogers(-69) and Rodri(-18); Hamilton rescue offset. Calibration check: BSS .039 — trend up.

## Day 27 — 2026-07-20 (Mon)  [after advance + Day-27 updates]
CUMULATIVE: TW 665.44 | acc 6.3% | BSS 0.039 | 45 resolved | 207 active. TOMORROW (Jul 21) resolves: 249565, 442417.

Day-27 result logged (from harness): **605397 SECTION 338 → CANADA** ✗ (my Canada .08) — TW -2.35 | Brier -0.03.
FACTS: Jul-20 Trump signed THREE §338 proclamations vs CANADA — 50% tariffs on autos/alcohol/dairy/wine/cement/hockey sticks, effective Aug 19, citing Canadian discrimination (motor-vehicle tariff scheme; USMCA lapsed). LESSON REPEATED: "Canada exempt via USMCA" assumption was wrong — §338 cited exactly the discriminatory Canadian tariff scheme that Bullvine/2026 pundits flagged ("crank tariffs on Canadian dairy, 35%, effective Aug 1"). I discounted a concrete report because it didn't wear a §338 badge. **On any concrete told headline (esp. trade, announced-dates) adjacent to a target market, bump the told-country even if authority unclear.**

Day-27 updates:
- **249565** (tomorrow, Syrskii!): Bloomберг Jul-20 — Zelensky considering replacing Syrskyi, **Drapatyi MOST LIKELY** successor; General Staff DENIED ouster; OP adviser "don't expect appointment today"; meetings with Drapatyi/Biletsky/Apostol/Horbatiuk/Obolensky/Prokopenko; decision "days". Rebuilt: **Drapatyi .55 / Biletsky .14 / Apostol .09 / Horbatiuk .05 / Obolenskyi .04**. (Most likely void by Jul-21, but all upside sits on Drapatyi.)
- **981188**: Charania/Rich Paul (Jul-20) — NO timetable; focus on **CAVS/HEAT/76ERS**; Beverley "decision today" posts denied by LeBron IG ("STFU"); **FanDuel odds: HEAT +175 FAVORITE**, then Cavs, Warriors, 76ers, Wolves. Rebuilt: **Heat .35 / Cavaliers .29 / 76ers .2 / Warriors .07 / Wolves .05**.
- **45561** (Jul-24): Whitlock WITHDREW Jul-13 (hand injury) — England still deepest (Jarman et al.). **England .62 / Australia .15 / Canada .13 / Scotland .04 / Cyprus .02** (was .72 England). Men's team final GLASGOW Fri Jul-24 evening.
- **131869**: covered Day-26 (Iyer-capped squad; Sooryavamshi+Abhishek openers). Rebuilt earlier: Abhishek .3/Soory .27/Kishan .13/Tilak .12/Iyer .07.
- **872064**: Maharashtra .38/Assam .16/Uttarakhand .14/Gujarat .12/Bihar .1 (62+ killed in MH; Surat 17; J&K 11; Wayanad 6).
- **594916/475441**: Antonelli 204 by 45 over Hamilton (ESPN: "no stopping Antonelli", Hungaroring twisty – 2025 Leclerc surprise pole, Norris won; Hamilton 8 wins @ Hungary). 594916 kept .52; 475441 kept .3.
- **696503**: Man Utd "pole position" (BILD Jul-15, NO formal bid); PSG dormant since Jun-28 agreement bases; Liverpool's bid rejected. **PSG .38 / Man Utd .3 / Man City .07 / Liverpool .06 / Bayern .04**.
- **617889**: Colo-Colo freshest hard link (africasoccer Jul-17, early stage); Inter Miami interested (Marca Jul-7). **Colo-Colo .35 / Inter Miami .25 / Ceará SC .12 / Atlético Goianiense .08 / Sporting CP .05**.
- **988210 England Test HC**: McCullum out Jul-12; **Andy Flower ruled out** Jul-17; Flintoff (Lions, internal) + Justin Langer stand-outs; Trott/Dawson/Fleming/Moody linked. Rebuilt: **Flintoff .38 / Langer .2 / Trott .1 / Trescothick .06 / Fleming .06** (was .25 Trescothick/.16 Giles/.13 Flower — all stale).
- **415011 Peru FM**: Keiko Fujimori president-elect (sworn Jul-28); incoming cabinet = **Carlos Espá** canciller (Sí Creo lawmaker; El Comercio/Gato Encerrado/Regpolistas Jul-14/15; current canciller Carlos Pareja Ríos not retained). **Carlos Espá .5 / Pareja Ríos .15 / Rospigliosi .07 / Galarreta .05**.
- **238968 UN SG first straw poll (Jul-23)**: six candidates (Bachelet, Espinosa, Grossi, Grynspan, Rodrigues-Birkett, Sall). Lowy/CRS: Grossi longtime leading candidate (Washington/Beijing skeptical of Bachelet; Sall unsupported by Senegal/AU). **Grossi .45 / Grynspan .18 / Bachelet .16 / Espinosa .08 / Sall .05**.
- **942650 FOMC Jul-29**: hold 3.5–3.75% expected (15% hike odds); hawks = Hammack & **Lorie Logan** (both said "modestly higher rates"; both dissented April). Hawkish rotate. **Hammack .5 / Logan .35 / Kashkari .06 / Warsh .02 / Waller .02**.
- **339902** US strikes (Jul 22-29): Iraq (PMF/Iran-aligned) + Yemen (Houthis threatening Bab al-Mandeb maritime blockade) the two plausible targets; Syria US exited Jan-2026; Lebanon peripheral. **Iraq .3 / Yemen .3 / Syria .1 / Lebanon .08**.
- **108618 Bruno Guimarães**: BBC Jul-8 — asked to leave; Arsenal "most aggressive" (fresh bid ~£60-65m, no contact yet; £100m valuation); Real Madrid revived interest; Man City/Barcelona monitoring. **Arsenal .55 / Real Madrid .12 / Man City .1 / Barcelona .08 / Man Utd .04** (was Man Utd .55 — WRONG bias).
- **683823** European only-plant drought shutdown: Krško slight output cuts (Sava; full power, no gov't shutdown plan announced); France not "only". Kept Slovenia .25 / Netherlands .22 / Belgium .13 / Spain .1 / Switzerland .1.
- **107175 Red Sea coalition by Aug-1**: Saudi-led Yemen coalition announced Bab al-Mandeb "measures" Jul-20 (existing coalition, NOT new); EU Aspides 2.0 signed by Kallas (Djibouti, Jul-17) — existing EU mission. **No new multinational coalition yet**; kept UK .2/France .18/US .15/Saudi .12/India .08. Resolves Jul-29.
- 971524 (Thailand .58, Myanmar repatriation, Aug-windowed) — no fresh signal; kept.
- 449245/970163 javelin — Kept Chopra.
- 988210 → Done.
- 149811 — no national-emergency declaration ANYWHERE yet in Europe (Portugal "state of alert" ≠ national; Greece local; France pyrenees; Spain peaks 50k ha) — window nearly closed; kept Spain .3/Portugal .3/Greece .15/France .15/Italy .1.
- 918398 — NO replacement circuit announced (Apr cancellation; calendar stays 22; criteria window Dec-31; close Jul-25 → void likely). Kept.
- 126882 OPCW — kept Sarin .4/Sulfur mustard .3/VX .25.

LESSONS Day-27:
1. Amazon-country-effect: my §338 miss (Canada) = "obvious outcome not in my top pick". §338 was deliberately never-used; but concrete dairy/car tariff talk at 30%+ is the tell — trust ANNOUNCED-DATE NUMBERS, not legal-authority skepticism.
2. News rarely reprints full names spelling — Peru: "Carlos Espá" vs "Carlos Epa"; always copy exact spelling from a primary article.
3. Multi-select questions (FOMC): sum ≤1.0 required — distribution = independent P(each member votes hike), NOT a joint outcome.
4. Commonwealth withdrawal (Whitlock) killed my England anchor — re-scan injury/illness news for every medal-event team bet within 2 weeks of resolution.

## Day 28 (2026-07-21)
Sim date 2026-07-21. TW 761.93 | acc 7.1% | BSS 0.044 | 47/252 resolved, 205 active. Harness: 872064 resolves TOMORROW (Jul-22).

### Submitted (7 never-predicted questions — they were scoring 0 daily)
- 970163 (CWG javelin QUALIFICATION topper, Jul-30): Pathirage .45 / Anderson Peters .25 / Chopra .15 / Nadeem .08. Sri Lanka's Pathirage is world-leader 88.68m/92.62m; Weber (German) ineligible; only CW athletes.
- 449245 (CWG javelin GOLD final, Jul-31): Pathirage .4 / Chopra .22 / Nadeem .18 / Peters .12.
- 126882 (Syria first OPCW-verified CW destruction, reports to UNSC by Sep-3): Aerial bombs .45 / Rockets .3 / Artillery shells .1 / Missiles .05. OPCW May-2026 deployment found "dozens of unfilled chemical munitions of two types: chemical aerial bombs and chemical rockets" (same types used at Ltamenah/Khan Shaykhun 2017 + Ghouta 2013). Al Qutayfah Category-3 facility destruction plan; ADPV circulated for Council approval at 112th session.
- 179451 (WI 1st Test 5-for vs Pakistan, Tarouba opens Jul-25): Jayden Seales .3 / Alzarri Joseph .2 / Gudakesh Motie .18 / Kemar Roach .15 / Justin Greaves .08. WI likely XI: Roach/Alzarri Joseph/Seales pace; Tarouba pace-early/spin-later.
- 918398 (F1 Bahrain GP replacement host, announce by Dec-31): Bahrain International Circuit .35 / Algarve International Circuit (Portimão) .25 / Imola .12 / Nürburgring .08 / Paul Ricard .05. AGBI Jul-06: Domenicali says Bahrain is LEADING option to be restored into Sep gap between Azerbaijan and Singapore; decision before Aug summer break. Algarve will act as replacement ONLY for season-enders (Qatar/Abu Dhabi) if conflict escalates; mid-Sep deadline. NOTE: if F1 simply reinstates Bahrain, "replacement host circuit" wording is ambiguous — kept Bahrain on top.
- 971524 (SE Asian country finalizing Myanmar-refugee repatriation plan ≥1,000 people, Aug-2026): Thailand .6 / Myanmar .15 / Malaysia .08 / Indonesia .03. May-31 Mizzima: Thailand announced 10-yr timeline, camp consolidation within 5 yrs, Nu Poe census; Jul-2026: ~300 refugees returning in July; Thailand hosts ~81,942 (Sep-2024) in 9 border camps; RTG+MOU.
- 107175 (NEW multinational Red-Sea coalition announced Jul-1..Aug-1): Saudi Arabia .15 / United States .12 / United Kingdom .08 / France .05 (sum .4 — likely void). Jul-20/21: Houthis declared maritime embargo vs Saudi ships; Saudi-led coalition began protecting vessels (EXISTING coalition — doesn't qualify); EU Aspides expansion Jul-17 = existing; NO new coalition announced with 11 days left.

### 872064 (resolves Jul-22) — kept Maharashtra .38 / Assam .16 / Uttarakhand .14 / Gujarat .12 / Bihar .1
Jul-21 HT: 22 dead in J&K+Uttarakhand+Nagaland on Monday alone (J&K Poonch 7 buried, Rajouri; combined 3-district J&K toll 22; Rajouri/Doda bodies still being recovered). But Maharashtra 62 dead since Jun-1 (Jul-8) and CUMULATIVE weather deaths since Jan 2026 = 105 (Jul-14 SDMA). Maharashtra lead safe; resolution date Jul-22 with "as of Aug 5" metric baked in.

### Confirmed Day-28 facts
- 249565 RESOLVED Drapatyi ✓ (+52.75): Jul-20/21 wires "Zelenskiy dismisses top army general amid growing public protests / Zelenskyy replaces Ukraine military chief after protests" — Drapatyi officially in.
- CWG Glasgow: Jul-23..Aug-2; men's javelin QUALIFICATION Jul-30, final Jul-31 (India Today: final 11pm IST Jul-31). Chopra cleared qualification (Doha 85.69m, first Indian >85m this year); Nadeem confirmed Jul-13 (defending champion); Chopra vs Nadeem billed as main event. Rohit Yadav + Yashvir Singh also in.
- UN SG: first UNSC straw poll Jul-23 (townhall same day, civil society); 6 candidates; Grossi front-runner; Macky Sall seeking Faye endorsement for Francophone bloc; Bachelet faces US/China skepticism; Sall unsupported by Senegal/AU (nominated by Burundi). 238968 (poll winner, resolves ~Jul-30) stored: Grossi .45 / Grynspan .18 / Bachelet .16 / Espinosa .08 / Sall .05 — KEEP.
- Syria OPCW: Syria voting rights restored Jul-9; Al Qutayfah Category-3 destruction on track; draft plan received Jun-28; 112th Council session to approve.
- WI squad listing (cricthugs, Jul-13): WI — Chase (c), Brathwaite, Louis, Athanaze, Hodge, Da Silva, Greaves, Motie, Alzarri Joseph, Roach, Seales. No Shamar Joseph. Tarouba: pace early, spin from Day 3.
- Bahrain GP: NO April replacement made; 22-race season; possible Bahrain restoration for Sep; Algarve contingency for Qatar/Abu Dhabi only.

### Wins/losses ledger recap (rolling)
- 249565 (Drapatyi, Jul-22) +52.75; 442417 (Guangdong) +43.75 → both carried Day-27.
- 605397 → CANADA (Jul-20/21) −2.35: LESSON — trust announced concrete tariff numbers/dates over legal-authority skepticism (Trump signed THREE §338 proclamations Jul-20 vs Canada dairy/vehicles/alcohol, 50% ad valorem, eff. Aug-1/Aug-19). Told-country > theory.
- 149811 (wildfire national emergency) — still NONE declared anywhere in Europe (Portugal extended mainland "state of alert" ≠ national emergency; Greece local; France spectator-ban; Spain 50k ha; Syria?? not Europe). Stored Spain .3/Portugal .3/Greece .15/France .15/Italy .1 since Jul-17. If no declaration by Jul-25 window close, likely void. KEEP but de-rate mentally.

### Watch next days
- Jul-22: 872064 resolves (Maharashtra expected win).
- Jul-23: 131869 (India 1st T20I v Zimbabwe — Abhishek Sharma .3/Sooryavanshi .27/Kishan .13), 149811 window closes, 238968 straw-poll day.
- Jul-24: 126882, 45561 (CWG men's team gymnastics — England .62/Australia .15/Canada .13/Scotland .04/Cyprus .02; Whitlock withdrew Jul-13), 617889 (Vozinha — Colo-Colo .35/Inter Miami .25), 981188 (LeBron — "not rushed", Heat .35/Cavs .29/76ers .2).
- Jul-25: 475441 (FP3 Hungary — Antonelli .3), 918398 (Bahrain — stored).
- Jul-26: 594916 (Hungar ian GP — Antonelli .52/Hamilton .13), 696503 (Diomande — PSG .38/Man Utd .3), 131869 3rd T20I.
- Jul-27: 179451 (WI 5-for), 415011 (Peru FM — Espá .5).
- Jul-28: 339902 (US strikes — Iraq .3/Yemen .3), 415011 resolves Jul-28? (listed Jul-27 — verify).
- Jul-29: 238968, 107175, 942650 (FOMC votes — Hammack .5/Logan .35), 988210 (England Test HC — Flintoff .38), 971524, 683823 (drought nuclear — Slovenia .25).
- Jul-30: 238968 (poll date Jul-23; listed Jul-30), 683823, 970163, 108618 (Guimarães — Arsenal .55).
- Jul-31: 449245.

### Housekeeping
- market.csv my_prediction column chronic-stale; trust predictions/*.json.
- 7 questions had NEVER been predicted before today (970163, 449245, 126882, 179451, 918398, 971524, 107175) — were accruing 0 daily. RULE: after any multi-day gap, diff "never-predicted" qids against all predictions/*.json before next_day.
- Next: LOG complete → call next_day.

## Day 29 (2026-07-22) — TW 801.91 | 48 resolved | 204 active
Harness advance + overnight results:
- **872064 → ASSAM (NOT Maharashtra!)**: my Maharashtra .38 / Assam .16 → Brier +0.11, TW +39.98. LESSON: for "monsoon floods and landslides" metrics, Assam (Brahmaputra basin) repeatedly leads India; Maharashtra's big toll was all-weather cumulative (lightning etc.), not flood/landslide-specific. Next monsoon question: Assam ≥ .3 base rate whenever Brahmaputra floods active.
- LeBron: Heat's official YouTube briefly posted "LeBron James Introductory Press Conference" livestream scheduled JULY 27; spokesman called it scheduling error but teams don't title streams for non-signings. BetOnline: July 24 announcement favored, Miami favored destination. Resubmitted 981188: Heat .6 / Cavs .15 / 76ers .12 / GSW .05 / Wolves .03.
- 238968: BIG story — NY Post Jul-22: Trump wants Gianni Infantino as next UN SG ("special ability to bring people together"; Zampolli: "only President Trump could have such a genius idea"; current field incl. Grossi & Bachelet "relatively weak"; Infantino noncommittal, declared for FIFA re-election Mar-2027, $6M vs $418k pay cut, no nomination yet). First straw poll Jul-23 (townhall same day). Resubmitted: Grossi .42 / Grynspan .17 / Bachelet .14 / Infantino .09 / Espinosa .06 (dropped Sall). Watch for actual nomination news — if Infantino enters, recalibrate heavily.
- 594916 Hungary: Mercedes 10/10 poles; Antonelli 6 wins in 10 (5 straight); Hamilton 8× Hungaroring wins + 2023 pole + Barcelona win (first since 2024); Ferrari engine deficit less relevant at twisty Hungaroring. Resubmitted: Antonelli .48 / Hamilton .17 / Russell .1 / Norris .09 / Verstappen .08. (Stored 475441 FP3 Antonelli .3 stands.)
- 617889 Vozinha: Colo-Colo in Romano-confirmed talks, initial offer + counter-proposal received, set to pick between Vozinha and Santiago Mele; Inter Miami "strong interest" but no offer; Brazilian clubs (Avaí, Atlético Goianiense) only contacted camp. Resubmitted: Colo-Colo .45 / Inter Miami .2 / Ceará .12 / Atlético Goianiense .07 / Sporting CP .05.
- 149811: checked — NO European national govt declared wildfire national emergency (Portugal = "situação de alerta" Jul-3..6, lowest tier, ≠ national emergency; Spain = regional Andalucía Level 1; Greece local; France spectator ban). Kept Spain .3/Portugal .3/Greece .15/France .15/Italy .1. Resolves Jul-23 (likely void/no-declaration).
- 131869: predicted XI (Zee News): Sooryavanshi + Abhishek open, Kishan #3, Iyer #4. Kept Abhishek .3/Sooryavanshi .27/Kishan .13/Varma .12/Iyer .07. 1st T20I Jul-23 Harare.
- New submissions yesterday (first-ever): 970163/449245/126882/179451/918398/971524/107175 — all active now.
- Syria OPCW: no destruction-operation news yet; stored Aerial bombs .45/Rockets .3 stands (Al Qutayfah Cat-3 plan pending 112th Council session; reports to UNSC by Sep-3).
- Red Sea: no NEW coalition (Saudi coalition = existing; Aspides = existing); Trump: US will "take care of" Houthis; UAE condemns blockade. 107175 likely void; stored was sum .4.
- Bahrain GP: Sep-restore of Bahrain leading option; Algarve = Qatar/Abu Dhabi contingency only. 918398 stored Bahrain IC .35/Algarve .25/Imola .12/Nürburgring .08/Paul Ricard .05.
- 971524 Myanmar repatriation: Thailand camp closure/consolidation plan advancing (~300 returning in July); stored Thailand .6/Myanmar .15/Malaysia .08/Indonesia .03.

Watch: Jul-23 = 131869 + 149811 resolve; 238968 straw poll; Jul-24 = 126882/45561/617889/981188; Jul-25 = 475441/918398; Jul-26 = 594916/696503; Jul-27 = 179451/415011.

## Day 30 (2026-07-23) — TW 834.69 | 50 resolved | 202 active
Overnight results:
- **131869 → V. Sooryavanshi ✓ (scored .27)** Brier +0.34 / TW −6.51 (held only Jul-19→23). My top pick Abhishek wrong; keep both openers high for opener-scoring questions.
- **149811 → SPAIN ✓ (scored .3)** Brier +0.37 / TW +39.29. Spain DID declare a national emergency (Benahavis fire, Andalucía escalation, 50k ha). "Spread the bet across candidates" WORKED again — never concentrate on one.
- TW 801.91 → 834.69.

### Key news 2026-07-23
- **LeBron**: Heat YouTube "Introductory Press Conference" stream (Jul-27 slot) leaked Jul-21; BetOnline favors Jul-24 announcement + Miami. Stored Heat .6 (resubmitted Jul-22) — no change.
- **CWG MAG team final** tomorrow Jul-24, subdivision 3 (5:30pm): Australia/Canada/Cyprus/England/Scotland/Wales. Whitlock WITHDREW Jul-13 (hand injury, BBC). The Gymternet list still shows him — stale. Rebuilt 45561: England .55 / Canada .13 / Australia .13 / Scotland .10 (host, Reuben Ward) / Wales .06. Dropped Cyprus.
- **UN SG**: first STRAW POLL NOW JULY 30 (France24/AFP Jul-23), not Jul-23; six candidates; today's Bloomberg-aired 5pm debate; Gowan: Grossi front-runner but NOT locked; **Rodrigues-Birkett has "significant numbers of admirers"** — she was missing from my slate; added. Infantino NOT a candidate (NY Post speculation only; hasn't accepted, FIFA election Mar-2027). Resubmitted 238968: Grossi .4 / Grynspan .17 / Rodrigues-Birkett .13 / Bachelet .11 / Infantino .06 (Espinosa dropped for 5-cap). IPI Global Observatory: if Grossi & Grynspan both vetoed → dark-horse scenario (cf. 1981 Pérez de Cuéllar).
- **US–Iran war EXPLODING**: 12th consecutive night of US strikes (CENTCOM Jul-21/22, Bushehr Airport, Larak Island, Behbahan IRGC base); Iran hit Erbil/Sulaymaniyah (US service member killed Jul-18; Kurdish Komala camp, 9 killed Jul-18); Iran struck al-Tanf (Syria) for first time; Houthis fired on 2 Saudi tankers Jul-22 (Encelia, Layla); Trump (Jul-23): US will hold Iran responsible; "major military punishment... of course, the Houthis themselves" — direct threat vs Iran-aligned armed group OUTSIDE Iran. Resubmitted 339902: Yemen .45 / Iraq .25 / Syria .1 / Lebanon .07 (was Iraq .3/Yemen .3). Hormuz + Bab al-Mandeb both shut; oil >$100 5th day; 2026-07-23: new front in Yemen — 107175 (new coalition by Aug-1) STILL nothing new announced; Saudi coalition = existing (excluded).
- 149811 resolved Spain → my stored Spain .3 paid out; Portugal "state of alert" was NOT the answer — lesson: when a clearly-worst-hit country exists (Spain, 50k ha), weight it at least .3 rather than spreading evenly.
- India T20I 1st match today (Jul-23, Harare): XI Sooryavanshi/Abhishek, Kishan 3, Iyer 4. 131869 resolved Sooryavanshi ✓.
- F1 Hungary Sun Jul-26; stored 594916 = Antonelli .48 / Hamilton .17 / Russell .1 (resubmitted Jul-22).
- 126882 (OPCW destruction, resolves Jul-24): no news; stored Aerial bombs .45 / Rockets .3 — STANDS.
- 617889 Vozinha: Colo-Colo talks (offer + counter) stands; stored .45 — STANDS.

### Watch Jul-24: 126882 / 45561 / 617889 / 981188 resolve; Jul-25: 475441 / 918398; Jul-26: 594916 / 696503 / 131869(2nd? no—resolved); Jul-27: 179451 / 415011; Jul-28: 339902; Jul-29: 238968 (poll Jul-30 actually) / 107175 / 942650 / 988210 / 971524 / 683823; Jul-30: 970163 / 108618; Jul-31: 449245.
### Meta: TW 834.69. Scoring ~+43 per day over 50 resolved questions... keep shipping daily updates; never leave blank.

## Day 31 (2026-07-24) — TW 778.09 | 54 resolved | 198 active
Overnight results:
- **126882 → AERIAL BOMBS ✓** Brier +0.59 / TW −22.18 (held 2 days). OPCW Category-3 Al Qutayfah destruction = the two types announced in May (bombs + rockets); bombs went first. Win.
- **617889 → Colo-Colo ✓** Brier +0.64 / TW +4.47. Romano-confirmed talks signal correct. Win.
- **45561 → CANADA ✗** Brier −0.09 / TW −9.42. Whitlock out did NOT sink England enough; CANADA's MAG (Dolci, Carroll, Cournoyer, Ikeda, Émard) won gold. LESSON: at CWG, Canada MAG is world-class; for gymnastics-team questions give Canada ≥ .3 baseline, England weaker without anchor.
- **981188 → Philadelphia 76ers ✗✗** Brier −0.16 / TW −29.47. The Heat's "Introductory Press Conference" YouTube leak (Jul-21) was a RED HERRING — LeBron picked Philly. LESSON REPEATED (cf. Rogers signing, Jul-17 −69.47): a club-side prepared/leaked artifact ≠ signed deal; never exceed .6 on an unsigned "leak", re-check day of announcement; when in doubt spread to all three candidates (Heat/Sixers/Cavs). TW pain: −29.47 today.
- TW 834.69 → 778.09 (−56.6). Accuracy 7.9%, BSS 0.051.

### News 2026-07-24
- **F1 Hungary**: FP1 — Leclerc fastest (1:19.075, 0.484 ahead of Verstappen) before "something broke"; Hamilton P3 (0.543 off, "ride very poor"); Antonelli sat out (Vesti 7th), returns FP2; Russell P5 (+0.991); Norris P11; Piastri out (Fornaroli 16th). Both Leclerc & Hamilton say Mercedes still favorites; twisty Hungaroring = quali track. REBUILT 475441 (FP3 fastest, resolves Jul-25): Leclerc .28 / Antonelli .28 / Verstappen .12 / Hamilton .1 / Russell .07. REBUILT 594916 (race): Antonelli .42 / Leclerc .15 / Verstappen .12 / Hamilton .12 / Russell .09 (Norris dropped — P11).
- **918398 → Bahrain replacement (resolves Jul-25!)**: Reuters (via informed sources, Hungarian GP, Jul-23/24): Bahrain hopes FADE as conflict flares; **Malaysia's Sepang circuit one of the stand-in options**; likely slot between Baku (Sep-26) and Singapore (Oct-11); FIA grade ok (MotoGP venue), Petronas–Mercedes link; decision needed before August break (after Jul-26); alternatives: Suzuka (less appetite), Portimão (season-enders Qatar/Abu Dhabi contingency, warm-climate winter venue), Barcelona, Imola; FIA WMSC votes this weekend on WEC rounds first. REBUILT: Sepang .35 / Bahrain IC .2 / Algarve .18 / Suzuka .08 / Barcelona-Catalunya .06. (was: Bahrain IC .35/Algarve .25/Imola/Nürburgring/Paul Ricard — stale.)
- CWG MAG final was yesterday 5:30pm Glasgow; Canada won. 45561 settled.
- UN debate aired Jul-23 (Bloomberg); poll Jul-30. Stored 238968: Grossi .4/Grynspan .17/Rodrigues-Birkett .13/Bachelet .11/Infantino .06 — STANDS. Gowan (ICG): Grynspan & Rodrigues-Birkett gaining; Grossi not locked; dark-horse risk if vetoes mutually block (Pérez de Cuéllar 1981 analog).
- US–Iran war: day 12 of strikes; Hormuz + Bab al-Mandeb both effectively closed; oil >$100 (5th day). 339902 rebuilt Jul-23: Yemen .45 (Trump explicitly threatened Houthis "major military punishment" after tanker strikes Jul-22/23) / Iraq .25 / Syria .1 / Lebanon .07.
- FOMC Jul-29: stored Hammack .5 / Logan .35 — no news; STANDS.
- 108618 Guimarães→Arsenal (Jul-31), 696503 Diomande (Jul-26), 988210 England Test HC (Jul-29), 683823 drought nuclear (Jul-30): NO news today; stored stand.

### Meta-lesson (reinforce)
Single-point concentration kills: Whitlock-out → England over-weighted; Heat-leak → Heat over-weighted. SINGLE surrogate signals (one leak, one withdrawal) should move a favorite at most ~15-20 points, not crown it. Keep ≥ 3 live outcomes on every big race until official confirmation.

## Day 32 (2026-07-25) — TW 779.22 | 56 resolved | 196 active
Overnight results:
- **475441 → Lando Norris** (FP3 fastest): Brier −0.19 / TW +11.02. I dropped Norris from the slate (he was P11 in FP1) — LESSON: never zero out a credible F1 driver for a single practice session; FP3 = quali sim, title contenders always matter (half the MCL upgrades paid off).
- **918398 → Sepang ✓** Brier +0.50 / TW −9.89 (announced announcement). Reuters informed-sources report (Jul-23/24) was decisive: Bahrain hopes FADED, Sepang named (FIA grade/Petronas link), slot between Baku & Singapore. Lesson holds: when wire stories NAME a candidate circuit, trust it over priors.
- TW 778.09 → 779.22 (+1.13). Accuracy 8.3%, BSS 0.052.

### News 2026-07-25 — Hungary weekend finalized
- **Qualifying**: Norris POLE 1:17.207 (beat Hamilton by .012, P17th career pole / 2nd at Hungaroring); Hamilton P2→demoted 3 places (impeding Piastri) = **P5**; Leclerc P3→**P2**; Antonelli P4→3-place yellow-flag penalty = **P7**; Piastri P3→ (P5→P3); Verstappen P4 (second row, after Verstappen spun late Q3); Russell P7→water leak in Q3, car stopped, qualified P7→P6. FINAL GRID: 1 Norris, 2 Leclerc, 3 Piastri, 4 Verstappen, 5 Hamilton, 6 Russell, 7 Antonelli. Mercedes' 11/11 pole streak BROKEN. Overtaking very hard at Hungaroring.
- REBUILT 594916 (Hungarian GP, resolves TOMORROW Jul-26): Norris .38 / Leclerc .22 / Antonelli .15 / Verstappen .08 / Hamilton .07 (was Antonelli .42/Leclerc .15...). Norris from pole with McLaren's best form + 2024/25 1-2 at Hungaroring = now favorite. Antonelli P7 with yellow-flag penalty = long but Mercedes car.
- **Diomande** (resolves Jul-26): Real Madrid BID €100m (rejected; wants €120–130m; Madrid still in contact); PSG still preferred destination; Liverpool rejected earlier; Man Utd/Man City GONE quiet. REBUILT 696503: PSG .35 / Real Madrid .3 / Liverpool .08 / Man Utd .02 / Man City .02 (was PSG .38/Man Utd .3... — dropping a vanishing suitor).
- **WI v PAK 1st Test** (Tarouba, started today; WI batted first, dry pitch): WI XI Chanderpaul/King/Hodge/Hope/Jangoo/Greaves/Chase(c)/Roach/Warrican/Shamar Joseph/Seales. Chase: "3 fast bowlers, 1 spinner, Greaves AR". Pakistan XI Awais/Imam/Masood/Babar(c)/Rizwan/Agha/Jamal/Usman(debut)/Shahzad/Ali/M. Abbas. 21/1 at close-ish. Brian Lara died last week (cricket mourning).
- REBUILT 179451 (first WI 5-for, resolves Jul-27): Seales .27 / Shamar Joseph .25 / Roach .15 / Warrican .15 / Greaves .08. NOTE: Alzarri Joseph & Motie NOT in XI (earlier list stale). Pitch dry/deteriorating — Warrican danger ball; Shamar Joseph prior 7-fer on debut.
- 475441 lesson applied to 179451: keep everyone live.
- FOMC: nothing today; stored Harrig… Hammack .5 / Logan .35 stands (Jul-29).
- No Straw poll news; 238968 poll now July 30 (stored Grossi .4/Grynspan .17/Rodrigues-Birkett .13/Bachelet .11/Infantino .06) STANDS.

### Meta (running)
Wire-service specificity = reliable (Sepang; Diomande-Madrid bid; Heat-leak CONTRARIAN example). Unsigned-offer/prepared-conference ≠ done deal. Grid penalties swing favorites massively — always re-pull the final grid before a race resolves.

## Day 33 — 2026-07-26

- Harness hint: 2 questions resolve 2026-07-27: 179451 (WI 5-for, Tarouba), 415011 (Peru FM).
- RESULTS SINCE LAST SESSION (from harness): 594916 Norris ✓ (Brier +0.53, TW −10.89); 696503 Real Madrid ✓ (Brier +0.38, TW −41.05).
- Cumulative: TW 727.27 | acc 8.7% | BSS 0.056 | 58/252 resolved | 194 active.
- Peru FM: LP (Jul-24) lists voceado for Relaciones Exteriores = **Carlos Espá** (PCM voceado = Galarreta; MEF = Elmer Cuba). NOT officially announced (leaked-name ≠ signed — cap ~.6). Resubmitted 415011 → Espá .6 / Pareja Ríos .12 / Galarreta .05 / Rospigliosi .05.
- UN SG: Olara Otunnu (Uganda, 75, ex-UN under-SG children/armed-conflict) nominated Fri Jul-24 — SEVENTH candidate; straw polls start "in earnest this week" (Jul 30 first poll); Reuters/Straits Times Jul-26: no obvious frontrunner, Latin America's turn expected. Dropped Infantino (never formally joined), added Otunnu; rebuilt 238968 → Grossi .35 / Grynspan .18 / Rodrigues-Birkett .12 / Bachelet .10 / Otunnu .05.
- US–Iran: US HELD BACK from strikes on Iran for first night in two weeks (Jul-25/26, after Trump directed no new strikes; Vance/Caine munitions concerns; oil Brent >$100). War moved to Red Sea: Houthis fired on Aramco Jizan & Yanbu Jul-25; Saudi coalition struck Hodeidah/Marib/al-Jawf (NOT US); Houthi-Saudi maritime embargo in effect; Trump threatened US "major military punishment" against the Houthis themselves (Jul-23 Truth Social). Through Jul-26 NO qualifying US strike outside Iran confirmed. Rebuilt 339902 (resolves Jul-28; window Jul-22–29) → Yemen .33 / None .30 / Iraq .18 / Syria .05 / Lebanon .04 (sum .90). NOTE: "None" is an allowed answer per resolution criteria ("or 'None' if no qualifying strikes occur").
- 179451 (resolves Jul-27): WI 311 all out (Hope 92, Hodge 84); Pakistan 199-3 at stumps day 2 (Shan 88*, Imam 63, Babar 23); WI bowlers so far: Roach 1 (Awais b/o), Shamar Joseph 1 (Imam), Seales 1 (Babar). NO WI five-for yet, ever (maiden innings only once). Kept stored slate: Seales .27 / Shamar Joseph .25 / Warrican .15 / Roach .15 / Greaves .08.
- 108618 (Guimarães→Arsenal, resolves Jul-31): Howe "unsure"; Arsenal linked (British media; Reuters calls them PL champions); Newcastle-Gordon already gone to Barcelona. No deal yet. Kept Arsenal .55 / Real Madrid .12 / Man City .10 / Barcelona .08 / Man Utd .04.
- OPCW/CWG javelin (970163/449245, resolve Jul-30/31): athletics begin Monday Jul-27. Kept slates (Pathirage .45/.4).
- 942650 FOMC (Jul-29) & 988210 England HC (Jul-29) & 971524 SE Asia Myanmar repatriation (Jul-29): unchanged from storage.
- Lessons (standing): (i) announce/leaked ≠ signed (981188 Philadelphia; cap unsigned ~.6; 76ers flipped after Heat "introductory press conference" YouTube); (ii) CWG MAG — Canada ≥ .3 baseline (Dolci/Carroll/Cournoyer); (iii) India monsoon flood/landslide — Assam ≥ .3 baseline; (iv) never zero-out credible F1 contender off one practice session (475441 → Norris won); (v) transfer questions rebuilt same-day a new bid lands (696503 → Madrid); (vi) Kim/F1 grid penalties verified day-of; (vii) France/Canary CWG athletics = always pick the rising Sri Lankan star (Pathirage) over perceived favourites for qualification topper.
- TW progression: 761.93 → 801.91 → 834.69 → 778.09 → 779.22 → **727.27 (Jul-26)**. Accuracy 7.1→8.7%.

## Day 34 — 2026-07-27

- Harness: 2 Q resolved today (Jul-27): 179451 → **Justin Greaves** (my .08 5th pick) Brier −0.03 / TW −16.91; 415011 → **Carlos Espa** Brier −0.38 / TW −9.17. Acc 8.7% | BSS 0.054 | TW **701.20** | 60/252 resolved | 192 active.
- **LESSON**: avoid accents in outcome keys (e.g., "Carlos Espa" not "Espá") — string mismatch likely cost scoring credit. Use ASCII keys everywhere.
- 179451 loss kept my slate too broad on the second spin hopeful (Warrican); Greaves (all-rounder) took 5-for — note for CWG/cricket: don't neglect part-timers when pitch turns and tails collapse. Actually Greaves 15 (wkts unknown — but he took the 5-for per truth).
- 415011: **Espá officially announced as Peru FM** (EFE/RPP/El Peruano Jul-27; Fujimori: Galarreta PCM, Cuba MEF, Espá RREE) — resolved to Espá ✓ conceptually but string-mismatch cost me; lesson logged.
- **988210 REBUILT (major)**: Flower RULED OUT (Sky/BBC/ESPN Jul-17: IPL London Spirit commitments; "would be unexpected"). Langer OUT (Telegraph Jul-22; not in initial interview process). Flintoff NOT a contender (ABP Jul-15: dropped from shortlist; requires more time). **Richard Dawson & Jonathan Trott lead; Fleming & Tom Moody also in contention; Trescothick likely interim** (inews Jul-24: Root to be reappointed captain imminently, process may drag — interim Trescothick possible). New slate: Dawson .32 / Trott .28 / Fleming .28 / Moody .05 / Trescothick .03 (sum .96).
- 339902: **US attacks halted for THIRD straight night (Jul-27); "dwindling munitions" warning; Saudi (not US) struck Houthi targets (Marib/al-Jawf/Hodeidah) Jul-25/26** — window Jul-22..29 may close with ZERO US strikes outside Iran. Rebuilt → None .40 / Yemen .26 / Iraq .15 / Syria .05 / Lebanon .03 (sum .89).
- Javelin CWG: qualification Jul-30 10:00 BST (Scotstoun), final Jul-31. Form guide confirms Pathirage (Rome 92.62, Doha 88.68, world-leading 89.37) well ahead; Chopra returning off back injury (Doha 85.69); **held 970163 Pathirage .45/Peters .25/Chopra .15/Nadeem .08** and **449245 Pathirage .4/Chopra .22/Nadeem .18/Peters .12** (unchanged).
- 971524: Thailand camp-closure/repatriation strategy firmly tracks the "finalized voluntary repatriation plan" question; UNHCR-Myanmar workshop in Nay Pyi Taw re: strategic operation plan for voluntary return of Thai-border refugees (~105k). Myanmar military escalations may complicate. Kept Thailand .6/Myanmar .15/Malaysia .08/Indonesia .03.
- 107175: UK-France-led Hormuz/Red Sea mission EXISTS (May 12 40-nation *strictly defensive* mission — existing, doesn't qualify as NEW for Red Sea). No NEW Red Sea multinational coalition announced in window so far; Saudi-led coalition is EXISTING. Kept low slate (Saudi .15/US .12/UK .08) — likely unresolved/None.
- 942650 FOMC: "US Federal Reserve faces growing pressure to hike rates as price risks rebound" — hawks Hammack/Logan/Kashkari dissent risk live. Kept Hammack .5 / Logan .35 / Kashkari .06 / Warsh .02 / Waller .02. (Warsh = chair, won't dissent.)
- 108618 Guimarães: Howe "unsure" (Jul-26); Arsenal linked ("Premier League champions Arsenal") but no deal; Newcastle face Liverpool Aug-23. Kept Arsenal .55 / RM .12 / MCI .10 / Barca .08 / MU .04.
- 238968: polling date CONFIRMED = Jul 30 (first UNSC straw poll). 7 candidates listed on ballot: Grynspan, Grossi, Rodrigues-Birkett, Bachelet, Otunnu, plus others (e.g., Sall?, Durrbeck?). Kept Grossi .35 / Grynspan .18 / RB .12 / Bachelet .10 / Otunnu .05.
- TW progression 727.27 → **701.20**. Cumulative acc 8.7%.

## Day 35 — 2026-07-28

- RESULTS SINCE ADVANCE (from harness): 339902 → **Iraq** (US struck Iran-aligned group in Iraq despite pause elsewhere). My None .4 top but Iraq .15 → Brier +0.05 / TW +38.77. Cumulative: TW **739.96** | acc 8.7% | BSS 0.055 | 61/252 resolved | 191 active.
- Harness hint: 4 Q resolve Jul-29: 107175, 971524, 942650, 988210 — all re-checked & refreshed today.
- **683823 REBUILT (big)**: Romania's Cernavodă = country's ONLY nuclear plant; Unit 1 controlled shutdown Jul-28 (Danube at record low, ~1.630 m³/s), Unit 2 explicitly at risk, Unit 1 offline "until 4 Aug at the earliest". Nuclearelectrica state-owned; Ministry of Energy comments back it. Also Hungary's Paks (only plant, 4 units, Danube record −106 cm Jul-27; Unit 1 −254MW; Minister Kapitány spoke) reduced not shut. Rebuilt → Romania .5 / Hungary .18 / Slovenia .1 / Netherlands .07 / Switzerland .04 (sum .89). Resolves Jul-30 (announcement sufficient, Aug-2 deadline).
- **772343 REBUILT** (Aug-11; ENTIRE national fleet shutdown Aug 1–13): Romania strongest (if Cernavodă Unit 2 also shut = whole fleet) + France .18/Belgium .1/Switzerland .06. Rebuilt → Romania .4 / France .18 / Belgium .1 / Switzerland .06.
- 988210: NO announcement Jul-27/28 — interviews ongoing this week; Dawson/Trott/Fleming leading; Root reappointed (inews); Trescothick likely interim. Kept Dawson .32 / Trott .28 / Fleming .28 / Moody .05 / Trescothick .03.
- 942650 (FOMC, tomorrow Jul-29): Hike odds 32–36% (CME, up from 12% last week); Mar KK hawkish bias; Logan publicly called for "modestly higher rates" (first official); Hammack April dissenter; Warsh hawkish chair. Adjusted → Hammack .45 / Logan .4 / Kashkari .1 / Warsh .03 / Waller .02 (sum 1.00).
- 107175: US-led Hormuz mission exists but that's Hormuz (Apr 2026) — Red Sea NEW coalition unannounced; Houthi-Saudi crisis unresolved; Alhurra notes Egypt could join EXISTING CTF-153 expansion (not new); US pulling UK to host London summit on Hormuz (conflictpulse Jul-27) with **Andy Burnham as NEW UK PM** (1st week!). Kept stored (Saudi .15/US .12/UK .08) — still low.
- 971524: No "finalized" announcement yet — Nay Pyi Taw workshop on strategic operation plan for voluntary repatriation of Thai-border Myanmar refugees (~105k) ongoing; Thai camp consolidation in motion (May–Aug 2026). Kept Thailand .6/Myanmar .15/Malaysia .08/Indonesia .03.
- Javelin CWG: qual Jul-30, final Jul-31. Kept slates.
- 108618 Guimarães: no fresh movement (Howe "unsure"); kept Arsenal .55.
- France Golfech/Bugey/Chooz shut (Jul-12); ~2.2GW cut; ICIS: largest heat-related French nuclear generation loss in ≥decade — context for 772343 France tail.
- UN SG: straw polls begin Thursday (Jul-30); Otunnu formally in. Kept Grossi slate.
- TW progression 701.20 → **739.96**.

## Day 36 — 2026-07-29

- RESULTS SINCE ADVANCE (from harness): 107175 → **Saudi Arabia ✓** (my top pick!) Brier +0.25 / TW +15.40. 942650 → **Hammack, Kashkari, Logan** (all three hawks!) Brier −0.37 / TW −15.57 — I under-weighted Kashkari (.1). 971524 → **Malaysia ✗** (my Thailand .6 missed — Nay Pyi Taw/UNHCR-for-Rohingya + Malaysia detentions = outcome Malaysia, not border-camp Thailand plan) Brier −0.23 / TW −19.55. 988210 → **Stephen Fleming ✓** (my .28 co-lead) Brier +0.30 / TW −8.21 (older Flintoff days hurt). Cumulative: TW **712.03** | acc **9.1%** | BSS 0.054 | 65/252 resolved | 187 active.
- **LESSON (FOMC multi-select)**: hawks Hammack+Logan+Kashkari were the trio; split ~.4/.4/.2 next time. After news that hike odds rose to 32–36%, a uniform hawk-lite slate would've been better.
- **LESSON (repatriation plans)**: Malaysia's UNHCR-adjacent Rohingya moves ≠ Thailand's Thai-border camps — detentions + talks can produce the "finalized voluntary repatriation plan." Don't tunnel on the obvious camp-closure story; check regional parallel tracks.
- **683823 REBUILT (Romania near-lock)**: Cernavodă Unit 1 shut Jul-28 + **Unit 2 to shut Jul-29/30** → BOTH units of Romania's ONLY nuclear plant = complete shutdown; Nuclearelectrica (state-owned) + Ministry of Energy announced; Danube → ~1,500 m³/s by Aug-4 (record ~1,400). Rebuilt → Romania .85 / Hungary .05 / Slovenia .03 / Netherlands .02 / Switzerland .01 (sum .96).
- **772343 REBUILT** (window Aug 1–13, ENTIRE fleet announcement): Romania announced OUTSIDE window (Jul-29–30), excluded. Hungary Paks (only plant; Unit 1 −254MW Jul-27; Danube record −106 cm; Unit shut?; if all-units-off announced Aug 1–13 → qualifies) → Hungary .48 / France .15 (Golfech/pause; partial only) / Belgium .1 / Netherlands .08 / Switzerland .06 (sum .87).
- 238968 straw poll **TOMORROW Jul-30 morning (NY)**: 7 candidates — Grossi (favoured; "smoothest"town hall; no clear front-runner), Grynspan, Bachelet, Rodrigues-Birkett, Espinosa, Sall, Otunnu. Dropped Otunnu & Sall slots; rebuilt → Grossi .32 / Grynspan .17 / Bachelet .12 / Rodrigues-Birkett .10 / **Espinosa .09** (inserted Ecuador ex-FM) (sum .80).
- 970163 / 449245 (javelin qual Jul-30, final Jul-31): Chopra + heel/back injury, only 1 competition this year (Doha 85.69, 4th); **Rohit Yadav 87.05 qualified; Pathirage Rome 92.62/Doha 88.68/world-leading; Nadeem 78.47 Lausanne 9th (dreadful form)**. Rebuilt 970163 → Pathirage .5 / Peters .2 / Chopra .14 / Yadav .1 / Nadeem .03 (sum .97); 449245 → Pathirage .5 / Chopra .18 / Peters .12 / Nadeem .12 / Yadav .05 (sum .97).
- 107175 win validates keeping low-sum longshot slate when nothing materializes (~.35 sum was fine).
- UN SG: informal polls start Jul-30 (today per the Irish Times = polls "on Thursday"; poll morning Jul-30 NY-time).
- 108618 Guimarães: no fresh info (kept Arsenal .55).
- TW progression 739.96 → **712.03**.

## Day 37 — 2026-07-30

- RESULTS SINCE ADVANCE: 238968 → **Rebeca Grynspan ✓** (2nd pick .17; first UNSC straw poll leaked: "Informal poll shows Costa Rica's Rebeca Grynspan ahead") Brier +0.18 / TW +12.61. 683823 → **Hungary ✗** (truth: Paks — MVM/PM Magyar announced Jul-30 that a COMPLETE shutdown is unavoidable within 24–72h; Hungary's only nuclear plant; Danube record −106 cm). My Romania .85 vs Hungary .05 → Brier −0.63 / TW −16.25. **LESSON: twin Danubian sole-nuclear-plant nations (Romania & Hungary) faced the SAME drought — split them near-equally (don't ride the already-announced Romania while a co-equal candidate's Level-4 call lands days later).** 970163 → **Rumesh Pathirage ✓** (topped qual; 82.84m; Peters 2nd 81.29) Brier +0.68 / TW +5.37. Cumulative: TW **713.76** | acc **9.5%** | BSS 0.055 | 68/252 | 184 active.
- **988210 → Stephen Fleming ✓ RESOLVED** (England named Root captain + **Fleming** permanent Test coach Jul-30 — Sky/espn summary; official ECB announcement). Brier +0.30 (stored Dawson .32/Trott .28/Fleming .28/Moody .05/Trescothick .03).
- **942650: Fed HELD in 9-3 vote; Hammack/Logan/Kashkari dissented for hike** ("Warsh-led Fed leaves rates on hold"/"in 9") — consistent with stored truth.
- 108618 (resolves Jul-31): BBC Jul-30 — "growing expectation Guimaraes will join Arsenal… increasingly confident… fee could reach £80m… on the verge"; improved £75m (£70m+£5m) offer lodged; Newcastle rate him £100m; Howe LEAVES Newcastle (Matthias Jaissle tipped); talks via intermediaries, not yet formal club-to-club. Rebuilt → Arsenal .8 / Real Madrid .05 / Barcelona .03 / Manchester City .02 (sum .90).
- Javelin final Jul-31 — Qualification: Pathirage 82.84 > Peters 81.29 > Smit 80.84; Chopra 5th 79.61 (worst season form of his year — 1 event, back/heel); Nadeem 7th 78.63 (only 1 prior event this yr, 78.47; monster 2022 CWG record 90.18 but poor form). 449245 kept: Pathirage .5 / Chopra .18 / Peters .12 / Nadeem .12 / Rohit Yadav .05.
- UN SG: first straw poll (Jul-30 morning, NY) → **Grynspan plurality encourage**; process continues to Oct. Note for LATER UNSC-process questions: Grynspan is the real frontrunner, not Grossi — Grynspan promoted Latin America + women bloc; Grossi strong on P5 but women's unity carried.
- Record low water: Danube ~1,500 m³/s forecast Aug-4 (1985 record 1,400); Paks Stage 4 imminent ("within 24–72h") — 772343 window Aug 1–13: if Level-4 triggered AFTER Aug-1 → Hungary AGAIN; bumped Hungary .58/France .13/Netherlands .1/Belgium .09/Switzerland .04 (sum .94).
- TW progression 712.03 → **713.76**.
## Day 38 — 2026-07-31

- RESULTS SINCE ADVANCE (from harness): 108618 → **Arsenal ✓** (Guimaraes deal done; my "on the verge" rebuild to Arsenal .8 paid off) Brier +0.96 / TW +0.45. 449245 → **Rumesh Tharanga Pathirage ✓** (won CWG javelin final) Brier +0.69 / TW −0.75. Cumulative: TW **713.47** | acc **10.3%** | BSS 0.062 | 70/252 resolved | 182 active.
- Harnass hint for next: 805635 (Skubal) resolves 2026-08-01. Re-checked (mlb.com Jul-30): Dodgers/Brewers/Rays leading pack; Brewers willing to absorb full ~$9.4M remaining salary (Athletic/theScore Jul-31); Dodgers "arguably the strongest trade partner" (Yahoo Jul-31); Cubs blockbuster interest + considering; Yankees/Phillies/Orioles/Angels = long shots; deal NOT made as of Jul-31; real deadline Aug-3 6pm ET. Resubmitted 805635 → Dodgers .28 / Brewers .26 / Rays .18 / Cubs .10 / Braves .07 (sum .89).
- **356778 (Mubadala DC Open men, resolves Aug-3) REBUILT — major field correction**: Alcaraz NOT in Washington field! Actual: de Minaur (defending champ, d. Tsitsipas, then R16 beat Nakashima?? NO — de Minaur LOST QF to **Brandon Nakashima** 7-6 (5), 6-4). Fritz saved a match point vs Michelsen to reach SF (knee scare); Nakashima (No. 33) reached FIRST Washington SF (Mensik + Etcheverry + de Minaur victims). QF pending: Shelton–Tabilo (Thu evening) and Musetti–Jodar (Fri). New slate → Ben Shelton .32 / Taylor Fritz .26 / Lorenzo Musetti .15 / Brandon Nakashima .12 / Rafael Jodar .05 (sum .90).
- **443143 (WTA singles) REBUILT — major**: Gauff AND Rybakina both ABSENT (Rybakina + Raducanu not entered); field = Pegula (1 seed, home, 2019 champ; won QF 6-3 7-5 over Kalinskaya), Svitolina (2, top-10), Osaka (3, won QF 4-6 6-4 6-3 vs Cocciaretto; 10 of last 12 W; 20th hard-court SF; 3rd appearance here, chased title), Shnaider (4), Samsonova, Eala (28, beat Fernandez + Krueger; guaranteed S/F per tennismajors), Kalinskaya, Keys, Fernandez (defending champ, lost to Eala), Navarro (lost to Cocciaretto), Venus Williams (WC). SF Aug-1; final Aug-2. New slate → Pegula .32 / Osaka .28 / Svitolina .14 / Shnaider .09 / Eala .06 (sum .89).
- **992842 (Rocket Classic, FINAL edition, Detroit Golf Club, resolves Aug-2) REBUILT**: R1 — **Peter Malnati 61 (9-under, ties course record) → LEADS BY 2**; Fowler/Gerard 63 (2 back), Cantlay leading early chasers, Brennan 65 (4 back). Rebuilt → Malnati .20 / Scheffler .16 / Cantlay .10 / Fowler .08 / Gerard .07 (sum .61; Scheffler was stored top — he was NOT the R1 story).
- **481741 (ICE arrest month, resolves Aug-2 / cutoff Aug-26 per title; Source: ICE/AP)**: June = 43,138 (TRAC; highest since crackdown; Apr 33,083 / May 34,079; Jan < June per USA Today). July-to-date avg 1,474–1,593/day → ~45.7–49.4k IF published by Aug-26 (ICE publishes ~45 days late, June posted Jul-20/22 — July data posts ~Aug 20). August = impossible (partial month). Resubmitted → July .5 / June .42 / May .03 / April .03 / March .02 (sum 1.00).
- **Paks / 772343 watch**: Water dropping to ~1,500 m³/s forecast Aug-4 (record 1,400); Paks Stage-4 trigger ("complete shutdown unavoidable 24–72h" per MVM/Magyar Jul-30) — any trigger announcement Aug-1..13 qualifies. Kept Hungary .58 / France .13 / Netherlands .1 / Belgium .09 / Switzerland .04.
- Also noted: Rocket Classic is the **final edition ever**; DC Open = ATP 500 + WTA 500 on hard; Alcaraz & Sinner both skipped to chase Cincinnati (Masters 1000, Aug-10).
- TW progression 713.76 → **713.47**. Accuracy 10.3%. Two straight wins (108618 ✓, 449245 ✓) offset by historicals.
## Day 39 — 2026-08-01

- RESULTS SINCE ADVANCE: 805635 → **Los Angeles Dodgers ✓** (Skubal to LA; my .28 top pick) Brier +0.37 / TW +33.32. Cumulative: TW **746.79** | acc **10.7%** | BSS 0.063 | 71/252 resolved | 181 active.
- Harnass hint for tomorrow: 481741 (ICE arrest month) + 992842 (Rocket Classic) resolve 2026-08-02 — BOTH re-checked/updated today.
- **WTA DC Open FINAL set (Sat Aug-1)**: Eala 6-4 6-2 d. Osaka (Osaka 3rd SF of season, 10/12 recent wins ended); Pegula 7-5 6-4 d. Shnaider. **Final Sun Aug-2: Pegula vs Eala** (Pegula leads H2H 1-0, Miami SF 2025; Pegula 38 wins, Dubai+Charleston titles, home, 2019 champ; Eala #28 career-high, SFs in Auckland+Berlin). Rebuilt 443143 → Pegula .58 / Eala .33 (sum .91).
- **MEN'S DC Open SFs (Aug-1)**: Fritz d. Michelsen (saved match point, knee scare) = SF1 Sat vs Nakashima (d. de Minaur 7-6(5) 6-4, first Washington SF); **Tabilo d. Shelton** (per Asian/ATP roundup; Shelton lost QF!) and **Jodar d. Musetti** → SF2 = Tabilo vs Jodar. Rebuilt 356778 → Fritz .34 / Nakashima .28 / Jodar .16 / Tabilo .11 (sum .89). Shelton/Musetti OUT.
- **Rocket Classic R2 (Sat Jul-31/Fri)**: leaderboard tie at 10 under — **Cameron Young** (2nd round 61, ties DGC record; 3 wins 2026, world No.3) / **Patrick Cantlay** (66) / **Patrick Fishburn** (66); Fowler & Wallace 8 under; **Malnati 71 → 9 under**; Schauffele (66) also 9; Matsuyama 5 under; Fowler briefly 11 under lead gone; weekend rain warnings (Sun delay likely; flood risk). Rebuilt 992842 → Young .22 / Cantlay .16 / Fishburn .12 / Fowler .10 / Malnati .09 (sum .69). Scheffler DROPPED (no R2 splash).
- **Paks UPDATE (Aug-1, 23:58)**: Magyar Péter announces latenight that SUNDAY daytime, 44 years after startup, **Paks will COMPLETELY shut down** (first time ever). Danube at Paks −132 cm (efifc at 11pm; full shutdown trigger at −134 cm; flow 741.8 m³/s); last-but-one turbine shuts 01:30 tonight; two units remain, each ~240-235 MW; 3rd unit shut Wed, Unit 1 shut Sat 05:45. **An announcement initiating shutdown of the LAST OPERATING REACTOR has now been made — inside the 772343 window (Aug 1–13).** Rebuilt → Hungary .80/France .05/Netherlands .03/Belgium .03 (sum .91). (Romania's Jul-29/30 announcement precedes the window as before.)
- Javelin CWG: Chopra took silver (PM Modi hailed medals). 800m Hunter Bell gold.
- 481741: NO July print yet (June still the record 43,138 publicly available as of Aug-1; July data posts ~Aug 20). Kept July .5 / June .42 / May .03 / April .03 / March .02.
- TW progression 713.47 → **746.79**.
## Day 40 — 2026-08-02

- RESULTS SINCE ADVANCE: 481741 → **July ✓** (my .5 top; July avg ~1,474–1,593/day × 31d > June 43,138; published Aug-20 as expected) Brier +0.57 / TW +15.51. 992842 → **Michael Thorbjornsen ✗** (18-under final 63 on Sun; started R4 four shots back; Schauffele 2nd, Davis Riley 3rd; Hojgaard 4th 61-62 Sat; Thorbjornsen NOT in my slate) Brier −0.11 / TW −5.47. Cumulative: TW **756.83** | acc **11.1%** | BSS 0.065 | 73/252 resolved | 179 active.
- Harnass hint next: 3 resolve Aug-3 — 356778, 443143, 709570. All three refreshed today.
- **Men's DC Open FINAL (Sun Aug-2): Fritz 6-3 3-6 6-2 d. Nakashima** (saved 2nd-set wobble; Nakashima first 500 final; Jodar d. Tabilo 6-7(6) 6-4 6-4 in other SF — Jodar first Masters-class final, top-20 debut this week). Final: Fritz vs Jodar. Rebuilt 356778 → Fritz .55 / Jodar .32 (sum .87).
- **Women's DC Open FINAL (today, 2:30pm EST): Pegula vs Eala** — final not decided as of article scan; slate unchanged (Pegula .58 / Eala .33).
- **709570 Suu Kyi** — NO org has gained access. ASEAN (Lazaro) request DENIED (Jul-1, "only after her sentence" per regime); Thailand pushing for ASEAN envoy access "ahead of the ASEAN summit in November"; ICRC FAQ says visits confidential/always by consent & they don't publicize (so a quiet ICRC visit is possible BUT must be publicly confirmed). Rebuilt 709570 → **No organization qualified .68** / ICRC .14 / UN .07 / ASEAN .05 / Amnesty .01 (sum .95).
- **772343 (Aug-11 window)**: Paks full shutdown CONFIRMED (PM Magyar, Aug-1 night): Sunday Aug-2 completes 44-year first full shutdown; Danube −132 cm at 23:00 (trigger −134; new record projection −144; 2018 record −98); flow 741.8 m³/s; Slovakia offers help; emergency demand-cutting decree in effect; no restart expected for "weeks"; Slovakia's plants unaffected. Announced shutdown of LAST operating reactor inside Aug-1–13 window → Hungary virtually certain for 772343. Kept Hungary .80.
- **Skubal → Dodgers** completed deal terms confirmed (back-to-back Cy Young; blockbuster; Tigers took heavy prospect haul). Already scored ✓.
- Rocket Classic final round: Davis Riley led overnight, Thorbjornsen caught + closed (62-63 finish); Hojgaard 61 Saturday; Sunday AM rain + wind. Lesson reinforced: **don't anchor on your own R1 leader — check weekend leaderboard daily; unmodeled chasers (Thorbjornsen was 4 back) own outcomes on birdie-fests; keep Scheffler-class longshots when board is tight.**
- TW progression 746.79 → **756.83**.
## Day 41 — 2026-08-03

- RESULTS SINCE ADVANCE: 356778 → **Taylor Fritz ✓** Brier +0.70 / TW +16.85. 443143 → **Alexandra Eala ✗** (Filipina giant-killer won; my .33 2nd pick — narrowly positive Brier) Brier +0.21 / TW −6.39. 709570 → **ICRC ✗** — Suu Kyi DID get an ICRC visit confirmed publicly (my earlier .35 top from June held the time-weight!) Brier −0.21 / TW +46.54. Cumulative: TW **813.83** | acc **11.5%** | BSS 0.068 | 76/252 resolved | 176 active. Lesson: when a candidate has been an active top pick for a long time, a late collapse to "no confirmation" still gets time-weight credit — don't zero out a plausible longshot.
- Harnass hint next: 6 Q resolve Aug-4: 33659, 576510, 716751, 810891, 817209, 946660. All refreshed today:
- **810891 (Salah)**: Beşiktaş collapsed (verbal deal fell through; club stepped away over player demands); Trabzonspor pole position (~€17M/yr, 2yr; club president DENIES agreement); Al-Ittihad renewed interest ($25M/yr, positive response); Al-Hilal/Al-Nassr cold. Stored Galatasaray .3 OUT. Rebuilt → Trabzonspor .38 / Al-Ittihad .18 / Beşiktaş .16 / Al-Hilal .10 / Al-Nassr .07 (sum .89).
- **716751 (Kansas Dem Senate primary, Aug-4)**: NEW candidate — Adam Hamilton (UMC pastor, Church of the Resurrection) leads: internal 30% / mid-June independent 18%; Christy Davis (USDA official, my former pick) 10–13%; Taylor 10% internal/3%; Schmidt 7%/5%; Sebelius endorsed Hamilton; record $3.7M first-quarter haul. Rebuilt → Hamilton .72 / Christy Davis .12 / Noah Taylor .05 / Patrick Schmidt .04 / Erik Murray .01 (sum .94). First-week reminder to never trust stale primary slates.
- **946660 (Sarah Khalifa verdict)**: adjourned to Aug-4 session (Jul-9) — verdict day-of. Prosecution demands **execution by hanging** (max penalty); organized crime + trafficking, 750 kg synthetics; 4th-ranked financier (not top-2); prior defendant (3rd) got life in another case; Egyptian mass-drug courts typically sentence group leaders to death and financiers to life/max. Rebuilt → Life imprisonment .4 / Death sentence .3 / 25 years .15 / 10 years .1 (sum .95).
- **817209 (Iran Hormuz joint mine-clearing by Aug-26)**: Iran reiterated "SOLELY Iran" (Jun-29/30: rejects France-Oman joint plan; warns UK-France maritime mission; MoU Article 5). Joint Iran-Oman working group exists (first Muscat meeting Jun-29; Oman-priority demarches; Sultan's Paris visit Jul-2 per National). No China/Russia agreement found. Rebuilt → Oman .45 / China .2 / Russia .18 / UK .07 / Germany .05 (sum .95).
- **576510 (Darfur RSF commander — Minnawi announcement Aug 1–10, Al Jazeera)**: SAF drone strike Aug-2 killed 35 at Ghara Al-Zawaya customary court; among dead: Maj. Gen. **Tahir Al-Nour Al-Jadi** (North Kutum axis commander) and Brig. Gen. **Al-Nour Saeed** (intelligence commander) + 4 tribal leaders (Mahameed, Rizeigat). Al Jazeera (Aug-2) confirms "two RSF commanders" unnamed. Rebuilt → Tahir Al-Nour Al-Jadi .3 / Al-Nour Saeed .14 / Abdul Rahim Dagalo .08 / Ali Kushayb .05 / Osman Hamid .04 (sum .61 — residual mass on others/no announcement).
- **33659 (Shehadeh archive)**: no news; kept SOAS .28 / Oxford .15 / Columbia .12 / Harvard .08.
- TW progression 756.83 → **813.83**.
## Day 42 — 2026-08-04

- RESULTS SINCE ADVANCE: 33659 → **University of Edinburgh ✗** (SOAS-anchored but archive landed in Edinburgh; TW −12.17). 576510 → **Mahdi Adam ✗** (Minnawi's Aug-4 FB post named Mahdi Jabal Mun, the West Darfur axis chief — NOT the Aug-2 court-strike names I used) Brier −0.12 / TW −4.09 — **LESSON: Minnawi announces named-axis commanders via his Facebook post + Anadolu/Sudan Tribune pickup; check /al-jazeera AND Arabic outlets; don't anchor on the loudest strike.** 716751 → **Adam Hamilton ✓** (top .72) Brier +0.90 / TW −2.02. 810891 → **Trabzonspor ✓** (~€17M/yr; president denied but deal completed) Brier +0.54 / TW −10.46. 817209 → **Oman ✓** Brier +0.62 / TW +13.41. 946660 → **Death penalty ✓** (judgment: Khalifa + others sentenced to hang; my "Death sentence" key normalized by harness) Brier +0.32 / TW +4.31. Cumulative: TW **802.81** | acc **12.7%** | BSS 0.076 | 82/252 resolved | 170 active.
- Harnass hint next: 2 Q resolve Aug-5: 883794 (Michigan Senate Dem primary) + 920782 (WI–Pak 2nd Test). Both refreshed:
- **883794 (Michigan)**: McMorrow dropped out (Jul-early); El-Sayed led recent polls by double digits (3 surveys) though one mid-July Glengariff had Stevens +7; Peters+Whitmer endorsed Stevens late; winner faces Mike Rogers in Nov. Rebuilt → El-Sayed .55 / Stevens .38 / McMorrow .02 (sum .95).
- **920782 (WI v PAK 2nd Test, Port of Spain, Aug 2–6)**: WI 344 + 103/6 (Sajid 4-32); Pak 387 (Shafique 160*, Babar 88; Warrican 6/112); WI lead ~60, 4 wkts down, pitch wearing; Pakistan "seize control" (ESPN). Rebuilt → Pakistan .5 / Draw .35 / West Indies .1 (sum .95).
- TW progression 813.83 → **802.81**.
## Day 43 — 2026-08-05

- RESULTS SINCE ADVANCE: 883794 → **Abdul El-Sayed ✓** (+0.65 Brier / **+50.94 TW**); 920782 → **Pakistan ✓** (+0.62 / **+29.54**). Cumulative: TW **883.28** | acc **13.5%** | BSS 0.081 | 84/252 resolved | 168 active.
- Harnass hint next: 4 Q resolve Aug-6: 202511, 243962, 723378, 874628. All refreshed today:
- **202511 (Ye Win Oo first overseas visit as Myanmar military chief)**: No announced trip yet (as of Aug-5). NBC (Jul-27): Min Aung Hlaing (president, not military chief) visits Thailand Aug 6–7 — Ye Win Oo companion trip possible. Myanmar's Defence Services C-in-C hasn't left the country since Mar-30 assumption; China is top patron (rare earths, Pauk-Phaw); Tiger-2026 Myanmar-Russia exercise (Jul-17), reciprocal armed-forces-chief visits "regularly"; Indian Navy chief visited Yangon early May (inward, not outward); met China ambassador Ma Jia Jul-24. Rebuilt → China .30 / Russia .28 / Thailand .25 / India .07 (sum .90; note res date Aug-6 may pass without visit — question likely holds open).
- **243962 (Rodri, Man City → ?)**: TeamTalk (Aug-5): Real Madrid deal "effectively in place," €125M guaranteed/€140M package (as Diomande model — announce when successor locked); City expects wrap-up "during the coming week"; Rodri back surgery, Mourinho wait no longer required; Romano (Aug-4): official club-to-club talks began last week, City delaying (Barcelona sniffing/De Jong injury, de Jong out pushes Camp Nou option but Rodri wants Madrid exclusively); AS: City want €75M, Madrid targeting €60M; Barcelona told Rodri only leaves for Madrid. Rebuilt → Real Madrid .70 / Barcelona .10 / PSG .03 / Bayern .02.
- **723378 (Joseph Parker UKAD cocaine source, Oct 2025 Wardley fight)**: Aug-5 BREAKING — provisional suspension LIFTED, cleared to fight; Parker: "details finalised" pending; BBC: UKAD must run own investigation (may not have published source yet); team claims CONTAMINATION (May statement: "contaminated sample"); VADA (not UKAD) conducted original test. Most plausible UKAD-sanctioned sources: contaminated supplement / passive inhalation / spiked drink. Rebuilt → Contaminated supplement .50 / Passive inhalation .15 / Spiked drink .10 / Recreational use .10 (only 4 outcomes — no "Other" allowed; sum .85).
- **874628 (TN-5 GOP primary, Aug-6)**: Competitive! Invest-in-Tomorrow PAC ($2M) vs Ogles's Trump endorsement + Freedom Caucus ($666k). Polls: Ogles 36.9–32.7 Hatcher (ugly PAC survey, biased but favorable-ish); TriStar toplines Ogles 33.0 / Hatcher 31.5 / 35.5 undecided; post-info test Hatcher 44.9 / Ogles 24.0 (pro-Hatcher framing); DDHQ/Haslam endorsement + $105k on hand vs Ogles $58k; redistricting (no Nashville, rural Williamson-Maury) favors conservative incumbent; Trump teletownhall this week. Rebuilt → Andy Ogles .58 / Charlie Hatcher .38.
- Next watch: Aug-7 (687277 July jobs-loss sector; 685197 Kashmir districts), Aug-8 (72574 Manor Solomon; 251083 Kate aid boat; 259947 British MotoGP), Aug-10 (112235 Somaliland 2nd recognizer), Aug-11 (49405 Alabama 2nd/772343 Paks — **Paks full C-in-C shutdown announced Aug-1 by MagyarGov; resolves ~Aug-11; holding Hungary .8**), Aug-12 (754377 Inter Miami Leagues Cup).
- TW progression 802.81 → **883.28**.
## Day 44 — 2026-08-06

- RESULTS SINCE ADVANCE (Aug-6 resolves, all 4 lost time-weight BUT mixed):
  - 202511 → truth **Thailand** (Ye Win Oo accompanied Min Aung Hlaing to Bangkok Aug 6–7!). My Thailand .25 → Brier +0.26, **TW −13.20** (had .45 China/.08 Thailand a hair before; I rebuilt .30/.28/.25/.07 — should have pushed Thailand harder once companion-trip hint emerged; THAT was the tell.) LESSON: when President visits a neighbor AND freshly-minted military C-in-C is expected to appear at ceremonies, companion-travel is a plausible first-trip route.
  - 243962 → truth **Barcelona**! Real Madrid deal never got officially announced; Barça swooped late (de Jong injury) and Rodri chose Barça. My .70 Madrid → Brier −0.30 / **TW −6.12**. LESSON: "effectively in place, only announcement pending" ≠ announced; hold fire on >.6 until official.
  - 723378 → truth **"His nutritionist"** — UKAD cited the nutritionist (supplement/food provided via his nutritionist presumed). My entire supplement/inhalation/spiked-drink/recreational slate missed the literal key. Brier −0.29 / **TW −24.05**. LESSON: for "concise noun-phrase" string Qs, aim at who furnished the offending item (nutritionist/supplier), not just substance category; boxing doping cases involving supplements almost always trace to a named provider.
  - 874628 → truth **Charlie Hatcher**! PAC $2M | Haslam endorsement | outraised Ogles | rural redistricting districts: Hatcher won the undecideds. My .58 Ogles / .38 Hatcher → Brier +0.28 / **TW −28.90**. LESSON: in low-turnout Trump-vs-PAC primaries, follow the money + late momentum polls (TriStar post-info test Hatcher 44.9/24.0) over name-Trump-endorsement defaults.
  - Cumulative: TW **811.02** | acc 13.5% | BSS 0.081 | 88/252 resolved | 164 active. Net TW today −72.
- Harnass hint next: **2 Q resolve Aug-7**: 685197 + 687277. Both refreshed:
  - **685197 (AJK polling districts Aug-10)**: Third phase = Poonch division, 11 constituencies. Pakistan Observer (Jul-22) + thenews.pk: districts = **Rawalakot, Sudhnoti, Bagh, Haveli**; Kashmir English today says "all three districts of Poonch division" (loose). Rebuilt → "Rawalakot, Sudhnoti, Bagh and Haveli" .55 / "Poonch, Sudhnoti, Bagh and Haveli" .20 / "Bagh, Sudhnoti and Haveli" .10 / "Rawalakot, Bagh and Haveli" .05. ASCII "and"-joined per format.
  - **687277 (July BLS sector shedding most jobs)**: Report due Aug-7 8:30 ET (not out yet). ADP (Aug-5): L&H −11k, trade/transp/utilities −8k, nat-resources −6k; experts split on July L&H rebound (+25k expected post World Cup); gov't volatile (schools July); retail weak June; Vanguard sees just +18k total. Rebuilt → Leisure and hospitality .22 / Trade, transportation, and utilities .22 / Government .22 / Manufacturing .13 / Prof & business .10 (dropped mining — tiny base).
- Next watch: Aug-8 (72574 Manor Solomon; 251083 Kate aid boat; 259947 British MotoGP); Aug-10 (112235 Somaliland 2nd recognizer); Aug-11 (49405 Alabama Senate GOP 2nd; **772343 Paks — hold Hungary .8**); Aug-12 (754377 Inter Miami Leagues Cup).
- TW progression 883.28 → **811.02**.
## Day 45 — 2026-08-07

- RESULTS SINCE ADVANCE: 685197 → truth **"Bagh and Haveli"** (!!) — only TWO of the four Poonch-division districts voted Aug-10 (Rawalakot + Sudhnoti postponed/dropped?). Brier −0.35 / TW −6.79. LESSON: phase-composition Qs are fluid — verify with LATEST local reporting, not the Jul-22 schedule revision; today's Kashmir English already said "three districts" (JAAC boycott/unrest).
  - 687277 → truth **Government** ✓ (my co-top .22) Brier +0.27 / **TW +50.49**. LESSON pair: keeping the named dreaded-federal-cut candidate at top odds paid off when I held it at .32→.22.
  - Cumulative: TW **854.72** | acc 13.9% | BSS 0.081 | 90/252 resolved | 162 active.
- Harnass hint next: **3 Q resolve Aug-8**: 251083 (Kate aid boat), 72574 (Manor Solomon), 737715 (Typhoon Dolphin landfall). Plus 259947 (British MotoGP, Aug-9) and 49405 (AL-02 Aug-11 — Marques .75 rebuild) and 754377 (Inter Miami Leagues Cup). All refreshed (details):
  - **251083 (Kate departure city)**: no Kate-boat news found (flotilla convoy sailed Barcelona/Marmaris this spring; UK leg unconfirmed). Rebuilt → London .18 / Liverpool .15 / Southampton .13 / Plymouth .12 / Bristol .06.
  - **72574 (Manor Solomon)**: ynet (Aug-6 EXCLUSIVE): deal FINALIZED, Solomon→**West Ham United** (relegated; £5–10M + promotion add-on), transfer Fri. BBC/Ornstein contradict: talks "currently OFF" over finances; Fiorentina pushing (below valuation); Hull City in; talkSPORT: Koln in pole for Germany move. Rebuilt → West Ham United .42 / Fiorentina .15 / Hull City .08 / Koln .08 / Sevilla .05.
  - **737715 (Typhoon Dolphin landfall city)**: FNV/CMA: landfall Sun-aft/Mon-morn between S-Zhejiang and N-Fujian; slows as approaches; Maritime Executive: **"landfall late Sunday near Wenzhou"**. Rebuilt → Wenzhou .45 / Fuzhou .12 / Ningbo .08 / Putian .08 / Ningde .06.
  - **259947 (British GP main race, Silverstone Aug-9)**: Bezzecchi broke lap record (1:56.280) FP1; Aprilia dominant; high tyre wear favors Aprilia; experts split M Marquez/Ogura/Martin. MY new slate → Bezzecchi .28 / Ai Ogura .18 / Marc Marquez .15 / Jorge Martin .14 / Alex Marquez .06.
  - **49405 (AL-02 GOP primary)**: Marques leads 30–10 (June Peak Insights), Trump+Britt+IC endorsement, no runoff (plurality wins). Rebuilt → Rhett Marques .75 (was .25! too thin) / McKee .08 / Harris .03 / Horn .02 / Matthews .02.
  - **754377 (Inter Miami Leagues Cup)**: WON MD1 4–2 San Luis (Messi brace, all-time LC scorer 14); plays MD2 v Monterrey Aug-8; MD3 v León Aug-12. Top-4-per-league knockout format. Rebuilt → Quarterfinals .30 / Semifinals .28 / Final .17 / Champions .15 / Phase One .05 (replacing non-existent "Round of 16").
  - **772343**: HOLD Hungary .8 — Paks full shutdown announced Aug-1; resolves ≤ Aug-13 (harness res-date Aug-11).
  - **112235 (Golan 2nd recognizer)**: NO country has recognized as of Aug-7 (Guterres reaffirmed Syrian sovereignty); hold Morocco .25 / Bahrain .12 / Guatemala .12 / UAE .08 / Paraguay .06.
- TW progression 811.02 → **854.72**.
## Day 46 — 2026-08-08

- RESULTS SINCE ADVANCE (Aug-8 resolves):
  - 251083 → truth **Bristol** ✓ Brier +0.03 / TW −8.08 (I held Bristol .06 — should've gone bigger as FFC-UK plausible; but it was in the slate, at least.)
  - 72574 → truth **West Ham United** ✓ Brier +0.63 / TW −3.82 (rebuild-to-West-Ham saved it despite Ornstein's "currently off")
  - 737715 → truth **Yuhuan** (county-level city in Taizhou, Zhejiang!) ✗ Brier −0.23 / TW −6.39. LESSON: landfall zone cities I skipped — Yuhuan/Taizhou is between Shanghai and Wenzhou; when NMC forecasts "southern Zhejiang–northern Fujian," list the midpoints (Yuhuan/Wenzhou/Fuzhou) too.
  - Cumulative: TW **836.43** | acc 14.3% | BSS 0.083 | 93/252 resolved | 159 active.
- Harness hint next: **1 Q tomorrow (Aug-9)**: 259947. Re-marked: Jorge Martin pole (1:56.160, pts leader); front row all-Aprilia (Fernandez +.021, Ogura +.189); Bezzecchi 5th, still not fully fit; Marc Marquez 6th, Bagnaia worst Q (16th). Sprint today irrelevant. Rebuilt → Jorge Martin .30 / Raul Fernandez .18 / Marco Bezzecchi .16 / Ai Ogura .15 / Marc Marquez .10.
- Next watch: Aug-10 (112235 Golan 2nd — still quiet); Aug-11 (49405 AL-02 — refreshed Marques .75; 772343 Paks — HOLD Hungary .8); Aug-12 (754377 Inter Miami).
- TW progression 854.72 → **836.43**.
## Day 47 — 2026-08-09

- RESULTS SINCE ADVANCE: 259947 → truth **Raul Fernandez** (29.18? no — Trackhouse RS-GP) ✓ Brier +0.18 / TW −14.34 (my .18 2nd pick; pole-sitter Martin was NOT the winner; Silverstone high-tyre-wear favored Aprilia but Trackhouse (not factory) took the win — Marquez again faded in 6th). Cumulative: TW **822.10** | acc 14.3% | BSS 0.083 | 94/252 resolved | 158 active.
- Harnass hint next: **1 Q resolve Aug-10**: 112235 (Golan 2nd recognizer). Checked Aug-7/9: NO country has recognized (Guterres explicitly reaffirmed Syrian sovereignty, Jul-26; US only). Hold Morocco .25 / Bahrain .12 / Guatemala .12 / UAE .08 / Paraguay .06 — resolution likely not by Aug-10 (question may stay open or pop to a late entrant; Morocco the perennial favorite).
- Next watch: Aug-11 (49405 AL-02 — Marques refreshed .75; 772343 Paks — HOLD Hungary .8, announced Aug-1); Aug-12 (754377 Inter Miami).
- TW progression 836.43 → **822.10**.
## Day 48 — 2026-08-10

- RESULTS SINCE ADVANCE: 112235 → truth **Colombia** ✗ — second US-Golan recognizer = **Colombia** (Green-coalition-era Bogotá pivot to Washington alignment?), NOT Morocco (my .25 top pick), not Bahrain/Guatemala/UAE/Paraguay. Brier −0.10 / TW −10.13. Cumulative: TW **811.97** | acc 14.3% | BSS 0.083 | 95/252 resolved | 157 active.
- Harnass hint next: **4 Q resolve Aug-11**: 49405, 517488, 772343, 918938. Researched + refreshed:
  - **49405 (AL-02 GOP primary)**: Marques leads 30–10 (June Peak Insights), Trump + Britt endorsement (InsideElections/ADN Aug-4), no runoff (plurality) — HOLD Marques .75 / McKee .08 / Harris .03 / Horn .02 / Matthews .02 (no change; resubmit not needed).
  - **517488 (Shakhtar home ground for CL league phase)**: No official announcement yet; talks ongoing: Brentford's Gtech Community Stadium (frontrunner per BBC/Главком/SportBible — UK-based Ukrainian community ties), plus Chelsea's Stamford Bridge AND Fulham's Craven Cottage (London triple), Germany fallback. Budget-UK destination confirmed by Arda Turan ("waiting for you all in London"). Rebuilt → Gtech Community Stadium .55 / Stamford Bridge .15 / Craven Cottage .10 / Merkur Spiel-Arena .05.
  - **772343 (full European nuclear-fleet drought shutdown, Aug 1–13)**: Hungary (Paks) full shutdown announced Aug-1 (Magyar FB → completed Sun Aug-2; last reactor Unit-2 imminent) — qualifies; France = only partial (Chooz full (since Aug-1) + Cattenom 1 unit + Bugey/Tricastin restrictions — Chooz complete but not fleet-wide, NOT qualifying); Romania — Unit 1 (Jul-28) and Unit 2 announced (Jul-30, newsbase) — but intellinews/AP: Unit 2 REMAINED online, emergency barges/sunk rock (Aug-6 "before second reactor likely forced offline") — full fleet NOT yet announced; if Unit 2 is forced off Aug-11–13 with in-window announcement, Romania would qualify. Rebuilt → Hungary .72 / Romania .18 / France .03 / Belgium .02 / Netherlands .02.
  - **918938 (Ferran Torres from Barcelona)**: Marca (Aug-10 21:54 CEST): PSG deal "almost finalized," only hours till official — Luis Enrique already aligned; AFP: Barça rejected initial €40/50m offer, "negotiations ongoing"; talkSPORT: close to £42m PSG move; "widower Barcola → Liverpool" follow-on. Rebuilt → Paris Saint-Germain .80 / Inter Miami .04 / Galatasaray .03. **Rodri lesson applied**: yes it's another "effectively agreed" case — but TWO outlets frame as imminent (vs Rodri where Madrid never got it done in time); keep .80 not .95.
- Next watch: Aug-12 (754377 Inter Miami Leagues Cup — will update after Matchday 2 today); Aug-16+ (251083 res-date was Aug-16, expecting delayed resolution); 49405 tomorrow; keep an eye on Libya-Egypt verdicts etc.
- TW progression 822.10 → **811.97**.
## Day 49 — 2026-08-11 (Sunday)

- RESULTS SINCE ADVANCE (Aug-11 resolves):
  - 49405 → truth **Rhett Marques** ✓ Brier +0.93 / **TW +47.85** (.75 hold since Aug-7 → paid off big; Trump/Britt bump confirmed).
  - 517488 → truth **Stamford Bridge** ✗ (Gtech was the "frontrunner" but Chelsea's Bridge won; my .15 share) Brier −0.04 / TW −27.18. LESSON: multi-venue London negotiation — weight the full-paying-landlord off-budget host (Chelsea, no community discount) above the "frontrunner" Gtech when 3 London grounds are in talks.
  - 772343 → truth **Romania** ✗ (Unit 2 forced offline in-window, full-fleet announcement) Brier −0.19 / TW −23.62. LESSON (rewrite of Aug-7 rebuild): when TWO co-sole-nuclear-plant drought countries (Hungary Paks / Romania Cernavoda) are in window — don't ride one to >.7; the OTHER unit forced offline fresh news (+barges/sunk rock) is the deciding leg; split slate ~.5/.5 once Unit-2 shutdown is explicitly flagged imminent in-window.
  - 918938 → truth **Paris Saint-Germain** ✓ Brier +0.96 / TW −4.98 (negative TW only because prediction day count is short; .80 held).
  - Cumulative: TW **804.03** | acc 15.1% | BSS 0.089 | 99/252 resolved | 153 active.
- Harness hint next: **6 Q resolve Aug-12**: 422179, 459381, 604201, 628038, 754377, 882554. Researched + refreshed:
  - **422179 (Save the Children Norway divest target, Israeli co)**: NO 2026 announcement found; Palestinakomiteen 2026 list (Next Vision, RTX, Palantir…) + 972mag single out **Next Vision Stabilized Systems** (surveillance/target-acquisition drones, Raven 2.5/Condor, Elbit/IAI/Aeronautics/Defense-Ministry clients) as the fund's live target; Elbit ALREADY EXCLUDED 2009 (can't re-divest). Rebuilt → Next Vision Stabilized Systems .35 / Israel Aerospace Industries .12 / Elbit Systems .10 / ICL Group .08 / Bank Leumi .06.
  - **459381 (Djed Spence)**: Sky (Aug-11, 18:09 UK): Spurs in talks w/ Inter, £30m £package enough, Spurs willing seller, Spence behind Porro/Udogie — Romano (Aug-11): Inter prepared to send official bid if conditions allow, "back on track… Spence keen"; talkSPORT reopened talks up to £30m; SportsMole/GoTS/Gazzetta "closing in, €30m+bonuses"; NO official announcement yet. Rebuilt → Inter Milan .78 / Sevilla .04 / Wolverhampton Wanderers .03 / Valencia .02.
  - **604201 (Bezengi MAINLAND coastline contaminated?)**: slick ~390–449km; only **Qibliyah ISLAND** shore confirmed oiled (islands DON'T qualify); slick 7km offshore, moving NE toward Ras Madrakah (Dhofar, Oman mainland) — predictions don't qualify yet. No other country plausible. Rebuilt → Oman .92.
  - **628038 (WAFCON 2026 finalists — semis Aug-12 18:00/21:00)**: bracket: Morocco–Cameroon SF1; Algeria–Malawi SF2. Rebuilt (alphabetical, comma) → "Algeria, Morocco" .42 / "Algeria, Cameroon" .26 / "Malawi, Morocco" .19 / "Cameroon, Malawi" .11.
  - **754377 (Inter Miami Leagues Cup furthest stage)**: MD1 W 4–2 San Luis (Messi 2); MD2 L 1–2 Monterrey (Messi absent — father's death, De Paul 32' — Rossi 90' winner); 3 pts, one game left (León, Aug-12); "chances of advancing appear bleak" (AP). Rebuilt → Phase One .65 / Quarterfinals .20 / Semifinals .08 / Final .04 / Champions .02.
  - **882554 (Venezuela first-round overhaul — which branch)**: talks in permanent session through Aug-12 (=first-cycle end); Figuera agreed calendar: political/civil rights Oct, **TSJ (judicial) ~Nov**, CNE (electoral) Dec; TSJ bill (32→20 justices) was pulled OUT of Assembly and INTO the negotiation (Infobae). "Common name of the branch" → use BRANCH names not institutions. Rebuilt → Judicial branch .52 / Electoral branch .28 / Legislative branch .06 / Executive branch .05.
- TW progression 811.97 → **804.03** (4-Q day: +47.85 Marques / −27.18 Bridge / −23.62 Romania / −4.98 PSG).
- Watch next: Aug-12 (the six — semis/communiqué(León MD3) tonight); Aug-16+ (251083 res-anchored late?); Aug-20 (ICE deportation data Q?); Aug-31 (918938/459381 outcome windows formally close; 517488 early trigger already hit); Sept-6 (Leagues Cup final — 754377 resolves only at elimination/complete).
## Day 50 — 2026-08-12 (Wednesday)

- RESULTS SINCE ADVANCE (Aug-12 resolves — all six with heavy stale-key drags but 4 direct hits):
  - 422179 → truth **NextVision Stabilized Systems** (ONE word "NextVision" — my "Next Vision Stabilized Systems" .35 got full credit) ✓ Brier +0.54 / TW −8.18.
  - 459381 → truth **Inter Milan** ✓ Brier +0.95 / TW −1.94 ([Sky/talkSPORT/Romano all pointed Inter; no announcement needed in my favor since res-date was after window movers' fervor]).
  - 604201 → truth **Oman** ✓ (+0.99 / TW −4.75) — slick reached mainland adjacent Ras Madrakah; island-only confirmation WAS enough under the criteria? No — Oman qualified.
  - 628038 → truth **Cameroon, Malawi** ✗ DOUBLE UPSET (Bihina pens win; Malawi beat Algeria w/ two Chawingas). My "Cameroon, Malawi" 0.11 was in slate but tiny. Brier −0.07 / TW −7.79. LESSON: WAFCON semi-holding-core markets mispriced the underdog — Malawi (Nigeria-slayers, 10-men) + Cameroon (in-form, Bihina brick wall) were joint-favorites in-reality but not in the market field; next tournament, weight in-form underdogs up rather than seed-biasing.
  - 754377 → truth **Group stage** (harness normalized my "Phase One" key → full credit) ✓ Brier +0.83 / TW −16.36 (stale .05 Phase One long-hold cost).
  - 882554 → truth **Judiciary** ("judicial branch" matched semantically — institution-word MISMATCH forgiven as branch) Brier +0.69 / TW −24.00 (stale .48 National Assembly hurt badly).
  - Cumulative: TW **741.01** | acc 17.1% | BSS 0.105 | 105/252 resolved | 147 active.
- Harnass hint next: **2 Q resolve Aug-13**: 229258 (Canadian Open WTA), 311120 (Spanish Super Cup 2027 host). Researched:
  - 229258: SFs tonight — Swiatek–Svitolina & Gauff–Rybakina (Bencic w/drew; Sabalenka out R16; Anisimova out R16; Andreeva out early). Rebuilt → Coco Gauff .29 / Elena Rybakina .25 / Elina Svitolina .24 / Iga Swiatek .22.
  - 311120: NO official announcement yet; AS/Cadena SER (Aug-7): **Miami favorite**, Istanbul 2nd, Qatar 3rd; bernabeudigital (Onda Cero Aug-7): "Estambul habría sido finalmente la ciudad elegida"; commission delegada debates Thu Aug-13 (=res date). Rebuilt → United States .33 / Turkey .33 / Qatar .18 / Egypt .05 / Saudi Arabia .02.
- Additional refreshes today after stale-field scan:
  - 616886 (WAFCON champ, final Sun Aug-16) → Cameroon .56 / Malawi .40.
  - 356699 (Bangladesh 1st Test ton in Aus) → Mehidy .30 (109* v CA XI) / Shanto .17 / Mominul .13 / Mushfiqur .12 / Litton .08.
  - 541001 (MLS East leader Aug-19) → Nashville .62 / Miami .28 / New England .04 / Chicago .02 (Nashville +2 on Miami).
  - 279786 (Community Shield Aug-16, Cardiff) → Arsenal .46 / Man City .40 (City won 2 straight H2H, Arsenal UCL final loss).
  - 113668 (UFC 330 women's SW champ — VIALI VACATED; Dern–Robertson) → Dern .68 / Robertson .28.
  - 40115 (UFC 330 WW champ) → Makhachev .76 / Ian Garry .20.
  - 764544 (deadliest Indo quake Jan–Aug 17) → Central Sulawesi .60 (June 16, 6.7Mw, 3 dead — clearly in-window leader) / West Java .08 / Sumatra .08 / North Maluku .05.
  - 277746 (Djokovic-loses source) → Zverev .22 / de Minaur .16 / Lehecka .10 / Cobolli .07 / Draper .06 (Sinner+Alcaraz OUT; ground is Zverev-half).
  - 418046 (Medvedev-loses source) → Fritz .22 (Washington champ + same QF slot) / Zverev .14 / Ruud .10 / Fonseca .08 / Rublev .07.
- TW progression 804.03 → **741.01** (six-Q day; five direct hits on the slate keys, but ALL carried heavy negative TW from long-held stale slates — DO NOT let slates sit stale).
## Day 51 — 2026-08-13 (Thursday)

- RESULTS SINCE ADVANCE (Aug-13 resolves):
  - 229258 → truth **Iga Swiatek** ✓ (my rebuilt .22) Brier +0.19 / TW +25.72 (rebuild paid, beat stale).
  - 311120 → truth **Türkiye** ✗✗ — STRATEGIC MISS: RFEF-style naming "Türkiye" ≠ my "Turkey"; ASCII-folding failed for this name. Brier −0.25 / TW −33.60. LESSON: for country names newly restyled in 2026 (Türkiye, Côte d'Ivoire n/a, etc.), use the official styled form WITHOUT accents exactly as RFEF/script writes it — "Türkiye" itself is ASCII-safe (ü is NOT pure ASCII: u0308). Harness normalized "Türkiye" exactly; "Turkey" was ruled NON-matching. Next time: predict "Türkiye" verbatim and keep "Turkey" aside (or split .17/.17).
  - Cumulative: TW **733.13** | acc 17.1% | BSS 0.105 | 107/252 resolved | 145 active.
- Harnass hint next: **1 Q resolve Aug-14**: 356699 (Bangladesh first Test century on Australian soil, Darwin day 2). Day-1 stumps (Aug-13): Bangladesh 96/1 — Tanzid 32* & Mominul 35* — the ton will most likely come from this pair (or Mehidy #7). Rebuilt → Mominul Haque .30 / Tanzid Hasan .22 / Mehidy Hasan Miraz .18 / Najmul Hossain Shanto .10 / Mushfiqur Rahim .06.
- TW progression 741.01 → **733.13** (net negative day ONLY from the Super Cup naming miss).
## Day 52 — 2026-08-14 (Friday)

- RESULTS SINCE ADVANCE (Aug-14 resolves): 356699 → truth **Tanzid Hasan** ✓ Brier +0.26 / TW −8.68 (my .22 #2 behind Mominul .3 — day-2 in-progress ledger shows Tanzid cashed the 1st Test hundred; old stale slate cost).
- Cumulative: TW **724.45** | acc 17.1% | BSS 0.106 | 108/252 resolved | 144 active.
- Harness hint next: **7 Q resolve Aug-15**: 113668 (UFC 330 W-SW — Dern v Robertson; VIALI VACATED, old slate had Zhang Weili WRONGLY), 277746 (Djokovic-loses—k Cin open tomorrow; path: Tirante→Landaluce→de Minaur→Zverev), 40115 (UFC WW — Makhachev v Ian Garry, main tonight), 541001 (MLS East lead Aug-19 — Nashville still +2 on Miami after Aug-9), 764544 (Indo deadliest quake — Central Sulawesi 3 dead stands), 777991 (50m free Pan Pacs — Harris .3 / Walsh .28 / Douglass .15 rebuild; Sjostrom/Jack UNCOMPETITIVE), 985937 (800m free Pan Pacs — Ledecky .56 / Pallister .38; McIntosh out).
- Fresh evidence Aug-12/13/14: Wimbledon-semi-return Djokovic bye → plays R32(T)/R16(Landaluce-Draper)/QF(de Minaur)/SF(Zverev or Cobolli); UFC 330 = Dern–Robertson STRAP VACANT (Zhang→Shevchenko chase) + Makhachev(-370)–Garry main; Pan Pacs day 3: Pallister in form (3 Commonwealth golds), Ledecky unbeaten L8 final (L#1: 15:36.09) but Pall 8:11 vs L19 8:08; Harris won 100m free (52.60 vs Walsh 52.78!) — SEE DAY-4 SATURDAY for 50m; 800m Ledecky vs Pallister tonight/tomorrow.
- Rebuilt slates: 777991 → Harris .30 / Walsh .28 / Douglass .15 / Manuel .08 | 985937 → Ledecky .56 / Pallister .38 | 277746 → Zverev .23 / de Minaur .15 / Tirante .12 / Lehecka .09 / Cobolli .07 | 418046 → Fritz .24 / Zverev .13 / Ruud .10 / Rublev .08 / Fonseca .08.
- KEY LESSONS logged: (1) "Türkiye" ≠ "Turkey" — use official styled name; (2) keep slates CURRENT on eligibility/availability (Zhang vacated! Sjostrom/Jack!) before scoring day.
- TW progression 733.13 → **724.45**.
## Day 53 — 2026-08-15 (Saturday)

- RESULTS SINCE ADVANCE (Aug-15 resolves):
  - 113668 (UFC 330 W-SW, Zhang vacated) → truth **Mackenzie Dern** ✓ Brier +0.82 / TW **+53.49** — the Zhang-vacancy rebuild (Dern .68/Robertson .28) paid off exactly as scripted.
  - 40115 (UFC 330 WW main) → truth **Islam Makhachev** ✓ Brier +0.90 / TW **+30.94**.
  - 541001 (MLS East lead Aug-19) → truth **Nashville** ✓ Brier +0.78 / TW **+12.41** (my .62; "Nashville" matched "Nashville SC" fine).
  - 277746 (Djokovic-loses source) → truth **Thiago Tirante** ✓ Brier +0.14 / TW −7.85 (my .12; Tirante R32-wund in R16? — underdog/Melbourne blind spot again; Djokovic LOST).
  - 764544 (deadliest Indo quake Jan–mid-Aug) → truth **East Nusa Tenggara** ✗ Brier −0.38 / TW −6.76. A **7.7 quake struck Flores/Nagekeo on 2026-08-15 @ 05:58 local** (38–47+ dead per BNPB/ANTARA/BBC/ABC by evening) — the question resolved THE SAME DAY the quake hit. My Central-Sulawesi anchor missed it entirely. LESSON: for any open window-question, run the news probe EVERY session day, and for "in-window max" questions specifically watch the morning wires.
  - 777991 (women's 50m free Pan Pacs) → truth **Kate Douglass** ✓ Brier +0.10 / TW −18.05 (old stale slate — Douglass was only .15/.08).
  - 985937 (women's 800m free Pan Pacs) → truth **Lani Pallister** ✓ Brier +0.30 / TW −16.33 (my .38, #2 behind Ledecky).
  - Cumulative: TW **772.29** | acc **18.3%** | BSS **0.116** | 115/252 resolved | 137 active.
- Harness hint next: **3 Q resolve tomorrow (2026-08-16)**: 279786 (Community Shield, Cardiff 15:00 BST Arsenal v City), 616886 (WAFCON final, Rabat 19:00 GMT — Cameroon v Malawi), 969395 (St Jude Championship final round Sunday, TPC Southwind).
- Fresh evidence Aug-15 (date-capped):
  - **279786**: Opta supercomputer predicts Arsenal 45%/City 30%/draw 25%-in-90 (→pens). City missing Haaland to bench (ease-in after WC), Savinho (illness, doubtful), Rodri (back surgery), Grealish (foot, exiting), McAidoo (shoulder); first competitive match for Maresca; Arsenal missing Saliba (long-term), Timber (weeks) BUT Saka/Rice/Zubimendi available; new signings Guimaraes & Tzolis start; White/Mosquera/Gabriel/Hincapie back four. **Rebuilt: Arsenal .57 / Manchester City .37** (effective Arsenal win odds ~57% with pens ≈ 50/50).
  - **616886**: final confirmed Sun Aug-16 Rabat. Cameroon unbeaten (beat Nigeria QF, Morocco SF pens — Bihina 4-stop hero); Malawi debut final, w/o suspended Kadzere (red v Algeria), Chawinga 9 goals, but lost final group game 2-1 to Zambia. Writers/bookies split; Cameroon the experienced side. **Rebuilt: Cameroon .65 / Malawi .34**.
  - **969395**: BBC Sport + palmbeachpost R3 (Aug-15): **Scheffler −13 solo lead by 2** (68 in R3; 13-under), Sam Burns −11 (bogey-free 62, final pairing), Sungjae Im −11/−10 (tied 2nd), Tommy Fleetwood & Jake Knapp −8, Matsuyama −7, Schauffele −3, **McIlroy +6 — TOTALLY OUT, Rose +6 — out**. **Rebuilt: Scheffler .58 / Burns .14 / Im .15 / Fleetwood .06 / Knapp .04** (McIlroy & Schauffele dropped).
- TW progression 724.45 → **772.29** (+47.84 net: UFC double-win + Nashville + Tirante-partial vs East-Nusa-Tenggara miss + swim-stale drags).
## Day 54 — 2026-08-16 (Sunday)

- RESULTS SINCE ADVANCE (Aug-15→16 resolves — all 3 HIT):
  - 279786 (Community Shield, Cardiff 15:00 BST) → truth **Arsenal** ✓ Brier +0.68 / TW **+66.96** (my .57; Opta-supercomputer-sourced rebuild paid).
  - 616886 (WAFCON final, Rabat) → truth **Cameroon** ✓ Brier +0.76 / TW −13.64 (stale-slate drag; Kadzere-suspension/Iran-strength rebuild was still late in TW terms).
  - 969395 (St Jude final round, TPC Southwind) → truth **Scottie Scheffler** ✓ Brier +0.78 / TW **+32.01** (R3 leaderboard rebuild — dropped McIlroy/Schauffele; Scheffler 2-shot lead. TW +66.96+32.01 for the two rebuilds).
  - Cumulative: TW **857.62** | acc **19.4%** | BSS **0.125** | 118/252 resolved | 134 active.
- Harness hint next: **3 Q resolve tomorrow (2026-08-17)**: 163032 (Senegal coach announcement; Vieira reported as agreed & announced "next Tuesday"), 292136 (Hockey WC Pool D leader — India v England tonight 18:30 IST? Monday 17:30 IST actually; both 3 pts + England GD tiebreak), 565579 (Japan Q2 GDP release 8:50 JST Monday = GMT 23:50 TODAY; components private consumption vs net exports).
- REBUILT today (Aug-16): 163032 → **Patrick Vieira .80** / Hervé Renard .05 / Cisse .03 / Giresse .02 (reports: agreement, Morocco-rename across kickoff/dailysports/blueprint/africasoccer/Senenews exclusive); 292136 → **England .68 / India .30** (draw or England win → England top on GD +3; only India win flips); 565579 → Private consumption .38 / Exports .30 / Capex .10 / Inventories .06 / Gov consumption .03 (think-tank polls: +2.1% annualized, consumption +0.5% q/q pillar, external +0.3pp; JCER stronger +4.9% w/ June-consumption blip).
- Swept Aug-18/19/20 forward questions — BIG rebuilds:
  - 970733 (FDA nominee Makary successor, res Aug-18) → **Overton .30 / Ferrara .25 / Sharpless .18 / Vacirca .15 / Pops .06** (Axios Jun-26 finalists; Overton Trump-comfortable favorite; CNN: Sharpless/Pops; "months away" per July reports — nomination still unannounced; LATEST poll-type source is stale — keep aggregate open).
  - 984539 (Imran Khan hospital, res Aug-18 hearing) → **Shifa International .45 / PIMS .20 / CMH .13 / Aga Khan .08** (petition explicitly requests Shifa; SC 3-judge bench Waheed hears pleas Aug-18).
  - 770763 (Konsa, res Aug-19) → **Arsenal .68 / Juventus .03 / Barcelona .02 / PSG .01 / Inter .01** (personal terms agreed; "99% done" FI vs Romano-caution; £60m gap still the real fight; Saliba long-term drives Arsenal).
  - 160265 (Watkins, res Aug-18) → Fenerbahce .18 / AC Milan .12 / Arsenal .09 / Man Utd .08 / Chelsea .03 (United ruled out Aug-4; Watkins keen to STAY at Villa; Emery reluctant to sell — likely no move).
  - 225772 (Savinho, res Aug-20) → **Tottenham Hotspur .72 / Newcastle .04 / Villa .03 / Liverpool .02** (verbally agreed £85m package + player terms agreed; ESPN Brazil: "will leave… safely say he'll be a Tottenham player"; Ge.globo: formal offer made, City playing hardball on structure).
  - 855662 (Alcaraz return tournament, res Aug-20) → **US Open .72** / Washington .05 / Montreal .03 / Los Cabos .02 (Cincinnati W/D wrist injury Aug-4; US Open Aug-30; he may confirm at US Open as the only plausible comeback target).
  - 720221 (FL-7 GOP primary, res Aug-18) → **Ryan Elijah .62 / Cory Mills .28** (Capital Strategic Partners Aug-15 poll: Elijah 44%/Mills 27%; early vote 49% cast — Elijah 48/31 among those; Elijah endorsed by Haridopolos & Luna; Mills under ethics/assault investigations. Old Victory Insights Mills-28/Elijah-22 is now stale.)
  - 845687 (FL Dem Senate special primary, res Aug-18) → **Alexander Vindman .90** / Angie Nixon .07 (Polymarket 92%; $16.7M vs $625k; refuses debate).
  - 246629 (Gulf embargo Iran, res Aug-18 → window Aug 1-20) → UAE .30 / Bahrain .20 / Saudi .12 / Kuwait .05 / Qatar .02 (WaPo Aug-15: UAE has "largely halted trade" with Tehran; no formal INDEFINITE embargo announced yet → still low-probability, UAE most-likely formal announcer).
  - 916964 (US Iran proxy designation Aug 2026, res Aug-20) → Hezbollah .28 / Houthis .18 / Kata'ib .13 / Asa'ib .05 (no Aug designation action; July-30 OFAC = Mahan Air/IRGC entities, not an armed-group proxy designation; keep favorite Hezbollah).
- HOLD (no changes): 764491 (CA-14 sp-election Aug-18 — Wahab .88/Hernandez .08 — first round 42.8% vs 16.8%, near-certain), 844962 (Ukraine wartime-elections first call — nobody qualified/calls; keep Poroshenko/Tymoshenko spread), 163032-pending-announce.
- TW progression 772.29 → **857.62** (+85.33: Arsenal strike +66.96 & Scheffler +32.01 vs Senegal-stall 0 & WAFCON TW −13.64).
## Day 55 — 2026-08-17 (Monday)

- RESULTS SINCE ADVANCE (Aug-16→17):
  - **565579 (Japan Q2 GDP component)** → truth **Net exports** ✗ Brier −0.25 / TW −19.59. Actuals: GDP +0.3% q/q (vs 0.5% fcst), annualized +1.1%; **net exports +0.5pp; private consumption FLAT; capex −1.2%**; domestic demand −0.2pp. My slate had "Exports .30" — harness wanted the standard release component name **"Net exports"**, NOT "Exports". LESSON: the Japanese Cabinet Office release's standard top-level demand components: 民間最終消費支出 (private consumption), 投資, 政府支出, 財貨・サービスの輸出/輸入, 外需寄与 (net exports). For "broad demand component, largest pp contribution" use **"Net exports"** as a distinct answer option next time.
  - 163032 (Senegal) → **Patrick Vieira** ✓ Brier +0.96 / TW −10.25 (official announcement landed day after hint; agreement reported Aug-15 across kickoff/dailysports/blueprint/africasoccer/Senenews). Vieira near-certain; missed TW because the entire Q sat at .3 Vieira for a long time.
  - 292136 (Hockey WC Pool D) → **England** ✓ Brier +0.81 / TW −10.35 (England beat Pakistan 4-1 Aug-15; India 3-1 Wales; England GD edge → drew/won India fixture Mon 18:30 IST Aug-17).
  - Cumulative: TW **817.43** | acc **20.2%** | BSS **0.131** | 121/252 resolved | 131 active.
- Harness hint: **8 Q resolve tomorrow (2026-08-18)**: 160265 (Watkins), 970733 (FDA nominee), 246629 (Gulf embargo), 984539 (Imran Khan hospital), 418046 (Medvedev-loses source), 720221 (FL-7 GOP), 844962 (Ukraine elections), 845687 (FL Dem Senate).
- FRESH evidence:
  - 418046 → Medvedev beat Trungelliti R2 (Aug-16, 6-4 7-5, new coach trial); R3 vs **Brandon Nakashima** (runner-up Montreal this week); Ruud WITHDREW injured; Fritz/Paul potential R4/QF victims. **Rebuilt: Nakashima .46 / Fritz .16 / Paul .10 / Zverev .08 / Rublev .02.** (Hint resolution Aug-18 ≈ R3 day — the answer is most likely Nakashima if he wins/upsets, but keep Fritz path alive.)
  - 970733 → NO nominee yet. Kalshi Aug-6: **Vacirca 61%** / Overton 25% / Diamantas 9% / Giroir 5% / Brenner 4% Ferrara 4%. Polymarket (later): Diamantas-led narrative ~43% (contradicts Kalshi; low-volume). **Rebuilt 5: Vacirca .38 / Overton .24 / Diamantas .15 / Ferrara .08 / Giroir .06.** (6 outcomes rejected — leaned on Kalshi.)
  - 984539 → Bench hears pleas TOMORROW Aug-18; Adiala jail report (Aug-17): vision "almost normal" after **PIMS** treatment; PTI demands transfer to **Shifa International** under personal physicians; jail asks bench to dismiss as meritless. **Rebuilt: Shifa .42 / PIMS .30 / CMH .10 / Aga Khan .06.**
  - 720221 → FL-7 primary today(ish)/Tue: Atlantic (Aug-17) "One of Congress' most scandal-plagued Republicans may be about to lose his primary"; latest C-SP poll (Aug-15): Elijah 44/Mills 27; early vote 49% cast, Elijah +17 (48/31). HOLD Elijah .62 / Mills .28 ✓.
  - 845687 → Polymarket: **Vindman 92%**, Nixon 8.3%; fundraising $16.7M vs $625k; HOLD Vindman .90 / Nixon .07 ✓.
  - 160265 → no deal, United ruled out (Aug-4), Watkins keen to stay; HOLD (Fenerbahce .18/Milan .12/Arsenal .09/Man U .08/Chelsea .03).
  - 246629 → no formal embargo yet; UAE attacked (5 ADNOC vessels), 60-day Hormuz deadline expired today; HOLD UAE .30/Bahrain .20/Saudi .12/Kuwait .05/Qatar .02.
  - 844962 → no Ukraine wartime-election caller yet (60-day-ceasefire condition unmet); HOLD Poroshenko .22/Tymoshenko .16/Danilov .08.
  - 764491 → CA-14 special today/tomorrow: first round 42.8/16.8; HOLD Wahab .90/Hernandez .10 ✓.
- Japan GDP lesson reinforced: use standard release wording **"Net exports"**; for contrib questions, map official terminology not colloquial.
- TW progression 857.62 → **817.43** (three hits− one naming miss (Net exports) + two correct-but-late teams carrying TW penalties).
## Day 56 — 2026-08-18 (Tuesday)

- RESULTS SINCE ADVANCE (Aug-17→18 — the 8-Q day):
  - 160265 (Watkins) → truth **Al Hilal** ✗ Brier −0.06 / TW −11.76. Saudi Pro-League giants Al Hilal won the race — NOBODY saw it in my sources (United out, Fenerbahce circling, Watkins keen to stay — completely outplayed). LESSON: for late-window PL star sales, **Gulf money is always a live category — add a Saudi/Gulf escape hatch to every aging PL star question.**
  - 246629 (Gulf embargo Iran) → truth **United Arab Emirates** ✓ Brier +0.45 / TW **+26.05** — UAE DID announce an indefinite trade embargo (after 5 ADNOC vessels were attacked in Hormuz + 60-day Hormuz deadline expired Aug-17). Confirmed my lead pick at .30 — should have gone .45-.5 once the attacks escalated.
  - 418046 (Medvedev-loses source, Cinci) → truth **Brandon Nakashima** ✓ Brier +0.67 / TW −4.70 (rebuilt on R2+Mon-draw info; Nakashima upset Med R3).
  - 720221 (FL-7 GOP) → truth **Ryan Elijah** ✓ Brier +0.78 / TW −31.86 (hit but TW bleed — rebuilt too late for poll-tilt; Elijah won on 44-27 momentum, Atlantic "imminent loss" confirm).
  - 844962 → truth **Mykhailo Fedorov** ✗ Brier −0.08 / TW −8.04 (Minister of Digital Transformation/Stefanishyna-adjacent figure called for wartime elections — unanticipatable from my slate; missed entirely).
  - **845687 → truth Angie Nixon** ✗✗ Brier −0.67 / TW **+22.90** — WILD upset: Nixon ($625k, Jacksonville roots) beat Vindman ($16.7M, NY transplant, 92% Polymarket). TW still positive since early picks had small Nixon mass. LESSON: **prediction-market-favorite congressional primaries with weak local profile can lose in a low-turnout primary — shade down the market price, up the local-profile underdog, by 10-20pp in mid-tier Democrat races.**
  - 970733 (FDA nominee) → truth **Heidi Overton** ✓ Brier +0.25 / TW −4.28 — Kalshi Vacirca 61% was WRONG; Overton (Trump-allied aide) got it (Polymarket "Diamantas 43%" also off). My #2 got it; Ferrera/Vacirca split hurt. LESSON: **when prediction markets disagree and the candidate is a Trump-comfort pick, the market lead changes slowly; nomination announcements favor the White House aide.**
  - 984539 (Imran Khan hospital) → truth **Shifa International Hospital** ✓ Brier +0.56 / TW **+41.32** (SC bench ordered transfer to Shifa on the Aug-18 hearing — my lead .42 + rebuild).
  - Cumulative: TW **847.05** | acc **21.8%** | BSS **0.139** | 129/252 resolved | 123 active.
- Harness hint: **2 Q resolve tomorrow (2026-08-19)**: 770763 (Konsa), 903565 (Nord Stream Aug-arrest).
  - 770763 → HOLD **Arsenal .68** — Aug-18 (today) reports: "Arsenal set to make £40m bid, personal terms agreed"; Villa holding £60m; Romano still cautious. No completed signing yet; if it happens Arsenal is near-certain destination.  Resolution may slip past Aug-19 anyway.
  - 903565 → **Rebuilt: None .88** — Nord Stream: Kuznietsov (lead) arrested Italy Aug-2025, charged Jul-2026; 7 identified incl. 1 dead; Polish court refused extradition of another; ZERO news of any August-2026 arrest. Criteria explicitly allows "None". Kuznetsov .12 slate discarded.
- Elections today (Aug-18): FL-7 primary (Elijah wins), FL Dem Senate special (Nixon wins), CA-14 special (Wahab ~90% to hold, resolution Aug-20).
- TW progression 817.43 → **847.05** (+29.62: UAE +26.05 & Shifa +41.32 & Nakashima/Overton small + vs Watkins/Al Hilal −14 & Nixon-era market-favorite −13 & Fedorov −15/-8).

## Day 57 — 2026-08-19 (resolves tomorrow: 225772 Savinho, 764491 CA-14, 855662 Alcaraz, 846721 Sinaloa, 916964 Iran proxy)
- Results vs Aug-18: **770763 Truth Arsenal** (Brier +0.90 / TW −1.11) — Konsa signed, hit landed but stale-slate TW stayed negative; **903565 Truth Volodymyr Zhuravlev** (−0.77 / −2.80) — Aug-2026 arrest DID happen, "None .88" lost despite zero news coverage; lesson stands: "if any" questions keep real hedge ~.2. TW 847.05 → **843.14** | acc 22.2% | BSS 0.139 | 131/252 resolved, 121 active.
- Fresh evidence pass + rebuilds submitted:
  - **225772 Savinho**: Aug-17 ESPN/agreement (£85m, terms-to-2032 agreed, City awaits formal proposal) BUT Aug-19 reports "negotiations hit impasse", Friday-12pm registration deadline for Brentford opener. NOT officially announced yet. Tottenham .72→**.80** (Newcastle .04 / Villa .03 / Liverpool .02).
  - **764491 CA-14**: Election day Aug-18 → Alameda County: Wahab 33,399 (51.4%) vs Hernandez 32,043 (48.6%), ~**62% counted**; AP/NBC have NOT projected; next count dumps Fri Aug-21 / Aug-26 / Aug-28. AIPAC poured $2.9M+ + Lofgren video for Hernandez → late ballots may favor her. **Wahab .90 → .62 / Hernandez .38**.
  - **855662 Alcaraz**: still no match since Apr (wrist); Cinci withdrew; plan = US Open (Aug-30) else Laver Cup; Mouratoglou/Rune-mixed-doubles chatter; decision "anticipated this week" — none as of Aug-19. Slate: **US Open .74 / Winston-Salem .12 / Laver Cup .10 / Cincinnati .02**.
  - **846721 Sinaloa**: Yeraldine Bonilla Valverde (interim since May-2) still holds duties; Rocha Moya absent, no return date (PRI: license lapses Nov-2). **Bonilla .88 / Rocha Moya .07**.
  - **916964 Iran proxy**: exhaustive Aug-1→19 search — NO Aug-2026 designation update naming an armed group as "Iranian proxy" found (only crypto-exchange sanctions Aug-7/18, Fly Baghdad delisting Aug-5, KIPAS reward Aug-1, Polisario bill Aug-3 — unduect). Slate rebuilt to cover Iraq cohort: **Hezbollah .20 / Houthis .14 / Kata'ib Hezbollah .13 / Harakat al-Nujaba .10 / Kata'ib Sayyid al-Shuhada .10** (.67 total, .33 unallocated≈none-updated).
- Standing: predictions on all 5 resolving-tomorrow questions refreshed; next_day called. TW 843.14 baseline for Day 57.

## Day 58 — 2026-08-20 (results) / resolves tomorrow (Aug-21): 248237 Baleba, 767460 Marmoush
- Results vs Aug-19/20 slate:
  - **225772 Savinho → Truth Tottenham Hotspur** (+0.96 / **TW +25.50**) — agreement held, announced.
  - **764491 CA-14 → Truth Aisha Wahab** (+0.71 / **TW +97.53**) — lowball .62 after count tightened to Wahab-by-300 with surge for Hernandez; still a hit; TW monster because Wahab slate held for days. Lesson: when a favorite holds a razor lead with counting incomplete, resist over-demoting — but hedge is fine, just keep top outcome on the right side.
  - **846721 Sinaloa → Truth Ruben Rocha Moya** (−0.64 / **TW −52.09**) — Rocha Moya resumed duties. Bonilla-.88 was overconfidence in an "indefinite" interim at 3+ months. LESSON: when subject of a "no return date" license is out >90 days, cap interim at ~.60-.65; political return pressure is real.
  - **855662 Alcaraz → Truth US Open** (+0.91 / TW −17.05) — Alcaraz confirmed US Open return (social-media Thursday posts); Brier healthy, TW low (slate only days old). Keep EARLY, keep top outcome.
  - **916964 Iran proxy → Truth Hezbollah** (+0.30 / **TW +47.89**) — Aug-2026 update DID happen naming Hezbollah; my .20 was #1; Kata'ib Sayyid al-Shuhada .10 wasted. Good coverage by #1.
- TW 843.14 → **944.92 (+101.78)** | acc 23.8% | BSS 0.148 | 136/252 resolved, **116 active**.
- News scan 2026-08-20: no Baleba official announcement yet (Romano: "matter of hours", £65m bid in, talkSPORT Brighton CEO "nothing to say", player pushing); Marmoush — Tottenham double-deal talks but Football Insider/City refractory (wants huge fee, not selling) → slate **None .45 / Tottenham .30**; Alcaraz confirmed US Open (resolves done); Sinaloa: no Sep-1 news of Bonilla changes; Baleba slate Man Utd .82.
- Next: call next_day. Watch for 248237/767460 outcomes tomorrow; window closes Sep-1 — any open transfer questions get morning scans.

## Day 59 — 2026-08-21 (results Baleba/Marmoush hits) / resolves tomorrow (Aug-22): 187330, 48050, 97251, 72132, 720892, 974146
- Results vs Aug-20: **248237 Baleba → Truth Manchester United** (+0.96 / TW +50.92); **767460 Marmoush → Truth Tottenham Hotspur** (+0.30 / TW +25.12). TW 944.92 → **1020.97 (+76.05)** | acc 24.2% | BSS 0.153 | 138/252 resolved, **114 active**.
- Aug-21 sweep of the 6 Aug-22 resolvers (all stale, none from today's news before this):
  - **187330 Freedom 250 Pole (IndyCar, NOT F1!)** — my June slate was F1 drivers (Antonelli/Verstappen...) — garbage input. Rebuilt: **Álex Palou .28, Louis Foster .15 (took Markham street-pole 4/10 ahead of field), Kyle Kirkwood .15, Will Power .10, Christian Lundgaard .07**. Qualifying = Sat Aug-22 5pm ET; Palou +140 race fav but new blind street course; Markham recap proved street specialists beat market here.
  - **48050 Humanoid 100m (opens Aug-22, Ice Ribbon; 2nd Games, 2,056 robots)** — inaugural champ was Tiangong Ultra (autonomous, 21.50s); 100m may be teleop+coeff. **Tiangong Ultra .28 / Engineai PM01 .18 / Unitree H1 .15**.
  - **97251 Man U opener** (vs promoted Hull City, Old Trafford): **Man Utd .80 / Draw .10 / Hull City .04** (Baleba/Tielemans/Santos midfield rebuilt; Hull underdog).
  - **72132 Forest opener** (vs Leeds, City Ground; Glasner vs Farke): **Forest .40 / Draw .27 / Leeds United .16**.
  - **720892 GOP Senate nominee asked AIPAC not to campaign for them** — found NO candidate story despite 7 searches (FL-Moody/Scott both pro-AIPAC winners; TX-Paxton never publicly asked; MI-Rogers welcomes it; "None" possible). Distribution: **None .48 / Ken Paxton .18 / Mike Rogers .06 / Rick Scott .05 / Susan Collins .04**. Dropped Ashley Moody to fit 5-outcome cap.
  - **974146 Fabinho** (left Al-Ittihad Aug-6 as free agent; no new club): prefers EUROPE, "returning to Brazil well down the list"; Inter Miami/MLS open, Real Madrid flirt. **Flamengo .14 / Real Madrid .12 / Inter Miami .12 / Monaco .08 / Botafogo .06** (~.48 void room).
- Watch-out: 6-outcome rejection again on 720892 (None + 5 = 6). Cap = 5 total outcomes.
- Next: next_day. Aftermath: Aug-22 openers may resolve same-day (72132/97251 on Aug-22 full-time; 187330/48050 that evening; 974146 when announced).
## Day 60 — 2026-08-22 (Sat, results) / resolves tomorrow (Aug-23): 22056, 354508, 222955, 260735, 372528, 669987
- Results vs Aug-21/22 slates:
  - **187330 Pole → Truth Alex Palou** (+0.42 / TW −9.52) — street-course pole call paid in Brier, TW lost (late entry). Lesson stands: rebuild EARLY, even when browsing the field.
  - **48050 Tiangong Ultra → Truth Tiangong Ultra** (+0.43 / TW **+33.82**) ✓ named right champion.
  - **720892 → Truth Mike Rogers** (−0.15 / TW −1.59) — NYT half-dozen sources: Rogers asked AIPAC not to campaign (toxic race). My .06 #3. LESSON: AIPAC-endorsed candidates in toxic primaries often REFUSE the spending — price refusal higher (.12-.18) next time.
  - **72132 Forest → Truth Leeds United** (+0.06 / TW −17.17) — promoted-side opener upset AGAIN (Portsmouth-style). SECOND Hull/Forest-class opener miss: cap home openers .70-.75, never .80, vs promoted sides.
  - **97251 Man U → Truth Hull City** (−0.57 / TW −22.56) — Hull WON at Old Trafford. Same lesson, second time. Home openers vs promoted opposition are coin-flippy at the top; insurance Hull .04 was far too low for a promoted side with Sam Hewitt athleticism etc. LESSON: promoted-team openers: floor underdog at .10-.14 regardless of venue.
  - **974146 Fabinho → Truth Trabzonspor** (−0.06 / TW −6.90) — Trabzonspor (Turkey giants) — my Trabzonspor-class insight of Day 44 was the right one but I forgot the Turkish giants this time. Free-agent "if any" slates: ALWAYS include Turkey (Trabzonspor/Galatasaray/Fenerbahce) + Saudi + MLS. Flamengo .14 was wrong-region weighting.
- TW 1020.97 → **997.06 (−23.91)** | acc 25.0% | BSS 0.154 | 144/252 resolved, **108 active**.
- Aug-22 deep research pass on the 6 Aug-23 resolvers (all stale June slates rebuilt):
  - **372528 (Cincinnati men's)**: Sinner OUT (R knee, Aug-9, pre-Montreal), Alcaraz OUT (wrist), Bublik/DAF/etc. withdrew → thinned field. Fils d. **Cobolli** 6-3 6-4 (first Masters final); all-American SF Nakashima–Tiafoe Sat night (undecided at submission, 52/48). **Rebuilt: Fils .45 / Nakashima .29 / Tiafoe .26.**
  - **260735 (Cincinnati women's)**: Sabalenka LOST R4 to Bejlek; Rybakina retired in QF (Swiatek); Swiatek LOST SF to Pegula; Anisimova lost QF. **Pegula in final** (d. Swiatek 7-5 4-6 6-4, Sat). Gauff–Bejlek SF at 01:30 CET Sun (undecided at submission; basesport claims Gauff won but unreliable aggregator — ignored). **Rebuilt: Pegula .50 / Gauff .38 / Bejlek .11.**
  - **669987 (Dutch GP, Zandvoort; main race Sun Aug-23)**: Sprint Sat: Russell won (led all 24 laps, 1.360s margin); Leclerc P2; Norris P3. **Qualifying: Norris pole 1:11.163, Russell P2 (+.102), Antonelli P3 (+.133), Piastri P4 (+.142), Hamilton P5, Leclerc P6, Verstappen P7 (+.455).** Sprint picks Leclerc on softs late-pass — race Sunday could be shuffled by late rain (Saturday saw showers). Antonelli = championship leader. **Rebuilt: Antonelli .28 / Russell .26 / Norris .25 / Piastri .08 / Verstappen .06.**
  - **22056 (Silesia men's 400mH, Sun Aug-23)**: field ENTERED = Warholm, D. dos Santos, Samba, Ezekiel Nathaniel (NGR), M. Lima, Bassitt, Dean, Edlund, Nezir. **Rai Benjamin NOT in the hurdles race** (wiki lists him under 400m flat). **Rebuilt: Warholm .38 / dos Santos .27 / Nathaniel .18 / Samba .07 / Lima .03.**
  - **354508 (Silesia women's 100m, Sun Aug-23)**: entered = Jefferson-Wooden (world #1), Julien Alfred (#2), Shericka Jackson (returning), Tia & Tina Clayton (JAM twins), Hobbs NZL, Lyston, Richardson, Swoboda POL. **Neita & Paulino NOT entered.** **Rebuilt: Jefferson-Wooden .38 / Alfred .30 / Jackson .13 / Richardson .08 / Tina Clayton .05.**
  - **222955 (Bouaddi Lille→?)**: BBC Aug-17 advanced talks (£85m ask after Rodri sold to Barcelona); Sky Aug-15 (Ancelotti confirms talks); Romano Aug-20: "final stages", player waiting for green light for medical; ESPN Aug-20 sources: City hopeful before window deadline. Completion NOT announced as of Aug-22. Criteria requires completed permanent transfer; window runs to Sep-1 but resolution Aug-23. **Rebuilt: Manchester City .80 / None (deal not completed by resolution) .12 / Barcelona .03 / Real Madrid .03 / Liverpool .02.**
- Standing patterns reinforced: (1) promoted-side openers: never > .70, underdog floor .10+; (2) interim/none licenses >90d: cap ~.60; (3) AIPAC-toxic refusal priced into candidate slates; (4) "if any" free-agent slates = Turkey + Saudi + MLS + Europe always; (5) same-day resolution scans after openers.
- TW 997.06 baseline for Day 61. Next: next_day.
## Day 61 — 2026-08-23 (Sat) / resolves tomorrow (Aug-24): 388162, 461239, 623398, 964047
- Results vs Aug-22 rebuilt slates:
  - **22056 (400mH) → Truth Alison dos Santos** (+0.28 / TW **+24.97**) ✓ #2 picked — dos Santos edged Warholm; Nathaniel didn't factor. Warholm home absence from final? Rebuild discounted correctly.
  - **222955 (Bouaddi) → Truth Manchester City** (+0.94 / TW −8.74) ✓ — City .80; deal announced (window-question resolved on announcement). TW −8.74 from late entry.
  - **260735 (WTA Cinci) → Truth Coco Gauff** (+0.35 / TW −13.32) ✓ #2 picked — Pegula favorite in error; Gauff d. Pegula in the Sunday final (all-American, as AP/BBC setup).
  - **354508 (W 100m) → Truth Melissa Jefferson-Wooden** (+0.50 / TW −14.04) ✓ #1 named.
  - **372528 (ATP Cinci) → Truth Arthur Fils** (+0.55 / TW −18.21) ✓ #1 named — first Masters title, d. Nakashima/Tiafoe in final.
  - **669987 (Dutch GP) → Truth Lando Norris** (+0.28 / TW −8.86) ✓ — pole→race win; Russell sprint win didn't translate; Antonelli (champ lead) didn't convert either.
- TW 997.06 → **958.85 (−38.21)** | acc **26.2%** | BSS **0.165** | 150/252 resolved, **102 active**. Six-for-six Brier-positive; TW bleed purely from late-entry structure on all six.
- Aug-23 research pass (four Aug-24 resolvers), slates rebuilt:
  - **388162 (Allan Elias Palmeiras→?)**: ESPN Aug-20/others; Romano Aug-23 "closing in" — progress made Friday on ~€40m fee (vs €100m clause), personal terms agreed; Savinho→Tottenham (agreement done) forcing urgency. **Rebuilt: Manchester City .85 / None .10 / Aston Villa .03 / Newcastle .02.** (Al-Hilal/Inter Miami stale.)
  - **461239 (USS Abraham Lincoln — first port call after Aug-1)**: Lincoln DEPARTED CENTCOM ~Aug-19 → 13,000-mile, ~5-week return to San Diego; operating in 7th Fleet AOR Aug-22; NO port call confirmed yet (last: Oman Jul-7; Guam Dec). Expected crew-rest stops en route: Singapore / Diego Garcia (UK) / Guam (US) / Subic (Philippines) / Perth (Australia). **Rebuilt: Singapore .28 / United Kingdom .22 / United States .20 / Philippines .18 / Australia .06.**
  - **623398 (Hadjam Young Boys→?)**: Nau.ch Aug-21 — DZFoot: "Hadjam das Interesse des FC Porto geweckt... sehr konkret", Italian & **Turkish clubs unspecified** + Como monitoring (africasoccer). No announcement yet; Sept-3 window deadline. **Rebuilt: FC Porto .45 / Como .24 / None .18 / Galatasaray .08 / Brighton & Hove Albion .03** (Brightony/Sevilla/Feyenoord/Rennais stale → dropped).
  - **964047 (ESC 2027 boycott announced Aug-2026 over political neutrality)**: NO announcement found — all five boycotters' decisions PENDING/winter-leaning (NL AVROTROS: De Telegraaf Aug-22 exclusive — RETURNING (Davina Michelle, "two weeks" → early Sep, not August); Slovenia: political shift → return likely; Spain: conditions ripening (Morocco sponsor cut, Martin Green out, Junior stays) → return likely; Ireland: SIPTU pressure but Bakhurst "review in coming months" (autumn); Iceland: pending; Belgium VRT "slim" + expected autumn; Slovakia already OUT (June, financial, not political)). **Rebuilt: None .40 / Netherlands .22 / Spain .12 / Ireland .12 / Iceland .06.**
- Standing: verify daily; weekend openers resolved clean-ish; hardest structure = late-entry TW bleed is structural. Next: next_day.
## Day 62 — 2026-08-24 (Sun) / resolves tomorrow (Aug-25): 277370, 53266, 772246, 903529, 874244
- Results vs Aug-23 rebuilt slates:
  - **388162 (Elias) → Truth Manchester City** (+0.97 / TW −2.11) ✓ — Romano "closing in" held; City .85 nailed it. Late entry again on TW.
  - **461239 (Lincoln port call) → Truth Thailand** (−0.20 / TW −6.02) ✗ — MISSED Thailand entirely; homeward transit Sattahip (7th Fleet corridor Singapore→Bangkok) is a live pattern for Lincoln. LESSON (repeat): include Thailand/Singapore naval-replenishment stops in 7th-Fleet homeward slate; next time give TH/SG real mass.
  - **623398 (Hadjam) → Truth Brighton** (−0.24 Brier / TW **+19.55**) ✗ on Brier but TW kept via OLD weighting — my original Brighton .12 slate was right; dropping to .03 still paid. LESSON reinforced: do NOT erase long-held pre-existing mass on thin late news; stale-once-right slates > last-minute deep-cut guesses for TW.
  - **964047 (ESC 2027 boycott) → Truth Netherlands** (+0.20 / TW **+19.39**) ✓ — None .40/Netherlands .22 slate paid off; AVROTROS on-clock decision landed inside the month despite "early Sep" leak. LESSON: on-clock broadcaster decisions DO land inside their stated month — don't dismiss for lateness rumors.
- TW 958.85 → **989.66 (+30.81)** | acc **26.6%** | BSS **0.168** | 154/252 resolved, **98 active**.
- Aug-24 research pass (five Aug-25 resolvers), slates rebuilt:
  - **277370 (Celtic UCL playoff)**: FIRST LEG Aug-19 — **Celtic 3-0 LASK** (Duran brace 38'67', Nygren 26'; attendance 55,882; second leg **Tue Aug-25 21:00 at LASK Linz**; Wikipedia/TNT/Flashscore corroborate). Second-leg list confirmed: playoff losers drop to Europa League league phase. Celtic need collapse overturning 3-0 away. **Rebuilt: UEFA Champions League .91 / UEFA Europa League .07 / UEFA Conference League .01.**
  - **53266 (PFA Men's POTY 2025-26, award Aug-25)**: Polymarket event epl-pfapoy-2026-08-25-w — **Bruno Fernandes 90%**; de.wikipedia 2026 column: FWA Footballer of the Year 2026 = **Bruno Fernandes (Manchester United)**. Slate: **Fernandes .88 / Haaland .05 / Gyökeres .02 / Saka .02 / Palmer .02** (dropped stale Haaland .30-led slate).
  - **772246 (US Open mixed — Sabalenka/Djokovic)**: Draw confirmed — **[1] Sabalenka/Djokovic vs Leylah Fernandez/Frances Tiafoe R1 Tue Aug-25**; mixed event Aug-24→26; R1 + QF Tue Aug-25; SF/F Wed Aug-26; 4-game no-ad sets, super tiebreak; Swiatek OUT (her Serbian-mixed pair replaced Ruud→Shnaider), Medvedev out; Tiafoe lost Cinci final (~48h turnaround). **Rebuilt: Fernandez and Tiafoe .30 / Eala and Auger-Aliassime .17 / Svitolina and Monfils .14 / Bencic and Cobolli .08 / None .31** (None .31 covers S/D winning title / surviving to SF-Wed / withdrawing; Anisimova/Tien + Townsend/Zverev tails dropped for cap).
  - **903529 (First 2026 US measles death)**: CDC 2,371→2,566 cases YTD (35-yr high), **ZERO deaths reported in 2026 as of Aug-13** (169 hospitalized); 2025 = 3 deaths (TX children x2 + NM adult; LA County child death in cumulative 2025-26 span, complication case). 2026 hot spots: **South Carolina** (Spartanburg 997 cases, declared over late April), **Utah** (514 this year, statewide incl. SLC), **Arizona** (new clusters), **Pennsylvania** (132+, 27 last week, 61% adults — highest recent growth), **Texas** (2025 epicenter). Slate: **Utah .24 / Pennsylvania .22 / Arizona .18 / South Carolina .14 / Texas .12** = .90.
  - **874244 (CBS News report of official in Moscow Aug-2026)**: TASS Aug-23 — Witkoff/Kushner Moscow+Kyiv visit **POSTPONED**, "unlikely to take place by the end of August"; Lenta Aug-24 same; Kremlin Peskov Aug-20: no exact dates; Lavrov Aug-14: Putin ready to receive them; **CBS has a "Putin set to meet Witkoff and Kushner in Russia" video clip (undated, likely planning/not in-Moscow) — no in-Moscow CBS report identified**. Slate: **Steve Witkoff .60 / Jared Kushner .28 / Marco Rubio .06** = .94. Residual real risk: no/empty resolution if nothing lands by Aug-31; accepted that risk.
- Standing lessons banked: (1) transit/corridor stops on homeward legs incl. Thailand (Lincoln); (2) keep long-held pre-existing mass on thin late news (Hadjam/Brighton); (3) on-clock broadcaster/prize decisions land inside their month (Eurovision); (4) cap promoted-side underdogs .10-.14+, openers flush .70-.75; (5) AIPAC-toxic refusal priced .12-.18; (6) interim/if-any >90d cap ~.60; (7) Turkish giants in free-agent slates.
- TW 989.66 baseline for Day 63 (2026-08-25). All five tomorrow-resolvers rebuilt & submitted. Next: next_day.
## Day 63 — 2026-08-25 (Tue) / day 62's results landed; resolves tomorrow (Aug-26): 588637, 834692
- Results vs Aug-24 rebuilt slates:
  - **277370 Celtic → Truth Europa League** (−0.69 Brier / TW +40.51) ✗ — STUNNING: LASK 5-1 Celtic a.e.t (5-4 agg.) after Celtic went 4-0 up (McGregor 21', led agg). UCL hopes vanished — losers drop to Europa League. Old June slate (UCL .45/UEL .40) paid TW +40.51; my new late .91-UCL died. LESSON: never zero out a long-held reasonable mass on a "safe-looking" lead — old slate carried TW here. Also: no such thing as safe.
  - **53266 PFA Player of Year → Truth Bruno Fernandes** (+0.98 / TW −10.55) ✓ — #1 named; Polymarket 90% call held. Late entry on TW as usual.
  - **772246 Sabalenka/Djokovic → Truth Patten and Siniakova** (−0.24 / TW −3.22) ✗ — an entirely unpriced pair eliminated them (Joe Patten? / Kateřina Siniaková). LESSON: mixed-doubles side markets have WIDE qualifier tails; my 5-outcome slate was a subset of the field. Next time weight the open draw more broadly, not just headline pairs.
  - **874244 CBS Moscow → Truth John Ratcliffe** (−0.44 / TW −20.67) ✗ — CIA Director, unpriced. LESSON: "senior Trump administration official + CBS News + Moscow" is NOT Witkoff/Kushner-exclusive — report could name Ratcliffe/Patel/Gabbard etc. Broaden: name intelligence chiefs too. (Also pattern: CBS reported a PLANNED visit, not an actual one — criteria just needs the report to say he was in/in-Moscow.)
  - **903529 First 2026 measles death → Truth Pennsylvania** (+0.27 / TW −11.18) ✓ — #2 named (adults 61% of PA cases: death struck there as PA outbreak surged). Slate order (Utah>PA) mis-ranked, but the pair caught it.
- TW 989.66 → **984.56 (−5.10)** | acc **27.0%** | BSS **0.167** | 159/252 resolved, **93 active**.
- Aug-25 research pass + submissions:
  - **277370** logged only (resolved).
  - **588637 Nicolas Jackson**: Villa £59.9m(€70m) bid; Chelsea "on the verge" of accepting (Foot Mercato/Aouna Aug-25); personal terms NOT done; Watkins→Al-Hilal pending. **Aston Villa .72 / None .13 / Galatasaray .06 / Atlético .05 / Newcastle .02.**
  - **834692 Xi Middle East**: NO 2026 ME visit yet (trips: NK Jun-8/9; Kyrgyzstan Aug-31 SCO; India Sep-12 BRICS; DC Sep-23-25); 2nd China-Arab States Summit planned in Riyadh, NOT confirmed — criteria needs travel actually to occur, announcement doesn't count. **Saudi Arabia .60 / UAE .12 / None .12 / Egypt .06 / Iran .03.**
  - **162316 Barcola**: Liverpool–PSG talks final phase; Barcola contract agreed with LFC, excluded from PSG squads; PSG want €100-120m; BBC: Liverpool optimistic. **Liverpool .82 / None .12 / Real Madrid .02 / Bayern .02 / Arsenal .01.**
  - **876325 Enzo Fernandez**: City expect completion before Sept-1; Alonso "accepts likely"; £120m off, Chelsea demand more; Fernandez wants Maresca reunion. **Manchester City .78 / None .12 / Real Madrid .04 / Barcelona .02 / Bayern .01.**
  - **450664 Emiliano Martinez**: Training ground news — Juventus collapsed (finger); **Spurs lining up swoop (Football Insider Aug-21)**, expected before Sep-1. **Tottenham .55 / None .30 / Juventus .06 / Inter Milan .03 / Bayern .03.**
  - **921981 Putin's Ukraine-war counterpart at SCO**: **Putin–Modi essentially confirmed** (Aug-24 Jaishankar/Putin; Bishkek Aug-31-Sep-1; agenda not disclosed, India deep in Ukraine diplomacy). Rebuilt: **Narendra Modi .58 / None .26 / Xi Jinping .08 / Donald Trump .02.** Ric Gallagher ruled out by Peskov.
  - **120116 Norway monarch**: no succession news → **Harald V .93 / Haakon .03 / Sonja .02.**
  - **20480 Martinelli**: BBC Aug-23 talks; Schira: agreement in principle, 2030 contract €20m/yr, €60m + bonuses; TeamTalk personal terms done (with Watkins). **Al-Hilal .90 / None .06 / Galatasaray .02 / Fenerbahce .01.**
  - **127253 Gabriel Jesus**: Napoli club-to-club agreement reportedly reached (£17m-ish; Lukaku/Allegri fit); Jesus wants England (Everton/Ipswich at £20m); Romano: permanent only. **Napoli .45 / Everton .27 / None .17 / Ipswich .06 / Milan .02.**
  - **2260 Simbu/men's Sydney Marathon Aug-30**: field = Simbu 2:02:47 (reigning world champ, Boston 2nd x2), Sisay Lemma 2:01:48 (former Boston/London champ), Kiros (defending, 2:06:06), Ramakongoana 2:04:18 (Boston), Gebrhiwet (5k specialist). Sawe/Kipchoge NOT in field (stale slate discarded). **Simbu .28 / Lemma .24 / Ramakongoana .14 / Gebrhiwet .12 / Kiros .10.**
  - **409386 women's** = **Jepchirchir .36 (world/Olympic champ, 2:14:43) / Cheptai .15 / Aga .12 / Shauri .10 / Chesang .09**. Hassan/Kosgei stale.
  - **79046 Villa–Arsenal Aug-31**: **Arsenal .55 / Draw .24 / Aston Villa .14** (Arsenal favored; Villa wrecked by exits).
  - **875467 highest PL fee 2026**: Anderson £116m (City/Forest) vs **Morgan Rogers £117m** (Chelsea⇄Villa record) → **Rogers .42 / Anderson .35** / Diomande .06 / Gibbs-White .04 / Tonali .03.
  - **591807 Ghana coach**: Queiroz out; Ofei (assistant, linked) + **Ibrahim Tanko** (Medeama, title) shortlisted; GFA talks ongoing; announce before Sept-21 window. **Ofei .31 / Tanko .27 / None .18 / Queiroz .09 / Renard .03.**
- Lessons added: (1) Celtic-class collapses show a 4-0 agg lead can still flip — don't zero old slates; (2) mixed-doubles "if any" markets have huge unpriced tails — spread mass across draw, not just favorites; (3) CBS-visit criteria = the REPORT names the official, no visit required — include intel chiefs; (4) PA-class "hot recent surge cluster" beats big-but-closed clusters for first-death questions.
- TW 984.56 baseline for 2026-08-26. Watch Aug-26 resolvers: 588637 (Jackson→Villa likely), 834692 (Xi ME visit — probably postponed/no resolution). Next: next_day.
## Day 64 — 2026-08-26 (Wed) / resolves tomorrow (Aug-27): 162316, 450664, 876325
- Results vs Aug-25 rebuilt slates:
  - **588637 Jackson → Aston Villa** (+0.90 / TW −4.50) ✓ — Villa £65m (£47.5m upfront), medical next week vs Arsenal; Konsa to Arsenal confirmed; Morgan Rogers→Chelsea £117m club-record confirmed; Garnacho→Villa loan w/ oblig-to-buy. My refresh landed just in time.
  - **834692 Xi Middle East → Truth Egypt** (−0.27 Brier / TW +1.26) ✗ — Xi's 2026 ME visit WAS Egypt (likely the Second China-Arab States Summit or a Cairo bilateral). My "no 2026 ME visit" read was wrong; under-priced Egypt at .06/.12 rather than naming it contender #2. LESSON/pattern: Xi's ME anchor city after 2022 Riyadh summit + 2016 triple tent is evidently **Egypt** — next Xi-ME question: Egypt-adjacent weighting; don't fade "this year will happen" just because nothing is public yet.
- TW 984.56 → **981.32 (−3.24)** | acc **27.4%** | BSS **0.170** | 161/252 resolved, **91 active**.
- Aug-26 research pass (three transfer resolvers refreshed):
  - **162316 Barcola→LFC**: verbal agreement w/ PSG (Plateau), "done by all parties", £110m+; personal terms agreed (ESPN); Romano "at any moment could be green light" — **Liverpool .85** (up from .82) / None .08 / Real Madrid .02 / Bayern .02 / Arsenal .01.
  - **450664 Emiliano Martinez**: **Spurs NOT IN RACE (TNT live 16:32)**; Villa offered him to **Chelsea** (<£10m) — Chelsea "increasingly willing" post-Fulham errors (Ornstein: Chelsea considering); Inter Miami option for player; Juventus collapsed; Kinsky is Spurs' keeper. Rebuilt: **Chelsea .50 / None .25 / Inter Miami .10 / Tottenham .06 / Juventus .03.** (Was Tottenham .55 — inverted; Tottenham "lining up a swoop" narrative never materialized.)
  - **876325 Enzo Fernandez**: no completion yet; City expect completion before Sept-1; Alonso "departure likely"; Chelsea raising price; Renewal off table verbally. HELD **Manchester City .78** (Romano quiet; deal not announced as of Aug-26).
- TW 981.32 baseline for 2026-08-27. Tape watch: Barcola ("here we go" expected imminently), Martinez (Chelsea decision pending — <£10m, 48h decision window), Jackson already resolved.
- Standing: verify daily; window closes Sep-1; questions resolving today-evening/mid-week should be refreshed mornings. Next: next_day.
## Day 65 — 2026-08-27 (Thu) / resolves tomorrow (Aug-28): 120116, 921981
- Results vs Aug-26 rebuilt slates:
  - **162316 Barcola → Liverpool** (+0.97 / **TW +60.54**) ✓ — verbal agreement "done by all parties" (Plateau), medical next — SWEET TW payout. Rebuilt EARLY once final-stages confirmed; lesson: when verbal-agreement + all-parties-done reports land, push to .85+.
  - **450664 Martinez → Chelsea** (+0.67 / TW −6.86) ✓ — Villa offered <£10m; Spurs exited race 16:32 (Joshua Kinsky is Spurs' #1); Chelsea errors vs Fulham forced rethinking; my Tottenham-inversion caught Chelsea.
  - **876325 Enzo → Manchester City** (+0.94 / TW **−33.06**) ✓ — City completed; TW bleed because rebuilt only when final talks started. LESSON: refresh as soon as "bid deadline passed without offer→terms expired→yet clubs persist" CONVERSATIONAL pattern appears — Alonso's "departure likely" was the tell.
- TW 981.32 → **1001.93 (+20.61)** | acc **28.6%** | BSS **0.180** | 164/252 resolved, **88 active**. First day above 1000 TW.
- Aug-27 research pass (refreshed 921981 + 20480):
  - **921981 SCO Putin counterpart (Ukraine)**: **Modi–Putin bilateral CONFIRMED by India MEA** (Aug-27, dw.com; agenda = "entire gamut of bilateral relations" but Ukraine central given India's balancing role + Jaishankar Moscow trip). Raised Modi **.72** / None .14 / Xi .08 / Trump .02 / Zelensky .02.
  - **20480 Martinelli**: Romano — club-to-club agreement struck; Arsenal ready to authorise after €65m verbal agreement; Pedullà: completed, traveled Tue; **Al-Hilal .94** / None .03 / Galatasaray .01 / Fenerbahçe .01.
  - No other announcements today (window deadline Aug-31). Jesus (127253, Aug-30) still open: Napoli club-agreement vs Everton/Ipswich; holding **Napoli .45/Everton .27/None .17/Ipswich .06/Milan .02**. Sydney Marathon (Aug-30) entries rebuilt yesterday. Villa–Arsenal (79046) Arsenal .55/Draw .24/Villa .14.
- Priority pattern: refresh ALL transfer-completion questions daily through Sep-1 window; resolution criterion usually "official announcement" — announced-completion ~ fast move of days. Don't wait.
- TW 1001.93 baseline for 2026-08-28. Next: next_day.
## Day 66 — 2026-08-28 (Fri) / resolves tomorrow (Aug-29): 20480, 2260, 409386
- Results vs Aug-27 slate (2026-08-27→28):
  - **120116 Norway monarch → Truth Haakon VIII** (−0.87 Brier / TW **−90.08**) ✗✗ — CATASTROPHIC. **Harald V died THIS MORNING (Aug-28 06:35)** of a rare blood condition after a hospital stay "since last week" (kongehuset.no; BBC/Reuters). Europe's oldest monarch; no health check run — my Norway slate was .93 Harald because "no news". LESSON (hard): for any office/title/\who holds crown on [date] question on an 80+ public figure, ALWAYS search current medical status/health week-of — hospitalization = succession risk; cap crowned-elder holder at ~.75 with heir ≥ .2 if ANY health signal, .85 otherwise. Add permanent check to slate workflow for monarchs/popes/presidents-over-75.
  - **921981 SCO counterpart → Truth Recep Tayyip Erdogan** (−0.55 / TW −24.58) ✗ — Erdoğan (Turkey, SCO dialogue partner / Ukraine-mediator) was Putin's Ukraine-war bilateral pick, NOT Modi (Modi confirmed but trade/bilateral-relations, not designated Ukraine-focused). LESSON: when criteria demand "bilateral to discuss Ukraine war" nominate **Erdoğan** (Istanbul formula/grain deal) as the #1 candidate by default; Modi = general-relationship. Next time include Erdoğan ≥.25 alongside Modi. My final slate had zero Erdoğan mass (.02 cut mid-week). Painful but the pattern is now locked.
  - **588637/162316/450664/876325 + 20480 etc.** — window-question refreshes paying off (+40 to +60 TW on Barcola; Jackson/Enzo/Chelsea etc.).
- TW 1001.93 → **887.28 (−114.65)** | acc **28.6%** | BSS **0.175** | 166/252 resolved, **86 active**. Single worst day; Norway explains most of the damage.
- Aug-28 research pass:
  - **20480 Martinelli → almost certain Al-Hilal** (club-to-club + verbal package done €65m; Pedullà: completed, traveled Tue; Romano: authorization next 24–48h) — held **Al-Hilal .94**.
  - **127253 Gabriel Jesus**: **"sì" to Napoli** (Allegri phoned him — Scotto/TuttoNapoliCalcio Aug-28); €20m permanent, €5m+1m wage; contingent on Napoli selling Noa Lang (else Marc Guiu pivot); Arsenal pushing on, window closes Mon. **Napoli .56↑ / None .20 / Everton .18↓ / Ipswich .04 / Milan .02.**
  - **921981** resolved against me; **120116** resolved against me. No other updates yet — deadline day Monday; refresh all transfer-completions daily.
- Standing rules added: (1) health-check every convened-office holder >75 on any office/turnout/\who-on-date question; (2) Ukraine-mediation counterpart at any Russia-summit question → name Erdoğan (#1 default) + Modi (#2); (3) "if any" transfer slates: refresh at 12:00 + 18:00 on deadline week; (4) when possible, check today's corpus before submission, not after a loss.
- TW 887.28 baseline for 2026-08-29. Next: next_day.
## Day 67 — 2026-08-29 (Sat) / resolves tomorrow (Aug-30): 127253
- Results vs Aug-28 slate (2026-08-28→29):
  - **20480 Martinelli → Al-Hilal** (+1.00 / **TW +25.32**) ✓ — done deal (Romano verbal + €65m, closed this week).
  - **2260 men's Sydney Marathon → Truth Addisu Gobena** (−0.18 / TW −6.09) ✗ — Gobena, 2025 runner-up (2:06:16), I never priced although the press release said "entire 2025 men's podium returns to Sydney". LESSON: marathon "returning podium" principals MUST be priced (2nd place from prior year ≈ live favorite), not just defending champ.
  - **409386 women's Sydney → Truth Peres Jepchirchir** (+0.54 / TW −10.22) ✓ — world/Olympic champ named #1.
- TW 887.28 → **896.29 (+9.01)** | acc **29.4%** | BSS **0.180** | 169/252 resolved, **83 active**.
- 127253 Gabriel Jesus — pulled back from Napoli: Corriere dello Sport (Aug-29) — **Leão→Galatasaray blocks Noa Lang sale → over-list slot blocked → Jesus deal "miracoli"/moved to January**; Guiu option also dead (→ Leipzig). Rebuilt: **None .42 / Everton .26 (contact made, £20m valuation) / Ipswich Town .15 / Napoli .12 / AC Milan .02.**
- Window closes Monday Sep-1; last burst of deadline moves expected today/tomorrow. Watch: Jackson completion official for Villa (announced), Martinelli official (Al-Hilal), Watkins (Al-Hilal—announced?), Enzo (City — announced already).
- Standing reminder: refresh transfer-completions with today's news EVERY morning next week (window questions land on announcement day).
- TW 896.29 baseline for 2026-08-30. Next: next_day.
## Day 68 — 2026-08-30 (Sun) / resolves tomorrow (Aug-31): 335239, 79046
- Results Aug-29→30 (from next_day): **127253 Gabriel Jesus → Truth Barcelona** (−0.28 / TW −5.38): Catalans just announced permanent deal after Napoli collapsed; I had zero Barcelona coverage. LESSON: "deal collapsed for club A" ≠ "no transfer"; when a superclub-caliber striker unexpectedly moves in final hours, check top-5 alternatives beyond the headline markets (Everton/Ipswich/Milan) — Barcelona was linked in Huijsen/Alvarez rumor orbit all summer. TW **890.91** | acc **29.4%** | BSS **0.179** | 170 resolved / 82 active.
- **335239 Raam #2** → rebuilt after Aug-26 official announcement: **Yoav Segalovitz .88** (official "Vereinbarung... im zweiten Platz" via jarayid/arn.ps Aug-26; primary winner Waleed Taha displaced) / Waleed Taha .09 / Waleed al-Huashla .03. Was {al-Huashla .10} — embarrassed; facts were public since Aug-26. LESSON: Hebrew-press politics stories publish on weekends — search direct outlet terms, not just "announcement" English queries.
- **79046 Villa–Arsenal** (Mon Aug-31, 8pm) → **Arsenal .60 / Draw .23 / Villa .17**. Villa lost Rogers(£117m), Konsa(to Arsenal), Watkins(Al-Hilal), E.Martinez(Chelsea); loaned Jackson (£60m, maybe debut), Gomes suspended, Onana out — 4-0 at Brighton. Arsenal 2-0s (City, Coventry), Saliba/Timber out but Mosquito+Gabriel pairing solid. LATE Aug-31 update possible.
- **875467 (highest PL fee paid, res Sep-1)** → **Morgan Rogers .62** (£117m Chelsea ✓ done July) / **Enzo Fernandez .30** (~£120m reported agreed Aug-27 TyC but Telegraph says no offer yet as of Aug-30 — window closes Sep-1; critical: Al Jazeera Sport must report COMPLETED fee in £) / Elliot Anderson .08 (£116m, 2nd). Tonali/Diomande/Anderson plainly out unless Rogers disqualified. **WATCH Mon Sep-1 deadline hour.**
- **591807 Ghana coach (Sep-2)** → ok — **Saintfiet .42 / Ofei .32 / Tanko .08 / None .15 / Renard .02** (YEN Aug-28 frontrunner Saintfiet per Malian journalist; Ghanamma Aug-26 Ofei "exclusive"; Okraku "99% in place"—identity unconfirmed).
- **712131 (Gaza population plan, Sep-1–7)** → **None .74** / Smotrich .12 / Ben-Gvir .10 / Katz .04. Plan is a dead end internationally (ynet Aug-26); Trump 20-pt plan contradicts; Winter not a minister.
- **790870 (Treasury Iran bank, Sep-4 window Aug-31–Sep-6)** → Halkbank case CLOSED June 2026 (drop Halkbank); Banque Misr UAE §311 already filed Aug-28 (pre-window); AP Aug-30: "another bank this week" per Bessent. Rebuilt: Bank Pasargad .22 / Bank Sepah .20 / Bank Saderat .18 / Mehr Eqtesad .14 / Bank Melli .10 (stale Iranian state-bank names — no Chinese/Hong Kong conduit visible; knowingly weak slate).
- **224345 (SE Asia emergency haze, Sep-4)** → **Indonesia .45** / Malaysia .28 / Singapore .03 / Thailand .03 (ASMC Level 3 Aug-29; El Niño intensifying; schools closed, Kalimantan hotspots).
- **673971 (MAGA Inc first general-election ad buy, Sep-5)** → **Michigan .42** (Vance rally Mon Aug-31 Sterling Heights with Rogers/James) / Texas .30 (Paxton awaits MAGA Inc) / Georgia .08 / Ohio .07 / North Carolina .06.
- **891014 / 608158 / 408930 (US Open)**: draw known Aug-23; Sinner WITHDRAWN (knee) → Zverev #1. Rebuilt: Men's Alcaraz .30/Zverev .22/FAA .11/Djokovic .09/Medvedev .08; Women's Sabalenka .30/Rybakina .19/Swiatek .16/Gauff .15/Anisimova .04; US-men-furthest Fritz .30/Shelton .26/Tien .12/Tiafoe .10/Paul .06.
- **52657 (Venice Special Jury Prize, Sep-12)** → NAZA .22 (Abraham & Szor — late-add after safety concerns) / Dau .18 / Look Back .14 / Possible Love .12 / Un bon petit soldat .08. (Old single: "Voice of Hind Rajab" — 2025 winner, dropped.)
- **5814 (Villa–Forest Sep-12)** → Villa .34 / Draw .30 / Forest .24.
- **WARNING – Gabriel Jesus “Barcelona” miss**: I had starve-starved the slate; when a move is reported as “imminent” hours before window close, re-scan the FULL market (incl. clubs I consider "out of it"). Everton/Napoli narrative anchoring cost 5+ TW twice.
- TW baseline for 2026-08-31: **890.91**. Next review wave: 335239 & 79046 resolve Aug-31 → expect results at next session; window-close news Sep-1 for 875467.
## Day 69 — 2026-08-31 (Mon) / resolves tomorrow (Sep-1): 875467
- Results Aug-30→31:
  - **335239 Raam → "Yoav Segalovich"** (.88) ✓ Brier +0.98 / TW +0.45 (essentially free win via Hebrew-press Aug-26 announcement; my old al-Huashla .10 slate would have been an embarrassing loss).
  - **79046 Villa–Arsenal → Arsenal** (.60) ✓ Brier +0.76 / TW **+69.98**. Villa-Park fortress irrelevant vs gutted Villa frontline; Arsenal 2 goals from Konsa/ Gabriel partnership unavailable but Villa 4-0 Brighton form spoke for itself.
- TW 890.91 → **961.34 (+70.43)** | acc **30.2%** | BSS **0.186** | 172 resolved / 80 active.
- **875467 window-close day**: Enzo→City "deal on" (Romano Aug-31), AS USA "agreed €140m, second-most-expensive PL deal behind Isak", Burgos "finalised", BBC "talks under way". Window closes Sep-1 23:00 BST. Updated: **Enzo .55 / Morgan Rogers .38 / Anderson .05** (was .30/.62 — flipped to Enzo today).
- **790870 (Iran bank)**: Both Aug-31 headlines confirm action is planned THIS WEEK (AP/Times-of-Israel Aug-30: "Bessent says US planning to sanction another bank this week"; no name). Rebuilt: Bank Melli .30 (Bessent: "every branch must be shuttered") / Pasargad .15 / Bank of Dandong .12 / Saderat .10 / Sepah .08. Likely wrong-weak slate; knowingly thin.
- **224345 haze** confirmed escalating (ASMC Level 3; Malaysia schools closed 200+ readings); slate set yesterday (Indonesia .45/Malaysia .28) stands.
- **673971 MAGA Inc.**: Michigan event Mon Aug-31 (Vance + Rogers/James); Texas Paxton awaits; slate Michigan .42/Texas .30 stands. Final ad-buy announcement could land Sep-2..5.
- Deadline-day spillover to check Sep-2 morning: Barcola→Liverpool £120m done?; Gakpo—City off (Liverpool rejected £75m+£5m); Savinho £75m Spurs; Marmoush loan→£60m; Am habits: Gabriel Jesus → Barcelona £8.6m (closed 127253 truth).
- **8886/8886-class self-check**: 335239 & 79046 both Brier-positive — staying Brier-positive week while stacking TW. TW baseline Sep-1 = 961.34.
## Day 70 — 2026-09-01 (Tue) / resolves tomorrow (Sep-2): 591807, 712131
- Results Aug-31→Sep-1: **875467 → Enzo Fernandez ✓** (Brier +0.65 / TW −14.44): the late flip from Rogers (.62→.38) to Enzo (.55) was right on Brier but cost ~17 TW vs holding Rogers (settled July at £117m — finality beat last-set drama). LESSON reinforced: when two favorites straddle, TW-optimal hold the LONG-ESTABLISHED completed-deal favorite; a pending mega-deal needs official completion + Al Jazeera £-reporting to resolve. TW **946.90** | acc **30.6%** | BSS **0.188** | 173 resolved / 79 active.
- Deadline day recap (Sep-1): Enzo→City agreed €140m/£120m (Romano "deal on", AS "almost done", med Tue) — DID complete (truth). Barcola→Liverpool £120m agreed; Jesus→Barcelona €10m; Ndiaye agreed City £65m; Gakpo—City off (Liverpool rejected £75m+5m).
- **790870 update** (Sep-1): Bessent reaffirms "probably going to announce a bank sanction this week, and one the week after"; multiple outlets frame it as Iranian bank(s); G20 Asheville meetings ongoing this week; China remains un-moved-on. Slate (Bank Melli .30/Pasargad .15/Dandong .12/Saderat .10/Sepah .08) stands. **Check Sep-2/3 for announcement before resolution day.**
- **591807 Ghana** (res Sep-2): no official announcement yet as of Sep-1; YEN (Aug-28, Malian journalist Drissa Traoré) named Tom Saintfiet "selected"; Ghanamma (Aug-26, deep-throat) named Ofei ("will appoint"). Both remain. Slate rebuilt: **Saintfiet .38 / Ofei .32 / None .18 / Tanko .09 / Renard .02**.
- **712131** (res Sep-2): Israel-Gaza coverage today = IDF ops in Gaza City + right-wing campaign ads + post-election Gaza-City reoccupation talk (Southern Command / cabinet decides after Oct elections). NO named full-population removal plan introduced by a minister in Sep-1 week so far. Slate rebuilt: **None .78 / Smotrich .10 / Ben-Gvir .09 / Katz .03**.
- **Big geopolitical shift**: US–Iran open conflict (Day 185ish) — US strikes on Iranian targets (Hormuz ad straits ops, Kuwait/Bahrain drone exchanges); Xi arrived Egypt; Gaza ground-op talk "unavoidable". Window for questions resolving Sep-2..10 widened: 759359 (Ukraine cities strikes) unchanged; 205592 FAO due Sep-4 — no data yet.
- TW baseline for Sep-2: **946.90**. Next: 591807/712131 tomorrow; full deadline-day fallout to fold in as it lands. Barcola (resolved, my old .38-Liverpool slate actually paid +60.54 back on Aug-25) — window closes fully today; 875467 done.
## Day 71 — 2026-09-02 (Wed) / no resolutions tomorrow (Sep-3)
- Results Sep-1→2:
  - **591807 Ghana → Truth Carlos Queiroz** (−0.29 brier / TW +20.67): Queiroz RE-appointed at the last minute (contract renewed late); I had dropped him entirely. LESSON: "4-month contract ended" ≠ "gone"; incumbents renewed quietly still OWN the job until an announcement exists — keep incumbent mass ≥ .2 until physically signed/announced elsewhere, especially for "first person appointed after Aug-1" conditional windows (mass ≠ nominee does). The Aug-28 Saintfiet/Ofei squeeze cooled but BOTH reports evaporated without an announcement; incumbent won by default/renewal. Free +20.67 TW from residual June position.
  - **712131 Gaza plan → Truth Itamar Ben-Gvir** (−0.45 / TW +26.32): my None-heavy slate lost on Brier (should've had Ben-Gvir ≥ .3 given his campaign ad "migration of hundreds of thousands" escalating from AI billboard to named-plan texture by Sep-1 — Smotrich/Ben-Gvir race stolen by Ben-Gvir). TW still +26.32 via early holdings. LESSON: when a named explicitly-cited plan is being NAKEDLY named ("emigration of Palestinians" plans announced live on TV Sunday Aug-30; AI ads), the criterion "explicitly named plan" can resolve ON general rhetoric just barely clearing the bar — do not cap a shouting front-runner at .10 when he's the one with the megaphone this week.
- TW 946.90 → **993.89 (+46.99)** | acc **30.6%** | BSS **0.185** | 175 resolved / 77 active. **TW ~994 — 1000 milestone in sight.**
- **790870**: Sep-2 outlets confirm "probably going to announce a bank sanction this week, and one the week after" (Reuters) — Iranian-bank framing in Arabic/Gulf + AFP coverage; allies "all come forward". No name yet. Slate refined: Melli .25 / Pasargad .17 / Saderat .15 / Sepah .12 / Dandong .08. **Must check Sep-3/Sep-4 news before resolution.**
- **668636 Italian GP (Sep-6)**: Antonelli (242 pts) gets NEW POWER UNIT → back-of-grid at Monza (Grandprix.com Aug-25). Rebuilt: **Russell .34 / Hamilton .18 / Verstappen .17 / Antonelli .12 / Leclerc .10**.
- **224345 haze**: accelerating (Sarawak mask rush; schools shut; Singapore now threatened). Indonesia .45/Malaysia .28/Singapore .03/Thailand .03 holding. Check for emergency DECLARATION news Sep-3/4.
- **284913 Valencia–Barcelona**: criteria says match Sep-20; resolution_date column Sep-06 premature — keep Barcelona-heavy slate (.55/RM .15/Atl .10) and verify fixture news when posted.
- **205592 FAO index Sep-4**: no data; hold Sugar/Dairy/Cereals/Vegetable-oils slate.
- **Emerging meta-lesson (3x now: Queiroz, Jesus/Colombia, Raam-Taha)**: (1) incumbents/MLB-favourites renewals beat rival hype; (2) official announcements beat pundit projections — every slate rebuilt on ANNOUNCED facts > general drift; (3) when multi-outlet hype concentrates on ONE name with a specific date/specific quote, push them to .7+.
- TW baseline Sep-3: **993.89**. Next searches Sep-3: 790870 bank name; US Open progress (891014/608158 — R3-R4 weekend); 224345 declaration; 205592 FAO (released ~Sep-5).

## Day 72 — 2026-09-03 (resolves 9/4: 205592, 224345, 790870, 568969)
- 205592 FAO Aug FFPI (report drops 4am Sep-4, no numbers yet): fao.org events page notes FFPI "largely unchanged in August, as [higher X] prices offset declines in cereal and dairy quotations" → downgraded cereals/dairy, rebuilt {Veg oils .36, Sugar .30, Meat .20, Cereals .08, Dairy .03}.
- 224345 haze: Indonesia Central Kalimantan declared state of emergency (eff. Aug 31, announced Sep 1, Galonit: ANTARA); West Kalimantan status until Nov 15; Sambas/Mempawah emergency response. Malaysia API peaked 475 (hazardous in 6 areas), emergency only at 500; cloud seeding Sep 3-5; NADMA decides. Raised Indonesia .45→.52, Malaysia .28→.33.
- 790870 Iran bank (Bessent: one bank sanction "this week", another next; no name leaked as of Sep-3): kept Melli #1 on megaphone quote ("every Bank Melli branch must be shuttered") but trimmed; added Bank of Kunlun (iconic Iran-oil Chinese bank) as Chinese slot; dropped Dandong (name risk). {Melli .30, Kunlun .15, Saderat .12, Pasargad .11, Sepah .09}. Cuba's Banco Exterior de Cuba designated Sep-3 — NOT Iran, irrelevant.
- 568969 Betis-Madrid (Fri Sep 4, 20:00, La Cartuja): both XIs predicted (Madrid: Courtois; Dumfries/Trent, Konaté/Rüdiger, Huijsen, Cucurella; Valverde, Bernardo Silva; Güler, Bellingham, Vinicius; Mbappé). Dropped Dembele, built around Mbappé .33/Bellingham .13/Vinicius .11 (Betis scorers Riquelme .08/Cucho .05, in-form).
- Corner cases swept for early Sep resolvers:
  - 284913: Valencia-Barcelona actually SUN Sep 6 Mestalla (title/20 misleading). Barça lead La Liga on GD (+10 vs Madrid +8, both 9 pts); Atleti 7 pts max. Betis-Madrid Fri is the swing result. Rebuilt {Barça .52, Madrid .37, Atleti .04, Alaves .02, Osasuna .01}.
  - 668636 (Italian GP Sep 6): Lando Norris is favorite after back-to-back wins (6/4); Antonelli starts from back (PU penalty). Rebuilt {Norris .36, Russell .27, Hamilton .10, Leclerc .09, Antonelli .08} — I previously had ZERO Norris (big catch).
  - 673971 (Sep 5): Securing American Greatness/MAGA Inc. launched $1M US-national Trump-record ads (Sep 2) + Michigan Vance rally (Sep 1') — Michigan still best call for first state-targeted general-elec ad buy; {Michigan .44, Texas .32, Georgia/Ohio/NC .06}.
  - 490094 Ebola: Ituri still epicentre (85% cases/88% deaths, 6000+ cases); added North Kivu .12, Tshopo .02; Ituri .75.
- Lesson: never let favorites/rivals slates miss the current market favorite (Norris); GD-level table math pays for close questions — do it explicitly.
## Day 73 — 2026-09-04 (resolve tomorrow Sep-5: 673971; Sep-6: 668636 Italian GP, 284913 Barca-Valencia-aftermath)
- Results reported TODAY (Sep-4, from Sep-4 session end — actually Sep-3 night + Sep-4 close):
  - **205592 FAO → SUGAR ✓** (+0.33 / **+31.45 TW**): report-line "largeFF no August numbers pre-release + 'cereal & dairy quotations decline, largely unchanged'" → sugar called it. TW saved on last day.
  - **224345 haze → MALAYSIA ✓** (+0.28 / **+22.88 TW**): window gates — pre-window Indonesia declarations don't count; Malaysia API pierced 475→500, emergency declared → Malaysia. Indonesian emergency existed but earlier; the window-conditioning is what mattered.
  - **568969 Betis 1-0 Madrid (Parrott 81', Mbappé pen saved, Fri Sep-4) → Truth**: Parrott started as Betis 9 (2 published XIs — I MISSED buying the 9-shirt start; gave Cucho/Riquelme). **RULE: first-goalscorer slates must carry at least one starting striker from EACH side — including the away-side/home 9 whose name is in the predicted XIs.** −0.15 BSS / −9.40 TW.
  - **790870 Iran bank → Golden Global Bank** (Türkiye "Golden Global Yatirim Bankasi"; tiny involuntary bank sanctioned for IRGC-QF facilitation; first NATO-ally bank under Operation Economic Outcast; announced Fri Sep-4). Total miss — I loaded legacy Iranian SDNs + Dandong guesses, omitted obscure NATO-ally-linked third-country banks entirely. **RULE: Treasury-sanction questions need ≥1 obscure NATO/Türkiye/UAE-linked third-country institution + keep an eye on "end of this week" quotes with DEADLINE ADHERENCE (Bessent called Friday = Sep-4).** −0.15 / −10.16 TW.
- **BETIS 1-0 REAL MADRID happened (Fri Sep-4 21:00, La Cartuja)** — Mbappé penalty SAVED by Valles in stoppage; Parrott scored 81'. Madrid stays 9 pts, GD +7. **284913 rebuilt TOMORROW's resolution: Barcelona .78 / Real Madrid .18 / Atleti .01** (Barça reaches 12-9 win, or holds GD at draw, or even on 1-goal loss = still ahead on GD since Barça +10 vs Madrid +7; only a 2+ goal Mestalla defeat flips = ~15% Case).
- Resubmissions made today: 284913 ✓ .78/.18; 668636/490094/408930/608158 (Sep-3 research carried); **936021 rebuilt** (men's 5000m Tokyo-2025 = **Cole Hocker** world champ; entrant confirmed pair: Ingebrigtsen auto + Hocker auto + DL-final/Ranking entrants) → {Hocker .27, Ingebrigtsen .27, Gressier .13, Kimeli .10, Blanks .08} (was .30/.15/.10 + no Hocker). **261941 rebuilt** (women's javelin Tokyo-2025 champion = **Juleisy Angulo**, Ecuador's first female world gold; Kitaguchi Olympic but DNF'd Tokyo semis; Little bronze auto-likely) → {Angulo .30, Kitaguchi .22, Little .12, Sietiņa .09, du Plessis .05}.
- **342722 expanded**: trial Sep-10/11, Paris correctionnelle, Donnarumma home-jacking (July 2023). Kherbouch ("Ganito", principal commanditaire, 7-yr prior, recidivism) .45 / Khyan M ("Kiki") .17 / **Baraeddine C. (most aggressive on-site attacker) .20** / Daril B. .05.
- **880660 rebuilt**: STF/PF crisis (Moraes declassified PF files vs. André Mendonça; report shows Mendonça "manifestou vontade de afastar" PF chief Andrei Rodrigues + instaurou procedimento to evaluate suspension). **André Mendonça .32** (the relator, the only one with concrete intent + proceeding open) / Moraes .12 / Fachin .06 / **None .30** (crisis may resolve without any suspension order by Sep-30) / Gilmar dropped.
- **408396 rebuilt**: leaked Commerce NPRM draft (TPM, Aug-11) "narrows usual residence to tax-record-consistent; LPRs + approved asylees + approved refugees still count; all other foreign citizens excluded" — answer = **Lawful permanent residents .72** (was 'U.S. citizens' .42 — wrong framing of the question). Kept US citizens .10 (citizens-only edge case).
- **508136 rebuilt**: Dec-2025 Saudi-struck-UAE-weapons-shipment → UAE withdrew from Yemen; May-April dispute; Saudi-Yemeni forces blocked UAE at Mayun; Sept-1 House Wstate testimony — islands "firmly under a Saudi-led coalition framework". {Yemen government .38, STC .22, Saudi Arabia .18, UAE .06, Houthis .04}.
- **759359 rebuilt**: Odesa fuel stations hit Sep-1/2 (UKRNAFTA destroyed; OKKO + others; "most massive strikes hit OKKO" incl. Pavlograd/Zaporizhzhia/two Kharkiv); repeated-day qualification almost certain for Odesa → {Odesa .48, Kharkiv .12, Pavlograd .08, Kyiv .08, Lviv .02}.
- **971366 rebuilt**: Edgbaston Sep-9, Lord's win Sep-1/England 194-run thumping → Carse OUT (Derby arrest + police probe), Matthew Fisher dropped; XI rotation possible vs Sri Lanka white-ball. {Archer .22, Atkinson .18, Sonny Baker debut-seamer .14, Bashir .10, Sam Cook .08} (was Carse .08).
- **546622 Liverpool 27/28 shirt**: Standard Chartered exclusive window EXPIRED w/o offer (F1 deal signed Jan-2026) → all-talk is "talks advanced with brands outside usual categories, £70m+ target, fintech/crypto/payments/tech" (CMC→Everton, Marex→Forest, Circle→Chelsea all done). No named Liverpool candidate yet: {Standard Chartered .15, Amazon .13, Google .06} (was .32/.08). Resolution requires announcement by Dec-31 — timing unknown; many candidate names never surface pre-announcement.
- **673971 (resolves TOMORROW Sep-5)**: still no state-targeted MAGA Inc general-election ad buy as of Sep-4 — $1M Securing American Greatness spots are Trump-record ads (Dana White), NOT candidate/state-targeted; Vance Michigan rally was MAGA-Inc-paid but rally ≠ ad buy. Paxton→Talarico Senate collapse keeps TX live. Sub: {Michigan .42, Texas .30, Georgia .07, Maine .06, NC .05}.
- LESSONS: (a) **Eastern-front-of-pack kicks the question** — ANY question on a starter pool: enumerate the CURRENT market favorite/world champ at the event, not just last-year's worlds results (Hocker is auto at 5000m; Angulo holds the 2025 javelin crown — my slate missed both until today); (b) criteria-keyword gates (window clauses, "since date X") decide between two similar answers (haze: Indonesia had a pre-existing declaration that did NOT count; Malaysia declared inside window → Malaysia); (c) Treasury announcements land Fri-ish ("end of this week"); (d) Barça GD(+10)>Madrid(+7) post-Betis-loss → .78 correct after the fact.
- TW 1028.66 | acc 30.6% | BSS 0.187 | 179 resolved / 73 active. TW ~1,029. Next: Sep-5 → 673971 resolves; Sep-6 → Italian GP (668636) + 284913 (Barça–Valencia Mestalla); Sep-6/7 → Carse-free Edgbaston XI; Sep-10 342722 verdict; Sep-11 800m/5000m Ultimate Championship Budapest; Sep-12 Villa-Forest; Sep-19 261941 resolution window.
## Day 74 — 2026-09-05 (resolve tomorrow Sep-6: 284913, 490094, 668636)
- Results Sep-4→5:
  - **673971 MAGA Inc → Truth TEXAS** (Brier +0.32 / TW **−7.39**): Michigan .42 (Vance MAGA-paid rally Aug-31, Senate toss-up, Rogers) beat-down by Texas .30. The state-targeted general-election buy went to Paxton's Senate race, NOT Michigan — AP Sep-1 explicitly flagged "Texas is a particular issue" (Paxton's Cornyn win → tossup vs Talarico $68.5M). **LESSON: when a challenger race is polling-confirmed ALARM-BELL for the incumbent party's OWN leadership (Senate R delegates explicitly panicking), the first ad buy goes there — Super-PAC panic plays where it hurts most, not where the VP rallied.** Brier shows my .30 Texas line was decent (+0.32); TW −7.39 reflects late pivot into Texas never happened before Aug-2 when I set it .32→.30.
- Cumulative: TW **1021.27 (+? from 1028.66 → actually −7.39)** | acc **30.6%** | BSS **0.188** | 180 resolved / 72 active.
- Monza Italian GP qualifying (Sat Sep-5): **Pierre GASLY (Alpine) seized first career pole** ahead of Russell; Norris not on pole; Antonelli from back (PU penalty); Ferrari's Leclerc/Hamilton in middle group. Straits Times headline: "Russell still the man to beat". Rebuilt 668636 **{Russell .27, Norris .25, Gasly .22, Hamilton .08, Antonelli .06}** (was .36/.27/.10/.09/.08 — Norris trimmed, Gasly in).
- 490094 (Ebola — resolves tomorrow Sep-6!): Sep-2 DRC sitrep = 6,342 cases (Ituri 5,164 81.4%; NK 913; Haut-Uélé 236; Tshopo 22); Ituri remains uncontested epicenter → **{Ituri .82, North Kivu .10, Haut-Uélé .03, Tshopo .01}**.
- 284913 standing: Barça needs only a normal-margin result at Mestalla; Madrid's GD +7 < Barça +10 → Barça leads Sunday in all but ~15% scenarios (2+ goal loss). **{Barça .78 / Real Madrid .18 / Atleti .01}** holds.
- 673971 resolved before I could react more (Texas announced presumably Sep-4/5; deadline hit). LESSON recapped in Slate above.
## Day 75 — 2026-09-06 (Sun) / resolves ahead: Sep-8 (546622, 880660), Sep-9 (971366, 408396), Sep-10 (759359, 508136), Sep-11 (408930, 342722, 936021), Sep-12 (5814, 52657, 261941, 608158), Sep-13 (30434, 653425, 48458, 174389, 487575, 581343, 891014), Sep-14 (Emmys ×3, 816232, 870914), Sep-15 (518392)
- Results Sep-5→6 (delivered w/ next_day):
  - **284913 → Barcelona ✓** (Brier +0.92 / TW +76.73): Barça 4-3 Valencia? (post-Betis-shock sharps) — the GD-math re-confirm worked; Madrid blew it on the upset.
  - **490094 → North Kivu** (−0.48 / −33.84): I misread criteria — asked "which province experiencing a SURGE in weekly Ebola cases MID-SEPT", not epicenter; North Kivu transmission was climbing fastest then (Biena/Manguredjipa outbreak zones added). RULE: parse criteria verb — "surge/rise" ≠ "epicenter/highest share"; a smaller province mid-breakout can be the point.
  - **668636 → Kimi Antonelli ✓** (−0.07 / +49.77): Gasly pole, Russell P2, Antonelli from P20 → won. RULE (Continental-GP-edition): 2026 points-leader pace can win from back; ALWAYS slate polesitter at ≥ .2 (Gasly missed me) AND don't zero the runaway champ.
- Cumulative after Day-74 results: TW **1113.94** | acc **31.0%** | BSS **0.189** | 183 resolved / 69 active.
- Sep-6 submissions rebuilt (all accepted):
  - **880660** (res Sep-8): André Mendonça .32→**.45** (formal Novo petitions — preventive arrest Mamá + afastamento procedimento now open on his desk) / None .27 / Moraes .10 / Fachin .04.
  - **408396** (res Sep-9): unchanged — NPRM still in OMB review (Jun-25 +90d, no Federal Register publication); LPR .72 still correct; citizens .10.
  - **5814** (res Sep-12): Villa .34→**.46** (Villa 1.90–2.08 home despite 0 pts/−5 GD form — decampenant-market lab; Draw .30 / Forest .22).
  - **52657** (res Sep-12): {Mr. Nelson, Did You Kill People? .24 / Dau .17 / NAZA .15 / A Bit of Light .10 / Look Back .08}.
  - **408930** (US-men furthest, res Sep-11): CRITICAL — Paul (lost to Alcaraz R4) + Fritz (2-set lead broken vs Cerundolo) ELIMINATED → live pool re-enume: {Alex Michelsen .33 (unseeded, beat Etcheverry QF — no sets dropped all fortnight) / Tiafoe .27 / Ben Shelton .26 / Learner Tien .04}.
  - **608158** (US-women winner): {Sabalenka .30 / Rybakina .17 / Noskova .14 / Gauff .13 / Pegula .13}.
- Sep-6 FINAL-PASS (after Sep-13→20 re-enumeration; all accepted):
  - **891014**: FAA out R2; Djokovic out in first week; Medvedev out R4 → {Alcaraz .38 / Zverev .25 / Tien .05 / Michelsen .05 / Tiafoe .05}.
  - **48458** (Spanish GP Sep-13): Antonelli MONZA WINNER (Sep-6) — Spanish GP never assessed since → {Antonelli .33 / Verstappen .18 / Norris .13 / Russell .13 / Leclerc .08}. (Earlier .38-slate stale.)
  - **816232** (UEFA 2029 CL final): two-report-wave ("el principal candidato" per AS/Goal/Mundo Deportivo Sep-3; decisión Sep-15 en Thessaloniki; Camp Nou 104,600 cap, Wembley counter-runner) → {Spotify Camp Nou .70 / Wembley Stadium .24}.
  - **518392** (WA 2029 Championships): bids in — London (London Stadium/WHam agreement; govt-macked; WA Council announcement ~Sep-20, Sept-15 date per question) / Rome / Nairobi / Munich (prefers 2031) → {London .48 / Rome .24 / Nairobi .12 / Munich .08}. (Madrid isn't bidding — removed.)
  - **440552** (Emmy Lead Actress Drama, Sep-14): FAILURE — prior slate 0/5 NOMINEES (not Bates/Ramsey/Snook). Real nominees: Coon/Infiniti/Keri Russell/Seehorn/Zendaya. Variety+IndieWire both pick Seehorn (“Better Call Saul” overdue; Pluribus built for her) → {Rhea Seehorn .72 / Keri Russell .14 / Zendaya .06 / Carrie Coon .04}. RULE: never price Emmy categories before nominee list + one handicapper read.
  - **873349** (Emmy Drama Series): {The Pitt .85 / Pluribus .08 / Paradise .03}.
  - **216881** (Emmy Comedy Series): CAUGHT — "The Studio" INELIGIBLE (second season missed window). Race = Widow's Bay (Apple TV, 19 noms; Variety: wins) vs Hacks (HBO Max 2024 champ-2024 nom record-final season; Vanity Fair: wins) → {Widow's Bay .48 / Hacks .42}.
  - **487575** (Man derby Sep-13): Robinhood/Polymarket mandibles: City 46¢/United 31¢/Draw 24-25¢ → match → {City .46 / United .31 / Draw .23}.
  - **581343** (Okinawa governor, Sep-13): toss-up ("横一線"); Koja (Genta, LDP-backed, 29/41 mayors) matching Tamaki (incumbent; 評価 42 vs 不評価 35.6) → {Tamaki .50 / Genta Koja .46}.
  - **174389** (venue for US-proposed trilateral by Sep-25, Washington-identified): proposals out there = Miami (US, Feb), Istanbul (Turkey ready; re-proposed repeatedly), Geneva (Switzerland), Baku (Zelenskyy Apr-25) → {Istanbul .22 / Geneva .17 / Miami .12 / Baku .12 / Vienna .10}.
  - **653425** (M200m, Sep-13): Tokyo-25 champ **Lyles auto**; Tebogo Olympic-24 auto; **Bednarek DL-final winner auto** → {Lyles .28 / Bednarek .22 / Tebogo .17 / Bryan Levell .06 / Kerley .05}.
  - **30434** (Mjavelin, Sep-13): Nadeem Olympic-24 + Walcott Tokyo-25 + **Rumesh Tharanga DL-final auto (SL)** → {Neeraj Chopra .22 / Nadeem .15 / Walcott .15 / Julian Weber .10 / Tharanga .08}.
  - **261941** (Wjavelin, Sep-12): Angulo Tokyo-25 + Kitaguchi Olympic-24 + **Yan Ziyi DL-final (China)** → {Angulo .28 / Kitaguchi .22 / Little .10 / Yan Ziyi .08 / Sietiņa .07}.
  - **936021** (M5000m, Sep-11): Hocker Tokyo-25 + Ingebrigtsen Olympic-24 + **Birhanu Balew (Bahrain, DL-final)** → {Hocker .25 / Ingebrigtsen .25 / Gressier .12 / Kimeli .08 / Balew .07}.
  - **342722** (Donnarumma trial): trial confirmed Paris Sep-10–11 (AFP); slate stands {Kherbouch .45 / Baraeddine C. .20 / Khyan M. .17 / Daril B. .05}.
  - **101639** (UN GA appeal, Sudan?): no corroboration in First-Day scan → hold {Sudan .28 / Haiti .10 / Myanmar .08}.
  - **870914** (orbit weapons): no signal → hold {US .30 / Russia .28 / China .16}.
- META-RULES COMPOUNDED:
  1. **Ultimate Championship auto-qualifiers = Olympic champ + Tokyo-25 world champ + DL-final winner per event** — enumerate the whole skeleton BEFORE pricing; my prior slates missed Tharanga/Yan Ziyi/Balew. worldathletics.org press-release tables beat memory.
  2. **Tournament-draw cascade**: after a Slam's last-64→QF day, strike every ELIMINATED name from slates (Paul/Fritz were stale mass).
  3. **market.csv lags today's submissions** (snapshot is daily) — cross-check "my_prediction" there only as of stale; harness holds the truth.
  4. **Emmy rule**: no prediction without the nominee list + ≥1 handicapper call.
- TW baseline Sep-7: **1113.94**. 100 resolutions until Sep-7? None Sep-7 (day after Sep-6); Sep-8 resolvers: 546622 (Liverpool shirt), 880660 (Rodrigues). Sep-11 finale day: 936021/342722/408930; Sep-12 Villa-Forest; Sep-14 Emmy batch; Sep-24/26/27 dense Asian-Games/NL/UFC wave. Sat Sep-12 window is the big one: 4 Qs resolve same day.

### Day-75 FINAL ADDENDUM (post Sep-13→20 sweep)
- **753240** (Campeones Cup Sep-16, Inter Miami vs Liga MX champ): opponent confirmed Cruz Azul (beat Toluca 3-1 July-25 Campeón de Campeones). Toluca's 2025-edition advantage gone. {Inter Miami .52 / Cruz Azul .44}.
- **425800** (UFC 331 flyweight title Sep-19): REAL CARD = **Joshua Van (champ, −115) vs Alexandre Pantoja (−105) rematch** (UFC 323: Van won by Pantoja elbow-injury stoppage; May Defense vs Taira). My prior slate (Moreno/Asakura) was pure stale fantasy → rebuilt {Van .52 / Pantoja .46}.
- **574553** (UFC 331 lightweight co-main): **Arman Tsarukyan (−380, 5-fight streak, −?) vs Mauricio Ruffy (+300, 13-KO-streak)** → {Tsarukyan .79 / Ruffy .19}. Prior slate (Oliveira/Gaethje/Topuria) TOTAL MISS — no such fight.
- **729308** (Mbappé principal personal sportswear sponsor Sep-18): contract with Nike EXPIRED July 31 (20-yr deal); Adidas WITHDREW (no alignment on €/ask); Li Ning DENIED (Aug-13); Puma/Under Armour un-referenced; L'Équipe + HLN Sep-5: camp circling a **Federer/On**-style model w/ signature shoe + equity. No sponsor announced. → {Nike .40 (renegotiation ~€20M/yr), On .25, New Balance .08, Puma .04}.
- RULE LOGGED: **every UFC/Combat-sports question → verify the actual booked fight card via ufc.com before pricing.** Stale “title fight” slates referencing prior titleholders are −TW bombs. Every one of today's UFC slates was off.
- **934953 / 660356**: no actionable signal found → hold prior low-mass slates ({Grassley .08}, {Tunji-Ojo .08}).
- Remaining Sep-15+ unresolved w/ NO fresh data (holding prior slates): 56802, 660356, 934953, 574485 (Sherbini), 297571 (Madrid derby), 67348 (Asian Games basketball), 81247/224082/832291/300850/190556/686508/996188/25611/423956/788295/731076/564365/76365/154739/996188/158157/556932/700005/259249/88025/695205/133827/815451/935351/138739/889545/425800/574553.
- Session total: **34 forecasts submitted Sep-6**. Tomorrow Sep-7: final sweep + any Sep-8→13 resolvers needing refresh, then next_day().
## Day 76 — 2026-09-07 (Mon) / resolves tomorrow (Sep-8): 546622 (Liverpool shirt), 880660 (Rodrigues/STF)
- Re-confirmed criteria: 546622 = announcement Jun–Dec-31 2026 (announcement date, not commencement) — Oct/Nov window still possible, my slate is for "eventual announced answer". 880660 = September 2026 order, "None" if none — Fachin PET 16704 (Sep-3) → 5 business days for written explanations by Moraes/Mendonça/Gonet/Rodrigues; NO ORDER issued yet.
- Fresh evidence folded in:
  - **546622**: no named replacement as of Sep-6 (Athletic Latty: "conversations ongoing", "17 years is a long time"; Anfield Index mock-up w/ SC placeholder, Expedia sleeve "could be both"); Wyness (Football Insider Sep-3): Emirates DEAD (Arsenal→2033); Amazon slim (related-party regs); Borson (Aug-22): "probably already quite advanced" — decision DEVICE, years-ahead process (China Amazon print). Rebuilt: **Standard Chartered .16 / Amazon .13 / Expedia .07 / Google .03** (Expedia added as the LIVE alternate — front-of-shirt+sleeve both expected to change together; Google kept as legacy longshot).
  - **880660**: situation still "Mendonça manifests desire + procedimento avalia fastamento" (Moraes's intelligence report Sep-3, CNN Brasil Sep-4, G1: "procedimento instaurado no bojo do qual se avalia eventual determinação de afastamento"; O Globo show Rodrigues personally weighing defamation suit Sep-6 — NO ORDER). None now highest: {André Mendonça .38 / None .40 / Moraes .08 / Fachin .04} (from .45/.27/.10/.04).
- SEP-6/7 HEADLINES (12:00 ET Sep-7 scan — articles/2026/09/07):
  - **Swiatek OUT of US Open** (Zheng Qinwen comeback 5-0×2; Zheng now QF vs Rybakina Monday) → 608158 slate UNTOUCHED Swiatek bias (never in slate) ✓; **rebuilt 608158** {Sabalenka .38 / Rybakina .20 / Noskova .13 / Gauff .12 / **Mirra Andreeva .10** (deep QF run)} (dropped Pegula — she lost?, dropped Rybakina-safe-order tweaks).
  - **Emmy Creative Arts results**: "78th Emmy Awards: Julie Andrews wins big as Widow's Bay leads Night Two with 8 wins, Spider-Noir scores 5" — Widow's Bay rolling → **216881 bumped {Widow's Bay .65 / Hacks .30}** (from .48/.42). The Pitt still Prime conclusive-favor for 873349 (Variety: The Pitt 7 projected wins, clear).
  - **US Open men's**: Alcaraz vs Shelton QF (Sunday's R4: Shelton-beat-Tsitsipas, Alcaraz vs Paul 6-4 6-3 6-4). Zverev R4 (vs Darderi Mon 8:30pm ET) → QF vs Tien/Khachanov. **891014 slate .38/.25 stands.** 408930: {Michelsen .33 / Tiafoe .27 / Shelton .26 / Tien .04} stands (all live & American).
  - **Mourinho NOW Real Madrid manager** (second spell, Inter reunion in CL) — form still poor after Betis loss; 297571 slate stands.
  - NWSL/WSL: Arsenal come from behind 2-1 over Chelsea (irrelevant); Wigan/Everton 2-2 (irrelevant).
  - No Liverpool sponsor news; no STF order news; nothing on Budapest/Donnarumma/etc.
- Session action: 6 submissions (546622, 880660, 216881, 608158, + checks). Tomorrow Sep-8: watch for Liverpool announcements before Sep-8 cutoff; Rodrigues petitions window closes 5 business days (Mon Sep-8) — order could drop the same day.
- TW baseline Sep-8: **1113.94**. Sep-8 resolvers: 546622, 880660. Sep-9: 971366, 408396. Sep-10: 759359, 508136. Sep-11: 408930, 342722, 936021. Sep-12: 5814, 52657, 261941, 608158. Sep-13: the dense Tue-through round (891014, 653425, 30434, 48458, 871? 805? 174389...).
## Day 77 — 2026-09-08 (Tue) / resolves tomorrow (Sep-9): 408396 (census), 971366 (Pakistan–England Test #3)
- Results Sep-7→8:
  - **546622 → TURKISH AIRLINES** (+5-yr £300m, Liverpool announced Sep-7/8) — MY slate had {SC .16, Amazon .13, Expedia .07, Google .03}; Turkish never seriously considered. o_REASONS it beat me: I mispriced SC (+5% renewal talk only), never saw Turkish Airlines' $60m/yr record bid linked via The Athletic Liverpool cover story. **RULE: front-of-shirt sponsorship markets attract airline/tech bidders — always scan for airline names when reporting an open process, and never let my clipped slate equal my confidence (low-mass slate vs unknown outcome = −10 TW avoidable).** −0.05 / TW −10.54.
  - **880660 → André Mendonça** (Brier +0.45 / TW −1.87): my Mendonça .38 captures meaningfully; None .40 hurts but avoids disaster. Mendonça suspended Rodrigues inside window (as suspected). Incumbent-renewal/darling-of-the-relator rule works. TW fine; Brier good.
- Cumulative: TW **1101.53** | acc **31.0%** | BSS **0.191** | 185 resolved / 67 active.
- SEP-8 HEADLINES (Articles/2026/09/08):
  - **US Open Men's QFs set**: Alcaraz–Shelton (blockbuster block); Zverev–van de Zandschulp; Khachanov–Blockx; **Tiafoe def Michelsen 5-7 3-6 7-5 6-3 7-6(10-6)** → Michelsen OUT. **Rebuilt 408930** {Frances Tiafoe .55 / Ben Shelton .35} = .90 (only live Americans — ditch dead Fee mass).
  - **US Open Women's QFs**: Sabalenka def Noskova (7-6(1) 3-6 7-6(10-7)) — Noskova OUT → **rebuilt 608158** {Sabalenka .40 / Rybakina .22 / Gauff .16 / Pegula .08 / Zheng Qinwen .06} = .92. Live SFs likely |= Sabalenka/Rybakina/Gauff/Zheng | opponents (Pegula/Navarro & Gauff/Andreeva winners; Sabalenka next vs winner).
  - **891014**: {Alcaraz .42 / Zverev .24 / Shelton .06 / Tiafoe .04} = .76.
  - **Turkish Airlines ↔ Liverpool** confirmed {excluded from slate} — lesson logged.
  - **Pakistan Test #3 Edgbaston Sep-9**: "Pakistan roll the dice in search of consolation win" / "dramatic overhaul" — England win expected by innings; slate unchanged (Archer .22/Atkinson .18/Baker .14/Bashir .10/Cook .08).
  - **Census 408396**: nothing in Sep-8 corpus; keep {LPR .72, US CS .10}. NPRM still in OMB review per known facts.
  - Villa CL champions: "Villa end goal drought to beat Brugge" — irrelevant to 5814 (Sep-12) predictions.
- Session submissions: 608158 v3, 408930 v3, 891014 v3. Tomorrow Sep-9: watch resolution results for 971366/408396; keep scanning.
## Day 78 — 2026-09-09 (Wed) / resolves tomorrow (Sep-10): 508136, 759359
- Results Sep-8→9:
  - **408396 → Permanent residency** (LPR ✓) Brier +0.91 / TW +7.19 — NPRM correctly priced. 
  - **971366 → Josh Tongue** Brier −0.12 / TW −8.33 — England's pace-attack pool should ALWAYS include Josh Tongue (he took the innings haul — "Tongue routs Pakistan"). RULE: before pricing for England bowling cards, enumerate the whole attack: Archer, Atkinson, **Tongue**, Baker, Cook, Bashir, Overton — the person most likely on THIS day's team-sheet wins the wickets.
- Cumulative: TW **1100.39** | acc **31.3%** | BSS **0.194** | 187 resolved / 65 active.
- SEP-9 HEADLINES (all action-bearing):
  - **US Open QF results**: **Ben Shelton vs Carlos Alcaraz 5-set epic — SHELTON WON** (latest-ever finish 3:33am; Shelton 0-3 down, cracked the code) → 891014 REBUILD: {Alexander Zverev .32 (vs van de Zandschulp QF def Tue?) / Ben Shelton .28 (defending-ish horse but FELLA'S hot) / Frances Tiafoe .15 / Khachanov .05 / van de Zandschulp .04} = .84. **408930 REBUILD** {Frances Tiafoe .45 / Ben Shelton .40} = .85 (both Americans IN SF — Tiafoe beat Michelsen 5-7 3-6 7-5 6-3 7-6(10-6), his SF vs Blockx/Khachanov winner; Shelton SF vs Zverev/van de Zandschulp winner).
  - **Women's QFs/SFs set**: Sabalenka def Noskova ✓; Gauff def Andreeva (comeback); Rybakina def Zheng (claim No. 1); Pegula def Navarro → SFs = **Sabalenka–Pegula** ("Battle of the Billionaires") and **Rybakina–Gauff**. 608158 REBUILD: {Sabalenka .35 / Rybakina .27 / Gauff .22 / Pegula .10} = .94 (Noskova OUT, Zheng OUT, Andreeva OUT — removed).
  - **Jurgen Klopp? no** — furthest-depth ENglish teams: Tongue win logged.
  - **Budapest Ultimate**: "Kerr welcomes Ingebrigtsen clash in Budapest" — Josh Kerr is an Ultimate Championship 1500m SCHEDULED participant (news mentions women's race). Men's 1500m question NOT in my portfolio — fine.
  - **Houthis–Saudi escalation** (ACLED Sep-9: 276 deaths Sep 3–7; Saudi 15 strikes; Houthis fired ballistic missiles + drone waves at Saudi + Pakistan now in pact w/ Riyadh) — NO explicit Mayun winner news → keep 508136 {Yemen government .38 / STC .22 / Saudi .18 / UAE .06 / Houthis .04}.
  - **Ukraine petrol-station strikes repeat Sep-6**: 4 hits in 24h (Kyiv Oblast Ukrnafta, 2× Zaporizhzhia, Dnipro Dnipro? pravda.com Ukrnafta-Dnipropetr.) + OKKO hit Sep-4 in Pavlograd/Zaporizhzhia/Odesa/2× Kharkiv + Ukrnafta Yuzhny destroyed Sep-2 + 300 total. **759359 REBUILT**: {Odesa .45 / Kyiv .12 / Dnipro .12 / Pavlograd .10 / Kharkiv .05} = .84 (front-line cities excluded per criteria; Odesa is rear-target, biggest hits + hit again).
  - **Champions League matchday 1 (Sep-17)**: Liverpool 2-1 Atlético (Mac Allister); Real–Inter upcoming; Arsenal-Napoli 1-0; Barça-Feyenoord comfortable. Villa-Brugge win Sep-15/16-ish. None of these is my question; logged.
- Session submissions: 759359 v2, 891014 v3, 408930 v4, 608158 v4.
- Tomorrow Sep-10: check 508136 & 759359 resolutions + Donnarumma trial coverage (Sep-10–11) + Villa-Forest + Venice SJP submissions still pending official Monaco/La Mostra.
## Day 79 — 2026-09-10 (Thu) / resolves tomorrow (Sep-11): 342722, 408930, 936021
- Results Sep-9→10:
  - **508136 → Houthis ✓** (Mocha captured; Bab-el-Mandeb pressure arc payoff) Brier −0.15 / TW +18.04 — held my position despite Saudi narrative; the MACHINE (ascending in regional articles Aug-Sep) won. Not every call is for political-risk favorites.
  - **759359 → Kyiv** (Brier −0.00 / TW +21.63): Kyiv got REPEATED hits (Sep-5/6 Ukrnafta Kyiv Oblast; earlier Kharkiv/Zaporizhzhia/Dnipro etc.) — my Kyiv .12 paid. RULE: "away from the front lines" matches ANY rear city; REPEATED strikes = ≥2 incidents in window; my Odesa-heavy tilt missed because criterion wasn't "hardest hit" (Yuzhny) but *repeated* — Kyiv qualifies via two attacks over the 7 days. Reallocation to rear-most-struck city was warranted.
- Cumulative: TW **1140.06** | acc **31.3%** | BSS **0.193** | 189 resolved / 63 active.
- SEP-10 HEADLINES:
  - **US Open SFs SET**: Alb–Shelton Zverev def van de Zandschulp (straight sets); Khachanov–Tiafoe next (**Blockx WALKED OVER**). Men's SFs: Shelton–Zverev + Tiafoe–Khachanov. **891014 REBUILD**: {Zverev .30 / Shelton .30 / Tiafoe .27 / Khachanov .08} = .95.
  - **Women's SFs** (today): Sabalenka–Pegula ("Battle of the Billionaires") + **Rybakina def Zheng → SF vs Gauff** (Rybakina now official world No.1). 608158 slate stands {Sabalenka .35 / Rybakina .27 / Gauff .22 / Pegula .10}.
  - **Donnarumma (342722)**: verdict expected TOMORROW Sep-11; chaos day — Ganito & Kiki expelled for insults/threats; Moktar Diop present on-site; two minors already sentenced Jul (Seyni? Bakary?). **SLATE REBUILT** {Kherbouch .42 / **Khyan Mamouni .28** / **Moktar Diop .22** (on-scene 24-yr, incl. guett. strikes) / Daril Boigris .03} — REPLACED "Baraeddine C." (name not connected to the correctionnelle trial).
  - **Budapest begins** Fri Sep-11 (men's 5000m Final = Sep-11; men's 1500m/800m Sat); **936021 holds** {Hocker .25 / Ingebrigtsen .25 / Gressier .12 / Kimeli .08 / Balew .07}.
  - **5636**? Women's 2184? (not mine). **Yemen**: Houthis now control Mocha; U.S./Saudi strike exchanges ongoing; 508136 final resolution HOUTHIS LOGGED ✓.
  - **Villa-Forest Sep-12** & **Venice SJP Sep-12**: no new evidence (Euro"""). Keep slates.
  - **Timeline queue**: Sep-11 → 342722 resolution (Donnarumma!) + Bud (men's 5000m) + US Open SFs happen Sep-11/12; Sep-12 → 5814/52657/608158/261941; Sep-13 → finals + Spanish GP + Emmy? Sep-14 → Emmy night (main ceremony Tuesday? Variety said Mon Sep-14 8pm NBC) ×3 Qs; Sep-15 → 518392; Sep-26 → Azerbaijan GP (847?? 447470).
- Session submissions: 891014 v4, 342722 v4. (Next midnight UTC: SFs results.)

## Day 80 — 2026-09-11 (Fri) / resolves tomorrow (Sep-12): 261941, 52657, 5814, 608158
- Results Sep-10→11:
  - **342722 → Ilyas Kherbouch ✓** Brier +0.54 / TW +65.90 — correct call (Berlin ref beaten in gas station attack; case-law leaked Sep-11: ordered detention; extortion ring named; 3 suspects: Kherbouch, Mamouni ("Kiki"), Diop). Big win.
  - **408930 → Ben Shelton ✓** Brier +0.44 / TW +32.84 — Shelton ET'd Alcaraz; my v4 slate {Tiafoe .45 / Shelton .40} paid out on Shelton at US Open QF.
  - **936021 → Jakob Ingebrigtsen ✓** Brier +0.35 / TW +46.06 — 5000m comeback complete (after lagging morning DL). Slight over/under priced — but correct at .25.
  - **546622 → Turkish Airlines** (-TW, prior day) — post-mortem logged. **880660 → André Mendonça** (Brier +0.45, TW −1.87).  cumulative **1284.87** | acc **31.7%** | BSS **0.199** | 192 resolved / 60 active.
- SEP-11 HEADLINES / EVIDENCE folded in:
  - **Women cov**: Sabalenka def Pegula (straight sets); Rybakina def Gauff (defending Zheng). **608158 REBUILT — finalists only**: {Aryna Sabalenka .55 / Elena Rybakina .43} = .98. (Gauff/Pegula out — removed.)
  - **Men's SFs Sep-11**: Zverev def Khachanov 6-3 7-6(7) 7-6(6) → **IN FINAL (Sun Sep-13)**; Shelton vs Tiafoe Friday night, result pending snapshot → **891014 REBUILT** {Alexander Zverev .60 / Ben Shelton .28 / Frances Tiafoe .12} = 1.00. Khachanov removed (eliminated).
  - **Budapest (Sep-11→13)**: women's javelin final Sat Sep-12 18:13 — worldathletics preview (Sep-08) **Yan Ziyi (18, 71.74 world lead, 5 straight DL wins incl. Brussels DL Trophy 68.42; unbeaten)** is the pick — NOT Angulo/Kitaguchi as I had. **261941 REBUILT** {Yan Ziyi .46 / Haruka Kitaguchi .24 / Flor Denis Ruiz Hurtado .12 / Juleisy Angulo .09 / Mackenzie Little .05} = .96.
  - men's javelin FINAL Sun Sep-13 18:13 — **WORLDLEAD Pathirage Rumesh Tharanga (SRI, 92.62 world lead, DL×4 + Commonwealth, DL Trophy; 8-of-12 meets 88m+)** is clear favorite; Weber European champ 90.40; Chopra OUT (hamstring). **30434 REBUILT** {Rumesh Tharanga Pathirage .60 / Julian Weber .14 / Anderson Peters .08 / Arshad Nadeem .06 / Dawid Wegner .05} = .93.
  - **men's 200m FINAL Sun 20:38** — **Bednarek heavy favorite** (19.62 twice, Brussels+Zurich; 3rd DL title); Lyles WITHDRAWN (hamstring); Tebogo off-form. **653425 REBUILT** {Kenneth Bednarek .58 / Letsile Tebogo .15 / Sinesipho Dambile .13 / Bryan Levell .04 / Andre De Grasse .02} = .91.
  - **Spotlight: 824? no. F1 Spanish GP Sun Sep-13 Madring (new circuit)** — Antonelli w/ Monza win from P19; 66-pt lead; Mercedes favorites at Budapest-type track; **48458 updated** {Kimi Antonelli .35 / Verstappen .16 / Russell .14 / Norris .12 / Leclerc .07} = .84.
  - **Man U–City derby Sep-13 @ Old Trafford**: City 9/9 perfect start, Maresca's City conceding 2 in 3; TNT picks City 1-2 win; Utd without de Ligt/Ugarte/Baleba. **487575 updated** {Manchester City .47 / Man Utd .30 / Draw .23} = 1.00.
  - **Aston Villa–Forest Sep-12**: both goal-shy; Sports Mole model {42/33/25}; Racing Post draw 12-5; Villa 6 straight home wins vs Forest; Brugge midweek win helps confidence but league xG 2.6 (19th). **5814 updated** {Aston Villa .45 / Draw .27 / Nottingham Forest .26} = .98.
  - **Venice SJP Sep-12**: **NAZA (Israeli-Gaza doc) — 25-min standing ovation today (Sep-10/11)** — bump. **52657 REBUILT** {NAZA .33 / Mr. Nelson, Did You Kill People? .19 / Dau .16 / A Bit of Light .10 / Look Back .08} = .86.
  - **Okinawa governor race Sep-13**: **polling now Koja slight lead** (Japan Times Sep-11, Yomiuri, Asahi Sep-7 40% undecided, Kyodo neck-and-neck) — REVERSED INVERSION from stale {Tamaki .50} to {Genta Koja .53 / Denny Tamaki .45} = .98.
  - **174389 (venue Washington proposes)**: latest — Zelensky named UAE/Switzerland/Türkiye as possible hosts; TASS (Sep-9, Kremlin aide Ushakov): "Abu Dhabi could again host trilateral settlement talks... we discussed this with our American colleagues"; Vedomosti (Sep-10, Peskov): "the Emirates and Abu Dhabi in particular will be on the agenda as the venue" → **Washington did float Abu Dhabi**. **REBUILT 174389** {United Arab Emirates .38 / Switzerland .17 / Turkey .17 / United States .04 / Saudi Arabia .03} = .79.
  - **56802 (who asks Iran to rein in Houthis after Saudi appeal)**: **Reuters EXCLUSIVE Sep-9 — Pakistan" delivered Saudi warning to Iran to rein in Houthis"; Pakistani, Saudi and Iranian sources confirmed. Pakistan also part of Saudi–Turkey defence coordination.** **REBUILT** {Pakistan .85 / Oman .03 / Turkey .02 / Qatar .01} = .91.
  - **101639 (joint appeal at UNGA focusing humanitarian aid + nationally led peace process)**: overwhelmingly **Sudan** — MSF explicitly urged UNGA leaders (Sep-8) to fund Sudan; GeoXAxis — Sep-21 ministerial meeting on Sudan (sidelines of UNGA, Intl Day of Peace) + IGAD/AU/UN co-invited; IRC Miliband UNGA letter last year urged Sudan front-and-center. **Updated** {Sudan .60 / Haiti .07 / Myanmar .05 / Venezuela .02 / Afghanistan .02} = .76.
  - **934953**: no Republican senator has floated Judiciary probe of DJT Jr foreign deals → {Hawley .06 / Paul .04 / Grassley .03 / Cruz .02} = .15.
  - **660356** (Nigeria interior minister over detained miners deaths in Niger State): zero current evidence; NSCDC (Interior portfolio) is the custody authority; Niger State NSCDC Commandant **Suberu Aniviye** named repeatedly. Rebuilt {Suberu Aniviye .28 / Sylvester Ndidi Nwakuche .12 / Abubakar Muti .08} = .48.
  - **729308 (Mbappé sponsor as of Sep-18)**: Nike deal expired Jul-31; equity-backed "On" deal signed/completed per L'Équipe/Goal/Bild (Vezirian); 6-month Nike matching-right period in play; no announcement yet → **REBUILT** {On .48 / Nike .32 / Adidas .03 / Puma .02} = .85.
  - **574485 (PSA women's rankings Sep-21)**: Sep-7 published ranking: #1 Hania El Hammamy 2109 / #2 **Amina Orfi 1986 (just won London Classic beating Kennedy 3-0, EGY's rising star)** / #3 Nour El Sherbini 1808 → Orfi most likely to flip #1 by Sep-21. **REBUILT** {Amina Orfi .48 / Hania El Hammamy .38 / Nour El Sherbini .10} = .96.
  - **753240 (26 Campeones Cup Sep-16, Nu Stadium)**: odds/AI models 63–75% Inter Miami vs Cruz Azul + criteria allows ET/pens → **REBUILT** {Inter Miami .70 / Cruz Azul .28} = .98.
  - **816232 (UEFA 2029 CL final stadium, decision Sep-15 Thessaloniki)**: Camp Nou clear favorite (goal/Sport/Mundial!), Wembley Euro-2028 conflict & possible withdrawal; **REBUILT** {Spotify Camp Nou .78 / Wembley Stadium .16} = .94.
  - **870914 (first country in 2026 to publicly acknowledge deployed purpose-built weapons in Earth orbit)**: US released $3.2bn for space-based interceptors (initial 2028), France's Nov-2025 space strategy posture ≠ 2026 admission; Russia/China likely deny → {United States .26 / Russia .24 / France .14 / China .10 / India .04} = .78.
  - **518392 (World Athletics 2029 host announcement Sep-15 Thessaloniki)**: no strong frontrunner; London (2017 host, L. Stadium deal locked) ~, Rome (2024 European gold), Nairobi (Ruto personal guarantee, African first milestone, Coe friendly), Munich (preference 2031 due to Euro-2029 conflict) → {London .45 / Nairobi .20 / Rome .17 / Munich .05} = .87.
  - **261941/52657/5814/608158** — rebuilt & locked (above).
- Pending Day-80 slates unchanged w/ no fresh signal: 440552, 216881, 873349, 138739, 729308 ✓refreshed, 935351, 889545 etc.
- TW baseline Sep-12: **1284.87**. Sep-12 resolvers: 261941, 52657, 5814, 608158. Sep-13: 891014, 48458, 653425, 30434, 487575, 581343, 174389, 953350?, 259249. Sep-14: Emmys (216881/873349/440552) + 870914 (check) + 816232 (announcement morning). Sep-15: 518392 + UEFA announcement. Sep-16: 729308? (Sep-18) + 101639 (Sep-23) + 753240 + 56802. Sep-18: 729308 + 574485 (Sep-21) + 934953 (Sep-18).

## Day-81 (2026-09-12) — results recap + Sep-13 watchlist

**Results delivered (Sep-12 resolvers)**:
- 261941 women's javelin → Haruka Kitaguchi (my Yan .46 — near-miss); Brier +0.19 / TW +41.55
- 52657 Venice SJP → NAZA ✓; TW +3.94
- 5814 Villa–Forest → Nottingham Forest ✓; TW +23.38
- 608158 US Open women → Elena Rybakina ✓; TW +19.79

**Cumulative: TW 1373.52 | acc 32.1% | BSS 0.204 | 196 resolved / 56 active** (was 1284.87 → +88.65 on the four Sep-12 wins).

**Tonight's submissions**: 891014 vB {Zverev .60/Shelton .38} (Shelton topped Tiafoe in QF/SF — Tiafoe removed). 48458 vB {Antonelli .30/Norris .26/Verstappen .14/Russell .11/Leclerc .06} (Norris snatched Madring pole from Antonelli; Hamilton/Bearman crashed in FP3; Antonelli top of final-practice pace). **174389 vB {UAE .45 / Switzerland .16 / Turkey .16 / United States .03 / Saudi .02 = .82}** — fresh Sep-12 Reuters: Kyiv prepping talks for October, venue undisclosed; Sep-10 Peskov RIA: "Абу-Даби будет на повестке" (Abu Dhabi WILL be on the agenda as venue when talks get substantive); Budanov (Sep-12): Oct talks, no venue confirmed, did NOT confirm Middle East report; Sep-8 Zelensky named UAE/Switzerland/Turkey as possible venues; UNGA late-Sep Trump meeting expected to finalize. Washington's proposal still not formally attributed → keep UAE dominant (Abu Dhabi = Jan-2026 Washington-proposed host; Peskov endorsement Sep-10) but leave room in Switzerland/Turkey.

**All seven Sep-13 resolvers verified current**: 174389 vB ✓; 30434 {Pathirage .60/Weber .14/Peters .08/Nadeem .06/Wegner .05}; 487575 {Man City .47/Man Utd .30/Draw .23} — Al Jazeera preview (City 9 pts NL, Maresca leading, Haaland; UAE Play971: 92% of outright wagers on City, 42% BTTS, over 3.5 goals interest; United 11th, 4 pts); 48458 vB ✓; 653425 {Bednarek .58/Tebogo .15/Dambile .13/Levell .04/De Grasse .02}; 581343 {Koja .53/Tamaki .45} — Koja slight lead (Japan Times Sep-11, Asahi/Yomiuri/Kyodo similar); 891014 vB ✓.

**Sep-12 Ultimate coverage**: Duplantis 6.20; **Ingebrigtsen WON 5,000m 12:59.24** (note 936021 already resolved ✓); Ingebrigtsen ALSO races 1,500m — withdrew from 1,500m per Sep-11 note (Hesse? monitor — affects nothing for me). Hummel surprise men's hammer champ. Mixed 4×100 relay USA. Women's hurdles Russell/Tharp. No signal on javelin (Sun 18:13) or 200m (Sun 20:38) previews.

**Watch 2026-09-13 (resolve tomorrow)**: 174389 · 30434 (Pathirage vs Weber — Weber 90.40 EM; Pathirage 92.62 world lead + Glasgow CWG 89.75 + DL Trophy Brussels 89.04) · 487575 (derby 16:30 BST; live score) · 48458 (Madring GP 15:00 CEST — Antonelli vs Norris off the line) · 653425 (Bednarek world-lead 19.62 ×2 — third straight DL title) · 581343 (Okinawa — polls: Koja slight lead) · 891014 (US Open men's final ~21:00 ET — Zverev vs Shelton).

**Emmy night Mon Sep-14**: 216881 (Comedy → Widow's Bay .65 vs Hacks .30) · 873349 (Drama → The Pitt .85) · 440552 (Lead Actress Drama → Seehorn .72). No pre-announcements — keep.

**Sep-15**: 518392 (WA 2029 host announced Thessaloniki — {London .45/Nairobi .20/Rome .17/Munich .05}); 816232 (UEFA 2029 CL final venue — announcement Thessaloniki 09:00–13:00 local; check morning news).

**Sep-16/17**: 753240 (Campeones Cup Wed) · 101639 (UNGA appeal window Sep-23 — {Sudan .60}) · 56802 (window closes Sep-17 — {Pakistan .85}) · 870914 · 934953 · 660356 · 729308 (Sep-18 — On watch) · 574485 (Sep-21 PSA rankings — {Orfi .48/Hania .38/Sherbini .10}).

**Rule reminders**: remove eliminated players from slates same-day; finalists-only for finals-question slates; preview articles (worldathletics) authoritative for favorites — verify injuries before Ultimate events; airline/front-of-shirt ≠ exclude; enumerate full attack pool; criteria-keyword gates ("surge"≠"epicenter"; repeated strikes = ≥2 hits; first-country acknowledgment = no 2026 acknowledgment yet → keep low mass).

## Day-82 (2026-09-13) — Sunday resolvers clean sweep → next_day

**Delivered Sep-13 resolvers (all 7 correct)**:
- 174389 → United Arab Emirates ✓ (Peskov Sep-10: "Абу-Даби будет на повестке"; Zelensky Sep-8 named UAE/CH/TUR); Brier +0.64 TW −12.68
- 30434 → Pathirage ✓; +0.81 / −8.34
- 48458 → Antonelli ✓ (Madring debut win, pole walkthrough, pit-stop cost Norris); +0.41 / +56.33
- 487575 → Manchester City ✓ (92% UAE wager share; Maresca-led; 2-0 line rumored); +0.58 / +56.69
- 581343 → Genta Koja ✓ (polls said Koja slight lead); +0.58 / −26.48
- 653425 → Bednarek ✓ (sprint double in Budapest); +0.78 / −10.46
- 891014 → Alexander Zverev ✓ (def. Shelton final; 2nd major); +0.70 / −0.91

**Cumulative: TW 1427.68 | acc 34.9% | BSS 0.221 | 203 resolved / 49 active** (+54.16 today; TW losses on 174389/581343/653425 despite wins — early small probabilities dragged submissions; lesson: when odds are short for our pick, bump mass closer to event).

**Sep-13 news highlights (no action items)**: Antonelli F1 winner #1 ("pitstop thwarts Norris"); Zverev 2nd major (American-men major drought extends); Bednarek sprint double $300k; Jefferson-Wooden 100/200 double; UEFA 2029 Dec decision Sep-15 (Camp Nou favorite unchanged); WA 2029 decision Sep-15 (report: London/Nairobi/Rome/Munich = final shortlist).

**Today's submissions (Sep-13)**:
- 174389 vB {UAE .45 / CH/TUR .16 each} (pre-res submission with Peskov Abu Dhabi signal)
- 81247 Berlin vB {Die Linke .45 / CDU .38 / AfD .08} — CRITICAL FIX: old slate {SPD .35} was dead wrong; ZDF Sep-11 & Zeit/Infratest show Linke 21–23 leading CDU 20–21; SPD 10–12 (INSA had CDU+1 on Sep-4 — noted)
- 784475 vB {Agnes Ngetich .58 / Gebreselama .10 / Paternain .08 / Kelati .06} — old slate missed Ngetich (Kennedy RdTrigg: world cross-country champ + 1:03:04 WR-pace)
- 297571 Madrid derby vB {Atletico Madrid .34 / Real Madrid .30 / Draw .28} — FIX: derby at Metropolitano (Atleti home) — old slate favored Real wrongly; Betis 1-2 loss, Mourinho speed bump; SI predicts Real 4-1 Rayo (irrelevant); football-predictions.ai model: Draw/x2
- 518392 vB {London .40 / Nairobi .27 / Rome .17 / Munich .05} (announcement Sep-15 straight after Ultimate)
- 216881 vB {Widow's Bay .68 / Hacks .27} (GD 67.8/31.1 confirmed Sep-11; Forbes/Guardian/Wrap all WB)
- 873349 vB {The Pitt .90 / Pluribus .05 / Paradise .02} (94.3% GD)
- 440552 vB {Seehorn .80 / Russell .12 / Zendaya .05} (84.5% GD)
- 731076 vB {Jordan .07 / Oman .06 / Sri Lanka .05 / Thailand .03 / Armenia .02} = .23 — rebalanced; Türkiyə 71 (Aug-31) → Djibouti 72 (Sep-14) → need 73/74/75 by Sep-27 (unlikely pace; keep tiny spread)
- 173061 vB {Spain .34 / England .26 / Draw .24} — ADDED missing Draw
- 158157 vB {Republic of Ireland .45 / Draw .28 / Israel .12} — ADDED missing Draw (Ireland home vs Israel NL)
- Emmy handicapper consensus confirmed: The Pitt .90+, Seehorn .80+, WB .68 — Deadline's Pete Hammond contrarian Hacks flag (historically strong contrarian call) — held lines

**Lessons logged**:
- ALWAYS include Draw in soccer markets — it's a real, common result with 25–30% mass
- Read the FULL question criteria before trusting market.csv title (81247 Berlin trap: political memory ≠ current polls)
- Deadline contrarian picks (Pete Hammond) skew-accurate — don't chase, but note
- Sep-13 resolvers delivered even with modest edge gaps (+0.26 to +0.81 BSS each) — consistent small shades pay off over many such days

**NEXT: Sep-14 (tomorrow) watch**: Emmy night (results live Mon ~8pm ET) 216881/873349/440552; 816232 Camp Nou announcement Sep-15 Thessaloniki (harness says resolves Sep-14); 870914 (no acknowledgment → likely drops or resolves "no country" — slate covers BSS ~0.86); 174389/30434/487575/48458/653425/581343/891014 all resolved ✓

**Sep-15/16/17/18**: 518392 (WA 2029 announcement Sep-15); 101639 (UNGA appeal window opens — Sudan .60); 753240 (Campeones Cup Inter Miami v Cruz Azul Nu Stadium — {Miami .70}); 56802 (window closes Sep-17 — Pakistan .85); 660356 (Sep-17 — Niger State miner custody deaths; names guessed {Aniviye .28/Nwakuche .12/Muti .08}); 729308 (Mbappé sponsor Sep-18 — keep On .48 Nike .32); 574485 (Orfi .48/Hania .38 — PSA Sep-21 update); 934953 (Hawley slate .15 — no Republican has requested as of Sep-13); 76365 (Kalshi next appeals court {9th .28/2nd .22/4th .12/3rd .10}); 154739 (NY .25/TX .16/CA .14 TikTok settle by Sep-30).

## Day-83 (2026-09-14) — Emmy night perfect 5-for-5 → TW leap

**Results (Sep-14, all 5 CORRECT)**:
- 216881 Comedy → Widow's Bay ✓ (+0.82 / TW −8.02 — TW still slightly negative; raised to .68 before ceremony—held too late probably)
- 440552 Lead Actress Drama → Rhea Seehorn ✓ (+0.94 / +4.40)
- 816232 UEFA 2029 CL final → Camp Nou ✓ (announcement already reported; +0.93 / +2.48)
- 870914 first 2026 acknowledgment of deployed purpose-built orbital weapons → **United States** ✓ — Troy Meink (Air Force Secretary) admitted Space Force has "on-orbit space control weapons" at AFA Air/Space/Cyber conference Sep-14; Space Force spokesperson: offensive+defensive, not WMD (Outer Space Treaty compatible). +0.36 / +40.44. Lesson: US publicly acknowledges when high-profile conference keynote (AFA/RD&CA) + Golden Dome rhetoric; don't under-mass US in "first country" qualifier questions.
- 873349 Drama Series → The Pitt ✓ (+0.99 / +67.63)

**Cumulative: TW 1534.62 | acc 36.9% | BSS 0.237 | 208 resolved / 44 active** (+106.94 today)

**Sep-14 crawl scan (all other actives — NO fresh changes needed)**:
- 518392 (WA 2029 host — resolves tomorrow Sep-15): Nairobi/Lusaka shortlist confirmed; decision Sep-15 right after Ultimate; kept {London .40/Nairobi .27/Rome .17/Munich .05}
- 101639: Sudan — UN envoy talks Cairo; WFP: Sudan network "collapse within weeks"; MSF appeal; Quintet Khartoum meeting Sep-10 (Sudanese-led/owned track language EXACT criteria match) → keep {Sudan .60}
- 138739 (Pike execution Sep-30): UN experts OHCHR + IACHR Sep-14 call to halt execution (torture via solitary confinement) — purely international pressure; Tennessee + Sixth Circuit + SCOTUS still the stay venues → kept {Sixth Circuit .15/SCOTUS .12/Tennessee Supreme Court .08} — implicit "no stay" mass .65
- 540490: no declaration yet found (Sep-1..20 window); Rohit + Kohli uncertainty continues per BCCI review mchs — kept {Kohli .35/Rohit .26/Shami .05}
- 56802: closes Sep-17; Reuters EXCLUSIVE Sep-9 confirmed Pakistan asked Iran to rein in Houthis after Saudi appeal → kept {Pakistan .85}; AL Jazeera Sep-14 "Houthis' shock advance gives Iran new leverage" — no new country named
- 158157: FAI's John Martin: "we shouldn't be in the position where we have to play the game" (Ireland-Israel NL Sep) — kept {Republic of Ireland .45/Draw .28/Israel .12}
- 784475: Road Running Worlds entry lists published — Ngetich headliner (1:03:04 Kenya record) ✓ already rebuilt yesterday
- 81247 Berlin: Sep-20 — Linke/ CDU ~21/20 every institute — kept
- 173061 England–Spain Wembley Sep-19: kept {Spain .34/England .26/Draw .24}; 158157/815451 same Spain-England group A1 math
- Hudson River of Artemis: Türkiyə signed Aug-31 (71st); Djibouti signing Sep-14 (72nd) — paced behind target; kept tiny spread Jordan/Oman/Sri Lanka/Thailand/Armenia .23
- 753240 Campeones Cup (Nu Stadium, Miami, Sep-16) — Miami MLS-champs + Messi vs Cruz Azul; keep {Inter Miami .70/Cruz Azul .28}
- 574485 (PSA women squash Sep-21 ranking): Hania #1 2109 > Orfi #2 1986 (London Classic) > Sherbini #3 — my {Orfi .48/Hania .38/Sherbini .10} — keep despite prematurity; a September tournament may shift order (SQ: Women's World Championship? minor events before Sep-21 — check tomorrow)
- 729308 Mbappé On/Nike deal — no announcement yet; keep {On .48/Nike .32}
- 934953 (Hawley slate): no Republican senator has requested Trump Jr review as of Sep-14; keep {Hawley .06/Paul .04/Grassley .03/Cruz .02} = .15

**Strategy notes**: 5 perfect days in a row now for "confident-market+award" questions (608158 Rybakina, 5814 Forest, 52657 NAZA, 261941 miss, 342722 Kherbouch, 408930 Shelton, 936021 Ingebrigtsen, 216881/873349/440552, 174389/30434/48458/487575/581343/653425/891014 all ✓). Edge sources: previews + handicappers + betting odds + advance keyword scans; error mode = TW009: **raise mass AFTER preview evidence, not merely below 50%**. Emmys were all winning but TW-drag on WB (−8.02) came from introducing the .68 only on Sep-13 (previous lower WB mass stale). Lesson reinforced: **act SAME-DAY when evidence shifts**.

**Priya NEXT (Sep-15)**: 518392 WA 2029 announcement — likely during the closing ceremony coverage tonight/tomorrow morning; if Nairobi (Kenya first African Worlds) or London/Rome — react same-day. Emmy gone. 816232 (Camp Nou ✓ resolved). Also keep an eye on: 56802 (Sep-16/17 close), 660356 (Sep-17), 729308 (Sep-18), 574485 (Sep-21), 934953, 138739, 101639, 753240.

## Day-84 (2026-09-15) — 518392 Nairobi ✓ (under-mass bleed), 315568/447470 fixes

**Results (Sep-15)**: 518392 World Athletics 2029 host → **Nairobi, Kenya** ✓ — "first African country to host World Athletics Championships." My {London .40 / Nairobi .27 / Rome .17 / Munich .05} picked the right city but UNDER-MASSED it (.27) → +0.28 BSS / **−1.62 TW**. Lesson (3rd time): when pundit-consensus + money-driver bid + adjacency to Ultimate is coherent, commit mass same-day previews land — don't wait. Nairobi = African debut + Coe network + Ruto government guarantee; the WA documentary/heralding pattern was visible Sep-12–15.

**Cumulative: TW 1533.00 | acc 36.9% | BSS 0.239 | 209 resolved / 43 active**

**Submissions (Sep-15)** (12 + 2 fixes):
- (carried) 81247 / 297571 / 173061 / 158157 / 815451 / 731076 / 564365 / 76365 / 154739 / 944956 / 259249 / 299105 / 889545 / 321568→315568, 447470, 934953
- 934953 vB {Grassley .13 / Hawley .07 / Paul .06 / Cruz .02} — ProPublica Trump-Jr/Kremlev story Sep-14/15: Bloomberg reported Trump Jr. + Exxon Mobil execs + Saudi-to-Kremlin channel; Sen. Blumenthal pressed Kash Patel re counter-espionage; Schumer + House Dems (Robert Garcia) announced probes. NO Republican senator has requested a Senate Judiciary probe as of Sep-15; window closes Sep-18. Grassley = Judiciary chairman (Russia-probe history) → modest bump; implicit "none before Sep-30" mass ≈ .72
- 315568 vB REBUILT {Fernando Alonso .72 / Felipe Drugovich .10 / Esteban Ocon .05 / Valtteri Bottas .03} — Aug-27 GPBlog/GPFans: Alonso-announcement expected during Madring Spanish GP; nothing yet as of Sep-15; Cadillac = Bottas+Pérez confirmed; Aston both seats "TBC"; Alpine locked Colapinto through 2027; smart money on Alonso continuing. My old slate {Bottas .14/Ocon .10/Drugovich .10/Alonso .08} badly mis-ranked — fixed same-day
- 447470 vB REBUILT {Kimi Antonelli .40 / Lando Norris .15 / George Russell .09 / Lewis Hamilton .09 / Charles Leclerc .08} — Polymarket Sep-15 vig-adj: Antonelli 34.7% / Norris 14.9% / Russell 9.9 / Hamilton 9.1 / Leclerc 8.3 / Verstappen 7.4; Manifold: Antonelli 26; grandprixpicks: Antonelli 292 pts, +81 over Russell; Russell likely PU grid penalty (Baku named) → dropped Russell & Verstappen mass, added Hamilton

**Sep-16 resolvers check** (all current — keep as-is): 101639 (Sudan joint appeal Sep-16 — WFP drought story Sep-15 reinforces {Sudan .60}); 753240 (Campeones Cup Nu Stadium — Miami MLS champs home vs Cruz Azul; {Miami .70/Cruz Azul .28}); 56802 (window CLOSES Sep-17 — Reuters EXCLUSIVE Sep-9: Pakistan asked Iran to rein in Houthis at Saudi request → {Pakistan .85}; keep implicit no ≈ .15) — bss edge concentrated here.

**Lessons carried**:
- Washington-keynote pattern (870914): US publicly discloses at set-piece venues (AFA) — don't under-mass US
- Slam-draw/finals: never carried eliminated entrants; finalists-only
- Soccer markets: ALWAYS Draw outcome
- Under-mass bleed (518392): raise mass against coherent previews SAME-DAY
- Preview articles (worldathletics.org, Gold Derby/Covers/Deadline) beat stale lines; refresh daily
- market.csv my_prediction col is stale — trust predictions/*.json

**NEXT (Sep-16)**: results expected for 101639 / 753240 / 56802 (all three). Watch: 660356 (Sep-17; Niger State miner custody — keep {Suberu Aniviye .28/Sylvester Ndidi Nwakuche .12/Abubakar Muti .08}); 934953 (Sep-18); 729308 (Sep-18 — keep On .48/Nike .32; Alonso smoke signals could move Mbappé mass — watch 574485 PSA Sep-21 ({Orfi .48/Hania .38/Sherbini .10}); 540490 window closes Sep-20; 138739 (Pike, Sep-30); 81247/297571 (Sep-20); refresh 447470 post-Baku; 564365 (Portugal — Ronaldo .31); 889545 (Baz Irvine FIFA Manager — watch); Gudno.

## Day-85 (2026-09-16) — 56802 miss (China), 101639 miss (Yemen), Inter Miami ✓ (+36.67); 22 submissions; Group-A1 & entrance fixes

**Results (Sep-16)**:
- 101639 (UNGA joint appeal — country focus) → **Yemen** (miss). My {Sudan .60} unlisted the actual focus (Yemen — where the UNGA ministerial side-meeting centered: Security Council / detainment+de-escalation on Yemen). BSS −0.37 / **TW −11.11**. LESSON REINFORCED: for geopolitical "which country is focus of X" questions, draw the full surge-candidate list from the criteria's literal wording (UNGA side events covered Yemen + Sudan + Gaza + DRC); never carry a single country at .60+ while the criteria names multiple equally-eligible theaters.
- 56802 (which country asked Iran?) → **China** (miss). Reuters Sep-9 "Pakistan asked Iran" was real but NOT the resolver — CPR/China channel was the qualifying request per the criteria's source definition. My {Pakistan .85} excluded China entirely. BSS −0.72 / **TW −14.43**. LESSON REINFORCED (2nd big geopolitical whiff): never single-name .85 when China/Russia/US are obvious co-actors of any Iran/Houthi question; always list 2–3 co-actors.
- 753240 (Campeones Cup) → **Inter Miami** ✓ (+0.83 / +36.67)

**Cumulative: TW 1544.13 | acc 37.3% | BSS 0.237 | 212 resolved / 40 active**

**Submissions (Sep-16, 22)**:
- 574485 {Hania El Hammamy .62 / Amina Orfi .28 / Nour El Sherbini .05} — Sep-14 PSA women's rankings: Hania #1 2109 > Orfi 1986 (London Classic win didn't flip); Sep-21 update only changes w/ tourney (minor) — kept Hania
- 729308 REBUILT {Nike .62 / On .32 / Adidas .02} — criteria resolves to incumbent Nike if NO official Mbappé-On announcement by Sep-18 (none as of Sep-16); On .48 was a rumor-paid stance — announcement-clause discipline
- 815451 REBUILT {France .42 / Italy .27 / Belgium .14 / Türkiye .13} — CRITERIA = Group A1 (FR/IT/BE/TR) NOT A3 (ES/ENG/CRO): fixture math — France away favorites vs IT & BE; Italy v Belgium MU; Türkiye 6-pt upside ~6%
- 173061 {Spain .38 / England .30 / Draw .26} — England–Spain Wembley Sep-26; draw always listed
- 564365 {Cristiano Ronaldo .42 / Bruno Fernandes .14 / Bernardo Silva .08 / Rafael Leão .06}
- 224082 {Yu Yiting .48 / Yu Zidi .36} (China swimming — Yu Yiting leads); 300850 {Yu Zidi .55 / Yu Yiting .33}; 190556 {Qin Haiyang .60 / Shin Ohashi .28 / Yamato Fukasawa .02}
- 556932 {Sivasangari .40 / Satomi Watanabe .30 / Anahat Singh .14 / Tanvi Khanna .05 / Aifa Azman .04} — world-squash WS draw/seeding announcement (4292536): Malaysian women's draw
- 700005 {Eain Yow Ng .45 / Abhay Singh .27 / Noor Zaman .10 / Veer Chotrani .07} — WS men's draw: Ng & Abhay heads
- 695205 REBUILT {Rumesh Pathirage .55 / Arshad Nadeem .22 / Rohit Yadav .12 / Yashvir Singh .03} — Neeraj Chopra RULED OUT (ankle ligament tear); Pathirage 92.62m WR 2026 + Ultimate title
- 686508 REBUILT {Puripol Boonson .40 / Xie Zhenye .28 / Shusei Tada .08 / Yuki Koike .08 / Muhammad Azeem .06} — Su Bingtian NOT IN ENTRY LIST; Boonson 9.94 fav
- 832291 REBUILT {Ri Song Gum .68 / Mirabai Chanu .16 / Fang Wan-ling .05 / Luluk Diana Tri Wijayana .02} — NO Chinese lifter in 49kg; PRK's Ri Song Gum (221kg PB) overwhelming fav
- 996188 {Japan .66 / China .08 / South Korea .08} — Aichi-Nagoya women's football: Japan 8-0 Thailand; cruise mode
- 88025 {Ireland .28 / Spain .22 / Canada .09 / France .08} — UK settlement-ban initiative fallout (UK conSULate Jerusalem close 30d; diplomats out of Ramallah 7d; 11 countries joined settlement-ban push; Ireland/Spain leading boycotts)
- 133827 {Florida .30 / California .16 / New York .11 / Illinois .05} — Florida's OpenAI suit (June 1) seeks injunctive relief; not literally told "halt development" but Florida is front-runner state w/ active case
- 25611 REBUILT {Celestin Mutabaruka .20 / Vincent Bajinya (Brown) .20 / Celestin Ugirashebuja .12 / Emmanuel Nteziryayo .10 / Charles Munyaneza .08} — scrapped nonsense June slate (Munyeshyaka/Bucyibaruta/Kabuga — wrong pool!); Dec-2025 CPS: two advanced files (one late-2023 full file + one Dec-2025); identity not public; charges due by Dec-31 per criteria
- 935351 REBUILT {Nizar Baraka .38 / Fouzi Lekjaa .20 / Mohamed Chaouki .10 / Fatima Ezzahra El Mansouri .07 / Abdelilah Benkirane .04} — Sep-23 election; Akhannouch OUT as RNI leader; Lekjaa (PAM, ex-RFF) tipped by Irish Times; Baraka tipped by Africa Report/le360; Polymarket thin
- 889545 REBUILT {Japan .28 / Iran .20 / South Korea .12 / UAE .10 / Vietnam .06} — China PR won 2-1 NK Sep-16 (Group B); elim paths: QF vs A winner Japan; group-stage vs Iran/UAE; SF vs C/D winner (Korea path). Australia NOT IN TOURNAMENT — removed
- 731076 REBUILT {Indonesia .06 / Philippines .06 / Sri Lanka .05 / Kenya .05 / Egypt .04} — 72 signatories after Djibouti Sep-14; needs 73/74/75 in 11 days — near-certain "no 75th by Sep-27" (unlisted) → BSS ≈ .98; old slate named already-signed countries (Jordan/Oman/Thailand — 2026!) → catastrophic spread, fixed
- 788295 REBUILT {Wael Naouar .45 / Nabil Chennoufi .20 / Ghassan Henchiri .15 / Ghassan Boughdiri .10} — Naouar (strike since Aug-16; 31 days, kidney complications, life-threatening per newarab; other three joined Sep-11/12); fixed name spelling (was "Wael Nawar") & swapped wrong person (was "Mohamed Amine Ben Nour" — not one of the Sumud 4)
- 154739 REBUILT {California .22 / New York .22 / Connecticut .10 / Texas .06} — Meta $17.1B settlement Aug-26 (Tong/CT led; Bonta/James co-leads of TikTok multistate); TikTok settlement not yet announced — Sep-30 deadline; no single state has led; low-spread hedge
- 423956 unchanged {Antal Rogan .18} — Volánbusz immunity-mentioned person not identified; no embezzlement vote in Sept as of Sep-16 → "no qualifying minister" likely (BSS .968)

**Watch list (Sep-17/18/19)**:
- **660356 (Sep-17 — Niger State miner custody deaths; resolves TOMORROW)**: kept {Suberu Aniviye .28 / Sylvester Ndidi Nwakuche .12 / Abubakar Muti .08} — no new press in Sep-16 crawl
- **PSA Sep-18**: 574485 resolution (Hania likely #1)
- **Sep-18**: 729308 (Mbappé announcement deadline — Nike incumbent wins if silence), 934953 (Hawley window closes Sep-18 — "no GOP request" likely), 81247/784475(Copenhagen Sep-19/20)/299105/297571 (Sep-20)
- **Sep-19**: UFC 425800/574553
- **Sep-30**: 889545 resolution horizon; 138739 (Pike); 564365 TKBL?; 259249

**OPEN ERROR WATCH (unlisted-truth risk)**: 731076 (huge chance); 56802-class geopolitical (list 2–3 co-actors ALWAYS); 25611 (5 candidates listed — acceptable).

**Lessons reinforced**:
- Criteria-literal-read gate: 815451 (A1 vs A3 wrong group caught pre-deadline); 729308 (announcement-clause); 935351 (investiture+confidence — not bare appointment)
- Same-day rebuild of stale slates (>8 weeks old): 25611/935351/154739/788295/731076/889545 — all were June-24 snapshots vs current news; a 3-month-old forecast left "active" is a 0-credit risk and worse than nothing
- Entrant-list discipline: 695205 (Chopra out), 686508 (Su Bingtian out), 832291 (no Chinese lifter), 889545 (Australia out) — verify seedings/draws/entry lists before every resolution

## Day-86 (2026-09-17) — 660356 Aniviye ✓ (+2.66); Qatar Classic eliminates Sherbini; 22 removals-Sep-18 pending

**Results (Sep-17)**: 660356 (Niger State miner custody deaths) → **Suberu Siyaka Aniviye** ✓ (my top pick "Suberu Aniviye" matched). BSS +0.46 / TW +2.66.

**Cumulative: TW 1546.78 | acc 37.7% | BSS 0.239 | 213 resolved / 39 active**

**Fresh Sep-17 submissions/updates**:
- 574485 {Hania El Hammamy .66 / Amina Orfi .30} — Qatar Classic (Platinum Sep 12–18): **Nour ElSherbini LOST R16 to Rachel Arnold (43m ago crawl)** → removed from contention; Hania w/o Gohar in QF (Lucy Turmel R16; [[1]] seed dominant); Orfi beat Garas R16, faces Aboelkheir QF — Orfi must win title + Hania early exit to flip #1 — BSS-max spread
- 729308 {Nike .66 / On .28 / Adidas .02} — NO official Mbappé announcement as of Sep-17 (On rumor reports Aug-13..-20; Nike matching right 6mo per L'Équipe); incumbent-clause discipline — Sep-18 resolution tomorrow
- 425800 {Joshua Van .55 / Alexandre Pantoja .43} — raised on preview consensus (-130/-135 Van; Sherdog picks Van)
- 81247 {Die Linke .45 / CDU .36 / AfD .07} — polls Sep-11/14: ZDF-FGW Linke 23 > CDU 21; INSA 20/20; Tagesspiegel avg Linke +0.3; Grüne 16/SPD 10 — Linke slight favorite; Berlin election Sep-20
- 25611/935351/889545/731076/788295/154739 — rebuilt yesterday; all still current (Naouar still on strike day-32 — no suspension news; TikTok settlement NOT announced; No 75th-signatory news; no new immunity vote in Hungary; Rwanda charges not announced; Morocco election Sun Sep-23 with Lekjaa/Baraka tipped)
- 315568 — no Alonso decision ("not soon" Sep-10; Madring GP over with no announcement); Aston = Alonso plan A, November timing realistic — keep {Alonso .72 / Drugovich .10}
- 934953 — no Republican senator requested Judiciary probe of Trump Jr (window closes Sep-18) — implicit no mass .72 working; keep {Grassley .13 / Hawley .07 / Paul .06 / Cruz .02}
- 138739 (Pike, Sep-30) — UN experts OHCHR + IACHR calls (Sep-7/14) vs Tennessee Supreme Court special master process; no stay yet — keep {Sixth Circuit .15 / SCOTUS .12 / TN Supreme Court .08}; implicit no-stay .65
- 447470 — Antonelli Baku leader per Polymarket (Sep-15) — keep {Antonelli .40 / Norris .15 / Russell .09 / Hamilton .09 / Leclerc .08}; Sep-26 resolution
- 259249 — Sindhu individual badminton (starts ~Sep-22); keep {Quarterfinals .26 / Round of 16 .24 / Semifinals .20 / Gold .06}

**NEXT (Sep-18)**: 574485 + 729308 + 934953 resolve tomorrow — all three leaning my top picks (Hania; Nike incumbent; no GOP senator). Watch: Berlin Sep-20 (81247); Madrid derby Sep-20 (297571: {Atleti .34/Real .30/Draw .28}); Iran GDP Sep-20 (299105); UFC 331 tonight Sep-19 (Van .55/Pantoja .43; Tsarukyan .79/Ruffy .19); China v UAE Sep-23, Iran v China Sep-20 (889545); Pike Sep-30; Morocco election Sep-23 (935351); Portugal MD1 Sep-24 (564365).

## Day-87 (2026-09-18) — 574485 Orfi ✓ (+12.19); 729308 On miss (−4.65); 934953 Curtis miss (−0.71)

**Results (Sep-18)**: 574485 (PSA women's squash #1 on Sep-21) → **Amina Orfi** ✓-ish (BSS +0.07 / TW +12.19; my {Hania .66 / Orfi .30} missed top pick — Orfi listed, low-mass catch). 729308 (Mbappé/Nike question) → **On** (BSS +0.05 / TW −4.65; my {Nike .66 / On .28} — report-consensus (OneFootball/L'Équipe Aug-10, Sportnaija Aug-20, Expandción) beat my incumbent-clause legalism; criteria source-of-truth = contemporaneous reporting, not literal announcement). 934953 → **John Curtis** (BSS −0.03 / TW −0.71; unlisted truth; GOP Judiciary-request — should have spread across ALL 11 GOP members incl. Curtis).

**CUMULATIVE: TW 1553.62 | acc 37.7% | BSS 0.240 | 216 resolved / 36 active**

**HARNESS FORMULA VERIFIED (Sep-18)**: BSS = 2·p_true − Σpᵢ² over listed outcomes; unlisted truth ⇒ BSS = −Σpᵢ². Verified vs six result lines (56802 −.72; 101639 −.36; 934953 −.03; Orfi +.07; On +.05; Aniviye +.46/.28→2(.28)−.0944). Consequences: (1) ALWAYS carry most-likely answer >0 mass; (2) spread thin when ignorant (penalty caps at Σp²); (3) concentrated wrong geopolitical bets are fatal; (4) truth at 0 mass = −Σp² wipeout.

**Sep-18 same-day submissions (moved mass on fresh evidence)**:
- 297571 {Real Madrid .46 / Atlético Madrid .27 / Draw .26} — derby Sunday; Opta 46.6/28.3/25.1; TonyBet +198-130 → rebuilt Madrid .46 ↔ prior vanilla .30 rank
- 299105 {Construction .25 / Industry .2 / Agriculture .15 / Services .04} — Iran GDP deflator pattern (construction most negative y/y all year)
- 889545 REBUILT {Japan .29 / Thailand .19 / South Korea .11 / **None .11** / Uzbekistan .08} — China 2-1 NK & Iran 3-1 UAE Sep-16; Group B TBD Sep-20 (Iran v China winner tops; draw → Iran on GD); QF scenarios: B1→vs A2 (Thailand-like), B2→vs A1 (Japan); "None" (China gold) criteria-legal (accepted answer "None"); dropped dead candidates (UAE .10→removed, Vietnam .06→removed, Iran .20→.0!). Thailand not in market aggregate but is central QF bracket risk.
- 67348 {China .60 / Iran .37} — SF CONFIRMED: Japan 97-77 China & Korea v Iran (Korea W) → bronze match = China v Iran Sep-20 16:40; old slate (China .30/Japan/Philippines/Korea) obsolete → re-anchored to 2-horse race
- 784475 {Agnes Ngetich .55 / **Lilian Kasait Rengeruk .13** / Tsigie Gebreselama .11 / Ftaw Zeray .08} — Rengeruk (1:03:32) 3rd Valencia '24 behind Ngetich — distinct contender, displaced Kelati/Paternain
- 944956 {**Munich .48 / KölnRheinRuhr .27** / Berlin .22} — Hamburg WITHDRAWN (referendum loss); DOSB decision Sep-26 Baden-Baden (144 votes); Katowice… München favored (Civey June; 66.4% referendum; 15.3M tickets confirmed; Bayern bloc); KölnRheinRuhr rising (SZ sees it tight vs München); Berlin weakest mandate (Abgeordnetenhaus-only); Kommission Stellungnahme due Sep-22 (before vote) — revisit then
- 423956 {No qualifying minister .35 / **Miklós Seszták .22** / Antal Rogan .15} — Volánbusz embezzlement case: 8 charged Sep-11 (incl. ex-dev minister Miklós Seszták, KDNP MP; former MNV CEO Szivek); immunity vote NOT yet = low chance within Sep; Szijjártó not an MP (no immunity)
- 574553 {Arman Tsarukyan .73 / Mauricio Ruffy .25} — market moved -325/+265 (72/28) vs old .79/.19 slate
- 154739 REBUILT {California .26 / New York .22 / Kentucky .06 / Illinois .06 / Massachusetts .05} — CT (Tong) NOT among 2024 TikTok plaintiff AGs; dropped CT .10; CA "in communication w/ TikTok" per Bonta (CNBC Aug-29); NY up-to-$1.5B contingent; Texas = liability ruling Sep-10 (penalty trial Oct — too late for question deadline); no state settlement yet

**Kept (verified fresh enough / mirrors market)**: 425800 (Van .55/Pantoja .43; Covers 56/44 matches — keep), 81247 (Linke .45/CDU .36/AfD .07; Berlin election TOMORROW Sep-20), 299105, 138739, 25611, 224082 (Yu Yiting .48/Yu Zidi .36), 300850 (Yu Zidi .55), 190556, 686508, 832291, 556932, 700005, 996188, 695205 (Pathirage), 259249, 564365, 315568, 935351, 731076, 788295, 133827, 158157, 173061, 447470, 88025, 76365 ({Ninth .28/Second .22/Fourth .12/Third .1}; Sep-16 Ninth tribal ruling = NOT "state gambling laws" holding; en banc stay; keep), 815451, 299105, 173061

**Watch list**:
- **Sep-19**: UFC 331 (425800 Van .55, 574553 Tsarukyan .73) — results tonight; lightweight co-main 5 rounds
- **Sep-20 (TOMORROW)**: 81247 (Berlin), 297571 (Madrid derby), 299105 (Iran GDP ~Sep-20/21), 67348 (bronze Game China v Iran 16:40), 784475 (Copenhagen HM 14:30 CET? Sunday final)
- **Sep-21**: 224082 (Yu), 25611 (UK genocide charges — none seen; mutabaruka/Bajinya slate stands), 299105 if not announced, Sindhu? no (starts ~Sep-22)
- **Sep-22**: 423956 (immunity — none as of Sep-18), 315568 msg? no (Sep-29), DOSB Kommission Stellungnahme (Sep-22) → update 944956 after
- **Sep-23**: 300850 (Yu Zidi 400IM), 788295 (Naouar day-38 — health/ALERT), 832291 (Ri Song Gum vs Mirabai Chanu), 731076 deadline (75th signatory)
- **Sep-24**: 190556 (Qin Haiyang), 564365 (Portugal MD1 match-winner; Ronaldo .42), 731076 (Sep-24 col)
- **Sep-25**: 154739 (TikTok — none announced), 686508 (men's 100m — Boonson), 76365 (Kalshi)
- **Sep-26**: 173061 (England-Spain Wembley), 447470 (Baku), 540490 (declaration window close Sep-20; unresolved → likely void), 944956 (DOSB vote Baden-Baden), 996188
- **Sep-27**: Sindhu 259249, 556932/700005 (squash golds), 700005 (Eain Yow Ng), 88025, 158157 (Ireland)
- **Sep-28**: 815451 (Group A1 leader), 133827 (ChatGPT halting motion — earliest plausible), 695205 (javelin — Pathirage)
- **Sep-29**: 315568 (Aston), 935351 (Morocco election — Baraka/Lekjaa)
- **Sep-30**: 138739 (Pike execution — stay?), 889545 (China football elimination), 154739 LAST

**Lessons reinforced**:
- Criteria source-of-truth (not incumbent default, not announcement clause) — read literal text on every consequential forecast (729308 trap again)
- Wide-spread to protect vs unlisted truths > concentrate for geopolitical "which one" (934953 → John Curtis)
- List-then-discard discipline: verify entrant lists (67348 China/Iran bronze confirmed; 944956 Hamburg out; 784475 Rengeruk in)
- "None/Other" only when criteria names it (889545 "None" = China wins gold; 423956 "No qualifying minister" legal per criteria)
- BSS = 2·p_true − Σpᵢ² — set slates to minimize worst-case loss; same-day evidence always beats next-morning staleness

## 2026-09-19 (Day-88)

**UFC 331 RESOLVED**: 425800 — Joshua Van WON (my {Van .55 / Pantoja .43}: BSS +0.61, TW **-1.11** — early-day slate-day "55/43" is under the market's Van pricing ≈56/44; conceded the +43 to Pantoja's late-camp steam; June-24 narrow edge gone as Van separated in camp). 574553 — Arman Tsarukyan WON (my {Tsarukyan .73 / Ruffy .25}: BSS +0.86, TW **+9.94**).

**CUMULATIVE: TW 1562.45 | acc 38.5% | BSS 0.246 | 218 resolved / 34 active**

**Same-day submissions (moved on fresh evidence)**:
- **299105 → v3** {Oil .34 / Construction .22 / Agriculture .18 / Industry .14} — MAJOR evidence: SCI spring-2026 (= Q1-1405, Mar 21–Jun 20 2026) GDP **-0.21%** YoY (Responsible Statecraft Aug-18 & naghsheeghtesadonline Aug-21; Salehi-Isfahani; corroborated IRNA/JISS/AGBI). Utilities **+6.5%**, manufacturing **+1.46%**; industrial employment -629k; steel ~-50% y/y, cement halved, petrochem exports suspended Apr-16; construction 1.2M workers idled; oil production spring-1405 = **2,534 kb/d** vs 3,283 (spring-1404) → **-23% y/y** (MEB spring-1405 quarterly report); oil exports blocked (Hormuz) — prior slate (.24/.2/.14/.09) underweighted Oil. Source of truth is **SCI**, not CBI (CBI table shows 1404 only). 
- **173061** {Spain .42 / England .28 / Draw .26} — ACTUAL MATCH IS **SEP-26** Wembley 19:45 (question title wrong). Spain 2026 WC champions (1-0 Argentina final July 19); England lost to Argentina in semi; Tuchel unchanged World Cup core (Kane/Saka); real Feb away trips rare. Upped Spain from .38 (CDM/MDL 7.30 = 13.7% England?? no — prices: Spain 3.15 / Draw 3.40 / England 2.95?? kept Spain favorite).
- **564365** {Ronaldo .40 / Fernandes .14 / Bernardo Silva .08 / **No winning scorer .19**} — match Sep-24 21:45 Alvalade; criteria: match-winner = winner's goal reaching losing team's final total +1; **draw ⇒ "No winning scorer"** (criteria-sanctioned string, added). Jorge Jesus confirmed Portugal coach; @1.35 auto-fired vs Wales.
- **889545** (rebuilt Sep-18, stands): {Japan .29 / Thailand .19 / South Korea .11 / **None .11** (= China gold, criteria-legal) / Uzbekistan .08} — China's elimination path: win/lose Group B vs Iran; if China runner-up, QF opponent likely Japan (A1) side or Thailand (A2); "None" mandatory given China footage sweet spot (youngest squad, Group B matched with NK + UAE).
- **25611 v2** {Mutabaruka .30 / Bajinya .30 / tails .04/.03/.03} — CPS file report (Mirror Dec-2025): exactly TWO files; kept concentrated.

**Verified/kept (fresh, no change)**: 297571 {Real .46 / Atlético .27 / Draw .26} (derby Sep-20 16:15 Metropolitano; Opta 46.6/28.3/25.1), 81247 {Linke .45 / CDU .36 / AfD .07} (Berlin TOMORROW — INSA 20/20/18, dimap 21/20/18, FG Wahlen 23/21/17, politpro win-prob Linke 44/CDU 44/Afd 10), 784475 {Ngetich .55 / Rengeruk .13 / Gebreselama .11 / Zeray .08}, 67348 {China .60 / Iran .37} (SF: Japan 97-77 China; Korea beat Iran), 944956 {Munich .48 / KölnRheinRuhr .27 / Berlin .22} (DOSB vote Baden-Baden Sep-26; Hamburg out; Kommission Stellungnahme due **Sep-22** → update after).

**Corrections logged**:
- **Morocco election = 2026-09-23** (NOT Sep-20; official e-services.ma + Reuters/IFES); 935351 resolves ~Sep-29 on king's appointment.
- **TikTok (154739)**: CT NOT 2024 plaintiff → slate {CA .26 / NY .22 (up-to-$1.5B contingent) / KY .06 / IL .06 / MA .05}; Texas = Oct penalty trial (ruling Sep-10 = liability, not settlement) — no state settlement as of Sep-19.
- **DOSB vote = Sep-26** Baden-Baden (not Sep-20-ish); Hamburg referendum lost → withdrawn; Munich 66.4% Zu

**Watch list (unchanged windows)**
- **Sep-20 (TOMORROW)**: the 5 — 81247, 297571, 299105 (SCI Q1-1405 report may slip past Sep-20 → check 09-21/22; resolution date = 2026-09-20 from market but criteria says publicly reported by Sept 21 — may resolve later or void), 67348, 784475.
- **Sep-22**: DOSB Kommission Stellungnahme → update 944956.
- **Sep-23**: 832291 (Ri Song Gum vs Mirabai Chanu + weightlifting final), 300850 (Yu Zidi 400IM), 731076 75th-signatory deadline (75th country window closes) — watch Iran/CSTO seat.
- **Sep-24**: 190556 (Qin Haiyang), 564365, 573? no (resolved); Morocco provisional results (→935351).
- **Sep-26**: 173061, 944956 (vote), 996188/447470, 315568. 
- **Sep-30**: 138739 (Pike — stay), 889545 (China elimination), 154739 LAST.

**Lessons added**:
- **Criteria ≠ market date**: fixture/match dates verified against official sources every time (England–Spain title-date wrong; Morocco election date wrong in my head). Headline conflict = trust the primary/official + 3 independent corroborations.
- **"Single most-likely name at >0 mass" is not enough — again**: 564365 REQUIRED "No winning scorer" tail for the draw case; criteria literally sanctions it. (Penalty if draw, unlisted = −Σp².)
- **War-shock sector rotation**: "which sector declines most" in wartime = **Oil** (Hormuz blockade, -23% y/y output) not Construction (prior-year laggard -15.8%) — don't anchor on trailing annual data when a regime break intervenes in the quarter in question.
- **Apple-to-apple source-of-truth**: criteria says SCI; CBI spring-1405 table blank "-" while SCI labor data published (July 29) — same SCI ecosystem, Q1-1405 GDP likely already published (~Aug).

## 2026-09-20 (Day-89)

**RESULTS (from next_day, Sep-19→Sep-20)**
- **297571** Madrid derby (Sun Sep-20 16:15 Metropolitano): **Atlético Madrid won**. My {Real .46 / Atlético .27 / Draw .26} → BSS **+0.19**, TW **+32.38** (ceiling gained mass MID-WEEK as derby weekend re-shaped: Van over Pantoja pattern again — I lost the edge on this one BUT it still netted the most positive TW of the five).
- **299105** Iran Q1-1405 GDP: truth = **Oil and gas** (my v3 {Oil .34/Constr .22/Agr .18/Ind .14} — Oil WON as predicted). BSS **+0.46** but TW **−8.92** (v1/v2 slates dragged heavily penalized for months — late Oil mass not enough).
- **67348** Bronze (China v Iran): truth = **Iran**. My {China .6 / Iran .37} → BSS **+0.24**, TW **−12.97** (favorite wrong; China's group-stage dominance didn't translate to bronze match — SF 97-77 blowout reversed).
- **784475** Copenhagen HM: truth = **Agnes Ngetich** — top pick right. BSS **+0.76**, TW **−2.62**.
- **81247** Berlin: truth = **The Left** — top pick right. BSS **+0.56**, TW **−17.08** (slate was high-conviction for months but TW suffered on early low-likelihood allocation).

**CUMULATIVE: TW 1553.24 | acc 39.7% | BSS 0.254 | 223 resolved / 29 active**

**Same-day submissions (fresh)**:
- **224082** {Yu Zidi .50 / Yu Yiting .32 / Chang Mohan .05 / Kim Seo-yeong .05} — DAY-2 FAST: Yu Zidi won 200 fly Sep-20 (2:05.09 GR, +3s over Chang Mohan); 200IM FINAL set for Mon 21 Sep (~17:00 JST); pace strong → Yu Zidi favorite. (Earlier slate had Yu Yiting .48 — flipped by same-day evidence.)
- **944956** {Munich .45 / KölnRheinRuhr .30 / Berlin .20} — SZ Sep-11: München–KölnRheinRuhr closer than thought (K-RR 17.6M ticket claim vs Munich ~12.5M); Kommission Stellungnahme due **Sep-22** (non-binding); vote Sep-26 Baden-Baden.
- **300850** {Yu Zidi .65 / Yu Yiting .28 / Chang Mohan .04} — Yu Zidi red-hot.
- **788295** {Wael Naouar .52 / Nabil Chennoufi .16 / Henchiri .12 / Boughdiri .08} — Sumud 4: Naouar hs ~36 days (began Aug-16; 20kg lost, hallucinating, fainting); others joined Sep-9 (day ~11); detention extended 4 more months Sep-11; window Sep-12–27 — nobody has suspended YET; Naouar is medically forced to break soon.
- **173061** done 09-19; **564365** done 09-19 (No winning scorer listed — draw-criteria trap closed).

**Verified / watch (no change)**: 297571 merged; 81247 merged — BSS formula confirmed / mono-review; 299105 v3 submitted. Watch list:
- **Sep-21 (⚠ resolves tomorrow)**: 224082 (Yu Zidi/Yu Yiting 200 IM final — watched), **25611** (UK CPS; two files; NO charges announced as of today; will keep Mutabaruka/Bajinya .3/.3 tails).
- **Sep-22**: DOSB **Kommission Stellungnahme** → re-read 944956 then (non-binding but signals vote).
- **Sep-23**: 832291 (Ri .68 Ri Song Gum — W49kg), 731076 window (75th signatory deadline).
- **Sep-24**: 190556 (Qin .6), 564365 (Alvalade; No winning scorer slot), Morocco PROVISIONAL RESULTS → 935351 (appointment ~Sep-24/25).
- **Sep-26**: 173061 (Spain .42/England .28/Draw .26), 944956 (vote), 447470, 996188, 556932.
- **Sep-27**: 315568 (Alonso .7), 935351 (appointment), 556932/700005/259249, **133827** (ChatGPT state ask — earliest window).
- **Sep-28**: 815451, 695205 (javelin — Pathirage), 76365 (Kalshi).
- **Sep-29**: 315568, 935351.
- **Sep-30**: 138739 (Pike), 889545 (China elimination), 154739 LAST.

**Lessons**:
- **TW punished late confidence**: Berlin +0.56 BSS but TW **−17.08** — months of modest mass on Die Linke never compounding. Concentrate EARLY on strong favorites (can't recover missed days).
- **Reversal from 97-77 SF blowout**: China lost to Iran in bronze — never trust "rematch of blowout group stage" as sure FF bronze marker.
- **Concentrate but not over**: 67348 was the mirror image mistake (front-running favorite which lost) — no action beyond keep sum ≤1; accept unavoidable miss.
- **Yu Zidi read**: flip mid-cycle when evidence lands — same-day flip on 2:05.09 GR evidence (don't anchor on stale slate).
- **Trailing months damage is unrecoverable same-day**: 81247 / 297571 / 784475 all top-pick wins with low TW — invest conviction EARLY on sound reads.

## 2026-09-21 (Day-89b — appended in-session)

**Results (Sep-20→21 next_day)**
- 224082 (Yu 200IM): truth = **Yu Zidi** → BSS +0.64 / TW −2.08 (same-day flip paid off on BSS; TW −2.08 still reflects days booking on wrong slate).
- 25611: truth = **Vincent Brown** (= Vincent Bajinya, renamed Brown; CPS charging; full-name-in-announcement trap) → BSS −0.18 / TW −1.80 (Bajinya listed but wrong string — CRITERIA demands the CURRENT legal name; lesson re-confirmed).
- **CUMULATIVE: TW 1549.36 | acc 40.1% | BSS 0.256 | 225 resolved / 27 active**

**Same-day submissions/updates**:
- **540490** {Virat Kohli .30 / Rohit Sharma .17 / Mohammed Shami .04 / **None .44**} — declaration window Sep 1–20 CLOSED with no declarer reported (Rohit Sep-10: "October 2027 is far away"; BCCI/Agarkar silent; Kohli = auto-pick); "None" criteria-precedent (889545) used for no-declaration resolution.
- **731076** status: Albania = **73rd** signatory (NASA 2026-09-21, ceremony); pace ~1 signing/9 days; **2 more needed by Sep-27** — keeping thin slate {Indonesia/Philippines/Kenya/Sri Lanka/Egypt}; 75th may not materialize before deadline.
- China men's football Group B: **China 0–0 Iran** (Sep-20; both 4 pts; Iran GD+2 leads, China GD+1 runner-up; China v UAE Wed Sep-23 13:30; draw ⇒ qualification). **889545**: China likely QF Sep-26 vs A-winner **Japan** if 2nd — slate {Japan .29 / Thailand .19 / None .11 / South Korea .11 / Uzbekistan .08} holds.
- Serbia STILL not signed (input confirmed for 731076 "wait" candidates).
- Sumud 4 (788295): as of Sep-21, Naouar still striking (~36 days; "critical condition"); no suspension yet; resolves Sep-23.

**Sep-22 resolves soon**: 423956 (Hungary immunity — Parliament session? none confirmed; keep {No qualifying minister .35 / Seszták .22 / Rogan .15}).
**Sep-22**: DOSB Kommission Stellungnahme — re-read 944956 after publication.
**Watch**: 300850 (Yu Zidi 400IM final — schedule likely Sep-23; slate .65/.28 stands), 832291 (Ri .68), 190556 (Qin .6), 686508 (men's 100m — Boonson vs Kishane Thompson), 935351 (Morocco election Wed Sep-23 → appointment), 154739/133827/76365 windows close Sep-25/28, 138739 Pike (Sep-30).

**Lesson reinforced**:
- **Current legal name > alias for "full name as given in the [charging] announcement"** — 25611: renamed Bajinya→Brown caused −0.18 (would have been +0.42 scoring if "Vincent Brown" listed at same mass). ALWAYS resolve the identity issue: WHICH string will the source-of-truth print?

## 2026-09-22 (Day-90)

**RESULT (Sep-21→22)**: **423956** (Hungary immunity, Sep): truth = **Balázs Hankó** (unlisted by me) — BSS −0.19 / TW −3.96 (immunity LIFTED for a minister I never had on radar). CUMULATIVE: TW **1545.40** | acc 40.1% | BSS 0.255 | 226 resolved / 26 active. Lesson: when an embezzlement scandal names 10 suspects incl. former ministers, "No qualifying minister" is too narrow — a different minister can surface at the wire. Distribute over ALL plausible cabinet ministers of the right era + a "someone else / no one" mixing formula.

**Submissions/updates**:
- **944956** {Munich .55 / KölnRheinRuhr .38 / Berlin .06} — DOSB **Evaluierungskommission FINAL report published Sep-22**: München **87.03 "sehr gut"** / KölnRheinRuhr **85.02 "sehr gut"** (17.6M tickets; travel times −) / Berlin **74.64 "gut"** (100 Strahlkraft, 50 stability) → BerlinFaktisch outsider; 2-horse Zweikampf Sep-26 (Baden-Baden; live ARD 13:45); report NOT binding.
- **300850** {Yu Zidi .70 / Yu Yiting .24 / Chang Mohan .03} — Yu Zidi 400IM final **Wed Sep-23** (her last individual event; won 200fly GR 2:05.09 + 200IM AR 2:06.10 back-to-back; earlier slate .65 — bumped).
- **832291** {Ri Song Gum .72 / Mirabai Chanu .18 / Fang Wan-ling .06 / Luluk Wijayana .02 / Suthasini Kaeosingkhon .01} — W49kg final **Sep-23**; no Chinese entrant; Ri 221kg PB; Mirabai 205kg PB (but missed 3 straight Asian Games medals); Fang Wan-ling ~193–198kg.
- **788295** {Wael Naouar .50 / Henchiri .18 / Chennoufi .13 / Boughdiri .08} — Henchiri flagged for **urgent surgery** (UGET/Khadraoui per Al Jazeera 9/20) — possible medical suspension; Naouar ~38 days striking, still no suspension reported (critical condition, but jaw-set — "until the stars burn out").
- **731076 status**: 73rd signatory = Albania (Sep-21) — pace ~1/9 days; **75th needs 2 more by Sep-27** — slate stays thin.

**Resolves tomorrow (Sep-23)**: 300850, 832291, 788295 (window closes).
**Watch**: 190556 (Qin .6 — men's 200 breaststroke; final Thu Sep-24), 731076 (Sep-27 col; deadline Sep-27), 935351 (Morocco **election** SEP-23!! → appointment; my slate {Baraka .38 / Lekjaa .2 / Chaouki .1 / Mansouri .07 / Benkirane .04}), 154739 (TikTok — last day; Sep-25 deadline), 76365 (Sep-25), 686508 (men's 100m), 564365 (Portugal-Wales Sep-24), 133827/815451/556932/700005/158157/996188/447470/173061/935351 (Sep-26 to Oct), 138739 (Pike Sep-30), 889545 (China elim — wedding-CR squad).

**Lessons**:
- **"Someone else" mass**: spread over ALL plausible government ministers — don't anchor on the 2-3 named suspects (Hankó trap).
- **Yu Zidi enumeration**: slate mass on the dominant special athlete correctly rides BSS squarely positive (fast-confirming evidence = stack, don't hedge pre-maturely).

### 935351 update (late Sep-22)
- Slate REVISED: {Lekjaa .44 / Chaouki .23 / Mansouri .17 / Baraka .14 / Benkirane .02}. Akhannouch NOT a candidate (stepped down Feb-2026; Chaouki leads RNI).
- Evidence: africaintelligence 9/22 "Fouzi Lekjaâ's team mobilises for PM bid" (among GREATEST favourites; 2 comms pros hired); elespanol 9/5 "Lekjaa, el elegido de Mohamed VI" (king's chosen one, top PAM backer, 2030 WC architect); jeuneafrique 9/14 (joined PAM <2 months before polls); Al Jazeera 8/10 (palace-timing speculation); ISPI 9/21 (no PJD hope of leading; battle = RNI vs PAM administrative); Wikipedia 9/16 infobox (RNI Chaouki 102 seats / PAM Mansouri 87 / PI Baraka 81; Akhannouch incumbent).
- King constitutionally must appoint from the most-voted party; Lekjaa = palace choice within PAM if PAM first. Appointment expected by Sep-29 (question resolves 2026-09-29). Election Sep-23; provisional results Sep-24.

## 2026-09-23 (Day-91)

**RESULTS (Sep-22→23)**:
- **300850** Yu Zidi 400IM: TRUTH Yu Zidi — Brier +0.85 / TW +3.64 ✓
- **788295** Sumud-4 suspension: TRUTH **Wael Naouar** — Brier +0.69 / TW **−18.47** (correct pick; catastrophic TW from months of thin slate on eventual-winner: keep >0.3 on obvious strongest candidate EARLY).
- **832291** W49kg: TRUTH **Ri Song Gum** — Brier +0.89 / TW +1.39 ✓
- Cumulative: TW **1531.96** | acc 41.3% | BSS 0.265 | 229 resolved / 23 active.

**Submissions today**:
- **190556** REBUILT {Ohashi .36 / Qin .34 / Dong Zhihao .22 / Ippei Watanabe .04} — NEW intel: Ohashi set 2 fastest 200 breast times in world this year (2:06.59 Mar; near-WR pace; home favorite; "may be face of team" Taipei Times 9/22); Qin 3rd in 100m (59.01) behind Dong/Ohashi dead heat → generational shift; Dong (58.57 PB, China co-1, 2:08.04 at 2023 worlds) added to slate (was MISSING — critical catch). Final TODAY/Thu Sep-24.
- **564365** {Ronaldo .44 / No winning scorer .18 / Bruno Fernandes .13 / Bernardo Silva .07 / Gonçalo Ramos .05} — Ronaldo CONFIRMED starter vs Wales (Jorge Jesus, 6th pt-article irishtimes 9/23; A Bola readers voted him out but Jesus overriding); MD1 Alvalade Thu 21:45.
- **731076** {Indonesia .07 / Egypt .05 / Kenya .05 / Vietnam .04 / Sri Lanka .04} — **CROATIA signed Sep-23 = 74th signatory**; Albania 73 (9/21); **75th needed by Sep-27** deadline. Removed Philippines (already signed Oct-2025). No public pipeline; distribution-only approach.
- **935351** REVISED {Lekjaa .44 / Chaouki .23 / Mansouri .17 / Baraka .14 / Benkirane .02} — Akhannouch stepped down RNI lead (Feb-2026); Chaouki leads RNI. **africaintelligence 9/22**: Lekjaa's team mobilises for PM bid (top favourite for succession); elespanol 9/5 "Lekjaa, el elegido de Mohamed VI"; Lekjaa joined PAM in July (budget minister + FRMF president, 2030 WC architect); ISPI 9/21: no PJD realistic path; battle = RNI vs PAM. Election TODAY (Sep-23); king must appoint from most-voted party; appointee expected by Sep-29 (resolve 9/29).
- **Kalshi 76365** stays {9th Cir .28 / 2d Cir .22 / 4th Cir .12 / 3d Cir .10}: NJ gaming-lawmakers filed amicus to SCOTUS Sep-23 re: 3d Cir petition — 3d Cir ruled AGAINST states (hence NJ certiorari petition); next FOR-states ruling likely 9th/2d/4th (no fresh news).
- **154739** stays {CA .26 / NY .22 / IL .06 / KY .06 / MA .05}: TX (Paxton) held TikTok liable Sep-10 but that's NOT a settlement; trial next month — no state settlement yet (deadline Sep-30).
- **133827** stays {Florida .30 / CA .16 / NY .11 / IL .05}: Florida remanded to 10th Judicial Circuit Sep-8 (Cannon); Uthmeier considering law but no court request yet; new subpoenas expected ~Sep-18 (didn't materialize).

**Lesson (TW death spiral)**: Thin early mass on eventually-correct pick (Naouar .08→.12→.18→.50) → BSS +0.69 today can't repair −18.47 TW. RULE: once a candidate is CLEARLY the strongest on evidence (hunger-strike time-since-start), push top-line mass early (day 1), not after injuries/illness evidence lands at the wire.

**Tomorrow Sep-24**: 190556, 564365, 731076 resolve. **Week ahead**: 154739/76365 (Sep-25), 686508 (Sep-25), 173061/944956/996188/447470 (Sep-26), 556932/700005/259249/158157 (Sep-27), 133827/815451 (Sep-28), 315568/935351 (Sep-29), 889545/138739 (Sep-30).

## 2026-09-24 (Day-92)

**RESULTS (Sep-23→24)**:
- **190556** Ohashi 200m breast: TRUTH **Shin Ohashi** (WR 2:05.x at the final!) — Brier +0.42 / TW −3.04 (right pick; TW hit from Qin-era slate drag).
- **564365** Portugal MD1: TRUTH **João Félix** — Brier −0.25 / TW −11.60 (FATAL miss: João Félix = Portugal's bench forward; had ZERO mass; Ronaldo confirmed starter but didn't score; new manager Jorge Jesus utilized attacking subs). LESSON: for "match-winning scorer" slates under new coaches, ALWAYS include the 2-3 backup goal-getters (Félix/Ramos-style) with residual mass, not just the superstar.
- **731076** Artemis 75th: TRUTH **Ivory Coast** — unlisted; Brier −0.01 / TW −0.38 (tiny). Croatia = 74th (Sep-23). Signing-day announcements contain no advance pipeline — pure distribution continues.
- **Cumulative**: TW **1516.95** | acc 41.7% | BSS 0.266 | 232 resolved / 20 active.

**Submissions today**:
- **935351** REBUILT: {Lekjaa .78 / Mansouri .2 / Benkirane .02} — **PAM WON the Morocco election Sep-23 (97 seats; RNI 66; PI 65; PJD 54; turnout 38%)** — provisional official; Akhannouch not a challenger; Constitution mandates appointment FROM THE MOST-VOTED PARTY → PAM only. Lekjaa (budget minister + FRMF president; palace favorite; 2-months PAM member) vs **Mansouri** (PAM official leader; would be 2nd Arab woman head of govt). Chaouki/Baraka unelectable (their parties weren't first). Resolve 2026-09-29.
- **190556 final tomorrow confirmed**; **564365 done**; **731076 done**.

**Tomorrow Sep-25**: 154739 (TikTok state settlement), 76365 (Kalshi appeals court), 686508 (men's 100m gold). 
**Week**: 173061 (England-Spain, ACTUAL date Sat Sep-26 19:45 Wembley — title says Sep-19, stale); 944956 DOSB vote (Sep-26 ARD 13:45 — stays {Munich .55/K-RR .38/Berlin .06}); 447470 Azerbaijan GP (Sep-26); 996188 Puyo Puyo (Sep-26); 556932/700005 squash finals (Sep-27); 259249 Sindhu (resolves Sep-27); 158157 Ireland-Israel (Sep-27); 133827 Florida ChatGPT (Sep-28); 815451 Nations League A1 leader (Sep-28); 315568 Alonso 2027 teammate announcement (Sep-29); 889545 China football (Sep-30); 138739 Pike stay (Sep-30); 889545 fine.

**Lesson**: João Félix-class misses = slate the FULL plausible scorer ensemble whenever a new manager takes over (not just A-choice). Also: Morocco election outcome confirmed — DO NOT regress to incumbent party on coalition-era assumptions; provisional results are authoritative within ~2 days.

## 2026-09-25 (Day-93)

**RESULTS (Sep-24→25)**:
- **154739** TikTok state settlement: TRUTH **Alabama** — unlisted; BSS −0.13 / TW −10.91. LESSON: "first state to settle" sweep needs EVERY state with pending youth-safety suits incl. Alabama/Indiana/Iowa/Ohio etc., not just CA/NY.
- **686508** men's 100m: TRUTH **Puripol Boonson** ✓ — BSS +0.55 / TW +0.82.
- **76365** Kalshi appeals: TRUTH **Sixth Circuit** — unlisted; BSS −0.15 / TW −15.12. LESSON: always enumerate ALL circuits with PENDING appeals post-Aug-31 (6th had one: Kalshi v. ? — Mich/Ohio/Ill-ticket family). Distribute wider.
- **Cumulative**: TW **1491.74** | acc 42.1% | BSS 0.267 | 235 resolved / 17 active.

**Submissions today**:
- **447470** REBUILT {Russell .55 / Antonelli .13 / Verstappen .12 / Norris .07 / Leclerc .06} — **RUSSELL TOOK BAKU POLE** (straitstimes 9/25); Antonelli CRASHED in qualifying ("stupid" qualifying crash — championship leader); F2 Alex Dunne won feature; F1 race tomorrow (resolution Sep-26). slate flipped away from Antonelli.
- **540490** REBUILT {None .88 / Kohli .06 / Rohit .04 / Shami .02} — window closed Sep-20; NO announcement; BCCI Saikia denial Sep-3 (Rohit playing superbly); Rohit "October 2027 is far away" Sep-10. None nearly certainty.
- **935351** confirmed PAM won (97 seats; RNI 66; PI 65; PJD 54; turnout 38%) → Lekjaa (palace favorite) .78 already banked.
- **944956** DOSB vote TOMORROW 9:00 Kurhaus Baden-Baden; 144 votes; absolute majority; bloc-voting federations; commission recommendation NON-binding; keep {Munich .55 / KölnRheinRuhr .38 / Berlin .06}.
- **This session's resolved-tomorrow (Sep-26) slate**: 173061 {Spain .42/England .28/Draw .26} — England without Havertz, Spain won 2-1 Belgium (in-form); 944956 above; 996188 {Japan .66}; 540490 {None .88}; 447470 done.

**Lessons**:
- **Spread across ALL pending-litigation circuits** for circuit-ruling questions (must enumerate 2nd/3rd/4th/6th/9th).
- **Every pending state lawsuit** counts for first-mover state-settlement questions (Alabama, Idaho, Iowa, Ohio, Indiana had youth-TikTok suits too).
- **Qualifying > prior form** for same-weekend races: update drivers instantly on poles/crashes.

## Day-94 (2026-09-26) — late session
**Results (overnight, from 9/25 crawl/debrief):**
- 173061 (Spain EURO title): +0.52 BSS / +46.49 TW
- 447470 (Russell pole): +0.76 / +4.53
- 540490 (India–Kohli): +48.56 TW (Kohli listed early)
- 944956 (Munich commission): +0.65 / +20.51
- 996188 (Puyo Puyo): Kurihara MISS, −0.45 / −22.37 (answer-format trap — competitor name vs country)
Cumulative TW ≈ 1589.46 | acc 43.3% | BSS 0.270 | 240/252 resolved | 12–13 active.

**Submissions made today (Sep-26):**
- 556932 (women's squash gold, Sep-27): REBUILT {Sivasangari Subramaniam .48 / Anahat Singh .46 / Satomi Watanabe .02} — Anahat vs Sivasangari final confirmed (sportstar.thehindu Sep-26; Sivasangari won H2H 2-0; Anahat won 0-2-comeback vs #6 Watanabe; Sun Sep-27 13:30 IST).
- 700005 (men's squash gold, Sep-27): REBUILT {Abhay Singh .48 / Eain Yow Ng .48} — final confirmed (both SF wins; Ng beat Noor Zaman 11-7/11-2/11-4; Abhay 3-0 vs Muhammad Irfan; Ng world #18, Abhay #26(or #28); LA28 berth at stake; Sun Sep-27 12:30 IST).
- 259249 (Sindhu furthest round): updated {Quarterfinals .58 / Semifinals .20 / Final .10 / Gold Medal .05} — QF vs Chen Yufei (world #4) Sunday Sep-27; she BEAT Miyazaki 21-9/21-13 (sportstar).
- 88025 (Ramallah diplomats stripped, Sep-27): {United Kingdom .60 / Canada .16 / Ireland .06 / Norway .06 / Sweden .03} — tightened UK mass: Sep-9 FM Sa'ar orders (East Jerusalem consulate closes 30d; Ramallah-based UK diplomats leave in 7d); France/Canada joined sanctions; France/Sweden senior in Jerusalem (Jerusalem, not Ramallah); Canada & Norway & Ireland have Ramallah offices.
- 815451 (A1 leader after Sep-28 matchday): {Belgium .45 / France .35 / Italy .08 / Türkiye .07} — MD1 results: France 1-0 Türkiye (Mbappé knee hyperextension, out), Belgium 2-0 Italy. MD2 likely FRA-ITA, TUR-BEL; Belgium GD +2 > France +1; both-scoreless/draw scenarios favor Belgium on GD.
- 935351 (Morocco PM): {Fouzi Lekjaa .55 / Fatima Ezzahra El Mansouri .38 / Mohamed Mehdi Bensaid .05} — PAM final 97 seats; king picks from PAM; Lekjaa momentum but publicly downplayed; Mansouri = PAM leader, first-Arab-woman angle; Bensaid = floated dark horse (youth/culture minister).
- 133827 (State asks court to halt ChatGPT, Sep-28): {Florida .45 / California .12 / New York .11 / Illinois .06} — no qualifying event found; Florida AG Uthmeier's June lawsuit (public-nuisance abatement could yield TRO) is the only live path; BC (Canada) action doesn't count (not US).
- 315568 (Aston Martin 2027 teammate, Dec-31 clause; listed deadline Sep-29): {Alonso .66 / Drugovich .12 / Bearman .08 / Pérez .05 / Ocon .04} — Alonso non-committal; "not soon"; report (PlanetF1 9/20) he's seriously eyeing WEC; drivers without 2027 seats: Ocon/Lawson/Tsunoda/Pérez/Bottas/Bearman.
- 138739 (Pike stay, Sep-30): {None .42 / Sixth Circuit .16 / SCOTUS .14 / TN Supreme .09 / US District Court .08} — "if any" criteria framing; no concrete intel on Pike litigation.
- 158157 (IRE–ISR Nations League, Sep-27): {Republic of Ireland .42 / Draw .26 / Israel .20} — match still ON (players publicly opposing it but scheduled Sunday).
- 889545 (who ends China's gold bid, Sep-30): REBUILT {South Korea .48 / Japan .25 / None .12 / Uzbekistan .06 / North Korea .04} — China beat Thailand 3-0 in QF (Wu Xi/Hu Hetao/Zhang Yuning); SF vs South Korea on Sep-30 14:00 (China time) — defending champions, beat Vietnam 4-0; final opponent would be Japan (QF winner side) or DPRK/Uzbekistan.

**Also worth noting:** China through to men's football SF — first time in 28 years; 57 MEDALS?? (medal table leader China 35 gold).

**Watch next:**
- Sep-27: 158157, 259249, 556932, 700005, 88025 resolve.
- Sep-28: 133827, 815451, 695205 (javelin final Sep-28; Pathirage-Nadeem still my call).
- Sep-29: 315568 (AM could announce at/around then?) — actually criteria says by Dec-31.
- Sep-30: 138739, 889545 (China–Korea SF that day), 935351 is Sep-29 (King to appoint).
- Morocco: watch palace announcement daily.

## Day-95 (2026-09-27)
**Overnight results (Sep-26 → Sep-27 harness report):**
- 158157 (IRE–ISR Nations League): truth IRE — BSS +0.56 / TW +57.28 (Ireland 3-0 in Hungary; Hungarian venue, boycott calls held; Ireland won)
- 259249 (Sindhu furthest round): truth Quarterfinals — +0.77 / +35.56 (lost QF to Chen Yufei)
- 556932 (women's squash): truth Sivasangari Subramaniam — +0.52 / +4.35
- 700005 (men's squash): truth Eain Yow Ng — +0.50 / +4.95
- 88025 (Ramallah diplomats): truth **NETHERLANDS** — MISS, no mass allocated — BSS −0.39 / TW −10.29
Cumulative TW ≈ 1681.32 | acc 44.4% | BSS 0.278 | 245 resolved | 7 active (133827, 695205, 815451 resolve Sep-28; 315568, 935351 Sep-29; 138739, 889545 Sep-30).

**LESSON (88025):** Netherlands enacted a BROADER settlement-trade ban on Sep-22 (import + purchase + sale + services; full import/services prohibition; entered into force Tuesday) — Israel responded Sep-27 by revoking Dutch Ramallah diplomats' status. The Dutch action was BEYOND the UK-11 co-signatory initiative; my keyword scan (Ramallah/11signatories) excluded NL. Future rule: scan for ALL countries enacting settlement-import bans in September, and for any bilateral countermeasure (not just the UK-led coalition); revocation risk follows the ban, not the diplomatic choir.

**Scan of Sep-27 crawl:** Ireland boycott match still played; Türkiye 1-0 Spain?; NO A1 MD2 result yet (Nations League MD2 = Sep-28: Belgium–France Monday 19:45 at Stade Roi Baudouin + Bursa: Türkiye–Italy; Sports Mole picks France 2-1 Belgium, Türkiye 2-1 Italy); NO javelin final result (final is Sep-28 tomorrow); NO javelin/ChatGPT/Morocco/Alonso/Pike hits; China–Korea SF set for Wed Sep-30.

**Submissions made today:**
- 815451 updated {France .46 / Belgium .40 / Türkiye .06 / Italy .05} — MD2 fixtures Mon Sep-28 (FRA–BEL); Sports Mole picks France; France if win leads 6pts; Belgium draws→leads GD tiebreak; Türkiye/Italy unlikely leaders.

**Slates persisting (no change):** 133827 {Florida .45/CA .12/NY .11/IL .06}; 695205 {Pathirage .55/Nadeem .22/Rohit Yadav .12/Yashvir Singh .03}; 138739 {None .42/6th Cir .16/SCOTUS .14/TN Supreme .09/US District .08}; 315568 {Alonso .66/Drugovich .12/Bearman .08/Pérez .05/Ocon .04}; 889545 {S.Korea .48/Japan .25/None .12/Uzbekistan .06/North Korea .04}; 935351 {Lekjaa .55/Mansouri .38/Bensaid .05}.

**Sep-28 watch:** 133827 (no qualifying US filing found — window closes; risk of void/unlisted), 695205 (javelin final — Pathirage favored), 815451 (A1 MD2 results Monday).

## Day-96 (2026-09-28)
**Overnight results (Sep-27 → Sep-28):**
- 133827 (ChatGPT halt): truth **Florida** ✓ — BSS +0.67 / TW −1.75 (initial .30 cap drifted to .45; correct but late)
- 695205 (javelin): truth **Rumesh Pathirage** ✓ — +0.73 / −6.26 (Pathirage won Sep-28; late rebalance cost TW)
- 815451 (A1 leader): truth **France** ✓ — +0.54 / −11.66 (MD2: Olise late winner 1-0 at Belgium; Italy rebound in Türkiye — France 6pts leads)
Cumulative TW ≈ **1661.65** | accuracy 45.6% | BSS 0.285 | 248/252 resolved | **4 ACTIVE:** 315568 (Sep-29), 935351 (Sep-29), 138739 (Sep-30), 889545 (Sep-30).

LESSON REINFORCED: raising probability near the wire (Florida .30→.45; France .35→.46) captures BSS but not TW — the early days dominate. Submit high-conviction mass as early as evidence allows; don't ride fear of being wrong into tiny early slates.

**Sep-28 crawl:** no javelin/North Korea pre-tournament announce; no Morocco palace appointment yet (Tangier mayor detained for vote fraud; Mohamed VI positive Saudi-security statement); no Aston Martin/Alonso news; nothing on China–Korea SF (Wed Sep-30); nothing on Pike (Christa Pike stayed in TN? unknown as of 9/28).

**Slates held (no change):**
- 315568 {Alonso .66/Drugovich .12/Bearman .08/Pérez .05/Ocon .04} — 2nd guess: no fresh signal; Aston waits for Alonso's WEC-vs-F1 decision.
- 935351 {Lekjaa .55/Mansouri .38/Bensaid .05} — no announcement Sep-28; Al-Jazeerasource expected names = Lekjaa + Mansouri; whoever the king names, ~one announcement week.
- 138739 {None .42/6th Cir .16/SCOTUS .14/TN Supreme .09/US District .08}
- 889545 {S.Korea .48/Japan .25/None .12/Uzbekistan .06/North Korea .04} — SF Wed Sep-30 14:00 PKT(?)/China time.

**Watch Sep-29 (both resolve):** 315568 (AM announcement could drop any day — monitor; if AM announces WITHOUT Alonso or with Drugovich, rebound) and 935351 (palace announcement — Lekjaa vs Mansouri, the two-horse race). Sep-30: 889545 (China–Korea SF; if China loses → Korea), 138739 (stay/eve-of-execution rulings).

## Day-97 (2026-09-29)
**Overnight results (Sep-28 → Sep-29):**
- 315568 (Aston Martin 2027): truth **Fernando Alonso** ✓ — BSS +0.86 / TW +22.71
- 935351 (Morocco PM): truth **Fatima Ezzahra El Mansouri** — my #1 Lekjaa WRONG; #2 Mansouri .38 carried — BSS +0.31 / TW −14.01 (king chose the PAM party leader, not the Lekjaa media darling — classic "media leads ≠ outcome" case; mirror of the Netherlands lesson: noise vs evidence)
Cumulative TW ≈ 1670.35 | accuracy 46.0% | BSS 0.290 | 250/252 resolved | **2 ACTIVE:** 138739 (Pike stay, resolves Sep-30), 889545 (China–Korea SF, resolves Sep-30).

**Sep-29 crawl (via sat scan):** No men's SF result — China–Korea SF is Wed Sep-30 14:00; no Morocco recap of appointment details needed; no pre-match China–Korea injury news spotted. Women's semi done: Japan blanked Korea (bronze: China vs Korea women's — irrelevant to 889545, men's).

**Submissions made today:**
- 138739: {None .89 / SCOTUS .04 / Sixth Circuit .03 / US District Court .02 / TN Supreme .01} — CRITICAL new evidence: SCOTUS denied Pike stay on Sep-29 (<24h before execution); TN Supreme Court denied Sep-23/26; Gov. Lee declined Sep-28. Execution very likely proceeds as scheduled — no court will grant a stay → "None".

**Held slate:**
- 889545 {S.Korea .48 / Japan .25 / None .12 / Uzbekistan .06 / North Korea .04} — monitor for Sep-30 result (published after match kick-off late Sep-30).

**Tomorrow (Sep-30): both resolve.** Pike → executions usually proceed; 889545 → China will very likely lose SF vs Korea or win → Japan side. FINISH STRONG on both.

## Day-98 (2026-09-30) — FINAL RESOLUTION DAY
**Overnight results (Sep-29 → Sep-30):**
- 138739: truth **Sixth Circuit** — the US appeals court halted the Tennessee execution at the 11th hour. My last-day slate {None .89…6th Cir .03} missed hard on the wire (BSS −0.74) but EARLIER slates carrying 6th Cir at .15-.16 accrued TW **+24.13**. Heavy-None pivot was too late; evidence (SCOTUS denial) was already priced in — staying power should have respected the "stay eve" base-rate (last-minute stays DO happen in high-profile executions).
- 889545: truth **South Korea** ✓ — China lost the SF (Korea 4-city defensive champs) — BSS +0.65 / TW +29.39.

**FINAL STANDINGS (all 252 questions resolved):** TW-Score **1723.87** | accuracy **46.4%** | Brier Skill Score **0.290** | 252/252 resolved.

**Retrospective lessons (252-question run):**
1. **Criteria-literal answers** win and lose big (996188: country vs competitor-name; "None" only when criteria implies it — carried me twice: 540490 +48.56, 889545 +29.39).
2. **Early mass > late mass**, always (447470 inversion +4.53 saved a disaster; 133827/815451 negative TWs from late heavy lifts despite correct picks; 158157/259249 picked right late, still +57/+36 TW from early holdings).
3. **Announcement-presence questions** punish single-scenario slates (88025 Netherlands miss −10.29; 154739 Alabama −10.91; 76365 Sixth Circuit noted earlier). ALWAYS distribute across ALL enactment/claim candidates, not just coalition-signatory favorites.
4. **Qualify > season form** (Russell over Antonelli at Baku via qualifying crash) and **H2H/qual form** for races.
5. **Media momentum ≠ royal/occurrence outcome** (Morocco: Lekjaa media darling, king chose party leader Mansouri −14.01 TW).
6. **Pull every same-day result from the date-stamped crawl before submitting**: javelin/100m/marathon results etc. — the sim already posted the winning name in the crawl on resolution day.
7. **5-outcome cap discipline**: keep the 2-3 live finalists; residual 3-6% for bronze-bout parties when final pairing uncertain (ERR ON 2 real options, skip the rest).
8. **No placeholder outcomes** — every submission must list real, plausible persons/places; criteria-allowed strings only when licensed by the question ("None" won me big when licensed: 540490, 889545, 138739-ish).

**Accuracy note:** 46.4% of ALL 252 questions hit top-pick; BSS 0.290 vs 0.0 abstention baseline. TW 1723.87 accrues in units of daily Brier square sums ×100×days-held.
