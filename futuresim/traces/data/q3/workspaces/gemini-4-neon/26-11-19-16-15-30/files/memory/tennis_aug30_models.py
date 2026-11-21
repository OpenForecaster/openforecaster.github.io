import math
import random
from collections import Counter

from tennis_aug28_models import (
    devig_mid, p_bo3, p_bo5,
    atp_bracket_raw, us_men_set, atp_base_elo,
    fd_atp_28, dk_atp_28, cz_atp_28, kalshi_atp_28,
    wta_bracket_raw, wta_base_elo, dk_wta_28,
)

# Exact calibrated Elos from tennis_aug28_calibrated.py (copied to avoid re-running top-level sims)
wta_cal_elo = dict(wta_base_elo)
for _p in wta_bracket_raw:
    if _p not in wta_cal_elo:
        wta_cal_elo[_p] = 1795.0
    elif wta_cal_elo[_p] < 1920:
        wta_cal_elo[_p] -= 40.0
    elif wta_cal_elo[_p] < 1970:
        wta_cal_elo[_p] -= 20.0
wta_cal_elo.update({
    "Aryna Sabalenka":   2185.0,
    "Iga Swiatek":       2148.0,
    "Coco Gauff":        2142.0,
    "Elena Rybakina":    2125.0,
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

atp_mkt_elo = dict(atp_base_elo)
atp_mkt_elo.update({
    "Alexander Zverev": 2166,
    "Arthur Fils":      2084,
    "Ben Shelton":      2082,
    "Taylor Fritz":     2048,
    "Rafael Jodar":     2056,
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

# ==============================================================================
# DAY 1 (SUNDAY AUG 30, 2026) CONDITIONAL EXACT-BRACKET SIMULATIONS
# ==============================================================================

# 1. WTA CONFIRMED DAY 1 R1 WINNERS (pairs -> winner)
wta_r1_locked = {
    ("Jessica Pegula", "Elena-Gabriela Ruse"): "Jessica Pegula",          # 6-3, 6-2
    ("Kamilla Rakhimova", "Barbora Krejcikova"): "Kamilla Rakhimova",     # 7-6(4), 6-2 (Sabalenka R3!)
    ("Marta Kostyuk", "Storm Hunter"): "Marta Kostyuk",                   # 6-4, 6-1
    ("Talia Gibson", "Donna Vekic"): "Donna Vekic",                       # 6-2, 4-6, 6-3
    ("Shuai Zhang", "Leylah Fernandez"): "Leylah Fernandez",              # 6-3, 6-2
    ("Jasmine Paolini", "Veronika Erjavec"): "Jasmine Paolini",           # 6-3, 3-6, 6-4
    ("Lucrezia Stefanini", "Dayana Yastremska"): "Lucrezia Stefanini",    # 6-3, 4-6, 6-1
}

# Verify all locked WTA pairs exist in wta_bracket_raw
wta_pairs = [(wta_bracket_raw[i], wta_bracket_raw[i+1]) for i in range(0, 128, 2)]
for pair in wta_r1_locked:
    assert pair in wta_pairs, f"WTA pair not found: {pair}"


def sim_wta_cond(locked_r1=None, ryb_mix=None, elo_adj=None, n_trials=80000, seed=9001):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    if ryb_mix is None:
        # Aug 28 baseline mixture
        ryb_mix = [(2130.0, 0.42), (2055.0, 0.30), (1955.0, 0.18), (1700.0, 0.10)]
    sab_mix = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]

    tc = Counter(); fc = Counter(); sc = Counter()
    for re_e, wr in ryb_mix:
        for se_e, ws in sab_mix:
            w = wr * ws
            tr = max(2000, int(round(n_trials * w)))
            emap = dict(wta_cal_elo)
            if elo_adj:
                emap.update(elo_adj)
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
                cur = list(wta_bracket_raw)
                rnd = 1
                while len(cur) > 1:
                    if rnd == 6:
                        for p in cur: lsc[p] += 1
                    elif rnd == 7:
                        for p in cur: lfc[p] += 1
                    nxt = []
                    for k in range(0, len(cur), 2):
                        a, b = cur[k], cur[k+1]
                        if rnd == 1 and (a, b) in locked_r1:
                            nxt.append(locked_r1[(a, b)])
                        else:
                            nxt.append(a if rng.random() < gp(emap[a], emap[b]) else b)
                    cur = nxt
                    rnd += 1
                ltc[cur[0]] += 1
            for p, c in ltc.items(): tc[p] += w * (c / tr)
            for p, c in lfc.items(): fc[p] += w * (c / tr)
            for p, c in lsc.items(): sc[p] += w * (c / tr)
    return tc, fc, sc


# Aug 28 baseline WTA (matches tennis_aug28_calibrated.py)
w28_t, w28_f, w28_sf = sim_wta_cond(locked_r1=None, n_trials=80000, seed=9001)

# Aug 30 Scenario A: Day 1 results ONLY (Rybakina unchanged)
w30_res_only, _, _ = sim_wta_cond(locked_r1=wta_r1_locked, n_trials=80000, seed=9002)

# Aug 30 Scenario B: Day 1 results + Rybakina conservative health update ("all good", practiced, confident)
ryb_mix_cons = [(2130.0, 0.52), (2065.0, 0.28), (1970.0, 0.14), (1740.0, 0.06)]
w30_cons, w30_cons_f, w30_cons_sf = sim_wta_cond(
    locked_r1=wta_r1_locked,
    ryb_mix=ryb_mix_cons,
    elo_adj={"Jessica Pegula": wta_cal_elo["Jessica Pegula"] + 6.0}, # tiny positive form signal (92% 1st serve)
    n_trials=80000, seed=9003
)

# Aug 30 Scenario C: Day 1 results + Rybakina moderate-bullish health update
ryb_mix_mod = [(2135.0, 0.58), (2070.0, 0.26), (1975.0, 0.12), (1740.0, 0.04)]
w30_mod, _, _ = sim_wta_cond(
    locked_r1=wta_r1_locked,
    ryb_mix=ryb_mix_mod,
    elo_adj={"Jessica Pegula": wta_cal_elo["Jessica Pegula"] + 10.0},
    n_trials=80000, seed=9004
)

# Aug 28 final unrounded posterior from tennis_aug28_calibrated.py
# Let's reproduce exact Aug 28 final posterior
w_rand_28 = Counter()
rng_r = random.Random(7001)
# Use exact ratios from Aug 28 calibrated run:
# Let's anchor directly to Aug 28 exact blend values:
aug28_wta_exact = {
    "Aryna Sabalenka":  0.221,
    "Coco Gauff":       0.140,
    "Iga Swiatek":      0.134,
    "Naomi Osaka":      0.064,
    "Elena Rybakina":   0.063,
    "Jessica Pegula":   0.058,
    "Mirra Andreeva":   0.049,
    "Amanda Anisimova": 0.037,
    "Marta Kostyuk":    0.031,
    "Karolina Muchova": 0.027,
    "Linda Noskova":    0.024,
    "Alexandra Eala":   0.021,
    "Belinda Bencic":   0.017,
    "Madison Keys":     0.015,
    "Elina Svitolina":  0.015,
}

print("=" * 92)
print("Q1 (608158) WOMEN'S SINGLES — SUN AUG 30 DAY 1 BAYESIAN UPDATE")
print("=" * 92)
print(f"{'Player':20s} | {'MC28':6s} | {'MC30_R':6s} | {'MC30_C':6s} | {'MC30_M':6s} | {'Post28':6s} | {'Upd_R':6s} | {'Upd_C':6s} | {'Upd_M':6s}")
upd_c_map = {}
upd_m_map = {}
for p, p28 in sorted(aug28_wta_exact.items(), key=lambda x: -x[1]):
    r_res = w30_res_only[p] / max(1e-6, w28_t[p])
    r_con = w30_cons[p] / max(1e-6, w28_t[p])
    r_mod = w30_mod[p] / max(1e-6, w28_t[p])
    u_r = p28 * r_res
    u_c = p28 * r_con
    u_m = p28 * r_mod
    upd_c_map[p] = u_c
    upd_m_map[p] = u_m
    print(f"{p:20s} | {w28_t[p]:6.4f} | {w30_res_only[p]:6.4f} | {w30_cons[p]:6.4f} | {w30_mod[p]:6.4f} | {p28:6.4f} | {u_r:6.4f} | {u_c:6.4f} | {u_m:6.4f}")

print("\nWTA Top-7 (Conservative Rybakina + Day 1):", [(k, round(v, 4)) for k, v in sorted(upd_c_map.items(), key=lambda x: -x[1])[:7]])
print("WTA Top-7 (Moderate Rybakina + Day 1):    ", [(k, round(v, 4)) for k, v in sorted(upd_m_map.items(), key=lambda x: -x[1])[:7]])


# ==============================================================================
# 2. ATP CONFIRMED DAY 1 RESULTS & WITHDRAWALS (Q3: 891014 & Q2: 408930)
# ==============================================================================
atp_bracket_30 = list(atp_bracket_raw)
# Replace withdrawn players & identified qualifiers
atp_bracket_30[atp_bracket_30.index("Casper Ruud")] = "Arthur Gea"       # LL replacing #19 Ruud (back)
atp_bracket_30[atp_bracket_30.index("Marin Cilic")] = "Otto Virtanen"    # LL replacing Cilic (injury)
atp_bracket_30[atp_bracket_30.index("Q_12")] = "Hugo Gaston"
atp_bracket_30[atp_bracket_30.index("Q_18")] = "Coleman Wong"
atp_bracket_30[atp_bracket_30.index("Q_17")] = "Lloyd Harris"
atp_bracket_30[atp_bracket_30.index("Q_14")] = "Federico Cina"
atp_bracket_30[atp_bracket_30.index("Q_15")] = "Jacob Fearnley"

atp_r1_locked = {
    ("Daniil Medvedev", "Hugo Gaston"): "Daniil Medvedev",                # 6-4, 6-2, 6-4
    ("Coleman Wong", "Tommy Paul"): "Tommy Paul",                         # 6-7, 6-1, 6-3, 6-3
    ("Jiri Lehecka", "Pablo Carreno Busta"): "Jiri Lehecka",              # 6-1, 7-6, 4-6, 6-2
    ("Luca Van Assche", "Cameron Norrie"): "Luca Van Assche",             # 6-7, 6-2, 6-2, 6-3
    ("Kamil Majchrzak", "Hamad Medjedovic"): "Kamil Majchrzak",           # 6-3, 6-3, 6-3
    ("Yibing Wu", "Adam Walton"): "Yibing Wu",                            # 7-6, 6-2, 7-5
    ("Lloyd Harris", "Jack Kennedy"): "Lloyd Harris",                     # 6-4, 6-2, 6-2
}

atp_pairs_30 = [(atp_bracket_30[i], atp_bracket_30[i+1]) for i in range(0, 128, 2)]
for pair in atp_r1_locked:
    assert pair in atp_pairs_30, f"ATP pair not found: {pair}"

extra_atp_elo = {
    "Arthur Gea":     1815.0,
    "Otto Virtanen":  1840.0,
    "Hugo Gaston":    1835.0,
    "Coleman Wong":   1855.0, # 13-5 NA hard swing, took set 1 off Paul
    "Lloyd Harris":   1855.0, # experienced hard-courter, beat Jack Kennedy
    "Federico Cina":  1825.0,
    "Jacob Fearnley": 1850.0,
}


def sim_atp_cond(bracket, elo_dict, locked_r1=None, med_boost=0.0, paul_boost=0.0, n_trials=60000, seed=9100):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    elos_base = []
    for nm in bracket:
        if nm.startswith("Q_"):
            el = 1830.0
        elif nm in elo_dict:
            el = float(elo_dict[nm])
        elif nm in extra_atp_elo:
            el = float(extra_atp_elo[nm])
        else:
            el = 1840.0
        elos_base.append(el)
    if med_boost:
        elos_base[bracket.index("Daniil Medvedev")] += med_boost
    if paul_boost:
        elos_base[bracket.index("Tommy Paul")] += paul_boost

    alc_idx = bracket.index("Carlos Alcaraz")
    djo_idx = bracket.index("Novak Djokovic")
    tia_idx = bracket.index("Frances Tiafoe")
    us_idxs = {i for i, nm in enumerate(bracket) if nm in us_men_set}

    alc_mix = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
    djo_mix = [(2135.0, 0.55), (2075.0, 0.30), (1985.0, 0.15)]
    tia_mix = [(0.0, 0.78), (-35.0, 0.16), (-95.0, 0.06)]

    # Pre-index locked R1 pairs by slot index
    locked_slots = {}
    for k in range(0, 128, 2):
        pair = (bracket[k], bracket[k+1])
        if pair in locked_r1:
            wname = locked_r1[pair]
            locked_slots[k] = k if wname == bracket[k] else k + 1

    tc = Counter(); r4c = Counter(); qfc = Counter(); sfc = Counter()
    uncond_us = Counter(); tie_rate = 0.0
    for ae, wa in alc_mix:
        for de, wd in djo_mix:
            for td, wt in tia_mix:
                w = wa * wd * wt
                tr = max(800, int(round(n_trials * w)))
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
                            if rnd == 1 and k in locked_slots:
                                win = locked_slots[k]
                                los = b if win == a else a
                            else:
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
                for p, c in ltc.items(): tc[bracket[p]] += w * (c / tr)
                for p, c in lr4.items(): r4c[bracket[p]] += w * (c / tr)
                for p, c in lqf.items(): qfc[bracket[p]] += w * (c / tr)
                for p, c in lsf.items(): sfc[bracket[p]] += w * (c / tr)
                for p, c in luc.items(): uncond_us[bracket[p]] += w * (c / tr)
                tie_rate += w * (ties / tr)
    cond_us = {nm: v / (1.0 - tie_rate) for nm, v in uncond_us.items()}
    return tc, r4c, qfc, sfc, cond_us, uncond_us, tie_rate


regimes_cal = [
    ("Market-Implied", 0.50, atp_mkt_elo),
    ("Pre-Draw Talent", 0.30, {**atp_mkt_elo, "Taylor Fritz": 2062, "Ben Shelton": 2084, "Arthur Fils": 2078, "Alexander Zverev": 2158}),
    ("BO5/NY Pedigree", 0.20, {**atp_mkt_elo, "Taylor Fritz": 2070, "Ben Shelton": 2072, "Frances Tiafoe": 2012, "Tommy Paul": 1998, "Brandon Nakashima": 1988, "Learner Tien": 1966, "Arthur Fils": 2068}),
]

def run_blend(bracket, locked, med_boost=0.0, paul_boost=0.0, seed_base=9100):
    b_tc = Counter(); b_r4 = Counter(); b_qf = Counter(); b_sf = Counter()
    b_cond = Counter(); b_uncond = Counter(); b_tie = 0.0
    for idx, (lbl, w, ed) in enumerate(regimes_cal):
        tc, r4c, qfc, sfc, cu, uu, tr = sim_atp_cond(
            bracket, ed, locked_r1=locked, med_boost=med_boost, paul_boost=paul_boost,
            n_trials=50000, seed=seed_base + idx
        )
        b_tie += w * tr
        for k, v in tc.items(): b_tc[k] += w * v
        for k, v in r4c.items(): b_r4[k] += w * v
        for k, v in qfc.items(): b_qf[k] += w * v
        for k, v in sfc.items(): b_sf[k] += w * v
        for k, v in cu.items(): b_cond[k] += w * v
        for k, v in uu.items(): b_uncond[k] += w * v
    return b_tc, b_r4, b_qf, b_sf, b_cond, b_uncond, b_tie

# Baseline Aug 28 (exact)
m28_tc, m28_r4, m28_qf, m28_sf, m28_cu, m28_uu, m28_tie = run_blend(atp_bracket_raw, None, 0.0, 0.0, 9100)
# Aug 30 Day 1 locked + withdrawals (no form Elo tweaks)
m30_tc, m30_r4, m30_qf, m30_sf, m30_cu, m30_uu, m30_tie = run_blend(atp_bracket_30, atp_r1_locked, 0.0, 0.0, 9200)
# Aug 30 Day 1 locked + withdrawals + modest Medvedev form recovery (+12 Elo after clean 3-0 win)
m30f_tc, m30f_r4, m30f_qf, m30f_sf, m30f_cu, m30f_uu, m30f_tie = run_blend(atp_bracket_30, atp_r1_locked, 12.0, 5.0, 9300)

# Q3 (891014) Bayesian update from Aug 28 market-calibrated posterior
fd_m, _, _, _ = devig_mid(fd_atp_28)
dk_m, _, _, _ = devig_mid(dk_atp_28)
cz_m, _, _, _ = devig_mid(cz_atp_28)
aug28_atp_exact = {}
for k in fd_atp_28:
    if k == "Field_Rest": continue
    bks = 0.45 * fd_m[k] + 0.40 * dk_m[k] + 0.15 * cz_m[k]
    aug28_atp_exact[k] = 0.45 * kalshi_atp_28[k] + 0.30 * bks + 0.25 * m28_tc.get(k, 0.0)

print("\n" + "=" * 92)
print("Q3 (891014) MEN'S SINGLES — SUN AUG 30 DAY 1 BAYESIAN UPDATE")
print("=" * 92)
print(f"{'Player':22s} | {'MC28':6s} | {'MC30':6s} | {'MC30F':6s} | {'Post28':6s} | {'Upd30':6s} | {'Upd30F':6s}")
for k, p28 in sorted(aug28_atp_exact.items(), key=lambda x: -x[1])[:12]:
    r1 = m30_tc.get(k, 0.0) / max(1e-6, m28_tc.get(k, 0.0))
    r2 = m30f_tc.get(k, 0.0) / max(1e-6, m28_tc.get(k, 0.0))
    print(f"{k:22s} | {m28_tc.get(k,0):6.4f} | {m30_tc.get(k,0):6.4f} | {m30f_tc.get(k,0):6.4f} | {p28:6.4f} | {p28*r1:6.4f} | {p28*r2:6.4f}")

print("\n" + "=" * 92)
print(f"Q2 (408930) FURTHEST U.S. MAN — SUN AUG 30 DAY 1 UPDATE (Tie: {m28_tie:.4f} -> {m30_tie:.4f})")
print("=" * 92)
print(f"{'Player':22s} | {'Cond28':7s} | {'Cond30':7s} | {'Cond30F':7s} | {'Delta':7s} | {'R4_30':6s} | {'QF_30':6s} | {'SF_30':6s}")
for k, _ in sorted(m30_cu.items(), key=lambda x: -x[1])[:9]:
    c28 = m28_cu.get(k, 0.0)
    c30 = m30_cu.get(k, 0.0)
    c30f = m30f_cu.get(k, 0.0)
    print(f"{k:22s} | {c28:7.4f} | {c30:7.4f} | {c30f:7.4f} | {c30-c28:+7.4f} | {m30_r4[k]:6.3f} | {m30_qf[k]:6.3f} | {m30_sf[k]:6.3f}")
