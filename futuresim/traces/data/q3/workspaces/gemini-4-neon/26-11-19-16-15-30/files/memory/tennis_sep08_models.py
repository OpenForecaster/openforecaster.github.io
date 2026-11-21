import math
import random
from collections import Counter

from tennis_aug28_models import (
    p_bo3, p_bo5,
    atp_bracket_raw, wta_bracket_raw,
)
from tennis_sep06_models import (
    wta_cal_elo, atp_mkt_elo, aug28_wta_exact,
    atp_bracket_04, us_men_04, us_men_28, extra_atp_elo,
    atp_r1_locked, atp_r2_locked, atp_r3_locked,
    wta_r1_locked, wta_r2_locked, wta_r3_locked,
    run_atp_blend, sim_wta,
    aug28_named, field_28, w_field_28,
)

# ==============================================================================
# DAY 10 (TUESDAY SEP 8, 2026 ~7:30 PM ET / 23:30 UTC) EXACT BRACKET & BAYES MODELS
# Batch: tennis (408930 Furthest US Man, 608158 WTA Title, 891014 ATP Title)
#
# COMPLETED SINCE SEP 7 SNAPSHOT:
#   ATP R4 (ALL 8/8 COMPLETE!):
#     - Alexander Zverev d. Luciano Darderi 6-2, 6-2, 7-6(3)
#     - Botic van de Zandschulp d. Arthur Gea in 5 sets (5h13m, from 0-2 sets, saved MP!)
#     - Karen Khachanov d. Learner Tien 7-5, 4-6, 6-7(6), 6-1, 6-4 (3h50m -> TIEN OUT!)
#   ATP QF #1 (COMPLETE Tue Sep 8 7:14 PM ET!):
#     - Frances Tiafoe d. Alex Michelsen 5-7, 3-6, 7-5, 6-3, 7-6(10-6) (4h38m -> TIAFOE IN SF! MICHELSEN OUT!)
#   WTA R4 (ALL 8/8 COMPLETE!):
#     - Coco Gauff d. Iva Jovic 6-1, 6-4 (1h20m, 20 straight sets! -> JOVIC OUT!)
#   WTA QF #1 (COMPLETE Tue Sep 8 ~2:00 PM ET!):
#     - Aryna Sabalenka d. Linda Noskova 7-6(1), 3-6, 7-6(10-7) (-> SABALENKA IN SF! NOSKOVA OUT!)
#
# REMAINING QFs & LIVE SEP 8 MARKET ODDS:
#   ATP:
#     - QF4 (Tue ~8:30pm ET): Carlos Alcaraz vs Ben Shelton (Kalshi 78/22; DK -421/+317)
#     - QF1 (Wed 7:30pm ET):  Alexander Zverev vs Botic van de Zandschulp (Betflag/WH/Bet365 1.10/6.40)
#     - QF2 (Wed 2:00pm ET):  Karen Khachanov vs Alexander Blockx (DK -166/+136; WH 8/13)
#   WTA:
#     - QF2 (Tue 7:00pm ET):  Jessica Pegula vs Emma Navarro (DK -437/+327; Kalshi 79/21; 4-0 H2H)
#     - QF3 (Wed 12:30pm ET): Coco Gauff vs Mirra Andreeva (DK -199/+161; 5-0 H2H)
#     - QF4 (Wed 11:30am ET): Elena Rybakina vs Qinwen Zheng (DK -293/+230; 4-1 H2H)
# ==============================================================================

def american_to_prob(odds):
    return (-odds) / (-odds + 100.0) if odds < 0 else 100.0 / (odds + 100.0)

def devig_mult(raw_dict):
    s = sum(raw_dict.values())
    return {k: v / s for k, v in raw_dict.items()}

def devig_power(raw_dict):
    # Solve sum(p_i^k) = 1 via binary search (standard sharp favorite-longshot correction)
    lo, hi = 1.0, 5.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if sum(v ** mid for v in raw_dict.values()) > 1.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    return {p: v ** k for p, v in raw_dict.items()}, k

def devig_two_way(p1, p2):
    m1 = p1 / (p1 + p2)
    pw, k = devig_power({"a": p1, "b": p2})
    return m1, pw["a"], k

print("=== LIVE SEP 8 QF MATCHLINE DEVIGS (Mult / Power) ===")
matches = [
    ("Alcaraz vs Shelton (DK -421/+317)", american_to_prob(-421), american_to_prob(317)),
    ("Zverev vs BVDZ (1.10/6.40)", 1.0/1.10, 1.0/6.40),
    ("Khachanov vs Blockx (DK -166/+136)", american_to_prob(-166), american_to_prob(136)),
    ("Pegula vs Navarro (DK -437/+327)", american_to_prob(-437), american_to_prob(327)),
    ("Gauff vs Andreeva (DK -199/+161)", american_to_prob(-199), american_to_prob(161)),
    ("Rybakina vs Zheng (DK -293/+230)", american_to_prob(-293), american_to_prob(230)),
    ("Sabalenka vs Noskova pre-match (DK -267/+212)", american_to_prob(-267), american_to_prob(212)),
    ("Tiafoe vs Michelsen pre-match (DK -156/+127)", american_to_prob(-156), american_to_prob(127)),
]
for label, p1, p2 in matches:
    m1, pw1, k = devig_two_way(p1, p2)
    print(f"  {label:46s}: Mult={m1:.4f} | Power={pw1:.4f} (vig={p1+p2-1:.4f})")

# ==============================================================================
# PART 1: DRAFTKINGS SEP 8 11:16 AM ET FUTURES & FINALS TABLE (PRE-TUE QFs!)
# ==============================================================================
dk_atp_win_am = {
    "Carlos Alcaraz": american_to_prob(-165),
    "Alexander Zverev": american_to_prob(240),
    "Ben Shelton": american_to_prob(850),
    "Frances Tiafoe": american_to_prob(2200),
    "Karen Khachanov": american_to_prob(3500),
    "Alexander Blockx": american_to_prob(4500),
    "Alex Michelsen": american_to_prob(4500),
    "Botic van de Zandschulp": american_to_prob(12000),
}
dk_atp_fin_top = {
    "Alexander Zverev": american_to_prob(-350),
    "Karen Khachanov": american_to_prob(500),
    "Alexander Blockx": american_to_prob(650),
    "Botic van de Zandschulp": american_to_prob(1300),
}
dk_atp_fin_bot = {
    "Carlos Alcaraz": american_to_prob(-390),
    "Ben Shelton": american_to_prob(350),
    "Frances Tiafoe": american_to_prob(950),
    "Alex Michelsen": american_to_prob(1500),
}

dk_wta_win_am = {
    "Aryna Sabalenka": american_to_prob(230),
    "Coco Gauff": american_to_prob(320),
    "Elena Rybakina": american_to_prob(380),
    "Jessica Pegula": american_to_prob(600),
    "Mirra Andreeva": american_to_prob(850),
    "Linda Noskova": american_to_prob(1500),
    "Qinwen Zheng": american_to_prob(2200),
    "Emma Navarro": american_to_prob(3500),
}
dk_wta_fin_top = {
    "Aryna Sabalenka": american_to_prob(-140),
    "Jessica Pegula": american_to_prob(180),
    "Linda Noskova": american_to_prob(475),
    "Emma Navarro": american_to_prob(1100),
}
dk_wta_fin_bot = {
    "Coco Gauff": american_to_prob(130),
    "Elena Rybakina": american_to_prob(160),
    "Mirra Andreeva": american_to_prob(310),
    "Qinwen Zheng": american_to_prob(650),
}

dk_atp_mult = devig_mult(dk_atp_win_am)
dk_atp_pow, k_am = devig_power(dk_atp_win_am)
dk_atp_ft_pow, _ = devig_power(dk_atp_fin_top)
dk_atp_fb_pow, _ = devig_power(dk_atp_fin_bot)

dk_wta_mult = devig_mult(dk_wta_win_am)
dk_wta_pow, k_wm = devig_power(dk_wta_win_am)
dk_wta_ft_pow, _ = devig_power(dk_wta_fin_top)
dk_wta_fb_pow, _ = devig_power(dk_wta_fin_bot)

print(f"\n=== DK SEP 8 11:16 AM ET ATP WIN & FINALS (k={k_am:.3f}, vig={sum(dk_atp_win_am.values())-1:.3f}) ===")
for p in dk_atp_win_am:
    fp = dk_atp_ft_pow.get(p, dk_atp_fb_pow.get(p, 0.0))
    print(f"  {p:24s}: Raw={dk_atp_win_am[p]:.4f} | Mult={dk_atp_mult[p]:.4f} | Pow={dk_atp_pow[p]:.4f} | FinPow={fp:.4f}")

print(f"\n=== DK SEP 8 11:16 AM ET WTA WIN & FINALS (k={k_wm:.3f}, vig={sum(dk_wta_win_am.values())-1:.3f}) ===")
for p in dk_wta_win_am:
    fp = dk_wta_ft_pow.get(p, dk_wta_fb_pow.get(p, 0.0))
    print(f"  {p:24s}: Raw={dk_wta_win_am[p]:.4f} | Mult={dk_wta_mult[p]:.4f} | Pow={dk_wta_pow[p]:.4f} | FinPow={fp:.4f}")

# ==============================================================================
# PART 2: EXACT ANALYTICAL 8-PLAYER BRACKET SOLVER (WITH SKILL UNCERTAINTY MIX!)
# ==============================================================================
def solve_8_exact(bracket8, elo_map, p_fn, locked_qfs=None, h2h_override=None):
    """
    Exact analytical probability for an 8-player bracket:
      Q1=(0,1), Q2=(2,3), Q3=(4,5), Q4=(6,7)
      SF1=(Q1,Q2), SF2=(Q3,Q4), F=(SF1,SF2)
    Returns dicts: sf_p, fin_p, win_p
    """
    locked_qfs = locked_qfs or {}
    h2h_override = h2h_override or {}
    def gp(a, b):
        if (a, b) in h2h_override: return h2h_override[(a, b)]
        if (b, a) in h2h_override: return 1.0 - h2h_override[(b, a)]
        return p_fn(elo_map[a], elo_map[b])

    # QF distributions
    q = []
    for idx in range(4):
        a, b = bracket8[2*idx], bracket8[2*idx+1]
        if idx in locked_qfs:
            w = locked_qfs[idx]
            q.append({w: 1.0})
        else:
            pa = gp(a, b)
            q.append({a: pa, b: 1.0 - pa})

    sf_p = {}
    for d in q:
        sf_p.update(d)

    # SF1 (q[0] vs q[1]) and SF2 (q[2] vs q[3])
    def combine(d1, d2):
        out = Counter()
        for a, pa in d1.items():
            for b, pb in d2.items():
                wab = gp(a, b)
                out[a] += pa * pb * wab
                out[b] += pa * pb * (1.0 - wab)
        return dict(out)

    f1 = combine(q[0], q[1])
    f2 = combine(q[2], q[3])
    fin_p = {**f1, **f2}
    win_p = combine(f1, f2)
    return sf_p, fin_p, win_p

def solve_8_mix(bracket8, base_elo, mix_list, p_fn, locked_qfs=None, h2h_override=None):
    """
    mix_list: list of (weight, elo_overrides_dict) representing latent player form/skill states!
    Crucially, if a QF is locked (or inside an outcome), we can compute EXACT Bayes posterior over latent states!
    Here we compute unconditional expectation over mix_list (assuming mix_list is ALREADY posterior given completed matches).
    """
    sf_tot, fin_tot, win_tot = Counter(), Counter(), Counter()
    for w, ov in mix_list:
        em = dict(base_elo)
        em.update(ov)
        sf, fin, win = solve_8_exact(bracket8, em, p_fn, locked_qfs, h2h_override)
        for k, v in sf.items(): sf_tot[k] += w * v
        for k, v in fin.items(): fin_tot[k] += w * v
        for k, v in win.items(): win_tot[k] += w * v
    return dict(sf_tot), dict(fin_tot), dict(win_tot)

# ==============================================================================
# PART 3: ATP MODELS (DAY 10 EVENING — TIAFOE IN SF! MICHELSEN & TIEN OUT!)
# ==============================================================================
atp_qfs = [
    "Alexander Zverev", "Botic van de Zandschulp",
    "Karen Khachanov", "Alexander Blockx",
    "Frances Tiafoe", "Alex Michelsen",
    "Carlos Alcaraz", "Ben Shelton",
]

# --- ATP Model B_MKT (Calibrated to ALL Sep 8 live QF lines AND DK Sep 8 Finals odds!) ---
# Check pairwise BO5 probs:
#   Alcaraz (2272) vs Shelton (2090) -> p_bo5 = 0.781 (Kalshi 78%, DK Pow 78.3%!)
#   Alcaraz (2272) vs Zverev  (2148) -> p_bo5 = 0.703 (matches DK -165 vs +240!)
#   Alcaraz (2272) vs Tiafoe  (2015) -> p_bo5 = 0.861
#   Shelton (2090) vs Tiafoe  (2015) -> p_bo5 = 0.640
#   Zverev  (2148) vs BVDZ    (1898) -> p_bo5 = 0.875 (Betflag/WH 1.10/6.40: Mult 85.3%, Power 88.2%!)
#   Zverev  (2148) vs Khach   (1982) -> p_bo5 = 0.771 (matches DK Zverev Finals -350 ~72%!)
#   Khach   (1982) vs Blockx  (1932) -> p_bo5 = 0.594 (DK -166/+136 = 59.6%!)
#   Tiafoe  (2015) vs Michelsen (1972) -> p_bo5 = 0.581 (pre-match consensus 58.2%!)
atp_elo_mkt = {
    "Carlos Alcaraz": 2272.0,
    "Alexander Zverev": 2148.0,
    "Ben Shelton": 2090.0,
    "Frances Tiafoe": 2015.0,
    "Karen Khachanov": 1982.0,
    "Alex Michelsen": 1972.0,
    "Alexander Blockx": 1932.0,
    "Botic van de Zandschulp": 1898.0,
}

# --- ATP Model B_ELO (Slightly more conservative on Alcaraz vs Zverev: Alcaraz 2245, Zverev 2158 -> 65.5%) ---
# Mirrors our pre-tournament Elo / Zverev RG-champ respect while STILL matching all 3 live QF lines!
atp_elo_cons = {
    "Carlos Alcaraz": 2245.0,
    "Alexander Zverev": 2158.0,
    "Ben Shelton": 2065.0,    # 2245 vs 2065 = 0.779 vs Alcaraz!
    "Frances Tiafoe": 2005.0,
    "Karen Khachanov": 1975.0,
    "Alex Michelsen": 1962.0,
    "Alexander Blockx": 1925.0,
    "Botic van de Zandschulp": 1905.0, # 2158 vs 1905 = 0.878 vs Zverev!
}

# Also test Tiafoe slight post-5-set-scare fatigue/form update (-15 Elo in evening state!)
atp_elo_mkt_fat = {**atp_elo_mkt, "Frances Tiafoe": 2000.0}
atp_elo_cons_fat = {**atp_elo_cons, "Frances Tiafoe": 1990.0}

print("\n=== ATP PAIRWISE CHECK (Model B_MKT) ===")
for a, b, note in [
    ("Carlos Alcaraz", "Ben Shelton", "Kalshi 78%, DK Pow 78.3%"),
    ("Alexander Zverev", "Botic van de Zandschulp", "1.10/6.40: Mult 85.3%, Pow 88.2%"),
    ("Karen Khachanov", "Alexander Blockx", "DK -166/+136 = 59.6%"),
    ("Frances Tiafoe", "Alex Michelsen", "Pre-match 58.2%"),
    ("Carlos Alcaraz", "Alexander Zverev", "Final H2H"),
    ("Carlos Alcaraz", "Frances Tiafoe", "SF2 if Alcaraz wins"),
    ("Ben Shelton", "Frances Tiafoe", "SF2 if Shelton wins"),
    ("Alexander Zverev", "Karen Khachanov", "SF1"),
    ("Alexander Zverev", "Alexander Blockx", "SF1"),
]:
    print(f"  {a:20s} vs {b:24s}: MKT={p_bo5(atp_elo_mkt[a], atp_elo_mkt[b]):.4f} | CONS={p_bo5(atp_elo_cons[a], atp_elo_cons[b]):.4f} ({note})")

# Compute Morning (pre-Tiafoe win) & Evening (Tiafoe locked QF3=idx 2) exact solutions
_, atp_fin_am_mkt, atp_win_am_mkt = solve_8_exact(atp_qfs, atp_elo_mkt, p_bo5, locked_qfs={})
atp_sf_pm_mkt, atp_fin_pm_mkt, atp_win_pm_mkt = solve_8_exact(atp_qfs, atp_elo_mkt, p_bo5, locked_qfs={2: "Frances Tiafoe"})
_, atp_fin_pm_mkt_f, atp_win_pm_mkt_f = solve_8_exact(atp_qfs, atp_elo_mkt_fat, p_bo5, locked_qfs={2: "Frances Tiafoe"})

_, atp_fin_am_cons, atp_win_am_cons = solve_8_exact(atp_qfs, atp_elo_cons, p_bo5, locked_qfs={})
_, atp_fin_pm_cons, atp_win_pm_cons = solve_8_exact(atp_qfs, atp_elo_cons, p_bo5, locked_qfs={2: "Frances Tiafoe"})
_, _, atp_win_pm_cons_f = solve_8_exact(atp_qfs, atp_elo_cons_fat, p_bo5, locked_qfs={2: "Frances Tiafoe"})

# Compare Model B_MKT morning vs DraftKings Sep 8 11:16 AM ET (both Win and Finals!)
print("\n=== ATP CALIBRATION CHECK: MODEL B_MKT (11:16 AM) vs DRAFTKINGS SEP 8 11:16 AM ===")
print(f"{'Player':24s} | {'DK_Mult':7s} | {'DK_Pow':7s} | {'MKT_AM':7s} | {'DK_FinP':7s} | {'MKT_Fin':7s}")
for p in atp_qfs:
    fp = dk_atp_ft_pow.get(p, dk_atp_fb_pow.get(p, 0.0))
    print(f"{p:24s} | {dk_atp_mult[p]:7.4f} | {dk_atp_pow[p]:7.4f} | {atp_win_am_mkt[p]:7.4f} | {fp:7.4f} | {atp_fin_am_mkt[p]:7.4f}")

# Exact Bayesian Update of DK Sep 8 11:16 AM (both Mult and Pow) conditioned on Tiafoe beating Michelsen!
def bayes_lr_update(prior_dict, mc_am, mc_pm):
    raw = {}
    for p, pr in prior_dict.items():
        if mc_pm.get(p, 0.0) == 0.0:
            raw[p] = 0.0
        else:
            raw[p] = pr * (mc_pm[p] / max(1e-9, mc_am[p]))
    tot = sum(raw.values())
    return {p: v / tot for p, v in raw.items()}

dk_atp_post_pow = bayes_lr_update(dk_atp_pow, atp_win_am_mkt, atp_win_pm_mkt_f)
dk_atp_post_mult = bayes_lr_update(dk_atp_mult, atp_win_am_mkt, atp_win_pm_mkt_f)

# Also run Full 128-player Strict Outcome-Only Bayes (Model A from Aug 28 -> Sep 8 evening!)
# Build all 8 locked R4 winners:
atp_r4_winners_08 = {
    "Alexander Zverev", "Botic van de Zandschulp", "Karen Khachanov", "Alexander Blockx",
    "Frances Tiafoe", "Alex Michelsen", "Carlos Alcaraz", "Ben Shelton",
}
atp_r4_locked_08 = {}
for i in range(0, 128, 16):
    r3a = atp_r3_locked[(
        atp_r2_locked[(atp_r1_locked[(atp_bracket_04[i], atp_bracket_04[i+1])],
                       atp_r1_locked[(atp_bracket_04[i+2], atp_bracket_04[i+3])])],
        atp_r2_locked[(atp_r1_locked[(atp_bracket_04[i+4], atp_bracket_04[i+5])],
                       atp_r1_locked[(atp_bracket_04[i+6], atp_bracket_04[i+7])])]
    )]
    r3b = atp_r3_locked[(
        atp_r2_locked[(atp_r1_locked[(atp_bracket_04[i+8], atp_bracket_04[i+9])],
                       atp_r1_locked[(atp_bracket_04[i+10], atp_bracket_04[i+11])])],
        atp_r2_locked[(atp_r1_locked[(atp_bracket_04[i+12], atp_bracket_04[i+13])],
                       atp_r1_locked[(atp_bracket_04[i+14], atp_bracket_04[i+15])])]
    )]
    if r3a in atp_r4_winners_08: atp_r4_locked_08[(r3a, r3b)] = r3a
    elif r3b in atp_r4_winners_08: atp_r4_locked_08[(r3a, r3b)] = r3b
assert len(atp_r4_locked_08) == 8

# Aug 28 baseline & strict outcome-only Bayes update for Sep 8 (using exact 8-player solve on base atp_mkt_elo!)
m28_tc, _, _, _, _, _, _, _, _ = run_atp_blend(
    atp_bracket_raw, us_men_28, None, None, None, None, None, None, None, None, 9100
)
# Exact Alcaraz posterior after R1-R4 (same as Sep 7)
alc_prior = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
w_r1r4 = [w * p_bo5(e, 1895.0) * p_bo5(e, 1840.0) * p_bo5(e, 1845.0) * p_bo5(e, 1984.0) for e, w in alc_prior]
alc_mix_A = [(ww / sum(w_r1r4), {"Carlos Alcaraz": e}) for (e, _), ww in zip(alc_prior, w_r1r4)]

base_atp_elo_A = {p: atp_mkt_elo.get(p, extra_atp_elo.get(p, 1840.0)) for p in atp_qfs}
_, _, m08A_win = solve_8_mix(atp_qfs, base_atp_elo_A, alc_mix_A, p_bo5, locked_qfs={2: "Frances Tiafoe"})

# Update Aug 28 market prior with m08A_win
rawA = {}
for k, p28 in aug28_named.items():
    rawA[k] = 0.0 if m08A_win.get(k, 0.0) == 0.0 else p28 * (m08A_win[k] / max(1e-6, m28_tc.get(k, 1e-6)))
mc28_f = 1.0 - sum(m28_tc.get(k, 0.0) for k in aug28_named)
mcnew_f = 1.0 - sum(m08A_win.get(k, 0.0) for k in aug28_named)
raw_f = field_28 * (mcnew_f / max(1e-6, mc28_f))
totA = sum(rawA.values()) + raw_f
updA_atp = {k: v / totA for k, v in rawA.items()}
for k, v in m08A_win.items():
    if k not in aug28_named and v > 0:
        updA_atp[k] = (raw_f / totA) * (v / max(1e-9, mcnew_f))

# Blend for Q3 (ATP Title):
#   15% Strict Aug28 Outcome-Only (updA_atp)
#   30% Live Sep 8 Market-Calibrated Elo (atp_win_pm_mkt_f)
#   20% Live Sep 8 Conservative-Final Elo (atp_win_pm_cons_f)
#   20% DK Sep 8 Power-Devig Bayes Post (dk_atp_post_pow)
#   15% DK Sep 8 Mult-Devig Bayes Post (dk_atp_post_mult)
blend_atp = {}
for p in atp_qfs:
    blend_atp[p] = (
        0.15 * updA_atp.get(p, 0.0)
        + 0.30 * atp_win_pm_mkt_f.get(p, 0.0)
        + 0.20 * atp_win_pm_cons_f.get(p, 0.0)
        + 0.20 * dk_atp_post_pow.get(p, 0.0)
        + 0.15 * dk_atp_post_mult.get(p, 0.0)
    )

print("\n" + "=" * 124)
print("Q3 (891014) ATP DAY 10 EVENING (TUE SEP 8 ~7:30 PM ET) — TIAFOE IN SF! MICHELSEN & TIEN OUT!")
print("=" * 124)
print(f"{'Player':24s} | {'UpdA':6s} | {'MKT_PM':6s} | {'CONS_P':6s} | {'DK_Pow':6s} | {'DK_Mlt':6s} | {'BLEND':6s} | {'SF_P':5s} | {'FIN_P':5s}")
for p, _ in sorted(blend_atp.items(), key=lambda x: -x[1]):
    print(f"{p:24s} | {updA_atp.get(p,0):6.4f} | {atp_win_pm_mkt_f.get(p,0):6.4f} | {atp_win_pm_cons_f.get(p,0):6.4f} | {dk_atp_post_pow.get(p,0):6.4f} | {dk_atp_post_mult.get(p,0):6.4f} | {blend_atp[p]:6.4f} | {atp_sf_pm_mkt.get(p,0):5.3f} | {atp_fin_pm_mkt_f.get(p,0):5.3f}")

# ==============================================================================
# PART 4: Q1 (408930) FURTHEST U.S. MAN — EXACT 2-PLAYER ANALYSIS!
# ==============================================================================
# Remaining US men: ONLY Frances Tiafoe (ALREADY IN SF!) and Ben Shelton (QF vs Alcaraz tonight!)
# Zero possibility of tie! If Alcaraz beats Shelton, Tiafoe wins Q1 100%.
# If Shelton beats Alcaraz, Shelton plays Tiafoe in SF2 — winner advances to Final & strictly wins Q1!
# Wait: Account for latent skill correlation! If Shelton beats Alcaraz (22% upset), Shelton's
# latent Elo posterior shifts UP by ~+20-30 Elo (e.g. mixture prior on Shelton: [2040 (0.25), 2090 (0.50), 2145 (0.25)])!
print("\n" + "=" * 100)
print("Q1 (408930) FURTHEST U.S. MAN — EXACT 2-OUTCOME ANALYSIS (TIAFOE IN SF, SHELTON IN QF)")
print("=" * 100)
# Sensitivity grid:
#   p_shelton_qf: 0.220 (Kalshi 22%, DK Pow 21.7%, DK Mult 22.9% -> consensus 22.2%)
#   p_shelton_sf_given_upset:
#     Case 1 (No skill correlation, Tiafoe fresh 2015 vs Shelton 2090): p_bo5(2090, 2015) = 0.640
#     Case 2 (Tiafoe -15 post-5-setter 2000 vs Shelton 2090):          p_bo5(2090, 2000) = 0.667
#     Case 3 (Exact Bayesian latent-skill update for Shelton upsetting Alcaraz!):
sh_states = [(2035.0, 0.25), (2090.0, 0.50), (2150.0, 0.25)]
# Check marginal P(Shelton > Alcaraz 2272):
p_sh_qf_states = [p_bo5(e, 2272.0) for e, _ in sh_states]
p_sh_qf_marg = sum(w * p for (_, w), p in zip(sh_states, p_sh_qf_states))
post_sh_w = [w * p / p_sh_qf_marg for (_, w), p in zip(sh_states, p_sh_qf_states)]
e_sh_post = sum(e * pw for (e, _), pw in zip(sh_states, post_sh_w))
p_sh_vs_tia_fresh = sum(pw * p_bo5(e, 2015.0) for (e, _), pw in zip(sh_states, post_sh_w))
p_sh_vs_tia_fat = sum(pw * p_bo5(e, 2000.0) for (e, _), pw in zip(sh_states, post_sh_w))
print(f"  Latent-skill Shelton prior mean=2091 -> P(Sh > Alc) = {p_sh_qf_marg:.4f}")
print(f"  Conditional on upsetting Alcaraz: Shelton post mean={e_sh_post:.1f}")
print(f"    P(Shelton > Tiafoe fresh 2015 | upset) = {p_sh_vs_tia_fresh:.4f} -> P(Shelton Q1) = {p_sh_qf_marg*p_sh_vs_tia_fresh:.4f}, P(Tiafoe Q1) = {1 - p_sh_qf_marg*p_sh_vs_tia_fresh:.4f}")
print(f"    P(Shelton > Tiafoe fat   2000 | upset) = {p_sh_vs_tia_fat:.4f} -> P(Shelton Q1) = {p_sh_qf_marg*p_sh_vs_tia_fat:.4f}, P(Tiafoe Q1) = {1 - p_sh_qf_marg*p_sh_vs_tia_fat:.4f}")
# Also check DK Finals ratio directly!
# DK Sep 8 11:16 AM Finals Pow: Shelton = 0.168, Alcaraz = 0.728, Tiafoe = 0.065, Michelsen = 0.039
# Note: Under DK, P(Shelton wins SF2) = P(Shelton reaches Final) = 0.168 (if Shelton vs Tiafoe/Michelsen)!
# Wait: Shelton reaching Final ALREADY equals P(Shelton beats Alcaraz AND Shelton beats Tiafoe/Michelsen)!
# Specifically, if Shelton beats Tiafoe slightly LESS often than Michelsen (~67% vs ~75%), then:
#   Before Tiafoe won: P(Shelton Final) = 0.22 * (0.58 * 0.67 + 0.42 * 0.75) = 0.22 * 0.704 = 0.155
#   NOW Tiafoe won:    P(Shelton Final) = P(Shelton wins Q1) = 0.222 * 0.68 = 0.151!
for p_qf in [0.215, 0.220, 0.225, 0.230]:
    for p_sf in [0.64, 0.67, 0.70]:
        ps = p_qf * p_sf
        print(f"  Grid P(QF)={p_qf:.3f}, P(SF|QF)={p_sf:.2f} -> Tiafoe={1-ps:.4f}, Shelton={ps:.4f}")

# ==============================================================================
# PART 5: WTA MODELS (DAY 10 EVENING — SABALENKA IN SF! NOSKOVA & JOVIC OUT!)
# ==============================================================================
wta_qfs = [
    "Aryna Sabalenka", "Linda Noskova",
    "Jessica Pegula", "Emma Navarro",
    "Coco Gauff", "Mirra Andreeva",
    "Elena Rybakina", "Qinwen Zheng",
]

# --- WTA Model B_MKT (Calibrated to ALL Sep 8 live QF lines AND DK Sep 8 11:16 AM Win + Finals odds!) ---
# Check exact pairwise BO3 probs vs Sep 8 DraftKings/Kalshi lines:
#   Sabalenka (2197) vs Noskova (2047) -> 0.703 (DK -267/+212 = 70.6%, Kalshi 70%!)
#   Pegula    (2082) vs Navarro (1955) -> H2H override 0.783 (DK -437/+327 Mult 77.7%/Pow 78.9%, Kalshi 79%!)
#   Gauff     (2175) vs Andreeva(2074) -> 0.638 (DK -199/+161 Mult 63.5%/Pow 63.8%! 5-0 H2H!)
#   Rybakina  (2148) vs Zheng   (1987) -> 0.715 (DK -293/+230 Mult 71.1%/Pow 71.8%! 4-1 H2H!)
#   Sabalenka (2197) vs Pegula  (2082) -> 0.656  (Wait: check DK Finals! Earlier we saw Sabalenka needed ~71-74% vs Pegula/Navarro to match DK Finals -140 vs +180!)
#   Let's check BOTH:
#     (1) wta_elo_mkt: Pegula 2075 (Sab vs Peg = 66.5% pure Elo, OR with Sab-Peg H2H 8-2 / USO 2-0 -> 70%!), Gauff 2175, Rybakina 2148
#     (2) wta_elo_ryb: Rybakina slightly stronger (2160 vs Gauff 2162 -> 50/50 SF) for robustness!
wta_elo_mkt = {
    "Aryna Sabalenka": 2198.0,
    "Linda Noskova":   2048.0,   # Sab vs Nosk = 0.703
    "Jessica Pegula":  2075.0,   # Sab vs Peg  = 0.667 (or 0.70 with H2H)
    "Emma Navarro":    1955.0,   # Sab vs Nav  = 0.802
    "Coco Gauff":      2175.0,   # Cin champ, 20 straight sets! Gauff vs Ryb = 0.538
    "Mirra Andreeva":  2074.0,   # Gauff vs And = 0.638 (DK 63.5-63.8%)
    "Elena Rybakina":  2148.0,   # Ryb vs Zheng = 0.715 (DK 71.1-71.8%)
    "Qinwen Zheng":    1987.0,
}
wta_h2h_mkt = {
    ("Jessica Pegula", "Emma Navarro"): 0.783,    # DK -437/+327 & Kalshi 79% (4-0 H2H)
    ("Aryna Sabalenka", "Jessica Pegula"): 0.700, # 2024 USO F & 2025 USO SF winner; matches DK Finals -140/+180!
}

# Sabalenka slight post-Noskova close-call update (-12 Elo after needing 7-6(7) 3rd set vs Noskova, Sab-Peg -> 0.685)
wta_elo_mkt_adj = {**wta_elo_mkt, "Aryna Sabalenka": 2186.0}
wta_h2h_mkt_adj = {
    ("Jessica Pegula", "Emma Navarro"): 0.783,
    ("Aryna Sabalenka", "Jessica Pegula"): 0.685,
}

# Alternative Elo model: Rybakina = Gauff (no Gauff edge over Rybakina; pure Elo Sab-Peg 66.7%)
wta_elo_bal = {
    "Aryna Sabalenka": 2192.0,
    "Linda Noskova":   2042.0,
    "Jessica Pegula":  2078.0,
    "Emma Navarro":    1955.0,
    "Coco Gauff":      2160.0,
    "Mirra Andreeva":  2060.0,   # Gauff vs And = 0.637
    "Elena Rybakina":  2158.0,   # Ryb vs Gauff = 0.497
    "Qinwen Zheng":    1998.0,   # Ryb vs Zheng = 0.714
}
wta_h2h_bal = {
    ("Jessica Pegula", "Emma Navarro"): 0.783,
}

print("\n=== WTA PAIRWISE CHECK (Model B_MKT vs BAL) ===")
for a, b, note in [
    ("Aryna Sabalenka", "Linda Noskova", "Pre-match 70.3%"),
    ("Jessica Pegula", "Emma Navarro", "DK -437/+327 = 77.7-78.9%"),
    ("Coco Gauff", "Mirra Andreeva", "DK -199/+161 = 63.5-63.8%"),
    ("Elena Rybakina", "Qinwen Zheng", "DK -293/+230 = 71.1-71.8%"),
    ("Aryna Sabalenka", "Jessica Pegula", "Potential SF1"),
    ("Coco Gauff", "Elena Rybakina", "Potential SF2"),
    ("Aryna Sabalenka", "Coco Gauff", "Potential Final"),
    ("Aryna Sabalenka", "Elena Rybakina", "Potential Final"),
]:
    pm = wta_h2h_mkt.get((a, b), p_bo3(wta_elo_mkt[a], wta_elo_mkt[b]))
    pb = wta_h2h_bal.get((a, b), p_bo3(wta_elo_bal[a], wta_elo_bal[b]))
    print(f"  {a:18s} vs {b:18s}: MKT={pm:.4f} | BAL={pb:.4f} ({note})")

_, wta_fin_am_mkt, wta_win_am_mkt = solve_8_exact(wta_qfs, wta_elo_mkt, p_bo3, locked_qfs={}, h2h_override=wta_h2h_mkt)
wta_sf_pm_mkt, wta_fin_pm_mkt, wta_win_pm_mkt = solve_8_exact(wta_qfs, wta_elo_mkt, p_bo3, locked_qfs={0: "Aryna Sabalenka"}, h2h_override=wta_h2h_mkt)
_, wta_fin_pm_adj, wta_win_pm_adj = solve_8_exact(wta_qfs, wta_elo_mkt_adj, p_bo3, locked_qfs={0: "Aryna Sabalenka"}, h2h_override=wta_h2h_mkt_adj)
_, _, wta_win_pm_bal = solve_8_exact(wta_qfs, wta_elo_bal, p_bo3, locked_qfs={0: "Aryna Sabalenka"}, h2h_override=wta_h2h_bal)

print("\n=== WTA CALIBRATION CHECK: MODEL B_MKT (11:16 AM) vs DRAFTKINGS SEP 8 11:16 AM ===")
print(f"{'Player':18s} | {'DK_Mult':7s} | {'DK_Pow':7s} | {'MKT_AM':7s} | {'DK_FinP':7s} | {'MKT_Fin':7s}")
for p in wta_qfs:
    fp = dk_wta_ft_pow.get(p, dk_wta_fb_pow.get(p, 0.0))
    print(f"{p:18s} | {dk_wta_mult[p]:7.4f} | {dk_wta_pow[p]:7.4f} | {wta_win_am_mkt[p]:7.4f} | {fp:7.4f} | {wta_fin_am_mkt[p]:7.4f}")

# Exact Bayesian Update of DK Sep 8 11:16 AM conditioned on Sabalenka beating Noskova!
dk_wta_post_pow = bayes_lr_update(dk_wta_pow, wta_win_am_mkt, wta_win_pm_mkt)
dk_wta_post_pow_adj = bayes_lr_update(dk_wta_pow, wta_win_am_mkt, wta_win_pm_adj)
dk_wta_post_mult_adj = bayes_lr_update(dk_wta_mult, wta_win_am_mkt, wta_win_pm_adj)

# Strict Outcome-Only Aug 28 -> Sep 8 Evening (Model A)
w28_t, _, _, _ = sim_wta(None, None, None, None, None, None, None, False, 100000, 9501)
ryb_prior_30 = [(2130.0, 0.52), (2065.0, 0.28), (1970.0, 0.14), (1740.0, 0.06)]
wr_a = [w * p_bo3(e, 1715.0) * p_bo3(e, 1845.0) * p_bo3(e, 1795.0) * p_bo3(e, 2062.0) for e, w in ryb_prior_30]
ryb_mix_A = [(e, ww / sum(wr_a)) for (e, _), ww in zip(ryb_prior_30, wr_a)]
# Sabalenka includes R5 win over Noskova (wta_cal_elo["Linda Noskova"])!
sab_prior_28 = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]
nosk_e = wta_cal_elo["Linda Noskova"]
ws_a = [w * p_bo3(e, 1845.0) * p_bo3(e, 1795.0) * p_bo3(e, 1795.0) * p_bo3(e, 1855.0) * p_bo3(e, nosk_e) for e, w in sab_prior_28]
sab_mix_A = [(e, ww / sum(ws_a)) for (e, _), ww in zip(sab_prior_28, ws_a)]

wta_mix_A = []
for re_e, wr in ryb_mix_A:
    for se_e, ws in sab_mix_A:
        wta_mix_A.append((wr * ws, {"Elena Rybakina": re_e, "Aryna Sabalenka": se_e}))
base_wta_elo_A = {p: wta_cal_elo[p] for p in wta_qfs}
_, _, w08A_win = solve_8_mix(wta_qfs, base_wta_elo_A, wta_mix_A, p_bo3, locked_qfs={0: "Aryna Sabalenka"})

rawW = {k: p28 * (w08A_win.get(k, 0.0) / max(1e-6, w28_t.get(k, 1e-6))) for k, p28 in aug28_wta_exact.items()}
mc28_wf = 1.0 - sum(w28_t.get(k, 0.0) for k in aug28_wta_exact)
mcnew_wf = 1.0 - sum(w08A_win.get(k, 0.0) for k in aug28_wta_exact)
raw_wf = w_field_28 * (mcnew_wf / max(1e-6, mc28_wf))
totW = sum(rawW.values()) + raw_wf
updA_wta = {k: v / totW for k, v in rawW.items()}
for k, v in w08A_win.items():
    if k not in aug28_wta_exact and v > 0:
        updA_wta[k] = (raw_wf / totW) * (v / max(1e-9, mcnew_wf))

# Blend for Q2 (WTA Title):
#   15% Strict Aug28 Outcome-Only (updA_wta)
#   25% Live Sep 8 Market-Calibrated Elo Post-Noskova-Adj (wta_win_pm_adj)
#   20% Live Sep 8 Balanced Elo (wta_win_pm_bal)
#   25% DK Sep 8 Power-Devig Bayes Post (dk_wta_post_pow_adj)
#   15% DK Sep 8 Mult-Devig Bayes Post (dk_wta_post_mult_adj)
blend_wta = {}
for p in wta_qfs:
    blend_wta[p] = (
        0.15 * updA_wta.get(p, 0.0)
        + 0.25 * wta_win_pm_adj.get(p, 0.0)
        + 0.20 * wta_win_pm_bal.get(p, 0.0)
        + 0.25 * dk_wta_post_pow_adj.get(p, 0.0)
        + 0.15 * dk_wta_post_mult_adj.get(p, 0.0)
    )

print("\n" + "=" * 130)
print("Q2 (608158) WTA DAY 10 EVENING (TUE SEP 8 ~7:30 PM ET) — SABALENKA IN SF! NOSKOVA & JOVIC OUT!")
print("=" * 130)
print(f"{'Player':18s} | {'UpdA':6s} | {'MKT_PM':6s} | {'MKT_Aj':6s} | {'BAL_PM':6s} | {'DK_Pow':6s} | {'DK_Aj':6s} | {'DK_Mlt':6s} | {'BLEND':6s} | {'SF_P':5s} | {'FIN_P':5s}")
for p, _ in sorted(blend_wta.items(), key=lambda x: -x[1]):
    print(f"{p:18s} | {updA_wta.get(p,0):6.4f} | {wta_win_pm_mkt.get(p,0):6.4f} | {wta_win_pm_adj.get(p,0):6.4f} | {wta_win_pm_bal.get(p,0):6.4f} | {dk_wta_post_pow.get(p,0):6.4f} | {dk_wta_post_pow_adj.get(p,0):6.4f} | {dk_wta_post_mult_adj.get(p,0):6.4f} | {blend_wta[p]:6.4f} | {wta_sf_pm_mkt.get(p,0):5.3f} | {wta_fin_pm_adj.get(p,0):5.3f}")
print(f"Top-5 sum = {sum(v for _, v in sorted(blend_wta.items(), key=lambda x: -x[1])[:5]):.4f}, Residual = {sum(v for _, v in sorted(blend_wta.items(), key=lambda x: -x[1])[5:]):.4f}")
print(f"ATP Top-5 sum = {sum(v for _, v in sorted(blend_atp.items(), key=lambda x: -x[1])[:5]):.4f}, Residual = {sum(v for _, v in sorted(blend_atp.items(), key=lambda x: -x[1])[5:]):.4f}")
