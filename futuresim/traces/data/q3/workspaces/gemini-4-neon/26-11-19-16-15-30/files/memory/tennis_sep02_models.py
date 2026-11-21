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
# DAY 4 (WEDNESDAY SEP 2, 2026, ~21:50 GMT / 5:50 PM ET) EXACT-BRACKET BAYES MC
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
# PART 1: ATP EXACT 128-PLAYER BRACKET (59/64 R1 + 6/32 R2 LOCKED!)
# ------------------------------------------------------------------------------
atp_replacements_02 = {
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
atp_bracket_02 = [atp_replacements_02.get(x, x) for x in atp_bracket_raw]

us_men_02 = {
    "Taylor Fritz", "Ben Shelton", "Frances Tiafoe", "Learner Tien",
    "Brandon Nakashima", "Tommy Paul",
    "Alex Michelsen", "Marcos Giron", "Zachary Svajda", "Jenson Brooksby",
    "Aleksandar Kovacevic", "Martin Damm", "Darwin Blanch", "J.J. Wolf",
    "Stefan Gorzny", "Jack Kennedy", "Michael Zheng",
    "Nishesh Basavareddy",
}
us_men_28 = set(us_men_02) - {"Nishesh Basavareddy"} | {"Q_4", "Q_10"}

# Confirmed ATP R1 winners (59 / 64 locked!)
atp_r1_winners_02 = {
    # Q1 (14/16 locked — unconfirmed: Sweeny/Moutet, J.M. Cerundolo/Gea)
    "Alexander Zverev",         # def. Sonego 6-4 3-6 6-7(7) 7-5 6-4 (4h53m, 1:55am!)
    "Quentin Halys",            # def. Diaz Acosta
    "Alexei Popyrin",           # def. Dimitrov
    "Alejandro Tabilo",         # def. Hanfmann
    "Luciano Darderi",          # def. Wendelken
    "Dalibor Svrcina",          # def. Royer
    "Lorenzo Musetti",          # def. Fery 6-3 6-3 7-5!
    "Yunchaokete Bu",           # def. #12 Rafael Jodar 6-2 6-1 6-1!! MASSIVE UPSET!
    "Michael Zheng",            # def. Marozsan 6-4 6-4 6-2!! (US!)
    "Zachary Svajda",           # def. Altmaier 6-3 6-1 6-7(5) 6-2!! (US!)
    "Zizou Bergs",              # def. Taberner 6-3 3-6 6-2 6-2
    "Jesper De Jong",           # def. Passaro 2-6 6-2 4-6 6-3 6-2
    "Botic van de Zandschulp",  # def. Choinski 6-3 6-1 7-6(5)
    "Alex de Minaur",           # def. Guerrieri 6-2 6-2 6-4!
    # Q2 (13/16 locked — unconfirmed: Vallejo/Monfils, Ugo Carabelli/Struff, Basavareddy/Schoolkate)
    "Felix Auger-Aliassime",    # def. Hijikata
    "Karen Khachanov",          # def. Burruchaga
    "Benjamin Bonzi",           # def. Molcan 6-4 3-6 6-3 6-2
    "Ignacio Buse",             # def. Marcos Giron 3-6 6-3 6-3 6-7(6) 6-1 (Giron OUT!)
    "Jakub Mensik",             # def. Mochizuki
    "Jurij Rodionov",           # def. Mpetshi Perricard
    "Learner Tien",             # def. Borges 6-4 6-1 6-2
    "Taylor Fritz",             # def. Blanch 6-3 6-2 6-4
    "Mattia Bellucci",          # def. Piros
    "Francisco Cerundolo",      # def. Misolic
    "Alexander Blockx",         # def. Barrios Vera
    "Marco Trungelliti",        # def. Shang
    "Flavio Cobolli",           # def. Comesana in 5 (4h13m)
    # Q3 (16/16 LOCKED!)
    "Daniil Medvedev",          # def. Gaston
    "Stefan Gorzny",            # def. Collignon
    "Jaume Munar",              # def. Atmane
    "Arthur Rinderknech",       # def. Shimabukuro
    "Valentin Vacherot",        # def. Kovacevic
    "Kamil Majchrzak",          # def. Medjedovic
    "Rei Sakamoto",             # def. Vukic
    "Frances Tiafoe",           # def. Damm
    "Brandon Nakashima",        # def. Baez
    "Alex Michelsen",           # def. Cina
    "Daniel Merida",            # def. Fucsovics
    "Andrey Rublev",            # def. Virtanen
    "Tomas Martin Etcheverry",  # def. Kopriva
    "Jacob Fearnley",           # def. Landaluce
    "Matteo Berrettini",        # def. Wawrinka
    "Mariano Navone",           # def. Djokovic!!
    # Q4 (16/16 LOCKED!)
    "Ben Shelton",              # def. Griekspoor
    "Hubert Hurkacz",           # def. Dzumhur
    "Denis Shapovalov",         # def. Kecmanovic
    "Luca Van Assche",          # def. Norrie
    "Jiri Lehecka",             # def. Carreno Busta
    "Toby Samuel",              # def. Machac
    "Lloyd Harris",             # def. Kennedy
    "Stefanos Tsitsipas",       # def. Fils!!
    "Alexander Bublik",         # def. Wolf
    "Adrian Mannarino",         # def. Tirante
    "Dino Prizmic",             # def. Shevchenko
    "Tommy Paul",               # def. Wong
    "James Duckworth",          # def. Arnaldi
    "Yibing Wu",                # def. Walton
    "Jaime Faria",              # def. Brooksby
    "Carlos Alcaraz",           # def. Safiullin
}

# Confirmed ATP R2 winners as of Wed Sep 2, ~5:50 PM ET (6 / 32 locked!)
atp_r2_winners_02 = {
    "Daniil Medvedev",          # def. Stefan Gorzny 6-1 6-3 7-5! (Gorzny OUT!)
    "Arthur Rinderknech",       # def. Jaume Munar 7-6(4) 6-2 7-5!
    "Alex Michelsen",           # def. #16 Brandon Nakashima 6-3 6-4 6-4!! (Nakashima OUT!)
    "Daniel Merida",            # def. #23 Andrey Rublev 6-7(3) 6-2 6-4 6-4!! (Rublev OUT!)
    "Tomas Martin Etcheverry",  # def. Jacob Fearnley 6-3 6-3 3-6 6-3!
    "Ben Shelton",              # def. Hubert Hurkacz 6-3 5-7 7-6(3) 7-5!!
}

atp_r1_locked_02 = {}
for i in range(0, 128, 2):
    a, b = atp_bracket_02[i], atp_bracket_02[i+1]
    if a in atp_r1_winners_02:
        assert b not in atp_r1_winners_02, f"Both in R1 winners: {a}, {b}"
        atp_r1_locked_02[(a, b)] = a
    elif b in atp_r1_winners_02:
        atp_r1_locked_02[(a, b)] = b

atp_r2_locked_02 = {}
for i in range(0, 128, 4):
    # Check if both feeder R1s are locked and one of them won R2
    w1 = atp_r1_locked_02.get((atp_bracket_02[i], atp_bracket_02[i+1]))
    w2 = atp_r1_locked_02.get((atp_bracket_02[i+2], atp_bracket_02[i+3]))
    if w1 and w2:
        if w1 in atp_r2_winners_02:
            assert w2 not in atp_r2_winners_02
            atp_r2_locked_02[(w1, w2)] = w1
        elif w2 in atp_r2_winners_02:
            atp_r2_locked_02[(w1, w2)] = w2

print(f"ATP R1 locked: {len(atp_r1_locked_02)} / 64 (expected 59)")
print(f"ATP R2 locked: {len(atp_r2_locked_02)} / 32 (expected 6)")
assert len(atp_r1_locked_02) == 59, f"Got {len(atp_r1_locked_02)}"
assert len(atp_r2_locked_02) == 6, f"Got {len(atp_r2_locked_02)}"

extra_atp_elo_02 = {
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
    "Yunchaokete Bu":      1865.0,  # Crushed Jodar 6-2 6-1 6-1 -> bump from 1840!
}

def sim_atp(bracket, elo_dict, us_set, locked_r1=None, locked_r2=None,
            alc_mix=None, tia_mix=None, zve_mix=None, elo_tweaks=None,
            n_trials=60000, seed=9200):
    rng = random.Random(seed)
    locked_r1 = locked_r1 or {}
    locked_r2 = locked_r2 or {}
    elos_base = []
    for nm in bracket:
        if nm.startswith("Q_"):
            el = 1830.0
        elif nm in elo_dict:
            el = float(elo_dict[nm])
        elif nm in extra_atp_elo_02:
            el = float(extra_atp_elo_02[nm])
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

    # Pre-index locked R1 and R2 by slot index
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

def run_atp_blend(bracket, us_set, locked_r1, locked_r2=None, alc_mix=None, tia_mix=None, zve_mix=None, elo_tweaks=None, seed_base=9200):
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

# Model A: Strict outcome-only Bayes (zero margin/fatigue Elo tweaks!)
alc_prior = [(2280.0, 0.30), (2175.0, 0.44), (2045.0, 0.22), (1750.0, 0.04)]
w_r1_only = [w * p_bo5(e, 1895.0) for e, w in alc_prior]
s_r1 = sum(w_r1_only)
alc_mix_A = [(e, ww / s_r1) for (e, _), ww in zip(alc_prior, w_r1_only)]

m02A_tc, m02A_fc, m02A_r4, m02A_qf, m02A_sf, m02A_cu, m02A_uu, m02A_tie = run_atp_blend(
    atp_bracket_02, us_men_02, atp_r1_locked_02, atp_r2_locked_02,
    alc_mix_A, None, None, None, 9600
)

# Model B: Conservative Margin/Form/Fatigue Bayes
alc_mix_B = [(2280.0, 0.42), (2175.0, 0.46), (2045.0, 0.095), (1750.0, 0.025)]
tia_mix_B = [(0.0, 0.70), (-35.0, 0.22), (-95.0, 0.08)]
# Zverev survived 4h53m 1:55am thriller vs #89 Sonego (2 pts from defeat) after Montreal/Cinci losses:
# Conservative form/fatigue mixture: 55% full form (0), 30% mild fatigue/dip (-25), 15% deeper dip (-60) -> mean -16.5 Elo
zve_mix_B = [(0.0, 0.55), (-25.0, 0.30), (-60.0, 0.15)]
tweaks_B = {
    "Daniil Medvedev":         +16.0,   # Back-to-back clean 3-setters (Gaston, Gorzny), calm & sharp!
    "Alex Michelsen":          +28.0,   # Crushed Cina 6-4 6-1 6-0 AND crushed #16 Nakashima 6-3 6-4 6-4!!
    "Ben Shelton":             +10.0,   # Beat Griekspoor in 4 AND Hurkacz in 4 (44 winners, 73% 1st serve)!
    "Learner Tien":            +12.0,   # Crushed Borges 6-4 6-1 6-2
    "Taylor Fritz":            +5.0,    # Clean 6-3 6-2 6-4
    "Tommy Paul":              +5.0,
    "Alex de Minaur":          +8.0,    # Crisp 6-2 6-2 6-4 vs Guerrieri
    "Lorenzo Musetti":         +8.0,    # Crisp 6-3 6-3 7-5 vs Wim SFist Fery
    "Daniel Merida":           +30.0,   # Beat Fucsovics in 3 AND #23 Rublev in 4! (1815->1845)
    "Flavio Cobolli":          -15.0,   # 4h13m 5-setter from 0-2 down
    "Stefanos Tsitsipas":      +12.0,   # Beat #10 Fils in 4
    "Karen Khachanov":         +8.0,
    "Matteo Berrettini":       +8.0,
    "Tomas Martin Etcheverry": +8.0,    # Clean into R3
    "Arthur Rinderknech":      +8.0,    # Clean 3-setter over Munar into R3
    "Michael Zheng":           +20.0,   # Beat Marozsan 6-4 6-4 6-2!
    "Zachary Svajda":          +15.0,   # Beat Altmaier in 4!
}

m02B_tc, m02B_fc, m02B_r4, m02B_qf, m02B_sf, m02B_cu, m02B_uu, m02B_tie = run_atp_blend(
    atp_bracket_02, us_men_02, atp_r1_locked_02, atp_r2_locked_02,
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

updA, fA, totA = bayes_update_atp(m02A_tc)
updB, fB, totB = bayes_update_atp(m02B_tc)

print("\n" + "=" * 106)
print(f"Q3 (891014) MEN'S SINGLES — WED SEP 2 DAY 4 BAYESIAN UPDATE (Pre-norm sums: A={totA:.4f}, B={totB:.4f})")
print("=" * 106)
print(f"{'Player':22s} | {'MC28':6s} | {'MC02A':6s} | {'MC02B':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(updB.items(), key=lambda x: -x[1])[:15]:
    print(f"{k:22s} | {m28_tc.get(k,0):6.4f} | {m02A_tc.get(k,0):6.4f} | {m02B_tc.get(k,0):6.4f} | {aug28_named.get(k,0):6.4f} | {updA[k]:6.4f} | {updB[k]:6.4f} | {m02B_sf.get(k,0):5.3f} | {m02B_fc.get(k,0):5.3f}")
print(f"{'Field_Rest':22s} | {1-sum(m28_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m02A_tc.get(k,0) for k in aug28_named):6.4f} | {1-sum(m02B_tc.get(k,0) for k in aug28_named):6.4f} | {field_28:6.4f} | {fA:6.4f} | {fB:6.4f} |")
print("Top-8 UpdA:", [(k, round(v, 4)) for k, v in sorted(updA.items(), key=lambda x: -x[1])[:8]])
print("Top-8 UpdB:", [(k, round(v, 4)) for k, v in sorted(updB.items(), key=lambda x: -x[1])[:8]])
print("MC02B raw top-10 (incl Field players like Michelsen/Tien):", [(k, round(v, 4)) for k, v in m02B_tc.most_common(10)])

print("\n" + "=" * 106)
print(f"Q1 (408930) FURTHEST U.S. MAN — WED SEP 2 DAY 4 UPDATE (Tie: 28={m28_tie:.4f}, A={m02A_tie:.4f}, B={m02B_tie:.4f})")
print("=" * 106)
print(f"{'Player':22s} | {'Cond28':7s} | {'CondA':7s} | {'CondB':7s} | {'UncondB':7s} | {'R4_B':5s} | {'QF_B':5s} | {'SF_B':5s}")
for k, _ in sorted(m02B_cu.items(), key=lambda x: -x[1])[:12]:
    print(f"{k:22s} | {m28_cu.get(k,0):7.4f} | {m02A_cu.get(k,0):7.4f} | {m02B_cu.get(k,0):7.4f} | {m02B_uu.get(k,0):7.4f} | {m02B_r4[k]:5.3f} | {m02B_qf[k]:5.3f} | {m02B_sf[k]:5.3f}")

# ------------------------------------------------------------------------------
# PART 2: WTA EXACT 128-PLAYER BRACKET (58/64 R1 + 10/32 R2 LOCKED!)
# ------------------------------------------------------------------------------
wta_r1_winners_02 = {
    # Q1 (ALL 16/16 LOCKED!)
    "Aryna Sabalenka", "Polina Iatcenko", "Oksana Selekhmeteva", "Kamilla Rakhimova",
    "Taylor Townsend", "Taylah Preston", "Karolina Pliskova", "Diana Shnaider",
    "Marta Kostyuk", "Sloane Stephens", "Kimberly Birrell", "Ekaterina Alexandrova",
    "Ann Li", "Donna Vekic", "Lanlana Tararudee", "Linda Noskova",
    # Q2 (ALL 16/16 LOCKED!)
    "Jessica Pegula", "Sofia Kenin", "Mananchaya Sawangkaew", "Leylah Fernandez",
    "Jasmine Paolini", "Lucrezia Stefanini", "Diane Parry", "Sorana Cirstea",
    "Elina Svitolina", "Maya Joint", "Xinyu Wang", "Anna Kalinskaya",
    "Emma Navarro", "Caty McNally", "Katie Boulter", "Karolina Muchova",
    # Q3 (13/16 locked — unconfirmed: Potapova/Valentova, Rus/Jeanjean, Jovic/Frech)
    "Mirra Andreeva", "Eva Lys", "Nikola Bartunkova", "Tatjana Maria",
    "Lilli Tagger", "Amanda Anisimova", "Francesca Jones", "Oleksandra Oliynykova",
    "Alexandra Eala", "Cristina Bucsa", "Himeno Sakatsume", "Paula Badosa",
    "Coco Gauff",
    # Q4 (13/16 locked — unconfirmed: Putintseva/Bencic, Quevedo/Mertens, Vidmanova/Bouzas Maneiro)
    "Iga Swiatek", "Nadia Podoroska", "Harriet Dart", "Marie Bouzkova",
    "Madison Keys", "Anna Bondar", "Qinwen Zheng", "Naomi Osaka",
    "Katerina Siniakova", "Maria Timofeeva", "Maria Sakkari", "Yuliia Starodubtseva",
    "Elena Rybakina",
}

# Confirmed WTA R2 winners as of Wed Sep 2, ~5:50 PM ET (10 / 32 locked!)
wta_r2_winners_02 = {
    # Q1 (4 locked)
    "Kamilla Rakhimova",   # def. Selekhmeteva 6-3 6-0
    "Taylor Townsend",     # def. Preston 6-1 6-1
    "Diana Shnaider",      # def. Pliskova 6-1 7-6(4)
    "Marta Kostyuk",       # def. Stephens 6-1 7-5
    # Q2 (6 locked)
    "Jessica Pegula",      # def. Kenin 6-3 6-1 (56 min!)
    "Leylah Fernandez",    # def. Sawangkaew 6-4 6-1
    "Jasmine Paolini",     # def. Stefanini 6-4 6-1
    "Sorana Cirstea",      # def. Parry 6-2 7-5
    "Emma Navarro",        # def. McNally 3-6 6-2 6-3
    "Karolina Muchova",    # def. Boulter 6-1 6-0!!
}

wta_r1_locked_02 = {}
for i in range(0, 128, 2):
    a, b = wta_bracket_raw[i], wta_bracket_raw[i+1]
    if a in wta_r1_winners_02:
        assert b not in wta_r1_winners_02, f"Both in WTA R1 winners: {a}, {b}"
        wta_r1_locked_02[(a, b)] = a
    elif b in wta_r1_winners_02:
        wta_r1_locked_02[(a, b)] = b

wta_r2_locked_02 = {}
for i in range(0, 128, 4):
    w1 = wta_r1_locked_02.get((wta_bracket_raw[i], wta_bracket_raw[i+1]))
    w2 = wta_r1_locked_02.get((wta_bracket_raw[i+2], wta_bracket_raw[i+3]))
    if w1 and w2:
        if w1 in wta_r2_winners_02:
            assert w2 not in wta_r2_winners_02
            wta_r2_locked_02[(w1, w2)] = w1
        elif w2 in wta_r2_winners_02:
            wta_r2_locked_02[(w1, w2)] = w2

print(f"\nWTA R1 locked: {len(wta_r1_locked_02)} / 64 (expected 58)")
print(f"WTA R2 locked: {len(wta_r2_locked_02)} / 32 (expected 10)")
assert len(wta_r1_locked_02) == 58, f"Got {len(wta_r1_locked_02)}"
assert len(wta_r2_locked_02) == 10, f"Got {len(wta_r2_locked_02)}"

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
w02A_t, w02A_f, w02A_sf = sim_wta(
    locked_r1=wta_r1_locked_02, locked_r2=wta_r2_locked_02,
    ryb_mix=ryb_mix_A, r1_cal_override=False, n_trials=90000, seed=9520
)

# Model B: Conservative Health/Form Bayes
ryb_mix_B = [(2130.0, 0.65), (2065.0, 0.22), (1970.0, 0.09), (1740.0, 0.04)]
sab_mix_B = [(2225.0, 0.54), (2175.0, 0.33), (2085.0, 0.13)]
wta_tweaks_B = {
    "Coco Gauff":       wta_cal_elo["Coco Gauff"] + 6.0,        # Crisp serving vs Sonmez 6-3 6-4
    "Iga Swiatek":      wta_cal_elo["Iga Swiatek"] + 6.0,       # Clean 6-2 6-3
    "Jessica Pegula":   wta_cal_elo["Jessica Pegula"] + 14.0,   # 56-min 6-3 6-1 demolition of Kenin (8 UEs!)
    "Mirra Andreeva":   wta_cal_elo["Mirra Andreeva"] + 12.0,   # Crushed Tjen 6-2 6-2
    "Naomi Osaka":      wta_cal_elo["Naomi Osaka"] - 10.0,      # Rusty 7-6 7-6 vs #101 Zakharova
    "Amanda Anisimova": wta_cal_elo["Amanda Anisimova"] + 10.0,
    "Karolina Muchova": wta_cal_elo["Karolina Muchova"] + 20.0, # Demolished Boulter 6-1 6-0!!
    "Marta Kostyuk":    wta_cal_elo["Marta Kostyuk"] + 6.0,     # Into R3 (6-1 7-5)
    "Alexandra Eala":   wta_cal_elo["Alexandra Eala"] + 10.0,   # Crushed Stoiana 6-1 6-2
    "Paula Badosa":     wta_cal_elo["Paula Badosa"] + 12.0,     # Crushed Kasatkina 6-1 6-4 (tricky R2 for Gauff!)
}
w02B_t, w02B_f, w02B_sf = sim_wta(
    locked_r1=wta_r1_locked_02, locked_r2=wta_r2_locked_02,
    ryb_mix=ryb_mix_B, sab_mix=sab_mix_B,
    elo_adj=wta_tweaks_B, r1_cal_override=False, n_trials=90000, seed=9530
)

# Model C: Same as B + R1-market-prob calibration
w02C_t, w02C_f, w02C_sf = sim_wta(
    locked_r1=wta_r1_locked_02, locked_r2=wta_r2_locked_02,
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

wupdA, wfA, wtotA = bayes_update_wta(w02A_t, w28_t)
wupdB, wfB, wtotB = bayes_update_wta(w02B_t, w28_t)
wupdC, wfC, wtotC = bayes_update_wta(w02C_t, w28_cal_t)

print("\n" + "=" * 110)
print(f"Q2 (608158) WOMEN'S SINGLES — WED SEP 2 DAY 4 BAYESIAN UPDATE (Pre-norm: A={wtotA:.4f}, B={wtotB:.4f}, C={wtotC:.4f})")
print("=" * 110)
print(f"{'Player':20s} | {'MC28':6s} | {'MC02B':6s} | {'Post28':6s} | {'UpdA':6s} | {'UpdB':6s} | {'UpdC(cal)':9s} | {'SF_B':5s} | {'F_B':5s}")
for k, _ in sorted(wupdC.items(), key=lambda x: -x[1])[:12]:
    print(f"{k:20s} | {w28_t[k]:6.4f} | {w02B_t[k]:6.4f} | {aug28_wta_exact[k]:6.4f} | {wupdA[k]:6.4f} | {wupdB[k]:6.4f} | {wupdC[k]:9.4f} | {w02B_sf[k]:5.3f} | {w02B_f[k]:5.3f}")
print("WTA Top-8 UpdA:", [(k, round(v, 4)) for k, v in sorted(wupdA.items(), key=lambda x: -x[1])[:8]])
print("WTA Top-8 UpdB:", [(k, round(v, 4)) for k, v in sorted(wupdB.items(), key=lambda x: -x[1])[:8]])
print("WTA Top-8 UpdC:", [(k, round(v, 4)) for k, v in sorted(wupdC.items(), key=lambda x: -x[1])[:8]])
