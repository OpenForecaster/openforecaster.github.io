"""
Quantitative Bayesian & Monte Carlo Models — Thu Sep 24, 2026 (Asian Games Day 5)
Batch: asian_games_sprint_esports

Models:
  1. qid=686508: Men's 100m (POST-HEATS! SF & Final TOMORROW Fri Sep 25, T+1d)
  2. qid=996188: Puyo Puyo Champions (POST-GROUP-STAGE! Exact Sat Sep 26 KO Bracket, T+2d)
  3. qid=695205: Men's Javelin Throw (Pre-Qual Sanity Check, Qual Sat Sep 26, Final Mon Sep 28)
"""
from collections import Counter
import math
import numpy as np


# ==============================================================================
# MODEL 1: qid=686508 — MEN'S 100m (POST-THU-SEP-24 HEATS, T+1d TO SF & FINAL)
# ==============================================================================
def model_686508_men100m_post_heats():
    print("=" * 78)
    print("MODEL 1: qid=686508 — Men's 100m (POST-HEATS, 2 ROUNDS LEFT: SF & FINAL)")
    print("=" * 78)
    # Verified Thu Sep 24 Heat Results (6 heats; top 3 + 6 fastest = 24 to Fri SF):
    #   #1 overall: Puripol Boonson (THA)          9.95  (Heat 1 winner! Beat Zeng Keli 10.22 by 0.27s, Kujur 10.36 by 0.41s!)
    #   #2 overall: Ali Anwar Al-Balushi (OMA)    10.06  (Heat 3 winner! Beat Bewesa 10.23 by 0.17s, Abdullah Abkar 10.32 by 0.26s!)
    #   #3 overall: Muhammad Azeem Fahmi (MAS)    10.17  (Heat 5 winner; 2023 AG bronze, 10.09 NR)
    #   #4 overall: Zeng Keli (CHN)               10.22  (Heat 1, 2nd behind Puripol)
    #   #5 overall: Namadi Joeljin (KOR)          10.23  (Heat 2 winner; 10.13 PB; beat Koike 10.33, Chen 10.33)
    #   #6 overall: Daniel Kasama Bewesa (KOR)    10.23  (Heat 3, 2nd behind Al-Balushi; 10.13 PB)
    #   Other confirmed:
    #     Mulham Al-Balushi (OMA)                 10.29  (Heat 4/6 winner; beat Gurindervir Singh 10.38, Taftian 10.49)
    #     Abdullah Abkar Mohammed (KSA)           10.32  (Heat 3, 3rd — 0.26s behind Al-Balushi in same heat!)
    #     Yuki Koike (JPN)                        10.33  (Heat 2, 2nd — 0.10s behind Namadi Joeljin)
    #     Animesh Kujur (IND)                     10.36  (Heat 1, 3rd)
    #     Gurindervir Singh (IND)                 10.38  (Heat 4/6, 2nd — "could relax midway")
    #   Unreported Heat (Heat 4 or 6):
    #     Shuhei Tada (JPN) & Xie Zhenye (CHN) MUST have run >= 10.24 (since 10.23 = 5th & 6th overall!).
    #     Most likely coasted/eased into SF in ~10.24-10.34, with ~12% unverified-status discount (DNS/FS/slow).
    #
    # Bayesian speed update from heats -> Friday Final expected performance (wind-neutralized):
    #   - Puripol Boonson: 9.95 in Heat 1 (+0.27s over Zeng Keli, +0.41s over Kujur in SAME wind!)
    #     Even with possible tailwind, his net level is ~9.96-10.00s (0.04s faster than pre-heat prior!).
    #     Remaining 2-round failure risk (SF+Final): ~2.5% false start + ~3.0% hamstring/pull-up (note 9.95 heat effort!)
    #     = ~5.5% base failure, ~7.5% pessimistic, ~4.0% optimistic.
    #   - Ali Anwar Al-Balushi: 10.06 in Heat 3 (+0.17s over Bewesa, +0.26s over Abdullah in SAME wind!)
    #     Huge upward update: posterior expected final time ~10.06-10.09s!
    #   - Muhammad Azeem Fahmi: 10.17 Heat 5 winner (controlled), 2023 AG bronze -> ~10.12-10.15s.
    #   - Shuhei Tada: home track, likely coasted Heat 4/6 (>=10.24) -> ~10.13s conditional on healthy SF advance (p_ok=0.84).
    #   - Xie Zhenye: defending champ, likely coasted (>=10.24) -> ~10.14s conditional on healthy SF advance (p_ok=0.82).
    #   - Zeng Keli: 10.22 behind Puripol -> ~10.14-10.16s.
    #   - Yuki Koike: 10.33 (2nd to Joeljin 10.23) -> ~10.16s.
    #   - Abdullah Abkar Mohammed: 10.32 (3rd behind Al-Balushi 10.06 & Bewesa 10.23) -> clearly off 9.96 peak, ~10.17-10.20s!
    #   - Namadi Joeljin & Daniel Bewesa: both 10.23 (10.13 PBs) -> ~10.17s each.
    #   - Gurindervir Singh, Mulham Al-Balushi, Animesh Kujur, others: ~10.19-10.25s.

    rng = np.random.default_rng(68650824)
    n = 200000

    # Regimes spanning uncertainty over:
    # (a) Heat 1 wind/effort for Puripol (was 9.95 easy sub-9.95 form, or full effort that adds Fri fatigue?)
    # (b) How hard Tada / Xie / Koike / Abdullah were coasting vs genuinely slower than Al-Balushi/Azeem
    regimes = [
        # (label, weight, puripol_mu, puripol_sd, puripol_fail, puripol_badstart_p, balushi_mu, coast_bonus)
        ("R1: Base Post-Heat (Puripol 9.97s, Al-Balushi 10.07s, moderate coasting for veterans)",
         0.50, 9.97, 0.065, 0.055, 0.06, 10.07, 0.00),
        ("R2: Veterans Coasted / Puripol Heat-Effort Fatigue (Puripol 10.00s, higher sd=0.072, rivals -0.02s)",
         0.30, 10.00, 0.072, 0.075, 0.08, 10.07, -0.02),
        ("R3: Puripol Blistering Form (9.95 was controlled -> 9.94s final, sd=0.060)",
         0.20, 9.94, 0.060, 0.042, 0.04, 10.08, +0.01),
    ]

    # (name, p_ok_2rounds, base_mu, sd, is_veteran_coaster)
    rivals = [
        ("Ali Anwar Al-Balushi",     0.955, 10.07, 0.068, False),
        ("Muhammad Azeem Fahmi",     0.955, 10.13, 0.068, False),
        ("Shuhei Tada",              0.840, 10.13, 0.068, True),
        ("Xie Zhenye",               0.820, 10.14, 0.072, True),
        ("Zeng Keli",                0.955, 10.15, 0.070, False),
        ("Yuki Koike",               0.950, 10.16, 0.068, True),
        ("Abdullah Abkar Mohammed",  0.945, 10.18, 0.075, True),
        ("Namadi Joeljin",           0.955, 10.17, 0.066, False),
        ("Daniel Kasama Bewesa",     0.955, 10.17, 0.066, False),
        ("Mulham Al-Balushi",        0.955, 10.20, 0.068, False),
        ("Gurindervir Singh",        0.950, 10.19, 0.068, True),
        ("Animesh Kujur",            0.950, 10.22, 0.068, False),
        ("Field_Other_Best",         0.950, 10.19, 0.072, False),
    ]

    blended = Counter()
    for label, w, p_mu, p_sd, p_fail, p_bs, b_mu, c_bonus in regimes:
        names = ["Puripol Boonson"] + [r[0] for r in rivals]
        times = []
        # Puripol
        t_p = rng.normal(p_mu, p_sd, n) + (rng.random(n) < p_bs) * rng.uniform(0.08, 0.18, n)
        t_p = np.where(rng.random(n) < p_fail, 99.0, t_p)
        times.append(t_p)
        for rname, p_ok, r_mu, r_sd, is_vet in rivals:
            mu = b_mu if rname == "Ali Anwar Al-Balushi" else (r_mu + (c_bonus if is_vet else 0.0))
            t_r = rng.normal(mu, r_sd, n)
            t_r = np.where(rng.random(n) >= p_ok, 99.0, t_r)
            times.append(t_r)
        mat = np.vstack(times)
        idx = np.argmin(mat, axis=0)
        res = {nm: float(np.mean(idx == i)) for i, nm in enumerate(names)}
        print(f"\n  [{w:.2f}] {label}")
        top6 = sorted(res.items(), key=lambda x: -x[1])[:6]
        print("        " + ", ".join(f"{k}={v:.4f}" for k, v in top6))
        for nm, val in res.items():
            blended[nm] += w * val

    print("\n  >>> BLENDED POST-HEATS PROBABILITIES (qid=686508):")
    for k, v in blended.most_common():
        print(f"      {k:26s}: {v:.4f}")
    top5 = blended.most_common(5)
    print(f"      Top-5 sum = {sum(v for _, v in top5):.4f}, Outside = {1 - sum(v for _, v in top5):.4f}")


# ==============================================================================
# MODEL 2: qid=996188 — PUYO PUYO CHAMPIONS (POST-GROUP-STAGE EXACT BRACKET!)
# ==============================================================================
def model_996188_puyo_post_groups():
    print("\n" + "=" * 78)
    print("MODEL 2: qid=996188 — Puyo Puyo Champions (EXACT SAT SEP 26 KO BRACKET)")
    print("=" * 78)
    # COMPLETE THU SEP 24 GROUP STAGE RESULTS (All matches Best-of-5 / First-to-3!):
    #   GROUP A:
    #     A1: Yuki Kurihara (JPN)         4-0  (3-0 Gonzalvo, 3-1 Kang, 3-0 Yu, 3-0 Pivovarov) -> 12-1 games!
    #     A2: Kang Dong-shin (KOR)        3-1  (1-3 Kurihara, 3-2 Gonzalvo, 3-0 Yu, 3-0 Pivovarov) -> 10-5 games
    #     A3: Karl Gonzalvo (PHI)         2-2  (0-3 Kurihara, 2-3 Kang, 3-2 Yu, 3-0 Pivovarov) -> 8-8 games
    #     A4: Yu Wing-lim (HKG)           1-3  (0-3 Kurihara, 0-3 Kang, 2-3 Gonzalvo, W Pivovarov)
    #     A5: Alexandr Pivovarov (KAZ)    0-4  (0-3 Kurihara, 0-3 Kang, 0-3 Gonzalvo, L Yu)
    #   GROUP B:
    #     B1: Kuo Tzu-ang (TPE)           4-0  (3-0 Wongkitikun, 3-1 Ganbold, 3-0 Paritosh, 3-1 Koh) -> 12-2 games!
    #     B2: Tanarak Wongkitikun (THA)   3-1  (0-3 Kuo, 3-2 Paritosh, W Koh, W Ganbold)
    #     B3: Paritosh (IND)              2-2  (3-0 Ganbold, 3-2 Koh, 0-3 Kuo, 2-3 Wongkitikun) -> 8-8 games
    #     B4/B5: Mun June Justin Koh (SGP) & Munkhzorig Ganbold (MGL) (both lost to Kuo, Wongkitikun, Paritosh)
    #
    # EXACT SATURDAY SEP 26 KNOCKOUT BRACKET:
    #   Play-in 1: B4 (Koh/Ganbold) vs A5 (Pivovarov)
    #   Play-in 2: A4 (Yu Wing-lim) vs B5 (Ganbold/Koh)
    #   QF1: A1 (Yuki Kurihara)        vs Winner(Play-in 1)
    #   QF2: B2 (Tanarak Wongkitikun)  vs A3 (Karl Gonzalvo)  [explicitly confirmed by Spin.ph!]
    #   QF3: B1 (Kuo Tzu-ang)          vs Winner(Play-in 2)
    #   QF4: A2 (Kang Dong-shin)       vs B3 (Paritosh)
    #   SF1: Winner(QF1) vs Winner(QF2)  --> Kurihara's side!
    #   SF2: Winner(QF3) vs Winner(QF4)  --> Kuo Tzu-ang vs Kang Dong-shin!!
    #   FINAL: Winner(SF1) vs Winner(SF2)
    #
    # Game-level Bayesian Bradley-Terry fitting:
    # Fit latent per-game strength theta_i where P(i beats j in 1 game) = sigmoid(theta_i - theta_j)
    # using MAP / Laplace approximation on observed Group A + Group B game counts + informative prior!
    #
    # Observed game records (winner, loser, w_games, l_games):
    # Note: where exact B4/B5/A4-A5 game score wasn't reported, use conservative 3-1 estimates.
    players = [
        "Yuki Kurihara", "Kang Dong-shin", "Kuo Tzu-ang",
        "Karl Gonzalvo", "Tanarak Wongkitikun", "Paritosh",
        "Yu Wing-lim", "Mun June Justin Koh", "Munkhzorig Ganbold", "Alexandr Pivovarov"
    ]
    idx_map = {p: i for i, p in enumerate(players)}

    # Prior means on logit scale (where delta=+1.0 => 73.1% per single game => 87.4% in Bo5!)
    # Prior from pre-tournament info (SEGA pro license for Kurihara, KOR/TPE top reps, others amateur):
    prior_mu = np.array([
        2.10,  # Yuki Kurihara (JPN pro)
        0.95,  # Kang Dong-shin (KOR vet)
        0.85,  # Kuo Tzu-ang (TPE top)
       -0.45,  # Karl Gonzalvo
       -0.45,  # Tanarak Wongkitikun
       -0.65,  # Paritosh
       -0.15,  # Yu Wing-lim
       -0.25,  # Mun June Justin Koh
       -0.75,  # Munkhzorig Ganbold
       -0.80,  # Alexandr Pivovarov
    ])
    prior_sd = np.array([0.65, 0.65, 0.65, 0.85, 0.85, 0.85, 0.80, 0.80, 0.85, 0.85])

    # Observed single-game results (i, j, wins_i, wins_j)
    obs = [
        # Group A
        ("Yuki Kurihara", "Kang Dong-shin", 3, 1),
        ("Yuki Kurihara", "Karl Gonzalvo", 3, 0),
        ("Yuki Kurihara", "Yu Wing-lim", 3, 0),
        ("Yuki Kurihara", "Alexandr Pivovarov", 3, 0),
        ("Kang Dong-shin", "Karl Gonzalvo", 3, 2),
        ("Kang Dong-shin", "Yu Wing-lim", 3, 0),
        ("Kang Dong-shin", "Alexandr Pivovarov", 3, 0),
        ("Karl Gonzalvo", "Yu Wing-lim", 3, 2),
        ("Karl Gonzalvo", "Alexandr Pivovarov", 3, 0),
        ("Yu Wing-lim", "Alexandr Pivovarov", 3, 1),  # inferred from A4 vs A5
        # Group B
        ("Kuo Tzu-ang", "Tanarak Wongkitikun", 3, 0),
        ("Kuo Tzu-ang", "Paritosh", 3, 0),
        ("Kuo Tzu-ang", "Mun June Justin Koh", 3, 1),
        ("Kuo Tzu-ang", "Munkhzorig Ganbold", 3, 1),
        ("Tanarak Wongkitikun", "Paritosh", 3, 2),
        ("Tanarak Wongkitikun", "Mun June Justin Koh", 3, 1),  # inferred B2 > B4/B5
        ("Tanarak Wongkitikun", "Munkhzorig Ganbold", 3, 1),   # inferred B2 > B4/B5
        ("Paritosh", "Mun June Justin Koh", 3, 2),
        ("Paritosh", "Munkhzorig Ganbold", 3, 0),
    ]

    # Simple Newton-Raphson MAP estimation + Hessian covariance for Laplace posterior!
    theta = prior_mu.copy()
    for _ in range(40):
        grad = -(theta - prior_mu) / (prior_sd ** 2)
        hess = -np.diag(1.0 / (prior_sd ** 2))
        for a_nm, b_nm, wa, wb in obs:
            ia, ib = idx_map[a_nm], idx_map[b_nm]
            d = theta[ia] - theta[ib]
            p = 1.0 / (1.0 + math.exp(-d))
            n_g = wa + wb
            grad[ia] += wa - n_g * p
            grad[ib] -= wa - n_g * p
            w_h = n_g * p * (1.0 - p)
            hess[ia, ia] -= w_h
            hess[ib, ib] -= w_h
            hess[ia, ib] += w_h
            hess[ib, ia] += w_h
        step = np.linalg.solve(-hess, grad)
        theta += step
        if np.max(np.abs(step)) < 1e-8:
            break

    cov = np.linalg.inv(-hess)
    post_sd = np.sqrt(np.diag(cov))

    print("\n  Posterior Game-Level Bradley-Terry Strengths (MAP +/- SD):")
    for i, p in enumerate(players):
        print(f"    {p:22s}: {theta[i]:+.3f} +/- {post_sd[i]:.3f}")

    # Check implied single-game and Bo5 win probabilities at MAP:
    def bo_n_prob(p, need):
        # Probability of reaching `need` wins before opponent reaches `need` wins
        total = 0.0
        for k in range(need):
            total += math.comb(need - 1 + k, k) * (p ** need) * ((1.0 - p) ** k)
        return total

    print("\n  MAP Implied Matchups (1-game | Bo5[FT3] | Bo7[FT4]):")
    for a_nm, b_nm in [
        ("Yuki Kurihara", "Kang Dong-shin"),
        ("Yuki Kurihara", "Kuo Tzu-ang"),
        ("Kang Dong-shin", "Kuo Tzu-ang"),
        ("Yuki Kurihara", "Karl Gonzalvo"),
        ("Yuki Kurihara", "Tanarak Wongkitikun"),
        ("Karl Gonzalvo", "Tanarak Wongkitikun"),
        ("Kang Dong-shin", "Paritosh"),
    ]:
        ia, ib = idx_map[a_nm], idx_map[b_nm]
        p1 = 1.0 / (1.0 + math.exp(-(theta[ia] - theta[ib])))
        print(f"    {a_nm:20s} vs {b_nm:20s}: p1={p1:.3f} | Bo5={bo_n_prob(p1,3):.3f} | Bo7={bo_n_prob(p1,4):.3f}")

    # Monte Carlo over Laplace posterior + regime uncertainty (Bo5 vs Bo7 final, 11yo finals pressure, DNS tail):
    rng = np.random.default_rng(99618824)
    n_sims = 80000

    # Notice: Group A and Group B haven't played each other yet! So add an extra inter-group shift
    # uncertainty sd_inter ~ 0.35 on logit scale between Group A and Group B!
    regimes = [
        # (label, weight, need_qf, need_sf, need_fin, kurihara_nerve_p, kurihara_nerve_drop, kurihara_dns_p, sd_inter)
        ("R1: Base Bo5 All Rounds (QF/SF/Fin FT3; inter-group sd=0.35; 5% Finals nerve; 1.5% DNS)",
         0.50, 3, 3, 3, 0.05, 0.85, 0.015, 0.35),
        ("R2: Higher Upset Variance / Shorter KO / Stronger TPE (FT3; inter-group sd=0.50; 8% nerve; 2% DNS)",
         0.25, 3, 3, 3, 0.08, 1.05, 0.020, 0.50),
        ("R3: Longer SF/Final Format (QF FT3, SF/Fin FT4 or FT5; 4% nerve; 1.2% DNS)",
         0.25, 3, 4, 4, 0.04, 0.75, 0.012, 0.35),
    ]

    grpB_idx = [idx_map[p] for p in ["Kuo Tzu-ang", "Tanarak Wongkitikun", "Paritosh", "Mun June Justin Koh", "Munkhzorig Ganbold"]]

    def play_series(ia, ib, th, need):
        p1 = 1.0 / (1.0 + math.exp(-(th[ia] - th[ib])))
        return ia if rng.random() < bo_n_prob(p1, need) else ib

    blended = Counter()
    for label, w_reg, n_qf, n_sf, n_fin, nerve_p, nerve_drop, dns_p, sd_inter in regimes:
        champs = Counter()
        draws = rng.multivariate_normal(theta, cov, size=n_sims)
        inter_shifts = rng.normal(0.0, sd_inter, size=n_sims)
        nerves = rng.random(n_sims) < nerve_p
        dnss = rng.random(n_sims) < dns_p
        b4_is_koh = rng.random(n_sims) < 0.65  # Koh slightly likelier B4 than Ganbold

        i_kur = idx_map["Yuki Kurihara"]
        i_kan = idx_map["Kang Dong-shin"]
        i_kuo = idx_map["Kuo Tzu-ang"]
        i_gon = idx_map["Karl Gonzalvo"]
        i_won = idx_map["Tanarak Wongkitikun"]
        i_par = idx_map["Paritosh"]
        i_yu  = idx_map["Yu Wing-lim"]
        i_koh = idx_map["Mun June Justin Koh"]
        i_gan = idx_map["Munkhzorig Ganbold"]
        i_piv = idx_map["Alexandr Pivovarov"]

        for s in range(n_sims):
            th = draws[s].copy()
            for bi in grpB_idx:
                th[bi] += inter_shifts[s]
            if nerves[s]:
                th[i_kur] -= nerve_drop
            if dnss[s]:
                th[i_kur] -= 20.0

            b4, b5 = (i_koh, i_gan) if b4_is_koh[s] else (i_gan, i_koh)
            pi1 = play_series(b4, i_piv, th, n_qf)
            pi2 = play_series(i_yu, b5, th, n_qf)

            qf1 = play_series(i_kur, pi1, th, n_qf)
            qf2 = play_series(i_won, i_gon, th, n_qf)
            qf3 = play_series(i_kuo, pi2, th, n_qf)
            qf4 = play_series(i_kan, i_par, th, n_qf)

            sf1 = play_series(qf1, qf2, th, n_sf)
            sf2 = play_series(qf3, qf4, th, n_sf)
            gold = play_series(sf1, sf2, th, n_fin)
            champs[players[gold]] += 1

        print(f"\n  [{w_reg:.2f}] {label}")
        top5 = champs.most_common(5)
        print("        " + ", ".join(f"{k}={v/n_sims:.4f}" for k, v in top5))
        for k, cnt in champs.items():
            blended[k] += w_reg * (cnt / n_sims)

    print("\n  >>> BLENDED POST-GROUP-STAGE PROBABILITIES (qid=996188):")
    for k, v in blended.most_common():
        print(f"      {k:24s}: {v:.4f}")
    top5 = blended.most_common(5)
    print(f"      Top-5 sum = {sum(v for _, v in top5):.4f}, Outside = {1 - sum(v for _, v in top5):.4f}")


if __name__ == "__main__":
    model_686508_men100m_post_heats()
    model_996188_puyo_post_groups()
