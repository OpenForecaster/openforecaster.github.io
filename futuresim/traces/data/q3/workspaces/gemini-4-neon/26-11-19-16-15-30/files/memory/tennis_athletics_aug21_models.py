import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — FRIDAY AUG 21, 2026
# Batch: tennis_and_athletics (260735, 372528, 22056, 354508, 30434)
# ==============================================================================

def win_prob(a, b, elos, h2h, scale=400.0):
    diff = elos[a] - elos[b]
    if (a, b) in h2h:
        diff += h2h[(a, b)]
    elif (b, a) in h2h:
        diff -= h2h[(b, a)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def solve_tree(tree, elos, h2h, scale=400.0):
    def rec(node):
        if isinstance(node, str):
            return {node: 1.0}
        l, r = node
        dl, dr = rec(l), rec(r)
        out = {}
        for a, pa in dl.items():
            out[a] = pa * sum(pb * win_prob(a, b, elos, h2h, scale) for b, pb in dr.items())
        for b, pb in dr.items():
            out[b] = pb * sum(pa * win_prob(b, a, elos, h2h, scale) for a, pa in dl.items())
        return out
    return rec(tree)


# ==============================================================================
# PART 1: Q1 (qid=260735) — WTA CINCINNATI 2026 — ONLY 5 PLAYERS REMAINING!
# ==============================================================================
# Verified bracket Fri Aug 21 evening:
#   TOP HALF:
#     SF1 Spot #1 LOCKED: Sara Bejlek (d. Keys 3-6, 6-4, 7-6(5) Fri afternoon!)
#     QF2 (Fri night): Coco Gauff (#4) vs Marta Kostyuk (#10)
#   BOTTOM HALF (SF2 SET FOR SAT AUG 22):
#     Jessica Pegula (#3, d. Anisimova Thu, carrying hip niggle, had Fri rest day)
#     vs
#     Iga Swiatek (#7, d. Rybakina 4-1 ret. Thu night, super fresh, 10-match HC win streak!)

wta_tree_play = (
    (
        "Sara Bejlek",
        ("Coco Gauff", "Marta Kostyuk"),
    ),
    (
        "Jessica Pegula",
        "Iga Swiatek",
    ),
)

wta_tree_pegula_wd = (
    (
        "Sara Bejlek",
        ("Coco Gauff", "Marta Kostyuk"),
    ),
    "Iga Swiatek",
)

wta_elo = {
    "Iga Swiatek": 2108,     # Defending champ, Toronto champ, 10-match HC streak, played <30m in QF (fresh!)
    "Coco Gauff": 2070,      # #4 seed, 2023 Cinci champ, crisp 6-3 6-2 vs Bouzkova, plays Fri night QF2
    "Marta Kostyuk": 2010,   # #10 seed, red-hot (crushed Andreeva 4-6 6-0 6-2), plays Fri night QF2
    "Jessica Pegula": 1995,  # Base ~2028 discounted -33 Elo for hip niggle/Anisimova grueling 3-setter (offset by Fri off)
    "Sara Bejlek": 1962,     # Upgraded +24 after backing up Sabalenka upset with Keys 3-6 6-4 7-6(5)! Already in SF1!
}

wta_h2h = {
    ("Iga Swiatek", "Jessica Pegula"): -12,  # Pegula tough fast-HC matchup historically (USO 24, Montreal 23), tempered by hip niggle -> ~64% Swiatek if played
    ("Iga Swiatek", "Coco Gauff"): +38,      # Swiatek leads H2H heavily (~11-4), tempered by fast US HC -> ~60.7% Swiatek
    ("Iga Swiatek", "Marta Kostyuk"): +35,   # Swiatek dominates matchup -> ~68.3% Swiatek
    ("Iga Swiatek", "Sara Bejlek"): +40,     # Major finals experience/consistency/defense gap -> ~74.5% Swiatek
    ("Coco Gauff", "Marta Kostyuk"): +18,    # 2023 Cinci champ + H2H edge -> ~61.0% Gauff
    ("Coco Gauff", "Sara Bejlek"): +35,      # Elite defense neutralizes Bejlek + pedigree -> ~69.5% Gauff
    ("Marta Kostyuk", "Sara Bejlek"): +25,   # Higher tier athlete/power -> ~60.3% Kostyuk
    ("Coco Gauff", "Jessica Pegula"): +12,   # Slight athleticism + Pegula hip edge -> ~61.6% Gauff
    ("Jessica Pegula", "Sara Bejlek"): +25,  # Flat fast-HC counterpunching & experience -> ~58.3% Pegula
}

def solve_wta(elos, h2h, scale, p_wd):
    r1 = solve_tree(wta_tree_play, elos, h2h, scale)
    r2 = solve_tree(wta_tree_pegula_wd, elos, h2h, scale)
    return {k: (1.0 - p_wd) * r1.get(k, 0.0) + p_wd * r2.get(k, 0.0) for k in elos}

wta_regimes = [
    ("Base (Balanced + Moderate Pegula Hip Discount, wd=7%)", wta_elo, wta_h2h, 400.0, 0.07, 0.45),
    ("Pegula Compromised (wd=16%, -40 Elo)", {
        **wta_elo, "Jessica Pegula": wta_elo["Jessica Pegula"] - 40
    }, wta_h2h, 400.0, 0.16, 0.20),
    ("Pegula Recovers w/ Fri Rest (wd=2%, +35 Elo)", {
        **wta_elo, "Jessica Pegula": wta_elo["Jessica Pegula"] + 35
    }, wta_h2h, 400.0, 0.02, 0.15),
    ("Bejlek & Kostyuk Hot / High-Parity Chaos", {
        **wta_elo,
        "Sara Bejlek": wta_elo["Sara Bejlek"] + 30,
        "Marta Kostyuk": wta_elo["Marta Kostyuk"] + 20,
        "Iga Swiatek": wta_elo["Iga Swiatek"] - 15,
    }, wta_h2h, 425.0, 0.06, 0.20),
]

print("=== Q1 (260735) WTA CINCINNATI — FRI AUG 21 (EXHAUSTIVE 5 PLAYERS) ===")
for a, b in [
    ("Iga Swiatek", "Jessica Pegula"),
    ("Coco Gauff", "Marta Kostyuk"),
    ("Coco Gauff", "Sara Bejlek"),
    ("Marta Kostyuk", "Sara Bejlek"),
    ("Iga Swiatek", "Coco Gauff"),
    ("Iga Swiatek", "Marta Kostyuk"),
    ("Iga Swiatek", "Sara Bejlek"),
    ("Jessica Pegula", "Coco Gauff"),
]:
    print(f"  P({a:15s} d. {b:15s}) = {win_prob(a, b, wta_elo, wta_h2h):.3f}")

wta_blend = {}
for name, elos, h2h, sc, pwd, w in wta_regimes:
    r = solve_wta(elos, h2h, sc, pwd)
    print(f"  [{name:55s} w={w:.2f}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(r.items(), key=lambda x: -x[1])))
    for k, v in r.items():
        wta_blend[k] = wta_blend.get(k, 0.0) + w * v

print("FINAL WTA BLEND (sum =", round(sum(wta_blend.values()), 4), "):")
for k, v in sorted(wta_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:20s}: {v:.4f}")


# ==============================================================================
# PART 2: Q2 (qid=372528) — ATP CINCINNATI 2026 — ONLY 5 PLAYERS REMAINING!
# ==============================================================================
# Verified bracket Fri Aug 21 evening:
#   TOP HALF (SF1 SET FOR SAT AUG 22 — BOTH GOT FRIDAY OFF!):
#     Flavio Cobolli (#7, d. Paul Thu in 3 sets, 4th straight 3-setter, gets Fri off)
#     vs
#     Arthur Fils (#21, d. Tirante Thu night 6-3 6-2 in 64 min! Demolished de Minaur too! Super fresh!)
#   BOTTOM HALF:
#     SF2 Spot #1 LOCKED: Brandon Nakashima (#27, d. Fritz Fri 7-6(9) 4-6 6-3! 12-2 last 14 HC, Montreal F!)
#     QF4 (Fri night): Lorenzo Musetti (#10) vs Frances Tiafoe (#17)

atp_tree = (
    (
        "Flavio Cobolli",
        "Arthur Fils",
    ),
    (
        "Brandon Nakashima",
        ("Lorenzo Musetti", "Frances Tiafoe"),
    ),
)

atp_elo = {
    "Arthur Fils": 2042,        # Blazing form (6-3 6-4 de Minaur, 6-3 6-2 Tirante in 64m), Friday off, 5th M1000 QF+ of 2026!
    "Brandon Nakashima": 2022,  # Upgraded +32 after beating Fritz 7-6(9) 4-6 6-3! 12-2 summer HC, Montreal F, guaranteed #16!
    "Flavio Cobolli": 1995,     # #7 seed, RG finalist, Acapulco HC champ, Friday off (4x 3-setters slight wear)
    "Lorenzo Musetti": 1995,    # #10 seed, crisp wins over Zheng & Faria, plays Fri night QF4 -> Sat SF2 -> Sun F
    "Frances Tiafoe": 1985,     # #17 seed, 2024 Cinci finalist, d. #2 FAA 6-3 6-4, 4-0 last 4 vs Top 10, home crowd!
}

atp_h2h = {
    ("Arthur Fils", "Flavio Cobolli"): +20,       # Fils much fresher + bigger fast-HC serve/power (~59.5% Fils)
    ("Arthur Fils", "Brandon Nakashima"): +20,    # Fils fresher (vs Nakashima 3-week heavy load) + bigger ceiling (~55.7% Fils)
    ("Arthur Fils", "Lorenzo Musetti"): +20,      # Fast Cinci HC power + rest edge (~59.5% Fils)
    ("Arthur Fils", "Frances Tiafoe"): +12,       # Freshness + form edge vs Tiafoe crowd (~59.8% Fils)
    ("Frances Tiafoe", "Lorenzo Musetti"): +15,   # Fast Cinci HC + US home crowd (2024 finalist) -> ~50.7% Tiafoe!
    ("Brandon Nakashima", "Lorenzo Musetti"): +10,# Fast HC + day-session rest edge over Fri-night QF4 (~55.3% Nakashima)
    ("Brandon Nakashima", "Frances Tiafoe"): -5,  # Tiafoe crowd/big-stage offsets some Elo gap (~54.6% Nakashima)
    ("Flavio Cobolli", "Lorenzo Musetti"): +10,   # Acapulco HC champ + Friday rest vs 3 straight days (~51.4% Cobolli)
}

atp_regimes = [
    ("Base (Balanced + Rest + Fast-HC)", atp_elo, atp_h2h, 400.0, 0.45),
    ("Fresh Weapons (Fils + Tiafoe surge; Cobolli & Nakashima cumulative wear)", {
        **atp_elo,
        "Arthur Fils": atp_elo["Arthur Fils"] + 25,
        "Frances Tiafoe": atp_elo["Frances Tiafoe"] + 20,
        "Flavio Cobolli": atp_elo["Flavio Cobolli"] - 22,
        "Brandon Nakashima": atp_elo["Brandon Nakashima"] - 20,
    }, atp_h2h, 395.0, 0.25),
    ("Hot Summer / Grit (Nakashima + Cobolli + Musetti)", {
        **atp_elo,
        "Brandon Nakashima": atp_elo["Brandon Nakashima"] + 25,
        "Flavio Cobolli": atp_elo["Flavio Cobolli"] + 22,
        "Lorenzo Musetti": atp_elo["Lorenzo Musetti"] + 15,
        "Arthur Fils": atp_elo["Arthur Fils"] - 18,
    }, atp_h2h, 410.0, 0.20),
    ("High-Parity 2026 Cinci Chaos", atp_elo, atp_h2h, 460.0, 0.10),
]

print("\n=== Q2 (372528) ATP CINCINNATI — FRI AUG 21 (EXHAUSTIVE 5 PLAYERS) ===")
for a, b in [
    ("Arthur Fils", "Flavio Cobolli"),
    ("Frances Tiafoe", "Lorenzo Musetti"),
    ("Brandon Nakashima", "Lorenzo Musetti"),
    ("Brandon Nakashima", "Frances Tiafoe"),
    ("Arthur Fils", "Brandon Nakashima"),
    ("Flavio Cobolli", "Brandon Nakashima"),
]:
    print(f"  P({a:18s} d. {b:18s}) = {win_prob(a, b, atp_elo, atp_h2h):.3f}")

atp_blend = {}
for name, elos, h2h, sc, w in atp_regimes:
    r = solve_tree(atp_tree, elos, h2h, sc)
    print(f"  [{name:70s} w={w:.2f}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(r.items(), key=lambda x: -x[1])))
    for k, v in r.items():
        atp_blend[k] = atp_blend.get(k, 0.0) + w * v

print("FINAL ATP BLEND (sum =", round(sum(atp_blend.values()), 4), "):")
for k, v in sorted(atp_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:22s}: {v:.4f}")


# ==============================================================================
# PART 3: Q5 (qid=30434) — MEN'S JAVELIN ULTIMATE CHAMPIONSHIP (BUDAPEST SEPT 13)
# ==============================================================================
# 6-throw competition (max of 6 throws with ~15% foul rate) + athlete-level meet-day form variance + availability/DNS prob.
# Calibrated to 2026 marks:
#   - Pathirage: 92.62m WL (Rome), 89.75m (CWG gold), 88.14m (Lausanne win), Doha win -> 3 DL wins + CWG gold!
#   - Julian Weber: 90.40m CR (Aug 15 Euro Gold! 2nd man >90m in 2026, 91.51m PB in 2025!), withdrew last-minute from Lausanne (mild 8% health/DNS risk)
#   - Neeraj Chopra: 88.05m SB (Lausanne 2nd, -9cm!), 85.83m (CWG silver), 90.23m PB, elite championship peaking!
#   - Anderson Peters: 86.69m SB (Lausanne 3rd), 93.07m PB, 2x World Champ, locked for Brussels DL Final!
#   - Curtis Thompson: 87.59m SB (NYC GP Jul 25), 2025 Worlds bronze, BUT bombed to 78.13m (6th) in Lausanne!
#   - Keshorn Walcott: 2025 World Champion (auto-qualified!), 83.71m (Lausanne 4th), big-meet gamer
#   - Arshad Nadeem: 2024 Olympic Champ (92.97m OR), BUT 75.39m/77.41m (9th CWG) & focusing on Asian Games (Sept 19) -> high skip/out-of-form prob!
#   - Field others (Vadlejch 77.32m/82.88m, Nick Thumm, Minichello 80.06m, Yego, Gailums)

def sim_javelin(n_trials=200000, seed=42):
    rng = random.Random(seed)
    # (name, p_compete, mean_best_meet_m, meet_day_sd, throw_sd, peak_bonus_prob, peak_bonus_m)
    # Note: In javelin, each athlete has a day-level form draw ~ N(mu, meet_sd) and takes 6 throws ~ N(day_form, throw_sd) with foul_rate=0.18.
    # Let's parametrize directly on expected meet-best distribution (which is approx Normal/skew-normal around season-best - 2m to -1m):
    # Wait — simulating 6 throws directly is even cleaner!
    # If a throw is N(day_mu, 2.3) and 5 valid throws, E[max_5] ≈ day_mu + 1.16*2.3 = day_mu + 2.67m!
    athletes = [
        # name, p_start, base_throw_mu, day_sd, throw_sd
        # Expected best = base_throw_mu + 2.65m (approx)
        ("Rumesh Tharanga Pathirage", 0.96, 86.4, 2.1, 2.3),  # E[best] ~ 89.1m, 90th pct ~ 91.8m
        ("Julian Weber",              0.89, 85.7, 2.2, 2.3),  # E[best] ~ 88.4m, 90th pct ~ 91.2m (slightly lower p_start due to Lausanne WD)
        ("Neeraj Chopra",             0.95, 85.2, 1.9, 2.1),  # E[best] ~ 87.7m, super consistent championship thrower!
        ("Anderson Peters",           0.95, 83.6, 2.4, 2.5),  # E[best] ~ 86.5m, high ceiling (93m PB), wider variance
        ("Curtis Thompson",           0.90, 82.0, 2.6, 2.5),  # E[best] ~ 84.9m (87.59m NYC vs 78.13m Lausanne -> huge variance!)
        ("Keshorn Walcott",           0.94, 81.8, 2.4, 2.4),  # E[best] ~ 84.6m, 2025 World Champ gamer
        ("Arshad Nadeem",             0.55, 82.0, 3.3, 2.7),  # 45% skips for Asian Games; huge upside if fit, poor CWG form
        ("Field_Other_1",             0.98, 81.2, 2.3, 2.3),  # Vadlejch / Thumm / Minichello / Gailums
        ("Field_Other_2",             0.98, 80.5, 2.3, 2.3),
    ]
    wins = Counter()
    for _ in range(n_trials):
        best_m = -1.0
        winner = None
        for name, p_start, mu, dsd, tsd in athletes:
            if rng.random() > p_start:
                continue
            day_mu = rng.gauss(mu, dsd)
            ath_best = 0.0
            for _t in range(6):
                if rng.random() < 0.16:
                    continue
                val = rng.gauss(day_mu, tsd)
                if val > ath_best:
                    ath_best = val
            if ath_best > best_m:
                best_m = ath_best
                winner = name
        wins[winner] += 1
    return {k: c / n_trials for k, c in wins.most_common()}

# Run 3 javelin regimes and blend:
# R1: Base (above)
# R2: Pathirage peak 92m dominance / Weber fully fit
# R3: Big-stage veteran surge (Chopra/Peters/Walcott/Nadeem peak in Budapest)
def sim_javelin_custom(athletes, n_trials=150000, seed=42):
    rng = random.Random(seed)
    wins = Counter()
    for _ in range(n_trials):
        best_m = -1.0
        winner = None
        for name, p_start, mu, dsd, tsd in athletes:
            if rng.random() > p_start:
                continue
            day_mu = rng.gauss(mu, dsd)
            ath_best = 0.0
            for _t in range(6):
                if rng.random() < 0.16:
                    continue
                val = rng.gauss(day_mu, tsd)
                if val > ath_best:
                    ath_best = val
            if ath_best > best_m:
                best_m = ath_best
                winner = name
        wins[winner] += 1
    return {k: c / n_trials for k, c in wins.items()}

jav_base = [
    ("Rumesh Tharanga Pathirage", 0.96, 86.4, 2.1, 2.3),
    ("Julian Weber",              0.89, 85.7, 2.2, 2.3),
    ("Neeraj Chopra",             0.95, 85.2, 1.9, 2.1),
    ("Anderson Peters",           0.95, 83.6, 2.4, 2.5),
    ("Curtis Thompson",           0.90, 82.0, 2.6, 2.5),
    ("Keshorn Walcott",           0.94, 81.8, 2.4, 2.4),
    ("Arshad Nadeem",             0.55, 82.0, 3.3, 2.7),
    ("Field_Other_1",             0.98, 81.2, 2.3, 2.3),
    ("Field_Other_2",             0.98, 80.5, 2.3, 2.3),
]
jav_90m_duel = [
    ("Rumesh Tharanga Pathirage", 0.96, 87.0, 2.1, 2.3),
    ("Julian Weber",              0.94, 86.4, 2.1, 2.3),
    ("Neeraj Chopra",             0.95, 84.8, 1.9, 2.1),
    ("Anderson Peters",           0.95, 83.3, 2.4, 2.5),
    ("Curtis Thompson",           0.90, 81.8, 2.6, 2.5),
    ("Keshorn Walcott",           0.94, 81.5, 2.4, 2.4),
    ("Arshad Nadeem",             0.45, 81.2, 3.2, 2.7),
    ("Field_Other_1",             0.98, 81.0, 2.3, 2.3),
    ("Field_Other_2",             0.98, 80.2, 2.3, 2.3),
]
jav_champs = [
    ("Rumesh Tharanga Pathirage", 0.95, 85.7, 2.3, 2.3),
    ("Julian Weber",              0.84, 85.2, 2.3, 2.3),
    ("Neeraj Chopra",             0.96, 85.8, 1.8, 2.1),
    ("Anderson Peters",           0.95, 84.3, 2.5, 2.5),
    ("Curtis Thompson",           0.90, 82.5, 2.6, 2.5),
    ("Keshorn Walcott",           0.95, 82.6, 2.4, 2.4),
    ("Arshad Nadeem",             0.65, 83.0, 3.4, 2.7),
    ("Field_Other_1",             0.98, 81.5, 2.3, 2.3),
    ("Field_Other_2",             0.98, 80.8, 2.3, 2.3),
]

j1 = sim_javelin_custom(jav_base, 150000, 11)
j2 = sim_javelin_custom(jav_90m_duel, 150000, 22)
j3 = sim_javelin_custom(jav_champs, 150000, 33)

j_blend = {}
for k in set(j1) | set(j2) | set(j3):
    j_blend[k] = 0.50 * j1.get(k, 0) + 0.25 * j2.get(k, 0) + 0.25 * j3.get(k, 0)

print("\n=== Q5 (30434) MEN'S JAVELIN ULTIMATE CHAMPIONSHIP (SEPT 13) ===")
for k, v in sorted(j_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: blend={v:.4f} (base={j1.get(k,0):.3f}, 90m={j2.get(k,0):.3f}, champs={j3.get(k,0):.3f})")
top5_j = sorted([(k, v) for k, v in j_blend.items() if not k.startswith("Field_")], key=lambda x: -x[1])[:5]
print("Top-5 named sum =", round(sum(v for _, v in top5_j), 4))
