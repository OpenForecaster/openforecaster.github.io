import math
import random
from collections import Counter

from tennis_aug28_models import (
    devig_mid, p_bo3, p_bo5,
    atp_bracket_raw, atp_base_elo,
    fd_atp_28, dk_atp_28, cz_atp_28, kalshi_atp_28,
    wta_bracket_raw, wta_base_elo, dk_wta_28,
)
from tennis_sep06_models import (
    wta_cal_elo, atp_mkt_elo, aug28_wta_exact,
    atp_bracket_04, us_men_04, us_men_28, extra_atp_elo,
    atp_r1_locked, atp_r2_locked, atp_r3_locked,
    wta_r1_locked, wta_r2_locked, wta_r3_locked,
    regimes_cal, sim_atp, run_atp_blend, sim_wta,
    aug28_named, field_28, w_field_28,
)

# ==============================================================================
# DAY 9 (MONDAY SEP 7, 2026, ~22:30 GMT / 6:30 PM ET) STANDALONE BAYES MC
# Batch: tennis (891014 ATP Title, 408930 Furthest U.S. Man, 608158 WTA Title)
#
# ATP LOCKED R4 (5/8):
#   - Sun Sep 6: Alcaraz d. Paul 6-4 6-3 6-4, Tiafoe d. Medvedev 7-6 6-4 7-6,
#                Michelsen d. Etcheverry 7-6 6-4 6-4, Shelton d. Tsitsipas 6-2 6-3 6-4!
#   - Mon Sep 7: #28 Alexander Blockx d. #24 Francisco Cerundolo 6-3 4-6 7-5 7-5!
# ATP PENDING R4 (3/8, live Betano Sep 7 odds):
#   - Zverev vs Darderi (Betano 1.07/8.00 -> 91.3% Zverev!)
#   - BVDZ vs Arthur Gea (Betano 1.57/2.40 -> 61.2% BVDZ!)
#   - Learner Tien vs Karen Khachanov (Betano 1.53/2.50 -> 62.9% Tien!)
# ATP LOCKED QFs (live Betano/DK/TAB Sep 7 odds):
#   - Tiafoe vs Michelsen (Betano 1.63/2.25, DK -156/+127, TAB 1.66/2.20 -> 58.2% Tiafoe!)
#   - Alcaraz vs Shelton (Betano 1.27/3.70 -> 76.3% Alcaraz / 23.7% Shelton!)
#
# WTA LOCKED R4 (7/8):
#   - Sun Sep 6: Sabalenka d. Townsend 6-4 6-3, Noskova d. Kostyuk 7-5 5-7 6-4,
#                Pegula d. Cirstea 6-3 6-4, Navarro d. Kalinskaya 6-4 6-2!
#   - Mon Sep 7: Andreeva d. Potapova 5-7 6-4 6-3,
#                Qinwen Zheng d. Iga Swiatek 7-5 6-3 (HUGE UPSET! SWIATEK OUT!),
#                Elena Rybakina d. Naomi Osaka 6-1 6-4 (66 min! OSAKA OUT!)
# WTA PENDING R4 (1/8, live Kalshi Sep 7 odds):
#   - Coco Gauff vs Iva Jovic (Kalshi 74/28 -> 73.1% Gauff / 26.9% Jovic!)
# WTA LOCKED QFs (live Kalshi/DK Sep 7 odds):
#   - Sabalenka vs Noskova (Kalshi 70/30, DK -267/+212 -> 70.3% Sabalenka!)
#   - Pegula vs Navarro (Kalshi 79/21, 4-0 H2H -> 79.0% Pegula!)
#   - Rybakina vs Qinwen Zheng (Wed QF)
#   - Mirra Andreeva vs Gauff/Jovic (Wed QF)
# ==============================================================================

# Build Day 9 R4 locks
atp_r4_winners_07 = {
    "Alexander Blockx", "Frances Tiafoe", "Alex Michelsen", "Ben Shelton", "Carlos Alcaraz",
}
atp_r4_locked_07 = {}
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
    if r3a in atp_r4_winners_07:
        atp_r4_locked_07[(r3a, r3b)] = r3a
    elif r3b in atp_r4_winners_07:
        atp_r4_locked_07[(r3a, r3b)] = r3b
assert len(atp_r4_locked_07) == 5, len(atp_r4_locked_07)

wta_r4_winners_07 = {
    "Aryna Sabalenka", "Linda Noskova", "Jessica Pegula", "Emma Navarro",
    "Mirra Andreeva", "Qinwen Zheng", "Elena Rybakina",
}
wta_r4_locked_07 = {}
for i in range(0, 128, 16):
    r3a = wta_r3_locked[(
        wta_r2_locked[(wta_r1_locked[(wta_bracket_raw[i], wta_bracket_raw[i+1])],
                       wta_r1_locked[(wta_bracket_raw[i+2], wta_bracket_raw[i+3])])],
        wta_r2_locked[(wta_r1_locked[(wta_bracket_raw[i+4], wta_bracket_raw[i+5])],
                       wta_r1_locked[(wta_bracket_raw[i+6], wta_bracket_raw[i+7])])]
    )]
    r3b = wta_r3_locked[(
        wta_r2_locked[(wta_r1_locked[(wta_bracket_raw[i+8], wta_bracket_raw[i+9])],
                       wta_r1_locked[(wta_bracket_raw[i+10], wta_bracket_raw[i+11])])],
        wta_r2_locked[(wta_r1_locked[(wta_bracket_raw[i+12], wta_bracket_raw[i+13])],
                       wta_r1_locked[(wta_bracket_raw[i+14], wta_bracket_raw[i+15])])]
    )]
    if r3a in wta_r4_winners_07: wta_r4_locked_07[(r3a, r3b)] = r3a
    elif r3b in wta_r4_winners_07: wta_r4_locked_07[(r3a, r3b)] = r3b
assert len(wta_r4_locked_07) == 7, len(wta_r4_locked_07)

# ==============================================================================
# PART 1: ATP DAY 9 MODELS
# ==============================================================================
m28_tc, _, _, _, _, m28_cu, _, _, m28_tie = run_atp_blend(
    atp_bracket_raw, us_men_28, None, None, None, None, None, None, None, None, 9100
)

# Exact Bayesian update for Alcaraz through R1-R4 (Safiullin, Faria, Wu, Paul)
alc_prior = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
w_r1r4 = [w * p_bo5(e, 1895.0) * p_bo5(e, 1840.0) * p_bo5(e, 1845.0) * p_bo5(e, 1984.0) for e, w in alc_prior]
alc_mix_A = [(e, ww / sum(w_r1r4)) for (e, _), ww in zip(alc_prior, w_r1r4)]

# Model A: Strict outcome-only Bayesian update (0 subjective tweaks)
m07A_tc, m07A_fc, m07A_r4, m07A_qf, m07A_sf, m07A_cu, m07A_uu, m07A_su, m07A_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked, atp_r2_locked, atp_r3_locked, atp_r4_locked_07,
    alc_mix_A, None, None, None, 9710
)

# Model B: Live Sep 7 Market-Calibrated Elo (matching ALL 5 live Betano/DK/TAB match odds!)
# Check pairwise BO5 probabilities in Market-Implied regime:
#   Alcaraz (mix mean ~2240) vs Shelton (2082) -> 76.2% (Betano 1.27/3.70 = 76.3%!)
#   Tiafoe (2032) vs Michelsen (1988) -> 58.2% (Betano/DK/TAB consensus = 58.2%!)
#   Zverev (mix mean ~2158) vs Darderi (1872) -> 90.3% (Betano 1.07/8.00 = 91.3%!)
#   BVDZ (1920) vs Arthur Gea (1858) -> 61.3% (Betano 1.57/2.40 = 61.2%!)
#   Learner Tien (2012) vs Karen Khachanov (1940) -> 62.9% (Betano 1.53/2.50 = 62.9%!)
#   Learner Tien (2012) vs Alexander Blockx (1950) -> 61.2%
#   Karen Khachanov (1940) vs Alexander Blockx (1950) -> 48.2% (note Blockx beat #5 Cobolli & #24 Cerundolo!)
#   Alcaraz (~2240) vs Zverev (~2158) -> 64.5% Alcaraz / 35.5% Zverev!
alc_mix_B = [(2280.0, 0.65), (2180.0, 0.31), (2050.0, 0.04)]
tia_mix_B = [(0.0, 0.96), (-25.0, 0.04)]
zve_mix_B = [(0.0, 0.68), (-25.0, 0.24), (-65.0, 0.08)]   # mean ~2155 (clean vs Tabilo + Betano 1.07 vs Darderi!)
zve_mix_C = [(0.0, 0.45), (-35.0, 0.35), (-75.0, 0.16), (-115.0, 0.04)]  # cautious Zverev (fatigue from early 5-setters)

tweaks_B = {
    "Frances Tiafoe":          +34.0,   # 1998 -> 2032 (crushed Medvedev 3-0, 2-0 H2H v Michelsen)
    "Alex Michelsen":          +63.0,   # 1925 -> 1988 (12-0 sets; 41.8% vs Tiafoe matching Betano/DK/TAB!)
    "Ben Shelton":              +0.0,   # 2082 -> 2082 (restored after 6-2 6-3 6-4 flow-state win over Tsitsipas; 23.8% vs Alcaraz!)
    "Learner Tien":            +36.0,   # 1976 -> 2012 (62.9% vs Khachanov matching Betano 1.53/2.50!)
    "Karen Khachanov":          -5.0,   # 1945 -> 1940 (37.1% vs Tien matching Betano 2.50/1.53!)
    "Alexander Blockx":        +58.0,   # 1892 -> 1950 (beat #5 Cobolli & #24 Cerundolo; Betano 1.60 fav vs Cerundolo!)
    "Luciano Darderi":         -23.0,   # 1895 -> 1872 (hard-court Elo matching Betano 8.00 vs Zverev!)
    "Botic van de Zandschulp": +40.0,   # 1880 -> 1920 (61.2% vs Gea matching Betano 1.57/2.40!)
    "Arthur Gea":              +43.0,   # 1815 -> 1858 (38.8% vs BVDZ matching Betano 2.40/1.57!)
}

# Verify pairwise probs in Market-Implied regime for Model B
print("--- ATP MODEL B PAIRWISE SANITY CHECK (Market-Implied regime) ---")
e_alc = sum(e * w for e, w in alc_mix_B)
e_zve = sum((atp_mkt_elo["Alexander Zverev"] + d) * w for d, w in zve_mix_B)
def get_e(nm):
    base = atp_mkt_elo.get(nm, extra_atp_elo.get(nm, 1840.0))
    return base + tweaks_B.get(nm, 0.0)
print(f"  Alcaraz ({e_alc:.1f}) vs Shelton ({get_e('Ben Shelton'):.1f}): {p_bo5(e_alc, get_e('Ben Shelton')):.4f} (Betano: 0.7626)")
print(f"  Tiafoe  ({get_e('Frances Tiafoe'):.1f}) vs Michelsen ({get_e('Alex Michelsen'):.1f}): {p_bo5(get_e('Frances Tiafoe'), get_e('Alex Michelsen')):.4f} (Mkt: 0.5821)")
print(f"  Zverev  ({e_zve:.1f}) vs Darderi ({get_e('Luciano Darderi'):.1f}): {p_bo5(e_zve, get_e('Luciano Darderi')):.4f} (Betano: 0.9128)")
print(f"  BVDZ    ({get_e('Botic van de Zandschulp'):.1f}) vs Gea ({get_e('Arthur Gea'):.1f}): {p_bo5(get_e('Botic van de Zandschulp'), get_e('Arthur Gea')):.4f} (Betano: 0.6116)")
print(f"  Tien    ({get_e('Learner Tien'):.1f}) vs Khachanov ({get_e('Karen Khachanov'):.1f}): {p_bo5(get_e('Learner Tien'), get_e('Karen Khachanov')):.4f} (Betano: 0.6285)")
print(f"  Tien    ({get_e('Learner Tien'):.1f}) vs Blockx ({get_e('Alexander Blockx'):.1f}): {p_bo5(get_e('Learner Tien'), get_e('Alexander Blockx')):.4f}")
print(f"  Alcaraz ({e_alc:.1f}) vs Zverev ({e_zve:.1f}): {p_bo5(e_alc, e_zve):.4f}")
print(f"  Alcaraz ({e_alc:.1f}) vs Tiafoe ({get_e('Frances Tiafoe'):.1f}): {p_bo5(e_alc, get_e('Frances Tiafoe')):.4f}")
print(f"  Shelton ({get_e('Ben Shelton'):.1f}) vs Tiafoe ({get_e('Frances Tiafoe'):.1f}): {p_bo5(get_e('Ben Shelton'), get_e('Frances Tiafoe')):.4f}")
print(f"  Zverev  ({e_zve:.1f}) vs Tien ({get_e('Learner Tien'):.1f}): {p_bo5(e_zve, get_e('Learner Tien')):.4f}")

m07B_tc, m07B_fc, m07B_r4, m07B_qf, m07B_sf, m07B_cu, m07B_uu, m07B_su, m07B_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked, atp_r2_locked, atp_r3_locked, atp_r4_locked_07,
    alc_mix_B, tia_mix_B, zve_mix_B, tweaks_B, 9720
)
m07C_tc, m07C_fc, m07C_r4, m07C_qf, m07C_sf, m07C_cu, m07C_uu, m07C_su, m07C_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked, atp_r2_locked, atp_r3_locked, atp_r4_locked_07,
    alc_mix_B, tia_mix_B, zve_mix_C, tweaks_B, 9730
)

def bayes_update_atp_full(mc_new):
    raw = {}
    for k, p28 in aug28_named.items():
        raw[k] = 0.0 if mc_new.get(k, 0.0) == 0.0 else p28 * (mc_new[k] / max(1e-6, m28_tc.get(k, 1e-6)))
    mc28_field = 1.0 - sum(m28_tc.get(k, 0.0) for k in aug28_named)
    mcnew_field = 1.0 - sum(mc_new.get(k, 0.0) for k in aug28_named)
    raw_field = field_28 * (mcnew_field / max(1e-6, mc28_field))
    tot = sum(raw.values()) + raw_field
    norm = {k: v / tot for k, v in raw.items()}
    field_post = raw_field / tot
    full = dict(norm)
    for k, v in mc_new.items():
        if k not in aug28_named and v > 0:
            full[k] = field_post * (v / max(1e-9, mcnew_field))
    return full, field_post, tot

updA, _, _ = bayes_update_atp_full(m07A_tc)
updB, _, _ = bayes_update_atp_full(m07B_tc)
updC, _, _ = bayes_update_atp_full(m07C_tc)
blend_atp = {k: 0.20 * updA.get(k, 0) + 0.65 * updB.get(k, 0) + 0.15 * updC.get(k, 0) for k in set(updA) | set(updB)}

print("\n" + "=" * 116)
print("Q3 (891014) ATP DAY 9 (MON SEP 7 ~6:30 PM ET) — SHELTON & BLOCKX IN QF; TSITSIPAS & CERUNDOLO OUT!")
print("=" * 116)
print(f"{'Player':22s} | {'MC07A':6s} | {'MC07B':6s} | {'UpdA':6s} | {'UpdB':6s} | {'UpdC':6s} | {'Blend':6s} | {'QF_B':5s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(blend_atp.items(), key=lambda x: -x[1])[:11]:
    print(f"{k:22s} | {m07A_tc.get(k,0):6.4f} | {m07B_tc.get(k,0):6.4f} | {updA.get(k,0):6.4f} | {updB.get(k,0):6.4f} | {updC.get(k,0):6.4f} | {blend_atp[k]:6.4f} | {m07B_qf.get(k,0):5.3f} | {m07B_sf.get(k,0):5.3f} | {m07B_fc.get(k,0):5.3f}")

print("\n" + "=" * 116)
print(f"Q1 (408930) FURTHEST U.S. MAN DAY 9 (TieRate: A={m07A_tie:.4f}, B={m07B_tie:.4f}, C={m07C_tie:.4f})")
print("=" * 116)
blend_us = {k: 0.20 * m07A_cu.get(k, 0) + 0.65 * m07B_cu.get(k, 0) + 0.15 * m07C_cu.get(k, 0) for k in set(m07A_cu) | set(m07B_cu)}
blend_us_uu = {k: 0.20 * m07A_uu.get(k, 0) + 0.65 * m07B_uu.get(k, 0) + 0.15 * m07C_uu.get(k, 0) for k in set(m07A_uu) | set(m07B_uu)}
blend_us_sp = {k: 0.20 * m07A_su.get(k, 0) + 0.65 * m07B_su.get(k, 0) + 0.15 * m07C_su.get(k, 0) for k in set(m07A_su) | set(m07B_su)}
print(f"{'Player':20s} | {'CondA':6s} | {'CondB':6s} | {'CondC':6s} | {'BlendC':6s} | {'Uncond':6s} | {'Split':6s} | {'QF_B':5s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(blend_us.items(), key=lambda x: -x[1])[:6]:
    print(f"{k:20s} | {m07A_cu.get(k,0):6.4f} | {m07B_cu.get(k,0):6.4f} | {m07C_cu.get(k,0):6.4f} | {blend_us[k]:6.4f} | {blend_us_uu[k]:6.4f} | {blend_us_sp[k]:6.4f} | {m07B_qf[k]:5.3f} | {m07B_sf[k]:5.3f} | {m07B_fc[k]:5.3f}")

# ==============================================================================
# PART 2: WTA DAY 9 MODELS (7/8 R4 LOCKED! SWIATEK & OSAKA OUT!)
# ==============================================================================
w28_t, _, _, _ = sim_wta(None, None, None, None, None, None, None, False, 100000, 9501)
w28_cal_t, _, _, _ = sim_wta(None, None, None, None, None, None, None, True, 100000, 9511)

# Exact Bayesian update for Rybakina through R1-R4 (including Osaka 2062!) and Sabalenka R1-R4
ryb_prior_30 = [(2130.0, 0.52), (2065.0, 0.28), (1970.0, 0.14), (1740.0, 0.06)]
wr_a = [w * p_bo3(e, 1715.0) * p_bo3(e, 1845.0) * p_bo3(e, 1795.0) * p_bo3(e, 2062.0) for e, w in ryb_prior_30]
ryb_mix_A = [(e, ww / sum(wr_a)) for (e, _), ww in zip(ryb_prior_30, wr_a)]
sab_prior_28 = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]
ws_a = [w * p_bo3(e, 1845.0) * p_bo3(e, 1795.0) * p_bo3(e, 1795.0) * p_bo3(e, 1855.0) for e, w in sab_prior_28]
sab_mix_A = [(e, ww / sum(ws_a)) for (e, _), ww in zip(sab_prior_28, ws_a)]

w07A_t, w07A_f, w07A_sf, w07A_qf = sim_wta(
    wta_r1_locked, wta_r2_locked, wta_r3_locked, wta_r4_locked_07,
    ryb_mix_A, sab_mix_A, None, False, 100000, 9521
)

# Model B: Live Sep 7 Market-Calibrated WTA Simulation (matching Kalshi & DraftKings!)
# Matchups to match:
#   - Sabalenka vs Noskova: 70.3% Sabalenka (Kalshi 70/30, DK -267/+212 = 70.6%)
#   - Pegula vs Navarro:    79.0% Pegula (Kalshi 79/21, 4-0 H2H!)
#   - Gauff vs Jovic:       73.1% Gauff (Kalshi 74/28 = 73.1%)
#   - Rybakina vs Zheng:    ~70-72% Rybakina (Rybakina 8-0 sets, 6-1 6-4 over Osaka in 66m; Zheng 7 matches from Q, 2x 0-5 down, beat Keys/Swiatek!)
#   - Gauff vs Andreeva:    ~63-65% Gauff (Gauff 6-0 sets, Cin champ; Andreeva dropped set to Potapova)
# Note: Use an explicit matchup override dict ONLY for Pegula-Navarro H2H (4-0 -> 79% Kalshi) so we don't distort Pegula's Elo vs Sabalenka/Rybakina!
def sim_wta_h2h(locked_r1, locked_r2, locked_r3, locked_r4, ryb_mix, sab_mix, elo_adj,
                h2h_override=None, r1_cal_override=False, n_trials=120000, seed=9750):
    rng = random.Random(seed)
    h2h_override = h2h_override or {}
    tc = Counter(); fc = Counter(); sc = Counter(); qc = Counter()
    for re_e, wr in ryb_mix:
        for se_e, ws in sab_mix:
            w = wr * ws; tr = max(2000, int(round(n_trials * w)))
            emap = dict(wta_cal_elo)
            if elo_adj: emap.update(elo_adj)
            emap["Elena Rybakina"] = re_e; emap["Aryna Sabalenka"] = se_e
            pc = {}
            def gp(a, b):
                if (a, b) in h2h_override: return h2h_override[(a, b)]
                if (b, a) in h2h_override: return 1.0 - h2h_override[(b, a)]
                k = (emap[a], emap[b])
                v = pc.get(k)
                if v is None: v = p_bo3(emap[a], emap[b]); pc[k] = v
                return v
            ltc = Counter(); lfc = Counter(); lsc = Counter(); lqc = Counter()
            for _ in range(tr):
                cur = list(wta_bracket_raw); rnd = 1
                while len(cur) > 1:
                    if rnd == 5:
                        for p in cur: lqc[p] += 1
                    elif rnd == 6:
                        for p in cur: lsc[p] += 1
                    elif rnd == 7:
                        for p in cur: lfc[p] += 1
                    nxt = []
                    for k in range(0, len(cur), 2):
                        a, b = cur[k], cur[k+1]
                        if rnd == 1 and (a, b) in locked_r1: nxt.append(locked_r1[(a, b)])
                        elif rnd == 2 and (a, b) in locked_r2: nxt.append(locked_r2[(a, b)])
                        elif rnd == 3 and (a, b) in locked_r3: nxt.append(locked_r3[(a, b)])
                        elif rnd == 4 and (a, b) in locked_r4: nxt.append(locked_r4[(a, b)])
                        else: nxt.append(a if rng.random() < gp(a, b) else b)
                    cur = nxt; rnd += 1
                ltc[cur[0]] += 1
            for p, c in ltc.items(): tc[p] += w * (c / tr)
            for p, c in lfc.items(): fc[p] += w * (c / tr)
            for p, c in lsc.items(): sc[p] += w * (c / tr)
            for p, c in lqc.items(): qc[p] += w * (c / tr)
    return tc, fc, sc, qc

ryb_mix_B = [(2160.0, 0.72), (2110.0, 0.23), (2035.0, 0.05)]   # mean ~2142 (dominant 6-1 6-4 vs Osaka in 66m, 8-0 sets!)
sab_mix_B = [(2220.0, 0.62), (2175.0, 0.30), (2100.0, 0.08)]   # mean ~2197 (8-0 sets, no set >4 games lost!)
wta_tweaks_B = {
    "Coco Gauff":      2162.0,   # Cincinnati champ, 6-0 sets; 73.1% vs Jovic (1988)!
    "Iva Jovic":       1988.0,   # 26.9% vs Gauff matching Kalshi 74/28!
    "Mirra Andreeva":  2062.0,   # RG champ, into QF (though dropped set to Potapova); 36% vs Gauff, 60% vs Jovic
    "Linda Noskova":   2047.0,   # Wimbledon champ, into QF; 29.7% vs Sabalenka matching DK -267/+212 & Kalshi 70/30!
    "Jessica Pegula":  2078.0,   # #3 seed, 2024 USO finalist, 13% on Kalshi Mon morning! (~34% vs Sabalenka, ~54% vs Noskova)
    "Emma Navarro":    1955.0,   # Beat Kalinskaya 6-4 6-2, 2024 USO SFist; H2H override 21% vs Pegula!
    "Qinwen Zheng":    2002.0,   # Beat Keys & Swiatek from 0-5 down! Former #4/Olympic champ; 31% vs Rybakina!
}
wta_h2h_B = {
    ("Jessica Pegula", "Emma Navarro"): 0.79,   # Exact Kalshi live QF price (4-0 H2H!)
}

print("\n--- WTA MODEL B PAIRWISE SANITY CHECK ---")
e_sab = sum(e * w for e, w in sab_mix_B)
e_ryb = sum(e * w for e, w in ryb_mix_B)
print(f"  Sabalenka ({e_sab:.1f}) vs Noskova ({wta_tweaks_B['Linda Noskova']:.1f}): {p_bo3(e_sab, wta_tweaks_B['Linda Noskova']):.4f} (Mkt: 0.7030)")
print(f"  Pegula    ({wta_tweaks_B['Jessica Pegula']:.1f}) vs Navarro ({wta_tweaks_B['Emma Navarro']:.1f}): H2H=0.7900 (Elo={p_bo3(wta_tweaks_B['Jessica Pegula'], wta_tweaks_B['Emma Navarro']):.4f})")
print(f"  Sabalenka ({e_sab:.1f}) vs Pegula  ({wta_tweaks_B['Jessica Pegula']:.1f}): {p_bo3(e_sab, wta_tweaks_B['Jessica Pegula']):.4f}")
print(f"  Gauff     ({wta_tweaks_B['Coco Gauff']:.1f}) vs Jovic   ({wta_tweaks_B['Iva Jovic']:.1f}): {p_bo3(wta_tweaks_B['Coco Gauff'], wta_tweaks_B['Iva Jovic']):.4f} (Kalshi: 0.7311)")
print(f"  Gauff     ({wta_tweaks_B['Coco Gauff']:.1f}) vs Andreeva({wta_tweaks_B['Mirra Andreeva']:.1f}): {p_bo3(wta_tweaks_B['Coco Gauff'], wta_tweaks_B['Mirra Andreeva']):.4f}")
print(f"  Rybakina  ({e_ryb:.1f}) vs Zheng   ({wta_tweaks_B['Qinwen Zheng']:.1f}): {p_bo3(e_ryb, wta_tweaks_B['Qinwen Zheng']):.4f}")
print(f"  Rybakina  ({e_ryb:.1f}) vs Gauff   ({wta_tweaks_B['Coco Gauff']:.1f}): {p_bo3(e_ryb, wta_tweaks_B['Coco Gauff']):.4f}")
print(f"  Sabalenka ({e_sab:.1f}) vs Gauff   ({wta_tweaks_B['Coco Gauff']:.1f}): {p_bo3(e_sab, wta_tweaks_B['Coco Gauff']):.4f}")
print(f"  Sabalenka ({e_sab:.1f}) vs Rybakina({e_ryb:.1f}): {p_bo3(e_sab, e_ryb):.4f}")

w07B_t, w07B_f, w07B_sf, w07B_qf = sim_wta_h2h(
    wta_r1_locked, wta_r2_locked, wta_r3_locked, wta_r4_locked_07,
    ryb_mix_B, sab_mix_B, wta_tweaks_B, wta_h2h_B, False, 120000, 9751
)

# Model K: Kalshi-anchored WTA update!
# Start from Kalshi Monday morning Sep 7 title odds (BEFORE Zheng d. Swiatek, Rybakina d. Osaka, Andreeva d. Potapova!)
# Kalshi Mon morning reported: Sabalenka 30%, Gauff 19%, Pegula 13%, Swiatek 7%, Rybakina 7%, Andreeva 6%, Osaka 4%, rest ~14% (Noskova ~6.5%, Navarro ~2.5%, Zheng ~2.0%, Jovic ~2.0%, Potapova ~1.0%)
# Simulate Model B at Monday morning state (4/8 R4 locked: Sabalenka, Noskova, Pegula, Navarro) to get exact Bayesian likelihood ratio for the 3 completed Monday matches!
wta_r4_mon_am = {k: v for k, v in wta_r4_locked_07.items() if v in {"Aryna Sabalenka", "Linda Noskova", "Jessica Pegula", "Emma Navarro"}}
w07_am_t, _, _, _ = sim_wta_h2h(
    wta_r1_locked, wta_r2_locked, wta_r3_locked, wta_r4_mon_am,
    [(2140.0, 0.65), (2090.0, 0.25), (2015.0, 0.10)], sab_mix_B,
    {**wta_tweaks_B, "Iga Swiatek": 2110.0, "Naomi Osaka": 2030.0, "Anastasia Potapova": 1950.0},
    wta_h2h_B, False, 120000, 9761
)
kalshi_mon_am = {
    "Aryna Sabalenka": 0.300,
    "Coco Gauff":      0.190,
    "Jessica Pegula":  0.130,
    "Elena Rybakina":  0.070,
    "Iga Swiatek":     0.070,
    "Mirra Andreeva":  0.060,
    "Linda Noskova":   0.065,
    "Naomi Osaka":     0.040,
    "Emma Navarro":    0.025,
    "Qinwen Zheng":    0.020,
    "Iva Jovic":       0.020,
    "Anastasia Potapova": 0.010,
}
raw_k = {}
for p, pk in kalshi_mon_am.items():
    if w07B_t.get(p, 0.0) == 0.0:
        raw_k[p] = 0.0
    else:
        raw_k[p] = pk * (w07B_t[p] / max(1e-6, w07_am_t.get(p, 1e-6)))
tot_k = sum(raw_k.values())
wupdK = {p: v / tot_k for p, v in raw_k.items()}

def bayes_update_wta_full(mc_new, mc_base):
    raw = {k: p28 * (mc_new.get(k, 0.0) / max(1e-6, mc_base.get(k, 1e-6))) for k, p28 in aug28_wta_exact.items()}
    mc28_f = 1.0 - sum(mc_base.get(k, 0.0) for k in aug28_wta_exact)
    mcnew_f = 1.0 - sum(mc_new.get(k, 0.0) for k in aug28_wta_exact)
    raw_f = w_field_28 * (mcnew_f / max(1e-6, mc28_f))
    tot = sum(raw.values()) + raw_f
    norm = {k: v / tot for k, v in raw.items()}
    f_post = raw_f / tot
    full = dict(norm)
    for k, v in mc_new.items():
        if k not in aug28_wta_exact and v > 0:
            full[k] = f_post * (v / max(1e-9, mcnew_f))
    return full, f_post, tot

wupdA, _, _ = bayes_update_wta_full(w07A_t, w28_t)
wupdB, _, _ = bayes_update_wta_full(w07B_t, w28_t)

# Blend: 20% Strict Aug28 Outcome-Only (UpdA) + 45% Pure Live-Calibrated MC (w07B_t) + 35% Kalshi-Mon-AM Updated (wupdK)
# Also print UpdB (Aug28 prior updated with Model B) for full transparency!
blend_wta = {
    k: 0.15 * wupdA.get(k, 0) + 0.25 * wupdB.get(k, 0) + 0.30 * w07B_t.get(k, 0) + 0.30 * wupdK.get(k, 0)
    for k in set(wupdA) | set(w07B_t) | set(wupdK)
}

print("\n" + "=" * 124)
print("Q2 (608158) WTA DAY 9 (MON SEP 7 ~6:30 PM ET) — 7/8 R4 LOCKED! SWIATEK & OSAKA OUT; RYBAKINA/ZHENG/ANDREEVA/PEGULA/NAVARRO IN QF!")
print("=" * 124)
print(f"{'Player':18s} | {'MC07A':6s} | {'MC07B':6s} | {'UpdA':6s} | {'UpdB':6s} | {'KalUpd':6s} | {'Blend':6s} | {'QF_B':5s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(blend_wta.items(), key=lambda x: -x[1])[:10]:
    print(f"{k:18s} | {w07A_t.get(k,0):6.4f} | {w07B_t.get(k,0):6.4f} | {wupdA.get(k,0):6.4f} | {wupdB.get(k,0):6.4f} | {wupdK.get(k,0):6.4f} | {blend_wta[k]:6.4f} | {w07B_qf.get(k,0):5.3f} | {w07B_sf.get(k,0):5.3f} | {w07B_f.get(k,0):5.3f}")
