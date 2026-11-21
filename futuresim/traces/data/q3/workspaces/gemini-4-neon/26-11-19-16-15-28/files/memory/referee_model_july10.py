# Quantitative Bayesian Model for Q524604: 2026 FIFA World Cup Final Referee
# Updated July 10, 2026 — Post-QF2 (Spain 2-1 Belgium -> SF1 locked as France vs Spain!)
#
# Key July 10 evidence:
# 1. SF1 LOCKED: France vs Spain (~56.6% France / ~43.4% Spain; Belgium ELIMINATED!).
#    Bottom half (SF2): Argentina ~0.425, England ~0.330, Norway ~0.145, Switzerland ~0.100.
#    Final mix: ~57.5% UEFA-vs-UEFA, ~42.5% UEFA-vs-CONMEBOL, 0% CAF!
#    -> Virtually identical confederation mix to July 9 (~58%/42%)!
# 2. Match-officiating updates:
#    - QF1 (FRA 2-0 MAR, Facundo Tello [ARG]): Morocco coach Ouahbi protested missed Rabiot handball in
#      build-up to Mbappe's 60' goal + Haaland/media criticized lengthy VAR delay on Mbappe's 1H penalty.
#      Minor blemish for Tello (1.40 -> 1.28), though Collina backs officials & Rabiot was prior phase.
#    - QF2 (ESP 2-1 BEL, Michael Oliver [ENG]): Clean match (correctly waived accidental Rodri arm contact),
#      still blocked ~75.5% by England (~33%) + Argentina (~42.5% Falklands rule).
#    - QF3 (ENG-NOR, Clement Turpin [FRA]): France's Final prob dropped ~63.3% -> ~56.6%, slightly easing
#      Turpin's country-conflict block (though France 3rd-place playoff discount still applies in 43.4%!).
#    - No FIFA semifinal referee appointments yet (expected July 12-13 after Saturday's QFs 3 & 4).

top = {"France": 0.566, "Spain": 0.434}
bot = {"Argentina": 0.425, "England": 0.330, "Norway": 0.145, "Switzerland": 0.100}

confed = {
    "France": "UEFA", "Spain": "UEFA",
    "Argentina": "CONMEBOL", "England": "UEFA", "Norway": "UEFA", "Switzerland": "UEFA"
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

    # UEFA Active Countries
    ("Clément Turpin", "France", "UEFA", 1.50, 1.30, 0.88, ["France"]),
    ("Michael Oliver", "England", "UEFA", 1.25, 1.35, 0.88, ["England", "Argentina"]),  # clean QF2 ESP-BEL
    ("Anthony Taylor", "England", "UEFA", 1.15, 1.18, 0.88, ["England", "Argentina"]),
    ("François Letexier", "France", "UEFA", 1.20, 0.50, 0.88, ["France"]),
    ("Sandro Schärer", "Switzerland", "UEFA", 0.65, 1.00, 0.88, ["Switzerland"]),
    ("Espen Eskås", "Norway", "UEFA", 0.50, 0.70, 0.88, ["Norway"]),
    ("Alejandro Hernández Hernández", "Spain", "UEFA", 0.45, 1.00, 0.88, ["Spain"]),

    # CONMEBOL
    ("Facundo Tello", "Argentina", "CONMEBOL", 1.15, 1.28, 0.02, ["Argentina"]),  # slight Rabiot handball/VAR noise
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

print("Q524604 BAYESIAN REFEREE RANKING (July 10, 2026 — Post-QF2):")
for name, p in sorted(probs.items(), key=lambda x: -x[1])[:16]:
    print(f"  {name:28s}: {p:.4f} ({p*100:.2f}%)")
top5 = sorted(probs.items(), key=lambda x: -x[1])[:5]
print(f"Top 5 sum: {sum(p for _, p in top5):.4f}")
