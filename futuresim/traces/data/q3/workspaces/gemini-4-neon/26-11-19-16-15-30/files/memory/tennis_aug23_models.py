import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — SUNDAY AUG 23, 2026
# Batch: tennis (772246, 608158, 891014)
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
    lo, hi = 1.0, 3.0
    for _ in range(100):
        k_exp = 0.5 * (lo + hi)
        tot = sum(q ** k_exp for q in qs.values())
        if tot > 1.0:
            lo = k_exp
        else:
            hi = k_exp
    k_exp = 0.5 * (lo + hi)
    return {name: q ** k_exp for name, q in qs.items()}, k_exp

def prop_devig(dec_odds_dict):
    qs = {k: 1.0 / d for k, d in dec_odds_dict.items()}
    s = sum(qs.values())
    return {k: q / s for k, q in qs.items()}


# ==============================================================================
# PART 1: Q1 (qid=772246) — 2026 US OPEN MIXED DOUBLES (POST-DRAW AUG 23!)
# ==============================================================================
# Official draw released Sun Aug 23 (en.tennistemple.com, tennistonic.com, AP):
#   Q1 (Top Half):
#     M1: [1] Sabalenka/Djokovic vs Fernandez/Tiafoe
#     M2: Svitolina/Monfils vs Eala/Auger-Aliassime
#   Q4 (Bottom Half):
#     M8: [2] Pegula/Fritz vs Shnaider/Ruud (Swiatek WD -> Ruud paired w/ Shnaider!)
#   Other R1 matches (distributed across Q2 [Top Half SF pod], Q3, and Q4-other):
#     Seeded matches (one in Q2, one in Q3):
#       - [3] Anisimova/Tien vs Andreeva/Rublev (vacated Swiatek slot -> moved into MD)
#       - [4] Bencic/Cobolli vs Townsend/Zverev
#     Unseeded/Qualifier matches (1 in Q2, 1 in Q3, 1 in Q4):
#       - Navarro/Paul vs Errani/Vavassori (2x defending champs)
#       - Williams/Alcaraz vs Qualifier_1
#       - Muchova/Mensik vs Qualifier_2
#   Qualifying draw (Mon Aug 24 -> 2 qualifiers):
#     QA: (Siniakova/Patten vs Maria/Vacherot) vs (Stearns/Harrison vs Krunic/Pavic)
#     QB: (Dabrowski/Heliovaara vs Mladenovic/Arevalo) vs (Routliffe/Glasspool vs Stefani/Skupski)
#
# CRITICAL AVAILABILITY / INJURY FACTORS:
#   - Tiafoe lost Cinci Final Sun Aug 23 (6-3, 1-6, 6-0 to Fils) after receiving massage
#     treatment on upper left leg & lower back before Set 3!
#     -> Significant ~25-30% WD risk before Tue Aug 25 + slight performance drag if playing!
#   - Svitolina withdrew from Cinci R3 on Aug 19 with ankle injury (~15-20% WD risk + slight drag).
#   - Pegula plays Cinci WTA Final Sun night Aug 23 + had hip niggle Thu QF.
#   - Format: Fast4 (sets to 4, no-ad, 10-pt MTB for 3rd set) R1-SF -> VERY HIGH VARIANCE (scale ~530-580)!

mixed_ratings = {
    "Sabalenka and Djokovic": 1955,    # Rested elite singles stars, modest doubles synergy
    "Fernandez and Tiafoe": 1895,      # Discounted -35 from 1930 for Tiafoe Cinci Final leg/back fatigue (when playing)
    "Alt_Tiafoe_Replace": 1875,        # If Tiafoe WDs and Fernandez re-pairs or alternate enters
    "Eala and Auger-Aliassime": 1945,  # Both healthy, rested, athletic lefty+big-serve combo
    "Svitolina and Monfils": 1845,     # Discounted for Svitolina Aug 19 ankle WD + Monfils age 39
    "Alt_Svitolina_Replace": 1850,
    "Errani and Vavassori": 2085,      # 2x defending champs, elite mixed specialists
    "Navarro and Paul": 1920,
    "Townsend and Zverev": 2035,       # Rested elite doubles #1 Townsend + #1 USO seed Zverev
    "Bencic and Cobolli": 1895,
    "Anisimova and Tien": 1910,
    "Andreeva and Rublev": 1930,
    "Williams and Alcaraz": 1900,      # Elite Alcaraz (4m layoff) + 44yo Serena (rust/knee)
    "Muchova and Mensik": 1925,        # Muchova great hands/net + Mensik huge serve
    "Pegula and Fritz": 1950,          # Pegula playing Cinci Final Sun night
    "Shnaider and Ruud": 1925,
    # Qualifying teams (strong doubles specialists!)
    "Siniakova and Patten": 2070,
    "Maria and Vacherot": 1840,
    "Stearns and Harrison": 1935,
    "Krunic and Pavic": 2015,
    "Dabrowski and Heliovaara": 2045,
    "Mladenovic and Arevalo": 2020,
    "Routliffe and Glasspool": 2025,
    "Stefani and Skupski": 2030,
}

def sim_mixed_post_draw(ratings, scale=540.0, n_trials=200000, seed=301,
                        djo_bonus=0, p_tiafoe_play=0.72, p_tiafoe_wo_if_wd=0.25,
                        p_svit_play=0.82, p_svit_wo_if_wd=0.20):
    rng = random.Random(seed)
    r = dict(ratings)
    r["Sabalenka and Djokovic"] += djo_bonus

    p_cache = {}
    def mp(a, b, is_final=False):
        sc = (scale * 0.88) if is_final else scale  # Final is traditional 6-game sets (lower variance)
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

    for _ in range(n_trials):
        # 1. Qualifying Mon Aug 24 -> 2 qualifiers (qa, qb)
        qa1, _ = play_match("Siniakova and Patten", "Maria and Vacherot")
        qa2, _ = play_match("Stearns and Harrison", "Krunic and Pavic")
        qa, _ = play_match(qa1, qa2)

        qb1, _ = play_match("Dabrowski and Heliovaara", "Mladenovic and Arevalo")
        qb2, _ = play_match("Routliffe and Glasspool", "Stefani and Skupski")
        qb, _ = play_match(qb1, qb2)

        if rng.random() < 0.5:
            q_wa, q_mm = qa, qb
        else:
            q_wa, q_mm = qb, qa

        # 2. Construct Q1 (KNOWN!)
        if rng.random() < p_tiafoe_play:
            r1_opp = "Fernandez and Tiafoe"
        else:
            r1_opp = None if rng.random() < p_tiafoe_wo_if_wd else "Alt_Tiafoe_Replace"

        if rng.random() < p_svit_play:
            svit_pair = "Svitolina and Monfils"
        else:
            svit_pair = None if rng.random() < p_svit_wo_if_wd else "Alt_Svitolina_Replace"

        # 3. Assign Q2, Q3, Q4 remaining matches symmetrically
        seed_matches = [
            ("Anisimova and Tien", "Andreeva and Rublev"),
            ("Bencic and Cobolli", "Townsend and Zverev"),
        ]
        if rng.random() < 0.5:
            q2_seed, q3_seed = seed_matches[0], seed_matches[1]
        else:
            q2_seed, q3_seed = seed_matches[1], seed_matches[0]

        uns_matches = [
            ("Navarro and Paul", "Errani and Vavassori"),
            ("Williams and Alcaraz", q_wa),
            ("Muchova and Mensik", q_mm),
        ]
        rng.shuffle(uns_matches)
        q2_uns, q3_uns, q4_uns = uns_matches[0], uns_matches[1], uns_matches[2]

        # 4. Play R1
        # Q1
        w1, l1 = play_match("Sabalenka and Djokovic", r1_opp)
        if l1 == "Sabalenka and Djokovic":
            elim_cnt[w1] += 1
            continue
        w2, _ = play_match(svit_pair, "Eala and Auger-Aliassime")

        # Q1 QF
        w_q1, l_q1 = play_match(w1, w2)
        if l_q1 == "Sabalenka and Djokovic":
            elim_cnt[w_q1] += 1
            continue

        # Q2 (Top Half SF opponent)
        w3, _ = play_match(q2_seed[0], q2_seed[1])
        w4, _ = play_match(q2_uns[0], q2_uns[1])
        w_q2, _ = play_match(w3, w4)

        # SF1 (Top Half)
        w_top, l_top = play_match(w_q1, w_q2)
        if l_top == "Sabalenka and Djokovic":
            elim_cnt[w_top] += 1
            continue

        # Bottom Half (Q3 + Q4)
        w5, _ = play_match(q3_seed[0], q3_seed[1])
        w6, _ = play_match(q3_uns[0], q3_uns[1])
        w_q3, _ = play_match(w5, w6)

        w7, _ = play_match(q4_uns[0], q4_uns[1])
        w8, _ = play_match("Pegula and Fritz", "Shnaider and Ruud")
        w_q4, _ = play_match(w7, w8)

        w_bot, _ = play_match(w_q3, w_q4)

        # Final (6-game sets!)
        champ, runner = play_match(w_top, w_bot, is_final=True)
        if runner == "Sabalenka and Djokovic":
            elim_cnt[champ] += 1
        else:
            win_cnt += 1

    p_win = win_cnt / n_trials
    return {k: c / n_trials for k, c in elim_cnt.items()}, p_win

# Multi-regime sensitivity for Q1 (772246)
regimes_mixed = [
    # (label, weight, p_djo_play, scale, djo_bonus, p_tiafoe_play, p_svit_play, rating_overrides)
    ("Base (Tiafoe 72% play w/ drag, Fast4 high-var)", 0.45, 0.91, 540.0, 0, 0.72, 0.82, {}),
    ("Tiafoe Healthy & Fired Up (85% play, +35 Elo)", 0.20, 0.92, 540.0, -15, 0.85, 0.85, {"Fernandez and Tiafoe": 1930}),
    ("Tiafoe Injured/WD Heavy (50% play, -25 Elo)", 0.20, 0.91, 540.0, +10, 0.50, 0.78, {"Fernandez and Tiafoe": 1870}),
    ("Djo/Sab Stronger Singles Dominance (+50 Elo, lower var)", 0.15, 0.89, 480.0, +50, 0.72, 0.82, {}),
]

print("=== Q1 (772246) US OPEN MIXED DOUBLES — POST-DRAW AUG 23 ===")
blend_mixed = Counter()
p_no_elim_total = 0.0
for lbl, w, p_play, sc, db, pt, ps, ov in regimes_mixed:
    rr = dict(mixed_ratings)
    rr.update(ov)
    elims, pwin = sim_mixed_post_draw(rr, scale=sc, n_trials=120000, seed=301 + int(w*1000),
                                      djo_bonus=db, p_tiafoe_play=pt, p_svit_play=ps)
    p_no_elim = (1.0 - p_play) + p_play * pwin
    p_no_elim_total += w * p_no_elim
    top5_str = ", ".join(f"{k}:{p_play*v:.3f}" for k, v in sorted(elims.items(), key=lambda x: -x[1])[:5])
    print(f"  [{lbl:55s} w={w:.2f}] no_qual={p_no_elim:.3f} | {top5_str}")
    for k, v in elims.items():
        blend_mixed[k] += w * p_play * v

print(f"\nFINAL MIXED DOUBLES BLEND (P(no pair qualifies: WD or Win) = {p_no_elim_total:.4f}):")
for k, v in blend_mixed.most_common(12):
    print(f"  {k:28s}: {v:.4f}")


# ==============================================================================
# PART 2: Q2 (qid=608158) — 2026 US OPEN WOMEN'S SINGLES (AUG 23)
# ==============================================================================
# Aug 21 FanDuel (post-Rybakina Cinci retirement, pre-Sat Aug 22 SFs):
fd_wta = {
    "Aryna Sabalenka": 4.40,    # +340
    "Iga Swiatek": 5.70,        # +470
    "Coco Gauff": 7.50,         # +650
    "Elena Rybakina": 10.50,    # +950
    "Naomi Osaka": 10.50,       # +950
    "Jessica Pegula": 15.00,    # +1400
    "Amanda Anisimova": 15.00,  # +1400
    "Mirra Andreeva": 17.00,    # est just outside FD top-7 (+1400 cutoff)
    "Linda Noskova": 20.00,     # est
    "Madison Keys": 23.00,      # est
    "Field_Rest": 2.85,         # ~35% raw sum for rest of 118 players (Eala, Paolini, Muchova, Mboko, Zheng, etc.)
}

# Aug 21 Euro / LiveTennis.it (post-Rybakina Cinci retirement, pre-Sat Aug 22 SFs):
euro_wta = {
    "Aryna Sabalenka": 3.75,
    "Iga Swiatek": 6.50,
    "Coco Gauff": 8.00,
    "Mirra Andreeva": 8.00,
    "Elena Rybakina": 9.00,
    "Naomi Osaka": 9.00,
    "Jessica Pegula": 11.00,
    "Amanda Anisimova": 15.00,
    "Linda Noskova": 17.00,
    "Madison Keys": 21.00,
    "Field_Rest": 3.30,         # ~30% raw sum for rest of field (Paolini 50.0, Eala, Muchova, etc.)
}

fd_w_sh, fd_wz = shin_devig(fd_wta)
fd_w_pw, _ = power_devig(fd_wta)
eu_w_sh, eu_wz = shin_devig(euro_wta)
eu_w_pw, _ = power_devig(euro_wta)

# Market midpoint (Aug 21 snapshot: 50% FD + 50% Euro, each 50% Shin + 50% Power)
mkt_wta_aug21 = {}
for k in fd_wta:
    fd_m = 0.5 * fd_w_sh[k] + 0.5 * fd_w_pw[k]
    eu_m = 0.5 * eu_w_sh[k] + 0.5 * eu_w_pw[k]
    mkt_wta_aug21[k] = 0.5 * fd_m + 0.5 * eu_m

# Post-Aug 21 Bayesian adjustments (Aug 22-23 events NOT YET in Aug 21 lines):
#   1. Rybakina: Withdrew from US Open mixed doubles (Aug 22) + Tennis365 reports she admitted
#      she "could barely walk" with heel/leg injury! Multiplicative discount x0.76 (WD + compromised risk).
#   2. Pegula: Beat #1-form Swiatek 7-5 4-6 6-4 on Sat Aug 22 to reach Cinci Final (45th win, #3 seed,
#      2024 USO finalist)! Boost x1.35 (partly tempered by hip niggle/heavy workload -> net x1.30).
#   3. Gauff: Crushed Kostyuk 6-2 6-2 and Bejlek 6-4 6-1 to reach Cinci Final (Wim SF, Tor SF, Cinci F,
#      serve settled)! Boost x1.14.
#   4. Swiatek: Lost tight 3-set Cinci SF to Pegula + drops to #8 seed (faces Top-4 in QF). Slight x0.96.
#   5. Sabalenka: Already priced after Bejlek loss; 19-1 at USO (2x defending champ) -> hold x1.02.
#   6. Andreeva: Already priced after Kostyuk 4-6 6-0 6-2 loss -> hold x0.98.
#   7. Osaka: Healthy, 2x USO champ, rested -> hold x1.02.
adj_wta = {
    "Aryna Sabalenka": 1.02,
    "Iga Swiatek": 0.96,
    "Coco Gauff": 1.14,
    "Elena Rybakina": 0.76,
    "Naomi Osaka": 1.02,
    "Jessica Pegula": 1.32,
    "Mirra Andreeva": 0.98,
    "Amanda Anisimova": 1.00,
    "Linda Noskova": 1.00,
    "Madison Keys": 1.00,
    "Field_Rest": 0.99,
}
wta_updated = {k: mkt_wta_aug21[k] * adj_wta[k] for k in mkt_wta_aug21}
s_wta = sum(wta_updated.values())
wta_updated = {k: v / s_wta for k, v in wta_updated.items()}

print("\n=== Q2 (608158) 2026 US OPEN WOMEN'S SINGLES (AUG 23) ===")
print(f"Overrounds: FD={sum(1/v for v in fd_wta.values()):.3f} (z={fd_wz:.4f}), Euro={sum(1/v for v in euro_wta.values()):.3f} (z={eu_wz:.4f})")
print(f"{'Player':20s} | {'FD_Mkt':7s} | {'EU_Mkt':7s} | {'Aug21':7s} | {'Adj':5s} | {'AUG23':7s}")
for k in sorted(wta_updated, key=lambda x: -wta_updated[x]):
    fd_m = 0.5 * fd_w_sh[k] + 0.5 * fd_w_pw[k]
    eu_m = 0.5 * eu_w_sh[k] + 0.5 * eu_w_pw[k]
    print(f"{k:20s} | {fd_m:7.4f} | {eu_m:7.4f} | {mkt_wta_aug21[k]:7.4f} | {adj_wta[k]:5.2f} | {wta_updated[k]:7.4f}")
top5_w = sorted([(k, v) for k, v in wta_updated.items() if k != "Field_Rest"], key=lambda x: -x[1])[:5]
print("WTA Top-5 sum:", round(sum(v for _, v in top5_w), 4), "| Top-5:", [(k, round(v, 3)) for k, v in top5_w])


# ==============================================================================
# PART 3: Q3 (qid=891014) — 2026 US OPEN MEN'S SINGLES (AUG 23 — SINNER OUT!)
# ==============================================================================
# Aug 21 DraftKings (post-Sinner WD, pre-Alcaraz mixed WC, pre-Fils Cinci title):
dk_atp = {
    "Carlos Alcaraz": 2.40,     # +140
    "Alexander Zverev": 4.00,   # +300
    "Ben Shelton": 8.50,        # +750
    "Novak Djokovic": 8.50,     # +750
    "Taylor Fritz": 11.00,      # +1000
    "Rafael Jodar": 12.00,      # +1100
    "Arthur Fils": 23.00,       # +2200 (BEFORE Cinci title Sun Aug 23!)
    "Felix Auger-Aliassime": 26.00, # +2500
    "Daniil Medvedev": 26.00,   # +2500
    "Joao Fonseca": 31.00,      # +3000
    "Jakub Mensik": 31.00,      # +3000
    "Flavio Cobolli": 36.00,    # +3500
    "Tommy Paul": 41.00,        # +4000
    "Frances Tiafoe": 41.00,    # +4000
    "Field_Rest": 7.50,         # ~13.3% raw for Nakashima/Musetti/de Minaur (+5000 each) + rest
}

# Aug 21 Euro / LiveTennis.it (post-Sinner WD):
euro_atp = {
    "Carlos Alcaraz": 2.55,     # 2.35 - 2.75 range
    "Alexander Zverev": 3.00,
    "Novak Djokovic": 5.00,
    "Taylor Fritz": 10.00,
    "Ben Shelton": 10.00,
    "Rafael Jodar": 16.00,      # est (not in Euro top 5)
    "Arthur Fils": 22.00,       # est pre-Cinci title
    "Felix Auger-Aliassime": 28.00,
    "Daniil Medvedev": 25.00,
    "Joao Fonseca": 33.00,
    "Jakub Mensik": 33.00,
    "Flavio Cobolli": 38.00,
    "Tommy Paul": 45.00,
    "Frances Tiafoe": 45.00,
    "Field_Rest": 8.50,         # Musetti 50.0 + rest
}

dk_a_sh, dk_az = shin_devig(dk_atp)
dk_a_pw, _ = power_devig(dk_atp)
eu_a_sh, eu_az = shin_devig(euro_atp)
eu_a_pw, _ = power_devig(euro_atp)

mkt_atp_aug21 = {}
for k in dk_atp:
    dk_m = 0.5 * dk_a_sh[k] + 0.5 * dk_a_pw[k]
    eu_m = 0.5 * eu_a_sh[k] + 0.5 * eu_a_pw[k]
    mkt_atp_aug21[k] = 0.55 * dk_m + 0.45 * eu_m  # slight edge to DK (full listed board)

# Post-Aug 21 adjustments (Aug 22-23 events):
#   1. Alcaraz: Accepted Mixed Doubles WC w/ Serena (Aug 22) -> strong positive wrist confidence signal,
#      gives live Arthur Ashe court rhythm before singles; still 4m layoff BO5 caveat -> x1.03.
#   2. Arthur Fils: WON CINCINNATI MASTERS Sun Aug 23 (crushed de Minaur, Tirante, Cobolli 6-3 6-4,
#      Tiafoe 6-3 1-6 6-0; 10-0 deciding sets, 8-0 vs Americans)! Huge form boost -> x1.55!
#   3. Frances Tiafoe: Leg/back massage & 6-0 3rd-set loss in Cinci Final -> x0.80.
#   4. Taylor Fritz: Lost Cinci QF 7-6(9) 4-6 6-3 to Nakashima (Fri night Aug 21) -> slight x0.96.
adj_atp = {k: 1.00 for k in dk_atp}
adj_atp["Carlos Alcaraz"] = 1.03
adj_atp["Arthur Fils"] = 1.55
adj_atp["Frances Tiafoe"] = 0.80
adj_atp["Taylor Fritz"] = 0.96

atp_mkt_aug23 = {k: mkt_atp_aug21[k] * adj_atp[k] for k in mkt_atp_aug21}
s_atp = sum(atp_mkt_aug23.values())
atp_mkt_aug23 = {k: v / s_atp for k, v in atp_mkt_aug23.items()}

# Fundamental 128-draw BO5 Monte Carlo Cross-Check (SINNER OUT, Zverev #1, Alcaraz #2!)
def p_bo5(ea, eb):
    p3 = 1.0 / (1.0 + 10.0 ** (-(ea - eb) / 400.0))
    ps = p3
    for _ in range(8):
        f = ps*ps*(3 - 2*ps) - p3
        df = 6*ps*(1 - ps) + 1e-12
        ps = max(1e-6, min(1 - 1e-6, ps - f / df))
    return ps**3 * (10 - 15*ps + 6*ps*ps)

def place_128_draw(idxs, rng):
    seeds = idxs[:32]
    unseeded = idxs[32:]
    rng.shuffle(unseeded)
    bracket = [None] * 128
    bracket[0] = seeds[0]
    bracket[127] = seeds[1]
    s34 = [seeds[2], seeds[3]]
    rng.shuffle(s34)
    bracket[63], bracket[64] = s34[0], s34[1]
    s58 = list(seeds[4:8])
    rng.shuffle(s58)
    for pos, p in zip([31, 32, 95, 96], s58):
        bracket[pos] = p
    s916 = list(seeds[8:16])
    rng.shuffle(s916)
    for pos, p in zip([15, 16, 47, 48, 79, 80, 111, 112], s916):
        bracket[pos] = p
    pos_25_32 = [7, 24, 39, 56, 71, 88, 103, 120]
    pos_17_24 = [8, 23, 40, 55, 72, 87, 104, 119]
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

# Updated field WITHOUT Sinner! Zverev #1, Alcaraz #2!
atp_field_nosinner = [
    ("Alexander Zverev", 2140),       # #1 seed! RG champ, Wim F, AO SF, modest Aug dip
    ("Carlos Alcaraz",   2240),       # #2 seed! Mixture below over wrist/rust state
    ("Novak Djokovic",   2110),       # #3/4 seed, age-39 BO5 giant w/ heat/health flag
    ("Taylor Fritz",     2075),       # #3/4 seed, 2024 USO F, DC champ
    ("Ben Shelton",      2075),       # #5 seed, Montreal champ (10-0 sets!), Ashe boost
    ("Alex de Minaur",   2010),
    ("Daniil Medvedev",  2010),
    ("Felix Auger-Aliassime", 2005),
    ("Rafael Jodar",     2035),
    ("Arthur Fils",      2055),       # Upgraded after Cinci Masters title!
    ("Lorenzo Musetti",  1980),
    ("Jakub Mensik",     2005),
    ("Flavio Cobolli",   1990),       # RG F, Cinci SF
    ("Tommy Paul",       1990),       # Beat Zverev in Cinci
    ("Frances Tiafoe",   1975),       # Cinci F w/ leg/back flag
    ("Learner Tien",     1975),
    ("Joao Fonseca",     1990),       # Had ab WD in Cinci
    ("Andrey Rublev",    1975),
    ("Jiri Lehecka",     1975),
    ("Casper Ruud",      1955),
    ("Brandon Nakashima",1985),       # Montreal F + Cinci SF
    ("Karen Khachanov",  1950),
    ("Ugo Humbert",      1945),
    ("Tomas Machac",     1940),
    ("Francisco Cerundolo", 1915),
    ("Matteo Berrettini",1930),
    ("Hubert Hurkacz",   1925),
    ("Alex Michelsen",   1915),
    ("Sebastian Korda",  1915),
    ("Luciano Darderi",  1905),
    ("Valentin Vacherot",1900),
    ("Matteo Arnaldi",   1910),
]
for k in range(128 - 32):
    atp_field_nosinner.append((f"Field_{k}", 1910 - (k * 200.0 / 96.0)))

# Alcaraz state mixture (now confirmed playing + entered mixed doubles!):
#   - NearPeak (90-100%, Elo 2295): 0.42
#   - MildRust (80-88%, Elo 2195):  0.40
#   - SignificantRust/Flareup (Elo 2060): 0.13
#   - Pre-match/Early WD (out):     0.05
alc_states = [("NearPeak", 0.42, 2295), ("MildRust", 0.40, 2195), ("Rusty", 0.13, 2060), ("WD", 0.05, None)]
rng = random.Random(404)
mc_atp = Counter()
for st_name, w, ae in alc_states:
    pool = []
    for nm, el in atp_field_nosinner:
        if nm == "Carlos Alcaraz":
            if ae is None:
                continue
            pool.append((nm, ae))
        else:
            pool.append((nm, el))
    if len(pool) < 128:
        pool.append(("LL_Extra", 1750))
    elos = [p[1] for p in pool]
    names = [p[0] for p in pool]
    idxs = list(range(128))
    pc = {}
    def gp(i, j):
        k = (elos[i], elos[j])
        v = pc.get(k)
        if v is None:
            v = p_bo5(elos[i], elos[j])
            pc[k] = v
        return v
    n_tr = 12000
    cnt = Counter()
    for _ in range(n_tr):
        cur = place_128_draw(idxs, rng)
        while len(cur) > 1:
            nxt = []
            for k in range(0, len(cur), 2):
                a, b = cur[k], cur[k+1]
                nxt.append(a if rng.random() < gp(a, b) else b)
            cur = nxt
        cnt[names[cur[0]]] += 1
    for nm, c in cnt.items():
        mc_atp[nm] += w * c / n_tr

# Final ATP blend: 65% Sharp Market (DK+Euro + Aug 22-23 updates) + 35% Fundamental BO5 MC
atp_final = {}
for k in dk_atp:
    if k == "Field_Rest":
        continue
    atp_final[k] = 0.65 * atp_mkt_aug23[k] + 0.35 * mc_atp.get(k, 0.0)

print("\n=== Q3 (891014) 2026 US OPEN MEN'S SINGLES (AUG 23 — SINNER OUT!) ===")
print(f"Overrounds: DK={sum(1/v for v in dk_atp.values()):.3f} (z={dk_az:.4f}), Euro={sum(1/v for v in euro_atp.values()):.3f} (z={eu_az:.4f})")
print(f"{'Player':22s} | {'DK_Mkt':7s} | {'EU_Mkt':7s} | {'Mkt23':7s} | {'BO5_MC':7s} | {'FINAL':7s}")
for k in sorted(atp_final, key=lambda x: -atp_final[x])[:10]:
    dk_m = 0.5 * dk_a_sh[k] + 0.5 * dk_a_pw[k]
    eu_m = 0.5 * eu_a_sh[k] + 0.5 * eu_a_pw[k]
    print(f"{k:22s} | {dk_m:7.4f} | {eu_m:7.4f} | {atp_mkt_aug23[k]:7.4f} | {mc_atp.get(k,0):7.4f} | {atp_final[k]:7.4f}")
top5_m = sorted(atp_final.items(), key=lambda x: -x[1])[:5]
print("ATP Top-5 sum:", round(sum(v for _, v in top5_m), 4), "| Top-5:", [(k, round(v, 3)) for k, v in top5_m])
