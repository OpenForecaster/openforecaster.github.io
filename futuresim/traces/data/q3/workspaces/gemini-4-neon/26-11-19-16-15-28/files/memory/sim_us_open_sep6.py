import math, random
from collections import defaultdict

def win_prob(p1, p2, elos, scale=400.0, h2h=None):
    diff = elos[p1] - elos[p2]
    if h2h:
        if (p1, p2) in h2h: diff += h2h[(p1, p2)]
        elif (p2, p1) in h2h: diff -= h2h[(p2, p1)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def bracket_dp(tree, elos, scale=400.0, h2h=None):
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

def fit_elos(tree_pre, targets, init_elos=None, scale=400.0, h2h=None, steps=250):
    elos = {k: 1850.0 for k in targets} if init_elos is None else dict(init_elos)
    for _ in range(steps):
        cur = bracket_dp(tree_pre, elos, scale, h2h)
        for p, tgt in targets.items():
            if tgt > 0 and cur.get(p, 0) > 0:
                elos[p] += 45.0 * math.log(tgt / cur[p])
        m = sum(elos.values()) / len(elos)
        for p in elos:
            elos[p] -= (m - 1850.0)
    return elos

def power_devig(raw_dict):
    # Find k >= 1 s.t. sum(p^k) = 1
    lo, hi = 1.0, 3.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        s = sum(v ** mid for v in raw_dict.values())
        if s > 1.0: lo = mid
        else: hi = mid
    k = 0.5 * (lo + hi)
    return {p: v ** k for p, v in raw_dict.items()}, k

def shin_devig(raw_dict):
    # Classic Shin (1993) devig for multi-outcome market with sum(q_i) = S > 1
    S = sum(raw_dict.values())
    # solve for z in (0,1) s.t. sum(p_i(z)) = 1 where p_i = (sqrt(z^2 + 4*(1-z)*q_i^2/S) - z) / (2*(1-z))
    def sum_p(z):
        tot = 0.0
        for q in raw_dict.values():
            tot += (math.sqrt(z*z + 4.0*(1.0-z)*(q*q)/S) - z) / (2.0*(1.0-z))
        return tot
    lo, hi = 1e-6, 0.99
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if sum_p(mid) > 1.0: lo = mid
        else: hi = mid
    z = 0.5 * (lo + hi)
    out = {p: (math.sqrt(z*z + 4.0*(1.0-z)*(q*q)/S) - z) / (2.0*(1.0-z)) for p, q in raw_dict.items()}
    return out, z

def exchange_spread_devig(raw_dict, spread_cap=0.016):
    # Prediction-market ask prices: subtract min(spread_cap, 0.42 * q) then renormalize slightly
    adj = {}
    for p, q in raw_dict.items():
        sp = min(spread_cap, 0.42 * q)
        adj[p] = max(0.001, q - sp)
    s = sum(adj.values())
    return {p: v / s for p, v in adj.items()}

def mult_devig(raw_dict):
    s = sum(raw_dict.values())
    return {p: v / s for p, v in raw_dict.items()}

# =====================================================================
# 1. MEN'S SINGLES — SEP 6 04:55 AM ET DK PREDICTIONS (PRE-SUNDAY R4)
# =====================================================================
men_dk_raw = {
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
    # Unlisted 6 players (all <= 2% on DK):
    "Karen Khachanov": 0.018,
    "Alexander Blockx": 0.013,
    "Tomas Martin Etcheverry": 0.012,
    "Luciano Darderi": 0.011,
    "Botic van de Zandschulp": 0.009,
    "Arthur Gea": 0.006,
}

men_tree_pre_sun = (
    (
        (("Alexander Zverev", "Luciano Darderi"), ("Arthur Gea", "Botic van de Zandschulp")),
        (("Karen Khachanov", "Learner Tien"), ("Francisco Cerundolo", "Alexander Blockx"))
    ),
    (
        (("Daniil Medvedev", "Frances Tiafoe"), ("Alex Michelsen", "Tomas Martin Etcheverry")),
        (("Ben Shelton", "Stefanos Tsitsipas"), ("Tommy Paul", "Carlos Alcaraz"))
    )
)

# POST-SUNDAY (as of Sep 6 7:50 PM ET):
# Alcaraz def. Paul 6-4 6-3 6-4
# Tiafoe def. Medvedev 7-6(1) 6-4 7-6(6)
# Michelsen def. Etcheverry 7-6(6) 6-4 6-4
# Shelton vs Tsitsipas PENDING Sunday night
men_tree_post_sun = (
    (
        (("Alexander Zverev", "Luciano Darderi"), ("Arthur Gea", "Botic van de Zandschulp")),
        (("Karen Khachanov", "Learner Tien"), ("Francisco Cerundolo", "Alexander Blockx"))
    ),
    (
        ("Frances Tiafoe", "Alex Michelsen"),
        (("Ben Shelton", "Stefanos Tsitsipas"), "Carlos Alcaraz")
    )
)

men_h2h = {
    ("Carlos Alcaraz", "Tommy Paul"): 35,
    ("Carlos Alcaraz", "Ben Shelton"): 25,       # 3-0 H2H
    ("Carlos Alcaraz", "Stefanos Tsitsipas"): 45,# 6-0 H2H
    ("Daniil Medvedev", "Frances Tiafoe"): 25,   # pre-Sunday H2H was 6-1
}

m_pow, mk = power_devig(men_dk_raw)
m_shin, mz = shin_devig(men_dk_raw)
m_ex = exchange_spread_devig(men_dk_raw, spread_cap=0.018)
m_mul = mult_devig(men_dk_raw)

print(f"MEN'S DK raw sum = {sum(men_dk_raw.values()):.4f} | Power k={mk:.4f} | Shin z={mz:.4f}")
print("Pre-Sunday Devigged Targets (Top 10):")
for p in list(men_dk_raw.keys())[:10]:
    print(f"  {p:23s}: raw={men_dk_raw[p]:.3f} | Exch={m_ex[p]:.4f} | Pow={m_pow[p]:.4f} | Shin={m_shin[p]:.4f} | Mult={m_mul[p]:.4f}")

# Fit Elos for each devigged market
melos_ex = fit_elos(men_tree_pre_sun, m_ex, h2h=men_h2h)
melos_pow = fit_elos(men_tree_pre_sun, m_pow, h2h=men_h2h)
melos_shin = fit_elos(men_tree_pre_sun, m_shin, h2h=men_h2h)

# Bayesian post-Sunday performance updates (Tiafoe beat #7 Medvedev 3-0, Alcaraz peak-form 3-0 Paul, Michelsen 12-0 sets 3-0 Etcheverry):
def apply_sun_men_bayes(elos):
    e = dict(elos)
    e["Carlos Alcaraz"] += 15       # wrist worry gone, peak form 3-0 Paul
    e["Frances Tiafoe"] += 35       # beat #7 Medvedev 3-0! 5 straight top-10 wins!
    e["Alex Michelsen"] += 25       # 12-0 sets, 81% 1st serve pts, 44 winners
    return e

melos_ex_adj = apply_sun_men_bayes(melos_ex)
melos_pow_adj = apply_sun_men_bayes(melos_pow)
melos_shin_adj = apply_sun_men_bayes(melos_shin)

# Fundamental bottom-up Men's Elo (scale=400, independent of DK US-player hype):
melos_fund = {
    "Carlos Alcaraz": 2255,         # peak form, 18 straight Slam wins, 1 set lost
    "Alexander Zverev": 2115,       # clean 3-0 vs Tabilo erased fatigue, #1 seed, RG champ
    "Ben Shelton": 2005,            # #8 Montreal champ, 2am finish vs Shapo
    "Daniil Medvedev": 1990,        # (eliminated)
    "Frances Tiafoe": 1985,         # #11, beat Medvedev 3-0, 5 straight top-10 wins, 2x US Open SF
    "Alex Michelsen": 1930,         # unseeded, 12-0 sets, 1st Slam QF
    "Learner Tien": 1935,           # #14, beat Mensik in 5, Canada SF
    "Karen Khachanov": 1915,        # beat #3 FAA & Bonzi 3-0, 2022 US Open SF
    "Stefanos Tsitsipas": 1900,     # beat Fils & Lehecka, 1-0 H2H vs Shelton
    "Francisco Cerundolo": 1895,    # #24, beat Fritz in 5
    "Alexander Blockx": 1875,       # #28, beat #5 Cobolli in 4
    "Luciano Darderi": 1870,        # #21, beat #13 Musetti 3-0, beat Zverev on clay
    "Botic van de Zandschulp": 1845,# beat #6 de Minaur 3-0 & Bergs in 5 (4h29m)
    "Arthur Gea": 1795,             # LL #87, beat Zheng in 5
    "Tommy Paul": 1900,             # (eliminated)
    "Tomas Martin Etcheverry": 1875,# (eliminated)
}

models_men = {
    "Exch_Raw": melos_ex,
    "Exch_Bayes": melos_ex_adj,
    "Pow_Bayes": melos_pow_adj,
    "Shin_Bayes": melos_shin_adj,
    "Fund_ATP": melos_fund,
}

print("\n=== MEN'S KEY MATCHUP PROBABILITIES ACROSS MODELS ===")
matchups_m = [
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
    ("Alexander Zverev", "Learner Tien"),
    ("Ben Shelton", "Frances Tiafoe"),
    ("Ben Shelton", "Alex Michelsen"),
]
hdr = f"{'Matchup':40s} | " + " | ".join(f"{k:>10s}" for k in models_men)
print(hdr)
print("-" * len(hdr))
for a, b in matchups_m:
    vals = [f"{win_prob(a, b, e, 400.0, men_h2h):10.3f}" for e in models_men.values()]
    print(f"{a[:18]:18s} vs {b[:18]:18s} | " + " | ".join(vals))

print("\n=== Q891014 MEN'S TITLE PROBS (POST-SUNDAY) ===")
dps_m = {k: bracket_dp(men_tree_post_sun, e, 400.0, men_h2h) for k, e in models_men.items()}
all_m_players = sorted(dps_m["Exch_Bayes"].keys(), key=lambda x: -dps_m["Exch_Bayes"][x])
hdr = f"{'Player':24s} | " + " | ".join(f"{k:>10s}" for k in models_men) + " |   Ensemble"
print(hdr)
print("-" * len(hdr))
for p in all_m_players:
    vals = [dps_m[k].get(p, 0.0) for k in models_men]
    # Ensemble: 0.30 Exch_Bayes + 0.25 Pow_Bayes + 0.20 Shin_Bayes + 0.25 Fund_ATP
    ens = 0.30*dps_m["Exch_Bayes"][p] + 0.25*dps_m["Pow_Bayes"][p] + 0.20*dps_m["Shin_Bayes"][p] + 0.25*dps_m["Fund_ATP"][p]
    print(f"{p:24s} | " + " | ".join(f"{v:10.4f}" for v in vals) + f" | {ens:10.4f}")

# =====================================================================
# 2. Q408930 — FURTHEST-ADVANCING U.S. MAN (EXACT + 400K MONTE CARLO)
# =====================================================================
US_MEN = ["Frances Tiafoe", "Alex Michelsen", "Ben Shelton", "Learner Tien"]

def sim_q408930(elos, label, N=400000):
    rng = random.Random(20260906)
    def play(a, b):
        return a if rng.random() < win_prob(a, b, elos, 400.0, men_h2h) else b
    uniq = defaultdict(int)
    split = defaultdict(float)
    rank_tb = defaultdict(int) # if SF tie broke by seed/ranking (Tiafoe #11 > Tien #14 > Michelsen unseeded)
    reach = {u: defaultdict(int) for u in US_MEN}
    ties_sf = 0
    for _ in range(N):
        # Completed as of Sun 7:50 PM ET:
        # Q1 R4: Zverev vs Darderi, Gea vs BvdZ
        # Q2 R4: Khachanov vs Tien, Cerundolo vs Blockx
        # Q3 QF: Tiafoe vs Michelsen (BOTH IN QF!)
        # Q4 R4: Shelton vs Tsitsipas -> winner plays Alcaraz in QF!
        score = {"Frances Tiafoe": 5, "Alex Michelsen": 5, "Ben Shelton": 4, "Learner Tien": 4}
        q1a = play("Alexander Zverev", "Luciano Darderi")
        q1b = play("Arthur Gea", "Botic van de Zandschulp")
        q2a = play("Karen Khachanov", "Learner Tien")
        if q2a == "Learner Tien": score["Learner Tien"] = 5
        q2b = play("Francisco Cerundolo", "Alexander Blockx")
        q4a = play("Ben Shelton", "Stefanos Tsitsipas")
        if q4a == "Ben Shelton": score["Ben Shelton"] = 5
        q4b = "Carlos Alcaraz"

        sf1 = play(q1a, q1b)
        sf2 = play(q2a, q2b)
        if sf2 == "Learner Tien": score["Learner Tien"] = 6
        sf3 = play("Frances Tiafoe", "Alex Michelsen")
        score[sf3] = 6 # GUARANTEED SF!
        sf4 = play(q4a, q4b)
        if sf4 == "Ben Shelton": score["Ben Shelton"] = 6

        f1 = play(sf1, sf2)
        if f1 == "Learner Tien": score["Learner Tien"] = 7
        f2 = play(sf3, sf4)
        if f2 in score: score[f2] = 7

        ch = play(f1, f2)
        if ch in score: score[ch] = 8

        for u, r in score.items():
            for rr in range(5, r+1): reach[u][rr] += 1

        mx = max(score.values())
        tops = [u for u, r in score.items() if r == mx]
        if len(tops) == 1:
            uniq[tops[0]] += 1
            split[tops[0]] += 1.0
            rank_tb[tops[0]] += 1
        else:
            ties_sf += 1
            for u in tops: split[u] += 1.0 / len(tops)
            # seed priority: Ben Shelton(8) > Frances Tiafoe(11) > Learner Tien(14) > Alex Michelsen(46)
            seed_ord = {"Ben Shelton": 8, "Frances Tiafoe": 11, "Learner Tien": 14, "Alex Michelsen": 46}
            best = min(tops, key=lambda x: seed_ord[x])
            rank_tb[best] += 1

    un = N - ties_sf
    print(f"\n=== Q408930 [{label}] (TieRate={ties_sf/N:.4f}) ===")
    print(f"{'Player':16s} | {'CondUniq':>8s} | {'TieSplit':>8s} | {'SeedTB':>8s} | {'P(QF+)':>6s} {'P(SF+)':>6s} {'P(F+)':>6s} {'P(W)':>6s}")
    for u in US_MEN:
        print(f"{u:16s} | {uniq[u]/un:8.4f} | {split[u]/N:8.4f} | {rank_tb[u]/N:8.4f} | {reach[u][5]/N:6.3f} {reach[u][6]/N:6.3f} {reach[u][7]/N:6.3f} {reach[u][8]/N:6.3f}")

for k in ["Exch_Bayes", "Pow_Bayes", "Shin_Bayes", "Fund_ATP"]:
    sim_q408930(models_men[k], k, N=300000)

# =====================================================================
# 3. WOMEN'S SINGLES — SEP 6 04:55 AM ET DK PREDICTIONS (PRE-SUNDAY R4)
# =====================================================================
wom_dk_raw = {
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
    # Unlisted 6 players (<= 3% on DK):
    "Emma Navarro": 0.025,
    "Zheng Qinwen": 0.023,
    "Anna Kalinskaya": 0.020,
    "Anastasia Potapova": 0.018,
    "Sorana Cirstea": 0.015,
    "Taylor Townsend": 0.012,
}

wom_tree_pre_sun = (
    (
        (("Aryna Sabalenka", "Taylor Townsend"), ("Marta Kostyuk", "Linda Noskova")),
        (("Jessica Pegula", "Sorana Cirstea"), ("Anna Kalinskaya", "Emma Navarro"))
    ),
    (
        (("Mirra Andreeva", "Anastasia Potapova"), ("Coco Gauff", "Iva Jovic")),
        (("Iga Swiatek", "Zheng Qinwen"), ("Naomi Osaka", "Elena Rybakina"))
    )
)

# POST-SUNDAY (as of Sep 6 7:50 PM ET):
# Sabalenka def. Townsend 6-4, 6-3
# Noskova def. Kostyuk 7-5, 5-7, 6-4
# Pegula vs Cirstea & Kalinskaya vs Navarro PENDING Sunday evening/night
wom_tree_post_sun = (
    (
        ("Aryna Sabalenka", "Linda Noskova"),
        (("Jessica Pegula", "Sorana Cirstea"), ("Anna Kalinskaya", "Emma Navarro"))
    ),
    (
        (("Mirra Andreeva", "Anastasia Potapova"), ("Coco Gauff", "Iva Jovic")),
        (("Iga Swiatek", "Zheng Qinwen"), ("Naomi Osaka", "Elena Rybakina"))
    )
)

wom_h2h = {
    ("Jessica Pegula", "Sorana Cirstea"): 20,    # 3-1 H2H incl. Cincy last month
    ("Anna Kalinskaya", "Emma Navarro"): 20,     # 2-0 H2H
    ("Iga Swiatek", "Zheng Qinwen"): 15,         # 7-1 H2H (though Zheng won Olympics)
    ("Elena Rybakina", "Naomi Osaka"): 15,       # Osaka Achilles niggle / MTO vs Mertens
}

w_pow, wk = power_devig(wom_dk_raw)
w_shin, wz = shin_devig(wom_dk_raw)
w_ex = exchange_spread_devig(wom_dk_raw, spread_cap=0.016)
w_mul = mult_devig(wom_dk_raw)

print(f"\nWOMEN'S DK raw sum = {sum(wom_dk_raw.values()):.4f} | Power k={wk:.4f} | Shin z={wz:.4f}")
print("Pre-Sunday Devigged Targets (Top 10):")
for p in list(wom_dk_raw.keys())[:10]:
    print(f"  {p:23s}: raw={wom_dk_raw[p]:.3f} | Exch={w_ex[p]:.4f} | Pow={w_pow[p]:.4f} | Shin={w_shin[p]:.4f} | Mult={w_mul[p]:.4f}")

welos_ex = fit_elos(wom_tree_pre_sun, w_ex, h2h=wom_h2h)
welos_pow = fit_elos(wom_tree_pre_sun, w_pow, h2h=wom_h2h)
welos_shin = fit_elos(wom_tree_pre_sun, w_shin, h2h=wom_h2h)

def apply_sun_wom_bayes(elos):
    e = dict(elos)
    # Noskova beat higher-priced Kostyuk (Wimbledon champ #6 seed!) -> +25 Elo Bayesian boost
    # Sabalenka beat Townsend 6-4, 6-3 (11 breaks early, strong finish) -> 0 Elo change (pure advancement)
    e["Linda Noskova"] += 25
    return e

welos_ex_adj = apply_sun_wom_bayes(welos_ex)
welos_pow_adj = apply_sun_wom_bayes(welos_pow)
welos_shin_adj = apply_sun_wom_bayes(welos_shin)

# Fundamental bottom-up Women's Elo (scale=400):
welos_fund = {
    "Aryna Sabalenka": 2120,     # #1, 2x defending champ, 8-0 sets, IN QF!
    "Coco Gauff": 2090,          # #4, 2023 champ, Cincy champ, 6-0 sets
    "Iga Swiatek": 2045,         # #8, 2022 champ, Toronto champ, tight vs Bouzkova
    "Elena Rybakina": 2035,      # #2, AO 2026 champ, beat Starodubtseva 2-0 cleanly
    "Mirra Andreeva": 2010,      # #5, RG 2026 champ, faces Potapova
    "Jessica Pegula": 1995,      # #3, 2024 finalist, plays Cirstea tonight
    "Naomi Osaka": 1985,         # #13, 2x US Open champ, Achilles niggle vs Mertens
    "Linda Noskova": 1960,       # #6, Wimbledon 2026 champ, beat Kostyuk in 3, IN QF!
    "Marta Kostyuk": 1945,       # (eliminated)
    "Iva Jovic": 1920,           # #14, beat Eala in 3h epic
    "Zheng Qinwen": 1930,        # Olympic champ, beat Keys from 0-5 down
    "Emma Navarro": 1915,        # #26, 2024 SF, beat Muchova
    "Anna Kalinskaya": 1905,     # #21, beat Svitolina, 2-0 H2H vs Navarro
    "Anastasia Potapova": 1885,  # #24, beat Anisimova 6-2 7-5
    "Sorana Cirstea": 1865,      # #16, 3 straight-set wins losing 16 games
    "Taylor Townsend": 1835,     # (eliminated)
}

models_wom = {
    "Exch_Raw": welos_ex,
    "Exch_Bayes": welos_ex_adj,
    "Pow_Bayes": welos_pow_adj,
    "Shin_Bayes": welos_shin_adj,
    "Fund_WTA": welos_fund,
}

print("\n=== WOMEN'S KEY MATCHUP PROBABILITIES ACROSS MODELS ===")
matchups_w = [
    ("Aryna Sabalenka", "Taylor Townsend"),
    ("Aryna Sabalenka", "Linda Noskova"),
    ("Jessica Pegula", "Sorana Cirstea"),
    ("Emma Navarro", "Anna Kalinskaya"),
    ("Aryna Sabalenka", "Jessica Pegula"),
    ("Mirra Andreeva", "Anastasia Potapova"),
    ("Coco Gauff", "Iva Jovic"),
    ("Coco Gauff", "Mirra Andreeva"),
    ("Iga Swiatek", "Zheng Qinwen"),
    ("Elena Rybakina", "Naomi Osaka"),
    ("Iga Swiatek", "Elena Rybakina"),
    ("Aryna Sabalenka", "Coco Gauff"),
    ("Aryna Sabalenka", "Iga Swiatek"),
]
hdr = f"{'Matchup':40s} | " + " | ".join(f"{k:>10s}" for k in models_wom)
print(hdr)
print("-" * len(hdr))
for a, b in matchups_w:
    vals = [f"{win_prob(a, b, e, 400.0, wom_h2h):10.3f}" for e in models_wom.values()]
    print(f"{a[:18]:18s} vs {b[:18]:18s} | " + " | ".join(vals))

print("\n=== Q608158 WOMEN'S TITLE PROBS (POST-SUNDAY) ===")
dps_w = {k: bracket_dp(wom_tree_post_sun, e, 400.0, wom_h2h) for k, e in models_wom.items()}
all_w_players = sorted(dps_w["Exch_Bayes"].keys(), key=lambda x: -dps_w["Exch_Bayes"][x])
hdr = f"{'Player':24s} | " + " | ".join(f"{k:>10s}" for k in models_wom) + " |   Ensemble"
print(hdr)
print("-" * len(hdr))
for p in all_w_players:
    vals = [dps_w[k].get(p, 0.0) for k in models_wom]
    ens = 0.30*dps_w["Exch_Bayes"][p] + 0.25*dps_w["Pow_Bayes"][p] + 0.20*dps_w["Shin_Bayes"][p] + 0.25*dps_w["Fund_WTA"][p]
    print(f"{p:24s} | " + " | ".join(f"{v:10.4f}" for v in vals) + f" | {ens:10.4f}")
