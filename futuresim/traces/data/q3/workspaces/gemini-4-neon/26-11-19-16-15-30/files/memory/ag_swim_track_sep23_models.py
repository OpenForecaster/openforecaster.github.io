"""
Quantitative Bayesian & Monte Carlo Models — Wed Sep 23, 2026 (Asian Games Day 4)
Batch: asian_games_swim_track

Models:
  1. qid=190556: Men's 200m Breaststroke (Thu Sep 24, T+1d — FINAL DAY TOMORROW)
  2. qid=686508: Men's 100m (Fri Sep 25, T+2d — HEATS THU SEP 24)
  3. qid=695205: Men's Javelin Throw (Mon Sep 28, T+5d — QUAL SAT SEP 26)
  4. qid=996188: Puyo Puyo Champions (Sat Sep 26, T+3d — GROUP STAGE THU SEP 24, ALL 10 PLAYERS KNOWN!)
"""
import math
from collections import Counter
import numpy as np


# ==============================================================================
# MODEL 1: qid=190556 — MEN'S 200m BREASTSTROKE (Thu Sep 24, T+1d)
# ==============================================================================
def model_190556_200breast():
    print("=" * 76)
    print("MODEL 1: qid=190556 — Men's 200m Breaststroke (Post-Day 4 Mixed Relay)")
    print("=" * 76)
    # Full evidence stack through Wed Sep 23 night:
    # - Prior 2026 200m baselines:
    #     Shin Ohashi (JPN, 17): 2:06.59 (Mar Tokyo Aquatics Centre WJR/WL), 2:06.91 (#2 WL);
    #       trained specifically for 200m PB/WR at Asian Games.
    #     Dong Zhihao (CHN, 21): 2024 World Champ (2:07.94), elite closing 50m, China pool taper is red-hot.
    #     Qin Haiyang (CHN, 27): WR 2:05.48 (2023), 2025 World Champ (2:07.41), 59.01 100m bronze Mon.
    #     Ippei Watanabe (JPN, 29): 2:08.57 Mar 2026, 2:09.72 Pan Pacs, former WR holder, rested.
    #     Cho Sung-jae (KOR): ~2:09.5-2:10.0 tier.
    # - Live Tokyo Evidence (Mon-Wed):
    #     Mon Sep 21 100m final: Ohashi 58.64 (while fighting cold!) = Dong 58.64 (caught late); Qin 59.01 (+0.37s).
    #     Tue Sep 22 Men 4x100m Medley final: Ohashi 57.64 split (JPN NR 3:28.70) beat Dong 57.94 by 0.30s!
    #       Qin Haiyang DROPPED from final.
    #     Wed Sep 23 Mixed 4x100m Medley final: Dong Zhihao SWAM AGAIN (China gold 3:40.38 by 3.60s)!
    #       Qin Haiyang DROPPED AGAIN (2nd straight relay final even with huge cushion, though gets 2 full rest days!).
    #       Shin Ohashi RESTED (Japan 3:43.98; full 48h recovery from Tue evening & cold clearing!).
    #
    # Modeling posterior 200m final times (in seconds: 2:07.00 = 127.00s):
    # Regimes span uncertainty over:
    #   (a) how much Ohashi's 57.64 + cold recovery translates to sub-2:07.0 200m speed vs 17yo pacing/fade risk;
    #   (b) how much Dong's 3-straight-night relay workload hurts (+0.10 to +0.25s) vs China's red-hot taper boost;
    #   (c) whether Qin's 2 rest days + 200m focus lets him bounce back despite 2 relay omissions.

    regimes = [
        # (label, w, oh_mu, oh_sd, oh_fade_p, dz_mu, dz_sd, qh_mu, qh_sd)
        ("R1: Base (Ohashi peak/rested 2:06.95, Dong slight fatigue 2:07.65, Qin sub-peak 2:08.35)",
         0.45, 126.95, 0.80, 0.12, 127.65, 0.80, 128.35, 0.95),
        ("R2: China Taper Hot / Ohashi 17yo Pressure (Ohashi 2:07.25, Dong sharp 2:07.45, Qin rebounds 2:08.05)",
         0.30, 127.25, 0.85, 0.16, 127.45, 0.80, 128.05, 0.95),
        ("R3: Ohashi WR-Threat Dominant (Ohashi 2:06.55, Dong heavier legs 2:07.85, Qin off-form 2:08.65)",
         0.25, 126.55, 0.78, 0.09, 127.85, 0.82, 128.65, 0.95),
    ]

    rng = np.random.default_rng(19055623)
    n = 150000
    blended = Counter()

    for label, w, oh_mu, oh_sd, oh_fp, dz_mu, dz_sd, qh_mu, qh_sd in regimes:
        wins = Counter()
        # Vectorized draw for speed & precision
        # DQ / scratch / heats mishap probability per swimmer (~2.0% on T+1d for Ohashi/Dong/Qin, 2.5% Watanabe/Cho)
        oh_t = rng.normal(oh_mu, oh_sd, n) + (rng.random(n) < oh_fp) * rng.uniform(0.6, 1.7, n)
        oh_t = np.where(rng.random(n) < 0.022, 999.0, oh_t)

        dz_t = rng.normal(dz_mu, dz_sd, n) + (rng.random(n) < 0.06) * rng.uniform(0.6, 1.4, n)
        dz_t = np.where(rng.random(n) < 0.020, 999.0, dz_t)

        qh_t = rng.normal(qh_mu, qh_sd, n) + (rng.random(n) < 0.08) * rng.uniform(0.6, 1.6, n)
        qh_t = np.where(rng.random(n) < 0.022, 999.0, qh_t)

        iw_t = rng.normal(128.95, 0.85, n)
        iw_t = np.where(rng.random(n) < 0.022, 999.0, iw_t)

        cs_t = rng.normal(129.85, 0.90, n)
        cs_t = np.where(rng.random(n) < 0.025, 999.0, cs_t)

        ra_t = rng.normal(129.95, 0.95, n)

        names = ["Shin Ohashi", "Dong Zhihao", "Qin Haiyang", "Ippei Watanabe", "Cho Sung-jae", "Rest_of_Asia"]
        mat = np.vstack([oh_t, dz_t, qh_t, iw_t, cs_t, ra_t])
        idx = np.argmin(mat, axis=0)
        for i, nm in enumerate(names):
            p = float(np.mean(idx == i))
            wins[nm] = p
            blended[nm] += w * p

        print(f"\n  [{w:.2f}] {label}")
        print("        " + ", ".join(f"{nm}={wins[nm]:.4f}" for nm in names))

    print("\n  >>> BLENDED POST-DAY-4 PROBABILITIES (qid=190556):")
    for k, v in blended.most_common():
        print(f"      {k:16s}: {v:.4f}")
    print(f"      Top-5 sum = {sum(blended[k] for k in ['Shin Ohashi','Dong Zhihao','Qin Haiyang','Ippei Watanabe','Cho Sung-jae']):.4f}")


# ==============================================================================
# MODEL 2: qid=686508 — MEN'S 100m (Fri Sep 25, T+2d — HEATS THU SEP 24)
# ==============================================================================
def model_686508_men100m():
    print("\n" + "=" * 76)
    print("MODEL 2: qid=686508 — Men's 100m (Post-Sep 23 Confirmations)")
    print("=" * 76)
    # Key verified facts through Sep 23:
    # - Puripol Boonson (THA): 9.94 PB (Dec 2025), 9.99 SB (Jun 2026) — ONLY Asian sub-10 in 2026!
    #   Healthy, in Nagoya, confident ("my body is in better condition now"), 3 rounds (heats Thu, SF & Final Fri).
    #   Risks: ~2.8% false-start DQ across 3 rounds, ~3.5% hamstring/pull-up (history at Hangzhou 200m SF).
    # - Confirmed Japan entries (2 max):
    #     Shuhei Tada (JPN): Asian #6, 10.10 2025-26 best, home track, explosive starter.
    #     Yuki Koike (JPN): Asian #9, 10.06 2025-26 best, home track.
    # - Confirmed China defending champion:
    #     Xie Zhenye (CHN): 9.97 2023 AG gold, veteran 33yo, explicitly cited by Reuters & ST Sep 23 as
    #       Puripol's biggest threat in Nagoya (no sub-10 in 2026, ~10.08-10.14 form).
    # - China #2 (Zeng Keli / Deng Xinrui / Wu Haolin / Chen Jiapeng): ~10.07-10.14 tier (name unconfirmed!).
    # - Abdullah Abkar Mohammed (KSA): 9.96 PB / ~10.06-10.13 tier (not sub-10 in 2026; ~78% confirmed start).
    # - Ali Anwar Al-Balushi (OMA): ~10.08-10.15 tier (~78% start).
    # - India confirmed: Gurindervir Singh (10.09 NR), Animesh Kujur (10.14).
    # - Other Asian contenders: Muhd Azeem Fahmi (MAS), Korea (Namadi Joeljin ~10.13), Yang Chun-han (TPE), Qatar/Bahrain.

    rng = np.random.default_rng(68650823)
    n = 150000

    # (name, p_start_and_no_fs_inj, mu_final, sd_final, bad_round_p)
    # Note: common track/wind shift cancels out in pairwise comparisons; individual sd ~ 0.065-0.075s in 100m final!
    regimes = [
        ("R1: Base (Puripol 10.00s, rivals clustered 10.10-10.16s, standard 100m sd=0.068s)", 0.50, 10.00, 0.068, 0.065),
        ("R2: Tight/Upset-prone (Puripol 10.03s, higher round variance sd=0.075s, rivals sharper)", 0.30, 10.03, 0.075, 0.080),
        ("R3: Puripol Dominant Form (Puripol 9.97s, sd=0.062s)", 0.20, 9.97, 0.062, 0.050),
    ]

    rivals_base = [
        ("Shuhei Tada",              0.94, 10.11, 0.068),
        ("Xie Zhenye",               0.92, 10.12, 0.072),
        ("Abdullah Abkar Mohammed",  0.76, 10.10, 0.075),  # start-list uncertainty ~76%
        ("Yuki Koike",               0.94, 10.13, 0.070),
        ("China_No2",                0.94, 10.11, 0.072),
        ("Ali Anwar Al-Balushi",     0.76, 10.13, 0.074),
        ("Gurindervir Singh",        0.94, 10.16, 0.070),
        ("Animesh Kujur",            0.94, 10.18, 0.070),
        ("Korea_MAS_TPE_Best1",      0.95, 10.14, 0.072),
        ("Korea_MAS_TPE_Best2",      0.95, 10.16, 0.072),
        ("WestAsia_Other_Best",      0.90, 10.15, 0.078),
    ]

    blended = Counter()
    for label, w, p_mu, p_sd, p_fail in regimes:
        names = ["Puripol Boonson"] + [r[0] for r in rivals_base]
        times = []
        # Puripol
        t_p = rng.normal(p_mu, p_sd, n) + (rng.random(n) < 0.06) * rng.uniform(0.08, 0.18, n)
        t_p = np.where(rng.random(n) < p_fail, 99.0, t_p)
        times.append(t_p)
        for rname, p_ok, r_mu, r_sd in rivals_base:
            t_r = rng.normal(r_mu, r_sd, n)
            t_r = np.where(rng.random(n) >= p_ok, 99.0, t_r)
            times.append(t_r)
        mat = np.vstack(times)
        idx = np.argmin(mat, axis=0)
        res = {nm: float(np.mean(idx == i)) for i, nm in enumerate(names)}
        print(f"\n  [{w:.2f}] {label}")
        print("        Puripol={:.4f}, Tada={:.4f}, Xie={:.4f}, Abdullah={:.4f}, Koike={:.4f}, CHN2={:.4f}".format(
            res["Puripol Boonson"], res["Shuhei Tada"], res["Xie Zhenye"],
            res["Abdullah Abkar Mohammed"], res["Yuki Koike"], res["China_No2"]))
        for nm, val in res.items():
            blended[nm] += w * val

    print("\n  >>> BLENDED PROBABILITIES (qid=686508):")
    for k, v in blended.most_common():
        print(f"      {k:26s}: {v:.4f}")
    top5_keys = ["Puripol Boonson", "Shuhei Tada", "Xie Zhenye", "Abdullah Abkar Mohammed", "Yuki Koike"]
    print(f"      Named Top-5 sum = {sum(blended[k] for k in top5_keys):.4f}, Outside = {1 - sum(blended[k] for k in top5_keys):.4f}")


# ==============================================================================
# MODEL 3: qid=695205 — MEN'S JAVELIN THROW (Mon Sep 28, T+5d)
# ==============================================================================
def model_695205_javelin():
    print("\n" + "=" * 76)
    print("MODEL 3: qid=695205 — Men's Javelin Throw (Sanity Check, 6-throw Final)")
    print("=" * 76)
    # 6 throws per athlete in final; best throw wins!
    # Pathirage: 92.62m PB/WL, 91.09m Sep 13, 12-for-12 unbeaten in 2026!
    #   Discount for T+5d pre-event injury/DNS (~4.5%), Sep 15 broken-javelin replacement risk (~4% shift -3m or DNS),
    #   and heavy 14-meet workload fatigue (~8% chance of sub-par 84-86m day).
    # Rohit Yadav: 87.68m Aug 2026 PB (#3 Asian SB, #2 healthy).
    # Arshad Nadeem: 81.49m 2026 SB, injured — bimodal! ~75% still injured/80-84m, ~25% sudden championship rebound 87-91m!
    # Yuta Sakiyama: 87.16m PB at Paloma Mizuho Stadium (home runway!).
    # Yash Vir Singh: 85.41m CWG bronze (#4 Asian SB).
    rng = np.random.default_rng(69520523)
    n = 120000

    def sim_best6(mu, sd, p_ok):
        # Athlete day-level form + 6 throw attempts
        day_form = rng.normal(mu, sd * 0.72, n)
        throws = day_form[:, None] + rng.normal(0.0, sd * 0.70, (n, 6))
        best = np.max(throws, axis=1)
        best = np.where(rng.random(n) >= p_ok, 0.0, best)
        return best

    # Pathirage with javelin/workload tail
    p_day = rng.normal(89.8, 1.8, n)  # expected mean throw ~89.8 -> best of 6 ~91.6m!
    p_day -= (rng.random(n) < 0.10) * rng.uniform(2.5, 6.0, n)  # replacement javelin / fatigue bad day
    p_best = np.max(p_day[:, None] + rng.normal(0.0, 1.45, (n, 6)), axis=1)
    p_best = np.where(rng.random(n) < 0.055, 0.0, p_best)  # DNS/injury/foul-out

    ry_best = sim_best6(84.4, 2.3, 0.95)  # best of 6 ~86.6m, upside 89m
    # Nadeem bimodal: 72% hampered (~81.5m), 28% partial/full championship surge (~86.8m, high sd!)
    nad_healthy = rng.random(n) < 0.28
    nad_mu = np.where(nad_healthy, 86.2, 81.0)
    nad_sd = np.where(nad_healthy, 2.8, 2.2)
    nad_day = rng.normal(nad_mu, nad_sd * 0.75)
    nad_best = np.max(nad_day[:, None] + rng.normal(0.0, 1.8, (n, 6)), axis=1)
    nad_best = np.where(rng.random(n) < 0.12, 0.0, nad_best)  # withdrawal/DNS risk higher for injured Nadeem

    ys_best = sim_best6(83.2, 2.3, 0.95)  # Yuta Sakiyama (home PB 87.16)
    yv_best = sim_best6(82.4, 2.1, 0.95)  # Yash Vir Singh (85.41 CWG bronze)
    ot_best = sim_best6(83.3, 2.2, 0.98)  # Rest of Asia best (Genki Dean, Sumeda Ranasinghe, China, etc.)

    names = ["Rumesh Tharanga Pathirage", "Rohit Yadav", "Arshad Nadeem", "Yuta Sakiyama", "Yash Vir Singh", "Rest_of_Asia"]
    mat = np.vstack([p_best, ry_best, nad_best, ys_best, yv_best, ot_best])
    idx = np.argmin(-mat, axis=0)
    for i, nm in enumerate(names):
        print(f"      {nm:28s}: {float(np.mean(idx == i)):.4f}")


# ==============================================================================
# MODEL 4: qid=996188 — PUYO PUYO CHAMPIONS (Sat Sep 26, T+3d — ALL 10 PLAYERS!)
# ==============================================================================
def model_996188_puyo():
    print("\n" + "=" * 76)
    print("MODEL 4: qid=996188 — Puyo Puyo Champions (EXACT 10-PLAYER FIELD!)")
    print("=" * 76)
    # COMPLETE 10-PLAYER ROSTER REVEALED BY PHILSTAR (SEP 22) + HINDUSTAN TIMES (SEP 23):
    #   Group A: Yuki Kurihara (JPN), Kang Dong-shin (KOR), Yu Wing-lim (HKG), Karl Gonzalvo (PHI), Kazakhstan (KAZ)
    #   Group B: Kuo Tzu-ang (TPE), Mun June Justin Koh (SGP), Tanarak Wongkitikun (THA), Paritosh (IND), Munkhzorig Ganbold (MGL)
    #
    # EXACT FORMAT (Sportstar / Philstar / Seoul Shinmun Sep 22):
    #   - Thu Sep 24: Two 5-player Round Robin groups (10 matches each).
    #   - Sat Sep 26: 10-player Knockout Bracket!
    #       * 2 First-Round Play-ins (A4 vs B5, B4 vs A5) + 6 byes (top 3 each group -> directly to QF!)
    #       * 4 QFs (15-min slots!):
    #           QF1: A1 vs Winner(B4/A5)
    #           QF2: B2 vs A3
    #           QF3: B1 vs Winner(A4/B5)
    #           QF4: A2 vs B3
    #       * 2 SFs (30-min slots!):
    #           SF1: W(QF1) vs W(QF2)   [A1 side!]
    #           SF2: W(QF3) vs W(QF4)   [B1 & A2 side!!]
    #       * Final (08:15 IST Sat Sep 26)
    #
    # Note: In Puyo Puyo Champions, skill gaps between Japanese pro-license champions and non-JPN amateurs are HUGE,
    # BUT:
    #   - Match format uncertainty (FT5 / Bo3 sets in short 15-min QF slots -> higher upset variance than long FT10!)
    #   - 11-year-old stage-nerve tail on Yuki Kurihara (explicitly warned by SEGA esports head Yasunobu!)
    #   - Rating uncertainty on Kang Dong-shin (8-yr Korean vet, named main rival), Kuo Tzu-ang (Acliv, top TPE player),
    #     Yu Wing-lim (HKG), and Singapore's Mun June Justin Koh!

    rng = np.random.default_rng(99618823)
    n_sims = 60000

    grpA = ["Yuki Kurihara", "Kang Dong-shin", "Yu Wing-lim", "Karl Gonzalvo", "Kazakhstan"]
    grpB = ["Kuo Tzu-ang", "Mun June Justin Koh", "Tanarak Wongkitikun", "Paritosh", "Munkhzorig Ganbold"]

    # Logistic match win probability from Elo ratings (400 scale; shorter QF sets compress Elo scale slightly to 440)
    def win_prob(ra, rb, scale=400.0):
        return 1.0 / (1.0 + 10.0 ** ((rb - ra) / scale))

    def play_match(a, b, r, scale=400.0):
        return a if rng.random() < win_prob(r[a], r[b], scale) else b

    def play_group(players, r):
        wins = {p: 0 for p in players}
        h2h = {}
        for i in range(len(players)):
            for j in range(i + 1, len(players)):
                p1, p2 = players[i], players[j]
                w = play_match(p1, p2, r, scale=420.0)
                wins[w] += 1
                h2h[(p1, p2)] = 1 if w == p1 else -1
                h2h[(p2, p1)] = -h2h[(p1, p2)]
        order = sorted(players, key=lambda p: (wins[p], rng.random()), reverse=True)
        # Resolve exact 2-way ties by H2H
        for i in range(len(order) - 1):
            p1, p2 = order[i], order[i + 1]
            if wins[p1] == wins[p2]:
                tied = [p for p in order if wins[p] == wins[p1]]
                if len(tied) == 2 and h2h.get((p2, p1), 0) > 0:
                    order[i], order[i + 1] = order[i + 1], order[i]
        return order

    # Regimes spanning skill-gap & stage-nerve uncertainty:
    # Check implied H2H win prob of Kurihara vs Kang:
    #   +220 Elo -> 78.0%; +260 Elo -> 81.7%; +180 Elo -> 73.8%
    regimes = [
        ("R1: Base (JPN Pro strong edge, KOR/TPE solid, SGP/HKG dark horses, 7% Kurihara stage-nerve/DNS)",
         0.50,
         {"Yuki Kurihara": 2180, "Kang Dong-shin": 1955, "Kuo Tzu-ang": 1915,
          "Yu Wing-lim": 1680, "Mun June Justin Koh": 1670,
          "Tanarak Wongkitikun": 1550, "Karl Gonzalvo": 1540,
          "Paritosh": 1480, "Munkhzorig Ganbold": 1460, "Kazakhstan": 1450},
         0.06, 0.02),
        ("R2: Higher Variance / Shorter Sets / Stage Pressure on 11yo",
         0.30,
         {"Yuki Kurihara": 2130, "Kang Dong-shin": 1965, "Kuo Tzu-ang": 1930,
          "Yu Wing-lim": 1730, "Mun June Justin Koh": 1720,
          "Tanarak Wongkitikun": 1600, "Karl Gonzalvo": 1590,
          "Paritosh": 1520, "Munkhzorig Ganbold": 1500, "Kazakhstan": 1490},
         0.10, 0.025),
        ("R3: Dominant JPN Pro Gap (Kurihara crushes non-JPN field)",
         0.20,
         {"Yuki Kurihara": 2260, "Kang Dong-shin": 1950, "Kuo Tzu-ang": 1900,
          "Yu Wing-lim": 1640, "Mun June Justin Koh": 1630,
          "Tanarak Wongkitikun": 1500, "Karl Gonzalvo": 1500,
          "Paritosh": 1440, "Munkhzorig Ganbold": 1420, "Kazakhstan": 1420},
         0.04, 0.015),
    ]

    blended = Counter()
    for label, w_reg, base_r, nerve_p, dns_p in regimes:
        champs = Counter()
        for _ in range(n_sims):
            # Tournament-level rating uncertainty (especially unknown international relative levels!)
            r = {}
            for p, val in base_r.items():
                sd = 75.0 if p in ("Yuki Kurihara", "Kang Dong-shin", "Kuo Tzu-ang") else 110.0
                r[p] = val + rng.normal(0.0, sd)
            # 11yo stage-nerve / cold-hands day in KO
            if rng.random() < nerve_p:
                r["Yuki Kurihara"] -= rng.uniform(160.0, 320.0)
            # Rare DNS/illness
            if rng.random() < dns_p:
                r["Yuki Kurihara"] -= 2000.0

            ordA = play_group(grpA, r)
            ordB = play_group(grpB, r)

            # Knockout Sat Sep 26 (2 play-ins -> 4 QFs [shorter 15m -> scale=450] -> 2 SFs [30m -> scale=380] -> Final [360])
            pi1 = play_match(ordB[3], ordA[4], r, scale=450.0)
            pi2 = play_match(ordA[3], ordB[4], r, scale=450.0)

            qf1 = play_match(ordA[0], pi1, r, scale=450.0)
            qf2 = play_match(ordB[1], ordA[2], r, scale=450.0)
            qf3 = play_match(ordB[0], pi2, r, scale=450.0)
            qf4 = play_match(ordA[1], ordB[2], r, scale=450.0)

            sf1 = play_match(qf1, qf2, r, scale=380.0)
            sf2 = play_match(qf3, qf4, r, scale=380.0)
            gold = play_match(sf1, sf2, r, scale=360.0)
            champs[gold] += 1

        print(f"\n  [{w_reg:.2f}] {label}")
        print("        " + ", ".join(f"{k}={champs[k]/n_sims:.4f}" for k in
              ["Yuki Kurihara", "Kang Dong-shin", "Kuo Tzu-ang", "Yu Wing-lim", "Mun June Justin Koh"]))
        for k, cnt in champs.items():
            blended[k] += w_reg * (cnt / n_sims)

    print("\n  >>> BLENDED EXACT-10-PLAYER PROBABILITIES (qid=996188):")
    for k, v in blended.most_common():
        print(f"      {k:24s}: {v:.4f}")
    top5 = blended.most_common(5)
    print(f"      Top-5 sum = {sum(v for _, v in top5):.4f}, Outside = {1 - sum(v for _, v in top5):.4f}")


if __name__ == "__main__":
    model_190556_200breast()
    model_686508_men100m()
    model_695205_javelin()
    model_996188_puyo()
