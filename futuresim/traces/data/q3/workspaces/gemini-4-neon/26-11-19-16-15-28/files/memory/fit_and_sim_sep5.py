import math
import random
from collections import defaultdict

# ============================================================
# 1. EXACT SHIN / ADDITIVE / POWER DEVIG COMPARISON
# ============================================================
def shin_devig(probs):
    # Standard Shin model: p_i = (sqrt(z^2 + 4*(1-z)*q_i^2/S) - z) / (2*(1-z))
    S = sum(probs.values())
    lo, hi = 0.0, 0.5
    for _ in range(80):
        z = (lo + hi) / 2
        tot = sum((math.sqrt(z*z + 4*(1-z)*(q*q)/S) - z) / (2*(1-z)) for q in probs.values())
        if tot > 1.0:
            lo = z
        else:
            hi = z
    z = (lo + hi) / 2
    return {k: (math.sqrt(z*z + 4*(1-z)*(q*q)/S) - z) / (2*(1-z)) for k, q in probs.items()}, z

def power_devig(probs):
    lo, hi = 1.0, 5.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if sum(v**mid for v in probs.values()) > 1.0:
            lo = mid
        else:
            hi = mid
    k = (lo + hi) / 2
    return {p: v**k for p, v in probs.items()}, k

def win_prob(p1, p2, elos, scale, h2h=None):
    diff = elos[p1] - elos[p2]
    if h2h:
        if (p1, p2) in h2h: diff += h2h[(p1, p2)]
        elif (p2, p1) in h2h: diff -= h2h[(p2, p1)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def bracket_dp(tree, elos, scale, h2h=None):
    if isinstance(tree, str):
        return {tree: 1.0}
    L = bracket_dp(tree[0], elos, scale, h2h)
    R = bracket_dp(tree[1], elos, scale, h2h)
    out = defaultdict(float)
    for p1, pr1 in L.items():
        for p2, pr2 in R.items():
            w1 = win_prob(p1, p2, elos, scale, h2h)
            out[p1] += pr1 * pr2 * w1
            out[p2] += pr1 * pr2 * (1.0 - w1)
    return dict(out)

# ============================================================
# 2. MEN'S TARGETS FROM SEP 5 7:46 AM ET DK PREDICTIONS
# ============================================================
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
men_shin, zm = shin_devig(men_dk)
men_pow, km = power_devig(men_dk)

print("=== MEN'S DEVIGGED SEP 5 MORNING TARGETS (SHIN vs POWER) ===")
for p in ["Carlos Alcaraz", "Alexander Zverev", "Ben Shelton", "Taylor Fritz", "Daniil Medvedev",
          "Frances Tiafoe", "Learner Tien", "Jakub Mensik", "Alex Michelsen", "Karen Khachanov", "Tommy Paul"]:
    print(f"  {p:22s}: raw={men_dk[p]:.3f} | shin={men_shin[p]:.4f} | pow={men_pow[p]:.4f} | mid={(men_shin[p]+men_pow[p])/2:.4f}")

# Fit Men's Elos to match the midpoint of Shin & Power devigged DK Predictions (scale=400 for realistic Bo5 upset dispersion!)
men_tree_pre = (
    (
        ((("Alexander Zverev", "Alejandro Tabilo"), ("Luciano Darderi", "Lorenzo Musetti")),
         (("Michael Zheng", "Arthur Gea"), ("Zizou Bergs", "Botic van de Zandschulp"))),
        ((("Karen Khachanov", "Benjamin Bonzi"), ("Jakub Mensik", "Learner Tien")),
         (("Francisco Cerundolo", "Taylor Fritz"), ("Alexander Blockx", "Flavio Cobolli")))
    ),
    (
        (("Daniil Medvedev", "Frances Tiafoe"), ("Alex Michelsen", "Tomas Martin Etcheverry")),
        (("Ben Shelton", "Stefanos Tsitsipas"), ("Tommy Paul", "Carlos Alcaraz"))
    )
)
men_tree_post = (
    (
        ((("Alexander Zverev", "Alejandro Tabilo"), "Luciano Darderi"),
         (("Michael Zheng", "Arthur Gea"), ("Zizou Bergs", "Botic van de Zandschulp"))),
        (("Karen Khachanov", ("Jakub Mensik", "Learner Tien")),
         ("Francisco Cerundolo", "Alexander Blockx"))
    ),
    (
        (("Daniil Medvedev", "Frances Tiafoe"), ("Alex Michelsen", "Tomas Martin Etcheverry")),
        (("Ben Shelton", "Stefanos Tsitsipas"), ("Tommy Paul", "Carlos Alcaraz"))
    )
)

# Let's fit Elos via iterative log-odds update so pre-Sat DP matches Shin/Power targets!
def fit_elos(tree_pre, targets, init_elos, scale=400.0, h2h=None, steps=120):
    elos = dict(init_elos)
    for _ in range(steps):
        cur = bracket_dp(tree_pre, elos, scale, h2h)
        for p, tgt in targets.items():
            if tgt > 0 and cur.get(p, 0) > 0:
                elos[p] += 55.0 * math.log(tgt / cur[p])
        # anchor mean
        mean_e = sum(elos.values()) / len(elos)
        for p in elos: elos[p] -= (mean_e - 1850.0)
    return elos

men_targets_shin = {k: v for k, v in men_shin.items()}
men_targets_pow  = {k: v for k, v in men_pow.items()}
men_targets_mid  = {k: 0.5*(men_shin[k] + men_pow[k]) for k in men_dk}

men_init = {k: 1850.0 for k in men_dk}
# Anchor lower-tier players sensibly where title odds alone have low leverage
men_h2h = {
    ("Carlos Alcaraz", "Tommy Paul"): 40,
    ("Daniil Medvedev", "Frances Tiafoe"): 25,
}

# Fit TWO models: (A) Shin-fitted (higher favorite share), (B) Power-fitted (lower favorite share, higher tail)
# Wait: also run a Fundamental-blended model where Alcaraz isn't 53% (accounts for wrist layoff risk + Shelton 54 UEs)
for label, tgts, sc in [
    ("SHIN_400", men_targets_shin, 400.0),
    ("MID_400",  men_targets_mid,  400.0),
    ("POW_400",  men_targets_pow,  400.0),
]:
    elos = fit_elos(men_tree_pre, tgts, men_init, sc, men_h2h, steps=150)
    pre_dp = bracket_dp(men_tree_pre, elos, sc, men_h2h)
    post_dp = bracket_dp(men_tree_post, elos, sc, men_h2h)
    print(f"\n--- MEN FIT: {label} ---")
    print("  Matchups:")
    for a, b in [
        ("Carlos Alcaraz", "Tommy Paul"),
        ("Carlos Alcaraz", "Ben Shelton"),
        ("Carlos Alcaraz", "Alexander Zverev"),
        ("Ben Shelton", "Stefanos Tsitsipas"),
        ("Daniil Medvedev", "Frances Tiafoe"),
        ("Alex Michelsen", "Tomas Martin Etcheverry"),
        ("Alexander Zverev", "Alejandro Tabilo"),
        ("Alexander Zverev", "Luciano Darderi"),
        ("Learner Tien", "Jakub Mensik"),
        ("Learner Tien", "Karen Khachanov"),
        ("Francisco Cerundolo", "Alexander Blockx"),
        ("Michael Zheng", "Arthur Gea"),
        ("Botic van de Zandschulp", "Zizou Bergs"),
    ]:
        print(f"    {a:23s} vs {b:23s}: {win_prob(a, b, elos, sc, men_h2h):.3f}")
    print("  Post-Sat Title Probs (Top 10):")
    top10 = sorted(post_dp.items(), key=lambda x: -x[1])[:10]
    for p, v in top10:
        print(f"    {p:23s}: pre={pre_dp[p]:.4f} (tgt={tgts[p]:.4f}) -> POST={v:.4f}")
    print(f"    Top-5 sum = {sum(v for _, v in top10[:5]):.4f}")

# ============================================================
# 3. RUN MONTE CARLO FOR Q408930 UNDER MARKET-FITTED ELOS + SENSITIVITY
# ============================================================
US_MEN = {"Ben Shelton", "Frances Tiafoe", "Alex Michelsen", "Learner Tien", "Tommy Paul", "Michael Zheng"}

def sim_us_men(elos, sc=400.0, h2h=None, N=250000, label=""):
    rng = random.Random(123)
    def play(a, b):
        return a if rng.random() < win_prob(a, b, elos, sc, h2h) else b
    uniq = defaultdict(int)
    split = defaultdict(float)
    reach = {u: defaultdict(int) for u in US_MEN}
    ties = 0
    for _ in range(N):
        score = {"Ben Shelton":4, "Frances Tiafoe":4, "Alex Michelsen":4, "Tommy Paul":4, "Learner Tien":3, "Michael Zheng":3}
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

        qfs = [
            play(r4_1a, r4_1b), play(r4_2a, r4_2b),
            play(r4_3a, r4_3b), play(r4_4a, r4_4b),
            play("Daniil Medvedev", "Frances Tiafoe"),
            play("Alex Michelsen", "Tomas Martin Etcheverry"),
            play("Ben Shelton", "Stefanos Tsitsipas"),
            play("Tommy Paul", "Carlos Alcaraz"),
        ]
        for w in qfs:
            if w in score: score[w] = 5
        sfs = [play(qfs[0], qfs[1]), play(qfs[2], qfs[3]), play(qfs[4], qfs[5]), play(qfs[6], qfs[7])]
        for w in sfs:
            if w in score: score[w] = 6
        fs = [play(sfs[0], sfs[1]), play(sfs[2], sfs[3])]
        for w in fs:
            if w in score: score[w] = 7
        ch = play(fs[0], fs[1])
        if ch in score: score[ch] = 8

        for u, s in score.items():
            for r in range(4, s+1): reach[u][r] += 1
        mx = max(score.values())
        tops = [u for u, s in score.items() if s == mx]
        if len(tops) == 1:
            uniq[tops[0]] += 1
            split[tops[0]] += 1.0
        else:
            ties += 1
            for u in tops: split[u] += 1.0 / len(tops)
    un = N - ties
    print(f"\n=== Q408930 MC [{label}] (N={N}, TieRate={ties/N:.3f}) ===")
    print(f"{'Player':16s} | {'CondUniq':>8s} | {'TieSplit':>8s} | {'P(QF+)':>6s} {'P(SF+)':>6s} {'P(F+)':>6s} {'P(W)':>6s}")
    for u in sorted(US_MEN, key=lambda x: -uniq[x]):
        print(f"{u:16s} | {uniq[u]/un:8.4f} | {split[u]/N:8.4f} | {reach[u][5]/N:6.3f} {reach[u][6]/N:6.3f} {reach[u][7]/N:6.3f} {reach[u][8]/N:6.3f}")

elos_mid = fit_elos(men_tree_pre, men_targets_mid, men_init, 400.0, men_h2h, steps=150)
sim_us_men(elos_mid, 400.0, men_h2h, N=250000, label="MID_MARKET_FIT")

# Sensitivity: What if Michelsen vs Etcheverry is 64% (slightly tighter than Elo fit?), Shelton vs Tsitsipas 68%, Tiafoe vs Medvedev 35%, Tien vs Khachanov 52%?
elos_sens = dict(elos_mid)
# Check actual Elo diffs first and run a fundamental-anchored sensitivity!
elos_sens["Ben Shelton"] -= 25          # respect 54 UEs vs Shapovalov & Tsitsipas resurgence
elos_sens["Stefanos Tsitsipas"] += 40
elos_sens["Daniil Medvedev"] += 35      # Medvedev 9-0 sets, crisp form vs Tiafoe
elos_sens["Tomas Martin Etcheverry"] += 35 # Etcheverry beat Navone easily, don't over-credit Michelsen to 75%+
elos_sens["Karen Khachanov"] += 40      # Khachanov beat FAA & Bonzi in straight sets!
elos_sens["Francisco Cerundolo"] += 35  # Cerundolo beat Fritz!
elos_sens["Alexander Blockx"] += 35     # Blockx crushed Cobolli!
sim_us_men(elos_sens, 400.0, men_h2h, N=250000, label="FUNDAMENTAL_SENSITIVITY")

print("\n  [FUNDAMENTAL_SENSITIVITY Matchups]:")
for a, b in [
    ("Carlos Alcaraz", "Tommy Paul"),
    ("Carlos Alcaraz", "Ben Shelton"),
    ("Ben Shelton", "Stefanos Tsitsipas"),
    ("Daniil Medvedev", "Frances Tiafoe"),
    ("Alex Michelsen", "Tomas Martin Etcheverry"),
    ("Alexander Zverev", "Alejandro Tabilo"),
    ("Learner Tien", "Jakub Mensik"),
    ("Learner Tien", "Karen Khachanov"),
    ("Learner Tien", "Francisco Cerundolo"),
    ("Michael Zheng", "Arthur Gea"),
]:
    print(f"    {a:23s} vs {b:23s}: {win_prob(a, b, elos_sens, 400.0, men_h2h):.3f}")

# Also print Post-Sat Title DP for FUNDAMENTAL_SENSITIVITY!
post_sens = bracket_dp(men_tree_post, elos_sens, 400.0, men_h2h)
print("  [FUNDAMENTAL_SENSITIVITY Men Title Top 8]:")
for p, v in sorted(post_sens.items(), key=lambda x: -x[1])[:8]:
    print(f"    {p:23s}: {v:.4f}")

# ============================================================
# 4. WOMEN'S MARKET-FITTED MODEL + POST-SAT CONDITIONING
# ============================================================
women_dk = {
    "Aryna Sabalenka": 0.28,
    "Coco Gauff": 0.21,
    "Iga Swiatek": 0.15,
    "Jessica Pegula": 0.10,
    "Elena Rybakina": 0.08,
    "Alexandra Eala": 0.050,   # haircut retail pop 0.07 -> 0.05 (0-2 vs Jovic this yr)
    "Mirra Andreeva": 0.06,
    "Naomi Osaka": 0.06,
    "Marta Kostyuk": 0.045,
    "Amanda Anisimova": 0.05,
    "Linda Noskova": 0.045,
    "Madison Keys": 0.030,
    "Emma Navarro": 0.025,
    "Anna Kalinskaya": 0.020,
    "Iva Jovic": 0.025,
    "Elise Mertens": 0.015,
    "Zheng Qinwen": 0.015,
    "Sorana Cirstea": 0.012,
    "Anastasia Potapova": 0.012,
    "Taylor Townsend": 0.009,
    "Marie Bouzkova": 0.007,
    "Cristina Bucsa": 0.005,
    "Nikola Bartunkova": 0.005,
    "Yuliia Starodubtseva": 0.006,
}
wom_shin, zw = shin_devig(women_dk)
wom_pow, kw = power_devig(women_dk)
wom_mid = {k: 0.5*(wom_shin[k] + wom_pow[k]) for k in women_dk}

women_tree_pre = (
    (
        (("Aryna Sabalenka", "Taylor Townsend"), ("Marta Kostyuk", "Linda Noskova")),
        (("Jessica Pegula", "Sorana Cirstea"), ("Anna Kalinskaya", "Emma Navarro"))
    ),
    (
        ((("Mirra Andreeva", "Nikola Bartunkova"), ("Anastasia Potapova", "Amanda Anisimova")),
         (("Coco Gauff", "Cristina Bucsa"), ("Iva Jovic", "Alexandra Eala"))),
        ((("Iga Swiatek", "Marie Bouzkova"), ("Zheng Qinwen", "Madison Keys")),
         (("Naomi Osaka", "Elise Mertens"), ("Elena Rybakina", "Yuliia Starodubtseva")))
    )
)
women_tree_post = (
    (
        (("Aryna Sabalenka", "Taylor Townsend"), ("Marta Kostyuk", "Linda Noskova")),
        (("Jessica Pegula", "Sorana Cirstea"), ("Anna Kalinskaya", "Emma Navarro"))
    ),
    (
        (("Mirra Andreeva", "Anastasia Potapova"),
         ("Coco Gauff", ("Iva Jovic", "Alexandra Eala"))),
        (("Iga Swiatek", "Zheng Qinwen"),
         (("Naomi Osaka", "Elise Mertens"), ("Elena Rybakina", "Yuliia Starodubtseva")))
    )
)

wom_init = {k: 1850.0 for k in women_dk}
wom_h2h = {
    ("Iva Jovic", "Alexandra Eala"): 25,
    ("Yuliia Starodubtseva", "Elena Rybakina"): 25,
    ("Naomi Osaka", "Elise Mertens"): 25,
    ("Coco Gauff", "Aryna Sabalenka"): 15,
}
for label, tgts in [("W_SHIN", wom_shin), ("W_MID", wom_mid), ("W_POW", wom_pow)]:
    welos = fit_elos(women_tree_pre, tgts, wom_init, 400.0, wom_h2h, steps=150)
    pre_w = bracket_dp(women_tree_pre, welos, 400.0, wom_h2h)
    post_w = bracket_dp(women_tree_post, welos, 400.0, wom_h2h)
    print(f"\n--- WOMEN FIT: {label} ---")
    if label == "W_MID":
        print("  Key Matchups:")
        for a, b in [
            ("Aryna Sabalenka", "Taylor Townsend"),
            ("Linda Noskova", "Marta Kostyuk"),
            ("Jessica Pegula", "Sorana Cirstea"),
            ("Emma Navarro", "Anna Kalinskaya"),
            ("Mirra Andreeva", "Anastasia Potapova"),
            ("Iva Jovic", "Alexandra Eala"),
            ("Coco Gauff", "Alexandra Eala"),
            ("Coco Gauff", "Mirra Andreeva"),
            ("Iga Swiatek", "Zheng Qinwen"),
            ("Naomi Osaka", "Elise Mertens"),
            ("Elena Rybakina", "Yuliia Starodubtseva"),
            ("Aryna Sabalenka", "Jessica Pegula"),
            ("Aryna Sabalenka", "Coco Gauff"),
            ("Iga Swiatek", "Elena Rybakina"),
        ]:
            print(f"    {a:23s} vs {b:23s}: {win_prob(a, b, welos, 400.0, wom_h2h):.3f}")
    top10 = sorted(post_w.items(), key=lambda x: -x[1])[:10]
    for p, v in top10:
        print(f"    {p:23s}: pre={pre_w[p]:.4f} (tgt={tgts[p]:.4f}) -> POST={v:.4f}")
    print(f"    Top-5 sum = {sum(v for _, v in top10[:5]):.4f}")
