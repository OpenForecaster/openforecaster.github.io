import random
from collections import Counter

# ==============================================================================
# MODEL 1: Q1 (qid=653425) — MEN'S 200m, WORLD ATHLETICS ULTIMATE CHAMPIONSHIP
# Budapest, Sept 12 (semis) & Sept 13 (final), 2026 (T+8d)
# ==============================================================================
# Key Sept 4-5 updates:
# - Noah Lyles OFFICIALLY OUT for 2026 season (announced Sept 4).
# - Kenny Bednarek won Brussels DL Final (Sept 5) in 19.62 (+0.8) despite 16C cold
#   and mild sickness! Matched his Zurich WL (19.62), 4-for-4 in 200m in 2026,
#   4-0 vs Tebogo in last 4 H2H!
# - Brussels DL Final: 1. Bednarek 19.62, 2. Dambile 19.89 (19.74 SB),
#   3. Charamba 19.99, 4. Tebogo 20.01 (19.84 SB, Olympic champ 19.46 PB),
#   5. Courtney Lindsey 20.09, 6. Jose Figueroa 20.44 (19.76 SB).
# - Field outside Brussels: Tate Taylor (19.75 Eugene win over Tebogo),
#   Alexander Ogando, Bryan Levell, Robert Gregory, Tapiwanashe Makarawu, etc.
#
# Mechanics of 200m race model (2 rounds: semi + final, 8 days out):
#   Each athlete draws a pre-meet state (DNS/DQ/injury, off/sick, normal, peak),
#   then draws a meet-form mean (meet_sd ~ 0.08-0.10s) and final-race noise
#   (race_sd ~ 0.07s) + small semi-survival / false-start risk (~1.5% per round).
#   Lowest time wins!

def sim_200m_mixture(regimes, n_trials=200000, seed=653425):
    rng = random.Random(seed)
    blend = Counter()
    for rname, weight, athletes in regimes:
        wins = Counter()
        for _ in range(n_trials):
            best_t = 99.0
            winner = None
            for name, states in athletes:
                u = rng.random()
                cum = 0.0
                chosen = None
                for st in states:
                    cum += st[0]
                    if u <= cum:
                        chosen = st
                        break
                if chosen is None or chosen[1] is None:
                    continue
                _, mu, sd = chosen
                # semi DQ/injury/non-advance small extra risk baked into DNS state
                t = rng.gauss(mu, sd)
                if t < best_t:
                    best_t = t
                    winner = name
            wins[winner] += 1
        probs = {k: c / n_trials for k, c in wins.items()}
        top6 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:6])
        print(f"  [{rname[:56]:56s} w={weight:.2f}] {top6}")
        for k, v in probs.items():
            blend[k] += weight * v
    return blend

# Standard deviation for single 200m final relative to field (~0.10-0.12s total)
regimes_200m = [
    ("R1: Base (Bednarek 19.62 peak; Tebogo bimodal 19.85/19.66)", 0.55, [
        # Bednarek: 6% DNS/DQ/hamstring/illness scratch, 14% lingering sickness/fatigue (19.84), 80% peak (19.63)
        ("Kenny Bednarek",        [(0.06, None, 0), (0.14, 19.84, 0.11), (0.80, 19.63, 0.10)]),
        # Tebogo: 5% DNS/DQ, 65% 2026 form (19.88), 30% Olympic-champ Budapest peak (19.66)
        ("Letsile Tebogo",        [(0.05, None, 0), (0.65, 19.88, 0.11), (0.30, 19.66, 0.11)]),
        # Dambile: 4% DNS/DQ, 96% strong 19.83 (19.74 SB, 19.89 Brussels w/ bend error)
        ("Sinesipho Dambile",     [(0.04, None, 0), (0.96, 19.84, 0.11)]),
        # Charamba: 4% DNS/DQ, 96% 19.95 (19.99 Brussels 3rd)
        ("Makanakaishe Charamba", [(0.04, None, 0), (0.96, 19.95, 0.11)]),
        # Tate Taylor: 35% doesn't start/qualify, 65% starts at 19.88 (high ceiling 19.75 Eugene)
        ("Tate Taylor",           [(0.35, None, 0), (0.65, 19.88, 0.13)]),
        # Rest of 16-man field (Ogando, Levell, Lindsey, Figueroa, Makarawu, Gregory):
        # modeled as 3 solid ~19.88-19.98 contenders
        ("Field_Contender_1",     [(0.10, None, 0), (0.90, 19.87, 0.12)]),
        ("Field_Contender_2",     [(0.10, None, 0), (0.90, 19.93, 0.12)]),
        ("Field_Contender_3",     [(0.10, None, 0), (0.90, 19.98, 0.12)]),
    ]),
    ("R2: Tebogo Championship Peak + Bednarek Sickness/Wear", 0.25, [
        ("Kenny Bednarek",        [(0.09, None, 0), (0.31, 19.82, 0.11), (0.60, 19.67, 0.10)]),
        ("Letsile Tebogo",        [(0.04, None, 0), (0.40, 19.82, 0.11), (0.56, 19.62, 0.11)]),
        ("Sinesipho Dambile",     [(0.04, None, 0), (0.96, 19.82, 0.11)]),
        ("Makanakaishe Charamba", [(0.04, None, 0), (0.96, 19.93, 0.11)]),
        ("Tate Taylor",           [(0.35, None, 0), (0.65, 19.84, 0.13)]),
        ("Field_Contender_1",     [(0.10, None, 0), (0.90, 19.84, 0.12)]),
        ("Field_Contender_2",     [(0.10, None, 0), (0.90, 19.90, 0.12)]),
        ("Field_Contender_3",     [(0.10, None, 0), (0.90, 19.96, 0.12)]),
    ]),
    ("R3: Bednarek PB Run (19.55-19.60) & Tebogo Flat in 2026", 0.20, [
        ("Kenny Bednarek",        [(0.04, None, 0), (0.08, 19.78, 0.10), (0.88, 19.58, 0.09)]),
        ("Letsile Tebogo",        [(0.06, None, 0), (0.82, 19.94, 0.11), (0.12, 19.72, 0.10)]),
        ("Sinesipho Dambile",     [(0.04, None, 0), (0.96, 19.85, 0.11)]),
        ("Makanakaishe Charamba", [(0.04, None, 0), (0.96, 19.96, 0.11)]),
        ("Tate Taylor",           [(0.35, None, 0), (0.65, 19.89, 0.13)]),
        ("Field_Contender_1",     [(0.10, None, 0), (0.90, 19.89, 0.12)]),
        ("Field_Contender_2",     [(0.10, None, 0), (0.90, 19.94, 0.12)]),
        ("Field_Contender_3",     [(0.10, None, 0), (0.90, 19.99, 0.12)]),
    ]),
]

print("=== Q1 (qid=653425) MEN'S 200M ULTIMATE CHAMPIONSHIP (SEPT 5 UPDATE) ===")
b200 = sim_200m_mixture(regimes_200m)
print("FINAL 200M BLEND:")
for k, v in sorted(b200.items(), key=lambda x: -x[1]):
    print(f"  {k:26s}: {v:.4f}")
field_sum = sum(v for k, v in b200.items() if k.startswith("Field_"))
print(f"  TOTAL FIELD (outside top5): {field_sum:.4f}")


# ==============================================================================
# MODEL 2: Q2 (qid=261941) — WOMEN'S JAVELIN, WORLD ATHLETICS ULTIMATE CHAMPIONSHIP
# Budapest, Sept 12, 2026 (T+7d)
# ==============================================================================
# Key Sept 5 Brussels DL Final results:
# 1. Yan Ziyi (CHN) 68.42m (5-for-5 undefeated in DL: 71.74, 67.11, 67.44, 68.75, 68.42!)
#    ALREADY IN EUROPE! Won auto-spot to Budapest ($150k first prize, 7 days away)!
#    DNS risk drops sharply from ~18% -> ~5-6% (normal travel/injury/China pullout tail).
# 2. Haruka Kitaguchi (JPN) 65.44m (surged past Ruiz & Vilagos! Reigning Olympic champ!)
# 3. Flor Denis Ruiz Hurtado (COL) 64.07m (2nd Lausanne, 3rd Brussels, 67.34m SAR Aug)
# 4. Adriana Vilagos (SRB) 62.22m (faded slightly from earlier 65-67m form)
# 5. Anete Sietina (LAT) 59.26m
# 6. Sigrid Borge (NOR) 58.08m (8th Lausanne, 6th Brussels -> deep slump!)
# + Auto-qualified Juleisy Angulo (ECU, 2025 World Champ) + 8th spot (Victoria Hudson / Little / van Dyk)

def sim_javelin_mixture(regimes, n_trials=200000, seed=261941):
    rng = random.Random(seed)
    blend = Counter()
    for rname, weight, athletes in regimes:
        wins = Counter()
        for _ in range(n_trials):
            best_m = -1.0
            winner = None
            for name, states in athletes:
                u = rng.random()
                cum = 0.0
                chosen = None
                for st in states:
                    cum += st[0]
                    if u <= cum:
                        chosen = st
                        break
                if chosen is None or chosen[1] is None:
                    continue
                _, mu, dsd, tsd, fr = chosen
                day_mu = rng.gauss(mu, dsd)
                ath_best = 0.0
                for _t in range(6):
                    if rng.random() < fr:
                        continue
                    val = rng.gauss(day_mu, tsd)
                    if val > ath_best:
                        ath_best = val
                if ath_best > best_m:
                    best_m = ath_best
                    winner = name
            wins[winner] += 1
        probs = {k: c / n_trials for k, c in wins.items()}
        top5 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:5])
        print(f"  [{rname[:56]:56s} w={weight:.2f}] {top5}")
        for k, v in probs.items():
            blend[k] += weight * v
    return blend

women_jav_sep05 = [
    ("R1: Base (Yan 94% starts, 68.5m mean best; Kitaguchi #2)", 0.60, [
        # Yan Ziyi: 6% DNS/China-AG-pull/injury, 94% throws with mu=66.1 (E[best6]~68.3m)
        ("Yan Ziyi",                [(0.06, None, 0, 0, 0), (0.94, 66.1, 1.8, 1.9, 0.16)]),
        # Haruka Kitaguchi: 4% DNS (already in Brussels!), mu=62.7 (E[best6]~64.9m, 65.44 Brussels!)
        ("Haruka Kitaguchi",        [(0.04, None, 0, 0, 0), (0.96, 62.7, 1.8, 1.9, 0.15)]),
        # Flor Denis Ruiz Hurtado: 4% DNS, mu=62.3 (64.07 Brussels, 67.34 SAR Aug)
        ("Flor Denis Ruiz Hurtado", [(0.04, None, 0, 0, 0), (0.96, 62.3, 1.9, 1.9, 0.16)]),
        # Adriana Vilagos: 4% DNS, mu=61.6 (62.22 Brussels dip, still 67.22 PB)
        ("Adriana Vilagos",         [(0.04, None, 0, 0, 0), (0.96, 61.6, 1.8, 1.8, 0.15)]),
        # Juleisy Angulo: reigning World Champ (auto-qualified), mu=60.5
        ("Juleisy Angulo",          [(0.08, None, 0, 0, 0), (0.92, 60.5, 2.0, 1.9, 0.17)]),
        # Victoria Hudson / Mackenzie Little / Jo-Ane van Dyk (spot #7-8)
        ("Field_Hudson_Little",     [(0.00, None, 0, 0, 0), (1.00, 61.2, 1.8, 1.8, 0.16)]),
        # Anete Sietina (59.26 Brussels)
        ("Anete Sietina",           [(0.05, None, 0, 0, 0), (0.95, 59.5, 1.7, 1.8, 0.16)]),
        # Sigrid Borge (58.08 Brussels slump)
        ("Sigrid Borge",            [(0.10, None, 0, 0, 0), (0.90, 58.8, 1.9, 1.8, 0.17)]),
    ]),
    ("R2: Yan Ziyi Fatigue / China Asian Games Pullout (15% DNS)", 0.20, [
        ("Yan Ziyi",                [(0.15, None, 0, 0, 0), (0.85, 65.1, 1.9, 1.9, 0.17)]),
        ("Haruka Kitaguchi",        [(0.04, None, 0, 0, 0), (0.96, 63.1, 1.8, 1.9, 0.15)]),
        ("Flor Denis Ruiz Hurtado", [(0.04, None, 0, 0, 0), (0.96, 62.6, 1.9, 1.9, 0.16)]),
        ("Adriana Vilagos",         [(0.04, None, 0, 0, 0), (0.96, 62.2, 1.8, 1.8, 0.15)]),
        ("Juleisy Angulo",          [(0.08, None, 0, 0, 0), (0.92, 60.8, 2.0, 1.9, 0.17)]),
        ("Field_Hudson_Little",     [(0.00, None, 0, 0, 0), (1.00, 61.5, 1.8, 1.8, 0.16)]),
        ("Anete Sietina",           [(0.05, None, 0, 0, 0), (0.95, 59.7, 1.7, 1.8, 0.16)]),
        ("Sigrid Borge",            [(0.10, None, 0, 0, 0), (0.90, 59.2, 1.9, 1.8, 0.17)]),
    ]),
    ("R3: Yan Ziyi Unstoppable 69m+ Form (97% starts)", 0.20, [
        ("Yan Ziyi",                [(0.03, None, 0, 0, 0), (0.97, 66.8, 1.7, 1.9, 0.15)]),
        ("Haruka Kitaguchi",        [(0.04, None, 0, 0, 0), (0.96, 62.6, 1.8, 1.9, 0.15)]),
        ("Flor Denis Ruiz Hurtado", [(0.04, None, 0, 0, 0), (0.96, 62.2, 1.9, 1.9, 0.16)]),
        ("Adriana Vilagos",         [(0.04, None, 0, 0, 0), (0.96, 61.4, 1.8, 1.8, 0.15)]),
        ("Juleisy Angulo",          [(0.08, None, 0, 0, 0), (0.92, 60.3, 2.0, 1.9, 0.17)]),
        ("Field_Hudson_Little",     [(0.00, None, 0, 0, 0), (1.00, 61.0, 1.8, 1.8, 0.16)]),
        ("Anete Sietina",           [(0.05, None, 0, 0, 0), (0.95, 59.3, 1.7, 1.8, 0.16)]),
        ("Sigrid Borge",            [(0.10, None, 0, 0, 0), (0.90, 58.6, 1.9, 1.8, 0.17)]),
    ]),
]

print("\n=== Q2 (qid=261941) WOMEN'S JAVELIN ULTIMATE CHAMPIONSHIP (SEPT 5 UPDATE) ===")
bwj = sim_javelin_mixture(women_jav_sep05)
print("FINAL WOMEN'S JAVELIN BLEND:")
for k, v in sorted(bwj.items(), key=lambda x: -x[1]):
    print(f"  {k:26s}: {v:.4f}")
