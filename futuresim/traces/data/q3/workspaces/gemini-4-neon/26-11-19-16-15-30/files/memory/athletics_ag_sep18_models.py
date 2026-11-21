"""
Quantitative Forecasting Models — Fri Sep 18, 2026
Batch: olympic_athletics_asian_games
Models:
  1. Q1 (qid=67348):  Asian Games Men's Basketball Bronze Medal (Sun Sep 20) — POST-SEMIFINALS! (BINARY: CHINA vs IRAN!)
  2. Q2 (qid=784475): Copenhagen 2026 WRRC Women's Half Marathon (Sun Sep 20) — DMI Wind/Rain Forecast + 2026 Form/PB Corrections!
  3. Q7 (qid=889545): Asian Games Men's Football China Gold-Medal Bid — POST-FRI SEP 18 GROUP C/D MD2 RESULTS!
"""
import math
import random
from collections import Counter
import numpy as np


# ==============================================================================
# MODEL 1: Q1 (qid=67348) — 2026 ASIAN GAMES MEN'S BASKETBALL BRONZE MEDAL
# ==============================================================================
# BOTH SEMIFINALS COMPLETED FRI SEP 18:
#   - SF1: Japan 97-77 China (some initial flashes 97-78; Kyodo/Xinhua/Global Times/ChinaNews final: 97-77)
#          -> Japan to Gold Final (0% bronze); CHINA to Bronze Match!
#   - SF2: South Korea 77-51 Iran
#          -> South Korea to Gold Final (0% bronze); IRAN to Bronze Match!
#
# BRONZE MEDAL MATCH (Sun Sep 20, 16:40 JST, Aichi International Arena):
#   EXACT BINARY MATCHUP: CHINA vs IRAN!
def model_q1_china_vs_iran_basketball():
    print("=" * 74)
    print("MODEL 1: qid=67348 — Asian Games Men's Basketball Bronze: CHINA vs IRAN")
    print("=" * 74)

    teams = [
        "China", "South Korea", "Japan", "Iran",
        "Chinese Taipei", "Jordan", "Saudi Arabia", "Bahrain",
        "Qatar", "Philippines", "Indonesia", "Kazakhstan",
    ]
    idx = {t: i for i, t in enumerate(teams)}
    n_t = len(teams)

    # ALL 24 COMPLETED GAMES (exact margins verified against Wikipedia official PDs!)
    # Format: (team_a, team_b, margin_a_minus_b, stage, hca_a)
    # Note: hca_a = +1 if team_a is host Japan in Nagoya, -1 if team_b is Japan, 0 otherwise
    games = [
        # Group A
        ("South Korea", "Saudi Arabia", 16.0, "G", 0),
        ("South Korea", "Indonesia", 54.0, "G", 0),
        ("South Korea", "Japan", 17.0, "G", -1),
        ("Japan", "Indonesia", 45.0, "G", 1),
        ("Japan", "Saudi Arabia", 6.0, "G", 1),
        ("Saudi Arabia", "Indonesia", 11.0, "G", 0),
        # Group B
        ("Qatar", "Iran", 6.0, "G", 0),
        ("Iran", "Chinese Taipei", 3.0, "G", 0),
        ("Iran", "Jordan", 13.0, "G", 0),
        ("Chinese Taipei", "Jordan", 3.0, "G", 0),
        ("Chinese Taipei", "Qatar", 22.0, "G", 0),
        ("Jordan", "Qatar", 11.0, "G", 0),
        # Group C
        ("China", "Kazakhstan", 38.0, "G", 0),
        ("China", "Bahrain", 46.0, "G", 0),
        ("China", "Philippines", 44.0, "G", 0),
        ("Bahrain", "Philippines", 4.0, "G", 0),
        ("Bahrain", "Kazakhstan", 23.0, "G", 0),
        ("Philippines", "Kazakhstan", 31.0, "G", 0),
        # Quarterfinals (Wed Sep 16)
        ("Japan", "Chinese Taipei", 7.0, "QF", 1),
        ("China", "Saudi Arabia", 9.0, "QF", 0),
        ("South Korea", "Jordan", 34.0, "QF", 0),
        ("Iran", "Bahrain", 5.0, "QF", 0),
        # Semifinals (Fri Sep 18)
        ("South Korea", "Iran", 26.0, "SF", 0),
        ("Japan", "China", 20.0, "SF", 1),
    ]

    # Pre-tournament FIBA / Roster prior (strength relative to 12-team field mean)
    # Note: Official Sep 17 rosters show Iran is MISSING Yakhchali, Vahedi, Amini, Mashayekhi!
    # China has Hu Jinqiu, Yu Jiahao, Cui Yongxi, Hu Mingxuan, Liao Sanning, Wang Junjie, Li Hongquan (returned!).
    prior_mu = np.array([
        18.0,  # China (Asian Cup silver core, missing Zhu Junlong/Zhao Jiayi in QF; Li Hongquan returned!)
        12.0,  # South Korea (full A-team w/ Lee Hyun-jung, Choi Jun-yong)
        10.0,  # Japan (B.League/college squad + Alex Kirk, Kanechika, Harper Jr.)
         4.0,  # Iran (severely depleted — no Yakhchali/Vahedi/Amini; led by 35yo Jamshidi & 36yo Kazemi)
         3.0,  # Chinese Taipei
         0.0,  # Jordan
        -4.0,  # Saudi Arabia
        -6.0,  # Bahrain
        -5.0,  # Qatar
        -6.0,  # Philippines (PBA B-team)
       -13.0,  # Indonesia
       -13.0,  # Kazakhstan
    ])

    def fit_bayesian_massey(cap=28.0, w_qf=1.5, w_sf=2.0, hca_jpn=3.5, prior_prec=0.25, game_sd=11.5):
        # Posterior precision & linear system: (X^T W X + P0) theta = X^T W y + P0 mu0
        X = []
        y = []
        W = []
        for ta, tb, m, st, hca in games:
            row = np.zeros(n_t)
            row[idx[ta]] = 1.0
            row[idx[tb]] = -1.0
            # Apply soft blowout cap (linear up to cap, then sqrt compression)
            sgn = 1.0 if m >= 0 else -1.0
            am = abs(m)
            cm = am if am <= cap else cap + 0.35 * (am - cap)
            m_adj = sgn * cm - hca * hca_jpn
            w = 1.0 if st == "G" else (w_qf if st == "QF" else w_sf)
            X.append(row)
            y.append(m_adj)
            W.append(w / (game_sd ** 2))
        X = np.array(X)
        y = np.array(y)
        W_mat = np.diag(W)
        # Prior precision: prior_prec * (1 / game_sd^2) equivalent to `prior_prec` pseudo-games
        P0 = np.eye(n_t) * (prior_prec / (game_sd ** 2))
        # Also tiny anchor so sum(theta)=0 is well-conditioned
        A = X.T @ W_mat @ X + P0
        b = X.T @ W_mat @ y + P0 @ prior_mu
        cov = np.linalg.inv(A)
        theta = cov @ b
        return theta, cov

    specs = [
        ("M1: Pure Connected Graph (Uncapped, Equal Weights, Weak Prior)",       99.0, 1.0, 1.0, 3.0, 0.05, 11.5),
        ("M2: Margin-Capped (25pt) + Moderate KO Weight (1.5/2.0) + HCA 3.5",    25.0, 1.5, 2.0, 3.5, 0.25, 11.5),
        ("M3: Heavy KO Recency (QF=2.0, SF=3.0) + Cap 22pt + HCA 3.0",           22.0, 2.0, 3.0, 3.0, 0.20, 11.5),
        ("M4: Heavy KO + Zero Japan HCA (worst-case for China SF collapse)",     22.0, 2.0, 3.5, 0.0, 0.15, 11.5),
        ("M5: Roster Prior Regularized (prior_prec=0.60) + Cap 25pt + HCA 3.5",  25.0, 1.5, 2.0, 3.5, 0.60, 11.5),
    ]

    # Blend weights across models + Student-t fat-tailed single-game simulation (df=8, slow-pace Iran adjustment)
    # Slow-pace adjustment: Iran games average ~133 total pts vs typical 155 -> scale spread by ~0.92, game_sd ~10.8
    # Plus subtle China morale/injury uncertainty (-1.0 pt slight discount in pessimistic draws)
    rng = np.random.default_rng(6734818)
    model_weights = [0.10, 0.35, 0.25, 0.10, 0.20]
    total_p_china = 0.0

    for (name, cap, wq, ws, hca, pp, gsd), mw in zip(specs, model_weights):
        theta, cov = fit_bayesian_massey(cap, wq, ws, hca, pp, gsd)
        c_i, ir_i = idx["China"], idx["Iran"]
        diff_mu = theta[c_i] - theta[ir_i]
        diff_var = cov[c_i, c_i] + cov[ir_i, ir_i] - 2.0 * cov[c_i, ir_i]
        diff_se = math.sqrt(diff_var)

        # Simulate 100k games with Student-t(df=8) noise & Iran slow-pace compression (0.92x spread, sd=10.8)
        n_sim = 100000
        true_spread = rng.normal(diff_mu * 0.92, diff_se * 0.92, n_sim)
        # Extra 0.8 pt bronze-game uncertainty / China injury/morale variance (mean -0.5, sd 2.5)
        situational = rng.normal(-0.5, 2.5, n_sim)
        # Student-t noise scaled so std = 10.8 (var of t_df is df/(df-2) = 8/6 = 1.333)
        game_noise = rng.standard_t(df=8, size=n_sim) * (10.8 / math.sqrt(8.0 / 6.0))
        margin = true_spread + situational + game_noise
        p_chn = float(np.mean(margin > 0.0))
        total_p_china += mw * p_chn

        print(f"\n  [{mw:.2f}] {name}")
        print(f"        Ratings: KOR={theta[idx['South Korea']]:+.1f}, JPN={theta[idx['Japan']]:+.1f}, "
              f"CHN={theta[c_i]:+.1f}, IRN={theta[ir_i]:+.1f}, TPE={theta[idx['Chinese Taipei']]:+.1f}")
        print(f"        China - Iran raw spread = {diff_mu:+.2f} +/- {diff_se:.2f} -> Pace-adj P(China) = {p_chn:.4f}")

    print(f"\n  >>> BLENDED POST-SF PROBABILITY (qid=67348): China = {total_p_china:.4f}, Iran = {1-total_p_china:.4f}")

    # Direct sensitivity table by expected China point spread (assuming game SD = 11.2, df=8)
    print("\n  Sensitivity by China true expected spread (game SD = 11.2, Student-t df=8):")
    for sp in [4.0, 6.0, 8.0, 10.0, 12.0, 14.0]:
        sim_m = sp + rng.standard_t(df=8, size=200000) * (11.2 / math.sqrt(8.0 / 6.0))
        print(f"    Spread China -{sp:4.1f}: P(China) = {np.mean(sim_m > 0):.4f}, P(Iran) = {np.mean(sim_m <= 0):.4f}")


# ==============================================================================
# MODEL 2: Q2 (qid=784475) — COPENHAGEN 2026 WRRC WOMEN'S HALF MARATHON (SUN SEP 20)
# ==============================================================================
# NEW SEP 17-18 FACTS:
#   1. DMI Weather Forecast (ekstrabladet.dk Sep 17): 14-18C (great temp), RAIN SHOWERS & WIND Sunday!
#      Sparta CEO explicitly warns: wind makes drafting/group tactics critical -> higher tactical probability (~62%)!
#   2. Agnes Jebet Ngetich (KEN): At Copenhagen press conf Sep 18 (healthy! DNS drops to ~1.5%).
#      2026 monster form: World XC gold by 42s, 28:58 10k WL, 8:08.95 3000m WL (July -> elite closing speed too!).
#      Only blemish: NYC Half March fade to 13th (1:10:25) after ambitious early pace -> slight headwind blowup risk!
#   3. Tsigie Gebreselama (ETH): 1:04:21 PB, 1:04:48 2026 SB winning Lisbon Half (fastest 2026 entrant!),
#      4th Riga 2023, 2023 World XC silver -> PROVEN 2026 sharp form + pack/XC toughness!
#   4. Lilian Kasait Rengeruk (KEN): 1:03:32 PB (2024 Valencia), 2023 Riga 5km silver, 2024 World XC silver.
#      FLAGGED by spnafricanews Sep 17-18: best times were TWO YEARS AGO (2024), NOT among the 2026 in-form runners!
#      -> Keep huge ceiling (1:03:32 + kick), but widen form uncertainty / slight rust shift (+12s mean, higher sd).
#   5. Ftaw Zeray (ETH): MAJOR CORRECTION! Won 2026 Paris Half in PB of 1:05:12 (NOT 1:06:04!) — 52 sec faster!
#      6th at Riga 2023 WRRC HM. Named in top-4 by ALL previews (Athletics Weekly, Leichtathletik, SPN Africa).
#   6. Daisilah Jerono (KEN): 1:05:21 PB (Berlin March 2026) + Aug 2026 Cape Town 10k PB in tough conditions!
#      Explicitly singled out by SPN Africa Sep 17-18 ahead of Veronica Loleo (also Berlin PB ~1:05:30s).
#   7. Rest of field: Klara Lukan (SLO, 29:51 Eur 10k rec Apr 2026), Weini Kelati (USA), Rebecca Chelangat (UGA),
#      Julia Paternain (URU), Glenrose Xaba (RSA), other ETH/ERI/NOR runners.
def model_q2_copenhagen_hm_sep18():
    print("\n" + "=" * 74)
    print("MODEL 2: qid=784475 — Copenhagen 2026 WRRC Women's Half Marathon (SEP 18)")
    print("=" * 74)

    # 1:03:00=3780, 1:04:00=3840, 1:05:00=3900, 1:06:00=3960
    # (name, p_start, honest_mu, tactical_kick_bonus, honest_sd, bad_day_prob)
    athletes = [
        ("Agnes Jebet Ngetich",    0.985, 3812, -12, 42, 0.085),  # 8:08.95 3000m speed! Slight wind/NYC blowup risk (8.5%)
        ("Tsigie Gebreselama",     0.985, 3856, -15, 42, 0.055),  # 1:04:48 Lisbon 2026 SB, sharp XC/pack runner!
        ("Lilian Kasait Rengeruk", 0.980, 3860, -16, 52, 0.080),  # 1:03:32 2024 PB, elite kick, higher 2026-form variance!
        ("Ftaw Zeray",             0.985, 3892,  -9, 46, 0.060),  # 1:05:12 Paris 2026 winner! Huge upgrade from 3932s!
        ("Daisilah Jerono",        0.985, 3912,  -8, 48, 0.060),  # 1:05:21 Berlin + Aug Cape Town 10k PB!
        ("Veronica Loleo",         0.985, 3918,  -7, 48, 0.060),  # Berlin PB behind Amebaw
        ("Klara Lukan",            0.985, 3948, -10, 50, 0.060),  # 29:51 Eur 10k record Apr 2026
        ("Weini Kelati",           0.985, 3960,  -8, 50, 0.060),
        ("Rebecca Chelangat",      0.985, 3965,  -6, 52, 0.060),
        ("Ethiopia_Other_Best",    0.985, 3965,  -6, 55, 0.060),
        ("Rest_of_Field_Best",     0.990, 3965,  -8, 52, 0.060),
    ]

    rng = random.Random(78447518)
    n_sims = 250000
    wins = Counter()
    wins_tac = Counter()
    wins_hon = Counter()
    n_tac = 0
    n_hon = 0

    for _ in range(n_sims):
        # Windy + rainy DMI forecast + women-only (no pacers) -> 62% tactical pack race, 38% honest/hard pace
        tactical = rng.random() < 0.62
        if tactical:
            n_tac += 1
        else:
            n_hon += 1
        best_t = 1e9
        winner = None
        for name, p_ok, mu_h, kick, sd, p_bad in athletes:
            if rng.random() > p_ok:
                continue
            if tactical:
                # Windy pack compresses gaps to 48% of honest gaps + closing kick matters
                mu = 3960 + 0.48 * (mu_h - 3812) + kick
                eff_sd = sd * 0.72
            else:
                mu = mu_h
                eff_sd = sd
            bad = rng.uniform(70, 170) if rng.random() < p_bad else 0.0
            t = rng.gauss(mu, eff_sd) + bad
            if t < best_t:
                best_t = t
                winner = name
        wins[winner] += 1
        if tactical:
            wins_tac[winner] += 1
        else:
            wins_hon[winner] += 1

    print(f"  250k Blended Honest(38%)/Windy-Tactical(62%) MC:")
    print(f"  {'Athlete':25s} {'Overall':>9s} {'Honest':>9s} {'Tactical':>9s}")
    for name, cnt in wins.most_common(9):
        print(f"  {name:25s} {cnt/n_sims:9.4f} {wins_hon[name]/n_hon:9.4f} {wins_tac[name]/n_tac:9.4f}")
    top5 = wins.most_common(5)
    print(f"  Top-5 sum = {sum(c for _, c in top5)/n_sims:.4f}, Outside = {1 - sum(c for _, c in top5)/n_sims:.4f}")


# ==============================================================================
# MODEL 3: Q7 (qid=889545) — ASIAN GAMES MEN'S FOOTBALL (POST-FRI SEP 18 MD2 C/D)
# ==============================================================================
# COMPLETED MATCHES (9 of 21 group matches played!):
#   Group A MD1 (Sep 15): Japan 2-0 Hong Kong; Thailand 3-2 Kyrgyzstan
#   Group B MD1 (Sep 16): Iran 3-1 UAE; China 2-1 North Korea
#   Group C MD1 (Sep 15): Uzbekistan 5-1 Philippines; Vietnam 1-1 Kuwait
#   Group C MD2 (Sep 18): Vietnam 2-0 Philippines [PHI ELIMINATED!]; Uzbekistan 2-0 Kuwait [UZB CLINCHED QF! Fayzullaev red card!]
#   Group D MD1 (Sep 15): South Korea 4-1 Qatar
#   Group D MD2 (Sep 18): Saudi Arabia 2-0 Qatar [QAT ELIMINATED! KOR & KSA CLINCHED QF!]
def model_q7_ag_football_sep18():
    print("\n" + "=" * 74)
    print("MODEL 3: qid=889545 — Asian Games Men's Football (POST-SEP 18 GROUP C/D)")
    print("=" * 74)
    rng = np.random.default_rng(20260918)

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

    def rank_group(teams, matches, h2h_first=False):
        pts = {t: 0 for t in teams}
        gd = {t: 0 for t in teams}
        gf = {t: 0 for t in teams}
        h2h = {}
        for a, b, ga, gb in matches:
            gf[a] += ga; gf[b] += gb
            gd[a] += (ga - gb); gd[b] += (gb - ga)
            if ga > gb:
                pts[a] += 3; h2h[(a, b)] = 1; h2h[(b, a)] = -1
            elif gb > ga:
                pts[b] += 3; h2h[(a, b)] = -1; h2h[(b, a)] = 1
            else:
                pts[a] += 1; pts[b] += 1; h2h[(a, b)] = 0; h2h[(b, a)] = 0
        order = sorted(teams, key=lambda t: (pts[t], gd[t], gf[t], rng.random()), reverse=True)
        if h2h_first:
            # Swap adjacent exact 2-team point ties by H2H (check it's truly a 2-team tie)
            for i in range(len(order) - 1):
                t1, t2 = order[i], order[i + 1]
                if pts[t1] == pts[t2]:
                    tied = [t for t in order if pts[t] == pts[t1]]
                    if len(tied) == 2 and h2h.get((t2, t1), 0) > 0:
                        order[i], order[i + 1] = order[i + 1], order[i]
        return order

    # Slight updates after Fri Sep 18:
    # - Uzbekistan won 2-0 vs Kuwait playing 42 min w/ 10 men -> bump 1655 -> 1665 (but -15 for MD3 vs VIE due to Fayzullaev red card)
    # - Saudi Arabia beat Qatar 2-0 cleanly -> bump 1615 -> 1620
    # - Vietnam beat Philippines 2-0 -> 1520
    regimes = [
        ("R1: Post-Sep18 Base (IRN 1610, CHN 1575, UZB 1665, KSA 1620)", 0.50, {
            "South Korea": 1720, "Japan": 1685, "Uzbekistan": 1665, "Saudi Arabia": 1620,
            "Iran": 1610, "China": 1575, "North Korea": 1545, "United Arab Emirates": 1525,
            "Vietnam": 1520, "Thailand": 1515, "Qatar": 1495, "Kuwait": 1460,
            "Kyrgyzstan": 1445, "Hong Kong": 1390, "Philippines": 1335,
        }),
        ("R2: China Underlying-xG Regression (CHN 1535, IRN 1625, PRK 1565, UAE 1540)", 0.28, {
            "South Korea": 1725, "Japan": 1690, "Uzbekistan": 1670, "Saudi Arabia": 1620,
            "Iran": 1625, "China": 1535, "North Korea": 1565, "United Arab Emirates": 1540,
            "Vietnam": 1520, "Thailand": 1515, "Qatar": 1495, "Kuwait": 1460,
            "Kyrgyzstan": 1445, "Hong Kong": 1390, "Philippines": 1335,
        }),
        ("R3: China Clinical Counterattack Shines (CHN 1610, IRN 1595, JPN U21 1655)", 0.22, {
            "South Korea": 1705, "Japan": 1655, "Uzbekistan": 1655, "Saudi Arabia": 1610,
            "China": 1610, "Iran": 1595, "North Korea": 1535, "United Arab Emirates": 1515,
            "Vietnam": 1520, "Thailand": 1510, "Qatar": 1495, "Kuwait": 1460,
            "Kyrgyzstan": 1445, "Hong Kong": 1390, "Philippines": 1335,
        }),
    ]

    n_trials = 40000
    total_elim = Counter()
    grp_c1 = Counter()
    grp_d1 = Counter()

    for rname, w_reg, base_r in regimes:
        elim = Counter()
        for _ in range(n_trials):
            r = {t: v + rng.normal(0, 32.0) for t, v in base_r.items()}
            h2h_flag = (rng.random() < 0.5)  # 50/50 blend GD-first vs H2H-first tiebreaker uncertainty

            # Group A (MD1 fixed)
            gA = ["Japan", "Thailand", "Kyrgyzstan", "Hong Kong"]
            mA = [
                ("Japan", "Hong Kong", 2, 0),
                ("Thailand", "Kyrgyzstan", 3, 2),
                ("Hong Kong", "Thailand", *sim_match_goals(r["Hong Kong"], r["Thailand"])),
                ("Kyrgyzstan", "Japan", *sim_match_goals(r["Kyrgyzstan"], r["Japan"])),
                ("Japan", "Thailand", *sim_match_goals(r["Japan"], r["Thailand"])),
                ("Kyrgyzstan", "Hong Kong", *sim_match_goals(r["Kyrgyzstan"], r["Hong Kong"])),
            ]
            ordA = rank_group(gA, mA, h2h_first=h2h_flag)

            # Group C (MD1 + MD2 FIXED!)
            gC = ["Vietnam", "Uzbekistan", "Philippines", "Kuwait"]
            mC = [
                ("Uzbekistan", "Philippines", 5, 1),
                ("Vietnam", "Kuwait", 1, 1),
                ("Vietnam", "Philippines", 2, 0),
                ("Uzbekistan", "Kuwait", 2, 0),
                ("Vietnam", "Uzbekistan", *sim_match_goals(r["Vietnam"], r["Uzbekistan"] - 15.0)),  # Fayzullaev red card
                ("Philippines", "Kuwait", *sim_match_goals(r["Philippines"], r["Kuwait"])),
            ]
            ordC = rank_group(gC, mC, h2h_first=h2h_flag)
            grp_c1[ordC[0]] += w_reg / n_trials

            # Group D (MD1 + MD2 FIXED! Qatar eliminated!)
            gD = ["South Korea", "Saudi Arabia", "Qatar"]
            mD = [
                ("South Korea", "Qatar", 4, 1),
                ("Saudi Arabia", "Qatar", 2, 0),
                ("South Korea", "Saudi Arabia", *sim_match_goals(r["South Korea"], r["Saudi Arabia"])),
            ]
            ordD = rank_group(gD, mD, h2h_first=h2h_flag)
            grp_d1[ordD[0]] += w_reg / n_trials

            # Group B (MD1 fixed)
            gB = ["China", "United Arab Emirates", "Iran", "North Korea"]
            mB = [
                ("China", "North Korea", 2, 1),
                ("Iran", "United Arab Emirates", 3, 1),
                ("Iran", "China", *sim_match_goals(r["Iran"], r["China"])),
                ("North Korea", "United Arab Emirates", *sim_match_goals(r["North Korea"], r["United Arab Emirates"])),
                ("China", "United Arab Emirates", *sim_match_goals(r["China"], r["United Arab Emirates"])),
                ("Iran", "North Korea", *sim_match_goals(r["Iran"], r["North Korea"])),
            ]
            ordB = rank_group(gB, mB, h2h_first=h2h_flag)
            c_pos = ordB.index("China") + 1
            if c_pos >= 3:
                elim["United Arab Emirates"] += 1
                continue

            r_ko = dict(r)
            for t in gD:
                r_ko[t] += 15.0  # Group D plays 1 fewer match

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
                continue

            sfs = [(qf_w[0], qf_w[3]), (qf_w[1], qf_w[2])]
            sf_w = []
            for t1, t2 in sfs:
                w = sim_knockout_winner(t1, t2, r_ko)
                sf_w.append(w)
                if "China" in (t1, t2) and w != "China":
                    killer = w
            if killer is not None:
                elim[killer] += 1
                continue

            gold = sim_knockout_winner(sf_w[0], sf_w[1], r_ko)
            if gold == "China":
                elim["None"] += 1
            else:
                elim[gold] += 1

        for k, v in elim.items():
            total_elim[k] += w_reg * (v / n_trials)

    print("  Group C Winner: " + ", ".join(f"{k}={v:.3f}" for k, v in grp_c1.most_common(3)))
    print("  Group D Winner: " + ", ".join(f"{k}={v:.3f}" for k, v in grp_d1.most_common(3)))
    print("  Ranked Eliminators (vs prev: Japan 0.28, UAE 0.24, South Korea 0.155, Thailand 0.12, Uzbekistan 0.06):")
    for k, p in total_elim.most_common(12):
        print(f"    {k:22s}: {p:.4f}")
    top5_sum = sum(p for _, p in total_elim.most_common(5))
    print(f"  Top-5 sum = {top5_sum:.4f}, Outside = {1-top5_sum:.4f}")


if __name__ == "__main__":
    model_q1_china_vs_iran_basketball()
    model_q2_copenhagen_hm_sep18()
    model_q7_ag_football_sep18()
