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

def gamma_poisson(mu, shape=2.0):
    if mu <= 0: return 0
    lam = random.gammavariate(shape, mu / shape)
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

# Market benchmark: POST-SF1 SI.com Champion odds (July 14 evening)
_, _, md_si, _ = vig_free_probs([am_to_prob(-155), am_to_prob(+290), am_to_prob(+370)])
champ_mkt_si = {"Spain": md_si[0], "England": md_si[1], "Argentina": md_si[2]}

def run_post_sf1_sim(label, elo_base,
                     eng_sf2_p=0.533,
                     esp_rest_elo=14.0,
                     fra_rest_elo=10.0,
                     scale_fin=410.0,
                     scale_3p=445.0,
                     sigma=36.0,
                     # Calibrated to PRE-SF1 FanDuel/BetMGM/Caesars consensus!
                     mb_mu=0.75, ms_mu=0.72, kn_mu=0.74, bl_mu=0.58, dm_mu=0.55, oy_mu=0.45,
                     mb_3p_miss=0.22, ms_3p_miss=0.12, other_3p_miss=0.16,
                     shape=2.0,
                     esp_vs_arg_esp_gb=0.51,
                     esp_vs_eng_esp_gb=0.63,
                     spain_shares=None,
                     N=250000, seed=20260714):
    random.seed(seed)
    if spain_shares is None:
        spain_shares = [
            ("Lamine Yamal",    0.37),
            ("Rodri",           0.32),
            ("Mikel Oyarzabal", 0.12),
            ("Fabián Ruiz",     0.085),
            ("Unai Simón",      0.045),
            ("Other_ESP",       0.060),
        ]
    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.91), ("Julián Álvarez", 0.045), ("Other_ARG", 0.045)],
        "England":   [("Jude Bellingham", 0.66), ("Harry Kane", 0.26), ("Other_ENG", 0.08)],
        "France":    [("Kylian Mbappé", 0.85), ("Michael Olise", 0.08), ("Ousmane Dembélé", 0.04), ("Other_FRA", 0.03)],
        "Spain":     spain_shares,
    }

    counts = {k: Counter() for k in ["SF2", "Champion", "ThirdPlace"]}
    gb_wins = Counter()
    gb_tie = Counter()
    gball_wins = Counter()
    gball_team_wins = Counter()

    opp_def_map = {"Spain": 0.72, "France": 0.90, "England": 0.94, "Argentina": 1.06}

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in elo_base.items()}

        # 1. SF2: England vs Argentina
        elo_diff_sf2 = (ELO["England"] - ELO["Argentina"]) - (elo_base["England"] - elo_base["Argentina"])
        logit0 = math.log(eng_sf2_p / (1.0 - eng_sf2_p))
        p_eng_sf2 = 1.0 / (1.0 + math.exp(-(logit0 + elo_diff_sf2 * math.log(10) / 405.0)))
        eng_won_sf2 = (random.random() < p_eng_sf2)
        sf2_w, sf2_l = ("England", "Argentina") if eng_won_sf2 else ("Argentina", "England")
        counts["SF2"][sf2_w] += 1

        # 2. Final: Spain vs sf2_w
        p_esp_fin = 1.0 / (1.0 + 10.0 ** (-((ELO["Spain"] + esp_rest_elo) - ELO[sf2_w]) / scale_fin))
        esp_won_fin = (random.random() < p_esp_fin)
        champ, runner_up = ("Spain", sf2_w) if esp_won_fin else (sf2_w, "Spain")
        counts["Champion"][champ] += 1

        # 3. Third-Place Playoff: France vs sf2_l (Miami Gardens — slight crowd edge if Argentina)
        crowd_mod = -8.0 if sf2_l == "Argentina" else 0.0
        p_fra_3p = 1.0 / (1.0 + 10.0 ** (-((ELO["France"] + fra_rest_elo + crowd_mod) - ELO[sf2_l]) / scale_3p))
        fra_won_3p = (random.random() < p_fra_3p)
        third_w, fourth_l = ("France", sf2_l) if fra_won_3p else (sf2_l, "France")
        counts["ThirdPlace"][third_w] += 1

        # 4. GOLDEN BOOT (EXACT POST-SF1 STATS: Mbappe 8g/3a/653m [1g left], Messi 8g/2a/608m [2g],
        #    Kane 6g/1a/627m [2g], Bellingham 6g/1a/574m [2g], Oyarzabal 5g/1a/600m [1g], Dembele 5g/2a/582m [1g])
        # Correlate scoring with match outcomes!
        eng_sf2_m = 1.24 if eng_won_sf2 else 0.72
        arg_sf2_m = 0.72 if eng_won_sf2 else 1.28
        esp_fin_m = 1.25 if esp_won_fin else 0.68
        opp_fin_m = 0.68 if esp_won_fin else 1.32
        fra_3p_m  = 1.20 if fra_won_3p  else 0.75
        opp_3p_m  = 0.75 if fra_won_3p  else 1.25

        # Mbappe (1 game: 3P vs sf2_l)
        if random.random() > mb_3p_miss:
            mb_g = 8 + gamma_poisson(mb_mu * opp_def_map[sf2_l] * 1.25 * fra_3p_m, shape)
            mb_a = 3 + gamma_poisson(0.28 * 1.25 * fra_3p_m, 3.0)
            mb_m = 653 + (78 if random.random() < 0.35 else 90)
        else:
            mb_g, mb_a, mb_m = 8, 3, 653

        # Dembele (1 game: 3P vs sf2_l)
        if random.random() > other_3p_miss:
            dm_g = 5 + gamma_poisson(dm_mu * opp_def_map[sf2_l] * 1.25 * fra_3p_m, shape)
            dm_a = 2 + gamma_poisson(0.25 * 1.25 * fra_3p_m, 3.0)
            dm_m = 582 + 80
        else:
            dm_g, dm_a, dm_m = 5, 2, 582

        # Oyarzabal (1 game: FIN vs sf2_w)
        if random.random() > 0.02:
            oy_g = 5 + gamma_poisson(oy_mu * opp_def_map[sf2_w] * 0.92 * esp_fin_m, shape)
            oy_a = 1 + gamma_poisson(0.15 * 0.92 * esp_fin_m, 3.0)
            oy_m = 600 + 85
        else:
            oy_g, oy_a, oy_m = 5, 1, 600

        # Messi (2 games: SF2 vs ENG + FIN vs ESP or 3P vs FRA)
        ms_g = 8 + gamma_poisson(ms_mu * 0.94 * 0.96 * arg_sf2_m, shape)
        ms_a = 2 + gamma_poisson(0.30 * arg_sf2_m, 3.0)
        ms_m = 608 + 90
        if not eng_won_sf2: # Argentina in Final vs Spain
            if random.random() > 0.02:
                ms_g += gamma_poisson(ms_mu * opp_def_map["Spain"] * 0.92 * opp_fin_m, shape)
                ms_a += gamma_poisson(0.30 * 0.92 * opp_fin_m, 3.0)
                ms_m += 90
        else: # Argentina in 3P vs France
            if random.random() > ms_3p_miss:
                ms_g += gamma_poisson(ms_mu * opp_def_map["France"] * 1.25 * opp_3p_m, shape)
                ms_a += gamma_poisson(0.30 * 1.25 * opp_3p_m, 3.0)
                ms_m += (80 if random.random() < 0.35 else 90)

        # Kane (2 games: SF2 vs ARG + FIN vs ESP or 3P vs FRA)
        kn_g = 6 + gamma_poisson(kn_mu * 1.06 * 0.96 * eng_sf2_m, shape)
        kn_a = 1 + gamma_poisson(0.18 * eng_sf2_m, 3.0)
        kn_m = 627 + 90
        if eng_won_sf2: # England in Final vs Spain
            if random.random() > 0.02:
                kn_g += gamma_poisson(kn_mu * opp_def_map["Spain"] * 0.92 * opp_fin_m, shape)
                kn_a += gamma_poisson(0.18 * 0.92 * opp_fin_m, 3.0)
                kn_m += 90
        else: # England in 3P vs France
            if random.random() > other_3p_miss:
                kn_g += gamma_poisson(kn_mu * opp_def_map["France"] * 1.25 * opp_3p_m, shape)
                kn_a += gamma_poisson(0.18 * 1.25 * opp_3p_m, 3.0)
                kn_m += 82

        # Bellingham (2 games: SF2 vs ARG + FIN vs ESP or 3P vs FRA)
        bl_g = 6 + gamma_poisson(bl_mu * 1.06 * 0.96 * eng_sf2_m, shape)
        bl_a = 1 + gamma_poisson(0.22 * eng_sf2_m, 3.0)
        bl_m = 574 + 90
        if eng_won_sf2:
            if random.random() > 0.02:
                bl_g += gamma_poisson(bl_mu * opp_def_map["Spain"] * 0.92 * opp_fin_m, shape)
                bl_a += gamma_poisson(0.22 * 0.92 * opp_fin_m, 3.0)
                bl_m += 90
        else:
            if random.random() > other_3p_miss:
                bl_g += gamma_poisson(bl_mu * opp_def_map["France"] * 1.25 * opp_3p_m, shape)
                bl_a += gamma_poisson(0.22 * 1.25 * opp_3p_m, 3.0)
                bl_m += 82

        cands = [
            ("Kylian Mbappé",   (mb_g, mb_a, -mb_m)),
            ("Lionel Messi",    (ms_g, ms_a, -ms_m)),
            ("Harry Kane",      (kn_g, kn_a, -kn_m)),
            ("Jude Bellingham", (bl_g, bl_a, -bl_m)),
            ("Ousmane Dembélé", (dm_g, dm_a, -dm_m)),
            ("Mikel Oyarzabal", (oy_g, oy_a, -oy_m)),
        ]
        best_gb = max(cands, key=lambda x: x[1])[0]
        gb_wins[best_gb] += 1
        if mb_g == ms_g and best_gb in ("Kylian Mbappé", "Lionel Messi"):
            gb_tie[best_gb] += 1

        # 5. GOLDEN BALL
        r = random.random()
        mb_won_gb = (best_gb == "Kylian Mbappé")
        ms_won_gb = (best_gb == "Lionel Messi")
        kn_won_gb = (best_gb == "Harry Kane")
        bl_won_gb = (best_gb == "Jude Bellingham")

        if champ == "Spain" and runner_up == "Argentina":
            p_esp = esp_vs_arg_esp_gb * (0.86 if ms_won_gb else 1.07)
            p_fra = (0.14 if mb_won_gb else 0.025)
            p_arg = max(0.06, 1.0 - p_esp - p_fra)
            tot = p_esp + p_arg + p_fra
            p_esp /= tot; p_arg /= tot; p_fra /= tot
            if r < p_esp: gb_team = "Spain"
            elif r < p_esp + p_arg: gb_team = "Argentina"
            else: gb_team = "France"
        elif champ == "Spain" and runner_up == "England":
            p_esp = esp_vs_eng_esp_gb * (0.85 if (kn_won_gb or bl_won_gb) else 1.03)
            p_fra = (0.18 if mb_won_gb else 0.03)
            p_arg = (0.09 if ms_won_gb else 0.015)
            p_eng = max(0.08, 1.0 - p_esp - p_fra - p_arg)
            tot = p_esp + p_eng + p_fra + p_arg
            p_esp /= tot; p_eng /= tot; p_fra /= tot; p_arg /= tot
            if r < p_esp: gb_team = "Spain"
            elif r < p_esp + p_eng: gb_team = "England"
            elif r < p_esp + p_eng + p_fra: gb_team = "France"
            else: gb_team = "Argentina"
        elif champ == "Argentina":
            p_arg = 0.91 if ms_won_gb else 0.84
            p_esp = 0.07 if ms_won_gb else 0.11
            p_fra = 1.0 - p_arg - p_esp
            if r < p_arg: gb_team = "Argentina"
            elif r < p_arg + p_esp: gb_team = "Spain"
            else: gb_team = "France"
        else:
            p_eng = 0.89 if (bl_won_gb or kn_won_gb) else 0.81
            p_esp = 0.07 if (bl_won_gb or kn_won_gb) else 0.12
            p_fra = (0.06 if mb_won_gb else 0.02)
            p_arg = (0.04 if ms_won_gb else 0.01)
            tot = p_eng + p_esp + p_fra + p_arg
            p_eng /= tot; p_esp /= tot; p_fra /= tot; p_arg /= tot
            if r < p_eng: gb_team = "England"
            elif r < p_eng + p_esp: gb_team = "Spain"
            elif r < p_eng + p_esp + p_fra: gb_team = "France"
            else: gb_team = "Argentina"

        gball_team_wins[gb_team] += 1
        shares = list(TEAM_SHARES[gb_team])
        if any(pl == best_gb for pl, _ in shares):
            adj = [(pl, sh * (2.30 if pl == best_gb else 0.70)) for pl, sh in shares]
            st = sum(x[1] for x in adj)
            shares = [(pl, sh / st) for pl, sh in adj]
        u = random.random(); cum = 0.0
        for pl, sh in shares:
            cum += sh
            if u <= cum:
                gball_wins[pl] += 1
                break

    out = {}
    for k in ["SF2", "Champion", "ThirdPlace"]:
        out[k] = {t: c/N for t, c in counts[k].most_common(6)}
    out["GOLDEN_BOOT"] = {n: c/N for n, c in gb_wins.most_common(8)}
    out["GOLDEN_BALL"] = {n: c/N for n, c in gball_wins.most_common(12)}
    out["GBALL_TEAM"]  = {n: c/N for n, c in gball_team_wins.most_common(6)}
    print(f"\n==================== {label} ====================")
    print("  SF2        :", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF2"].items()))
    print("  Champion   :", ", ".join(f"{k}:{v:.4f}" for k, v in out["Champion"].items()))
    print("  ThirdPlace :", ", ".join(f"{k}:{v:.4f}" for k, v in out["ThirdPlace"].items()))
    print("  GOLDEN_BOOT:", ", ".join(f"{k}:{v:.4f}" for k, v in out["GOLDEN_BOOT"].items()))
    print(f"  Tiebreaks  : {dict(gb_tie)} (tie rate={(gb_tie['Kylian Mbappé']+gb_tie['Lionel Messi'])/N:.3f})")
    print("  GBALL_TEAM :", ", ".join(f"{k}:{v:.4f}" for k, v in out["GBALL_TEAM"].items()))
    print("  GOLDEN_BALL:", ", ".join(f"{k}:{v:.4f}" for k, v in list(out["GOLDEN_BALL"].items())[:8]))
    return out

m1 = run_post_sf1_sim(
    "1. MARKET-CALIBRATED (45%)",
    elo_base={"Spain": 2164, "France": 2160, "England": 2122, "Argentina": 2096},
    eng_sf2_p=0.534, esp_rest_elo=14.0, fra_rest_elo=10.0,
    mb_mu=0.75, ms_mu=0.72, kn_mu=0.74, bl_mu=0.58, mb_3p_miss=0.22, ms_3p_miss=0.12, shape=2.0,
    esp_vs_arg_esp_gb=0.51, esp_vs_eng_esp_gb=0.63,
    spain_shares=[("Lamine Yamal", 0.37), ("Rodri", 0.32), ("Mikel Oyarzabal", 0.12), ("Fabián Ruiz", 0.085), ("Unai Simón", 0.045), ("Other_ESP", 0.060)],
    N=250000, seed=101
)

m2 = run_post_sf1_sim(
    "2. SPAIN DOMINANT + TSG RODRI (25%)",
    elo_base={"Spain": 2178, "France": 2158, "England": 2120, "Argentina": 2094},
    eng_sf2_p=0.530, esp_rest_elo=18.0, fra_rest_elo=12.0,
    mb_mu=0.74, ms_mu=0.70, kn_mu=0.72, bl_mu=0.56, mb_3p_miss=0.28, ms_3p_miss=0.14, shape=2.0,
    esp_vs_arg_esp_gb=0.57, esp_vs_eng_esp_gb=0.69,
    spain_shares=[("Rodri", 0.38), ("Lamine Yamal", 0.32), ("Mikel Oyarzabal", 0.115), ("Fabián Ruiz", 0.085), ("Unai Simón", 0.045), ("Other_ESP", 0.055)],
    N=250000, seed=202
)

m3 = run_post_sf1_sim(
    "3. STAR-HALO / 2010 COLLECTIVE-SPLIT (20%)",
    elo_base={"Spain": 2156, "France": 2156, "England": 2122, "Argentina": 2100},
    eng_sf2_p=0.528, esp_rest_elo=12.0, fra_rest_elo=8.0,
    mb_mu=0.80, ms_mu=0.70, kn_mu=0.74, bl_mu=0.58, mb_3p_miss=0.14, ms_3p_miss=0.10, shape=2.2,
    esp_vs_arg_esp_gb=0.42, esp_vs_eng_esp_gb=0.54,
    spain_shares=[("Lamine Yamal", 0.43), ("Rodri", 0.25), ("Mikel Oyarzabal", 0.13), ("Fabián Ruiz", 0.08), ("Unai Simón", 0.04), ("Other_ESP", 0.07)],
    N=250000, seed=303
)

m4 = run_post_sf1_sim(
    "4. CONSERVATIVE / HIGH-VAR (10%)",
    elo_base={"Spain": 2154, "France": 2148, "England": 2118, "Argentina": 2098},
    eng_sf2_p=0.530, esp_rest_elo=10.0, fra_rest_elo=6.0,
    scale_fin=430.0, scale_3p=470.0,
    mb_mu=0.72, ms_mu=0.68, kn_mu=0.76, bl_mu=0.60, mb_3p_miss=0.25, ms_3p_miss=0.14, shape=1.8,
    esp_vs_arg_esp_gb=0.47, esp_vs_eng_esp_gb=0.59,
    spain_shares=[("Lamine Yamal", 0.36), ("Rodri", 0.30), ("Mikel Oyarzabal", 0.13), ("Fabián Ruiz", 0.09), ("Unai Simón", 0.05), ("Other_ESP", 0.07)],
    N=250000, seed=404
)

wts = [(m1, 0.45), (m2, 0.25), (m3, 0.20), (m4, 0.10)]
print("\n==================== JULY 14 POST-SF1 WEIGHTED ENSEMBLE ====================")
ens = {}
for key in ["SF2", "Champion", "ThirdPlace", "GOLDEN_BOOT", "GOLDEN_BALL", "GBALL_TEAM"]:
    agg = Counter()
    for m, w in wts:
        for k, v in m[key].items():
            agg[k] += w * v
    ens[key] = dict(agg)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in agg.most_common(8)))

print("\n=== CHAMPION FINAL BLEND (55% SI POST-SF1 MKT / 45% ENSEMBLE) ===")
ch_blend = {t: 0.55 * champ_mkt_si[t] + 0.45 * ens["Champion"][t] for t in ["Spain", "England", "Argentina"]}
print("  SI Mkt :", {k: round(v, 4) for k, v in champ_mkt_si.items()})
print("  Ens    :", {k: round(v, 4) for k, v in ens["Champion"].items()})
print("  Blend  :", {k: round(v, 4) for k, v in ch_blend.items()})
