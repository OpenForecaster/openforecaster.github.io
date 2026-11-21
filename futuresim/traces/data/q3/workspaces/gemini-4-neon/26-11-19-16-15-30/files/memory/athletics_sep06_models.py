import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — SUNDAY SEPT 6, 2026 (Batch: athletics)
# Q1: qid=936021 — Men's 5,000m, World Athletics Ultimate Championship (Sep 11, T+5d)
# Q2: qid=30434  — Men's Javelin, World Athletics Ultimate Championship (Sep 13, T+7d)
# ==============================================================================

# ------------------------------------------------------------------------------
# MODEL 1: Q1 (qid=936021) — MEN'S 5,000m ULTIMATE CHAMPIONSHIP (12-MAN FINAL)
# ------------------------------------------------------------------------------
# Key Sept 4-5 Brussels Diamond League Final signals:
#   - Fri Sep 4 Men's 1,500m: Cam Myers 3:30.14, Koech 3:30.18, Strand 3:30.50,
#     Jakob Ingebrigtsen 4th in 3:30.52 SB (beat Hocker, legs 'definitely improving',
#     confirmed doubling 5k+1500m, reigning Olympic & 2026 Euro 5k champ).
#     Cole Hocker faded to 7th/8th in 3:30.80 (won Zurich 1500m Aug 27; reigning
#     2025 World 5k champ; ~8% scratch/skip-5k risk + minor sickness/fatigue question).
#   - Sat Sep 5 Men's 5,000m DL Final:
#     1. Birhanu Balew (BRN) 12:45.70 WL/AR (53.4 last lap! AUTO-QUALIFIED to Budapest!)
#     2. Egide Ntakarutimana (BDI) 12:46.73 NR
#     3. Cornelius Kemboi (KEN) 12:47.29 PR
#     4. Biniam Mehary (ETH) 12:47.78 (led 3k in 7:41.98!)
#     5. Graham Blanks (USA) 12:47.98 PR (2nd with 300m left!)
#     6. Nico Young (USA) 12:48.12
#     7. Jacob Krop (KEN) 12:51.23
#     8. Dominic Lobalu (SUI) 12:56.07
#     9. Grant Fisher (USA) 12:59.10 (DROPPED >1 mile out! Huge negative form signal!)
#   - Fresh top-ranked European contenders who skipped Brussels 5k:
#     Andreas Almgren (SWE: 12:48.61 Oslo, 27:23.44 Euro 10k CR)
#     Jimmy Gressier (FRA: World #1 5k ranking, 2025 World 10k Gold & 5k Bronze)
#
# Mechanics of a 12-man pacemaker-free championship 5,000m final:
#   Race unfolds in one of 3 tactical pace regimes:
#     - Slow/Tactical sit-and-kick (45%): 13:05-13:20 -> favors 1,500m closers
#       (Hocker, Ingebrigtsen) and strong kickers (Gressier, Balew, Almgren, Young/Blanks).
#     - Medium/Honest wind-up (35%): 12:52-13:05 -> Ingebrigtsen long drive from 1200m
#       or Balew/Almgren/Mehary grinding pace; Hocker still dangerous if he hangs on.
#     - Fast/Burn-up (20%): <12:52 -> favors pure 5k strength + kick (Balew, Almgren,
#       Ingebrigtsen, Mehary, Ntakarutimana, Blanks, Young, Yihune); hurts Hocker slightly.
#   We model each runner with:
#     (p_start_in_12, tactical_mu, honest_mu, fast_mu, race_sd)
#     where higher score = stronger winning performance (think Gumbel/Normal race rating,
#     calibrated so sd=1.0 -> +1.0 rating advantage over a single rival = ~76% H2H win).

def sim_5000m(regimes, n_trials=200000, seed=936021):
    rng = random.Random(seed)
    blend = Counter()
    for rname, weight, pace_probs, athletes in regimes:
        wins = Counter()
        for _ in range(n_trials):
            # Draw pace scenario: 0=tactical, 1=honest, 2=fast
            up = rng.random()
            if up < pace_probs[0]:
                pace = 0
            elif up < pace_probs[0] + pace_probs[1]:
                pace = 1
            else:
                pace = 2

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

# Rating calibration (higher is better, race_sd ~ 1.0):
#   ~2.0 = elite world favorite in optimal pace
#   ~1.2-1.6 = top-tier contender
#   ~0.6-1.1 = strong 12:46-12:50 finalist
#   ~0.0-0.5 = back-half finalist / out-of-form star
regimes_5000m = [
    # R1 (55%): Base calibrated (Day-1 fresh 5k; Ingebrigtsen slight edge over Hocker;
    #           Balew strong #3 with modest 6-day 12:45 fatigue discount)
    ("R1: Base Calibrated (Ingebrigtsen/Hocker/Balew)", 0.55, (0.45, 0.35, 0.20), [
        # Jakob Ingebrigtsen: 96% starts (confirmed), bimodal recovery (25% still lacking final gear, 75% sharp 5k form)
        ("Jakob Ingebrigtsen", 0.96, [
            (0.25, (1.15, 1.55, 1.45), 0.95),
            (0.75, (1.75, 2.15, 1.95), 0.95),
        ]),
        # Cole Hocker: 90% starts (10% scratch/1500m-only/illness after Brussels fade), bimodal (25% off/sick, 75% lethal kick)
        ("Cole Hocker", 0.90, [
            (0.25, (1.20, 0.90, 0.50), 0.95),
            (0.75, (2.25, 1.85, 1.35), 0.95),
        ]),
        # Birhanu Balew: 91% starts (auto DL champ, 9% DNS/AG), bimodal (25% 6-day 12:45 fatigue, 75% 12:45+53.4 peak)
        ("Birhanu Balew", 0.91, [
            (0.25, (0.90, 1.00, 1.15), 0.95),
            (0.75, (1.45, 1.65, 1.95), 0.95),
        ]),
        # Andreas Almgren: 93% in field & starts (fresh!), elite 12:48 + Euro 10k CR + 3:32 speed
        ("Andreas Almgren", 0.93, [
            (1.00, (1.15, 1.45, 1.50), 0.95),
        ]),
        # Jimmy Gressier: 95% in field & starts (World #1, fresh!), tactical closer
        ("Jimmy Gressier", 0.95, [
            (1.00, (1.30, 1.15, 0.95), 0.95),
        ]),
        # Biniam Mehary: 70% in 12-man field (ran 12:47.78 Brussels, 6d fatigue)
        ("Biniam Mehary", 0.70, [
            (1.00, (0.90, 1.25, 1.45), 1.00),
        ]),
        # Nico Young: 78% in 12-man field (12:48.12 Brussels, 6d fatigue)
        ("Nico Young", 0.78, [
            (1.00, (1.00, 1.10, 1.20), 0.95),
        ]),
        # Graham Blanks: 68% in 12-man field (12:47.98 PR Brussels, 6d fatigue)
        ("Graham Blanks", 0.68, [
            (1.00, (1.05, 1.15, 1.20), 0.95),
        ]),
        # Egide Ntakarutimana: 55% in 12-man field (12:46.73 NR Brussels, 6d fatigue)
        ("Egide Ntakarutimana", 0.55, [
            (1.00, (0.90, 1.15, 1.35), 0.95),
        ]),
        # Addisu Yihune / top fresh Ethiopian (12:47.62 earlier WL, didn't run Brussels!)
        ("Field_Yihune_ETH", 0.80, [
            (1.00, (0.95, 1.25, 1.45), 1.00),
        ]),
        # Grant Fisher: 88% in field, severely downgraded after 12:59.10 Brussels collapse (dropped >1 mile out!)
        ("Grant Fisher", 0.88, [
            (0.70, (0.25, 0.20, 0.05), 0.95),
            (0.30, (0.95, 1.00, 0.90), 0.95),
        ]),
        # Remaining 2-3 finalists (Lobalu, Kemboi, Kimeli, Wolfe, Mills, Gebrhiwet)
        ("Field_Pack_A", 0.95, [(1.00, (0.95, 1.00, 1.05), 1.00)]),
        ("Field_Pack_B", 0.95, [(1.00, (0.80, 0.90, 0.95), 1.00)]),
    ]),

    # R2 (25%): Tactical sit-and-kick favors Hocker/Ingebrigtsen; Brussels 5k runners slightly flat from 6-day turnaround
    ("R2: Slow Tactical / Brussels 6d Fatigue", 0.25, (0.65, 0.25, 0.10), [
        ("Jakob Ingebrigtsen", 0.96, [(0.20, (1.25, 1.60, 1.50), 0.95), (0.80, (1.85, 2.20, 2.00), 0.95)]),
        ("Cole Hocker",        0.92, [(0.20, (1.30, 1.00, 0.60), 0.95), (0.80, (2.35, 1.95, 1.45), 0.95)]),
        ("Birhanu Balew",      0.90, [(0.40, (0.75, 0.85, 1.00), 0.95), (0.60, (1.35, 1.55, 1.85), 0.95)]),
        ("Andreas Almgren",    0.93, [(1.00, (1.20, 1.45, 1.50), 0.95)]),
        ("Jimmy Gressier",     0.95, [(1.00, (1.40, 1.25, 1.00), 0.95)]),
        ("Biniam Mehary",      0.70, [(1.00, (0.75, 1.05, 1.25), 1.00)]),
        ("Nico Young",         0.78, [(1.00, (0.85, 0.95, 1.05), 0.95)]),
        ("Graham Blanks",      0.68, [(1.00, (0.90, 1.00, 1.05), 0.95)]),
        ("Egide Ntakarutimana",0.55, [(1.00, (0.75, 1.00, 1.20), 0.95)]),
        ("Field_Yihune_ETH",   0.80, [(1.00, (0.95, 1.25, 1.40), 1.00)]),
        ("Grant Fisher",       0.88, [(0.75, (0.20, 0.15, 0.00), 0.95), (0.25, (0.90, 0.95, 0.85), 0.95)]),
        ("Field_Pack_A",       0.95, [(1.00, (0.90, 0.95, 0.95), 1.00)]),
        ("Field_Pack_B",       0.95, [(1.00, (0.75, 0.85, 0.85), 1.00)]),
    ]),

    # R3 (20%): Honest/Fast 5,000m + Doublers (Ingebrigtsen/Hocker) vulnerable to 5k specialists
    ("R3: Fast Race / 5k Specialists Dominate", 0.20, (0.20, 0.40, 0.40), [
        ("Jakob Ingebrigtsen", 0.95, [(0.35, (1.05, 1.40, 1.35), 0.95), (0.65, (1.60, 1.95, 1.85), 0.95)]),
        ("Cole Hocker",        0.85, [(0.35, (1.05, 0.75, 0.35), 0.95), (0.65, (2.05, 1.65, 1.15), 0.95)]),
        ("Birhanu Balew",      0.93, [(0.15, (1.05, 1.20, 1.35), 0.95), (0.85, (1.60, 1.85, 2.15), 0.95)]),
        ("Andreas Almgren",    0.93, [(1.00, (1.20, 1.55, 1.65), 0.95)]),
        ("Jimmy Gressier",     0.95, [(1.00, (1.25, 1.20, 1.05), 0.95)]),
        ("Biniam Mehary",      0.70, [(1.00, (1.00, 1.40, 1.65), 1.00)]),
        ("Nico Young",         0.78, [(1.00, (1.05, 1.20, 1.35), 0.95)]),
        ("Graham Blanks",      0.68, [(1.00, (1.10, 1.25, 1.35), 0.95)]),
        ("Egide Ntakarutimana",0.55, [(1.00, (1.00, 1.30, 1.55), 0.95)]),
        ("Field_Yihune_ETH",   0.80, [(1.00, (1.00, 1.35, 1.55), 1.00)]),
        ("Grant Fisher",       0.88, [(0.75, (0.20, 0.15, 0.00), 0.95), (0.25, (0.90, 0.95, 0.90), 0.95)]),
        ("Field_Pack_A",       0.95, [(1.00, (0.95, 1.05, 1.15), 1.00)]),
        ("Field_Pack_B",       0.95, [(1.00, (0.80, 0.95, 1.05), 1.00)]),
    ]),
]

print("=== Q1 (qid=936021) MEN'S 5,000m ULTIMATE CHAMPIONSHIP (SEPT 6 UPDATE) ===")
b5k = sim_5000m(regimes_5000m)
print("FINAL 5,000m BLEND:")
for k, v in sorted(b5k.items(), key=lambda x: -x[1]):
    print(f"  {k:26s}: {v:.4f}")
top5_5k = sorted([(k, v) for k, v in b5k.items() if not k.startswith("Field_")], key=lambda x: -x[1])[:5]
print("Top-5:", [(k, round(v, 4)) for k, v in top5_5k], "sum =", round(sum(v for _, v in top5_5k), 4))


# ------------------------------------------------------------------------------
# MODEL 2: Q2 (qid=30434) — MEN'S JAVELIN ULTIMATE CHAMPIONSHIP (8-MAN FINAL)
# ------------------------------------------------------------------------------
# Key Sept 5 Brussels Diamond League Final signals:
#   - 1. Rumesh Tharanga Pathirage (SRI): 89.04m (Rd 3) in cold 16C weather!
#        12/13 wins in 2026 (7 straight!): 92.62, 88.68, 89.75, 88.14, 92.07, 89.04!
#        SURVIVED BRUSSELS 100% HEALTHY -> DNS risk drops to ~2.5-3%!
#   - 2. Dawid Wegner (POL): 87.47m PB! Huge surge! Uncertain if inside final 8-man
#        Budapest startlist (est ~50% starts via #8 ranking or Weber/Nadeem/Thompson withdrawal).
#   - 3. Keshorn Walcott (TTO): 83.99m (beat Peters! Auto World Champ, steady 83-84m).
#   - 4. Anderson Peters (GRN): 83.70m (down slightly from 86.93m Zurich, cold weather).
#   - 5. Julius Yego (KEN): 76.79m (poor form).
#   - 7. Curtis Thompson (USA): 69.52m (total collapse: 78.13 -> 80.31 -> 69.52! Injured/broken).
#   - Julian Weber (GER): Still absent from DL (Lausanne/Zurich/Brussels) due to injury,
#        but threw 90.40m CR Aug 15 -> bimodal (~38% DNS, ~25% hurt, ~37% healthy peak).
#   - Arshad Nadeem (PAK): Auto Olympic Champ (92.97m PB), training in Potchefstroom
#        specifically targeting Budapest & Asian Games, but 77.41m/78.63m CWG injury cloud!
#   - Neeraj Chopra (IND): OFFICIALLY OUT FOR SEASON. Sachin Yadav (IND) moves up to #7.

def sim_javelin_mixture(regimes, n_trials=200000, seed=30434):
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

# Reminder: with dsd=2.0, tsd=2.3, foul_rate=0.16 over 6 throws, E[best6] ≈ mu + 2.7m!
# So Pathirage mu=87.6 -> E[best6] ≈ 90.3m (matches 92.62, 88.68, 89.75, 88.14, 92.07, 89.04!).
men_jav_sep06 = [
    ("R1: Base Calibrated (Pathirage healthy 90.3m; Weber 38% DNS)", 0.55, [
        ("Rumesh Tharanga Pathirage", [(0.025, None, 0, 0, 0), (0.125, 85.6, 2.0, 2.3, 0.16), (0.85, 87.7, 2.0, 2.3, 0.16)]),
        ("Julian Weber",              [(0.38,  None, 0, 0, 0), (0.25,  83.2, 2.2, 2.3, 0.16), (0.37, 86.2, 2.1, 2.3, 0.16)]),
        ("Anderson Peters",           [(0.03,  None, 0, 0, 0), (0.97,  83.9, 2.4, 2.5, 0.17)]),
        ("Keshorn Walcott",           [(0.04,  None, 0, 0, 0), (0.96,  82.4, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.42,  None, 0, 0, 0), (0.40,  79.2, 2.5, 2.5, 0.18), (0.18, 84.8, 2.7, 2.6, 0.17)]),
        ("Dawid Wegner",              [(0.48,  None, 0, 0, 0), (0.52,  82.5, 2.3, 2.4, 0.17)]),
        ("Sachin Yadav",              [(0.05,  None, 0, 0, 0), (0.95,  81.4, 2.1, 2.3, 0.16)]),
        ("Curtis Thompson",           [(0.25,  None, 0, 0, 0), (0.65,  76.0, 2.8, 2.5, 0.20), (0.10, 82.8, 2.4, 2.4, 0.17)]),
        ("Field_Alt_Vadlejch_Yego",   [(0.50,  None, 0, 0, 0), (0.50,  80.8, 2.4, 2.4, 0.17)]),
    ]),
    ("R2: Pathirage Workload Dip + Weber/Peters/Nadeem Peak", 0.25, [
        ("Rumesh Tharanga Pathirage", [(0.04,  None, 0, 0, 0), (0.26,  85.2, 2.1, 2.3, 0.17), (0.70, 87.0, 2.1, 2.3, 0.16)]),
        ("Julian Weber",              [(0.22,  None, 0, 0, 0), (0.23,  84.0, 2.1, 2.3, 0.16), (0.55, 86.6, 2.0, 2.3, 0.16)]),
        ("Anderson Peters",           [(0.03,  None, 0, 0, 0), (0.97,  84.7, 2.4, 2.5, 0.17)]),
        ("Keshorn Walcott",           [(0.04,  None, 0, 0, 0), (0.96,  82.9, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.35,  None, 0, 0, 0), (0.38,  80.0, 2.5, 2.5, 0.18), (0.27, 85.4, 2.7, 2.6, 0.17)]),
        ("Dawid Wegner",              [(0.45,  None, 0, 0, 0), (0.55,  83.0, 2.3, 2.4, 0.17)]),
        ("Sachin Yadav",              [(0.05,  None, 0, 0, 0), (0.95,  81.6, 2.1, 2.3, 0.16)]),
        ("Curtis Thompson",           [(0.25,  None, 0, 0, 0), (0.60,  76.5, 2.8, 2.5, 0.20), (0.15, 83.2, 2.4, 2.4, 0.17)]),
        ("Field_Alt_Vadlejch_Yego",   [(0.50,  None, 0, 0, 0), (0.50,  81.2, 2.4, 2.4, 0.17)]),
    ]),
    ("R3: Pathirage Unstoppable (91m+) + Weber Truly Injured (55% DNS)", 0.20, [
        ("Rumesh Tharanga Pathirage", [(0.015, None, 0, 0, 0), (0.085, 86.2, 1.9, 2.3, 0.16), (0.90, 88.2, 1.9, 2.3, 0.16)]),
        ("Julian Weber",              [(0.55,  None, 0, 0, 0), (0.25,  82.6, 2.2, 2.3, 0.16), (0.20, 85.6, 2.1, 2.3, 0.16)]),
        ("Anderson Peters",           [(0.03,  None, 0, 0, 0), (0.97,  83.6, 2.3, 2.5, 0.17)]),
        ("Keshorn Walcott",           [(0.04,  None, 0, 0, 0), (0.96,  82.1, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.55,  None, 0, 0, 0), (0.35,  78.5, 2.4, 2.5, 0.18), (0.10, 84.0, 2.7, 2.6, 0.17)]),
        ("Dawid Wegner",              [(0.52,  None, 0, 0, 0), (0.48,  82.2, 2.2, 2.4, 0.17)]),
        ("Sachin Yadav",              [(0.05,  None, 0, 0, 0), (0.95,  81.2, 2.1, 2.3, 0.16)]),
        ("Curtis Thompson",           [(0.30,  None, 0, 0, 0), (0.65,  75.5, 2.8, 2.5, 0.20), (0.05, 82.0, 2.4, 2.4, 0.17)]),
        ("Field_Alt_Vadlejch_Yego",   [(0.50,  None, 0, 0, 0), (0.50,  80.5, 2.3, 2.4, 0.17)]),
    ]),
]

print("\n=== Q2 (qid=30434) MEN'S JAVELIN ULTIMATE CHAMPIONSHIP (SEPT 6 UPDATE) ===")
bmj = sim_javelin_mixture(men_jav_sep06)
print("FINAL MEN'S JAVELIN BLEND:")
for k, v in sorted(bmj.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")
top5_mj = sorted([(k, v) for k, v in bmj.items() if not k.startswith("Field_")], key=lambda x: -x[1])[:5]
print("Top-5:", [(k, round(v, 4)) for k, v in top5_mj], "sum =", round(sum(v for _, v in top5_mj), 4))
