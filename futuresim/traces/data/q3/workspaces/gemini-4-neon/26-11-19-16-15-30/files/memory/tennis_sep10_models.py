import math
from collections import Counter

def p_bo3(ea, eb):
    return 1.0 / (1.0 + 10.0 ** (-(ea - eb) / 400.0))

def p_bo5(ea, eb):
    p3 = p_bo3(ea, eb)
    ps = p3
    for _ in range(10):
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
    lo, hi = 0.5, 5.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if sum(v ** mid for v in raw_dict.values()) > 1.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    return {p: v ** k for p, v in raw_dict.items()}, k

def devig_shin_2way(p1, p2):
    # Exact additive/Shin approx for 2-way
    vig = p1 + p2 - 1.0
    # Shin parameter z
    s = p1 + p2
    z = (s - 1.0) / (s + 1.0)  # approximate
    # Exact Shin 2-way: q_i = (sqrt(z^2 + 4*(1-z)*p_i^2/s) - z) / (2*(1-z))
    # Solve z so q1+q2=1
    lo, hi = 0.0, 0.5
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        q1 = (math.sqrt(mid*mid + 4*(1-mid)*p1*p1/s) - mid) / (2*(1-mid))
        q2 = (math.sqrt(mid*mid + 4*(1-mid)*p2*p2/s) - mid) / (2*(1-mid))
        if q1 + q2 > 1.0:
            lo = mid
        else:
            hi = mid
    z = 0.5 * (lo + hi)
    q1 = (math.sqrt(z*z + 4*(1-z)*p1*p1/s) - z) / (2*(1-z))
    return q1, 1.0 - q1, z

def solve_4(sf1, sf2, match_probs):
    """Exact 4-player SF -> Final -> Champion solver.
    sf1 = (a, b), sf2 = (c, d)
    match_probs[(x, y)] = P(x beats y)
    """
    def gp(x, y):
        if (x, y) in match_probs: return match_probs[(x, y)]
        if (y, x) in match_probs: return 1.0 - match_probs[(y, x)]
        raise KeyError((x, y))
    a, b = sf1
    c, d = sf2
    pa = gp(a, b)
    pb = 1.0 - pa
    pc = gp(c, d)
    pd = 1.0 - pc
    win = {
        a: pa * (pc * gp(a, c) + pd * gp(a, d)),
        b: pb * (pc * gp(b, c) + pd * gp(b, d)),
        c: pc * (pa * gp(c, a) + pb * gp(c, b)),
        d: pd * (pa * gp(d, a) + pb * gp(d, b)),
    }
    fin = {a: pa, b: pb, c: pc, d: pd}
    return fin, win

# ==============================================================================
# PART 1: Q1 (408930) — BEN SHELTON vs FRANCES TIAFOE (Fri Sep 11 SF)
# ==============================================================================
print("=" * 100)
print("PART 1: Q1 (408930) — BEN SHELTON vs FRANCES TIAFOE (Sep 10 Fresh Markets)")
print("=" * 100)

# 1. SportsLine / US Sportsbooks (Sep 10 5:27 PM ET): Shelton -325 vs Tiafoe +253
p_sh_sl, p_ti_sl = american_to_prob(-325), american_to_prob(253)
sl_mult = p_sh_sl / (p_sh_sl + p_ti_sl)
sl_pow_d, k_sl = devig_power({"sh": p_sh_sl, "ti": p_ti_sl})
sl_shin, _, _ = devig_shin_2way(p_sh_sl, p_ti_sl)
print(f"1. SportsLine 5:27 PM ET (-325 / +253): Raw={p_sh_sl:.4f}/{p_ti_sl:.4f} (vig={p_sh_sl+p_ti_sl-1:.4f})")
print(f"   Mult={sl_mult:.4f} | Shin={sl_shin:.4f} | Power={sl_pow_d['sh']:.4f} (k={k_sl:.3f})")

# 2. Kalshi (Sep 10, si.com): Shelton 74% / Tiafoe 28% (2% spread)
kal_sh_mult = 0.74 / (0.74 + 0.28)
kal_sh_mid = 0.5 * (0.74 + (1.0 - 0.28))
kal_sh_pow, _ = devig_power({"sh": 0.74, "ti": 0.28})
print(f"2. Kalshi Sep 10 (74% / 28%): Midpoint={kal_sh_mid:.4f} | Mult={kal_sh_mult:.4f} | Power={kal_sh_pow['sh']:.4f}")

# 3. DraftKings Predictions (Sep 10 2:39 PM ET, covers.com): Shelton 73%
dkp_sh = 0.730
print(f"3. DK Predictions Sep 10 2:39 PM ET: {dkp_sh:.4f}")

# 4. UniversTennis Market Aggregation (Sep 10): Shelton 72.5% / Tiafoe 27.5%
ut_sh = 0.725
print(f"4. UniversTennis Sep 10: {ut_sh:.4f}")

# 5. Elo/Fundamental posterior from Sep 9 (0.688) updated slightly upward for 2026 HC stats (1.18 vs 1.05 DR, 76% HC win rate, 73.4% SPW, 3-1 H2H)
elo_sh = 0.705
print(f"5. Elo + 2026 HC Dominance/Serve + 3-1 H2H prior: {elo_sh:.4f}")

# Weighted ensemble for Q1:
#   30% SportsLine 5:27pm (avg of Mult/Shin/Power = 0.738)
#   25% Kalshi Sep 10 (0.730)
#   20% DK Predictions Sep 10 (0.730)
#   10% UniversTennis Sep 10 (0.725)
#   15% Elo/Fundamentals (0.705)
sl_est = (sl_mult + sl_shin + sl_pow_d["sh"]) / 3.0
q1_blend = 0.30 * sl_est + 0.25 * kal_sh_mid + 0.20 * dkp_sh + 0.10 * ut_sh + 0.15 * elo_sh
print(f"\n==> Q1 BLEND: Ben Shelton = {q1_blend:.4f} ({q1_blend*100:.2f}%), Frances Tiafoe = {1-q1_blend:.4f} ({(1-q1_blend)*100:.2f}%)")
print(f"    (SportsLine sharp est = {sl_est:.4f}; pure market avg = {0.35*sl_est + 0.30*kal_sh_mid + 0.25*dkp_sh + 0.10*ut_sh:.4f})")

# ==============================================================================
# PART 2: Q3 (891014) — ATP US OPEN CHAMPION (EXACT 4-PLAYER SF MARKET!)
# ==============================================================================
print("\n" + "=" * 100)
print("PART 2: Q3 (891014) — ATP US OPEN CHAMPION (Zverev beat BVDZ! ONLY 4 PLAYERS LEFT!)")
print("=" * 100)

# Zverev vs Khachanov SF1 lines:
p_zv_sl, p_kh_sl = american_to_prob(-487), american_to_prob(358)
zv_mult = p_zv_sl / (p_zv_sl + p_kh_sl)
zv_pow_d, _ = devig_power({"zv": p_zv_sl, "kh": p_kh_sl})
zv_shin, _, _ = devig_shin_2way(p_zv_sl, p_kh_sl)
print(f"SF1 Zverev vs Khachanov:")
print(f"  SportsLine 5:27 PM ET (-487 / +358): Mult={zv_mult:.4f} | Shin={zv_shin:.4f} | Power={zv_pow_d['zv']:.4f}")
print(f"  DK Predictions 2:39 PM ET: Khachanov 20% -> Zverev ~80.0%")
print(f"  UniversTennis Sep 10: Zverev 77.8% / Khachanov 22.2%")
p_zv_sf = 0.45 * ((zv_mult + zv_shin + zv_pow_d['zv'])/3.0) + 0.30 * 0.800 + 0.25 * 0.778
print(f"  --> SF1 Consensus: Zverev = {p_zv_sf:.4f}, Khachanov = {1-p_zv_sf:.4f}")

# Championship Futures Markets (Sep 10, ALL 4 post-Zverev win!):
kal_atp_raw = {"Alexander Zverev": 0.49, "Ben Shelton": 0.36, "Frances Tiafoe": 0.09, "Karen Khachanov": 0.07}
kal_atp_mult = devig_mult(kal_atp_raw)
kal_atp_pow, _ = devig_power(kal_atp_raw)

dkp_atp_raw = {"Alexander Zverev": 0.53, "Ben Shelton": 0.40, "Frances Tiafoe": 0.12, "Karen Khachanov": 0.06}
dkp_atp_mult = devig_mult(dkp_atp_raw)
dkp_atp_pow, _ = devig_power(dkp_atp_raw)

kn_atp_raw = {
    "Alexander Zverev": american_to_prob(113),
    "Ben Shelton": american_to_prob(150),
    "Frances Tiafoe": american_to_prob(809),
    "Karen Khachanov": american_to_prob(1567),
}
kn_atp_mult = devig_mult(kn_atp_raw)
kn_atp_pow, k_kn = devig_power(kn_atp_raw)

ut_atp = {"Alexander Zverev": 0.454, "Ben Shelton": 0.345, "Frances Tiafoe": 0.123, "Karen Khachanov": 0.078}

# Exact 4-player bracket model consistent with SF1 (Zverev 79.7%) & SF2 (Shelton 73.0%):
# Conditional Final probabilities:
#   - Zverev vs Shelton: Zverev 5-0 H2H (3-0 HC), 2026 RG champ/Wim F vs Shelton 2026 Canada champ & upset Alcaraz -> ~57.5% Zverev / 42.5% Shelton
#   - Zverev vs Tiafoe: Zverev huge favorite (~71% Zverev / 29% Tiafoe)
#   - Khachanov vs Shelton: Shelton ~74% / Khachanov ~26%
#   - Khachanov vs Tiafoe: roughly even ~48% Khachanov / 52% Tiafoe
atp_match_base = {
    ("Alexander Zverev", "Karen Khachanov"): p_zv_sf,
    ("Ben Shelton", "Frances Tiafoe"): q1_blend,
    ("Alexander Zverev", "Ben Shelton"): 0.575,
    ("Alexander Zverev", "Frances Tiafoe"): 0.710,
    ("Karen Khachanov", "Ben Shelton"): 0.260,
    ("Karen Khachanov", "Frances Tiafoe"): 0.480,
}
_, atp_model_base = solve_4(("Alexander Zverev", "Karen Khachanov"), ("Ben Shelton", "Frances Tiafoe"), atp_match_base)

# Alt bracket model (slightly stronger Shelton peak form: Zverev vs Shelton 54.5%, Zverev vs Tiafoe 68%, Khachanov vs Shelton 23%)
atp_match_sh = {
    ("Alexander Zverev", "Karen Khachanov"): p_zv_sf,
    ("Ben Shelton", "Frances Tiafoe"): q1_blend,
    ("Alexander Zverev", "Ben Shelton"): 0.545,
    ("Alexander Zverev", "Frances Tiafoe"): 0.680,
    ("Karen Khachanov", "Ben Shelton"): 0.230,
    ("Karen Khachanov", "Frances Tiafoe"): 0.460,
}
_, atp_model_sh = solve_4(("Alexander Zverev", "Karen Khachanov"), ("Ben Shelton", "Frances Tiafoe"), atp_match_sh)

# Also check Sep 9 Bayes-conditioned posterior (conditioning Sep 9 blend on Zverev beating BVDZ!)
# From Sep 9: Zverev won QF with 88% prob -> BVDZ=0, Zverev gains ~0.045, Khachanov drops ~0.015
print(f"\nSep 10 ATP Championship Markets & Bracket Models (KhelNow vig={sum(kn_atp_raw.values())-1:.4f}):")
print(f"{'Player':20s} | {'Kal_M':6s} | {'DKP_M':6s} | {'DKP_P':6s} | {'KN_M':6s} | {'KN_P':6s} | {'UT':6s} | {'Mod1':6s} | {'Mod2':6s} | {'BLEND':6s}")

# Ensemble weights for Q3:
#   30% Kalshi (1% vig liquid exchange, direct Sep 10!)
#   20% KhelNow Sportsbook (avg Mult/Pow — only 3.95% vig!)
#   15% DraftKings Predictions (avg Mult/Pow)
#   10% UniversTennis (market agg)
#   15% Exact Bracket Model 1 (Zverev 5-0 H2H weight)
#   10% Exact Bracket Model 2 (Shelton post-Alcaraz form weight)
atp_blend = {}
for p in ["Alexander Zverev", "Ben Shelton", "Frances Tiafoe", "Karen Khachanov"]:
    kn_avg = 0.5 * (kn_atp_mult[p] + kn_atp_pow[p])
    dkp_avg = 0.5 * (dkp_atp_mult[p] + dkp_atp_pow[p])
    b = (
        0.30 * kal_atp_mult[p]
        + 0.20 * kn_avg
        + 0.15 * dkp_avg
        + 0.10 * ut_atp[p]
        + 0.15 * atp_model_base[p]
        + 0.10 * atp_model_sh[p]
    )
    atp_blend[p] = b
    print(f"{p:20s} | {kal_atp_mult[p]:6.4f} | {dkp_atp_mult[p]:6.4f} | {dkp_atp_pow[p]:6.4f} | {kn_atp_mult[p]:6.4f} | {kn_atp_pow[p]:6.4f} | {ut_atp[p]:6.4f} | {atp_model_base[p]:6.4f} | {atp_model_sh[p]:6.4f} | {b:6.4f}")
print(f"Sum = {sum(atp_blend.values()):.4f}")

# Implied Final conditional win rates of our blend!
print("\nImplied Conditional Final Win Probabilities (assuming SF1=79.7/20.3, SF2=73.0/27.0):")
sf_probs = {"Alexander Zverev": p_zv_sf, "Karen Khachanov": 1-p_zv_sf, "Ben Shelton": q1_blend, "Frances Tiafoe": 1-q1_blend}
for p in atp_blend:
    print(f"  {p:20s}: Title={atp_blend[p]:.4f} / SF={sf_probs[p]:.4f} => Cond Final Win = {atp_blend[p]/sf_probs[p]:.4f}")

# ==============================================================================
# PART 3: Q2 (608158) — WTA US OPEN CHAMPION (THU SEP 10 NIGHT SEMIFINALS!)
# ==============================================================================
print("\n" + "=" * 100)
print("PART 3: Q2 (608158) — WTA US OPEN CHAMPION (Fresh Thu Sep 10 Pre-Match Markets)")
print("=" * 100)

# SF1: Aryna Sabalenka vs Jessica Pegula
#   1. CBS Sports / DraftKings (Sep 10 5:01 PM ET): -195 / +158
p_sab_dk, p_peg_dk = american_to_prob(-195), american_to_prob(158)
sab_dk_m = p_sab_dk / (p_sab_dk + p_peg_dk)
sab_dk_p, _ = devig_power({"s": p_sab_dk, "p": p_peg_dk})
sab_dk_sh, _, _ = devig_shin_2way(p_sab_dk, p_peg_dk)

#   2. RotoWire / DK earlier: -178 / +170
p_sab_rw, p_peg_rw = american_to_prob(-178), american_to_prob(170)
sab_rw_m = p_sab_rw / (p_sab_rw + p_peg_rw)
sab_rw_p, _ = devig_power({"s": p_sab_rw, "p": p_peg_rw})

#   3. Kalshi (Sep 10 morning): Sabalenka 64% / Pegula 36%
sab_kal = 0.640

#   4. WinnersAndWhiners (Sep 10 8:13 AM ET): Sabalenka 1.55 / Pegula +160 (2.60)
p_sab_ww, p_peg_ww = 1.0/1.55, 1.0/2.60
sab_ww_m = p_sab_ww / (p_sab_ww + p_peg_ww)
sab_ww_p, _ = devig_power({"s": p_sab_ww, "p": p_peg_ww})

print("SF1 Sabalenka vs Pegula:")
print(f"  DK/CBS 5:01pm (-195/+158): Mult={sab_dk_m:.4f} | Shin={sab_dk_sh:.4f} | Power={sab_dk_p['s']:.4f}")
print(f"  RotoWire (-178/+170):      Mult={sab_rw_m:.4f} | Power={sab_rw_p['s']:.4f}")
print(f"  WinnersWhiners (1.55/2.6): Mult={sab_ww_m:.4f} | Power={sab_ww_p['s']:.4f}")
print(f"  Kalshi Sep 10:             {sab_kal:.4f}")
p_sab_sf = 0.45 * ((sab_dk_m + sab_dk_sh + sab_dk_p['s'])/3.0) + 0.35 * sab_kal + 0.10 * sab_rw_p['s'] + 0.10 * sab_ww_p['s']
print(f"  --> SF1 Consensus: Sabalenka = {p_sab_sf:.4f}, Pegula = {1-p_sab_sf:.4f}")

# SF2: Coco Gauff vs Elena Rybakina
#   1. CBS Sports / ActionNetwork / Pickswise (Sep 10 5:01 PM ET): Gauff -118 / Rybakina -103
p_gau_dk, p_ryb_dk = american_to_prob(-118), american_to_prob(-103)
gau_dk_m = p_gau_dk / (p_gau_dk + p_ryb_dk)
gau_dk_p, _ = devig_power({"g": p_gau_dk, "r": p_ryb_dk})

#   2. RotoWire: Gauff -108 / Rybakina +100
p_gau_rw, p_ryb_rw = american_to_prob(-108), american_to_prob(100)
gau_rw_m = p_gau_rw / (p_gau_rw + p_ryb_rw)

#   3. Kalshi (Sep 10 morning): Rybakina 52% / Gauff 48%
gau_kal = 0.480

#   4. WinnersAndWhiners (Sep 10 8:13 AM ET): Gauff -110 / Rybakina even (~51%)
gau_ww = 0.512

print("\nSF2 Gauff vs Rybakina:")
print(f"  DK/CBS 5:01pm (-118/-103): Mult={gau_dk_m:.4f} | Power={gau_dk_p['g']:.4f}")
print(f"  RotoWire (-108/+100):      Mult={gau_rw_m:.4f}")
print(f"  WinnersWhiners (-110/+100):{gau_ww:.4f}")
print(f"  Kalshi Sep 10:             Gauff {gau_kal:.4f} / Rybakina {1-gau_kal:.4f}")
p_gau_sf = 0.45 * gau_dk_p['g'] + 0.35 * gau_kal + 0.10 * gau_rw_m + 0.10 * gau_ww
print(f"  --> SF2 Consensus: Gauff = {p_gau_sf:.4f}, Rybakina = {1-p_gau_sf:.4f}")

# Kalshi Championship Market (Sep 10 morning): Sab 38%, Ryb 26%, Gauff 26%, Pegula 14% (sum = 104%)
kal_wta_raw = {"Aryna Sabalenka": 0.38, "Elena Rybakina": 0.26, "Coco Gauff": 0.26, "Jessica Pegula": 0.14}
kal_wta_mult = devig_mult(kal_wta_raw)
kal_wta_pow, _ = devig_power(kal_wta_raw)

# Exact 4-Player WTA Bracket Models calibrated to LIVE Sep 10 SF lines (Sab 63.8% / Peg 36.2%, Gauff 50.3% / Ryb 49.7%)
# AND DraftKings Sabalenka +150 title favorite (~36.5-37% devigged)!
# Wait: If Sabalenka has 63.8% SF win prob and ~35.5-36.5% title prob, her conditional Final win prob is:
#   36.0% / 63.8% = 56.4%!! (Makes total sense: 2x defending USO champ vs Gauff/Rybakina!)
#   - Model WTA_M1 (Market-Calibrated Final): Sab vs Gauff = 56.0%, Sab vs Rybakina = 56.5%, Peg vs Gauff = 39.0%, Peg vs Rybakina = 38.0%
#   - Model WTA_M2 (Balanced / Closer Final): Sab vs Gauff = 54.0%, Sab vs Rybakina = 55.0%, Peg vs Gauff = 40.0%, Peg vs Rybakina = 39.0%
wta_m1 = {
    ("Aryna Sabalenka", "Jessica Pegula"): p_sab_sf,
    ("Coco Gauff", "Elena Rybakina"): p_gau_sf,
    ("Aryna Sabalenka", "Coco Gauff"): 0.560,
    ("Aryna Sabalenka", "Elena Rybakina"): 0.565,
    ("Jessica Pegula", "Coco Gauff"): 0.390,
    ("Jessica Pegula", "Elena Rybakina"): 0.380,
}
_, wta_win_m1 = solve_4(("Aryna Sabalenka", "Jessica Pegula"), ("Coco Gauff", "Elena Rybakina"), wta_m1)

wta_m2 = {
    ("Aryna Sabalenka", "Jessica Pegula"): p_sab_sf,
    ("Coco Gauff", "Elena Rybakina"): p_gau_sf,
    ("Aryna Sabalenka", "Coco Gauff"): 0.540,
    ("Aryna Sabalenka", "Elena Rybakina"): 0.550,
    ("Jessica Pegula", "Coco Gauff"): 0.400,
    ("Jessica Pegula", "Elena Rybakina"): 0.390,
}
_, wta_win_m2 = solve_4(("Aryna Sabalenka", "Jessica Pegula"), ("Coco Gauff", "Elena Rybakina"), wta_m2)

# Check what Kalshi's title probs imply for Conditional Final win rates (using Kalshi's own SF 64/36 and 48/52!):
print("\nKalshi WTA Implied Conditional Final Win Probabilities (using Kalshi SF 64/36 & 48/52):")
kal_sf_wta = {"Aryna Sabalenka": 0.64, "Jessica Pegula": 0.36, "Coco Gauff": 0.48, "Elena Rybakina": 0.52}
for p in kal_wta_mult:
    print(f"  {p:18s}: Kal_Mult={kal_wta_mult[p]:.4f} / SF={kal_sf_wta[p]:.2f} => Cond Final={kal_wta_mult[p]/kal_sf_wta[p]:.4f}")

# Ensemble for Q2 (WTA Title — Thu Sep 10 pre-match):
#   35% Kalshi Sep 10 (avg Mult & Pow)
#   35% Exact Bracket M1 (using live DK 5:01pm + Kalshi SF lines, Sab +150 calibrated!)
#   30% Exact Bracket M2 (slightly flatter Finals, respecting Sabalenka's 2026 Slam hiccups & Noskova 3-setter)
wta_blend = {}
print(f"\n{'Player':18s} | {'Kal_M':6s} | {'Kal_P':6s} | {'M1_Br':6s} | {'M2_Br':6s} | {'BLEND':6s} | {'Prev09':6s} | {'Diff':6s}")
prev_wta = {"Aryna Sabalenka": 0.37, "Coco Gauff": 0.26, "Elena Rybakina": 0.25, "Jessica Pegula": 0.12}
for p in ["Aryna Sabalenka", "Coco Gauff", "Elena Rybakina", "Jessica Pegula"]:
    kal_avg = 0.5 * (kal_wta_mult[p] + kal_wta_pow[p])
    b = 0.35 * kal_avg + 0.35 * wta_win_m1[p] + 0.30 * wta_win_m2[p]
    wta_blend[p] = b
    print(f"{p:18s} | {kal_wta_mult[p]:6.4f} | {kal_wta_pow[p]:6.4f} | {wta_win_m1[p]:6.4f} | {wta_win_m2[p]:6.4f} | {b:6.4f} | {prev_wta[p]:6.4f} | {b - prev_wta[p]:+6.4f}")
print(f"Sum = {sum(wta_blend.values()):.4f}")
