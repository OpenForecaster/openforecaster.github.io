import numpy as np

rng = np.random.default_rng(20260907)

# ==============================================================================
# 1. Q2 (qid=261941): WOMEN'S JAVELIN — EXACT 8-WOMAN FIELD, 8-8-6-4 FORMAT
# ==============================================================================
def sim_javelin_8864_np(regimes, n_trials=400_000):
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

        # Round 1
        valid1 = active & (rng.random((n, k)) >= fr)
        t1 = np.where(valid1, rng.normal(day_mu, np.where(active, tsd, 1.0)), 0.0)
        best = np.maximum(best, t1)
        has_valid |= valid1

        # Round 2 (safer banker throw if fouled R1)
        fr2 = np.where(has_valid, fr, fr * 0.55)
        mu2 = np.where(has_valid, day_mu, day_mu - 0.8)
        valid2 = active & (rng.random((n, k)) >= fr2)
        t2 = np.where(valid2, rng.normal(mu2, np.where(active, tsd, 1.0)), 0.0)
        best = np.maximum(best, t2)
        has_valid |= valid2

        # Cut to Top 6 after Round 2 (break ties slightly randomly)
        rank2 = np.argsort(-(best + rng.uniform(0, 1e-6, (n, k))), axis=1)
        in_top6 = np.zeros((n, k), dtype=bool)
        rows = np.arange(n)[:, None]
        in_top6[rows, rank2[:, :6]] = True
        in_top6 &= active

        # Round 3 (Top 6 only)
        valid3 = in_top6 & (rng.random((n, k)) >= fr)
        t3 = np.where(valid3, rng.normal(day_mu, np.where(active, tsd, 1.0)), 0.0)
        best = np.maximum(best, t3)

        # Cut to Top 4 after Round 3
        rank3 = np.argsort(-(best + rng.uniform(0, 1e-6, (n, k))), axis=1)
        in_top4 = np.zeros((n, k), dtype=bool)
        in_top4[rows, rank3[:, :4]] = True
        in_top4 &= in_top6

        # Round 4 (Top 4 only)
        valid4 = in_top4 & (rng.random((n, k)) >= fr)
        t4 = np.where(valid4, rng.normal(day_mu, np.where(active, tsd, 1.0)), 0.0)
        best = np.maximum(best, t4)

        winners = np.argmax(best + rng.uniform(0, 1e-6, (n, k)), axis=1)
        probs = np.bincount(winners, minlength=k) / n
        top6_str = ", ".join(f"{names[i].split()[-1]}:{probs[i]:.3f}" for i in np.argsort(-probs)[:6])
        print(f"  [{rname[:58]:58s} w={weight:.2f}] {top6_str}")
        if rname.startswith("R1:"):
            for j in range(k):
                cond_valid = best[active[:, j] & (best[:, j] > 0), j].mean()
                cut2_rate = 1.0 - in_top6[active[:, j], j].mean()
                print(f"      {names[j]:26s}: E[best|valid]={cond_valid:.2f}m | cut@R2={cut2_rate:.3f}")
        blend += weight * probs
    return dict(zip(names, blend))

women_jav_refined = [
    ("R1: Base Calibrated (Yan 2% DNS, 68.5m; 8864 survival)", 0.55, [
        ("Yan Ziyi",                [(0.020, None, 0, 0, 0), (0.095, 64.8, 1.8, 1.9, 0.16), (0.885, 66.9, 1.75, 1.9, 0.15)]),
        ("Haruka Kitaguchi",        [(0.020, None, 0, 0, 0), (0.980, 63.3, 1.8, 1.9, 0.15)]),
        ("Flor Denis Ruiz Hurtado", [(0.020, None, 0, 0, 0), (0.980, 63.0, 1.9, 1.9, 0.16)]),
        ("Adriana Vilagos",         [(0.020, None, 0, 0, 0), (0.980, 62.1, 1.9, 1.8, 0.15)]),
        ("Sigrid Borge",            [(0.025, None, 0, 0, 0), (0.780, 58.8, 1.9, 1.8, 0.17), (0.195, 62.6, 1.9, 1.8, 0.17)]),
        ("Mackenzie Little",        [(0.030, None, 0, 0, 0), (0.820, 60.0, 1.7, 1.8, 0.15), (0.150, 62.8, 1.8, 1.8, 0.15)]),
        ("Tori Moorby",             [(0.020, None, 0, 0, 0), (0.980, 58.9, 1.7, 1.7, 0.16)]),
        ("Anete Sietina",           [(0.020, None, 0, 0, 0), (0.980, 58.8, 1.7, 1.8, 0.16)]),
    ]),
    ("R2: Yan Mild Fatigue/Early-Round Pressure + Rivals Peak", 0.25, [
        ("Yan Ziyi",                [(0.035, None, 0, 0, 0), (0.245, 64.4, 1.9, 1.9, 0.18), (0.720, 66.2, 1.85, 1.9, 0.16)]),
        ("Haruka Kitaguchi",        [(0.020, None, 0, 0, 0), (0.980, 63.8, 1.8, 1.9, 0.15)]),
        ("Flor Denis Ruiz Hurtado", [(0.020, None, 0, 0, 0), (0.980, 63.4, 1.9, 1.9, 0.16)]),
        ("Adriana Vilagos",         [(0.020, None, 0, 0, 0), (0.980, 62.7, 1.9, 1.8, 0.15)]),
        ("Sigrid Borge",            [(0.025, None, 0, 0, 0), (0.720, 59.1, 1.9, 1.8, 0.17), (0.255, 63.0, 1.9, 1.8, 0.17)]),
        ("Mackenzie Little",        [(0.030, None, 0, 0, 0), (0.750, 60.2, 1.7, 1.8, 0.15), (0.220, 63.2, 1.8, 1.8, 0.15)]),
        ("Tori Moorby",             [(0.020, None, 0, 0, 0), (0.980, 59.1, 1.7, 1.7, 0.16)]),
        ("Anete Sietina",           [(0.020, None, 0, 0, 0), (0.980, 59.1, 1.7, 1.8, 0.16)]),
    ]),
    ("R3: Yan Ziyi Dominant 69m+ Trajectory (5/5 DL)", 0.20, [
        ("Yan Ziyi",                [(0.015, None, 0, 0, 0), (0.045, 65.5, 1.7, 1.9, 0.15), (0.940, 67.5, 1.7, 1.9, 0.14)]),
        ("Haruka Kitaguchi",        [(0.020, None, 0, 0, 0), (0.980, 63.0, 1.8, 1.9, 0.15)]),
        ("Flor Denis Ruiz Hurtado", [(0.020, None, 0, 0, 0), (0.980, 62.8, 1.9, 1.9, 0.16)]),
        ("Adriana Vilagos",         [(0.020, None, 0, 0, 0), (0.980, 61.9, 1.8, 1.8, 0.15)]),
        ("Sigrid Borge",            [(0.025, None, 0, 0, 0), (0.830, 58.6, 1.9, 1.8, 0.17), (0.145, 62.2, 1.9, 1.8, 0.17)]),
        ("Mackenzie Little",        [(0.030, None, 0, 0, 0), (0.860, 59.8, 1.7, 1.8, 0.15), (0.110, 62.4, 1.8, 1.8, 0.15)]),
        ("Tori Moorby",             [(0.020, None, 0, 0, 0), (0.980, 58.7, 1.7, 1.7, 0.16)]),
        ("Anete Sietina",           [(0.020, None, 0, 0, 0), (0.980, 58.6, 1.7, 1.8, 0.16)]),
    ]),
]

print("=== Q2 (qid=261941) REFINED WOMEN'S JAVELIN (EXACT 8-WOMAN, 8-8-6-4) ===")
bwj = sim_javelin_8864_np(women_jav_refined)
for k_name, v in sorted(bwj.items(), key=lambda x: -x[1]):
    print(f"  {k_name:26s}: {v:.4f}")
top5_wj = sorted(bwj.items(), key=lambda x: -x[1])[:5]
print("Top-5 sum:", round(sum(v for _, v in top5_wj), 4))


# ==============================================================================
# 2. Q3 (qid=653425): MEN'S 200M — EXACT 16-MAN FIELD, 2-ROUND SAME-EVENING
# ==============================================================================
def sim_200m_2round_np(regimes, n_trials=400_000):
    names = [a[0] for a in regimes[0][2]]
    is_dbl = np.array([a[1] for a in regimes[0][2]], dtype=bool)
    k = len(names)
    blend = np.zeros(k)
    semi_a_idx = np.array([i for i in range(k) if (i % 4) in (0, 3)])
    semi_b_idx = np.array([i for i in range(k) if (i % 4) in (1, 2)])

    for rname, weight, athletes in regimes:
        n = n_trials
        day_mu = np.full((n, k), 99.0)
        race_sd = np.full((n, k), 0.07)
        active = np.zeros((n, k), dtype=bool)

        for j, (name, dbl, states) in enumerate(athletes):
            u = rng.random(n)
            cum = 0.0
            for p, mu, msd, rsd in states:
                mask = (u >= cum) & (u < cum + p)
                cum += p
                if mu is not None:
                    cnt = mask.sum()
                    if cnt > 0:
                        active[mask, j] = True
                        day_mu[mask, j] = rng.normal(mu, msd, cnt)
                        race_sd[mask, j] = rsd

        # Semifinals (DQ/injury 1.2% for doublers, 0.8% for specialists)
        dq_semi = np.where(is_dbl[None, :], 0.012, 0.008)
        ok_semi = active & (rng.random((n, k)) >= dq_semi)
        t_semi = np.where(ok_semi, day_mu + rng.normal(0.08, race_sd), 99.0)

        # Top 3 in Semi A + Top 3 in Semi B + 2 fastest remaining
        rows = np.arange(n)[:, None]
        ord_a = semi_a_idx[np.argsort(t_semi[:, semi_a_idx], axis=1)]
        ord_b = semi_b_idx[np.argsort(t_semi[:, semi_b_idx], axis=1)]
        in_final = np.zeros((n, k), dtype=bool)
        in_final[rows, ord_a[:, :3]] = True
        in_final[rows, ord_b[:, :3]] = True

        rem_times = np.where(in_final, 99.0, t_semi)
        ord_rem = np.argsort(rem_times, axis=1)
        in_final[rows, ord_rem[:, :2]] = True
        in_final &= ok_semi

        # Final (2h20m later: DQ/cramp 1.2% for doublers, 0.8% for specialists)
        dq_fin = np.where(is_dbl[None, :], 0.012, 0.008)
        ok_fin = in_final & (rng.random((n, k)) >= dq_fin)
        t_fin = np.where(ok_fin, day_mu + rng.normal(0.0, race_sd), 99.0)

        winners = np.argmin(t_fin, axis=1)
        probs = np.bincount(winners, minlength=k) / n
        top7_str = ", ".join(f"{names[i].split()[-1]}:{probs[i]:.3f}" for i in np.argsort(-probs)[:7])
        print(f"  [{rname[:58]:58s} w={weight:.2f}] {top7_str}")
        blend += weight * probs
    return dict(zip(names, blend))

regimes_200m_refined = [
    ("R1: Base Calibrated (Bednarek 19.63; Tebogo bimodal; 100m dbl)", 0.55, [
        ("Kenny Bednarek",         True,  [(0.035, None, 0, 0), (0.145, 19.83, 0.085, 0.070), (0.820, 19.63, 0.080, 0.068)]),
        ("Letsile Tebogo",         True,  [(0.035, None, 0, 0), (0.670, 19.89, 0.090, 0.070), (0.295, 19.66, 0.085, 0.070)]),
        ("Sinesipho Dambile",      False, [(0.020, None, 0, 0), (0.980, 19.83, 0.085, 0.070)]),
        ("Bryan Levell",           False, [(0.025, None, 0, 0), (0.825, 19.94, 0.090, 0.070), (0.150, 19.73, 0.085, 0.070)]),
        ("Andre De Grasse",        False, [(0.025, None, 0, 0), (0.835, 19.92, 0.085, 0.070), (0.140, 19.77, 0.085, 0.070)]),
        ("Makanakaishe Charamba",  False, [(0.020, None, 0, 0), (0.980, 19.90, 0.085, 0.070)]),
        ("Jose Figueroa",          False, [(0.020, None, 0, 0), (0.780, 20.12, 0.100, 0.075), (0.200, 19.84, 0.090, 0.070)]),
        ("Alexander Ogando",       False, [(0.020, None, 0, 0), (0.980, 19.95, 0.085, 0.070)]),
        ("Courtney Lindsey",       False, [(0.020, None, 0, 0), (0.880, 20.05, 0.090, 0.070), (0.100, 19.84, 0.085, 0.070)]),
        ("Yassine Hssine",         False, [(0.020, None, 0, 0), (0.980, 20.00, 0.090, 0.070)]),
        ("Brandon Hicklin",        False, [(0.020, None, 0, 0), (0.980, 20.02, 0.090, 0.070)]),
        ("Udodi Chudi Onwuzurike", False, [(0.020, None, 0, 0), (0.980, 20.06, 0.095, 0.070)]),
        ("Aaron Brown",            False, [(0.020, None, 0, 0), (0.980, 20.09, 0.085, 0.070)]),
        ("Timothe Mumenthaler",    False, [(0.020, None, 0, 0), (0.980, 20.13, 0.085, 0.070)]),
        ("Christopher Taylor",     False, [(0.020, None, 0, 0), (0.980, 20.15, 0.090, 0.070)]),
        ("Kyree King",             False, [(0.020, None, 0, 0), (0.980, 20.18, 0.090, 0.070)]),
    ]),
    ("R2: 100m-Double Wear on Bednarek + Tebogo/Fresh Specialists", 0.25, [
        ("Kenny Bednarek",         True,  [(0.055, None, 0, 0), (0.275, 19.83, 0.085, 0.070), (0.670, 19.68, 0.080, 0.068)]),
        ("Letsile Tebogo",         True,  [(0.040, None, 0, 0), (0.480, 19.83, 0.090, 0.070), (0.480, 19.63, 0.085, 0.070)]),
        ("Sinesipho Dambile",      False, [(0.020, None, 0, 0), (0.980, 19.80, 0.085, 0.070)]),
        ("Bryan Levell",           False, [(0.025, None, 0, 0), (0.740, 19.91, 0.090, 0.070), (0.235, 19.71, 0.085, 0.070)]),
        ("Andre De Grasse",        False, [(0.025, None, 0, 0), (0.775, 19.90, 0.085, 0.070), (0.200, 19.75, 0.085, 0.070)]),
        ("Makanakaishe Charamba",  False, [(0.020, None, 0, 0), (0.980, 19.87, 0.085, 0.070)]),
        ("Jose Figueroa",          False, [(0.020, None, 0, 0), (0.720, 20.08, 0.100, 0.075), (0.260, 19.81, 0.090, 0.070)]),
        ("Alexander Ogando",       False, [(0.020, None, 0, 0), (0.980, 19.92, 0.085, 0.070)]),
        ("Courtney Lindsey",       False, [(0.020, None, 0, 0), (0.830, 20.02, 0.090, 0.070), (0.150, 19.81, 0.085, 0.070)]),
        ("Yassine Hssine",         False, [(0.020, None, 0, 0), (0.980, 19.97, 0.090, 0.070)]),
        ("Brandon Hicklin",        False, [(0.020, None, 0, 0), (0.980, 19.99, 0.090, 0.070)]),
        ("Udodi Chudi Onwuzurike", False, [(0.020, None, 0, 0), (0.980, 20.03, 0.095, 0.070)]),
        ("Aaron Brown",            False, [(0.020, None, 0, 0), (0.980, 20.06, 0.085, 0.070)]),
        ("Timothe Mumenthaler",    False, [(0.020, None, 0, 0), (0.980, 20.11, 0.085, 0.070)]),
        ("Christopher Taylor",     False, [(0.020, None, 0, 0), (0.980, 20.13, 0.090, 0.070)]),
        ("Kyree King",             False, [(0.020, None, 0, 0), (0.980, 20.16, 0.090, 0.070)]),
    ]),
    ("R3: Bednarek PB Run (19.55-19.60) & Tebogo Flat in 2026", 0.20, [
        ("Kenny Bednarek",         True,  [(0.025, None, 0, 0), (0.075, 19.77, 0.080, 0.068), (0.900, 19.58, 0.075, 0.065)]),
        ("Letsile Tebogo",         True,  [(0.040, None, 0, 0), (0.820, 19.94, 0.090, 0.070), (0.140, 19.72, 0.085, 0.070)]),
        ("Sinesipho Dambile",      False, [(0.020, None, 0, 0), (0.980, 19.85, 0.085, 0.070)]),
        ("Bryan Levell",           False, [(0.025, None, 0, 0), (0.880, 19.96, 0.090, 0.070), (0.095, 19.76, 0.085, 0.070)]),
        ("Andre De Grasse",        False, [(0.025, None, 0, 0), (0.890, 19.95, 0.085, 0.070), (0.085, 19.80, 0.085, 0.070)]),
        ("Makanakaishe Charamba",  False, [(0.020, None, 0, 0), (0.980, 19.92, 0.085, 0.070)]),
        ("Jose Figueroa",          False, [(0.020, None, 0, 0), (0.830, 20.15, 0.100, 0.075), (0.150, 19.88, 0.090, 0.070)]),
        ("Alexander Ogando",       False, [(0.020, None, 0, 0), (0.980, 19.97, 0.085, 0.070)]),
        ("Courtney Lindsey",       False, [(0.020, None, 0, 0), (0.900, 20.07, 0.090, 0.070), (0.080, 19.88, 0.085, 0.070)]),
        ("Yassine Hssine",         False, [(0.020, None, 0, 0), (0.980, 20.02, 0.090, 0.070)]),
        ("Brandon Hicklin",        False, [(0.020, None, 0, 0), (0.980, 20.04, 0.090, 0.070)]),
        ("Udodi Chudi Onwuzurike", False, [(0.020, None, 0, 0), (0.980, 20.08, 0.095, 0.070)]),
        ("Aaron Brown",            False, [(0.020, None, 0, 0), (0.980, 20.11, 0.085, 0.070)]),
        ("Timothe Mumenthaler",    False, [(0.020, None, 0, 0), (0.980, 20.15, 0.085, 0.070)]),
        ("Christopher Taylor",     False, [(0.020, None, 0, 0), (0.980, 20.17, 0.090, 0.070)]),
        ("Kyree King",             False, [(0.020, None, 0, 0), (0.980, 20.20, 0.090, 0.070)]),
    ]),
]

print("\n=== Q3 (qid=653425) REFINED MEN'S 200M (EXACT 16-MAN, 2-ROUND SAME-EVENING) ===")
b200 = sim_200m_2round_np(regimes_200m_refined)
for k_name, v in sorted(b200.items(), key=lambda x: -x[1]):
    print(f"  {k_name:26s}: {v:.4f}")
top5_200 = sorted(b200.items(), key=lambda x: -x[1])[:5]
print("Top-5:", [(k, round(v, 4)) for k, v in top5_200], "sum =", round(sum(v for _, v in top5_200), 4))
