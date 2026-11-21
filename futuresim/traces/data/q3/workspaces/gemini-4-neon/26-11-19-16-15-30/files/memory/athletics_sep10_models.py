import numpy as np

rng = np.random.default_rng(202609102)

# ==============================================================================
# REFINED CALIBRATION CHECK — THURSDAY SEPT 10, 2026
# ==============================================================================

def sim_javelin_8864(regimes, n_trials=400_000):
    names = [a[0] for a in regimes[0][2]]
    k = len(names)
    blend = np.zeros(k)

    for rname, weight, athletes in regimes:
        n = n_trials
        day_mu = np.full((n, k), -999.0)
        tsd = np.zeros((n, k))
        fr = np.zeros((n, k))
        round_adj = np.zeros((k, 4))
        active = np.zeros((n, k), dtype=bool)

        for j, (name, r_adj, states) in enumerate(athletes):
            round_adj[j] = r_adj
            u = rng.random(n)
            cum = 0.0
            for p, mu, dsd_v, tsd_v, fr_v in states:
                mask = (u >= cum) & (u < cum + p)
                cum += p
                if mu is not None:
                    cnt = int(mask.sum())
                    if cnt > 0:
                        active[mask, j] = True
                        day_mu[mask, j] = rng.normal(mu, dsd_v, cnt)
                        tsd[mask, j] = tsd_v
                        fr[mask, j] = fr_v

        best = np.zeros((n, k))
        has_valid = np.zeros((n, k), dtype=bool)
        rows = np.arange(n)[:, None]

        # R1 (all 8)
        valid1 = active & (rng.random((n, k)) >= fr)
        t1 = rng.normal(day_mu + round_adj[None, :, 0], np.where(active, tsd, 1.0))
        best = np.maximum(best, np.where(valid1, t1, 0.0))
        has_valid |= valid1

        # R2 (all 8; safer banker if fouled R1)
        fr2 = np.where(has_valid, fr, fr * 0.55)
        m2 = day_mu + round_adj[None, :, 1] - np.where(has_valid, 0.0, 1.0)
        valid2 = active & (rng.random((n, k)) >= fr2)
        t2 = rng.normal(m2, np.where(active, tsd, 1.0))
        best = np.maximum(best, np.where(valid2, t2, 0.0))
        has_valid |= valid2

        # Top 6 -> R3
        rank2 = np.argsort(-(best + rng.uniform(0, 1e-6, (n, k))), axis=1)
        in_top6 = np.zeros((n, k), dtype=bool)
        in_top6[rows, rank2[:, :6]] = True
        in_top6 &= active

        valid3 = in_top6 & (rng.random((n, k)) >= fr)
        t3 = rng.normal(day_mu + round_adj[None, :, 2], np.where(active, tsd, 1.0))
        best = np.maximum(best, np.where(valid3, t3, 0.0))

        # Top 4 -> R4
        rank3 = np.argsort(-(best + rng.uniform(0, 1e-6, (n, k))), axis=1)
        in_top4 = np.zeros((n, k), dtype=bool)
        in_top4[rows, rank3[:, :4]] = True
        in_top4 &= in_top6

        valid4 = in_top4 & (rng.random((n, k)) >= fr)
        t4 = rng.normal(day_mu + round_adj[None, :, 3], np.where(active, tsd, 1.0))
        best = np.maximum(best, np.where(valid4, t4, 0.0))

        winners = np.argmax(best + rng.uniform(0, 1e-6, (n, k)), axis=1)
        probs = np.bincount(winners, minlength=k) / n
        top6_str = ", ".join(
            f"{names[idx].split()[-1]}:{probs[idx]:.3f}"
            for idx in np.argsort(-probs)[:6]
        )
        p_valid = best[(active[:, 0]) & (best[:, 0] > 0), 0]
        w_valid = best[(active[:, 1]) & (best[:, 1] > 0), 1]
        print(f"  [{rname[:52]:52s} w={weight:.2f}] {top6_str}")
        print(f"     -> valid median best: Pathirage={np.median(p_valid):.2f}m (P>=88:{(p_valid>=88).mean():.2f}), Weber={np.median(w_valid):.2f}m (P>=88:{(w_valid>=88).mean():.2f})")
        blend += weight * probs

    return dict(zip(names, blend))


men_jav_ref = [
    # R1 (55%): Base Calibrated 8-8-6-4
    # Pathirage: 12-1 in 2026, 8/12 meets >=88m (last 5 straight), 92.62m & 92.07m ceiling
    # Weber: Healthy (87.04m Luzern, 90.40m Birmingham R6, 89.54m ISTAF Berlin R6), modest slow-start in 4-round format
    # Peters: 86.93m SB, beat Pathirage in Rabat, 83.70m Brussels
    # Wegner: 87.47m PB Brussels (peaking)
    # Walcott: Reigning 2025 World champ, 83.99m SB Brussels (3rd, beat Peters)
    # Nadeem: Travelled to Budapest Sep 9, BUT 78.63m SB, 9th CWG, manager says long-term LA28 rebuild
    ("R1: Base 8-8-6-4 (Pathirage peak vs healthy Weber)", 0.55, [
        ("Rumesh Tharanga Pathirage", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.12, 85.2, 1.8, 2.2, 0.17), (0.86, 87.3, 1.8, 2.2, 0.16)]),
        ("Julian Weber", [-0.7, -0.2, 0.1, 0.4],
         [(0.03, None, 0, 0, 0), (0.12, 84.0, 1.9, 2.2, 0.17), (0.85, 86.2, 1.8, 2.2, 0.16)]),
        ("Anderson Peters", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 83.6, 2.2, 2.4, 0.18)]),
        ("Dawid Wegner", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 82.6, 2.1, 2.3, 0.18)]),
        ("Keshorn Walcott", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 82.1, 2.1, 2.3, 0.18)]),
        ("Arshad Nadeem", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.84, 78.8, 2.3, 2.4, 0.20), (0.14, 84.5, 2.5, 2.5, 0.18)]),
        ("Curtis Thompson", [0.0, 0.0, 0.0, 0.0],
         [(0.10, None, 0, 0, 0), (0.72, 75.8, 2.6, 2.4, 0.22), (0.18, 82.8, 2.2, 2.3, 0.18)]),
        ("Julius Yego", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 78.6, 2.1, 2.3, 0.19)]),
    ]),
    # R2 (22.5%): Weber Fresh/Sharp (ISTAF strategy pays off) vs Pathirage 13-meet slight fatigue -> coin flip top-2
    ("R2: Weber Fresh/Even vs Pathirage Workload Dip", 0.225, [
        ("Rumesh Tharanga Pathirage", [0.0, 0.0, 0.0, 0.0],
         [(0.03, None, 0, 0, 0), (0.22, 85.0, 1.9, 2.2, 0.18), (0.75, 86.7, 1.9, 2.2, 0.17)]),
        ("Julian Weber", [-0.3, 0.0, 0.2, 0.4],
         [(0.02, None, 0, 0, 0), (0.10, 84.5, 1.8, 2.2, 0.16), (0.88, 86.5, 1.8, 2.2, 0.16)]),
        ("Anderson Peters", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 84.0, 2.3, 2.4, 0.18)]),
        ("Dawid Wegner", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 83.0, 2.1, 2.3, 0.18)]),
        ("Keshorn Walcott", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 82.5, 2.1, 2.3, 0.18)]),
        ("Arshad Nadeem", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.80, 79.2, 2.3, 2.4, 0.20), (0.18, 85.0, 2.5, 2.5, 0.18)]),
        ("Curtis Thompson", [0.0, 0.0, 0.0, 0.0],
         [(0.10, None, 0, 0, 0), (0.70, 76.2, 2.6, 2.4, 0.22), (0.20, 83.2, 2.2, 2.3, 0.18)]),
        ("Julius Yego", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 79.0, 2.1, 2.3, 0.19)]),
    ]),
    # R3 (22.5%): Pathirage 90m+ Early-Round Dominant + Weber Hurt by No R5-R6
    ("R3: Pathirage Early 90m+ + Weber Hurt By 4-Rd Cut", 0.225, [
        ("Rumesh Tharanga Pathirage", [0.2, 0.1, 0.0, 0.0],
         [(0.01, None, 0, 0, 0), (0.08, 85.8, 1.7, 2.2, 0.16), (0.91, 87.8, 1.8, 2.2, 0.16)]),
        ("Julian Weber", [-1.3, -0.6, 0.0, 0.3],
         [(0.04, None, 0, 0, 0), (0.20, 83.5, 1.9, 2.2, 0.18), (0.76, 85.6, 1.9, 2.2, 0.17)]),
        ("Anderson Peters", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 83.2, 2.2, 2.4, 0.18)]),
        ("Dawid Wegner", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 82.1, 2.1, 2.3, 0.18)]),
        ("Keshorn Walcott", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 81.7, 2.1, 2.3, 0.18)]),
        ("Arshad Nadeem", [0.0, 0.0, 0.0, 0.0],
         [(0.03, None, 0, 0, 0), (0.89, 78.4, 2.3, 2.4, 0.20), (0.08, 83.8, 2.5, 2.5, 0.18)]),
        ("Curtis Thompson", [0.0, 0.0, 0.0, 0.0],
         [(0.12, None, 0, 0, 0), (0.76, 75.5, 2.6, 2.4, 0.22), (0.12, 82.3, 2.2, 2.3, 0.18)]),
        ("Julius Yego", [0.0, 0.0, 0.0, 0.0],
         [(0.02, None, 0, 0, 0), (0.98, 78.3, 2.1, 2.3, 0.19)]),
    ]),
]

print("=== REFINED Q3 (qid=30434) MEN'S JAVELIN (8-8-6-4) ===")
bmj = sim_javelin_8864(men_jav_ref)
for k, v in sorted(bmj.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")
top5_mj = sorted(bmj.items(), key=lambda x: -x[1])[:5]
print("Top-5:", [(k, round(v, 4)) for k, v in top5_mj], "sum =", round(sum(v for _, v in top5_mj), 4))


# ==============================================================================
# REFINED Q1 (qid=936021) MEN'S 5,000m — FIXING INGEBRIGTSEN TACTICAL 5K PEDIGREE
# ==============================================================================
def sim_5000m_vec(regimes, n_trials=400_000):
    names = [a[0] for a in regimes[0][3]]
    k = len(names)
    blend = np.zeros(k)

    for rname, weight, pace_probs, athletes in regimes:
        n = n_trials
        up = rng.random(n)
        pace = np.where(up < pace_probs[0], 0, np.where(up < pace_probs[0] + pace_probs[1], 1, 2))
        scores = np.full((n, k), -1e9)
        for j, (name, p_start, states) in enumerate(athletes):
            starts = rng.random(n) < p_start
            u = rng.random(n)
            cum = 0.0
            for p_st, mus, sd in states:
                mask = starts & (u >= cum) & (u < cum + p_st)
                cum += p_st
                cnt = int(mask.sum())
                if cnt > 0:
                    mu_arr = np.array(mus)[pace[mask]]
                    scores[mask, j] = rng.normal(mu_arr, sd)
        winners = np.argmax(scores, axis=1)
        probs = np.bincount(winners, minlength=k) / n
        top7_str = ", ".join(
            f"{names[idx].split()[-1]}:{probs[idx]:.3f}"
            for idx in np.argsort(-probs)[:7]
        )
        print(f"  [{rname[:52]:52s} w={weight:.2f}] {top7_str}")
        blend += weight * probs
    return dict(zip(names, blend))

regimes_5k_ref = [
    # R1 (55%): Base T+1d — Pacer-less Championship (52% tactical, 35% honest wind-up, 13% fast)
    # Ingebrigtsen: 4x major tactical 5k champ (22, 23 Budapest, 24 Paris, 26 Euros) & beat Hocker in Brussels 1500m!
    # Hocker: Reigning 2025 World 5k champ & Olympic 1500m champ, lethal 400m kick, but 0 5ks in 2026 & 7th Brussels 1500m
    ("R1: Base T+1d (52% tact / 35% honest / 13% fast)", 0.55, (0.52, 0.35, 0.13), [
        ("Jakob Ingebrigtsen", 0.985, [(0.18, (1.40, 1.70, 1.55), 0.95), (0.82, (2.15, 2.38, 2.12), 0.95)]),
        ("Cole Hocker",        0.985, [(0.22, (1.30, 0.95, 0.55), 0.95), (0.78, (2.30, 1.88, 1.32), 0.95)]),
        ("Addisu Yihune",      0.985, [(1.00, (1.15, 1.50, 1.75), 0.95)]),
        ("Parker Wolfe",       0.985, [(1.00, (1.30, 1.28, 1.15), 0.95)]),
        ("Biniam Mehary",      0.985, [(1.00, (0.95, 1.35, 1.60), 0.98)]),
        ("Graham Blanks",      0.985, [(1.00, (1.05, 1.20, 1.25), 0.95)]),
        ("Nico Young",         0.985, [(1.00, (1.00, 1.15, 1.25), 0.95)]),
        ("Egide Ntakarutimana",0.985, [(1.00, (0.90, 1.20, 1.45), 0.95)]),
        ("Cornelius Kemboi",   0.985, [(1.00, (0.85, 1.15, 1.35), 0.95)]),
        ("Grant Fisher",       0.980, [(0.70, (0.30, 0.25, 0.10), 0.95), (0.30, (1.10, 1.15, 1.05), 0.95)]),
        ("Ky Robinson",        0.985, [(1.00, (0.85, 0.95, 0.95), 0.95)]),
        ("Jacob Krop",         0.985, [(1.00, (0.70, 0.85, 0.95), 0.95)]),
    ]),
    # R2 (25%): Pure Slow Sit-and-Kick (70% tactical, 25% honest, 5% fast)
    ("R2: Pure Tactical Kick (5 US + Jakob control)", 0.25, (0.70, 0.25, 0.05), [
        ("Jakob Ingebrigtsen", 0.985, [(0.15, (1.45, 1.75, 1.60), 0.95), (0.85, (2.20, 2.42, 2.15), 0.95)]),
        ("Cole Hocker",        0.985, [(0.18, (1.35, 1.00, 0.60), 0.95), (0.82, (2.40, 1.92, 1.38), 0.95)]),
        ("Addisu Yihune",      0.985, [(1.00, (1.12, 1.45, 1.65), 0.95)]),
        ("Parker Wolfe",       0.985, [(1.00, (1.38, 1.32, 1.15), 0.95)]),
        ("Biniam Mehary",      0.985, [(1.00, (0.85, 1.20, 1.45), 0.98)]),
        ("Graham Blanks",      0.985, [(1.00, (0.98, 1.12, 1.15), 0.95)]),
        ("Nico Young",         0.985, [(1.00, (0.92, 1.07, 1.15), 0.95)]),
        ("Egide Ntakarutimana",0.985, [(1.00, (0.80, 1.05, 1.30), 0.95)]),
        ("Cornelius Kemboi",   0.985, [(1.00, (0.75, 1.00, 1.20), 0.95)]),
        ("Grant Fisher",       0.980, [(0.75, (0.25, 0.20, 0.05), 0.95), (0.25, (1.05, 1.10, 1.00), 0.95)]),
        ("Ky Robinson",        0.985, [(1.00, (0.85, 0.90, 0.90), 0.95)]),
        ("Jacob Krop",         0.985, [(1.00, (0.65, 0.80, 0.85), 0.95)]),
    ]),
    # R3 (20%): Honest/Fast Ethiopian Grind + Top-2 Rust/Untested 5k
    ("R3: Honest/Fast Grind + Top-2 Vulnerable", 0.20, (0.25, 0.45, 0.30), [
        ("Jakob Ingebrigtsen", 0.980, [(0.32, (1.25, 1.50, 1.38), 0.95), (0.68, (1.88, 2.15, 1.95), 0.95)]),
        ("Cole Hocker",        0.975, [(0.35, (1.10, 0.80, 0.40), 0.95), (0.65, (2.10, 1.65, 1.15), 0.95)]),
        ("Addisu Yihune",      0.985, [(1.00, (1.25, 1.65, 1.95), 0.95)]),
        ("Parker Wolfe",       0.985, [(1.00, (1.25, 1.32, 1.25), 0.95)]),
        ("Biniam Mehary",      0.985, [(1.00, (1.10, 1.55, 1.85), 0.98)]),
        ("Graham Blanks",      0.985, [(1.00, (1.15, 1.35, 1.45), 0.95)]),
        ("Nico Young",         0.985, [(1.00, (1.10, 1.30, 1.45), 0.95)]),
        ("Egide Ntakarutimana",0.985, [(1.00, (1.05, 1.40, 1.70), 0.95)]),
        ("Cornelius Kemboi",   0.985, [(1.00, (1.00, 1.35, 1.60), 0.95)]),
        ("Grant Fisher",       0.980, [(0.70, (0.30, 0.25, 0.10), 0.95), (0.30, (1.15, 1.20, 1.15), 0.95)]),
        ("Ky Robinson",        0.985, [(1.00, (0.90, 1.05, 1.10), 0.95)]),
        ("Jacob Krop",         0.985, [(1.00, (0.80, 1.00, 1.15), 0.95)]),
    ]),
]

print("\n=== REFINED Q1 (qid=936021) MEN'S 5,000m (T+1d) ===")
b5k = sim_5000m_vec(regimes_5k_ref)
for k, v in sorted(b5k.items(), key=lambda x: -x[1]):
    print(f"  {k:24s}: {v:.4f}")
top5_5k = sorted(b5k.items(), key=lambda x: -x[1])[:5]
print("Top-5:", [(k, round(v, 4)) for k, v in top5_5k], "sum =", round(sum(v for _, v in top5_5k), 4))
