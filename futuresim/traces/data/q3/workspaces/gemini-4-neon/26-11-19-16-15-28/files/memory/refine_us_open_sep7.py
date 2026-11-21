import math
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

def shin_devig(raw_dict):
    # Standard Shin (1993) devigging for prediction-market / bookmaker longshot bias
    S = sum(raw_dict.values())
    lo, hi = 0.0, 0.5
    for _ in range(100):
        z = 0.5 * (lo + hi)
        ps = {}
        for p, q in raw_dict.items():
            val = (math.sqrt(z*z + 4*(1-z)*q*q/S) - z) / (2*(1-z))
            ps[p] = val
        if sum(ps.values()) > 1.0:
            lo = z
        else:
            hi = z
    z = 0.5 * (lo + hi)
    return {p: (math.sqrt(z*z + 4*(1-z)*q*q/S) - z) / (2*(1-z)) for p, q in raw_dict.items()}, z

# =====================================================================
# PART 1: MEN'S SINGLES (Q891014 & Q408930)
# =====================================================================
men_dk_sep7_am = {
    "Carlos Alcaraz": 0.62,
    "Alexander Zverev": 0.23,
    "Ben Shelton": 0.11,
    "Frances Tiafoe": 0.06,
    "Alex Michelsen": 0.05,
    "Learner Tien": 0.04,
    "Alexander Blockx": 0.015,
    "Francisco Cerundolo": 0.010,
    "Karen Khachanov": 0.010,
    "Luciano Darderi": 0.005,
    "Botic van de Zandschulp": 0.005,
    "Arthur Gea": 0.002,
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

m_pow, mk = power_devig(men_dk_sep7_am)
m_shin, mz = shin_devig(men_dk_sep7_am)
print(f"=== MEN DK SEP 7 AM DEVIG (sum={sum(men_dk_sep7_am.values()):.3f}, pow_k={mk:.3f}, shin_z={mz:.4f}) ===")
for p in sorted(men_dk_sep7_am, key=lambda x: -men_dk_sep7_am[x])[:8]:
    print(f"  {p:23s}: Raw={men_dk_sep7_am[p]:.3f} | Pow={m_pow[p]:.4f} | Shin={m_shin[p]:.4f}")

melos_pow = fit_elos(men_tree_sep7_am, m_pow, h2h=men_h2h)
melos_shin = fit_elos(men_tree_sep7_am, m_shin, h2h=men_h2h)
for d in (melos_pow, melos_shin):
    d["Alexander Blockx"] += 15  # beat Cerundolo 3-1

# Book-Anchored + Fundamental ATP Elo (calibrated to peak Alcaraz + Betano/DK Sep 7 lines!):
# Check exact match lines:
#   Alcaraz vs Shelton: 2295 - 2100 + 20 = +215 -> 77.5% (Betano Pow=76.7%, Prop=74.5%; DK-implied ~79.8%)
#   Zverev vs Alcaraz: 2140 - 2295 + 15 = -140 -> 30.9% Zverev / 69.1% Alcaraz
#   Zverev vs Darderi: 2140 - 1785 = +355 -> 88.5% (Betano 88.2%-92.1%)
#   Tiafoe vs Michelsen: 2015 - 1974 + 15 = +56 -> 58.0% (EXACT DK -156/+127 & Betano 1.63/2.25!)
#   Shelton vs Tiafoe: 2100 - 2015 = +85 -> 62.0%
#   Tien vs Khachanov: 1960 - 1875 = +85 -> 62.0% (EXACT Betano 1.53/2.50!)
#   Tien vs Blockx: 1960 - 1915 = +45 -> 56.4%
#   BvdZ vs Gea: 1855 - 1781 = +74 -> 60.5% (EXACT Betano 1.57/2.40!)
melos_book = {
    "Carlos Alcaraz": 2295,
    "Alexander Zverev": 2140,
    "Ben Shelton": 2100,
    "Frances Tiafoe": 2015,
    "Alex Michelsen": 1974,
    "Learner Tien": 1960,
    "Alexander Blockx": 1915,
    "Karen Khachanov": 1875,
    "Francisco Cerundolo": 1885,
    "Botic van de Zandschulp": 1855,
    "Arthur Gea": 1781,
    "Luciano Darderi": 1785,
}

# Blend: 35% Mkt-Power + 25% Mkt-Shin + 40% Book-Anchored Fundamental
melos_blend = {
    p: 0.35 * melos_pow[p] + 0.25 * melos_shin[p] + 0.40 * melos_book[p]
    for p in melos_book
}

print("\n=== MEN'S REFINED MATCHUPS (2026-09-07 EOD) ===")
for a, b in [
    ("Carlos Alcaraz", "Ben Shelton"),
    ("Frances Tiafoe", "Alex Michelsen"),
    ("Alexander Zverev", "Luciano Darderi"),
    ("Botic van de Zandschulp", "Arthur Gea"),
    ("Learner Tien", "Karen Khachanov"),
    ("Learner Tien", "Alexander Blockx"),
    ("Alexander Zverev", "Learner Tien"),
    ("Carlos Alcaraz", "Frances Tiafoe"),
    ("Carlos Alcaraz", "Alex Michelsen"),
    ("Ben Shelton", "Frances Tiafoe"),
    ("Carlos Alcaraz", "Alexander Zverev"),
]:
    print(
        f"  {a:23s} vs {b:23s}: "
        f"Pow={win_prob(a,b,melos_pow,400,men_h2h):.3f} | "
        f"Shin={win_prob(a,b,melos_shin,400,men_h2h):.3f} | "
        f"Book={win_prob(a,b,melos_book,400,men_h2h):.3f} | "
        f"Blend={win_prob(a,b,melos_blend,400,men_h2h):.3f}"
    )

mdp_pow = bracket_dp(men_tree_sep7_eod, melos_pow, 400, men_h2h)
mdp_shin = bracket_dp(men_tree_sep7_eod, melos_shin, 400, men_h2h)
mdp_book = bracket_dp(men_tree_sep7_eod, melos_book, 400, men_h2h)
mdp_bld = bracket_dp(men_tree_sep7_eod, melos_blend, 400, men_h2h)

print("\n=== Q891014 REFINED MEN'S TITLE PROBS ===")
for p in sorted(mdp_bld, key=lambda x: -mdp_bld[x]):
    pblend = 0.35 * mdp_pow[p] + 0.25 * mdp_shin[p] + 0.40 * mdp_book[p]
    print(
        f"  {p:23s}: Pow={mdp_pow[p]:.4f} | Shin={mdp_shin[p]:.4f} | "
        f"Book={mdp_book[p]:.4f} | EloBlend={mdp_bld[p]:.4f} | ProbBlend={pblend:.4f}"
    )

# Exact Q408930 with exact book lines check
def exact_q408930(elos, label, overrides=None):
    def wp(a, b):
        if overrides:
            if (a, b) in overrides: return overrides[(a, b)]
            if (b, a) in overrides: return 1.0 - overrides[(b, a)]
        return win_prob(a, b, elos, 400.0, men_h2h)

    US = ["Frances Tiafoe", "Alex Michelsen", "Ben Shelton", "Learner Tien"]
    uniq = defaultdict(float)
    split = defaultdict(float)
    tie_prob = 0.0
    q1_dist = bracket_dp((("Alexander Zverev", "Luciano Darderi"), ("Arthur Gea", "Botic van de Zandschulp")), elos, 400.0, men_h2h)
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
                                    sc = {"Frances Tiafoe": 5, "Alex Michelsen": 5, "Ben Shelton": 5, "Learner Tien": tien_r_sf}
                                    sc[q3w] = 6
                                    if q4w == "Ben Shelton": sc["Ben Shelton"] = 6
                                    if f2 in sc: sc[f2] = 7
                                    if ch in sc: sc[ch] = 8
                                    mx = max(sc.values())
                                    tops = [u for u in US if sc[u] == mx]
                                    if len(tops) == 1:
                                        uniq[tops[0]] += prob
                                        split[tops[0]] += prob
                                    else:
                                        tie_prob += prob
                                        for u in tops: split[u] += prob / len(tops)
    un = 1.0 - tie_prob
    print(f"  [{label:40s}] Tie={tie_prob:.3f} | Uniq: " +
          " ".join(f"{u.split()[1][:4]}={uniq[u]/un:.3f}" for u in US) +
          " | 85U15S: " + " ".join(f"{u.split()[1][:4]}={0.85*uniq[u]/un+0.15*split[u]:.3f}" for u in US))

print("\n=== Q408930 REFINED SENSITIVITY ===")
exact_q408930(melos_pow, "MktPow")
exact_q408930(melos_shin, "MktShin")
exact_q408930(melos_book, "BookFund (Alc77.5, Tia58, Tien62)")
exact_q408930(melos_blend, "Blend (35Pow/25Shin/40Book)")
exact_q408930(melos_blend, "Blend + ExactBook (Alc76, Tia58, Tien62)", {
    ("Carlos Alcaraz", "Ben Shelton"): 0.760,
    ("Frances Tiafoe", "Alex Michelsen"): 0.580,
    ("Learner Tien", "Karen Khachanov"): 0.620,
})
exact_q408930(melos_blend, "Blend + ExactBook (Alc77, Tia58.5, Tien62.5)", {
    ("Carlos Alcaraz", "Ben Shelton"): 0.770,
    ("Frances Tiafoe", "Alex Michelsen"): 0.585,
    ("Learner Tien", "Karen Khachanov"): 0.625,
})

# =====================================================================
# PART 2: WOMEN'S SINGLES (Q608158)
# =====================================================================
wom_dk_sep7_am = {
    "Aryna Sabalenka": 0.33,
    "Coco Gauff": 0.23,
    "Iga Swiatek": 0.16,
    "Jessica Pegula": 0.13,
    "Mirra Andreeva": 0.08,
    "Elena Rybakina": 0.07,
    "Linda Noskova": 0.06,
    "Emma Navarro": 0.05,
    "Naomi Osaka": 0.05,
    "Iva Jovic": 0.02,
    "Zheng Qinwen": 0.018,
    "Anastasia Potapova": 0.012,
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
    ("Aryna Sabalenka", "Linda Noskova"): 20,  # 2-0 H2H, 0 sets lost
    ("Coco Gauff", "Iva Jovic"): 20,           # 1-0 H2H + Jovic 3h epic
    ("Elena Rybakina", "Zheng Qinwen"): 15,    # Rybakina 2-1 H2H, elite serve
    ("Aryna Sabalenka", "Jessica Pegula"): 15, # 2024 USO final winner
}

w_pow, wk = power_devig(wom_dk_sep7_am)
w_shin, wz = shin_devig(wom_dk_sep7_am)
print(f"\n=== WOMEN DK SEP 7 AM DEVIG (sum={sum(wom_dk_sep7_am.values()):.3f}, pow_k={wk:.3f}, shin_z={wz:.4f}) ===")
for p in sorted(wom_dk_sep7_am, key=lambda x: -wom_dk_sep7_am[x]):
    print(f"  {p:20s}: Raw={wom_dk_sep7_am[p]:.3f} | Pow={w_pow[p]:.4f} | Shin={w_shin[p]:.4f}")

welos_pow = fit_elos(wom_tree_sep7_am, w_pow, h2h=wom_h2h)
welos_shin = fit_elos(wom_tree_sep7_am, w_shin, h2h=wom_h2h)

# Bayesian post-Monday updates (check sensitivity: Moderate +40/+50 vs Strong +55/+65!)
welos_pow_b = dict(welos_pow)
welos_shin_b = dict(welos_shin)
for d in (welos_pow_b, welos_shin_b):
    d["Elena Rybakina"] += 50
    d["Zheng Qinwen"] += 60
    d["Mirra Andreeva"] -= 5

# Fundamental WTA Hard-Court Elo (anchored to DK Sabalenka -267/+212 = 70.5% vs Noskova,
# AO 2026 final Rybakina def Sabalenka, 2x defending USO champ Sabalenka, 2023 USO & Cincy champ Gauff!)
welos_fund = {
    "Aryna Sabalenka": 2135,    # #1, 2x defending USO champ, 8-0 sets (vs Noskova 2000+20=+155 -> 70.9%!)
    "Coco Gauff": 2095,         # #4, 2023 USO & 2026 Cincy champ, 6-0 sets
    "Elena Rybakina": 2090,     # #2, 2026 AO champ (beat Sabalenka!), 8-0 sets, 66-min 6-1 6-4 vs Osaka
    "Jessica Pegula": 2020,     # #3, 2024 USO finalist, AO 2026 SF
    "Mirra Andreeva": 2010,     # #5, 2026 RG champ, 1st USO QF
    "Linda Noskova": 2000,      # #6, 2026 Wimbledon champ
    "Zheng Qinwen": 1965,       # Q #121, Olympic gold, 7 straight NY wins incl. Keys & Swiatek
    "Emma Navarro": 1935,       # #26, 2024 USO SF, beat Muchova & Kalinskaya
    "Iva Jovic": 1885,          # #14, 18yo, 3h match vs Eala
    "Iga Swiatek": 2040,
    "Naomi Osaka": 1960,
    "Anastasia Potapova": 1890,
}

welos_blend = {
    p: 0.35 * welos_pow_b[p] + 0.25 * welos_shin_b[p] + 0.40 * welos_fund[p]
    for p in welos_fund
}

print("\n=== WOMEN'S REFINED MATCHUPS ===")
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
]:
    print(
        f"  {a:20s} vs {b:20s}: "
        f"PowB={win_prob(a,b,welos_pow_b,400,wom_h2h):.3f} | "
        f"ShinB={win_prob(a,b,welos_shin_b,400,wom_h2h):.3f} | "
        f"Fund={win_prob(a,b,welos_fund,400,wom_h2h):.3f} | "
        f"Blend={win_prob(a,b,welos_blend,400,wom_h2h):.3f}"
    )

wdp_pow = bracket_dp(wom_tree_sep7_eod, welos_pow_b, 400, wom_h2h)
wdp_shin = bracket_dp(wom_tree_sep7_eod, welos_shin_b, 400, wom_h2h)
wdp_fund = bracket_dp(wom_tree_sep7_eod, welos_fund, 400, wom_h2h)
wdp_bld = bracket_dp(wom_tree_sep7_eod, welos_blend, 400, wom_h2h)

# Also check sensitivity if Rybakina Bayes boost is smaller (+30 instead of +50)
welos_pow_mild = dict(welos_pow); welos_pow_mild["Elena Rybakina"] += 30; welos_pow_mild["Zheng Qinwen"] += 45; welos_pow_mild["Mirra Andreeva"] -= 5
wdp_mild = bracket_dp(wom_tree_sep7_eod, welos_pow_mild, 400, wom_h2h)

print("\n=== Q608158 REFINED WOMEN'S TITLE PROBS ===")
for p in sorted(wdp_bld, key=lambda x: -wdp_bld[x]):
    pblend = 0.35 * wdp_pow[p] + 0.25 * wdp_shin[p] + 0.40 * wdp_fund[p]
    print(
        f"  {p:20s}: MildPow={wdp_mild[p]:.4f} | PowB={wdp_pow[p]:.4f} | ShinB={wdp_shin[p]:.4f} | "
        f"Fund={wdp_fund[p]:.4f} | EloBlend={wdp_bld[p]:.4f} | ProbBlend={pblend:.4f}"
    )
