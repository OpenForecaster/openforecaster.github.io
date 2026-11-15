# Batch 01 notes: World Cup 2026 + Nations League 2026-27 (sim date 2026-06-24)

Searches used: 13 of 46. Simulation script: /tmp/b01_wc_scripts/sim.py (Elo-style ratings, Poisson goals, K=0.0025, host bonus USA/MEX +50, CAN +25; FIFA H2H-first group tiebreaks; random valid third-place matching). It may be wiped, so rebuild from these notes if needed.

## WC bracket (checked against Al Jazeera's Jun 24 path analysis)
R32: M73 A2vB2 (LA Jun 28); M74 E1v3[ABCDF] (Boston); M75 F1vC2 (Monterrey); M76 C1vF2 (Houston); M77 I1v3[CDFGH] (NJ); M78 E2vI2 (Dallas); M79 A1v3[CEFHI] (Mexico City); M80 L1v3[EHIJK] (Atlanta); M81 D1v3[BEFIJ] (SF Bay); M82 G1v3[AEHIJ] (Seattle); M83 K2vL2 (Toronto); M84 H1vJ2 (LA); M85 B1v3[EFGIJ] (Vancouver); M86 J1vH2 (Miami); M87 K1v3[DEIJL] (KC); M88 D2vG2 (Dallas).
R16: 89=W74vW77, 90=W73vW75, 91=W76vW78, 92=W79vW80, 93=W83vW84, 94=W81vW82, 95=W86vW88, 96=W85vW87.
QF: 97 Boston Jul 9 (W89vW90); 98 LA Jul 10 (W93vW94); 99 Miami Jul 11 (W91vW92); 100 KC Jul 11 (W95vW96). SF 101 Dallas Jul 14 (W97vW98); SF 102 Atlanta Jul 15 (W99vW100).
Spain (H1) and France (I1) are in the SF101 half. Argentina (J1), England (L1), Mexico (A1) and C1 (Brazil?) are in the SF102 half.

## Standings after MD2 (results)
- A: MEX 2-0 RSA, KOR 2-1 CZE, MEX 1-0 KOR, CZE 1-1 RSA. MEX 6 (won the group), KOR 3, CZE 1, RSA 1. MD3 Jun 24: CZE v MEX, RSA v KOR.
- B (FINAL): SUI 7 (1st), CAN 4 (+5, 2nd), BIH 4 (3rd, very likely through), QAT 1. Switzerland beat Canada 2-1 on Jun 24 (Vargas, Manzambi).
- C: BRA 1-1 MAR, SCO 1-0 HAI, MAR 1-0 SCO, BRA 3-0 HAI. BRA 4 (+3), MAR 4 (+1), SCO 3, HAI 0. Opta gives Brazil 63.7% to top. MD3 Jun 24: SCO v BRA, MAR v HAI.
- D: USA 6 (already won the group), AUS 3, PAR 3, TUR 0 (out). A draw is enough for Australia v Paraguay.
- E: GER 6 (guaranteed 1st), CIV 3 (82.7% to finish 2nd), ECU 1, CUW 1.
- F: NED 4 (GF7), JPN 4 (GF6), SWE 3, TUN 0. MD3 Jun 25: JPN v SWE, TUN v NED.
- G: EGY 4, IRN 2, BEL 2, NZL 1 (BEL 1-1 EGY, IRN 2-2 NZL, EGY 3-1 NZL, IRN 0-0 BEL). Belgium top in only 26.6% (Opta).
- H: ESP 4, URU 2, CPV 2, KSA 1. Spain top 85% (Opta). If Uruguay beat Spain, Spain go to H2 and meet Argentina in R32.
- I: FRA 6 (+5), NOR 6 (+4). A draw on Jun 26 (Boston) is enough for France to top the group.
- J: ARG 6 (already won the group), AUT 3, ALG 3, JOR 0.
- K: COL 6, POR 4, COD 1, UZB 0. Jun 27 COL v POR: a Portugal win makes Portugal K1. K1 goes to the KC QF path; K2 goes to the LA QF path (vs Spain in R16).
- L: ENG 4 (+2), GHA 4 (+1), CRO 3, PAN 0 (out). England are 81.7% to top (Opta).

## Odds and models
- Outright odds Jun 23 (Metro/bet365/BetOnline): FRA 4/1, ESP 5/1-6/1, ENG 13/2, ARG 13/2, POR 10/1-12/1, GER 14/1, BRA 12/1-16/1, NED 16/1, USA 30/1, NOR 33/1, JPN 40/1.
- Opta after MD2: ARG 15.46%, FRA 15.06%, ESP 12.48%, ENG 12.28%, then POR, GER, NOR, BRA, NED, USA/COL.
- Opta for Germany (Jun 22): SF 24.3%, win 7.3%. Opta for USA (Jun 21): QF 47.5%, SF 22.4%, win 4.7%.
- Market Jun 23: Argentina to reach the SF at 6/5 (45%). Models put it at about 62%.
- My sim: QF97 FRA .40, GER .21, NED .13, BRA .06, MAR .05. QF100 ARG .57, POR .13, COL .07, SUI .07, BEL .05. SF101 ESP .27, FRA .26, GER .10. SF102 ARG .36, ENG .21. Winner ARG .205, FRA .187, ESP .177, ENG .128, POR .064.
- Golden Boot: Messi 5, Mbappe 4, Haaland 4, David 3, Undav 3; 18 players on 2 (Kane, Ronaldo, Vinicius, Oyarzabal...).
  - Sky Bet Jun 23: Mbappe 6/4, Messi 13/8, Haaland 5/1, Kane 6/1, Oyarzabal 22/1, Undav 25/1, Yamal/Vinicius 33/1, Ronaldo 40/1.
  - My sim gives Messi .58 and Mbappe .20, but it rates favourites high and ignores rest/minutes, so I blended it with the market.
- Golden Ball: Kalshi Jun 17 had Messi 25%, Mbappe 23%, Kane 8%. 1xBet Jun 19: Mbappe 6.0, Messi 7.0, Olise 7.0, Kane 9.0, Yamal 11, Vinicius 17.

## Final referee
- FIFA picked 52 referees on Apr 9.
- Superbet odds (Jun 12): Marciniak 7.5, Letexier 8, Kovacs 12, Makkelie 12, Vincic 12, Turpin 13, Oliver 13, Tello 13.
- Faghani (Australia) refereed both the opening match and the final of the 2025 Club World Cup (final at MetLife).
- Nationality conflicts: FRA (Letexier, Turpin), ENG (Oliver, Taylor), ARG (Tello, Herrera, Falcon), BRA (Sampaio, Claus, Abatti), NED (Makkelie), ESP (Hernandez), POR (Pinheiro), GER (Zwayer).
- No referee has ever done two World Cup finals, which counts against Marciniak.
- Watch QF/SF appointments (Jul 9-15) and the FIFA announcement around Jul 16.

## Nations League 2026-27 (UEFA draw Feb 12; fixtures confirmed)
- Group A1: France, Italy, Belgium, Turkiye. Sep 25: Italy v Belgium, Turkiye v France. Sep 28: Belgium v France, Turkiye v Italy. Oct 2: Belgium v Turkiye, France v Italy. My sim of the leader after Sep 28: FRA .49, ITA .21, TUR .17, BEL .12.
- Group A3: Spain, Croatia, England, Czechia. **England v Spain is Sat Sep 26, Wembley, 19:45 BST.** The question says Sep 19, which is wrong. Then Czechia v England Sep 29, Spain v Croatia Sep 29.
- Group A4: Portugal, Denmark, Norway, Wales. **Portugal v Wales Thu Sep 24, Estadio da Luz**, then Norway v Portugal Sep 27, Denmark v Portugal Oct 1, Portugal v Norway Oct 4.
- Group B3: Israel, Austria, Republic of Ireland, Kosovo. Kosovo v Ireland Sep 24; **Israel v Republic of Ireland Sun Sep 27** (Israel home, venue TBD, Israel hopes for Tel Aviv). Ireland v Israel Oct 4 has been moved to a neutral venue behind closed doors (FAI, Jun 12).
- Rating-model match odds: England v Spain .43/.27/.31; Israel v Ireland .33/.27/.40; Portugal v Wales .82/.12/.06 (submitted .72/.18/.10 after shading).
