import random, math
from collections import Counter

# ==============================================================================
# JULY 10, 2026 WORLD CUP SIMULATION v2 — JOINTLY CALIBRATED TO ALL 4 HARD MARKETS!
#
# Hard July 10 Market Targets:
# 1. SF1 France vs Spain (SI.com opening -144/+118): FRA 56.3%-56.7% / ESP 43.3%-43.7%
# 2. Post-QF2 Outrights (DK foxillinois +150/+310/+430/+470/+1600/+4000, AND Kalshi pre-QF2 Bayesian):
#    - DK Post-QF2 mid (50% prop / 50% pow): FRA 37.3%, ESP 22.4%, ARG 17.2%, ENG 15.9%, NOR 5.2%, SUI 2.1%
#    - Kalshi pre-QF2 Bayesian (conditioned on ESP beating BEL):
#      Wait: Kalshi pre-QF2 was FRA 39.6%, ARG 18.2%, ESP 16.8%, ENG 15.3%, NOR 6.2%, BEL 2.1%, SUI 1.9%.
#      Conditional on ESP beating BEL (~74.5%): ESP -> 16.8/0.745 = 22.5%, FRA trims ~39.6 -> 37.6%,
#      ARG ~18.0%, ENG ~15.1%, NOR ~5.0-5.8%, SUI ~1.8%!
#    - Consensus Market Champion: FRA 37.5%, ESP 22.5%, ARG 17.6%, ENG 15.5%, NOR 5.2%, SUI 1.8%
# 3. QF3 ENG-NOR (Kalshi 64.4%, DK 65.2-66.3%): ~64.8% ENG / 35.2% NOR
# 4. QF4 ARG-SUI (Kalshi 73.3%, DK 72.0-73.7%): ~73.2% ARG / 26.8% SUI
# ==============================================================================

# 1. MARKET-CALIBRATED ELO (jointly matches SF1 ~57/43, Champion ~37.5/22.5/17.6/15.5/5.2/1.8, QF3 ~64.8%, QF4 ~73.2%!)
ELO_MARKET = {
    "France": 2194,       # Strongest team vs bottom half (~65% in Final -> 0.573 * 0.65 = 37.2% Champion!)
    "Spain": 2138,        # ~42.7% vs FRA, ~53.5% vs bottom half -> 0.427 * 0.535 = 22.8% Champion!
    "Argentina": 2124,    # Respects DK +430 / Kalshi +441 (~17.5% Champion!)
    "England": 2116,      # Respects DK +470 / Kalshi +545 (~15.2% Champion!)
    "Norway": 2001,       # Matches QF3 ~64.8% ENG / 35.2% NOR and NOR ~4.9% Champion!
    "Switzerland": 1972,  # Matches QF4 ~73.2% ARG / 26.8% SUI (with Manzambi OUT) and SUI ~2.2% Champion!
}

# 2. BALANCED BAYESIAN + MARKET BLEND (slightly more credit to Spain's 37-match unbeaten defense)
ELO_BALANCED = {
    "France": 2190,
    "Spain": 2140,
    "Argentina": 2112,
    "England": 2098,
    "Norway": 1986,
    "Switzerland": 1962,
}

# 3. PURE BAYESIAN / SPAIN-H2H FORM (Spain 37 unbeaten, beat FRA in Euro 2024 SF & UNL 2025 SF)
ELO_BAYESIAN = {
    "France": 2178,
    "Spain": 2146,
    "Argentina": 2104,
    "England": 2082,
    "Norway": 1976,
    "Switzerland": 1952,
}

# 4. UPSET-CONSERVATIVE
ELO_CONSERVATIVE = {
    "France": 2180,
    "Spain": 2134,
    "Argentina": 2098,
    "England": 2084,
    "Norway": 1986,
    "Switzerland": 1962,
}

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=405.0, sigma=40.0,
            fra_sf1_net=2.5,       # +5 extra rest day (Jul 9 vs Jul 10) - 2.5 minor Mbappe ankle/Tchouameni caution
            eng_qf_pen=-8,         # Quansah ban (-5) + Guehi hamstring / Rice bug uncertainty (-3)
            eng_sf_pen=-7,         # Quansah 2nd match ban (-3) + yellow-card tightrope (-4)
            arg_kc_crowd=6,
            sui_fatigue_qf=-9,
            sui_inj_qf=-11,        # Manzambi 100% RULED OUT + Aebischer/Jaquez unlikely
            sui_inj_late=-6,
            messi_gpg=0.66, mbappe_gpg=0.88, haaland_gpg=0.92, kane_gpg=0.73,
            mbappe_sf_miss=0.035,
            tp_rot_miss=0.08,
            win_goal_ratio=1.72,
            N=200000, seed=20260710):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"
    ]}
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    players = [
        ("Kylian Mbappé", "France", 8, 3, mbappe_gpg, 0.28, 512),
        ("Lionel Messi", "Argentina", 8, 1, messi_gpg, 0.22, 435),
        ("Erling Haaland", "Norway", 7, 0, haaland_gpg, 0.08, 355),
        ("Harry Kane", "England", 6, 1, kane_gpg, 0.17, 435),
        ("Ousmane Dembélé", "France", 5, 2, 0.47, 0.28, 510),
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.46, 0.18, 495),
        ("Jude Bellingham", "England", 4, 1, 0.38, 0.22, 390),
        ("Johan Manzambi", "Switzerland", 3, 2, 0.30, 0.14, 340),
        ("Julián Álvarez", "Argentina", 2, 1, 0.44, 0.18, 390),
        ("Breel Embolo", "Switzerland", 2, 2, 0.36, 0.16, 440),
        ("Lamine Yamal", "Spain", 1, 1, 0.32, 0.34, 485),
        ("Mikel Merino", "Spain", 2, 0, 0.25, 0.10, 120),
        ("Field", "NONE", 0, 0, 0, 0, 350),
    ]

    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.91), ("Other_ARG", 0.09)],
        "France": [("Kylian Mbappé", 0.70), ("Michael Olise", 0.16), ("Ousmane Dembélé", 0.10), ("Other_FRA", 0.04)],
        "Spain": [("Lamine Yamal", 0.43), ("Rodri", 0.19), ("Pedri", 0.13), ("Fabián Ruiz", 0.09), ("Mikel Oyarzabal", 0.08), ("Other_ESP", 0.08)],
        "England": [("Harry Kane", 0.46), ("Jude Bellingham", 0.43), ("Other_ENG", 0.11)],
        "Norway": [("Erling Haaland", 0.88), ("Martin Ødegaard", 0.08), ("Other_NOR", 0.04)],
        "Switzerland": [("Gregor Kobel", 0.38), ("Granit Xhaka", 0.36), ("Johan Manzambi", 0.12), ("Other_SUI", 0.14)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.42,
        "France": 1.42,
        "Norway": 1.24,
        "England": 1.15,
        "Spain": 1.00,      # Collective depth (Ruiz/Merino scored QF2, Yamal only 1g so far!)
        "Switzerland": 0.82,
    }

    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} ====================")
    print(f"  Base: SF1 FRA-ESP={base_p('France','Spain',fra_sf1_net,0):.4f} | QF3 ENG-NOR={base_p('England','Norway',eng_qf_pen,0):.4f} | QF4 ARG-SUI={base_p('Argentina','Switzerland',arg_kc_crowd,sui_fatigue_qf+sui_inj_qf):.4f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        team_matches = {}

        def play_ko(a, b, mod_a=0, mod_b=0, stage="KO"):
            p_a = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + mod_a) - (ELO[b] + mod_b)) / scale))
            a_won = (random.random() < p_a)
            team_matches.setdefault(a, []).append((base_elo[b], a_won, p_a, stage))
            team_matches.setdefault(b, []).append((base_elo[a], not a_won, 1.0 - p_a, stage))
            return (a, b) if a_won else (b, a)

        w97 = "France"
        w98 = "Spain"
        w99, _ = play_ko("England", "Norway", mod_a=eng_qf_pen, mod_b=0, stage="QF")
        w100, _ = play_ko("Argentina", "Switzerland", mod_a=arg_kc_crowd, mod_b=sui_fatigue_qf + sui_inj_qf, stage="QF")

        counts["QF_Miami"][w99] += 1
        counts["QF_KC"][w100] += 1
        for t in (w97, w98, w99, w100):
            counts["Reach_SF"][t] += 1

        w101, l101 = play_ko(w97, w98, mod_a=fra_sf1_net, mod_b=0, stage="SF")

        sf2_ma = eng_sf_pen if w99 == "England" else 0
        sf2_mb = sui_inj_late if w100 == "Switzerland" else 0
        w102, l102 = play_ko(w99, w100, mod_a=sf2_ma, mod_b=sf2_mb, stage="SF")

        counts["SF1_Dallas"][w101] += 1
        counts["SF2_Atlanta"][w102] += 1
        counts["Reach_Final"][w101] += 1
        counts["Reach_Final"][w102] += 1

        tp_mb = sui_inj_late if l102 == "Switzerland" else 0
        w103, l103 = play_ko(l101, l102, mod_a=0, mod_b=tp_mb, stage="3P")

        fin_mb = sui_inj_late if w102 == "Switzerland" else 0
        w104, l104 = play_ko(w101, w102, mod_a=0, mod_b=fin_mb, stage="FIN")

        counts["ThirdPlace"][w103] += 1
        counts["Champion"][w104] += 1

        # GOLDEN BOOT
        best_key = (-1, -1, -9999)
        best_name = None
        for pname, team, cg, ca, gpg, apg, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(1.2)
                key = (fg, poisson(0.8), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg; assists = ca; mins = gmins
            ms = list(team_matches.get(team, []))
            if pname == "Johan Manzambi":
                if len(ms) > 0 and ms[0][3] == "QF":
                    ms = ms[1:]
                if len(ms) > 0 and ms[0][3] == "SF" and random.random() < 0.70:
                    ms = ms[1:]
            if pname in ("Harry Kane", "Jude Bellingham") and len(ms) >= 2 and random.random() < 0.13:
                ms = [ms[0]] + ms[2:]

            eff_ms = []
            for oe, won, p_win, stg in ms:
                if pname == "Kylian Mbappé" and stg == "SF":
                    mp = mbappe_sf_miss
                elif stg == "3P":
                    mp = tp_rot_miss * (0.65 if pname in ("Kylian Mbappé", "Lionel Messi", "Erling Haaland", "Harry Kane") else 1.2)
                else:
                    mp = 0.045 if pname == "Lionel Messi" else 0.025
                if random.random() > mp:
                    eff_ms.append((oe, won, p_win, stg))

            eff_ng = len(eff_ms)
            if eff_ng > 0:
                mult = max(0.35, random.gauss(1.0, 0.25))
                exp_g = 0.0
                for oe, won, p_win, stg in eff_ms:
                    opp_mult = max(0.75, min(1.38, 1.0 + (1920.0 - oe) / 420.0))
                    if team == "France" and stg == "SF":
                        opp_mult *= 0.90
                    stg_mult = 1.12 if stg == "3P" else (0.92 if stg == "FIN" else 1.0)
                    mu = gpg * mult * opp_mult * stg_mult
                    denom = 1.0 + p_win * (win_goal_ratio - 1.0)
                    mu_adj = (mu * win_goal_ratio / denom) if won else (mu / denom)
                    exp_g += mu_adj
                goals += poisson(exp_g)
                assists += poisson(eff_ng * apg)
            mins += eff_ng * (85 if pname == "Lionel Messi" else 87)
            key = (goals, assists, -mins)
            if key > best_key:
                best_key = key; best_name = pname
        gb_wins[best_name] += 1

        # GOLDEN BALL MODEL 1: Team Finish
        r = random.random()
        if r < 0.56: gb_team = w104
        elif r < 0.86: gb_team = l104
        elif r < 0.95: gb_team = w103
        else: gb_team = l103
        shares = TEAM_SHARES.get(gb_team, [("Other_TEAM", 1.0)])
        u = random.random(); cum = 0.0
        for pl, sh in shares:
            cum += sh
            if u <= cum:
                gball_team_wins[pl] += 1
                break

        # GOLDEN BALL MODEL 2: Star-power + Golden Boot coupled
        f4_items = [(w104, 0.52), (l104, 0.31), (w103, 0.11), (l103, 0.06)]
        gb_winner_team = None
        for pname, team, *_ in players:
            if pname == best_name:
                gb_winner_team = team; break
        weights = []
        for t, bw in f4_items:
            sm = TEAM_STAR_MULT.get(t, 0.85)
            gb_bonus = 1.38 if t == gb_winner_team else 1.0
            weights.append((t, bw * sm * gb_bonus))
        tot_w = sum(x[1] for x in weights)
        u = random.random() * tot_w; cum = 0.0
        gb_team2 = w104
        for t, wt in weights:
            cum += wt
            if u <= cum:
                gb_team2 = t; break
        shares2 = list(TEAM_SHARES.get(gb_team2, [("Other_TEAM", 1.0)]))
        if gb_team2 == gb_winner_team and any(pl == best_name for pl, _ in shares2):
            adj = [(pl, sh * (1.80 if pl == best_name else 0.72)) for pl, sh in shares2]
            s_tot = sum(x[1] for x in adj)
            shares2 = [(pl, sh / s_tot) for pl, sh in adj]
        u = random.random(); cum = 0.0
        for pl, sh in shares2:
            cum += sh
            if u <= cum:
                gball_star_wins[pl] += 1
                break

    out = {}
    for key in ["QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"]:
        out[key] = {t: cnt/N for t, cnt in counts[key].most_common(8)}
    out["GOLDEN_BOOT"] = {n: c/N for n, c in gb_wins.most_common(8)}
    out["GBALL_TEAM"] = {n: c/N for n, c in gball_team_wins.most_common(12)}
    out["GBALL_STAR"] = {n: c/N for n, c in gball_star_wins.most_common(12)}
    print("  SF1_Dallas :", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF1_Dallas"].items()))
    print("  SF2_Atlanta:", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF2_Atlanta"].items()))
    print("  ThirdPlace :", ", ".join(f"{k}:{v:.4f}" for k, v in list(out["ThirdPlace"].items())[:6]))
    print("  Champion   :", ", ".join(f"{k}:{v:.4f}" for k, v in list(out["Champion"].items())[:6]))
    print("  GOLDEN_BOOT:", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(5)))
    return out

r1 = run_sim("1. MARKET-CALIBRATED (45%)", ELO_MARKET, scale=405.0, sigma=38.0,
             fra_sf1_net=2.5, eng_qf_pen=-8, eng_sf_pen=-7,
             arg_kc_crowd=6, sui_fatigue_qf=-9, sui_inj_qf=-11, sui_inj_late=-6,
             messi_gpg=0.65, mbappe_gpg=0.88, haaland_gpg=0.90, kane_gpg=0.73,
             mbappe_sf_miss=0.03, win_goal_ratio=1.68, N=200000)

r2 = run_sim("2. BALANCED BAYES+MARKET (30%)", ELO_BALANCED, scale=410.0, sigma=42.0,
             fra_sf1_net=2.5, eng_qf_pen=-9, eng_sf_pen=-7,
             arg_kc_crowd=6, sui_fatigue_qf=-9, sui_inj_qf=-11, sui_inj_late=-6,
             messi_gpg=0.67, mbappe_gpg=0.87, haaland_gpg=0.92, kane_gpg=0.73,
             mbappe_sf_miss=0.035, win_goal_ratio=1.72, N=200000)

r3 = run_sim("3. PURE BAYESIAN / SPAIN-H2H (12.5%)", ELO_BAYESIAN, scale=410.0, sigma=44.0,
             fra_sf1_net=1.0, eng_qf_pen=-10, eng_sf_pen=-8,
             arg_kc_crowd=7, sui_fatigue_qf=-10, sui_inj_qf=-12, sui_inj_late=-7,
             messi_gpg=0.70, mbappe_gpg=0.86, haaland_gpg=0.95, kane_gpg=0.74,
             mbappe_sf_miss=0.04, win_goal_ratio=1.80, N=150000)

r4 = run_sim("4. UPSET-CONSERVATIVE (12.5%)", ELO_CONSERVATIVE, scale=425.0, sigma=50.0,
             fra_sf1_net=0.0, eng_qf_pen=-8, eng_sf_pen=-8,
             arg_kc_crowd=4, sui_fatigue_qf=-8, sui_inj_qf=-10, sui_inj_late=-5,
             messi_gpg=0.65, mbappe_gpg=0.85, haaland_gpg=0.90, kane_gpg=0.71,
             mbappe_sf_miss=0.05, win_goal_ratio=1.68, N=150000)

weights = [(r1, 0.45), (r2, 0.30), (r3, 0.125), (r4, 0.125)]
print("\n==================== JULY 10 v2 WEIGHTED ENSEMBLE (45/30/12.5/12.5) ====================")
ens = {}
for key in ["QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final", "GOLDEN_BOOT"]:
    agg = Counter()
    for res, wt in weights:
        for k, v in res[key].items():
            agg[k] += wt * v
    ens[key] = dict(agg)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in agg.most_common(8)))

agg_gb_sim = Counter()
for res, wt in weights:
    for k, v in res["GBALL_TEAM"].items():
        agg_gb_sim[k] += wt * 0.40 * v
    for k, v in res["GBALL_STAR"].items():
        agg_gb_sim[k] += wt * 0.60 * v
print("  GBALL_SIM   : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb_sim.most_common(12)))

# CHAMPION BLEND: 60% Market Consensus (DK post-QF2 + Bayesian Kalshi) + 40% Ensemble
mkt_champ = {"France": 0.375, "Spain": 0.225, "Argentina": 0.176, "England": 0.155, "Norway": 0.051, "Switzerland": 0.018}
champ_blend = {t: 0.60 * mkt_champ[t] + 0.40 * ens["Champion"][t] for t in mkt_champ}
print("\n  CHAMPION BLEND (60% Mkt / 40% Ens): " + ", ".join(f"{t}:{v:.4f}" for t, v in sorted(champ_blend.items(), key=lambda x:-x[1])))

# GOLDEN BALL BAYESIAN MARKET UPDATE (combining bet365 Jul 9 + Racing Post Jul 8 conditioned on FRA beat MAR & ESP beat BEL!)
# Look at bet365 Jul 9 pre-QF1 raw odds:
#   Mbappe 7/4 (36.36%), Messi 3/1 (25.00%), Haaland 7/1 (12.50%), Kane 8/1 (11.11%),
#   Olise 10/1 (9.09%), Bellingham 10/1 (9.09%), Yamal 20/1 (4.76%).
# Note: in a ~132% book, pre-QF1 vig-free probs were approx:
#   Mbappe ~27.5%, Messi ~19.0%, Haaland ~9.5%, Kane ~8.4%, Olise ~6.9%, Bellingham ~6.9%, Yamal ~3.6% (+ Dembele ~2.8%, Pedri ~3.2%, Rodri ~2.5%).
# Now condition on BOTH QF1 (FRA 2-0 MAR; Mbappe 1g+1a; France SF 0.76->1.00, Final 0.485->0.573, Champ 0.323->0.375)
# AND QF2 (ESP 2-1 BEL; Spain SF 0.746->1.00, Final 0.308->0.427, Champ 0.173->0.225; Pedri benched, Yamal lively):
# Using the exact ratios of Final/Champion & narrative multipliers:
# - Mbappe: pre-QF1 ~27.5% * (1.28 QF1 win+1g/1a boost) * (0.91 ESP beat BEL vs 75/25) -> ~31.8%!
#   (Compare Jul 9 market Bayes = 34.5% -> * 0.905 (FRA Final 0.64->0.573, Champ 0.43->0.375) = 31.2%!)
# - Messi: Jul 9 market Bayes = 21.4% -> * 1.01 (ARG Champ 0.172->0.174) = 21.6%!
# - Haaland: Jul 9 market Bayes = 7.5% -> * 1.03 (NOR QF3 34.1->35.6%) = 7.7%!
# - Kane: Jul 9 market Bayes = 6.3% -> * 0.99 = 6.2% (note bet365 had Kane ~8.4% pre-QF1 -> avg ~7.2%!)
# - Bellingham: Jul 9 market Bayes = 5.2% -> ~5.3% (bet365 ~6.7% -> avg ~5.9%!)
# - Michael Olise: bet365 10/1 pre-QF1 (~6.9%) * (1.28 FRA QF1 + no yellow ban) * (0.91 ESP wins QF2) = ~8.0%!!
#   Wait: Racing Post Jul 8 had Olise lower (~3.6% -> 4.8% Jul 9 -> ~4.4% Jul 10). Avg of bet365 & RP market = ~6.2%!
# - Lamine Yamal: bet365 20/1 pre-QF1 (~3.6%) * 1.40 (Spain wins QF2 + Pedri benched) = ~5.0% (RP Jul 8 had Yamal ~4.2% -> * 1.40 = ~5.9%). Market avg ~5.5%!
# Let's blend 50% Sim + 50% Market Bayes!
mkt_gball = {
    "Kylian Mbappé": 0.312,
    "Lionel Messi": 0.215,
    "Erling Haaland": 0.077,
    "Harry Kane": 0.070,
    "Michael Olise": 0.062,
    "Jude Bellingham": 0.058,
    "Lamine Yamal": 0.055,
    "Ousmane Dembélé": 0.036,
    "Rodri": 0.025,
    "Pedri": 0.022,
}
print("\n=== GOLDEN BALL BLEND (50% SIM / 50% MARKET BAYES) ===")
gb_blend = {}
for pl in set(list(mkt_gball.keys()) + list(agg_gb_sim.keys())):
    if pl.startswith("Other"): continue
    gb_blend[pl] = 0.50 * agg_gb_sim.get(pl, 0.0) + 0.50 * mkt_gball.get(pl, 0.0)
for pl, v in sorted(gb_blend.items(), key=lambda x:-x[1])[:10]:
    print(f"  {pl:18s}: Blend={v:.4f} (Sim={agg_gb_sim.get(pl,0):.4f}, Mkt={mkt_gball.get(pl,0):.4f})")
