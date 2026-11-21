import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — FRIDAY AUG 28, 2026
# Batch: olympic_athletics_asian_games (30434, 2260, 409386)
# ==============================================================================

# ------------------------------------------------------------------------------
# PART 1: Q3 (qid=30434) — MEN'S JAVELIN, WORLD ATHLETICS ULTIMATE CHAMPIONSHIP
# Budapest, Sept 11-13, 2026 (T+16d)
# ------------------------------------------------------------------------------
# EXACT 8-MAN QUALIFICATION PICTURE (The Hindu & Outlook India, Aug 28, 2026):
#   Qualification period ends Sept 1; final eligibility list published Sept 6.
#   Only 8 athletes compete!
#     Auto #1: Arshad Nadeem (PAK, 2024 Olympic Champ) — 2026 SB only 78.63m (77.41m 9th CWG), skipped Lausanne & Zurich
#     Auto #2: Keshorn Walcott (TTO, 2025 World Champ) — 23 DL pts (#3), 83.71m Lausanne, 83.02m Zurich
#     Auto #3: Brussels DL Final winner (Sept 5) — almost surely already in top 7 unless Julius Yego wins Brussels
#     Road to Ultimate Top 6 (plus #8):
#       - Rumesh Tharanga Pathirage (SRI): 92.62m Rome WL/NR, 89.75m CWG Gold, 88.14m Lausanne win,
#         92.07m Zurich win (series: 81.50, 88.23, 89.90, 84.91, X, 92.07 WITH A HEADACHE!).
#         11 wins in 12 meets in 2026; 6 straight wins; 4th man in history with 2x 92m+!
#       - Julian Weber (GER): 90.40m CR at Birmingham Euros (Aug 15), ONLY other >90m in 2026;
#         HOWEVER, withdrew Lausanne (Aug 20), missed Zurich (Aug 27), Hindu (Aug 28):
#         "dogged by injury, he did not compete in any DL event and he will not be there in the Finals also."
#         -> High injury/DNS or compromised-form risk!
#       - Anderson Peters (GRN): 86.93m SB (2nd Zurich), 86.69m (3rd Lausanne), 35 DL pts (#2), 93.07m PB, 2x World Champ.
#       - Curtis Thompson (USA): 87.59m SB (Jul 25 NYC GP), 20 DL pts (#4), BUT 78.13m (6th Lausanne) & 80.31m (7th Zurich)!
#       - Neeraj Chopra (IND): #7 on Road to UC! Recovering from lower back injury since Sept 2025;
#         trending up: 85.69m Doha -> 85.83m CWG silver -> 88.05m SB Lausanne (9cm behind Pathirage!);
#         wisely skipped Zurich to manage health/workload for Brussels & Budapest! 90.23m PB, clutch champ.
#       - Sachin Yadav (IND): #8 on Road to UC (or Julius Yego / #9 replacement if someone skips).

def sim_javelin_mixture(regimes, n_trials_per_regime=120000, seed=20260828):
    rng = random.Random(seed)
    blend = Counter()
    per_regime = []
    for rname, weight, athletes in regimes:
        wins = Counter()
        for _ in range(n_trials_per_regime):
            best_m = -1.0
            winner = None
            for name, states in athletes:
                # Sample athlete state: (prob, base_throw_mu, day_sd, throw_sd, foul_rate)
                # If base_throw_mu is None -> DNS
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
        probs = {k: c / n_trials_per_regime for k, c in wins.items()}
        per_regime.append((rname, weight, probs))
        for k, v in probs.items():
            blend[k] += weight * v
    return blend, per_regime

# Calibration check: with 6 throws, foul_rate=0.16 (~5 valid throws), E[max_5] ≈ day_mu + 1.16 * throw_sd.
# For throw_sd=2.3 -> E[best] ≈ mu + 2.67m!
# E.g. Pathirage at mu=87.3 -> E[best] ≈ 90.0m (matches his 88.14 / 89.75 / 92.07 / 92.62 stretch: mean ~90.4m, slight regression from Zurich peak!)
# Weber healthy at mu=86.1 -> E[best] ≈ 88.8m (90.40m Euro peak, 91.51m PB)
# Chopra healthy at mu=85.4 -> E[best] ≈ 87.9m (88.05m Lausanne, clutch + 16d more recovery)
# Peters at mu=84.2 -> E[best] ≈ 87.1m (86.69m Lausanne, 86.93m Zurich, 93m ceiling -> wider sd)
# Walcott at mu=82.2 -> E[best] ≈ 85.0m (83.71m Lausanne, 83.02m Zurich, big-meet +1.5m upside)
# Thompson at mu=81.4 -> E[best] ≈ 84.3m (87.59m July vs 78.13/80.31m Aug -> huge state uncertainty)
# Nadeem at mu=80.0 (if starts) -> E[best] ≈ 83.0m (78.63m SB, 77.41m CWG; 50% DNS/skip for Asian Games)
# Spot #8 (Sachin Yadav / Yego / #9 sub): mu=81.0 -> E[best] ≈ 83.7m

jav_regimes = [
    ("R1: Base Calibrated (Pathirage 90m+ juggernaut, Weber 30% DNS / 25% hurt / 45% peak)", 0.50, [
        ("Rumesh Tharanga Pathirage", [(0.04, None, 0, 0, 0), (0.14, 85.4, 2.0, 2.3, 0.16), (0.82, 87.4, 2.0, 2.3, 0.16)]),
        ("Julian Weber",              [(0.30, None, 0, 0, 0), (0.25, 83.4, 2.2, 2.3, 0.16), (0.45, 86.2, 2.1, 2.3, 0.16)]),
        ("Neeraj Chopra",             [(0.06, None, 0, 0, 0), (0.22, 83.8, 1.8, 2.1, 0.15), (0.72, 85.6, 1.8, 2.1, 0.15)]),
        ("Anderson Peters",           [(0.04, None, 0, 0, 0), (0.96, 84.2, 2.3, 2.5, 0.17)]),
        ("Keshorn Walcott",           [(0.05, None, 0, 0, 0), (0.95, 82.3, 2.3, 2.4, 0.17)]),
        ("Curtis Thompson",           [(0.08, None, 0, 0, 0), (0.60, 79.8, 2.2, 2.4, 0.18), (0.32, 83.5, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.50, None, 0, 0, 0), (0.38, 78.5, 2.5, 2.5, 0.18), (0.12, 84.2, 2.8, 2.6, 0.17)]),
        ("Field_8th_Yadav_Yego_Sub",  [(0.00, None, 0, 0, 0), (1.00, 81.2, 2.2, 2.3, 0.17)]),
    ]),
    ("R2: Pathirage Workload Fatigue / Veterans Peak (Brussels->Budapest 7d wear, Chopra & Weber peak)", 0.25, [
        ("Rumesh Tharanga Pathirage", [(0.07, None, 0, 0, 0), (0.30, 85.0, 2.1, 2.3, 0.17), (0.63, 86.7, 2.1, 2.3, 0.16)]),
        ("Julian Weber",              [(0.18, None, 0, 0, 0), (0.22, 84.2, 2.1, 2.3, 0.16), (0.60, 86.6, 2.0, 2.3, 0.16)]),
        ("Neeraj Chopra",             [(0.05, None, 0, 0, 0), (0.15, 84.4, 1.8, 2.1, 0.15), (0.80, 86.2, 1.8, 2.1, 0.15)]),
        ("Anderson Peters",           [(0.04, None, 0, 0, 0), (0.96, 84.8, 2.4, 2.5, 0.17)]),
        ("Keshorn Walcott",           [(0.05, None, 0, 0, 0), (0.95, 83.0, 2.3, 2.4, 0.17)]),
        ("Curtis Thompson",           [(0.08, None, 0, 0, 0), (0.50, 80.2, 2.2, 2.4, 0.18), (0.42, 84.0, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.45, None, 0, 0, 0), (0.35, 79.5, 2.5, 2.5, 0.18), (0.20, 85.0, 2.8, 2.6, 0.17)]),
        ("Field_8th_Yadav_Yego_Sub",  [(0.00, None, 0, 0, 0), (1.00, 81.5, 2.2, 2.3, 0.17)]),
    ]),
    ("R3: Pathirage Historic Season Continues + Weber Truly Injured (50% DNS)", 0.25, [
        ("Rumesh Tharanga Pathirage", [(0.02, None, 0, 0, 0), (0.08, 86.0, 2.0, 2.3, 0.16), (0.90, 88.2, 1.9, 2.3, 0.16)]),
        ("Julian Weber",              [(0.50, None, 0, 0, 0), (0.25, 82.8, 2.2, 2.3, 0.16), (0.25, 85.8, 2.1, 2.3, 0.16)]),
        ("Neeraj Chopra",             [(0.08, None, 0, 0, 0), (0.30, 83.5, 1.9, 2.1, 0.15), (0.62, 85.3, 1.8, 2.1, 0.15)]),
        ("Anderson Peters",           [(0.04, None, 0, 0, 0), (0.96, 84.0, 2.3, 2.5, 0.17)]),
        ("Keshorn Walcott",           [(0.05, None, 0, 0, 0), (0.95, 82.0, 2.3, 2.4, 0.17)]),
        ("Curtis Thompson",           [(0.10, None, 0, 0, 0), (0.70, 79.5, 2.2, 2.4, 0.18), (0.20, 83.0, 2.3, 2.4, 0.17)]),
        ("Arshad Nadeem",             [(0.60, None, 0, 0, 0), (0.32, 78.0, 2.4, 2.5, 0.18), (0.08, 83.5, 2.7, 2.6, 0.17)]),
        ("Field_8th_Yadav_Yego_Sub",  [(0.00, None, 0, 0, 0), (1.00, 81.0, 2.2, 2.3, 0.17)]),
    ]),
]

j_blend, j_regs = sim_javelin_mixture(jav_regimes)
print("=== Q3 (qid=30434) MEN'S JAVELIN ULTIMATE CHAMPIONSHIP (BUDAPEST SEPT 13) ===")
for rname, w, probs in j_regs:
    top6 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:6])
    print(f"  [{rname[:58]:58s} w={w:.2f}] {top6}")
print("FINAL JAVELIN BLEND:")
for k, v in sorted(j_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:28s}: {v:.4f}")
top5_j = sorted([(k, v) for k, v in j_blend.items() if not k.startswith("Field_")], key=lambda x: -x[1])[:5]
print("Top-5 sum =", round(sum(v for _, v in top5_j), 4))


# ------------------------------------------------------------------------------
# PART 2: Q1 (qid=2260) — MEN'S ELITE RACE, 2026 SYDNEY MARATHON (Sun Aug 30 AEST)
# ------------------------------------------------------------------------------
# Model finish time in seconds on Sydney's brutal 320m climb (CR = 2:06:06 = 7566s;
# athletes targeting new CR ~ 2:05:15 - 2:05:45 = 7515-7545s).
# Each runner has: (p_start, expected_sydney_sec, form_sd_sec, blowup_prob, blowup_add_sec)
# Note: Marathons have heavy right tails (DNF/bonk/blowup) and ~75-110s day-to-day SD among elites!

def sim_marathon(regimes, n_trials_per_regime=120000, seed=2260):
    rng = random.Random(seed)
    blend = Counter()
    per_reg = []
    for rname, weight, runners in regimes:
        wins = Counter()
        for _ in range(n_trials_per_regime):
            best_t = 1e9
            winner = None
            for name, p_start, mu_s, sd_s, p_blow, blow_s in runners:
                if rng.random() > p_start:
                    continue
                t = rng.gauss(mu_s, sd_s)
                if rng.random() < p_blow:
                    t += rng.expovariate(1.0 / blow_s)
                if t < best_t:
                    best_t = t
                    winner = name
            wins[winner] += 1
        probs = {k: c / n_trials_per_regime for k, c in wins.items()}
        per_reg.append((rname, weight, probs))
        for k, v in probs.items():
            blend[k] += weight * v
    return blend, per_reg

# Men's field (~20 sub-2:06 + debutant Gebrhiwet):
#   Alphonce Simbu: 2:02:47 Boston '26 2nd, 2025 World Champ, Arusha hill-trained, confirmed on-site Aug 27 press conf!
#   Hailemaryam Kiros: Defending Sydney champ (2:06:06 CR), 2:03:42 4th Boston '26 on hills!
#   Sisay Lemma: 2:01:48 #8 all-time PB, Boston & London winner, BUT DNF'd Seoul Mar '26 (higher blowup/rust!)
#   Hagos Gebrhiwet: Debutant (12:36.73 5k #2 AT, 57:41 HM #4 AT), highlighted by RW Aug 27 & Canadian Running Aug 28;
#     missing from WA PB-only table -> mild ~15% scratch risk + ~28% debut blowup/hill risk, huge ceiling if he handles distance!
#   Timothy Kiplagat: 2:02:55 PB (2024 Tokyo 2nd), confirmed on WA list
#   Vincent Ngetich: 2:03:13 PB, 9th Tokyo '26 (2:05:21)
#   Tebello Ramakongoana: 3rd Sydney '25, 6th Boston '26 (2:04:18), proven hilly beast!
#   Gilbert Kibet: 3rd Seoul '26 (2:04:31)
#   Addisu Gobena: 2nd Sydney '25 (2:05:01), knows course
#   Dawit Wolde (2:03:48), Leul Gebresilase (2:04:02), Seifu Tura (2:04:29), Chimdesa Debele (2:04:44),
#   Enock Kinyamal (2:04:46), Chalu Deso (2:04:53), Kennedy Kimutai (2:04:56), Chala Regassa (2:05:06),
#   Ibrahim Hassan (2:05:20), Jemal Yimmer (2:05:48)

men_base = [
    # name, p_start, mu_sec, sd_sec, p_blow, blow_sec
    ("Alphonce Simbu",       0.98, 7560, 82, 0.12, 180),
    ("Hailemaryam Kiros",    0.97, 7590, 85, 0.14, 180),
    ("Sisay Lemma",          0.95, 7610, 98, 0.24, 240),
    ("Hagos Gebrhiwet",      0.84, 7605, 108, 0.28, 260),
    ("Timothy Kiplagat",     0.95, 7628, 92, 0.18, 200),
    ("Vincent Ngetich",      0.96, 7635, 90, 0.16, 190),
    ("Tebello Ramakongoana", 0.96, 7638, 88, 0.15, 190),
    ("Gilbert Kibet",        0.95, 7660, 92, 0.18, 200),
    ("Addisu Gobena",        0.95, 7665, 90, 0.17, 200),
    ("Dawit Wolde",          0.95, 7675, 95, 0.20, 210),
    ("Leul Gebresilase",     0.95, 7688, 95, 0.20, 210),
    ("Seifu Tura",           0.95, 7695, 95, 0.20, 210),
    ("Chimdesa Debele",      0.95, 7710, 95, 0.20, 210),
    ("Enock Kinyamal",       0.95, 7715, 95, 0.20, 210),
    ("Chalu Deso",           0.95, 7725, 95, 0.20, 210),
    ("Kennedy Kimutai",      0.95, 7730, 95, 0.20, 210),
    ("Chala Regassa",        0.95, 7740, 95, 0.20, 210),
    ("Ibrahim Hassan",       0.95, 7755, 95, 0.20, 210),
    ("Jemal Yimmer",         0.95, 7765, 95, 0.20, 210),
]

men_hills_tactical = [
    # Hilly/tactical race favors Simbu (World Champ kick + Arusha hills), Kiros (defending), Ramakongoana, Gobena; hurts debutant Gebrhiwet
    (nm, ps,
     mu - (18 if nm == "Alphonce Simbu" else 15 if nm == "Hailemaryam Kiros" else 15 if nm == "Tebello Ramakongoana" else 10 if nm == "Addisu Gobena" else -25 if nm == "Hagos Gebrhiwet" else 0),
     sd, pb, bs)
    for (nm, ps, mu, sd, pb, bs) in men_base
]

men_fast_speed = [
    # Fast CR attempt favors Lemma (2:01:48), Gebrhiwet (57:41 HM!), Kiplagat (2:02:55), Ngetich (2:03:13)
    (nm, (0.94 if nm == "Hagos Gebrhiwet" else ps),
     mu - (28 if nm == "Hagos Gebrhiwet" else 22 if nm == "Sisay Lemma" else 15 if nm == "Timothy Kiplagat" else 12 if nm == "Vincent Ngetich" else 0),
     sd, (0.20 if nm == "Hagos Gebrhiwet" else pb), bs)
    for (nm, ps, mu, sd, pb, bs) in men_base
]

m_blend, m_regs = sim_marathon([
    ("Base", 0.50, men_base),
    ("Hilly/Tactical", 0.28, men_hills_tactical),
    ("Fast CR Pace / Gebrhiwet Runs & Crushes", 0.22, men_fast_speed),
], seed=2260)

print("\n=== Q1 (qid=2260) MEN'S 2026 SYDNEY MARATHON ===")
for rname, w, probs in m_regs:
    top6 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:6])
    print(f"  [{rname:42s} w={w:.2f}] {top6}")
print("FINAL MEN'S SYDNEY BLEND:")
for k, v in sorted(m_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"  {k:24s}: {v:.4f}")
print("Top-5 sum =", round(sum(v for _, v in sorted(m_blend.items(), key=lambda x: -x[1])[:5]), 4))


# ------------------------------------------------------------------------------
# PART 3: Q2 (qid=409386) — WOMEN'S ELITE RACE, 2026 SYDNEY MARATHON (Sun Aug 30 AEST)
# ------------------------------------------------------------------------------
# World Athletics Aug 27 official Leading entries (21 women; Ruti Aga ABSENT):
#   Peres Jepchirchir (KEN) 2:14:43 — CONFIRMED ON-SITE at Thu Aug 27 Sydney press conf (SMH photo)!
#     Olympic/World/NYC/Boston/London champ; returning from spring stress fracture (missed London) -> mild rust/blowup risk!
#   Shure Demise (ETH) 2:18:34 — WA: "perhaps the most in-form athlete in the field" (won Apr '26 Paris >1m under CR w/ neg split)
#   Irine Cheptai (KEN) 2:17:51 — #2 PB, 6th Boston '26 (2:20:54)
#   Magdalena Shauri (TAN) 2:18:03 — #3 PB, 3rd Oct '25 Chicago NR
#   Stella Chesang (UGA) 2:18:26 — Jan '26 Osaka winner
#   Haven Hailu (ETH) 2:19:09 — Mar '26 Seoul winner
#   Vivian Cheruiyot (KEN) 2:18:31 — age 42 veteran
#   Sharon Chelimo (2:19:33), Joyce Tele (2:19:50), Meseret Abebaayahu (2:19:50), Aberu Ayana (2:20:20),
#   Waganesh Mekasha (2:20:26), Azmera Gebru (2:20:48), Jackline Cherono (2:21:14)

women_base = [
    # Sydney women's CR = 2:18:22 (8302s, Sifan Hassan 2025)
    # Jepchirchir: 98% starts; 20% stress-fracture rust/blowup (+260s exp), otherwise 8320s mean!
    ("Peres Jepchirchir",    0.98, 8325, 105, 0.22, 260),
    ("Shure Demise",         0.97, 8455, 105, 0.14, 210),
    ("Irine Cheptai",        0.97, 8465, 108, 0.15, 220),
    ("Magdalena Shauri",     0.96, 8490, 110, 0.16, 220),
    ("Stella Chesang",       0.96, 8500, 110, 0.16, 220),
    ("Haven Hailu",          0.96, 8525, 110, 0.16, 220),
    ("Vivian Cheruiyot",     0.95, 8580, 115, 0.20, 240),
    ("Sharon Chelimo",       0.95, 8605, 115, 0.18, 230),
    ("Joyce Tele",           0.95, 8625, 115, 0.18, 230),
    ("Meseret Abebaayahu",   0.95, 8630, 115, 0.18, 230),
    ("Aberu Ayana",          0.95, 8655, 115, 0.18, 230),
    ("Waganesh Mekasha",     0.95, 8665, 115, 0.18, 230),
    ("Azmera Gebru",         0.95, 8685, 115, 0.18, 230),
    ("Jackline Cherono",     0.95, 8710, 115, 0.18, 230),
]

women_jep_sharp = [
    (nm, ps, (8285 if nm == "Peres Jepchirchir" else mu), sd, (0.12 if nm == "Peres Jepchirchir" else pb), bs)
    for (nm, ps, mu, sd, pb, bs) in women_base
]

women_jep_rusty = [
    (nm, ps, (8430 if nm == "Peres Jepchirchir" else mu), sd, (0.34 if nm == "Peres Jepchirchir" else pb), bs)
    for (nm, ps, mu, sd, pb, bs) in women_base
]

w_blend, w_regs = sim_marathon([
    ("Base (Healthy on-site, moderate SF return risk)", 0.50, women_base),
    ("Jepchirchir Sharp (Classic tactical killer)", 0.25, women_jep_sharp),
    ("Jepchirchir Rusty (Under-trained post-SF)", 0.25, women_jep_rusty),
], seed=409386)

print("\n=== Q2 (qid=409386) WOMEN'S 2026 SYDNEY MARATHON ===")
for rname, w, probs in w_regs:
    top6 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(probs.items(), key=lambda x: -x[1])[:6])
    print(f"  [{rname:48s} w={w:.2f}] {top6}")
print("FINAL WOMEN'S SYDNEY BLEND:")
for k, v in sorted(w_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"  {k:24s}: {v:.4f}")
print("Top-5 sum =", round(sum(v for _, v in sorted(w_blend.items(), key=lambda x: -x[1])[:5]), 4))
