import math
import random
from collections import Counter

from tennis_aug28_models import (
    devig_mid, p_bo3, p_bo5,
    atp_bracket_raw, atp_base_elo,
    fd_atp_28, dk_atp_28, cz_atp_28, kalshi_atp_28,
    wta_bracket_raw, wta_base_elo, dk_wta_28,
)

# ==============================================================================
# DAY 3 (TUESDAY SEP 1, 2026, ~21:30 GMT / 5:30 PM ET) EXACT-BRACKET BAYESIAN MODELS
# Batch: tennis (891014 ATP Title, 408930 Furthest U.S. Man, 608158 WTA Title)
# ==============================================================================

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

# ------------------------------------------------------------------------------
# PART 1: ATP EXACT 128-PLAYER BRACKET (ALL 18 Q + 3 LL: Gea, Virtanen, Yunchaokete Bu)
# ------------------------------------------------------------------------------
atp_replacements_01 = {
    "Casper Ruud": "Arthur Gea",          # LL replacing #19 Ruud (back)
    "Marin Cilic": "Otto Virtanen",       # LL replacing Cilic (injury)
    "Thanasi Kokkinakis": "Yunchaokete Bu", # LL replacing Kokkinakis (injury, Sep 1!)
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
atp_bracket_01 = [atp_replacements_01.get(x, x) for x in atp_bracket_raw]

# Exact 18 US men in the 2026 US Open main draw (note: Sebastian Gorzny stored as "Stefan Gorzny" in raw bracket)
us_men_01 = {
    "Taylor Fritz", "Ben Shelton", "Frances Tiafoe", "Learner Tien",
    "Brandon Nakashima", "Tommy Paul",
    "Alex Michelsen", "Marcos Giron", "Zachary Svajda", "Jenson Brooksby",
    "Aleksandar Kovacevic", "Martin Damm", "Darwin Blanch", "J.J. Wolf",
    "Stefan Gorzny", "Jack Kennedy", "Michael Zheng",
    "Nishesh Basavareddy",
}
us_men_28 = set(us_men_01) - {"Nishesh Basavareddy"} | {"Q_4", "Q_10"}

# Confirmed ATP R1 results as of Tue Sep 1, 2026 (~21:30 GMT): 48 of 64 MATCHES LOCKED!
atp_r1_winners_01 = {
    # Q1 (5 locked)
    "Quentin Halys",            # def. Diaz Acosta 6-4 7-5 6-7 6-1
    "Alexei Popyrin",           # def. Dimitrov 3-6 6-3 6-2 6-4
    "Alejandro Tabilo",         # def. Hanfmann 6-3 6-2 6-7 6-3
    "Luciano Darderi",          # def. Wendelken 6-2 3-6 6-2 7-5
    "Dalibor Svrcina",          # def. Royer 6-4 6-3 5-7 5-7 6-2
    # Q2 (11 locked)
    "Felix Auger-Aliassime",    # def. Hijikata 7-5 4-6 6-3 7-5
    "Karen Khachanov",          # def. Burruchaga 6-3 6-0 6-1
    "Stefan Gorzny",            # Sebastian Gorzny def. Collignon 3-6 6-3 3-6 6-3 7-6(9)
    "Learner Tien",             # def. Borges 6-4 6-1 6-2!!
    "Taylor Fritz",             # def. Blanch 6-3 6-2 6-4!!
    "Mattia Bellucci",          # def. Piros 6-4 6-2 6-0
    "Francisco Cerundolo",      # def. Misolic 6-4 6-3 7-5
    "Jakub Mensik",             # def. Mochizuki 6-1 6-4 7-5
    "Jurij Rodionov",           # def. Mpetshi Perricard 7-6 6-0 7-6
    "Alexander Blockx",         # def. Barrios Vera 6-3 6-4 6-2
    "Marco Trungelliti",        # def. Shang 0-6 7-6 1-6 6-3 6-4
    "Flavio Cobolli",           # def. Comesana 3-6 2-6 6-3 6-4 6-4 (4h13m)
    # Q3 (ALL 16 LOCKED!)
    "Daniil Medvedev",          # def. Gaston 6-4 6-2 6-4
    "Jaume Munar",              # def. Atmane in 5
    "Rei Sakamoto",             # def. Vukic 6-4 6-7 6-4 3-6 6-4
    "Arthur Rinderknech",       # def. Shimabukuro in 4
    "Valentin Vacherot",        # def. Kovacevic 6-2 6-3 7-5
    "Adrian Mannarino",         # def. Tirante 4-6 3-6 6-3 6-3 6-3
    "Kamil Majchrzak",          # def. Medjedovic 6-3 6-3 6-3
    "Frances Tiafoe",           # def. Damm 6-4 4-6 3-6 6-3 6-4
    "Brandon Nakashima",        # def. Baez 6-2 6-1 6-0
    "Alex Michelsen",           # def. Cina 6-4 6-1 6-0
    "Daniel Merida",            # def. Fucsovics 6-4 6-4 6-2
    "Andrey Rublev",            # def. Virtanen 6-7 6-7 6-0 6-2 7-6
    "Tomas Martin Etcheverry",  # def. Kopriva 6-3 6-4 6-0
    "Matteo Berrettini",        # def. Wawrinka 7-6 7-6 6-0
    "Jacob Fearnley",           # def. Landaluce 4-6 6-2 4-6 7-5 6-3
    "Mariano Navone",           # def. Djokovic 7-6 5-7 4-6 6-2 6-1!!
    # Q4 (ALL 16 LOCKED!)
    "Ben Shelton",              # def. Griekspoor 1-6 6-1 7-6 6-2!!
    "Hubert Hurkacz",           # def. Dzumhur 6-4 4-6 6-1 6-1
    "Denis Shapovalov",         # def. Kecmanovic 6-4 4-6 6-4 6-1
    "Luca Van Assche",          # def. Norrie 6-7 6-2 6-2 6-3
    "Jiri Lehecka",             # def. Carreno Busta 6-1 7-6 4-6 6-2
    "Toby Samuel",              # def. Machac 6-2 6-3 6-2
    "Lloyd Harris",             # def. Kennedy 6-4 6-2 6-2
    "Stefanos Tsitsipas",       # def. Fils 4-6 7-6 6-1 6-4!!
    "Alexander Bublik",         # def. Wolf 6-4 6-2 3-6 6-1
    "Dino Prizmic",             # def. Shevchenko in 5
    "Tommy Paul",               # def. Wong 6-7 6-1 6-3 6-3
    "James Duckworth",          # def. Arnaldi 5-7 6-3 6-2 7-6
    "Yibing Wu",                # def. Walton 7-6 6-2 7-5
    "Jaime Faria",              # def. Brooksby in 5
    "Carlos Alcaraz",           # def. Safiullin 6-4 6-4 6-4!!
}

atp_r1_locked_01 = {}
for i in range(0, 128, 2):
    a, b = atp_bracket_01[i], atp_bracket_01[i+1]
    if a in atp_r1_winners_01:
        assert b not in atp_r1_winners_01, f"Both in winners: {a}, {b}"
        atp_r1_locked_01[(a, b)] = a
    elif b in atp_r1_winners_01:
        atp_r1_locked_01[(a, b)] = b
print(f"ATP R1 locked count: {len(atp_r1_locked_01)} / 64 (expected 48)")
# Check unmatched winners
matched_w = set(atp_r1_locked_01.values())
unmatched = atp_r1_winners_01 - matched_w
if unmatched:
    print("WARNING UNMATCHED ATP WINNERS:", unmatched)
assert len(atp_r1_locked_01) == 48, f"Expected 48, got {len(atp_r1_locked_01)}"

extra_atp_elo_01 = {
    "Grigor Dimitrov":     1905.0,
    "Harry Wendelken":     1815.0,
    "Dalibor Svrcina":     1835.0,
    "Francesco Passaro":   1830.0,
    "Andrea Guerrieri":    1810.0,
    "Shintaro Mochizuki":  1835.0,
    "Jurij Rodionov":      1855.0,
    "Zsombor Piros":       1830.0,
    "Tomas Barrios Vera":  1825.0,
    "Nishesh Basavareddy": 1845.0,
    "Tristan Schoolkate":  1840.0,
    "Arthur Gea":          1815.0,
    "Otto Virtanen":       1840.0,
    "Hugo Gaston":         1835.0,
    "Rei Sakamoto":        1840.0,
    "Federico Cina":       1825.0,
    "Jacob Fearnley":      1855.0,
    "Toby Samuel":         1865.0,
    "Lloyd Harris":        1855.0,
    "Coleman Wong":        1855.0,
    "Yunchaokete Bu":      1840.0,  # LL replacing Kokkinakis (1885)
}

def sim_atp(bracket, elo_dict, us_set, locked_r1=None, alc_mix=None, tia_mix=None, elo_tweaks=None, n_trials=60000, seed=9100):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    elos_base = []
    for nm in bracket:
        if nm.startswith("Q_"):
            el = 1830.0
        elif nm in elo_dict:
            el = float(elo_dict[nm])
        elif nm in extra_atp_elo_01:
            el = float(extra_atp_elo_01[nm])
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
    djo_elim = ("Mariano Navone", "Novak Djokovic") in locked_r1
    djo_mix = [(2100.0, 1.0)] if djo_elim else [(2135.0, 0.55), (2075.0, 0.30), (1985.0, 0.15)]
    if tia_mix is None:
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

def run_atp_blend(bracket, us_set, locked, alc_mix=None, tia_mix=None, elo_tweaks=None, seed_base=9100):
    b_tc = Counter(); b_fc = Counter(); b_r4 = Counter(); b_qf = Counter(); b_sf = Counter()
    b_cond = Counter(); b_uncond = Counter(); b_tie = 0.0
    for idx, (lbl, w, ed) in enumerate(regimes_cal):
        tc, fc, r4c, qfc, sfc, cu, uu, tr = sim_atp(
            bracket, ed, us_set, locked_r1=locked, alc_mix=alc_mix, tia_mix=tia_mix,
            elo_tweaks=elo_tweaks, n_trials=60000, seed=seed_base + idx
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
    atp_bracket_raw, us_men_28, None, None, None, None, 9100
)

# Model A: Strict outcome-only Bayes (no extra margin/form Elo tweaks, strict R1-win-only Alcaraz Bayes)
alc_prior = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
w_r1_only = [w * p_bo5(e, 1895.0) for e, w in alc_prior]
s_r1 = sum(w_r1_only)
alc_mix_A = [(e, ww / s_r1) for (e, _), ww in zip(alc_prior, w_r1_only)]

# Model B: Conservative Margin/Form/Fatigue Bayes (consistent with Aug 31 Model B + Day 2/3 evidence)
alc_mix_B = [(2280.0, 0.42), (2175.0, 0.46), (2045.0, 0.095), (1750.0, 0.025)]
# Tiafoe dragged to 5 sets vs Martin Damm (slight uptick in rust/fatigue weight vs pre-tournament)
tia_mix_B = [(0.0, 0.70), (-35.0, 0.22), (-95.0, 0.08)]
tweaks_B = {
    "Daniil Medvedev": +10.0,     # Clean 6-4 6-2 6-4
    "Brandon Nakashima": +10.0,   # 6-2 6-1 6-0 vs Baez
    "Alex Michelsen": +10.0,      # 6-4 6-1 6-0 vs Cina
    "Learner Tien": +12.0,        # 6-4 6-1 6-2 masterclass vs #35-ish Borges!
    "Taylor Fritz": +5.0,         # Clean 6-3 6-2 6-4, 14 aces
    "Tommy Paul": +5.0,           # Solid comeback vs Wong
    "Andrey Rublev": -12.0,       # Exhausted 5-set TB comeback vs LL Virtanen
    "Flavio Cobolli": -15.0,      # 4h13m 5-set comeback from 0-2 down vs #119 Comesana
    "Stefanos Tsitsipas": +12.0,  # Beat #10 Fils in 4
    "Karen Khachanov": +8.0,      # 6-3 6-0 6-1
    "Matteo Berrettini": +8.0,    # 7-6 7-6 6-0
}

m01A_tc, m01A_fc, m01A_r4, m01A_qf, m01A_sf, m01A_cu, m01A_uu, m01A_tie = run_atp_blend(
    atp_bracket_01, us_men_01, atp_r1_locked_01, alc_mix_A, None, None, 9600
)
m01B_tc, m01B_fc, m01B_r4, m01B_qf, m01B_sf, m01B_cu, m01B_uu, m01B_tie = run_atp_blend(
    atp_bracket_01, us_men_01, atp_r1_locked_01, alc_mix_B, tia_mix_B, tweaks_B, 9700
)

# Full-128 renormalized market-anchored Bayesian update (from Aug 28 consensus prior)
fd_m, _, _, _ = devig_mid(fd_atp_28)
dk_m, _, _, _ = devig_mid(dk_atp_28)
cz_m, _, _, _ = devig_mid(cz_atp_28)
aug28_named = {}
for k in fd_atp_28:
    if k == "Field_Rest": continue
    bks = 0.45 * fd_m[k] + 0.40 * dk_m[k] + 0.15 * cz_m[k]
    aug28_named[k] = 0.45 * kalshi_atp_28[k] + 0.30 * bks + 0.25 * m28_tc.get(k, 0.0)
field_28 = max(0.0, 1.0 - sum(aug28_named.values()))

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

updA, fA, totA = bayes_update_atp(m01A_tc)
updB, fB, totB = bayes_update_atp(m01B_tc)

print("\n" + "=" * 102)
print(f"Q3 (891014) MEN'S SINGLES — TUE SEP 1 DAY 3 BAYESIAN UPDATE (Pre-norm sums: A={totA:.4f}, B={totB:.4f})")
print("=" * 102)
print(f"{'Player':22s} | {'MC28':6s} | {'MC01A':6s} | {'MC01B':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(updB.items(), key=lambda x: -x[1])[:15]:
    print(f"{k:22s} | {m28_tc.get(k,0):6.4f} | {m01A_tc.get(k,0):6.4f} | {m01B_tc.get(k,0):6.4f} | {aug28_named.get(k,0):6.4f} | {updA[k]:6.4f} | {updB[k]:6.4f} | {m01B_sf.get(k,0):5.3f} | {m01B_fc.get(k,0):5.3f}")
print(f"{'Field_Rest':22s} | {1-sum(m28_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m01A_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m01B_tc.get(k,0) for k in aug28_named):6.4f} | {field_28:6.4f} | {fA:6.4f} | {fB:6.4f} |")
print("Top-8 UpdA:", [(k, round(v, 4)) for k, v in sorted(updA.items(), key=lambda x: -x[1])[:8]])
print("Top-8 UpdB:", [(k, round(v, 4)) for k, v in sorted(updB.items(), key=lambda x: -x[1])[:8]])

print("\n" + "=" * 102)
print(f"Q1 (408930) FURTHEST U.S. MAN — TUE SEP 1 DAY 3 UPDATE (Tie: 28={m28_tie:.4f}, A={m01A_tie:.4f}, B={m01B_tie:.4f})")
print("=" * 102)
print(f"{'Player':22s} | {'Cond28':7s} | {'CondA':7s} | {'CondB':7s} | {'UncondB':7s} | {'R3_B':5s} | {'R4_B':5s} | {'QF_B':5s} | {'SF_B':5s}")
for k, _ in sorted(m01B_cu.items(), key=lambda x: -x[1])[:12]:
    print(f"{k:22s} | {m28_cu.get(k,0):7.4f} | {m01A_cu.get(k,0):7.4f} | {m01B_cu.get(k,0):7.4f} | {m01B_uu.get(k,0):7.4f} | {'--':5s} | {m01B_r4[k]:5.3f} | {m01B_qf[k]:5.3f} | {m01B_sf[k]:5.3f}")

# ------------------------------------------------------------------------------
# PART 2: WTA EXACT 128-PLAYER BRACKET (46 OF 64 R1 MATCHES LOCKED!)
# ------------------------------------------------------------------------------
wta_r1_winners_01 = {
    # Q1 (13 locked)
    "Aryna Sabalenka", "Polina Iatcenko", "Oksana Selekhmeteva", "Kamilla Rakhimova",
    "Taylor Townsend", "Taylah Preston", "Karolina Pliskova", "Diana Shnaider",
    "Marta Kostyuk", "Ekaterina Alexandrova", "Donna Vekic", "Lanlana Tararudee",
    "Linda Noskova",
    # Q2 (14 locked)
    "Jessica Pegula", "Sofia Kenin", "Mananchaya Sawangkaew", "Leylah Fernandez",
    "Jasmine Paolini", "Lucrezia Stefanini", "Diane Parry", "Elina Svitolina",
    "Xinyu Wang", "Anna Kalinskaya", "Emma Navarro", "Caty McNally",
    "Katie Boulter", "Karolina Muchova",
    # Q3 (6 locked — NEW: Andreeva, Eva Lys!)
    "Mirra Andreeva",           # def. Janice Tjen 6-2 6-2!!
    "Eva Lys",                  # def. Gabriela Knutson 6-3 6-3
    "Lilli Tagger",
    "Amanda Anisimova",
    "Cristina Bucsa",
    "Himeno Sakatsume",
    # Q4 (13 locked — NEW: Swiatek, Keys, Bondar, Osaka, Siniakova, Sakkari, Starodubtseva, Rybakina!)
    "Iga Swiatek",              # def. Xiyu Wang 6-2 6-3!!
    "Nadia Podoroska",
    "Harriet Dart",
    "Marie Bouzkova",
    "Madison Keys",             # def. Alina Korneeva 7-5 6-4
    "Anna Bondar",              # def. Lucie Havlickova 6-3 6-3
    "Qinwen Zheng",
    "Naomi Osaka",              # def. Anastasia Zakharova 7-6(6) 7-6(3)
    "Katerina Siniakova",       # def. Cocciaretto (confirmed Osaka R2 opponent!)
    "Maria Timofeeva",
    "Maria Sakkari",            # def. Robin Montgomery 2-6 7-5 6-2
    "Yuliia Starodubtseva",     # def. Ella Seidel 6-2 6-2
    "Elena Rybakina",           # def. Thea Frodin 6-3 6-2!!
}

wta_r1_locked_01 = {}
for i in range(0, 128, 2):
    a, b = wta_bracket_raw[i], wta_bracket_raw[i+1]
    if a in wta_r1_winners_01:
        assert b not in wta_r1_winners_01
        wta_r1_locked_01[(a, b)] = a
    elif b in wta_r1_winners_01:
        wta_r1_locked_01[(a, b)] = b
print(f"\nWTA R1 locked count: {len(wta_r1_locked_01)} / 64 (expected 46)")
assert len(wta_r1_locked_01) == 46, f"Expected 46, got {len(wta_r1_locked_01)}"

def sim_wta(locked_r1=None, ryb_mix=None, sab_mix=None, elo_adj=None, r1_cal_override=False, n_trials=90000, seed=9500):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    if ryb_mix is None:
        ryb_mix = [(2130.0, 0.42), (2055.0, 0.30), (1955.0, 0.18), (1700.0, 0.10)]
    if sab_mix is None:
        sab_mix = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]

    # Optional R1 market-prob calibration for unseeded R1 foes (Gauff vs Sonmez ~0.89, Swiatek vs Wang ~0.89, etc.)
    r1_foe_adj = {}
    if r1_cal_override:
        r1_foe_adj = {
            "Camila Osorio": -25.0,
            "Xiyu Wang": -40.0,
            "Zeynep Sonmez": -40.0,
            "Thea Frodin": -55.0,
            "Janice Tjen": -35.0,
            "Elena-Gabriela Ruse": -35.0,
            "Anastasia Zakharova": -20.0,
        }

    tc = Counter(); fc = Counter(); sc = Counter()
    for re_e, wr in ryb_mix:
        for se_e, ws in sab_mix:
            w = wr * ws
            tr = max(2000, int(round(n_trials * w)))
            emap = dict(wta_cal_elo)
            for k, dv in r1_foe_adj.items():
                if k in emap:
                    emap[k] = emap[k] + dv
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

# Baseline Aug 28 WTA (standard & R1-calibrated)
w28_t, _, _ = sim_wta(locked_r1=None, r1_cal_override=False, n_trials=90000, seed=9501)
w28_cal_t, _, _ = sim_wta(locked_r1=None, r1_cal_override=True, n_trials=90000, seed=9511)

# Model A (Strict Outcome-Only + conservative Aug 30 Rybakina mix updated strictly for R1 win)
ryb_prior_30 = [(2130.0, 0.52), (2065.0, 0.28), (1970.0, 0.14), (1740.0, 0.06)]
wr_a = [w * p_bo3(e, 1715.0) for e, w in ryb_prior_30]
ryb_mix_A = [(e, ww / sum(wr_a)) for (e, _), ww in zip(ryb_prior_30, wr_a)]
w01A_t, w01A_f, w01A_sf = sim_wta(locked_r1=wta_r1_locked_01, ryb_mix=ryb_mix_A, r1_cal_override=False, n_trials=90000, seed=9520)

# Model B (Conservative Health/Form Bayes: Rybakina clean 6-3 6-2, Sabalenka clean, Swiatek clean, Andreeva 6-2 6-2, Osaka rusty 7-6 7-6)
# Note: Rybakina said "we'll see how I feel tomorrow", so retain 4% flare-up + 9% hampered tail!
ryb_mix_B = [(2130.0, 0.65), (2065.0, 0.22), (1970.0, 0.09), (1740.0, 0.04)]
sab_mix_B = [(2225.0, 0.54), (2175.0, 0.33), (2085.0, 0.13)]
wta_tweaks_B = {
    "Iga Swiatek":      wta_cal_elo["Iga Swiatek"] + 6.0,       # Clean 6-2 6-3
    "Mirra Andreeva":   wta_cal_elo["Mirra Andreeva"] + 12.0,   # Crushed Tjen 6-2 6-2
    "Naomi Osaka":      wta_cal_elo["Naomi Osaka"] - 10.0,      # Rusty 7-6 7-6 vs #101 Zakharova
    "Jessica Pegula":   wta_cal_elo["Jessica Pegula"] + 6.0,
    "Amanda Anisimova": wta_cal_elo["Amanda Anisimova"] + 10.0,
    "Karolina Muchova": wta_cal_elo["Karolina Muchova"] + 10.0,
}
w01B_t, w01B_f, w01B_sf = sim_wta(
    locked_r1=wta_r1_locked_01, ryb_mix=ryb_mix_B, sab_mix=sab_mix_B,
    elo_adj=wta_tweaks_B, r1_cal_override=False, n_trials=90000, seed=9530
)

# Model C (Same as B but with R1 market-prob calibration so Gauff vs Sonmez ~0.89 instead of 0.85)
w01C_t, w01C_f, w01C_sf = sim_wta(
    locked_r1=wta_r1_locked_01, ryb_mix=ryb_mix_B, sab_mix=sab_mix_B,
    elo_adj=wta_tweaks_B, r1_cal_override=True, n_trials=90000, seed=9540
)

w_field_28 = 1.0 - sum(aug28_wta_exact.values())
def bayes_update_wta(mc_new, mc_base):
    raw = {}
    for k, p28 in aug28_wta_exact.items():
        raw[k] = p28 * (mc_new.get(k, 0.0) / max(1e-6, mc_base.get(k, 1e-6)))
    mc28_f = 1.0 - sum(mc_base.get(k, 0.0) for k in aug28_wta_exact)
    mcnew_f = 1.0 - sum(mc_new.get(k, 0.0) for k in aug28_wta_exact)
    raw_f = w_field_28 * (mcnew_f / max(1e-6, mc28_f))
    tot = sum(raw.values()) + raw_f
    return {k: v / tot for k, v in raw.items()}, raw_f / tot, tot

wupdA, wfA, wtotA = bayes_update_wta(w01A_t, w28_t)
wupdB, wfB, wtotB = bayes_update_wta(w01B_t, w28_t)
wupdC, wfC, wtotC = bayes_update_wta(w01C_t, w28_cal_t)

print("\n" + "=" * 108)
print(f"Q2 (608158) WOMEN'S SINGLES — TUE SEP 1 DAY 3 BAYESIAN UPDATE (Pre-norm: A={wtotA:.4f}, B={wtotB:.4f}, C={wtotC:.4f})")
print("=" * 108)
print(f"{'Player':20s} | {'MC28':6s} | {'MC01B':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'UpdC(cal)':9s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(wupdC.items(), key=lambda x: -x[1])[:12]:
    print(f"{k:20s} | {w28_t[k]:6.4f} | {w01B_t[k]:6.4f} | {aug28_wta_exact[k]:6.4f} | {wupdA[k]:6.4f} | {wupdB[k]:6.4f} | {wupdC[k]:9.4f} | {w01B_sf[k]:5.3f} | {w01B_f[k]:5.3f}")
print("WTA Top-8 UpdA:", [(k, round(v, 4)) for k, v in sorted(wupdA.items(), key=lambda x: -x[1])[:8]])
print("WTA Top-8 UpdB:", [(k, round(v, 4)) for k, v in sorted(wupdB.items(), key=lambda x: -x[1])[:8]])
print("WTA Top-8 UpdC:", [(k, round(v, 4)) for k, v in sorted(wupdC.items(), key=lambda x: -x[1])[:8]])
