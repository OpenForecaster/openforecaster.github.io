# Quantitative Bayesian Model for Q524604: 2026 FIFA World Cup Final Referee
# Updated July 15, 2026 — POST SF2 (ARGENTINA 2-1 ENGLAND, ISMAIL ELFATH / MAURIZIO MARIANI)
# FINAL 100% LOCKED: SPAIN (UEFA) vs ARGENTINA (CONMEBOL) on Sunday July 19, MetLife Stadium!
#
# Verified hard July 15, 2026 evidence:
# 1. FINAL MATCHUP 100% LOCKED = SPAIN (UEFA) vs ARGENTINA (CONMEBOL):
#    - CONMEBOL referees (Jesús Valenzuela [VEN], Wilton Sampaio [BRA]) are CRUSHED for the Final!
#      Zero CONMEBOL refs have been appointed to a UEFA-CONMEBOL World Cup Final since 1986 (0/6:
#      1990 CONCACAF, 1994 UEFA, 1998 CAF, 2002 UEFA, 2014 UEFA, 2022 UEFA). Valenzuela becomes
#      the heavy favorite for Saturday's all-UEFA 3rd-place playoff (France vs England); Sampaio
#      is Brazilian (Argentina's fiercest rival) -> virtually 0% for Final!
#    - CONCACAF referees (Iván Barton [SLV] = SF1, Ismail Elfath [USA] = SF2) are BOTH consumed
#      by the semifinals -> ~0% for the Final!
# 2. ALIREZA FAGHANI (Australia / AFC) — MASSIVE STRUCTURAL SURGE TO CLEAR #1:
#    - Sole elite strictly neutral (non-UEFA, non-CONMEBOL) referee remaining in the 13-man pool!
#    - England's elimination REMOVES Thomas Tuchel's post-ENG-MEX criticism drag (was 0.84x in 53%
#      of Finals yesterday -> now 1.00x, zero friction with Spain or Argentina!).
#    - Collina's hand-picked 2025 FIFA Club World Cup Final referee at MetLife Stadium (exact same
#      venue!), already did 2018 WC 3rd-place playoff, rested/protected since R16 ENG-MEX (Jul 5/6).
#    - Explicitly flagged by The Mirror (Jul 14) as surging due to FIFA's strict inter-confederation
#      neutrality preference once Barton & Elfath took both semifinals.
# 3. SLAVKO VINČIĆ (Slovenia / UEFA) — STRONG #2:
#    - Undisputed #1 unused UEFA referee on pedigree (2024 UCL Final, 2022 UEL Final, Euro 2024 SF
#      Spain 2-1 France, spotless WC 2026, zero Spain/Argentina controversy).
#    - UEFA referees have been appointed to 4 of the last 5 UEFA-CONMEBOL Finals (1994 Puhl,
#      2002 Collina, 2014 Rizzoli GER-ARG, 2022 Marciniak ARG-FRA) — including BOTH modern
#      Argentina Finals! Collina retained 6 UEFA refs in the final 13.
# 4. SZYMON MARCINIAK (Poland / UEFA) — #3:
#    - Retained in final 13 (with Polish VAR Kwiatkowski working SF1), flagged by Mundo Deportivo.
#    - Tempered by 3 real drags for Spain-Argentina: (a) 0/22 repeat WC Final referee precedent;
#      (b) ALREADY refereed Argentina's 2022 Final win; (c) July 14 AFP "'VAR-gentina?'" viral storm
#      highlighting his missed red card on Messi vs Algeria (official Algerian FA complaint).
# 5. REMAINING DARK HORSES FOR SLOTS #4 & #5:
#    - Adham Makhadmeh (Jordan / AFC, UNUSED): Strictly neutral confederation, zero conflict,
#      top backup if Collina insists on non-UEFA/CONMEBOL neutrality and passes on 48yo Faghani.
#    - Espen Eskås (Norway / UEFA, UNUSED): England's exit removes Norway-England QF drag;
#      2024 Olympic Gold Medal Final ref (note: Spain 5-3 France), mild Croatia-Portugal R32 chip noise.
#    - Jalal Jayed (Morocco / CAF, UNUSED): Sole CAF ref retained (cf. 1998 Belqola MAR in BRA-FRA!),
#      mildly tempered by Morocco being Spain's direct neighbor & 2030 co-host + lower final pedigree.
#    - Maurizio Mariani (Italy / UEFA, SF2 4th official): Collina protégé, BUT served as SF2 4th
#      official (ARG-ENG Jul 15) — 0 of last 5 WC Final refs were SF 4th officials!
#    - Glenn Nyberg (Sweden / UEFA, SF1 4th official): SF1 4th official (ESP-FRA) + reffed ESP-AUT.
#    - João Pinheiro (Portugal / UEFA, UNUSED): Iberian neighbor knocked out by Spain in R16 +
#      ARG-SUI QF4 Embolo VAR storm & viral Messi clash -> virtually eliminated!

def eval_model(label, cfg):
    refs = [
        ("Alireza Faghani",   "Australia",  "AFC",      cfg["faghani"],    "UNUSED"),
        ("Slavko Vinčić",     "Slovenia",   "UEFA",     cfg["vincic"],     "UNUSED"),
        ("Szymon Marciniak",  "Poland",     "UEFA",     cfg["marciniak"],  "UNUSED"),
        ("Adham Makhadmeh",   "Jordan",     "AFC",      cfg["makhadmeh"],  "UNUSED"),
        ("Espen Eskås",       "Norway",     "UEFA",     cfg["eskas"],      "UNUSED"),
        ("Jalal Jayed",       "Morocco",    "CAF",      cfg["jayed"],      "UNUSED"),
        ("Maurizio Mariani",  "Italy",      "UEFA",     cfg["mariani"],    "SF_4TH"),
        ("Glenn Nyberg",      "Sweden",     "UEFA",     cfg["nyberg"],     "SF_4TH"),
        ("Jesús Valenzuela",  "Venezuela",  "CONMEBOL", cfg["valenzuela"], "UNUSED"),
        ("João Pinheiro",     "Portugal",   "UEFA",     cfg["pinheiro"],   "UNUSED"),
        ("Wilton Sampaio",    "Brazil",     "CONMEBOL", cfg["sampaio"],    "UNUSED"),
        ("Ismail Elfath",     "USA",        "CONCACAF", 1.80,              "SF_CTR"),
        ("Iván Barton",       "El Salvador","CONCACAF", 1.10,              "SF_CTR"),
    ]
    w = {}
    for rname, country, rconf, base, role in refs:
        val = base
        if role == "SF_CTR":
            val *= 0.002
        elif role == "SF_4TH":
            val *= cfg["sf4_mult"]

        # 100% UEFA (Spain) vs CONMEBOL (Argentina) Final:
        if rconf == "UEFA":
            val *= cfg["u_in_uc"]
        elif rconf == "CONMEBOL":
            val *= cfg["c_in_uc"]
        else:  # AFC / CAF / CONCACAF (strictly neutral)
            val *= cfg["n_in_uc"]

        # Specific Spain-Argentina matchup adjustments:
        if rname == "Szymon Marciniak":
            # 2022 ARG Final repeat + Algeria missed Messi red card ('VAR-gentina' Jul 14 AFP)
            val *= cfg["marc_arg"]
        if rname == "João Pinheiro":
            # Portugal = Spain Iberian neighbor knocked out in R16 + ARG-SUI Messi clash/Embolo VAR
            val *= 0.05
        if rname == "Wilton Sampaio":
            # Brazil-Argentina rivalry on top of CONMEBOL
            val *= 0.15
        if rname == "Jalal Jayed":
            # Spain-Morocco Strait of Gibraltar neighbor / 2030 co-host mild optics factor
            val *= cfg["jayed_esp"]
        if rname == "Espen Eskås":
            # Mild Croatia-Portugal R32 noise + reffed 2024 Olympic Final Spain 5-3 France
            val *= cfg["eskas_adj"]
        if rname == "Glenn Nyberg":
            # Worked Spain-France SF1 as 4th official + Spain-Austria R32
            val *= 0.72
        if rname == "Maurizio Mariani":
            # Worked Argentina-England SF2 as 4th official
            val *= 0.90

        w[rname] = val

    tot = sum(w.values())
    return {rn: v / tot for rn, v in w.items()}

if __name__ == "__main__":
    # Model A (35%): Balanced (Faghani neutral edge vs Vincic UEFA pedigree)
    mA = eval_model("A (Balanced)", dict(
        faghani=1.70, vincic=1.95, marciniak=1.10, makhadmeh=0.36, eskas=0.48,
        jayed=0.33, mariani=1.25, nyberg=0.85, valenzuela=1.20, pinheiro=0.80, sampaio=1.20,
        sf4_mult=0.26, u_in_uc=0.92, c_in_uc=0.04, n_in_uc=1.35,
        marc_arg=0.58, jayed_esp=0.90, eskas_adj=0.95
    ))
    # Model B (30%): UEFA Pedigree / Collina-UEFA Historical Precedent (1994/2002/2014/2022 -> Vincic!)
    mB = eval_model("B (UEFA Pedigree / Vincic)", dict(
        faghani=1.45, vincic=2.12, marciniak=1.20, makhadmeh=0.28, eskas=0.50,
        jayed=0.26, mariani=1.25, nyberg=0.85, valenzuela=1.20, pinheiro=0.80, sampaio=1.20,
        sf4_mult=0.22, u_in_uc=1.10, c_in_uc=0.03, n_in_uc=1.08,
        marc_arg=0.62, jayed_esp=0.88, eskas_adj=0.95
    ))
    # Model C (25%): Strict Inter-Confederation Neutrality (Mirror Jul 14 / 2025 CWC MetLife -> Faghani!)
    mC = eval_model("C (Strict Neutrality / Faghani)", dict(
        faghani=1.95, vincic=1.72, marciniak=1.05, makhadmeh=0.42, eskas=0.45,
        jayed=0.38, mariani=1.20, nyberg=0.80, valenzuela=1.20, pinheiro=0.70, sampaio=1.20,
        sf4_mult=0.26, u_in_uc=0.72, c_in_uc=0.03, n_in_uc=1.60,
        marc_arg=0.55, jayed_esp=0.92, eskas_adj=0.92
    ))
    # Model D (10%): SF4 Eligible / Italian Collina Dark Horse (Mariani / wider uncertainty)
    mD = eval_model("D (SF4 Eligible / Mariani)", dict(
        faghani=1.60, vincic=1.85, marciniak=1.05, makhadmeh=0.34, eskas=0.46,
        jayed=0.30, mariani=1.50, nyberg=0.85, valenzuela=1.15, pinheiro=0.75, sampaio=1.15,
        sf4_mult=0.48, u_in_uc=0.92, c_in_uc=0.04, n_in_uc=1.30,
        marc_arg=0.58, jayed_esp=0.90, eskas_adj=0.95
    ))

    models = [("A_Bal(35%)", mA, 0.35), ("B_UEFA(30%)", mB, 0.30), ("C_Neut(25%)", mC, 0.25), ("D_SF4(10%)", mD, 0.10)]
    ens = {k: sum(w * m[k] for _, m, w in models) for k in mA}

    print("=== Q524604 JULY 15 POST-SF2 ENSEMBLE (100% SPAIN vs ARGENTINA) ===")
    for rname, p in sorted(ens.items(), key=lambda x: -x[1]):
        breakdown = " | ".join(f"{lbl[:5]}:{m[rname]:.3f}" for lbl, m, _ in models)
        print(f"  {rname:20s}: {p:.4f} ({p*100:5.2f}%)  [{breakdown}]")
    top5 = sorted(ens.items(), key=lambda x: -x[1])[:5]
    print(f"\nTop 5 sum: {sum(p for _, p in top5):.4f} (residual outside Top 5: {1-sum(p for _, p in top5):.4f})")
