import math
import random
from collections import Counter

from tennis_aug28_models import (
    devig_mid, p_bo3, p_bo5,
    atp_bracket_raw, atp_base_elo,
    fd_atp_28, dk_atp_28, cz_atp_28, kalshi_atp_28,
    wta_bracket_raw, wta_base_elo, dk_wta_28,
)

# Exact calibrated Elos from tennis_aug28_calibrated.py / tennis_aug30_models.py
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

# ==============================================================================
# DAY 2 (MONDAY AUG 31, 2026, ~22:48 UK / 17:48 ET) EXACT-BRACKET BAYESIAN MODELS
# Batch: tennis (891014 ATP Title, 408930 Furthest U.S. Man, 608158 WTA Title)
# ==============================================================================

# ------------------------------------------------------------------------------
# PART 1: ATP EXACT 128-PLAYER BRACKET (ALL 18 QUALIFIERS + 2 LL IDENTIFIED!)
# ------------------------------------------------------------------------------
atp_bracket_31 = list(atp_bracket_raw)
atp_replacements = {
    "Casper Ruud": "Arthur Gea",          # LL replacing #19 Ruud (back)
    "Marin Cilic": "Otto Virtanen",       # LL replacing Cilic (injury)
    "Q_1":  "Grigor Dimitrov",
    "Q_2":  "Harry Wendelken",
    "Q_3":  "Dalibor Svrcina",
    "Q_4":  "Francesco Passaro",
    "Q_5":  "Andrea Guerrieri",
    "Q_6":  "Shintaro Mochizuki",
    "Q_7":  "Jurij Rodionov",
    "Q_8":  "Zsombor Piros",
    "Q_9":  "Tomas Barrios Vera",
    "Q_10": "Nishesh Basavareddy",        # AMERICAN!
    "Q_11": "Tristan Schoolkate",
    "Q_12": "Hugo Gaston",
    "Q_13": "Rei Sakamoto",
    "Q_14": "Federico Cina",
    "Q_15": "Jacob Fearnley",
    "Q_16": "Toby Samuel",
    "Q_17": "Lloyd Harris",
    "Q_18": "Coleman Wong",
}
for old, new in atp_replacements.items():
    idx = atp_bracket_31.index(old)
    atp_bracket_31[idx] = new

# Exact 18 US men in the 2026 US Open main draw (zero placeholders!)
us_men_31 = {
    "Taylor Fritz", "Ben Shelton", "Frances Tiafoe", "Learner Tien",
    "Brandon Nakashima", "Tommy Paul",
    "Alex Michelsen", "Marcos Giron", "Zachary Svajda", "Jenson Brooksby",
    "Aleksandar Kovacevic", "Martin Damm", "Darwin Blanch", "J.J. Wolf",
    "Stefan Gorzny", "Jack Kennedy", "Michael Zheng",
    "Nishesh Basavareddy",
}
us_men_28 = set(us_men_31) - {"Nishesh Basavareddy"} | {"Q_4", "Q_10"}

# Confirmed ATP R1 results as of Mon Aug 31, 2026 22:48 UK (25 matches!)
atp_r1_locked_31 = {
    # Top half (1 completed)
    ("Jurij Rodionov", "Giovanni Mpetshi Perricard"): "Jurij Rodionov",        # 7-6, 6-0, 7-6
    # Bottom half Q3 Section 9 (Medvedev)
    ("Daniil Medvedev", "Hugo Gaston"): "Daniil Medvedev",                     # 6-4, 6-2, 6-4
    ("Jaume Munar", "Terence Atmane"): "Jaume Munar",                          # 6-7, 3-6, 6-1, 7-6, 7-5
    ("Sho Shimabukuro", "Arthur Rinderknech"): "Arthur Rinderknech",           # 6-7, 6-2, 7-6, 6-2
    # Bottom half Q3 Section 10 (Tiafoe)
    ("Valentin Vacherot", "Aleksandar Kovacevic"): "Valentin Vacherot",        # 6-2, 6-3, 7-5 (US elim)
    ("Kamil Majchrzak", "Hamad Medjedovic"): "Kamil Majchrzak",                # 6-3, 6-3, 6-3
    # Bottom half Q3 Section 11 (Nakashima)
    ("Brandon Nakashima", "Sebastian Baez"): "Brandon Nakashima",              # 6-2, 6-1, 6-0!!
    ("Daniel Merida", "Marton Fucsovics"): "Daniel Merida",                    # 6-4, 6-4, 6-2
    ("Otto Virtanen", "Andrey Rublev"): "Andrey Rublev",                       # 6-7, 6-7, 6-0, 6-2, 7-6(5)
    # Bottom half Q3 Section 12 (Djokovic OUT!)
    ("Tomas Martin Etcheverry", "Vit Kopriva"): "Tomas Martin Etcheverry",     # 6-3, 6-4, 6-0
    ("Mariano Navone", "Novak Djokovic"): "Mariano Navone",                    # 7-6, 5-7, 4-6, 6-2, 6-1!!
    # Bottom half Q4 Section 13 (Shelton)
    ("Damir Dzumhur", "Hubert Hurkacz"): "Hubert Hurkacz",                     # 6-4, 4-6, 6-1, 6-1
    ("Miomir Kecmanovic", "Denis Shapovalov"): "Denis Shapovalov",             # 6-4, 4-6, 6-4, 6-1
    ("Luca Van Assche", "Cameron Norrie"): "Luca Van Assche",                  # 6-7, 6-2, 6-2, 6-3
    # Bottom half Q4 Section 14 (Fils OUT!)
    ("Jiri Lehecka", "Pablo Carreno Busta"): "Jiri Lehecka",                   # 6-1, 7-6, 4-6, 6-2
    ("Toby Samuel", "Tomas Machac"): "Toby Samuel",                            # 6-2, 6-3, 6-2!!
    ("Lloyd Harris", "Jack Kennedy"): "Lloyd Harris",                          # 6-4, 6-2, 6-2 (US elim)
    ("Stefanos Tsitsipas", "Arthur Fils"): "Stefanos Tsitsipas",               # 4-6, 7-6, 6-1, 6-4!!
    # Bottom half Q4 Section 15 (Bublik / Paul)
    ("Alexander Bublik", "J.J. Wolf"): "Alexander Bublik",                     # 6-4, 6-2, 3-6, 6-1 (US elim)
    ("Dino Prizmic", "Alexander Shevchenko"): "Dino Prizmic",                  # 2-6, 6-3, 6-3, 5-7, 7-5
    ("Coleman Wong", "Tommy Paul"): "Tommy Paul",                              # 6-7, 6-1, 6-3, 6-3
    # Bottom half Q4 Section 16 (Alcaraz)
    ("Matteo Arnaldi", "James Duckworth"): "James Duckworth",                  # 5-7, 6-3, 6-2, 7-6(8)
    ("Yibing Wu", "Adam Walton"): "Yibing Wu",                                 # 7-6, 6-2, 7-5
    ("Jaime Faria", "Jenson Brooksby"): "Jaime Faria",                         # 6-3, 7-6, 4-6, 1-6, 6-2 (US elim)
    ("Roman Safiullin", "Carlos Alcaraz"): "Carlos Alcaraz",                   # 6-4, 6-4, 6-4!!
}

atp_pairs_31 = [(atp_bracket_31[i], atp_bracket_31[i+1]) for i in range(0, 128, 2)]
for pair in atp_r1_locked_31:
    assert pair in atp_pairs_31, f"ATP pair not found: {pair}"

extra_atp_elo_31 = {
    "Grigor Dimitrov":     1905.0,  # Qualified after rank drop, still dangerous hard-courter
    "Harry Wendelken":     1815.0,
    "Dalibor Svrcina":     1830.0,
    "Francesco Passaro":   1830.0,
    "Andrea Guerrieri":    1810.0,
    "Shintaro Mochizuki":  1835.0,
    "Jurij Rodionov":      1855.0,  # Beat Mpetshi Perricard in 3
    "Zsombor Piros":       1830.0,
    "Tomas Barrios Vera":  1825.0,
    "Nishesh Basavareddy": 1845.0,
    "Tristan Schoolkate":  1840.0,
    "Arthur Gea":          1815.0,
    "Otto Virtanen":       1840.0,
    "Hugo Gaston":         1835.0,
    "Rei Sakamoto":        1835.0,
    "Federico Cina":       1825.0,
    "Jacob Fearnley":      1850.0,
    "Toby Samuel":         1865.0,  # Crushed Machac 6-2, 6-3, 6-2
    "Lloyd Harris":        1855.0,
    "Coleman Wong":        1855.0,
}

# Print model implied R1 win probabilities for key ATP winners (sanity check!)
print("=== ATP R1 IMPLIED WIN PROBABILITY SANITY CHECK ===")
for (a, b), w in [
    (("Roman Safiullin", "Carlos Alcaraz"), "Carlos Alcaraz"),
    (("Daniil Medvedev", "Hugo Gaston"), "Daniil Medvedev"),
    (("Brandon Nakashima", "Sebastian Baez"), "Brandon Nakashima"),
    (("Coleman Wong", "Tommy Paul"), "Tommy Paul"),
    (("Mariano Navone", "Novak Djokovic"), "Mariano Navone"),
    (("Stefanos Tsitsipas", "Arthur Fils"), "Stefanos Tsitsipas"),
]:
    ea = atp_mkt_elo.get(a, extra_atp_elo_31.get(a, 1840.0))
    eb = atp_mkt_elo.get(b, extra_atp_elo_31.get(b, 1840.0))
    pa = p_bo5(ea, eb)
    pw = pa if w == a else (1 - pa)
    print(f"  {a} vs {b} -> {w} won (model P(win)={pw:.3f})")


def sim_atp_31(bracket, elo_dict, us_set, locked_r1=None, alc_mix=None, elo_tweaks=None, n_trials=60000, seed=9100):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    elos_base = []
    for nm in bracket:
        if nm.startswith("Q_"):
            el = 1830.0
        elif nm in elo_dict:
            el = float(elo_dict[nm])
        elif nm in extra_atp_elo_31:
            el = float(extra_atp_elo_31[nm])
        else:
            el = 1840.0
        if elo_tweaks and nm in elo_tweaks:
            el += float(elo_tweaks[nm])
        elos_base.append(el)

    alc_idx = bracket.index("Carlos Alcaraz")
    djo_idx = bracket.index("Novak Djokovic")
    tia_idx = bracket.index("Frances Tiafoe")
    us_idxs = {i for i, nm in enumerate(bracket) if nm in us_set}

    if alc_mix is None:
        alc_mix = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
    # If Djokovic already lost, no need to loop over djo_mix
    djo_elim = ("Mariano Navone", "Novak Djokovic") in locked_r1
    djo_mix = [(2100.0, 1.0)] if djo_elim else [(2135.0, 0.55), (2075.0, 0.30), (1985.0, 0.15)]
    tia_mix = [(0.0, 0.78), (-35.0, 0.16), (-95.0, 0.06)]

    locked_slots = {}
    for k in range(0, 128, 2):
        pair = (bracket[k], bracket[k+1])
        if pair in locked_r1:
            wname = locked_r1[pair]
            locked_slots[k] = k if wname == bracket[k] else k + 1

    tc = Counter(); fc = Counter(); r4c = Counter(); qfc = Counter(); sfc = Counter()
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
                ltc = Counter(); lfc = Counter(); lr4 = Counter(); lqf = Counter(); lsf = Counter()
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
                        elif rnd == 7:
                            for p in cur: lfc[p] += 1
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
                for p, c in lfc.items(): fc[bracket[p]] += w * (c / tr)
                for p, c in lr4.items(): r4c[bracket[p]] += w * (c / tr)
                for p, c in lqf.items(): qfc[bracket[p]] += w * (c / tr)
                for p, c in lsf.items(): sfc[bracket[p]] += w * (c / tr)
                for p, c in luc.items(): uncond_us[bracket[p]] += w * (c / tr)
                tie_rate += w * (ties / tr)
    cond_us = {nm: v / (1.0 - tie_rate) for nm, v in uncond_us.items()}
    return tc, fc, r4c, qfc, sfc, cond_us, uncond_us, tie_rate


regimes_cal = [
    ("Market-Implied", 0.50, atp_mkt_elo),
    ("Pre-Draw Talent", 0.30, {**atp_mkt_elo, "Taylor Fritz": 2062, "Ben Shelton": 2084, "Arthur Fils": 2078, "Alexander Zverev": 2158}),
    ("BO5/NY Pedigree", 0.20, {**atp_mkt_elo, "Taylor Fritz": 2070, "Ben Shelton": 2072, "Frances Tiafoe": 2012, "Tommy Paul": 1998, "Brandon Nakashima": 1988, "Learner Tien": 1966, "Arthur Fils": 2068}),
]

def run_atp_blend(bracket, us_set, locked, alc_mix=None, elo_tweaks=None, seed_base=9100):
    b_tc = Counter(); b_fc = Counter(); b_r4 = Counter(); b_qf = Counter(); b_sf = Counter()
    b_cond = Counter(); b_uncond = Counter(); b_tie = 0.0
    for idx, (lbl, w, ed) in enumerate(regimes_cal):
        tc, fc, r4c, qfc, sfc, cu, uu, tr = sim_atp_31(
            bracket, ed, us_set, locked_r1=locked, alc_mix=alc_mix, elo_tweaks=elo_tweaks,
            n_trials=60000, seed=seed_base + idx
        )
        b_tie += w * tr
        for k, v in tc.items(): b_tc[k] += w * v
        for k, v in fc.items(): b_fc[k] += w * v
        for k, v in r4c.items(): b_r4[k] += w * v
        for k, v in qfc.items(): b_qf[k] += w * v
        for k, v in sfc.items(): b_sf[k] += w * v
        for k, v in cu.items(): b_cond[k] += w * v
        for k, v in uu.items(): b_uncond[k] += w * v
    return b_tc, b_fc, b_r4, b_qf, b_sf, b_cond, b_uncond, b_tie

# Baseline Aug 28
m28_tc, m28_fc, m28_r4, m28_qf, m28_sf, m28_cu, m28_uu, m28_tie = run_atp_blend(
    atp_bracket_raw, us_men_28, None, None, None, 9100
)

# Exact Bayes update of Alcaraz mixture GIVEN Alcaraz WON R1 (just winning R1 vs 1895 Safiullin)
# vs GIVEN Alcaraz won 6-4, 6-4, 6-4 cleanly with 20+ FH winners!
alc_prior = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
# Scenario A: Strict R1-win-only Bayes on Alcaraz (P(win R1 | state)) + no other form Elo tweaks
w_r1_only = [w * p_bo5(e, 1895.0) for e, w in alc_prior]
s_r1 = sum(w_r1_only)
alc_mix_A = [(e, ww / s_r1) for (e, _), ww in zip(alc_prior, w_r1_only)]

# Scenario B (Conservative Form/Margin Bayes): clean 6-4 6-4 6-4 + 20 FH winners, retaining 2.5% residual wrist flare-up hazard
# Likelihoods of 3-0 crisp win: 2280 -> 0.72, 2175 -> 0.54, 2045 -> 0.22
alc_mix_B = [(2280.0, 0.42), (2175.0, 0.46), (2045.0, 0.095), (1750.0, 0.025)]
tweaks_B = {
    "Daniil Medvedev": +10.0,    # Clean 6-4 6-2 6-4, 34W/11UE
    "Brandon Nakashima": +10.0,  # Crushed Baez 6-2 6-1 6-0
    "Tommy Paul": +5.0,          # Solid comeback vs hot Wong
    "Andrey Rublev": -12.0,      # Exhausted 5-set comeback vs LL Virtanen
    "Stefanos Tsitsipas": +12.0, # Beat #10 Fils in 4
}

# Scenario C (Moderate-Bullish Alcaraz): stronger wrist-healthy update
alc_mix_C = [(2285.0, 0.50), (2185.0, 0.38), (2060.0, 0.10), (1750.0, 0.02)]
tweaks_C = {
    "Daniil Medvedev": +15.0,
    "Brandon Nakashima": +14.0,
    "Tommy Paul": +6.0,
    "Andrey Rublev": -18.0,
    "Stefanos Tsitsipas": +15.0,
}

m31A_tc, m31A_fc, m31A_r4, m31A_qf, m31A_sf, m31A_cu, m31A_uu, m31A_tie = run_atp_blend(
    atp_bracket_31, us_men_31, atp_r1_locked_31, alc_mix_A, None, 9200
)
m31B_tc, m31B_fc, m31B_r4, m31B_qf, m31B_sf, m31B_cu, m31B_uu, m31B_tie = run_atp_blend(
    atp_bracket_31, us_men_31, atp_r1_locked_31, alc_mix_B, tweaks_B, 9300
)
m31C_tc, m31C_fc, m31C_r4, m31C_qf, m31C_sf, m31C_cu, m31C_uu, m31C_tie = run_atp_blend(
    atp_bracket_31, us_men_31, atp_r1_locked_31, alc_mix_C, tweaks_C, 9400
)

# Exact Aug 28 full-128 market-calibrated prior (including Field_Rest!)
fd_m, _, _, _ = devig_mid(fd_atp_28)
dk_m, _, _, _ = devig_mid(dk_atp_28)
cz_m, _, _, _ = devig_mid(cz_atp_28)
aug28_named = {}
for k in fd_atp_28:
    if k == "Field_Rest": continue
    bks = 0.45 * fd_m[k] + 0.40 * dk_m[k] + 0.15 * cz_m[k]
    aug28_named[k] = 0.45 * kalshi_atp_28[k] + 0.30 * bks + 0.25 * m28_tc.get(k, 0.0)
field_28 = max(0.0, 1.0 - sum(aug28_named.values()))

# Compute FULL-128 RENORMALIZED Bayesian updates!
def bayes_update_atp(mc_new):
    raw = {}
    for k, p28 in aug28_named.items():
        if mc_new.get(k, 0.0) == 0.0:
            raw[k] = 0.0
        else:
            raw[k] = p28 * (mc_new[k] / max(1e-6, m28_tc.get(k, 1e-6)))
    mc28_field = 1.0 - sum(m28_tc.get(k, 0.0) for k in aug28_named)
    mcnew_field = 1.0 - sum(mc_new.get(k, 0.0) for k in aug28_named)
    raw_field = field_28 * (mcnew_field / max(1e-6, mc28_field))
    tot = sum(raw.values()) + raw_field
    norm = {k: v / tot for k, v in raw.items()}
    return norm, raw_field / tot, tot

updA, fA, totA = bayes_update_atp(m31A_tc)
updB, fB, totB = bayes_update_atp(m31B_tc)
updC, fC, totC = bayes_update_atp(m31C_tc)

print("\n" + "=" * 102)
print(f"Q1 (891014) MEN'S SINGLES — MON AUG 31 DAY 2 BAYESIAN UPDATE (Pre-norm sums: A={totA:.4f}, B={totB:.4f}, C={totC:.4f})")
print("=" * 102)
print(f"{'Player':22s} | {'MC28':6s} | {'MC31A':6s} | {'MC31B':6s} | {'MC31C':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'UpdC':6s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(updB.items(), key=lambda x: -x[1])[:14]:
    print(f"{k:22s} | {m28_tc.get(k,0):6.4f} | {m31A_tc.get(k,0):6.4f} | {m31B_tc.get(k,0):6.4f} | {m31C_tc.get(k,0):6.4f} | {aug28_named.get(k,0):6.4f} | {updA[k]:6.4f} | {updB[k]:6.4f} | {updC[k]:6.4f} | {m31B_sf.get(k,0):5.3f} | {m31B_fc.get(k,0):5.3f}")
print(f"{'Field_Rest':22s} | {1-sum(m28_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m31A_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m31B_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m31C_tc.get(k,0) for k in aug28_named):6.4f} | {field_28:6.4f} | {fA:6.4f} | {fB:6.4f} | {fC:6.4f} |")

# Also check if any un-named player in Field_Rest (like Tsitsipas, Lehecka, Rublev) broke >1.5%
print("\nTop non-named MC31B players:", [(k, round(v, 4)) for k, v in sorted(m31B_tc.items(), key=lambda x: -x[1]) if k not in aug28_named][:6])
print("Top-7 UpdA:", [(k, round(v, 4)) for k, v in sorted(updA.items(), key=lambda x: -x[1])[:8]])
print("Top-7 UpdB:", [(k, round(v, 4)) for k, v in sorted(updB.items(), key=lambda x: -x[1])[:8]])
print("Top-7 UpdC:", [(k, round(v, 4)) for k, v in sorted(updC.items(), key=lambda x: -x[1])[:8]])

print("\n" + "=" * 102)
print(f"Q2 (408930) FURTHEST U.S. MAN — MON AUG 31 DAY 2 UPDATE (Tie: 28={m28_tie:.4f}, A={m31A_tie:.4f}, B={m31B_tie:.4f}, C={m31C_tie:.4f})")
print("=" * 102)
print(f"{'Player':22s} | {'Cond28':7s} | {'CondA':7s} | {'CondB':7s} | {'CondC':7s} | {'UncondB':7s} | {'R4_B':5s} | {'QF_B':5s} | {'SF_B':5s}")
for k, _ in sorted(m31B_cu.items(), key=lambda x: -x[1])[:10]:
    print(f"{k:22s} | {m28_cu.get(k,0):7.4f} | {m31A_cu.get(k,0):7.4f} | {m31B_cu.get(k,0):7.4f} | {m31C_cu.get(k,0):7.4f} | {m31B_uu.get(k,0):7.4f} | {m31B_r4[k]:5.3f} | {m31B_qf[k]:5.3f} | {m31B_sf[k]:5.3f}")

# ------------------------------------------------------------------------------
# PART 2: WTA EXACT 128-PLAYER BRACKET (36 COMPLETED R1 MATCHES!)
# ------------------------------------------------------------------------------
wta_r1_locked_31 = {
    # Q1
    ("Aryna Sabalenka", "Camila Osorio"): "Aryna Sabalenka",                 # 6-2, 6-4
    ("Renata Zarazua", "Polina Iatcenko"): "Polina Iatcenko",                # 4-6, 6-4, 7-6(7)
    ("Aoi Ito", "Oksana Selekhmeteva"): "Oksana Selekhmeteva",               # 6-2, 6-4
    ("Kamilla Rakhimova", "Barbora Krejcikova"): "Kamilla Rakhimova",        # 7-6(4), 6-2
    ("Maja Chwalinska", "Taylor Townsend"): "Taylor Townsend",               # 6-2, 6-3
    ("Taylah Preston", "Alycia Parks"): "Taylah Preston",                    # 6-3, 6-3
    ("Hanne Vandewinkel", "Karolina Pliskova"): "Karolina Pliskova",         # 2-6, 7-5, 6-3
    ("Daria Snigur", "Diana Shnaider"): "Diana Shnaider",                    # 6-0, 6-4
    ("Marta Kostyuk", "Storm Hunter"): "Marta Kostyuk",                      # 6-4, 6-1
    ("McCartney Kessler", "Ekaterina Alexandrova"): "Ekaterina Alexandrova", # 6-2, 6-2
    ("Talia Gibson", "Donna Vekic"): "Donna Vekic",                          # 6-2, 4-6, 6-3
    ("Elvina Kalieva", "Lanlana Tararudee"): "Lanlana Tararudee",            # 6-3, 6-7, 6-2
    ("Katie Volynets", "Linda Noskova"): "Linda Noskova",                    # 7-5, 6-1
    # Q2
    ("Jessica Pegula", "Elena-Gabriela Ruse"): "Jessica Pegula",             # 6-3, 6-2
    ("Venus Williams", "Sofia Kenin"): "Sofia Kenin",                        # 6-2, 7-6(6)
    ("Mananchaya Sawangkaew", "Panna Udvardy"): "Mananchaya Sawangkaew",     # 6-4, 6-3
    ("Shuai Zhang", "Leylah Fernandez"): "Leylah Fernandez",                 # 6-3, 6-2
    ("Jasmine Paolini", "Veronika Erjavec"): "Jasmine Paolini",              # 6-3, 3-6, 6-4
    ("Lucrezia Stefanini", "Dayana Yastremska"): "Lucrezia Stefanini",       # 6-3, 4-6, 6-1
    ("Viktorija Golubic", "Diane Parry"): "Diane Parry",                     # 7-5, 6-4
    ("Elina Svitolina", "Solana Sierra"): "Elina Svitolina",                 # 6-1, 6-2
    ("Emiliana Arango", "Xinyu Wang"): "Xinyu Wang",                         # 6-4, 6-2
    ("Anna Blinkova", "Anna Kalinskaya"): "Anna Kalinskaya",                 # 6-4, 6-3
    ("Emma Navarro", "Lois Boisson"): "Emma Navarro",                        # 7-6, 6-7, 6-3
    ("Anouk Koevermans", "Caty McNally"): "Caty McNally",                    # 7-5, 6-1
    ("Claire Lee", "Katie Boulter"): "Katie Boulter",                        # 6-4, 3-6, 6-0
    ("Sinja Kraus", "Karolina Muchova"): "Karolina Muchova",                 # 6-3, 6-0
    # Q3
    ("Lilli Tagger", "Tamara Korpatsch"): "Lilli Tagger",                    # 6-0, 7-6(4)
    ("Ashlyn Krueger", "Amanda Anisimova"): "Amanda Anisimova",              # 6-1, 6-3
    ("Sara Bejlek", "Cristina Bucsa"): "Cristina Bucsa",                     # 7-5, 4-6, 6-1
    ("Anhelina Kalinina", "Himeno Sakatsume"): "Himeno Sakatsume",           # 6-3, 6-3
    # Q4
    ("Nadia Podoroska", "Simona Waltert"): "Nadia Podoroska",                # 4-6, 7-6, 6-3
    ("Harriet Dart", "Peyton Stearns"): "Harriet Dart",                      # 3-6, 6-3, 6-2
    ("Elsa Jacquemot", "Marie Bouzkova"): "Marie Bouzkova",                  # 6-2, 6-2
    ("Qinwen Zheng", "Ksenia Liutova"): "Qinwen Zheng",                      # 4-6, 6-3, 6-1
    ("Tamara Zidansek", "Maria Timofeeva"): "Maria Timofeeva",               # 6-3, 7-5
}

wta_pairs_31 = [(wta_bracket_raw[i], wta_bracket_raw[i+1]) for i in range(0, 128, 2)]
for pair in wta_r1_locked_31:
    assert pair in wta_pairs_31, f"WTA pair not found: {pair}"

print("\n=== WTA R1 IMPLIED WIN PROBABILITY SANITY CHECK ===")
for (a, b), w in [
    (("Aryna Sabalenka", "Camila Osorio"), "Aryna Sabalenka"),
    (("Jessica Pegula", "Elena-Gabriela Ruse"), "Jessica Pegula"),
    (("Ashlyn Krueger", "Amanda Anisimova"), "Amanda Anisimova"),
    (("Sinja Kraus", "Karolina Muchova"), "Karolina Muchova"),
    (("Katie Volynets", "Linda Noskova"), "Linda Noskova"),
    (("Marta Kostyuk", "Storm Hunter"), "Marta Kostyuk"),
    (("Elina Svitolina", "Solana Sierra"), "Elina Svitolina"),
    (("Venus Williams", "Sofia Kenin"), "Sofia Kenin"),
]:
    ea, eb = wta_cal_elo[a], wta_cal_elo[b]
    pa = p_bo3(ea, eb)
    pw = pa if w == a else (1 - pa)
    print(f"  {a} vs {b} -> {w} won (model P(win)={pw:.3f})")

def sim_wta_31(locked_r1=None, ryb_mix=None, sab_mix=None, elo_adj=None, n_trials=90000, seed=9500):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    if ryb_mix is None:
        ryb_mix = [(2130.0, 0.42), (2055.0, 0.30), (1955.0, 0.18), (1700.0, 0.10)]
    if sab_mix is None:
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

# Baseline Aug 28 WTA
w28_t, _, _ = sim_wta_31(locked_r1=None, n_trials=90000, seed=9501)

# Aug 31 Scenario A: Locked R1 + Aug 30 conservative Rybakina health update (no extra Sabalenka/Anisimova form bump)
ryb_mix_31 = [(2130.0, 0.52), (2065.0, 0.28), (1970.0, 0.14), (1740.0, 0.06)]
w31A_t, w31A_f, w31A_sf = sim_wta_31(locked_r1=wta_r1_locked_31, ryb_mix=ryb_mix_31, n_trials=90000, seed=9502)

# Aug 31 Scenario B: + modest Sabalenka/Pegula/Anisimova/Muchova sharp-R1 form updates
# Sabalenka 32 winners 6-2 6-4 eases slump weight (0.45/0.35/0.20 -> 0.54/0.33/0.13)
sab_mix_31 = [(2225.0, 0.54), (2175.0, 0.33), (2085.0, 0.13)]
wta_tweaks_B = {
    "Jessica Pegula": wta_cal_elo["Jessica Pegula"] + 6.0,
    "Amanda Anisimova": wta_cal_elo["Amanda Anisimova"] + 10.0, # 6-1 6-3
    "Karolina Muchova": wta_cal_elo["Karolina Muchova"] + 10.0, # 6-3 6-0
}
w31B_t, w31B_f, w31B_sf = sim_wta_31(
    locked_r1=wta_r1_locked_31, ryb_mix=ryb_mix_31, sab_mix=sab_mix_31,
    elo_adj=wta_tweaks_B, n_trials=90000, seed=9503
)

# Full-128 renormalized Bayesian update for WTA
w_field_28 = 1.0 - sum(aug28_wta_exact.values())
def bayes_update_wta(mc_new):
    raw = {}
    for k, p28 in aug28_wta_exact.items():
        raw[k] = p28 * (mc_new.get(k, 0.0) / max(1e-6, w28_t.get(k, 1e-6)))
    mc28_f = 1.0 - sum(w28_t.get(k, 0.0) for k in aug28_wta_exact)
    mcnew_f = 1.0 - sum(mc_new.get(k, 0.0) for k in aug28_wta_exact)
    raw_f = w_field_28 * (mcnew_f / max(1e-6, mc28_f))
    tot = sum(raw.values()) + raw_f
    return {k: v / tot for k, v in raw.items()}, raw_f / tot, tot

wupdA, wfA, wtotA = bayes_update_wta(w31A_t)
wupdB, wfB, wtotB = bayes_update_wta(w31B_t)

print("\n" + "=" * 102)
print(f"Q3 (608158) WOMEN'S SINGLES — MON AUG 31 DAY 2 BAYESIAN UPDATE (Pre-norm sums: A={wtotA:.4f}, B={wtotB:.4f})")
print("=" * 102)
print(f"{'Player':20s} | {'MC28':6s} | {'MC31A':6s} | {'MC31B':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(wupdB.items(), key=lambda x: -x[1])[:12]:
    print(f"{k:20s} | {w28_t[k]:6.4f} | {w31A_t[k]:6.4f} | {w31B_t[k]:6.4f} | {aug28_wta_exact[k]:6.4f} | {wupdA[k]:6.4f} | {wupdB[k]:6.4f} | {w31B_sf[k]:5.3f} | {w31B_f[k]:5.3f}")
print("WTA Top-8 UpdA:", [(k, round(v, 4)) for k, v in sorted(wupdA.items(), key=lambda x: -x[1])[:8]])
print("WTA Top-8 UpdB:", [(k, round(v, 4)) for k, v in sorted(wupdB.items(), key=lambda x: -x[1])[:8]])
