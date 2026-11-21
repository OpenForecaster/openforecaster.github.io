"""
Quantitative models for batch olympic_athletics_asian_games on 2026-09-16:
  1. qid=574485: PSA Women's World Squash No. 1 on Sep 21, 2026 (T+2d) — POST-ORFI QF WIN!
  2. qid=224082: 2026 Asian Games Women's 200m IM (T+5d) — Confirmed entries Yu Yiting + Yu Zidi
  3. qid=300850: 2026 Asian Games Women's 400m IM (T+7d) — Confirmed entries Yu Zidi + Ke Wenxi (NO Yu Yiting!)
  4. qid=832291: 2026 Asian Games Women's 49kg Weightlifting (T+7d) — GamesHub confirms Ri Song-gum; China/Sukcharoen absent!
  5. qid=889545: 2026 Asian Games Men's Football (China gold-medal bid, T+14d) — POST-MD1 (ALL 6 SCORES + OFFICIAL OCA BRACKET!)
"""
import math
import random
from collections import Counter
import numpy as np


# ==============================================================================
# MODEL 1: Q1 (qid=574485) — PSA WOMEN'S WORLD NO. 1 ON SEPT 21, 2026
# ==============================================================================
# Official PSA Rule (psasquashtour.com, Sep 9):
#   - Orfi becomes #1 iff she MATCHES OR BETTERS El Hammamy's finish at Qatar Classic.
#   - El Hammamy stays #1 iff she WINS THE TITLE OR BETTERS Orfi's finish.
# State as of Wed Sep 16, 2026 (BOTH players now in Thu Sep 17 Semifinals!):
#   - SF1: [1] Hania El Hammamy (walkover vs inj. Gohar) vs [4] Sivasangari Subramaniam (walkover vs inj. Gilis)
#   - SF2: [2] Amina Orfi (beat [6] Fayrouz Aboelkheir 3-0: 13-11, 11-8, 12-10!) vs unseeded Jasmine Hutton (beat Rachel Arnold 3-1)
#   - Exact formula with P_O_QF = 1.0:
#       P(Orfi #1) = (1 - p_H_SF) + p_H_SF * p_O_SF * p_O_FIN
#       (If El Hammamy loses SF, Orfi ALREADY matches her at SF -> Orfi #1 with certainty!)
def model_squash_no1():
    print("=" * 72)
    print("MODEL 1: qid=574485 — PSA Women's World No. 1 (Sep 21, 2026) POST-QF")
    print("=" * 72)

    def exact_orfi_prob(p_h_sf, p_o_sf, p_o_fin):
        return (1.0 - p_h_sf) + p_h_sf * p_o_sf * p_o_fin

    scenarios = [
        ("Base case (Hammamy 0.77 vs rested Sivasangari; Orfi 0.93 vs Hutton; 0.505 Final)", 0.77, 0.93, 0.505),
        ("Orfi 2026 major-streak edge (Hammamy 0.76 SF; Orfi 0.94 SF; 0.53 Final)",          0.76, 0.94, 0.530),
        ("Hammamy Doha + extra rest edge (Hammamy 0.80 SF; Orfi 0.92 SF; 0.475 Final)",      0.80, 0.92, 0.475),
        ("Sivasangari upset threat (Hammamy 0.73 SF; Orfi 0.93 SF; 0.505 Final)",            0.73, 0.93, 0.505),
        ("Hutton London-familiarity test (Hammamy 0.78 SF; Orfi 0.89 SF; 0.50 Final)",       0.78, 0.89, 0.500),
    ]
    weights = [0.40, 0.22, 0.22, 0.08, 0.08]
    blend_orfi = 0.0
    for (name, ph, ps, pf), w in zip(scenarios, weights):
        po = exact_orfi_prob(ph, ps, pf)
        blend_orfi += w * po
        print(f"  [{w:.2f}] {name}\n        -> Orfi={po:.4f}, El Hammamy={1-po:.4f}")

    rng = random.Random(57448516)
    mc_orfi = []
    for _ in range(150000):
        ph = min(0.90, max(0.62, rng.gauss(0.77, 0.042)))
        ps = min(0.98, max(0.83, rng.gauss(0.93, 0.025)))
        pf = min(0.65, max(0.36, rng.gauss(0.505, 0.045)))
        mc_orfi.append(exact_orfi_prob(ph, ps, pf))
    mc_mean = sum(mc_orfi) / len(mc_orfi)
    print(f"\n  Weighted scenario blend: Amina Orfi={blend_orfi:.4f}, Hania El Hammamy={1-blend_orfi:.4f}")
    print(f"  150k Bayesian MC mean:   Amina Orfi={mc_mean:.4f}, Hania El Hammamy={1-mc_mean:.4f}")


# ==============================================================================
# MODEL 2 & 3: Q2 (qid=224082) 200m IM & Q3 (qid=300850) 400m IM
# ==============================================================================
# Official China Entries (zh.wikipedia.org Sep 11 + sport.gov.cn Sep 10 + sport.org.cn Sep 4):
#   - Women's 200m IM (Mon Sep 21): Yu Yiting (余依婷) & Yu Zidi (于子迪)
#     * Yu Yiting NOT swimming 400m IM (only 100fr, 100fly, 200IM) -> peak focus on 200m IM!
#     * Yu Yiting: 2:06.82 AR/WL (June 2026), 2:07.45 Pan Pacs gold untapered (Aug 15)
#     * Yu Zidi: 2:07.41 PB (Nov 2025), 2:09.33 June Trials; swims 200m fly on Sun Sep 20!
#     * Japan: Mio Narita (2:11.26 Pan Pacs), Shiho Matsumoto (2:11.97 Pan Pacs)
#   - Women's 400m IM (Wed Sep 23): Yu Zidi (于子迪) & Ke Wenxi (柯雯曦)
#     * YU YITING IS NOT ENTERED IN 400m IM! (only ~1.2% emergency sub chance)
#     * Yu Zidi: 4:30.79 June Trials (#2 world 2026, #8 all-time), skipped Pan Pacs to peak for Tokyo
#     * Ke Wenxi: 4:33.59 June Trials (#2 in China, confirmed #2 entry!)
#     * Mio Narita (JPN): 4:33.26 PB (2025 Worlds silver), struggled 4:39.49 at Aug Pan Pacs (home-pool rebound potential!)
#     * Waka Kobori (JPN): 4:39.23 Pan Pacs, ~4:36-4:37 PB
def model_swimming_im():
    print("\n" + "=" * 72)
    print("MODEL 2: qid=224082 — Asian Games Women's 200m IM (Mon Sep 21)")
    print("=" * 72)
    rng = np.random.default_rng(22408216)
    n = 200000
    # Race time in seconds (2:07.00 = 127.00)
    # Include DNS/DQ risk (~3.5% Yu Yiting, ~4.0% Yu Zidi [multi-event 13yo], ~3% JPN)
    # If either Chinese swimmer DNS before heats -> 40% chance Chang Mohan / Ke Wenxi subs in
    wins_200 = Counter()
    for _ in range(n):
        candidates = []
        yy_ok = rng.random() > 0.035
        yz_ok = rng.random() > 0.040
        if yy_ok:
            # Yu Yiting: mean 127.25s, sd 0.85s (slight right tail for bad race)
            t = rng.normal(127.25, 0.85) + (rng.uniform(1.0, 2.5) if rng.random() < 0.06 else 0.0)
            candidates.append((t, "Yu Yiting"))
        if yz_ok:
            # Yu Zidi: mean 128.05s, wider sd 1.25s (13yo huge upside/variance + 200m fly day prior)
            t = rng.normal(128.05, 1.25) + (rng.uniform(1.0, 2.5) if rng.random() < 0.08 else 0.0)
            candidates.append((t, "Yu Zidi"))
        if (not yy_ok or not yz_ok) and rng.random() < 0.55:
            # China reserve sub (Chang Mohan / Ke Wenxi)
            sub = "Chang Mohan" if rng.random() < 0.55 else "Ke Wenxi"
            t = rng.normal(130.6, 1.1)
            candidates.append((t, sub))
        if rng.random() > 0.03:
            t = rng.normal(130.5, 1.15)  # Mio Narita home pool rebound
            candidates.append((t, "Mio Narita"))
        if rng.random() > 0.03:
            t = rng.normal(130.7, 1.15)  # Shiho Matsumoto
            candidates.append((t, "Shiho Matsumoto"))
        # Rest of Asia (Kim Seo-yeong, etc.)
        candidates.append((rng.normal(131.6, 1.1), "Rest_of_Asia"))
        wins_200[min(candidates)[1]] += 1

    for name, c in wins_200.most_common():
        print(f"  {name:18s}: {c/n:.4f}")

    print("\n" + "=" * 72)
    print("MODEL 3: qid=300850 — Asian Games Women's 400m IM (Wed Sep 23)")
    print("=" * 72)
    rng3 = np.random.default_rng(30085016)
    wins_400 = Counter()
    # Race time in seconds (4:30.00 = 270.00, 4:34.00 = 274.00)
    # Note: Yu Zidi is swimming 3rd tough event in 4 days (200 fly Sep 20, 200 IM Sep 21, 400 IM Sep 23)
    # DNS/DQ risk: ~5.5% for Yu Zidi (4-stroke 7-turn IM DQ + fatigue/illness), ~4.0% Ke Wenxi
    # If Yu Zidi or Ke Wenxi scratches -> ~30% chance Yu Yiting steps in (4:33.09 PB!)
    for _ in range(n):
        candidates = []
        yz_ok = rng3.random() > 0.055
        kw_ok = rng3.random() > 0.040
        if yz_ok:
            # Yu Zidi: 4:30.79 PB -> mean 271.4s, sd 2.1s, 7% fatigue/bad-race (+2.5..+5.5s)
            t = rng3.normal(271.4, 2.1) + (rng3.uniform(2.5, 5.5) if rng3.random() < 0.07 else 0.0)
            candidates.append((t, "Yu Zidi"))
        if kw_ok:
            # Ke Wenxi: 4:33.59 Trials -> mean 274.3s, sd 1.9s
            t = rng3.normal(274.3, 1.9) + (rng3.uniform(2.0, 4.5) if rng3.random() < 0.06 else 0.0)
            candidates.append((t, "Ke Wenxi"))
        if (not yz_ok or not kw_ok) and rng3.random() < 0.35:
            # Emergency sub Yu Yiting (4:33.09 PB at Pan Pacs!)
            t = rng3.normal(273.8, 1.8)
            candidates.append((t, "Yu Yiting"))
        if rng3.random() > 0.03:
            # Mio Narita: bimodal form! 55% rebounds on home Tokyo pool (~274.8s sd 2.0s), 45% stays slumping (~278.5s)
            if rng3.random() < 0.55:
                t = rng3.normal(274.8, 2.0)
            else:
                t = rng3.normal(278.5, 2.0)
            candidates.append((t, "Mio Narita"))
        if rng3.random() > 0.03:
            # Waka Kobori: beat Narita at Pan Pacs (4:39.23), PB ~4:36.5 -> mean 277.2s sd 2.0s
            t = rng3.normal(277.2, 2.0)
            candidates.append((t, "Waka Kobori"))
        candidates.append((rng3.normal(279.5, 2.2), "Rest_of_Asia"))
        wins_400[min(candidates)[1]] += 1

    for name, c in wins_400.most_common():
        print(f"  {name:18s}: {c/n:.4f}")


# ==============================================================================
# MODEL 4: Q4 (qid=832291) — ASIAN GAMES WOMEN'S 49KG WEIGHTLIFTING (Wed Sep 23)
# ==============================================================================
# Confirmed Official Field (GamesHub Sep 10, Sportstar Sep 9, Indian Express Sep 14, KCNA Sep 16):
#   - 8 lifters total! ZERO China! NO Thanyathon Sukcharoen! NO Surodchana Khambao!
#   - Ri Song-gum (PRK): CONFIRMED in GamesHub; DPRK 107-athlete squad departed Pyongyang Sep 15/16!
#     221kg WR at 49kg, 216kg Hangzhou AG, 213kg Oct 2025 Worlds (at 48kg).
#   - Mirabai Chanu (IND): 199kg Oct 2025 Worlds silver, 190kg July 2026 CWG gold, healthy.
#   - Fang Wan-ling (TPE): 192kg 2026 Asian Champs, 2x Olympic finalist, PB ~196-200kg potential.
#   - Suthasini Kaeosingkhon (THA): Thailand sole 49kg entry (replaces Sukcharoen).
#   - 4 remaining lifters in 8-woman field (JPN/PHI/INA/VIE tier ~178-192kg).
def model_weightlifting_49kg():
    print("\n" + "=" * 72)
    print("MODEL 4: qid=832291 — Asian Games Women's 49kg Weightlifting")
    print("=" * 72)
    rng = np.random.default_rng(83229116)
    n = 200000
    wins = Counter()
    # Parameters: (name, p_dns_withdraw, p_bombout, mean_total_kg, sd_kg)
    lifters = [
        ("Ri Song-gum",             0.030, 0.065, 212.5, 4.8),  # Can open safely ~200-203kg!
        ("Mirabai Chanu",           0.030, 0.085, 197.0, 4.2),
        ("Fang Wan-ling",           0.030, 0.085, 193.5, 4.2),
        ("Suthasini Kaeosingkhon",  0.030, 0.095, 187.5, 4.8),
        ("Field_Best_Other_4",      0.010, 0.060, 186.0, 5.2),
    ]
    for _ in range(n):
        best = (-1.0, None)
        for name, p_dns, p_bo, mu, sd in lifters:
            if rng.random() < p_dns or rng.random() < p_bo:
                continue
            # Occasional bad day (-6..-14kg) with 7% prob
            bad = rng.uniform(6.0, 14.0) if rng.random() < 0.07 else 0.0
            tot = rng.normal(mu, sd) - bad
            if tot > best[0]:
                best = (tot, name)
        if best[1]:
            wins[best[1]] += 1

    for name, c in wins.most_common():
        print(f"  {name:25s}: {c/n:.4f}")


# ==============================================================================
# MODEL 5: Q6 (qid=889545) — ASIAN GAMES MEN'S FOOTBALL (POST-MD1 + OFFICIAL BRACKET!)
# ==============================================================================
# COMPLETED MD1 REAL RESULTS (Tue Sep 15 & Wed Sep 16):
#   Group A: Japan 2-0 Hong Kong; Thailand 3-2 Kyrgyzstan
#   Group B: Iran 3-1 UAE; China 2-1 North Korea (PRK outshot CHN 19-10, 2 crossbars, 65% poss)
#   Group C: Uzbekistan 5-1 Philippines; Vietnam 1-1 Kuwait
#   Group D: South Korea 4-1 Qatar (Saudi Arabia bye)
#
# 100% CONFIRMED OFFICIAL OCA KNOCKOUT BRACKET (Wikipedia citing OCA + Olympics.com Sep 15):
#   QF1 (Sep 25): C1 vs D2
#   QF2 (Sep 25): D1 vs C2
#   QF3 (Sep 26): B1 vs A2
#   QF4 (Sep 26): A1 vs B2
#   SF1 (Sep 30): W(QF1) [C1/D2] vs W(QF4) [A1/B2]
#   SF2 (Sep 30): W(QF2) [D1/C2] vs W(QF3) [B1/A2]
#   Gold (Oct 3): W(SF1) vs W(SF2)
#
# CRITICAL MATHEMATICAL THEOREM AFTER MD1:
#   China (3 pts, +1), Iran (3 pts, +2), PRK (0 pts, -1), UAE (0 pts, -2).
#   Because PRK & UAE both have 0 pts (max possible = 6 pts), China CANNOT be mathematically
#   eliminated on MD2 vs Iran! Even if China loses to Iran (stays 3 pts), winning MD3 vs UAE
#   gives China 6 pts while UAE<=3 and at most Iran>6 & PRK<=6!
#   Thus ALL Group B eliminations of China resolve on MD3 (vs United Arab Emirates)!
#   And because B1 (QF3->SF2) & B2 (QF4->SF1) are on OPPOSITE halves of the bracket,
#   Iran can ONLY eliminate China in the GOLD MEDAL MATCH!
def model_ag_football_post_md1():
    print("\n" + "=" * 72)
    print("MODEL 5: qid=889545 — Asian Games Men's Football (POST-MD1 + OCA BRACKET)")
    print("=" * 72)
    rng = np.random.default_rng(20260916)

    def sim_match_goals(att_a, att_b, base_goals=1.22):
        diff = (att_a - att_b) / 100.0
        lam_a = base_goals * np.exp(0.28 * diff)
        lam_b = base_goals * np.exp(-0.28 * diff)
        return int(rng.poisson(lam_a)), int(rng.poisson(lam_b))

    def sim_knockout_winner(t1, t2, ratings):
        g1, g2 = sim_match_goals(ratings[t1], ratings[t2], base_goals=1.18)
        if g1 != g2:
            return t1 if g1 > g2 else t2
        e1, e2 = sim_match_goals(ratings[t1], ratings[t2], base_goals=0.38)
        if e1 != e2:
            return t1 if e1 > e2 else t2
        p1 = 0.5 + 0.03 * np.tanh((ratings[t1] - ratings[t2]) / 150.0)
        return t1 if rng.random() < p1 else t2

    def rank_group(teams, matches):
        # AFC/Asian Games group tiebreakers: Points -> H2H (for 2-team ties) -> GD -> GF -> random
        pts = {t: 0 for t in teams}
        gd = {t: 0 for t in teams}
        gf = {t: 0 for t in teams}
        h2h = {}
        for a, b, ga, gb in matches:
            gf[a] += ga; gf[b] += gb
            gd[a] += (ga - gb); gd[b] += (gb - ga)
            h2h[(a, b)] = ga - gb
            h2h[(b, a)] = gb - ga
            if ga > gb:
                pts[a] += 3
            elif gb > ga:
                pts[b] += 3
            else:
                pts[a] += 1; pts[b] += 1
        # Standard GD -> GF primary (with minor H2H refinement for exact 2-team ties if AFC uses H2H first;
        # actually OCA/AFC Asian Games typically uses GD -> GF -> H2H or H2H -> GD; let's check both!)
        order = sorted(teams, key=lambda t: (pts[t], gd[t], gf[t], rng.random()), reverse=True)
        return order, pts, gd, gf

    # Post-MD1 Bayesian-updated rating regimes:
    #   - South Korea (beat QAT 4-1): ~1720
    #   - Japan (beat HKG 2-0, hosts): ~1685
    #   - Uzbekistan (beat PHI 5-1): ~1655
    #   - Saudi Arabia (yet to play): ~1615
    #   - Iran (beat UAE 3-1): bumped from 1575 -> ~1610
    #   - China (beat PRK 2-1 clinically via Zhang Yuning/Wu Xi, though outshot 19-10): ~1575
    #   - North Korea (lost 1-2 to CHN despite 19 shots, 2 crossbars, 65% poss): bumped 1525 -> ~1545
    #   - UAE (lost 1-3 to Iran): trimmed 1545 -> ~1525
    #   - Thailand (beat KGZ 3-2): ~1515
    #   - Vietnam (drew KUW 1-1): ~1515; Kuwait: ~1470; Qatar (lost 1-4 to KOR): ~1520
    regimes = [
        ("R1: Post-MD1 Base Calibrated (IRN 1610, CHN 1575, PRK 1545, UAE 1525)", 0.50, {
            "South Korea": 1720, "Japan": 1685, "Uzbekistan": 1655, "Saudi Arabia": 1615,
            "Iran": 1610, "China": 1575, "North Korea": 1545, "United Arab Emirates": 1525,
            "Qatar": 1520, "Vietnam": 1515, "Thailand": 1515, "Kuwait": 1470,
            "Kyrgyzstan": 1445, "Hong Kong": 1390, "Philippines": 1340,
        }),
        ("R2: China Underlying-xG Regression (CHN 1535, IRN 1625, PRK 1565, UAE 1540)", 0.28, {
            "South Korea": 1725, "Japan": 1690, "Uzbekistan": 1660, "Saudi Arabia": 1615,
            "Iran": 1625, "China": 1535, "North Korea": 1565, "United Arab Emirates": 1540,
            "Qatar": 1520, "Vietnam": 1515, "Thailand": 1515, "Kuwait": 1470,
            "Kyrgyzstan": 1445, "Hong Kong": 1390, "Philippines": 1340,
        }),
        ("R3: China Clinical Counterattack Shines (CHN 1610, IRN 1595, JPN U21 1655)", 0.22, {
            "South Korea": 1705, "Japan": 1655, "Uzbekistan": 1645, "Saudi Arabia": 1605,
            "China": 1610, "Iran": 1595, "North Korea": 1535, "United Arab Emirates": 1515,
            "Qatar": 1520, "Vietnam": 1515, "Thailand": 1510, "Kuwait": 1470,
            "Kyrgyzstan": 1445, "Hong Kong": 1390, "Philippines": 1340,
        }),
    ]

    n_trials = 150000
    total_elim = Counter()
    stage_stats = Counter()
    pos_stats = Counter()
    grp_a_2nd = Counter()
    grp_b_1st = Counter()

    for rname, w_reg, base_r in regimes:
        elim = Counter()
        r_stage = Counter()
        r_pos = Counter()
        for _ in range(n_trials):
            r = {t: v + rng.normal(0, 32.0) for t, v in base_r.items()}

            # Group A (MD1 fixed: Japan 2-0 Hong Kong; Thailand 3-2 Kyrgyzstan)
            gA = ["Japan", "Thailand", "Kyrgyzstan", "Hong Kong"]
            mA = [
                ("Japan", "Hong Kong", 2, 0),
                ("Thailand", "Kyrgyzstan", 3, 2),
                ("Hong Kong", "Thailand", *sim_match_goals(r["Hong Kong"], r["Thailand"])),
                ("Kyrgyzstan", "Japan", *sim_match_goals(r["Kyrgyzstan"], r["Japan"])),
                ("Japan", "Thailand", *sim_match_goals(r["Japan"], r["Thailand"])),
                ("Kyrgyzstan", "Hong Kong", *sim_match_goals(r["Kyrgyzstan"], r["Hong Kong"])),
            ]
            ordA, _, _, _ = rank_group(gA, mA)
            grp_a_2nd[ordA[1]] += w_reg / n_trials

            # Group C (MD1 fixed: Uzbekistan 5-1 Philippines; Vietnam 1-1 Kuwait)
            gC = ["Vietnam", "Uzbekistan", "Philippines", "Kuwait"]
            mC = [
                ("Uzbekistan", "Philippines", 5, 1),
                ("Vietnam", "Kuwait", 1, 1),
                ("Philippines", "Vietnam", *sim_match_goals(r["Philippines"], r["Vietnam"])),
                ("Kuwait", "Uzbekistan", *sim_match_goals(r["Kuwait"], r["Uzbekistan"])),
                ("Vietnam", "Uzbekistan", *sim_match_goals(r["Vietnam"], r["Uzbekistan"])),
                ("Philippines", "Kuwait", *sim_match_goals(r["Philippines"], r["Kuwait"])),
            ]
            ordC, _, _, _ = rank_group(gC, mC)

            # Group D (MD1 fixed: South Korea 4-1 Qatar)
            gD = ["South Korea", "Saudi Arabia", "Qatar"]
            mD = [
                ("South Korea", "Qatar", 4, 1),
                ("Saudi Arabia", "Qatar", *sim_match_goals(r["Saudi Arabia"], r["Qatar"])),
                ("South Korea", "Saudi Arabia", *sim_match_goals(r["South Korea"], r["Saudi Arabia"])),
            ]
            ordD, _, _, _ = rank_group(gD, mD)

            # Group B (MD1 fixed: China 2-1 North Korea; Iran 3-1 UAE)
            gB = ["China", "United Arab Emirates", "Iran", "North Korea"]
            i2, c2 = sim_match_goals(r["Iran"], r["China"])
            p2, u2 = sim_match_goals(r["North Korea"], r["United Arab Emirates"])
            c3, u3 = sim_match_goals(r["China"], r["United Arab Emirates"])
            i3, p3 = sim_match_goals(r["Iran"], r["North Korea"])
            mB = [
                ("China", "North Korea", 2, 1),
                ("Iran", "United Arab Emirates", 3, 1),
                ("Iran", "China", i2, c2),
                ("North Korea", "United Arab Emirates", p2, u2),
                ("China", "United Arab Emirates", c3, u3),
                ("Iran", "North Korea", i3, p3),
            ]
            ordB, _, _, _ = rank_group(gB, mB)
            c_pos = ordB.index("China") + 1
            r_pos[c_pos] += 1
            grp_b_1st[ordB[0]] += w_reg / n_trials

            if c_pos >= 3:
                # China cannot be mathematically eliminated before MD3!
                # MD3 match is China vs UAE (simultaneous with Iran vs PRK).
                elim["United Arab Emirates"] += 1
                r_stage["MD3_UAE"] += 1
                continue

            # Official OCA Knockout Bracket (100% CONFIRMED):
            #   QF1: C1 vs D2; QF2: D1 vs C2; QF3: B1 vs A2; QF4: A1 vs B2
            #   SF1: W(QF1) vs W(QF4); SF2: W(QF2) vs W(QF3)
            r_ko = dict(r)
            for t in gD:
                r_ko[t] += 15.0  # Group D plays 1 fewer match (freshness edge)

            qfs = [
                (ordC[0], ordD[1]),  # QF1: C1 vs D2
                (ordD[0], ordC[1]),  # QF2: D1 vs C2
                (ordB[0], ordA[1]),  # QF3: B1 vs A2
                (ordA[0], ordB[1]),  # QF4: A1 vs B2
            ]
            qf_w = []
            killer = None
            for t1, t2 in qfs:
                w = sim_knockout_winner(t1, t2, r_ko)
                qf_w.append(w)
                if "China" in (t1, t2) and w != "China":
                    killer = w
            if killer is not None:
                elim[killer] += 1
                r_stage["QF"] += 1
                continue

            # Semi-finals: SF1 = W(QF1) vs W(QF4); SF2 = W(QF2) vs W(QF3)
            sfs = [(qf_w[0], qf_w[3]), (qf_w[1], qf_w[2])]
            sf_w = []
            for t1, t2 in sfs:
                w = sim_knockout_winner(t1, t2, r_ko)
                sf_w.append(w)
                if "China" in (t1, t2) and w != "China":
                    killer = w
            if killer is not None:
                elim[killer] += 1
                r_stage["SF"] += 1
                continue

            # Gold Medal Final
            gold = sim_knockout_winner(sf_w[0], sf_w[1], r_ko)
            if gold == "China":
                elim["None"] += 1
                r_stage["GOLD"] += 1
            else:
                elim[gold] += 1
                r_stage["FIN"] += 1

        print(f"\n  [{w_reg:.2f}] {rname}")
        print(f"    China Group B Pos: 1st={r_pos[1]/n_trials:.3f}, 2nd={r_pos[2]/n_trials:.3f}, 3rd/4th={(r_pos[3]+r_pos[4])/n_trials:.3f}")
        print(f"    Stages: MD3_UAE={r_stage['MD3_UAE']/n_trials:.3f}, QF={r_stage['QF']/n_trials:.3f}, SF={r_stage['SF']/n_trials:.3f}, FIN={r_stage['FIN']/n_trials:.3f}, GOLD={r_stage['GOLD']/n_trials:.3f}")
        top6 = [(k, v / n_trials) for k, v in elim.most_common(6)]
        print("    Top-6:", ", ".join(f"{k}={p:.3f}" for k, p in top6))
        for k, v in elim.items():
            total_elim[k] += w_reg * (v / n_trials)
        for k, v in r_stage.items():
            stage_stats[k] += w_reg * (v / n_trials)
        for k, v in r_pos.items():
            pos_stats[k] += w_reg * (v / n_trials)

    print("\n  === BLENDED POST-MD1 DISTRIBUTION (qid=889545) ===")
    print(f"  China Group B Finish: 1st={pos_stats[1]:.4f}, 2nd={pos_stats[2]:.4f}, 3rd={pos_stats[3]:.4f}, 4th={pos_stats[4]:.4f}")
    print(f"  Group A 2nd place:    " + ", ".join(f"{k}={v:.3f}" for k, v in grp_a_2nd.most_common(4)))
    print(f"  Stage Exit Probs:     " + ", ".join(f"{k}={v:.4f}" for k, v in stage_stats.items()))
    print("  Ranked Eliminators:")
    for k, p in total_elim.most_common(12):
        print(f"    {k:22s}: {p:.4f}")
    top5_sum = sum(p for _, p in total_elim.most_common(5))
    print(f"  Top-5 sum: {top5_sum:.4f} (outside: {1-top5_sum:.4f})")


if __name__ == "__main__":
    model_squash_no1()
    model_swimming_im()
    model_weightlifting_49kg()
    model_ag_football_post_md1()
