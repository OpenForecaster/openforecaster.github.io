import numpy as np

rng = np.random.default_rng(20260904)

print("==========================================================")
print("1. Q2 (qid=284913): LA LIGA LEADER AFTER VALENCIA-BARCELONA")
print("==========================================================")
# Confirmed state after Fri Sep 4 Real Betis 1-0 Real Madrid:
# - Barcelona: 9 pts, +10 GD, 12 GF (3 MP) -> plays Valencia (A) Sun Sep 6 16:15 CEST
# - Real Madrid: 9 pts, +7 GD, 10 GF (4 MP) -> DONE
# - Atletico Madrid: 7 pts, +4 GD, ~7 GF (3 MP) -> plays Athletic Club (A) Sat Sep 5 16:15 CEST
# - Alaves (7), Osasuna (7), Sevilla (6-7) all play AFTER Valencia-Barcelona!
# - Betis (7 or 9 pts, 0 GD) -> DONE, cannot beat +10/+7 GD.

def sim_laliga(lam_val, lam_bar, lam_ath, lam_atm, n=1_000_000, sigma=0.12, red_card_p=0.025):
    # Hierarchical Poisson with match-level tempo/form dispersion + rare early red card tail
    # Team-level lognormal noise
    z_v = np.exp(rng.normal(0, sigma, n))
    z_b = np.exp(rng.normal(0, sigma, n))
    z_h = np.exp(rng.normal(0, sigma, n))
    z_a = np.exp(rng.normal(0, sigma, n))

    # Rare early red card shock in Valencia-Barcelona (e.g. Barca red card -> Val +0.75x, Bar *0.65)
    bar_rc = rng.random(n) < red_card_p
    val_rc = rng.random(n) < red_card_p

    lv = lam_val * z_v * np.where(bar_rc, 1.65, 1.0) * np.where(val_rc, 0.60, 1.0)
    lb = lam_bar * z_b * np.where(bar_rc, 0.60, 1.0) * np.where(val_rc, 1.40, 1.0)

    gv = rng.poisson(lv)
    gb = rng.poisson(lb)
    gh = rng.poisson(lam_ath * z_h)
    ga = rng.poisson(lam_atm * z_a)

    # Resulting tables
    bar_pts = 9 + np.where(gb > gv, 3, np.where(gb == gv, 1, 0))
    bar_gd  = 10 + (gb - gv)
    bar_gf  = 12 + gb

    atm_pts = 7 + np.where(ga > gh, 3, np.where(ga == gh, 1, 0))
    atm_gd  = 4 + (ga - gh)
    atm_gf  = 7 + ga

    rm_pts  = np.full(n, 9)
    rm_gd   = np.full(n, 7)
    rm_gf   = np.full(n, 10)

    # Rank tuples (pts, gd, gf)
    bar_key = bar_pts * 10000 + (bar_gd + 50) * 100 + bar_gf
    atm_key = atm_pts * 10000 + (atm_gd + 50) * 100 + atm_gf
    rm_key  = rm_pts  * 10000 + (rm_gd  + 50) * 100 + rm_gf

    p_bar_win = np.mean(gb > gv)
    p_bar_drw = np.mean(gb == gv)
    p_val_win = np.mean(gv > gb)
    p_atm_win = np.mean(ga > gh)

    lead_bar = np.mean((bar_key >= atm_key) & (bar_key >= rm_key))
    lead_atm = np.mean((atm_key > bar_key) & (atm_key >= rm_key))
    lead_rm  = np.mean((rm_key > bar_key) & (rm_key > atm_key))
    return (p_bar_win, p_bar_drw, p_val_win, p_atm_win, lead_bar, lead_atm, lead_rm)

scenarios = [
    ("Base (Bar ~74%, Val ~10%, ATM ~40%)",    0.88, 2.45, 1.10, 1.32),
    ("Market Sep4 (Bar ~75%, Val ~9.5%, ATM ~41%)", 0.85, 2.50, 1.08, 1.34),
    ("Conservative upset (Bar ~70%, Val ~12%, ATM ~42%)", 0.96, 2.32, 1.06, 1.35),
    ("High-scoring BTTS (Over2.5 ~69%, BTTS ~56%)", 0.98, 2.65, 1.10, 1.32),
]
res_list = []
for name, lv, lb, lh, la in scenarios:
    out = sim_laliga(lv, lb, lh, la)
    res_list.append(out)
    print(f"{name:52s} | Val-Bar W/D/L={out[0]:.3f}/{out[1]:.3f}/{out[2]:.3f} ATM_W={out[3]:.3f} => LEAD: Bar={out[4]:.4f}, ATM={out[5]:.4f}, RM={out[6]:.5f}")
avg_bar = np.mean([r[4] for r in res_list])
avg_atm = np.mean([r[5] for r in res_list])
avg_rm  = np.mean([r[6] for r in res_list])
print(f"ENSEMBLE MEAN => Barcelona={avg_bar:.4f}, Atletico Madrid={avg_atm:.4f}, Real Madrid={avg_rm:.5f}")


print("\n==========================================================")
print("2. Q1 (qid=668636): 2026 F1 ITALIAN GRAND PRIX (MONZA)")
print("==========================================================")
# Combine pre-FP2 market prior (Sep 3 Betfair/Snai/TABtouch) + Fri FP1/FP2 evidence + Post-FP2 Bet365 Quali market
# Drivers: Russell, Leclerc, Hamilton, Norris, Antonelli, Piastri, Verstappen, Field
# Pre-FP2 win probs (Sep 3):
# Norris 0.31, Russell 0.27, Leclerc 0.125, Hamilton 0.125, Antonelli 0.06, Piastri 0.055, Verstappen 0.045, Field 0.010

# Simulate Monza Qualifying + Race Pace (500k trials):
# Effective grid pace (s relative to Russell=0.00):
# FP2 quali gaps: RUS 0.00, LEC +0.12, ANT +0.14 (P20 penalty!), NOR +0.38, HAM +0.46 (FP1 +0.17 vs LEC), PIA +0.47, VER +0.82
# Account for overnight setup evolution (sigma_overnight ~ 0.18s for McLaren recovery, 0.12s for others) + tow advantage for Russell (-0.08s from Antonelli!)
N = 500_000
drivers = ["George Russell", "Charles Leclerc", "Lewis Hamilton", "Lando Norris", "Kimi Antonelli", "Oscar Piastri", "Max Verstappen", "Field"]

# Qualifying true pace distribution (relative to 0, lower = faster)
# Note: Norris/Piastri get mean -0.15s overnight recovery from FP2 (still +0.23s behind RUS, matching 11/2 pole odds!)
# Hamilton gets mean -0.22s from FP2 (FP1 was +0.17s behind LEC, admitted didn't hook lap up, 5/1 pole odds!)
q_mean = np.array([-0.06, 0.08, 0.20, 0.24, 9.99, 0.36, 0.50, 0.85]) # ANT penalized to back!
q_sd   = np.array([ 0.16, 0.16, 0.18, 0.22, 0.01, 0.22, 0.24, 0.30])
q_pace = rng.normal(q_mean, q_sd, size=(N, len(drivers)))
grid_pos = np.argsort(np.argsort(q_pace, axis=1), axis=1) + 1 # 1..8 (ANT is 8 -> actually P20)

# Race pace (s/lap relative to Ferrari/Merc benchmark):
# Motorsport.com adjusted long runs: LEC 0.00, HAM 0.00, RUS +0.02, ANT +0.04, NOR +0.19 (with overnight gain -> +0.11), PIA +0.22 (-> +0.16), VER +0.22
r_mean = np.array([0.01, 0.01, 0.02, 0.12, 0.03, 0.18, 0.24, 0.55])
r_sd   = np.array([0.14, 0.14, 0.14, 0.16, 0.14, 0.16, 0.18, 0.25])
r_pace = rng.normal(r_mean, r_sd, size=(N, len(drivers)))

# Monza race time proxy (53 laps): grid position penalty (~2.2s per grid spot for top 7, +18s for ANT starting P20 in traffic)
# Plus safety car event (32% chance) compresses grid gaps by 65% (huge help for Antonelli & mid-pack!)
sc = rng.random(N) < 0.32
pos_pen = np.where(grid_pos == 8, 17.5, (grid_pos - 1) * 2.1)
pos_pen = np.where(sc[:, None], pos_pen * 0.38, pos_pen)

# DNF / incident rate (~6% per driver)
dnf = rng.random((N, len(drivers))) < 0.06
# Race time = 53 * r_pace + pos_pen + strategy/pit noise
race_time = 53 * r_pace + pos_pen + rng.normal(0, 3.2, size=(N, len(drivers))) + np.where(dnf, 9999.0, 0.0)

pole_idx = np.argmin(q_pace, axis=1)
win_idx  = np.argmin(race_time, axis=1)
print("Simulated Monza Pole (ex-ANT) & Race Win probabilities:")
for i, d in enumerate(drivers):
    print(f"  {d:18s} | Pole={np.mean(pole_idx==i):.3f} | RaceWin={np.mean(win_idx==i):.3f}")


print("\n==========================================================")
print("3. Q5 (qid=971366): ENGLAND MOST WICKETS PAKISTAN 1ST INN (3RD TEST)")
print("==========================================================")
# Bowlers: Robinson, Tongue, Atkinson, Archer, Cook, Baker, Bashir, PartTimers(Root/Lawrence)
# Selection probs after Sep 4 Sri Lanka T20I squad announcement (T20Is start Sep 15, 2d after Test ends!):
# T20I squad includes: Archer, Atkinson, Tongue, Baker. EXCLUDES: Robinson, Cook, Bashir!
# England played 4 seamers at Lord's (Robinson, Tongue, Atkinson, Archer).
# Enumerate plausible Edgbaston 4-seamer + optional spinner XI combos!
# Base wicket-taking power (relative rate when playing, adjusted for economy tie-breaker edge!):
# Robinson 1.32 (16 wkts in 2 Tests, best economy), Tongue 1.15 (strike rate), Atkinson 1.08, Archer 1.05, Cook 0.92, Baker 0.85, Bashir 0.58 (Sep English seam pitch), PartTimers 0.12
bowlers = ["Ollie Robinson", "Josh Tongue", "Gus Atkinson", "Jofra Archer", "Sam Cook", "Sonny Baker", "Shoaib Bashir", "PartTimers"]
rates   = np.array([1.32, 1.15, 1.08, 1.05, 0.92, 0.85, 0.58, 0.12])
# Tie-breaker priority (lower economy wins tie in cricket scorecards! Robinson/Cook/Atkinson lowest econ)
econ_order = np.array([0, 4, 2, 3, 1, 5, 6, 7]) # lower = better economy

# Weighted XI combinations (4 seamers + PartTimers, or 3 seamers + Bashir + PartTimers):
# Note: Robinson plays ~95%; at least 1-2 of Archer/Atkinson/Tongue likely rested before Sep 15 T20Is in 2-0 dead rubber!
xis = [
    # (weight, [indices of playing bowlers])
    (0.18, [0, 1, 2, 3, 7]),       # Unchanged Lord's 4-seam attack (Rob, Ton, Atk, Arc)
    (0.22, [0, 1, 2, 4, 7]),       # Archer rested for T20Is -> Sam Cook in
    (0.14, [0, 1, 2, 5, 7]),       # Archer rested -> Sonny Baker debut/in
    (0.12, [0, 1, 4, 5, 7]),       # Archer & Atkinson rested -> Cook + Baker in
    (0.10, [0, 2, 4, 5, 7]),       # Archer & Tongue rested -> Cook + Baker in
    (0.08, [0, 1, 3, 4, 7]),       # Atkinson rested -> Cook in
    (0.06, [0, 1, 2, 6, 7]),       # Archer rested -> Bashir spinner in
    (0.05, [0, 1, 4, 6, 7]),       # Archer & Atkinson rested -> Cook + Bashir
    (0.05, [1, 2, 3, 4, 7]),       # Robinson rested (small 5% risk) -> Cook in
]
assert abs(sum(w for w, _ in xis) - 1.0) < 1e-9

win_counts = np.zeros(len(bowlers))
play_probs = np.zeros(len(bowlers))
M = 100_000
for w, idxs in xis:
    for idx in idxs:
        play_probs[idx] += w
    m_sub = int(M * w)
    sub_rates = rates[idxs]
    # Dirichlet-Multinomial (alpha scale = 8.0 captures overdispersion of 5-fers/spells!)
    alpha = 8.0 * sub_rates / sub_rates.sum()
    probs = rng.dirichlet(alpha, size=m_sub)
    # 10 wickets (occasionally 9 if run-out, say 9.6 avg -> 60% 10, 35% 9, 5% 8)
    n_wkts = rng.choice([10, 9, 8], size=m_sub, p=[0.65, 0.30, 0.05])
    # Draw multinomial wickets
    for k in [10, 9, 8]:
        mask = (n_wkts == k)
        if not np.any(mask): continue
        p_k = probs[mask]
        # vectorised draw via cumsum
        u = rng.random((p_k.shape[0], k))
        cdf = np.cumsum(p_k, axis=1)
        draws = (u[:, :, None] > cdf[:, None, :]).sum(axis=2) # shape (n, k) in 0..len(idxs)-1
        counts = np.zeros((p_k.shape[0], len(idxs)), dtype=int)
        for j in range(len(idxs)):
            counts[:, j] = (draws == j).sum(axis=1)
        # Winner: max wickets; ties broken by better economy (with slight noise)
        # In official scorecard, ties on wickets -> fewest runs conceded (economy order + noise)
        score = counts * 100.0 - econ_order[idxs] * 1.5 + rng.normal(0, 2.0, size=counts.shape)
        winners = np.argmax(score, axis=1)
        for j, b_idx in enumerate(idxs):
            win_counts[b_idx] += np.sum(winners == j)

win_probs = win_counts / win_counts.sum()
print("Simulated Edgbaston 3rd Test Most Wickets (Pakistan 1st innings):")
for i, b in enumerate(bowlers):
    print(f"  {b:18s} | P(Play)={play_probs[i]:.2f} | P(TopWkt)={win_probs[i]:.3f}")
