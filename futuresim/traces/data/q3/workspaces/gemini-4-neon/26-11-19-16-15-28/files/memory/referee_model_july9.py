# Quantitative Bayesian Model for Q524604: 2026 FIFA World Cup Final Referee
# Updated July 9, 2026 — Post-QF1 (France 2-0 Morocco) + ALL 4 QF Referees Confirmed!
#
# Key July 9 evidence:
# 1. Morocco ELIMINATED! Top half (SF1) is 100% UEFA: France ~0.633, Spain ~0.315, Belgium ~0.052.
#    Bottom half (SF2): Argentina ~0.420, England ~0.332, Norway ~0.139, Switzerland ~0.109.
#    Final mix: ~58% UEFA-vs-UEFA, ~42% UEFA-vs-CONMEBOL, 0% CAF!
#    -> Ismail Elfath (USA, born Casablanca) is now 100% CONFLICT-FREE in ALL possible finals!
# 2. ALL 4 QF REFEREES CONFIRMED:
#    - QF1 (Jul 9, FRA 2-0 MAR): Facundo Tello (ARG) [4th: Dario Herrera] — clean match, no VAR overturns, 10-day spacing (like Pitana 2018: FRA QF -> FRA Final!)
#    - QF2 (Jul 10, ESP-BEL): Michael Oliver (ENG) [4th: Ramon Abatti] — BUT AS USA Jul 9 confirms Falklands ban (English refs NEVER ref Argentina!) + ENG conflict -> blocked in ~75% of Finals!
#    - QF3 (Jul 11, ENG-NOR): Clement Turpin (FRA) — 4th match, 2025 Best Ref, BUT France now ~63% in Final (blocked) & 37% in 3P!
#    - QF4 (Jul 11, ARG-SUI): Joao Pinheiro (POR) [4th: Drew Fischer] — 100% conflict-free, 8-day spacing (Rizzoli/Elizondo), proves neutral UEFA ref works UEFA-CONMEBOL!
# 3. Istvan Kovacs (ROM) now confirmed 0 R32 + 0 R16 + 0 QF (all 6 modern WC final refs 2002-2022 worked >=1 R16 or QF!).
# 4. Anthony Taylor (ENG) also blocked by BOTH England (~33%) and Argentina (~42% Falklands) -> ~75% excluded!

top = {"France": 0.633, "Spain": 0.315, "Belgium": 0.052}
bot = {"Argentina": 0.420, "England": 0.332, "Norway": 0.139, "Switzerland": 0.109}

confed = {
    "France": "UEFA", "Spain": "UEFA", "Belgium": "UEFA",
    "Argentina": "CONMEBOL", "England": "UEFA", "Norway": "UEFA", "Switzerland": "UEFA"
}

# (name, country, confed, base_quality, july9_signal, same_confed_pen_interconfed, hard_conflicts)
candidates = [
    # CONCACAF (100% strictly neutral in ALL 2026 Finals now that USA, MEX, CAN, MAR are ALL out!)
    ("Ismail Elfath", "USA", "CONCACAF", 1.32, 1.18, 1.0, []),          # 2022 Final 4th off, R16 NOR-BRA, rested through QFs (Marciniak blueprint!), Morocco out -> 0% conflict!
    ("César Arturo Ramos", "Mexico", "CONCACAF", 1.25, 1.05, 1.0, []),  # 2022 WC SF, age 42, rested through QFs, 0% conflict
    ("Iván Barton", "El Salvador", "CONCACAF", 0.50, 1.00, 1.0, []),
    ("Drew Fischer", "Canada", "CONCACAF", 0.42, 1.05, 1.0, []),        # 4th official QF4 ARG-SUI (retained!)

    # UEFA Neutrals (0% country conflict! Pinheiro's ARG-SUI QF proves neutral UEFA viable in UEFA-CONMEBOL: inter_pen=0.88)
    ("Slavko Vinčić", "Slovenia", "UEFA", 1.45, 1.05, 0.88, []),        # 2024 UCL Final, Euro 2024 SF, rested through QFs
    ("João Pinheiro", "Portugal", "UEFA", 0.90, 1.35, 0.88, []),        # SURGING: appointed QF4 ARG-SUI! 8-day spacing, 0% conflict, 1st WC/age 38
    ("István Kovács", "Romania", "UEFA", 1.45, 0.58, 0.88, []),         # 2025 UCL Final, BUT 0 R32 + 0 R16 + 0 QF (24 days cold if straight to Final!)
    ("Danny Makkelie", "Netherlands", "UEFA", 0.95, 1.00, 0.88, []),    # Age 43, NED out, rested through QFs
    ("Glenn Nyberg", "Sweden", "UEFA", 0.78, 1.05, 0.88, []),           # Clean R32 ESP-AUT, age 37
    ("Szymon Marciniak", "Poland", "UEFA", 0.40, 1.00, 0.88, []),       # 2022 Final ref -> huge no-repeat penalty
    ("Maurizio Mariani", "Italy", "UEFA", 0.58, 1.00, 0.88, []),
    ("Felix Zwayer", "Germany", "UEFA", 0.50, 0.85, 0.88, []),          # Cramped up in USA-AUS + baggage

    # UEFA Active Countries (disqualified when country reaches Final; ENG also Falklands-blocked vs ARG!)
    ("Clément Turpin", "France", "UEFA", 1.50, 1.30, 0.88, ["France"]),               # 2025 Best Ref, QF3 ENG-NOR! Blocked 63% (FRA Final), 3P discount in 37%
    ("Michael Oliver", "England", "UEFA", 1.25, 1.32, 0.88, ["England", "Argentina"]),# QF2 ESP-BEL! Blocked 75% (ENG or ARG Final!)
    ("Anthony Taylor", "England", "UEFA", 1.15, 1.18, 0.88, ["England", "Argentina"]),# R16 ESP-POR, rested QFs, BUT blocked 75% (ENG or ARG Final!)
    ("François Letexier", "France", "UEFA", 1.20, 0.50, 0.88, ["France"]),            # EFA complaint + FRA 63% Final
    ("Sandro Schärer", "Switzerland", "UEFA", 0.65, 1.00, 0.88, ["Switzerland"]),
    ("Espen Eskås", "Norway", "UEFA", 0.50, 0.70, 0.88, ["Norway"]),
    ("Alejandro Hernández Hernández", "Spain", "UEFA", 0.45, 1.00, 0.88, ["Spain"]),

    # CONMEBOL (strictly neutral in UEFA-UEFA 58% Finals! Heavily excluded in ARG Finals 42%!)
    ("Facundo Tello", "Argentina", "CONMEBOL", 1.15, 1.40, 0.02, ["Argentina"]),      # Clean QF1 FRA-MAR! Exact Pitana 2018 path (FRA QF -> Final!), 10-day spacing
    ("Jesús Valenzuela", "Venezuela", "CONMEBOL", 0.92, 1.00, 0.15, []),              # Age 42, 0% country conflict
    ("Wilton Sampaio", "Brazil", "CONMEBOL", 0.90, 1.00, 0.15, []),                   # 2022 QF, BRA out
    ("Darío Herrera", "Argentina", "CONMEBOL", 0.65, 1.12, 0.02, ["Argentina"]),      # 4th official QF1
    ("Ramon Abatti", "Brazil", "CONMEBOL", 0.55, 1.08, 0.15, []),                     # 4th official QF2
    ("Raphael Claus", "Brazil", "CONMEBOL", 0.70, 0.12, 0.15, []),                    # Trump controversy over Balogun red -> virtually impossible in NJ Final
    ("Other_CONMEBOL", "Other", "CONMEBOL", 0.65, 1.00, 0.15, []),

    # AFC / CAF / OFC
    ("Alireza Faghani", "Australia", "AFC", 0.78, 1.05, 1.0, []),                     # R16 ENG-MEX, 100% neutral, age 48
    ("Abdulrahman Al-Jassim", "Qatar", "AFC", 0.45, 1.00, 1.0, []),
    ("Other_AFC_CAF_OFC", "Other", "AFC", 0.95, 1.00, 1.0, []),
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
            if c1 != c2:
                if rconf in (c1, c2):
                    w *= inter_pen
                else:
                    w *= 1.18  # strictly neutral confederation boost (CONCACAF/AFC)
            else:
                if rconf == "UEFA":
                    w *= 1.08
                elif rconf == "CONMEBOL":
                    w *= 1.16  # Pitana 2018 precedent
                elif rconf == "CONCACAF":
                    w *= 1.08
            # Country-in-SF/3P historical discount (France is 100% in SF -> 3P if misses Final!)
            if country == "France" and t1 != "France":
                w *= 0.65  # France guaranteed playing 3rd-place playoff July 18!
            if country == "Argentina" and t2 != "Argentina":
                # Argentina plays 3P only ~30% of the time when missing Final (loses SF2 vs loses QF4)
                w *= 0.88
                # Slight extra France-Argentina rivalry caution if France is in Final
                if t1 == "France":
                    w *= 0.88
            weights[name] = w
        tot = sum(weights.values())
        for name, w in weights.items():
            probs[name] += p_match * (w / tot)

print("Q524604 BAYESIAN REFEREE RANKING (July 9, 2026 — Post-QF1 & All 4 QF Refs Confirmed):")
for name, p in sorted(probs.items(), key=lambda x: -x[1])[:16]:
    print(f"  {name:28s}: {p:.4f} ({p*100:.2f}%)")
top5 = sorted(probs.items(), key=lambda x: -x[1])[:5]
print(f"Top 5 sum: {sum(p for _, p in top5):.4f}")
