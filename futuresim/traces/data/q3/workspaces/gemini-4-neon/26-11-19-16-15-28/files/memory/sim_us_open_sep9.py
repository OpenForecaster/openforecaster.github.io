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

def fit_elos(tree_pre, targets, scale=400.0, h2h=None, steps=500):
    elos = {k: 2000.0 for k in targets}
    for _ in range(steps):
        cur = bracket_dp(tree_pre, elos, scale, h2h)
        for p, tgt in targets.items():
            if tgt > 0 and cur.get(p, 0) > 0:
                elos[p] += 35.0 * math.log(tgt / cur[p])
        m = sum(elos.values()) / len(elos)
        for p in elos:
            elos[p] -= (m - 2000.0)
    return elos

def prop_devig(d):
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}

def power_devig(raw_dict):
    lo, hi = 0.5, 5.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if sum(v ** mid for v in raw_dict.values()) > 1.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    return {p: v ** k for p, v in raw_dict.items()}, k

def shin_devig(raw_dict):
    S = sum(raw_dict.values())
    lo, hi = 0.0, 0.5
    for _ in range(100):
        z = 0.5 * (lo + hi)
        ps = {p: (math.sqrt(z*z + 4*(1-z)*q*q/S) - z) / (2*(1-z)) for p, q in raw_dict.items()}
        if sum(ps.values()) > 1.0:
            lo = z
        else:
            hi = z
    z = 0.5 * (lo + hi)
    return {p: (math.sqrt(z*z + 4*(1-z)*q*q/S) - z) / (2*(1-z)) for p, q in raw_dict.items()}, z

def am_to_raw(odds):
    return 100.0 / (odds + 100.0) if odds > 0 else (-odds) / (-odds + 100.0)

def dec_to_raw(odds):
    return 1.0 / odds

# ==============================================================================
# 1. Q408930: SHELTON VS TIAFOE (EXACT 2-WAY MATCH)
# ==============================================================================
print("==================================================================")
print("1. Q408930: BEN SHELTON vs FRANCES TIAFOE (ALL-AMERICAN SF)")
print("==================================================================")
books_st = {
    "TAB (1.33 / 3.40)": {"Ben Shelton": dec_to_raw(1.33), "Frances Tiafoe": dec_to_raw(3.40)},
    "Leon.bet (1.31 / 3.35)": {"Ben Shelton": dec_to_raw(1.31), "Frances Tiafoe": dec_to_raw(3.35)},
    "SI (-285 / +225 est)": {"Ben Shelton": am_to_raw(-285), "Frances Tiafoe": am_to_raw(225)},
    "SI (-285 / +230 est)": {"Ben Shelton": am_to_raw(-285), "Frances Tiafoe": am_to_raw(230)},
}
for name, raw in books_st.items():
    p_pr = prop_devig(raw)
    p_pw, _ = power_devig(raw)
    p_sh, _ = shin_devig(raw)
    print(f"  {name:24s} | Raw sum={sum(raw.values()):.4f} | Prop={p_pr['Ben Shelton']:.4f} | Pow={p_pw['Ben Shelton']:.4f} | Shin={p_sh['Ben Shelton']:.4f}")
print("  Stats Insider ML model   | Shelton = 0.7200 | Tiafoe = 0.2800")

# ==============================================================================
# 2. Q891014: MEN'S SINGLES TITLE (5 SURVIVORS, KHACHANOV ALREADY WON QF!)
# ==============================================================================
print("\n==================================================================")
print("2. Q891014: MEN'S SINGLES TITLE (POST-ALCARAZ & POST-KHACHANOV WIN)")
print("==================================================================")
si_men_raw = {
    "Alexander Zverev": am_to_raw(110),
    "Ben Shelton": am_to_raw(140),
    "Frances Tiafoe": am_to_raw(650),
    "Karen Khachanov": am_to_raw(1700),
    "Alexander Blockx": am_to_raw(3000),
    "Botic van de Zandschulp": am_to_raw(4000),
}
si_pr = prop_devig(si_men_raw)
si_pw, sk = power_devig(si_men_raw)
si_sh, sz = shin_devig(si_men_raw)
print(f"SI.com pre-Khachanov raw sum = {sum(si_men_raw.values()):.4f} (pow k={sk:.3f}, shin z={sz:.4f})")
for p in si_men_raw:
    print(f"  {p:24s}: Raw={si_men_raw[p]:.4f} | Prop={si_pr[p]:.4f} | Pow={si_pw[p]:.4f} | Shin={si_sh[p]:.4f}")

# Kalshi pre-Khachanov: Zverev 44%, Shelton 37%, Tiafoe 10%, remaining 9% split across Khachanov/Blockx/BvdZ
# Proportional to SI devigged shares of the 3 bottom-half longshots:
rem_si = {p: si_pw[p] for p in ["Karen Khachanov", "Alexander Blockx", "Botic van de Zandschulp"]}
rem_s = sum(rem_si.values())
kalshi_men_pre = {
    "Alexander Zverev": 0.440,
    "Ben Shelton": 0.370,
    "Frances Tiafoe": 0.100,
    "Karen Khachanov": 0.090 * rem_si["Karen Khachanov"] / rem_s,
    "Alexander Blockx": 0.090 * rem_si["Alexander Blockx"] / rem_s,
    "Botic van de Zandschulp": 0.090 * rem_si["Botic van de Zandschulp"] / rem_s,
}
print("\nKalshi pre-Khachanov (with 9% longshot mass split per SI Power):")
for p, v in kalshi_men_pre.items():
    print(f"  {p:24s}: {v:.4f}")

men_tree_pre_wed = (
    (("Alexander Zverev", "Botic van de Zandschulp"),
     ("Karen Khachanov", "Alexander Blockx")),
    ("Ben Shelton", "Frances Tiafoe")
)
men_tree_post_khach = (
    (("Alexander Zverev", "Botic van de Zandschulp"),
     "Karen Khachanov"),
    ("Ben Shelton", "Frances Tiafoe")
)

# H2H adjustments:
# Zverev is 5-0 vs Shelton! Let's test both with H2H (+35 Elo = ~+5% edge for Zverev) and without!
# Shelton is 3-1 vs Tiafoe (+15 Elo)
men_h2h_strong = {
    ("Alexander Zverev", "Ben Shelton"): 35,
    ("Ben Shelton", "Frances Tiafoe"): 15,
}
men_h2h_mild = {
    ("Alexander Zverev", "Ben Shelton"): 20,
    ("Ben Shelton", "Frances Tiafoe"): 10,
}

for label, targets, h2h in [
    ("SI_Power + H2H_mild", si_pw, men_h2h_mild),
    ("SI_Shin  + H2H_mild", si_sh, men_h2h_mild),
    ("Kalshi   + H2H_mild", kalshi_men_pre, men_h2h_mild),
    ("Kalshi   + H2H_strong", kalshi_men_pre, men_h2h_strong),
    ("SI_Power + H2H_strong", si_pw, men_h2h_strong),
]:
    elos = fit_elos(men_tree_pre_wed, targets, h2h=h2h)
    post = bracket_dp(men_tree_post_khach, elos, h2h=h2h)
    p_zv_bvdz = win_prob("Alexander Zverev", "Botic van de Zandschulp", elos, h2h=h2h)
    p_kh_bl = win_prob("Karen Khachanov", "Alexander Blockx", elos, h2h=h2h)
    p_zv_kh = win_prob("Alexander Zverev", "Karen Khachanov", elos, h2h=h2h)
    p_sh_ti = win_prob("Ben Shelton", "Frances Tiafoe", elos, h2h=h2h)
    p_zv_sh = win_prob("Alexander Zverev", "Ben Shelton", elos, h2h=h2h)
    p_zv_fin_pre = p_zv_bvdz * (p_kh_bl * p_zv_kh + (1 - p_kh_bl) * win_prob("Alexander Zverev", "Alexander Blockx", elos, h2h=h2h))
    p_zv_fin_post = p_zv_bvdz * p_zv_kh
    print(f"\n[{label}]")
    print(f"  Implied match probs: Zv>BvdZ={p_zv_bvdz:.3f} | Kh>Bl={p_kh_bl:.3f} | Zv>Kh={p_zv_kh:.3f} | Sh>Ti={p_sh_ti:.3f} | Zv>Sh={p_zv_sh:.3f}")
    print(f"  Zverev Final prob: pre={p_zv_fin_pre:.3f} -> post-Khach={p_zv_fin_post:.3f}")
    for p in ["Alexander Zverev", "Ben Shelton", "Frances Tiafoe", "Karen Khachanov", "Botic van de Zandschulp"]:
        print(f"    {p:24s}: pre={targets[p]:.4f} -> post={post[p]:.4f}")

# Direct explicit match-probability matrix check (anchored to EXACT Sep 9 match markets!)
# Known Sep 9 match markets:
#   P(Zverev > BvdZ) = 0.880 (Kalshi exact!)
#   P(Shelton > Tiafoe) = 0.725 (TAB/Leon/SI/StatsInsider!)
#   P(Zverev > Khachanov) = 0.790 - 0.820 (check: Kalshi pre-QF Zverev Final=74% / 88% QF = 84.1% avg vs {Kh, injured Bl}; if Zv>Bl=0.90 & Kh>Bl=0.65, then 0.65*x + 0.35*0.90 = 0.841 => x = 0.809!)
#   Wait: Check Zverev vs Khachanov H2H & form: Zverev #1 seed vs #30s unseeded Khachanov (who saved energy in 1h38m vs Blockx) -> ~0.79-0.81!
#   P(Zverev > Shelton in Final): Zverev is 5-0 vs Shelton, #1 seed, RG 2026 champ! If Zverev~0.59 vs Shelton, 0.75 vs Tiafoe:
print("\n--- Direct Explicit Bracket Check (Anchored to Kalshi 88% QF / 74% Final & TAB 72.5% SF1) ---")
for p_zv_sh, p_zv_ti, p_zv_kh, p_kh_sh, p_kh_ti, lbl in [
    (0.58, 0.76, 0.81, 0.32, 0.48, "Balanced (Zv>Sh 58%, Zv>Kh 81%)"),
    (0.55, 0.74, 0.80, 0.33, 0.48, "Shelton hot (Zv>Sh 55%, Zv>Kh 80%)"),
    (0.60, 0.77, 0.81, 0.30, 0.47, "Zverev 5-0 H2H (Zv>Sh 60%, Zv>Kh 81%)"),
    (0.56, 0.75, 0.82, 0.31, 0.47, "Kalshi-aligned (Zv>Sh 56%, Zv>Kh 82%)"),
]:
    p_zv_bvdz = 0.88
    p_bvdz_kh = 0.34
    p_sh_ti = 0.725
    # Bottom finalist probs:
    f_zv = p_zv_bvdz * p_zv_kh
    f_kh = p_zv_bvdz * (1 - p_zv_kh) + (1 - p_zv_bvdz) * (1 - p_bvdz_kh)
    f_bv = (1 - p_zv_bvdz) * p_bvdz_kh
    # Top finalist probs:
    f_sh = p_sh_ti
    f_ti = 1 - p_sh_ti
    # Champion probs:
    p_bv_sh, p_bv_ti = 0.22, 0.36
    c_zv = f_zv * (f_sh * p_zv_sh + f_ti * p_zv_ti)
    c_kh = f_kh * (f_sh * p_kh_sh + f_ti * p_kh_ti)
    c_bv = f_bv * (f_sh * p_bv_sh + f_ti * p_bv_ti)
    c_sh = f_sh * (f_zv * (1 - p_zv_sh) + f_kh * (1 - p_kh_sh) + f_bv * (1 - p_bv_sh))
    c_ti = f_ti * (f_zv * (1 - p_zv_ti) + f_kh * (1 - p_kh_ti) + f_bv * (1 - p_bv_ti))
    print(f"  [{lbl:40s}] Zv={c_zv:.4f} Sh={c_sh:.4f} Ti={c_ti:.4f} Kh={c_kh:.4f} Bv={c_bv:.4f} (sum={c_zv+c_sh+c_ti+c_kh+c_bv:.4f})")

# ==============================================================================
# 3. Q608158: WOMEN'S SINGLES TITLE (ALL 4 SEMIFINALISTS LOCKED!)
# ==============================================================================
print("\n==================================================================")
print("3. Q608158: WOMEN'S SINGLES TITLE (FINAL 4: SAB-PEG & RYB-GAUFF)")
print("==================================================================")
# Source A: Sep 9 05:35 AM ET Covers DraftKings Predictions (AFTER Sab & Peg won, BEFORE Ryb & Gauff won!)
cov_wom_raw = {
    "Aryna Sabalenka": 0.41,
    "Coco Gauff": 0.24,
    "Elena Rybakina": 0.20,
    "Jessica Pegula": 0.13,
    "Mirra Andreeva": 0.09,
    "Zheng Qinwen": 0.06,
}
cov_pr = prop_devig(cov_wom_raw)
cov_pw, ck = power_devig(cov_wom_raw)
cov_sh, cz = shin_devig(cov_wom_raw)
print(f"Covers DK Predictions Sep 9 05:35 AM ET (raw sum={sum(cov_wom_raw.values()):.3f}, pow k={ck:.3f}, shin z={cz:.4f}):")
for p in cov_wom_raw:
    print(f"  {p:20s}: Raw={cov_wom_raw[p]:.3f} | Prop={cov_pr[p]:.4f} | Pow={cov_pw[p]:.4f} | Shin={cov_sh[p]:.4f}")

# Source B: Sep 8 11:16 AM ET ESPN DraftKings Sportsbook (8 QFists -> condition on all 4 QF winners!)
espn_wom_raw = {
    "Aryna Sabalenka": am_to_raw(230),
    "Coco Gauff": am_to_raw(320),
    "Elena Rybakina": am_to_raw(380),
    "Jessica Pegula": am_to_raw(600),
    "Mirra Andreeva": am_to_raw(850),
    "Linda Noskova": am_to_raw(1500),
    "Zheng Qinwen": am_to_raw(2200),
    "Emma Navarro": am_to_raw(3500),
}
espn_pw, ek = power_devig(espn_wom_raw)
espn_sh, ez = shin_devig(espn_wom_raw)

# Source C: TAB Sep 9 11:02 PM AEST SF1 (Sabalenka vs Pegula)
tab_sp_raw = {"Aryna Sabalenka": dec_to_raw(1.53), "Jessica Pegula": dec_to_raw(2.50)}
tab_sp_pr = prop_devig(tab_sp_raw)
tab_sp_pw, _ = power_devig(tab_sp_raw)
tab_sp_sh, _ = shin_devig(tab_sp_raw)
print(f"\nTAB Sabalenka vs Pegula ($1.53/$2.50): Prop={tab_sp_pr['Aryna Sabalenka']:.4f} | Pow={tab_sp_pw['Aryna Sabalenka']:.4f} | Shin={tab_sp_sh['Aryna Sabalenka']:.4f} | StatsInsider ML=0.6100")

wom_tree_pre_wed = (
    ("Aryna Sabalenka", "Jessica Pegula"),
    (("Coco Gauff", "Mirra Andreeva"), ("Elena Rybakina", "Zheng Qinwen"))
)
wom_tree_sep8 = (
    (("Aryna Sabalenka", "Linda Noskova"), ("Jessica Pegula", "Emma Navarro")),
    (("Coco Gauff", "Mirra Andreeva"), ("Elena Rybakina", "Zheng Qinwen"))
)
wom_tree_sf = (
    ("Aryna Sabalenka", "Jessica Pegula"),
    ("Coco Gauff", "Elena Rybakina")
)

wom_h2h = {
    ("Aryna Sabalenka", "Jessica Pegula"): 10,  # 9-4 overall, 2-0 USO, but Pegula won Berlin 2026
    ("Elena Rybakina", "Aryna Sabalenka"): 5,   # Rybakina won 2026 AO final vs Sabalenka
    ("Elena Rybakina", "Coco Gauff"): 5,        # 1-1 H2H, Rybakina won Toronto SF last month
}

for label, tree_in, targets in [
    ("Covers_Sep9_AM Power", wom_tree_pre_wed, cov_pw),
    ("Covers_Sep9_AM Shin",  wom_tree_pre_wed, cov_sh),
    ("Covers_Sep9_AM Prop",  wom_tree_pre_wed, cov_pr),
    ("ESPN_DK_Sep8   Power", wom_tree_sep8,    espn_pw),
    ("ESPN_DK_Sep8   Shin",  wom_tree_sep8,    espn_sh),
]:
    elos = fit_elos(tree_in, targets, h2h=wom_h2h)
    post = bracket_dp(wom_tree_sf, elos, h2h=wom_h2h)
    p_sp = win_prob("Aryna Sabalenka", "Jessica Pegula", elos, h2h=wom_h2h)
    p_gr = win_prob("Coco Gauff", "Elena Rybakina", elos, h2h=wom_h2h)
    p_sg = win_prob("Aryna Sabalenka", "Coco Gauff", elos, h2h=wom_h2h)
    p_sr = win_prob("Aryna Sabalenka", "Elena Rybakina", elos, h2h=wom_h2h)
    print(f"\n[{label}]")
    print(f"  Implied match probs: Sab>Peg={p_sp:.3f} | Gauff>Ryb={p_gr:.3f} | Sab>Gauff={p_sg:.3f} | Sab>Ryb={p_sr:.3f}")
    for p in ["Aryna Sabalenka", "Coco Gauff", "Elena Rybakina", "Jessica Pegula"]:
        print(f"    {p:20s}: {post[p]:.4f}")

# Explicit Direct 4-Player Semifinal Matrix Sensitivity (anchored to TAB Sabalenka ~62.5% vs Pegula!)
print("\n--- Direct 4-Player Final Four Matrix (Anchored to TAB Sab>Peg = 62.5% & StatsInsider 61%) ---")
# Matchups to explore:
#   SF1: p_sp = P(Sab > Peg) in {0.615, 0.625, 0.635}
#   SF2: p_rg = P(Ryb > Gauff) in {0.46, 0.50, 0.52, 0.55} (check: pre-QF Gauff > Ryb slightly in DK, but Gauff saved 2 MP & struggled with serve vs Andreeva, while Ryb beat Gauff in Toronto SF last month & just became World #1!)
#   Finals:
#     Sab vs Ryb: ~0.52 - 0.55 (Sab 2x defending USO champ, 49-3 hard Slams, but Ryb beat her at AO 2026 final!)
#     Sab vs Gauff: ~0.57 - 0.60 (Sab leads recent hard Slams, Gauff won USO 2023 final & 2026 Cincy)
#     Peg vs Ryb: ~0.41 - 0.44
#     Peg vs Gauff: ~0.43 - 0.46 (Gauff beat Pegula in 2026 Cincinnati final!)
for p_sp, p_rg, p_sr, p_sg, p_pr, p_pg, lbl in [
    (0.625, 0.50, 0.54, 0.58, 0.42, 0.44, "Tossup SF2 (Ryb=50/Gauff=50), Sab62.5"),
    (0.625, 0.52, 0.53, 0.58, 0.41, 0.44, "Slight Ryb SF2 (52/48), Sab62.5"),
    (0.625, 0.48, 0.54, 0.57, 0.43, 0.44, "Slight Gauff SF2 (52/48), Sab62.5"),
    (0.620, 0.51, 0.53, 0.57, 0.42, 0.44, "TAB-Prop/SI Sab62.0, Ryb51/Gauff49"),
    (0.635, 0.52, 0.55, 0.59, 0.41, 0.43, "Sab-strong 63.5, Ryb52/Gauff48"),
    (0.625, 0.46, 0.55, 0.57, 0.43, 0.44, "Market-Gauff-fav (Gauff54/Ryb46)"),
]:
    c_sab = p_sp * (p_rg * p_sr + (1 - p_rg) * p_sg)
    c_peg = (1 - p_sp) * (p_rg * p_pr + (1 - p_rg) * p_pg)
    c_ryb = p_rg * (p_sp * (1 - p_sr) + (1 - p_sp) * (1 - p_pr))
    c_gau = (1 - p_rg) * (p_sp * (1 - p_sg) + (1 - p_sp) * (1 - p_pg))
    print(f"  [{lbl:40s}] Sab={c_sab:.4f} Ryb={c_ryb:.4f} Gau={c_gau:.4f} Peg={c_peg:.4f} (sum={c_sab+c_ryb+c_gau+c_peg:.4f})")
