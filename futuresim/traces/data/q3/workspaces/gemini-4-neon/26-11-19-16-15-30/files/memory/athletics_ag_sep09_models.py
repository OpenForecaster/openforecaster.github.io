import numpy as np

rng = np.random.default_rng(20260909)

# ==============================================================================
# PART 1: Q4 (qid=889545) — 2026 ASIAN GAMES MEN'S FOOTBALL (EXACT 15-TEAM SIM)
# ==============================================================================
# Official Groups (15 teams, Iraq withdrew; top 2 per group -> QF):
#   Group A: Japan (U-21, hosts), Thailand, Kyrgyzstan, Hong Kong
#   Group B: China (U23 Asian Cup silver core + 3 senior wildcards: Zhang Yuning, Zhu Chenjie, Wu Xi + Wolves U21 Xu Bin),
#            United Arab Emirates, Iran, North Korea
#   Group C: Vietnam, Uzbekistan, Philippines, Kuwait
#   Group D: South Korea (U23 + 4 WC players + 9 Europe-based incl. Yang Hyun-jun, Eom Ji-sung, Lee Gi-hyuk, Bae Jun-ho, Kim Ji-soo),
#            Saudi Arabia, Qatar
#
# Official Confirmed Group B Schedule (borna.news, mehrnews, tehrantimes, globaltimes):
#   MD1 (Sep 16): China vs North Korea; UAE vs Iran
#   MD2 (Sep 20): China vs Iran; UAE vs North Korea
#   MD3 (Sep 23): China vs UAE; Iran vs North Korea
#
# Resolution Criteria (qid=889545):
#   "Identify the opposing national team in the match that eliminates China from contention
#    for the men's football gold medal. Any subsequent bronze-medal match is excluded.
#    If China wins gold, resolve to no country." -> "None" if China wins gold.

def sim_match_goals(att_a, att_b, base_goals=1.22):
    """Poisson goals from team ratings (scale ~100 pts = ~0.35 log-goal ratio)."""
    diff = (att_a - att_b) / 100.0
    lam_a = base_goals * np.exp(0.28 * diff)
    lam_b = base_goals * np.exp(-0.28 * diff)
    ga = rng.poisson(lam_a)
    gb = rng.poisson(lam_b)
    return int(ga), int(gb)

def sim_knockout_winner(t1, t2, ratings):
    """Simulate knockout match (90 min + ET + penalties). Returns winning team name."""
    g1, g2 = sim_match_goals(ratings[t1], ratings[t2], base_goals=1.18)
    if g1 > g2:
        return t1
    if g2 > g1:
        return t2
    # Extra time (30 min ~ 1/3 scoring rate)
    e1, e2 = sim_match_goals(ratings[t1], ratings[t2], base_goals=0.38)
    if e1 > e2:
        return t1
    if e2 > e1:
        return t2
    # Penalties (slight skill edge, mostly 50/50)
    p1 = 0.5 + 0.03 * np.tanh((ratings[t1] - ratings[t2]) / 150.0)
    return t1 if rng.random() < p1 else t2

def rank_group(teams, matches):
    """Rank teams by Points -> GD -> GF -> H2H -> random tiebreak."""
    pts = {t: 0 for t in teams}
    gd = {t: 0 for t in teams}
    gf = {t: 0 for t in teams}
    for a, b, ga, gb in matches:
        gf[a] += ga; gf[b] += gb
        gd[a] += (ga - gb); gd[b] += (gb - ga)
        if ga > gb:
            pts[a] += 3
        elif gb > ga:
            pts[b] += 3
        else:
            pts[a] += 1; pts[b] += 1
    order = sorted(teams, key=lambda t: (pts[t], gd[t], gf[t], rng.random()), reverse=True)
    return order, pts, gd, gf

def is_china_eliminated_after_md2(pts2, gd2):
    """Check if China is mathematically eliminated from top-2 of Group B after MD2.
    Schedule remaining on MD3: China vs UAE, Iran vs North Korea.
    China can gain at most +3 points (total max_c = pts2['China'] + 3).
    Note: Any team ALREADY strictly > max_c is guaranteed ahead of China.
    Even stronger: in Iran vs North Korea, the higher-finishing of {Iran, PRK} will end with
    at least max(pts2['Iran'], pts2['North Korea']) + 1 if they are tied, or >= max if not.
    Actually we can check exact feasibility over the 3x3 outcomes of MD3!"""
    # Check if there exists ANY outcome of (CHN vs UAE) and (IRN vs PRK) where China finishes top 2
    # (allowing tie on points to count as alive unless China's max pts < 2 teams' guaranteed pts)
    for res_cu in [(3, 0), (1, 1), (0, 3)]:  # CHN, UAE
        for res_ip in [(3, 0), (1, 1), (0, 3)]:  # IRN, PRK
            fin = {
                "China": pts2["China"] + res_cu[0],
                "United Arab Emirates": pts2["United Arab Emirates"] + res_cu[1],
                "Iran": pts2["Iran"] + res_ip[0],
                "North Korea": pts2["North Korea"] + res_ip[1],
            }
            strictly_ahead = sum(1 for k, v in fin.items() if k != "China" and v > fin["China"])
            if strictly_ahead < 2:
                return False  # China still has a mathematical path to top 2!
    return True

def run_ag_simulation(n_trials=120_000):
    # Strength regimes (calibrated to 2026 U23 Asian Cup + confirmed overage wildcards & home advantage):
    #   - South Korea: stacked (4 WC players, 9 Europe-based, 3 strong wildcards, military exemption motivation, only 2 group matches)
    #   - Japan: home advantage in Aichi-Nagoya, U-21 Go Oiwa squad (beat China U23 4-0 & Korea U23 1-0 in Jan 2026 Asian Cup!)
    #   - Uzbekistan: perennial Asian U23 superpower
    #   - Saudi Arabia: top Gulf U23 power
    #   - China: Jan 2026 U23 Asian Cup silver medal core + Antonio Puche + senior wildcards Zhang Yuning, Zhu Chenjie, Wu Xi + Xu Bin
    #   - Iran: strong Omid U23 squad (tough physical side)
    #   - UAE: solid Gulf U23 side
    #   - North Korea: gritty, organized Asian Games regular
    #   - Qatar, Vietnam, Thailand: solid competitive Asian U23 sides
    regimes = [
        # Regime 1 (45%): Base Calibrated (China boosted by senior stars & silver core, Group B still tough)
        ("R1: Base Calibrated (China strong ~1575; Group B tough)", 0.45, {
            "South Korea": 1705, "Japan": 1685, "Uzbekistan": 1645, "Saudi Arabia": 1615,
            "China": 1575, "Iran": 1575, "United Arab Emirates": 1545, "Qatar": 1545,
            "North Korea": 1525, "Vietnam": 1530, "Thailand": 1515,
            "Kyrgyzstan": 1435, "Kuwait": 1445, "Hong Kong": 1390, "Philippines": 1350,
        }),
        # Regime 2 (30%): Group B Dogfight / China Overhyped (Jan 2026 silver was fluke; Wu Xi 37yo slow; Iran/UAE strong wildcards)
        ("R2: China Regression / Group B Brutal (China ~1530)", 0.30, {
            "South Korea": 1710, "Japan": 1690, "Uzbekistan": 1650, "Saudi Arabia": 1615,
            "China": 1530, "Iran": 1595, "United Arab Emirates": 1575, "Qatar": 1545,
            "North Korea": 1545, "Vietnam": 1525, "Thailand": 1515,
            "Kyrgyzstan": 1435, "Kuwait": 1445, "Hong Kong": 1390, "Philippines": 1350,
        }),
        # Regime 3 (25%): China All-In Senior Spine Shines (China best in Group B ~1610; Japan U21 slightly vulnerable to senior wildcards)
        ("R3: China Senior Spine Shines (China ~1610; Japan U21 ~1650)", 0.25, {
            "South Korea": 1695, "Japan": 1650, "Uzbekistan": 1635, "Saudi Arabia": 1605,
            "China": 1610, "Iran": 1560, "United Arab Emirates": 1535, "Qatar": 1540,
            "North Korea": 1510, "Vietnam": 1530, "Thailand": 1510,
            "Kyrgyzstan": 1435, "Kuwait": 1445, "Hong Kong": 1390, "Philippines": 1350,
        }),
    ]

    # Bracket structures (uncertainty over official OCA 2026 QF/SF crossover):
    #   B_CANON (0.75): Canonical AFC U23 / Olympic 4-group bracket:
    #       QF1: 1A vs 2B, QF2: 1B vs 2A, QF3: 1C vs 2D, QF4: 1D vs 2C
    #       SF1: W(QF1) vs W(QF3), SF2: W(QF2) vs W(QF4)
    #   B_SAME_HALF (0.13): Same QFs (A-B, C-D), but SF1: W(1A v 2B) vs W(1B v 2A)
    #   B_ALT_BC (0.06): Alternate QF crossover: B-C / A-D (1B v 2C, 1C v 2B, 1A v 2D, 1D v 2A)
    #   B_ALT_BD (0.06): Alternate QF crossover: B-D / A-C (1B v 2D, 1D v 2B, 1A v 2C, 1C v 2A)
    bracket_probs = [0.75, 0.13, 0.06, 0.06]
    bracket_cum = np.cumsum(bracket_probs)

    total_elim = {}
    stage_stats = {"MD2_IRN": 0.0, "MD3_UAE": 0.0, "QF": 0.0, "SF": 0.0, "FIN": 0.0, "GOLD": 0.0}
    pos_stats = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}

    for rname, weight, base_r in regimes:
        elim = {}
        r_stage = {k: 0 for k in stage_stats}
        r_pos = {1: 0, 2: 0, 3: 0, 4: 0}

        for _ in range(n_trials):
            # Per-tournament team form noise (sd=35 Elo pts -> captures real tournament variance!)
            r = {t: v + rng.normal(0, 35.0) for t, v in base_r.items()}

            # Group A: Japan, Thailand, Kyrgyzstan, Hong Kong
            gA = ["Japan", "Thailand", "Kyrgyzstan", "Hong Kong"]
            mA = []
            for i in range(4):
                for j in range(i + 1, 4):
                    ga, gb = sim_match_goals(r[gA[i]], r[gA[j]])
                    mA.append((gA[i], gA[j], ga, gb))
            ordA, _, _, _ = rank_group(gA, mA)

            # Group C: Vietnam, Uzbekistan, Philippines, Kuwait
            gC = ["Vietnam", "Uzbekistan", "Philippines", "Kuwait"]
            mC = []
            for i in range(4):
                for j in range(i + 1, 4):
                    ga, gb = sim_match_goals(r[gC[i]], r[gC[j]])
                    mC.append((gC[i], gC[j], ga, gb))
            ordC, _, _, _ = rank_group(gC, mC)

            # Group D (3 teams): South Korea, Saudi Arabia, Qatar
            gD = ["South Korea", "Saudi Arabia", "Qatar"]
            mD = []
            for i in range(3):
                for j in range(i + 1, 3):
                    ga, gb = sim_match_goals(r[gD[i]], r[gD[j]])
                    mD.append((gD[i], gD[j], ga, gb))
            ordD, _, _, _ = rank_group(gD, mD)

            # Group B (EXACT confirmed matchday order!)
            gB = ["China", "United Arab Emirates", "Iran", "North Korea"]
            # MD1: China vs North Korea; UAE vs Iran
            c1, p1 = sim_match_goals(r["China"], r["North Korea"])
            u1, i1 = sim_match_goals(r["United Arab Emirates"], r["Iran"])
            # MD2: China vs Iran; UAE vs North Korea
            c2, i2 = sim_match_goals(r["China"], r["Iran"])
            u2, p2 = sim_match_goals(r["United Arab Emirates"], r["North Korea"])
            mB_md2 = [
                ("China", "North Korea", c1, p1),
                ("United Arab Emirates", "Iran", u1, i1),
                ("China", "Iran", c2, i2),
                ("United Arab Emirates", "North Korea", u2, p2),
            ]
            _, pts2, gd2, _ = rank_group(gB, mB_md2)
            elim_md2 = is_china_eliminated_after_md2(pts2, gd2)

            # MD3: China vs UAE; Iran vs North Korea
            c3, u3 = sim_match_goals(r["China"], r["United Arab Emirates"])
            i3, p3 = sim_match_goals(r["Iran"], r["North Korea"])
            mB_all = mB_md2 + [
                ("China", "United Arab Emirates", c3, u3),
                ("Iran", "North Korea", i3, p3),
            ]
            ordB, _, _, _ = rank_group(gB, mB_all)
            c_pos = ordB.index("China") + 1
            r_pos[c_pos] += 1

            if c_pos >= 3:
                if elim_md2:
                    # Slight ~15% edge-case chance resolver credits MD3 UAE even if mathematically out on MD2
                    if rng.random() < 0.85:
                        killer = "Iran"
                        r_stage["MD2_IRN"] += 1
                    else:
                        killer = "United Arab Emirates"
                        r_stage["MD3_UAE"] += 1
                else:
                    killer = "United Arab Emirates"
                    r_stage["MD3_UAE"] += 1
                elim[killer] = elim.get(killer, 0) + 1
                continue

            # China advanced to Quarterfinals!
            # Group D teams have 1 fewer match (slight +15 Elo freshness edge in KO)
            r_ko = dict(r)
            for t in gD:
                r_ko[t] += 15.0

            ub = rng.random()
            if ub < bracket_cum[0]:
                # Canonical AFC/Olympic: 1A v 2B -> SF vs 1C v 2D; 1B v 2A -> SF vs 1D v 2C
                qfs = [(ordA[0], ordB[1]), (ordB[0], ordA[1]), (ordC[0], ordD[1]), (ordD[0], ordC[1])]
                sf_pairs = [(0, 2), (1, 3)]
            elif ub < bracket_cum[1]:
                # Same-half A-B
                qfs = [(ordA[0], ordB[1]), (ordB[0], ordA[1]), (ordC[0], ordD[1]), (ordD[0], ordC[1])]
                sf_pairs = [(0, 1), (2, 3)]
            elif ub < bracket_cum[2]:
                # Alt B-C / A-D
                qfs = [(ordC[0], ordB[1]), (ordB[0], ordC[1]), (ordA[0], ordD[1]), (ordD[0], ordA[1])]
                sf_pairs = [(0, 2), (1, 3)]
            else:
                # Alt B-D / A-C
                qfs = [(ordD[0], ordB[1]), (ordB[0], ordD[1]), (ordA[0], ordC[1]), (ordC[0], ordA[1])]
                sf_pairs = [(0, 2), (1, 3)]

            qf_w = []
            killer = None
            for t1, t2 in qfs:
                w = sim_knockout_winner(t1, t2, r_ko)
                qf_w.append(w)
                if "China" in (t1, t2) and w != "China":
                    killer = w
                    r_stage["QF"] += 1
            if killer:
                elim[killer] = elim.get(killer, 0) + 1
                continue

            sf_w = []
            for idx1, idx2 in sf_pairs:
                t1, t2 = qf_w[idx1], qf_w[idx2]
                w = sim_knockout_winner(t1, t2, r_ko)
                sf_w.append(w)
                if "China" in (t1, t2) and w != "China":
                    killer = w
                    r_stage["SF"] += 1
            if killer:
                elim[killer] = elim.get(killer, 0) + 1
                continue

            # Final!
            t1, t2 = sf_w[0], sf_w[1]
            w = sim_knockout_winner(t1, t2, r_ko)
            if w == "China":
                killer = "None"
                r_stage["GOLD"] += 1
            else:
                killer = w
                r_stage["FIN"] += 1
            elim[killer] = elim.get(killer, 0) + 1

        probs = {k: v / n_trials for k, v in elim.items()}
        top7 = ", ".join(f"{k}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:7])
        grp_exit = (r_pos[3] + r_pos[4]) / n_trials
        print(f"  [{rname[:58]:58s} w={weight:.2f}] GrpExit={grp_exit:.3f} (1B={r_pos[1]/n_trials:.2f},2B={r_pos[2]/n_trials:.2f}) | {top7}")
        for k, v in probs.items():
            total_elim[k] = total_elim.get(k, 0.0) + weight * v
        for k in stage_stats:
            stage_stats[k] += weight * (r_stage[k] / n_trials)
        for k in pos_stats:
            pos_stats[k] += weight * (r_pos[k] / n_trials)

    print("\n=== Q4 (qid=889545) BLENDED PROBABILITIES ===")
    print("China Group B finish probs:", {k: round(v, 4) for k, v in pos_stats.items()})
    print("Elimination stage breakdown:", {k: round(v, 4) for k, v in stage_stats.items()})
    for k, v in sorted(total_elim.items(), key=lambda x: -x[1])[:12]:
        print(f"  {k:24s}: {v:.4f}")
    top5 = sorted(total_elim.items(), key=lambda x: -x[1])[:5]
    print("Top-5:", [(k, round(v, 4)) for k, v in top5], "sum =", round(sum(v for _, v in top5), 4))
    return total_elim

print("=== RUNNING Q4 ASIAN GAMES MEN'S FOOTBALL SIMULATION ===")
run_ag_simulation(n_trials=80_000)


# ==============================================================================
# PART 2: SENSITIVITY CHECK ON Q2 (qid=261941) WOMEN'S JAVELIN (BRUSSELS FOUL EVIDENCE)
# ==============================================================================
# In Brussels Sep 5, Yan Ziyi went: X, 62.21, X, 64.95, 68.42 (took lead R4 over Kitaguchi 64.56;
# Kitaguchi threw 65.44 in R6). In Xiamen/Oslo/Paris Yan won on R1 (71.74/67.11/67.44).
# Check sensitivity if women's javelin foul rates are slightly higher (0.19-0.22 instead of 0.15)
# and Vilagos gets slight bump for her Sep 1 65.93m Mediterranean Games win!

def sim_javelin_8864_sens(regimes, n_trials=250_000):
    names = [a[0] for a in regimes[0][2]]
    k = len(names)
    blend = np.zeros(k)
    for rname, weight, athletes in regimes:
        n = n_trials
        day_mu = np.full((n, k), -999.0)
        tsd = np.zeros((n, k))
        fr = np.zeros((n, k))
        active = np.zeros((n, k), dtype=bool)
        for j, (name, states) in enumerate(athletes):
            u = rng.random(n)
            cum = 0.0
            for p, mu, dsd_v, tsd_v, fr_v in states:
                mask = (u >= cum) & (u < cum + p)
                cum += p
                if mu is not None:
                    cnt = mask.sum()
                    if cnt > 0:
                        active[mask, j] = True
                        day_mu[mask, j] = rng.normal(mu, dsd_v, cnt)
                        tsd[mask, j] = tsd_v
                        fr[mask, j] = fr_v
        best = np.zeros((n, k))
        has_valid = np.zeros((n, k), dtype=bool)
        # R1
        valid1 = active & (rng.random((n, k)) >= fr)
        best = np.maximum(best, np.where(valid1, rng.normal(day_mu, np.where(active, tsd, 1.0)), 0.0))
        has_valid |= valid1
        # R2 (safer banker if fouled R1)
        fr2 = np.where(has_valid, fr, fr * 0.55)
        mu2 = np.where(has_valid, day_mu, day_mu - 0.8)
        valid2 = active & (rng.random((n, k)) >= fr2)
        best = np.maximum(best, np.where(valid2, rng.normal(mu2, np.where(active, tsd, 1.0)), 0.0))
        has_valid |= valid2
        # Top 6
        rows = np.arange(n)[:, None]
        rank2 = np.argsort(-(best + rng.uniform(0, 1e-6, (n, k))), axis=1)
        in_top6 = np.zeros((n, k), dtype=bool)
        in_top6[rows, rank2[:, :6]] = True
        in_top6 &= active
        # R3
        valid3 = in_top6 & (rng.random((n, k)) >= fr)
        best = np.maximum(best, np.where(valid3, rng.normal(day_mu, np.where(active, tsd, 1.0)), 0.0))
        # Top 4
        rank3 = np.argsort(-(best + rng.uniform(0, 1e-6, (n, k))), axis=1)
        in_top4 = np.zeros((n, k), dtype=bool)
        in_top4[rows, rank3[:, :4]] = True
        in_top4 &= in_top6
        # R4
        valid4 = in_top4 & (rng.random((n, k)) >= fr)
        best = np.maximum(best, np.where(valid4, rng.normal(day_mu, np.where(active, tsd, 1.0)), 0.0))
        winners = np.argmax(best + rng.uniform(0, 1e-6, (n, k)), axis=1)
        probs = np.bincount(winners, minlength=k) / n
        blend += weight * probs
    return dict(zip(names, blend))

women_jav_sep09 = [
    ("R1: Base + Realistic 0.20 Foul Rate + Vilagos 65.93 Form", 0.55, [
        ("Yan Ziyi",                [(0.020, None, 0, 0, 0), (0.110, 64.7, 1.85, 1.95, 0.22), (0.870, 66.9, 1.75, 1.95, 0.20)]),
        ("Haruka Kitaguchi",        [(0.020, None, 0, 0, 0), (0.980, 63.3, 1.80, 1.90, 0.18)]),
        ("Flor Denis Ruiz Hurtado", [(0.020, None, 0, 0, 0), (0.980, 63.0, 1.90, 1.90, 0.20)]),
        ("Adriana Vilagos",         [(0.020, None, 0, 0, 0), (0.980, 62.5, 1.85, 1.85, 0.18)]),
        ("Sigrid Borge",            [(0.025, None, 0, 0, 0), (0.780, 58.8, 1.90, 1.80, 0.21), (0.195, 62.6, 1.9, 1.8, 0.21)]),
        ("Mackenzie Little",        [(0.030, None, 0, 0, 0), (0.820, 60.0, 1.70, 1.80, 0.18), (0.150, 62.8, 1.8, 1.8, 0.18)]),
        ("Tori Moorby",             [(0.020, None, 0, 0, 0), (0.980, 58.9, 1.70, 1.70, 0.19)]),
        ("Anete Sietina",           [(0.020, None, 0, 0, 0), (0.980, 58.8, 1.70, 1.80, 0.19)]),
    ]),
    ("R2: Yan Early-Round Pressure/Fouls (Brussels-like)", 0.25, [
        ("Yan Ziyi",                [(0.035, None, 0, 0, 0), (0.265, 64.3, 1.90, 2.00, 0.25), (0.700, 66.2, 1.85, 1.95, 0.22)]),
        ("Haruka Kitaguchi",        [(0.020, None, 0, 0, 0), (0.980, 63.8, 1.80, 1.90, 0.18)]),
        ("Flor Denis Ruiz Hurtado", [(0.020, None, 0, 0, 0), (0.980, 63.4, 1.90, 1.90, 0.20)]),
        ("Adriana Vilagos",         [(0.020, None, 0, 0, 0), (0.980, 63.0, 1.85, 1.85, 0.18)]),
        ("Sigrid Borge",            [(0.025, None, 0, 0, 0), (0.720, 59.1, 1.90, 1.80, 0.21), (0.255, 63.0, 1.9, 1.8, 0.21)]),
        ("Mackenzie Little",        [(0.030, None, 0, 0, 0), (0.750, 60.2, 1.70, 1.80, 0.18), (0.220, 63.2, 1.8, 1.8, 0.18)]),
        ("Tori Moorby",             [(0.020, None, 0, 0, 0), (0.980, 59.1, 1.70, 1.70, 0.19)]),
        ("Anete Sietina",           [(0.020, None, 0, 0, 0), (0.980, 59.1, 1.70, 1.80, 0.19)]),
    ]),
    ("R3: Yan One-Throw-Win 68.5m+ Form (Xiamen/Oslo/Paris/Monaco)", 0.20, [
        ("Yan Ziyi",                [(0.015, None, 0, 0, 0), (0.045, 65.5, 1.70, 1.90, 0.18), (0.940, 67.6, 1.70, 1.90, 0.16)]),
        ("Haruka Kitaguchi",        [(0.020, None, 0, 0, 0), (0.980, 63.0, 1.80, 1.90, 0.18)]),
        ("Flor Denis Ruiz Hurtado", [(0.020, None, 0, 0, 0), (0.980, 62.8, 1.90, 1.90, 0.20)]),
        ("Adriana Vilagos",         [(0.020, None, 0, 0, 0), (0.980, 62.2, 1.80, 1.85, 0.18)]),
        ("Sigrid Borge",            [(0.025, None, 0, 0, 0), (0.830, 58.6, 1.90, 1.80, 0.21), (0.145, 62.2, 1.9, 1.8, 0.21)]),
        ("Mackenzie Little",        [(0.030, None, 0, 0, 0), (0.860, 59.8, 1.70, 1.80, 0.18), (0.110, 62.4, 1.8, 1.8, 0.18)]),
        ("Tori Moorby",             [(0.020, None, 0, 0, 0), (0.980, 58.7, 1.70, 1.70, 0.19)]),
        ("Anete Sietina",           [(0.020, None, 0, 0, 0), (0.980, 58.6, 1.70, 1.80, 0.19)]),
    ]),
]

print("\n=== Q2 (qid=261941) WOMEN'S JAVELIN SENSITIVITY CHECK (SEP 9) ===")
wj = sim_javelin_8864_sens(women_jav_sep09)
for k, v in sorted(wj.items(), key=lambda x: -x[1]):
    print(f"  {k:26s}: {v:.4f}")
print("Top-5 sum:", round(sum(v for _, v in sorted(wj.items(), key=lambda x: -x[1])[:5]), 4))
