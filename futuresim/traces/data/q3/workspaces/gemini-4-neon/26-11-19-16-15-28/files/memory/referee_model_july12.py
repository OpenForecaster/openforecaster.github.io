# Quantitative Bayesian Model for Q524604: 2026 FIFA World Cup Final Referee
# Updated July 12, 2026 — Post-QF4 (Argentina 3-1 Switzerland a.e.t.)
#
# Key July 12 evidence:
# 1. FINAL FOUR LOCKED:
#    - SF1 (Dallas, Jul 14): France 0.568 / Spain 0.432 (100% UEFA)
#    - SF2 (Atlanta, Jul 15): England 0.540 / Argentina 0.460 (Switzerland ELIMINATED!)
#    - Final confederation mix shifts from 61.2% UEFA-UEFA / 38.8% UEFA-CONMEBOL (Jul 11)
#      to 54.0% UEFA-UEFA / 46.0% UEFA-CONMEBOL!
#      -> Major structural boost to strictly neutral confederations (CONCACAF: Elfath, Ramos; AFC: Faghani)!
# 2. COUNTRY-CONFLICT SHIFTS:
#    - Michael Oliver (ENG) & Anthony Taylor (ENG): Now blocked by England (54.0%) +
#      Argentina (46.0%, Falklands rule) = ~100% BLOCKED!
#    - Facundo Tello (ARG) & Darío Herrera (ARG): Now blocked in 46.0% of Finals (up from 38.8%),
#      remaining eligible ONLY in the 54.0% UEFA-UEFA Finals!
#    - Sandro Schärer (SUI): Switzerland eliminated -> now 0% conflict.
# 3. QF4 PERFORMANCE UPDATE (João Pinheiro, POR):
#    - Pinheiro officiated QF4 ARG-SUI on Jul 11:
#      (a) Missed Embolo's dive on-field and wrongly booked Paredes -> lengthy VAR mistaken-identity
#          reversal sending Embolo off; sparked fierce Swiss outcry demanding FIFA explanation
#          (partially mitigated: neutral observers agreed post-VAR red card was technically correct).
#      (b) Viral first-half confrontation with Lionel Messi ("Do not disrespect me").
#    - Signal drops from 1.35 (pre-match QF4 trust) to 0.92 overall, PLUS a 0.35x optics friction
#      if Argentina reaches the Final (46.0% of Finals — Collina avoids putting the ref from
#      ARG's viral Messi clash & Swiss red-card storm on an Argentina Final!).
# 4. FIFA SF1/SF2 referee announcements still TBC as of Jul 12 (ESPN 09:39 AM Jul 12: "Referee: TBC").

top = {"France": 0.568, "Spain": 0.432}
bot = {"England": 0.540, "Argentina": 0.460}

confed = {
    "France": "UEFA", "Spain": "UEFA",
    "Argentina": "CONMEBOL", "England": "UEFA"
}

candidates = [
    # CONCACAF (100% strictly neutral in ALL 2026 Finals!)
    ("Ismail Elfath", "USA", "CONCACAF", 1.32, 1.18, 1.0, []),
    ("César Arturo Ramos", "Mexico", "CONCACAF", 1.25, 1.06, 1.0, []),
    ("Iván Barton", "El Salvador", "CONCACAF", 0.50, 1.00, 1.0, []),
    ("Drew Fischer", "Canada", "CONCACAF", 0.42, 1.05, 1.0, []),

    # UEFA Neutrals (0% country conflict)
    ("Slavko Vinčić", "Slovenia", "UEFA", 1.45, 1.05, 0.88, []),
    ("Danny Makkelie", "Netherlands", "UEFA", 0.98, 0.92, 0.88, []),  # slight Balogun U-turn friction
    ("João Pinheiro", "Portugal", "UEFA", 0.90, 0.92, 0.88, []),      # QF4 VAR reversal + Messi clash!
    ("Glenn Nyberg", "Sweden", "UEFA", 0.80, 1.05, 0.88, []),
    ("István Kovács", "Romania", "UEFA", 1.45, 0.58, 0.88, []),
    ("Sandro Schärer", "Switzerland", "UEFA", 0.65, 1.00, 0.88, []),  # Switzerland now eliminated!
    ("Maurizio Mariani", "Italy", "UEFA", 0.58, 1.00, 0.88, []),
    ("Felix Zwayer", "Germany", "UEFA", 0.50, 0.85, 0.88, []),
    ("Szymon Marciniak", "Poland", "UEFA", 0.40, 1.00, 0.88, []),
    ("Espen Eskås", "Norway", "UEFA", 0.50, 0.70, 0.88, []),

    # UEFA Active Countries
    ("Clément Turpin", "France", "UEFA", 1.50, 0.92, 0.88, ["France"]),
    ("Michael Oliver", "England", "UEFA", 1.25, 1.35, 0.88, ["England", "Argentina"]),  # 100% blocked!
    ("Anthony Taylor", "England", "UEFA", 1.15, 1.18, 0.88, ["England", "Argentina"]),  # 100% blocked!
    ("François Letexier", "France", "UEFA", 1.20, 0.50, 0.88, ["France"]),
    ("Alejandro Hernández Hernández", "Spain", "UEFA", 0.45, 1.00, 0.88, ["Spain"]),

    # CONMEBOL
    ("Facundo Tello", "Argentina", "CONMEBOL", 1.15, 1.28, 0.02, ["Argentina"]),
    ("Jesús Valenzuela", "Venezuela", "CONMEBOL", 0.92, 1.00, 0.15, []),
    ("Wilton Sampaio", "Brazil", "CONMEBOL", 0.90, 1.00, 0.15, []),
    ("Darío Herrera", "Argentina", "CONMEBOL", 0.65, 1.12, 0.02, ["Argentina"]),
    ("Ramon Abatti", "Brazil", "CONMEBOL", 0.55, 1.08, 0.15, []),
    ("Raphael Claus", "Brazil", "CONMEBOL", 0.70, 0.12, 0.15, []),
    ("Other_CONMEBOL", "Other", "CONMEBOL", 0.65, 1.00, 0.15, []),

    # AFC / CAF / OFC (100% strictly neutral in ALL 2026 Finals!)
    ("Alireza Faghani", "Australia", "AFC", 0.85, 1.10, 1.0, []),  # 2025 CWC Final at MetLife + R16 ENG-MEX, rested through QFs!
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
                    w *= 1.20
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
            # Pinheiro optics friction if Argentina is in the Final (Messi clash + Swiss VAR storm)
            if name == "João Pinheiro" and t2 == "Argentina":
                w *= 0.35
            weights[name] = w
        tot = sum(weights.values())
        for name, w in weights.items():
            probs[name] += p_match * (w / tot)

print("Q524604 BAYESIAN REFEREE RANKING (July 12, 2026 — Post-QF4):")
for name, p in sorted(probs.items(), key=lambda x: -x[1])[:16]:
    print(f"  {name:28s}: {p:.4f} ({p*100:.2f}%)")
top5 = sorted(probs.items(), key=lambda x: -x[1])[:5]
print(f"Top 5 sum: {sum(p for _, p in top5):.4f}")
