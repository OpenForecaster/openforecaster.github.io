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
# DAY 7 (SATURDAY SEP 5, 2026, ~21:30 GMT / 5:30 PM ET) STANDALONE BAYES MC
# Batch: tennis (891014 ATP Title, 408930 Furthest U.S. Man, 608158 WTA Title)
# ATP: 64/64 R1 + 32/32 R2 + 12/16 R3 LOCKED! (Fritz & Cobolli OUT!)
# WTA: 64/64 R1 + 32/32 R2 + 13/16 R3 LOCKED! (Svitolina, Anisimova, Keys OUT!)
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
atp_r3_winners_05 = {
    "Luciano Darderi",
    "Karen Khachanov", "Francisco Cerundolo", "Alexander Blockx",
    "Daniil Medvedev", "Frances Tiafoe", "Alex Michelsen", "Tomas Martin Etcheverry",
    "Ben Shelton", "Stefanos Tsitsipas", "Tommy Paul", "Carlos Alcaraz",
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
    if r2a in atp_r3_winners_05:
        atp_r3_locked[(r2a, r2b)] = r2a
    elif r2b in atp_r3_winners_05:
        atp_r3_locked[(r2a, r2b)] = r2b

assert len(atp_r1_locked) == 64 and len(atp_r2_locked) == 32 and len(atp_r3_locked) == 12

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

def sim_atp(bracket, elo_dict, us_set, locked_r1=None, locked_r2=None, locked_r3=None,
            alc_mix=None, tia_mix=None, zve_mix=None, elo_tweaks=None,
            n_trials=60000, seed=9400):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}; locked_r2 = locked_r2 or {}; locked_r3 = locked_r3 or {}
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
    l2p = to_idx_pairs(locked_r2); l3p = to_idx_pairs(locked_r3)

    tc = Counter(); fc = Counter(); r4c = Counter(); qfc = Counter(); sfc = Counter()
    uncond_us = Counter(); tie_rate = 0.0
    for ae, wa in alc_mix:
        for de, wd in djo_mix:
            for td, wt in tia_mix:
                for zd, wz in zve_mix:
                    w = wa * wd * wt * wz
                    tr = max(600, int(round(n_trials * w)))
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
                    luc = Counter(); ties = 0
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

def run_atp_blend(bracket, us_set, locked_r1, locked_r2=None, locked_r3=None,
                  alc_mix=None, tia_mix=None, zve_mix=None, elo_tweaks=None, seed_base=9400):
    b_tc = Counter(); b_fc = Counter(); b_r4 = Counter(); b_qf = Counter(); b_sf = Counter()
    b_cond = Counter(); b_uncond = Counter(); b_tie = 0.0
    for idx, (lbl, w, ed) in enumerate(regimes_cal):
        tc, fc, r4c, qfc, sfc, cu, uu, tr = sim_atp(
            bracket, ed, us_set, locked_r1=locked_r1, locked_r2=locked_r2, locked_r3=locked_r3,
            alc_mix=alc_mix, tia_mix=tia_mix, zve_mix=zve_mix,
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

m28_tc, _, _, _, _, m28_cu, _, m28_tie = run_atp_blend(atp_bracket_raw, us_men_28, None, None, None, None, None, None, None, 9100)

alc_prior = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
w_r1r3 = [w * p_bo5(e, 1895.0) * p_bo5(e, 1845.0) * p_bo5(e, 1860.0) for e, w in alc_prior]
alc_mix_A = [(e, ww / sum(w_r1r3)) for (e, _), ww in zip(alc_prior, w_r1r3)]

# Model A: Strict outcome-only
m05A_tc, m05A_fc, m05A_r4, m05A_qf, m05A_sf, m05A_cu, m05A_uu, m05A_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked, atp_r2_locked, atp_r3_locked, alc_mix_A, None, None, None, 9610
)

# Model B2: Realistic Form / H2H / Fatigue Calibrated (Medvedev 60.5% vs Tiafoe, Michelsen 61% vs Etcheverry, Shelton 68% vs Tsitsipas)
alc_mix_B = [(2280.0, 0.50), (2175.0, 0.43), (2045.0, 0.06), (1750.0, 0.01)]
tia_mix_B = [(0.0, 0.90), (-30.0, 0.10)]
zve_mix_B = [(0.0, 0.30), (-35.0, 0.40), (-75.0, 0.22), (-120.0, 0.08)]
zve_mix_C = [(0.0, 0.18), (-45.0, 0.42), (-90.0, 0.28), (-140.0, 0.12)]

tweaks_B2 = {
    "Daniil Medvedev":         +54.0,   # 9-0 sets, broken ONCE in 3 matches, ~5-1 H2H vs Tiafoe! (2002 -> 2056)
    "Frances Tiafoe":          +2.0,    # 9-0 sets (beat Vacherot cleanly), trails Medvedev H2H (1998 -> 2000)
    "Alex Michelsen":          +42.0,   # 9-0 sets! Beat #16 Nakashima & Merida cleanly (1925 -> 1967)
    "Tomas Martin Etcheverry": +10.0,   # Clay specialist into R4 (1895 -> 1905)
    "Ben Shelton":             -12.0,   # 54 UEs, 3 four-setters, 4 TBs, finished >2am Sat! (2082 -> 2070)
    "Stefanos Tsitsipas":      +40.0,   # Resurgent under Mouratoglou! Beat #10 Fils & #18 Lehecka (1925 -> 1965)
    "Tommy Paul":              -12.0,   # 5-setter vs Bublik + 0-5 recent H2H vs Alcaraz (1984 -> 1972)
    "Learner Tien":            +22.0,   # 0 sets lost, 1-0 H2H vs Mensik (1976 -> 1998)
    "Jakub Mensik":            +6.0,    # 1 set lost (2002 -> 2008)
    "Karen Khachanov":         +35.0,   # Beat #3 FAA + Bonzi straight sets, locked R4 in Q2! (1945 -> 1980)
    "Francisco Cerundolo":     +22.0,   # Stunned #9 Fritz from 0-2 down (1910 -> 1932)
    "Alexander Blockx":        +42.0,   # Stunned #5 Cobolli 6-7 6-3 6-0 6-3 (1892 -> 1934)
    "Luciano Darderi":         +18.0,   # Clean 6-4 6-3 6-3 vs Sweeny (1895 -> 1913)
    "Botic van de Zandschulp": +30.0,   # Crushed #6 De Minaur
    "Alejandro Tabilo":        +12.0,
    "Zizou Bergs":             +10.0,
    "Michael Zheng":           +45.0,
    "Arthur Gea":              +20.0,
}

m05B2_tc, m05B2_fc, m05B2_r4, m05B2_qf, m05B2_sf, m05B2_cu, m05B2_uu, m05B2_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked, atp_r2_locked, atp_r3_locked, alc_mix_B, tia_mix_B, zve_mix_B, tweaks_B2, 9720
)
m05C2_tc, m05C2_fc, m05C2_r4, m05C2_qf, m05C2_sf, m05C2_cu, m05C2_uu, m05C2_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked, atp_r2_locked, atp_r3_locked, alc_mix_B, tia_mix_B, zve_mix_C, tweaks_B2, 9820
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

updA, _, _ = bayes_update_atp_full(m05A_tc)
updB2, _, _ = bayes_update_atp_full(m05B2_tc)
updC2, _, _ = bayes_update_atp_full(m05C2_tc)
blend_atp = {k: 0.25 * updA.get(k, 0) + 0.65 * updB2.get(k, 0) + 0.10 * updC2.get(k, 0) for k in set(updA) | set(updB2)}

print("=" * 116)
print("Q3 (891014) ATP REFINED (B2: Med 60.5% v Tia, Mich 61% v Etc, Shel 68% v Tsi)")
print("=" * 116)
print(f"{'Player':22s} | {'MC05A':6s} | {'MC05B2':6s} | {'UpdA':6s} | {'UpdB2':6s} | {'UpdC2':6s} | {'Blend':6s} | {'QF_B2':5s} | {'SF_B2':5s} | {'F_B2':5s}")
for k, _ in sorted(blend_atp.items(), key=lambda x: -x[1])[:12]:
    print(f"{k:22s} | {m05A_tc.get(k,0):6.4f} | {m05B2_tc.get(k,0):6.4f} | {updA.get(k,0):6.4f} | {updB2.get(k,0):6.4f} | {updC2.get(k,0):6.4f} | {blend_atp[k]:6.4f} | {m05B2_qf.get(k,0):5.3f} | {m05B2_sf.get(k,0):5.3f} | {m05B2_fc.get(k,0):5.3f}")

print("\n" + "=" * 116)
print(f"Q1 (408930) FURTHEST U.S. MAN REFINED (Tie: A={m05A_tie:.4f}, B2={m05B2_tie:.4f}, C2={m05C2_tie:.4f})")
print("=" * 116)
blend_us = {k: 0.30 * m05A_cu.get(k, 0) + 0.60 * m05B2_cu.get(k, 0) + 0.10 * m05C2_cu.get(k, 0) for k in set(m05A_cu) | set(m05B2_cu)}
print(f"{'Player':22s} | {'CondA':7s} | {'CondB2':7s} | {'CondC2':7s} | {'Blend':7s} | {'R4_B2':5s} | {'QF_B2':5s} | {'SF_B2':5s} | {'F_B2':5s}")
for k, _ in sorted(blend_us.items(), key=lambda x: -x[1])[:6]:
    print(f"{k:22s} | {m05A_cu.get(k,0):7.4f} | {m05B2_cu.get(k,0):7.4f} | {m05C2_cu.get(k,0):7.4f} | {blend_us[k]:7.4f} | {m05B2_r4[k]:5.3f} | {m05B2_qf[k]:5.3f} | {m05B2_sf[k]:5.3f} | {m05B2_fc[k]:5.3f}")

# ------------------------------------------------------------------------------
# PART 2: WTA REFINED (NO double-counting Andreeva; Reuters-confirmed healthy Rybakina + Starodubtseva H2H)
# ------------------------------------------------------------------------------
wta_r1_winners_05 = {
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
wta_r2_winners_05 = {
    "Aryna Sabalenka", "Kamilla Rakhimova", "Taylor Townsend", "Diana Shnaider",
    "Marta Kostyuk", "Ekaterina Alexandrova", "Ann Li", "Linda Noskova",
    "Jessica Pegula", "Leylah Fernandez", "Jasmine Paolini", "Sorana Cirstea",
    "Elina Svitolina", "Anna Kalinskaya", "Emma Navarro", "Karolina Muchova",
    "Mirra Andreeva", "Nikola Bartunkova", "Anastasia Potapova", "Amanda Anisimova",
    "Iva Jovic", "Alexandra Eala", "Cristina Bucsa", "Coco Gauff",
    "Iga Swiatek", "Marie Bouzkova", "Madison Keys", "Qinwen Zheng",
    "Naomi Osaka", "Elise Mertens", "Yuliia Starodubtseva", "Elena Rybakina",
}
wta_r3_winners_05 = {
    "Aryna Sabalenka", "Taylor Townsend", "Marta Kostyuk", "Linda Noskova",
    "Jessica Pegula", "Sorana Cirstea", "Anna Kalinskaya", "Emma Navarro",
    "Mirra Andreeva", "Anastasia Potapova", "Coco Gauff",
    "Iga Swiatek", "Qinwen Zheng",
}

wta_r1_locked = {(wta_bracket_raw[i], wta_bracket_raw[i+1]): (wta_bracket_raw[i] if wta_bracket_raw[i] in wta_r1_winners_05 else wta_bracket_raw[i+1]) for i in range(0, 128, 2)}
wta_r2_locked = {}
for i in range(0, 128, 4):
    w1 = wta_r1_locked[(wta_bracket_raw[i], wta_bracket_raw[i+1])]
    w2 = wta_r1_locked[(wta_bracket_raw[i+2], wta_bracket_raw[i+3])]
    wta_r2_locked[(w1, w2)] = w1 if w1 in wta_r2_winners_05 else w2
wta_r3_locked = {}
for i in range(0, 128, 8):
    r2a = wta_r2_locked[(wta_r1_locked[(wta_bracket_raw[i], wta_bracket_raw[i+1])],
                         wta_r1_locked[(wta_bracket_raw[i+2], wta_bracket_raw[i+3])])]
    r2b = wta_r2_locked[(wta_r1_locked[(wta_bracket_raw[i+4], wta_bracket_raw[i+5])],
                         wta_r1_locked[(wta_bracket_raw[i+6], wta_bracket_raw[i+7])])]
    if r2a in wta_r3_winners_05: wta_r3_locked[(r2a, r2b)] = r2a
    elif r2b in wta_r3_winners_05: wta_r3_locked[(r2a, r2b)] = r2b

assert len(wta_r3_locked) == 13

def sim_wta(locked_r1=None, locked_r2=None, locked_r3=None,
            ryb_mix=None, sab_mix=None, elo_adj=None, r1_cal_override=False, n_trials=90000, seed=9500):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}; locked_r2 = locked_r2 or {}; locked_r3 = locked_r3 or {}
    if ryb_mix is None: ryb_mix = [(2130.0, 0.42), (2055.0, 0.30), (1955.0, 0.18), (1700.0, 0.10)]
    if sab_mix is None: sab_mix = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]
    r1_foe_adj = {"Camila Osorio": -25.0, "Xiyu Wang": -40.0, "Zeynep Sonmez": -40.0, "Thea Frodin": -55.0,
                  "Janice Tjen": -35.0, "Elena-Gabriela Ruse": -35.0, "Anastasia Zakharova": -20.0} if r1_cal_override else {}
    tc = Counter(); fc = Counter(); sc = Counter()
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
            ltc = Counter(); lfc = Counter(); lsc = Counter()
            for _ in range(tr):
                cur = list(wta_bracket_raw); rnd = 1
                while len(cur) > 1:
                    if rnd == 6:
                        for p in cur: lsc[p] += 1
                    elif rnd == 7:
                        for p in cur: lfc[p] += 1
                    nxt = []
                    for k in range(0, len(cur), 2):
                        a, b = cur[k], cur[k+1]
                        if rnd == 1 and (a, b) in locked_r1: nxt.append(locked_r1[(a, b)])
                        elif rnd == 2 and (a, b) in locked_r2: nxt.append(locked_r2[(a, b)])
                        elif rnd == 3 and (a, b) in locked_r3: nxt.append(locked_r3[(a, b)])
                        else: nxt.append(a if rng.random() < gp(emap[a], emap[b]) else b)
                    cur = nxt; rnd += 1
                ltc[cur[0]] += 1
            for p, c in ltc.items(): tc[p] += w * (c / tr)
            for p, c in lfc.items(): fc[p] += w * (c / tr)
            for p, c in lsc.items(): sc[p] += w * (c / tr)
    return tc, fc, sc

w28_t, _, _ = sim_wta(None, None, None, None, None, None, False, 90000, 9501)
w28_cal_t, _, _ = sim_wta(None, None, None, None, None, None, True, 90000, 9511)

ryb_prior_30 = [(2130.0, 0.52), (2065.0, 0.28), (1970.0, 0.14), (1740.0, 0.06)]
wr_a = [w * p_bo3(e, 1715.0) * p_bo3(e, 1860.0) for e, w in ryb_prior_30]
ryb_mix_A = [(e, ww / sum(wr_a)) for (e, _), ww in zip(ryb_prior_30, wr_a)]
sab_prior_28 = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]
ws_a = [w * p_bo3(e, 1845.0) * p_bo3(e, 1795.0) * p_bo3(e, 1825.0) for e, w in sab_prior_28]
sab_mix_A = [(e, ww / sum(ws_a)) for (e, _), ww in zip(sab_prior_28, ws_a)]

w05A_t, w05A_f, w05A_sf = sim_wta(wta_r1_locked, wta_r2_locked, wta_r3_locked, ryb_mix_A, sab_mix_A, None, False, 90000, 9521)

# B2: No double-counting Andreeva (+12 instead of +24), Reuters-confirmed healthy Rybakina (82/14/3/1) + Starodubtseva +30 RG H2H
ryb_mix_B2 = [(2130.0, 0.82), (2065.0, 0.14), (1970.0, 0.03), (1740.0, 0.01)]
sab_mix_B2 = [(2225.0, 0.68), (2175.0, 0.26), (2085.0, 0.06)]
wta_tweaks_B2 = {
    "Coco Gauff":           wta_cal_elo["Coco Gauff"] + 16.0,
    "Iga Swiatek":          wta_cal_elo["Iga Swiatek"] + 8.0,
    "Jessica Pegula":       wta_cal_elo["Jessica Pegula"] + 8.0,
    "Mirra Andreeva":       wta_cal_elo["Mirra Andreeva"] + 12.0,    # Moderate +12 (avoids double-counting DK market prior!)
    "Marta Kostyuk":        wta_cal_elo["Marta Kostyuk"] + 18.0,
    "Emma Navarro":         wta_cal_elo["Emma Navarro"] + 24.0,
    "Anna Kalinskaya":      wta_cal_elo["Anna Kalinskaya"] + 28.0,
    "Sorana Cirstea":       wta_cal_elo["Sorana Cirstea"] + 22.0,
    "Taylor Townsend":      wta_cal_elo["Taylor Townsend"] + 20.0,
    "Linda Noskova":        wta_cal_elo["Linda Noskova"] + 6.0,
    "Anastasia Potapova":   wta_cal_elo["Anastasia Potapova"] + 30.0,
    "Qinwen Zheng":         wta_cal_elo["Qinwen Zheng"] + 22.0,
    "Naomi Osaka":          wta_cal_elo["Naomi Osaka"] - 12.0,
    "Alexandra Eala":       wta_cal_elo["Alexandra Eala"] + 16.0,
    "Iva Jovic":            wta_cal_elo["Iva Jovic"] + 12.0,
    "Yuliia Starodubtseva": wta_cal_elo["Yuliia Starodubtseva"] + 30.0,
}

w05B2_t, w05B2_f, w05B2_sf = sim_wta(wta_r1_locked, wta_r2_locked, wta_r3_locked, ryb_mix_B2, sab_mix_B2, wta_tweaks_B2, False, 90000, 9532)
w05C2_t, w05C2_f, w05C2_sf = sim_wta(wta_r1_locked, wta_r2_locked, wta_r3_locked, ryb_mix_B2, sab_mix_B2, wta_tweaks_B2, True, 90000, 9542)

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

wupdA, _, _ = bayes_update_wta_full(w05A_t, w28_t)
wupdB2, _, _ = bayes_update_wta_full(w05B2_t, w28_t)
wupdC2, _, _ = bayes_update_wta_full(w05C2_t, w28_cal_t)
blend_wta = {k: 0.35 * wupdA.get(k, 0) + 0.35 * wupdB2.get(k, 0) + 0.30 * wupdC2.get(k, 0) for k in set(wupdA) | set(wupdB2)}

print("\n" + "=" * 116)
print("Q2 (608158) WTA REFINED (B2: Healthy Rybakina 82/14/3/1 + Starodubtseva H2H; Andreeva +12 no double-count)")
print("=" * 116)
print(f"{'Player':20s} | {'MC05A':6s} | {'MC05B2':6s} | {'UpdA':6s} | {'UpdB2':6s} | {'UpdC2':6s} | {'Blend':6s} | {'SF_B2':5s} | {'F_B2':5s}")
for k, _ in sorted(blend_wta.items(), key=lambda x: -x[1])[:10]:
    print(f"{k:20s} | {w05A_t.get(k,0):6.4f} | {w05B2_t.get(k,0):6.4f} | {wupdA.get(k,0):6.4f} | {wupdB2.get(k,0):6.4f} | {wupdC2.get(k,0):6.4f} | {blend_wta[k]:6.4f} | {w05B2_sf.get(k,0):5.3f} | {w05B2_f.get(k,0):5.3f}")
