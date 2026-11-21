import math

# ==============================================================================
# A. Q891014 MEN'S SINGLES — EXACT CALIBRATED SYNTHESIS
# ==============================================================================
# Blending:
#   1. SI.com US Sportsbook (Power/Shin devig -> DP post-Khachanov):
#      Zverev 0.429, Shelton 0.380, Tiafoe 0.109, Khachanov 0.070, BvdZ 0.013
#   2. Kalshi Prediction Market (DP post-Khachanov):
#      Zverev 0.431, Shelton 0.370, Tiafoe 0.099, Khachanov 0.082, BvdZ 0.017
#   3. Exact Kalshi-Anchored Explicit Bracket (QF Zv>BvdZ=0.88, SF1 Sh>Ti=0.725, SF2 Zv>Kh=0.815, Final Zv>Sh=0.555, Zv>Ti=0.715, Sh>Kh=0.70, Ti>Kh=0.54, Kh>BvdZ=0.65):

def men_explicit(p_zv_bv=0.88, p_zv_kh=0.815, p_kh_bv=0.66, p_sh_ti=0.725,
                 p_zv_sh=0.56, p_zv_ti=0.72, p_sh_kh=0.70, p_ti_kh=0.54,
                 p_sh_bv=0.79, p_ti_bv=0.66):
    f_zv = p_zv_bv * p_zv_kh
    f_kh = p_zv_bv * (1 - p_zv_kh) + (1 - p_zv_bv) * p_kh_bv
    f_bv = (1 - p_zv_bv) * (1 - p_kh_bv)
    f_sh = p_sh_ti
    f_ti = 1 - p_sh_ti
    res = {
        "Alexander Zverev": f_zv * (f_sh * p_zv_sh + f_ti * p_zv_ti),
        "Ben Shelton":      f_sh * (f_zv * (1 - p_zv_sh) + f_kh * p_sh_kh + f_bv * p_sh_bv),
        "Frances Tiafoe":   f_ti * (f_zv * (1 - p_zv_ti) + f_kh * p_ti_kh + f_bv * p_ti_bv),
        "Karen Khachanov":  f_kh * (f_sh * (1 - p_sh_kh) + f_ti * (1 - p_ti_kh)),
        "Botic van de Zandschulp": f_bv * (f_sh * (1 - p_sh_bv) + f_ti * (1 - p_ti_bv)),
    }
    return res, (f_zv, f_kh, f_bv)

print("=== Q891014 MEN'S EXACT SYNTHESIS ===")
m_exp1, f1 = men_explicit(p_zv_kh=0.815, p_zv_sh=0.56, p_zv_ti=0.72)
m_exp2, f2 = men_explicit(p_zv_kh=0.820, p_zv_sh=0.555, p_zv_ti=0.715)
m_exp3, f3 = men_explicit(p_zv_kh=0.805, p_zv_sh=0.57, p_zv_ti=0.72)

si_post = {"Alexander Zverev": 0.4287, "Ben Shelton": 0.3799, "Frances Tiafoe": 0.1087, "Karen Khachanov": 0.0697, "Botic van de Zandschulp": 0.0131}
kal_post = {"Alexander Zverev": 0.4309, "Ben Shelton": 0.3702, "Frances Tiafoe": 0.0994, "Karen Khachanov": 0.0821, "Botic van de Zandschulp": 0.0174}

for name, d in [("SI_DP_avg", si_post), ("Kalshi_DP", kal_post), ("Explicit_Base", m_exp1), ("Explicit_Zv82", m_exp2), ("Explicit_Zv57", m_exp3)]:
    print(f"  {name:15s}: " + " ".join(f"{k.split()[-1][:4]}={v:.4f}" for k, v in d.items()) + f" (sum={sum(d.values()):.4f})")

# Equal blend of SI_DP (35%), Kalshi_DP (35%), Explicit_Base (30%):
men_blend = {k: 0.35*si_post[k] + 0.35*kal_post[k] + 0.30*m_exp1[k] for k in si_post}
print("  35SI/35Kal/30Ex: " + " ".join(f"{k.split()[-1][:4]}={v:.4f}" for k, v in men_blend.items()) + f" (sum={sum(men_blend.values()):.4f})")

# ==============================================================================
# B. Q608158 WOMEN'S SINGLES — EXACT BAYESIAN + TAB-ANCHORED SYNTHESIS
# ==============================================================================
print("\n=== Q608158 WOMEN'S EXACT SYNTHESIS ===")
# We have:
#   1. TAB Sep 9 11:02 PM AEST exact SF1 line: Sabalenka $1.53 vs Pegula $2.50
#      -> Prop 62.0%, Shin 62.7%, Pow 63.0% | Stats Insider ML = 61.0% -> anchored SF1 = 0.625 (range 0.615-0.640)
#   2. Pre-Wed-QF markets (Covers DK Predictions Sep 9 AM + ESPN DK Sep 8):
#      Conditioned pure DP: Sab 0.346, Gauff 0.300, Rybakina 0.237, Pegula 0.118
#      NOTE why Pegula was only 0.118 there: Covers DK Predictions had Sab/Peg implied SF1 = 69.5% vs TAB's actual 62.5%!
#      Let's check what happens when we fit Covers Sep 9 AM + ESPN DK Sep 8 AND anchor Sab vs Peg to 62.5-64.0% AND test Gauff Bayesian QF adjustment (-0, -15, -25 Elo)!

def wom_4p(p_sp, p_gr, p_sg, p_sr, p_pg, p_pr):
    return {
        "Aryna Sabalenka": p_sp * (p_gr * p_sg + (1 - p_gr) * p_sr),
        "Coco Gauff":      p_gr * (p_sp * (1 - p_sg) + (1 - p_sp) * (1 - p_pg)),
        "Elena Rybakina":  (1 - p_gr) * (p_sp * (1 - p_sr) + (1 - p_sp) * (1 - p_pr)),
        "Jessica Pegula":  (1 - p_sp) * (p_gr * p_pg + (1 - p_gr) * p_pr),
    }

# Realistic Final probabilities given:
#   - Sabalenka: 2x defending USO champ (49-3 hard Slams), beat Gauff in 2024 AO SF, lost 2023 USO F to Gauff, lost 2026 AO F to Rybakina.
#     Wait: On Arthur Ashe hard courts vs Gauff (home crowd, 11-match win streak) -> Sab ~54-56% (NOT 59%, look at Covers/ESPN implying 49-51%!).
#     Wait! Why did Covers/ESPN imply Sab~50% vs Gauff and ~53-55% vs Rybakina?!
#     BECAUSE Sabalenka has NOT won a title since Miami in March AND nearly lost to Noskova, while Gauff won Cincy & Rybakina won AO 2026 (beating Sabalenka!) and just became World #1!
#     Let's check BOTH Sab-neutral (53% vs Gauff, 54% vs Ryb) and Sab-favored (56% vs Gauff, 55% vs Ryb)!
#   - Pegula in Final: lost to Gauff in 2026 Cincinnati final (on hard courts, 2 weeks ago!) -> Peg vs Gauff ~36-38%, Peg vs Ryb ~36-38%!
scenarios = [
    ("A: TAB62.5, Gauff53/47 (pre-QF mkt), Sab54/54, Peg37/37", 0.625, 0.53, 0.54, 0.54, 0.37, 0.37),
    ("B: TAB62.5, Tossup50/50 (Gauff -15Elo), Sab54/53, Peg37/37", 0.625, 0.50, 0.54, 0.53, 0.37, 0.37),
    ("C: TAB62.5, Ryb52/48 (Gauff -25Elo), Sab55/53, Peg37/37", 0.625, 0.48, 0.55, 0.53, 0.37, 0.37),
    ("D: MktBlend64.0, Tossup50/50, Sab55/54, Peg36/36", 0.640, 0.50, 0.55, 0.54, 0.36, 0.36),
    ("E: MktBlend64.0, Gauff51.5/48.5, Sab54/54, Peg36/36", 0.640, 0.515, 0.54, 0.54, 0.36, 0.36),
    ("F: TAB-SI61.5, Ryb51/49, Sab54/53, Peg38/37", 0.615, 0.49, 0.54, 0.53, 0.38, 0.37),
]
vals = []
for lbl, *args in scenarios:
    r = wom_4p(*args)
    vals.append(r)
    print(f"  [{lbl:57s}] Sab={r['Aryna Sabalenka']:.4f} Gau={r['Coco Gauff']:.4f} Ryb={r['Elena Rybakina']:.4f} Peg={r['Jessica Pegula']:.4f}")

# Average across scenarios A-F:
avg_w = {k: sum(v[k] for v in vals)/len(vals) for k in vals[0]}
print(f"  [{'AVERAGE A-F':57s}] Sab={avg_w['Aryna Sabalenka']:.4f} Gau={avg_w['Coco Gauff']:.4f} Ryb={avg_w['Elena Rybakina']:.4f} Peg={avg_w['Jessica Pegula']:.4f}")

# Also compare with pure Covers_Sep9_AM (Power/Shin) + ESPN_DK_Sep8 (Power/Shin) conditioned DP:
dp_cov = {"Aryna Sabalenka": 0.3500, "Coco Gauff": 0.3069, "Elena Rybakina": 0.2450, "Jessica Pegula": 0.0982}
dp_espn = {"Aryna Sabalenka": 0.3425, "Coco Gauff": 0.2924, "Elena Rybakina": 0.2276, "Jessica Pegula": 0.1375}
print(f"  [{'Pure Covers Sep9 AM DP (note Sab>Peg=69.5% too high)':57s}] Sab={dp_cov['Aryna Sabalenka']:.4f} Gau={dp_cov['Coco Gauff']:.4f} Ryb={dp_cov['Elena Rybakina']:.4f} Peg={dp_cov['Jessica Pegula']:.4f}")
print(f"  [{'Pure ESPN DK Sep8 DP (note Sab>Peg=65.0%)':57s}] Sab={dp_espn['Aryna Sabalenka']:.4f} Gau={dp_espn['Coco Gauff']:.4f} Ryb={dp_espn['Elena Rybakina']:.4f} Peg={dp_espn['Jessica Pegula']:.4f}")

# Weighted blend: 60% TAB-Anchored Scenarios (B/D/E center) + 25% ESPN_DK_DP + 15% Covers_DP
# Wait: adjust Covers & ESPN for Gauff's 2-MP-saved shaky QF vs Rybakina's World #1 dominant sets 2-3 (~-0.015 Gauff, +0.015 Rybakina):
adj_mkt = {
    "Aryna Sabalenka": 0.5*dp_espn["Aryna Sabalenka"] + 0.5*dp_cov["Aryna Sabalenka"],
    "Coco Gauff":      0.5*dp_espn["Coco Gauff"] + 0.5*dp_cov["Coco Gauff"] - 0.020,
    "Elena Rybakina":  0.5*dp_espn["Elena Rybakina"] + 0.5*dp_cov["Elena Rybakina"] + 0.020,
    "Jessica Pegula":  0.5*dp_espn["Jessica Pegula"] + 0.5*dp_cov["Jessica Pegula"],
}
final_w = {k: 0.65 * avg_w[k] + 0.35 * adj_mkt[k] for k in avg_w}
print(f"  [{'65% TAB-Anchored + 35% Adj-Market-DP':57s}] Sab={final_w['Aryna Sabalenka']:.4f} Gau={final_w['Coco Gauff']:.4f} Ryb={final_w['Elena Rybakina']:.4f} Peg={final_w['Jessica Pegula']:.4f} (sum={sum(final_w.values()):.4f})")
