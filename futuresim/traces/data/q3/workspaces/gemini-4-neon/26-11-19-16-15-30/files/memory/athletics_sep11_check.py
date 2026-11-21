import numpy as np

rng = np.random.default_rng(20260911)

# ------------------------------------------------------------------
# 1. WOMEN'S JAVELIN (qid=261941) — T+1d (Sat Sep 12 18:13 CEST)
# Check: (a) baseline Sep 09 model, (b) Yan DNS 0.005 + Katzberg-calibrated R2 foul (0.72*fr) + chilly var
# ------------------------------------------------------------------
def sim_jav(regimes, fr2_mult=0.55, n_trials=400_000):
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
        # R1
        v1 = active & (rng.random((n, k)) >= fr)
        t1 = rng.normal(day_mu + round_adj[None, :, 0], np.where(active, tsd, 1.0))
        best = np.maximum(best, np.where(v1, t1, 0.0))
        has_valid |= v1
        # R2
        fr2 = np.where(has_valid, fr, fr * fr2_mult)
        m2 = day_mu + round_adj[None, :, 1] - np.where(has_valid, 0.0, 0.8)
        v2 = active & (rng.random((n, k)) >= fr2)
        t2 = rng.normal(m2, np.where(active, tsd, 1.0))
        best = np.maximum(best, np.where(v2, t2, 0.0))
        has_valid |= v2
        # Cut to Top 6
        r2 = np.argsort(-(best + rng.uniform(0, 1e-6, (n, k))), axis=1)
        top6 = np.zeros((n, k), dtype=bool)
        top6[rows, r2[:, :6]] = True
        top6 &= active & (best > 0) # Double-foul = eliminated (or 0 mark loses to >=6 valid marks)
        # Wait: if >2 athletes double-foul, top6 still passes valid ones; best>0 check is exact if >=6 have valid marks
        # Actually use standard rank2[:, :6] &= active (since 0.0 loses to any valid mark)
        top6 = np.zeros((n, k), dtype=bool)
        top6[rows, r2[:, :6]] = True
        top6 &= active
        # R3
        v3 = top6 & (rng.random((n, k)) >= fr)
        t3 = rng.normal(day_mu + round_adj[None, :, 2], np.where(active, tsd, 1.0))
        best = np.maximum(best, np.where(v3, t3, 0.0))
        # Cut to Top 4
        r3 = np.argsort(-(best + rng.uniform(0, 1e-6, (n, k))), axis=1)
        top4 = np.zeros((n, k), dtype=bool)
        top4[rows, r3[:, :4]] = True
        top4 &= top6
        # R4
        v4 = top4 & (rng.random((n, k)) >= fr)
        t4 = rng.normal(day_mu + round_adj[None, :, 3], np.where(active, tsd, 1.0))
        best = np.maximum(best, np.where(v4, t4, 0.0))
        winners = np.argmax(best + rng.uniform(0, 1e-6, (n, k)), axis=1)
        probs = np.bincount(winners, minlength=k) / n
        blend += weight * probs
    return dict(zip(names, blend))

z = [0.0, 0.0, 0.0, 0.0]
wj_sep09 = [
    ("R1", 0.55, [
        ("Yan Ziyi", z,                [(0.020, None, 0, 0, 0), (0.110, 64.7, 1.85, 1.95, 0.22), (0.870, 66.9, 1.75, 1.95, 0.20)]),
        ("Haruka Kitaguchi", z,        [(0.020, None, 0, 0, 0), (0.980, 63.3, 1.80, 1.90, 0.18)]),
        ("Flor Denis Ruiz Hurtado", z, [(0.020, None, 0, 0, 0), (0.980, 63.0, 1.90, 1.90, 0.20)]),
        ("Adriana Vilagos", z,         [(0.020, None, 0, 0, 0), (0.980, 62.5, 1.85, 1.85, 0.18)]),
        ("Sigrid Borge", z,            [(0.025, None, 0, 0, 0), (0.780, 58.8, 1.90, 1.80, 0.21), (0.195, 62.6, 1.9, 1.8, 0.21)]),
        ("Mackenzie Little", z,        [(0.030, None, 0, 0, 0), (0.820, 60.0, 1.70, 1.80, 0.18), (0.150, 62.8, 1.8, 1.8, 0.18)]),
        ("Tori Moorby", z,             [(0.020, None, 0, 0, 0), (0.980, 58.9, 1.70, 1.70, 0.19)]),
        ("Anete Sietina", z,           [(0.020, None, 0, 0, 0), (0.980, 58.8, 1.70, 1.80, 0.19)]),
    ]),
    ("R2", 0.25, [
        ("Yan Ziyi", z,                [(0.035, None, 0, 0, 0), (0.265, 64.3, 1.90, 2.00, 0.25), (0.700, 66.2, 1.85, 1.95, 0.22)]),
        ("Haruka Kitaguchi", z,        [(0.020, None, 0, 0, 0), (0.980, 63.8, 1.80, 1.90, 0.18)]),
        ("Flor Denis Ruiz Hurtado", z, [(0.020, None, 0, 0, 0), (0.980, 63.4, 1.90, 1.90, 0.20)]),
        ("Adriana Vilagos", z,         [(0.020, None, 0, 0, 0), (0.980, 63.0, 1.85, 1.85, 0.18)]),
        ("Sigrid Borge", z,            [(0.025, None, 0, 0, 0), (0.720, 59.1, 1.90, 1.80, 0.21), (0.255, 63.0, 1.9, 1.8, 0.21)]),
        ("Mackenzie Little", z,        [(0.030, None, 0, 0, 0), (0.750, 60.2, 1.70, 1.80, 0.18), (0.220, 63.2, 1.8, 1.8, 0.18)]),
        ("Tori Moorby", z,             [(0.020, None, 0, 0, 0), (0.980, 59.1, 1.70, 1.70, 0.19)]),
        ("Anete Sietina", z,           [(0.020, None, 0, 0, 0), (0.980, 59.1, 1.70, 1.80, 0.19)]),
    ]),
    ("R3", 0.20, [
        ("Yan Ziyi", z,                [(0.015, None, 0, 0, 0), (0.045, 65.5, 1.70, 1.90, 0.18), (0.940, 67.6, 1.70, 1.90, 0.16)]),
        ("Haruka Kitaguchi", z,        [(0.020, None, 0, 0, 0), (0.980, 63.0, 1.80, 1.90, 0.18)]),
        ("Flor Denis Ruiz Hurtado", z, [(0.020, None, 0, 0, 0), (0.980, 62.8, 1.90, 1.90, 0.20)]),
        ("Adriana Vilagos", z,         [(0.020, None, 0, 0, 0), (0.980, 62.2, 1.80, 1.85, 0.18)]),
        ("Sigrid Borge", z,            [(0.025, None, 0, 0, 0), (0.830, 58.6, 1.90, 1.80, 0.21), (0.145, 62.2, 1.9, 1.8, 0.21)]),
        ("Mackenzie Little", z,        [(0.030, None, 0, 0, 0), (0.860, 59.8, 1.70, 1.80, 0.18), (0.110, 62.4, 1.8, 1.8, 0.18)]),
        ("Tori Moorby", z,             [(0.020, None, 0, 0, 0), (0.980, 58.7, 1.70, 1.70, 0.19)]),
        ("Anete Sietina", z,           [(0.020, None, 0, 0, 0), (0.980, 58.6, 1.70, 1.80, 0.19)]),
    ]),
]

# T+1d update: DNS drops from ~2-3.5% to ~0.5% for all confirmed entrants, AND fr2_mult=0.72 (Katzberg 2-throw cut lesson!)
wj_sep11 = []
for rname, w, aths in wj_sep09:
    new_aths = []
    for name, radj, states in aths:
        dns = states[0][0]
        new_dns = 0.005
        diff = dns - new_dns
        new_st = [(new_dns, None, 0, 0, 0)] + list(states[1:])
        # Add freed DNS mass proportionally to active states
        tot_act = sum(s[0] for s in states[1:])
        new_st = [(new_dns, None, 0, 0, 0)] + [(s[0] * (1.0 - new_dns) / tot_act, *s[1:]) for s in states[1:]]
        new_aths.append((name, radj, new_st))
    wj_sep11.append((rname, w, new_aths))

print("=== Q1 (261941) WOMEN'S JAVELIN: SEP 09 BASELINE ===")
r09 = sim_jav(wj_sep09, fr2_mult=0.55)
for k, v in sorted(r09.items(), key=lambda x: -x[1]):
    print(f"  {k:26s}: {v:.4f}")

print("=== Q1 (261941) WOMEN'S JAVELIN: SEP 11 (DNS=0.5%, fr2=0.72*fr) ===")
r11 = sim_jav(wj_sep11, fr2_mult=0.72)
for k, v in sorted(r11.items(), key=lambda x: -x[1]):
    print(f"  {k:26s}: {v:.4f}")

# ------------------------------------------------------------------
# 2. MEN'S JAVELIN (qid=30434) — Sensitivity to fr2_mult=0.72 & DNS=0.008
# ------------------------------------------------------------------
mj_sep10 = [
    ("R1", 0.55, [
        ("Rumesh Tharanga Pathirage", [0.0, 0.0, 0.0, 0.0], [(0.008, None, 0, 0, 0), (0.122, 85.2, 1.8, 2.2, 0.18), (0.870, 87.3, 1.8, 2.2, 0.17)]),
        ("Julian Weber", [-0.7, -0.2, 0.1, 0.4],            [(0.010, None, 0, 0, 0), (0.120, 84.0, 1.9, 2.2, 0.18), (0.870, 86.2, 1.8, 2.2, 0.17)]),
        ("Anderson Peters", [0.0, 0.0, 0.0, 0.0],           [(0.008, None, 0, 0, 0), (0.992, 83.6, 2.2, 2.4, 0.19)]),
        ("Dawid Wegner", [0.0, 0.0, 0.0, 0.0],              [(0.008, None, 0, 0, 0), (0.992, 82.6, 2.1, 2.3, 0.19)]),
        ("Keshorn Walcott", [0.0, 0.0, 0.0, 0.0],           [(0.008, None, 0, 0, 0), (0.992, 82.1, 2.1, 2.3, 0.19)]),
        ("Arshad Nadeem", [0.0, 0.0, 0.0, 0.0],             [(0.010, None, 0, 0, 0), (0.848, 78.8, 2.3, 2.4, 0.21), (0.142, 84.5, 2.5, 2.5, 0.19)]),
        ("Curtis Thompson", [0.0, 0.0, 0.0, 0.0],           [(0.050, None, 0, 0, 0), (0.760, 75.8, 2.6, 2.4, 0.23), (0.190, 82.8, 2.2, 2.3, 0.19)]),
        ("Julius Yego", [0.0, 0.0, 0.0, 0.0],               [(0.008, None, 0, 0, 0), (0.992, 78.6, 2.1, 2.3, 0.20)]),
    ]),
    ("R2", 0.225, [
        ("Rumesh Tharanga Pathirage", [0.0, 0.0, 0.0, 0.0], [(0.010, None, 0, 0, 0), (0.225, 85.0, 1.9, 2.2, 0.19), (0.765, 86.7, 1.9, 2.2, 0.18)]),
        ("Julian Weber", [-0.3, 0.0, 0.2, 0.4],             [(0.010, None, 0, 0, 0), (0.100, 84.5, 1.8, 2.2, 0.17), (0.890, 86.5, 1.8, 2.2, 0.17)]),
        ("Anderson Peters", [0.0, 0.0, 0.0, 0.0],           [(0.008, None, 0, 0, 0), (0.992, 84.0, 2.3, 2.4, 0.19)]),
        ("Dawid Wegner", [0.0, 0.0, 0.0, 0.0],              [(0.008, None, 0, 0, 0), (0.992, 83.0, 2.1, 2.3, 0.19)]),
        ("Keshorn Walcott", [0.0, 0.0, 0.0, 0.0],           [(0.008, None, 0, 0, 0), (0.992, 82.5, 2.1, 2.3, 0.19)]),
        ("Arshad Nadeem", [0.0, 0.0, 0.0, 0.0],             [(0.010, None, 0, 0, 0), (0.808, 79.2, 2.3, 2.4, 0.21), (0.182, 85.0, 2.5, 2.5, 0.19)]),
        ("Curtis Thompson", [0.0, 0.0, 0.0, 0.0],           [(0.050, None, 0, 0, 0), (0.740, 76.2, 2.6, 2.4, 0.23), (0.210, 83.2, 2.2, 2.3, 0.19)]),
        ("Julius Yego", [0.0, 0.0, 0.0, 0.0],               [(0.008, None, 0, 0, 0), (0.992, 79.0, 2.1, 2.3, 0.20)]),
    ]),
    ("R3", 0.225, [
        ("Rumesh Tharanga Pathirage", [0.2, 0.1, 0.0, 0.0], [(0.006, None, 0, 0, 0), (0.080, 85.8, 1.7, 2.2, 0.17), (0.914, 87.8, 1.8, 2.2, 0.17)]),
        ("Julian Weber", [-1.3, -0.6, 0.0, 0.3],            [(0.015, None, 0, 0, 0), (0.205, 83.5, 1.9, 2.2, 0.19), (0.780, 85.6, 1.9, 2.2, 0.18)]),
        ("Anderson Peters", [0.0, 0.0, 0.0, 0.0],           [(0.008, None, 0, 0, 0), (0.992, 83.2, 2.2, 2.4, 0.19)]),
        ("Dawid Wegner", [0.0, 0.0, 0.0, 0.0],              [(0.008, None, 0, 0, 0), (0.992, 82.1, 2.1, 2.3, 0.19)]),
        ("Keshorn Walcott", [0.0, 0.0, 0.0, 0.0],           [(0.008, None, 0, 0, 0), (0.992, 81.7, 2.1, 2.3, 0.19)]),
        ("Arshad Nadeem", [0.0, 0.0, 0.0, 0.0],             [(0.015, None, 0, 0, 0), (0.903, 78.4, 2.3, 2.4, 0.21), (0.082, 83.8, 2.5, 2.5, 0.19)]),
        ("Curtis Thompson", [0.0, 0.0, 0.0, 0.0],           [(0.060, None, 0, 0, 0), (0.810, 75.5, 2.6, 2.4, 0.23), (0.130, 82.3, 2.2, 2.3, 0.19)]),
        ("Julius Yego", [0.0, 0.0, 0.0, 0.0],               [(0.008, None, 0, 0, 0), (0.992, 78.3, 2.1, 2.3, 0.20)]),
    ]),
]

print("\n=== Q2 (30434) MEN'S JAVELIN: SEP 11 (DNS=0.8%, fr+0.01, fr2=0.72*fr) ===")
rmj = sim_jav(mj_sep10, fr2_mult=0.72)
for k, v in sorted(rmj.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")

# ------------------------------------------------------------------
# 3. MEN'S 200M (qid=653425) — Sensitivity to Bednarek headwind+cold revelation (NBC Sports Sep 11)
#    (19.62 Zurich headwind & 19.62 Brussels with cold -> true peak ~19.59-19.60, vs Sat 100m double & chilly Budapest!)
# ------------------------------------------------------------------
def sim_200m(regimes, n_trials=400_000):
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
                    cnt = int(mask.sum())
                    if cnt > 0:
                        active[mask, j] = True
                        day_mu[mask, j] = rng.normal(mu, msd, cnt)
                        race_sd[mask, j] = rsd
        dq_semi = np.where(is_dbl[None, :], 0.014, 0.008)
        ok_semi = active & (rng.random((n, k)) >= dq_semi)
        t_semi = np.where(ok_semi, day_mu + rng.normal(0.08, race_sd), 99.0)
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
        dq_fin = np.where(is_dbl[None, :], 0.014, 0.008)
        ok_fin = in_final & (rng.random((n, k)) >= dq_fin)
        t_fin = np.where(ok_fin, day_mu + rng.normal(0.0, race_sd), 99.0)
        winners = np.argmin(t_fin, axis=1)
        probs = np.bincount(winners, minlength=k) / n
        blend += weight * probs
    return dict(zip(names, blend))

# Modest +0.025s boost to Bednarek healthy form (19.63 -> 19.605 in R1, 19.68 -> 19.66 in R2, 19.58 -> 19.56 in R3)
# AND slightly lower pre-meet DNS (3.5% -> 2.5% in R1, since confirmed healthy in Budapest, keeping 100m injury risk)
regimes_200m_sep11 = [
    ("R1", 0.55, [
        ("Kenny Bednarek",         True,  [(0.025, None, 0, 0), (0.125, 19.81, 0.085, 0.070), (0.850, 19.605, 0.080, 0.068)]),
        ("Letsile Tebogo",         True,  [(0.030, None, 0, 0), (0.675, 19.89, 0.090, 0.070), (0.295, 19.66, 0.085, 0.070)]),
        ("Sinesipho Dambile",      False, [(0.015, None, 0, 0), (0.985, 19.83, 0.085, 0.070)]),
        ("Bryan Levell",           False, [(0.020, None, 0, 0), (0.830, 19.94, 0.090, 0.070), (0.150, 19.73, 0.085, 0.070)]),
        ("Andre De Grasse",        False, [(0.020, None, 0, 0), (0.840, 19.92, 0.085, 0.070), (0.140, 19.77, 0.085, 0.070)]),
        ("Makanakaishe Charamba",  False, [(0.015, None, 0, 0), (0.985, 19.90, 0.085, 0.070)]),
        ("Jose Figueroa",          False, [(0.015, None, 0, 0), (0.785, 20.12, 0.100, 0.075), (0.200, 19.84, 0.090, 0.070)]),
        ("Alexander Ogando",       False, [(0.015, None, 0, 0), (0.985, 19.95, 0.085, 0.070)]),
        ("Courtney Lindsey",       False, [(0.015, None, 0, 0), (0.885, 20.05, 0.090, 0.070), (0.100, 19.84, 0.085, 0.070)]),
        ("Yassine Hssine",         False, [(0.015, None, 0, 0), (0.985, 20.00, 0.090, 0.070)]),
        ("Brandon Hicklin",        False, [(0.015, None, 0, 0), (0.985, 20.02, 0.090, 0.070)]),
        ("Udodi Chudi Onwuzurike", False, [(0.015, None, 0, 0), (0.985, 20.06, 0.095, 0.070)]),
        ("Aaron Brown",            False, [(0.015, None, 0, 0), (0.985, 20.09, 0.085, 0.070)]),
        ("Timothe Mumenthaler",    False, [(0.015, None, 0, 0), (0.985, 20.13, 0.085, 0.070)]),
        ("Christopher Taylor",     False, [(0.015, None, 0, 0), (0.985, 20.15, 0.090, 0.070)]),
        ("Kyree King",             False, [(0.015, None, 0, 0), (0.985, 20.18, 0.090, 0.070)]),
    ]),
    ("R2", 0.25, [
        ("Kenny Bednarek",         True,  [(0.045, None, 0, 0), (0.265, 19.82, 0.085, 0.070), (0.690, 19.66, 0.080, 0.068)]),
        ("Letsile Tebogo",         True,  [(0.035, None, 0, 0), (0.485, 19.83, 0.090, 0.070), (0.480, 19.63, 0.085, 0.070)]),
        ("Sinesipho Dambile",      False, [(0.015, None, 0, 0), (0.985, 19.80, 0.085, 0.070)]),
        ("Bryan Levell",           False, [(0.020, None, 0, 0), (0.745, 19.91, 0.090, 0.070), (0.235, 19.71, 0.085, 0.070)]),
        ("Andre De Grasse",        False, [(0.020, None, 0, 0), (0.780, 19.90, 0.085, 0.070), (0.200, 19.75, 0.085, 0.070)]),
        ("Makanakaishe Charamba",  False, [(0.015, None, 0, 0), (0.985, 19.87, 0.085, 0.070)]),
        ("Jose Figueroa",          False, [(0.015, None, 0, 0), (0.725, 20.08, 0.100, 0.075), (0.260, 19.81, 0.090, 0.070)]),
        ("Alexander Ogando",       False, [(0.015, None, 0, 0), (0.985, 19.92, 0.085, 0.070)]),
        ("Courtney Lindsey",       False, [(0.015, None, 0, 0), (0.835, 20.02, 0.090, 0.070), (0.150, 19.81, 0.085, 0.070)]),
        ("Yassine Hssine",         False, [(0.015, None, 0, 0), (0.985, 19.97, 0.090, 0.070)]),
        ("Brandon Hicklin",        False, [(0.015, None, 0, 0), (0.985, 19.99, 0.090, 0.070)]),
        ("Udodi Chudi Onwuzurike", False, [(0.015, None, 0, 0), (0.985, 20.03, 0.095, 0.070)]),
        ("Aaron Brown",            False, [(0.015, None, 0, 0), (0.985, 20.06, 0.085, 0.070)]),
        ("Timothe Mumenthaler",    False, [(0.015, None, 0, 0), (0.985, 20.11, 0.085, 0.070)]),
        ("Christopher Taylor",     False, [(0.015, None, 0, 0), (0.985, 20.13, 0.090, 0.070)]),
        ("Kyree King",             False, [(0.015, None, 0, 0), (0.985, 20.16, 0.090, 0.070)]),
    ]),
    ("R3", 0.20, [
        ("Kenny Bednarek",         True,  [(0.020, None, 0, 0), (0.065, 19.75, 0.080, 0.068), (0.915, 19.56, 0.075, 0.065)]),
        ("Letsile Tebogo",         True,  [(0.035, None, 0, 0), (0.825, 19.94, 0.090, 0.070), (0.140, 19.72, 0.085, 0.070)]),
        ("Sinesipho Dambile",      False, [(0.015, None, 0, 0), (0.985, 19.85, 0.085, 0.070)]),
        ("Bryan Levell",           False, [(0.020, None, 0, 0), (0.885, 19.96, 0.090, 0.070), (0.095, 19.76, 0.085, 0.070)]),
        ("Andre De Grasse",        False, [(0.020, None, 0, 0), (0.895, 19.95, 0.085, 0.070), (0.085, 19.80, 0.085, 0.070)]),
        ("Makanakaishe Charamba",  False, [(0.015, None, 0, 0), (0.985, 19.92, 0.085, 0.070)]),
        ("Jose Figueroa",          False, [(0.015, None, 0, 0), (0.835, 20.15, 0.100, 0.075), (0.150, 19.88, 0.090, 0.070)]),
        ("Alexander Ogando",       False, [(0.015, None, 0, 0), (0.985, 19.97, 0.085, 0.070)]),
        ("Courtney Lindsey",       False, [(0.015, None, 0, 0), (0.905, 20.07, 0.090, 0.070), (0.080, 19.88, 0.085, 0.070)]),
        ("Yassine Hssine",         False, [(0.015, None, 0, 0), (0.985, 20.02, 0.090, 0.070)]),
        ("Brandon Hicklin",        False, [(0.015, None, 0, 0), (0.985, 20.04, 0.090, 0.070)]),
        ("Udodi Chudi Onwuzurike", False, [(0.015, None, 0, 0), (0.985, 20.08, 0.095, 0.070)]),
        ("Aaron Brown",            False, [(0.015, None, 0, 0), (0.985, 20.11, 0.085, 0.070)]),
        ("Timothe Mumenthaler",    False, [(0.015, None, 0, 0), (0.985, 20.15, 0.085, 0.070)]),
        ("Christopher Taylor",     False, [(0.015, None, 0, 0), (0.985, 20.17, 0.090, 0.070)]),
        ("Kyree King",             False, [(0.015, None, 0, 0), (0.985, 20.20, 0.090, 0.070)]),
    ]),
]

print("\n=== Q3 (653425) MEN'S 200M: SEP 11 (Bednarek healthy 19.605 / DNS=2.5%) ===")
r200 = sim_200m(regimes_200m_sep11)
for k, v in sorted(r200.items(), key=lambda x: -x[1])[:7]:
    print(f"  {k:26s}: {v:.4f}")
