"""
Quantitative Monte Carlo Model — Sun Sep 20, 2026
qid=889545: Which country will end China's gold-medal bid in men's football at the 2026 Asian Games?

POST-SUN SEP 20 GROUP A & B MD2 RESULTS (13 of 21 group matches completed!):
  Group A:
    MD1 (Sep 16): Japan 2-0 Hong Kong; Thailand 3-2 Kyrgyzstan
    MD2 (Sep 20): Japan 7-0 Kyrgyzstan; Thailand 5-1 Hong Kong
    -> Standings: Japan 6 pts (+9 GD, 9-0), Thailand 6 pts (+5 GD, 8-3) [BOTH CLINCHED QF!]
                  Kyrgyzstan 0 pts (-8), Hong Kong 0 pts (-6) [ELIMINATED]
    -> MD3 (Sep 23): Japan vs Thailand (Japan wins A1 on Win or Draw!)
  Group B:
    MD1 (Sep 16): China 2-1 North Korea; Iran 3-1 UAE
    MD2 (Sep 20): Iran 0-0 China (Wu Xi crossbar, Iran 0 SOT, Zhu Chenjie subbed off injured; Iran Kahriz injured)
                  North Korea 0-0 UAE (Song Ri PRK RED 60' -> susp vs Iran; Khamis Al Mansouri UAE RED 90+3' -> susp vs China!)
    -> Standings: Iran 4 pts (+2 GD, 3-1), China 4 pts (+1 GD, 2-1),
                  North Korea 1 pt (-1 GD, 1-2), UAE 1 pt (-2 GD, 1-3)
    -> MD3 (Sep 23, simultaneous 13:30 CST / 14:30 JST): China vs UAE; Iran vs North Korea
  Group C (through MD2 Sep 18):
    MD1: Uzbekistan 5-1 Philippines; Vietnam 1-1 Kuwait
    MD2: Vietnam 2-0 Philippines [PHI out]; Uzbekistan 2-0 Kuwait [UZB clinched; Fayzullaev RED -> susp vs VIE]
    -> MD3 (Sep 22): Vietnam vs Uzbekistan; Philippines vs Kuwait
  Group D (through MD2 Sep 18):
    MD1: South Korea 4-1 Qatar
    MD2: Saudi Arabia 2-0 Qatar [QAT out; KOR (+3 GD) & KSA (+2 GD) BOTH CLINCHED QF!]
    -> MD3 (Sep 22): South Korea vs Saudi Arabia (KOR wins D1 on Win or Draw!)

Official OCA Knockout Bracket:
  QF1: C1 vs D2 | QF2: D1 vs C2 | QF3: B1 vs A2 | QF4: A1 vs B2
  SF1: W(QF1) vs W(QF4) | SF2: W(QF2) vs W(QF3)
  Gold Medal Final: W(SF1) vs W(SF2)  (Bronze match excluded!)

Tiebreaker Rules:
  Multiple Sep 20 Chinese reports explicitly confirm OCA Asian Games rules:
    Points -> Overall GD -> Overall GF -> H2H (pts, GD, GF) -> Fair Play / Draw.
  We test both pure OCA GD-first, pure AFC H2H-first, and an 85/15 primary blend (reflecting OCA rule w/ 15% ambiguity hedge).
"""
import math
from collections import Counter
import numpy as np


def run_model():
    rng = np.random.default_rng(20260920)

    def sim_match_goals(att_a, att_b, base_goals=1.22):
        diff = (att_a - att_b) / 100.0
        lam_a = base_goals * math.exp(0.28 * diff)
        lam_b = base_goals * math.exp(-0.28 * diff)
        return int(rng.poisson(lam_a)), int(rng.poisson(lam_b))

    def sim_knockout_winner(t1, t2, ratings, china_def_scale=1.0):
        bg = 1.18 * (china_def_scale if "China" in (t1, t2) else 1.0)
        g1, g2 = sim_match_goals(ratings[t1], ratings[t2], base_goals=bg)
        if g1 != g2:
            return t1 if g1 > g2 else t2
        et_bg = 0.38 * (china_def_scale if "China" in (t1, t2) else 1.0)
        e1, e2 = sim_match_goals(ratings[t1], ratings[t2], base_goals=et_bg)
        if e1 != e2:
            return t1 if e1 > e2 else t2
        p1 = 0.5 + 0.03 * math.tanh((ratings[t1] - ratings[t2]) / 150.0)
        return t1 if rng.random() < p1 else t2

    def rank_group(teams, matches, h2h_first=False):
        pts = {t: 0 for t in teams}
        gd = {t: 0 for t in teams}
        gf = {t: 0 for t in teams}
        h2h_pts = {t: {} for t in teams}
        h2h_gd = {t: {} for t in teams}
        for a, b, ga, gb in matches:
            gf[a] += ga
            gf[b] += gb
            gd[a] += (ga - gb)
            gd[b] += (gb - ga)
            h2h_gd[a][b] = ga - gb
            h2h_gd[b][a] = gb - ga
            if ga > gb:
                pts[a] += 3
                h2h_pts[a][b] = 3
                h2h_pts[b][a] = 0
            elif gb > ga:
                pts[b] += 3
                h2h_pts[a][b] = 0
                h2h_pts[b][a] = 3
            else:
                pts[a] += 1
                pts[b] += 1
                h2h_pts[a][b] = 1
                h2h_pts[b][a] = 1

        if not h2h_first:
            # OCA rules: Points -> Overall GD -> Overall GF -> H2H (for exact 2-team ties) -> random
            order = sorted(teams, key=lambda t: (pts[t], gd[t], gf[t], rng.random()), reverse=True)
            # Refine exact 2-team ties on (pts, gd, gf) via H2H
            for i in range(len(order) - 1):
                t1, t2 = order[i], order[i + 1]
                if (pts[t1], gd[t1], gf[t1]) == (pts[t2], gd[t2], gf[t2]):
                    tied = [t for t in order if (pts[t], gd[t], gf[t]) == (pts[t1], gd[t1], gf[t1])]
                    if len(tied) == 2 and h2h_pts[t2].get(t1, 0) > h2h_pts[t1].get(t2, 0):
                        order[i], order[i + 1] = order[i + 1], order[i]
            return order
        else:
            # AFC H2H-first: Points -> H2H among tied group -> Overall GD -> Overall GF -> random
            # Group by points
            by_pts = {}
            for t in teams:
                by_pts.setdefault(pts[t], []).append(t)
            order = []
            for p in sorted(by_pts.keys(), reverse=True):
                grp = by_pts[p]
                if len(grp) == 1:
                    order.extend(grp)
                elif len(grp) == len(teams):
                    # All teams tied on points -> H2H = overall!
                    order.extend(sorted(grp, key=lambda t: (gd[t], gf[t], rng.random()), reverse=True))
                else:
                    # Mini-table among tied teams
                    m_pts = {t: 0 for t in grp}
                    m_gd = {t: 0 for t in grp}
                    m_gf = {t: 0 for t in grp}
                    gset = set(grp)
                    for a, b, ga, gb in matches:
                        if a in gset and b in gset:
                            m_gf[a] += ga
                            m_gf[b] += gb
                            m_gd[a] += (ga - gb)
                            m_gd[b] += (gb - ga)
                            if ga > gb:
                                m_pts[a] += 3
                            elif gb > ga:
                                m_pts[b] += 3
                            else:
                                m_pts[a] += 1
                                m_pts[b] += 1
                    order.extend(
                        sorted(
                            grp,
                            key=lambda t: (m_pts[t], m_gd[t], m_gf[t], gd[t], gf[t], rng.random()),
                            reverse=True,
                        )
                    )
            return order

    # 4 calibrated regimes capturing post-Sep 20 signals:
    # - Japan 7-0 KGZ -> JPN bumped 1685->1705 (base); THA 5-1 HKG -> 1535
    # - China 0-0 Iran (0 SOT conceded, hit crossbar) -> solid compact defense, but Zhu Chenjie injury risk!
    # - UAE 0-0 10-man PRK + Al Mansouri red card -> UAE trimmed to 1510 (-15 MD3 susp)
    # - PRK Song Ri red card -> -20 MD3 susp vs Iran
    # - Iran Kahriz injury -> slight -5 vs PRK
    regimes = [
        (
            "R1: Base Post-Sep20 (JPN 1705, KOR 1720, UZB 1665, IRN 1605, CHN 1580, THA 1535, UAE 1510)",
            0.42,
            0.90,  # china_def_scale (compact Puche low-block slightly reduces total goals)
            0.0,   # zhu_inj_pen
            {
                "South Korea": 1720, "Japan": 1705, "Uzbekistan": 1665, "Saudi Arabia": 1620,
                "Iran": 1605, "China": 1580, "North Korea": 1540, "Thailand": 1535,
                "Vietnam": 1520, "United Arab Emirates": 1510, "Qatar": 1495, "Kuwait": 1460,
                "Kyrgyzstan": 1425, "Hong Kong": 1380, "Philippines": 1335,
            },
        ),
        (
            "R2: Strong Japan Host Surge + Zhu Chenjie Injury Drag on China (JPN 1730, CHN 1545)",
            0.26,
            0.95,
            -18.0,  # Zhu Chenjie misses/limited
            {
                "South Korea": 1725, "Japan": 1730, "Uzbekistan": 1670, "Saudi Arabia": 1620,
                "Iran": 1615, "China": 1545, "North Korea": 1550, "Thailand": 1540,
                "Vietnam": 1520, "United Arab Emirates": 1520, "Qatar": 1495, "Kuwait": 1460,
                "Kyrgyzstan": 1425, "Hong Kong": 1380, "Philippines": 1335,
            },
        ),
        (
            "R3: Puche Defensive Fortress / Clinical China (CHN 1610, ultra-low-scoring 0.78x)",
            0.20,
            0.78,
            -5.0,
            {
                "South Korea": 1710, "Japan": 1685, "Uzbekistan": 1655, "Saudi Arabia": 1610,
                "Iran": 1595, "China": 1610, "North Korea": 1535, "Thailand": 1525,
                "Vietnam": 1520, "United Arab Emirates": 1500, "Qatar": 1495, "Kuwait": 1460,
                "Kyrgyzstan": 1425, "Hong Kong": 1380, "Philippines": 1335,
            },
        ),
        (
            "R4: Japan MD3 Rotation / Thailand Upset Threat + Open Goals (1.05x)",
            0.12,
            1.05,
            -8.0,
            {
                "South Korea": 1715, "Japan": 1675, "Uzbekistan": 1660, "Saudi Arabia": 1615,
                "Iran": 1605, "China": 1570, "North Korea": 1540, "Thailand": 1560,
                "Vietnam": 1520, "United Arab Emirates": 1515, "Qatar": 1495, "Kuwait": 1460,
                "Kyrgyzstan": 1425, "Hong Kong": 1380, "Philippines": 1335,
            },
        ),
    ]

    def simulate(h2h_prob=0.15, n_trials=60000):
        total_elim = Counter()
        pos_stats = Counter()
        stage_stats = Counter()
        grp_a1 = Counter()
        grp_b1 = Counter()
        grp_c1 = Counter()
        grp_d1 = Counter()
        qf_opp = Counter()

        for rname, w_reg, c_def, zhu_pen, base_r in regimes:
            elim = Counter()
            r_pos = Counter()
            r_stage = Counter()
            for _ in range(n_trials):
                r = {t: v + rng.normal(0, 30.0) for t, v in base_r.items()}
                h2h_flag = rng.random() < h2h_prob

                # Group A (MD1 + MD2 FIXED!)
                # Japan rotates very slightly (-10) since draw clinches A1; Thailand already clinched
                gA = ["Japan", "Thailand", "Kyrgyzstan", "Hong Kong"]
                mA = [
                    ("Japan", "Hong Kong", 2, 0),
                    ("Thailand", "Kyrgyzstan", 3, 2),
                    ("Japan", "Kyrgyzstan", 7, 0),
                    ("Thailand", "Hong Kong", 5, 1),
                    ("Japan", "Thailand", *sim_match_goals(r["Japan"] - 10.0, r["Thailand"])),
                    ("Kyrgyzstan", "Hong Kong", *sim_match_goals(r["Kyrgyzstan"], r["Hong Kong"])),
                ]
                ordA = rank_group(gA, mA, h2h_first=h2h_flag)
                grp_a1[ordA[0]] += w_reg / n_trials

                # Group C (MD1 + MD2 FIXED!)
                gC = ["Vietnam", "Uzbekistan", "Philippines", "Kuwait"]
                mC = [
                    ("Uzbekistan", "Philippines", 5, 1),
                    ("Vietnam", "Kuwait", 1, 1),
                    ("Vietnam", "Philippines", 2, 0),
                    ("Uzbekistan", "Kuwait", 2, 0),
                    ("Vietnam", "Uzbekistan", *sim_match_goals(r["Vietnam"], r["Uzbekistan"] - 15.0)),
                    ("Philippines", "Kuwait", *sim_match_goals(r["Philippines"], r["Kuwait"])),
                ]
                ordC = rank_group(gC, mC, h2h_first=h2h_flag)
                grp_c1[ordC[0]] += w_reg / n_trials

                # Group D (MD1 + MD2 FIXED!)
                gD = ["South Korea", "Saudi Arabia", "Qatar"]
                mD = [
                    ("South Korea", "Qatar", 4, 1),
                    ("Saudi Arabia", "Qatar", 2, 0),
                    ("South Korea", "Saudi Arabia", *sim_match_goals(r["South Korea"], r["Saudi Arabia"])),
                ]
                ordD = rank_group(gD, mD, h2h_first=h2h_flag)
                grp_d1[ordD[0]] += w_reg / n_trials

                # Group B (MD1 + MD2 FIXED!)
                # MD3 suspensions/injuries:
                #   - UAE: Khamis Al Mansouri RED CARD (-15)
                #   - PRK: Song Ri RED CARD (-20)
                #   - China: Zhu Chenjie possible injury drag (zhu_pen)
                #   - Iran: Kahriz minor injury (-5)
                gB = ["China", "United Arab Emirates", "Iran", "North Korea"]
                c_md3_bg = 1.22 * c_def
                c3, u3 = sim_match_goals(
                    r["China"] + zhu_pen,
                    r["United Arab Emirates"] - 15.0,
                    base_goals=c_md3_bg,
                )
                i3, p3 = sim_match_goals(
                    r["Iran"] - 5.0,
                    r["North Korea"] - 20.0,
                    base_goals=1.18,
                )
                mB = [
                    ("China", "North Korea", 2, 1),
                    ("Iran", "United Arab Emirates", 3, 1),
                    ("Iran", "China", 0, 0),
                    ("North Korea", "United Arab Emirates", 0, 0),
                    ("China", "United Arab Emirates", c3, u3),
                    ("Iran", "North Korea", i3, p3),
                ]
                ordB = rank_group(gB, mB, h2h_first=h2h_flag)
                grp_b1[ordB[0]] += w_reg / n_trials
                c_pos = ordB.index("China") + 1
                r_pos[c_pos] += 1

                if c_pos >= 3:
                    elim["United Arab Emirates"] += 1
                    r_stage["MD3_UAE"] += 1
                    continue

                # Knockout ratings (Group D played 1 fewer match -> +15 freshness; Zhu Chenjie half-recovered by KO)
                r_ko = dict(r)
                r_ko["China"] += 0.5 * zhu_pen
                for t in gD:
                    r_ko[t] += 15.0

                qfs = [
                    (ordC[0], ordD[1]),  # QF1: C1 vs D2
                    (ordD[0], ordC[1]),  # QF2: D1 vs C2
                    (ordB[0], ordA[1]),  # QF3: B1 vs A2
                    (ordA[0], ordB[1]),  # QF4: A1 vs B2
                ]
                qf_w = []
                killer = None
                for t1, t2 in qfs:
                    if "China" in (t1, t2):
                        opp = t2 if t1 == "China" else t1
                        qf_opp[opp] += w_reg / n_trials
                    w = sim_knockout_winner(t1, t2, r_ko, china_def_scale=c_def)
                    qf_w.append(w)
                    if "China" in (t1, t2) and w != "China":
                        killer = w
                if killer is not None:
                    elim[killer] += 1
                    r_stage["QF"] += 1
                    continue

                sfs = [(qf_w[0], qf_w[3]), (qf_w[1], qf_w[2])]
                sf_w = []
                for t1, t2 in sfs:
                    w = sim_knockout_winner(t1, t2, r_ko, china_def_scale=c_def)
                    sf_w.append(w)
                    if "China" in (t1, t2) and w != "China":
                        killer = w
                if killer is not None:
                    elim[killer] += 1
                    r_stage["SF"] += 1
                    continue

                gold = sim_knockout_winner(sf_w[0], sf_w[1], r_ko, china_def_scale=c_def)
                if gold == "China":
                    elim["None"] += 1
                    r_stage["GOLD"] += 1
                else:
                    elim[gold] += 1
                    r_stage["FIN"] += 1

            for k, v in elim.items():
                total_elim[k] += w_reg * (v / n_trials)
            for k, v in r_pos.items():
                pos_stats[k] += w_reg * (v / n_trials)
            for k, v in r_stage.items():
                stage_stats[k] += w_reg * (v / n_trials)

            if h2h_prob == 0.15:
                top6 = [(k, v / n_trials) for k, v in elim.most_common(6)]
                print(f"  [{w_reg:.2f}] {rname}")
                print(f"        Pos: B1={r_pos[1]/n_trials:.3f}, B2={r_pos[2]/n_trials:.3f}, Out={(r_pos[3]+r_pos[4])/n_trials:.3f}")
                print("        Top6:", ", ".join(f"{k}={p:.3f}" for k, p in top6))

        return total_elim, pos_stats, stage_stats, grp_a1, grp_b1, grp_c1, grp_d1, qf_opp

    print("=" * 78)
    print("POST-SEP 20 ASIAN GAMES MEN'S FOOTBALL MC (qid=889545) — 85% OCA GD / 15% H2H")
    print("=" * 78)
    elim_85, pos_85, stg_85, a1, b1, c1, d1, qf_opp = simulate(h2h_prob=0.15, n_trials=80000)

    print("\n--- PRIMARY BLEND SUMMARY (85% OCA GD-first / 15% H2H-first; 320,000 trials) ---")
    print(f"  Group A1: " + ", ".join(f"{k}={v:.3f}" for k, v in a1.most_common(2)))
    print(f"  Group B1: " + ", ".join(f"{k}={v:.3f}" for k, v in b1.most_common(3)))
    print(f"  Group C1: " + ", ".join(f"{k}={v:.3f}" for k, v in c1.most_common(2)))
    print(f"  Group D1: " + ", ".join(f"{k}={v:.3f}" for k, v in d1.most_common(2)))
    print(f"  China Group B Finish: 1st={pos_85[1]:.4f}, 2nd={pos_85[2]:.4f}, 3rd={pos_85[3]:.4f}, 4th={pos_85[4]:.4f}")
    print(f"  China QF Opponent:    " + ", ".join(f"{k}={v:.4f}" for k, v in qf_opp.most_common(4)))
    print(f"  China Exit Stage:     " + ", ".join(f"{k}={v:.4f}" for k, v in stg_85.items()))
    print("\n  RANKED ELIMINATORS (vs Sep 19: Japan 0.28, UAE 0.24, South Korea 0.155, Thailand 0.12, Uzbekistan 0.06):")
    for k, p in elim_85.most_common(10):
        print(f"    {k:22s}: {p:.4f}")
    top5 = sum(p for _, p in elim_85.most_common(5))
    print(f"  Top-5 sum = {top5:.4f}, Outside = {1 - top5:.4f}")

    # Sensitivity: Pure OCA GD-first (h2h_prob=0.0) vs Pure H2H-first (h2h_prob=1.0)
    print("\n" + "=" * 78)
    print("SENSITIVITY: 100% OCA GD-FIRST vs 100% AFC H2H-FIRST")
    print("=" * 78)
    elim_gd, pos_gd, _, _, _, _, _, _ = simulate(h2h_prob=0.0, n_trials=40000)
    elim_h2h, pos_h2h, _, _, _, _, _, _ = simulate(h2h_prob=1.0, n_trials=40000)
    print(f"  {'Outcome':22s} {'100% GD-first':>14s} {'85/15 Blend':>14s} {'100% H2H-first':>15s}")
    keys = [k for k, _ in elim_85.most_common(9)]
    for k in keys:
        print(f"  {k:22s} {elim_gd[k]:14.4f} {elim_85[k]:14.4f} {elim_h2h[k]:15.4f}")
    print(f"  China Group Exit:      {pos_gd[3]+pos_gd[4]:14.4f} {pos_85[3]+pos_85[4]:14.4f} {pos_h2h[3]+pos_h2h[4]:15.4f}")


if __name__ == "__main__":
    run_model()
