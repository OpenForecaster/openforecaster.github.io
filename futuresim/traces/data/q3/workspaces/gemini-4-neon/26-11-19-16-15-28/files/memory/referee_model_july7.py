# Quantitative Bayesian Model for Q524604: 2026 FIFA World Cup Final Referee
# Updated July 7, 2026 — All 8 QF teams locked!

# Finalist probabilities (from July 7 WC bracket):
# Top half (SF1): France 0.44, Spain 0.39, Morocco 0.09, Belgium 0.08
# Bottom half (SF2): Argentina 0.41, England 0.32, Norway 0.15, Switzerland 0.12

top = {"France": 0.44, "Spain": 0.39, "Morocco": 0.09, "Belgium": 0.08}
bot = {"Argentina": 0.41, "England": 0.32, "Norway": 0.15, "Switzerland": 0.12}

confed = {
    "France": "UEFA", "Spain": "UEFA", "Morocco": "CAF", "Belgium": "UEFA",
    "Argentina": "CONMEBOL", "England": "UEFA", "Norway": "UEFA", "Switzerland": "UEFA"
}

# Candidate pool of realistic Final referees (weighted by pedigree, age, Collina trust, 2026 signals):
# Fields: (name, country, confed, base_quality, r16_qf_signal, same_confed_penalty_if_interconfed, home_or_birth_conflict_countries)
candidates = [
    # CONCACAF (neutral in 100% of UEFA/CONMEBOL/CAF finals! USA & Mexico ELIMINATED!)
    ("Ismail Elfath", "USA", "CONCACAF", 1.30, 1.15, 1.0, ["Morocco"]),  # 2022 Final 4th off, R16 NOR-BRA (minor VAR overturn), born in Casablanca
    ("César Arturo Ramos", "Mexico", "CONCACAF", 1.25, 1.00, 1.0, []),  # 2022 SF FRA-MAR, age 42, zero conflict
    ("Iván Barton", "El Salvador", "CONCACAF", 0.55, 1.00, 1.0, []),
    ("Drew Fischer", "Canada", "CONCACAF", 0.40, 1.00, 1.0, []),

    # UEFA Neutrals (countries eliminated! Eligible in UEFA-UEFA and historically preferred in UEFA-CONMEBOL too!)
    ("Slavko Vinčić", "Slovenia", "UEFA", 1.45, 1.00, 0.85, []),         # 2024 UCL Final, Euro 2024 SF, Collina elite tier
    ("István Kovács", "Romania", "UEFA", 1.50, 0.78, 0.85, []),          # 2025 UCL Final, age 41; slight discount for 2-wk gap w/o R32/R16/QF1 (though Tello had same pattern!)
    ("Danny Makkelie", "Netherlands", "UEFA", 0.95, 1.00, 0.85, []),     # Age 43, NED eliminated
    ("Szymon Marciniak", "Poland", "UEFA", 0.45, 1.00, 0.85, []),        # 2022 Final ref -> huge repeat-ref penalty (0 repeats in 96 yrs)
    ("Glenn Nyberg", "Sweden", "UEFA", 0.75, 1.05, 0.85, []),            # Did R32 ESP-AUT cleanly, age 37
    ("Felix Zwayer", "Germany", "UEFA", 0.65, 1.00, 0.85, []),           # Euro 2024 SF, age 45, match-fixing baggage
    ("Maurizio Mariani", "Italy", "UEFA", 0.60, 1.00, 0.85, []),         # Age 44
    ("João Pinheiro", "Portugal", "UEFA", 0.55, 1.00, 0.85, []),         # POR eliminated

    # UEFA Active Countries (disqualified when country reaches Final, discounted if in SF/3P!)
    ("Clément Turpin", "France", "UEFA", 1.40, 1.00, 0.85, ["France"]),          # 2022 UCL Final, FRA ~44% Final!
    ("Michael Oliver", "England", "UEFA", 1.15, 1.18, 0.85, ["England"]),        # Did R16 MAR-CAN! ENG ~32% Final
    ("Anthony Taylor", "England", "UEFA", 1.15, 1.22, 0.85, ["England"]),        # Did R16 ESP-POR! ENG ~32% Final
    ("François Letexier", "France", "UEFA", 1.25, 0.60, 0.85, ["France"]),       # Euro 2024 Final, BUT VAR controversy in R16 ARG-EGY + FRA 44% Final
    ("Espen Eskås", "Norway", "UEFA", 0.55, 0.70, 0.85, ["Norway"]),             # Controversy in POR-CRO + NOR alive
    ("Sandro Schärer", "Switzerland", "UEFA", 0.65, 1.00, 0.85, ["Switzerland"]),
    ("Alejandro Hernández Hernández", "Spain", "UEFA", 0.50, 1.00, 0.85, ["Spain"]),

    # CONMEBOL (eligible in UEFA-UEFA 55%, heavily penalized/excluded in ARG finals 41%!)
    ("Facundo Tello", "Argentina", "CONMEBOL", 1.10, 1.35, 0.05, ["Argentina"]), # JUST APPOINTED QF1 FRA-MAR!! Huge Collina trust!
    ("Jesús Valenzuela", "Venezuela", "CONMEBOL", 0.90, 1.00, 0.20, []),         # Age 42, zero country conflict
    ("Wilton Sampaio", "Brazil", "CONMEBOL", 0.90, 1.00, 0.20, []),              # 2022 QF ENG-FRA, BRA eliminated
    ("Darío Herrera", "Argentina", "CONMEBOL", 0.65, 1.10, 0.05, ["Argentina"]), # 4th official QF1 FRA-MAR
    ("Raphael Claus", "Brazil", "CONMEBOL", 0.75, 0.15, 0.20, []),               # Trump attacked him over Balogun red -> zero chance in NJ Final!
    ("Other_CONMEBOL", "Other", "CONMEBOL", 0.80, 1.00, 0.20, []),

    # AFC / CAF / OFC
    ("Alireza Faghani", "Australia", "AFC", 0.75, 1.05, 1.0, []),                # Did R16 ENG-MEX (Azteca!), neutral 100%, but age 48 & 2 VAR overturns
    ("Abdulrahman Al-Jassim", "Qatar", "AFC", 0.45, 1.00, 1.0, []),              # 2022 3rd place ref
    ("Other_AFC_CAF_OFC", "Other", "AFC", 1.10, 1.00, 1.0, []),
]

probs = {c[0]: 0.0 for c in candidates}

for t1, p1 in top.items():
    for t2, p2 in bot.items():
        p_match = p1 * p2
        c1, c2 = confed[t1], confed[t2]
        weights = {}
        for name, country, rconf, base_q, sig, inter_pen, conflicts in candidates:
            if t1 in conflicts or t2 in conflicts:
                continue
            w = base_q * sig
            # If Final is inter-confederation (e.g., UEFA vs CONMEBOL), apply confederation bias
            if c1 != c2:
                if rconf in (c1, c2):
                    w *= inter_pen
                else:
                    # Strictly neutral confederation (CONCACAF, AFC, or CONMEBOL in UEFA-CAF) gets boost
                    w *= 1.15
            else:
                # UEFA vs UEFA final (55%): UEFA neutral refs & CONMEBOL/CONCACAF all strong
                if rconf == "UEFA":
                    w *= 1.10
                elif rconf == "CONMEBOL":
                    w *= 1.15  # like Pitana 2018!
                elif rconf == "CONCACAF":
                    w *= 1.05
            # Slight discount if France is in SF/3P (76% of time) even when France misses final (for Turpin/Letexier)
            if country == "France" and t1 != "France":
                w *= 0.85
            if country == "Argentina" and t2 != "Argentina":
                w *= 0.90
            weights[name] = w
        tot = sum(weights.values())
        for name, w in weights.items():
            probs[name] += p_match * (w / tot)

print("Q524604 BAYESIAN REFEREE RANKING (July 7, 2026):")
for name, p in sorted(probs.items(), key=lambda x: -x[1])[:15]:
    print(f"  {name:28s}: {p:.4f} ({p*100:.2f}%)")
print(f"Top 5 sum: {sum(p for _, p in sorted(probs.items(), key=lambda x: -x[1])[:5]):.4f}")
