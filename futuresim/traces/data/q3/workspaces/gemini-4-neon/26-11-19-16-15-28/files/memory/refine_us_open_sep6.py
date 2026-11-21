import math, random
from collections import defaultdict

def win_prob(p1, p2, elos, scale=400.0, h2h=None):
    diff = elos[p1] - elos[p2]
    if h2h:
        if (p1, p2) in h2h: diff += h2h[(p1, p2)]
        elif (p2, p1) in h2h: diff -= h2h[(p2, p1)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def bracket_dp(tree, elos, scale=400.0, h2h=None):
    if isinstance(tree, str): return {tree: 1.0}
    L = bracket_dp(tree[0], elos, scale, h2h)
    R = bracket_dp(tree[1], elos, scale, h2h)
    out = defaultdict(float)
    for p1, pr1 in L.items():
        for p2, pr2 in R.items():
            w1 = win_prob(p1, p2, elos, scale, h2h)
            out[p1] += pr1 * pr2 * w1
            out[p2] += pr1 * pr2 * (1.0 - w1)
    return dict(out)

def fit_elos(tree_pre, targets, scale=400.0, h2h=None, steps=260):
    elos = {k: 1850.0 for k in targets}
    for _ in range(steps):
        cur = bracket_dp(tree_pre, elos, scale, h2h)
        for p, tgt in targets.items():
            if tgt > 0 and cur.get(p, 0) > 0:
                elos[p] += 45.0 * math.log(tgt / cur[p])
        m = sum(elos.values()) / len(elos)
        for p in elos: elos[p] -= (m - 1850.0)
    return elos

def power_devig(raw_dict):
    lo, hi = 1.0, 3.0
    for _ in range(80):
        mid = 0.5*(lo+hi)
        if sum(v**mid for v in raw_dict.values()) > 1.0: lo = mid
        else: hi = mid
    k = 0.5*(lo+hi)
    return {p: v**k for p, v in raw_dict.items()}

# =====================================================================
# REFINED MEN'S MODEL (Check sensitivity to unlisted player priors & Tiafoe-Michelsen!)
# =====================================================================
# Better estimates for unlisted 6 players (Etcheverry is a clay specialist vs Michelsen; Paul ~1.4%):
men_dk_refined = {
    "Carlos Alcaraz": 0.55,
    "Alexander Zverev": 0.26,
    "Ben Shelton": 0.10,
    "Daniil Medvedev": 0.08,
    "Learner Tien": 0.05,
    "Alex Michelsen": 0.03,
    "Frances Tiafoe": 0.03,
    "Francisco Cerundolo": 0.02,
    "Stefanos Tsitsipas": 0.02,
    "Tommy Paul": 0.02,
    "Karen Khachanov": 0.017,
    "Alexander Blockx": 0.011,
    "Tomas Martin Etcheverry": 0.008,  # clay-courter underdog vs Michelsen
    "Luciano Darderi": 0.009,
    "Botic van de Zandschulp": 0.008,
    "Arthur Gea": 0.004,
}

men_tree_pre = (
    ((("Alexander Zverev", "Luciano Darderi"), ("Arthur Gea", "Botic van de Zandschulp")),
     (("Karen Khachanov", "Learner Tien"), ("Francisco Cerundolo", "Alexander Blockx"))),
    ((("Daniil Medvedev", "Frances Tiafoe"), ("Alex Michelsen", "Tomas Martin Etcheverry")),
     (("Ben Shelton", "Stefanos Tsitsipas"), ("Tommy Paul", "Carlos Alcaraz")))
)
men_tree_post = (
    ((("Alexander Zverev", "Luciano Darderi"), ("Arthur Gea", "Botic van de Zandschulp")),
     (("Karen Khachanov", "Learner Tien"), ("Francisco Cerundolo", "Alexander Blockx"))),
    (("Frances Tiafoe", "Alex Michelsen"),
     (("Ben Shelton", "Stefanos Tsitsipas"), "Carlos Alcaraz"))
)
men_h2h = {
    ("Carlos Alcaraz", "Tommy Paul"): 35,
    ("Carlos Alcaraz", "Ben Shelton"): 20,        # 3-0 H2H
    ("Carlos Alcaraz", "Stefanos Tsitsipas"): 45, # 6-0 H2H
    ("Daniil Medvedev", "Frances Tiafoe"): 25,
    ("Alexander Zverev", "Carlos Alcaraz"): 20,   # Zverev competitive hard-court H2H vs Alcaraz!
}

m_pow = power_devig(men_dk_refined)
melos_mkt = fit_elos(men_tree_pre, m_pow, h2h=men_h2h)
melos_mkt_adj = dict(melos_mkt)
melos_mkt_adj["Carlos Alcaraz"] += 15
melos_mkt_adj["Frances Tiafoe"] += 35
melos_mkt_adj["Alex Michelsen"] += 20

# Refined Fundamental ATP Elo (realistic Shelton, Tiafoe, Michelsen, Zverev, Alcaraz):
melos_fund2 = {
    "Carlos Alcaraz": 2255,         # peak form, 18 straight Slam wins
    "Alexander Zverev": 2120,       # #1 seed, clean 3-0 Tabilo, RG champ
    "Ben Shelton": 2030,            # #8 seed, Montreal Masters champ (18-21% vs Alcaraz, 68% vs Tsitsipas)
    "Daniil Medvedev": 1995,        # (out)
    "Frances Tiafoe": 1985,         # #11 seed, beat Medvedev 3-0, 5 straight top-10 wins, 4th USO QF
    "Alex Michelsen": 1925,         # #46 unseeded, 12-0 sets, 1st Slam QF (~41% vs Tiafoe)
    "Learner Tien": 1935,           # #14 seed, beat Mensik in 5 (~55% vs Khachanov)
    "Karen Khachanov": 1900,        # beat #3 FAA & Bonzi 3-0, 2022 USO SF
    "Stefanos Tsitsipas": 1900,     # beat Fils & Lehecka, 1-0 vs Shelton
    "Francisco Cerundolo": 1895,    # #24, beat Fritz in 5
    "Alexander Blockx": 1875,       # #28, beat Cobolli in 4
    "Luciano Darderi": 1870,        # #21, beat Musetti 3-0
    "Botic van de Zandschulp": 1845,# beat de Minaur & Bergs
    "Arthur Gea": 1790,             # LL #87
    "Tommy Paul": 1900,             # (out)
    "Tomas Martin Etcheverry": 1865,# (out)
}

# Blend Elo ratings directly (60% Market-Bayes + 40% Fundamental) AND check sensitivity on Tiafoe-Michelsen!
melos_blend = {p: 0.60 * melos_mkt_adj[p] + 0.40 * melos_fund2[p] for p in melos_fund2}

print("=== REFINED MEN'S MATCHUPS (MktBayes vs Fund2 vs 60/40 Blend) ===")
for a, b in [
    ("Carlos Alcaraz", "Tommy Paul"),
    ("Daniil Medvedev", "Frances Tiafoe"),
    ("Alex Michelsen", "Tomas Martin Etcheverry"),
    ("Frances Tiafoe", "Alex Michelsen"),
    ("Ben Shelton", "Stefanos Tsitsipas"),
    ("Carlos Alcaraz", "Ben Shelton"),
    ("Carlos Alcaraz", "Frances Tiafoe"),
    ("Carlos Alcaraz", "Alex Michelsen"),
    ("Carlos Alcaraz", "Alexander Zverev"),
    ("Alexander Zverev", "Luciano Darderi"),
    ("Botic van de Zandschulp", "Arthur Gea"),
    ("Learner Tien", "Karen Khachanov"),
    ("Francisco Cerundolo", "Alexander Blockx"),
    ("Ben Shelton", "Frances Tiafoe"),
]:
    print(f"  {a:23s} vs {b:23s}: Mkt={win_prob(a,b,melos_mkt_adj,400,men_h2h):.3f} | Fund={win_prob(a,b,melos_fund2,400,men_h2h):.3f} | Blend={win_prob(a,b,melos_blend,400,men_h2h):.3f}")

dp_mkt = bracket_dp(men_tree_post, melos_mkt_adj, 400, men_h2h)
dp_fnd = bracket_dp(men_tree_post, melos_fund2, 400, men_h2h)
dp_bld = bracket_dp(men_tree_post, melos_blend, 400, men_h2h)
print("\n=== Q891014 REFINED MEN'S TITLE PROBS ===")
for p in sorted(dp_bld.keys(), key=lambda x: -dp_bld[x])[:8]:
    avg_p = 0.60*dp_mkt[p] + 0.40*dp_fnd[p]
    print(f"  {p:23s}: Mkt={dp_mkt[p]:.4f} | Fund={dp_fnd[p]:.4f} | EloBlend={dp_bld[p]:.4f} | ProbBlend={avg_p:.4f}")

# Run 500k MC on Q408930 for Mkt, Fund2, EloBlend, PLUS sensitivity where Tiafoe-Michelsen is 55%, 58%, 61%
US_MEN = ["Frances Tiafoe", "Alex Michelsen", "Learner Tien", "Ben Shelton"]
def run_q408930(elos, label, tm_override=None, N=400000):
    rng = random.Random(777)
    def play(a, b):
        if tm_override is not None and {a, b} == {"Frances Tiafoe", "Alex Michelsen"}:
            p_t = tm_override
            return "Frances Tiafoe" if rng.random() < p_t else "Alex Michelsen"
        return a if rng.random() < win_prob(a, b, elos, 400.0, men_h2h) else b
    uniq = defaultdict(int)
    split = defaultdict(float)
    ties = 0
    for _ in range(N):
        sc = {"Frances Tiafoe":5, "Alex Michelsen":5, "Ben Shelton":4, "Learner Tien":4}
        q1a = play("Alexander Zverev", "Luciano Darderi")
        q1b = play("Arthur Gea", "Botic van de Zandschulp")
        q2a = play("Karen Khachanov", "Learner Tien")
        if q2a == "Learner Tien": sc["Learner Tien"] = 5
        q2b = play("Francisco Cerundolo", "Alexander Blockx")
        q4a = play("Ben Shelton", "Stefanos Tsitsipas")
        if q4a == "Ben Shelton": sc["Ben Shelton"] = 5
        q4b = "Carlos Alcaraz"
        sf1 = play(q1a, q1b)
        sf2 = play(q2a, q2b)
        if sf2 == "Learner Tien": sc["Learner Tien"] = 6
        sf3 = play("Frances Tiafoe", "Alex Michelsen")
        sc[sf3] = 6
        sf4 = play(q4a, q4b)
        if sf4 == "Ben Shelton": sc["Ben Shelton"] = 6
        f1 = play(sf1, sf2)
        if f1 == "Learner Tien": sc["Learner Tien"] = 7
        f2 = play(sf3, sf4)
        if f2 in sc: sc[f2] = 7
        ch = play(f1, f2)
        if ch in sc: sc[ch] = 8
        mx = max(sc.values())
        tops = [u for u, v in sc.items() if v == mx]
        if len(tops) == 1:
            uniq[tops[0]] += 1
            split[tops[0]] += 1.0
        else:
            ties += 1
            for u in tops: split[u] += 1.0/len(tops)
    un = N - ties
    print(f"Q408930 [{label:22s}] Tie={ties/N:.3f} | Uniq: " + "  ".join(f"{u.split()[1]}={uniq[u]/un:.3f}" for u in US_MEN) + " | 85U+15S: " + "  ".join(f"{u.split()[1]}={0.85*uniq[u]/un+0.15*split[u]/N:.3f}" for u in US_MEN))

print("\n=== Q408930 SENSITIVITY GRID ===")
run_q408930(melos_mkt_adj, "MktBayes")
run_q408930(melos_fund2,   "Fund2")
run_q408930(melos_blend,   "Blend60/40 (auto)")
run_q408930(melos_blend,   "Blend (Tiafoe=55%)", tm_override=0.55)
run_q408930(melos_blend,   "Blend (Tiafoe=58%)", tm_override=0.58)
run_q408930(melos_blend,   "Blend (Tiafoe=61%)", tm_override=0.61)

# =====================================================================
# REFINED WOMEN'S MODEL (Check Townsend=0.8%, Jovic fatigue, Osaka Achilles!)
# =====================================================================
wom_dk_ref = {
    "Aryna Sabalenka": 0.31,
    "Coco Gauff": 0.21,
    "Iga Swiatek": 0.14,
    "Jessica Pegula": 0.09,
    "Mirra Andreeva": 0.08,
    "Elena Rybakina": 0.08,
    "Naomi Osaka": 0.07,
    "Marta Kostyuk": 0.05,
    "Iva Jovic": 0.03,
    "Linda Noskova": 0.03,
    "Emma Navarro": 0.023,
    "Zheng Qinwen": 0.022,
    "Anna Kalinskaya": 0.019,
    "Anastasia Potapova": 0.017,
    "Sorana Cirstea": 0.014,
    "Taylor Townsend": 0.008,  # #96 underdog vs #1 Sabalenka (~86% Sabalenka!)
}
wom_tree_pre = (
    ((("Aryna Sabalenka", "Taylor Townsend"), ("Marta Kostyuk", "Linda Noskova")),
     (("Jessica Pegula", "Sorana Cirstea"), ("Anna Kalinskaya", "Emma Navarro"))),
    ((("Mirra Andreeva", "Anastasia Potapova"), ("Coco Gauff", "Iva Jovic")),
     (("Iga Swiatek", "Zheng Qinwen"), ("Naomi Osaka", "Elena Rybakina")))
)
wom_tree_post = (
    (("Aryna Sabalenka", "Linda Noskova"),
     (("Jessica Pegula", "Sorana Cirstea"), ("Anna Kalinskaya", "Emma Navarro"))),
    ((("Mirra Andreeva", "Anastasia Potapova"), ("Coco Gauff", "Iva Jovic")),
     (("Iga Swiatek", "Zheng Qinwen"), ("Naomi Osaka", "Elena Rybakina")))
)
wom_h2h = {
    ("Jessica Pegula", "Sorana Cirstea"): 20,
    ("Anna Kalinskaya", "Emma Navarro"): 20,
    ("Iga Swiatek", "Zheng Qinwen"): 15,
    ("Elena Rybakina", "Naomi Osaka"): 20,    # Osaka Achilles niggle + MTO vs Mertens
    ("Coco Gauff", "Iva Jovic"): 20,          # Jovic played 3h+ epic vs Eala
}

w_pow = power_devig(wom_dk_ref)
welos_mkt = fit_elos(wom_tree_pre, w_pow, h2h=wom_h2h)
welos_mkt_adj = dict(welos_mkt)
welos_mkt_adj["Linda Noskova"] += 25  # Wimbledon champ beat higher-priced Kostyuk

welos_fund2 = {
    "Aryna Sabalenka": 2120,     # #1, 2x defending champ, IN QF!
    "Coco Gauff": 2090,          # #4, 2023 champ, Cincy champ, 6-0 sets
    "Iga Swiatek": 2045,         # #8, 2022 champ, Toronto champ, tight vs Bouzkova
    "Elena Rybakina": 2035,      # #2, AO 2026 champ, beat Starodubtseva 2-0
    "Mirra Andreeva": 2010,      # #5, RG 2026 champ, faces Potapova
    "Jessica Pegula": 1995,      # #3, 2024 finalist, plays Cirstea tonight
    "Naomi Osaka": 1980,         # #13, 2x US Open champ, Achilles niggle
    "Linda Noskova": 1960,       # #6, Wimbledon champ, IN QF!
    "Marta Kostyuk": 1945,       # (out)
    "Iva Jovic": 1915,           # #14, 3h epic vs Eala
    "Zheng Qinwen": 1930,        # Olympic champ, beat Keys from 0-5 down
    "Emma Navarro": 1915,        # #26, 2024 SF
    "Anna Kalinskaya": 1905,     # #21, beat Svitolina
    "Anastasia Potapova": 1885,  # #24, beat Anisimova
    "Sorana Cirstea": 1865,      # #16, 3 straight-set wins
    "Taylor Townsend": 1815,     # (out)
}
welos_blend = {p: 0.60 * welos_mkt_adj[p] + 0.40 * welos_fund2[p] for p in welos_fund2}

print("\n=== REFINED WOMEN'S MATCHUPS (MktBayes vs Fund2 vs 60/40 Blend) ===")
for a, b in [
    ("Aryna Sabalenka", "Taylor Townsend"),
    ("Aryna Sabalenka", "Linda Noskova"),
    ("Jessica Pegula", "Sorana Cirstea"),
    ("Emma Navarro", "Anna Kalinskaya"),
    ("Mirra Andreeva", "Anastasia Potapova"),
    ("Coco Gauff", "Iva Jovic"),
    ("Iga Swiatek", "Zheng Qinwen"),
    ("Elena Rybakina", "Naomi Osaka"),
    ("Aryna Sabalenka", "Coco Gauff"),
]:
    print(f"  {a:23s} vs {b:23s}: Mkt={win_prob(a,b,welos_mkt_adj,400,wom_h2h):.3f} | Fund={win_prob(a,b,welos_fund2,400,wom_h2h):.3f} | Blend={win_prob(a,b,welos_blend,400,wom_h2h):.3f}")

wdp_mkt = bracket_dp(wom_tree_post, welos_mkt_adj, 400, wom_h2h)
wdp_fnd = bracket_dp(wom_tree_post, welos_fund2, 400, wom_h2h)
wdp_bld = bracket_dp(wom_tree_post, welos_blend, 400, wom_h2h)
print("\n=== Q608158 REFINED WOMEN'S TITLE PROBS ===")
for p in sorted(wdp_bld.keys(), key=lambda x: -wdp_bld[x])[:9]:
    avg_p = 0.60*wdp_mkt[p] + 0.40*wdp_fnd[p]
    print(f"  {p:23s}: Mkt={wdp_mkt[p]:.4f} | Fund={wdp_fnd[p]:.4f} | EloBlend={wdp_bld[p]:.4f} | ProbBlend={avg_p:.4f}")
