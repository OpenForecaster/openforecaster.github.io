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
# DAY 6 (FRIDAY SEP 4, 2026, ~23:30 GMT / 6:30 PM ET) EXACT-BRACKET BAYES MC
# Batch: tennis (891014 ATP Title, 408930 Furthest U.S. Man, 608158 WTA Title)
# ATP: 64/64 R1 + 32/32 R2 + 3/16 R3 LOCKED! (Alcaraz, Medvedev, Paul in R4!)
# WTA: 62/64 R1 + 30/32 R2 + 7/16 R3 LOCKED! (All Q1 & 3/4 Q2 R3s complete!)
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

# ------------------------------------------------------------------------------
# PART 1: ATP EXACT 128-PLAYER BRACKET (64/64 R1 + 32/32 R2 + 3/16 R3 LOCKED!)
# ------------------------------------------------------------------------------
atp_replacements_04 = {
    "Casper Ruud":        "Arthur Gea",
    "Marin Cilic":        "Otto Virtanen",
    "Thanasi Kokkinakis": "Yunchaokete Bu",
    "Q_1":  "Grigor Dimitrov",
    "Q_2":  "Harry Wendelken",
    "Q_3":  "Dalibor Svrcina",
    "Q_4":  "Francesco Passaro",
    "Q_5":  "Andrea Guerrieri",
    "Q_6":  "Shintaro Mochizuki",
    "Q_7":  "Jurij Rodionov",
    "Q_8":  "Zsombor Piros",
    "Q_9":  "Tomas Barrios Vera",
    "Q_10": "Nishesh Basavareddy",
    "Q_11": "Tristan Schoolkate",
    "Q_12": "Hugo Gaston",
    "Q_13": "Rei Sakamoto",
    "Q_14": "Federico Cina",
    "Q_15": "Jacob Fearnley",
    "Q_16": "Toby Samuel",
    "Q_17": "Lloyd Harris",
    "Q_18": "Coleman Wong",
}
atp_bracket_04 = [atp_replacements_04.get(x, x) for x in atp_bracket_raw]

us_men_04 = {
    "Taylor Fritz", "Ben Shelton", "Frances Tiafoe", "Learner Tien",
    "Brandon Nakashima", "Tommy Paul",
    "Alex Michelsen", "Marcos Giron", "Zachary Svajda", "Jenson Brooksby",
    "Aleksandar Kovacevic", "Martin Damm", "Darwin Blanch", "J.J. Wolf",
    "Stefan Gorzny", "Jack Kennedy", "Michael Zheng",
    "Nishesh Basavareddy",
}
us_men_28 = set(us_men_04) - {"Nishesh Basavareddy"} | {"Q_4", "Q_10"}

# Confirmed ATP R1 winners (ALL 64 / 64 LOCKED!)
atp_r1_winners_04 = {
    # Q1 (16/16)
    "Alexander Zverev", "Quentin Halys", "Alexei Popyrin", "Alejandro Tabilo",
    "Luciano Darderi", "Dalibor Svrcina", "Dane Sweeny", "Lorenzo Musetti",
    "Yunchaokete Bu", "Michael Zheng", "Zachary Svajda", "Arthur Gea",
    "Zizou Bergs", "Jesper De Jong", "Botic van de Zandschulp", "Alex de Minaur",
    # Q2 (16/16)
    "Felix Auger-Aliassime", "Karen Khachanov", "Benjamin Bonzi", "Ignacio Buse",
    "Jakub Mensik", "Jurij Rodionov", "Gael Monfils", "Learner Tien",
    "Taylor Fritz", "Mattia Bellucci", "Jan-Lennard Struff", "Francisco Cerundolo",
    "Alexander Blockx", "Marco Trungelliti", "Tristan Schoolkate", "Flavio Cobolli",
    # Q3 (16/16)
    "Daniil Medvedev", "Stefan Gorzny", "Jaume Munar", "Arthur Rinderknech",
    "Valentin Vacherot", "Kamil Majchrzak", "Rei Sakamoto", "Frances Tiafoe",
    "Brandon Nakashima", "Alex Michelsen", "Daniel Merida", "Andrey Rublev",
    "Tomas Martin Etcheverry", "Jacob Fearnley", "Matteo Berrettini", "Mariano Navone",
    # Q4 (16/16)
    "Ben Shelton", "Hubert Hurkacz", "Denis Shapovalov", "Luca Van Assche",
    "Jiri Lehecka", "Toby Samuel", "Lloyd Harris", "Stefanos Tsitsipas",
    "Alexander Bublik", "Adrian Mannarino", "Dino Prizmic", "Tommy Paul",
    "James Duckworth", "Yibing Wu", "Jaime Faria", "Carlos Alcaraz",
}

# Confirmed ATP R2 winners (ALL 32 / 32 LOCKED!)
atp_r2_winners_04 = {
    # Q1 (8/8 ALL LOCKED!)
    "Alexander Zverev",         # def. Halys 6-4 4-6 7-6(3) 6-7(3) 6-3 (4h33m, 2:15am!)
    "Alejandro Tabilo",         # def. Popyrin
    "Luciano Darderi",          # def. Svrcina in 4
    "Dane Sweeny",              # def. #13 Musetti 3-6 6-1 6-2 6-2!
    "Michael Zheng",            # def. Yunchaokete Bu! (US WC!)
    "Arthur Gea",               # def. Zachary Svajda (US ELIMINATED!)
    "Zizou Bergs",              # def. De Jong
    "Botic van de Zandschulp",  # def. #6 Alex de Minaur 6-4 7-5 6-2!!
    # Q2 (8/8 ALL LOCKED!)
    "Karen Khachanov",          # def. #3 FAA 6-7(5) 6-3 6-2 6-2!
    "Benjamin Bonzi",           # def. Buse
    "Jakub Mensik",             # def. Rodionov in 4
    "Learner Tien",             # def. Monfils 6-3 6-4 6-3 (saved 8/8 BPs!)
    "Taylor Fritz",             # def. Bellucci 6-0 6-1 6-1 (98m!)
    "Francisco Cerundolo",      # def. Struff in 5
    "Alexander Blockx",         # def. Trungelliti
    "Flavio Cobolli",           # def. Schoolkate 3-6 6-3 6-4 7-5
    # Q3 (8/8 ALL LOCKED!)
    "Daniil Medvedev",          # def. Gorzny 6-1 6-3 7-5
    "Arthur Rinderknech",       # def. Munar 7-6(4) 6-2 7-5
    "Valentin Vacherot",        # def. Majchrzak in 4
    "Frances Tiafoe",           # def. Sakamoto 6-3 7-6(2) 7-5
    "Alex Michelsen",           # def. #16 Nakashima 6-3 6-4 6-4
    "Daniel Merida",            # def. #23 Rublev in 4
    "Tomas Martin Etcheverry",  # def. Fearnley in 4
    "Mariano Navone",           # def. Berrettini in 4
    # Q4 (8/8 ALL LOCKED!)
    "Ben Shelton",              # def. Hurkacz in 4
    "Denis Shapovalov",         # def. Van Assche 6-0 6-4 7-6(7)
    "Jiri Lehecka",             # def. Samuel 6-4 6-2 6-4
    "Stefanos Tsitsipas",       # def. Harris in 4
    "Alexander Bublik",         # def. Mannarino 6-3 6-1 6-1
    "Tommy Paul",               # def. Prizmic in 4
    "Yibing Wu",                # def. Duckworth 7-5 6-3 6-1
    "Carlos Alcaraz",           # def. Faria 4-6 6-0 6-3 6-2
}

# Confirmed ATP R3 winners as of Fri Sep 4 ~6:30 PM ET (3 / 16 LOCKED!)
atp_r3_winners_04 = {
    "Daniil Medvedev",          # def. #26 Rinderknech 6-4 6-4 6-4 (2h00m, 9-0 sets!)
    "Tommy Paul",               # def. #15 Bublik 6-4 3-6 6-7(4) 6-1 6-3 (3+ hr 5-setter!)
    "Carlos Alcaraz",           # def. Yibing Wu 6-3 6-4 6-1 (2h20m, 17th straight Slam win!)
}

atp_r1_locked_04 = {}
for i in range(0, 128, 2):
    a, b = atp_bracket_04[i], atp_bracket_04[i+1]
    if a in atp_r1_winners_04:
        assert b not in atp_r1_winners_04, f"Both R1: {a}, {b}"
        atp_r1_locked_04[(a, b)] = a
    elif b in atp_r1_winners_04:
        atp_r1_locked_04[(a, b)] = b

atp_r2_locked_04 = {}
for i in range(0, 128, 4):
    w1 = atp_r1_locked_04.get((atp_bracket_04[i], atp_bracket_04[i+1]))
    w2 = atp_r1_locked_04.get((atp_bracket_04[i+2], atp_bracket_04[i+3]))
    if w1 and w2:
        if w1 in atp_r2_winners_04:
            assert w2 not in atp_r2_winners_04, f"Both R2: {w1}, {w2}"
            atp_r2_locked_04[(w1, w2)] = w1
        elif w2 in atp_r2_winners_04:
            atp_r2_locked_04[(w1, w2)] = w2

atp_r3_locked_04 = {}
for i in range(0, 128, 8):
    r2_a = atp_r2_locked_04.get((
        atp_r1_locked_04[(atp_bracket_04[i], atp_bracket_04[i+1])],
        atp_r1_locked_04[(atp_bracket_04[i+2], atp_bracket_04[i+3])]
    ))
    r2_b = atp_r2_locked_04.get((
        atp_r1_locked_04[(atp_bracket_04[i+4], atp_bracket_04[i+5])],
        atp_r1_locked_04[(atp_bracket_04[i+6], atp_bracket_04[i+7])]
    ))
    if r2_a and r2_b:
        if r2_a in atp_r3_winners_04:
            assert r2_b not in atp_r3_winners_04
            atp_r3_locked_04[(r2_a, r2_b)] = r2_a
        elif r2_b in atp_r3_winners_04:
            atp_r3_locked_04[(r2_a, r2_b)] = r2_b

print(f"ATP R1 locked: {len(atp_r1_locked_04)} / 64 (expected 64)")
print(f"ATP R2 locked: {len(atp_r2_locked_04)} / 32 (expected 32)")
print(f"ATP R3 locked: {len(atp_r3_locked_04)} / 16 (expected 3)")
assert len(atp_r1_locked_04) == 64
assert len(atp_r2_locked_04) == 32
assert len(atp_r3_locked_04) == 3

extra_atp_elo_04 = {
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
    "Yunchaokete Bu":      1865.0,
    "Dane Sweeny":         1835.0,
}

def sim_atp(bracket, elo_dict, us_set, locked_r1=None, locked_r2=None, locked_r3=None,
            alc_mix=None, tia_mix=None, zve_mix=None, elo_tweaks=None,
            n_trials=60000, seed=9400):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    locked_r2 = locked_r2 or {}
    locked_r3 = locked_r3 or {}
    elos_base = []
    for nm in bracket:
        if nm.startswith("Q_"):
            el = 1830.0
        elif nm in elo_dict:
            el = float(elo_dict[nm])
        elif nm in extra_atp_elo_04:
            el = float(extra_atp_elo_04[nm])
        else:
            el = 1840.0
        if elo_tweaks and nm in elo_tweaks:
            el += float(elo_tweaks[nm])
        elos_base.append(el)

    alc_idx = bracket.index("Carlos Alcaraz")
    djo_idx = bracket.index("Novak Djokovic")
    tia_idx = bracket.index("Frances Tiafoe")
    zve_idx = bracket.index("Alexander Zverev")
    us_idxs = {i for i, nm in enumerate(bracket) if nm in us_set}

    if alc_mix is None:
        alc_mix = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
    djo_elim = ("Mariano Navone", "Novak Djokovic") in locked_r1
    djo_mix = [(2100.0, 1.0)] if djo_elim else [(2135.0, 0.55), (2075.0, 0.30), (1985.0, 0.15)]
    if tia_mix is None:
        tia_mix = [(0.0, 0.78), (-35.0, 0.16), (-95.0, 0.06)]
    if zve_mix is None:
        zve_mix = [(0.0, 1.0)]

    locked_r1_slots = {}
    for k in range(0, 128, 2):
        pair = (bracket[k], bracket[k+1])
        if pair in locked_r1:
            wname = locked_r1[pair]
            locked_r1_slots[k] = k if wname == bracket[k] else k + 1

    def to_idx_pairs(locked_map):
        out = {}
        for (a_nm, b_nm), w_nm in locked_map.items():
            ia = bracket.index(a_nm)
            ib = bracket.index(b_nm)
            iw = ia if w_nm == a_nm else ib
            out[(ia, ib)] = iw
            out[(ib, ia)] = iw
        return out

    locked_r2_pairs = to_idx_pairs(locked_r2)
    locked_r3_pairs = to_idx_pairs(locked_r3)

    tc = Counter(); fc = Counter(); r4c = Counter(); qfc = Counter(); sfc = Counter()
    uncond_us = Counter(); tie_rate = 0.0
    for ae, wa in alc_mix:
        for de, wd in djo_mix:
            for td, wt in tia_mix:
                for zd, wz in zve_mix:
                    w = wa * wd * wt * wz
                    tr = max(600, int(round(n_trials * w)))
                    elos = list(elos_base)
                    elos[alc_idx] = float(ae)
                    elos[djo_idx] = float(de)
                    elos[tia_idx] = elos_base[tia_idx] + float(td)
                    elos[zve_idx] = elos_base[zve_idx] + float(zd)
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
                                if rnd == 1 and k in locked_r1_slots:
                                    win = locked_r1_slots[k]
                                    los = b if win == a else a
                                elif rnd == 2 and (a, b) in locked_r2_pairs:
                                    win = locked_r2_pairs[(a, b)]
                                    los = b if win == a else a
                                elif rnd == 3 and (a, b) in locked_r3_pairs:
                                    win = locked_r3_pairs[(a, b)]
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

# Baseline Aug 28
m28_tc, m28_fc, m28_r4, m28_qf, m28_sf, m28_cu, m28_uu, m28_tie = run_atp_blend(
    atp_bracket_raw, us_men_28, None, None, None, None, None, None, None, 9100
)

# Model A: Strict outcome-only Bayes (Alcaraz updated cleanly for Safiullin + Faria + Wu)
alc_prior = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
w_r1r3 = [w * p_bo5(e, 1895.0) * p_bo5(e, 1845.0) * p_bo5(e, 1860.0) for e, w in alc_prior]
s_r1r3 = sum(w_r1r3)
alc_mix_A = [(e, ww / s_r1r3) for (e, _), ww in zip(alc_prior, w_r1r3)]

m04A_tc, m04A_fc, m04A_r4, m04A_qf, m04A_sf, m04A_cu, m04A_uu, m04A_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked_04, atp_r2_locked_04, atp_r3_locked_04,
    alc_mix_A, None, None, None, 9600
)

# Model B: Form / Fatigue / H2H-Calibrated Bayes (Moderate Zverev fatigue)
alc_mix_B = [(2280.0, 0.50), (2175.0, 0.43), (2045.0, 0.06), (1750.0, 0.01)]
tia_mix_B = [(0.0, 0.80), (-35.0, 0.15), (-95.0, 0.05)]
# Zverev played 4h53m vs Sonego (2am Wed) + 4h33m vs Halys (2:15am Fri) = 9h26m in 2 rounds; "performance quite shit"
zve_mix_B = [(0.0, 0.30), (-35.0, 0.40), (-75.0, 0.22), (-120.0, 0.08)]
zve_mix_C = [(0.0, 0.18), (-45.0, 0.42), (-90.0, 0.28), (-140.0, 0.12)]

tweaks_B = {
    "Taylor Fritz":            +16.0,   # 0 sets lost, 6-0 6-1 6-1 (98m!)
    "Daniil Medvedev":         +24.0,   # 9-0 sets into R4! Crushed #26 Rinderknech 6-4 6-4 6-4 in 2h00m!
    "Alex Michelsen":          +28.0,   # Crushed Cina & #16 Nakashima 6-3 6-4 6-4
    "Ben Shelton":             +14.0,   # Beat Griekspoor & Hurkacz in 4; 4-0 H2H vs Shapovalov!
    "Denis Shapovalov":        +6.0,    # Sharp vs Van Assche, but 0-4 H2H vs Shelton
    "Learner Tien":            +22.0,   # Crushed Borges & Monfils 6-3 6-4 6-3 (8/8 BPs saved, 0 sets lost!)
    "Tommy Paul":              -12.0,   # Grueling 3+ hr 5-setter vs Bublik + 0-6 recent H2H vs Alcaraz!
    "Karen Khachanov":         +18.0,   # Beat dizzy FAA in 4
    "Jakub Mensik":            +6.0,    # Beat Rodionov in 4
    "Jiri Lehecka":            +8.0,    # Clean 6-4 6-2 6-4
    "Stefanos Tsitsipas":      +14.0,   # Beat Fils & Harris in 4
    "Francisco Cerundolo":     -10.0,   # 5-set grueler vs Struff before Fritz
    "Flavio Cobolli":          -8.0,    # 5-setter R1 + 4-setter vs Schoolkate
    "Botic van de Zandschulp": +30.0,   # Demolished #6 Alex de Minaur 6-4 7-5 6-2!!
    "Alejandro Tabilo":        +12.0,   # Beat Popyrin to reach R3 vs exhausted Zverev
    "Zizou Bergs":             +10.0,   # Beat De Jong
    "Alexander Blockx":        +15.0,   # Into R3
    "Benjamin Bonzi":          +12.0,   # Beat Buse
    "Mariano Navone":          +24.0,   # Beat Djokovic & Berrettini!
    "Dane Sweeny":             +25.0,   # Beat #13 Musetti in 4!
    "Daniel Merida":           +30.0,   # Beat Fucsovics & #23 Rublev!
    "Valentin Vacherot":       +8.0,
    "Tomas Martin Etcheverry": +8.0,
    "Michael Zheng":           +45.0,   # Base 1785 -> 1830 after beating Bu!
    "Arthur Gea":              +20.0,   # Base 1815 -> 1835 after beating Svajda!
}

m04B_tc, m04B_fc, m04B_r4, m04B_qf, m04B_sf, m04B_cu, m04B_uu, m04B_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked_04, atp_r2_locked_04, atp_r3_locked_04,
    alc_mix_B, tia_mix_B, zve_mix_B, tweaks_B, 9700
)

m04C_tc, m04C_fc, m04C_r4, m04C_qf, m04C_sf, m04C_cu, m04C_uu, m04C_tie = run_atp_blend(
    atp_bracket_04, us_men_04, atp_r1_locked_04, atp_r2_locked_04, atp_r3_locked_04,
    alc_mix_B, tia_mix_B, zve_mix_C, tweaks_B, 9800
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

updA, fA, totA = bayes_update_atp(m04A_tc)
updB, fB, totB = bayes_update_atp(m04B_tc)
updC, fC, totC = bayes_update_atp(m04C_tc)

print("\n" + "=" * 116)
print(f"Q3 (891014) MEN'S SINGLES — FRI SEP 4 DAY 6 BAYESIAN UPDATE (Pre-norm: A={totA:.4f}, B={totB:.4f}, C={totC:.4f})")
print("=" * 116)
print(f"{'Player':22s} | {'MC28':6s} | {'MC04B':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'UpdC':6s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(updB.items(), key=lambda x: -x[1])[:12]:
    print(f"{k:22s} | {m28_tc.get(k,0):6.4f} | {m04B_tc.get(k,0):6.4f} | {aug28_named.get(k,0):6.4f} | {updA[k]:6.4f} | {updB[k]:6.4f} | {updC[k]:6.4f} | {m04B_sf.get(k,0):5.3f} | {m04B_fc.get(k,0):5.3f}")
print(f"{'Field_Rest':22s} | {1-sum(m28_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m04B_tc.get(k,0) for k in aug28_named):6.4f} | {field_28:6.4f} | {fA:6.4f} | {fB:6.4f} | {fC:6.4f} |")
print("Top-8 UpdA:", [(k, round(v, 4)) for k, v in sorted(updA.items(), key=lambda x: -x[1])[:8]])
print("Top-8 UpdB:", [(k, round(v, 4)) for k, v in sorted(updB.items(), key=lambda x: -x[1])[:8]])
print("Top-8 UpdC:", [(k, round(v, 4)) for k, v in sorted(updC.items(), key=lambda x: -x[1])[:8]])
print("MC04B raw top-10:", [(k, round(v, 4)) for k, v in m04B_tc.most_common(10)])
print("Key H2H sanity (B): Shelton vs Shapovalov =", round(p_bo5(atp_mkt_elo["Ben Shelton"]+14, atp_mkt_elo["Denis Shapovalov"]+6), 4),
      "| Alcaraz(2215) vs Paul =", round(p_bo5(2215, atp_mkt_elo["Tommy Paul"]-12), 4),
      "| Zheng vs Gea =", round(p_bo5(1785+45, 1815+20), 4))

print("\n" + "=" * 116)
print(f"Q1 (408930) FURTHEST U.S. MAN — FRI SEP 4 DAY 6 UPDATE (Tie: 28={m28_tie:.4f}, A={m04A_tie:.4f}, B={m04B_tie:.4f}, C={m04C_tie:.4f})")
print("=" * 116)
print(f"{'Player':22s} | {'Cond28':7s} | {'CondA':7s} | {'CondB':7s} | {'CondC':7s} | {'UncondB':7s} | {'R4_B':5s} | {'QF_B':5s} | {'SF_B':5s}")
for k, _ in sorted(m04B_cu.items(), key=lambda x: -x[1])[:10]:
    print(f"{k:22s} | {m28_cu.get(k,0):7.4f} | {m04A_cu.get(k,0):7.4f} | {m04B_cu.get(k,0):7.4f} | {m04C_cu.get(k,0):7.4f} | {m04B_uu.get(k,0):7.4f} | {m04B_r4[k]:5.3f} | {m04B_qf[k]:5.3f} | {m04B_sf[k]:5.3f}")

# ------------------------------------------------------------------------------
# PART 2: WTA EXACT 128-PLAYER BRACKET (62/64 R1 + 30/32 R2 + 7/16 R3 LOCKED!)
# ------------------------------------------------------------------------------
wta_r1_winners_04 = {
    # Q1 (16/16)
    "Aryna Sabalenka", "Polina Iatcenko", "Oksana Selekhmeteva", "Kamilla Rakhimova",
    "Taylor Townsend", "Taylah Preston", "Karolina Pliskova", "Diana Shnaider",
    "Marta Kostyuk", "Sloane Stephens", "Kimberly Birrell", "Ekaterina Alexandrova",
    "Ann Li", "Donna Vekic", "Lanlana Tararudee", "Linda Noskova",
    # Q2 (16/16)
    "Jessica Pegula", "Sofia Kenin", "Mananchaya Sawangkaew", "Leylah Fernandez",
    "Jasmine Paolini", "Lucrezia Stefanini", "Diane Parry", "Sorana Cirstea",
    "Elina Svitolina", "Maya Joint", "Xinyu Wang", "Anna Kalinskaya",
    "Emma Navarro", "Caty McNally", "Katie Boulter", "Karolina Muchova",
    # Q3 (14/16 — unconfirmed minor R1s: Potapova/Valentova, Rus/Jeanjean)
    "Mirra Andreeva", "Eva Lys", "Nikola Bartunkova", "Tatjana Maria",
    "Lilli Tagger", "Amanda Anisimova", "Iva Jovic", "Francesca Jones",
    "Oleksandra Oliynykova", "Alexandra Eala", "Cristina Bucsa", "Himeno Sakatsume",
    "Paula Badosa", "Coco Gauff",
    # Q4 (16/16 ALL LOCKED — Putintseva upset Bencic in R1!)
    "Iga Swiatek", "Nadia Podoroska", "Harriet Dart", "Marie Bouzkova",
    "Madison Keys", "Anna Bondar", "Yulia Putintseva", "Qinwen Zheng",
    "Naomi Osaka", "Katerina Siniakova", "Maria Timofeeva", "Elise Mertens",
    "Maria Sakkari", "Yuliia Starodubtseva", "Jessica Bouzas Maneiro", "Elena Rybakina",
}

# Confirmed WTA R2 winners (30 / 32 LOCKED!)
wta_r2_winners_04 = {
    # Q1 (8/8 ALL LOCKED!)
    "Aryna Sabalenka", "Kamilla Rakhimova", "Taylor Townsend", "Diana Shnaider",
    "Marta Kostyuk", "Ekaterina Alexandrova", "Ann Li", "Linda Noskova",
    # Q2 (8/8 ALL LOCKED!)
    "Jessica Pegula", "Leylah Fernandez", "Jasmine Paolini", "Sorana Cirstea",
    "Elina Svitolina", "Anna Kalinskaya", "Emma Navarro", "Karolina Muchova",
    # Q3 (6/8 — only Bartunkova/Potapova/Valentova and Maria/Rus/Jeanjean unconfirmed)
    "Mirra Andreeva",      # def. Eva Lys 6-0 6-2!
    "Amanda Anisimova",    # def. Tagger 6-3 3-6 6-1
    "Iva Jovic",           # def. Francesca Jones 6-4 6-4
    "Alexandra Eala",      # def. Oliynykova 6-1 6-4
    "Cristina Bucsa",      # def. Sakatsume
    "Coco Gauff",          # def. Paula Badosa 6-4 7-6(5)!!
    # Q4 (8/8 ALL LOCKED!)
    "Iga Swiatek",         # def. Podoroska 6-3 6-2
    "Marie Bouzkova",      # def. Dart
    "Madison Keys",        # def. Bondar 5-7 6-4 7-6(5)
    "Qinwen Zheng",        # def. Putintseva 6-4 2-6 6-1!
    "Naomi Osaka",         # def. Siniakova 6-2 5-7 6-1
    "Elise Mertens",       # def. Timofeeva 6-2 7-6(5)
    "Yuliia Starodubtseva",# def. #32 Maria Sakkari!
    "Elena Rybakina",      # def. Bouzas Maneiro 6-2 6-4!
}

# Confirmed WTA R3 winners as of Fri Sep 4 ~6:30 PM ET (7 / 16 LOCKED — ALL Q1 + 3/4 Q2!)
wta_r3_winners_04 = {
    # Q1 (4/4 ALL LOCKED!)
    "Aryna Sabalenka",     # def. Rakhimova 6-3 6-4 (0 BPs faced, 29W, 10 aces!)
    "Taylor Townsend",     # def. #15 Diana Shnaider 6-2 6-7(3) 6-3!! (HUGE gift for Sabalenka!)
    "Marta Kostyuk",       # def. #18 Ekaterina Alexandrova 6-3 6-2!
    "Linda Noskova",       # def. #29 Ann Li 6-2 6-7(6) 6-2!
    # Q2 (3/4 LOCKED — Svitolina vs Kalinskaya pending Fri night!)
    "Jessica Pegula",      # def. #31 Leylah Fernandez 1-6 6-4 6-3!
    "Sorana Cirstea",      # def. #19 Jasmine Paolini 6-3 6-3!
    "Emma Navarro",        # def. #7 Karolina Muchova 6-3 7-5!! (HUGE gift for Pegula & Sabalenka!)
}

wta_r1_locked_04 = {}
for i in range(0, 128, 2):
    a, b = wta_bracket_raw[i], wta_bracket_raw[i+1]
    if a in wta_r1_winners_04:
        assert b not in wta_r1_winners_04, f"Both WTA R1: {a}, {b}"
        wta_r1_locked_04[(a, b)] = a
    elif b in wta_r1_winners_04:
        wta_r1_locked_04[(a, b)] = b

wta_r2_locked_04 = {}
for i in range(0, 128, 4):
    w1 = wta_r1_locked_04.get((wta_bracket_raw[i], wta_bracket_raw[i+1]))
    w2 = wta_r1_locked_04.get((wta_bracket_raw[i+2], wta_bracket_raw[i+3]))
    if w1 and w2:
        if w1 in wta_r2_winners_04:
            assert w2 not in wta_r2_winners_04
            wta_r2_locked_04[(w1, w2)] = w1
        elif w2 in wta_r2_winners_04:
            wta_r2_locked_04[(w1, w2)] = w2

wta_r3_locked_04 = {}
for i in range(0, 128, 8):
    w1 = wta_r1_locked_04.get((wta_bracket_raw[i], wta_bracket_raw[i+1]))
    w2 = wta_r1_locked_04.get((wta_bracket_raw[i+2], wta_bracket_raw[i+3]))
    w3 = wta_r1_locked_04.get((wta_bracket_raw[i+4], wta_bracket_raw[i+5]))
    w4 = wta_r1_locked_04.get((wta_bracket_raw[i+6], wta_bracket_raw[i+7]))
    r2a = wta_r2_locked_04.get((w1, w2)) if (w1 and w2) else None
    r2b = wta_r2_locked_04.get((w3, w4)) if (w3 and w4) else None
    if r2a and r2b:
        if r2a in wta_r3_winners_04:
            assert r2b not in wta_r3_winners_04
            wta_r3_locked_04[(r2a, r2b)] = r2a
        elif r2b in wta_r3_winners_04:
            wta_r3_locked_04[(r2a, r2b)] = r2b

print(f"\nWTA R1 locked: {len(wta_r1_locked_04)} / 64 (expected 62)")
print(f"WTA R2 locked: {len(wta_r2_locked_04)} / 32 (expected 30)")
print(f"WTA R3 locked: {len(wta_r3_locked_04)} / 16 (expected 7)")
assert len(wta_r1_locked_04) == 62
assert len(wta_r2_locked_04) == 30
assert len(wta_r3_locked_04) == 7

def sim_wta(locked_r1=None, locked_r2=None, locked_r3=None,
            ryb_mix=None, sab_mix=None, elo_adj=None, r1_cal_override=False, n_trials=90000, seed=9500):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    locked_r2 = locked_r2 or {}
    locked_r3 = locked_r3 or {}
    if ryb_mix is None:
        ryb_mix = [(2130.0, 0.42), (2055.0, 0.30), (1955.0, 0.18), (1700.0, 0.10)]
    if sab_mix is None:
        sab_mix = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]

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
                        elif rnd == 2 and (a, b) in locked_r2:
                            nxt.append(locked_r2[(a, b)])
                        elif rnd == 3 and (a, b) in locked_r3:
                            nxt.append(locked_r3[(a, b)])
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
w28_t, _, _ = sim_wta(locked_r1=None, locked_r2=None, locked_r3=None, r1_cal_override=False, n_trials=90000, seed=9501)
w28_cal_t, _, _ = sim_wta(locked_r1=None, locked_r2=None, locked_r3=None, r1_cal_override=True, n_trials=90000, seed=9511)

# Model A: Strict Outcome-Only
ryb_prior_30 = [(2130.0, 0.52), (2065.0, 0.28), (1970.0, 0.14), (1740.0, 0.06)]
wr_a = [w * p_bo3(e, 1715.0) * p_bo3(e, 1860.0) for e, w in ryb_prior_30]
ryb_mix_A = [(e, ww / sum(wr_a)) for (e, _), ww in zip(ryb_prior_30, wr_a)]
sab_prior_28 = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]
ws_a = [w * p_bo3(e, 1845.0) * p_bo3(e, 1795.0) * p_bo3(e, 1825.0) for e, w in sab_prior_28]
sab_mix_A = [(e, ww / sum(ws_a)) for (e, _), ww in zip(sab_prior_28, ws_a)]

w04A_t, w04A_f, w04A_sf = sim_wta(
    locked_r1=wta_r1_locked_04, locked_r2=wta_r2_locked_04, locked_r3=wta_r3_locked_04,
    ryb_mix=ryb_mix_A, sab_mix=sab_mix_A, r1_cal_override=False, n_trials=90000, seed=9520
)

# Model B: Conservative Health/Form Bayes
ryb_mix_B = [(2130.0, 0.74), (2065.0, 0.19), (1970.0, 0.055), (1740.0, 0.015)]
sab_mix_B = [(2225.0, 0.68), (2175.0, 0.26), (2085.0, 0.06)]
wta_tweaks_B = {
    "Coco Gauff":           wta_cal_elo["Coco Gauff"] + 14.0,        # Beat 3-5 H2H nemesis Badosa 6-4 7-6(5)!
    "Iga Swiatek":          wta_cal_elo["Iga Swiatek"] + 12.0,       # Clean 6-2 6-3, 6-3 6-2
    "Jessica Pegula":       wta_cal_elo["Jessica Pegula"] + 8.0,     # Into R4, rallied 1-6 6-4 6-3 vs Fernandez
    "Mirra Andreeva":       wta_cal_elo["Mirra Andreeva"] + 22.0,    # Crushed Tjen 6-2 6-2 & Lys 6-0 6-2!!
    "Marta Kostyuk":        wta_cal_elo["Marta Kostyuk"] + 18.0,     # Crushed #18 Alexandrova 6-3 6-2 into R4!
    "Emma Navarro":         wta_cal_elo["Emma Navarro"] + 24.0,      # Upset #7 Muchova 6-3 7-5 into R4!
    "Sorana Cirstea":       wta_cal_elo["Sorana Cirstea"] + 22.0,    # Clinical 6-3 6-3 upset of #19 Paolini!
    "Taylor Townsend":      wta_cal_elo["Taylor Townsend"] + 20.0,   # Upset #15 Shnaider in 3 sets
    "Linda Noskova":        wta_cal_elo["Linda Noskova"] + 6.0,      # Into R4 in 3 sets vs Ann Li
    "Naomi Osaka":          wta_cal_elo["Naomi Osaka"] - 12.0,       # Rusty R1 + 20 UEs set 2 vs Siniakova
    "Amanda Anisimova":     wta_cal_elo["Amanda Anisimova"] + 4.0,   # Dropped set to Tagger
    "Alexandra Eala":       wta_cal_elo["Alexandra Eala"] + 16.0,    # 6-1 6-2, 6-1 6-4
    "Iva Jovic":            wta_cal_elo["Iva Jovic"] + 12.0,         # Clean 6-4 6-4
    "Qinwen Zheng":         wta_cal_elo["Qinwen Zheng"] + 10.0,      # Beat Putintseva in 3
    "Madison Keys":         wta_cal_elo["Madison Keys"] - 10.0,      # Saved 5 MPs vs Bondar
    "Elina Svitolina":      wta_cal_elo["Elina Svitolina"] - 4.0,    # 3-setter vs Joint
    "Yuliia Starodubtseva": wta_cal_elo["Yuliia Starodubtseva"] + 20.0,
}

w04B_t, w04B_f, w04B_sf = sim_wta(
    locked_r1=wta_r1_locked_04, locked_r2=wta_r2_locked_04, locked_r3=wta_r3_locked_04,
    ryb_mix=ryb_mix_B, sab_mix=sab_mix_B,
    elo_adj=wta_tweaks_B, r1_cal_override=False, n_trials=90000, seed=9530
)

w04C_t, w04C_f, w04C_sf = sim_wta(
    locked_r1=wta_r1_locked_04, locked_r2=wta_r2_locked_04, locked_r3=wta_r3_locked_04,
    ryb_mix=ryb_mix_B, sab_mix=sab_mix_B,
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

wupdA, wfA, wtotA = bayes_update_wta(w04A_t, w28_t)
wupdB, wfB, wtotB = bayes_update_wta(w04B_t, w28_t)
wupdC, wfC, wtotC = bayes_update_wta(w04C_t, w28_cal_t)

print("\n" + "=" * 116)
print(f"Q2 (608158) WOMEN'S SINGLES — FRI SEP 4 DAY 6 BAYESIAN UPDATE (Pre-norm: A={wtotA:.4f}, B={wtotB:.4f}, C={wtotC:.4f})")
print("=" * 116)
print(f"{'Player':20s} | {'MC28':6s} | {'MC04B':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'UpdC(cal)':9s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(wupdC.items(), key=lambda x: -x[1])[:13]:
    print(f"{k:20s} | {w28_t[k]:6.4f} | {w04B_t[k]:6.4f} | {aug28_wta_exact[k]:6.4f} | {wupdA[k]:6.4f} | {wupdB[k]:6.4f} | {wupdC[k]:9.4f} | {w04B_sf[k]:5.3f} | {w04B_f[k]:5.3f}")
print("WTA Top-8 UpdA:", [(k, round(v, 4)) for k, v in sorted(wupdA.items(), key=lambda x: -x[1])[:8]])
print("WTA Top-8 UpdB:", [(k, round(v, 4)) for k, v in sorted(wupdB.items(), key=lambda x: -x[1])[:8]])
print("WTA Top-8 UpdC:", [(k, round(v, 4)) for k, v in sorted(wupdC.items(), key=lambda x: -x[1])[:8]])
print("WTA Field_Rest:", round(wfA, 4), round(wfB, 4), round(wfC, 4))
