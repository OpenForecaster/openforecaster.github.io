# Quantitative Bayesian Model for Q524604: 2026 FIFA World Cup Final Referee
# Updated July 11, 2026 — Post-QF3 (England 2-1 Norway a.e.t.!)
#
# Key July 11 evidence:
# 1. BRACKET SHIFT:
#    - SF1 (Dallas, Jul 14): France 0.568 / Spain 0.432 (LOCKED; 100% UEFA)
#    - SF2 (Atlanta, Jul 15): England ~0.531, Argentina ~0.388, Switzerland ~0.081 (Norway ELIMINATED!)
#    - Final confederation mix shifts from ~57.5% UEFA-UEFA / ~42.5% UEFA-CONMEBOL
#      to ~61.2% UEFA-UEFA / ~38.8% UEFA-CONMEBOL!
# 2. COUNTRY-CONFLICT SHIFTS:
#    - Michael Oliver (ENG) & Anthony Taylor (ENG): Now blocked by England (53.1%) +
#      Argentina (38.8%, Falklands rule) = 91.9% BLOCKED (vs 75.5% yesterday)!!
#    - Facundo Tello (ARG) & Darío Herrera (ARG): Argentina's Final prob drops 42.5% -> 38.8%,
#      leaving Tello unblocked in 61.2% of Finals (all UEFA-UEFA, where CONMEBOL refs are
#      favored as strictly neutral, though slight QF1 Rabiot-handball/VAR-delay blemish remains).
#    - Clément Turpin (FRA): Still blocked by France (56.8%) + 3P discount (43.2%), AND in QF3
#      ENG-NOR today had TWO major on-field calls overturned by VAR (missed Haaland foul on
#      disallowed Heggem goal + wrongly awarded ET penalty to Djed Spence overturned by VAR) ->
#      signal drops 1.30 -> 0.92!
#    - João Pinheiro (POR): Officiating QF4 ARG-SUI tonight (result pending); 100% conflict-free.
#    - Ismail Elfath (USA), Slavko Vinčić (SVN), César Arturo Ramos (MEX): 100% conflict-free!
# 3. No FIFA semifinal referee announcements yet (expected July 12-13 after QF4 finishes).

top = {"France": 0.568, "Spain": 0.432}
bot = {"England": 0.531, "Argentina": 0.388, "Switzerland": 0.081}

confed = {
    "France": "UEFA", "Spain": "UEFA",
    "Argentina": "CONMEBOL", "England": "UEFA", "Switzerland": "UEFA"
}

candidates = [
    # CONCACAF (100% strictly neutral in ALL 2026 Finals!)
    ("Ismail Elfath", "USA", "CONCACAF", 1.32, 1.18, 1.0, []),
    ("César Arturo Ramos", "Mexico", "CONCACAF", 1.25, 1.05, 1.0, []),
    ("Iván Barton", "El Salvador", "CONCACAF", 0.50, 1.00, 1.0, []),
    ("Drew Fischer", "Canada", "CONCACAF", 0.42, 1.05, 1.0, []),

    # UEFA Neutrals (0% country conflict)
    ("Slavko Vinčić", "Slovenia", "UEFA", 1.45, 1.05, 0.88, []),
    ("João Pinheiro", "Portugal", "UEFA", 0.90, 1.35, 0.88, []),
    ("István Kovács", "Romania", "UEFA", 1.45, 0.58, 0.88, []),
    ("Danny Makkelie", "Netherlands", "UEFA", 0.95, 1.00, 0.88, []),
    ("Glenn Nyberg", "Sweden", "UEFA", 0.78, 1.05, 0.88, []),
    ("Szymon Marciniak", "Poland", "UEFA", 0.40, 1.00, 0.88, []),
    ("Maurizio Mariani", "Italy", "UEFA", 0.58, 1.00, 0.88, []),
    ("Felix Zwayer", "Germany", "UEFA", 0.50, 0.85, 0.88, []),
    ("Espen Eskås", "Norway", "UEFA", 0.50, 0.70, 0.88, []),  # Norway now eliminated -> conflict-free!

    # UEFA Active Countries
    ("Clément Turpin", "France", "UEFA", 1.50, 0.92, 0.88, ["France"]),  # 2 VAR reversals in QF3 ENG-NOR!
    ("Michael Oliver", "England", "UEFA", 1.25, 1.35, 0.88, ["England", "Argentina"]),  # 91.9% blocked!
    ("Anthony Taylor", "England", "UEFA", 1.15, 1.18, 0.88, ["England", "Argentina"]),
    ("François Letexier", "France", "UEFA", 1.20, 0.50, 0.88, ["France"]),
    ("Sandro Schärer", "Switzerland", "UEFA", 0.65, 1.00, 0.88, ["Switzerland"]),
    ("Alejandro Hernández Hernández", "Spain", "UEFA", 0.45, 1.00, 0.88, ["Spain"]),

    # CONMEBOL
    ("Facundo Tello", "Argentina", "CONMEBOL", 1.15, 1.28, 0.02, ["Argentina"]),
    ("Jesús Valenzuela", "Venezuela", "CONMEBOL", 0.92, 1.00, 0.15, []),
    ("Wilton Sampaio", "Brazil", "CONMEBOL", 0.90, 1.00, 0.15, []),
    ("Darío Herrera", "Argentina", "CONMEBOL", 0.65, 1.12, 0.02, ["Argentina"]),
    ("Ramon Abatti", "Brazil", "CONMEBOL", 0.55, 1.08, 0.15, []),
    ("Raphael Claus", "Brazil", "CONMEBOL", 0.70, 0.12, 0.15, []),
    ("Other_CONMEBOL", "Other", "CONMEBOL", 0.65, 1.00, 0.15, []),

    # AFC / CAF / OFC
    ("Alireza Faghani", "Australia", "AFC", 0.78, 1.05, 1.0, []),
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
                    w *= 1.18
            else:
                if rconf == "UEFA":
                    w *= 1.08
                elif rconf == "CONMEBOL":
                    w *= 1.16
                elif rconf == "CONCACAF":
                    w *= 1.08
            if country == "France" and t1 != "France":
                w *= 0.65
            if country == "Argentina" and t2 != "Argentina":
                w *= 0.88
                if t1 == "France":
                    w *= 0.88
            weights[name] = w
        tot = sum(weights.values())
        for name, w in weights.items():
            probs[name] += p_match * (w / tot)

print("Q524604 BAYESIAN REFEREE RANKING (July 11, 2026 — Post-QF3):")
for name, p in sorted(probs.items(), key=lambda x: -x[1])[:16]:
    print(f"  {name:28s}: {p:.4f} ({p*100:.2f}%)")
top5 = sorted(probs.items(), key=lambda x: -x[1])[:5]
print(f"Top 5 sum: {sum(p for _, p in top5):.4f}")
