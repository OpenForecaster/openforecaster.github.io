import math
import random
from collections import defaultdict

def win_prob(p1, p2, elos, scale=400.0, h2h=None):
    diff = elos[p1] - elos[p2]
    if h2h:
        if (p1, p2) in h2h:
            diff += h2h[(p1, p2)]
        elif (p2, p1) in h2h:
            diff -= h2h[(p2, p1)]
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

def fit_elos(tree_pre, targets, scale=400.0, h2h=None, steps=350):
    elos = {k: 1850.0 for k in targets}
    for _ in range(steps):
        cur = bracket_dp(tree_pre, elos, scale, h2h)
        for p, tgt in targets.items():
            if tgt > 0 and cur.get(p, 0) > 0:
                elos[p] += 40.0 * math.log(tgt / cur[p])
        m = sum(elos.values()) / len(elos)
        for p in elos:
            elos[p] -= (m - 1850.0)
    return elos

def prop_devig(raw_dict):
    s = sum(raw_dict.values())
    return {p: v / s for p, v in raw_dict.items()}

def power_devig(raw_dict):
    lo, hi = 0.5, 4.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if sum(v ** mid for v in raw_dict.values()) > 1.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    return {p: v ** k for p, v in raw_dict.items()}, k

def dec_devig_pair(o1, o2):
    # Returns (prop_p1, pow_p1)
    q1, q2 = 1.0 / o1, 1.0 / o2
    prop = q1 / (q1 + q2)
    d, _ = power_devig({"a": q1, "b": q2})
    return prop, d["a"]

def am_to_dec(am):
    return 1.0 + (am / 100.0) if am > 0 else 1.0 + (100.0 / (-am))

print("=== SPORTSBOOK MATCH ODDS DEVIG CHECK (2026-09-07) ===")
match_odds_check = [
    ("Cerundolo vs Blockx (Betano, Blockx WON)", 2.30, 1.60),
    ("Gea vs van de Zandschulp (Betano)", 2.40, 1.57),
    ("Khachanov vs Tien (Betano)", 2.50, 1.53),
    ("Zverev vs Darderi (Betano)", 1.07, 8.00),
    ("Tiafoe vs Michelsen (Betano)", 1.63, 2.25),
    ("Tiafoe vs Michelsen (DK -156/+127)", am_to_dec(-156), am_to_dec(127)),
    ("Shelton vs Alcaraz (Betano)", 3.70, 1.27),
    ("Sabalenka vs Noskova (DK -267/+212)", am_to_dec(-267), am_to_dec(212)),
]
for name, o1, o2 in match_odds_check:
    pr, pw = dec_devig_pair(o1, o2)
    print(f"  {name:44s}: Prop={pr:.4f}/{1-pr:.4f} | Pow={pw:.4f}/{1-pw:.4f}")

# =====================================================================
# PART 1: MEN'S SINGLES (Q891014 & Q408930)
# =====================================================================
# Pre-Monday Sept 7 05:33 AM ET DraftKings Predictions (AFTER Shelton beat Tsitsipas!)
men_dk_sep7_am = {
    "Carlos Alcaraz": 0.62,
    "Alexander Zverev": 0.23,
    "Ben Shelton": 0.11,
    "Frances Tiafoe": 0.06,
    "Alex Michelsen": 0.05,
    "Learner Tien": 0.04,
    "Alexander Blockx": 0.015,     # unlisted (<2%), Betano 1.60 fav vs Cerundolo 2.30 (1% on DK)
    "Francisco Cerundolo": 0.010,  # listed 1% -> ELIMINATED Mon Sep 7!
    "Karen Khachanov": 0.010,      # listed 1%
    "Luciano Darderi": 0.005,      # unlisted
    "Botic van de Zandschulp": 0.005, # unlisted
    "Arthur Gea": 0.002,           # unlisted
}

men_tree_sep7_am = (
    ((("Alexander Zverev", "Luciano Darderi"), ("Arthur Gea", "Botic van de Zandschulp")),
     (("Karen Khachanov", "Learner Tien"), ("Francisco Cerundolo", "Alexander Blockx"))),
    (("Frances Tiafoe", "Alex Michelsen"),
     ("Ben Shelton", "Carlos Alcaraz"))
)

men_tree_sep7_eod = (
    ((("Alexander Zverev", "Luciano Darderi"), ("Arthur Gea", "Botic van de Zandschulp")),
     (("Karen Khachanov", "Learner Tien"), "Alexander Blockx")),
    (("Frances Tiafoe", "Alex Michelsen"),
     ("Ben Shelton", "Carlos Alcaraz"))
)

men_h2h = {
    ("Carlos Alcaraz", "Ben Shelton"): 20,      # 3-0 H2H
    ("Frances Tiafoe", "Alex Michelsen"): 15,   # 2-0 H2H (both straight sets)
    ("Alexander Zverev", "Carlos Alcaraz"): 15, # competitive H2H on hard courts
}

m_prop = prop_devig(men_dk_sep7_am)
m_pow, m_k = power_devig(men_dk_sep7_am)
print(f"\nMen DK Sep 7 AM sum={sum(men_dk_sep7_am.values()):.4f}, power k={m_k:.3f}")
print("  Devigged (Prop vs Power):")
for p in sorted(men_dk_sep7_am, key=lambda x: -men_dk_sep7_am[x])[:8]:
    print(f"    {p:23s}: Raw={men_dk_sep7_am[p]:.3f} | Prop={m_prop[p]:.4f} | Pow={m_pow[p]:.4f}")

# Fit Elos to BOTH Prop-devig and Power-devig Sep 7 AM DK Predictions!
melos_prop = fit_elos(men_tree_sep7_am, m_prop, h2h=men_h2h)
melos_pow = fit_elos(men_tree_sep7_am, m_pow, h2h=men_h2h)

# Model 3: Pure Sportsbook-Anchored + Fundamental ATP Elo (explicitly anchored to Betano/DK Sep 7 match lines!)
# Let's check exact Elo diffs needed to reproduce Sept 7 Betano/DK match lines:
#   Tiafoe vs Michelsen: 58.0% -> total diff = +56 Elo (with +15 H2H -> base diff +41)
#   Alcaraz vs Shelton: 74.5%-76% -> total diff = +186 to +200 Elo (with +20 H2H -> base diff +166 to +180)
#   Zverev vs Darderi: 88.2%-89% -> diff = +350 to +363 Elo
#   Tien vs Khachanov: 62.0% -> diff = +85 Elo
#   BvdZ vs Gea: 60.5% -> diff = +74 Elo
#   Blockx vs Cerundolo: 59.0% (and Blockx WON 3-1) -> Blockx ~1905
melos_book_fund = {
    "Carlos Alcaraz": 2260,         # Defending champ, peak form (vs Shelton: 2260-2085+20=+195 -> 75.4%!)
    "Alexander Zverev": 2125,       # #1 seed, RG champ (vs Darderi 1775 -> +350 -> 88.2%; vs Alcaraz 2125-2260+15=-120 -> 33.4%)
    "Ben Shelton": 2085,            # #8 seed, crushed Tsitsipas 6-2 6-3 6-4 (14 pts lost on serve!) -> vs Tiafoe +75 -> 60.6%
    "Frances Tiafoe": 2010,         # #11 seed, beat Medvedev 3-0 (vs Michelsen 1969+15=+56 -> 58.0%)
    "Alex Michelsen": 1969,         # unseeded, 12-0 sets, 1st Slam QF
    "Learner Tien": 1955,           # #14 seed (vs Khachanov 1870 -> +85 -> 62.0%; vs Blockx 1915 -> +40 -> 55.7%)
    "Alexander Blockx": 1915,       # #28 seed, beat Cobolli & Cerundolo, IN QF!
    "Karen Khachanov": 1870,        # beat #3 FAA, 2022 USO SF
    "Francisco Cerundolo": 1885,    # (OUT)
    "Botic van de Zandschulp": 1850,# beat #6 de Minaur & Bergs (vs Gea 1776 -> +74 -> 60.5%)
    "Arthur Gea": 1776,             # LL #87
    "Luciano Darderi": 1775,        # #21 seed (clay specialist, beat Zverev on clay in Rome)
}

# Small Bayesian bump to Blockx in market models since he WON 3-1 over Cerundolo
for d in (melos_prop, melos_pow):
    d["Alexander Blockx"] += 15

# Blend: 35% Mkt-Power + 25% Mkt-Prop + 40% Book-Anchored Fundamental
melos_blend = {
    p: 0.35 * melos_pow[p] + 0.25 * melos_prop[p] + 0.40 * melos_book_fund[p]
    for p in melos_book_fund
}

print("\n=== MEN'S IMPLIED MATCH WIN PROBS (2026-09-07 EOD) ===")
for a, b in [
    ("Carlos Alcaraz", "Ben Shelton"),
    ("Frances Tiafoe", "Alex Michelsen"),
    ("Alexander Zverev", "Luciano Darderi"),
    ("Botic van de Zandschulp", "Arthur Gea"),
    ("Learner Tien", "Karen Khachanov"),
    ("Learner Tien", "Alexander Blockx"),
    ("Karen Khachanov", "Alexander Blockx"),
    ("Alexander Zverev", "Learner Tien"),
    ("Alexander Zverev", "Alexander Blockx"),
    ("Carlos Alcaraz", "Frances Tiafoe"),
    ("Carlos Alcaraz", "Alex Michelsen"),
    ("Ben Shelton", "Frances Tiafoe"),
    ("Ben Shelton", "Alex Michelsen"),
    ("Carlos Alcaraz", "Alexander Zverev"),
    ("Ben Shelton", "Alexander Zverev"),
]:
    print(
        f"  {a:23s} vs {b:23s}: "
        f"MktPow={win_prob(a,b,melos_pow,400,men_h2h):.3f} | "
        f"MktProp={win_prob(a,b,melos_prop,400,men_h2h):.3f} | "
        f"BookFund={win_prob(a,b,melos_book_fund,400,men_h2h):.3f} | "
        f"Blend={win_prob(a,b,melos_blend,400,men_h2h):.3f}"
    )

mdp_pow = bracket_dp(men_tree_sep7_eod, melos_pow, 400, men_h2h)
mdp_prop = bracket_dp(men_tree_sep7_eod, melos_prop, 400, men_h2h)
mdp_bf = bracket_dp(men_tree_sep7_eod, melos_book_fund, 400, men_h2h)
mdp_bld = bracket_dp(men_tree_sep7_eod, melos_blend, 400, men_h2h)

print("\n=== Q891014 MEN'S TITLE PROBS (2026-09-07 EOD) ===")
for p in sorted(mdp_bld, key=lambda x: -mdp_bld[x]):
    pblend = 0.35 * mdp_pow[p] + 0.25 * mdp_prop[p] + 0.40 * mdp_bf[p]
    print(
        f"  {p:23s}: MktPow={mdp_pow[p]:.4f} | MktProp={mdp_prop[p]:.4f} | "
        f"BookFund={mdp_bf[p]:.4f} | EloBlend={mdp_bld[p]:.4f} | ProbBlend={pblend:.4f}"
    )

# Exact DP (NO MC NOISE!) for Q408930 (Furthest U.S. Man)
# Actually let's compute exact probability table by enumerating or 500k MC!
# Wait: only 11 players -> 10 matches total -> 2^10 = 1024 outcomes!! We can compute 100% EXACT probabilities!!
def exact_q408930(elos, label, overrides=None):
    # overrides: dict of (a, b) -> p(a beats b)
    def wp(a, b):
        if overrides:
            if (a, b) in overrides:
                return overrides[(a, b)]
            if (b, a) in overrides:
                return 1.0 - overrides[(b, a)]
        return win_prob(a, b, elos, 400.0, men_h2h)

    US = ["Frances Tiafoe", "Alex Michelsen", "Ben Shelton", "Learner Tien"]
    uniq = defaultdict(float)
    split = defaultdict(float)
    seed_tb = defaultdict(float)  # if tie resolved by seed: Shelton(8) > Tiafoe(11) > Tien(14) > Michelsen(unseeded)
    seed_rank = {"Ben Shelton": 8, "Frances Tiafoe": 11, "Learner Tien": 14, "Alex Michelsen": 99}
    tie_prob = 0.0
    tie_breakdown = defaultdict(float)

    # Top half: Q1 = ((Zverev, Darderi), (Gea, BvdZ)), Q2 = ((Khachanov, Tien), Blockx)
    # Enumerate Q1 winner distribution
    q1_dist = bracket_dp((("Alexander Zverev", "Luciano Darderi"), ("Arthur Gea", "Botic van de Zandschulp")), elos, 400.0, men_h2h)

    # Enumerate all exact paths of Q2, Q3, Q4, SF1, SF2, Final!
    p_tien_r4 = wp("Learner Tien", "Karen Khachanov")
    q2_r4_cases = [("Learner Tien", p_tien_r4, 5), ("Karen Khachanov", 1.0 - p_tien_r4, 4)]
    p_tia_q3 = wp("Frances Tiafoe", "Alex Michelsen")
    q3_cases = [("Frances Tiafoe", p_tia_q3), ("Alex Michelsen", 1.0 - p_tia_q3)]
    p_sh_q4 = wp("Ben Shelton", "Carlos Alcaraz")
    q4_cases = [("Ben Shelton", p_sh_q4), ("Carlos Alcaraz", 1.0 - p_sh_q4)]

    for q1w, pq1 in q1_dist.items():
        for q2a, pq2a, tien_r_base in q2_r4_cases:
            p_q2a_w = wp(q2a, "Alexander Blockx")
            for q2w, pq2w in [(q2a, p_q2a_w), ("Alexander Blockx", 1.0 - p_q2a_w)]:
                tien_r_qf = 6 if q2w == "Learner Tien" else tien_r_base
                p_sf1_q1 = wp(q1w, q2w)
                for f1, pf1 in [(q1w, p_sf1_q1), (q2w, 1.0 - p_sf1_q1)]:
                    tien_r_sf = 7 if f1 == "Learner Tien" else tien_r_qf
                    for q3w, pq3 in q3_cases:
                        for q4w, pq4 in q4_cases:
                            p_sf2_q3 = wp(q3w, q4w)
                            for f2, pf2 in [(q3w, p_sf2_q3), (q4w, 1.0 - p_sf2_q3)]:
                                p_ch_f1 = wp(f1, f2)
                                for ch, pch in [(f1, p_ch_f1), (f2, 1.0 - p_ch_f1)]:
                                    prob = pq1 * pq2a * pq2w * pf1 * pq3 * pq4 * pf2 * pch
                                    sc = {
                                        "Frances Tiafoe": 5,
                                        "Alex Michelsen": 5,
                                        "Ben Shelton": 5,
                                        "Learner Tien": tien_r_sf,
                                    }
                                    sc[q3w] = 6
                                    if q4w == "Ben Shelton":
                                        sc["Ben Shelton"] = 6
                                    if f2 in sc:
                                        sc[f2] = 7
                                    if ch in sc:
                                        sc[ch] = 8
                                    mx = max(sc.values())
                                    tops = [u for u in US if sc[u] == mx]
                                    if len(tops) == 1:
                                        uniq[tops[0]] += prob
                                        split[tops[0]] += prob
                                        seed_tb[tops[0]] += prob
                                    else:
                                        tie_prob += prob
                                        tie_breakdown[tuple(sorted(tops))] += prob
                                        for u in tops:
                                            split[u] += prob / len(tops)
                                        best_seed = min(tops, key=lambda u: seed_rank[u])
                                        seed_tb[best_seed] += prob

    un = 1.0 - tie_prob
    print(f"\nQ408930 EXACT [{label}] (TieProb={tie_prob:.4f})")
    print("  Tie breakdown:", {k: round(v, 4) for k, v in tie_breakdown.items()})
    print("  UniqCond : " + " | ".join(f"{u.split()[1]}={uniq[u]/un:.4f}" for u in US))
    print("  Split50  : " + " | ".join(f"{u.split()[1]}={split[u]:.4f}" for u in US))
    print("  85U+15S  : " + " | ".join(f"{u.split()[1]}={0.85*uniq[u]/un + 0.15*split[u]:.4f}" for u in US))
    print("  SeedTB   : " + " | ".join(f"{u.split()[1]}={seed_tb[u]:.4f}" for u in US))

print("\n=== Q408930 EXACT SENSITIVITY GRID (2026-09-07 EOD) ===")
exact_q408930(melos_pow, "MktPow")
exact_q408930(melos_prop, "MktProp")
exact_q408930(melos_book_fund, "BookFund (Alcaraz=75.4%, Tiafoe=58.0%, Tien=62.0%)")
exact_q408930(melos_blend, "Blend (35Pow/25Prop/40BookFund)")
exact_q408930(
    melos_blend,
    "Blend + Exact Book Lines (Tia58, Alc75, Tien62)",
    overrides={
        ("Frances Tiafoe", "Alex Michelsen"): 0.580,
        ("Carlos Alcaraz", "Ben Shelton"): 0.750,
        ("Learner Tien", "Karen Khachanov"): 0.620,
    },
)
exact_q408930(
    melos_blend,
    "Blend + Stronger Alcaraz (Tia58, Alc78, Tien62)",
    overrides={
        ("Frances Tiafoe", "Alex Michelsen"): 0.580,
        ("Carlos Alcaraz", "Ben Shelton"): 0.780,
        ("Learner Tien", "Karen Khachanov"): 0.620,
    },
)

# =====================================================================
# PART 2: WOMEN'S SINGLES (Q608158)
# =====================================================================
wom_dk_sep7_am = {
    "Aryna Sabalenka": 0.33,
    "Coco Gauff": 0.23,
    "Iga Swiatek": 0.16,        # ELIMINATED Mon Sep 7!
    "Jessica Pegula": 0.13,
    "Mirra Andreeva": 0.08,     # WON R4!
    "Elena Rybakina": 0.07,     # CRUSHED Osaka 6-1, 6-4!
    "Linda Noskova": 0.06,
    "Emma Navarro": 0.05,
    "Naomi Osaka": 0.05,        # ELIMINATED Mon Sep 7!
    "Iva Jovic": 0.02,          # plays Gauff Mon night
    "Zheng Qinwen": 0.018,      # unlisted (<2%), STUNNED Swiatek 7-5, 6-3!
    "Anastasia Potapova": 0.012,# unlisted (<2%), ELIMINATED Mon Sep 7!
}

wom_tree_sep7_am = (
    (("Aryna Sabalenka", "Linda Noskova"),
     ("Jessica Pegula", "Emma Navarro")),
    ((("Mirra Andreeva", "Anastasia Potapova"), ("Coco Gauff", "Iva Jovic")),
     (("Iga Swiatek", "Zheng Qinwen"), ("Naomi Osaka", "Elena Rybakina")))
)

wom_tree_sep7_eod = (
    (("Aryna Sabalenka", "Linda Noskova"),
     ("Jessica Pegula", "Emma Navarro")),
    (("Mirra Andreeva", ("Coco Gauff", "Iva Jovic")),
     ("Zheng Qinwen", "Elena Rybakina"))
)

wom_h2h = {
    ("Aryna Sabalenka", "Linda Noskova"): 20,  # 2-0 H2H, never dropped a set, Indian Wells 2026 SF
    ("Coco Gauff", "Iva Jovic"): 20,           # 1-0 H2H + Jovic 3h epic vs Eala
    ("Elena Rybakina", "Zheng Qinwen"): 15,    # Rybakina 2-1 H2H, elite serve on fast hard courts
    ("Aryna Sabalenka", "Jessica Pegula"): 15, # Sabalenka won 2024 USO final & strong hard-court H2H
}

w_prop = prop_devig(wom_dk_sep7_am)
w_pow, w_k = power_devig(wom_dk_sep7_am)
print(f"\nWomen DK Sep 7 AM sum={sum(wom_dk_sep7_am.values()):.4f}, power k={w_k:.3f}")
for p in sorted(wom_dk_sep7_am, key=lambda x: -wom_dk_sep7_am[x]):
    print(f"    {p:23s}: Raw={wom_dk_sep7_am[p]:.3f} | Prop={w_prop[p]:.4f} | Pow={w_pow[p]:.4f}")

welos_prop = fit_elos(wom_tree_sep7_am, w_prop, h2h=wom_h2h)
welos_pow = fit_elos(wom_tree_sep7_am, w_pow, h2h=wom_h2h)

# Bayesian post-Monday updates to market-fitted Elos:
# - Rybakina destroyed Osaka 6-1, 6-4 in 66 min (erasing fitness worries that depressed her Sep 7 AM price from 9% to 7%!)
# - Zheng beat Swiatek 7-5, 6-3 (7 straight wins, 2x 0-5 comebacks; former #4/Olympic champ recapturing peak!)
# - Andreeva needed 3 sets (5-7, 6-4, 6-3) vs Potapova (slight -5 Elo)
welos_pow_bayes = dict(welos_pow)
welos_prop_bayes = dict(welos_prop)
for d in (welos_pow_bayes, welos_prop_bayes):
    d["Elena Rybakina"] += 50
    d["Zheng Qinwen"] += 60
    d["Mirra Andreeva"] -= 5

# Model 3: Fundamental WTA Hard-Court Elo (anchored to DK Sabalenka-Noskova 70%/30%, 2026 Slam winners & form!)
welos_fund = {
    "Aryna Sabalenka": 2125,     # #1, 2x defending USO champ, 8-0 sets (vs Noskova 1995+20=+150 -> 70.3%!)
    "Coco Gauff": 2095,          # #4, 2023 USO champ, 2026 Cincy champ, 6-0 sets
    "Elena Rybakina": 2085,      # #2, 2026 AO champ, 8-0 sets, crushed Osaka 6-1 6-4, playing for #1!
    "Jessica Pegula": 2020,      # #3, 2024 USO finalist, AO 2026 SF, beat Cirstea 6-3 6-4
    "Mirra Andreeva": 2015,      # #5, 2026 RG champ, 1st USO QF (beat Potapova in 3)
    "Linda Noskova": 1995,       # #6, 2026 Wimbledon champ, 1st USO QF (DK +212 vs Sabalenka -> ~30%)
    "Zheng Qinwen": 1965,        # Q #121, former #4 & Olympic gold, 7 straight NY wins incl. Keys & Swiatek!
    "Emma Navarro": 1935,        # #26, 2024 USO SF, beat Muchova & Kalinskaya 6-4 6-2 (vs Pegula: -85 -> 38%)
    "Iva Jovic": 1885,           # #14, 18yo, fatigued after 3h vs Eala (vs Gauff: -210-20=-230 -> 21%)
    "Iga Swiatek": 2040,         # (OUT)
    "Naomi Osaka": 1960,         # (OUT)
    "Anastasia Potapova": 1890,  # (OUT)
}

welos_blend = {
    p: 0.35 * welos_pow_bayes[p] + 0.25 * welos_prop_bayes[p] + 0.40 * welos_fund[p]
    for p in welos_fund
}

print("\n=== WOMEN'S IMPLIED MATCH WIN PROBS (2026-09-07 EOD) ===")
for a, b in [
    ("Aryna Sabalenka", "Linda Noskova"),
    ("Jessica Pegula", "Emma Navarro"),
    ("Coco Gauff", "Iva Jovic"),
    ("Coco Gauff", "Mirra Andreeva"),
    ("Elena Rybakina", "Zheng Qinwen"),
    ("Aryna Sabalenka", "Jessica Pegula"),
    ("Aryna Sabalenka", "Coco Gauff"),
    ("Aryna Sabalenka", "Elena Rybakina"),
    ("Coco Gauff", "Elena Rybakina"),
    ("Mirra Andreeva", "Elena Rybakina"),
    ("Mirra Andreeva", "Zheng Qinwen"),
]:
    print(
        f"  {a:20s} vs {b:20s}: "
        f"MktPowB={win_prob(a,b,welos_pow_bayes,400,wom_h2h):.3f} | "
        f"MktPropB={win_prob(a,b,welos_prop_bayes,400,wom_h2h):.3f} | "
        f"Fund={win_prob(a,b,welos_fund,400,wom_h2h):.3f} | "
        f"Blend={win_prob(a,b,welos_blend,400,wom_h2h):.3f}"
    )

wdp_pow_raw = bracket_dp(wom_tree_sep7_eod, welos_pow, 400, wom_h2h)
wdp_pow_b = bracket_dp(wom_tree_sep7_eod, welos_pow_bayes, 400, wom_h2h)
wdp_prop_b = bracket_dp(wom_tree_sep7_eod, welos_prop_bayes, 400, wom_h2h)
wdp_fnd = bracket_dp(wom_tree_sep7_eod, welos_fund, 400, wom_h2h)
wdp_bld = bracket_dp(wom_tree_sep7_eod, welos_blend, 400, wom_h2h)

print("\n=== Q608158 WOMEN'S TITLE PROBS (2026-09-07 EOD) ===")
for p in sorted(wdp_bld, key=lambda x: -wdp_bld[x]):
    pblend = 0.35 * wdp_pow_b[p] + 0.25 * wdp_prop_b[p] + 0.40 * wdp_fnd[p]
    print(
        f"  {p:20s}: PowNoB={wdp_pow_raw[p]:.4f} | PowB={wdp_pow_b[p]:.4f} | "
        f"PropB={wdp_prop_b[p]:.4f} | Fund={wdp_fnd[p]:.4f} | EloBlend={wdp_bld[p]:.4f} | ProbBlend={pblend:.4f}"
    )
