import random, math
from collections import Counter

def am_to_prob(odds):
    return (-odds / (-odds + 100.0)) if odds < 0 else (100.0 / (odds + 100.0))

def vig_free_probs(raw_probs):
    s = sum(raw_probs)
    prop = [p / s for p in raw_probs]
    lo, hi = 1.0, 2.5
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if sum(p**mid for p in raw_probs) > 1.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    pw = [p**k for p in raw_probs]
    mid_p = [0.5 * (a + b) for a, b in zip(prop, pw)]
    return prop, pw, mid_p, s - 1.0

def gamma_poisson(mu, shape=2.2):
    if mu <= 0:
        return 0
    lam = random.gammavariate(shape, mu / shape)
    L = math.exp(-lam)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1

# ============================================================
# 1. VERIFIED JULY 15 POST-SF2 MARKET BENCHMARKS (FINAL: ESP vs ARG)
# ============================================================
_, _, fd_fin, fd_vig = vig_free_probs([am_to_prob(-156), am_to_prob(+136)])
_, _, dk_fin, dk_vig = vig_free_probs([am_to_prob(-154), am_to_prob(+134)])
_, _, mgm_fin, mgm_vig = vig_free_probs([am_to_prob(-175), am_to_prob(+125)])
kalshi_fin = [0.580, 0.420]

print("=== POST-SF2 WORLD CUP FINAL MARKET ODDS (SPAIN vs ARGENTINA) ===")
print(f"  FanDuel (-156/+136, vig {fd_vig*100:.2f}%): Spain {fd_fin[0]:.4f} / Argentina {fd_fin[1]:.4f}")
print(f"  SI/DK   (-154/+134, vig {dk_vig*100:.2f}%): Spain {dk_fin[0]:.4f} / Argentina {dk_fin[1]:.4f}")
print(f"  BetMGM  (-175/+125, vig {mgm_vig*100:.2f}%): Spain {mgm_fin[0]:.4f} / Argentina {mgm_fin[1]:.4f}")
print(f"  Kalshi  (58%/42%)              : Spain {kalshi_fin[0]:.4f} / Argentina {kalshi_fin[1]:.4f}")
mkt_fin_esp = 0.35 * fd_fin[0] + 0.30 * dk_fin[0] + 0.15 * mgm_fin[0] + 0.20 * kalshi_fin[0]
print(f"  Weighted Market Consensus      : Spain {mkt_fin_esp:.4f} / Argentina {1-mkt_fin_esp:.4f}\n")

# ============================================================
# 2. COUPLED POST-SF2 MONTE CARLO SIMULATION (4-MODEL ENSEMBLE)
#    MATCH 103 (Jul 18, Miami): France vs England (3rd-Place Playoff)
#    MATCH 104 (Jul 19, NJ):    Spain vs Argentina (World Cup Final)
#
#    VERIFIED EXACT POST-SF2 GOLDEN BOOT STANDINGS (1 match left each!):
#      1. Lionel Messi (ARG)     : 8g, 4a, 698m  [Final vs Spain]
#      2. Kylian Mbappé (FRA)    : 8g, 3a, 653m  [3P vs England]
#      3. Erling Haaland (NOR)   : 7g, 0a        [ELIMINATED]
#      4. Jude Bellingham (ENG)  : 6g, 1a, 664m  [3P vs France]
#      5. Harry Kane (ENG)       : 6g, 1a, 717m  [3P vs France]
#      6. Ousmane Dembélé (FRA)  : 5g, 2a, 582m  [3P vs England]
#      7. Mikel Oyarzabal (ESP)  : 5g, 1a, 600m  [Final vs Argentina]
#
#    IMPORTANT MINUTES NOTE:
#      - Mbappe starts with 45 FEWER minutes than Messi (653m vs 698m)!
#      - So if both finish tied on GOALS AND ASSISTS (e.g. 8g/4a if Mbappe gets +1a,
#        or 9g/4a if both score 1g and Mbappe gets +1a), Mbappe wins on fewer minutes
#        unless Mbappe plays 120m ET AND Messi plays 90m (653+120=773 vs 698+90=788 ->
#        EVEN THEN Mbappe has 15 fewer minutes!!). So Mbappe ALWAYS wins exact (G, A) ties!
#      - Conversely, Messi starts AHEAD on assists (4a vs 3a)! So whenever both finish
#        with the same number of goals AND Mbappe does NOT out-assist Messi by >=1,
#        MESSI wins the tiebreaker!
# ============================================================

def run_post_sf2_sim(label,
                     p_esp_fin_base=0.592,
                     p_fra_3p_base=0.580,
                     p_fin_et=0.33,
                     p_3p_et=0.24,
                     # Expected goals in their SINGLE remaining match (baseline before match-outcome correlation):
                     ms_mu_fin=0.42,   # Messi vs Spain (Spain allowed 1 goal in 7 games, U2.5 -170, ARG ~1.02 xG incl. ET)
                     mb_mu_3p=0.76,    # Mbappe vs England in open 3P (FRA ~1.85 xG incl. ET, Mbappe on pens & GB chase)
                     kn_mu_3p=0.68,    # Kane vs France in 3P
                     bl_mu_3p=0.46,    # Bellingham vs France in 3P
                     dm_mu_3p=0.52,    # Dembele vs England in 3P
                     oy_mu_fin=0.46,   # Oyarzabal vs Argentina in Final (Spain pen taker)
                     # Assist rates in remaining match:
                     ms_a_fin=0.25,
                     mb_a_3p=0.30,
                     # Rest / rotation / DNP probabilities in 3rd-place playoff:
                     mb_3p_dnp=0.10,
                     kn_3p_dnp=0.18,
                     bl_3p_dnp=0.18,
                     dm_3p_dnp=0.15,
                     shape=2.1,
                     # Golden Ball structural params:
                     # Conditional on Spain winning Final:
                     p_esp_gb_if_esp_and_ms_boot=0.45,  # Spain wins Final, Messi wins Golden Boot
                     p_esp_gb_if_esp_and_mb_boot=0.61,  # Spain wins Final, Mbappe wins Golden Boot
                     p_fra_gb_if_esp_and_mb_boot=0.09,  # 2010 Forlan / 1990 Schillaci 3P Golden Boot path for Mbappe
                     # Conditional on Argentina winning Final:
                     p_arg_gb_if_arg_win=0.955,
                     ms_share_of_arg=0.955,
                     spain_shares=None,
                     N=250000, seed=20260715):
    random.seed(seed)
    if spain_shares is None:
        spain_shares = [
            ("Rodri",           0.37),
            ("Lamine Yamal",    0.35),
            ("Mikel Oyarzabal", 0.13),
            ("Fabián Ruiz",     0.075),
            ("Unai Simón",      0.035),
            ("Other_ESP",       0.040),
        ]

    champ_cnt = Counter()
    tp_cnt = Counter()
    gb_cnt = Counter()
    gb_tie_cnt = Counter()
    gball_cnt = Counter()
    gball_team_cnt = Counter()

    for _ in range(N):
        # 1. Final: Spain vs Argentina (epistemic uncertainty around base prob)
        p_esp = min(0.85, max(0.30, p_esp_fin_base + random.gauss(0, 0.03)))
        esp_won = (random.random() < p_esp)
        fin_et = (random.random() < p_fin_et)
        champ = "Spain" if esp_won else "Argentina"
        champ_cnt[champ] += 1

        # 2. Third-Place Playoff: France vs England
        p_fra = min(0.85, max(0.30, p_fra_3p_base + random.gauss(0, 0.04)))
        fra_won = (random.random() < p_fra)
        tp_et = (random.random() < p_3p_et)
        tp_w = "France" if fra_won else "England"
        tp_cnt[tp_w] += 1

        # Match-outcome & ET scoring multipliers (correlated!)
        et_fin_mult = 1.24 if fin_et else 0.92
        et_3p_mult  = 1.22 if tp_et else 0.94
        arg_m = (1.36 if not esp_won else 0.75) * et_fin_mult
        esp_m = (1.24 if esp_won else 0.68) * et_fin_mult
        fra_m = (1.22 if fra_won else 0.74) * et_3p_mult
        eng_m = (1.24 if not fra_won else 0.76) * et_3p_mult

        # 3. GOLDEN BOOT (1 game left!)
        # Messi (8g, 4a, 698m) - Final vs Spain (~98.5% starts)
        if random.random() > 0.015:
            ms_g = 8 + gamma_poisson(ms_mu_fin * arg_m, shape)
            ms_a = 4 + gamma_poisson(ms_a_fin * arg_m, 3.0)
            ms_m = 698 + (120 if fin_et else 90)
        else:
            ms_g, ms_a, ms_m = 8, 4, 698

        # Oyarzabal (5g, 1a, 600m) - Final vs Argentina
        if random.random() > 0.03:
            oy_g = 5 + gamma_poisson(oy_mu_fin * esp_m, shape)
            oy_a = 1 + gamma_poisson(0.16 * esp_m, 3.0)
            oy_m = 600 + (105 if fin_et else 82)
        else:
            oy_g, oy_a, oy_m = 5, 1, 600

        # Mbappe (8g, 3a, 653m) - 3P vs England
        u_mb = random.random()
        if u_mb > mb_3p_dnp:
            # 20% chance of early sub/reduced minutes (~60 min) when playing 3P
            mins_factor = 0.72 if random.random() < 0.20 else 1.00
            mb_g = 8 + gamma_poisson(mb_mu_3p * fra_m * mins_factor, shape)
            mb_a = 3 + gamma_poisson(mb_a_3p * fra_m * mins_factor, 3.0)
            mb_m = 653 + int((115 if tp_et else 90) * mins_factor)
        else:
            mb_g, mb_a, mb_m = 8, 3, 653

        # Dembele (5g, 2a, 582m) - 3P vs England
        if random.random() > dm_3p_dnp:
            dm_g = 5 + gamma_poisson(dm_mu_3p * fra_m, shape)
            dm_a = 2 + gamma_poisson(0.25 * fra_m, 3.0)
            dm_m = 582 + 80
        else:
            dm_g, dm_a, dm_m = 5, 2, 582

        # Kane (6g, 1a, 717m) - 3P vs France
        if random.random() > kn_3p_dnp:
            kn_mins = 0.72 if random.random() < 0.25 else 1.00
            kn_g = 6 + gamma_poisson(kn_mu_3p * eng_m * kn_mins, shape)
            kn_a = 1 + gamma_poisson(0.18 * eng_m * kn_mins, 3.0)
            kn_m = 717 + int(90 * kn_mins)
        else:
            kn_g, kn_a, kn_m = 6, 1, 717

        # Bellingham (6g, 1a, 664m) - 3P vs France
        if random.random() > bl_3p_dnp:
            bl_mins = 0.72 if random.random() < 0.25 else 1.00
            bl_g = 6 + gamma_poisson(bl_mu_3p * eng_m * bl_mins, shape)
            bl_a = 1 + gamma_poisson(0.22 * eng_m * bl_mins, 3.0)
            bl_m = 664 + int(90 * bl_mins)
        else:
            bl_g, bl_a, bl_m = 6, 1, 664

        cands = [
            ("Lionel Messi",    (ms_g, ms_a, -ms_m)),
            ("Kylian Mbappé",   (mb_g, mb_a, -mb_m)),
            ("Harry Kane",      (kn_g, kn_a, -kn_m)),
            ("Jude Bellingham", (bl_g, bl_a, -bl_m)),
            ("Ousmane Dembélé", (dm_g, dm_a, -dm_m)),
            ("Mikel Oyarzabal", (oy_g, oy_a, -oy_m)),
        ]
        best_gb = max(cands, key=lambda x: x[1])[0]
        gb_cnt[best_gb] += 1
        if ms_g == mb_g and best_gb in ("Lionel Messi", "Kylian Mbappé"):
            gb_tie_cnt[best_gb] += 1

        # 4. GOLDEN BALL (Coupled to Champion & Golden Boot!)
        r = random.random()
        if not esp_won:
            # Argentina wins Final -> Messi is an overwhelming lock!
            p_arg = p_arg_gb_if_arg_win
            p_esp_gb = 0.035 if best_gb != "Kylian Mbappé" else 0.025
            p_fra_gb = max(0.005, 1.0 - p_arg - p_esp_gb)
            if r < p_arg:
                gb_team = "Argentina"
            elif r < p_arg + p_esp_gb:
                gb_team = "Spain"
            else:
                gb_team = "France"
        else:
            # Spain wins Final!
            if best_gb == "Lionel Messi":
                p_esp_gb = p_esp_gb_if_esp_and_ms_boot
                p_fra_gb = 0.015
                p_eng_gb = 0.005
                p_arg_gb = 1.0 - p_esp_gb - p_fra_gb - p_eng_gb
            elif best_gb == "Kylian Mbappé":
                p_esp_gb = p_esp_gb_if_esp_and_mb_boot
                p_fra_gb = p_fra_gb_if_esp_and_mb_boot
                p_eng_gb = 0.008
                p_arg_gb = max(0.10, 1.0 - p_esp_gb - p_fra_gb - p_eng_gb)
            else:
                # Kane / Bellingham / Oyarzabal / Dembele won Golden Boot!
                p_esp_gb = 0.65 if best_gb == "Mikel Oyarzabal" else 0.54
                p_fra_gb = 0.05 if best_gb == "Ousmane Dembélé" else 0.02
                p_eng_gb = 0.16 if best_gb in ("Harry Kane", "Jude Bellingham") else 0.005
                p_arg_gb = max(0.10, 1.0 - p_esp_gb - p_fra_gb - p_eng_gb)
            tot = p_esp_gb + p_arg_gb + p_fra_gb + p_eng_gb
            p_esp_gb /= tot; p_arg_gb /= tot; p_fra_gb /= tot; p_eng_gb /= tot
            if r < p_esp_gb: gb_team = "Spain"
            elif r < p_esp_gb + p_arg_gb: gb_team = "Argentina"
            elif r < p_esp_gb + p_arg_gb + p_fra_gb: gb_team = "France"
            else: gb_team = "England"

        gball_team_cnt[gb_team] += 1
        if gb_team == "Argentina":
            if random.random() < ms_share_of_arg:
                winner = "Lionel Messi"
            else:
                winner = random.choice(["Enzo Fernández", "Lautaro Martínez", "Julián Álvarez"])
        elif gb_team == "Spain":
            shares = list(spain_shares)
            # If Oyarzabal scored 2+ in Final, boost his share!
            if oy_g >= 7:
                adj = [(pl, sh * (2.6 if pl == "Mikel Oyarzabal" else 0.78)) for pl, sh in shares]
                st = sum(x[1] for x in adj)
                shares = [(pl, sh / st) for pl, sh in adj]
            u = random.random(); cum = 0.0; winner = shares[-1][0]
            for pl, sh in shares:
                cum += sh
                if u <= cum:
                    winner = pl; break
        elif gb_team == "France":
            winner = "Kylian Mbappé" if random.random() < 0.88 else "Ousmane Dembélé"
        else:
            winner = "Jude Bellingham" if random.random() < 0.60 else "Harry Kane"

        gball_cnt[winner] += 1

    out = {
        "Champion":   {k: c/N for k, c in champ_cnt.most_common()},
        "ThirdPlace": {k: c/N for k, c in tp_cnt.most_common()},
        "GOLDEN_BOOT":{k: c/N for k, c in gb_cnt.most_common(6)},
        "GOLDEN_BALL":{k: c/N for k, c in gball_cnt.most_common(10)},
        "GBALL_TEAM": {k: c/N for k, c in gball_team_cnt.most_common()},
    }
    print(f"=== {label} ===")
    print("  Champion   :", ", ".join(f"{k}:{v:.4f}" for k, v in out["Champion"].items()))
    print("  ThirdPlace :", ", ".join(f"{k}:{v:.4f}" for k, c in tp_cnt.most_common() for v in [c/N]))
    print("  GOLDEN_BOOT:", ", ".join(f"{k}:{v:.4f}" for k, v in out["GOLDEN_BOOT"].items()))
    print(f"  GB Ties    : Messi {gb_tie_cnt['Lionel Messi']/N:.3f}, Mbappe {gb_tie_cnt['Kylian Mbappé']/N:.3f}")
    print("  GBALL_TEAM :", ", ".join(f"{k}:{v:.4f}" for k, v in out["GBALL_TEAM"].items()))
    print("  GOLDEN_BALL:", ", ".join(f"{k}:{v:.4f}" for k, v in list(out["GOLDEN_BALL"].items())[:7]))
    print()
    return out

# 4-MODEL ENSEMBLE:
# Model 1 (40%): Market-Anchored Balanced
m1 = run_post_sf2_sim(
    "M1: MARKET-ANCHORED BALANCED (40%)",
    p_esp_fin_base=0.591, p_fra_3p_base=0.580,
    ms_mu_fin=0.43, mb_mu_3p=0.76, kn_mu_3p=0.68, bl_mu_3p=0.46, dm_mu_3p=0.52, oy_mu_fin=0.46,
    mb_3p_dnp=0.10, kn_3p_dnp=0.18, bl_3p_dnp=0.18,
    p_esp_gb_if_esp_and_ms_boot=0.45, p_esp_gb_if_esp_and_mb_boot=0.61, p_fra_gb_if_esp_and_mb_boot=0.09,
    spain_shares=[("Rodri", 0.37), ("Lamine Yamal", 0.35), ("Mikel Oyarzabal", 0.13), ("Fabián Ruiz", 0.075), ("Unai Simón", 0.035), ("Other_ESP", 0.040)],
    N=250000, seed=101
)

# Model 2 (25%): Spain Defensive Dominance & TSG Rodri Reward (Spain shuts Messi down, rewards Champion!)
m2 = run_post_sf2_sim(
    "M2: SPAIN DOMINANCE + TSG RODRI (25%)",
    p_esp_fin_base=0.605, p_fra_3p_base=0.592,
    ms_mu_fin=0.36, mb_mu_3p=0.74, kn_mu_3p=0.62, bl_mu_3p=0.42, dm_mu_3p=0.50, oy_mu_fin=0.48,
    mb_3p_dnp=0.14, kn_3p_dnp=0.22, bl_3p_dnp=0.22,
    p_esp_gb_if_esp_and_ms_boot=0.55, p_esp_gb_if_esp_and_mb_boot=0.70, p_fra_gb_if_esp_and_mb_boot=0.08,
    spain_shares=[("Rodri", 0.43), ("Lamine Yamal", 0.30), ("Mikel Oyarzabal", 0.12), ("Fabián Ruiz", 0.075), ("Unai Simón", 0.040), ("Other_ESP", 0.035)],
    N=250000, seed=202
)

# Model 3 (25%): Messi Halo / 2014 Runner-Up & Passing-of-Torch Yamal + High-Scoring 3P Mbappe
m3 = run_post_sf2_sim(
    "M3: MESSI HALO + YAMAL TORCH + OPEN 3P (25%)",
    p_esp_fin_base=0.580, p_fra_3p_base=0.572,
    ms_mu_fin=0.47, mb_mu_3p=0.82, kn_mu_3p=0.72, bl_mu_3p=0.50, dm_mu_3p=0.56, oy_mu_fin=0.44,
    mb_3p_dnp=0.07, kn_3p_dnp=0.14, bl_3p_dnp=0.14,
    p_esp_gb_if_esp_and_ms_boot=0.35, p_esp_gb_if_esp_and_mb_boot=0.50, p_fra_gb_if_esp_and_mb_boot=0.11,
    spain_shares=[("Lamine Yamal", 0.42), ("Rodri", 0.30), ("Mikel Oyarzabal", 0.13), ("Fabián Ruiz", 0.070), ("Unai Simón", 0.035), ("Other_ESP", 0.045)],
    N=250000, seed=303
)

# Model 4 (10%): High-Variance / Heavy 3P Rotation (Mbappe more likely rested/subbed; tighter 3P)
m4 = run_post_sf2_sim(
    "M4: HIGH-VAR / 3P ROTATION (10%)",
    p_esp_fin_base=0.585, p_fra_3p_base=0.560,
    ms_mu_fin=0.42, mb_mu_3p=0.68, kn_mu_3p=0.66, bl_mu_3p=0.46, dm_mu_3p=0.48, oy_mu_fin=0.44,
    mb_3p_dnp=0.20, kn_3p_dnp=0.24, bl_3p_dnp=0.24, shape=1.8,
    p_esp_gb_if_esp_and_ms_boot=0.44, p_esp_gb_if_esp_and_mb_boot=0.58, p_fra_gb_if_esp_and_mb_boot=0.09,
    spain_shares=[("Rodri", 0.36), ("Lamine Yamal", 0.36), ("Mikel Oyarzabal", 0.13), ("Fabián Ruiz", 0.075), ("Unai Simón", 0.035), ("Other_ESP", 0.040)],
    N=250000, seed=404
)

wts = [(m1, 0.40), (m2, 0.25), (m3, 0.25), (m4, 0.10)]
print("================ JULY 15 POST-SF2 WEIGHTED ENSEMBLE ================")
for key in ["Champion", "ThirdPlace", "GOLDEN_BOOT", "GBALL_TEAM", "GOLDEN_BALL"]:
    agg = Counter()
    for m, w in wts:
        for k, v in m[key].items():
            agg[k] += w * v
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in agg.most_common(8)))
