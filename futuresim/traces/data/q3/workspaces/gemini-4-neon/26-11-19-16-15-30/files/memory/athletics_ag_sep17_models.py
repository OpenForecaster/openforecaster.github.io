"""
Quantitative Forecasting Models — Thu Sep 17, 2026
Batch: olympic_athletics_asian_games
Models:
  1. Q1 (qid=574485): PSA Women's World Squash No. 1 (Sep 21, 2026) — Verification check
  2. Q2 (qid=67348):  Asian Games Men's Basketball Bronze Medal (Sun Sep 20) — POST-QUARTERFINALS! (Only 4 teams left!)
  3. Q5 (qid=259249): PV Sindhu Furthest Round in 2026 Asian Games Badminton — World No. 11 -> Top-8 Seed Confirmation!
  4. Q6 (qid=556932): Asian Games Women's Singles Squash Gold — Official Seeds + London/Qatar Classic Form!
  5. Q7 (qid=700005): Asian Games Men's Singles Squash Gold — Official Seeds (#10 Al-Tamimi!) + London/Qatar Form!
"""
import math
import random
from collections import Counter
import numpy as np


def normal_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


# ==============================================================================
# MODEL 1: Q1 (qid=574485) — PSA WOMEN'S WORLD NO. 1 (SEP 21) SANITY CHECK
# ==============================================================================
def model_q1_squash_no1():
    print("=" * 74)
    print("MODEL 1: qid=574485 — PSA Women's World No. 1 (Sep 21, 2026) CHECK")
    print("=" * 74)
    # Check sensitivity to "match or better" (psasquashtour.com Sep 9 official) vs "strictly better" (squashinfo Sep 17 paraphrase)
    # Only differs when BOTH lose SF: (1 - p_H) * (1 - p_O) ~ 0.23 * 0.07 = 0.016
    p_h_sf = 0.77
    p_o_sf = 0.93
    p_o_fin = 0.505
    p_orfi_match = (1.0 - p_h_sf) + p_h_sf * p_o_sf * p_o_fin
    p_orfi_strict = (1.0 - p_h_sf) * p_o_sf + p_h_sf * p_o_sf * p_o_fin
    print(f"  Exact match-or-better (PSA official): Orfi = {p_orfi_match:.4f}, El Hammamy = {1-p_orfi_match:.4f}")
    print(f"  Strict-better sensitivity:            Orfi = {p_orfi_strict:.4f}, El Hammamy = {1-p_orfi_strict:.4f}")
    print(f"  Diff = {p_orfi_match - p_orfi_strict:.4f} (both-lose-SF mass = {(1-p_h_sf)*(1-p_o_sf):.4f})")
    print(f"  80/20 blend -> Orfi = {0.8*p_orfi_match + 0.2*p_orfi_strict:.4f} (vs prev 0.59 -> HOLD UNCHANGED!)")


# ==============================================================================
# MODEL 2: Q2 (qid=67348) — 2026 ASIAN GAMES MEN'S BASKETBALL BRONZE MEDAL
# ==============================================================================
# ALL FOUR QUARTERFINALS COMPLETED Wed Sep 16 (Xinhua / Yonhap / Korea Times):
#   - China 87-78 Saudi Arabia (+9; Zhu Junlong, Zhao Jiayi, Li Hongquan ALL OUT INJURED! Tied 62-62 after Q3!)
#   - Japan 85-78 Chinese Taipei (+7; Kotetsu Kurokawa 23 pts; host Nagoya crowd)
#   - South Korea 114-80 Jordan (+34; Lee Hyun-jung 28 pts in 21 min, Choi Jun-yong returned!)
#   - Iran 79-74 Bahrain (+5; missed 3 straight FTs up 3 w/ 10.4s left, Bahrain missed corner 3 to tie!)
#
# OFFICIAL FRI SEP 18 SEMIFINALS:
#   SF1: China vs Japan
#   SF2: South Korea vs Iran
# OFFICIAL SUN SEP 20 BRONZE MEDAL MATCH:
#   Loser(China vs Japan) vs Loser(South Korea vs Iran)
# ONLY 4 POSSIBLE WINNERS (sum = 1.00)! Chinese Taipei/Bahrain/Jordan/Saudi Arabia ELIMINATED!
def model_q2_basketball_bronze():
    print("\n" + "=" * 74)
    print("MODEL 2: qid=67348 — 2026 Asian Games Men's Basketball Bronze (POST-QF!)")
    print("=" * 74)

    # Full tournament resume calibration (margin vs average QF team, incl. Japan Nagoya HCA ~+2.0):
    #   China:       +38 KAZ, +46 BAH, +44 PHI, +9 KSA (w/ 3 forwards out injured!)
    #                Prior was +18.5; injury depletion + tight +9 KSA pulls posterior down to ~+13.8 (wide sd=3.5 due to injury status!)
    #   South Korea: +16 KSA, +54 INA, +17 JPN, +34 JOR (Choi Jun-yong back, 4-0!)
    #                Prior was +12.5; +34 over Jordan (vs Iran +13, TPE +3) pulls posterior UP to ~+14.5 (sd=2.5)
    #   Japan:       +45 INA, +6 KSA, -17 KOR, +7 TPE (3-1, host in Nagoya!)
    #                Prior was +4.8; beating TPE +7 pulls posterior UP to ~+6.2 (sd=2.5)
    #   Iran:        -6 QAT, +3 TPE, +13 JOR, +5 BAH (nearly choked to Bahrain, whom China beat by +46!)
    #                Prior was +5.0; +5 over Bahrain pulls posterior DOWN to ~+2.8 (sd=2.7)

    scenarios = [
        # (name, weight, {team: (mean, sd)}, game_sd_range, bronze_letdown_fav_pen)
        (
            "S1: Base Posterior (China injured wings ~half-limited, KOR surging, Iran sluggish)",
            0.45,
            {"China": (13.8, 3.4), "South Korea": (14.5, 2.5), "Japan": (6.2, 2.4), "Iran": (2.8, 2.6)},
            (10.8, 12.6),
            1.0,  # Slight letdown penalty (-1.0 pt) if a heavy gold favorite loses SF and plays Bronze
        ),
        (
            "S2: China Rebounds / Forwards Return (China +16.2, KOR +14.2, Japan +6.0, Iran +3.2)",
            0.25,
            {"China": (16.2, 2.8), "South Korea": (14.2, 2.5), "Japan": (6.0, 2.4), "Iran": (3.2, 2.6)},
            (10.8, 12.6),
            1.0,
        ),
        (
            "S3: China Wing Injuries Severe + Home Japan Hot (China +11.5, KOR +14.8, Japan +7.2, Iran +2.5)",
            0.20,
            {"China": (11.5, 3.2), "South Korea": (14.8, 2.5), "Japan": (7.2, 2.4), "Iran": (2.5, 2.6)},
            (10.8, 12.6),
            1.0,
        ),
        (
            "S4: Iran Veteran Knockout Resurgence (China +13.5, KOR +13.0, Japan +5.8, Iran +4.8)",
            0.10,
            {"China": (13.5, 3.0), "South Korea": (13.0, 2.5), "Japan": (5.8, 2.4), "Iran": (4.8, 2.6)},
            (11.0, 13.0),
            1.0,
        ),
    ]

    rng = random.Random(6734817)
    n_per = 150000
    blend_bronze = Counter()
    blend_appear = Counter()
    blend_gold = Counter()

    def play(t1, t2, r, sd, pen1=0.0, pen2=0.0):
        eff_sd = sd * (1.25 if rng.random() < 0.15 else 1.0)
        margin = ((r[t1] - pen1) - (r[t2] - pen2)) + rng.gauss(0.0, eff_sd)
        return (t1, t2) if margin > 0 else (t2, t1)

    for sname, w, ratings_spec, (sd_lo, sd_hi), letdown in scenarios:
        bc = Counter()
        ac = Counter()
        gc = Counter()
        sf1_chn = 0
        sf2_kor = 0
        for _ in range(n_per):
            # Sample true team strengths ONCE per tournament (crucial Bayesian correlation between SF & Bronze!)
            r = {t: rng.gauss(mu, s) for t, (mu, s) in ratings_spec.items()}
            sd = rng.uniform(sd_lo, sd_hi)

            w_sf1, l_sf1 = play("China", "Japan", r, sd)
            w_sf2, l_sf2 = play("South Korea", "Iran", r, sd)
            if w_sf1 == "China":
                sf1_chn += 1
            if w_sf2 == "South Korea":
                sf2_kor += 1

            ac[l_sf1] += 1
            ac[l_sf2] += 1

            # Bronze match: minor letdown if China or South Korea got upset in SF vs hungrier underdog
            p1 = letdown if l_sf1 in ("China", "South Korea") else 0.0
            p2 = letdown if l_sf2 in ("China", "South Korea") else 0.0
            bw, _ = play(l_sf1, l_sf2, r, sd * 1.05, pen1=p1, pen2=p2)
            gw, _ = play(w_sf1, w_sf2, r, sd)
            bc[bw] += 1
            gc[gw] += 1

        print(f"\n  [{w:.2f}] {sname}")
        print(f"        SF win probs: China={sf1_chn/n_per:.3f} vs Japan={1-sf1_chn/n_per:.3f} | Korea={sf2_kor/n_per:.3f} vs Iran={1-sf2_kor/n_per:.3f}")
        print("        Bronze: " + ", ".join(f"{t}={bc[t]/n_per:.4f}" for t in ["Japan", "Iran", "China", "South Korea"]))
        for t in ["Japan", "Iran", "China", "South Korea"]:
            blend_bronze[t] += w * (bc[t] / n_per)
            blend_appear[t] += w * (ac[t] / n_per)
            blend_gold[t] += w * (gc[t] / n_per)

    print("\n  FINAL BLENDED POST-QF PROBABILITIES (SUM = 1.0000):")
    print(f"  {'Country':14s} {'Bronze%':>9s} {'InBronze%':>10s} {'Gold%':>9s}")
    for t, p in sorted(blend_bronze.items(), key=lambda x: -x[1]):
        print(f"  {t:14s} {p:9.4f} {blend_appear[t]:10.4f} {blend_gold[t]:9.4f}")
    print(f"  Sum = {sum(blend_bronze.values()):.4f}")


# ==============================================================================
# MODEL 3: Q5 (qid=259249) — PV SINDHU FURTHEST ROUND (2026 ASIAN GAMES BADMINTON)
# ==============================================================================
# New Sep 16 HT Evidence:
#   - Skipped China Masters intentionally for recovery/training block (NOT injured! "best physical shape in a long time")
#   - World No. 11 -> HT explicitly notes: "A higher seeding in Aichi-Nagoya will ensure world No.11 Sindhu
#     avoids premature landmines in the opening rounds, allowing her to build rhythm before encountering the
#     heavyweights in the quarter-finals and beyond."
#   - Under Asian Games 2-per-NOC cap (excludes China #3/#4 Han Yue/Gao Fangjie + any non-Asians / 3rd Thai/JPN),
#     World No. 11 is ~82% likely to be Seed #5-#8 (likely #7 or #8) and only ~18% Seed #9 (unseeded)!
#   - Recent peak form: Won Japan Open Super 750 in Tokyo (July), beating Chen Yufei (SF) & Akane Yamaguchi (F);
#     lost razor-close 3-gamer (11-21, 21-15, 17-21) to Wang Zhiyi at Aug Worlds R16.
#   - Still 0-10 career H2H vs World No. 1 An Se-young!
def model_q5_pv_sindhu():
    print("\n" + "=" * 74)
    print("MODEL 3: qid=259249 — PV Sindhu Furthest Round (2026 Asian Games Badminton)")
    print("=" * 74)

    rng = random.Random(25924917)
    n_sims = 250000
    rounds = Counter()

    # Asian Games WS draw structure: 32-bracket (top 16+ get R64 bye; Sindhu ALWAYS starts in R32 unless rare R64 unseeded)
    # Top 4 seeds: An Se-young (#1), Wang Zhiyi (#2), Chen Yufei (#3), Akane Yamaguchi (#4)
    # Seeds 5-8: Tomoka Miyazaki, Gregoria Mariska Tunjung / Putri Kusuma Wardani, Pornpawee Chochuwong, PV Sindhu (82%)
    # Unseeded tier (R32/R16): mix of dangerous #9-#16 Asians (Ratchanok/Supanida/Busanan, Yeo Jia Min, Putri/Gregoria #2,
    #                          Sim Yu-jin/Kim Ga-eun, Chiu Pin-chian/Wen Chi-hsu, Goh Jin Wei) + weak #17-#32 field!
    for _ in range(n_sims):
        # 1.2% pre-event withdrawal / freak R64 edge case
        if rng.random() < 0.012:
            rounds["Outside_DNS_R64"] += 1
            continue

        # Form draw for Sindhu across the tournament (correlated match quality)
        form = rng.gauss(0.0, 0.06)  # +/- ~6% shift in win prob from tournament form

        def clamp(p):
            return min(0.97, max(0.03, p))

        is_top8_seed = rng.random() < 0.82

        if is_top8_seed:
            # --- PATH A: SEEDED #5-#8 (82%) ---
            # R32: vs weak/unseeded opponent (75% easy #17-32 [94% win], 25% tricky unseeded #9-16 [76% win])
            p_r32 = clamp((0.94 if rng.random() < 0.75 else 0.76) + form)
            if rng.random() > p_r32:
                rounds["Round of 32"] += 1
                continue

            # R16: vs winner of two unseeded opponents (typically #9-#18 Asia, e.g. Yeo Jia Min, Putri, Busanan, Kim Ga-eun)
            # Sindhu in peak July/Sep form wins ~70%
            p_r16 = clamp(rng.uniform(0.64, 0.77) + form)
            if rng.random() > p_r16:
                rounds["Round of 16"] += 1
                continue

            # QF: vs Top-4 seed (or upsetter ~12% of time!)
            if rng.random() < 0.12:
                # Top-4 seed upset before QF -> Sindhu plays an unseeded/fringe QF opponent (~65%)
                p_qf = clamp(0.65 + form)
            else:
                opp = rng.choice(["An", "Wang", "Chen", "Yamaguchi"])
                base_qf = {"An": 0.07, "Wang": 0.32, "Chen": 0.40, "Yamaguchi": 0.42}[opp]
                p_qf = clamp(base_qf + form)
            if rng.random() > p_qf:
                rounds["Quarterfinals"] += 1
                continue

            # SF: vs another elite Top-4 / Top-6 opponent (higher chance of hitting An Se-young here if not in QF!)
            if rng.random() < 0.38:
                p_sf = clamp(0.08 + form)  # An Se-young
            else:
                p_sf = clamp(rng.uniform(0.32, 0.44) + form)  # Wang/Chen/Yamaguchi/Miyazaki
            if rng.random() > p_sf:
                rounds["Semifinals"] += 1
                continue

            rounds["Final"] += 1

        else:
            # --- PATH B: UNSEEDED #9 (18%) ---
            # R32: ~25% draws Top-4 seed right away, ~25% draws 5-8 seed, ~50% draws unseeded
            u = rng.random()
            if u < 0.25:
                opp = rng.choice(["An", "Wang", "Chen", "Yamaguchi"])
                p_r32 = clamp({"An": 0.07, "Wang": 0.32, "Chen": 0.40, "Yamaguchi": 0.42}[opp] + form)
                beat_top4_early = True
            elif u < 0.50:
                p_r32 = clamp(0.54 + form)  # vs 5-8 seed
                beat_top4_early = False
            else:
                p_r32 = clamp(0.84 + form)  # vs unseeded
                beat_top4_early = False

            if rng.random() > p_r32:
                rounds["Round of 32"] += 1
                continue

            # R16: if didn't beat Top-4 in R32, ~50% chance to meet Top-4 or 5-8 seed in R16
            if beat_top4_early:
                p_r16 = clamp(0.70 + form)
            else:
                v = rng.random()
                if v < 0.45:
                    opp = rng.choice(["An", "Wang", "Chen", "Yamaguchi"])
                    p_r16 = clamp({"An": 0.07, "Wang": 0.32, "Chen": 0.40, "Yamaguchi": 0.42}[opp] + form)
                elif v < 0.75:
                    p_r16 = clamp(0.55 + form)
                else:
                    p_r16 = clamp(0.72 + form)
            if rng.random() > p_r16:
                rounds["Round of 16"] += 1
                continue

            # QF
            opp = rng.choice(["An", "Wang", "Chen", "Yamaguchi", "Seed58"])
            p_qf = clamp({"An": 0.07, "Wang": 0.32, "Chen": 0.40, "Yamaguchi": 0.42, "Seed58": 0.54}[opp] + form)
            if rng.random() > p_qf:
                rounds["Quarterfinals"] += 1
                continue

            # SF
            p_sf = clamp((0.08 if rng.random() < 0.35 else 0.38) + form)
            if rng.random() > p_sf:
                rounds["Semifinals"] += 1
                continue

            rounds["Final"] += 1

    print("  250k Bracket MC Results:")
    for k in ["Quarterfinals", "Round of 16", "Semifinals", "Round of 32", "Final", "Outside_DNS_R64"]:
        print(f"    {k:18s}: {rounds[k]/n_sims:.4f}")
    top5 = sum(rounds[k] for k in ["Quarterfinals", "Round of 16", "Semifinals", "Round of 32", "Final"]) / n_sims
    print(f"  Top-5 sum = {top5:.4f}")


# ==============================================================================
# MODEL 4 & 5: Q6 (qid=556932) WOMEN'S & Q7 (qid=700005) MEN'S SQUASH GOLD
# ==============================================================================
# Official Seedings Confirmed (Sep 10 Sportstar & Sep 16 KhelNow)!
# Uses 16-slot seeded bracket (so #10 seed Abdulla Al-Tamimi ACTUALLY plays R16 vs a Top-8 seed!)
def rank_to_elo(r, scale=215.0):
    return 2300.0 - scale * math.log(r)


def sim_seeded_16_bracket(seeds_1_to_8, unseeded_threats, n_trials=200000, seed=55693217):
    """
    seeds_1_to_8: list of 8 tuples (name, p_play, states) in exact official seed order 1..8
                  where states = [(prob, mu_elo, sd_elo), ...]
    unseeded_threats: list of tuples (name, p_play, states) placed in random R16 slots against seeds 1..8
                      (remaining R16 slots filled by weak Asian field Elo ~1220)
    """
    rng = random.Random(seed)
    wins = Counter()

    def draw_elo(p_play, states):
        if rng.random() > p_play:
            return None
        u = rng.random()
        cum = 0.0
        chosen = states[-1]
        for st in states:
            cum += st[0]
            if u <= cum:
                chosen = st
                break
        _, mu, sd = chosen
        return rng.gauss(mu, sd)

    def match(a, b):
        if a is None:
            return b
        if b is None:
            return a
        p_a = 1.0 / (1.0 + 10.0 ** (-(a[1] - b[1]) / 400.0))
        return a if rng.random() < p_a else b

    for _ in range(n_trials):
        s_players = []
        for nm, pp, sts in seeds_1_to_8:
            e = draw_elo(pp, sts)
            s_players.append((nm, e) if e is not None else ("Field_Sub", 1320.0))

        # Standard squash bracket order of 8 pods:
        # Top half: Pod0=(#1), Pod1=(5-8), Pod2=(3/4), Pod3=(5-8)
        # Bot half: Pod4=(5-8), Pod5=(3/4), Pod6=(5-8), Pod7=(#2)
        p34 = [s_players[2], s_players[3]]
        rng.shuffle(p34)
        p58 = [s_players[4], s_players[5], s_players[6], s_players[7]]
        rng.shuffle(p58)
        pods = [s_players[0], p58[0], p34[0], p58[1], p58[2], p34[1], p58[3], s_players[1]]

        # Fill 8 R16 opponent slots with unseeded threats + weak field
        r16_opps = []
        for nm, pp, sts in unseeded_threats:
            e = draw_elo(pp, sts)
            if e is not None:
                r16_opps.append((nm, e))
        while len(r16_opps) < 8:
            r16_opps.append(("Field_Weak", rng.gauss(1240.0, 50.0)))
        rng.shuffle(r16_opps)

        # R16 -> QF -> SF -> F
        qfs = [match(pods[i], r16_opps[i]) for i in range(8)]
        sfs = [match(qfs[0], qfs[1]), match(qfs[2], qfs[3]), match(qfs[4], qfs[5]), match(qfs[6], qfs[7])]
        fin = [match(sfs[0], sfs[1]), match(sfs[2], sfs[3])]
        champ = match(fin[0], fin[1])
        wins[champ[0]] += 1

    return {k: c / n_trials for k, c in wins.items()}


def model_q6_women_squash():
    print("\n" + "=" * 74)
    print("MODEL 4: qid=556932 — Asian Games Women's Singles Squash Gold (OFFICIAL SEEDS!)")
    print("=" * 74)
    # Official Top-8 Seeds (KhelNow Sep 16 / Sportstar Sep 10):
    #   [1] Sivasangari Subramaniam (MAS, WR #5; London Classic SF crushing Anahat 11-4,11-4; Qatar Classic Platinum SF TODAY!)
    #       Slight fatigue/injury risk from deep Doha run (-3% injury/scratch, +25 Elo hot-form vs Watanabe London QF loss)
    #   [2] Satomi Watanabe (JPN, WR #6; lost London QF 0-2 to Kennedy; fresh & home court Nagoya +18 Elo)
    #   [3] Anahat Singh (IND, WR #20; beat #11 Nele Gilis at London R16, crushed 4-11,4-11 by Siva in QF -> Elo ~1675, sd=60)
    #   [4] Aira Azman (MAS, WR #21 -> Elo ~1645)
    #   [5] Chan Sin Yuk (HKG, WR ~#24, 2023 AG silver -> Elo ~1620)
    #   [6] Ho Tze-Lok (HKG, WR ~#27, 2025 Asian Champ -> Elo ~1595)
    #   [7] Tanvi Khanna (IND -> Elo ~1460)
    #   [8] Akari Midorikawa (JPN -> Elo ~1440)
    seeds_w = [
        ("Sivasangari Subramaniam", 0.965, [(1.0, rank_to_elo(5) + 25, 48)]),  # ~1979
        ("Satomi Watanabe",         0.975, [(1.0, rank_to_elo(6) + 15, 50)]),  # ~1930
        ("Anahat Singh",            0.985, [(1.0, rank_to_elo(19) + 10, 60)]), # ~1677
        ("Aira Azman",              0.985, [(1.0, rank_to_elo(21), 55)]),      # ~1645
        ("Chan Sin Yuk",            0.985, [(1.0, rank_to_elo(24), 55)]),      # ~1617
        ("Ho Tze-Lok",              0.985, [(1.0, rank_to_elo(27), 55)]),      # ~1591
        ("Tanvi Khanna",            0.985, [(1.0, rank_to_elo(48), 55)]),      # ~1468
        ("Akari Midorikawa",        0.985, [(1.0, rank_to_elo(55), 55)]),      # ~1438
    ]
    res = sim_seeded_16_bracket(seeds_w, [], n_trials=250000, seed=55693217)
    for k, v in sorted(res.items(), key=lambda x: -x[1])[:8]:
        print(f"  {k:26s}: {v:.4f}")
    top5 = sorted([(k, v) for k, v in res.items() if not k.startswith("Field")], key=lambda x: -x[1])[:5]
    print("  Top-5 sum:", round(sum(v for _, v in top5), 4))


def model_q7_men_squash():
    print("\n" + "=" * 74)
    print("MODEL 5: qid=700005 — Asian Games Men's Singles Squash Gold (OFFICIAL SEEDS!)")
    print("=" * 74)
    # Official Top-10 Seeds (KhelNow Sep 16 / Sportstar Sep 10):
    #   [1] Ng Eain Yow (MAS, WR #18, defending AG champ, played Qatar Classic R1 vs Soliman)
    #   [2] Abhay Singh (IND, WR #24, played Qatar Classic R1 vs Steinmann)
    #   [3] Noor Zaman (PAK, WR #29, played Qatar Classic R1 vs El Torkey)
    #   [4] Veer Chotrani (IND, WR #38, lost London R1 9-11, 9-11 vs #34 Wilhelmi)
    #   [5] Muhammad Ashab Irfan (PAK, WR ~#42)
    #   [6] Alex Lau (Tsz Kwan Lau, HKG, 2025 Asian Individual Champ! WR ~#44, +25 Asian-event punch!)
    #   [7] Ryunosuke Tsukue (JPN, WR ~#48, home court Nagoya +25 Elo!)
    #   [8] Henry Leung (Chi Hin Henry Leung, HKG, WR ~#55)
    #   Unseeded threats:
    #   [9] Sanjay Jeeva (MAS, WR #63)
    #   [10] Abdulla Al-Tamimi (QAT, WR #61 post-Achilles; lost London R1 6-11,7-11 to #42 Tandon,
    #        THEN pushed WR #4 Karim Abdel Gawad to 4 hard games 7-11,13-15,11-5,8-11 at Qatar Classic Sep 12!!
    #        Bimodal form: 35% near-peak WR #18-22 level [Elo ~1670], 45% solid WR #32 level [Elo ~1560], 20% rusty/fatigued [Elo ~1430];
    #        AND must play 4 brutal rounds from #10 seed!)
    seeds_m = [
        ("Ng Eain Yow",          0.975, [(1.0, rank_to_elo(18) + 15, 52)]),  # ~1694
        ("Abhay Singh",          0.980, [(1.0, rank_to_elo(24) + 5,  52)]),  # ~1622
        ("Noor Zaman",           0.980, [(1.0, rank_to_elo(28) + 5,  55)]),  # ~1589
        ("Veer Chotrani",        0.980, [(1.0, rank_to_elo(38),      55)]),  # ~1518
        ("Muhammad Ashab Irfan", 0.980, [(1.0, rank_to_elo(41),      55)]),  # ~1502
        ("Alex Lau",             0.980, [(1.0, rank_to_elo(44) + 22, 55)]),  # ~1508 (2025 Asian Champ!)
        ("Ryunosuke Tsukue",     0.980, [(1.0, rank_to_elo(48) + 22, 55)]),  # ~1490 (Home Nagoya!)
        ("Henry Leung",          0.980, [(1.0, rank_to_elo(54),      55)]),  # ~1442
    ]
    unseeded_m = [
        ("Abdulla Al-Tamimi", 0.92, [
            (0.35, rank_to_elo(20) + 15, 55),  # ~1671 (Gawad 4-game form!)
            (0.45, rank_to_elo(32),      55),  # ~1555 (mid-comeback)
            (0.20, rank_to_elo(58),      55),  # ~1427 (rusty / Tandon form / Achilles load)
        ]),
        ("Sanjay Jeeva", 0.98, [(1.0, rank_to_elo(63), 50)]),
    ]
    res = sim_seeded_16_bracket(seeds_m, unseeded_m, n_trials=250000, seed=70000517)
    for k, v in sorted(res.items(), key=lambda x: -x[1])[:10]:
        print(f"  {k:24s}: {v:.4f}")
    top5 = sorted([(k, v) for k, v in res.items() if not k.startswith("Field")], key=lambda x: -x[1])[:5]
    print("  Top-5 sum:", round(sum(v for _, v in top5), 4))


if __name__ == "__main__":
    model_q1_squash_no1()
    model_q2_basketball_bronze()
    model_q5_pv_sindhu()
    model_q6_women_squash()
    model_q7_men_squash()
