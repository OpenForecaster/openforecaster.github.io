# Quantitative Bayesian Model for Q524604: 2026 FIFA World Cup Final Referee
# Updated July 13, 2026 — POST OFFICIAL FIFA 13-MAN CUT & POST BOTH SF APPOINTMENTS
#
# Verified hard July 13, 2026 evidence:
# 1. FIFA officially cut the referee pool to EXACTLY 13 retained referees (confirmed by
#    Mundo Deportivo / Ramon Fuentes, Eurosport.ro / GSP, Law 5):
#      - UEFA (6): Slavko Vincic (SLO), Szymon Marciniak (POL), Maurizio Mariani (ITA),
#                  Glenn Nyberg (SWE), Joao Pinheiro (POR), Espen Eskas (NOR)
#      - CONCACAF (2): Ivan Barton (SLV), Ismail Elfath (USA)
#      - AFC (2): Alireza Faghani (AUS), Adham Makhadmeh (JOR)
#      - CAF (1): Jalal Jayed (MAR)
#      - CONMEBOL (2): Wilton Sampaio (BRA), Jesus Valenzuela (VEN)
#    -> Sent home (0.00%): Cesar Arturo Ramos (MEX), Danny Makkelie (NED), Istvan Kovacs (ROU),
#       Facundo Tello (ARG), Dario Herrera (ARG), Clement Turpin (FRA), Francois Letexier (FRA),
#       Michael Oliver (ENG), Anthony Taylor (ENG), Sandro Scharer (SUI), Felix Zwayer (GER), etc.
# 2. BOTH Semifinal appointments officially confirmed:
#      - SF1 (Jul 14, FRA-ESP, Dallas): Center = Ivan Barton (SLV), 4th = Glenn Nyberg (SWE),
#        VAR = Tomasz Kwiatkowski (POL)
#      - SF2 (Jul 15, ENG-ARG, Atlanta): Center = Ismail Elfath (USA), 4th = Maurizio Mariani (ITA)
#    -> BOTH CONCACAF retained refs are consumed by SF1 & SF2 -> ~0% for the Final!
#    -> Only 11 non-SF-center retained refs remain (9 completely unused in SFs + 2 SF 4th officials).
#    -> 0 of the last 5 World Cup Final refs (2006-2022) served as an SF 4th official
#       (live SF injury substitute risk -> heavy structural discount for Mariani & Nyberg).

top = {"France": 0.568, "Spain": 0.432}
bot = {"England": 0.540, "Argentina": 0.460}
confed = {"France": "UEFA", "Spain": "UEFA", "England": "UEFA", "Argentina": "CONMEBOL"}

def eval_model(label, cfg):
    refs = [
        ("Slavko Vinčić",     "Slovenia",   "UEFA",     cfg["vincic"],     "UNUSED"),
        ("Alireza Faghani",   "Australia",  "AFC",      cfg["faghani"],    "UNUSED"),
        ("Szymon Marciniak",  "Poland",     "UEFA",     cfg["marciniak"],  "UNUSED"),
        ("Jesús Valenzuela",  "Venezuela",  "CONMEBOL", cfg["valenzuela"], "UNUSED"),
        ("Wilton Sampaio",    "Brazil",     "CONMEBOL", cfg["sampaio"],    "UNUSED"),
        ("Maurizio Mariani",  "Italy",      "UEFA",     cfg["mariani"],    "SF_4TH"),
        ("João Pinheiro",     "Portugal",   "UEFA",     cfg["pinheiro"],   "UNUSED"),
        ("Espen Eskås",       "Norway",     "UEFA",     cfg["eskas"],      "UNUSED"),
        ("Adham Makhadmeh",   "Jordan",     "AFC",      cfg["makhadmeh"],  "UNUSED"),
        ("Jalal Jayed",       "Morocco",    "CAF",      cfg["jayed"],      "UNUSED"),
        ("Glenn Nyberg",      "Sweden",     "UEFA",     cfg["nyberg"],     "SF_4TH"),
        ("Ismail Elfath",     "USA",        "CONCACAF", 1.80,              "SF_CTR"),
        ("Iván Barton",       "El Salvador","CONCACAF", 1.10,              "SF_CTR"),
    ]
    probs = {r[0]: 0.0 for r in refs}
    by_type = {"UEFA-UEFA": {r[0]: 0.0 for r in refs}, "UEFA-CONM": {r[0]: 0.0 for r in refs}}
    for t1, p1 in top.items():
        for t2, p2 in bot.items():
            pm = p1 * p2
            mtype = "UEFA-UEFA" if confed[t1] == confed[t2] else "UEFA-CONM"
            w = {}
            for rname, country, rconf, base, role in refs:
                val = base
                if role == "SF_CTR":
                    val *= 0.004
                elif role == "SF_4TH":
                    val *= cfg["sf4_mult"]

                if mtype == "UEFA-CONM":
                    if rconf == "UEFA": val *= cfg["u_in_uc"]
                    elif rconf == "CONMEBOL": val *= cfg["c_in_uc"]
                    else: val *= cfg["n_in_uc"]
                else:
                    if rconf == "UEFA": val *= cfg["u_in_uu"]
                    elif rconf == "CONMEBOL": val *= cfg["c_in_uu"]
                    else: val *= cfg["n_in_uu"]

                if rname == "Szymon Marciniak":
                    if t1 == "France" and t2 == "Argentina": val *= 0.35
                    elif t2 == "Argentina": val *= 0.70
                if rname == "João Pinheiro" and t2 == "Argentina":
                    val *= 0.25
                if rname == "Wilton Sampaio":
                    if t1 == "France" and t2 == "England": val *= 0.72
                    elif t2 == "England": val *= 0.90
                    if t2 == "Argentina": val *= 0.25
                if rname == "Glenn Nyberg" and t2 == "England":
                    val *= 0.70
                if rname == "Espen Eskås" and t2 == "England":
                    val *= 0.65
                if rname == "Jalal Jayed" and t1 == "France":
                    val *= 0.65
                if rname == "Alireza Faghani" and t2 == "England":
                    val *= 0.95

                w[rname] = val
            tot = sum(w.values())
            for rname, val in w.items():
                p = pm * (val / tot)
                probs[rname] += p
                by_type[mtype][rname] += p
    return probs, by_type

if __name__ == "__main__":
    mA, _ = eval_model("A", dict(
        vincic=1.90, faghani=1.50, marciniak=1.15, valenzuela=1.15, sampaio=1.20,
        mariani=1.25, pinheiro=0.80, eskas=0.45, makhadmeh=0.35, jayed=0.30, nyberg=0.85,
        sf4_mult=0.28, u_in_uc=0.92, c_in_uc=0.04, n_in_uc=1.32, u_in_uu=0.92, c_in_uu=1.30, n_in_uu=1.12
    ))
    mB, _ = eval_model("B", dict(
        vincic=2.05, faghani=1.30, marciniak=1.25, valenzuela=1.15, sampaio=1.20,
        mariani=1.25, pinheiro=0.80, eskas=0.45, makhadmeh=0.28, jayed=0.25, nyberg=0.85,
        sf4_mult=0.22, u_in_uc=1.10, c_in_uc=0.03, n_in_uc=1.05, u_in_uu=0.95, c_in_uu=1.35, n_in_uu=0.95
    ))
    mC, _ = eval_model("C", dict(
        vincic=1.75, faghani=1.75, marciniak=1.15, valenzuela=1.15, sampaio=1.20,
        mariani=1.20, pinheiro=0.70, eskas=0.42, makhadmeh=0.38, jayed=0.33, nyberg=0.80,
        sf4_mult=0.28, u_in_uc=0.75, c_in_uc=0.03, n_in_uc=1.55, u_in_uu=0.82, c_in_uu=1.30, n_in_uu=1.25
    ))
    mD, _ = eval_model("D", dict(
        vincic=1.85, faghani=1.45, marciniak=1.10, valenzuela=1.10, sampaio=1.15,
        mariani=1.45, pinheiro=0.75, eskas=0.42, makhadmeh=0.33, jayed=0.28, nyberg=0.85,
        sf4_mult=0.50, u_in_uc=0.92, c_in_uc=0.04, n_in_uc=1.30, u_in_uu=0.92, c_in_uu=1.25, n_in_uu=1.10
    ))
    ens = {k: 0.35*mA[k] + 0.30*mB[k] + 0.25*mC[k] + 0.10*mD[k] for k in mA}
    print("Q524604 JULY 13 ENSEMBLE:")
    for rname, p in sorted(ens.items(), key=lambda x: -x[1]):
        print(f"  {rname:20s}: {p:.4f} ({p*100:5.2f}%)")
