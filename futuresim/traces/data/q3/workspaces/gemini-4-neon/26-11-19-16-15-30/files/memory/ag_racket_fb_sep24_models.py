"""
Quantitative Monte Carlo Models — Thu Sep 24, 2026
Batch: asian_games_racket_fb (4 questions)
  1. qid=259249: PV Sindhu Furthest Round in 2026 Asian Games Individual Badminton (EXACT DRAW RELEASED!)
  2. qid=556932: Asian Games Women's Singles Squash Gold (POST-R16 -> EXACT QF BRACKET!)
  3. qid=700005: Asian Games Men's Singles Squash Gold (POST-R16 -> 7/8 QFs LOCKED + BAYESIAN AL-TAMIMI!)
  4. qid=889545: Asian Games Men's Football China Eliminator (SF DATE SEP 30 REST-BONUS AUDIT!)
"""
import math
import random
from collections import Counter
import numpy as np


def rank_to_elo(r, scale=215.0):
    return 2300.0 - scale * math.log(r)


# ==============================================================================
# MODEL 1: qid=259249 — PV SINDHU FURTHEST ROUND (EXACT OFFICIAL DRAW SEP 24!)
# ==============================================================================
def model_pv_sindhu_sep24(n_trials=300000, seed=25924924):
    """
    CONFIRMED EXACT DRAW (Indian Express, Outlook India, PTI/ThePrint, HT Sep 24):
      - R64 (Fri Sep 25): BYE!
      - R32 (Sat Sep 26, 06:00 IST): Winner of Chiu Pin-chian (TPE, WR ~#13) vs Letshanaa Karupathevan (MAS)
      - R16 (Sat Sep 26, 12:30 IST — SAME-DAY DOUBLEHEADER): [7] Tomoka Miyazaki (JPN, WR #7, home court)
      - QF  (Sun Sep 27, 09:30 IST): [4] Chen Yufei (CHN, WR #4, Tokyo Olympic champion)
      - SF  (Mon Sep 28, 09:30 IST): [1] An Se-young (KOR, WR #1, 51-1 in 2026, 10-0 H2H vs Sindhu!)
      - Final (Tue Sep 29, 07:30 IST): Winner of bottom half (Wang Zhiyi / Akane Yamaguchi / Putri etc.)

    KEY MATCHUP & FATIGUE FACTORS:
      - R32: Sindhu rested 3 full days (since Tue Sep 22) while Chiu/Letshanaa play Fri R64.
        Chiu Pin-chian is WR #13 (solid Top-15 player!) -> NOT a free win (~74% base for Sindhu vs Chiu, ~91% vs Letshanaa).
      - R16: SAME-DAY DOUBLEHEADER (~6.5h after R32)! Sindhu leads Miyazaki 2-1 H2H (crushed her 21-8, 21-13
        at Malaysia Open Jan 2026), AND Miyazaki played Team QF Tue + Team SF Wed + Team Final Thu (China 3-0 Japan).
        HOWEVER: Miyazaki is WR #7, plays at home in Nagoya, looked sharp beating Unnati Hooda & Sim Yu-jin 2-0,
        and Indian Express explicitly noted Sindhu's endurance fade in G3 vs Yamaguchi (11-21).
        Plus: if Sindhu gets dragged into a grueling R32 morning match vs Chiu, R16 fatigue hits harder!
      - QF: Chen Yufei leads H2H 8-6/9-7 (won 5 straight completed matches incl. 2026 Indonesia Masters 21-13, 21-17;
        Sindhu's 2026 Japan Open SF win over Chen was a WALKOVER!). Healthy enough to win Women's Team gold 3-0 Thu.
      - SF: An Se-young is LOCKED into Sindhu's semifinal half! 51-1 in 2026, 10-0 H2H vs Sindhu!
    """
    rng = random.Random(seed)
    print("=" * 80)
    print("MODEL 1: qid=259249 — PV Sindhu Furthest Round (EXACT DRAW SEP 24)")
    print("=" * 80)

    def logit(p):
        p = min(0.995, max(0.005, p))
        return math.log(p / (1.0 - p))

    def inv_logit(x):
        return 1.0 / (1.0 + math.exp(-x))

    # Multi-regime blend spanning tournament form / doubleheader stamina uncertainty:
    # (name, weight, p_chiu_wins_r64, p_vs_chiu, p_vs_letsh, p_miy_reaches, p_vs_miy, p_chen_reaches, p_vs_chen, p_an_reaches, p_vs_an)
    regimes = [
        (
            "R1: Base Post-Draw (rested R32, coin-flip+ R16 vs Miyazaki, underdog vs Chen, longshot vs An)",
            0.45,
            0.80, 0.74, 0.91,
            0.87, 0.52,
            0.88, 0.31,
            0.93, 0.06,
        ),
        (
            "R2: Peak Japan-Open Sindhu (crushes Miyazaki again, threatens Chen Yufei, Miyazaki fatigued from Team Final)",
            0.30,
            0.80, 0.81, 0.94,
            0.84, 0.62,
            0.85, 0.40,
            0.91, 0.09,
        ),
        (
            "R3: Endurance Drag / Tough Home Doubleheader (Chiu grinder + home Miyazaki + dominant Chen/An)",
            0.25,
            0.80, 0.66, 0.86,
            0.90, 0.39,
            0.91, 0.22,
            0.95, 0.03,
        ),
    ]

    blend = Counter()
    for rname, w, p_chiu, p_vs_c, p_vs_l, p_miy_r, p_vs_m, p_chen_r, p_vs_ch, p_an_r, p_vs_a in regimes:
        counts = Counter()
        for _ in range(n_trials):
            # 0.5% pre-R32 freak withdrawal/DNS
            if rng.random() < 0.005:
                counts["Outside_DNS"] += 1
                continue

            # Correlated tournament-level form shock in log-odds space (sd=0.28 ~ +/-6-7% at p=0.5)
            form_lo = rng.gauss(0.0, 0.28)

            # R32 (Sat morning)
            opp_r32_is_chiu = rng.random() < p_chiu
            base_r32 = p_vs_c if opp_r32_is_chiu else p_vs_l
            p_r32 = inv_logit(logit(base_r32) + form_lo)
            if rng.random() > p_r32:
                counts["Round of 32"] += 1
                continue

            # Extra afternoon fatigue if Chiu forced a tight 3-gamer (~35% conditional on beating Chiu)
            r32_fatigue_lo = -0.18 if (opp_r32_is_chiu and rng.random() < 0.35) else 0.0

            # R16 (Sat afternoon, 6.5h later)
            if rng.random() < p_miy_r:
                p_r16 = inv_logit(logit(p_vs_m) + form_lo + r32_fatigue_lo)
            else:
                # Miyazaki upset in R32 -> weaker R16 opponent (~78% base)
                p_r16 = inv_logit(logit(0.78) + form_lo + r32_fatigue_lo)
            if rng.random() > p_r16:
                counts["Round of 16"] += 1
                continue

            # QF (Sun morning)
            if rng.random() < p_chen_r:
                p_qf = inv_logit(logit(p_vs_ch) + form_lo)
            else:
                p_qf = inv_logit(logit(0.65) + form_lo)
            if rng.random() > p_qf:
                counts["Quarterfinals"] += 1
                continue

            # SF (Mon morning)
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

    print("\n  === FINAL BLENDED PV SINDHU PROBABILITIES (vs Sep 23: QF 0.38, R16 0.27, SF 0.15, R32 0.13, Final 0.06) ===")
    for k in ["Round of 16", "Quarterfinals", "Round of 32", "Semifinals", "Final", "Outside_DNS"]:
        print(f"    {k:16s}: {blend[k]:.4f}")
    top5 = sum(blend[k] for k in ["Round of 16", "Quarterfinals", "Round of 32", "Semifinals", "Final"])
    print(f"  Top-5 sum = {top5:.4f}")


# ==============================================================================
# MODEL 2: qid=556932 — WOMEN'S SINGLES SQUASH GOLD (POST-R16 EXACT QFs!)
# ==============================================================================
def model_women_squash_sep24(n_trials=300000, seed=55693224):
    """
    VERIFIED THU SEP 24 R16 RESULTS & FRI SEP 25 EXACT QFs (The Star, Bernama, HT, Outlook):
      TOP HALF (100% LOCKED):
        QF1: [1] Sivasangari Subramaniam (MAS, WR #5; 17m 3-0 win!) vs Ho Tze Lok (HKG, WR #39!)
        QF2: [4] Aira Azman (MAS, WR #24; 3-0 w/ G3 dip)            vs Chan Sin Yuk (HKG, WR #21; beat Aira at AG22 QF!)
      BOTTOM HALF (3 of 4 LOCKED):
        QF3: [3] Anahat Singh (IND, WR #17; 19m 3-0 win!)           vs [7] Tanvi Khanna (IND, WR #71; 39m 3-1 win)
        QF4: [2] Satomi Watanabe (JPN, WR #6; p_alive=0.985)        vs Bottom QF4 opp (~WR #55 Akari Midorikawa / field)
    """
    rng = random.Random(seed)
    print("\n" + "=" * 80)
    print("MODEL 2: qid=556932 — Women's Singles Squash Gold (POST-R16 EXACT QFs)")
    print("=" * 80)

    scenarios = [
        # (name, weight, siva_boost, siva_sd, wat_boost, wat_sd, wat_alive, anahat_boost, a_vs_w)
        ("S1: Base Posterior (Siva +42 peak Doha+17m sharp; Wat +18 home; Anahat WR#17 +12)", 0.50, 42.0, 50.0, 18.0, 48.0, 0.985, 12.0, 35.0),
        ("S2: Siva Dominant Form (+55 Elo; mild travel drag; Wat +15)",                       0.25, 55.0, 46.0, 15.0, 50.0, 0.988,  8.0, 30.0),
        ("S3: Watanabe Home Edge (Siva +25 Elo, wider sd=60; Wat +28 home; Anahat +18)",      0.25, 25.0, 60.0, 28.0, 45.0, 0.985, 18.0, 40.0),
    ]

    blend = Counter()
    for sname, w, s_b, s_sd, w_b, w_sd, w_alive, a_b, a_vs_w in scenarios:
        wins = Counter()
        for _ in range(n_trials):
            siva = ("Sivasangari Subramaniam", rng.gauss(rank_to_elo(5) + s_b, s_sd))
            ho   = ("Ho Tze-Lok",              rng.gauss(rank_to_elo(39), 52.0))
            aira = ("Aira Azman",              rng.gauss(rank_to_elo(24), 52.0))
            chan = ("Chan Sin Yuk",            rng.gauss(rank_to_elo(21) + 10.0, 52.0))  # beat Aira at AG22 QF
            ana  = ("Anahat Singh",            rng.gauss(rank_to_elo(17) + a_b, 55.0))
            tanv = ("Tanvi Khanna",            rng.gauss(rank_to_elo(71), 52.0))
            wat  = ("Satomi Watanabe",         rng.gauss(rank_to_elo(6) + w_b, w_sd)) if rng.random() < w_alive else ("QF4_Upsetter", rng.gauss(rank_to_elo(65), 55.0))
            mido = ("Akari Midorikawa",        rng.gauss(rank_to_elo(55) + 15.0, 55.0))

            def play(p1, p2):
                e1, e2 = p1[1], p2[1]
                n1, n2 = p1[0], p2[0]
                if {n1, n2} == {"Anahat Singh", "Satomi Watanabe"}:
                    if n1 == "Anahat Singh": e1 += a_vs_w
                    else: e2 += a_vs_w
                elif {n1, n2} == {"Sivasangari Subramaniam", "Anahat Singh"}:
                    if n1 == "Sivasangari Subramaniam": e1 += 35.0
                    else: e2 += 35.0
                elif {n1, n2} == {"Sivasangari Subramaniam", "Aira Azman"}:
                    if n1 == "Sivasangari Subramaniam": e1 += 25.0
                    else: e2 += 25.0
                p1_w = 1.0 / (1.0 + 10.0 ** (-(e1 - e2) / 400.0))
                return p1 if rng.random() < p1_w else p2

            qf1 = play(siva, ho)
            qf2 = play(aira, chan)
            qf3 = play(ana, tanv)
            qf4 = play(wat, mido)
            sf1 = play(qf1, qf2)
            sf2 = play(qf3, qf4)
            champ = play(sf1, sf2)
            wins[champ[0]] += 1

        print(f"\n  [{w:.2f}] {sname}")
        for nm in ["Sivasangari Subramaniam", "Satomi Watanabe", "Anahat Singh", "Chan Sin Yuk", "Aira Azman", "Ho Tze-Lok"]:
            p = wins[nm] / n_trials
            blend[nm] += w * p
            print(f"        {nm:26s}: {p:.4f}")

    print("\n  === FINAL BLENDED WOMEN'S SQUASH (vs Sep 23: Siva 0.54, Wat 0.36, Anahat 0.04, Aira 0.03, Chan 0.015) ===")
    for nm, p in sorted(blend.items(), key=lambda x: -x[1])[:7]:
        print(f"    {nm:26s}: {p:.4f}")
    top5 = sum(p for _, p in sorted(blend.items(), key=lambda x: -x[1])[:5])
    print(f"  Top-5 sum = {top5:.4f}")


# ==============================================================================
# MODEL 3: qid=700005 — MEN'S SINGLES SQUASH GOLD (POST-R16: 7/8 QFs LOCKED!)
# ==============================================================================
def model_men_squash_sep24(n_trials=300000, seed=70000524):
    """
    VERIFIED THU SEP 24 R16 RESULTS & FRI SEP 25 QFs (The Star, HT, Express Tribune):
      QF-A: [1] Ng Eain Yow (MAS, WR #18; 11-3, 11-4, 11-5)          vs Alex Lau / Lau Tsz Kwan (HKG, WR #44)
      QF-B: [4] Veer Chotrani (IND, WR #38; 77-min 3-2 war vs Jeeva) vs [5] Muhammad Ashab Irfan (PAK, WR #49; 3-0 win)
      QF-C: [2] Abhay Singh (IND, WR #26; 11-3, 11-5, 11-6)          vs Ryunosuke Tsukue (JPN, WR #48; home court)
      QF-D: [3] Noor Zaman (PAK, WR #29; 11-4, 11-9, 11-4)           vs [8] Henry Leung (HKG, WR #54) OR [10] Abdulla Al-Tamimi (QAT)

    BAYESIAN POSTERIOR ON ABDULLA AL-TAMIMI BEING ALIVE IN QF-D:
      - Of the 4 open R16 slots from Sep 23 (#1 Eain Yow, #6 Alex Lau, #7 Tsukue, #8 Henry Leung):
        * #1 Eain Yow played Ryu Jeong-min (NOT Al-Tamimi!)
        * #6 Alex Lau WON his R16 (so if Al-Tamimi was there, Al-Tamimi LOST!)
        * #7 Tsukue WON his R16 (so if Al-Tamimi was there, Al-Tamimi LOST!)
        * ONLY #8 Henry Leung's R16 slot is unobserved!
      - Plus ZERO Qatar press coverage of Al-Tamimi across Sep 18-24 (even on R32 & R16 days!).
      - Exact Bayes update across prior p_enter in {0.55, 0.70, 0.85}:
    """
    print("\n" + "=" * 80)
    print("MODEL 3: qid=700005 — Men's Singles Squash Gold (POST-R16 + BAYESIAN AL-TAMIMI)")
    print("=" * 80)

    # Exact Bayes calculation for P(Al-Tamimi is alive in QF-D vs Noor Zaman)
    for p_enter in [0.55, 0.70, 0.85]:
        # Given Al-Tamimi entered & reached R16, equally likely in 1 of 3 non-Eain-Yow open slots: {Lau, Tsukue, Leung}
        # P(Lau wins vs weak)=0.90, P(Tsukue wins vs weak)=0.90
        # P(Lau beats Tamimi)=0.36, P(Tsukue beats Tamimi)=0.34, P(Tamimi beats Leung)=0.74
        l_no_enter = (1.0 - p_enter) * (0.90 * 0.90)
        l_vs_lau_lost = p_enter * (1/3) * 0.36 * 0.90
        l_vs_tsu_lost = p_enter * (1/3) * 0.34 * 0.90
        l_vs_leu_lost = p_enter * (1/3) * 0.26 * (0.90 * 0.90)
        l_vs_leu_won  = p_enter * (1/3) * 0.74 * (0.90 * 0.90)
        post_alive = l_vs_leu_won / (l_no_enter + l_vs_lau_lost + l_vs_tsu_lost + l_vs_leu_lost + l_vs_leu_won)
        print(f"  Bayes P(Al-Tamimi alive in QF-D | p_enter={p_enter:.2f}) = {post_alive:.4f}")

    # Blended posterior across prior participation uncertainty: ~0.245 (test 0.20, 0.25, 0.31)
    rng = random.Random(seed)

    def draw_tamimi_elo():
        # If Al-Tamimi IS alive and just beat Henry Leung, condition slightly upward on healthy/solid states!
        u = rng.random()
        if u < 0.42:
            return rng.gauss(rank_to_elo(20) + 15.0, 52.0)
        elif u < 0.85:
            return rng.gauss(rank_to_elo(32), 52.0)
        else:
            return rng.gauss(rank_to_elo(54), 52.0)

    def match(a, b):
        p_a = 1.0 / (1.0 + 10.0 ** (-(a[1] - b[1]) / 400.0))
        return a if rng.random() < p_a else b

    regimes = [
        # (name, weight, p_tamimi_alive, chotrani_qf_fatigue, tsukue_home_bonus)
        ("R1: Base Post-R16 (P_Tamimi=0.24, Chotrani 77m fatigue -22 Elo in QF, Tsukue +22 home)", 0.50, 0.24, -22.0, 22.0),
        ("R2: Al-Tamimi Lower / Heavy Chotrani Fatigue (P_Tamimi=0.16, Chotrani -30 Elo, Tsukue +25)", 0.25, 0.16, -30.0, 25.0),
        ("R3: Al-Tamimi Higher / Mild Chotrani Fatigue (P_Tamimi=0.32, Chotrani -12 Elo, Tsukue +16)", 0.25, 0.32, -12.0, 16.0),
    ]

    blend = Counter()
    for rname, w, p_tam, cho_fat, tsu_home in regimes:
        wins = Counter()
        for _ in range(n_trials):
            # Updated PSA rankings from Thu Sep 24 reports:
            # Eain Yow #18 (+20 sharp clinical), Abhay #26 (HT explicitly cites WR #26, clinical 3-0),
            # Noor Zaman #29 (+10 sharp), Veer Chotrani #38 (survived 77m war), Ashab Irfan #49 (+10 clinical 3-0),
            # Alex Lau #44 (+18 experienced Asian champ), Tsukue #48 (+home), Henry Leung #54
            eain = ("Ng Eain Yow",          rng.gauss(rank_to_elo(18) + 20.0, 48.0))
            lau  = ("Alex Lau",             rng.gauss(rank_to_elo(44) + 18.0, 52.0))
            cho  = ("Veer Chotrani",        rng.gauss(rank_to_elo(38), 52.0))
            ash  = ("Muhammad Ashab Irfan", rng.gauss(rank_to_elo(49) + 12.0, 54.0))
            abh  = ("Abhay Singh",          rng.gauss(rank_to_elo(26) + 8.0,  50.0))
            tsu  = ("Ryunosuke Tsukue",     rng.gauss(rank_to_elo(48) + tsu_home, 52.0))
            noor = ("Noor Zaman",           rng.gauss(rank_to_elo(29) + 10.0, 52.0))

            if rng.random() < p_tam:
                qfd_opp = ("Abdulla Al-Tamimi", draw_tamimi_elo())
            else:
                qfd_opp = ("Henry Leung", rng.gauss(rank_to_elo(54), 52.0))

            # QF matches (Chotrani gets 1-match QF fatigue penalty from 77-min 5-gamer on Thu!)
            w_qfa = match(eain, lau)
            w_qfb = match((cho[0], cho[1] + cho_fat), ash)
            # Restore Chotrani rating if he survives QF (overnight recovery, minor residual -6)
            if w_qfb[0] == "Veer Chotrani":
                w_qfb = (cho[0], cho[1] - 6.0)
            w_qfc = match(abh, tsu)
            w_qfd = match(noor, qfd_opp)

            # 50/50 split on whether 3/4 seed Noor or Chotrani is in #1 Eain Yow's half vs #2 Abhay's half
            if rng.random() < 0.50:
                sf1 = match(w_qfa, w_qfb)
                sf2 = match(w_qfc, w_qfd)
            else:
                sf1 = match(w_qfa, w_qfd)
                sf2 = match(w_qfc, w_qfb)

            champ = match(sf1, sf2)
            wins[champ[0]] += 1

        print(f"\n  [{w:.2f}] {rname}")
        for nm, c in wins.most_common(9):
            p = c / n_trials
            blend[nm] += w * p
            print(f"        {nm:24s}: {p:.4f}")

    print("\n  === FINAL BLENDED MEN'S SQUASH (vs Sep 23: Eain Yow 0.31, Abhay 0.20, Noor 0.15, Tamimi 0.08, Chotrani 0.07) ===")
    for nm, p in sorted(blend.items(), key=lambda x: -x[1])[:9]:
        print(f"    {nm:24s}: {p:.4f}")
    top5 = sum(p for _, p in sorted(blend.items(), key=lambda x: -x[1])[:5])
    print(f"  Top-5 sum = {top5:.4f} (Outside = {1 - top5:.4f})")


# ==============================================================================
# MODEL 4: qid=889545 — MEN'S FOOTBALL AUDIT (SEP 30 SF -> REDUCED REST GAP!)
# ==============================================================================
def model_football_sep24_audit(n_trials=150000, seed=20260924):
    """
    Korea Times (Sep 22) confirms:
      - QFs: Fri Sep 25 (UZB-KSA, KOR-VIE) & Sat Sep 26 (CHN-THA, JPN-PRK)
      - SFs: Wed Sep 30 in Osaka (4 FULL rest days after Sat QF3 vs 5 days after Fri QF2!)
      - Final: Sat Oct 3 at Toyota Stadium
    Check exact sensitivity of reducing the Sep 23 sf2_rest bonus (+15 -> +4) and Group D SF bonus (+8 -> +4)!
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

    regimes = [
        ("R1", 0.40, 0.86, -20.0, 4.0, {"South Korea": 1740, "Japan": 1730, "Uzbekistan": 1685, "Saudi Arabia": 1610, "China": 1590, "North Korea": 1580, "Thailand": 1525, "Vietnam": 1515}),
        ("R2", 0.25, 0.94, -28.0, 5.0, {"South Korea": 1745, "Japan": 1740, "Uzbekistan": 1685, "Saudi Arabia": 1610, "China": 1575, "North Korea": 1585, "Thailand": 1545, "Vietnam": 1520}),
        ("R3", 0.22, 0.76, -15.0, 3.0, {"South Korea": 1730, "Japan": 1720, "Uzbekistan": 1680, "Saudi Arabia": 1605, "China": 1615, "North Korea": 1590, "Thailand": 1515, "Vietnam": 1510}),
        ("R4", 0.13, 0.92, -20.0, 3.0, {"South Korea": 1715, "Japan": 1710, "Uzbekistan": 1665, "Saudi Arabia": 1615, "China": 1585, "North Korea": 1595, "Thailand": 1535, "Vietnam": 1540}),
    ]

    total_elim = Counter()
    for _, w_reg, c_def, wang_pen, sf2_rest, base_r in regimes:
        elim = Counter()
        for _ in range(n_trials):
            r = {t: v + rng.normal(0, 26.0) for t, v in base_r.items()}
            r_qf = dict(r)
            r_qf["South Korea"] += 15.0
            r_qf["Saudi Arabia"] += 15.0
            # Host Japan slight home bump (+10)
            r_qf["Japan"] += 10.0

            w_qf1 = sim_ko("Uzbekistan", "Saudi Arabia", r_qf["Uzbekistan"], r_qf["Saudi Arabia"])
            w_qf2 = sim_ko("South Korea", "Vietnam", r_qf["South Korea"], r_qf["Vietnam"])
            w_qf3 = sim_ko("China", "Thailand", r_qf["China"] + wang_pen, r_qf["Thailand"], base_goals=1.18 * c_def * 0.94, et_goals=0.38 * c_def * 0.94)
            w_qf4 = sim_ko("Japan", "North Korea", r_qf["Japan"], r_qf["North Korea"])

            # SF1 (Sep 30): 4 vs 5 rest days -> minimal rest edge (+3)
            r_sf1_a = r[w_qf1] + 3.0 + (4.0 if w_qf1 == "Saudi Arabia" else 0.0)
            r_sf1_b = r[w_qf4] + (10.0 if w_qf4 == "Japan" else 0.0)
            w_sf1 = sim_ko(w_qf1, w_qf4, r_sf1_a, r_sf1_b)

            if w_qf3 != "China":
                elim["Thailand"] += 1
                continue

            # SF2 (Sep 30): China (Wang Yudong returns!) vs W(QF2)
            opp_sf2 = w_qf2
            r_opp_sf2 = r[opp_sf2] + sf2_rest + (4.0 if opp_sf2 == "South Korea" else 0.0)
            w_sf2 = sim_ko("China", opp_sf2, r["China"], r_opp_sf2, base_goals=1.18 * c_def, et_goals=0.38 * c_def)
            if w_sf2 != "China":
                elim[opp_sf2] += 1
                continue

            # Final (Oct 3)
            opp_fin = w_sf1
            r_fin_opp = r[opp_fin] + (10.0 if opp_fin == "Japan" else 0.0)
            w_gold = sim_ko("China", opp_fin, r["China"], r_fin_opp, base_goals=1.18 * c_def, et_goals=0.38 * c_def)
            if w_gold == "China":
                elim["None"] += 1
            else:
                elim[opp_fin] += 1

        for k, v in elim.items():
            total_elim[k] += w_reg * (v / n_trials)

    print("\n" + "=" * 80)
    print("MODEL 4: qid=889545 — Football Audit w/ Sep 30 SF (vs Sep 23: THA 0.42, KOR 0.37, JPN 0.065, None 0.06, VIE 0.035)")
    print("=" * 80)
    for k, p in total_elim.most_common(8):
        print(f"    {k:18s}: {p:.4f}")


if __name__ == "__main__":
    model_pv_sindhu_sep24()
    model_women_squash_sep24()
    model_men_squash_sep24()
    model_football_sep24_audit()
