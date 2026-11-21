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
# DAY 5 (THURSDAY SEP 3, 2026, ~23:05 CET / 5:05 PM ET) EXACT-BRACKET BAYES MC
# Batch: tennis (891014 ATP Title, 408930 Furthest U.S. Man, 608158 WTA Title)
# ATP: 64/64 R1 LOCKED! 22/32 R2 LOCKED! (All Q3 & Q4 R2s complete!)
# WTA: 61/64 R1 LOCKED! 22/32 R2 LOCKED! (All Q2 & 7/8 Q1 R2s complete!)
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
# PART 1: ATP EXACT 128-PLAYER BRACKET (64/64 R1 + 22/32 R2 LOCKED!)
# ------------------------------------------------------------------------------
atp_replacements_03 = {
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
atp_bracket_03 = [atp_replacements_03.get(x, x) for x in atp_bracket_raw]

us_men_03 = {
    "Taylor Fritz", "Ben Shelton", "Frances Tiafoe", "Learner Tien",
    "Brandon Nakashima", "Tommy Paul",
    "Alex Michelsen", "Marcos Giron", "Zachary Svajda", "Jenson Brooksby",
    "Aleksandar Kovacevic", "Martin Damm", "Darwin Blanch", "J.J. Wolf",
    "Stefan Gorzny", "Jack Kennedy", "Michael Zheng",
    "Nishesh Basavareddy",
}
us_men_28 = set(us_men_03) - {"Nishesh Basavareddy"} | {"Q_4", "Q_10"}

# Confirmed ATP R1 winners (ALL 64 / 64 LOCKED!)
atp_r1_winners_03 = {
    # Q1 (16/16 LOCKED!)
    "Alexander Zverev", "Quentin Halys", "Alexei Popyrin", "Alejandro Tabilo",
    "Luciano Darderi", "Dalibor Svrcina", "Dane Sweeny", "Lorenzo Musetti",
    "Yunchaokete Bu", "Michael Zheng", "Zachary Svajda", "Arthur Gea",
    "Zizou Bergs", "Jesper De Jong", "Botic van de Zandschulp", "Alex de Minaur",
    # Q2 (16/16 LOCKED!)
    "Felix Auger-Aliassime", "Karen Khachanov", "Benjamin Bonzi", "Ignacio Buse",
    "Jakub Mensik", "Jurij Rodionov", "Gael Monfils", "Learner Tien",
    "Taylor Fritz", "Mattia Bellucci", "Jan-Lennard Struff", "Francisco Cerundolo",
    "Alexander Blockx", "Marco Trungelliti", "Tristan Schoolkate", "Flavio Cobolli",
    # Q3 (16/16 LOCKED!)
    "Daniil Medvedev", "Stefan Gorzny", "Jaume Munar", "Arthur Rinderknech",
    "Valentin Vacherot", "Kamil Majchrzak", "Rei Sakamoto", "Frances Tiafoe",
    "Brandon Nakashima", "Alex Michelsen", "Daniel Merida", "Andrey Rublev",
    "Tomas Martin Etcheverry", "Jacob Fearnley", "Matteo Berrettini", "Mariano Navone",
    # Q4 (16/16 LOCKED!)
    "Ben Shelton", "Hubert Hurkacz", "Denis Shapovalov", "Luca Van Assche",
    "Jiri Lehecka", "Toby Samuel", "Lloyd Harris", "Stefanos Tsitsipas",
    "Alexander Bublik", "Adrian Mannarino", "Dino Prizmic", "Tommy Paul",
    "James Duckworth", "Yibing Wu", "Jaime Faria", "Carlos Alcaraz",
}

# Confirmed ATP R2 winners as of Thu Sep 3 ~5:05 PM ET (22 / 32 LOCKED!)
atp_r2_winners_03 = {
    # Q1 (2/8)
    "Luciano Darderi",          # def. Svrcina 6-3 6-7(5) 6-4 6-4
    "Dane Sweeny",              # def. #13 Lorenzo Musetti 3-6 6-1 6-2 6-2!!
    # Q2 (4/8)
    "Karen Khachanov",          # def. #3 Felix Auger-Aliassime 6-7(5) 6-3 6-2 6-2!!
    "Jakub Mensik",             # def. Rodionov 6-3 3-6 6-2 6-3
    "Taylor Fritz",             # def. Bellucci 6-0 6-1 6-1!! (98 min!)
    "Francisco Cerundolo",      # def. Struff 5-7 7-5 4-6 6-2 6-3 (5-setter!)
    # Q3 (8/8 ALL LOCKED!)
    "Daniil Medvedev",          # def. Gorzny 6-1 6-3 7-5
    "Arthur Rinderknech",       # def. Munar 7-6(4) 6-2 7-5
    "Valentin Vacherot",        # def. Majchrzak 6-4 4-6 7-6(3) 6-2
    "Frances Tiafoe",           # def. Sakamoto 6-3 7-6(2) 7-5
    "Alex Michelsen",           # def. #16 Nakashima 6-3 6-4 6-4
    "Daniel Merida",            # def. #23 Rublev 6-7(3) 6-2 6-4 6-4
    "Tomas Martin Etcheverry",  # def. Fearnley 6-3 6-3 3-6 6-3
    "Mariano Navone",           # def. Berrettini 3-6 6-3 6-4 7-6(4)!!
    # Q4 (8/8 ALL LOCKED!)
    "Ben Shelton",              # def. Hurkacz 6-3 5-7 7-6(3) 7-5
    "Denis Shapovalov",         # def. Van Assche 6-0 6-4 7-6(7)
    "Jiri Lehecka",             # def. Samuel 6-4 6-2 6-4
    "Stefanos Tsitsipas",       # def. Harris 6-7(1) 6-3 7-6(4) 6-4
    "Alexander Bublik",         # def. Mannarino 6-3 6-1 6-1
    "Tommy Paul",               # def. Prizmic 6-2 6-3 5-7 6-4
    "Yibing Wu",                # def. Duckworth 7-5 6-3 6-1
    "Carlos Alcaraz",           # def. Faria 4-6 6-0 6-3 6-2
}

atp_r1_locked_03 = {}
for i in range(0, 128, 2):
    a, b = atp_bracket_03[i], atp_bracket_03[i+1]
    if a in atp_r1_winners_03:
        assert b not in atp_r1_winners_03, f"Both in R1 winners: {a}, {b}"
        atp_r1_locked_03[(a, b)] = a
    elif b in atp_r1_winners_03:
        atp_r1_locked_03[(a, b)] = b

atp_r2_locked_03 = {}
for i in range(0, 128, 4):
    w1 = atp_r1_locked_03.get((atp_bracket_03[i], atp_bracket_03[i+1]))
    w2 = atp_r1_locked_03.get((atp_bracket_03[i+2], atp_bracket_03[i+3]))
    if w1 and w2:
        if w1 in atp_r2_winners_03:
            assert w2 not in atp_r2_winners_03
            atp_r2_locked_03[(w1, w2)] = w1
        elif w2 in atp_r2_winners_03:
            atp_r2_locked_03[(w1, w2)] = w2

print(f"ATP R1 locked: {len(atp_r1_locked_03)} / 64 (expected 64)")
print(f"ATP R2 locked: {len(atp_r2_locked_03)} / 32 (expected 22)")
assert len(atp_r1_locked_03) == 64, f"Got {len(atp_r1_locked_03)}"
assert len(atp_r2_locked_03) == 22, f"Got {len(atp_r2_locked_03)}"

extra_atp_elo_03 = {
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

def sim_atp(bracket, elo_dict, us_set, locked_r1=None, locked_r2=None,
            alc_mix=None, tia_mix=None, zve_mix=None, elo_tweaks=None,
            n_trials=60000, seed=9300):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    locked_r2 = locked_r2 or {}
    elos_base = []
    for nm in bracket:
        if nm.startswith("Q_"):
            el = 1830.0
        elif nm in elo_dict:
            el = float(elo_dict[nm])
        elif nm in extra_atp_elo_03:
            el = float(extra_atp_elo_03[nm])
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

    locked_r2_pairs = {}
    for (a_nm, b_nm), w_nm in locked_r2.items():
        ia = bracket.index(a_nm)
        ib = bracket.index(b_nm)
        iw = ia if w_nm == a_nm else ib
        locked_r2_pairs[(ia, ib)] = iw
        locked_r2_pairs[(ib, ia)] = iw

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

def run_atp_blend(bracket, us_set, locked_r1, locked_r2=None, alc_mix=None, tia_mix=None, zve_mix=None, elo_tweaks=None, seed_base=9300):
    b_tc = Counter(); b_fc = Counter(); b_r4 = Counter(); b_qf = Counter(); b_sf = Counter()
    b_cond = Counter(); b_uncond = Counter(); b_tie = 0.0
    for idx, (lbl, w, ed) in enumerate(regimes_cal):
        tc, fc, r4c, qfc, sfc, cu, uu, tr = sim_atp(
            bracket, ed, us_set, locked_r1=locked_r1, locked_r2=locked_r2,
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
    atp_bracket_raw, us_men_28, None, None, None, None, None, None, 9100
)

# Model A: Strict outcome-only Bayes (Alcaraz updated cleanly for beating Safiullin + Faria)
alc_prior = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
w_r1r2 = [w * p_bo5(e, 1895.0) * p_bo5(e, 1845.0) for e, w in alc_prior]
s_r1r2 = sum(w_r1r2)
alc_mix_A = [(e, ww / s_r1r2) for (e, _), ww in zip(alc_prior, w_r1r2)]

m03A_tc, m03A_fc, m03A_r4, m03A_qf, m03A_sf, m03A_cu, m03A_uu, m03A_tie = run_atp_blend(
    atp_bracket_03, us_men_03, atp_r1_locked_03, atp_r2_locked_03,
    alc_mix_A, None, None, None, 9600
)

# Model B: Conservative Margin/Form/Fatigue Bayes
# Alcaraz dropped set 1 rushing, then crushed Faria 6-0 6-3 6-2 over 2h40m with healthy wrist!
alc_mix_B = [(2280.0, 0.48), (2175.0, 0.42), (2045.0, 0.085), (1750.0, 0.015)]
# Tiafoe bounced back from R1 5-setter with clean 6-3 7-6(2) 7-5 win over Sakamoto
tia_mix_B = [(0.0, 0.80), (-35.0, 0.15), (-95.0, 0.05)]
# Zverev unchanged pending Thu night R2 vs Halys (4h53m 1:55am thriller vs Sonego)
zve_mix_B = [(0.0, 0.55), (-25.0, 0.30), (-60.0, 0.15)]
tweaks_B = {
    "Taylor Fritz":            +16.0,   # 6-3 6-2 6-4 R1 + 6-0 6-1 6-1 (98m!) R2! Peak NY form!
    "Daniil Medvedev":         +16.0,   # Back-to-back clean 3-setters (Gaston, Gorzny)
    "Alex Michelsen":          +28.0,   # Crushed Cina & #16 Nakashima 6-3 6-4 6-4
    "Ben Shelton":             +10.0,   # Beat Griekspoor & Hurkacz in 4
    "Learner Tien":            +12.0,   # Crushed Borges 6-4 6-1 6-2 (plays Monfils Thu night)
    "Tommy Paul":              +5.0,    # Clean into R3 (beat Prizmic in 4)
    "Alexander Bublik":        +18.0,   # Crushed Mannarino 6-3 6-1 6-1!
    "Karen Khachanov":         +20.0,   # Crushed #3 FAA in 4 (broke 7x!)
    "Jakub Mensik":            +6.0,    # Beat Rodionov in 4
    "Alex de Minaur":          +8.0,    # Crisp 6-2 6-2 6-4 R1
    "Denis Shapovalov":        +12.0,   # Crushed Van Assche 6-0 6-4 7-6(7)
    "Jiri Lehecka":            +8.0,    # Clean 6-4 6-2 6-4
    "Stefanos Tsitsipas":      +14.0,   # Beat #10 Fils & Harris in 4
    "Francisco Cerundolo":     -10.0,   # 5-set grueler vs Struff before facing fresh Fritz!
    "Flavio Cobolli":          -15.0,   # 4h13m 5-setter R1
    "Mariano Navone":          +24.0,   # Beat Djokovic & Berrettini in 4!
    "Dane Sweeny":             +25.0,   # Crushed #13 Musetti 3-6 6-1 6-2 6-2!
    "Daniel Merida":           +30.0,   # Beat Fucsovics & #23 Rublev!
    "Yibing Wu":               +14.0,   # Beat Walton & Duckworth 7-5 6-3 6-1
    "Valentin Vacherot":       +8.0,
    "Tomas Martin Etcheverry": +8.0,
    "Arthur Rinderknech":      +8.0,
    "Michael Zheng":           +20.0,
    "Zachary Svajda":          +15.0,
}

m03B_tc, m03B_fc, m03B_r4, m03B_qf, m03B_sf, m03B_cu, m03B_uu, m03B_tie = run_atp_blend(
    atp_bracket_03, us_men_03, atp_r1_locked_03, atp_r2_locked_03,
    alc_mix_B, tia_mix_B, zve_mix_B, tweaks_B, 9700
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

updA, fA, totA = bayes_update_atp(m03A_tc)
updB, fB, totB = bayes_update_atp(m03B_tc)

print("\n" + "=" * 106)
print(f"Q3 (891014) MEN'S SINGLES — THU SEP 3 DAY 5 BAYESIAN UPDATE (Pre-norm sums: A={totA:.4f}, B={totB:.4f})")
print("=" * 106)
print(f"{'Player':22s} | {'MC28':6s} | {'MC03A':6s} | {'MC03B':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(updB.items(), key=lambda x: -x[1])[:15]:
    print(f"{k:22s} | {m28_tc.get(k,0):6.4f} | {m03A_tc.get(k,0):6.4f} | {m03B_tc.get(k,0):6.4f} | {aug28_named.get(k,0):6.4f} | {updA[k]:6.4f} | {updB[k]:6.4f} | {m03B_sf.get(k,0):5.3f} | {m03B_fc.get(k,0):5.3f}")
print(f"{'Field_Rest':22s} | {1-sum(m28_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m03A_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m03B_tc.get(k,0) for k in aug28_named):6.4f} | {field_28:6.4f} | {fA:6.4f} | {fB:6.4f} |")
print("Top-8 UpdA:", [(k, round(v, 4)) for k, v in sorted(updA.items(), key=lambda x: -x[1])[:8]])
print("Top-8 UpdB:", [(k, round(v, 4)) for k, v in sorted(updB.items(), key=lambda x: -x[1])[:8]])
print("MC03B raw top-10 (incl Field players):", [(k, round(v, 4)) for k, v in m03B_tc.most_common(10)])

print("\n" + "=" * 106)
print(f"Q1 (408930) FURTHEST U.S. MAN — THU SEP 3 DAY 5 UPDATE (Tie: 28={m28_tie:.4f}, A={m03A_tie:.4f}, B={m03B_tie:.4f})")
print("=" * 106)
print(f"{'Player':22s} | {'Cond28':7s} | {'CondA':7s} | {'CondB':7s} | {'UncondB':7s} | {'R4_B':5s} | {'QF_B':5s} | {'SF_B':5s}")
for k, _ in sorted(m03B_cu.items(), key=lambda x: -x[1])[:10]:
    print(f"{k:22s} | {m28_cu.get(k,0):7.4f} | {m03A_cu.get(k,0):7.4f} | {m03B_cu.get(k,0):7.4f} | {m03B_uu.get(k,0):7.4f} | {m03B_r4[k]:5.3f} | {m03B_qf[k]:5.3f} | {m03B_sf[k]:5.3f}")

# ------------------------------------------------------------------------------
# PART 2: WTA EXACT 128-PLAYER BRACKET (61/64 R1 + 22/32 R2 LOCKED!)
# ------------------------------------------------------------------------------
wta_r1_winners_03 = {
    # Q1 (16/16 LOCKED!)
    "Aryna Sabalenka", "Polina Iatcenko", "Oksana Selekhmeteva", "Kamilla Rakhimova",
    "Taylor Townsend", "Taylah Preston", "Karolina Pliskova", "Diana Shnaider",
    "Marta Kostyuk", "Sloane Stephens", "Kimberly Birrell", "Ekaterina Alexandrova",
    "Ann Li", "Donna Vekic", "Lanlana Tararudee", "Linda Noskova",
    # Q2 (16/16 LOCKED!)
    "Jessica Pegula", "Sofia Kenin", "Mananchaya Sawangkaew", "Leylah Fernandez",
    "Jasmine Paolini", "Lucrezia Stefanini", "Diane Parry", "Sorana Cirstea",
    "Elina Svitolina", "Maya Joint", "Xinyu Wang", "Anna Kalinskaya",
    "Emma Navarro", "Caty McNally", "Katie Boulter", "Karolina Muchova",
    # Q3 (14/16 locked — unconfirmed: Potapova/Valentova, Rus/Jeanjean)
    "Mirra Andreeva", "Eva Lys", "Nikola Bartunkova", "Tatjana Maria",
    "Lilli Tagger", "Amanda Anisimova", "Iva Jovic", "Francesca Jones",
    "Oleksandra Oliynykova", "Alexandra Eala", "Cristina Bucsa", "Himeno Sakatsume",
    "Paula Badosa", "Coco Gauff",
    # Q4 (15/16 locked — unconfirmed: Putintseva/Bencic)
    "Iga Swiatek", "Nadia Podoroska", "Harriet Dart", "Marie Bouzkova",
    "Madison Keys", "Anna Bondar", "Qinwen Zheng", "Naomi Osaka",
    "Katerina Siniakova", "Maria Timofeeva", "Elise Mertens", "Maria Sakkari",
    "Yuliia Starodubtseva", "Jessica Bouzas Maneiro", "Elena Rybakina",
}

# Confirmed WTA R2 winners as of Thu Sep 3 ~5:05 PM ET (22 / 32 LOCKED!)
wta_r2_winners_03 = {
    # Q1 (7/8 — only Alexandrova vs Birrell unconfirmed)
    "Aryna Sabalenka",     # def. Iatcenko 6-1 6-1 (53 min!)
    "Kamilla Rakhimova",   # def. Selekhmeteva 6-3 6-0
    "Taylor Townsend",     # def. Preston 6-1 6-1
    "Diana Shnaider",      # def. Pliskova 6-1 7-6(4)
    "Marta Kostyuk",       # def. Stephens 6-1 7-5
    "Ann Li",              # def. Donna Vekic
    "Linda Noskova",       # def. Tararudee 6-4 6-2
    # Q2 (8/8 ALL LOCKED!)
    "Jessica Pegula",      # def. Kenin 6-3 6-1
    "Leylah Fernandez",    # def. Sawangkaew 6-4 6-1
    "Jasmine Paolini",     # def. Stefanini 6-4 6-1
    "Sorana Cirstea",      # def. Parry 6-2 7-5
    "Elina Svitolina",     # def. Joint 6-2 6-7(6) 6-4
    "Anna Kalinskaya",     # def. Xinyu Wang
    "Emma Navarro",        # def. McNally 3-6 6-2 6-3
    "Karolina Muchova",    # def. Boulter 6-1 6-0
    # Q3 (2/8)
    "Amanda Anisimova",    # def. Tagger 6-3 3-6 6-1
    "Alexandra Eala",      # def. Oliynykova 6-1 6-4 (1 hr!)
    # Q4 (5/8)
    "Iga Swiatek",         # def. Podoroska 6-3 6-2 (71 min!)
    "Marie Bouzkova",      # def. Harriet Dart
    "Madison Keys",        # def. Bondar 5-7 6-4 7-6 (saved 5 MPs!)
    "Naomi Osaka",         # def. Siniakova 6-2 5-7 6-1
    "Elise Mertens",       # def. Timofeeva 6-2 7-6(5)
}

wta_r1_locked_03 = {}
for i in range(0, 128, 2):
    a, b = wta_bracket_raw[i], wta_bracket_raw[i+1]
    if a in wta_r1_winners_03:
        assert b not in wta_r1_winners_03, f"Both in WTA R1 winners: {a}, {b}"
        wta_r1_locked_03[(a, b)] = a
    elif b in wta_r1_winners_03:
        wta_r1_locked_03[(a, b)] = b

wta_r2_locked_03 = {}
for i in range(0, 128, 4):
    w1 = wta_r1_locked_03.get((wta_bracket_raw[i], wta_bracket_raw[i+1]))
    w2 = wta_r1_locked_03.get((wta_bracket_raw[i+2], wta_bracket_raw[i+3]))
    if w1 and w2:
        if w1 in wta_r2_winners_03:
            assert w2 not in wta_r2_winners_03
            wta_r2_locked_03[(w1, w2)] = w1
        elif w2 in wta_r2_winners_03:
            wta_r2_locked_03[(w1, w2)] = w2

print(f"\nWTA R1 locked: {len(wta_r1_locked_03)} / 64 (expected 61)")
print(f"WTA R2 locked: {len(wta_r2_locked_03)} / 32 (expected 22)")
assert len(wta_r1_locked_03) == 61, f"Got {len(wta_r1_locked_03)}"
assert len(wta_r2_locked_03) == 22, f"Got {len(wta_r2_locked_03)}"

def sim_wta(locked_r1=None, locked_r2=None, ryb_mix=None, sab_mix=None, elo_adj=None, r1_cal_override=False, n_trials=90000, seed=9500):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    locked_r2 = locked_r2 or {}
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
w28_t, _, _ = sim_wta(locked_r1=None, locked_r2=None, r1_cal_override=False, n_trials=90000, seed=9501)
w28_cal_t, _, _ = sim_wta(locked_r1=None, locked_r2=None, r1_cal_override=True, n_trials=90000, seed=9511)

# Model A: Strict Outcome-Only
ryb_prior_30 = [(2130.0, 0.52), (2065.0, 0.28), (1970.0, 0.14), (1740.0, 0.06)]
wr_a = [w * p_bo3(e, 1715.0) for e, w in ryb_prior_30]
ryb_mix_A = [(e, ww / sum(wr_a)) for (e, _), ww in zip(ryb_prior_30, wr_a)]
sab_prior_28 = [(2225.0, 0.45), (2175.0, 0.35), (2085.0, 0.20)]
ws_a = [w * p_bo3(e, 1845.0) * p_bo3(e, 1795.0) for e, w in sab_prior_28]
sab_mix_A = [(e, ww / sum(ws_a)) for (e, _), ww in zip(sab_prior_28, ws_a)]

w03A_t, w03A_f, w03A_sf = sim_wta(
    locked_r1=wta_r1_locked_03, locked_r2=wta_r2_locked_03,
    ryb_mix=ryb_mix_A, sab_mix=sab_mix_A, r1_cal_override=False, n_trials=90000, seed=9520
)

# Model B: Conservative Health/Form Bayes
ryb_mix_B = [(2130.0, 0.65), (2065.0, 0.22), (1970.0, 0.09), (1740.0, 0.04)]
sab_mix_B = [(2225.0, 0.62), (2175.0, 0.29), (2085.0, 0.09)]
wta_tweaks_B = {
    "Coco Gauff":       wta_cal_elo["Coco Gauff"] + 6.0,        # Crisp serving vs Sonmez (plays Badosa Thu night)
    "Paula Badosa":     wta_cal_elo["Paula Badosa"] + 25.0,     # Healthy former #2, crushed Kasatkina, 5-3 H2H vs Gauff!
    "Iga Swiatek":      wta_cal_elo["Iga Swiatek"] + 12.0,      # Clean 6-2 6-3 R1 + 6-3 6-2 (71m) R2!
    "Jessica Pegula":   wta_cal_elo["Jessica Pegula"] + 14.0,   # 56-min 6-3 6-1 demolition of Kenin
    "Mirra Andreeva":   wta_cal_elo["Mirra Andreeva"] + 12.0,   # Crushed Tjen 6-2 6-2 (plays Lys Thu)
    "Naomi Osaka":      wta_cal_elo["Naomi Osaka"] - 12.0,      # Rusty R1 + 20 UEs set 2 vs Siniakova
    "Amanda Anisimova": wta_cal_elo["Amanda Anisimova"] + 4.0,  # Dropped set to Tagger 6-3 3-6 6-1
    "Karolina Muchova": wta_cal_elo["Karolina Muchova"] + 20.0, # Demolished Boulter 6-1 6-0
    "Marta Kostyuk":    wta_cal_elo["Marta Kostyuk"] + 6.0,     # Into R3
    "Linda Noskova":    wta_cal_elo["Linda Noskova"] + 8.0,     # Clean 6-4 6-2 vs Tararudee
    "Alexandra Eala":   wta_cal_elo["Alexandra Eala"] + 16.0,   # 6-1 6-2 R1 + 6-1 6-4 (1hr) R2!
    "Madison Keys":     wta_cal_elo["Madison Keys"] - 10.0,     # Saved 5 MPs in grueling 3-setter vs Bondar
    "Elina Svitolina":  wta_cal_elo["Elina Svitolina"] - 4.0,   # 2h10m 3-setter vs Maya Joint
}
w03B_t, w03B_f, w03B_sf = sim_wta(
    locked_r1=wta_r1_locked_03, locked_r2=wta_r2_locked_03,
    ryb_mix=ryb_mix_B, sab_mix=sab_mix_B,
    elo_adj=wta_tweaks_B, r1_cal_override=False, n_trials=90000, seed=9530
)

# Model C: Same as B + R1-market-prob calibration
w03C_t, w03C_f, w03C_sf = sim_wta(
    locked_r1=wta_r1_locked_03, locked_r2=wta_r2_locked_03,
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

wupdA, wfA, wtotA = bayes_update_wta(w03A_t, w28_t)
wupdB, wfB, wtotB = bayes_update_wta(w03B_t, w28_t)
wupdC, wfC, wtotC = bayes_update_wta(w03C_t, w28_cal_t)

print("\n" + "=" * 110)
print(f"Q2 (608158) WOMEN'S SINGLES — THU SEP 3 DAY 5 BAYESIAN UPDATE (Pre-norm: A={wtotA:.4f}, B={wtotB:.4f}, C={wtotC:.4f})")
print("=" * 110)
print(f"{'Player':20s} | {'MC28':6s} | {'MC03B':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'UpdC(cal)':9s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(wupdC.items(), key=lambda x: -x[1])[:13]:
    print(f"{k:20s} | {w28_t[k]:6.4f} | {w03B_t[k]:6.4f} | {aug28_wta_exact[k]:6.4f} | {wupdA[k]:6.4f} | {wupdB[k]:6.4f} | {wupdC[k]:9.4f} | {w03B_sf[k]:5.3f} | {w03B_f[k]:5.3f}")
print("WTA Top-8 UpdA:", [(k, round(v, 4)) for k, v in sorted(wupdA.items(), key=lambda x: -x[1])[:8]])
print("WTA Top-8 UpdB:", [(k, round(v, 4)) for k, v in sorted(wupdB.items(), key=lambda x: -x[1])[:8]])
print("WTA Top-8 UpdC:", [(k, round(v, 4)) for k, v in sorted(wupdC.items(), key=lambda x: -x[1])[:8]])
print("Gauff vs Badosa R2 prob (B):", round(p_bo3(wta_tweaks_B["Coco Gauff"], wta_tweaks_B["Paula Badosa"]), 4))
