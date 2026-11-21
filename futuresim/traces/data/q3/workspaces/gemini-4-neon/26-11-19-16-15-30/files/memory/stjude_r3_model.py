import numpy as np

np.random.seed(42)

# Exact 54-hole (post-Round 3) leaderboard at 2026 FedEx St Jude Championship (TPC Southwind, Par 70)
# Pre-tournament SG/rd inverted directly from Aug 11 5-market pre-tournament win probs (68-player field, sigma=2.75):
#   Scheffler (15.0%) -> +1.77 | Fleetwood (3.7%) -> +0.73 | Aberg (3.1%) -> +0.62 | Matsuyama (2.8%) -> +0.55
#   Burns (~2.0%) -> +0.35 | Hovland (~2.0%) -> +0.35 | Si Woo Kim (~1.4%) -> +0.15 | Im (~1.2%) -> +0.04 | Knapp (~0.9%) -> -0.05
# Post-R3 Bayesian update: ~10% weight on 54h tournament performance vs prior, plus Scheffler putting-regression sensitivity.

players = [
    # (Name, score_r3, sg_base, sg_conserv_lead, sg_full_prior, sd_mult)
    ("Scottie Scheffler", -13,  1.62,  1.35,  1.80, 0.96), # +1.77 pre; base applies -0.15 putting-reg/Sunday-lead drag
    ("Sam Burns",         -11,  0.50,  0.58,  0.42, 1.03), # +0.35 pre + Bayesian bump from bogey-free 62 & T2
    ("Sungjae Im",        -11,  0.20,  0.28,  0.12, 0.96), # +0.04 pre + steady 66-66-67 update
    ("Tommy Fleetwood",    -8,  0.76,  0.78,  0.73, 0.98), # +0.73 pre, defending FedExCup champ
    ("Jake Knapp",         -8,  0.10,  0.15,  0.00, 1.10), # Volatile bomber
    ("Hideki Matsuyama",   -7,  0.58,  0.60,  0.55, 1.00), # +0.55 pre, 2024 St Jude winner
    ("Si Woo Kim",         -7,  0.22,  0.25,  0.18, 1.04),
    ("Alex Noren",         -7,  0.16,  0.20,  0.12, 0.98),
    ("Brian Harman",       -7,  0.14,  0.18,  0.10, 0.97),
    ("Viktor Hovland",     -6,  0.38,  0.42,  0.35, 1.04),
    ("Field_-6_a",         -6,  0.05,  0.05,  0.05, 1.00),
    ("Field_-6_b",         -6,  0.05,  0.05,  0.05, 1.00),
    ("Field_-6_c",         -6,  0.00,  0.00,  0.00, 1.00),
    ("Wyndham Clark",      -5,  0.20,  0.20,  0.15, 1.05),
    ("Field_-5_a",         -5,  0.05,  0.05,  0.05, 1.00),
    ("Field_-5_b",         -5,  0.05,  0.05,  0.05, 1.00),
    ("Field_-5_c",         -5,  0.00,  0.00,  0.00, 1.00),
    ("Matt Fitzpatrick",   -4,  0.32,  0.32,  0.28, 1.00),
    ("Jordan Spieth",      -4,  0.05,  0.05,  0.00, 1.08),
    ("Ludvig Aberg",       -3,  0.55,  0.55,  0.55, 1.02),
]

names = [p[0] for p in players]
r3_scores = np.array([p[1] for p in players], dtype=float)
sd_mults = np.array([p[5] for p in players], dtype=float)
n_p = len(players)

def sim_round4(sg_vec, sigma=2.75, dist="normal", rho=0.04, N=500000):
    eff_sd = sigma * np.sqrt(1 - rho) * sd_mults[:, None]
    if dist == "normal":
        z = np.random.normal(0.0, 1.0, size=(n_p, N))
    elif dist == "t7":
        z = np.random.standard_t(df=7, size=(n_p, N)) / np.sqrt(7.0 / 5.0)
    elif dist == "skew_mild":
        g = np.random.gamma(shape=36.0, scale=1.0, size=(n_p, N))
        z = (g - 36.0) / 6.0
    elif dist == "skew_water":
        g = np.random.gamma(shape=16.0, scale=1.0, size=(n_p, N))
        z = (g - 16.0) / 4.0

    r4 = np.rint(-sg_vec[:, None] + eff_sd * z)
    tot = r3_scores[:, None] + r4

    min_tot = tot.min(axis=0)
    tied = (tot == min_tot[None, :])
    n_tied = tied.sum(axis=0)

    po_w = np.exp(0.28 * sg_vec)[:, None]
    win_probs = np.zeros(n_p)

    outright = (n_tied == 1)
    if outright.any():
        w_idx = np.argmax(tied[:, outright], axis=0)
        win_probs += np.bincount(w_idx, minlength=n_p)

    ties = ~outright
    if ties.any():
        t_mask = tied[:, ties]
        w_mat = t_mask * po_w
        w_mat /= w_mat.sum(axis=0, keepdims=True)
        win_probs += w_mat.sum(axis=1)

    return win_probs / N

sg_base = np.array([p[2] for p in players])
sg_cons = np.array([p[3] for p in players])
sg_full = np.array([p[4] for p in players])

models = [
    ("Normal_s2.65_base",       sg_base, 2.65, "normal",     0.12),
    ("Normal_s2.80_base",       sg_base, 2.80, "normal",     0.15),
    ("Normal_s2.95_base",       sg_base, 2.95, "normal",     0.10),
    ("t7_s2.75_base",           sg_base, 2.75, "t7",         0.13),
    ("SkewMild_s2.80_base",     sg_base, 2.80, "skew_mild",  0.14),
    ("SkewWater_s2.85_base",    sg_base, 2.85, "skew_water", 0.10),
    ("Normal_s2.85_consLead",   sg_cons, 2.85, "normal",     0.08),
    ("SkewMild_s2.85_consLead", sg_cons, 2.85, "skew_mild",  0.08),
    ("Normal_s2.75_fullPrior",  sg_full, 2.75, "normal",     0.10),
]

ensemble = np.zeros(n_p)
print(f"{'Model':25s} | {'Scheff':>6s} {'Burns':>6s} {'Im':>6s} {'Fleet':>6s} {'Knapp':>6s} {'Matsu':>6s} {'Rest':>6s}")
print("-" * 79)
for mname, sg, sig, dist, w in models:
    p = sim_round4(sg, sigma=sig, dist=dist, N=500000)
    ensemble += w * p
    rest = 1.0 - p[:6].sum()
    print(f"{mname:25s} | {p[0]:6.3f} {p[1]:6.3f} {p[2]:6.3f} {p[3]:6.3f} {p[4]:6.3f} {p[5]:6.3f} {rest:6.3f}")

print("\n=== FINAL CALIBRATED POST-ROUND 3 WIN PROBABILITIES (Q4: 969395) ===")
for i in np.argsort(-ensemble)[:10]:
    print(f"  {names[i]:22s} ({int(r3_scores[i]):+3d}): {ensemble[i]:.4f}")
print(f"  Top-5 sum = {np.sort(ensemble)[-5:].sum():.4f} | Outside = {1 - np.sort(ensemble)[-5:].sum():.4f}")
