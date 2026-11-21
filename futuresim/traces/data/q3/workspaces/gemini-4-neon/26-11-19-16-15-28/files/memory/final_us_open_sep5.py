import math, random
from collections import defaultdict

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

def fit_elos(tree_pre, targets, init_elos, scale=400.0, h2h=None, steps=160):
    elos = dict(init_elos)
    for _ in range(steps):
        cur = bracket_dp(tree_pre, elos, scale, h2h)
        for p, tgt in targets.items():
            if tgt > 0 and cur.get(p, 0) > 0:
                elos[p] += 50.0 * math.log(tgt / cur[p])
        m = sum(elos.values()) / len(elos)
        for p in elos: elos[p] -= (m - 1850.0)
    return elos

# ============================================================
# EXCHANGE-SPREAD DEVIG FOR WOMEN'S (Realistic top-contender weights!)
# ============================================================
# DK Predictions Sep 5 7:46 AM ET (pre-Saturday):
# Sabalenka 28, Gauff 21, Swiatek 15, Pegula 10, Rybakina 8, Eala 7, Andreeva 6, Osaka 6, Kostyuk 5, Anisimova 5
# Subtract ~1.5-2.0c ask spread per exchange contract (typical Kalshi/DK Predictions spread):
wom_exchange_mid = {
    "Aryna Sabalenka": 0.265,
    "Coco Gauff": 0.185,
    "Iga Swiatek": 0.130,
    "Jessica Pegula": 0.095,
    "Elena Rybakina": 0.068,
    "Mirra Andreeva": 0.052,
    "Naomi Osaka": 0.045,
    "Alexandra Eala": 0.032,     # discount retail hype; 0-2 H2H vs Jovic
    "Amanda Anisimova": 0.032,
    "Linda Noskova": 0.030,
    "Marta Kostyuk": 0.025,
    "Madison Keys": 0.018,
    "Emma Navarro": 0.016,
    "Iva Jovic": 0.015,
    "Anna Kalinskaya": 0.012,
    "Zheng Qinwen": 0.010,
    "Elise Mertens": 0.010,
    "Sorana Cirstea": 0.008,
    "Anastasia Potapova": 0.007,
    "Taylor Townsend": 0.006,
    "Marie Bouzkova": 0.004,
    "Yuliia Starodubtseva": 0.004,
    "Cristina Bucsa": 0.003,
    "Nikola Bartunkova": 0.003,
}
s = sum(wom_exchange_mid.values())
wom_tgt = {k: v/s for k, v in wom_exchange_mid.items()}

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

wom_h2h = {
    ("Iva Jovic", "Alexandra Eala"): 20,
    ("Yuliia Starodubtseva", "Elena Rybakina"): 25,
    ("Naomi Osaka", "Elise Mertens"): 25,
}
welos = fit_elos(women_tree_pre, wom_tgt, {k: 1850.0 for k in wom_tgt}, 400.0, wom_h2h, steps=180)
# Apply minor Saturday form adjustments:
# - Swiatek needed two tiebreaks (saved 3 set pts) vs Bouzkova -> tiny -10 Elo
# - Zheng Qinwen beat Keys in dramatic comeback from 0-5 down -> +15 Elo (dangerous R4 vs Swiatek, Olympic SF winner!)
# - Potapova beat Anisimova 6-2 7-5 saving 13/16 BPs -> +15 Elo
welos_adj = dict(welos)
welos_adj["Iga Swiatek"] -= 10
welos_adj["Zheng Qinwen"] += 20
welos_adj["Anastasia Potapova"] += 15

pre_w = bracket_dp(women_tree_pre, welos, 400.0, wom_h2h)
post_w_raw = bracket_dp(women_tree_post, welos, 400.0, wom_h2h)
post_w_adj = bracket_dp(women_tree_post, welos_adj, 400.0, wom_h2h)

print("=== WOMEN'S EXCHANGE-SPREAD FIT (CHECK MATCHUPS!) ===")
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
    ("Aryna Sabalenka", "Iga Swiatek"),
    ("Iga Swiatek", "Elena Rybakina"),
]:
    print(f"  {a:23s} vs {b:23s}: base={win_prob(a,b,welos,400,wom_h2h):.3f} | adj={win_prob(a,b,welos_adj,400,wom_h2h):.3f}")

print("\n=== WOMEN'S TITLE PROBS: PRE-SAT -> POST-SAT (BASE vs FORM-ADJ) ===")
for p, v in sorted(post_w_adj.items(), key=lambda x: -x[1])[:12]:
    print(f"  {p:23s}: pre={pre_w[p]:.4f} | post_base={post_w_raw[p]:.4f} | post_adj={v:.4f}")
print(f"  Top-5 post_adj sum = {sum(v for _, v in sorted(post_w_adj.items(), key=lambda x: -x[1])[:5]):.4f}")

# ============================================================
# MEN'S EXCHANGE-SPREAD FIT + FUNDAMENTAL CHECK
# ============================================================
# DK Predictions Sep 5 7:46 AM ET (pre-Saturday):
# Alcaraz 52, Zverev 21, Shelton 14, Fritz 13, Medvedev 8, Tiafoe 4, Tien 4, Mensik 4, Michelsen 3
men_exchange_mid = {
    "Carlos Alcaraz": 0.480,
    "Alexander Zverev": 0.185,
    "Ben Shelton": 0.115,
    "Taylor Fritz": 0.105,
    "Daniil Medvedev": 0.065,
    "Frances Tiafoe": 0.025,
    "Learner Tien": 0.025,
    "Jakub Mensik": 0.025,
    "Alex Michelsen": 0.018,
    "Flavio Cobolli": 0.011,
    "Karen Khachanov": 0.010,
    "Stefanos Tsitsipas": 0.009,
    "Tommy Paul": 0.009,
    "Lorenzo Musetti": 0.008,
    "Francisco Cerundolo": 0.007,
    "Tomas Martin Etcheverry": 0.005,
    "Alexander Blockx": 0.005,
    "Botic van de Zandschulp": 0.005,
    "Alejandro Tabilo": 0.004,
    "Zizou Bergs": 0.004,
    "Luciano Darderi": 0.003,
    "Michael Zheng": 0.0025,
    "Arthur Gea": 0.0018,
    "Benjamin Bonzi": 0.0018,
}
sm = sum(men_exchange_mid.values())
men_tgt = {k: v/sm for k, v in men_exchange_mid.items()}

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
men_h2h = {
    ("Carlos Alcaraz", "Tommy Paul"): 40,
    ("Daniil Medvedev", "Frances Tiafoe"): 30,
}
melos = fit_elos(men_tree_pre, men_tgt, {k: 1850.0 for k in men_tgt}, 400.0, men_h2h, steps=180)
# Apply Saturday Bayesian performance updates!
# - Cerundolo just beat #9 Fritz from 0-2 sets down -> +35 Elo
# - Blockx just destroyed #5 Cobolli 6-7, 6-3, 6-0, 6-3 -> +35 Elo
# - Darderi just beat #13 Musetti 6-4, 6-3, 6-3 -> +30 Elo
# - Khachanov beat Bonzi 6-3, 6-2, 6-4 (after beating #3 FAA) -> +25 Elo
# - Medvedev 9-0 sets / sharp vs Shelton 54 UEs -> slight +20 Medvedev, -15 Shelton
melos_adj = dict(melos)
melos_adj["Francisco Cerundolo"] += 35
melos_adj["Alexander Blockx"] += 35
melos_adj["Luciano Darderi"] += 30
melos_adj["Karen Khachanov"] += 25
melos_adj["Daniil Medvedev"] += 20
melos_adj["Ben Shelton"] -= 15
melos_adj["Stefanos Tsitsipas"] += 20
melos_adj["Tomas Martin Etcheverry"] += 20

pre_m = bracket_dp(men_tree_pre, melos, 400.0, men_h2h)
post_m_raw = bracket_dp(men_tree_post, melos, 400.0, men_h2h)
post_m_adj = bracket_dp(men_tree_post, melos_adj, 400.0, men_h2h)

print("\n=== MEN'S EXCHANGE-SPREAD FIT (CHECK MATCHUPS!) ===")
for a, b in [
    ("Carlos Alcaraz", "Tommy Paul"),
    ("Carlos Alcaraz", "Ben Shelton"),
    ("Carlos Alcaraz", "Daniil Medvedev"),
    ("Carlos Alcaraz", "Alexander Zverev"),
    ("Ben Shelton", "Stefanos Tsitsipas"),
    ("Daniil Medvedev", "Frances Tiafoe"),
    ("Alex Michelsen", "Tomas Martin Etcheverry"),
    ("Alexander Zverev", "Alejandro Tabilo"),
    ("Alexander Zverev", "Luciano Darderi"),
    ("Learner Tien", "Jakub Mensik"),
    ("Learner Tien", "Karen Khachanov"),
    ("Learner Tien", "Francisco Cerundolo"),
    ("Francisco Cerundolo", "Alexander Blockx"),
    ("Michael Zheng", "Arthur Gea"),
    ("Botic van de Zandschulp", "Zizou Bergs"),
]:
    print(f"  {a:23s} vs {b:23s}: base={win_prob(a,b,melos,400,men_h2h):.3f} | adj={win_prob(a,b,melos_adj,400,men_h2h):.3f}")

print("\n=== MEN'S TITLE PROBS: PRE-SAT -> POST-SAT (BASE vs BAYESIAN-ADJ) ===")
for p, v in sorted(post_m_adj.items(), key=lambda x: -x[1])[:12]:
    print(f"  {p:23s}: pre={pre_m[p]:.4f} | post_base={post_m_raw[p]:.4f} | post_adj={v:.4f}")
print(f"  Top-5 post_adj sum = {sum(v for _, v in sorted(post_m_adj.items(), key=lambda x: -x[1])[:5]):.4f}")

# Run 300k MC for Q408930 under BOTH melos and melos_adj!
US_MEN = {"Ben Shelton", "Frances Tiafoe", "Alex Michelsen", "Learner Tien", "Tommy Paul", "Michael Zheng"}
def sim_us_men(elos, sc=400.0, h2h=None, N=300000, label=""):
    rng = random.Random(2026)
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

        for u, sc_u in score.items():
            for r in range(4, sc_u+1): reach[u][r] += 1
        mx = max(score.values())
        tops = [u for u, sc_u in score.items() if sc_u == mx]
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

sim_us_men(melos, 400.0, men_h2h, N=300000, label="EXCHANGE_BASE")
sim_us_men(melos_adj, 400.0, men_h2h, N=300000, label="EXCHANGE_BAYESIAN_ADJ")
