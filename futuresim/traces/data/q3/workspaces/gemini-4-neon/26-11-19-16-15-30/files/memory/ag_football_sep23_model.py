"""
Quantitative Monte Carlo Model — Wed Sep 23, 2026
qid=889545: Which country will end China's gold-medal bid in men's football at the 2026 Asian Games?

ALL GROUP STAGE MATCHES COMPLETED (Wed Sep 23)!
  Group A FINAL:
    Japan 2-0 Hong Kong; Thailand 3-2 Kyrgyzstan; Japan 7-0 Kyrgyzstan; Thailand 5-1 Hong Kong;
    Japan 3-0 Thailand (Nakajima 31', Kosugi 47', Ishii 48'); Kyrgyzstan 4-0 Hong Kong.
    -> A1 = Japan (9 pts, +12 GD, 12-0!), A2 = Thailand (6 pts, +2 GD, 8-6)
  Group B FINAL:
    China 2-1 North Korea; Iran 3-1 UAE; Iran 0-0 China; North Korea 0-0 UAE;
    China 0-0 UAE; North Korea 4-1 Iran!
    -> B1 = China (5 pts, +1 GD, 2-1), B2 = North Korea (4 pts, +2 GD) [Iran 4 pts -1 GD OUT, UAE 2 pts OUT!]
  Group C FINAL:
    -> C1 = Uzbekistan (9 pts, +8), C2 = Vietnam (4 pts, 0)
  Group D FINAL:
    -> D1 = South Korea (6 pts, +5), D2 = Saudi Arabia (3 pts, 0)

EXACT 100% LOCKED-IN KNOCKOUT BRACKET (confirmed Zamin.uz / Vietnam.vn / Xinhua / Yonhap / Seoul Shinmun):
  QF1 (Fri Sep 25, 10:00): Uzbekistan (C1)  vs Saudi Arabia (D2)
  QF2 (Fri Sep 25, 15:30): South Korea (D1) vs Vietnam (C2)
  QF3 (Sat Sep 26, 11:00): China (B1)       vs Thailand (A2)
  QF4 (Sat Sep 26, 15:30): Japan (A1)       vs North Korea (B2)

  SF1 (Mon Sep 28): W(QF1: Uzbekistan vs Saudi Arabia) vs W(QF4: Japan vs North Korea)
  SF2 (Mon Sep 28): W(QF2: South Korea vs Vietnam)     vs W(QF3: China vs Thailand)
  Gold Medal Final (Wed Sep 30): W(SF1) vs W(SF2)  [Bronze match EXCLUDED per criteria!]

KEY SEP 23 TEAM NEWS & ADJUSTMENTS:
  1. WANG YUDONG SUSPENDED FOR QF3 VS THAILAND (Xinhua Sep 23):
     Received 2nd yellow card in 53' vs UAE -> misses Sat Sep 26 QF vs Thailand (returns fresh for SF2!).
     Applied as QF-only China Elo penalty (-18 to -28 Elo across regimes) + tighter scoring!
  2. REST/SCHEDULE ASYMMETRY IN SF2:
     South Korea (and Saudi Arabia) played ONLY 2 group matches (Group D had 3 teams) AND plays QF2
     on Fri Sep 25 — giving KOR/VIE 1 extra rest day over China/Thailand (who play Sat Sep 26 QF3)!
  3. GROUP B STRENGTH UPGRADE & JAPAN DOMINANCE:
     - North Korea crushing Iran 4-1 upgrades both North Korea (+40 -> ~1580) & China's Group B form (+10 -> ~1590)!
     - Japan 3-0 Thailand (12-0 across 3 matches!) upgrades Japan (+25 -> ~1730) and trims Thailand (-10 -> ~1525).
     - Uzbekistan welcomes back star Fayzullaev from suspension for QF1 vs Saudi Arabia.
"""
import math
from collections import Counter
import numpy as np


def run_model():
    rng = np.random.default_rng(20260923)

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

    # Four calibrated regimes spanning tactical uncertainty:
    # (name, weight, chn_def_scale, wang_qf_pen, sf2_rest_bonus_kor_vie, base_ratings)
    regimes = [
        (
            "R1: Base Post-Group (KOR 1740, JPN 1730, UZB 1685, KSA 1610, CHN 1590, PRK 1580, THA 1525, VIE 1515)",
            0.40,
            0.86,   # China conceded 1 goal in 3 games (2-1, 0-0, 0-0)!
            -20.0,  # Wang Yudong suspended for QF3 vs Thailand
            15.0,   # Fri QF2 winner gets 1 extra rest day over Sat QF3 winner
            {
                "South Korea": 1740, "Japan": 1730, "Uzbekistan": 1685,
                "Saudi Arabia": 1610, "China": 1590, "North Korea": 1580,
                "Thailand": 1525, "Vietnam": 1515,
            },
        ),
        (
            "R2: Thailand Fast-Flank Threat / Heavy Wang Yudong Loss (CHN 1575, THA 1545, Wang -28)",
            0.25,
            0.94,
            -28.0,
            18.0,
            {
                "South Korea": 1745, "Japan": 1740, "Uzbekistan": 1685,
                "Saudi Arabia": 1610, "China": 1575, "North Korea": 1585,
                "Thailand": 1545, "Vietnam": 1520,
            },
        ),
        (
            "R3: Puche 5-3-2 Defensive Fortress / Battle-Tested Group B (CHN 1615, THA 1515, low-scoring 0.76x)",
            0.22,
            0.76,
            -15.0,
            12.0,
            {
                "South Korea": 1730, "Japan": 1720, "Uzbekistan": 1680,
                "Saudi Arabia": 1605, "China": 1615, "North Korea": 1590,
                "Thailand": 1515, "Vietnam": 1510,
            },
        ),
        (
            "R4: Upset-Heavy / High-Variance U23 Football (compressed ratings, KOR 1715, JPN 1710, VIE 1540)",
            0.13,
            0.92,
            -20.0,
            10.0,
            {
                "South Korea": 1715, "Japan": 1710, "Uzbekistan": 1665,
                "Saudi Arabia": 1615, "China": 1585, "North Korea": 1595,
                "Thailand": 1535, "Vietnam": 1540,
            },
        ),
    ]

    n_trials = 150000
    total_elim = Counter()
    total_stage = Counter()
    qf_chn_win = 0.0
    sf_chn_win_given_qf = 0.0
    kor_beats_vie = 0.0
    jpn_reaches_fin = 0.0

    print("=" * 80)
    print("POST-SEP 23 LOCKED KNOCKOUT MC: qid=889545 (China Men's Football Eliminator)")
    print("=" * 80)

    for rname, w_reg, c_def, wang_pen, sf2_rest, base_r in regimes:
        elim = Counter()
        stg = Counter()
        r_chn_qf = 0
        r_chn_sf = 0
        r_kor_qf = 0
        r_jpn_fin = 0

        for _ in range(n_trials):
            r = {t: v + rng.normal(0, 26.0) for t, v in base_r.items()}
            # Group D (KOR & KSA) played only 2 group matches -> +15 freshness throughout QFs
            r_qf = dict(r)
            r_qf["South Korea"] += 15.0
            r_qf["Saudi Arabia"] += 15.0

            # QF1 (Sep 25): Uzbekistan vs Saudi Arabia
            w_qf1 = sim_ko("Uzbekistan", "Saudi Arabia", r_qf["Uzbekistan"], r_qf["Saudi Arabia"])
            # QF2 (Sep 25): South Korea vs Vietnam
            w_qf2 = sim_ko("South Korea", "Vietnam", r_qf["South Korea"], r_qf["Vietnam"])
            if w_qf2 == "South Korea":
                r_kor_qf += 1
            # QF3 (Sep 26): China (w/o Wang Yudong!) vs Thailand
            # Wang Yudong absence also slightly suppresses total goals in QF3 (0.94x extra)
            w_qf3 = sim_ko(
                "China", "Thailand",
                r_qf["China"] + wang_pen, r_qf["Thailand"],
                base_goals=1.18 * c_def * 0.94,
                et_goals=0.38 * c_def * 0.94,
            )
            # QF4 (Sep 26): Japan vs North Korea
            w_qf4 = sim_ko("Japan", "North Korea", r_qf["Japan"], r_qf["North Korea"])

            # SF1 (Sep 28): W(QF1) vs W(QF4) — QF1 winner gets +10 rest over QF4 winner
            r_sf1_a = r[w_qf1] + 10.0 + (8.0 if w_qf1 == "Saudi Arabia" else 0.0)
            r_sf1_b = r[w_qf4]
            w_sf1 = sim_ko(w_qf1, w_qf4, r_sf1_a, r_sf1_b)
            if w_sf1 == "Japan":
                r_jpn_fin += 1

            if w_qf3 != "China":
                elim["Thailand"] += 1
                stg["QF"] += 1
                continue

            r_chn_qf += 1

            # SF2 (Sep 28): W(QF2: KOR/VIE) vs China (Wang Yudong returns fresh!)
            # QF2 played Fri Sep 25 vs China Sat Sep 26 -> sf2_rest bonus (+10 more if KOR 2-match group)
            opp_sf2 = w_qf2
            r_opp_sf2 = r[opp_sf2] + sf2_rest + (8.0 if opp_sf2 == "South Korea" else 0.0)
            w_sf2 = sim_ko(
                "China", opp_sf2,
                r["China"], r_opp_sf2,
                base_goals=1.18 * c_def,
                et_goals=0.38 * c_def,
            )
            if w_sf2 != "China":
                elim[opp_sf2] += 1
                stg["SF"] += 1
                continue

            r_chn_sf += 1

            # Gold Medal Final (Sep 30): China vs W(SF1)
            opp_fin = w_sf1
            w_gold = sim_ko(
                "China", opp_fin,
                r["China"], r[opp_fin],
                base_goals=1.18 * c_def,
                et_goals=0.38 * c_def,
            )
            if w_gold == "China":
                elim["None"] += 1
                stg["GOLD"] += 1
            else:
                elim[opp_fin] += 1
                stg["FINAL"] += 1

        for k, v in elim.items():
            total_elim[k] += w_reg * (v / n_trials)
        for k, v in stg.items():
            total_stage[k] += w_reg * (v / n_trials)
        qf_chn_win += w_reg * (r_chn_qf / n_trials)
        sf_chn_win_given_qf += w_reg * (r_chn_sf / max(1, r_chn_qf))
        kor_beats_vie += w_reg * (r_kor_qf / n_trials)
        jpn_reaches_fin += w_reg * (r_jpn_fin / n_trials)

        top6 = [(k, v / n_trials) for k, v in elim.most_common(6)]
        print(f"\n  [{w_reg:.2f}] {rname}")
        print(f"        P(CHN>THA)={r_chn_qf/n_trials:.3f} | P(KOR>VIE)={r_kor_qf/n_trials:.3f} | P(CHN reaches Final)={r_chn_sf/n_trials:.3f}")
        print("        Top6:", ", ".join(f"{k}={p:.4f}" for k, p in top6))

    print("\n" + "-" * 80)
    print(f"BLENDED SUMMARY (600,000 trials):")
    print(f"  P(China beats Thailand in QF3)  = {qf_chn_win:.4f}")
    print(f"  P(South Korea beats Vietnam)    = {kor_beats_vie:.4f}")
    print(f"  P(China wins SF2 | won QF3)     = {sf_chn_win_given_qf:.4f}")
    print(f"  P(Japan reaches Gold Final)     = {jpn_reaches_fin:.4f}")
    print(f"  China Exit Stages: " + ", ".join(f"{k}={v:.4f}" for k, v in total_stage.items()))
    print("\n  ALL OUTCOMES RANKED:")
    for k, p in total_elim.most_common(10):
        print(f"    {k:22s}: {p:.4f}")
    top5 = sum(p for _, p in total_elim.most_common(5))
    print(f"  Top-5 sum = {top5:.4f} | Outside = {1 - top5:.4f}")


if __name__ == "__main__":
    run_model()
