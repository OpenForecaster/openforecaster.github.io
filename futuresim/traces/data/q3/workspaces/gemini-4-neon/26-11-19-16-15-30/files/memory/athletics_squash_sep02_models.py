import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — WEDNESDAY SEPT 2, 2026
# Batch: athletics_and_squash (30434, 261941, 556932, 700005; 695205 sanity check)
# ==============================================================================

def sim_javelin_mixture(regimes, n_trials_per_regime=150000, seed=20260902):
    rng = random.Random(seed)
    blend = Counter()
    per_regime = []
    for rname, weight, athletes in regimes:
        wins = Counter()
        for _ in range(n_trials_per_regime):
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
        probs = {k: c / n_trials_per_regime for k, c in wins.items()}
        per_regime.append((rname, weight, probs))
        for k, v in probs.items():
            blend[k] += weight * v
    return blend, per_regime


# ------------------------------------------------------------------------------
# MODEL 1: Q2 (qid=30434) — MEN'S JAVELIN, WORLD ATHLETICS ULTIMATE CHAMPIONSHIP
# Budapest, Sept 11-13, 2026 (T+11d)
# MAJOR UPDATE: Neeraj Chopra OFFICIALLY OUT (ankle ligament tear, out for season)!
# 8-man field: Pathirage, Weber (injury uncertainty), Peters, Walcott, Thompson,
#              Nadeem (auto Olympic champ, 78.63m SB, high DNS/rust risk),
#              Sachin Yadav (moves up to #7), Spot #8 (Julius Yego / Vadlejch / Rohit Yadav / sub)
# ------------------------------------------------------------------------------
men_jav_regimes = [
    ("R1: Base Calibrated (Pathirage 90m+ peak, Weber 32% DNS / 25% hurt / 43% healthy)", 0.50, [
        ("Rumesh Tharanga Pathirage", [(0.04, None, 0, 0, 0), (0.14, 85.4, 2.0, 2.3, 0.16), (0.82, 87.4, 2.0, 2.3, 0.16)]),
        ("Julian Weber",              [(0.32, None, 0, 0, 0), (0.25, 83.4, 2.2, 2.3, 0.16), (0.43, 86.2, 2.1, 2.3, 0.16)]),
        ("Anderson Peters",           [(0.04, None, 0, 0, 0), (0.96, 84.3, 2.3, 2.5, 0.17)]),
        ("Keshorn Walcott",           [(0.05, None, 0, 0, 0), (0.95, 82.4, 2.3, 2.4, 0.17)]),
        ("Curtis Thompson",           [(0.08, None, 0, 0, 0), (0.58, 79.8, 2.2, 2.4, 0.18), (0.34, 83.6, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.48, None, 0, 0, 0), (0.38, 78.8, 2.5, 2.5, 0.18), (0.14, 84.4, 2.8, 2.6, 0.17)]),
        ("Sachin Yadav",              [(0.05, None, 0, 0, 0), (0.95, 81.4, 2.1, 2.3, 0.16)]),
        ("Field_8th_Yego_Vadlejch",   [(0.00, None, 0, 0, 0), (1.00, 81.6, 2.3, 2.4, 0.17)]),
    ]),
    ("R2: Pathirage Brussels->Budapest Wear + Weber & Peters Peak", 0.25, [
        ("Rumesh Tharanga Pathirage", [(0.07, None, 0, 0, 0), (0.30, 85.0, 2.1, 2.3, 0.17), (0.63, 86.7, 2.1, 2.3, 0.16)]),
        ("Julian Weber",              [(0.20, None, 0, 0, 0), (0.22, 84.2, 2.1, 2.3, 0.16), (0.58, 86.6, 2.0, 2.3, 0.16)]),
        ("Anderson Peters",           [(0.04, None, 0, 0, 0), (0.96, 84.9, 2.4, 2.5, 0.17)]),
        ("Keshorn Walcott",           [(0.05, None, 0, 0, 0), (0.95, 83.0, 2.3, 2.4, 0.17)]),
        ("Curtis Thompson",           [(0.08, None, 0, 0, 0), (0.48, 80.2, 2.2, 2.4, 0.18), (0.44, 84.1, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.42, None, 0, 0, 0), (0.36, 79.6, 2.5, 2.5, 0.18), (0.22, 85.0, 2.8, 2.6, 0.17)]),
        ("Sachin Yadav",              [(0.05, None, 0, 0, 0), (0.95, 81.6, 2.1, 2.3, 0.16)]),
        ("Field_8th_Yego_Vadlejch",   [(0.00, None, 0, 0, 0), (1.00, 82.0, 2.3, 2.4, 0.17)]),
    ]),
    ("R3: Pathirage Historic Juggernaut + Weber Truly Injured (55% DNS)", 0.25, [
        ("Rumesh Tharanga Pathirage", [(0.02, None, 0, 0, 0), (0.08, 86.0, 2.0, 2.3, 0.16), (0.90, 88.1, 1.9, 2.3, 0.16)]),
        ("Julian Weber",              [(0.55, None, 0, 0, 0), (0.25, 82.8, 2.2, 2.3, 0.16), (0.20, 85.8, 2.1, 2.3, 0.16)]),
        ("Anderson Peters",           [(0.04, None, 0, 0, 0), (0.96, 84.1, 2.3, 2.5, 0.17)]),
        ("Keshorn Walcott",           [(0.05, None, 0, 0, 0), (0.95, 82.1, 2.3, 2.4, 0.17)]),
        ("Curtis Thompson",           [(0.10, None, 0, 0, 0), (0.68, 79.5, 2.2, 2.4, 0.18), (0.22, 83.2, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.58, None, 0, 0, 0), (0.34, 78.0, 2.4, 2.5, 0.18), (0.08, 83.5, 2.7, 2.6, 0.17)]),
        ("Sachin Yadav",              [(0.05, None, 0, 0, 0), (0.95, 81.2, 2.1, 2.3, 0.16)]),
        ("Field_8th_Yego_Vadlejch",   [(0.00, None, 0, 0, 0), (1.00, 81.4, 2.2, 2.3, 0.17)]),
    ]),
]

mj_blend, mj_regs = sim_javelin_mixture(men_jav_regimes, seed=30434)
print("=== Q2 (qid=30434) MEN'S JAVELIN ULTIMATE CHAMPIONSHIP (NEERAJ OUT!) ===")
for rname, w, probs in mj_regs:
    top6 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:6])
    print(f"  [{rname[:58]:58s} w={w:.2f}] {top6}")
print("FINAL MEN'S JAVELIN UC BLEND:")
for k, v in sorted(mj_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")
top5_mj = sorted([(k, v) for k, v in mj_blend.items() if not k.startswith("Field_")], key=lambda x: -x[1])[:5]
print("Top-5 sum =", round(sum(v for _, v in top5_mj), 4))


# ------------------------------------------------------------------------------
# MODEL 2: Q3 (qid=261941) — WOMEN'S JAVELIN, WORLD ATHLETICS ULTIMATE CHAMPIONSHIP
# Budapest, Sept 12, 2026 (T+10d)
# Calibration: Women's javelin throw_sd ~ 1.8m, day_sd ~ 1.6m -> E[best_5] ≈ mu + 2.1m
# Yan Ziyi: 71.74, 67.11, 67.44, 68.75 -> E[best] ~ 68.0m (mu=65.9) if starts!
#   Start prob: ~83% (17% risk China prioritizes Asian Games Sept 19-Oct 4 or skips)
# Flor Denis Ruiz Hurtado: 67.34m SAR Aug + 2nd Lausanne DL (20 DL pts #3) -> E[best] ~ 64.5m (mu=62.4, wider upside)
# Adriana Vilagos: 32 DL pts (tied #1), 3rd Lausanne, 67.22m PB -> E[best] ~ 64.3m (mu=62.3)
# Haruka Kitaguchi: Olympic Champ (auto), jumped to 16 DL pts (#5, strong Lausanne!), 67.38m PB -> E[best] ~ 64.3m (mu=62.2, clutch!)
#   Small ~8% risk Kitaguchi prioritizes home Asian Games in Nagoya (Sept 19)
# Sigrid Borge: 65.00m Xiamen, 16 DL pts (#4), BUT 8th (+1 pt) Lausanne -> E[best] ~ 62.6m (mu=60.5)
# Anete Sietina (#6 DL, 11 pts), Juleisy Angulo (auto World Champ), Field #8 (Hudson/Little/van Dyk/Kolak)
# ------------------------------------------------------------------------------
women_jav_regimes = [
    ("R1: Base (Yan 83% starts & dominant; Ruiz/Vilagos/Kitaguchi close chase pack)", 0.55, [
        ("Yan Ziyi",                 [(0.17, None, 0, 0, 0), (0.83, 65.8, 1.8, 1.9, 0.16)]),
        ("Adriana Vilagos",          [(0.04, None, 0, 0, 0), (0.96, 62.2, 1.7, 1.8, 0.15)]),
        ("Haruka Kitaguchi",         [(0.08, None, 0, 0, 0), (0.92, 62.1, 1.9, 1.9, 0.16)]),
        ("Flor Denis Ruiz Hurtado",  [(0.05, None, 0, 0, 0), (0.95, 62.3, 1.9, 1.9, 0.16)]),
        ("Sigrid Borge",             [(0.05, None, 0, 0, 0), (0.95, 60.4, 1.8, 1.8, 0.17)]),
        ("Anete Sietina",            [(0.05, None, 0, 0, 0), (0.95, 60.3, 1.7, 1.8, 0.16)]),
        ("Juleisy Angulo",           [(0.08, None, 0, 0, 0), (0.92, 60.0, 2.0, 1.9, 0.18)]),
        ("Field_8th_Hudson_Little",  [(0.00, None, 0, 0, 0), (1.00, 61.2, 1.8, 1.8, 0.16)]),
    ]),
    ("R2: Yan Ziyi Skips/Fatigued (30% DNS) & Veterans Peak", 0.25, [
        ("Yan Ziyi",                 [(0.30, None, 0, 0, 0), (0.70, 64.9, 1.9, 1.9, 0.17)]),
        ("Adriana Vilagos",          [(0.04, None, 0, 0, 0), (0.96, 62.6, 1.7, 1.8, 0.15)]),
        ("Haruka Kitaguchi",         [(0.06, None, 0, 0, 0), (0.94, 62.7, 1.9, 1.9, 0.16)]),
        ("Flor Denis Ruiz Hurtado",  [(0.05, None, 0, 0, 0), (0.95, 62.7, 1.9, 1.9, 0.16)]),
        ("Sigrid Borge",             [(0.05, None, 0, 0, 0), (0.95, 60.6, 1.8, 1.8, 0.17)]),
        ("Anete Sietina",            [(0.05, None, 0, 0, 0), (0.95, 60.5, 1.7, 1.8, 0.16)]),
        ("Juleisy Angulo",           [(0.08, None, 0, 0, 0), (0.92, 60.3, 2.0, 1.9, 0.18)]),
        ("Field_8th_Hudson_Little",  [(0.00, None, 0, 0, 0), (1.00, 61.5, 1.8, 1.8, 0.16)]),
    ]),
    ("R3: Yan Ziyi Confirmed & Unstoppable (95% starts, 69m+ form)", 0.20, [
        ("Yan Ziyi",                 [(0.05, None, 0, 0, 0), (0.95, 66.6, 1.7, 1.9, 0.15)]),
        ("Adriana Vilagos",          [(0.04, None, 0, 0, 0), (0.96, 62.1, 1.7, 1.8, 0.15)]),
        ("Haruka Kitaguchi",         [(0.10, None, 0, 0, 0), (0.90, 61.9, 1.9, 1.9, 0.16)]),
        ("Flor Denis Ruiz Hurtado",  [(0.05, None, 0, 0, 0), (0.95, 62.2, 1.9, 1.9, 0.16)]),
        ("Sigrid Borge",             [(0.05, None, 0, 0, 0), (0.95, 60.2, 1.8, 1.8, 0.17)]),
        ("Anete Sietina",            [(0.05, None, 0, 0, 0), (0.95, 60.1, 1.7, 1.8, 0.16)]),
        ("Juleisy Angulo",           [(0.08, None, 0, 0, 0), (0.92, 59.8, 2.0, 1.9, 0.18)]),
        ("Field_8th_Hudson_Little",  [(0.00, None, 0, 0, 0), (1.00, 61.0, 1.8, 1.8, 0.16)]),
    ]),
]

wj_blend, wj_regs = sim_javelin_mixture(women_jav_regimes, seed=261941)
print("\n=== Q3 (qid=261941) WOMEN'S JAVELIN ULTIMATE CHAMPIONSHIP ===")
for rname, w, probs in wj_regs:
    top5 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:5])
    print(f"  [{rname[:58]:58s} w={w:.2f}] {top5}")
print("FINAL WOMEN'S JAVELIN UC BLEND:")
for k, v in sorted(wj_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")


# ------------------------------------------------------------------------------
# SQUASH KNOCKOUT BRACKET ENGINE (Best-of-5 PSA Singles, 8-quarterfinalist model)
# Empirical PSA Elo scale:
#   Log-rank rating: Elo ~ 2300 - 205 * ln(rank) (so WR #5 vs #6 = 37 pts -> ~55%;
#   WR #5 vs #20 = 284 pts -> ~84% in Bo5; WR #18 vs #24 = 59 pts -> ~58.5%;
#   WR #18 vs #29 = 98 pts -> ~64%; WR #18 vs #38 = 153 pts -> ~71%)
# Let's check exact Elo formula: P(A beats B) = 1 / (1 + 10^(-(E_A - E_B)/400))
# With scale=215*ln(rank):
#   #5 vs #20 -> dE = 298 -> P = 0.848 (very realistic for PSA Bo5!)
#   #18 vs #24 -> dE = 62 -> P = 0.588
#   #18 vs #29 -> dE = 102 -> P = 0.643
#   #18 vs #38 -> dE = 161 -> P = 0.716
#   #24 vs #29 -> dE = 41 -> P = 0.558
#   #24 vs #38 -> dE = 99 -> P = 0.639
# Also add pre-tournament injury/form uncertainty (day/tournament sigma ~ 45 Elo pts)!
# ------------------------------------------------------------------------------
def sim_squash_bracket(players_spec, n_trials=200000, seed=556932):
    """
    players_spec: list of (name, p_enter_singles, states)
    where states = list of (prob, elo_mean, elo_tourney_sd)
    Seed top 8 active players in standard bracket:
      Top half: (1 vs 8) vs (4 vs 5) [randomly shuffle 3/4 and 5-8 per squash seeding]
      Bottom half: (2 vs 7) vs (3 vs 6)
    """
    rng = random.Random(seed)
    wins = Counter()
    for _ in range(n_trials):
        active = []
        for name, p_ent, states in players_spec:
            if rng.random() > p_ent:
                continue
            u = rng.random()
            cum = 0.0
            chosen = states[-1]
            for st in states:
                cum += st[0]
                if u <= cum:
                    chosen = st
                    break
            _, mu_e, sd_e = chosen
            true_elo = rng.gauss(mu_e, sd_e)
            # seeding based roughly on expected rating (with slight seed noise)
            seed_score = mu_e + rng.gauss(0, 18)
            active.append((seed_score, name, true_elo))
        active.sort(key=lambda x: -x[0])
        top8 = [(nm, el) for _, nm, el in active[:8]]
        while len(top8) < 8:
            top8.append(("Field_Other", 1300.0))

        # Standard squash seeding: 1 top, 2 bottom; 3/4 randomly placed opposite 1/2; 5-8 randomly placed in QFs
        p1, p2 = top8[0], top8[1]
        p34 = [top8[2], top8[3]]
        rng.shuffle(p34)
        p58 = [top8[4], top8[5], top8[6], top8[7]]
        rng.shuffle(p58)

        def match(a, b):
            p_a = 1.0 / (1.0 + 10.0 ** (-(a[1] - b[1]) / 400.0))
            return a if rng.random() < p_a else b

        qf1 = match(p1, p58[0])
        qf2 = match(p34[0], p58[1])
        qf3 = match(p34[1], p58[2])
        qf4 = match(p2, p58[3])
        sf1 = match(qf1, qf2)
        sf2 = match(qf3, qf4)
        champ = match(sf1, sf2)
        wins[champ[0]] += 1
    return {k: c / n_trials for k, c in wins.items()}


def rank_to_elo(r, scale=215.0):
    return 2300.0 - scale * math.log(r)


# ------------------------------------------------------------------------------
# MODEL 3: Q4 (qid=556932) — WOMEN'S SINGLES SQUASH, 2026 ASIAN GAMES (T+25d)
# Confirmed:
#   Sivasangari Subramaniam (MAS, WR #5, defending champ, won Aus Open & Grasshopper Cup, beat Orfi)
#   Satomi Watanabe (JPN, WR #6, home court in Nagoya! +25 Elo home boost -> very close to Siva!)
#   Anahat Singh (IND, WR #20, 2026 World Junior Champ, confirmed singles, rapidly improving -> effective ~#17-19!)
#   Aira Azman (MAS, WR #21, confirmed MAS #2 singles!)
#   Rachel Arnold (MAS): CONFIRMED NOT PLAYING SINGLES (mixed doubles only)!
#   Hong Kong top 2 singles (likely 2 of: Chan Sin Yuk ~#24, Ho Tze-Lok ~#27 [2025 Asian Champ], Tomato Ho ~#26, Lee Ka Yi ~#32)
#   Other: Tanvi Khanna (IND), Akari Midorikawa/Risa Sugimoto (JPN), Korean/Pakistani field
# ------------------------------------------------------------------------------
women_squash = [
    # Sivasangari: WR #5 (Elo 1954) + defending champ/2026 hot streak (+15) -> 1969; 3% injury/scratch risk before Sept 23
    ("Sivasangari Subramaniam", 0.97, [(1.0, rank_to_elo(5) + 15, 50)]),
    # Satomi Watanabe: WR #6 (Elo 1915) + home court Nagoya (+20) -> 1935; 3% injury/scratch risk
    ("Satomi Watanabe",         0.97, [(1.0, rank_to_elo(6) + 20, 50)]),
    # Anahat Singh: WR #20 (Elo 1656), rising 18yo World Junior Champ (+25 momentum/upside, higher sd=65)
    ("Anahat Singh",            0.97, [(1.0, rank_to_elo(20) + 25, 65)]),
    # Aira Azman: WR #21 (Elo 1645), confirmed MAS #2 singles
    ("Aira Azman",              0.96, [(1.0, rank_to_elo(21), 55)]),
    # Chan Sin Yuk: ~WR #24 (in London Classic draw), 2023 AG silver medalist; ~82% plays singles for HKG
    ("Chan Sin Yuk",            0.82, [(1.0, rank_to_elo(24), 55)]),
    # Ho Tze-Lok: ~WR #27, 2025 Asian Individual Champ; ~78% plays singles for HKG
    ("Ho Tze-Lok",              0.78, [(1.0, rank_to_elo(27) + 10, 55)]),
    # Tomato Ho / Lee Ka Yi / other HKG if one of above plays mixed doubles
    ("Field_HKG_Other",         0.60, [(1.0, rank_to_elo(28), 55)]),
    # Rest of Asia (Tanvi Khanna, JPN #2, KOR)
    ("Field_Asia_8th",          1.00, [(1.0, rank_to_elo(45), 55)]),
]

ws_probs = sim_squash_bracket(women_squash, seed=556932)
print("\n=== Q4 (qid=556932) WOMEN'S SINGLES SQUASH ASIAN GAMES ===")
for k, v in sorted(ws_probs.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")


# ------------------------------------------------------------------------------
# MODEL 4: Q5 (qid=700005) — MEN'S SINGLES SQUASH ASIAN GAMES (T+25d)
# HUGE UPDATES:
#   Ng Eain Yow (MAS): WR #18 (struggled in 2026 PSA!), defending champ, confirmed singles.
#     Effective Elo: rank_to_elo(18)=1679, slight big-games experience +15, minus 2026 struggle -10 -> ~1684; higher form uncertainty (sd=65)
#   Abhay Singh (IND): WR #24 (1617), confirmed India #1 singles, rising! -> ~1625 (sd=55)
#   Noor Zaman (PAK): WR #29 (1576), surging rapidly (explicitly cited by Eain Yow & NST!) -> ~1595 (sd=65)
#   Abdulla Al-Tamimi (QAT): RUPTURED ACHILLES TENDON at Qatar Classic ~Oct 2025!
#     Just returning at London Classic Sept 1! Massive bimodality:
#       15% doesn't play singles / re-aggravates injury,
#       50% rusty/compromised movement (effective WR ~#48 -> Elo 1468),
#       35% recovers close to peak WR #20-24 (Elo 1615)!
#   Alex Lau (HKG): Reigning 2025 Asian Individual Champ (beat Al-Tamimi 3-0), ~WR #38-42 (not in London Classic top-24);
#     ~82% plays singles for HKG (vs mixed doubles), Asian Games/Championship overperformer (+20) -> Elo ~1530
#   Veer Chotrani (IND): WR #38 (1518), confirmed India #2 singles, in London Classic draw! -> Elo ~1525
#   Henry Leung (HKG): ~WR #42-48; ~75% plays singles -> Elo ~1490
#   Ryunosuke Tsukue (JPN): ~WR #45-50 + Nagoya home court (+25) -> Elo ~1505
#   Muhammad Ashab Irfan (PAK): in London Classic draw (~WR #35-45!), Pakistan #2 singles -> Elo ~1515
#   Sanjay Jeeva (MAS): WR #63, confirmed MAS #2 singles -> Elo ~1410
# ------------------------------------------------------------------------------
men_squash = [
    ("Ng Eain Yow",          0.96, [(0.35, rank_to_elo(22), 55), (0.65, rank_to_elo(16), 55)]),
    ("Abhay Singh",          0.97, [(1.00, rank_to_elo(23), 55)]),
    ("Noor Zaman",           0.95, [(1.00, rank_to_elo(27), 62)]),
    ("Abdulla Al-Tamimi",    0.85, [(0.55, rank_to_elo(48), 65), (0.45, rank_to_elo(23), 65)]),
    ("Alex Lau",             0.82, [(1.00, rank_to_elo(36), 58)]),
    ("Veer Chotrani",        0.96, [(1.00, rank_to_elo(37), 55)]),
    ("Muhammad Ashab Irfan", 0.90, [(1.00, rank_to_elo(40), 58)]),
    ("Ryunosuke Tsukue",     0.94, [(1.00, rank_to_elo(44) + 25, 55)]),
    ("Henry Leung",          0.75, [(1.00, rank_to_elo(46), 55)]),
    ("Field_Others_Jeeva",   1.00, [(1.00, rank_to_elo(60), 55)]),
]

ms_probs = sim_squash_bracket(men_squash, seed=700005)
print("\n=== Q5 (qid=700005) MEN'S SINGLES SQUASH ASIAN GAMES ===")
for k, v in sorted(ms_probs.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")
top5_ms = sorted([(k, v) for k, v in ms_probs.items() if not k.startswith("Field_")], key=lambda x: -x[1])[:5]
print("Top-5 sum =", round(sum(v for _, v in top5_ms), 4))
