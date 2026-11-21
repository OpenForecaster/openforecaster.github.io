import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — TUESDAY SEPT 8, 2026 (Batch: athletics)
# Q1: qid=936021 — Men's 5,000m, World Athletics Ultimate Championship (Sep 11, T+3d)
# Q2: qid=30434  — Men's Javelin, World Athletics Ultimate Championship (Sep 13, T+5d)
# Q4: qid=574485 — PSA Women's World Squash Rankings on Sept 21, 2026 (T+10d)
# ==============================================================================

# ------------------------------------------------------------------------------
# MODEL 1: Q1 (qid=936021) — MEN'S 5,000m ULTIMATE CHAMPIONSHIP (EXACT 12-MAN FIELD)
# ------------------------------------------------------------------------------
# OFFICIAL REVISED ENTRY LIST (World Athletics, Sept 7, 2026 15:30 CEST):
#   OUT (0%): Birhanu Balew (was 0.115), Andreas Almgren (was 0.085), Jimmy Gressier (was 0.070)!
#   IN (Exact 12 men, Fri Sep 11 20:36 CEST):
#     1. Jakob Ingebrigtsen (NOR) - PB 12:48.45, SB 13:15.29 (Euro gold), WR #40
#        Fresh from 1500m only (Sep 4: 4th 3:30.52 SB, beat Hocker); Dagbladet says may skip 1500m to focus on 5k!
#     2. Cole Hocker (USA) - PB 12:57.82i, SB -- (first 5k of 2026), WR #5
#        Reigning 2025 World 5k champ; won Zurich DL 1500m (Aug 27), 7th Brussels 1500m (3:30.80); doubling 5k+1500m.
#     3. Addisu Yihune (ETH) - PB/SB 12:47.62, WR #1!
#        Won Xiamen & Oslo DL 5k in 2026; SKIPPED Brussels -> 100% FRESH!
#     4. Parker Wolfe (USA) - PB/SB 12:49.45, WR #3!
#        Won Zurich DL 3,000m (Aug 27); SKIPPED Brussels -> 100% FRESH!
#     5. Biniam Mehary (ETH) - PB 12:45.93, SB 12:47.78, WR #9
#        Age 19; led Brussels 3k in 7:41.98, finished 4th in 12:47.78 (6d turnaround).
#     6. Graham Blanks (USA) - PB/SB 12:47.98, WR #6
#        5th in Brussels (PR, was 2nd with 300m left; 6d turnaround).
#     7. Nico Young (USA) - PB 12:45.27, SB 12:48.12, WR #11
#        6th in Brussels (6d turnaround).
#     8. Egide Ntakarutimana (BDI) - PB/SB 12:46.73 (NR, fastest SB in field!), WR #13
#        2nd in Brussels DL Final (6d turnaround).
#     9. Cornelius Kemboi (KEN) - PB/SB 12:47.29 (PR), WR #14
#        3rd in Brussels DL Final (6d turnaround).
#    10. Grant Fisher (USA) - PB 12:44.09i, SB 12:49.61, WR #7
#        Won Paris DL 5k earlier, Olympic double bronze, BUT collapsed to 9th in Brussels (12:59.10).
#    11. Ky Robinson (AUS) - PB/SB 12:50.82, WR #8
#        SKIPPED Brussels -> 100% FRESH!
#    12. Jacob Krop (KEN) - PB 12:45.71, SB 12:51.23, WR #12
#        7th in Brussels (6d turnaround).

def sim_5000m(regimes, n_trials=250000, seed=93602108):
    rng = random.Random(seed)
    blend = Counter()
    for rname, weight, pace_probs, athletes in regimes:
        wins = Counter()
        for _ in range(n_trials):
            up = rng.random()
            if up < pace_probs[0]:
                pace = 0  # tactical sit-and-kick (13:05-13:25)
            elif up < pace_probs[0] + pace_probs[1]:
                pace = 1  # honest wind-up (12:53-13:05)
            else:
                pace = 2  # fast burn-up (<12:53)
            best_s = -1e9
            winner = None
            for name, p_start, states in athletes:
                if rng.random() > p_start:
                    continue
                u = rng.random()
                cum = 0.0
                chosen = states[-1]
                for st in states:
                    cum += st[0]
                    if u <= cum:
                        chosen = st
                        break
                _, mus, sd = chosen
                s = rng.gauss(mus[pace], sd)
                if s > best_s:
                    best_s = s
                    winner = name
            wins[winner] += 1
        probs = {k: c / n_trials for k, c in wins.items()}
        top7 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:7])
        print(f"  [{rname[:52]:52s} w={weight:.2f}] {top7}")
        for k, v in probs.items():
            blend[k] += weight * v
    return blend

regimes_5000m = [
    # R1 (50%): Base calibrated on exact 12-man field
    # Modest 6-day Brussels fatigue penalty (~0.15-0.20 rating) vs fresh runners (Ingebrigtsen, Hocker, Yihune, Wolfe, Robinson)
    ("R1: Base Exact-12 (Modest Brussels 6d Fatigue)", 0.50, (0.45, 0.35, 0.20), [
        # Ingebrigtsen: 98% starts (confirmed + may focus solely on 5k), bimodal Achilles recovery (22% slightly flat, 78% sharp)
        ("Jakob Ingebrigtsen", 0.98, [(0.22, (1.25, 1.60, 1.50), 0.95), (0.78, (1.90, 2.25, 2.05), 0.95)]),
        # Hocker: 95% starts (confirmed on Sep 7 list, minor 5% 1500m-only/illness scratch), bimodal (22% off/untested at 5k, 78% lethal kick)
        ("Cole Hocker",        0.95, [(0.22, (1.25, 0.95, 0.55), 0.95), (0.78, (2.30, 1.90, 1.35), 0.95)]),
        # Addisu Yihune: WR #1, 2x DL winner, 12:47.62, 100% FRESH!
        ("Addisu Yihune",      0.98, [(1.00, (1.15, 1.50, 1.75), 0.95)]),
        # Parker Wolfe: WR #3, won Zurich DL 3000m (Aug 27), 12:49.45, 100% FRESH!
        ("Parker Wolfe",       0.98, [(1.00, (1.25, 1.25, 1.15), 0.95)]),
        # Biniam Mehary: 19yo, 12:45.93 PB, 4th Brussels (12:47.78 after leading 3k in 7:41.98), 6d fatigue
        ("Biniam Mehary",      0.98, [(1.00, (0.95, 1.35, 1.60), 0.98)]),
        # Graham Blanks: WR #6, 12:47.98 PR Brussels (2nd at 300m left), 6d fatigue
        ("Graham Blanks",      0.98, [(1.00, (1.05, 1.20, 1.25), 0.95)]),
        # Nico Young: 12:45.27 PB, 12:48.12 Brussels (6th), 6d fatigue
        ("Nico Young",         0.98, [(1.00, (1.00, 1.15, 1.25), 0.95)]),
        # Egide Ntakarutimana: 12:46.73 NR (fastest SB, 2nd Brussels), 6d fatigue
        ("Egide Ntakarutimana",0.98, [(1.00, (0.90, 1.20, 1.45), 0.95)]),
        # Cornelius Kemboi: 12:47.29 PR (3rd Brussels), 6d fatigue
        ("Cornelius Kemboi",   0.98, [(1.00, (0.85, 1.15, 1.35), 0.95)]),
        # Grant Fisher: Paris DL winner, 12:44i PB, BUT collapsed 12:59.10 Brussels (70% flat / 30% bounce-back)
        ("Grant Fisher",       0.97, [(0.70, (0.30, 0.25, 0.10), 0.95), (0.30, (1.10, 1.15, 1.05), 0.95)]),
        # Ky Robinson: WR #8, 12:50.82, 100% FRESH
        ("Ky Robinson",        0.98, [(1.00, (0.85, 0.95, 0.95), 0.95)]),
        # Jacob Krop: 12:45.71 PB, 7th Brussels 12:51.23, 6d fatigue
        ("Jacob Krop",         0.98, [(1.00, (0.70, 0.85, 0.95), 0.95)]),
    ]),
    # R2 (25%): Slow Tactical Championship Sit-and-Kick (5 Americans + Ingebrigtsen control pace)
    ("R2: Slow Tactical / Fresh Kickers Dominate", 0.25, (0.65, 0.25, 0.10), [
        ("Jakob Ingebrigtsen", 0.98, [(0.18, (1.30, 1.65, 1.55), 0.95), (0.82, (1.95, 2.30, 2.10), 0.95)]),
        ("Cole Hocker",        0.96, [(0.18, (1.30, 1.00, 0.60), 0.95), (0.82, (2.40, 1.95, 1.40), 0.95)]),
        ("Addisu Yihune",      0.98, [(1.00, (1.15, 1.45, 1.65), 0.95)]),
        ("Parker Wolfe",       0.98, [(1.00, (1.35, 1.30, 1.15), 0.95)]),
        ("Biniam Mehary",      0.98, [(1.00, (0.85, 1.20, 1.45), 0.98)]),
        ("Graham Blanks",      0.98, [(1.00, (0.95, 1.10, 1.15), 0.95)]),
        ("Nico Young",         0.98, [(1.00, (0.90, 1.05, 1.15), 0.95)]),
        ("Egide Ntakarutimana",0.98, [(1.00, (0.80, 1.05, 1.30), 0.95)]),
        ("Cornelius Kemboi",   0.98, [(1.00, (0.75, 1.00, 1.20), 0.95)]),
        ("Grant Fisher",       0.97, [(0.75, (0.25, 0.20, 0.05), 0.95), (0.25, (1.05, 1.10, 1.00), 0.95)]),
        ("Ky Robinson",        0.98, [(1.00, (0.85, 0.90, 0.90), 0.95)]),
        ("Jacob Krop",         0.98, [(1.00, (0.65, 0.80, 0.85), 0.95)]),
    ]),
    # R3 (25%): Ethiopian/African Fast Honest Pace + Doublers Vulnerable (Achilles rust / Hocker untested 5k)
    ("R3: Honest/Fast 5k + Top-2 Vulnerable", 0.25, (0.20, 0.40, 0.40), [
        ("Jakob Ingebrigtsen", 0.97, [(0.35, (1.15, 1.45, 1.35), 0.95), (0.65, (1.70, 2.05, 1.90), 0.95)]),
        ("Cole Hocker",        0.92, [(0.35, (1.10, 0.80, 0.40), 0.95), (0.65, (2.10, 1.65, 1.15), 0.95)]),
        ("Addisu Yihune",      0.98, [(1.00, (1.25, 1.65, 1.95), 0.95)]),
        ("Parker Wolfe",       0.98, [(1.00, (1.20, 1.30, 1.25), 0.95)]),
        ("Biniam Mehary",      0.98, [(1.00, (1.10, 1.55, 1.85), 0.98)]),
        ("Graham Blanks",      0.98, [(1.00, (1.15, 1.35, 1.45), 0.95)]),
        ("Nico Young",         0.98, [(1.00, (1.10, 1.30, 1.45), 0.95)]),
        ("Egide Ntakarutimana",0.98, [(1.00, (1.05, 1.40, 1.70), 0.95)]),
        ("Cornelius Kemboi",   0.98, [(1.00, (1.00, 1.35, 1.60), 0.95)]),
        ("Grant Fisher",       0.97, [(0.70, (0.30, 0.25, 0.10), 0.95), (0.30, (1.15, 1.20, 1.15), 0.95)]),
        ("Ky Robinson",        0.98, [(1.00, (0.90, 1.05, 1.10), 0.95)]),
        ("Jacob Krop",         0.98, [(1.00, (0.80, 1.00, 1.15), 0.95)]),
    ]),
]

print("=== Q1 (qid=936021) MEN'S 5,000m ULTIMATE CHAMPIONSHIP (SEPT 8 EXACT 12-MAN FIELD) ===")
b5k = sim_5000m(regimes_5000m)
print("FINAL 5,000m BLEND (ALL 12):")
for k, v in sorted(b5k.items(), key=lambda x: -x[1]):
    print(f"  {k:24s}: {v:.4f}")
top5_5k = sorted(b5k.items(), key=lambda x: -x[1])[:5]
print("Top-5:", [(k, round(v, 4)) for k, v in top5_5k], "sum =", round(sum(v for _, v in top5_5k), 4))


# ------------------------------------------------------------------------------
# MODEL 2: Q2 (qid=30434) — MEN'S JAVELIN ULTIMATE CHAMPIONSHIP (EXACT 8-MAN FIELD)
# ------------------------------------------------------------------------------
# OFFICIAL REVISED ENTRY LIST (World Athletics, Sept 7, 2026 15:30 CEST):
#   OUT (0%): Neeraj Chopra, Sachin Yadav, Jakub Vadlejch!
#   IN (Exact 8 men, Sun Sep 13):
#     1. Rumesh Tharanga Pathirage (SRI, Bib 244) - WR #1, PB/SB 92.62m (12/13 wins in 2026, 89.04m Brussels)
#     2. Julian Weber (GER, Bib 165) - WR #3, PB 91.51m, SB 90.40m (Aug 15 Euro CR! CONFIRMED ENTERED!)
#     3. Anderson Peters (GRN, Bib 168) - WR #2, PB 93.07m, SB 86.93m (83.70m 4th Brussels)
#     4. Dawid Wegner (POL, Bib 232) - WR #9, PB/SB 87.47m (2nd Brussels PB! CONFIRMED ENTERED!)
#     5. Keshorn Walcott (TTO, Bib 251) - WR #5, PB 90.16m, SB 83.99m (3rd Brussels, reigning World champ)
#     6. Arshad Nadeem (PAK, Bib 228) - WR #10, PB 92.97m, SB 78.63m (Olympic champ, CONFIRMED ENTERED!)
#     7. Curtis Thompson (USA, Bib 286) - WR #4, PB 87.76m, SB 87.59m (69.52m Brussels collapse)
#     8. Julius Yego (KEN, Bib 209) - WR #7, PB 92.72m, SB 82.22m (76.79m Brussels)

def sim_javelin_mixture(regimes, n_trials=250000, seed=3043408):
    rng = random.Random(seed)
    blend = Counter()
    for rname, weight, athletes in regimes:
        wins = Counter()
        for _ in range(n_trials):
            best_m = -1.0
            winner = None
            for name, states in athletes:
                u = rng.random()
                cum = 0.0
                chosen = None
                for st in states:
                    cum += st[0]
                    if u <= cum:
                        chosen = st
                        break
                if chosen is None or chosen[1] is None:
                    continue
                _, mu, dsd, tsd, fr = chosen
                day_mu = rng.gauss(mu, dsd)
                ath_best = 0.0
                for _t in range(6):
                    if rng.random() < fr:
                        continue
                    val = rng.gauss(day_mu, tsd)
                    if val > ath_best:
                        ath_best = val
                if ath_best > best_m:
                    best_m = ath_best
                    winner = name
            wins[winner] += 1
        probs = {k: c / n_trials for k, c in wins.items()}
        top6 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:6])
        print(f"  [{rname[:52]:52s} w={weight:.2f}] {top6}")
        for k, v in probs.items():
            blend[k] += weight * v
    return blend

men_jav_sep08 = [
    # R1 (55%): Base Calibrated on Exact 8-Man Field
    # Weber confirmed entered -> DNS drops 38%->10%, ~30% sub-100% rust, ~60% peak ~89m E[best6]!
    # Wegner confirmed entered -> DNS drops 48%->2%, riding 87.47m PB wave (~85.5m E[best6])!
    # Nadeem confirmed entered -> DNS drops 42%->12%, ~58% injury rust (~82m), ~30% healthy peak (~88m)!
    ("R1: Base Exact-8 (Weber 10% DNS/60% peak; Wegner IN)", 0.55, [
        ("Rumesh Tharanga Pathirage", [(0.02, None, 0, 0, 0), (0.13, 85.6, 2.0, 2.3, 0.16), (0.85, 87.7, 2.0, 2.3, 0.16)]),
        ("Julian Weber",              [(0.10, None, 0, 0, 0), (0.30, 83.4, 2.2, 2.3, 0.16), (0.60, 86.3, 2.1, 2.3, 0.16)]),
        ("Anderson Peters",           [(0.02, None, 0, 0, 0), (0.98, 83.9, 2.4, 2.5, 0.17)]),
        ("Dawid Wegner",              [(0.02, None, 0, 0, 0), (0.98, 82.8, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.12, None, 0, 0, 0), (0.58, 79.5, 2.5, 2.5, 0.18), (0.30, 84.8, 2.7, 2.6, 0.17)]),
        ("Keshorn Walcott",           [(0.02, None, 0, 0, 0), (0.98, 82.3, 2.3, 2.4, 0.17)]),
        ("Curtis Thompson",           [(0.12, None, 0, 0, 0), (0.76, 76.0, 2.8, 2.5, 0.20), (0.12, 82.8, 2.4, 2.4, 0.17)]),
        ("Julius Yego",               [(0.03, None, 0, 0, 0), (0.97, 79.2, 2.3, 2.4, 0.17)]),
    ]),
    # R2 (25%): Pathirage Slight Workload Dip + Weber/Nadeem/Peters Peak
    ("R2: Pathirage Dip + Weber/Nadeem/Peters Peak", 0.25, [
        ("Rumesh Tharanga Pathirage", [(0.03, None, 0, 0, 0), (0.27, 85.2, 2.1, 2.3, 0.17), (0.70, 87.0, 2.1, 2.3, 0.16)]),
        ("Julian Weber",              [(0.05, None, 0, 0, 0), (0.20, 84.2, 2.1, 2.3, 0.16), (0.75, 86.7, 2.0, 2.3, 0.16)]),
        ("Anderson Peters",           [(0.02, None, 0, 0, 0), (0.98, 84.7, 2.4, 2.5, 0.17)]),
        ("Dawid Wegner",              [(0.02, None, 0, 0, 0), (0.98, 83.4, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.08, None, 0, 0, 0), (0.52, 80.2, 2.5, 2.5, 0.18), (0.40, 85.4, 2.7, 2.6, 0.17)]),
        ("Keshorn Walcott",           [(0.02, None, 0, 0, 0), (0.98, 82.8, 2.3, 2.4, 0.17)]),
        ("Curtis Thompson",           [(0.12, None, 0, 0, 0), (0.73, 76.5, 2.8, 2.5, 0.20), (0.15, 83.2, 2.4, 2.4, 0.17)]),
        ("Julius Yego",               [(0.03, None, 0, 0, 0), (0.97, 79.8, 2.3, 2.4, 0.17)]),
    ]),
    # R3 (20%): Pathirage Dominant (91m+) + Weber/Nadeem Rusty from Injury Layoff
    ("R3: Pathirage 91m+ & Weber/Nadeem Rusty", 0.20, [
        ("Rumesh Tharanga Pathirage", [(0.01, None, 0, 0, 0), (0.09, 86.2, 1.9, 2.3, 0.16), (0.90, 88.2, 1.9, 2.3, 0.16)]),
        ("Julian Weber",              [(0.20, None, 0, 0, 0), (0.45, 82.8, 2.2, 2.3, 0.16), (0.35, 85.8, 2.1, 2.3, 0.16)]),
        ("Anderson Peters",           [(0.02, None, 0, 0, 0), (0.98, 83.6, 2.3, 2.5, 0.17)]),
        ("Dawid Wegner",              [(0.02, None, 0, 0, 0), (0.98, 82.4, 2.2, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.22, None, 0, 0, 0), (0.63, 78.8, 2.4, 2.5, 0.18), (0.15, 84.0, 2.7, 2.6, 0.17)]),
        ("Keshorn Walcott",           [(0.02, None, 0, 0, 0), (0.98, 82.0, 2.3, 2.4, 0.17)]),
        ("Curtis Thompson",           [(0.15, None, 0, 0, 0), (0.78, 75.5, 2.8, 2.5, 0.20), (0.07, 82.0, 2.4, 2.4, 0.17)]),
        ("Julius Yego",               [(0.03, None, 0, 0, 0), (0.97, 78.8, 2.3, 2.4, 0.17)]),
    ]),
]

print("\n=== Q2 (qid=30434) MEN'S JAVELIN ULTIMATE CHAMPIONSHIP (SEPT 8 EXACT 8-MAN FIELD) ===")
bmj = sim_javelin_mixture(men_jav_sep08)
print("FINAL MEN'S JAVELIN BLEND (ALL 8):")
for k, v in sorted(bmj.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")
top5_mj = sorted(bmj.items(), key=lambda x: -x[1])[:5]
print("Top-5:", [(k, round(v, 4)) for k, v in top5_mj], "sum =", round(sum(v for _, v in top5_mj), 4))


# ------------------------------------------------------------------------------
# MODEL 3: Q4 (qid=574485) — PSA WOMEN'S WORLD NO. 1 ON SEPT 21, 2026
# ------------------------------------------------------------------------------
# Exact facts as of Tuesday Sept 8, 2026:
#   - London Squash Classic 2026 (Gold, Sept 1-6):
#       * [1] Hania El Hammamy UPSET in SF 3-1 by [5] Georgina Kennedy (11-6, 14-12, 7-11, 11-8)!
#       * [2] Amina Orfi beat [3] Subramaniam 3-0 in SF & crushed Kennedy 3-0 (11-6, 11-8, 11-2) in Final
#         to defend her 1,800 title points!
#       * Post-London reports (Sept 6-7): El Hammamy STILL World No. 1 entering Qatar Classic,
#         Orfi CLOSED THE GAP and now has a direct chance to dethrone El Hammamy at Qatar Classic!
#   - QTerminals Qatar Classic 2026 (Platinum, Sept 12-18) is the ONLY tournament before Sept 21 rankings!
#       * Platinum points: W=2800, F=1820, SF=1120, QF=685, R16=410, R32=250.
#       * Top half ([1] El Hammamy): R1/R2 -> QF vs returning [6] Nouran Gohar -> SF vs [4] Olivia Weaver
#       * Bottom half ([2] Amina Orfi): R1/R2 -> QF vs [7] Fayrouz Aboelkheir -> SF vs [3] Nour El Sherbini
#   - CRITICAL 52-WEEK EXPIRY ON SEPT 21, 2026:
#       * 2025 CIB Egyptian Open (Diamond, Sept 12-19, 2025 -> added Sep 22, 2025 -> expires Mon Sep 21, 2026):
#         El Hammamy drops 3,100 pts vs Orfi drops 2,015 pts -> NET SWING = -1,085 RAW PTS against El Hammamy!
#       * With divisor ~11-12, that's roughly -90 to -100 AVERAGE POINTS against El Hammamy!
#
# Because we do not have the exact Sept 7 PSA table printed verbatim, we integrate over
# uncertainty in the exact Sept 7 average-points lead `L_sep7` (El Hammamy minus Orfi)
# AND divisor `D` (~11.5), conditional on El Hammamy still leading on Sept 7 (> 0)
# and the pre-London gap being <150 avg pts (closed by El Hammamy's London SF exit):
#   - Regime A (55%): Average-point drop in London worked as standard -> L_sep7 in [15, 70] avg pts
#                     (so after -92 avg pt Egyptian Open expiry, Orfi starts Sept 21 +22 to +77 avg pts AHEAD!)
#   - Regime B (30%): Smaller London drop or higher pre-London lead -> L_sep7 in [70, 125] avg pts
#                     (so after -92 avg pt expiry, basically DEAD EVEN: Orfi -33 to +22 avg pts!)
#   - Regime C (15%): Expiry timing / divisor nuance favors El Hammamy (e.g. smaller net expiry ~45 avg pts
#                     or L_sep7 ~130-160) -> El Hammamy enters Qatar +40 to +85 avg pts ahead after expiry.

def sim_squash_no1(n_trials=200000, seed=57448508):
    rng = random.Random(seed)
    # Qatar Classic Platinum points by round reached
    # Outcomes for each half independently (then Final H2H if both reach Final):
    # Top half (El Hammamy): [1] El Hammamy vs field, QF vs returning [6] Gohar, SF vs [4] Weaver
    #   Given London SF shock loss + Gohar QF + Weaver SF:
    #   P(lose R32/R16)=0.06, P(lose QF)=0.22, P(lose SF)=0.24, P(reach Final)=0.48
    # Bottom half (Orfi): [2] Orfi vs field, QF vs [7] Aboelkheir, SF vs [3] El Sherbini
    #   Given blazing London 3-0 form (reigning World & British Open champ):
    #   P(lose R32/R16)=0.04, P(lose QF)=0.14, P(lose SF)=0.26, P(reach Final)=0.56
    # Final win probs:
    #   - El Hammamy vs Orfi in Final: slight edge to Orfi on red-hot 2026 form (Worlds/British/London)
    #     vs El Hammamy's career H2H & 7 titles -> 50/50 (actually 0.52 Orfi, 0.48 El Hammamy)!
    #   - El Hammamy vs bottom-half winner (El Sherbini/other): 0.62 El Hammamy
    #   - Orfi vs top-half winner (Weaver/Gohar/other): 0.68 Orfi

    regimes = [
        ("R_A: Standard avg-pt drop (L_sep7 ~ 15..70, exp=-92)", 0.55, 15.0, 70.0, 92.0),
        ("R_B: Tight / Dead-even post-expiry (L_sep7 ~ 70..125, exp=-92)", 0.30, 70.0, 125.0, 92.0),
        ("R_C: Nuance favors Hammamy (net lead +35..+85 post-exp)", 0.15, 127.0, 177.0, 92.0),
    ]

    pts_map = {"R16": 410, "QF": 685, "SF": 1120, "F": 1820, "W": 2800}

    def sample_half(p_r16, p_qf, p_sf):
        u = rng.random()
        if u < p_r16:
            return "R16"
        elif u < p_r16 + p_qf:
            return "QF"
        elif u < p_r16 + p_qf + p_sf:
            return "SF"
        return "FIN"

    total_orfi = 0.0
    total_hamm = 0.0
    for rname, w, lo, hi, exp_hit in regimes:
        orfi_w = 0
        hamm_w = 0
        for _ in range(n_trials):
            l_sep7 = rng.uniform(lo, hi)
            div = rng.uniform(11.0, 12.5)
            h_res = sample_half(0.06, 0.22, 0.24)
            o_res = sample_half(0.04, 0.14, 0.26)

            if h_res == "FIN" and o_res == "FIN":
                if rng.random() < 0.52:
                    o_pts, h_pts = pts_map["W"], pts_map["F"]
                else:
                    o_pts, h_pts = pts_map["F"], pts_map["W"]
            elif h_res == "FIN":
                h_pts = pts_map["W"] if rng.random() < 0.62 else pts_map["F"]
                o_pts = pts_map[o_res]
            elif o_res == "FIN":
                o_pts = pts_map["W"] if rng.random() < 0.68 else pts_map["F"]
                h_pts = pts_map[h_res]
            else:
                h_pts = pts_map[h_res]
                o_pts = pts_map[o_res]

            # Net El Hammamy lead on Sept 21 (in avg pts):
            # L_sep21 = L_sep7 - exp_hit + (h_pts - o_pts) / div
            l_sep21 = l_sep7 - exp_hit + (h_pts - o_pts) / div
            if l_sep21 > 0:
                hamm_w += 1
            else:
                orfi_w += 1
        ph = hamm_w / n_trials
        po = orfi_w / n_trials
        print(f"  [{rname[:58]:58s} w={w:.2f}] Orfi:{po:.3f}, El Hammamy:{ph:.3f}")
        total_orfi += w * po
        total_hamm += w * ph

    # Reserve 0.005 for Nour El Sherbini / extreme tail
    print(f"FINAL SQUASH BLEND (raw): Amina Orfi={total_orfi:.4f}, Hania El Hammamy={total_hamm:.4f}")
    print(f"WITH 0.005 El Sherbini tail: Amina Orfi={total_orfi*0.995:.4f}, Hania El Hammamy={total_hamm*0.995:.4f}, Nour El Sherbini=0.0050")

print("\n=== Q4 (qid=574485) PSA WOMEN'S WORLD NO. 1 ON SEPT 21, 2026 ===")
sim_squash_no1()
