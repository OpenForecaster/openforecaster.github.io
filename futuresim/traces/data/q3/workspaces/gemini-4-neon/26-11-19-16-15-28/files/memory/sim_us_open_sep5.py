import math
import random
from collections import defaultdict

# ============================================================
# HELPER: Power Devig & Shin-like calibration check
# ============================================================
def power_devig(probs_dict):
    # Find k > 1 such that sum(p^k) = 1
    vals = list(probs_dict.values())
    lo, hi = 1.0, 5.0
    for _ in range(80):
        mid = (lo + hi) / 2
        s = sum(v**mid for v in vals)
        if s > 1.0:
            lo = mid
        else:
            hi = mid
    k = (lo + hi) / 2
    return {name: round(v**k, 4) for name, v in probs_dict.items()}, k

def prop_devig(probs_dict):
    s = sum(probs_dict.values())
    return {name: round(v / s, 4) for name, v in probs_dict.items()}, s

# ============================================================
# 1. CHECK DEVIGGED SEP 5 MORNING DK PREDICTIONS MARKET
# ============================================================
print("=== MEN'S DK PREDICTIONS (Sep 5 7:46 AM ET, PRE-SATURDAY) ===")
men_dk = {
    "Carlos Alcaraz": 0.52,
    "Alexander Zverev": 0.21,
    "Ben Shelton": 0.14,
    "Taylor Fritz": 0.13,
    "Daniil Medvedev": 0.08,
    "Frances Tiafoe": 0.04,
    "Learner Tien": 0.04,
    "Jakub Mensik": 0.04,
    "Alex Michelsen": 0.03,
    # Remaining 15 players in draw as of Saturday morning:
    "Flavio Cobolli": 0.015,
    "Tommy Paul": 0.012,
    "Karen Khachanov": 0.012,
    "Stefanos Tsitsipas": 0.012,
    "Lorenzo Musetti": 0.010,
    "Francisco Cerundolo": 0.008,
    "Tomas Martin Etcheverry": 0.006,
    "Botic van de Zandschulp": 0.006,
    "Alexander Blockx": 0.006,
    "Alejandro Tabilo": 0.005,
    "Zizou Bergs": 0.005,
    "Luciano Darderi": 0.004,
    "Michael Zheng": 0.003,
    "Arthur Gea": 0.002,
    "Benjamin Bonzi": 0.002,
}
men_pow, km = power_devig(men_dk)
men_prop, sm = prop_devig(men_dk)
print(f"Raw sum={sm:.3f}, Power k={km:.3f}")
for p in ["Carlos Alcaraz", "Alexander Zverev", "Ben Shelton", "Taylor Fritz", "Daniil Medvedev",
          "Frances Tiafoe", "Learner Tien", "Jakub Mensik", "Alex Michelsen"]:
    print(f"  {p:20s}: raw={men_dk[p]:.3f} | power={men_pow[p]:.4f} | prop={men_prop[p]:.4f}")

print("\n=== WOMEN'S DK PREDICTIONS (Sep 5 7:46 AM ET, PRE-SATURDAY) ===")
women_dk = {
    "Aryna Sabalenka": 0.28,
    "Coco Gauff": 0.21,
    "Iga Swiatek": 0.15,
    "Jessica Pegula": 0.10,
    "Elena Rybakina": 0.08,
    "Alexandra Eala": 0.07,
    "Mirra Andreeva": 0.06,
    "Naomi Osaka": 0.06,
    "Marta Kostyuk": 0.05,
    "Amanda Anisimova": 0.05,
    # Remaining 14 players Saturday morning:
    "Linda Noskova": 0.040,
    "Madison Keys": 0.030,
    "Emma Navarro": 0.025,
    "Anna Kalinskaya": 0.020,
    "Iva Jovic": 0.020,
    "Elise Mertens": 0.015,
    "Zheng Qinwen": 0.015,
    "Sorana Cirstea": 0.010,
    "Anastasia Potapova": 0.010,
    "Taylor Townsend": 0.008,
    "Marie Bouzkova": 0.006,
    "Cristina Bucsa": 0.004,
    "Nikola Bartunkova": 0.004,
    "Yuliia Starodubtseva": 0.005,
}
wom_pow, kw = power_devig(women_dk)
wom_prop, sw = prop_devig(women_dk)
print(f"Raw sum={sw:.3f}, Power k={kw:.3f}")
for p in ["Aryna Sabalenka", "Coco Gauff", "Iga Swiatek", "Jessica Pegula", "Elena Rybakina",
          "Alexandra Eala", "Mirra Andreeva", "Naomi Osaka", "Marta Kostyuk", "Amanda Anisimova", "Linda Noskova"]:
    print(f"  {p:20s}: raw={women_dk[p]:.3f} | power={wom_pow[p]:.4f} | prop={wom_prop[p]:.4f}")

# ============================================================
# 2. EXACT BRACKET DP ENGINE
# ============================================================
def win_prob(p1, p2, elos, scale=400.0, h2h_adj=None):
    # Elo win prob in Bo5 (scale ~330 for Bo5, ~400 for Bo3)
    diff = elos[p1] - elos[p2]
    if h2h_adj:
        if (p1, p2) in h2h_adj:
            diff += h2h_adj[(p1, p2)]
        elif (p2, p1) in h2h_adj:
            diff -= h2h_adj[(p2, p1)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def bracket_dp(tree, elos, scale=400.0, h2h_adj=None):
    """tree is nested tuple of binary matches or player string."""
    if isinstance(tree, str):
        return {tree: 1.0}
    left_dist = bracket_dp(tree[0], elos, scale, h2h_adj)
    right_dist = bracket_dp(tree[1], elos, scale, h2h_adj)
    out = defaultdict(float)
    for p1, pr1 in left_dist.items():
        for p2, pr2 in right_dist.items():
            w1 = win_prob(p1, p2, elos, scale, h2h_adj)
            out[p1] += pr1 * pr2 * w1
            out[p2] += pr1 * pr2 * (1.0 - w1)
    return dict(out)

# ============================================================
# 3. MEN'S BRACKET MODEL (Bo5 scale=330)
# ============================================================
# Elo ratings (hard-court + current US Open form/fatigue adjusted):
# Note: Zverev fatigued after two 5-setters (9h26m), Alcaraz slight wrist variance,
# Medvedev sharp 9-0 sets, Shelton strong serve but 54 UEs vs Shapo,
# Michelsen 9-0 sets, Tien sharp, Khachanov beat FAA & Bonzi cleanly.
men_elos = {
    "Carlos Alcaraz": 2185,
    "Alexander Zverev": 2035,   # base ~2080 minus ~45 fatigue/form penalty
    "Ben Shelton": 1975,
    "Taylor Fritz": 1965,       # for pre-Saturday calibration check
    "Daniil Medvedev": 1975,
    "Frances Tiafoe": 1880,
    "Learner Tien": 1880,
    "Jakub Mensik": 1880,
    "Alex Michelsen": 1865,
    "Karen Khachanov": 1870,
    "Tommy Paul": 1875,
    "Stefanos Tsitsipas": 1865,
    "Flavio Cobolli": 1850,
    "Francisco Cerundolo": 1845,
    "Lorenzo Musetti": 1840,
    "Alexander Blockx": 1825,
    "Tomas Martin Etcheverry": 1790,
    "Luciano Darderi": 1795,
    "Alejandro Tabilo": 1825,
    "Botic van de Zandschulp": 1805,
    "Zizou Bergs": 1790,
    "Michael Zheng": 1745,
    "Arthur Gea": 1730,
    "Benjamin Bonzi": 1755,
}
men_h2h = {
    ("Carlos Alcaraz", "Tommy Paul"): 50,     # 5 straight wins vs Paul + Paul tired from 5-setter
    ("Carlos Alcaraz", "Ben Shelton"): 30,    # 3-0 H2H
    ("Daniil Medvedev", "Frances Tiafoe"): 35, # strong historical H2H on hard
}

men_tree_pre_sat = (
    ( # Top Half
        ( # Q1
            (("Alexander Zverev", "Alejandro Tabilo"), ("Luciano Darderi", "Lorenzo Musetti")),
            (("Michael Zheng", "Arthur Gea"), ("Zizou Bergs", "Botic van de Zandschulp"))
        ),
        ( # Q2
            (("Karen Khachanov", "Benjamin Bonzi"), ("Jakub Mensik", "Learner Tien")),
            (("Francisco Cerundolo", "Taylor Fritz"), ("Alexander Blockx", "Flavio Cobolli"))
        )
    ),
    ( # Bottom Half (R4 already set!)
        ( # Q3
            ("Daniil Medvedev", "Frances Tiafoe"),
            ("Alex Michelsen", "Tomas Martin Etcheverry")
        ),
        ( # Q4
            ("Ben Shelton", "Stefanos Tsitsipas"),
            ("Tommy Paul", "Carlos Alcaraz")
        )
    )
)

men_tree_post_sat = (
    ( # Top Half (4 R3 completed!)
        ( # Q1
            (("Alexander Zverev", "Alejandro Tabilo"), "Luciano Darderi"),
            (("Michael Zheng", "Arthur Gea"), ("Zizou Bergs", "Botic van de Zandschulp"))
        ),
        ( # Q2
            ("Karen Khachanov", ("Jakub Mensik", "Learner Tien")),
            ("Francisco Cerundolo", "Alexander Blockx")
        )
    ),
    ( # Bottom Half (R4 set!)
        ( # Q3
            ("Daniil Medvedev", "Frances Tiafoe"),
            ("Alex Michelsen", "Tomas Martin Etcheverry")
        ),
        ( # Q4
            ("Ben Shelton", "Stefanos Tsitsipas"),
            ("Tommy Paul", "Carlos Alcaraz")
        )
    )
)

print("\n=== MEN'S KEY MATCHUP WIN PROBS (Bo5 scale=330) ===")
for a, b in [
    ("Alexander Zverev", "Alejandro Tabilo"),
    ("Alexander Zverev", "Luciano Darderi"),
    ("Michael Zheng", "Arthur Gea"),
    ("Botic van de Zandschulp", "Zizou Bergs"),
    ("Learner Tien", "Jakub Mensik"),
    ("Learner Tien", "Karen Khachanov"),
    ("Francisco Cerundolo", "Alexander Blockx"),
    ("Daniil Medvedev", "Frances Tiafoe"),
    ("Alex Michelsen", "Tomas Martin Etcheverry"),
    ("Ben Shelton", "Stefanos Tsitsipas"),
    ("Carlos Alcaraz", "Tommy Paul"),
    ("Carlos Alcaraz", "Ben Shelton"),
    ("Carlos Alcaraz", "Daniil Medvedev"),
    ("Carlos Alcaraz", "Alexander Zverev"),
]:
    print(f"  {a:24s} vs {b:24s}: {win_prob(a, b, men_elos, 330, men_h2h):.3f}")

pre_m = bracket_dp(men_tree_pre_sat, men_elos, 330, men_h2h)
post_m = bracket_dp(men_tree_post_sat, men_elos, 330, men_h2h)
print("\n=== MEN'S TITLE DP: PRE-SAT (vs Power-Devig DK) -> POST-SAT ===")
for p, pr in sorted(post_m.items(), key=lambda x: -x[1])[:12]:
    dk_p = men_pow.get(p, 0.0)
    print(f"  {p:24s}: pre_sat={pre_m.get(p,0):.4f} (DK_pow={dk_p:.4f}) -> POST_SAT={pr:.4f}")
print(f"  (Fritz pre_sat={pre_m.get('Taylor Fritz',0):.4f}, DK_pow={men_pow['Taylor Fritz']:.4f} -> ELIMINATED)")
print(f"  Top-5 post_sat sum = {sum(v for _, v in sorted(post_m.items(), key=lambda x: -x[1])[:5]):.4f}")

# ============================================================
# 4. MONTE CARLO FOR Q408930 (FURTHEST US MAN)
# ============================================================
US_MEN = {"Ben Shelton", "Frances Tiafoe", "Alex Michelsen", "Learner Tien", "Tommy Paul", "Michael Zheng"}

def sim_men_once(tree, elos, scale=330.0, h2h_adj=None, round_num=0):
    # Returns (winner, dict of max round reached for all players in subtree)
    # Rounds: R3=3, R4=4, QF=5, SF=6, F=7, W=8
    pass

def sim_men_bracket(elos, scale=330.0, h2h_adj=None, N=200000):
    rng = random.Random(42)
    def play(a, b):
        return a if rng.random() < win_prob(a, b, elos, scale, h2h_adj) else b

    unique_wins = defaultdict(int)
    split_wins = defaultdict(float)
    reach_counts = {u: defaultdict(int) for u in US_MEN}
    tie_count = 0

    for _ in range(N):
        # Round reached: everyone starts at least R3 (3); those already in R4 start at 4!
        # Scores: R3 loss=3, R4 loss=4, QF loss=5, SF loss=6, F loss=7, Champ=8
        score = {
            "Ben Shelton": 4, "Frances Tiafoe": 4, "Alex Michelsen": 4, "Tommy Paul": 4,
            "Learner Tien": 3, "Michael Zheng": 3
        }
        # Remaining R3 matches:
        r4_1a = play("Alexander Zverev", "Alejandro Tabilo")
        r4_1b = "Luciano Darderi"
        r4_2a = play("Michael Zheng", "Arthur Gea")
        if r4_2a == "Michael Zheng": score["Michael Zheng"] = 4
        r4_2b = play("Zizou Bergs", "Botic van de Zandschulp")
        r4_3a = "Karen Khachanov"
        r4_3b = play("Jakub Mensik", "Learner Tien")
        if r4_3b == "Learner Tien": score["Learner Tien"] = 4
        r4_4a = "Francisco Cerundolo"
        r4_4b = "Alexander Blockx"

        # R4 matches (winners get 5 = QF):
        qf1 = play(r4_1a, r4_1b)
        qf2 = play(r4_2a, r4_2b)
        qf3 = play(r4_3a, r4_3b)
        qf4 = play(r4_4a, r4_4b)
        qf5 = play("Daniil Medvedev", "Frances Tiafoe")
        qf6 = play("Alex Michelsen", "Tomas Martin Etcheverry")
        qf7 = play("Ben Shelton", "Stefanos Tsitsipas")
        qf8 = play("Tommy Paul", "Carlos Alcaraz")
        for w in [qf1, qf2, qf3, qf4, qf5, qf6, qf7, qf8]:
            if w in score: score[w] = 5

        # QF matches (winners get 6 = SF):
        sf1 = play(qf1, qf2)
        sf2 = play(qf3, qf4)
        sf3 = play(qf5, qf6)
        sf4 = play(qf7, qf8)
        for w in [sf1, sf2, sf3, sf4]:
            if w in score: score[w] = 6

        # SF matches (winners get 7 = F):
        f1 = play(sf1, sf2)
        f2 = play(sf3, sf4)
        for w in [f1, f2]:
            if w in score: score[w] = 7

        # Final (winner gets 8 = Champ):
        champ = play(f1, f2)
        if champ in score: score[champ] = 8

        for u, sc in score.items():
            for r in range(4, sc + 1):
                reach_counts[u][r] += 1

        mx = max(score.values())
        top_us = [u for u, sc in score.items() if sc == mx]
        if len(top_us) == 1:
            unique_wins[top_us[0]] += 1
            split_wins[top_us[0]] += 1.0
        else:
            tie_count += 1
            for u in top_us:
                split_wins[u] += 1.0 / len(top_us)

    uniq_total = N - tie_count
    print(f"\n=== Q408930 FURTHEST US MAN MC (N={N}, Tie rate={tie_count/N:.3f}) ===")
    print(f"{'Player':18s} | {'CondUniq':>8s} | {'TieSplit':>8s} | {'P(R4+)':>6s} {'P(QF+)':>6s} {'P(SF+)':>6s} {'P(F+)':>6s}")
    for u in sorted(US_MEN, key=lambda x: -unique_wins[x]):
        cu = unique_wins[u] / uniq_total
        sp = split_wins[u] / N
        r4 = reach_counts[u][4] / N
        qf = reach_counts[u][5] / N
        sf = reach_counts[u][6] / N
        fn = reach_counts[u][7] / N
        print(f"{u:18s} | {cu:8.4f} | {sp:8.4f} | {r4:6.3f} {qf:6.3f} {sf:6.3f} {fn:6.3f}")

sim_men_bracket(men_elos, 330, men_h2h, N=200000)

# ============================================================
# 5. WOMEN'S BRACKET MODEL (Bo3 scale=400)
# ============================================================
women_elos = {
    "Aryna Sabalenka": 2125,
    "Coco Gauff": 2055,
    "Iga Swiatek": 2025,
    "Jessica Pegula": 1975,
    "Elena Rybakina": 1990,
    "Mirra Andreeva": 1955,
    "Naomi Osaka": 1935,
    "Linda Noskova": 1915,
    "Marta Kostyuk": 1900,
    "Amanda Anisimova": 1910,   # pre-sat
    "Madison Keys": 1885,       # pre-sat
    "Alexandra Eala": 1885,     # strong hard summer (10-2), though 0-2 vs Jovic
    "Iva Jovic": 1875,          # 2-0 vs Eala
    "Zheng Qinwen": 1875,       # Olympic champ, beat Keys from 0-5 down, slight rust/fatigue
    "Emma Navarro": 1870,
    "Anna Kalinskaya": 1850,
    "Elise Mertens": 1835,
    "Anastasia Potapova": 1825, # beat Anisimova 6-2 7-5
    "Sorana Cirstea": 1810,
    "Taylor Townsend": 1795,
    "Marie Bouzkova": 1810,
    "Cristina Bucsa": 1765,
    "Nikola Bartunkova": 1745,
    "Yuliia Starodubtseva": 1775, # beat Rybakina at RG
}
women_h2h = {
    ("Iva Jovic", "Alexandra Eala"): 30,       # 2-0 H2H in straight sets this year
    ("Yuliia Starodubtseva", "Elena Rybakina"): 25, # beat Rybakina at RG 2026
    ("Naomi Osaka", "Elise Mertens"): 25,      # 6-3 H2H, 2-0 in 2026 straight sets
    ("Aryna Sabalenka", "Taylor Townsend"): 30,
}

women_tree_pre_sat = (
    ( # Top Half (R4 set!)
        ( # Q1
            ("Aryna Sabalenka", "Taylor Townsend"),
            ("Marta Kostyuk", "Linda Noskova")
        ),
        ( # Q2
            ("Jessica Pegula", "Sorana Cirstea"),
            ("Anna Kalinskaya", "Emma Navarro")
        )
    ),
    ( # Bottom Half
        ( # Q3
            (("Mirra Andreeva", "Nikola Bartunkova"), ("Anastasia Potapova", "Amanda Anisimova")),
            (("Coco Gauff", "Cristina Bucsa"), ("Iva Jovic", "Alexandra Eala"))
        ),
        ( # Q4
            (("Iga Swiatek", "Marie Bouzkova"), ("Zheng Qinwen", "Madison Keys")),
            (("Naomi Osaka", "Elise Mertens"), ("Elena Rybakina", "Yuliia Starodubtseva"))
        )
    )
)

women_tree_post_sat = (
    ( # Top Half (R4 set!)
        ( # Q1
            ("Aryna Sabalenka", "Taylor Townsend"),
            ("Marta Kostyuk", "Linda Noskova")
        ),
        ( # Q2
            ("Jessica Pegula", "Sorana Cirstea"),
            ("Anna Kalinskaya", "Emma Navarro")
        )
    ),
    ( # Bottom Half (5 R3 completed!)
        ( # Q3
            ("Mirra Andreeva", "Anastasia Potapova"),
            ("Coco Gauff", ("Iva Jovic", "Alexandra Eala"))
        ),
        ( # Q4
            ("Iga Swiatek", "Zheng Qinwen"),
            (("Naomi Osaka", "Elise Mertens"), ("Elena Rybakina", "Yuliia Starodubtseva"))
        )
    )
)

print("\n=== WOMEN'S KEY MATCHUP WIN PROBS (Bo3 scale=400) ===")
for a, b in [
    ("Aryna Sabalenka", "Taylor Townsend"),
    ("Linda Noskova", "Marta Kostyuk"),
    ("Jessica Pegula", "Sorana Cirstea"),
    ("Emma Navarro", "Anna Kalinskaya"),
    ("Mirra Andreeva", "Anastasia Potapova"),
    ("Iva Jovic", "Alexandra Eala"),
    ("Coco Gauff", "Alexandra Eala"),
    ("Iga Swiatek", "Zheng Qinwen"),
    ("Naomi Osaka", "Elise Mertens"),
    ("Elena Rybakina", "Yuliia Starodubtseva"),
    ("Aryna Sabalenka", "Jessica Pegula"),
    ("Coco Gauff", "Mirra Andreeva"),
    ("Iga Swiatek", "Elena Rybakina"),
    ("Aryna Sabalenka", "Coco Gauff"),
]:
    print(f"  {a:24s} vs {b:24s}: {win_prob(a, b, women_elos, 400, women_h2h):.3f}")

pre_w = bracket_dp(women_tree_pre_sat, women_elos, 400, women_h2h)
post_w = bracket_dp(women_tree_post_sat, women_elos, 400, women_h2h)
print("\n=== WOMEN'S TITLE DP: PRE-SAT (vs Power-Devig DK) -> POST-SAT ===")
for p, pr in sorted(post_w.items(), key=lambda x: -x[1])[:12]:
    dk_p = wom_pow.get(p, 0.0)
    print(f"  {p:24s}: pre_sat={pre_w.get(p,0):.4f} (DK_pow={dk_p:.4f}) -> POST_SAT={pr:.4f}")
print(f"  Top-5 post_sat sum = {sum(v for _, v in sorted(post_w.items(), key=lambda x: -x[1])[:5]):.4f}")
