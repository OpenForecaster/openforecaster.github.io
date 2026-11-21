import math
import random
from collections import Counter

# ==============================================================================
# CALIBRATED EXACT-BRACKET MODELS — FRIDAY AUG 28, 2026 (POST-DRAW)
# ==============================================================================
# Import brackets and devig functions from tennis_aug28_models
from tennis_aug28_models import (
    devig_mid, p_bo3, p_bo5,
    atp_bracket_raw, us_men_set, atp_base_elo,
    fd_atp_28, dk_atp_28, cz_atp_28, kalshi_atp_28,
    wta_bracket_raw, wta_base_elo, dk_wta_28,
)

def place_random_128(seed_names, unseeded_names, rng):
    """Official 32-seed Grand Slam random draw placement (for pre-draw calibration check)."""
    un = list(unseeded_names)
    rng.shuffle(un)
    b = [None] * 128
    b[0] = seed_names[0]
    b[127] = seed_names[1]
    s34 = list(seed_names[2:4]); rng.shuffle(s34)
    b[32], b[95] = s34[0], s34[1]
    s58 = list(seed_names[4:8]); rng.shuffle(s58)
    for pos, p in zip([31, 63, 64, 96], s58): b[pos] = p
    s912 = list(seed_names[8:12]); rng.shuffle(s912)
    for pos, p in zip([16, 48, 79, 111], s912): b[pos] = p
    s1316 = list(seed_names[12:16]); rng.shuffle(s1316)
    for pos, p in zip([15, 47, 80, 112], s1316): b[pos] = p
    s1724 = list(seed_names[16:24]); rng.shuffle(s1724)
    for pos, p in zip([8, 23, 40, 55, 72, 87, 104, 119], s1724): b[pos] = p
    s2532 = list(seed_names[24:32]); rng.shuffle(s2532)
    for pos, p in zip([7, 24, 39, 56, 71, 88, 103, 120], s2532): b[pos] = p
    ui = 0
    for i in range(128):
        if b[i] is None:
            b[i] = un[ui]; ui += 1
    return b


# ==============================================================================
# 1. WTA PRE-DRAW CALIBRATION -> EXACT FIXED-BRACKET DRAW EFFECT (Q1: 608158)
# ==============================================================================
wta_seeds_32 = [
    "Aryna Sabalenka", "Elena Rybakina", "Jessica Pegula", "Coco Gauff",
    "Mirra Andreeva", "Linda Noskova", "Karolina Muchova", "Iga Swiatek",
    "Elina Svitolina", "Amanda Anisimova", "Marta Kostyuk", "Belinda Bencic",
    "Naomi Osaka", "Iva Jovic", "Diana Shnaider", "Sorana Cirstea",
    "Alexandra Eala", "Ekaterina Alexandrova", "Jasmine Paolini", "Maja Chwalinska",
    "Anna Kalinskaya", "Madison Keys", "Elise Mertens", "Anastasia Potapova",
    "Marie Bouzkova", "Emma Navarro", "Barbora Krejcikova", "Sara Bejlek",
    "Ann Li", "Jelena Ostapenko", "Leylah Fernandez", "Maria Sakkari",
]
wta_unseeded = [p for p in wta_bracket_raw if p not in set(wta_seeds_32)]
assert len(wta_unseeded) == 96

# Calibrated WTA talent Elos (tuned so random-seed pre-draw matches Aug 26 multi-market:
# Sabalenka ~21.5%, Swiatek ~15.0%, Gauff ~14.5%, Osaka ~7.2%, Pegula ~5.6%, Andreeva ~5.4%,
# Rybakina ~6.0% post-Thu practice update [up from 4.5% pre-practice])!
wta_cal_elo = dict(wta_base_elo)
# Compress unseeded/lower-seed floor slightly (real WTA top-8 vs #60-128 gap is ~320-400 Elo!)
for p in wta_bracket_raw:
    if p not in wta_cal_elo:
        wta_cal_elo[p] = 1795.0
    elif wta_cal_elo[p] < 1920:
        wta_cal_elo[p] -= 40.0
    elif wta_cal_elo[p] < 1970:
        wta_cal_elo[p] -= 20.0

wta_cal_elo.update({
    "Aryna Sabalenka":   2185.0,
    "Iga Swiatek":       2148.0,
    "Coco Gauff":        2142.0,
    "Elena Rybakina":    2125.0, # healthy baseline (mixture below)
    "Naomi Osaka":       2062.0,
    "Jessica Pegula":    2038.0,
    "Mirra Andreeva":    2036.0,
    "Amanda Anisimova":  2018.0,
    "Marta Kostyuk":     2005.0,
    "Karolina Muchova":  1992.0,
    "Linda Noskova":     1985.0,
    "Alexandra Eala":    1985.0,
    "Belinda Bencic":    1982.0,
    "Madison Keys":      1978.0,
    "Elina Svitolina":   1972.0,
    "Qinwen Zheng":      1965.0,
})

def sim_wta(fixed=True, n_trials=60000, seed=7001):
    rng = random.Random(seed)
    # Rybakina Achilles health mixture (practiced Thu per AFP, retired Cinci QF, WD mixed):
    # Healthy 0.42 (2130), Mild 0.30 (2055), Compromised 0.18 (1955), WD/Retire 0.10 (1700)
    ryb_mix = [(2130.0, 0.42), (2055.0, 0.30), (1955.0, 0.18), (1700.0, 0.10)]
    # Sabalenka form/pressure variance (17-7 post-March vs 34-6 NY):
    sab_mix = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]

    tc = Counter(); fc = Counter(); sc = Counter()
    for re_e, wr in ryb_mix:
        for se_e, ws in sab_mix:
            w = wr * ws
            tr = max(1500, int(round(n_trials * w)))
            emap = dict(wta_cal_elo)
            emap["Elena Rybakina"] = re_e
            emap["Aryna Sabalenka"] = se_e
            pc = {}
            def gp(ea, eb):
                k = (ea, eb)
                v = pc.get(k)
                if v is None:
                    v = p_bo3(ea, eb)
                    pc[k] = v
                return v
            ltc = Counter(); lfc = Counter(); lsc = Counter()
            for _ in range(tr):
                cur = list(wta_bracket_raw) if fixed else place_random_128(wta_seeds_32, wta_unseeded, rng)
                rnd = 1
                while len(cur) > 1:
                    if rnd == 6:
                        for p in cur: lsc[p] += 1
                    elif rnd == 7:
                        for p in cur: lfc[p] += 1
                    nxt = []
                    for k in range(0, len(cur), 2):
                        a, b = cur[k], cur[k+1]
                        nxt.append(a if rng.random() < gp(emap[a], emap[b]) else b)
                    cur = nxt
                    rnd += 1
                ltc[cur[0]] += 1
            for p, c in ltc.items(): tc[p] += w * (c / tr)
            for p, c in lfc.items(): fc[p] += w * (c / tr)
            for p, c in lsc.items(): sc[p] += w * (c / tr)
    return tc, fc, sc

w_rand_t, _, _ = sim_wta(fixed=False, n_trials=45000, seed=7001)
w_fix_t, w_fix_f, w_fix_sf = sim_wta(fixed=True, n_trials=60000, seed=7002)

# DraftKings Post-Draw (Aug 28) devigged:
dk_w, dkw_ov, _, _ = devig_mid(dk_wta_28)

# Also construct Aug 26 Multi-Market (Poly $7M + Kalshi + FD + OT + GoBet) * Exact Draw Multiplier!
aug26_wta_prior = {
    "Aryna Sabalenka": 0.212,
    "Iga Swiatek":     0.148,
    "Coco Gauff":      0.138,
    "Naomi Osaka":     0.072,
    "Elena Rybakina":  0.060, # upgraded from 0.045 -> 0.060 upon Thu practice confirmation (AFP)
    "Jessica Pegula":  0.056,
    "Mirra Andreeva":  0.053,
    "Amanda Anisimova":0.034,
    "Marta Kostyuk":   0.025,
    "Karolina Muchova":0.030,
    "Linda Noskova":   0.026,
    "Alexandra Eala":  0.022,
    "Belinda Bencic":  0.020,
    "Madison Keys":    0.018,
    "Elina Svitolina": 0.016,
}
wta_prior_shifted = {}
for p, pr in aug26_wta_prior.items():
    mult = w_fix_t[p] / max(1e-6, w_rand_t[p])
    wta_prior_shifted[p] = pr * mult

# Final Q1 (608158) Blend:
# 45% Post-Draw DraftKings (Aug 28) + 35% Aug-26 Multi-Market * Exact Draw Multiplier + 20% Exact Fixed-Bracket MC
print("=== Q1 (608158) CALIBRATED WTA POST-DRAW ANALYSIS (FRI AUG 28) ===")
print(f"{'Player':20s} | {'RandMC':6s} | {'FixMC':6s} | {'DrawX':5s} | {'Pr*DX':6s} | {'DK_28':6s} | {'FINAL':6s} | {'SF%':5s}")
wta_blend_final = {}
for p in aug26_wta_prior:
    val = 0.45 * dk_w.get(p, 0.0) + 0.35 * wta_prior_shifted[p] + 0.20 * w_fix_t[p]
    wta_blend_final[p] = val
for p, v in sorted(wta_blend_final.items(), key=lambda x: -x[1])[:12]:
    dx = w_fix_t[p] / max(1e-6, w_rand_t[p])
    print(f"{p:20s} | {w_rand_t[p]:6.4f} | {w_fix_t[p]:6.4f} | {dx:5.2f} | {wta_prior_shifted[p]:6.4f} | {dk_w.get(p,0):6.4f} | {v:6.4f} | {w_fix_sf[p]:5.3f}")
top7_w = sorted(wta_blend_final.items(), key=lambda x: -x[1])[:7]
print("WTA Top-7:", [(k, round(v, 4)) for k, v in top7_w])
print("WTA Top-5 sum:", round(sum(v for _, v in top7_w[:5]), 4))


# ==============================================================================
# 2. ATP MARKET-CALIBRATED FIXED-BRACKET MODEL (Q3: 891014 & Q2: 408930)
# ==============================================================================
# Tune Elos so Fixed-Bracket BO5 MC matches Post-Draw Sharp Consensus (Kalshi + FD + DK):
#   Alcaraz ~25.5%, Zverev ~22.0%, Djokovic ~10.5%, Fils ~6.3%, Fritz ~6.2%, Shelton ~5.5%, Jodar ~5.2%
atp_mkt_elo = dict(atp_base_elo)
atp_mkt_elo.update({
    "Alexander Zverev": 2166,  # Matches ~22.0% in soft top half!
    "Arthur Fils":      2084,  # Matches ~6.3% in tough Q4
    "Ben Shelton":      2082,  # Matches ~5.5% in tough Q4 (notice Shelton ≈ Fils talent!)
    "Taylor Fritz":     2048,  # Matches ~6.2% in soft Q2! (Crucial: tests lower Fritz talent!)
    "Rafael Jodar":     2056,  # Matches ~5.2% in Q1
    "Felix Auger-Aliassime": 2015,
    "Frances Tiafoe":   1998,
    "Brandon Nakashima":1992,
    "Tommy Paul":       1984,
    "Learner Tien":     1976,
    "Daniil Medvedev":  2002,
    "Flavio Cobolli":   1998,
    "Jakub Mensik":     2002,
    "Alex de Minaur":   1984,
})

def sim_atp_cal(elo_dict, alc_shift=0.0, djo_shift=0.0, n_trials=50000, seed=8001):
    rng = random.Random(seed)
    elos_base = [1830.0 if nm.startswith("Q_") else float(elo_dict.get(nm, 1840.0)) for nm in atp_bracket_raw]
    alc_idx = atp_bracket_raw.index("Carlos Alcaraz")
    djo_idx = atp_bracket_raw.index("Novak Djokovic")
    tia_idx = atp_bracket_raw.index("Frances Tiafoe")
    us_idxs = {i for i, nm in enumerate(atp_bracket_raw) if nm in us_men_set}

    alc_mix = [(2280+alc_shift, 0.30), (2175+alc_shift, 0.44), (2045+alc_shift, 0.22), (1750, 0.04)]
    djo_mix = [(2135+djo_shift, 0.55), (2075+djo_shift, 0.30), (1985+djo_shift, 0.15)]
    tia_mix = [(0, 0.78), (-35, 0.16), (-95, 0.06)]

    tc = Counter(); r4c = Counter(); qfc = Counter(); sfc = Counter()
    uncond_us = Counter(); tie_rate = 0.0
    for ae, wa in alc_mix:
        for de, wd in djo_mix:
            for td, wt in tia_mix:
                w = wa * wd * wt
                tr = max(600, int(round(n_trials * w)))
                elos = list(elos_base)
                elos[alc_idx] = float(ae)
                elos[djo_idx] = float(de)
                elos[tia_idx] = elos_base[tia_idx] + float(td)
                pc = {}
                def gp(i, j):
                    k = (elos[i], elos[j])
                    v = pc.get(k)
                    if v is None:
                        v = p_bo5(elos[i], elos[j])
                        pc[k] = v
                    return v
                ltc = Counter(); lr4 = Counter(); lqf = Counter(); lsf = Counter()
                luc = Counter(); ties = 0
                for _ in range(tr):
                    cur = list(range(128))
                    best_rnd = 0; best_us = []
                    rnd = 1
                    while len(cur) > 1:
                        if rnd == 4:
                            for p in cur: lr4[p] += 1
                        elif rnd == 5:
                            for p in cur: lqf[p] += 1
                        elif rnd == 6:
                            for p in cur: lsf[p] += 1
                        nxt = []
                        for k in range(0, len(cur), 2):
                            a, b = cur[k], cur[k+1]
                            if rng.random() < gp(a, b): win, los = a, b
                            else: win, los = b, a
                            nxt.append(win)
                            if los in us_idxs:
                                if rnd > best_rnd:
                                    best_rnd = rnd; best_us = [los]
                                elif rnd == best_rnd:
                                    best_us.append(los)
                        cur = nxt; rnd += 1
                    champ = cur[0]; ltc[champ] += 1
                    if champ in us_idxs:
                        best_rnd = 8; best_us = [champ]
                    if len(best_us) == 1: luc[best_us[0]] += 1
                    else: ties += 1
                for p, c in ltc.items(): tc[atp_bracket_raw[p]] += w * (c / tr)
                for p, c in lr4.items(): r4c[atp_bracket_raw[p]] += w * (c / tr)
                for p, c in lqf.items(): qfc[atp_bracket_raw[p]] += w * (c / tr)
                for p, c in lsf.items(): sfc[atp_bracket_raw[p]] += w * (c / tr)
                for p, c in luc.items(): uncond_us[atp_bracket_raw[p]] += w * (c / tr)
                tie_rate += w * (ties / tr)
    cond_us = {nm: v / (1.0 - tie_rate) for nm, v in uncond_us.items()}
    return tc, r4c, qfc, sfc, cond_us, uncond_us, tie_rate

# Run 3 calibrated ATP regimes:
# A: Market-Implied Exact Fixed-Bracket (Fritz 2048, Shelton 2082, Fils 2084, Zverev 2166) -> matches Kalshi/FD/DK!
# B: Pre-Draw Talent Exact Fixed-Bracket (Fritz 2062, Shelton 2084, Fils 2078, Zverev 2158)
# C: BO5/NY Pedigree (Fritz 2070, Shelton 2072, Tiafoe 2012, Paul 1998, Nakashima 1988, Tien 1966)
regimes_cal = [
    ("Market-Implied Exact-Bracket", 0.50, atp_mkt_elo),
    ("Pre-Draw Talent Exact-Bracket", 0.30, {**atp_mkt_elo, "Taylor Fritz": 2062, "Ben Shelton": 2084, "Arthur Fils": 2078, "Alexander Zverev": 2158}),
    ("BO5/NY Pedigree Exact-Bracket", 0.20, {**atp_mkt_elo, "Taylor Fritz": 2070, "Ben Shelton": 2072, "Frances Tiafoe": 2012, "Tommy Paul": 1998, "Brandon Nakashima": 1988, "Learner Tien": 1966, "Arthur Fils": 2068}),
]

b_tc = Counter(); b_r4 = Counter(); b_qf = Counter(); b_sf = Counter()
b_cond = Counter(); b_uncond = Counter(); b_tie = 0.0
print("\n=== CALIBRATED EXACT-BRACKET ATP MC ===")
for idx, (lbl, w, ed) in enumerate(regimes_cal):
    tc, r4c, qfc, sfc, cu, uu, tr = sim_atp_cal(ed, n_trials=45000, seed=8100 + idx)
    b_tie += w * tr
    for k, v in tc.items(): b_tc[k] += w * v
    for k, v in r4c.items(): b_r4[k] += w * v
    for k, v in qfc.items(): b_qf[k] += w * v
    for k, v in sfc.items(): b_sf[k] += w * v
    for k, v in cu.items(): b_cond[k] += w * v
    for k, v in uu.items(): b_uncond[k] += w * v
    print(f"  [{w:.2f}] {lbl}:")
    print("    Title:", [(k, round(v, 3)) for k, v in tc.most_common(7)])
    print(f"    US Cond (tie={tr:.3f}):", [(k, round(v, 3)) for k, v in sorted(cu.items(), key=lambda x: -x[1])[:6]])

# Recompute Q3 (891014) final blend using calibrated MC:
fd_m, _, _, _ = devig_mid(fd_atp_28)
dk_m, _, _, _ = devig_mid(dk_atp_28)
cz_m, _, _, _ = devig_mid(cz_atp_28)

atp_final_cal = {}
for k in fd_atp_28:
    if k == "Field_Rest": continue
    bks = 0.45 * fd_m[k] + 0.40 * dk_m[k] + 0.15 * cz_m[k]
    atp_final_cal[k] = 0.45 * kalshi_atp_28[k] + 0.30 * bks + 0.25 * b_tc.get(k, 0.0)

print("\n=== Q3 (891014) CALIBRATED FINAL BLEND — FRI AUG 28 ===")
print(f"{'Player':22s} | {'Kal28':6s} | {'Books':6s} | {'CalMC':6s} | {'FINAL':6s}")
for k, v in sorted(atp_final_cal.items(), key=lambda x: -x[1])[:9]:
    bks = 0.45 * fd_m[k] + 0.40 * dk_m[k] + 0.15 * cz_m[k]
    print(f"{k:22s} | {kalshi_atp_28[k]:6.4f} | {bks:6.4f} | {b_tc.get(k,0):6.4f} | {v:6.4f}")

print(f"\n=== Q2 (408930) CALIBRATED FURTHEST U.S. MAN — FRI AUG 28 (Tie={b_tie:.4f}) ===")
print(f"{'Player':22s} | {'Cond':7s} | {'Uncond':7s} | {'R4%':6s} | {'QF%':6s} | {'SF%':6s} | {'Win%':6s}")
for k, v in sorted(b_cond.items(), key=lambda x: -x[1])[:8]:
    print(f"{k:22s} | {v:7.4f} | {b_uncond[k]:7.4f} | {b_r4[k]:6.3f} | {b_qf[k]:6.3f} | {b_sf[k]:6.3f} | {b_tc[k]:6.4f}")
