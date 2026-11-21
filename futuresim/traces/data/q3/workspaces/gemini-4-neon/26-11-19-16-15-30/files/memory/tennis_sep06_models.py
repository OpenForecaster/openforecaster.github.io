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
# DAY 8 (SUNDAY SEP 6, 2026, ~23:50 GMT / 7:50 PM ET) STANDALONE BAYES MC
# Batch: tennis (891014 ATP Title, 408930 Furthest U.S. Man, 608158 WTA Title)
# ATP: 64/64 R1 + 32/32 R2 + 16/16 R3 + 3/8 R4 LOCKED!
#   - Sat night R3: Zverev d. Tabilo, Gea d. M.Zheng, BVDZ d. Bergs, Tien d. Mensik!
#   - Sun R4: Alcaraz d. Paul, Tiafoe d. Medvedev, Michelsen d. Etcheverry!
#   - ALL-AMERICAN QF LOCKED: Tiafoe vs Michelsen (guarantees US man in SF!)
# WTA: 64/64 R1 + 32/32 R2 + 16/16 R3 + 2/8 R4 LOCKED!
#   - Sat night R3: Jovic d. Eala, Osaka d. Mertens (Achilles niggle), Rybakina d. Starodubtseva!
#   - Sun R4: Sabalenka d. Townsend, Noskova d. Kostyuk!
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
    "Alexander Zverev":      2166,
    "Arthur Fils":           2084,
    "Ben Shelton":           2082,
    "Taylor Fritz":          2048,
    "Rafael Jodar":          2056,
    "Felix Auger-Aliassime": 2015,
    "Frances Tiafoe":        1998,
    "Brandon Nakashima":     1992,
    "Tommy Paul":            1984,
    "Learner Tien":          1976,
    "Daniil Medvedev":       2002,
    "Flavio Cobolli":        1998,
    "Jakub Mensik":          2002,
    "Alex de Minaur":        1984,
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

atp_replacements_04 = {
    "Casper Ruud":        "Arthur Gea",
    "Marin Cilic":        "Otto Virtanen",
    "Thanasi Kokkinakis": "Yunchaokete Bu",
    "Q_1":  "Grigor Dimitrov",   "Q_2":  "Harry Wendelken",
    "Q_3":  "Dalibor Svrcina",   "Q_4":  "Francesco Passaro",
    "Q_5":  "Andrea Guerrieri",  "Q_6":  "Shintaro Mochizuki",
    "Q_7":  "Jurij Rodionov",    "Q_8":  "Zsombor Piros",
    "Q_9":  "Tomas Barrios Vera","Q_10": "Nishesh Basavareddy",
    "Q_11": "Tristan Schoolkate","Q_12": "Hugo Gaston",
    "Q_13": "Rei Sakamoto",      "Q_14": "Federico Cina",
    "Q_15": "Jacob Fearnley",    "Q_16": "Toby Samuel",
    "Q_17": "Lloyd Harris",      "Q_18": "Coleman Wong",
}
atp_bracket_04 = [atp_replacements_04.get(x, x) for x in atp_bracket_raw]

us_men_04 = {
    "Taylor Fritz", "Ben Shelton", "Frances Tiafoe", "Learner Tien",
    "Brandon Nakashima", "Tommy Paul",
    "Alex Michelsen", "Marcos Giron", "Zachary Svajda", "Jenson Brooksby",
    "Aleksandar Kovacevic", "Martin Damm", "Darwin Blanch", "J.J. Wolf",
    "Stefan Gorzny", "Jack Kennedy", "Michael Zheng", "Nishesh Basavareddy",
}
us_men_28 = set(us_men_04) - {"Nishesh Basavareddy"} | {"Q_4", "Q_10"}

atp_r1_winners = {
    "Alexander Zverev", "Quentin Halys", "Alexei Popyrin", "Alejandro Tabilo",
    "Luciano Darderi", "Dalibor Svrcina", "Dane Sweeny", "Lorenzo Musetti",
    "Yunchaokete Bu", "Michael Zheng", "Zachary Svajda", "Arthur Gea",
    "Zizou Bergs", "Jesper De Jong", "Botic van de Zandschulp", "Alex de Minaur",
    "Felix Auger-Aliassime", "Karen Khachanov", "Benjamin Bonzi", "Ignacio Buse",
    "Jakub Mensik", "Jurij Rodionov", "Gael Monfils", "Learner Tien",
    "Taylor Fritz", "Mattia Bellucci", "Jan-Lennard Struff", "Francisco Cerundolo",
    "Alexander Blockx", "Marco Trungelliti", "Tristan Schoolkate", "Flavio Cobolli",
    "Daniil Medvedev", "Stefan Gorzny", "Jaume Munar", "Arthur Rinderknech",
    "Valentin Vacherot", "Kamil Majchrzak", "Rei Sakamoto", "Frances Tiafoe",
    "Brandon Nakashima", "Alex Michelsen", "Daniel Merida", "Andrey Rublev",
    "Tomas Martin Etcheverry", "Jacob Fearnley", "Matteo Berrettini", "Mariano Navone",
    "Ben Shelton", "Hubert Hurkacz", "Denis Shapovalov", "Luca Van Assche",
    "Jiri Lehecka", "Toby Samuel", "Lloyd Harris", "Stefanos Tsitsipas",
    "Alexander Bublik", "Adrian Mannarino", "Dino Prizmic", "Tommy Paul",
    "James Duckworth", "Yibing Wu", "Jaime Faria", "Carlos Alcaraz",
}
atp_r2_winners = {
    "Alexander Zverev", "Alejandro Tabilo", "Luciano Darderi", "Dane Sweeny",
    "Michael Zheng", "Arthur Gea", "Zizou Bergs", "Botic van de Zandschulp",
    "Karen Khachanov", "Benjamin Bonzi", "Jakub Mensik", "Learner Tien",
    "Taylor Fritz", "Francisco Cerundolo", "Alexander Blockx", "Flavio Cobolli",
    "Daniil Medvedev", "Arthur Rinderknech", "Valentin Vacherot", "Frances Tiafoe",
    "Alex Michelsen", "Daniel Merida", "Tomas Martin Etcheverry", "Mariano Navone",
    "Ben Shelton", "Denis Shapovalov", "Jiri Lehecka", "Stefanos Tsitsipas",
    "Alexander Bublik", "Tommy Paul", "Yibing Wu", "Carlos Alcaraz",
}
atp_r3_winners_06 = {
    "Alexander Zverev", "Luciano Darderi", "Arthur Gea", "Botic van de Zandschulp",
    "Karen Khachanov", "Learner Tien", "Francisco Cerundolo", "Alexander Blockx",
    "Daniil Medvedev", "Frances Tiafoe", "Alex Michelsen", "Tomas Martin Etcheverry",
    "Ben Shelton", "Stefanos Tsitsipas", "Tommy Paul", "Carlos Alcaraz",
}
atp_r4_winners_06 = {
    "Frances Tiafoe", "Alex Michelsen", "Carlos Alcaraz",
}

atp_r1_locked = {}
for i in range(0, 128, 2):
    a, b = atp_bracket_04[i], atp_bracket_04[i+1]
    atp_r1_locked[(a, b)] = a if a in atp_r1_winners else b
atp_r2_locked = {}
for i in range(0, 128, 4):
    w1 = atp_r1_locked[(atp_bracket_04[i], atp_bracket_04[i+1])]
    w2 = atp_r1_locked[(atp_bracket_04[i+2], atp_bracket_04[i+3])]
    atp_r2_locked[(w1, w2)] = w1 if w1 in atp_r2_winners else w2
atp_r3_locked = {}
for i in range(0, 128, 8):
    r2a = atp_r2_locked[(atp_r1_locked[(atp_bracket_04[i], atp_bracket_04[i+1])],
                         atp_r1_locked[(atp_bracket_04[i+2], atp_bracket_04[i+3])])]
    r2b = atp_r2_locked[(atp_r1_locked[(atp_bracket_04[i+4], atp_bracket_04[i+5])],
                         atp_r1_locked[(atp_bracket_04[i+6], atp_bracket_04[i+7])])]
    atp_r3_locked[(r2a, r2b)] = r2a if r2a in atp_r3_winners_06 else r2b
atp_r4_locked = {}
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
    if r3a in atp_r4_winners_06:
        atp_r4_locked[(r3a, r3b)] = r3a
    elif r3b in atp_r4_winners_06:
        atp_r4_locked[(r3a, r3b)] = r3b

assert len(atp_r1_locked) == 64 and len(atp_r2_locked) == 32 and len(atp_r3_locked) == 16 and len(atp_r4_locked) == 3, \
    (len(atp_r1_locked), len(atp_r2_locked), len(atp_r3_locked), len(atp_r4_locked))

extra_atp_elo = {
    "Grigor Dimitrov": 1905.0, "Harry Wendelken": 1815.0, "Dalibor Svrcina": 1835.0,
    "Francesco Passaro": 1830.0, "Andrea Guerrieri": 1810.0, "Shintaro Mochizuki": 1835.0,
    "Jurij Rodionov": 1855.0, "Zsombor Piros": 1830.0, "Tomas Barrios Vera": 1825.0,
    "Nishesh Basavareddy": 1845.0, "Tristan Schoolkate": 1840.0, "Arthur Gea": 1815.0,
    "Otto Virtanen": 1840.0, "Hugo Gaston": 1835.0, "Rei Sakamoto": 1840.0,
    "Federico Cina": 1825.0, "Jacob Fearnley": 1855.0, "Toby Samuel": 1865.0,
    "Lloyd Harris": 1855.0, "Coleman Wong": 1855.0, "Yunchaokete Bu": 1865.0,
    "Dane Sweeny": 1835.0,
}

def sim_atp(bracket, elo_dict, us_set, locked_r1=None, locked_r2=None, locked_r3=None, locked_r4=None,
            alc_mix=None, tia_mix=None, zve_mix=None, elo_tweaks=None,
            n_trials=80000, seed=9600):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}; locked_r2 = locked_r2 or {}
    locked_r3 = locked_r3 or {}; locked_r4 = locked_r4 or {}
    elos_base = []
    for nm in bracket:
        if nm.startswith("Q_"): el = 1830.0
        elif nm in elo_dict: el = float(elo_dict[nm])
        elif nm in extra_atp_elo: el = float(extra_atp_elo[nm])
        else: el = 1840.0
        if elo_tweaks and nm in elo_tweaks: el += float(elo_tweaks[nm])
        elos_base.append(el)
    alc_idx = bracket.index("Carlos Alcaraz")
    djo_idx = bracket.index("Novak Djokovic")
    tia_idx = bracket.index("Frances Tiafoe")
    zve_idx = bracket.index("Alexander Zverev")
    us_idxs = {i for i, nm in enumerate(bracket) if nm in us_set}
    if alc_mix is None: alc_mix = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
    djo_elim = ("Mariano Navone", "Novak Djokovic") in locked_r1
    djo_mix = [(2100.0, 1.0)] if djo_elim else [(2135.0, 0.55), (2075.0, 0.30), (1985.0, 0.15)]
    if tia_mix is None: tia_mix = [(0.0, 0.78), (-35.0, 0.16), (-95.0, 0.06)]
    if zve_mix is None: zve_mix = [(0.0, 1.0)]

    locked_r1_slots = {}
    for k in range(0, 128, 2):
        pair = (bracket[k], bracket[k+1])
        if pair in locked_r1:
            wname = locked_r1[pair]
            locked_r1_slots[k] = k if wname == bracket[k] else k + 1
    def to_idx_pairs(lm):
        out = {}
        for (a_nm, b_nm), w_nm in lm.items():
            ia, ib = bracket.index(a_nm), bracket.index(b_nm)
            iw = ia if w_nm == a_nm else ib
            out[(ia, ib)] = iw; out[(ib, ia)] = iw
        return out
    l2p = to_idx_pairs(locked_r2); l3p = to_idx_pairs(locked_r3); l4p = to_idx_pairs(locked_r4)

    tc = Counter(); fc = Counter(); r4c = Counter(); qfc = Counter(); sfc = Counter()
    uncond_us = Counter(); split_us = Counter(); tie_rate = 0.0
    for ae, wa in alc_mix:
        for de, wd in djo_mix:
            for td, wt in tia_mix:
                for zd, wz in zve_mix:
                    w = wa * wd * wt * wz
                    tr = max(800, int(round(n_trials * w)))
                    elos = list(elos_base)
                    elos[alc_idx] = float(ae); elos[djo_idx] = float(de)
                    elos[tia_idx] = elos_base[tia_idx] + float(td)
                    elos[zve_idx] = elos_base[zve_idx] + float(zd)
                    pc = {}
                    def gp(i, j):
                        k = (elos[i], elos[j])
                        v = pc.get(k)
                        if v is None:
                            v = p_bo5(elos[i], elos[j]); pc[k] = v
                        return v
                    ltc = Counter(); lfc = Counter(); lr4 = Counter(); lqf = Counter(); lsf = Counter()
                    luc = Counter(); lsp = Counter(); ties = 0
                    for _ in range(tr):
                        cur = list(range(128)); best_rnd = 0; best_us = []; rnd = 1
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
                                if rnd == 1 and k in locked_r1_slots:
                                    win = locked_r1_slots[k]; los = b if win == a else a
                                elif rnd == 2 and (a, b) in l2p:
                                    win = l2p[(a, b)]; los = b if win == a else a
                                elif rnd == 3 and (a, b) in l3p:
                                    win = l3p[(a, b)]; los = b if win == a else a
                                elif rnd == 4 and (a, b) in l4p:
                                    win = l4p[(a, b)]; los = b if win == a else a
                                else:
                                    if rng.random() < gp(a, b): win, los = a, b
                                    else: win, los = b, a
                                nxt.append(win)
                                if los in us_idxs:
                                    if rnd > best_rnd: best_rnd = rnd; best_us = [los]
                                    elif rnd == best_rnd: best_us.append(los)
                            cur = nxt; rnd += 1
                        champ = cur[0]; ltc[champ] += 1
                        if champ in us_idxs: best_rnd = 8; best_us = [champ]
                        if len(best_us) == 1:
                            luc[best_us[0]] += 1
                            lsp[best_us[0]] += 1.0
                        else:
                            ties += 1
                            for u in best_us:
                                lsp[u] += 1.0 / len(best_us)
                    for p, c in ltc.items(): tc[bracket[p]] += w * (c / tr)
                    for p, c in lfc.items(): fc[bracket[p]] += w * (c / tr)
                    for p, c in lr4.items(): r4c[bracket[p]] += w * (c / tr)
                    for p, c in lqf.items(): qfc[bracket[p]] += w * (c / tr)
                    for p, c in lsf.items(): sfc[bracket[p]] += w * (c / tr)
                    for p, c in luc.items(): uncond_us[bracket[p]] += w * (c / tr)
                    for p, c in lsp.items(): split_us[bracket[p]] += w * (c / tr)
                    tie_rate += w * (ties / tr)
    cond_us = {nm: v / (1.0 - tie_rate) for nm, v in uncond_us.items()}
    return tc, fc, r4c, qfc, sfc, cond_us, uncond_us, split_us, tie_rate

regimes_cal = [
    ("Market-Implied", 0.50, atp_mkt_elo),
    ("Pre-Draw Talent", 0.30, {**atp_mkt_elo, "Taylor Fritz": 2062, "Ben Shelton": 2084, "Arthur Fils": 2078, "Alexander Zverev": 2158}),
    ("BO5/NY Pedigree", 0.20, {**atp_mkt_elo, "Taylor Fritz": 2070, "Ben Shelton": 2072, "Frances Tiafoe": 2012, "Tommy Paul": 1998, "Brandon Nakashima": 1988, "Learner Tien": 1966, "Arthur Fils": 2068}),
]

def run_atp_blend(bracket, us_set, locked_r1, locked_r2=None, locked_r3=None, locked_r4=None,
                  alc_mix=None, tia_mix=None, zve_mix=None, elo_tweaks=None, seed_base=9600):
    b_tc = Counter(); b_fc = Counter(); b_r4 = Counter(); b_qf = Counter(); b_sf = Counter()
    b_cond = Counter(); b_uncond = Counter(); b_split = Counter(); b_tie = 0.0
    for idx, (lbl, w, ed) in enumerate(regimes_cal):
        tc, fc, r4c, qfc, sfc, cu, uu, su, tr = sim_atp(
            bracket, ed, us_set, locked_r1=locked_r1, locked_r2=locked_r2, locked_r3=locked_r3, locked_r4=locked_r4,
            alc_mix=alc_mix, tia_mix=tia_mix, zve_mix=zve_mix,
            elo_tweaks=elo_tweaks, n_trials=80000, seed=seed_base + idx
        )
        b_tie += w * tr
        for k, v in tc.items(): b_tc[k] += w * v
        for k, v in fc.items(): b_fc[k] += w * v
        for k, v in r4c.items(): b_r4[k] += w * v
        for k, v in qfc.items(): b_qf[k] += w * v
        for k, v in sfc.items(): b_sf[k] += w * v
        for k, v in cu.items(): b_cond[k] += w * v
        for k, v in uu.items(): b_uncond[k] += w * v
        for k, v in su.items(): b_split[k] += w * v
    return b_tc, b_fc, b_r4, b_qf, b_sf, b_cond, b_uncond, b_split, b_tie

m28_tc, _, _, _, _, m28_cu, _, _, m28_tie = run_atp_blend(atp_bracket_raw, us_men_28, None, None, None, None, None, None, None, None, 9100)

# Exact Bayesian update for Alcaraz through R1 (Safiullin 1895), R2 (Faria 1840), R3 (Wu 1845), R4 (Paul 1984)
alc_prior = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
w_r1r4 = [w * p_bo5(e, 1895.0) * p_bo5(e, 1840.0) * p_bo5(e, 1845.0) * p_bo5(e, 1984.0) for e, w in alc_prior]
alc_mix_A = [(e, ww / sum(w_r1r4)) for (e, _), ww in zip(alc_prior, w_r1r4)]

# Model A: Strict outcome-only
m06A_tc, m06A_fc, m06A_r4, m06A_qf, m06A_sf, m06A_cu, m06A_uu, m06A_su, m06A_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked, atp_r2_locked, atp_r3_locked, atp_r4_locked, alc_mix_A, None, None, None, 9610
)

# Model B2: Form / H2H / Live-Odds Calibrated
# Check pairwise BO5 probs in B2 (Market-Implied regime):
#   Alcaraz (mean ~2235) vs Shelton (2070) -> 76.7%, vs Tiafoe (2032) -> 81.8%, vs Zverev (2140) -> 66.8%
#   Shelton (2070) vs Tsitsipas (1965) -> 68.9% (matches Racing Post -3.5 games @ 8/11!)
#   Tiafoe (2032) vs Michelsen (1980) -> 59.5% Tiafoe / 40.5% Michelsen!
#   Tien (2000) vs Khachanov (1983) -> 53.1% Tien / 46.9% Khachanov!
#   Cerundolo (1932) vs Blockx (1934) -> 49.6% / 50.4%!
#   Zverev (mean ~2140) vs Darderi (1917) -> 83.8%!
#   BVDZ (1920) vs Arthur Gea (1860) -> 60.9%!
alc_mix_B = [(2280.0, 0.62), (2175.0, 0.34), (2045.0, 0.04)]
tia_mix_B = [(0.0, 0.96), (-25.0, 0.04)]
zve_mix_B = [(0.0, 0.48), (-35.0, 0.36), (-75.0, 0.13), (-115.0, 0.03)]
zve_mix_C = [(0.0, 0.30), (-40.0, 0.40), (-80.0, 0.22), (-125.0, 0.08)]

tweaks_B2 = {
    "Frances Tiafoe":          +34.0,   # Crushed #7 Medvedev 3-0! 5 straight Top-10 wins, 9 of last 10! (1998 -> 2032)
    "Alex Michelsen":          +55.0,   # 12-0 IN SETS! Only man without a dropped set! First Slam QF! (1925 -> 1980)
    "Ben Shelton":             -12.0,   # 3 four-setters, 54 UEs, >2am Sat finish (2082 -> 2070)
    "Stefanos Tsitsipas":      +40.0,   # Beat #10 Fils & #18 Lehecka (1925 -> 1965)
    "Learner Tien":            +24.0,   # Gritty 5-set comeback over #17 Mensik! Slight 5-set fatigue offset (1976 -> 2000)
    "Karen Khachanov":         +38.0,   # Beat #3 FAA & Bonzi straight sets, rested (1945 -> 1983)
    "Francisco Cerundolo":     +22.0,   # Beat #9 Fritz from 0-2 down (1910 -> 1932)
    "Alexander Blockx":        +42.0,   # Beat #5 Cobolli 6-7 6-3 6-0 6-3 (1892 -> 1934)
    "Luciano Darderi":         +22.0,   # Clean R3 + beat Zverev in Rome (clay) May 2026 (1895 -> 1917)
    "Botic van de Zandschulp": +40.0,   # Beat #6 De Minaur & #31 Bergs (1880 -> 1920)
    "Arthur Gea":              +45.0,   # LL into R4, beat M. Zheng in 5 sets (1815 -> 1860)
}

m06B2_tc, m06B2_fc, m06B2_r4, m06B2_qf, m06B2_sf, m06B2_cu, m06B2_uu, m06B2_su, m06B2_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked, atp_r2_locked, atp_r3_locked, atp_r4_locked, alc_mix_B, tia_mix_B, zve_mix_B, tweaks_B2, 9720
)
m06C2_tc, m06C2_fc, m06C2_r4, m06C2_qf, m06C2_sf, m06C2_cu, m06C2_uu, m06C2_su, m06C2_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked, atp_r2_locked, atp_r3_locked, atp_r4_locked, alc_mix_B, tia_mix_B, zve_mix_C, tweaks_B2, 9820
)

fd_m, _, _, _ = devig_mid(fd_atp_28)
dk_m, _, _, _ = devig_mid(dk_atp_28)
cz_m, _, _, _ = devig_mid(cz_atp_28)
aug28_named = {}
for k in fd_atp_28:
    if k == "Field_Rest": continue
    bks = 0.45 * fd_m[k] + 0.40 * dk_m[k] + 0.15 * cz_m[k]
    aug28_named[k] = 0.45 * kalshi_atp_28[k] + 0.30 * bks + 0.25 * m28_tc.get(k, 0.0)
field_28 = max(0.0, 1.0 - sum(aug28_named.values()))

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

updA, _, _ = bayes_update_atp_full(m06A_tc)
updB2, _, _ = bayes_update_atp_full(m06B2_tc)
updC2, _, _ = bayes_update_atp_full(m06C2_tc)
blend_atp = {k: 0.25 * updA.get(k, 0) + 0.65 * updB2.get(k, 0) + 0.10 * updC2.get(k, 0) for k in set(updA) | set(updB2)}

print("=" * 116)
print("Q3 (891014) ATP DAY 8 (SUN SEP 6 ~7:50 PM ET) — ALCARAZ/TIAFOE/MICHELSEN IN QF; MEDVEDEV/MENSIK/PAUL OUT!")
print("=" * 116)
print(f"{'Player':22s} | {'MC06A':6s} | {'MC06B2':6s} | {'UpdA':6s} | {'UpdB2':6s} | {'UpdC2':6s} | {'Blend':6s} | {'QF_B2':5s} | {'SF_B2':5s} | {'F_B2':5s}")
for k, _ in sorted(blend_atp.items(), key=lambda x: -x[1])[:12]:
    print(f"{k:22s} | {m06A_tc.get(k,0):6.4f} | {m06B2_tc.get(k,0):6.4f} | {updA.get(k,0):6.4f} | {updB2.get(k,0):6.4f} | {updC2.get(k,0):6.4f} | {blend_atp[k]:6.4f} | {m06B2_qf.get(k,0):5.3f} | {m06B2_sf.get(k,0):5.3f} | {m06B2_fc.get(k,0):5.3f}")

print("\n" + "=" * 116)
print(f"Q1 (408930) FURTHEST U.S. MAN DAY 8 (TieRate: A={m06A_tie:.4f}, B2={m06B2_tie:.4f}, C2={m06C2_tie:.4f})")
print("=" * 116)
blend_us = {k: 0.30 * m06A_cu.get(k, 0) + 0.60 * m06B2_cu.get(k, 0) + 0.10 * m06C2_cu.get(k, 0) for k in set(m06A_cu) | set(m06B2_cu)}
blend_us_uu = {k: 0.30 * m06A_uu.get(k, 0) + 0.60 * m06B2_uu.get(k, 0) + 0.10 * m06C2_uu.get(k, 0) for k in set(m06A_uu) | set(m06B2_uu)}
blend_us_sp = {k: 0.30 * m06A_su.get(k, 0) + 0.60 * m06B2_su.get(k, 0) + 0.10 * m06C2_su.get(k, 0) for k in set(m06A_su) | set(m06B2_su)}
print(f"{'Player':20s} | {'CondA':6s} | {'CondB2':6s} | {'CondC2':6s} | {'BlendC':6s} | {'Uncond':6s} | {'Split':6s} | {'QF_B2':5s} | {'SF_B2':5s} | {'F_B2':5s}")
for k, _ in sorted(blend_us.items(), key=lambda x: -x[1])[:6]:
    print(f"{k:20s} | {m06A_cu.get(k,0):6.4f} | {m06B2_cu.get(k,0):6.4f} | {m06C2_cu.get(k,0):6.4f} | {blend_us[k]:6.4f} | {blend_us_uu[k]:6.4f} | {blend_us_sp[k]:6.4f} | {m06B2_qf[k]:5.3f} | {m06B2_sf[k]:5.3f} | {m06B2_fc[k]:5.3f}")

# ------------------------------------------------------------------------------
# PART 2: WTA DAY 8 (ALL 16/16 R3 + 2/8 R4 LOCKED: Sabalenka & Noskova IN QF!)
# ------------------------------------------------------------------------------
wta_r1_winners_06 = {
    "Aryna Sabalenka", "Polina Iatcenko", "Oksana Selekhmeteva", "Kamilla Rakhimova",
    "Taylor Townsend", "Taylah Preston", "Karolina Pliskova", "Diana Shnaider",
    "Marta Kostyuk", "Sloane Stephens", "Kimberly Birrell", "Ekaterina Alexandrova",
    "Ann Li", "Donna Vekic", "Lanlana Tararudee", "Linda Noskova",
    "Jessica Pegula", "Sofia Kenin", "Mananchaya Sawangkaew", "Leylah Fernandez",
    "Jasmine Paolini", "Lucrezia Stefanini", "Diane Parry", "Sorana Cirstea",
    "Elina Svitolina", "Maya Joint", "Xinyu Wang", "Anna Kalinskaya",
    "Emma Navarro", "Caty McNally", "Katie Boulter", "Karolina Muchova",
    "Mirra Andreeva", "Eva Lys", "Nikola Bartunkova", "Tatjana Maria",
    "Anastasia Potapova", "Arantxa Rus", "Lilli Tagger", "Amanda Anisimova",
    "Iva Jovic", "Francesca Jones", "Oleksandra Oliynykova", "Alexandra Eala",
    "Cristina Bucsa", "Himeno Sakatsume", "Paula Badosa", "Coco Gauff",
    "Iga Swiatek", "Nadia Podoroska", "Harriet Dart", "Marie Bouzkova",
    "Madison Keys", "Anna Bondar", "Yulia Putintseva", "Qinwen Zheng",
    "Naomi Osaka", "Katerina Siniakova", "Maria Timofeeva", "Elise Mertens",
    "Maria Sakkari", "Yuliia Starodubtseva", "Jessica Bouzas Maneiro", "Elena Rybakina",
}
wta_r2_winners_06 = {
    "Aryna Sabalenka", "Kamilla Rakhimova", "Taylor Townsend", "Diana Shnaider",
    "Marta Kostyuk", "Ekaterina Alexandrova", "Ann Li", "Linda Noskova",
    "Jessica Pegula", "Leylah Fernandez", "Jasmine Paolini", "Sorana Cirstea",
    "Elina Svitolina", "Anna Kalinskaya", "Emma Navarro", "Karolina Muchova",
    "Mirra Andreeva", "Nikola Bartunkova", "Anastasia Potapova", "Amanda Anisimova",
    "Iva Jovic", "Alexandra Eala", "Cristina Bucsa", "Coco Gauff",
    "Iga Swiatek", "Marie Bouzkova", "Madison Keys", "Qinwen Zheng",
    "Naomi Osaka", "Elise Mertens", "Yuliia Starodubtseva", "Elena Rybakina",
}
wta_r3_winners_06 = {
    "Aryna Sabalenka", "Taylor Townsend", "Marta Kostyuk", "Linda Noskova",
    "Jessica Pegula", "Sorana Cirstea", "Anna Kalinskaya", "Emma Navarro",
    "Mirra Andreeva", "Anastasia Potapova", "Iva Jovic", "Coco Gauff",
    "Iga Swiatek", "Qinwen Zheng", "Naomi Osaka", "Elena Rybakina",
}
wta_r4_winners_06 = {
    "Aryna Sabalenka", "Linda Noskova",
}

wta_r1_locked = {(wta_bracket_raw[i], wta_bracket_raw[i+1]): (wta_bracket_raw[i] if wta_bracket_raw[i] in wta_r1_winners_06 else wta_bracket_raw[i+1]) for i in range(0, 128, 2)}
wta_r2_locked = {}
for i in range(0, 128, 4):
    w1 = wta_r1_locked[(wta_bracket_raw[i], wta_bracket_raw[i+1])]
    w2 = wta_r1_locked[(wta_bracket_raw[i+2], wta_bracket_raw[i+3])]
    wta_r2_locked[(w1, w2)] = w1 if w1 in wta_r2_winners_06 else w2
wta_r3_locked = {}
for i in range(0, 128, 8):
    r2a = wta_r2_locked[(wta_r1_locked[(wta_bracket_raw[i], wta_bracket_raw[i+1])],
                         wta_r1_locked[(wta_bracket_raw[i+2], wta_bracket_raw[i+3])])]
    r2b = wta_r2_locked[(wta_r1_locked[(wta_bracket_raw[i+4], wta_bracket_raw[i+5])],
                         wta_r1_locked[(wta_bracket_raw[i+6], wta_bracket_raw[i+7])])]
    wta_r3_locked[(r2a, r2b)] = r2a if r2a in wta_r3_winners_06 else r2b
wta_r4_locked = {}
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
    if r3a in wta_r4_winners_06: wta_r4_locked[(r3a, r3b)] = r3a
    elif r3b in wta_r4_winners_06: wta_r4_locked[(r3a, r3b)] = r3b

assert len(wta_r3_locked) == 16 and len(wta_r4_locked) == 2

def sim_wta(locked_r1=None, locked_r2=None, locked_r3=None, locked_r4=None,
            ryb_mix=None, sab_mix=None, elo_adj=None, r1_cal_override=False, n_trials=100000, seed=9500):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}; locked_r2 = locked_r2 or {}
    locked_r3 = locked_r3 or {}; locked_r4 = locked_r4 or {}
    if ryb_mix is None: ryb_mix = [(2130.0, 0.42), (2055.0, 0.30), (1955.0, 0.18), (1700.0, 0.10)]
    if sab_mix is None: sab_mix = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]
    r1_foe_adj = {"Camila Osorio": -25.0, "Xiyu Wang": -40.0, "Zeynep Sonmez": -40.0, "Thea Frodin": -55.0,
                  "Janice Tjen": -35.0, "Elena-Gabriela Ruse": -35.0, "Anastasia Zakharova": -20.0} if r1_cal_override else {}
    tc = Counter(); fc = Counter(); sc = Counter(); qc = Counter()
    for re_e, wr in ryb_mix:
        for se_e, ws in sab_mix:
            w = wr * ws; tr = max(2000, int(round(n_trials * w)))
            emap = dict(wta_cal_elo)
            for k, dv in r1_foe_adj.items():
                if k in emap: emap[k] += dv
            if elo_adj: emap.update(elo_adj)
            emap["Elena Rybakina"] = re_e; emap["Aryna Sabalenka"] = se_e
            pc = {}
            def gp(ea, eb):
                k = (ea, eb); v = pc.get(k)
                if v is None: v = p_bo3(ea, eb); pc[k] = v
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
                        else: nxt.append(a if rng.random() < gp(emap[a], emap[b]) else b)
                    cur = nxt; rnd += 1
                ltc[cur[0]] += 1
            for p, c in ltc.items(): tc[p] += w * (c / tr)
            for p, c in lfc.items(): fc[p] += w * (c / tr)
            for p, c in lsc.items(): sc[p] += w * (c / tr)
            for p, c in lqc.items(): qc[p] += w * (c / tr)
    return tc, fc, sc, qc

w28_t, _, _, _ = sim_wta(None, None, None, None, None, None, None, False, 100000, 9501)
w28_cal_t, _, _, _ = sim_wta(None, None, None, None, None, None, None, True, 100000, 9511)

ryb_prior_30 = [(2130.0, 0.52), (2065.0, 0.28), (1970.0, 0.14), (1740.0, 0.06)]
wr_a = [w * p_bo3(e, 1715.0) * p_bo3(e, 1845.0) * p_bo3(e, 1795.0) for e, w in ryb_prior_30]
ryb_mix_A = [(e, ww / sum(wr_a)) for (e, _), ww in zip(ryb_prior_30, wr_a)]
sab_prior_28 = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]
ws_a = [w * p_bo3(e, 1845.0) * p_bo3(e, 1795.0) * p_bo3(e, 1795.0) * p_bo3(e, 1855.0) for e, w in sab_prior_28]
sab_mix_A = [(e, ww / sum(ws_a)) for (e, _), ww in zip(sab_prior_28, ws_a)]

w06A_t, w06A_f, w06A_sf, w06A_qf = sim_wta(wta_r1_locked, wta_r2_locked, wta_r3_locked, wta_r4_locked, ryb_mix_A, sab_mix_A, None, False, 100000, 9521)

# B2: Market-odds & form calibrated:
#   Sabalenka (~2202) vs Noskova (2009) -> 75.2% Sabalenka!
#   Pegula (2044) vs Cirstea (1888) -> 71.1% Pegula! (Matches Tennis Tonic 1.33/3.28 & DK Cirstea +221!)
#   Navarro (1960) vs Kalinskaya (1950) -> 51.4% Navarro! (Matches DK -117 / Pickswise -110!)
#   Gauff (2160) vs Jovic (1962) -> 75.8% Gauff! (Jovic played 3h03m epic!)
#   Andreeva (2050) vs Potapova (1932) -> 66.4% Andreeva! (Moderate +14 to avoid double-counting!)
#   Swiatek (2156) vs Qinwen Zheng (1987) -> 72.6% Swiatek!
#   Rybakina (~2123) vs Osaka (2015, Achilles niggle + MTO!) -> 65.0% Rybakina!
ryb_mix_B2 = [(2135.0, 0.85), (2070.0, 0.12), (1980.0, 0.03)]
sab_mix_B2 = [(2225.0, 0.65), (2175.0, 0.29), (2085.0, 0.06)]
wta_tweaks_B2 = {
    "Coco Gauff":           wta_cal_elo["Coco Gauff"] + 18.0,        # 2160 (0 sets lost, flow state)
    "Iga Swiatek":          wta_cal_elo["Iga Swiatek"] + 8.0,        # 2156 (0 sets lost, 7-1 H2H v Zheng)
    "Jessica Pegula":       wta_cal_elo["Jessica Pegula"] + 6.0,     # 2044 (71.1% vs Cirstea matching live odds)
    "Mirra Andreeva":       wta_cal_elo["Mirra Andreeva"] + 14.0,    # 2050 (RG champ, 0 sets lost; no double-count)
    "Linda Noskova":        wta_cal_elo["Linda Noskova"] + 24.0,     # 2009 (Wim champ, into QF!)
    "Emma Navarro":         wta_cal_elo["Emma Navarro"] + 35.0,      # 1960 (51.4% vs Kalinskaya matching DK -117!)
    "Anna Kalinskaya":      wta_cal_elo["Anna Kalinskaya"] + 35.0,   # 1950 (48.6% vs Navarro)
    "Sorana Cirstea":       wta_cal_elo["Sorana Cirstea"] + 10.0,    # 1888 (28.9% vs Pegula matching DK +221!)
    "Anastasia Potapova":   wta_cal_elo["Anastasia Potapova"] + 32.0,# 1932 (upset #10 Anisimova)
    "Qinwen Zheng":         wta_cal_elo["Qinwen Zheng"] + 22.0,      # 1987 (heroic comeback vs Keys)
    "Naomi Osaka":          wta_cal_elo["Naomi Osaka"] - 47.0,       # 2015 (Achilles niggle + MTO + emotional struggle!)
    "Iva Jovic":            wta_cal_elo["Iva Jovic"] + 30.0,         # 1962 (beat Eala in 3h03m epic)
}

w06B2_t, w06B2_f, w06B2_sf, w06B2_qf = sim_wta(wta_r1_locked, wta_r2_locked, wta_r3_locked, wta_r4_locked, ryb_mix_B2, sab_mix_B2, wta_tweaks_B2, False, 100000, 9532)
w06C2_t, w06C2_f, w06C2_sf, w06C2_qf = sim_wta(wta_r1_locked, wta_r2_locked, wta_r3_locked, wta_r4_locked, ryb_mix_B2, sab_mix_B2, wta_tweaks_B2, True, 100000, 9542)

w_field_28 = 1.0 - sum(aug28_wta_exact.values())
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

wupdA, _, _ = bayes_update_wta_full(w06A_t, w28_t)
wupdB2, _, _ = bayes_update_wta_full(w06B2_t, w28_t)
wupdC2, _, _ = bayes_update_wta_full(w06C2_t, w28_cal_t)
blend_wta = {k: 0.35 * wupdA.get(k, 0) + 0.35 * wupdB2.get(k, 0) + 0.30 * wupdC2.get(k, 0) for k in set(wupdA) | set(wupdB2)}

print("\n" + "=" * 116)
print("Q2 (608158) WTA DAY 8 (SUN SEP 6 ~7:50 PM ET) — SABALENKA/NOSKOVA IN QF; KOSTYUK/EALA OUT; OSAKA ACHILLES!")
print("=" * 116)
print(f"{'Player':20s} | {'MC06A':6s} | {'MC06B2':6s} | {'UpdA':6s} | {'UpdB2':6s} | {'UpdC2':6s} | {'Blend':6s} | {'QF_B2':5s} | {'SF_B2':5s} | {'F_B2':5s}")
for k, _ in sorted(blend_wta.items(), key=lambda x: -x[1])[:12]:
    print(f"{k:20s} | {w06A_t.get(k,0):6.4f} | {w06B2_t.get(k,0):6.4f} | {wupdA.get(k,0):6.4f} | {wupdB2.get(k,0):6.4f} | {wupdC2.get(k,0):6.4f} | {blend_wta[k]:6.4f} | {w06B2_qf.get(k,0):5.3f} | {w06B2_sf.get(k,0):5.3f} | {w06B2_f.get(k,0):5.3f}")
