"""
Quantitative Bayesian Monte Carlo Updates — Mon Sep 21, 2026 (Asian Games Day 2)
Batch: asian_games_swim_wt_track

Updates driven by LIVE Day 2 Tokyo Aquatics Centre Finals:
  1. qid=300850: Women's 400m IM (Wed Sep 23, T+2d)
     - LIVE DATA: Yu Zidi won 200m IM in 2:06.10 (Asian Record, WJR, #2 All-Time, -1.31s PB!)
       beating Yu Yiting (2:07.99) by 1.89s and Mio Narita (2:10.40) by 4.30s!
     - Day 1 LIVE DATA: Yu Zidi won 200m fly in 2:05.08 GR (-0.63s PB).
     - Schedule: Full rest day Tue Sep 22 before Wed Sep 23 400m IM; NOT on 4x200m free relay.
  2. qid=190556: Men's 200m Breaststroke (Thu Sep 24, T+3d)
     - LIVE DATA: Mon Sep 21 Men's 100m Breaststroke Final:
         * T-1st Gold: Dong Zhihao (CHN) 58.64 (0.07s off 58.57 PB; roared back late!)
         * T-1st Gold: Shin Ohashi (JPN) 58.64 (0.10s off 58.54 NR/WJR; led early, caught late)
         * 3rd Bronze: Qin Haiyang (CHN) 59.01 (0.37s behind both; ~0.7-0.8s off 2025 Worlds 58.23)
"""
import math
from collections import Counter
import numpy as np


# ==============================================================================
# MODEL 1: qid=300850 — WOMEN'S 400m IM (Wed Sep 23, T+2d)
# ==============================================================================
def model_women_400im():
    print("=" * 74)
    print("MODEL 1: qid=300850 — Women's 400m IM (Post-Day 2: Yu Zidi 2:06.10 AR!)")
    print("=" * 74)
    # Baselines (in seconds: 4:30.00 = 270.00s):
    # - Yu Zidi (CHN, 13yo):
    #     June Trials: 4:30.79 (270.79s).
    #     Live Tokyo form: -0.63s PB in 200m fly (2:05.08), -1.31s PB in 200m IM (2:06.10, AR, #2 all-time).
    #     Implied tapered 400m IM readiness: ~268.6s - 269.6s (4:28.6 - 4:29.6), i.e., ~1.5-2.0s faster than June!
    #     Residual risks over next 48h (Tue rest -> Wed heats/final):
    #       * DQ risk (400m IM turns/breaststroke touch/false start): ~2.8%
    #       * Sudden illness/injury/DNS/heats mishap over 48h: ~1.8%
    #       * Accumulated 13yo multi-day fatigue "heavy legs" tail: ~8% chance of +3.0..+6.5s slower swim
    # - Ke Wenxi (CHN #2 entry):
    #     June Trials: 4:33.59 (273.59s).
    #     China team taper boost in Tokyo is strong (China won 11/14 golds Days 1-2, multiple PBs/ARs).
    #     Expected mean: ~272.7s (4:32.7), sd ~1.65s (upside to ~4:30.5-4:31.5 if she drops 2s like teammates).
    #     DQ/DNS risk: ~3.5% combined.
    # - Mio Narita (JPN #1):
    #     2025 Worlds silver PB: 4:33.26 (273.26s); Aug Pan Pacs: 4:39.49 (279.49s).
    #     Live Day 2 200m IM: 2:10.40 (0.86s faster than her 2:11.26 Pan Pacs -> partial home rebound!).
    #     Implied 400m IM mean: ~275.5s (4:35.5), sd ~1.9s (could rebound to ~4:33 on a great swim).
    #     DQ/DNS risk: ~3.0%.
    # - Waka Kobori (JPN #2):
    #     Aug Pan Pacs: 4:39.23 (279.23s), PB ~4:36-4:37.
    #     Implied mean: ~277.3s (4:37.3), sd ~1.8s.
    # - Yu Yiting (CHN — NOT entered in 400m IM; only emergency sub if Yu Zidi or Ke Wenxi scratches before heats):
    #     If either Chinese swimmer DNS before heats (~1.5% each), ~20% chance Yu Yiting subs in (she also has 100m fly Wed Sep 23!).

    scenarios = [
        # (label, weight, yz_mu, yz_sd, yz_dq, yz_dns, yz_fat_p, kw_mu, kw_sd, mn_mu, mn_sd)
        ("Base: Yu peaks (~4:29.0), Ke solid (~4:32.7), Narita partial rebound (~4:35.5)",
         0.45, 269.0, 1.45, 0.028, 0.018, 0.08, 272.7, 1.65, 275.5, 1.90),
        ("Conservative/Fatigue: Yu heavier legs (~4:30.0, 13% fatigue tail), Ke peaks (~4:32.0)",
         0.30, 270.0, 1.70, 0.032, 0.022, 0.13, 272.0, 1.65, 274.8, 1.90),
        ("Dominant: Yu crushes WR pace (~4:28.0), Ke near Trials (~4:33.3), Narita (~4:36.2)",
         0.25, 268.0, 1.35, 0.025, 0.015, 0.05, 273.3, 1.65, 276.2, 1.90),
    ]

    rng = np.random.default_rng(30085021)
    n = 150000
    blended = Counter()

    for label, w, yz_mu, yz_sd, yz_dq, yz_dns, yz_fat_p, kw_mu, kw_sd, mn_mu, mn_sd in scenarios:
        wins = Counter()
        for _ in range(n):
            cands = []
            yz_dns_flag = rng.random() < yz_dns
            kw_dns_flag = rng.random() < 0.015

            if not yz_dns_flag and (rng.random() >= yz_dq):
                fat = rng.uniform(3.0, 6.5) if rng.random() < yz_fat_p else 0.0
                t = rng.normal(yz_mu, yz_sd) + fat
                cands.append((t, "Yu Zidi"))

            if not kw_dns_flag and (rng.random() >= 0.025):
                bad = rng.uniform(2.0, 4.5) if rng.random() < 0.06 else 0.0
                t = rng.normal(kw_mu, kw_sd) + bad
                cands.append((t, "Ke Wenxi"))

            # Emergency sub Yu Yiting only if a CHN swimmer scratches BEFORE heats (and she has 100m fly same day!)
            if (yz_dns_flag or kw_dns_flag) and rng.random() < 0.18:
                cands.append((rng.normal(275.0, 1.8), "Yu Yiting"))

            if rng.random() >= 0.030:
                bad = rng.uniform(2.0, 4.5) if rng.random() < 0.07 else 0.0
                cands.append((rng.normal(mn_mu, mn_sd) + bad, "Mio Narita"))

            if rng.random() >= 0.030:
                cands.append((rng.normal(277.3, 1.8), "Waka Kobori"))

            cands.append((rng.normal(280.5, 2.0), "Rest_of_Asia"))
            wins[min(cands)[1]] += 1

        print(f"\n  [{w:.2f}] {label}")
        for k in ["Yu Zidi", "Ke Wenxi", "Mio Narita", "Waka Kobori", "Yu Yiting", "Rest_of_Asia"]:
            p = wins[k] / n
            blended[k] += w * p
            print(f"        {k:15s}: {p:.4f}")

    print("\n  >>> BLENDED POST-DAY-2 PROBABILITIES (qid=300850):")
    for k, v in blended.most_common():
        print(f"      {k:15s}: {v:.4f}")


# ==============================================================================
# MODEL 2: qid=190556 — MEN'S 200m BREASTSTROKE (Thu Sep 24, T+3d)
# ==============================================================================
def model_men_200breast():
    print("\n" + "=" * 74)
    print("MODEL 2: qid=190556 — Men's 200m Breaststroke (Bayesian Update from 100m Final)")
    print("=" * 74)
    # BAYESIAN BIVARIATE LATENT-FORM MODEL:
    # For each swimmer i, let (X_100, X_200) be their (100m final time, 200m final time) in Tokyo.
    # Model:
    #   X_100 = mu100_i + eps100_i,   eps100_i ~ N(0, sd100_i^2)
    #   X_200 = mu200_i + eps200_i,   eps200_i ~ N(0, sd200_i^2)
    #   Corr(eps100_i, eps200_i) = rho_i (same-meet form/taper correlation, typically 0.55 - 0.75!)
    #
    # By bivariate normal conditioning, observing X_100 = x_obs updates X_200 to:
    #   mu200_post = mu200_i + rho_i * (sd200_i / sd100_i) * (x_obs - mu100_i)
    #   sd200_post = sd200_i * sqrt(1 - rho_i^2)
    # Plus additional race-day execution variance on Thu Sep 24 (pacing, fatigue, stroke execution)!
    #
    # PRIOR BASELINES (calibrated to reproduce pre-Day 2 forecast: Ohashi 0.42, Qin 0.31, Dong 0.20, Watanabe 0.04):
    # 1. Shin Ohashi (17yo, JPN):
    #    - 100m prior: 58.65 +/- 0.35s (58.54 Pan Pacs NR/WJR). Observed: 58.64 (z = -0.03 -> right on peak!).
    #    - 200m prior: 127.45s (2:07.45) +/- 0.95s (2:06.59 March Tokyo WJR, 2:08.27 Pan Pacs after 34.04 fade).
    #      Note: asymmetric fade tail if he goes out too fast again!
    # 2. Qin Haiyang (27yo, CHN):
    #    - 100m prior: 58.45 +/- 0.40s (58.23 2025 Worlds gold, 57.69 2023 AR). Observed: 59.01 (z = +1.40 -> SLOW!).
    #    - 200m prior: 127.65s (2:07.65) +/- 1.05s (2:07.41 2025 Worlds gold, 2:05.48 2023 WR).
    # 3. Dong Zhihao (21yo, CHN):
    #    - 100m prior: 59.05 +/- 0.40s (58.57 PB June Nationals; historically more 59.0-59.3 in 100m).
    #      Observed: 58.64 (z = -1.03 -> SHARP PEAK + roaring closing 50m!).
    #    - 200m prior: 128.05s (2:08.05) +/- 1.00s (2:07.94 2024 Worlds gold, elite closer).
    # 4. Ippei Watanabe (JPN):
    #    - 200m baseline: 129.10s (2:09.10) +/- 0.85s (2:08.57 March, 2:09.72 Pan Pacs).
    # 5. Cho Sung-jae (KOR):
    #    - 200m baseline: 129.90s (2:09.90) +/- 0.90s.
    # 6. Rest of Asia (e.g., Yamato Fukasawa if entered, Yu Hanaguruma, etc.):
    #    - 200m baseline: 130.0s +/- 1.0s.

    rng = np.random.default_rng(19055621)
    n = 150000

    # First verify our PRIOR reproduces Sep 20 (~0.42 / 0.31 / 0.20 / 0.04 / 0.01)
    def sim_field(params, oh_fade_p=0.14, oh_fade_add=(0.6, 1.7), dq_dns=0.025):
        wins = Counter()
        for _ in range(n):
            cands = []
            for name, mu, sd, is_ohashi in params:
                if rng.random() < dq_dns:
                    continue
                t = rng.normal(mu, sd)
                if is_ohashi and rng.random() < oh_fade_p:
                    t += rng.uniform(*oh_fade_add)
                cands.append((t, name))
            cands.append((rng.normal(130.1, 1.0), "Rest_of_Asia"))
            wins[min(cands)[1]] += 1
        return {k: wins[k] / n for k in ["Shin Ohashi", "Dong Zhihao", "Qin Haiyang", "Ippei Watanabe", "Cho Sung-jae", "Rest_of_Asia"]}

    prior_params = [
        ("Shin Ohashi",    127.45, 0.95, True),
        ("Qin Haiyang",    127.65, 1.05, False),
        ("Dong Zhihao",    128.05, 1.00, False),
        ("Ippei Watanabe", 129.10, 0.85, False),
        ("Cho Sung-jae",   129.90, 0.90, False),
    ]
    prior_res = sim_field(prior_params)
    print("\n  [CHECK] PRIOR (Pre-100m Final):")
    for k, v in prior_res.items():
        print(f"        {k:16s}: {v:.4f}")

    # Now compute POSTERIOR across correlation & interpretation regimes!
    # Observations: Ohashi = 58.64, Dong = 58.64, Qin = 59.01
    # Note: Even after conditioning on 100m form, race-day Thu 200m execution noise keeps posterior SD >= 0.72-0.80s
    regimes = [
        # (label, weight, rho_oh, rho_qh, rho_dz, dz_close_bonus, oh_fade_p)
        ("R1: Moderate 100m->200m corr (rho=0.60), Dong closing edge (-0.15s)",
         0.40, 0.55, 0.60, 0.60, -0.15, 0.14),
        ("R2: Strong 100m->200m corr (rho=0.72), Dong closing edge (-0.25s), Ohashi late-fade risk",
         0.30, 0.65, 0.72, 0.72, -0.25, 0.17),
        ("R3: Weak 100m->200m corr (rho=0.42; Qin focused on 200m, Ohashi home-pool 200m peak)",
         0.30, 0.45, 0.42, 0.45, -0.05, 0.11),
    ]

    blended = Counter()
    for label, w, r_oh, r_qh, r_dz, dz_bonus, oh_fp in regimes:
        # Bayesian update for each of the Big 3:
        # Ohashi: mu100=58.65, sd100=0.35, obs=58.64 -> dz=-0.01
        oh_mu = 127.45 + r_oh * (0.95 / 0.35) * (58.64 - 58.65)
        oh_sd = math.sqrt((0.95 ** 2) * (1 - r_oh ** 2) + 0.35 ** 2)  # keep min execution sd

        # Qin: mu100=58.45, sd100=0.40, obs=59.01 -> +0.56s slower than prior!
        qh_mu = 127.65 + r_qh * (1.05 / 0.40) * (59.01 - 58.45)
        qh_sd = math.sqrt((1.05 ** 2) * (1 - r_qh ** 2) + 0.35 ** 2)

        # Dong: mu100=59.05, sd100=0.40, obs=58.64 -> -0.41s faster than prior! + closing bonus
        dz_mu = 128.05 + r_dz * (1.00 / 0.40) * (58.64 - 59.05) + dz_bonus
        dz_sd = math.sqrt((1.00 ** 2) * (1 - r_dz ** 2) + 0.35 ** 2)

        post_params = [
            ("Shin Ohashi",    oh_mu, oh_sd, True),
            ("Dong Zhihao",    dz_mu, dz_sd, False),
            ("Qin Haiyang",    qh_mu, qh_sd, False),
            ("Ippei Watanabe", 129.10, 0.85, False),
            ("Cho Sung-jae",   129.90, 0.90, False),
        ]
        res = sim_field(post_params, oh_fade_p=oh_fp)
        print(f"\n  [{w:.2f}] {label}")
        print(f"        Post means: Ohashi={oh_mu:.2f}s (sd={oh_sd:.2f}), Dong={dz_mu:.2f}s (sd={dz_sd:.2f}), Qin={qh_mu:.2f}s (sd={qh_sd:.2f})")
        for k, v in res.items():
            blended[k] += w * v
            print(f"        {k:16s}: {v:.4f}")

    print("\n  >>> BLENDED POST-100m-FINAL PROBABILITIES (qid=190556):")
    for k, v in blended.most_common():
        print(f"      {k:16s}: {v:.4f}")


if __name__ == "__main__":
    model_women_400im()
    model_men_200breast()
