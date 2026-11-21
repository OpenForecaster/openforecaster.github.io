"""
Quantitative Bayesian Monte Carlo Models — Sat Sep 26, 2026 (Asian Games Day 8 Night)
Batch: asian_games_final5 (5 questions)

VERIFIED SAT SEP 26 RESULTS:
  1. qid=259249 (PV Sindhu Furthest Round, res=2026-09-27):
     - R32: PV Sindhu def. Chiu Pin-chian (TPE, WR #17) 21-19, 21-14!
     - R16: PV Sindhu CRUSHED [7] Tomoka Miyazaki (JPN, WR #7, home court!) 21-9, 21-13!
     - R32 & R16 ELIMINATED (0%!) -> Exhaustive 3-outcome distribution: {Quarterfinals, Semifinals, Final}!
     - QF (Sun Sep 27, 9:30 AM IST): PV Sindhu vs [4] Chen Yufei (CHN, WR #4; 9-7 H2H, healthy per An Se-young,
       beat Liang Ka-wing & Nguyen Thuy Linh; Sindhu beat injured Chen 21-19 15-10 ret at Jul 2026 Japan Open!).
     - Section 1 QF: [1] An Se-young (crushed Smagulova 21-5 21-5 & Riyanage 21-9 21-10; 10-0 H2H vs Sindhu!)
       vs [5] Ratchanok Intanon (THA, WR #5).

  2. qid=556932 (Women's Singles Squash Gold, res=2026-09-27):
     - SF1: [1] Sivasangari Subramaniam (MAS, WR #5) def. [5] Chan Sin Yuk 11-6, 11-8, 11-7 (26 min)!
     - SF2: [3] Anahat Singh (IND, WR #17-20, 18yo) UPSET [2] Satomi Watanabe (JPN, WR #6, home!)
       9-11, 11-13, 12-10, 11-6, 11-3 (saved 2-3 match points, brief medical stop for head-shoulder collision)!
     - Watanabe & Chan ELIMINATED -> Exhaustive 2-player Final (Sun Sep 27, 13:30 IST):
       Sivasangari Subramaniam vs Anahat Singh!
     - H2H: Sivasangari leads 3-0 (2025 British Open 3-1; Jan 2026 ToC 3-2; Sep 4 2026 London Classic 11-4 11-4 in 17m).

  3. qid=700005 (Men's Singles Squash Gold, res=2026-09-27):
     - SF1: [1] Ng Eain Yow (MAS, WR #18) OBLITERATED [3] Noor Zaman (PAK, WR #29) 11-7, 11-2, 11-4 in 20 MIN!!
     - SF2: [2] Abhay Singh (IND, WR #24) def. [5] Muhammad Ashab Irfan (PAK, WR #49) 11-3, 12-10, 11-6 (3-0)!
     - Noor Zaman & Ashab Irfan ELIMINATED -> Exhaustive 2-player Final (Sun Sep 27, 12:30 IST):
       Ng Eain Yow vs Abhay Singh! Both unbeaten without dropping a game; Eain Yow defending champ + monster 20m SF.

  4. qid=695205 (Men's Javelin Throw Gold, res=2026-09-28):
     - No men's javelin qualification occurred/reported on Sat Sep 26 (likely straight Mon Sep 28 final).
     - Gulf News Sep 26 re-confirmed Neeraj Chopra OUT, India entries Rohit Yadav (87.68m SB) & Yash Vir Singh (85.41m SB).
     - Wet/rainy track conditions in Nagoya Day 8 + Pathirage T+2d sanity check.

  5. qid=889545 (China Men's Football Eliminator, res=2026-09-30):
     - QF3: CHINA CRUSHED THAILAND 3-0 (45+2' OG, 47' Hu Hetao, 63' Zhang Yuning) WITHOUT suspended Wang Yudong!
       China has conceded ONLY 1 goal in 4 matches (Wu Xi, Zhu Chenjie, Zhang Yuning overage spine + Li Hao GK);
       Wang Yudong RETURNS for Wed Sep 30 SF! Thailand (0.43!) ELIMINATED!
     - QF4: JAPAN (U-21, host, 13-0 GD) def. NORTH KOREA 1-0 (39' Nwadike)! North Korea ELIMINATED!
     - EXACT 4-OUTCOME EXHAUSTIVE BRACKET LOCKED:
         SF1 (Wed Sep 30): Uzbekistan (U-23, 4W 12-1 GD, +1 rest day) vs Japan (U-21, host, 4W 13-0 GD)
         SF2 (Wed Sep 30): South Korea (3x defending champ, 4-0 VIE, Lee Young-jun & Kim Ji-soo, +1 rest day) vs China
         Final (Sat Oct 3): W(SF1) vs W(SF2) -> Exhaustive outcomes: {South Korea, Japan, Uzbekistan, None}!
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
# MODEL 1: qid=259249 — PV SINDHU FURTHEST ROUND (IN QUARTERFINALS!)
# ==============================================================================
def model_pv_sindhu_sep26(n_trials=400000, seed=25924926):
    rng = random.Random(seed)
    print("=" * 80)
    print("MODEL 1: qid=259249 — PV Sindhu Furthest Round (IN QF vs Chen Yufei!)")
    print("=" * 80)
    # Multi-regime blend after 21-19 21-14 over Chiu AND 21-9 21-13 demolition of WR #7 Miyazaki!
    # Regimes span:
    #   (a) Base Bayesian posterior: Sindhu's 21-9 21-13 blitz upgrades her form sharply (+0.20 to +0.25 logit),
    #       putting her at ~35% vs healthy WR #4 Chen Yufei (who leads 9-7 H2H, 5-1 since 2020 excl/incl ret,
    #       and is in 'very good condition' per An Se-young).
    #   (b) Peak Japan-Conditions Sindhu: 2026 Japan Open champ (led Chen 21-19 15-10 ret in Tokyo!), explosive attack
    #       translates directly to Ichinomiya hall -> ~43% vs Chen Yufei!
    #   (c) Chen Yufei Defensive Control / Attrition: Chen healthy (unlike July), extends rallies like Yamaguchi did
    #       in team QF (where Sindhu faded after G1), plus Sindhu's 3rd match in 26h -> ~26% vs Chen Yufei.
    regimes = [
        # (name, w, p_vs_chen, p_an_beats_intanon, p_vs_an, p_vs_intanon)
        ("R1: Base Post-Miyazaki Blitz (Healthy WR#4 Chen ~65% fav; An Se-young 91% vs Intanon, 10-0 vs Sindhu)",
         0.50, 0.35, 0.91, 0.065, 0.53),
        ("R2: Peak Japan-Open Sindhu (explosive smash-drop rhythm carries over -> 43% vs Chen, 9% vs An)",
         0.25, 0.43, 0.89, 0.090, 0.58),
        ("R3: Chen Defensive Attrition / 31yo Back-to-Back Load (Chen 74% fav; An 94% vs Intanon, 4% vs Sindhu)",
         0.25, 0.26, 0.94, 0.045, 0.47),
    ]

    blend = Counter()
    p_qf_win_tot = 0.0
    p_sf_win_cond_tot = 0.0

    for rname, w, p_ch, p_an_r, p_vs_an, p_vs_in in regimes:
        counts = Counter()
        sf_reach = 0
        fin_reach = 0
        for _ in range(n_trials):
            # Shared day-to-day latent tournament form correlation between QF and SF
            form_lo = rng.gauss(0.0, 0.22)
            # QF: Sindhu vs Chen Yufei
            if rng.random() > inv_logit(logit(p_ch) + form_lo):
                counts["Quarterfinals"] += 1
                continue
            sf_reach += 1
            # SF: vs W(An Se-young vs Ratchanok Intanon)
            if rng.random() < p_an_r:
                p_sf = inv_logit(logit(p_vs_an) + 0.75 * form_lo)
            else:
                p_sf = inv_logit(logit(p_vs_in) + 0.75 * form_lo)
            if rng.random() > p_sf:
                counts["Semifinals"] += 1
                continue
            fin_reach += 1
            counts["Final"] += 1

        p_qf_win_tot += w * (sf_reach / n_trials)
        p_sf_win_cond_tot += w * (fin_reach / max(1, sf_reach))
        print(f"\n  [{w:.2f}] {rname}")
        for k in ["Quarterfinals", "Semifinals", "Final"]:
            p = counts[k] / n_trials
            blend[k] += w * p
            print(f"        {k:16s}: {p:.4f}")

    print("\n  === FINAL BLENDED PV SINDHU (EXHAUSTIVE 3-OUTCOME SUM = 1.000) ===")
    print(f"  Checkpoints: P(Sindhu>Chen QF)={p_qf_win_tot:.3f} | P(Sindhu reaches Final | reaches SF)={p_sf_win_cond_tot:.3f}")
    for k in ["Quarterfinals", "Semifinals", "Final"]:
        print(f"    {k:16s}: {blend[k]:.4f}")
    print(f"  Sum = {sum(blend.values()):.4f}")


# ==============================================================================
# MODEL 2: qid=556932 — WOMEN'S SINGLES SQUASH FINAL (SIVASANGARI vs ANAHAT)
# ==============================================================================
def model_women_squash_sep26(n_trials=400000, seed=55693226):
    rng = random.Random(seed)
    print("\n" + "=" * 80)
    print("MODEL 2: qid=556932 — Women's Singles Squash Final (Sivasangari vs Anahat)")
    print("=" * 80)
    # Exact 2-player Best-of-5 Gold Medal Final (Sun Sep 27, 13:30 IST):
    #   Sivasangari Subramaniam (WR #5): fresh (25m QF + 26m SF, 0 games lost), defending champ,
    #     3-0 H2H (2025 British Open 3-1, Jan 2026 ToC 3-2, Sep 4 2026 London Classic 11-4 11-4 in 17m).
    #   Anahat Singh (WR #17-20, 18yo): JUST beat WR #6 Satomi Watanabe 3-2 (9-11 11-13 12-10 11-6 11-3)
    #     on Japanese home soil! Huge rising-prodigy skill update (+65 to +95 Elo above raw WR #18),
    #     partially offset by 5-game SF fatigue + head-shoulder knock (~-15 to -25 Elo) & Sivasangari matchup/H2H!
    scenarios = [
        # (name, w, siva_elo_mean, ana_elo_mean, h2h_siva_edge, fatigue_siva_edge, sd)
        ("S1: Base Posterior (Siva WR#5 sharp +40; Anahat upgraded +75 after Watanabe win; +35 H2H +20 freshness)",
         0.45, rank_to_elo(5) + 40, rank_to_elo(18) + 75, 35.0, 20.0, 58.0),
        ("S2: Prodigy Breakout / ToC-Style 5-Game Threat (Anahat plays like WR#9 -> +115; smaller +20 H2H +10 fatigue)",
         0.30, rank_to_elo(5) + 30, rank_to_elo(18) + 115, 20.0, 10.0, 62.0),
        ("S3: London Classic Dominance / Matchup & Fatigue Bite (Siva +50; Anahat +45; +45 H2H +30 fatigue)",
         0.25, rank_to_elo(5) + 50, rank_to_elo(18) + 45, 45.0, 30.0, 52.0),
    ]

    blend = Counter()
    for sname, w, s_mu, a_mu, h2h, fat, sd in scenarios:
        s_wins = 0
        for _ in range(n_trials):
            es = rng.gauss(s_mu + h2h + fat, sd)
            ea = rng.gauss(a_mu, sd)
            p_s = 1.0 / (1.0 + 10.0 ** (-(es - ea) / 400.0))
            if rng.random() < p_s:
                s_wins += 1
        ps = s_wins / n_trials
        pa = 1.0 - ps
        blend["Sivasangari Subramaniam"] += w * ps
        blend["Anahat Singh"] += w * pa
        print(f"\n  [{w:.2f}] {sname}")
        print(f"        Sivasangari={ps:.4f} | Anahat Singh={pa:.4f}")

    print("\n  === FINAL BLENDED WOMEN'S SQUASH (EXHAUSTIVE 2-PLAYER SUM = 1.000) ===")
    for nm in ["Sivasangari Subramaniam", "Anahat Singh"]:
        print(f"    {nm:26s}: {blend[nm]:.4f}")


# ==============================================================================
# MODEL 3: qid=700005 — MEN'S SINGLES SQUASH FINAL (NG EAIN YOW vs ABHAY SINGH)
# ==============================================================================
def model_men_squash_sep26(n_trials=400000, seed=70000526):
    rng = random.Random(seed)
    print("\n" + "=" * 80)
    print("MODEL 3: qid=700005 — Men's Singles Squash Final (Ng Eain Yow vs Abhay Singh)")
    print("=" * 80)
    # Exact 2-player Best-of-5 Gold Medal Final (Sun Sep 27, 12:30 IST):
    #   [1] Ng Eain Yow (MAS, WR #18): defending Asian Games champ, former top-12 PSA regular,
    #       OBLITERATED WR #29 Noor Zaman 11-7, 11-2, 11-4 in JUST 20 MINUTES in SF!
    #   [2] Abhay Singh (IND, WR #24): career-high form, crushed Tsukue 11-4 11-3 11-6 & beat Irfan 11-3 12-10 11-6
    #       (0 games dropped!), clutch big-stage player (2023 Team Gold hero).
    #   Both 100% fresh!
    scenarios = [
        # (name, w, eain_elo, abhay_elo, big_match_edge, sd)
        ("S1: Base Post-SF (Eain Yow WR#18 +55 after 20m Noor blitz; Abhay WR#24 +22 unbeaten; +20 pedigree)",
         0.50, rank_to_elo(18) + 55, rank_to_elo(24) + 22, 20.0, 55.0),
        ("S2: Peak Defending Champ Gap (Eain Yow plays true top-12 level +75; Abhay +15; +30 pedigree)",
         0.25, rank_to_elo(18) + 75, rank_to_elo(24) + 15, 30.0, 52.0),
        ("S3: Tight WR#18 vs WR#24 Battle (Abhay 0-games-lost peak +38; Eain Yow +38; +10 pedigree)",
         0.25, rank_to_elo(18) + 38, rank_to_elo(24) + 38, 10.0, 58.0),
    ]

    blend = Counter()
    for sname, w, e_mu, a_mu, ped, sd in scenarios:
        e_wins = 0
        for _ in range(n_trials):
            ee = rng.gauss(e_mu + ped, sd)
            ea = rng.gauss(a_mu, sd)
            p_e = 1.0 / (1.0 + 10.0 ** (-(ee - ea) / 400.0))
            if rng.random() < p_e:
                e_wins += 1
        pe = e_wins / n_trials
        pa = 1.0 - pe
        blend["Ng Eain Yow"] += w * pe
        blend["Abhay Singh"] += w * pa
        print(f"\n  [{w:.2f}] {sname}")
        print(f"        Ng Eain Yow={pe:.4f} | Abhay Singh={pa:.4f}")

    print("\n  === FINAL BLENDED MEN'S SQUASH (EXHAUSTIVE 2-PLAYER SUM = 1.000) ===")
    for nm in ["Ng Eain Yow", "Abhay Singh"]:
        print(f"    {nm:20s}: {blend[nm]:.4f}")


# ==============================================================================
# MODEL 4: qid=695205 — MEN'S JAVELIN THROW (T+2d SANITY CHECK)
# ==============================================================================
def model_javelin_sep26(n=200000, seed=69520526):
    rng = np.random.default_rng(seed)
    print("\n" + "=" * 80)
    print("MODEL 4: qid=695205 — Men's Javelin Throw (T+2d Sanity Check)")
    print("=" * 80)
    # T+2d: Slightly lower pre-event DNS risk (4.0% vs 5.5% at T+5d), offset by wet/rainy Nagoya runway variance!
    def sim_best6(mu, sd, p_ok):
        day_form = rng.normal(mu, sd * 0.72, n)
        throws = day_form[:, None] + rng.normal(0.0, sd * 0.72, (n, 6))
        best = np.max(throws, axis=1)
        return np.where(rng.random(n) >= p_ok, 0.0, best)

    p_day = rng.normal(89.8, 1.9, n)
    p_day -= (rng.random(n) < 0.11) * rng.uniform(2.5, 6.0, n)
    p_best = np.max(p_day[:, None] + rng.normal(0.0, 1.50, (n, 6)), axis=1)
    p_best = np.where(rng.random(n) < 0.042, 0.0, p_best)

    ry_best = sim_best6(84.4, 2.35, 0.96)
    nad_healthy = rng.random(n) < 0.27
    nad_mu = np.where(nad_healthy, 86.2, 81.0)
    nad_sd = np.where(nad_healthy, 2.8, 2.2)
    nad_day = rng.normal(nad_mu, nad_sd * 0.75)
    nad_best = np.max(nad_day[:, None] + rng.normal(0.0, 1.85, (n, 6)), axis=1)
    nad_best = np.where(rng.random(n) < 0.10, 0.0, nad_best)

    ys_best = sim_best6(83.2, 2.35, 0.96)
    yv_best = sim_best6(82.4, 2.15, 0.96)
    ot_best = sim_best6(83.3, 2.25, 0.98)

    names = ["Rumesh Tharanga Pathirage", "Rohit Yadav", "Arshad Nadeem", "Yuta Sakiyama", "Yash Vir Singh", "Rest_of_Asia"]
    mat = np.vstack([p_best, ry_best, nad_best, ys_best, yv_best, ot_best])
    idx = np.argmin(-mat, axis=0)
    for i, nm in enumerate(names):
        print(f"    {nm:28s}: {float(np.mean(idx == i)):.4f}")
    print("  (Prior forecast: Pathirage 0.74, Rohit 0.09, Nadeem 0.065, Sakiyama 0.04, Yash Vir 0.015)")


# ==============================================================================
# MODEL 5: qid=889545 — MEN'S FOOTBALL CHINA ELIMINATOR (EXACT SEMIFINALS!)
# ==============================================================================
def model_football_sep26(n_trials=250000, seed=20260926):
    rng = np.random.default_rng(seed)
    print("\n" + "=" * 80)
    print("MODEL 5: qid=889545 — Men's Football China Eliminator (EXACT 4-TEAM SF LOCKED!)")
    print("=" * 80)
    # EXACT LOCKED SEMIFINALS (Wed Sep 30, Nagai Stadium, Osaka):
    #   SF1: Uzbekistan (4W, 12-1 GD, 3-0 KSA, +1 rest day, U-23) vs Japan (4W, 13-0 GD, 1-0 PRK, host U-21)
    #   SF2: South Korea (3W, 4-0 VIE, Lee Young-jun & Kim Ji-soo, +1 rest day & 1 fewer group game, military exemption!)
    #        vs China (2W 2D, 1 GA in 4 games, CRUSHED Thailand 3-0 WITHOUT Wang Yudong; Wang RETURNS + Wu Xi/Zhu Chenjie/Zhang Yuning!)
    #   Gold Medal Final (Sat Oct 3, Toyota Stadium): W(SF1) vs W(SF2).

    def sim_match_goals(att_a, att_b, base_goals=1.18):
        diff = (att_a - att_b) / 100.0
        lam_a = base_goals * math.exp(0.28 * diff)
        lam_b = base_goals * math.exp(-0.28 * diff)
        return int(rng.poisson(lam_a)), int(rng.poisson(lam_b))

    def sim_ko(t1, t2, r1, r2, base_goals=1.16, et_goals=0.38):
        g1, g2 = sim_match_goals(r1, r2, base_goals=base_goals)
        if g1 != g2:
            return t1 if g1 > g2 else t2
        e1, e2 = sim_match_goals(r1, r2, base_goals=et_goals)
        if e1 != e2:
            return t1 if e1 > e2 else t2
        p1 = 0.5 + 0.03 * math.tanh((r1 - r2) / 150.0)
        return t1 if rng.random() < p1 else t2

    # Post-QF3/QF4 Bayesian ratings:
    # - China upgraded from 1590 -> 1622 (+32 Elo!) after 3-0 Thailand WITHOUT Wang Yudong + Wu Xi/Zhu Chenjie/Zhang Yuning + 1 GA in 4!
    # - Japan U-21 slightly trimmed from 1730 -> 1718 (narrow 1-0 vs PRK, younger U-21 squad vs UZB U-23), keeps +12 home edge -> 1730 eff.
    # - Uzbekistan U-23 1708 (+4 extra rest day -> 1712 eff vs Japan 1730 eff -> ~53-54% Japan, ~46-47% UZB in SF1!).
    # - South Korea 1758 (+4 extra rest day + 3 fewer group match = +7 -> 1765 eff vs China 1622 -> +143 Elo!).
    regimes = [
        ("R1: Base Post-QF3/4 (KOR 1758+7, JPN 1718+12h, UZB 1708+4r, CHN 1622 w/ Wang back & veterans)",
         0.45, 0.85, 7.0,
         {"South Korea": 1758, "Japan": 1718, "Uzbekistan": 1708, "China": 1622}),
        ("R2: South Korea Military-Exemption & Talent Dominance (KOR 1775+8; CHN 1605; JPN 1725+12h; UZB 1705+4r)",
         0.25, 0.92, 8.0,
         {"South Korea": 1775, "Japan": 1725, "Uzbekistan": 1705, "China": 1605}),
        ("R3: China Elite Low-Block + Senior Spine Surge (CHN 1645, c_def=0.76; KOR 1748+6; UZB 1715+4r; JPN 1712+12h)",
         0.20, 0.76, 6.0,
         {"South Korea": 1748, "Japan": 1712, "Uzbekistan": 1715, "China": 1645}),
        ("R4: High-Variance Knockout / Tight Semis (KOR 1738+5, CHN 1630, UZB 1705+4r, JPN 1710+10h)",
         0.10, 0.88, 5.0,
         {"South Korea": 1738, "Japan": 1710, "Uzbekistan": 1705, "China": 1630}),
    ]

    total_elim = Counter()
    jpn_sf1_tot = 0.0
    chn_sf2_tot = 0.0
    chn_fin_win_cond = 0.0

    for rname, w_reg, c_def, kor_rest, base_r in regimes:
        elim = Counter()
        jpn_sf1 = 0
        chn_sf2 = 0
        chn_gold = 0

        for _ in range(n_trials):
            r = {t: v + rng.normal(0.0, 26.0) for t, v in base_r.items()}
            # SF1 (Wed Sep 30): Japan (+12 home) vs Uzbekistan (+4 extra rest day)
            w_sf1 = sim_ko("Japan", "Uzbekistan", r["Japan"] + 12.0, r["Uzbekistan"] + 4.0)
            if w_sf1 == "Japan":
                jpn_sf1 += 1

            # SF2 (Wed Sep 30): China vs South Korea (+kor_rest)
            w_sf2 = sim_ko("China", "South Korea", r["China"], r["South Korea"] + kor_rest,
                           base_goals=1.16 * c_def, et_goals=0.38 * c_def)
            if w_sf2 != "China":
                elim["South Korea"] += 1
                continue
            chn_sf2 += 1

            # Final (Sat Oct 3): China vs W(SF1)
            r_fin_opp = r[w_sf1] + (12.0 if w_sf1 == "Japan" else 0.0)
            w_gold = sim_ko("China", w_sf1, r["China"], r_fin_opp,
                            base_goals=1.16 * c_def, et_goals=0.38 * c_def)
            if w_gold == "China":
                elim["None"] += 1
                chn_gold += 1
            else:
                elim[w_sf1] += 1

        jpn_sf1_tot += w_reg * (jpn_sf1 / n_trials)
        chn_sf2_tot += w_reg * (chn_sf2 / n_trials)
        chn_fin_win_cond += w_reg * (chn_gold / max(1, chn_sf2))

        print(f"\n  [{w_reg:.2f}] {rname}")
        print(f"        P(JPN>UZB SF1)={jpn_sf1/n_trials:.3f} | P(KOR>CHN SF2)={1 - chn_sf2/n_trials:.3f} | P(CHN wins Final | reaches Final)={chn_gold/max(1,chn_sf2):.3f}")
        for k in ["South Korea", "Japan", "Uzbekistan", "None"]:
            p = elim[k] / n_trials
            total_elim[k] += w_reg * p
            print(f"        {k:14s}: {p:.4f}")

    print("\n  === FINAL BLENDED FOOTBALL (EXHAUSTIVE 4-OUTCOME SUM = 1.000) ===")
    print(f"  Checkpoints: P(JPN>UZB SF1)={jpn_sf1_tot:.3f} | P(KOR>CHN SF2)={1 - chn_sf2_tot:.3f} | P(CHN Gold | Final)={chn_fin_win_cond:.3f}")
    for k, p in total_elim.most_common():
        print(f"    {k:14s}: {p:.4f}")
    print(f"  Sum = {sum(total_elim.values()):.4f}")


if __name__ == "__main__":
    model_pv_sindhu_sep26()
    model_women_squash_sep26()
    model_men_squash_sep26()
    model_javelin_sep26()
    model_football_sep26()
