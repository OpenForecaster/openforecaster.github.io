import numpy as np

rng = np.random.default_rng(20260912)

# ==============================================================================
# 1. MEN'S JAVELIN (qid=30434) — Sat Sep 12 (T+1d to Sun Sep 13 18:13 CEST)
#    Check sensitivity to:
#    - Warm fast Budapest conditions confirmed Sat Sep 12 (67F, Kitaguchi 68.92m / Yan 68.05m!)
#    - T+1d DNS decay (0.5% for confirmed entrants, 2% Thompson)
#    - Slightly wider championship-day variance (dsd +0.15m, tsd +0.15m) vs slightly lower warm foul rate
# ==============================================================================
def sim_jav(regimes, fr2_mult=0.65, n_trials=400_000):
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
        # Top 6
        r2 = np.argsort(-(best + rng.uniform(0, 1e-6, (n, k))), axis=1)
        top6 = np.zeros((n, k), dtype=bool)
        top6[rows, r2[:, :6]] = True
        top6 &= active
        # R3
        v3 = top6 & (rng.random((n, k)) >= fr)
        t3 = rng.normal(day_mu + round_adj[None, :, 2], np.where(active, tsd, 1.0))
        best = np.maximum(best, np.where(v3, t3, 0.0))
        # Top 4
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

mj_sep12 = [
    ("R1", 0.55, [
        ("Rumesh Tharanga Pathirage", [0.0, 0.0, 0.0, 0.0], [(0.005, None, 0, 0, 0), (0.125, 85.2, 1.95, 2.35, 0.17), (0.870, 87.3, 1.95, 2.35, 0.16)]),
        ("Julian Weber", [-0.7, -0.2, 0.1, 0.4],            [(0.006, None, 0, 0, 0), (0.124, 84.0, 2.05, 2.35, 0.17), (0.870, 86.2, 1.95, 2.35, 0.16)]),
        ("Anderson Peters", [0.0, 0.0, 0.0, 0.0],           [(0.005, None, 0, 0, 0), (0.995, 83.6, 2.35, 2.55, 0.18)]),
        ("Dawid Wegner", [0.0, 0.0, 0.0, 0.0],              [(0.005, None, 0, 0, 0), (0.995, 82.6, 2.25, 2.45, 0.18)]),
        ("Keshorn Walcott", [0.0, 0.0, 0.0, 0.0],           [(0.005, None, 0, 0, 0), (0.995, 82.1, 2.25, 2.45, 0.18)]),
        ("Arshad Nadeem", [0.0, 0.0, 0.0, 0.0],             [(0.006, None, 0, 0, 0), (0.844, 78.8, 2.45, 2.55, 0.20), (0.150, 84.5, 2.65, 2.65, 0.18)]),
        ("Curtis Thompson", [0.0, 0.0, 0.0, 0.0],           [(0.020, None, 0, 0, 0), (0.780, 75.8, 2.75, 2.55, 0.22), (0.200, 82.8, 2.35, 2.45, 0.18)]),
        ("Julius Yego", [0.0, 0.0, 0.0, 0.0],               [(0.005, None, 0, 0, 0), (0.995, 78.6, 2.25, 2.45, 0.19)]),
    ]),
    ("R2", 0.225, [
        ("Rumesh Tharanga Pathirage", [0.0, 0.0, 0.0, 0.0], [(0.006, None, 0, 0, 0), (0.224, 85.0, 2.05, 2.35, 0.18), (0.770, 86.7, 2.05, 2.35, 0.17)]),
        ("Julian Weber", [-0.3, 0.0, 0.2, 0.4],             [(0.006, None, 0, 0, 0), (0.104, 84.5, 1.95, 2.35, 0.16), (0.890, 86.5, 1.95, 2.35, 0.16)]),
        ("Anderson Peters", [0.0, 0.0, 0.0, 0.0],           [(0.005, None, 0, 0, 0), (0.995, 84.0, 2.45, 2.55, 0.18)]),
        ("Dawid Wegner", [0.0, 0.0, 0.0, 0.0],              [(0.005, None, 0, 0, 0), (0.995, 83.0, 2.25, 2.45, 0.18)]),
        ("Keshorn Walcott", [0.0, 0.0, 0.0, 0.0],           [(0.005, None, 0, 0, 0), (0.995, 82.5, 2.25, 2.45, 0.18)]),
        ("Arshad Nadeem", [0.0, 0.0, 0.0, 0.0],             [(0.006, None, 0, 0, 0), (0.804, 79.2, 2.45, 2.55, 0.20), (0.190, 85.0, 2.65, 2.65, 0.18)]),
        ("Curtis Thompson", [0.0, 0.0, 0.0, 0.0],           [(0.020, None, 0, 0, 0), (0.760, 76.2, 2.75, 2.55, 0.22), (0.220, 83.2, 2.35, 2.45, 0.18)]),
        ("Julius Yego", [0.0, 0.0, 0.0, 0.0],               [(0.005, None, 0, 0, 0), (0.995, 79.0, 2.25, 2.45, 0.19)]),
    ]),
    ("R3", 0.225, [
        ("Rumesh Tharanga Pathirage", [0.2, 0.1, 0.0, 0.0], [(0.005, None, 0, 0, 0), (0.080, 85.8, 1.85, 2.35, 0.16), (0.915, 87.8, 1.95, 2.35, 0.16)]),
        ("Julian Weber", [-1.3, -0.6, 0.0, 0.3],            [(0.008, None, 0, 0, 0), (0.202, 83.5, 2.05, 2.35, 0.18), (0.790, 85.6, 2.05, 2.35, 0.17)]),
        ("Anderson Peters", [0.0, 0.0, 0.0, 0.0],           [(0.005, None, 0, 0, 0), (0.995, 83.2, 2.35, 2.55, 0.18)]),
        ("Dawid Wegner", [0.0, 0.0, 0.0, 0.0],              [(0.005, None, 0, 0, 0), (0.995, 82.1, 2.25, 2.45, 0.18)]),
        ("Keshorn Walcott", [0.0, 0.0, 0.0, 0.0],           [(0.005, None, 0, 0, 0), (0.995, 81.7, 2.25, 2.45, 0.18)]),
        ("Arshad Nadeem", [0.0, 0.0, 0.0, 0.0],             [(0.008, None, 0, 0, 0), (0.902, 78.4, 2.45, 2.55, 0.20), (0.090, 83.8, 2.65, 2.65, 0.18)]),
        ("Curtis Thompson", [0.0, 0.0, 0.0, 0.0],           [(0.025, None, 0, 0, 0), (0.825, 75.5, 2.75, 2.55, 0.22), (0.150, 82.3, 2.35, 2.45, 0.18)]),
        ("Julius Yego", [0.0, 0.0, 0.0, 0.0],               [(0.005, None, 0, 0, 0), (0.995, 78.3, 2.25, 2.45, 0.19)]),
    ]),
]

print("=== Q1 (30434) MEN'S JAVELIN: SEP 12 (T+1d, warm fast runway + slightly wider champ variance) ===")
rmj = sim_jav(mj_sep12, fr2_mult=0.65)
for k, v in sorted(rmj.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")

# ==============================================================================
# 2. MEN'S 200M (qid=653425) — Sat Sep 12 POST-100m UPDATE!
#    Sat Sep 12 100m Results:
#    - Bednarek: 9.94 (-0.7) Semi -> 9.85 (-0.6) SB FINAL WIN over Seville (9.90)!
#      Completely healthy, warm 67F Budapest track, targeting $300k double!
#    - Tebogo: 9.95 (-0.2) Semi -> 10.07 (-0.6) 7th in Final (0.22s behind Bednarek!)
#    Model 3 regimes carefully balancing:
#    - R1 (55%): Bednarek confirmed peak (~19.575 mean, small 100m-fatigue/off-day tail 14% at 19.79, DNS=1.2%);
#                Tebogo sub-peak / 2-round drag (20% peak 19.68, 76% 19.91, 4% DNS/tweak after 10.07 final).
#    - R2 (25%): Post-100m fatigue / emotional dip for Bednarek (DNS=2.5%, 28% tired 19.80, 69.5% 19.65)
#                + Tebogo saved legs in 100m final & rebounds in his signature 200m (38% peak 19.64, 59% 19.85, 3% DNS)
#                + Fresh specialists (Dambile, Levell, De Grasse, Charamba) slightly faster.
#    - R3 (20%): Bednarek unstoppable momentum PB run (DNS=0.8%, 7.2% 19.73, 92% 19.53)
#                + Tebogo genuinely off-form/fatigued (10% 19.74, 84% 19.96, 6% DNS).
# ==============================================================================
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
        # False start / DQ / acute cramp risk per round (higher for 100/200 doublers on race #3 & #4)
        dq_semi = np.where(is_dbl[None, :], 0.015, 0.008)
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
        dq_fin = np.where(is_dbl[None, :], 0.015, 0.008)
        ok_fin = in_final & (rng.random((n, k)) >= dq_fin)
        t_fin = np.where(ok_fin, day_mu + rng.normal(0.0, race_sd), 99.0)
        winners = np.argmin(t_fin, axis=1)
        probs = np.bincount(winners, minlength=k) / n
        top5 = ", ".join(f"{names[i].split()[-1]}:{probs[i]:.3f}" for i in np.argsort(-probs)[:5])
        print(f"  [{rname:28s} w={weight:.2f}] {top5}")
        blend += weight * probs
    return dict(zip(names, blend))

regimes_200m_sep12 = [
    ("R1: Base Post-100m Peak", 0.55, [
        ("Kenny Bednarek",         True,  [(0.012, None, 0, 0), (0.138, 19.79, 0.085, 0.070), (0.850, 19.575, 0.078, 0.068)]),
        ("Letsile Tebogo",         True,  [(0.040, None, 0, 0), (0.760, 19.91, 0.092, 0.072), (0.200, 19.68, 0.085, 0.070)]),
        ("Sinesipho Dambile",      False, [(0.008, None, 0, 0), (0.992, 19.83, 0.085, 0.070)]),
        ("Bryan Levell",           False, [(0.010, None, 0, 0), (0.840, 19.94, 0.090, 0.070), (0.150, 19.73, 0.085, 0.070)]),
        ("Andre De Grasse",        False, [(0.010, None, 0, 0), (0.850, 19.92, 0.085, 0.070), (0.140, 19.77, 0.085, 0.070)]),
        ("Makanakaishe Charamba",  False, [(0.008, None, 0, 0), (0.992, 19.90, 0.085, 0.070)]),
        ("Jose Figueroa",          False, [(0.008, None, 0, 0), (0.792, 20.12, 0.100, 0.075), (0.200, 19.84, 0.090, 0.070)]),
        ("Alexander Ogando",       False, [(0.008, None, 0, 0), (0.992, 19.95, 0.085, 0.070)]),
        ("Courtney Lindsey",       False, [(0.008, None, 0, 0), (0.892, 20.05, 0.090, 0.070), (0.100, 19.84, 0.085, 0.070)]),
        ("Yassine Hssine",         False, [(0.008, None, 0, 0), (0.992, 20.00, 0.090, 0.070)]),
        ("Brandon Hicklin",        False, [(0.008, None, 0, 0), (0.992, 20.02, 0.090, 0.070)]),
        ("Udodi Chudi Onwuzurike", False, [(0.008, None, 0, 0), (0.992, 20.06, 0.095, 0.070)]),
        ("Aaron Brown",            False, [(0.008, None, 0, 0), (0.992, 20.09, 0.085, 0.070)]),
        ("Timothe Mumenthaler",    False, [(0.008, None, 0, 0), (0.992, 20.13, 0.085, 0.070)]),
        ("Christopher Taylor",     False, [(0.008, None, 0, 0), (0.992, 20.15, 0.090, 0.070)]),
        ("Kyree King",             False, [(0.008, None, 0, 0), (0.992, 20.18, 0.090, 0.070)]),
    ]),
    ("R2: Bednarek Fatigue/Tebogo Rebound", 0.25, [
        ("Kenny Bednarek",         True,  [(0.025, None, 0, 0), (0.280, 19.80, 0.085, 0.070), (0.695, 19.65, 0.080, 0.068)]),
        ("Letsile Tebogo",         True,  [(0.030, None, 0, 0), (0.590, 19.85, 0.090, 0.070), (0.380, 19.64, 0.085, 0.070)]),
        ("Sinesipho Dambile",      False, [(0.008, None, 0, 0), (0.992, 19.80, 0.085, 0.070)]),
        ("Bryan Levell",           False, [(0.010, None, 0, 0), (0.755, 19.91, 0.090, 0.070), (0.235, 19.71, 0.085, 0.070)]),
        ("Andre De Grasse",        False, [(0.010, None, 0, 0), (0.790, 19.90, 0.085, 0.070), (0.200, 19.75, 0.085, 0.070)]),
        ("Makanakaishe Charamba",  False, [(0.008, None, 0, 0), (0.992, 19.87, 0.085, 0.070)]),
        ("Jose Figueroa",          False, [(0.008, None, 0, 0), (0.732, 20.08, 0.100, 0.075), (0.260, 19.81, 0.090, 0.070)]),
        ("Alexander Ogando",       False, [(0.008, None, 0, 0), (0.992, 19.92, 0.085, 0.070)]),
        ("Courtney Lindsey",       False, [(0.008, None, 0, 0), (0.842, 20.02, 0.090, 0.070), (0.150, 19.81, 0.085, 0.070)]),
        ("Yassine Hssine",         False, [(0.008, None, 0, 0), (0.992, 19.97, 0.090, 0.070)]),
        ("Brandon Hicklin",        False, [(0.008, None, 0, 0), (0.992, 19.99, 0.090, 0.070)]),
        ("Udodi Chudi Onwuzurike", False, [(0.008, None, 0, 0), (0.992, 20.03, 0.095, 0.070)]),
        ("Aaron Brown",            False, [(0.008, None, 0, 0), (0.992, 20.06, 0.085, 0.070)]),
        ("Timothe Mumenthaler",    False, [(0.008, None, 0, 0), (0.992, 20.11, 0.085, 0.070)]),
        ("Christopher Taylor",     False, [(0.008, None, 0, 0), (0.992, 20.13, 0.090, 0.070)]),
        ("Kyree King",             False, [(0.008, None, 0, 0), (0.992, 20.16, 0.090, 0.070)]),
    ]),
    ("R3: Bednarek PB Momentum", 0.20, [
        ("Kenny Bednarek",         True,  [(0.008, None, 0, 0), (0.072, 19.73, 0.080, 0.068), (0.920, 19.53, 0.075, 0.065)]),
        ("Letsile Tebogo",         True,  [(0.060, None, 0, 0), (0.840, 19.96, 0.092, 0.072), (0.100, 19.74, 0.085, 0.070)]),
        ("Sinesipho Dambile",      False, [(0.008, None, 0, 0), (0.992, 19.85, 0.085, 0.070)]),
        ("Bryan Levell",           False, [(0.010, None, 0, 0), (0.895, 19.96, 0.090, 0.070), (0.095, 19.76, 0.085, 0.070)]),
        ("Andre De Grasse",        False, [(0.010, None, 0, 0), (0.905, 19.95, 0.085, 0.070), (0.085, 19.80, 0.085, 0.070)]),
        ("Makanakaishe Charamba",  False, [(0.008, None, 0, 0), (0.992, 19.92, 0.085, 0.070)]),
        ("Jose Figueroa",          False, [(0.008, None, 0, 0), (0.842, 20.15, 0.100, 0.075), (0.150, 19.88, 0.090, 0.070)]),
        ("Alexander Ogando",       False, [(0.008, None, 0, 0), (0.992, 19.97, 0.085, 0.070)]),
        ("Courtney Lindsey",       False, [(0.008, None, 0, 0), (0.912, 20.07, 0.090, 0.070), (0.080, 19.88, 0.085, 0.070)]),
        ("Yassine Hssine",         False, [(0.008, None, 0, 0), (0.992, 20.02, 0.090, 0.070)]),
        ("Brandon Hicklin",        False, [(0.008, None, 0, 0), (0.992, 20.04, 0.090, 0.070)]),
        ("Udodi Chudi Onwuzurike", False, [(0.008, None, 0, 0), (0.992, 20.08, 0.095, 0.070)]),
        ("Aaron Brown",            False, [(0.008, None, 0, 0), (0.992, 20.11, 0.085, 0.070)]),
        ("Timothe Mumenthaler",    False, [(0.008, None, 0, 0), (0.992, 20.15, 0.085, 0.070)]),
        ("Christopher Taylor",     False, [(0.008, None, 0, 0), (0.992, 20.17, 0.090, 0.070)]),
        ("Kyree King",             False, [(0.008, None, 0, 0), (0.992, 20.20, 0.090, 0.070)]),
    ]),
]

print("\n=== Q2 (653425) MEN'S 200M: SEP 12 (Post-100m 9.85 SB win vs Tebogo 10.07 7th) ===")
r200 = sim_200m(regimes_200m_sep12)
for k, v in sorted(r200.items(), key=lambda x: -x[1])[:8]:
    print(f"  {k:26s}: {v:.4f}")

# ==============================================================================
# 3. UFC 331 ODDS & MARGINALS (qid=425800 & qid=574553) — T+7d (Sep 19)
# ==============================================================================
def vig_free(odds_a, odds_b):
    pa = (-odds_a) / (-odds_a + 100) if odds_a < 0 else 100 / (odds_a + 100)
    pb = (-odds_b) / (-odds_b + 100) if odds_b < 0 else 100 / (odds_b + 100)
    return pa / (pa + pb), pb / (pa + pb)

print("\n=== Q3 (425800) UFC 331 FLYWEIGHT TITLE: VAN vs PANTOJA ===")
v_19, p_19 = vig_free(-121, 100)
v_bov, p_bov = vig_free(-122, 102)
v_kh, p_kh = vig_free(-120, -102)
print(f"  19-book avg (-121/+100): Van={v_19:.4f}, Pantoja={p_19:.4f}")
print(f"  Bovada (-122/+102):      Van={v_bov:.4f}, Pantoja={p_bov:.4f}")
print(f"  KhelNow (-120/-102):     Van={v_kh:.4f}, Pantoja={p_kh:.4f}")
p_van_cond = 0.55 * v_19 + 0.30 * v_bov + 0.15 * v_kh
p_pan_cond = 1.0 - p_van_cond
# T-7d (card confirmed intact Sep 11): Pantoja pullout 1.7%, Van pullout 1.3%, Draw/NC 1.5%
p_both = 1.0 - 0.017 - 0.013
p_dec = p_both * (1.0 - 0.015)
# Replacement bout happens 55% of time if one pulls out; remaining champ/challenger 60% vs replacement
van_marg = p_dec * p_van_cond + 0.017 * 0.55 * 0.60
pan_marg = p_dec * p_pan_cond + 0.013 * 0.55 * 0.60
rep_win = (0.017 + 0.013) * 0.55 * 0.40
print(f"  Conditional blend: Van={p_van_cond:.4f}, Pantoja={p_pan_cond:.4f}")
print(f"  Marginal T-7d:     Van={van_marg:.4f}, Pantoja={pan_marg:.4f}, AnyReplacement={rep_win:.4f}")

print("\n=== Q4 (574553) UFC 331 LW CO-MAIN: TSARUKYAN vs RUFFY ===")
t_sep11, r_sep11 = vig_free(-325, 265)
t_bov, r_bov = vig_free(-340, 275)
t_old, r_old = vig_free(-380, 305)
print(f"  Heavy Sep 11 (-325/+265): Tsarukyan={t_sep11:.4f}, Ruffy={r_sep11:.4f}")
print(f"  Bovada Sep 9 (-340/+275): Tsarukyan={t_bov:.4f}, Ruffy={r_bov:.4f}")
print(f"  Old Sep 2    (-380/+305): Tsarukyan={t_old:.4f}, Ruffy={r_old:.4f}")
p_tsa_cond = 0.65 * t_sep11 + 0.35 * t_bov
p_ruf_cond = 1.0 - p_tsa_cond
# T-7d: Tsarukyan 3.2% pullout (weigh-in/back risk still ahead on Sep 18), Ruffy 1.2%, Draw/NC 1.0%
p_dec_lw = (1.0 - 0.032 - 0.012) * (1.0 - 0.010)
# Moicano (-190) vs Ortega (+163) on same main card (LW!) -> vig-free:
m_cond, o_cond = vig_free(-190, 163)
# If Tsarukyan out (3.2%): 40% Ruffy vs repl (55/45), 45% Moicano-Ortega elevated, 15% non-LW elevated
# If Ruffy out (1.2%): 75% Tsarukyan vs repl (72/28), 25% Moicano-Ortega elevated
tsa_marg = p_dec_lw * p_tsa_cond + 0.012 * 0.75 * 0.72
ruf_marg = p_dec_lw * p_ruf_cond + 0.032 * 0.40 * 0.55
# Moicano/Ortega win via elevation OR stepping in as replacement (~55% of replacements = Moicano, ~20% Ortega, ~15% Oliveira)
elev = 0.032 * 0.45 + 0.012 * 0.25
repl_win_lw = 0.032 * 0.40 * 0.45 + 0.012 * 0.75 * 0.28
moi_marg = elev * m_cond + repl_win_lw * 0.50
ort_marg = elev * o_cond + repl_win_lw * 0.15
oli_marg = repl_win_lw * 0.20
print(f"  Conditional blend: Tsarukyan={p_tsa_cond:.4f}, Ruffy={p_ruf_cond:.4f} (Moicano-Ortega: {m_cond:.3f}/{o_cond:.3f})")
print(f"  Marginal T-7d:     Tsarukyan={tsa_marg:.4f}, Ruffy={ruf_marg:.4f}, Moicano={moi_marg:.4f}, Ortega={ort_marg:.4f}, Oliveira={oli_marg:.4f}")
