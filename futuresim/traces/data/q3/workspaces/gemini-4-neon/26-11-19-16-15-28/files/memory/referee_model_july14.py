# Quantitative Bayesian Model for Q524604: 2026 FIFA World Cup Final Referee
# Updated July 14, 2026 — POST SF1 (SPAIN 2-0 FRANCE, IVAN BARTON / GLENN NYBERG)
#                        + MIRROR JULY 14 REPORT ON FAGHANI / TUCHEL ROW
#                        + STRAITS TIMES JULY 14 'VAR-GENTINA' ARTICLE (MARCINIAK / PINHEIRO)
#
# Verified July 14 updates vs July 13:
# 1. SPAIN (100% locked!) replaces France (56.8%) / Spain (43.2%) as Finalist #1:
#    - Joao Pinheiro (Portugal) is Spain's Iberian neighbor AND Spain knocked Portugal out in R16 ->
#      virtually eliminated (~0.10x multiplier vs Spain, plus ARG-SUI Embolo VAR controversy!).
#    - Szymon Marciniak (Poland): 2022 France-Argentina rematch block is GONE (France out!),
#      so Marciniak is clean for Spain-England, though still faces 0/22 no-repeat norm and
#      July 14 AFP/Straits Times resurfacing his missed Messi red card vs Algeria.
#    - Wilton Sampaio (Brazil): 2022 France-England rematch is GONE (still mild ENG friction 0.88x).
# 2. Alireza Faghani (Australia/AFC):
#    - Mirror (Jul 14) explicitly flags Faghani as surging into prime contention for the Final
#      after CONCACAF refs Barton (SF1) & Elfath (SF2) were used, noting widespread praise for
#      his England-Mexico match (plus Collina's 2025 Club World Cup Final at MetLife Stadium!).
#    - HOWEVER, Mirror ALSO reveals Thomas Tuchel raged against Faghani ("not good enough") after
#      England 3-2 Mexico (Quansah red + 2 pens) -> apply modest ~0.82-0.88 England friction
#      (Collina backs his refs vs manager complaints, e.g. Egypt, so NOT a disqualifier, just drag).
# 3. SF2 probabilities updated slightly to ENG 53.3% / ARG 46.7% (UEFA-UEFA 53.3% / UEFA-CONM 46.7%).

top = {"Spain": 1.000}
bot = {"England": 0.533, "Argentina": 0.467}
confed = {"Spain": "UEFA", "England": "UEFA", "Argentina": "CONMEBOL"}

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
    by_match = {}
    for t1, p1 in top.items():
        for t2, p2 in bot.items():
            pm = p1 * p2
            mtype = "UEFA-UEFA" if confed[t1] == confed[t2] else "UEFA-CONM"
            w = {}
            for rname, country, rconf, base, role in refs:
                val = base
                if role == "SF_CTR":
                    val *= 0.003
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

                # Specific Spain-finalist & July 14 matchup adjustments:
                if rname == "João Pinheiro":
                    # Portugal = Spain's Iberian neighbor + Spain knocked out Portugal in R16!
                    # Plus Embolo VAR controversy in ARG-SUI!
                    val *= (0.08 if t2 == "Argentina" else 0.14)
                if rname == "Szymon Marciniak":
                    # No France-Argentina rematch block anymore! Mild Algeria/Messi noise vs ARG
                    if t2 == "Argentina": val *= 0.65
                if rname == "Wilton Sampaio":
                    if t2 == "England": val *= 0.86   # 2022 ENG-FRA residual
                    if t2 == "Argentina": val *= 0.20 # South American rival
                if rname == "Alireza Faghani":
                    if t2 == "England": val *= cfg["faghani_eng"]  # Tuchel post-MEX friction
                if rname == "Glenn Nyberg" and t2 == "England":
                    val *= 0.72
                if rname == "Espen Eskås" and t2 == "England":
                    val *= 0.65  # Norway knocked out by England in QF!

                w[rname] = val
            tot = sum(w.values())
            by_match[f"{t1}-{t2}"] = {rn: v/tot for rn, v in w.items()}
            for rname, val in w.items():
                probs[rname] += pm * (val / tot)
    return probs, by_match

if __name__ == "__main__":
    mA, bmA = eval_model("A (Balanced)", dict(
        vincic=1.92, faghani=1.60, marciniak=1.12, valenzuela=1.18, sampaio=1.20,
        mariani=1.25, pinheiro=0.80, eskas=0.45, makhadmeh=0.35, jayed=0.30, nyberg=0.85,
        sf4_mult=0.28, faghani_eng=0.84,
        u_in_uc=0.92, c_in_uc=0.04, n_in_uc=1.35, u_in_uu=0.92, c_in_uu=1.30, n_in_uu=1.12
    ))
    mB, _ = eval_model("B (UEFA Pedigree / Vincic)", dict(
        vincic=2.08, faghani=1.35, marciniak=1.22, valenzuela=1.18, sampaio=1.20,
        mariani=1.25, pinheiro=0.80, eskas=0.45, makhadmeh=0.28, jayed=0.25, nyberg=0.85,
        sf4_mult=0.22, faghani_eng=0.78,
        u_in_uc=1.08, c_in_uc=0.03, n_in_uc=1.08, u_in_uu=0.95, c_in_uu=1.35, n_in_uu=0.95
    ))
    mC, _ = eval_model("C (Strict Neutrality / Faghani)", dict(
        vincic=1.75, faghani=1.85, marciniak=1.10, valenzuela=1.18, sampaio=1.20,
        mariani=1.20, pinheiro=0.70, eskas=0.42, makhadmeh=0.38, jayed=0.33, nyberg=0.80,
        sf4_mult=0.28, faghani_eng=0.92,
        u_in_uc=0.75, c_in_uc=0.03, n_in_uc=1.55, u_in_uu=0.82, c_in_uu=1.30, n_in_uu=1.25
    ))
    mD, _ = eval_model("D (SF4 Eligible / Mariani)", dict(
        vincic=1.85, faghani=1.50, marciniak=1.08, valenzuela=1.12, sampaio=1.15,
        mariani=1.45, pinheiro=0.75, eskas=0.42, makhadmeh=0.33, jayed=0.28, nyberg=0.85,
        sf4_mult=0.50, faghani_eng=0.84,
        u_in_uc=0.92, c_in_uc=0.04, n_in_uc=1.30, u_in_uu=0.92, c_in_uu=1.25, n_in_uu=1.10
    ))
    ens = {k: 0.35*mA[k] + 0.30*mB[k] + 0.25*mC[k] + 0.10*mD[k] for k in mA}
    print("Q524604 JULY 14 POST-SF1 ENSEMBLE:")
    for rname, p in sorted(ens.items(), key=lambda x: -x[1]):
        print(f"  {rname:20s}: {p:.4f} ({p*100:5.2f}%)")
    print("\nModel A breakdown by Final matchup:")
    for mk, d in bmA.items():
        top5 = sorted(d.items(), key=lambda x: -x[1])[:6]
        print(f"  {mk:16s}: " + ", ".join(f"{k}:{v:.3f}" for k, v in top5))
