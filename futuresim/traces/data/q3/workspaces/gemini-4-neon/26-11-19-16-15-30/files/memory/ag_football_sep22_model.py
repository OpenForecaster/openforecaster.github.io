"""
Quantitative Monte Carlo Model — Tue Sep 22, 2026
qid=889545: Which country will end China's gold-medal bid in men's football at the 2026 Asian Games?

POST-TUE SEP 22 GROUP C & D FINAL RESULTS (16 of 21 group matches completed!):
  Group C (FINAL — Sep 22):
    MD1: Uzbekistan 5-1 Philippines; Vietnam 1-1 Kuwait
    MD2: Vietnam 2-0 Philippines; Uzbekistan 2-0 Kuwait
    MD3 (Sep 22): Uzbekistan 2-0 Vietnam; Philippines 2-1 Kuwait
    -> FINAL: C1 = Uzbekistan (9 pts, +8), C2 = Vietnam (4 pts, 0) [Philippines 3, Kuwait 1 OUT]
  Group D (FINAL — Sep 22):
    MD1: South Korea 4-1 Qatar
    MD2: Saudi Arabia 2-0 Qatar
    MD3 (Sep 22): South Korea 2-0 Saudi Arabia
    -> FINAL: D1 = South Korea (6 pts, +5), D2 = Saudi Arabia (3 pts, 0) [Qatar 0 OUT]

  LOCKED QFs (confirmed Dan Tri / Yonhap / Seoul Shinmun Sep 22):
    QF1 (C1 vs D2): Uzbekistan vs Saudi Arabia
    QF2 (D1 vs C2): South Korea vs Vietnam
    QF3 (B1 vs A2): TBD (Wed Sep 23)
    QF4 (A1 vs B2): TBD (Wed Sep 23)
  LOCKED SF CROSSOVER (confirmed Seoul Shinmun Sep 22 — KOR D1 cannot meet JPN A1 or UZB C1 until Final!):
    SF1: W(QF1: Uzbekistan vs Saudi Arabia) vs W(QF4: A1 vs B2)
    SF2: W(QF2: South Korea vs Vietnam)     vs W(QF3: B1 vs A2)
    Gold Medal Final: W(SF1) vs W(SF2)

  REMAINING MD3 MATCHES (Wed Sep 23):
    Group A: Japan (6 pts, +9) vs Thailand (6 pts, +5); Kyrgyzstan (0) vs Hong Kong (0)
             [Japan wins A1 on Win or Draw!]
    Group B: China (4 pts, +1) vs UAE (1 pt, -2); Iran (4 pts, +2) vs North Korea (1 pt, -1)
             [7msport & 24h Sep 22 project BOTH Zhu Chenjie & Hu Hetao starting for China;
              UAE missing red-carded Khamis Al Mansouri; PRK missing red-carded Song Ri.]
"""
import math
from collections import Counter
import numpy as np


def run_model():
    rng = np.random.default_rng(20260922)

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
        for a, b, ga, gb in matches:
            gf[a] += ga
            gf[b] += gb
            gd[a] += (ga - gb)
            gd[b] += (gb - ga)
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
            order = sorted(teams, key=lambda t: (pts[t], gd[t], gf[t], rng.random()), reverse=True)
            for i in range(len(order) - 1):
                t1, t2 = order[i], order[i + 1]
                if (pts[t1], gd[t1], gf[t1]) == (pts[t2], gd[t2], gf[t2]):
                    tied = [t for t in order if (pts[t], gd[t], gf[t]) == (pts[t1], gd[t1], gf[t1])]
                    if len(tied) == 2 and h2h_pts[t2].get(t1, 0) > h2h_pts[t1].get(t2, 0):
                        order[i], order[i + 1] = order[i + 1], order[i]
            return order
        else:
            by_pts = {}
            for t in teams:
                by_pts.setdefault(pts[t], []).append(t)
            order = []
            for p in sorted(by_pts.keys(), reverse=True):
                grp = by_pts[p]
                if len(grp) == 1:
                    order.extend(grp)
                elif len(grp) == len(teams):
                    order.extend(sorted(grp, key=lambda t: (gd[t], gf[t], rng.random()), reverse=True))
                else:
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

    # Post-Sep 22 calibrated regimes:
    # - South Korea 2-0 Saudi Arabia -> KOR +15 (1735), KSA -10 (1610)
    # - Uzbekistan 2-0 Vietnam (without Fayzullaev!) -> UZB +10 (1675), VIE -5 (1515)
    # - China Zhu Chenjie & Hu Hetao projected to start -> lighter injury drag (-10 in R2, 0 in R1)
    regimes = [
        (
            "R1: Base Post-Sep22 (KOR 1735, JPN 1705, UZB 1675, KSA 1610, IRN 1605, CHN 1580, THA 1535, UAE 1510)",
            0.42,
            0.90,
            0.0,
            {
                "South Korea": 1735, "Japan": 1705, "Uzbekistan": 1675, "Saudi Arabia": 1610,
                "Iran": 1605, "China": 1580, "North Korea": 1540, "Thailand": 1535,
                "Vietnam": 1515, "United Arab Emirates": 1510, "Qatar": 1490, "Kuwait": 1455,
                "Kyrgyzstan": 1425, "Hong Kong": 1380, "Philippines": 1350,
            },
        ),
        (
            "R2: Strong Japan/Korea + Mild China Stamina Drag (KOR 1740, JPN 1730, CHN 1550)",
            0.26,
            0.95,
            -10.0,
            {
                "South Korea": 1740, "Japan": 1730, "Uzbekistan": 1680, "Saudi Arabia": 1605,
                "Iran": 1615, "China": 1550, "North Korea": 1550, "Thailand": 1540,
                "Vietnam": 1515, "United Arab Emirates": 1520, "Qatar": 1490, "Kuwait": 1455,
                "Kyrgyzstan": 1425, "Hong Kong": 1380, "Philippines": 1350,
            },
        ),
        (
            "R3: Puche Defensive Fortress / Clinical China (CHN 1610, ultra-low-scoring 0.78x)",
            0.20,
            0.78,
            -3.0,
            {
                "South Korea": 1725, "Japan": 1685, "Uzbekistan": 1665, "Saudi Arabia": 1600,
                "Iran": 1595, "China": 1610, "North Korea": 1535, "Thailand": 1525,
                "Vietnam": 1515, "United Arab Emirates": 1500, "Qatar": 1490, "Kuwait": 1455,
                "Kyrgyzstan": 1425, "Hong Kong": 1380, "Philippines": 1350,
            },
        ),
        (
            "R4: Japan MD3 Rotation / Thailand Upset Threat + Open Goals (1.05x)",
            0.12,
            1.05,
            -5.0,
            {
                "South Korea": 1730, "Japan": 1675, "Uzbekistan": 1670, "Saudi Arabia": 1605,
                "Iran": 1605, "China": 1570, "North Korea": 1540, "Thailand": 1560,
                "Vietnam": 1515, "United Arab Emirates": 1515, "Qatar": 1490, "Kuwait": 1455,
                "Kyrgyzstan": 1425, "Hong Kong": 1380, "Philippines": 1350,
            },
        ),
    ]

    def simulate(h2h_prob=0.15, n_trials=80000):
        total_elim = Counter()
        pos_stats = Counter()
        stage_stats = Counter()
        qf_opp = Counter()

        for rname, w_reg, c_def, zhu_pen, base_r in regimes:
            elim = Counter()
            r_pos = Counter()
            r_stage = Counter()
            for _ in range(n_trials):
                r = {t: v + rng.normal(0, 28.0) for t, v in base_r.items()}
                h2h_flag = rng.random() < h2h_prob

                # Group A (MD3 Wed Sep 23)
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

                # Group C & D LOCKED FINAL!
                c1, c2 = "Uzbekistan", "Vietnam"
                d1, d2 = "South Korea", "Saudi Arabia"

                # Group B (MD3 Wed Sep 23)
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
                c_pos = ordB.index("China") + 1
                r_pos[c_pos] += 1

                if c_pos >= 3:
                    elim["United Arab Emirates"] += 1
                    r_stage["MD3_UAE"] += 1
                    continue

                # Knockout ratings (Group D played 1 fewer group match -> +15 freshness; UZB gets Fayzullaev back)
                r_ko = dict(r)
                r_ko["China"] += 0.5 * zhu_pen
                r_ko["South Korea"] += 15.0
                r_ko["Saudi Arabia"] += 15.0

                qfs = [
                    (c1, d2),        # QF1: Uzbekistan vs Saudi Arabia (LOCKED!)
                    (d1, c2),        # QF2: South Korea vs Vietnam (LOCKED!)
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

        return total_elim, pos_stats, stage_stats, qf_opp

    print("=" * 78)
    print("POST-SEP 22 ASIAN GAMES MEN'S FOOTBALL MC (qid=889545) — C & D LOCKED!")
    print("=" * 78)
    elim_85, pos_85, stg_85, qf_opp = simulate(h2h_prob=0.15, n_trials=80000)

    print("\n--- PRIMARY BLEND SUMMARY (85% OCA GD-first / 15% H2H-first; 320,000 trials) ---")
    print(f"  China Group B Finish: 1st={pos_85[1]:.4f}, 2nd={pos_85[2]:.4f}, 3rd={pos_85[3]:.4f}, 4th={pos_85[4]:.4f}")
    print(f"  China QF Opponent:    " + ", ".join(f"{k}={v:.4f}" for k, v in qf_opp.most_common(4)))
    print(f"  China Exit Stage:     " + ", ".join(f"{k}={v:.4f}" for k, v in stg_85.items()))
    print("\n  RANKED ELIMINATORS (vs Sep 21: Japan 0.37, Thailand 0.165, South Korea 0.135, UAE 0.13, Uzbekistan 0.065):")
    for k, p in elim_85.most_common(10):
        print(f"    {k:22s}: {p:.4f}")
    top5 = sum(p for _, p in elim_85.most_common(5))
    print(f"  Top-5 sum = {top5:.4f}, Outside = {1 - top5:.4f}")

    # Sensitivity: Pure OCA GD-first vs Pure H2H-first
    elim_gd, _, _, _ = simulate(h2h_prob=0.0, n_trials=40000)
    elim_h2h, _, _, _ = simulate(h2h_prob=1.0, n_trials=40000)
    print("\n--- SENSITIVITY: 100% OCA GD-FIRST vs 85/15 vs 100% H2H-FIRST ---")
    for k, _ in elim_85.most_common(9):
        print(f"  {k:22s}  GD={elim_gd[k]:.4f}  85/15={elim_85[k]:.4f}  H2H={elim_h2h[k]:.4f}")


if __name__ == "__main__":
    run_model()
