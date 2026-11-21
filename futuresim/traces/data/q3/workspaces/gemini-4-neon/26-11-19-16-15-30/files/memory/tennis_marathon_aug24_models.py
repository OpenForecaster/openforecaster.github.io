import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — MONDAY AUG 24, 2026
# Batch: tennis_and_marathon (772246, 408930, 2260, 409386)
# ==============================================================================

# ------------------------------------------------------------------------------
# PART 0: FIRST-PRINCIPLES FAST4 + 10-PT MTB MATCH PROBABILITY CALIBRATION
# ------------------------------------------------------------------------------
def sim_fast4_vs_bo3(p_game_a_serve, p_game_b_serve, n_trials=40000, seed=101):
    """Compare normal BO3 (6-game sets, ad) vs Fast4 (4-game sets, no-ad, 10-pt MTB)."""
    # Approximate point-win prob on serve from game-win prob (no-ad vs ad)
    # In doubles, hold rates are high (~75%-85% for strong servers, ~68%-76% in mixed)
    # Let's simulate directly from point-win probabilities:
    # p_pt_a = prob A wins point on A's serve; p_pt_b = prob B wins point on B's serve
    rng = random.Random(seed)

    def play_game(p_srv, no_ad=True):
        a, b = 0, 0
        while True:
            if rng.random() < p_srv:
                a += 1
            else:
                b += 1
            if no_ad:
                if a == 4: return True
                if b == 4: return False
            else:
                if a >= 4 and a - b >= 2: return True
                if b >= 4 and b - a >= 2: return False

    def play_tb(p_a, p_b, target=7, start_a=True):
        a, b = 0, 0
        pt = 0
        while True:
            # 1st point server0, then pairs
            srv_a = start_a if ((pt + 1) // 2) % 2 == 0 else (not start_a)
            p_win_a = p_a if srv_a else (1.0 - p_b)
            if rng.random() < p_win_a:
                a += 1
            else:
                b += 1
            if a >= target and a - b >= 2: return True
            if b >= target and b - a >= 2: return False
            pt += 1

    def play_set(p_a, p_b, target_games=4, no_ad=True, start_a=True):
        ga, gb = 0, 0
        srv_a = start_a
        while True:
            if srv_a:
                if play_game(p_a, no_ad=no_ad): ga += 1
                else: gb += 1
            else:
                if play_game(p_b, no_ad=no_ad): gb += 1
                else: ga += 1
            srv_a = not srv_a
            if target_games == 4:
                if ga == 4 and gb <= 2: return True
                if gb == 4 and ga <= 2: return False
                if ga == 4 and gb == 3:
                    # US Open Fast4: TB at 4-4? Wait: rules say "first to four games with a tiebreak at 4-4"
                    # Wait: if ga=4, gb=3, does 4-3 win? Wait: Tennis365 says "first to four games to win a set with a tiebreak at 4-4"
                    # Actually in 2025/2026 US Open mixed doubles, you must win by 2 (4-2, 5-3) or TB at 4-4!
                    pass
                if ga == 5 and gb == 3: return True
                if gb == 5 and ga == 3: return False
                if ga == 4 and gb == 4:
                    return play_tb(p_a, p_b, target=7, start_a=srv_a)
            else:
                if ga >= 6 and ga - gb >= 2: return True
                if gb >= 6 and gb - ga >= 2: return False
                if ga == 6 and gb == 6:
                    return play_tb(p_a, p_b, target=7, start_a=srv_a)

    w_fast4, w_bo3 = 0, 0
    for _ in range(n_trials):
        # Fast4 + 10-pt MTB
        sa, sb = 0, 0
        for s_idx in range(2):
            if play_set(p_game_a_serve, p_game_b_serve, target_games=4, no_ad=True, start_a=(s_idx % 2 == 0)):
                sa += 1
            else:
                sb += 1
        if sa == 2: w_fast4 += 1
        elif sa == 1 and sb == 1:
            if play_tb(p_game_a_serve, p_game_b_serve, target=10, start_a=True):
                w_fast4 += 1

        # Normal BO3 (6 games, ad, full 3rd set)
        sa, sb = 0, 0
        for s_idx in range(3):
            if play_set(p_game_a_serve, p_game_b_serve, target_games=6, no_ad=False, start_a=(s_idx % 2 == 0)):
                sa += 1
            else:
                sb += 1
            if sa == 2:
                w_bo3 += 1
                break
            if sb == 2:
                break
    return w_fast4 / n_trials, w_bo3 / n_trials

print("=== FAST4 + 10-PT MTB vs NORMAL BO3 COMPRESSION CHECK ===")
for pa, pb, desc in [
    (0.65, 0.62, "Modest edge (+3% serve pt diff)"),
    (0.67, 0.62, "Clear edge (+5% serve pt diff)"),
    (0.68, 0.61, "Strong specialist edge (+7% serve pt diff)"),
    (0.70, 0.61, "Dominant specialist edge (+9% serve pt diff)"),
]:
    pf4, pbo3 = sim_fast4_vs_bo3(pa, pb, n_trials=25000)
    # Implied Elo scale for Fast4 relative to 400 in BO3:
    logit_f4 = math.log10(pf4 / (1 - pf4))
    logit_b3 = math.log10(pbo3 / (1 - pbo3))
    scale_f4 = 400.0 * (logit_b3 / logit_f4)
    print(f"  {desc:44s}: BO3={pbo3:.3f} -> Fast4={pf4:.3f} (implied Fast4 Elo scale={scale_f4:.0f})")


# ------------------------------------------------------------------------------
# PART 1: Q1 (qid=772246) — 2026 US OPEN MIXED DOUBLES (POST-QUALIFYING AUG 24!)
# ------------------------------------------------------------------------------
# CONFIRMED FULL 16-TEAM BRACKET (Tennis365, IANS, TennisUpToDate, BBC Sport Aug 24):
#   TOP HALF:
#     Q1:
#       M1: [1] Sabalenka/Djokovic vs [Q] Siniakova/Patten (BBC Sport Aug 24 evening!)
#           [OR vs Fernandez/Tiafoe in ~15% BBC-error branch]
#       M2: Svitolina/Monfils vs Eala/Auger-Aliassime
#     Q2 (CONFIRMED TOP-HALF SF POD!):
#       M3: [4] Bencic/Cobolli vs Townsend/Zverev
#       M4: Williams/Alcaraz vs [Q] Routliffe/Glasspool (CONFIRMED BBC Sport Aug 24!)
#   BOTTOM HALF (FINAL OPPONENT ONLY!):
#     Q3:
#       M5: Muchova/Mensik vs LuckyLoser (Stearns/Harrison or Mladenovic/Arevalo)
#           [OR vs Siniakova/Patten in BBC-error branch]
#       M6: Navarro/Paul vs [3] Anisimova/Tien
#     Q4:
#       M7: Andreeva/Rublev vs Errani/Vavassori (CONFIRMED BOTTOM HALF!)
#       M8: Shnaider/Ruud vs [2] Pegula/Fritz

mixed_ratings = {
    "Sabalenka and Djokovic": 1955,    # Rested elite singles stars, Sabalenka former Slam doubles champ, Djo elite return
    "Siniakova and Patten": 2090,      # WTA #1 & ATP #1 doubles specialists! Olympic mixed gold + 2x Wim champ + 2 live Mon Q wins!
    "Fernandez and Tiafoe": 1895,      # Discounted for Tiafoe Sun Cinci Final leg/back treatment (only in BBC-error branch)
    "Alt_Tiafoe_Replace": 1875,
    "Eala and Auger-Aliassime": 1945,  # Both healthy, rested, strong lefty+big-serve combo
    "Svitolina and Monfils": 1845,     # Discounted for Svitolina Aug 19 ankle WD + Monfils age 39
    "Alt_Svitolina_Replace": 1850,
    "Townsend and Zverev": 2035,       # Elite doubles #1 Townsend + #1 USO seed Zverev (CONFIRMED Q2!)
    "Bencic and Cobolli": 1895,
    "Williams and Alcaraz": 1900,      # Alcaraz 4m layoff + 44yo Serena
    "Routliffe and Glasspool": 2045,   # Slam doubles champs + 2 live Mon Q wins beating Stefani/Skupski & Arevalo/Mladenovic!
    "Muchova and Mensik": 1925,
    "LuckyLoser_Q3": 1975,             # Stearns/Harrison (beat Krunic/Pavic) or Arevalo/Mladenovic (beat Dabrowski/Heliovaara)
    "Navarro and Paul": 1920,
    "Anisimova and Tien": 1910,
    "Andreeva and Rublev": 1930,
    "Errani and Vavassori": 2095,      # 2x defending champs, proven Fast4 kings (CONFIRMED BOTTOM HALF Q4!)
    "Shnaider and Ruud": 1925,
    "Pegula and Fritz": 1945,          # Pegula played Cinci Final Sun night
}

def sim_mixed_aug24(ratings, scale=540.0, n_trials=200000, seed=401,
                    p_bbc_true=0.85, p_djo_play=0.95, djo_bonus=0,
                    p_tiafoe_play_if_err=0.72, p_svit_play=0.84):
    rng = random.Random(seed)
    r = dict(ratings)
    r["Sabalenka and Djokovic"] += djo_bonus

    p_cache = {}
    def mp(a, b, is_final=False):
        sc = (scale * 0.87) if is_final else scale  # Final uses 6-game sets (no-ad + 10-pt MTB)
        k = (a, b, is_final)
        v = p_cache.get(k)
        if v is None:
            v = 1.0 / (1.0 + 10.0 ** (-(r[a] - r[b]) / sc))
            p_cache[k] = v
        return v

    def play_match(a, b, is_final=False):
        if a is None: return b, None
        if b is None: return a, None
        return (a, b) if rng.random() < mp(a, b, is_final) else (b, a)

    elim_cnt = Counter()
    win_cnt = 0
    wd_cnt = 0

    for _ in range(n_trials):
        if rng.random() >= p_djo_play:
            wd_cnt += 1
            continue

        bbc_ok = (rng.random() < p_bbc_true)
        if bbc_ok:
            r1_opp = "Siniakova and Patten"
            q3_opp = "LuckyLoser_Q3"
        else:
            if rng.random() < p_tiafoe_play_if_err:
                r1_opp = "Fernandez and Tiafoe"
            else:
                r1_opp = None if rng.random() < 0.25 else "Alt_Tiafoe_Replace"
            q3_opp = "Siniakova and Patten"

        if rng.random() < p_svit_play:
            svit_pair = "Svitolina and Monfils"
        else:
            svit_pair = None if rng.random() < 0.20 else "Alt_Svitolina_Replace"

        # Q1 (Top Half)
        w1, l1 = play_match("Sabalenka and Djokovic", r1_opp)
        if l1 == "Sabalenka and Djokovic":
            elim_cnt[w1] += 1
            continue
        w2, _ = play_match(svit_pair, "Eala and Auger-Aliassime")
        w_q1, l_q1 = play_match(w1, w2)
        if l_q1 == "Sabalenka and Djokovic":
            elim_cnt[w_q1] += 1
            continue

        # Q2 (CONFIRMED Top Half SF Pod!)
        w3, _ = play_match("Bencic and Cobolli", "Townsend and Zverev")
        w4, _ = play_match("Williams and Alcaraz", "Routliffe and Glasspool")
        w_q2, _ = play_match(w3, w4)

        # SF1 (Top Half)
        w_top, l_top = play_match(w_q1, w_q2)
        if l_top == "Sabalenka and Djokovic":
            elim_cnt[w_top] += 1
            continue

        # Bottom Half (Q3 + Q4)
        w5, _ = play_match("Muchova and Mensik", q3_opp)
        w6, _ = play_match("Navarro and Paul", "Anisimova and Tien")
        w_q3, _ = play_match(w5, w6)

        w7, _ = play_match("Andreeva and Rublev", "Errani and Vavassori")
        w8, _ = play_match("Shnaider and Ruud", "Pegula and Fritz")
        w_q4, _ = play_match(w7, w8)

        w_bot, _ = play_match(w_q3, w_q4)

        # Final (6-game sets!)
        champ, runner = play_match(w_top, w_bot, is_final=True)
        if runner == "Sabalenka and Djokovic":
            elim_cnt[champ] += 1
        else:
            win_cnt += 1

    return {k: c / n_trials for k, c in elim_cnt.items()}, win_cnt / n_trials, wd_cnt / n_trials

regimes_mixed = [
    # (label, weight, p_bbc, p_djo_play, scale, djo_bonus, rating_overrides)
    ("Base (BBC=85%, Siniakova/Patten +135 Elo, sc=540)", 0.45, 0.85, 0.95, 540.0, 0, {}),
    ("Doubles-Dom (BBC=90%, Specialists +35 Elo, sc=500)", 0.25, 0.90, 0.95, 500.0, -15, {"Siniakova and Patten": 2115, "Routliffe and Glasspool": 2070, "Errani and Vavassori": 2120}),
    ("Singles-Power (BBC=85%, Djo/Sab +45 Elo, sc=560)", 0.15, 0.85, 0.96, 560.0, +45, {}),
    ("BBC-Hedge (BBC=72% in case wire/draw error)", 0.15, 0.72, 0.94, 540.0, 0, {"Fernandez and Tiafoe": 1915}),
]

print("\n=== Q1 (772246) US OPEN MIXED DOUBLES — POST-QUALIFYING AUG 24 ===")
# Also check exact R1 win prob of Siniakova/Patten vs Sabalenka/Djokovic across regimes
for lbl, w, pbbc, pdp, sc, db, ov in regimes_mixed:
    rr = dict(mixed_ratings)
    rr.update(ov)
    p_sp_r1 = 1.0 / (1.0 + 10.0 ** (-((rr["Siniakova and Patten"] - (rr["Sabalenka and Djokovic"] + db)) / sc)))
    print(f"  [{lbl}] P(Sin/Pat beat Djo/Sab in R1) = {p_sp_r1:.3f}")

blend_mixed = Counter()
p_win_tot, p_wd_tot = 0.0, 0.0
for idx, (lbl, w, pbbc, pdp, sc, db, ov) in enumerate(regimes_mixed):
    rr = dict(mixed_ratings)
    rr.update(ov)
    elims, pwin, pwd = sim_mixed_aug24(rr, scale=sc, n_trials=150000, seed=500 + idx,
                                       p_bbc_true=pbbc, p_djo_play=pdp, djo_bonus=db)
    p_win_tot += w * pwin
    p_wd_tot += w * pwd
    top5_s = ", ".join(f"{k}:{v:.3f}" for k, v in sorted(elims.items(), key=lambda x: -x[1])[:6])
    print(f"  [{lbl[:38]:38s} w={w:.2f}] win={pwin:.3f} wd={pwd:.3f} | {top5_s}")
    for k, v in elims.items():
        blend_mixed[k] += w * v

print(f"\nFINAL MIXED DOUBLES BLEND (P(Djo/Sab Win)={p_win_tot:.4f}, P(WD)={p_wd_tot:.4f}, P(No pair qualifies)={p_win_tot+p_wd_tot:.4f}):")
for k, v in blend_mixed.most_common(12):
    print(f"  {k:28s}: {v:.4f}")


# ------------------------------------------------------------------------------
# PART 2: Q2 (qid=408930) — FURTHEST U.S. MAN AT 2026 US OPEN (CONFIRMED SEEDS!)
# ------------------------------------------------------------------------------
def p_bo5(ea, eb):
    p3 = 1.0 / (1.0 + 10.0 ** (-(ea - eb) / 400.0))
    ps = p3
    for _ in range(8):
        f = ps*ps*(3 - 2*ps) - p3
        df = 6*ps*(1 - ps) + 1e-12
        ps = max(1e-6, min(1 - 1e-6, ps - f / df))
    return ps**3 * (10 - 15*ps + 6*ps*ps)

def place_128_draw_official(idxs, rng):
    """Official Grand Slam 128-draw seeding placement (1-4 vs 13-16 in R4, 5-8 vs 9-12 in R4, etc.)."""
    seeds = idxs[:32]
    unseeded = idxs[32:]
    rng.shuffle(unseeded)
    bracket = [None] * 128
    # 1 at top (0), 2 at bottom (127)
    bracket[0] = seeds[0]
    bracket[127] = seeds[1]
    # 3-4 at 32 (Q2 top) / 95 (Q3 bottom) — wait: in 128-draw:
    # Quarters: Q1=0..31, Q2=32..63, Q3=64..95, Q4=96..127
    # Top half: Q1 (seed 1 at 0) + Q2 (seed 3/4 at 32)
    # Bottom half: Q3 (seed 3/4 at 95) + Q4 (seed 2 at 127)
    #Wait: let's verify standard GS 128-draw slots!
    # Q1 (0..31):   0 = #1,     15 = #13-16, 16 = #9-12,  31 = #5-8
    # Q2 (32..63):  32 = #3/4,  47 = #13-16, 48 = #9-12,  63 = #5-8
    # Q3 (64..95):  64 = #5-8,  79 = #9-12,  80 = #13-16, 95 = #3/4
    # Q4 (96..127): 96 = #5-8,  111 = #9-12, 112 = #13-16, 127 = #2
    # CHECK R4 pairings (16-player pods: 0..15, 16..31, 32..47, 48..63, 64..79, 80..95, 96..111, 112..127):
    #   0..15: #1 vs #13-16!   16..31: #9-12 vs #5-8!
    #   32..47: #3/4 vs #13-16! 48..63: #9-12 vs #5-8!
    #   64..79: #5-8 vs #9-12! 80..95: #13-16 vs #3/4!
    #   96..111: #5-8 vs #9-12! 112..127: #13-16 vs #2!
    # CHECK R3 pairings (8-player pods):
    #   0..7: #1 vs #25-32 (pos 7)
    #   8..15: #17-24 (pos 8) vs #13-16 (pos 15)
    #   16..23: #9-12 (pos 16) vs #17-24 (pos 23)
    #   24..31: #25-32 (pos 24) vs #5-8 (pos 31)
    # YES!! THAT MATCHES OFFICIAL GRAND SLAM SEEDING RULES 100%!!
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
# Ordered strictly by seed #1 to #32!
seeded_atp_2026 = [
    ("Alexander Zverev",      2145),  # 1
    ("Carlos Alcaraz",        2235),  # 2 (mixture applied below!)
    ("Felix Auger-Aliassime", 2005),  # 3
    ("Novak Djokovic",        2110),  # 4
    ("Flavio Cobolli",        1995),  # 5 (RG F, Cinci SF)
    ("Alex de Minaur",        2010),  # 6
    ("Daniil Medvedev",       2005),  # 7
    ("Ben Shelton",           2082),  # 8 [USA] Montreal champ (10-0), DK +750, 2wks rest!
    ("Taylor Fritz",          2074),  # 9 [USA] 2024 USO F, DC champ, DK +1000, lost Cinci QF to Nakashima
    ("Arthur Fils",           2060),  # 10 Cincinnati Masters champ (d. Tiafoe, Cobolli, de Minaur)
    ("Frances Tiafoe",        2008),  # 11 [USA] Cinci Finalist (d. Tien, FAA, Musetti, Nakashima), 2x USO SF (injury mix below!)
    ("Rafael Jodar",          2035),  # 12 DK +1100
    ("Lorenzo Musetti",       1975),  # 13
    ("Learner Tien",          1968),  # 14 [USA] Montreal SF, lost Cinci R3 to Tiafoe 6-4 4-6 6-4
    ("Alexander Bublik",      1940),  # 15
    ("Brandon Nakashima",     1995),  # 16 [USA] DC SF + Montreal F + Cinci SF (d. Medvedev, Fritz!)
    ("Jakub Mensik",          2005),  # 17
    ("Jiri Lehecka",          1975),  # 18
    ("Casper Ruud",           1948),  # 19
    ("Tommy Paul",            1992),  # 20 [USA] Beat Zverev in Cinci R4, Cinci QF, DK +4000, strong BO5 floor
    ("Luciano Darderi",       1905),  # 21
    ("Valentin Vacherot",     1900),  # 22
    ("Andrey Rublev",         1970),  # 23
    ("Francisco Cerundolo",   1915),  # 24
    ("Alejandro Tabilo",      1900),  # 25 (up from 26 after Fonseca WD)
    ("Arthur Rinderknech",    1895),  # 26
    ("Ugo Humbert",           1935),  # 27
    ("Tomas Martin Etcheverry", 1895),# 28
    ("Alexander Blockx",      1890),  # 29
    ("Zizou Bergs",           1895),  # 30
    ("Cameron Norrie",        1900),  # 31
    ("Matteo Arnaldi",        1905),  # 32 (enters after Fonseca WD)
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

def run_us_open_mc(elo_overrides=None, n_trials=40000, seed=701):
    rng = random.Random(seed)
    # Build base 128-player list
    base_pool = list(seeded_atp_2026) + list(unseeded_us)
    # Remaining 86 unseeded non-US players (Berrettini, Hurkacz, Khachanov, Machac, Shapovalov, etc.)
    for k in range(128 - len(base_pool)):
        # Top unseeded players around 1925 tapering down to 1715 qualifiers
        el = 1925.0 - (k * 210.0 / 85.0)
        base_pool.append((f"NonUS_{k}", el))

    if elo_overrides:
        base_pool = [(nm, elo_overrides.get(nm, el)) for nm, el in base_pool]

    # Joint mixture over Alcaraz state x Tiafoe recovery state
    # Alcaraz: NearPeak (2290, 0.42), MildRust (2190, 0.40), Rusty (2060, 0.13), WD (1750, 0.05)
    # Tiafoe (7 full days rest + likely skipped mixed doubles):
    #   Recovered (0, 0.72), MildDrag (-35, 0.21), Compromised/Early (-105, 0.07)
    alc_mix = [(2290, 0.42), (2190, 0.40), (2060, 0.13), (1750, 0.05)]
    tia_mix = [(0, 0.72), (-35, 0.21), (-105, 0.07)]

    title_cnt = Counter()
    unique_us_cnt = Counter()
    uncond_us_cnt = Counter()
    tie_cnt = 0.0
    tot_w = 0.0

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
                # Round reached: 1=R1 loss, 2=R2, 3=R3, 4=R4, 5=QF, 6=SF, 7=F, 8=Champion
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
            tot_w += w

    cond_us = {nm: v / (1.0 - tie_cnt) for nm, v in uncond_us_cnt.items()}
    return title_cnt, cond_us, uncond_us_cnt, tie_cnt

us_regimes = [
    ("Base (Market-Calibrated + Aug 24 Official Seeds)", 0.50, {}),
    ("BO5-Pedigree (Fritz +16, Paul +14, Shelton -10, Nak -15)", 0.25, {
        "Taylor Fritz": 2090, "Tommy Paul": 2006, "Ben Shelton": 2072,
        "Brandon Nakashima": 1980, "Learner Tien": 1958
    }),
    ("Hot-August-Form (Shelton +15, Tiafoe +18, Nak +15, Fritz -12)", 0.25, {
        "Ben Shelton": 2097, "Frances Tiafoe": 2026, "Brandon Nakashima": 2010,
        "Taylor Fritz": 2062, "Learner Tien": 1978
    }),
]

print("\n=== Q2 (408930) FURTHEST U.S. MAN AT 2026 US OPEN (OFFICIAL AUG 24 SEEDS!) ===")
blend_title = Counter()
blend_cond = Counter()
blend_uncond = Counter()
blend_tie = 0.0

for idx, (lbl, w, ov) in enumerate(us_regimes):
    tc, cu, uu, tr = run_us_open_mc(elo_overrides=ov, n_trials=45000, seed=800 + idx)
    blend_tie += w * tr
    for k, v in tc.items(): blend_title[k] += w * v
    for k, v in cu.items(): blend_cond[k] += w * v
    for k, v in uu.items(): blend_uncond[k] += w * v
    top6 = ", ".join(f"{k}:{v:.3f}" for k, v in sorted(cu.items(), key=lambda x: -x[1])[:6])
    print(f"  [{lbl[:48]:48s} w={w:.2f}] tie={tr:.3f} | {top6}")

print("\nTITLE SANITY CHECK (should match DK/Euro market!):")
for k, v in blend_title.most_common(12):
    print(f"  {k:24s}: {v:.4f}")

print(f"\nFINAL FURTHEST U.S. MAN BLEND (Tie Rate = {blend_tie:.4f}):")
print(f"{'Player':22s} | {'Cond(Unique)':12s} | {'Uncond':8s} | {'Title%':7s}")
for k, v in blend_cond.most_common(10):
    print(f"{k:22s} | {v:12.4f} | {blend_uncond[k]:8.4f} | {blend_title[k]:7.4f}")
