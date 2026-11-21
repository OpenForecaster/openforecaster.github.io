"""
Quantitative Monte Carlo Models — Fri Sep 25, 2026
Batch: asian_games_racket_fb (4 questions)
  1. qid=259249: PV Sindhu Furthest Round in Individual Badminton
     - Chiu Pin-chian CRUSHED Letshanaa 21-13, 21-13 -> p_chiu = 1.00!
     - Wikipedia Section 2 bracket: Tomoka Miyazaki plays S. Kherlenbaatar (MGL) in R32 -> p_miy_reaches = 0.995!
     - Olympics.com exact schedule: R32 8:00 AM IST -> R16 12:30 PM IST (4.5h turnaround vs 6.5h prior!);
       The Star confirms <4h same-day badminton doubleheaders took heavy toll on Day 1!
  2. qid=556932: Asian Games Women's Singles Squash Gold
     - ALL 4 QFs COMPLETED! EXACT FINAL FOUR LOCKED (exhaustive sum = 1.00):
       SF1: [1] Sivasangari Subramaniam (def. Ho Tze Lok 11-8, 11-7, 11-8 in 25m)
            vs [5] Chan Sin Yuk (def. Aira Azman 10-12, 11-9, 11-5, 11-9 in 32m)!
       SF2: [2] Satomi Watanabe (won QF)
            vs [3] Anahat Singh (crushed Tanvi Khanna 11-2, 11-5, 11-3)!
     - Aira Azman ELIMINATED!
  3. qid=700005: Asian Games Men's Singles Squash Gold
     - ALL 4 QFs COMPLETED! EXACT FINAL FOUR & EXACT SEMIFINAL PAIRINGS LOCKED (exhaustive sum = 1.00):
       SF1 (16:15 JST): [1] Ng Eain Yow (strolled past Alex Lau) vs [3] Noor Zaman (def. Henry Leung 3-1 in 28m)
       SF2 (14:45 JST): [2] Abhay Singh (crushed Tsukue 11-4, 11-3, 11-6!) vs [5] Muhammad Ashab Irfan (def. Chotrani 3-1 in 41m)
     - Chotrani, Alex Lau, Tsukue, Henry Leung, Al-Tamimi ALL ELIMINATED!
  4. qid=889545: Asian Games Men's Football China Eliminator
     - QF1 COMPLETED: Uzbekistan 3-0 Saudi Arabia (KSA ELIMINATED; UZB locked in SF1, 4W 12-1 GD!)
     - QF2 COMPLETED: South Korea 4-0 Vietnam (VIE ELIMINATED; KOR locked as China's SF2 opponent!
       Grasshopper FW Lee Young-jun brace + assist on first start, Brentford CB Kim Ji-soo goal!)
     - Sat Sep 26 QF3: China (Wang Yudong suspended!) vs Thailand; QF4: Japan vs North Korea.
"""
import math
import random
from collections import Counter
import numpy as np


def rank_to_elo(r, scale=215.0):
    return 2300.0 - scale * math.log(r)


def logit(p):
    p = min(0.995, max(0.005, p))
    return math.log(p / (1.0 - p))


def inv_logit(x):
    return 1.0 / (1.0 + math.exp(-x))


# ==============================================================================
# MODEL 1: qid=259249 — PV SINDHU FURTHEST ROUND (POST-R64 + EXACT SEC 2 DRAW!)
# ==============================================================================
def model_pv_sindhu_sep25(n_trials=300000, seed=25924925):
    """
    VERIFIED FRI SEP 25 UPDATES:
      1. Chiu Pin-chian (TPE, WR ~#13) beat Letshanaa 21-13, 21-13 (clean 2-game win -> p_chiu = 1.00!).
      2. Wikipedia Section 2 exact R32/R16 opponents:
         - [7] Tomoka Miyazaki (JPN, WR #7) plays S. Kherlenbaatar (MGL) in R32 -> ~99.5% Miyazaki reaches R16
           AND plays an effortless ~15-min morning warm-up while Sindhu battles WR #13 Chiu Pin-chian!
         - [4] Chen Yufei (CHN, WR #4) plays Liang Ka Wing (HKG) in R32 -> W(Nguyen Thuy Linh / Wiryawan) in R16
           -> ~91% Chen Yufei reaches QF!
         - [1] An Se-young (KOR, WR #1) in Section 1 -> ~94% reaches SF!
      3. Olympics.com exact Sat Sep 26 schedule:
         - R32: PV Sindhu vs Chiu Pin-chian at 8:00 AM IST (11:30 AM JST)
         - R16: 12:30 PM IST (4:00 PM JST) — ONLY ~4.5h turnaround (The Star Sep 25 specifically flagged
           the <4h badminton doubleheader toll causing early upsets on Day 1!).
    """
    rng = random.Random(seed)
    print("=" * 80)
    print("MODEL 1: qid=259249 — PV Sindhu Furthest Round (POST-R64 + EXACT SECTION 2)")
    print("=" * 80)

    # Multi-regime blend:
    # (name, weight, p_vs_chiu, p_miy_reaches, p_vs_miy_fresh, p_chen_reaches, p_vs_chen, p_an_reaches, p_vs_an)
    regimes = [
        (
            "R1: Base Post-R64 (Chiu 21-13 21-13 sharp; 4.5h doubleheader vs fresh home Miyazaki; Chen/An)",
            0.45,
            0.73,
            0.995, 0.49,
            0.91, 0.30,
            0.94, 0.06,
        ),
        (
            "R2: Peak Big-Stage Sindhu (handles Chiu cleanly, beats Miyazaki as at Malaysia Open, threatens Chen)",
            0.30,
            0.80,
            0.992, 0.59,
            0.88, 0.39,
            0.92, 0.09,
        ),
        (
            "R3: Doubleheader Fatigue / Chiu Grinder (tough R32 + <4.5h turnaround vs fresh home Miyazaki)",
            0.25,
            0.65,
            0.997, 0.37,
            0.93, 0.22,
            0.95, 0.03,
        ),
    ]

    blend = Counter()
    for rname, w, p_vs_c, p_miy_r, p_vs_m, p_chen_r, p_vs_ch, p_an_r, p_vs_a in regimes:
        counts = Counter()
        for _ in range(n_trials):
            # 0.4% pre-match freak withdrawal/DNS
            if rng.random() < 0.004:
                counts["Outside_DNS"] += 1
                continue

            form_lo = rng.gauss(0.0, 0.28)

            # R32 (Sat 8:00 AM IST): LOCKED vs Chiu Pin-chian (TPE, WR #13)
            p_r32 = inv_logit(logit(p_vs_c) + form_lo)
            if rng.random() > p_r32:
                counts["Round of 32"] += 1
                continue

            # Conditional on beating Chiu: ~40% chance Chiu pushed her to a draining 3-gamer
            # With ONLY ~4.5h gap vs Miyazaki who jogged past Mongolia, 3-game drag is real (-0.22 logit)
            r32_fatigue_lo = -0.22 if rng.random() < 0.40 else -0.05

            # R16 (Sat 12:30 PM IST): 99.5% vs [7] Tomoka Miyazaki (JPN, home)
            if rng.random() < p_miy_r:
                p_r16 = inv_logit(logit(p_vs_m) + form_lo + r32_fatigue_lo)
            else:
                p_r16 = inv_logit(logit(0.95) + form_lo)
            if rng.random() > p_r16:
                counts["Round of 16"] += 1
                continue

            # QF (Sun 9:30 AM JST): ~91% vs [4] Chen Yufei (CHN)
            if rng.random() < p_chen_r:
                p_qf = inv_logit(logit(p_vs_ch) + form_lo)
            else:
                p_qf = inv_logit(logit(0.68) + form_lo)
            if rng.random() > p_qf:
                counts["Quarterfinals"] += 1
                continue

            # SF (Mon 9:30 AM JST): ~94% vs [1] An Se-young (KOR)
            if rng.random() < p_an_r:
                p_sf = inv_logit(logit(p_vs_a) + form_lo)
            else:
                p_sf = inv_logit(logit(0.52) + form_lo)
            if rng.random() > p_sf:
                counts["Semifinals"] += 1
                continue

            counts["Final"] += 1

        print(f"\n  [{w:.2f}] {rname}")
        for k in ["Round of 32", "Round of 16", "Quarterfinals", "Semifinals", "Final", "Outside_DNS"]:
            p = counts[k] / n_trials
            blend[k] += w * p
            print(f"        {k:16s}: {p:.4f}")

    print("\n  === FINAL BLENDED PV SINDHU (vs Sep 24: R16 0.35, QF 0.27, R32 0.215, SF 0.14, Final 0.02) ===")
    for k in ["Round of 16", "Round of 32", "Quarterfinals", "Semifinals", "Final", "Outside_DNS"]:
        print(f"    {k:16s}: {blend[k]:.4f}")
    top5 = sum(blend[k] for k in ["Round of 16", "Round of 32", "Quarterfinals", "Semifinals", "Final"])
    print(f"  Top-5 sum = {top5:.4f}")


# ==============================================================================
# MODEL 2: qid=556932 — WOMEN'S SINGLES SQUASH GOLD (EXACT FINAL FOUR LOCKED!)
# ==============================================================================
def model_women_squash_sep25(n_trials=400000, seed=55693225):
    """
    EXACT FINAL FOUR LOCKED AFTER FRI SEP 25 QFs (EXHAUSTIVE: ONLY 4 PLAYERS REMAIN!):
      SF1 (Sat Sep 26): [1] Sivasangari Subramaniam (MAS, WR #5; def. Ho Tze Lok 11-8, 11-7, 11-8 in 25m)
                        vs [5] Chan Sin Yuk (HKG, WR #21; def. Aira Azman 10-12, 11-9, 11-5, 11-9 in 32m)
      SF2 (Sat Sep 26): [2] Satomi Watanabe (JPN, WR #6, home court; won QF)
                        vs [3] Anahat Singh (IND, WR #17; crushed Tanvi Khanna 11-2, 11-5, 11-3!)
      Final (Sun Sep 27): W(SF1) vs W(SF2)
    """
    rng = random.Random(seed)
    print("\n" + "=" * 80)
    print("MODEL 2: qid=556932 — Women's Singles Squash Gold (EXACT FINAL FOUR LOCKED!)")
    print("=" * 80)

    scenarios = [
        # (name, weight, siva_boost, siva_sd, wat_boost, wat_sd, anahat_boost, chan_boost, a_vs_w)
        ("S1: Base Posterior (Siva +40 sharp 25m; Wat +18 home; Anahat +15 clinical 10-pt QF; Chan +12)",
         0.50, 40.0, 48.0, 18.0, 46.0, 15.0, 12.0, 35.0),
        ("S2: Siva Dominant Form (+54 Elo; Wat +15; Anahat +10; Chan +8)",
         0.25, 54.0, 44.0, 15.0, 48.0, 10.0,  8.0, 30.0),
        ("S3: Watanabe Home Edge + Tighter SF Upsets (Siva +24 sd=56; Wat +28; Anahat +20; Chan +18)",
         0.25, 24.0, 56.0, 28.0, 44.0, 20.0, 18.0, 40.0),
    ]

    blend = Counter()
    sf1_siva_tot = 0.0
    sf2_wat_tot = 0.0
    fin_sw_siva = 0.0

    for sname, w, s_b, s_sd, w_b, w_sd, a_b, c_b, a_vs_w in scenarios:
        wins = Counter()
        sf1_siva = 0
        sf2_wat = 0
        sw_cnt = 0
        sw_siva = 0

        for _ in range(n_trials):
            siva = ("Sivasangari Subramaniam", rng.gauss(rank_to_elo(5)  + s_b, s_sd))
            chan = ("Chan Sin Yuk",            rng.gauss(rank_to_elo(21) + c_b, 50.0))
            wat  = ("Satomi Watanabe",         rng.gauss(rank_to_elo(6)  + w_b, w_sd))
            ana  = ("Anahat Singh",            rng.gauss(rank_to_elo(17) + a_b, 52.0))

            def play(p1, p2):
                e1, e2 = p1[1], p2[1]
                n1, n2 = p1[0], p2[0]
                if {n1, n2} == {"Anahat Singh", "Satomi Watanabe"}:
                    if n1 == "Anahat Singh": e1 += a_vs_w
                    else: e2 += a_vs_w
                elif {n1, n2} == {"Sivasangari Subramaniam", "Anahat Singh"}:
                    if n1 == "Sivasangari Subramaniam": e1 += 35.0
                    else: e2 += 35.0
                p1_w = 1.0 / (1.0 + 10.0 ** (-(e1 - e2) / 400.0))
                return p1 if rng.random() < p1_w else p2

            sf1 = play(siva, chan)
            sf2 = play(wat, ana)
            if sf1[0] == "Sivasangari Subramaniam": sf1_siva += 1
            if sf2[0] == "Satomi Watanabe": sf2_wat += 1
            champ = play(sf1, sf2)
            if sf1[0] == "Sivasangari Subramaniam" and sf2[0] == "Satomi Watanabe":
                sw_cnt += 1
                if champ[0] == "Sivasangari Subramaniam":
                    sw_siva += 1
            wins[champ[0]] += 1

        sf1_siva_tot += w * (sf1_siva / n_trials)
        sf2_wat_tot += w * (sf2_wat / n_trials)
        fin_sw_siva += w * (sw_siva / sw_cnt)

        print(f"\n  [{w:.2f}] {sname}")
        print(f"        P(Siva SF1)={sf1_siva/n_trials:.3f} | P(Wat SF2)={sf2_wat/n_trials:.3f} | P(Siva>Wat Final)={sw_siva/sw_cnt:.3f}")
        for nm in ["Sivasangari Subramaniam", "Satomi Watanabe", "Anahat Singh", "Chan Sin Yuk"]:
            p = wins[nm] / n_trials
            blend[nm] += w * p
            print(f"        {nm:26s}: {p:.4f}")

    print("\n  === FINAL BLENDED WOMEN'S SQUASH (vs Sep 24: Siva 0.55, Wat 0.35, Anahat 0.055, Chan 0.025, Aira 0.015 OUT!) ===")
    print(f"  Blended match probs: P(Siva SF1)={sf1_siva_tot:.3f} | P(Wat SF2)={sf2_wat_tot:.3f} | P(Siva>Wat Final)={fin_sw_siva:.3f}")
    for nm, p in sorted(blend.items(), key=lambda x: -x[1]):
        print(f"    {nm:26s}: {p:.4f}")
    print(f"  Exact 4-player sum = {sum(blend.values()):.4f}")


# ==============================================================================
# MODEL 3: qid=700005 — MEN'S SINGLES SQUASH GOLD (EXACT FINAL FOUR LOCKED!)
# ==============================================================================
def model_men_squash_sep25(n_trials=400000, seed=70000525):
    """
    EXACT FINAL FOUR & PAIRINGS LOCKED AFTER FRI SEP 25 QFs (EXHAUSTIVE: ONLY 4 PLAYERS REMAIN!):
      SF1 (Sat 16:15 JST): [1] Ng Eain Yow (MAS, WR #18; strolled past Alex Lau)
                           vs [3] Noor Zaman (PAK, WR #29; beat Henry Leung 11-7, 11-6, 3-11, 11-4 in 28m)
      SF2 (Sat 14:45 JST): [2] Abhay Singh (IND, WR #26; CRUSHED home #1 Tsukue 11-4, 11-3, 11-6!)
                           vs [5] Muhammad Ashab Irfan (PAK, WR #49; beat fatigued Chotrani 6-11, 11-8, 11-3, 11-3 in 41m)
      Final (Sun Sep 27): W(SF1) vs W(SF2)
    """
    rng = random.Random(seed)
    print("\n" + "=" * 80)
    print("MODEL 3: qid=700005 — Men's Singles Squash Gold (EXACT FINAL FOUR LOCKED!)")
    print("=" * 80)

    def match(a, b):
        p_a = 1.0 / (1.0 + 10.0 ** (-(a[1] - b[1]) / 400.0))
        return a if rng.random() < p_a else b

    regimes = [
        # (name, weight, eain_b, abhay_b, noor_b, ashab_b)
        ("R1: Base Post-QF (Eain Yow +22 defending champ/stroll; Abhay +16 crushed Tsukue; Noor +10; Ashab +18)",
         0.50, 22.0, 16.0, 10.0, 18.0),
        ("R2: Pedigree / Top-Seed Edge (Eain Yow +36; Abhay +20; Noor +6; Ashab +8 [Chotrani was exhausted])",
         0.25, 36.0, 20.0,  6.0,  8.0),
        ("R3: Pakistan Momentum / Tighter Field (Eain Yow +12; Abhay +10; Noor +22; Ashab +30)",
         0.25, 12.0, 10.0, 22.0, 30.0),
    ]

    blend = Counter()
    sf1_eain_tot = 0.0
    sf2_abh_tot = 0.0
    fin_ea_eain = 0.0

    for rname, w, eb, ab, nb, ib in regimes:
        wins = Counter()
        sf1_e = 0
        sf2_a = 0
        ea_cnt = 0
        ea_e = 0

        for _ in range(n_trials):
            eain = ("Ng Eain Yow",          rng.gauss(rank_to_elo(18) + eb, 46.0))
            noor = ("Noor Zaman",           rng.gauss(rank_to_elo(29) + nb, 50.0))
            abh  = ("Abhay Singh",          rng.gauss(rank_to_elo(26) + ab, 48.0))
            ash  = ("Muhammad Ashab Irfan", rng.gauss(rank_to_elo(49) + ib, 52.0))

            sf1 = match(eain, noor)
            sf2 = match(abh, ash)
            if sf1[0] == "Ng Eain Yow": sf1_e += 1
            if sf2[0] == "Abhay Singh": sf2_a += 1

            champ = match(sf1, sf2)
            if sf1[0] == "Ng Eain Yow" and sf2[0] == "Abhay Singh":
                ea_cnt += 1
                if champ[0] == "Ng Eain Yow":
                    ea_e += 1
            wins[champ[0]] += 1

        sf1_eain_tot += w * (sf1_e / n_trials)
        sf2_abh_tot += w * (sf2_a / n_trials)
        fin_ea_eain += w * (ea_e / ea_cnt)

        print(f"\n  [{w:.2f}] {rname}")
        print(f"        P(Eain>Noor SF1)={sf1_e/n_trials:.3f} | P(Abhay>Ashab SF2)={sf2_a/n_trials:.3f} | P(Eain>Abhay Final)={ea_e/ea_cnt:.3f}")
        for nm in ["Ng Eain Yow", "Abhay Singh", "Noor Zaman", "Muhammad Ashab Irfan"]:
            p = wins[nm] / n_trials
            blend[nm] += w * p
            print(f"        {nm:24s}: {p:.4f}")

    print("\n  === FINAL BLENDED MEN'S SQUASH (vs Sep 24: Eain 0.36, Abhay 0.195, Noor 0.155, Chotrani 0.075 OUT, Ashab 0.055) ===")
    print(f"  Blended match probs: P(Eain>Noor SF1)={sf1_eain_tot:.3f} | P(Abhay>Ashab SF2)={sf2_abh_tot:.3f} | P(Eain>Abhay Final)={fin_ea_eain:.3f}")
    for nm, p in sorted(blend.items(), key=lambda x: -x[1]):
        print(f"    {nm:24s}: {p:.4f}")
    print(f"  Exact 4-player sum = {sum(blend.values()):.4f}")


# ==============================================================================
# MODEL 4: qid=889545 — MEN'S FOOTBALL CHINA ELIMINATOR (POST QF1 & QF2!)
# ==============================================================================
def model_football_sep25(n_trials=200000, seed=20260925):
    """
    FRI SEP 25 QUARTERFINAL RESULTS:
      - QF1: Uzbekistan 3-0 Saudi Arabia -> Uzbekistan LOCKED IN SF1! (4W 0D 0L, 12-1 GD, 3 straight clean sheets!)
      - QF2: South Korea 4-0 Vietnam -> South Korea LOCKED IN SF2 (China's SF opponent if China beats Thailand)!
        Grasshopper FW Lee Young-jun scored brace + created Kim Ji-soo goal on first start!
    SAT SEP 26 REMAINING QFs:
      - QF3 (15:00 JST, Toyota): China (Wang Yudong suspended!) vs Thailand
      - QF4 (19:30 JST, Toyota): Japan (host, 12-0 in groups!) vs North Korea (beat Iran 4-1)
    WED SEP 30 SFs (Nagai Stadium, Osaka):
      - SF1: Uzbekistan vs W(Japan vs North Korea)
      - SF2: South Korea vs W(China vs Thailand)
    SAT OCT 3 Gold Medal Final (Toyota Stadium): W(SF1) vs W(SF2) [Bronze excluded per criteria!]
    """
    rng = np.random.default_rng(seed)

    def sim_match_goals(att_a, att_b, base_goals=1.20):
        diff = (att_a - att_b) / 100.0
        lam_a = base_goals * math.exp(0.28 * diff)
        lam_b = base_goals * math.exp(-0.28 * diff)
        return int(rng.poisson(lam_a)), int(rng.poisson(lam_b))

    def sim_ko(t1, t2, r1, r2, base_goals=1.18, et_goals=0.38):
        g1, g2 = sim_match_goals(r1, r2, base_goals=base_goals)
        if g1 != g2:
            return t1 if g1 > g2 else t2
        e1, e2 = sim_match_goals(r1, r2, base_goals=et_goals)
        if e1 != e2:
            return t1 if e1 > e2 else t2
        p1 = 0.5 + 0.03 * math.tanh((r1 - r2) / 150.0)
        return t1 if rng.random() < p1 else t2

    # Post-QF1/QF2 Bayesian rating upgrades:
    # - South Korea: 4-0 vs Vietnam with Lee Young-jun starting -> +15 to +20 Elo (1755-1765 base!)
    # - Uzbekistan: 3-0 vs rested Saudi Arabia (4W, 12-1 GD!) -> +15 to +20 Elo (1700-1705 base!)
    # - China, Thailand, Japan, North Korea unchanged from verified group-stage posteriors
    regimes = [
        ("R1: Base Post-QF1/2 (KOR 1758 w/ Lee Young-jun, JPN 1730+10h, UZB 1702, CHN 1590, PRK 1580, THA 1525)",
         0.42, 0.86, -20.0, 5.0,
         {"South Korea": 1758, "Japan": 1730, "Uzbekistan": 1702, "China": 1590, "North Korea": 1580, "Thailand": 1525}),
        ("R2: Wang Suspension Hits Harder / Thailand Sharp (CHN 1575 -28 Wang; THA 1545; KOR 1765)",
         0.24, 0.94, -28.0, 6.0,
         {"South Korea": 1765, "Japan": 1740, "Uzbekistan": 1705, "China": 1575, "North Korea": 1585, "Thailand": 1545}),
        ("R3: China Elite Low-Block Grit (CHN 1615 -15 Wang; c_def=0.76; KOR 1745)",
         0.22, 0.76, -15.0, 4.0,
         {"South Korea": 1745, "Japan": 1720, "Uzbekistan": 1695, "China": 1615, "North Korea": 1590, "Thailand": 1515}),
        ("R4: High-Variance Knockout / Tighter Field (KOR 1730, JPN 1715, UZB 1685, CHN 1585, PRK 1595, THA 1535)",
         0.12, 0.92, -20.0, 4.0,
         {"South Korea": 1730, "Japan": 1715, "Uzbekistan": 1685, "China": 1585, "North Korea": 1595, "Thailand": 1535}),
    ]

    total_elim = Counter()
    chn_beats_tha = 0.0
    kor_beats_chn_cond = 0.0
    uzb_makes_fin = 0.0
    jpn_makes_fin = 0.0

    for rname, w_reg, c_def, wang_pen, sf2_rest, base_r in regimes:
        elim = Counter()
        c_qf_w = 0
        k_sf_w = 0
        u_f = 0
        j_f = 0

        for _ in range(n_trials):
            r = {t: v + rng.normal(0, 25.0) for t, v in base_r.items()}

            # QF3 (Sat Sep 26): China (Wang Yudong suspended!) vs Thailand
            w_qf3 = sim_ko("China", "Thailand", r["China"] + wang_pen, r["Thailand"],
                           base_goals=1.18 * c_def * 0.94, et_goals=0.38 * c_def * 0.94)
            # QF4 (Sat Sep 26): Japan (+10 home) vs North Korea
            w_qf4 = sim_ko("Japan", "North Korea", r["Japan"] + 10.0, r["North Korea"])

            # SF1 (Wed Sep 30): Uzbekistan (+3 extra rest day) vs W(QF4)
            w_sf1 = sim_ko("Uzbekistan", w_qf4, r["Uzbekistan"] + 3.0, r[w_qf4] + (10.0 if w_qf4 == "Japan" else 0.0))
            if w_sf1 == "Uzbekistan": u_f += 1
            elif w_sf1 == "Japan": j_f += 1

            if w_qf3 != "China":
                elim["Thailand"] += 1
                continue
            c_qf_w += 1

            # SF2 (Wed Sep 30): China (Wang returns!) vs LOCKED South Korea (+sf2_rest + 4 fewer group match)
            w_sf2 = sim_ko("China", "South Korea", r["China"], r["South Korea"] + sf2_rest + 4.0,
                           base_goals=1.18 * c_def, et_goals=0.38 * c_def)
            if w_sf2 != "China":
                elim["South Korea"] += 1
                k_sf_w += 1
                continue

            # Final (Sat Oct 3): China vs W(SF1)
            opp_fin = w_sf1
            r_fin_opp = r[opp_fin] + (10.0 if opp_fin == "Japan" else 0.0)
            w_gold = sim_ko("China", opp_fin, r["China"], r_fin_opp,
                            base_goals=1.18 * c_def, et_goals=0.38 * c_def)
            if w_gold == "China":
                elim["None"] += 1
            else:
                elim[opp_fin] += 1

        chn_beats_tha += w_reg * (c_qf_w / n_trials)
        kor_beats_chn_cond += w_reg * (k_sf_w / c_qf_w)
        uzb_makes_fin += w_reg * (u_f / n_trials)
        jpn_makes_fin += w_reg * (j_f / n_trials)

        print(f"\n  [{w_reg:.2f}] {rname}")
        print(f"        P(CHN>THA)={c_qf_w/n_trials:.3f} | P(KOR>CHN|SF2)={k_sf_w/c_qf_w:.3f} | P(JPN Fin)={j_f/n_trials:.3f} | P(UZB Fin)={u_f/n_trials:.3f}")
        for k in ["Thailand", "South Korea", "Japan", "Uzbekistan", "None", "North Korea"]:
            p = elim[k] / n_trials
            total_elim[k] += w_reg * p
            print(f"        {k:16s}: {p:.4f}")

    print("\n" + "=" * 80)
    print("MODEL 4: qid=889545 — FINAL BLENDED FOOTBALL (vs Sep 24: THA 0.42, KOR 0.37, JPN 0.065, None 0.06, VIE 0.035 OUT!)")
    print("=" * 80)
    print(f"  Blended checkpoints: P(CHN>THA)={chn_beats_tha:.3f} | P(KOR>CHN|SF2)={kor_beats_chn_cond:.3f} | P(JPN Fin)={jpn_makes_fin:.3f} | P(UZB Fin)={uzb_makes_fin:.3f}")
    for k, p in total_elim.most_common(6):
        print(f"    {k:16s}: {p:.4f}")
    top5 = sum(p for _, p in total_elim.most_common(5))
    print(f"  Top-5 sum = {top5:.4f} (Outside = North Korea {total_elim['North Korea']:.4f})")


if __name__ == "__main__":
    model_pv_sindhu_sep25()
    model_women_squash_sep25()
    model_men_squash_sep25()
    model_football_sep25()
