import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — WEDNESDAY AUG 26, 2026 (T-4d to US Open Start, T-1d to Draw!)
# Batch: tennis (608158, 408930, 891014)
# ==============================================================================

def shin_devig(dec_odds_dict):
    qs = {k: 1.0 / d for k, d in dec_odds_dict.items()}
    s = sum(qs.values())
    if s <= 1.0:
        return {k: v / s for k, v in qs.items()}, 0.0
    lo, hi = 0.0, 0.9999
    for _ in range(100):
        z = 0.5 * (lo + hi)
        tot = sum((math.sqrt(z*z + 4.0*(1.0 - z)*(q*q)/s) - z) / (2.0*(1.0 - z)) for q in qs.values())
        if tot > 1.0:
            lo = z
        else:
            hi = z
    z = 0.5 * (lo + hi)
    return {k: (math.sqrt(z*z + 4.0*(1.0 - z)*(q*q)/s) - z) / (2.0*(1.0 - z)) for k, q in qs.items()}, z

def power_devig(dec_odds_dict):
    qs = {k: 1.0 / d for k, d in dec_odds_dict.items()}
    lo, hi = 1.0, 3.5
    for _ in range(100):
        k_exp = 0.5 * (lo + hi)
        tot = sum(q ** k_exp for q in qs.values())
        if tot > 1.0:
            lo = k_exp
        else:
            hi = k_exp
    k_exp = 0.5 * (lo + hi)
    return {name: q ** k_exp for name, q in qs.items()}, k_exp

def devig_mid(dec_odds_dict):
    sh, z = shin_devig(dec_odds_dict)
    pw, ke = power_devig(dec_odds_dict)
    ov = sum(1.0 / d for d in dec_odds_dict.values())
    return {k: 0.5 * sh[k] + 0.5 * pw[k] for k in dec_odds_dict}, ov, z, ke


# ==============================================================================
# PART 1: Q1 (qid=608158) — 2026 US OPEN WOMEN'S SINGLES (AUG 26)
# ==============================================================================
# 1. Linxi / FanDuel US Sportsbook (Aug 26, post-Gauff Cinci title & Rybakina Achilles slide):
fd_wta_aug26 = {
    "Aryna Sabalenka":   4.40,  # +340
    "Iga Swiatek":       5.80,  # +480
    "Coco Gauff":        6.00,  # +500
    "Naomi Osaka":      11.00,  # +1000
    "Jessica Pegula":   15.00,  # +1400
    "Mirra Andreeva":   15.00,  # +1400
    "Elena Rybakina":   15.00,  # +1400 (lengthened from +950 on Aug 21!)
    "Karolina Muchova": 16.50,  # est scaled from OddsTrader (+1100 vs +1000 tier)
    "Amanda Anisimova": 17.50,  # est
    "Linda Noskova":    19.00,  # est
    "Alexandra Eala":   22.00,  # est
    "Madison Keys":     25.00,  # est
    "Victoria Mboko":   28.00,  # est
    "Field_Rest":        4.35,  # ~23% raw for remaining 115 players (Svitolina, Bencic, Paolini, etc.)
}

# 2. OddsTrader Full Top-15 Board (Aug 25, high US composite overround; Rybakina +700 stale -> adjust separately):
ot_wta_raw = {
    "Aryna Sabalenka":   3.50,  # +250
    "Iga Swiatek":       4.50,  # +350
    "Coco Gauff":        5.75,  # +475
    "Elena Rybakina":    8.00,  # +700 (stale vs Polymarket 6% / Kalshi 3% / FD +1400)
    "Mirra Andreeva":   11.00,  # +1000
    "Jessica Pegula":   11.00,  # +1000
    "Naomi Osaka":      11.00,  # +1000
    "Karolina Muchova": 12.00,  # +1100
    "Amanda Anisimova": 13.00,  # +1200
    "Linda Noskova":    14.00,  # +1300
    "Alexandra Eala":   16.00,  # +1500
    "Madison Keys":     19.00,  # +1800
    "Victoria Mboko":   21.00,  # +2000
    "Field_Rest":        6.50,  # Svitolina +4000, Bencic +4500, + rest (~15.4% raw)
}
# OddsTrader with Rybakina updated to current Achilles injury market (~14.00 matching FD/Poly/Kalshi):
ot_wta_adj = dict(ot_wta_raw)
ot_wta_adj["Elena Rybakina"] = 14.00

# 3. GoBet.com.au (Aug 25):
gobet_wta = {
    "Aryna Sabalenka":   4.33,  # $4.33
    "Iga Swiatek":       5.50,  # $5.50
    "Coco Gauff":        6.00,  # $6.00
    "Naomi Osaka":      11.00,  # est
    "Mirra Andreeva":   13.00,  # $13.00
    "Jessica Pegula":   13.50,  # est
    "Elena Rybakina":   14.00,  # updated from single-figure stale AU line for Achilles news
    "Karolina Muchova": 16.00,
    "Amanda Anisimova": 17.00,
    "Linda Noskova":    18.00,
    "Alexandra Eala":   21.00,
    "Madison Keys":     24.00,
    "Victoria Mboko":   27.00,
    "Field_Rest":        4.40,
}

fd_w, fd_ov, fd_z, fd_k = devig_mid(fd_wta_aug26)
ot_w, ot_ov, ot_z, ot_k = devig_mid(ot_wta_adj)
gb_w, gb_ov, gb_z, gb_k = devig_mid(gobet_wta)

# 4. Prediction Markets (Polymarket Aug 26 >$7M vol + Kalshi Aug 25):
#    Polymarket (Aug 26, TheLines): Sabalenka=0.22, Gauff=0.16, Rybakina=0.06
#    Kalshi (Aug 25, WeeBet): Sabalenka=~0.28, Swiatek=~0.18, Gauff=~0.14, Osaka=~0.08, Rybakina=0.03
#    Note: Kalshi WeeBet numbers (~28, ~18, ~14, ~8, 3 -> sum 71% for 5 players, leaving only 29% for
#    Pegula+Andreeva+Muchova+Anisimova+Noskova+Eala+Keys+Mboko+115 others!) clearly reflect ask/top-of-book
#    quotes with ~1.12x sum; normalizing/devigging Kalshi gently by ~1.10 gives:
#    Sabalenka ~0.255, Swiatek ~0.164, Gauff ~0.127, Osaka ~0.073, Rybakina ~0.030.
#    Blending Polymarket (60%, $7M+ vol, Aug 26) + Kalshi-mid (40%, Aug 25):
#    Sabalenka = 0.60*0.22 + 0.40*0.255 = 0.234
#    Gauff     = 0.60*0.16 + 0.40*0.127 = 0.147
#    Swiatek   = ~0.155 (Kalshi ~0.164, sportsbook ratio Swiatek/Gauff = 1.03-1.15 -> ~0.15-0.16 on Poly too)
#    Osaka     = ~0.073 (Kalshi ~0.073, FD clear #4 at +1000)
#    Rybakina  = 0.60*0.06 + 0.40*0.030 = 0.048
#    Pegula & Andreeva: split remaining ~0.060 / 0.058 tier.

books_wta = {}
for k in fd_wta_aug26:
    books_wta[k] = 0.45 * fd_w[k] + 0.30 * ot_w[k] + 0.25 * gb_w[k]

exch_wta = {
    "Aryna Sabalenka": 0.234,
    "Iga Swiatek":     0.155,
    "Coco Gauff":      0.147,
    "Naomi Osaka":     0.073,
    "Jessica Pegula":  0.060,
    "Mirra Andreeva":  0.058,
    "Elena Rybakina":  0.048,
}
# Remaining mass in exchanges distributed proportionally to books:
rem_exch = 1.0 - sum(exch_wta.values())
rem_books_sum = sum(v for k, v in books_wta.items() if k not in exch_wta)
for k, v in books_wta.items():
    if k not in exch_wta:
        exch_wta[k] = rem_exch * (v / rem_books_sum)

# Final WTA Blend: 50% Sharp Prediction Markets (Poly Aug 26 + Kalshi Aug 25) + 50% Devigged Books (FD+OT+GoBet)
# Small qualitative sanity adjustments:
#   - Sabalenka: Hindustan Times Aug 26 highlights 17-7 post-March slump + 3 straight R16 losses + 3-peat/No.1 pressure,
#     balanced against 19-1 NY record -> Polymarket 0.22 & Books ~0.195 already price this! Blend ~0.215.
#   - Swiatek: Won Toronto, tight 3-set Cinci SF loss to Pegula, drops to #8 seed (faces Top-4 in QF, ~-0.5% path drag) -> ~0.145-0.15.
#   - Gauff: Dominant Cinci title (12 straight sets, beat Pegula 6-2 6-4 in 75 min), #4 seed, Polymarket 0.16 -> ~0.14-0.145.
#   - Osaka: Clear #4 on FD (+1000 vs +1400) & Kalshi (~8%), 2x USO champ, beat Sabalenka at Wim, rested -> ~0.075.
#   - Pegula vs Andreeva:
#     * Pegula: #3 seed (avoids Top-4 until SF!! Huge seeding advantage over Andreeva/Swiatek!), tour-leading 45 wins,
#       2024 USO finalist, beat Swiatek in Cinci SF, lost F to red-hot Gauff.
#     * Andreeva: 2026 RG champ, won IW 2025, but poor post-RG form (lost Cinci R4 4-6 6-0 6-2 to Kostyuk), never past R3 at USO.
#     Both tied at +1400 (FD) and +1000 (OddsTrader); Pegula's #3 seed + hard-court consistency gives slight edge (~0.06 vs ~0.058).
wta_blend = {}
for k in fd_wta_aug26:
    wta_blend[k] = 0.50 * exch_wta[k] + 0.50 * books_wta[k]

print("=== Q1 (608158) 2026 US OPEN WOMEN'S SINGLES — AUG 26 ===")
print(f"Overrounds: FD={fd_ov:.3f} (z={fd_z:.4f}), OT_adj={ot_ov:.3f} (z={ot_z:.4f}), GoBet={gb_ov:.3f} (z={gb_z:.4f})")
print(f"{'Player':20s} | {'FD_26':6s} | {'OT_25':6s} | {'GB_25':6s} | {'Books':6s} | {'Exch':6s} | {'BLEND':6s}")
for k in sorted(wta_blend, key=lambda x: -wta_blend[x]):
    print(f"{k:20s} | {fd_w[k]:6.4f} | {ot_w[k]:6.4f} | {gb_w[k]:6.4f} | {books_wta[k]:6.4f} | {exch_wta[k]:6.4f} | {wta_blend[k]:6.4f}")
top5_w = sorted([(k, v) for k, v in wta_blend.items() if k != "Field_Rest"], key=lambda x: -x[1])[:6]
print("WTA Top-6:", [(k, round(v, 4)) for k, v in top5_w])
print("WTA Top-5 sum:", round(sum(v for _, v in top5_w[:5]), 4))


# ==============================================================================
# PART 2: Q3 (qid=891014) — 2026 US OPEN MEN'S SINGLES (AUG 26)
# ==============================================================================
# 1. Tennisnerd full board (Aug 24, REMOVING Joao Fonseca who withdrew Aug 24!):
tn_atp = {
    "Carlos Alcaraz":        2.60,  # +160
    "Alexander Zverev":      4.00,  # +300
    "Novak Djokovic":        8.00,  # +700
    "Ben Shelton":           8.50,  # +750
    "Rafael Jodar":         13.00,  # +1200
    "Taylor Fritz":         13.00,  # +1200
    "Arthur Fils":          17.00,  # +1600
    "Daniil Medvedev":      21.00,  # +2000
    "Felix Auger-Aliassime":26.00,  # +2500
    "Flavio Cobolli":       36.00,  # +3500
    "Jakub Mensik":         36.00,  # +3500
    "Frances Tiafoe":       36.00,  # +3500
    "Tommy Paul":           36.00,  # +3500
    "Lorenzo Musetti":      36.00,  # +3500
    "Field_Rest":            8.50,  # ~11.8% raw for Nakashima, Tien, de Minaur, Rublev, Lehecka, etc.
}

# 2. SportsLine / Fresh US Sportsbook (Aug 26 10:50 AM ET — POST-ALCARAZ MIXED DOUBLES!):
#    Alcaraz +195 (2.95), Zverev +340 (4.40), Djokovic +700 (8.00); other lines anchored to Tennisnerd/Kalshi moves
sl_atp_aug26 = dict(tn_atp)
sl_atp_aug26["Carlos Alcaraz"] = 2.95   # +195 (drifted from +140 Aug 21 -> +160 Aug 24 -> +195 Aug 26!)
sl_atp_aug26["Alexander Zverev"] = 4.40 # +340
sl_atp_aug26["Novak Djokovic"] = 8.00   # +700
sl_atp_aug26["Arthur Fils"] = 15.00     # slightly tightened post-Cinci/Kalshi 6-7%
sl_atp_aug26["Taylor Fritz"] = 14.00    # drifted slightly toward Kalshi 4%

tn_a, tn_ov, tn_z, tn_k = devig_mid(tn_atp)
sl_a, sl_ov, sl_z, sl_k = devig_mid(sl_atp_aug26)

# 3. Prediction Markets (Polymarket $10M+ vol Aug 25 + Kalshi $7.1M vol Aug 24):
#    Polymarket Aug 25 (TheLines): Alcaraz = 0.30 (down from 0.34 Aug 24!), Zverev = 0.20 (steady!)
#    Kalshi Aug 24 (Prediction Authority): Alcaraz 0.34, Zverev 0.19-0.21 (0.20), Djokovic 0.09-0.10 (0.095),
#      Shelton 0.07, Fils 0.06 (Poly 0.07), Jodar 0.05, Fritz 0.04, Medvedev 0.02, Mensik 0.02, Musetti 0.01, Rest 0.105.
#    Adjusting Kalshi/Poly joint board for the confirmed Aug 25 Alcaraz drift 0.34 -> 0.30 (+0.04 redistributed
#    proportionally to non-Alcaraz field, keeping Zverev ~0.205 since Poly Aug 25 kept Zverev at 0.20):
exch_atp_aug25 = {
    "Carlos Alcaraz":        0.300, # Polymarket Aug 25 exact!
    "Alexander Zverev":      0.202, # Polymarket Aug 25 0.20, Kalshi 0.19-0.21
    "Novak Djokovic":        0.102, # 0.095-0.10 + small Alcaraz drift share
    "Ben Shelton":           0.074, # 0.07 + small share
    "Arthur Fils":           0.068, # Kalshi 0.06 / Poly 0.07 + small share
    "Rafael Jodar":          0.053, # Kalshi 0.05 + small share
    "Taylor Fritz":          0.043, # Kalshi 0.04 + small share
    "Daniil Medvedev":       0.022,
    "Jakub Mensik":          0.021,
    "Lorenzo Musetti":       0.011,
    "Felix Auger-Aliassime": 0.018,
    "Flavio Cobolli":        0.015,
    "Frances Tiafoe":        0.015,
    "Tommy Paul":            0.015,
    "Field_Rest":            0.041,
}
s_ex = sum(exch_atp_aug25.values())
exch_atp_aug25 = {k: v / s_ex for k, v in exch_atp_aug25.items()}


# ==============================================================================
# PART 3: EXACT-SEED 128-DRAW BO5 MONTE CARLO FOR BOTH Q3 (891014) & Q2 (408930)
# ==============================================================================
def p_bo5(ea, eb):
    p3 = 1.0 / (1.0 + 10.0 ** (-(ea - eb) / 400.0))
    ps = p3
    for _ in range(8):
        f = ps*ps*(3 - 2*ps) - p3
        df = 6*ps*(1 - ps) + 1e-12
        ps = max(1e-6, min(1 - 1e-6, ps - f / df))
    return ps**3 * (10 - 15*ps + 6*ps*ps)

def place_128_draw_official(idxs, rng):
    seeds = idxs[:32]
    unseeded = idxs[32:]
    rng.shuffle(unseeded)
    bracket = [None] * 128
    bracket[0] = seeds[0]
    bracket[127] = seeds[1]
    s34 = [seeds[2], seeds[3]]
    rng.shuffle(s34)
    bracket[32], bracket[95] = s34[0], s34[1]
    s58 = list(seeds[4:8])
    rng.shuffle(s58)
    for pos, p in zip([31, 63, 64, 96], s58):
        bracket[pos] = p
    s912 = list(seeds[8:12])
    rng.shuffle(s912)
    for pos, p in zip([16, 48, 79, 111], s912):
        bracket[pos] = p
    s1316 = list(seeds[12:16])
    rng.shuffle(s1316)
    for pos, p in zip([15, 47, 80, 112], s1316):
        bracket[pos] = p
    pos_17_24 = [8, 23, 40, 55, 72, 87, 104, 119]
    pos_25_32 = [7, 24, 39, 56, 71, 88, 103, 120]
    s1724 = list(seeds[16:24])
    s2532 = list(seeds[24:32])
    rng.shuffle(s1724)
    rng.shuffle(s2532)
    for pos, p in zip(pos_17_24, s1724):
        bracket[pos] = p
    for pos, p in zip(pos_25_32, s2532):
        bracket[pos] = p
    ui = 0
    for i in range(128):
        if bracket[i] is None:
            bracket[i] = unseeded[ui]
            ui += 1
    return bracket

# EXACT CONFIRMED 2026 US OPEN MEN'S SINGLES SEEDS (Aug 24; Sinner & Fonseca OUT!):
# Calibrated to Aug 25-26 Markets (Polymarket, Kalshi, SportsLine, Tennisnerd):
seeded_atp_aug26 = [
    ("Alexander Zverev",      2145),  # 1  (Poly 20%, Kalshi 19-21%, SL +340)
    ("Carlos Alcaraz",        2205),  # 2  (Mixture below! Played mixed Tue Aug 25 w/o pain, some rust -> ~30%)
    ("Felix Auger-Aliassime", 2005),  # 3
    ("Novak Djokovic",        2108),  # 4  (Kalshi/Poly 10%, SL +700)
    ("Flavio Cobolli",        1995),  # 5
    ("Alex de Minaur",        2010),  # 6
    ("Daniil Medvedev",       2010),  # 7
    ("Ben Shelton",           2084),  # 8  [USA] Kalshi/Poly 7%, Tennisnerd 8.50, #8 top-8 seed!
    ("Taylor Fritz",          2062),  # 9  [USA] Drifted to 13.00 (+1200) & Kalshi 4% (down from 2074!)
    ("Arthur Fils",           2074),  # 10 Upgraded! Cinci champ, Kalshi 6%/Poly 7%, Tennisnerd 17.00
    ("Frances Tiafoe",        2008),  # 11 [USA] Cinci F, Tennisnerd 36.00 (=Paul!), skipped mixed -> 7d rest (injury mix below)
    ("Rafael Jodar",          2052),  # 12 Kalshi 5%, Tennisnerd 13.00
    ("Lorenzo Musetti",       1975),  # 13
    ("Learner Tien",          1968),  # 14 [USA]
    ("Alexander Bublik",      1940),  # 15
    ("Brandon Nakashima",     1995),  # 16 [USA]
    ("Jakub Mensik",          2005),  # 17
    ("Jiri Lehecka",          1975),  # 18
    ("Casper Ruud",           1948),  # 19
    ("Tommy Paul",            1994),  # 20 [USA] Tennisnerd 36.00 (=Tiafoe!)
    ("Luciano Darderi",       1905),  # 21
    ("Valentin Vacherot",     1900),  # 22
    ("Andrey Rublev",         1970),  # 23
    ("Francisco Cerundolo",   1915),  # 24
    ("Alejandro Tabilo",      1900),  # 25
    ("Arthur Rinderknech",    1895),  # 26
    ("Ugo Humbert",           1935),  # 27
    ("Tomas Martin Etcheverry", 1895),# 28
    ("Alexander Blockx",      1890),  # 29
    ("Zizou Bergs",           1895),  # 30
    ("Cameron Norrie",        1900),  # 31
    ("Matteo Arnaldi",        1905),  # 32
]

unseeded_us = [
    ("Alex Michelsen",        1925),
    ("Sebastian Korda",       1920),
    ("Reilly Opelka",         1895),
    ("Marcos Giron",          1875),
    ("Jenson Brooksby",       1870),
    ("Aleksandar Kovacevic",  1855),
    ("Nishesh Basavareddy",   1835),
    ("Zachary Svajda",        1815),
    ("Christopher Eubanks",   1815),
    ("Emilio Nava",           1805),
]
us_names = {
    "Ben Shelton", "Taylor Fritz", "Frances Tiafoe", "Learner Tien",
    "Brandon Nakashima", "Tommy Paul"
} | {u[0] for u in unseeded_us}

def run_atp_mc(elo_overrides=None, n_trials=45000, seed=901):
    rng = random.Random(seed)
    base_pool = list(seeded_atp_aug26) + list(unseeded_us)
    for k in range(128 - len(base_pool)):
        el = 1925.0 - (k * 210.0 / 85.0)
        base_pool.append((f"NonUS_{k}", el))
    if elo_overrides:
        base_pool = [(nm, elo_overrides.get(nm, el)) for nm, el in base_pool]

    # Alcaraz post-mixed-doubles state mixture:
    # Played 2 matches Tue Aug 25 cleanly (WD risk 0.05 -> 0.03), but 4m rust/BO5 endurance
    # risk slightly heavier consistent with Polymarket 0.30 & SportsLine +195:
    #   NearPeak (2285, 0.34), MildRust (2185, 0.44), SignificantRust (2055, 0.19), WD/Re-injury (1750, 0.03)
    alc_mix = [(2285, 0.34), (2185, 0.44), (2055, 0.19), (1750, 0.03)]
    # Tiafoe skipped mixed doubles (confirmed Tue Aug 25) -> full 7d recovery, still moderate leg/back risk:
    tia_mix = [(0, 0.72), (-35, 0.21), (-105, 0.07)]

    title_cnt = Counter()
    uncond_us_cnt = Counter()
    tie_cnt = 0.0

    for ae, wa in alc_mix:
        for td, wt in tia_mix:
            w = wa * wt
            tr = max(2000, int(round(n_trials * w)))
            pool = []
            for nm, el in base_pool:
                if nm == "Carlos Alcaraz":
                    pool.append((nm, ae))
                elif nm == "Frances Tiafoe":
                    pool.append((nm, el + td))
                else:
                    pool.append((nm, el))
            names = [p[0] for p in pool]
            elos = [p[1] for p in pool]
            us_idx_set = {i for i, nm in enumerate(names) if nm in us_names}
            idxs = list(range(128))
            pc = {}
            def gp(i, j):
                k = (elos[i], elos[j])
                v = pc.get(k)
                if v is None:
                    v = p_bo5(elos[i], elos[j])
                    pc[k] = v
                return v

            t_c = Counter()
            u_c = Counter()
            ties = 0
            for _ in range(tr):
                cur = place_128_draw_official(idxs, rng)
                best_round = 0
                best_players = []
                rnd = 1
                while len(cur) > 1:
                    nxt = []
                    for k in range(0, len(cur), 2):
                        a, b = cur[k], cur[k+1]
                        if rng.random() < gp(a, b):
                            win, los = a, b
                        else:
                            win, los = b, a
                        nxt.append(win)
                        if los in us_idx_set:
                            if rnd > best_round:
                                best_round = rnd
                                best_players = [los]
                            elif rnd == best_round:
                                best_players.append(los)
                    cur = nxt
                    rnd += 1
                champ = cur[0]
                t_c[names[champ]] += 1
                if champ in us_idx_set:
                    best_round = 8
                    best_players = [champ]
                if len(best_players) == 1:
                    u_c[names[best_players[0]]] += 1
                else:
                    ties += 1

            for nm, c in t_c.items():
                title_cnt[nm] += w * (c / tr)
            for nm, c in u_c.items():
                uncond_us_cnt[nm] += w * (c / tr)
            tie_cnt += w * (ties / tr)

    cond_us = {nm: v / (1.0 - tie_cnt) for nm, v in uncond_us_cnt.items()}
    return title_cnt, cond_us, uncond_us_cnt, tie_cnt

us_regimes = [
    ("Base (Aug 25-26 Markets + Official Seeds)", 0.50, {}),
    ("BO5-Pedigree (Fritz +18, Paul +14, Shelton -8, Fils -12)", 0.25, {
        "Taylor Fritz": 2080, "Tommy Paul": 2008, "Ben Shelton": 2076,
        "Arthur Fils": 2062, "Brandon Nakashima": 1982
    }),
    ("Market-Kalshi-Sharp (Shelton +12, Fritz -14, Fils +12, Tiafoe +12)", 0.25, {
        "Ben Shelton": 2096, "Taylor Fritz": 2048, "Arthur Fils": 2086,
        "Frances Tiafoe": 2020, "Brandon Nakashima": 2005
    }),
]

blend_title = Counter()
blend_cond = Counter()
blend_uncond = Counter()
blend_tie = 0.0
for idx, (lbl, w, ov) in enumerate(us_regimes):
    tc, cu, uu, tr = run_atp_mc(elo_overrides=ov, n_trials=45000, seed=910 + idx)
    blend_tie += w * tr
    for k, v in tc.items(): blend_title[k] += w * v
    for k, v in cu.items(): blend_cond[k] += w * v
    for k, v in uu.items(): blend_uncond[k] += w * v

# Final Q3 (891014) Men's Singles Blend:
# 45% Sharp Prediction Markets (Polymarket $10M+ Aug 25 + Kalshi $7.1M Aug 24)
# + 30% Sportsbooks (60% SportsLine Aug 26 + 40% Tennisnerd Aug 24)
# + 25% Exact-Seed 128-Draw BO5 Monte Carlo
atp_final = {}
for k in tn_atp:
    if k == "Field_Rest":
        continue
    books_k = 0.60 * sl_a[k] + 0.40 * tn_a[k]
    atp_final[k] = 0.45 * exch_atp_aug25[k] + 0.30 * books_k + 0.25 * blend_title.get(k, 0.0)

print("\n=== Q3 (891014) 2026 US OPEN MEN'S SINGLES — AUG 26 ===")
print(f"Overrounds: TN={tn_ov:.3f} (z={tn_z:.4f}), SL_26={sl_ov:.3f} (z={sl_z:.4f})")
print(f"{'Player':22s} | {'Exch25':6s} | {'SL_26':6s} | {'TN_24':6s} | {'BO5_MC':6s} | {'FINAL':6s}")
for k in sorted(atp_final, key=lambda x: -atp_final[x])[:10]:
    print(f"{k:22s} | {exch_atp_aug25[k]:6.4f} | {sl_a[k]:6.4f} | {tn_a[k]:6.4f} | {blend_title.get(k,0):6.4f} | {atp_final[k]:6.4f}")
top5_m = sorted(atp_final.items(), key=lambda x: -x[1])[:6]
print("ATP Top-6:", [(k, round(v, 4)) for k, v in top5_m])
print("ATP Top-5 sum:", round(sum(v for _, v in top5_m[:5]), 4))

print(f"\n=== Q2 (408930) FURTHEST U.S. MAN — AUG 26 (Tie Rate = {blend_tie:.4f}) ===")
print(f"{'Player':22s} | {'Cond(Unique)':12s} | {'Uncond':8s} | {'Title%':7s}")
for k, v in blend_cond.most_common(10):
    print(f"{k:22s} | {v:12.4f} | {blend_uncond[k]:8.4f} | {blend_title[k]:7.4f}")
