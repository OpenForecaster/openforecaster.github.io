import math
from collections import Counter

def p_bo3(ea, eb):
    return 1.0 / (1.0 + 10.0 ** (-(ea - eb) / 400.0))

def p_bo5(ea, eb):
    p3 = p_bo3(ea, eb)
    ps = p3
    for _ in range(8):
        f = ps*ps*(3 - 2*ps) - p3
        df = 6*ps*(1 - ps) + 1e-12
        ps = max(1e-6, min(1 - 1e-6, ps - f / df))
    return ps**3 * (10 - 15*ps + 6*ps*ps)

def american_to_prob(odds):
    return (-odds) / (-odds + 100.0) if odds < 0 else 100.0 / (odds + 100.0)

def devig_mult(raw_dict):
    s = sum(raw_dict.values())
    return {k: v / s for k, v in raw_dict.items()}

def devig_power(raw_dict):
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

def solve_8_exact(bracket8, elo_map, p_fn, locked_qfs=None, h2h_override=None):
    locked_qfs = locked_qfs or {}
    h2h_override = h2h_override or {}
    def gp(a, b):
        if (a, b) in h2h_override: return h2h_override[(a, b)]
        if (b, a) in h2h_override: return 1.0 - h2h_override[(b, a)]
        return p_fn(elo_map[a], elo_map[b])

    q = []
    for idx in range(4):
        a, b = bracket8[2*idx], bracket8[2*idx+1]
        if idx in locked_qfs:
            q.append({locked_qfs[idx]: 1.0})
        else:
            pa = gp(a, b)
            q.append({a: pa, b: 1.0 - pa})

    sf_p = {}
    for d in q:
        sf_p.update(d)

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

def bayes_lr_update(prior_dict, model_before, model_after):
    raw = {}
    for p, pr in prior_dict.items():
        if model_after.get(p, 0.0) == 0.0:
            raw[p] = 0.0
        else:
            raw[p] = pr * (model_after[p] / max(1e-9, model_before[p]))
    tot = sum(raw.values())
    return {p: v / tot for p, v in raw.items()}

# ==============================================================================
# PART 1: Q1 (408930) — BEN SHELTON vs FRANCES TIAFOE (EXACT 2-OUTCOME SF!)
# ==============================================================================
print("=" * 95)
print("PART 1: Q1 (408930) FURTHEST U.S. MAN — DIRECT SF: BEN SHELTON vs FRANCES TIAFOE (Fri Sep 11)")
print("=" * 95)

# 1A. SI.com Sep 9 direct moneyline: Shelton -285 vs Tiafoe (implied opposing dog +220 to +240)
print("\n[1A] SI.com Sep 9 Moneyline Devig (Shelton -285 across plausible opposing Tiafoe lines):")
for dog in [215, 220, 225, 230, 235, 240]:
    p1, p2 = american_to_prob(-285), american_to_prob(dog)
    m1, pw1, _ = devig_two_way(p1, p2)
    print(f"  -285 / +{dog}: Raw={p1:.4f}/{p2:.4f} (vig={p1+p2-1:.4f}) | Mult={m1:.4f} | Power={pw1:.4f}")

# 1B. Implied SF win prob from Sep 9 Futures ratios (Kalshi, DK Predictions, SI.com)
# Note: Ratio R = P(Shelton title) / P(Tiafoe title) = [p / (1-p)] * [W_sh / W_tia]
# where W_sh, W_tia are conditional Final win probabilities vs Top Half (~72% Zverev, ~24% Khachanov, ~4% BVDZ)
print("\n[1B] Futures-Implied Shelton vs Tiafoe SF Probability:")
for label, r_fut in [
    ("Kalshi Sep 9 (37% / 10%)", 0.37 / 0.10),
    ("DK Predictions Sep 9 (40% / 11%)", 0.40 / 0.11),
    ("SI.com Pow-devig (+140 / +650)", None),
]:
    if r_fut is None:
        si_raw = {
            "Alexander Zverev": american_to_prob(110),
            "Ben Shelton": american_to_prob(140),
            "Frances Tiafoe": american_to_prob(650),
            "Karen Khachanov": american_to_prob(1700),
            "Alexander Blockx": american_to_prob(3000),
            "Botic van de Zandschulp": american_to_prob(4000),
        }
        si_pw, _ = devig_power(si_raw)
        si_mlt = devig_mult(si_raw)
        r_fut = si_pw["Ben Shelton"] / si_pw["Frances Tiafoe"]
        print(f"  SI.com Pow ratio = {si_pw['Ben Shelton']:.4f} / {si_pw['Frances Tiafoe']:.4f} = {r_fut:.3f} (Mult ratio = {si_mlt['Ben Shelton']/si_mlt['Frances Tiafoe']:.3f})")
    for w_ratio in [1.40, 1.48, 1.56]:
        odds_sf = r_fut / w_ratio
        p_sf = odds_sf / (1.0 + odds_sf)
        print(f"  {label:35s} (W_sh/W_tia={w_ratio:.2f}) -> P(Shelton > Tiafoe) = {p_sf:.4f}")

# 1C. Pre-committed Sep 8 Elo + Bayesian latent-skill update for beating Alcaraz
sh_states = [(2035.0, 0.25), (2090.0, 0.50), (2150.0, 0.25)]
p_sh_qf_states = [p_bo5(e, 2272.0) for e, _ in sh_states]
p_sh_qf_marg = sum(w * p for (_, w), p in zip(sh_states, p_sh_qf_states))
post_sh_w = [w * p / p_sh_qf_marg for (_, w), p in zip(sh_states, p_sh_qf_states)]
e_sh_post = sum(e * pw for (e, _), pw in zip(sh_states, post_sh_w))
p_sh_vs_tia_2015 = sum(pw * p_bo5(e, 2015.0) for (e, _), pw in zip(sh_states, post_sh_w))
p_sh_vs_tia_2000 = sum(pw * p_bo5(e, 2000.0) for (e, _), pw in zip(sh_states, post_sh_w))
print(f"\n[1C] Sep 8 Latent-Skill Posterior (Shelton post-Alcaraz Elo = {e_sh_post:.1f}):")
print(f"  vs Tiafoe 2015 (fresh): {p_sh_vs_tia_2015:.4f} | vs Tiafoe 2000 (5-set adj): {p_sh_vs_tia_2000:.4f}")
print(f"  Wait: With both playing 4.5h 5-setters + Shelton 3:33am finish + 3-1 H2H:")
print(f"  Consensus blend: 45% SI -285 moneyline (0.713) + 25% Kalshi/DK futures-implied (0.710) + 30% Elo/Bayes+H2H (0.688) = {0.45*0.713 + 0.25*0.710 + 0.30*0.688:.4f}")

# ==============================================================================
# PART 2: Q3 (891014) — ATP US OPEN TITLE (WED SEP 9 EVENING — KHACHANOV IN SF!)
# ==============================================================================
print("\n" + "=" * 95)
print("PART 2: Q3 (891014) ATP TITLE — ALCARAZ & BLOCKX OUT! KHACHANOV, SHELTON, TIAFOE IN SF!")
print("=" * 95)

atp_6 = [
    "Alexander Zverev", "Botic van de Zandschulp",
    "Karen Khachanov", "Alexander Blockx",
    "Frances Tiafoe", "Ben Shelton",
]
# Wait: rewrite as 8-bracket with locked QFs for clean solver:
atp_qfs = [
    "Alexander Zverev", "Botic van de Zandschulp",
    "Karen Khachanov", "Alexander Blockx",
    "Frances Tiafoe", "Alex Michelsen",
    "Carlos Alcaraz", "Ben Shelton",
]
locked_am_09 = {2: "Frances Tiafoe", 3: "Ben Shelton"}  # Morning Sep 9 (pre-Khachanov win!)
locked_pm_09 = {1: "Karen Khachanov", 2: "Frances Tiafoe", 3: "Ben Shelton"}  # Evening Sep 9 (Khachanov beat Blockx!)

# Market snapshots from Sep 9 MORNING (BEFORE Khachanov beat Blockx!)
# 1. Kalshi Sep 9 morning: Zverev 44%, Shelton 37%, Tiafoe 10%, Khachanov 5%, Blockx 3%, BVDZ ~1% (sum=100%)
kalshi_am_09 = {
    "Alexander Zverev": 0.440,
    "Ben Shelton": 0.370,
    "Frances Tiafoe": 0.100,
    "Karen Khachanov": 0.050,
    "Alexander Blockx": 0.030,
    "Botic van de Zandschulp": 0.010,
}
# 2. SI.com Sportsbook Sep 9 morning: Zverev +110, Shelton +140, Tiafoe +650, Khachanov +1700, Blockx +3000, BVDZ +4000
si_am_raw = {
    "Alexander Zverev": american_to_prob(110),
    "Ben Shelton": american_to_prob(140),
    "Frances Tiafoe": american_to_prob(650),
    "Karen Khachanov": american_to_prob(1700),
    "Alexander Blockx": american_to_prob(3000),
    "Botic van de Zandschulp": american_to_prob(4000),
}
si_am_mult = devig_mult(si_am_raw)
si_am_pow, k_si = devig_power(si_am_raw)

# 3. DraftKings Predictions Sep 9 5:35 AM ET: Zverev 45%, Shelton 40%, Tiafoe 11%, Khachanov 6%
# Add proportional tail for Blockx (2.5%) & BVDZ (1.0%) matching Kalshi/SI before normalizing
dkp_am_raw = {
    "Alexander Zverev": 0.450,
    "Ben Shelton": 0.400,
    "Frances Tiafoe": 0.110,
    "Karen Khachanov": 0.060,
    "Alexander Blockx": 0.028,
    "Botic van de Zandschulp": 0.012,
}
dkp_am_norm = devig_mult(dkp_am_raw)

print(f"\n[2A] Sep 9 MORNING (PRE-KHACHANOV WIN) Markets (SI vig={sum(si_am_raw.values())-1:.4f}, k={k_si:.3f}):")
print(f"{'Player':24s} | {'Kalshi':7s} | {'DK_Pred':7s} | {'SI_Mult':7s} | {'SI_Pow':7s}")
for p in kalshi_am_09:
    print(f"{p:24s} | {kalshi_am_09[p]:7.4f} | {dkp_am_norm[p]:7.4f} | {si_am_mult[p]:7.4f} | {si_am_pow[p]:7.4f}")

# Calibrate TWO ATP Elo models to Sep 9 morning market lines:
#   - Zverev vs BVDZ = 0.880 (Kalshi 88%)
#   - Khachanov vs Blockx = 0.600 (Kalshi 60%)
#   - Shelton vs Tiafoe = 0.712 (SI -285)
#   - Model MKT_CAL: Zverev Finals = 74% (Kalshi exact!), Zverev vs Shelton = 56.5% (5-0 H2H, matches Kalshi 44/37!)
#   - Model ELO_SH: Slightly higher Shelton post-Alcaraz form (Zverev vs Shelton = 52.5%, matches DK Pred 45/40 & SI +110/+140!)
atp_elo_kal = {
    "Alexander Zverev": 2168.0,
    "Ben Shelton":      2128.0,   # Zverev vs Shelton = 0.576 (5-0 H2H!)
    "Frances Tiafoe":   2010.0,   # Shelton vs Tiafoe = 0.713 (matches -285!)
    "Karen Khachanov":  1965.0,   # Zverev vs Khach = 0.822 -> Zverev Finals = 0.88 * (0.6*0.822 + 0.4*0.875) = 0.742 (Kalshi 74%!)
    "Alexander Blockx": 1912.0,   # Khach vs Blockx = 0.600 (Kalshi 60%!)
    "Botic van de Zandschulp": 1912.0, # Zverev vs BVDZ = 0.880 (Kalshi 88%!)
    "Carlos Alcaraz":   2272.0,
    "Alex Michelsen":   1972.0,
}

# Model ELO_BAL: Respects Shelton's Alcaraz upset + Khachanov beating FAA/Tien (Zverev vs Khach ~78%, Zverev vs Shelton ~53.5%)
atp_elo_bal = {
    "Alexander Zverev": 2160.0,
    "Ben Shelton":      2140.0,   # Zverev vs Shelton = 0.538 (respects 5-0 H2H + Shelton peak form!)
    "Frances Tiafoe":   2024.0,   # Shelton vs Tiafoe = 0.710
    "Karen Khachanov":  1988.0,   # Zverev vs Khach = 0.785; Khach vs BVDZ = 0.654
    "Alexander Blockx": 1936.0,   # Khach vs Blockx = 0.598
    "Botic van de Zandschulp": 1906.0, # Zverev vs BVDZ = 0.878
    "Carlos Alcaraz":   2272.0,
    "Alex Michelsen":   1972.0,
}

# Check pairwise probs!
print("\n[2B] ATP Pairwise Matchup Calibration (BO5):")
for a, b, note in [
    ("Alexander Zverev", "Botic van de Zandschulp", "Kalshi 88%"),
    ("Karen Khachanov", "Alexander Blockx", "Kalshi 60% (COMPLETED: Khach won!)"),
    ("Ben Shelton", "Frances Tiafoe", "SI -285 (~71.3%)"),
    ("Alexander Zverev", "Karen Khachanov", "Likely SF1"),
    ("Alexander Zverev", "Ben Shelton", "Likely Final (Zverev 5-0 H2H)"),
    ("Alexander Zverev", "Frances Tiafoe", "Alt Final"),
    ("Ben Shelton", "Karen Khachanov", "Alt Final"),
    ("Frances Tiafoe", "Karen Khachanov", "Alt Final"),
]:
    print(f"  {a:20s} vs {b:24s}: KAL={p_bo5(atp_elo_kal[a], atp_elo_kal[b]):.4f} | BAL={p_bo5(atp_elo_bal[a], atp_elo_bal[b]):.4f} ({note})")

_, atp_fin_am_kal, atp_win_am_kal = solve_8_exact(atp_qfs, atp_elo_kal, p_bo5, locked_qfs=locked_am_09)
atp_sf_pm_kal, atp_fin_pm_kal, atp_win_pm_kal = solve_8_exact(atp_qfs, atp_elo_kal, p_bo5, locked_qfs=locked_pm_09)

_, atp_fin_am_bal, atp_win_am_bal = solve_8_exact(atp_qfs, atp_elo_bal, p_bo5, locked_qfs=locked_am_09)
_, atp_fin_pm_bal, atp_win_pm_bal = solve_8_exact(atp_qfs, atp_elo_bal, p_bo5, locked_qfs=locked_pm_09)

print("\n[2C] Model Fit to Sep 9 MORNING Markets (before Khachanov beat Blockx):")
print(f"{'Player':24s} | {'Kalshi':7s} | {'KAL_AM':7s} | {'DK_Pred':7s} | {'SI_Pow':7s} | {'BAL_AM':7s} | {'Fin_KAL':7s}")
for p in kalshi_am_09:
    print(f"{p:24s} | {kalshi_am_09[p]:7.4f} | {atp_win_am_kal[p]:7.4f} | {dkp_am_norm[p]:7.4f} | {si_am_pow[p]:7.4f} | {atp_win_am_bal[p]:7.4f} | {atp_fin_am_kal[p]:7.4f}")

# Exact Bayesian update of ALL THREE Sep 9 Morning Markets conditioned on Khachanov beating Blockx!
# Use average likelihood ratio of KAL & BAL (they agree almost identically on Khachanov winning 60% QF!)
lr_avg_am = {p: 0.5*atp_win_am_kal.get(p, 0.0) + 0.5*atp_win_am_bal.get(p, 0.0) for p in kalshi_am_09}
lr_avg_pm = {p: 0.5*atp_win_pm_kal.get(p, 0.0) + 0.5*atp_win_pm_bal.get(p, 0.0) for p in kalshi_am_09}

kal_post = bayes_lr_update(kalshi_am_09, atp_win_am_kal, atp_win_pm_kal)
dkp_post = bayes_lr_update(dkp_am_norm, lr_avg_am, lr_avg_pm)
si_pow_post = bayes_lr_update(si_am_pow, lr_avg_am, lr_avg_pm)
si_mlt_post = bayes_lr_update(si_am_mult, lr_avg_am, lr_avg_pm)

# Blend for Q3 (ATP Title — Evening Sep 9, Khachanov IN SF, ONLY 5 players left, sum=1.00!):
#   25% Kalshi Bayes-Post (liquid prediction market)
#   20% DK Predictions Bayes-Post
#   20% SI.com Power-Devig Bayes-Post (sharp sportsbook)
#   10% SI.com Mult-Devig Bayes-Post
#   15% Exact Bracket Model KAL_PM (5-0 Zverev H2H weight)
#   10% Exact Bracket Model BAL_PM (Shelton form & Khachanov run weight)
atp_5 = ["Alexander Zverev", "Ben Shelton", "Frances Tiafoe", "Karen Khachanov", "Botic van de Zandschulp"]
blend_atp = {}
for p in atp_5:
    blend_atp[p] = (
        0.25 * kal_post[p]
        + 0.20 * dkp_post[p]
        + 0.20 * si_pow_post[p]
        + 0.10 * si_mlt_post[p]
        + 0.15 * atp_win_pm_kal[p]
        + 0.10 * atp_win_pm_bal[p]
    )

print("\n" + "=" * 120)
print("Q3 (891014) ATP EVENING SEP 9 (POST-KHACHANOV WIN; ONLY 5 PLAYERS REMAIN, EXHAUSTIVE SUM=1.00!)")
print("=" * 120)
print(f"{'Player':24s} | {'Kal_P':6s} | {'DKP_P':6s} | {'SI_Pw':6s} | {'SI_Ml':6s} | {'KAL_M':6s} | {'BAL_M':6s} | {'BLEND':6s} | {'FIN_P':5s}")
for p, _ in sorted(blend_atp.items(), key=lambda x: -x[1]):
    fp = 0.5*atp_fin_pm_kal[p] + 0.5*atp_fin_pm_bal[p]
    print(f"{p:24s} | {kal_post[p]:6.4f} | {dkp_post[p]:6.4f} | {si_pow_post[p]:6.4f} | {si_mlt_post[p]:6.4f} | {atp_win_pm_kal[p]:6.4f} | {atp_win_pm_bal[p]:6.4f} | {blend_atp[p]:6.4f} | {fp:5.3f}")
print(f"Sum of 5 remaining players = {sum(blend_atp.values()):.4f}")

# ==============================================================================
# PART 3: Q2 (608158) — WTA US OPEN TITLE (ALL 4 TOP SEEDS LOCKED IN SEMIFINALS!)
# ==============================================================================
print("\n" + "=" * 95)
print("PART 3: Q2 (608158) WTA TITLE — ALL 4 TOP SEEDS IN SF! (EXHAUSTIVE 4-PLAYER MARKET, SUM=1.00!)")
print("=" * 95)

wta_qfs = [
    "Aryna Sabalenka", "Linda Noskova",
    "Jessica Pegula", "Emma Navarro",
    "Coco Gauff", "Mirra Andreeva",
    "Elena Rybakina", "Qinwen Zheng",
]
locked_wta_sf = {
    0: "Aryna Sabalenka",
    1: "Jessica Pegula",
    2: "Coco Gauff",
    3: "Elena Rybakina",
}

# Re-import Sep 8 11:16 AM ET DraftKings WTA Championship & Finals odds for EXACT Bayesian conditioning!
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
dk_wta_mult = devig_mult(dk_wta_win_am)
dk_wta_pow, _ = devig_power(dk_wta_win_am)

# Pre-QF calibrated Elo (exact match to Sep 8 DK QF lines & Finals odds — same as tennis_sep08_models.py!)
wta_elo_pre = {
    "Aryna Sabalenka": 2198.0,
    "Linda Noskova":   2048.0,
    "Jessica Pegula":  2075.0,
    "Emma Navarro":    1955.0,
    "Coco Gauff":      2175.0,
    "Mirra Andreeva":  2074.0,
    "Elena Rybakina":  2148.0,
    "Qinwen Zheng":    1987.0,
}
wta_h2h_pre = {
    ("Jessica Pegula", "Emma Navarro"): 0.783,
    ("Aryna Sabalenka", "Jessica Pegula"): 0.700,
}
_, _, wta_win_pre = solve_8_exact(wta_qfs, wta_elo_pre, p_bo3, locked_qfs={}, h2h_override=wta_h2h_pre)

# Now define 3 well-grounded POST-QF WTA models for the exact 4-player SF bracket!
#
# Model W1 (DK_PURE — strict outcome-only Bayes update of Sep 8 DK with NO subjective form tweaking):
#   Sabalenka 2198 vs Pegula 2075 (H2H 0.700), Gauff 2175 vs Rybakina 2148 (0.539), Sab vs Gauff (0.533), Sab vs Ryb (0.571)
_, w1_fin, w1_win = solve_8_exact(wta_qfs, wta_elo_pre, p_bo3, locked_qfs=locked_wta_sf, h2h_override=wta_h2h_pre)
dk_pow_pure = bayes_lr_update(dk_wta_pow, wta_win_pre, w1_win)
dk_mlt_pure = bayes_lr_update(dk_wta_mult, wta_win_pre, w1_win)

# Model W2 (FORM_ADJ — incorporates actual Tue/Wed QF performance + H2H facts!):
#   - Sabalenka slight -10 after 7-6(10-7) 3rd-set scare vs Noskova & no title since Miami, STILL 9-4 H2H & 49-3 HC majors!
#     -> Sab vs Pegula = 0.680 (H2H/USO dominance vs Pegula's Berlin win & Cin final!)
#   - Gauff slight -12 after 2-6 opening set & saving 2 MPs vs Andreeva (20-set streak broken)
#   - Rybakina slight +8 after beating Zheng 3-6, 6-1, 6-4 & clinching World #1 (injury cleared + beat Gauff in Toronto SF!)
#     -> Gauff 2163 vs Rybakina 2156 -> 0.510 (virtual coin flip! Gauff home crowd & Cin title vs Ryb #1 & Toronto H2H!)
#   - Sabalenka 2188 vs Gauff 2163 = 0.536 | Sabalenka 2188 vs Rybakina 2156 = 0.546
#   - Pegula 2075 vs Gauff 2163 = 0.376 | Pegula 2075 vs Rybakina 2156 = 0.386
wta_elo_adj = {
    "Aryna Sabalenka": 2188.0,
    "Jessica Pegula":  2075.0,
    "Coco Gauff":      2163.0,
    "Elena Rybakina":  2156.0,
    "Linda Noskova":   2048.0,
    "Emma Navarro":    1955.0,
    "Mirra Andreeva":  2074.0,
    "Qinwen Zheng":    1987.0,
}
wta_h2h_adj = {
    ("Aryna Sabalenka", "Jessica Pegula"): 0.680,
}
_, w2_fin, w2_win = solve_8_exact(wta_qfs, wta_elo_adj, p_bo3, locked_qfs=locked_wta_sf, h2h_override=wta_h2h_adj)
dk_pow_adj = bayes_lr_update(dk_wta_pow, wta_win_pre, w2_win)
dk_mlt_adj = bayes_lr_update(dk_wta_mult, wta_win_pre, w2_win)

# Model W3 (RYB_NO1 — stronger Rybakina World #1 / Toronto H2H edge & slightly tougher Pegula):
#   - Sabalenka vs Pegula = 0.665 (pure Elo, no extra H2H boost)
#   - Rybakina 2168 vs Gauff 2152 = 0.523 Rybakina (Toronto 5-7, 6-2, 6-2 winner + World #1!)
#   - Sabalenka 2190 vs Rybakina 2168 = 0.532 | Sabalenka 2190 vs Gauff 2152 = 0.554
wta_elo_ryb = {
    "Aryna Sabalenka": 2190.0,
    "Jessica Pegula":  2078.0,
    "Coco Gauff":      2152.0,
    "Elena Rybakina":  2168.0,
    "Linda Noskova":   2048.0,
    "Emma Navarro":    1955.0,
    "Mirra Andreeva":  2074.0,
    "Qinwen Zheng":    1987.0,
}
_, w3_fin, w3_win = solve_8_exact(wta_qfs, wta_elo_ryb, p_bo3, locked_qfs=locked_wta_sf, h2h_override={})

print("\n[3A] WTA Semifinal & Final Pairwise Probabilities:")
for a, b in [
    ("Aryna Sabalenka", "Jessica Pegula"),
    ("Coco Gauff", "Elena Rybakina"),
    ("Aryna Sabalenka", "Coco Gauff"),
    ("Aryna Sabalenka", "Elena Rybakina"),
    ("Jessica Pegula", "Coco Gauff"),
    ("Jessica Pegula", "Elena Rybakina"),
]:
    p1 = wta_h2h_pre.get((a, b), p_bo3(wta_elo_pre[a], wta_elo_pre[b]))
    p2 = wta_h2h_adj.get((a, b), p_bo3(wta_elo_adj[a], wta_elo_adj[b]))
    p3 = p_bo3(wta_elo_ryb[a], wta_elo_ryb[b])
    print(f"  {a:18s} vs {b:18s}: W1(Pre)={p1:.4f} | W2(Adj)={p2:.4f} | W3(Ryb#1)={p3:.4f}")

# Blend for Q2 (WTA Title — 4 exhaustive semifinalists, sum=1.00!):
#   20% DK_Pow Pure Outcome-Only Bayes (respects market pre-QF Gauff>Rybakina & Sabalenka edge!)
#   25% DK_Pow Form-Adj Bayes
#   15% DK_Mlt Form-Adj Bayes
#   25% W2 Form-Adj Exact Bracket
#   15% W3 Rybakina-#1 / Balanced Exact Bracket
wta_4 = ["Aryna Sabalenka", "Coco Gauff", "Elena Rybakina", "Jessica Pegula"]
blend_wta = {}
for p in wta_4:
    blend_wta[p] = (
        0.20 * dk_pow_pure[p]
        + 0.25 * dk_pow_adj[p]
        + 0.15 * dk_mlt_adj[p]
        + 0.25 * w2_win[p]
        + 0.15 * w3_win[p]
    )

print("\n" + "=" * 120)
print("Q2 (608158) WTA EVENING SEP 9 (ALL 4 TOP SEEDS IN SF — EXHAUSTIVE 4-PLAYER MARKET, SUM=1.00!)")
print("=" * 120)
print(f"{'Player':18s} | {'DK_Pur':6s} | {'DK_Adj':6s} | {'DK_Mlt':6s} | {'W1_Pre':6s} | {'W2_Adj':6s} | {'W3_Ryb':6s} | {'BLEND':6s} | {'FIN_P':5s}")
for p, _ in sorted(blend_wta.items(), key=lambda x: -x[1]):
    fp = 0.25*w1_fin[p] + 0.55*w2_fin[p] + 0.20*w3_fin[p]
    print(f"{p:18s} | {dk_pow_pure[p]:6.4f} | {dk_pow_adj[p]:6.4f} | {dk_mlt_adj[p]:6.4f} | {w1_win[p]:6.4f} | {w2_win[p]:6.4f} | {w3_win[p]:6.4f} | {blend_wta[p]:6.4f} | {fp:5.3f}")
print(f"Sum of 4 semifinalists = {sum(blend_wta.values()):.4f}")
