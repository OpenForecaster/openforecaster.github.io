import random, math
from collections import Counter

# ==============================================================================
# JULY 8, 2026 WORLD CUP SIMULATION — POST-R16 FULL MARKET + TEAM NEWS UPDATE
# Key July 8 updates:
#   - FIRST published odds for QF4 ARG-SUI: DK -275/+215 (69.8%/71.3%), BO -295/+250 (72.3%/73.4%)
#   - Full July 8 QF markets:
#       QF1 FRA-MAR: FD -410/+310, DK -370/+285, BO -375/+305 -> ~76.0% FRA / 24.0% MAR
#       QF2 ESP-BEL: FD -370/+280, DK -340/+260, BO -335/+280 -> ~74.5% ESP / 25.5% BEL
#       QF3 ENG-NOR: FD -225/+178, DK -225/+180, BO -197/+172 -> ~65.4% ENG / 34.6% NOR
#       QF4 ARG-SUI: DK -275/+215, BO -295/+250 -> ~71.5% ARG / 28.5% SUI
#   - Full July 8 Outrights (BO, SI, AP) + FD Reach-Final (FRA -115, ARG +125, NOR +550):
#       France ~32.8% Champ / ~49% Final (clear #1 ahead of Spain ~19.3%, Argentina ~18.6%, England ~15.6%, Norway ~5.6%)
#   - Team News July 8:
#       FRA: Tchouameni probably out (-2 net); Olise yellow card upheld (plays QF1, SF1 ban risk if booked w/ Barcola, Kone)
#       MAR: Saibari expected out (-14 QF, -6 late)
#       BEL: Onana ACL out (-14); ESP: Yamal regaining sharpness (1g/1a), collective depth
#       ENG: Quansah suspended, Rice/Guehi/James trained separately Wed, 5 starters on yellows; NOR: grind/illness (Strand Larsen fever)
#       SUI: Manzambi knee contusion (brace), Vargas recovering, west coast -> KC flight vs ARG KC training base
#   - Golden Boot July 8 (FanDuel CBS / Racing Post): Messi +120 (11/10 UK), Mbappe +140, Haaland +700, Kane +800
#   - Golden Ball July 8 (Racing Post UK): Mbappe 7/4, Messi 2/1, Haaland 7/1, Kane 8/1, Bellingham 10/1, Olise 10/1
# ==============================================================================

# 1. MARKET-CALIBRATED ELO (tight to Jul 8 BetOnline/SI/AP/DK/FD outrights + QFs + Reach-Final)
ELO_MARKET = {
    "France": 2192,       # Clear #1 (~33% Champ, ~49% Final, ~76.5% vs MAR, ~60% vs ESP)
    "Spain": 2124,        # ~20% Champ, ~36% Final, ~74.5% vs BEL
    "Argentina": 2094,    # ~18.5% Champ, ~41.5% Final, ~71.5% vs SUI
    "England": 2076,      # ~15.5% Champ, ~34.5% Final, ~65.5% vs NOR
    "Morocco": 1990,      # -14 Saibari -> ~76.6% FRA
    "Norway": 1966,       # ~65.5% ENG, ~5.3% Champ
    "Belgium": 1948,      # -14 Onana -> ~74.5% ESP
    "Switzerland": 1948,  # KC/travel/inj -> ~71.4% ARG
}

# 2. BALANCED BAYESIAN + MARKET BLEND
ELO_BALANCED = {
    "France": 2180,       # Strong #1 (~31.5% Champ, ~47.5% Final)
    "Spain": 2128,        # Respects 35 unbeaten / 6 CS (~21.5% Champ, ~37% Final)
    "Argentina": 2092,    # ~19% Champ, ~42% Final
    "England": 2070,      # ~15% Champ, ~34% Final
    "Morocco": 1986,      # -14 Saibari -> ~76.0% FRA
    "Norway": 1960,       # ~65.0% ENG
    "Belgium": 1948,      # -14 Onana -> ~74.9% ESP
    "Switzerland": 1942,  # ~72.0% ARG
}

# 3. PURE BAYESIAN / SPAIN-DEFENSE FORM (closer to Jul 7 form model)
ELO_BAYESIAN = {
    "France": 2168,
    "Spain": 2138,        # 35 unbeaten, 0 GA in 5 WC matches
    "Argentina": 2094,    # 2.90-0.97 xG vs Egypt
    "England": 2064,
    "Morocco": 1978,
    "Norway": 1958,
    "Belgium": 1948,
    "Switzerland": 1936,
}

# 4. UPSET-CONSERVATIVE (wider variance, ENG knocks + card risks + SUI/NOR/MAR resilience)
ELO_CONSERVATIVE = {
    "France": 2170,
    "Spain": 2122,
    "Argentina": 2082,
    "England": 2060,
    "Morocco": 1990,
    "Norway": 1966,
    "Belgium": 1952,
    "Switzerland": 1948,
}

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=410.0, sigma=42.0,
            fra_tchou_qf=-2, fra_card_sf=-3, mar_saibari_qf=-14, mar_saibari_late=-6,
            bel_onana=-14,
            eng_quansah_qf=-5, eng_card_sf=-4,
            arg_kc_crowd=6, sui_fatigue_qf=-9, sui_inj_qf=-9, sui_inj_late=-4,
            messi_gpg=0.66, mbappe_gpg=0.88, haaland_gpg=0.92, kane_gpg=0.73,
            win_goal_ratio=1.72,
            N=200000, seed=20260708):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"
    ]}
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    players = [
        ("Lionel Messi", "Argentina", 8, 1, messi_gpg, 0.22, 435),
        ("Kylian Mbappé", "France", 7, 2, mbappe_gpg, 0.28, 435),
        ("Erling Haaland", "Norway", 7, 0, haaland_gpg, 0.08, 355),
        ("Harry Kane", "England", 6, 1, kane_gpg, 0.17, 435),
        ("Ousmane Dembélé", "France", 4, 2, 0.45, 0.28, 425),
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.48, 0.20, 415),
        ("Jude Bellingham", "England", 4, 1, 0.38, 0.22, 390),
        ("Johan Manzambi", "Switzerland", 3, 2, 0.34, 0.16, 340),
        ("Ismael Saibari", "Morocco", 3, 0, 0.32, 0.15, 392),
        ("Charles De Ketelaere", "Belgium", 2, 0, 0.45, 0.18, 320),
        ("Leandro Trossard", "Belgium", 2, 3, 0.38, 0.22, 440),
        ("Azzedine Ounahi", "Morocco", 2, 0, 0.28, 0.18, 440),
        ("Bradley Barcola", "France", 2, 0, 0.35, 0.22, 345),
        ("Julián Álvarez", "Argentina", 2, 1, 0.44, 0.18, 390),
        ("Breel Embolo", "Switzerland", 2, 2, 0.36, 0.16, 440),
        ("Lamine Yamal", "Spain", 1, 1, 0.32, 0.34, 395),
        ("Field", "NONE", 0, 0, 0, 0, 350),
    ]

    # Updated Golden Ball intra-team shares incorporating July 8 news:
    # - France: Mbappe 0.69 (7g/2a, 7/4 Racing Post fav), Olise 0.18 (drifted 6/1->10/1, yellow-card tightrope), Dembele 0.08
    # - Spain: Yamal 0.38 (still regaining sharpness after April hamstring, 1g/1a), Pedri 0.28, Oyarzabal 0.14, Unai Simon 0.12
    # - England: Kane 0.46 (6g/1a, 8/1 RP), Bellingham 0.43 (4g/1a, 10/1 RP), Other 0.11
    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.91), ("Other_ARG", 0.09)],
        "France": [("Kylian Mbappé", 0.69), ("Michael Olise", 0.18), ("Ousmane Dembélé", 0.08), ("Other_FRA", 0.05)],
        "Spain": [("Lamine Yamal", 0.38), ("Pedri", 0.28), ("Mikel Oyarzabal", 0.14), ("Unai Simón", 0.12), ("Other_ESP", 0.08)],
        "England": [("Harry Kane", 0.46), ("Jude Bellingham", 0.43), ("Other_ENG", 0.11)],
        "Norway": [("Erling Haaland", 0.88), ("Martin Ødegaard", 0.08), ("Other_NOR", 0.04)],
        "Morocco": [("Achraf Hakimi", 0.42), ("Brahim Díaz", 0.22), ("Yassine Bounou", 0.20), ("Azzedine Ounahi", 0.16)],
        "Switzerland": [("Gregor Kobel", 0.34), ("Granit Xhaka", 0.32), ("Johan Manzambi", 0.20), ("Other_SUI", 0.14)],
        "Belgium": [("Charles De Ketelaere", 0.32), ("Thibaut Courtois", 0.26), ("Leandro Trossard", 0.22), ("Other_BEL", 0.20)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.42,  # Messi 8g/1a + iconic narrative
        "France": 1.36,     # Mbappe 7g/2a + Olise 5a + 14 goals
        "Norway": 1.24,     # Haaland 7g
        "England": 1.15,    # Kane 6g + Bellingham 4g
        "Spain": 1.00,      # Collective depth, no runaway individual scorer
        "Morocco": 0.94,
        "Belgium": 0.88,
        "Switzerland": 0.84,
    }

    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} (scale={scale}, sigma={sigma}) ====================")
    print(f"  QF1 FRA-MAR = {base_p('France','Morocco',fra_tchou_qf,mar_saibari_qf):.4f} / {1-base_p('France','Morocco',fra_tchou_qf,mar_saibari_qf):.4f}")
    print(f"  QF2 ESP-BEL = {base_p('Spain','Belgium',0,bel_onana):.4f} / {1-base_p('Spain','Belgium',0,bel_onana):.4f}")
    print(f"  QF3 ENG-NOR = {base_p('England','Norway',eng_quansah_qf,0):.4f} / {1-base_p('England','Norway',eng_quansah_qf,0):.4f}")
    print(f"  QF4 ARG-SUI = {base_p('Argentina','Switzerland',arg_kc_crowd,sui_fatigue_qf+sui_inj_qf):.4f} / {1-base_p('Argentina','Switzerland',arg_kc_crowd,sui_fatigue_qf+sui_inj_qf):.4f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        team_matches = {}

        def play_ko(a, b, mod_a=0, mod_b=0):
            p_a = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + mod_a) - (ELO[b] + mod_b)) / scale))
            a_won = (random.random() < p_a)
            team_matches.setdefault(a, []).append((base_elo[b], a_won, p_a))
            team_matches.setdefault(b, []).append((base_elo[a], not a_won, 1.0 - p_a))
            return (a, b) if a_won else (b, a)

        w97, _ = play_ko("France", "Morocco", mod_a=fra_tchou_qf, mod_b=mar_saibari_qf)
        w98, _ = play_ko("Spain", "Belgium", mod_a=0, mod_b=bel_onana)
        w99, _ = play_ko("England", "Norway", mod_a=eng_quansah_qf, mod_b=0)
        w100, _ = play_ko("Argentina", "Switzerland", mod_a=arg_kc_crowd, mod_b=sui_fatigue_qf + sui_inj_qf)

        counts["QF_Boston"][w97] += 1
        counts["QF_LA"][w98] += 1
        counts["QF_Miami"][w99] += 1
        counts["QF_KC"][w100] += 1
        for t in (w97, w98, w99, w100):
            counts["Reach_SF"][t] += 1

        sf1_ma = fra_card_sf if w97 == "France" else mar_saibari_late
        sf1_mb = bel_onana if w98 == "Belgium" else 0
        w101, l101 = play_ko(w97, w98, mod_a=sf1_ma, mod_b=sf1_mb)

        sf2_ma = eng_card_sf if w99 == "England" else 0
        sf2_mb = sui_inj_late if w100 == "Switzerland" else 0
        w102, l102 = play_ko(w99, w100, mod_a=sf2_ma, mod_b=sf2_mb)

        counts["SF1_Dallas"][w101] += 1
        counts["SF2_Atlanta"][w102] += 1
        counts["Reach_Final"][w101] += 1
        counts["Reach_Final"][w102] += 1

        tp_ma = (mar_saibari_late if l101 == "Morocco" else (bel_onana if l101 == "Belgium" else 0))
        tp_mb = (sui_inj_late if l102 == "Switzerland" else 0)
        w103, l103 = play_ko(l101, l102, mod_a=tp_ma, mod_b=tp_mb)

        fin_ma = (mar_saibari_late if w101 == "Morocco" else (bel_onana if w101 == "Belgium" else 0))
        fin_mb = (sui_inj_late if w102 == "Switzerland" else 0)
        w104, l104 = play_ko(w101, w102, mod_a=fin_ma, mod_b=fin_mb)

        counts["ThirdPlace"][w103] += 1
        counts["Champion"][w104] += 1

        # GOLDEN BOOT
        best_key = (-1, -1, -9999)
        best_name = None
        for pname, team, cg, ca, gpg, apg, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(1.4)
                key = (fg, poisson(0.9), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg; assists = ca; mins = gmins
            ms = list(team_matches.get(team, []))
            if pname == "Ismael Saibari" and len(ms) > 0 and random.random() < 0.80:
                ms = ms[1:]
            if pname == "Johan Manzambi" and len(ms) > 0 and random.random() < 0.72:
                ms = ms[1:]
            # Yellow-card SF suspension risk for Kane & Bellingham (~14% chance of missing SF if ENG advances)
            if pname in ("Harry Kane", "Jude Bellingham") and len(ms) >= 2 and random.random() < 0.13:
                ms = [ms[0]] + ms[2:]
            miss_p = 0.045 if pname == "Lionel Messi" else 0.025
            eff_ms = [m for m in ms if random.random() > miss_p]
            eff_ng = len(eff_ms)
            if eff_ng > 0:
                mult = max(0.35, random.gauss(1.0, 0.25))
                exp_g = 0.0
                for oe, won, p_win in eff_ms:
                    opp_mult = max(0.75, min(1.38, 1.0 + (1920.0 - oe) / 420.0))
                    mu = gpg * mult * opp_mult
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
    for key in ["QF_Boston", "QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"]:
        out[key] = {t: cnt/N for t, cnt in counts[key].most_common(8)}
    out["GOLDEN_BOOT"] = {n: c/N for n, c in gb_wins.most_common(8)}
    out["GBALL_TEAM"] = {n: c/N for n, c in gball_team_wins.most_common(10)}
    out["GBALL_STAR"] = {n: c/N for n, c in gball_star_wins.most_common(10)}
    print("  QF_KC      :", ", ".join(f"{k}:{v:.4f}" for k, v in out["QF_KC"].items()))
    print("  SF1_Dallas :", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF1_Dallas"].items()))
    print("  SF2_Atlanta:", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF2_Atlanta"].items()))
    print("  Champion   :", ", ".join(f"{k}:{v:.4f}" for k, v in list(out["Champion"].items())[:5]))
    print("  GOLDEN_BOOT:", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(5)))
    return out

r1 = run_sim("1. MARKET-CALIBRATED (40%)", ELO_MARKET, scale=405.0, sigma=38.0,
             fra_tchou_qf=-2, fra_card_sf=-3, mar_saibari_qf=-14, mar_saibari_late=-6, bel_onana=-14,
             eng_quansah_qf=-5, eng_card_sf=-4, arg_kc_crowd=5, sui_fatigue_qf=-9, sui_inj_qf=-8, sui_inj_late=-4,
             messi_gpg=0.65, mbappe_gpg=0.88, haaland_gpg=0.90, kane_gpg=0.73, win_goal_ratio=1.68, N=200000)

r2 = run_sim("2. BALANCED BAYES+MARKET (30%)", ELO_BALANCED, scale=410.0, sigma=42.0,
             fra_tchou_qf=-2, fra_card_sf=-3, mar_saibari_qf=-14, mar_saibari_late=-6, bel_onana=-14,
             eng_quansah_qf=-5, eng_card_sf=-4, arg_kc_crowd=6, sui_fatigue_qf=-9, sui_inj_qf=-9, sui_inj_late=-4,
             messi_gpg=0.67, mbappe_gpg=0.87, haaland_gpg=0.92, kane_gpg=0.73, win_goal_ratio=1.72, N=200000)

r3 = run_sim("3. PURE BAYESIAN / SPAIN-CS (15%)", ELO_BAYESIAN, scale=410.0, sigma=44.0,
             fra_tchou_qf=-3, fra_card_sf=-4, mar_saibari_qf=-15, mar_saibari_late=-7, bel_onana=-15,
             eng_quansah_qf=-6, eng_card_sf=-5, arg_kc_crowd=7, sui_fatigue_qf=-10, sui_inj_qf=-10, sui_inj_late=-5,
             messi_gpg=0.70, mbappe_gpg=0.86, haaland_gpg=0.95, kane_gpg=0.74, win_goal_ratio=1.80, N=150000)

r4 = run_sim("4. UPSET-CONSERVATIVE (15%)", ELO_CONSERVATIVE, scale=425.0, sigma=50.0,
             fra_tchou_qf=-4, fra_card_sf=-4, mar_saibari_qf=-12, mar_saibari_late=-5, bel_onana=-12,
             eng_quansah_qf=-6, eng_card_sf=-5, arg_kc_crowd=4, sui_fatigue_qf=-8, sui_inj_qf=-7, sui_inj_late=-4,
             messi_gpg=0.65, mbappe_gpg=0.85, haaland_gpg=0.90, kane_gpg=0.71, win_goal_ratio=1.68, N=150000)

weights = [(r1, 0.40), (r2, 0.30), (r3, 0.15), (r4, 0.15)]
print("\n==================== JULY 8 WEIGHTED ENSEMBLE (40/30/15/15) ====================")
ens = {}
for key in ["QF_Boston", "QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final", "GOLDEN_BOOT"]:
    agg = Counter()
    for res, wt in weights:
        for k, v in res[key].items():
            agg[k] += wt * v
    ens[key] = dict(agg)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in agg.most_common(8)))

# GOLDEN BOOT: Blend 65% Monte Carlo + 35% FanDuel/Racing Post July 8 vig-free
# FanDuel +120/+140/+700/+800 (power/mult mid): Messi 0.407, Mbappe 0.371, Haaland 0.104, Kane 0.092, Field 0.026
# Racing Post Messi 11/10 (+110 -> ~0.425): blended market = Messi 0.415, Mbappe 0.368, Haaland 0.103, Kane 0.090, Dembele 0.008, Oyarzabal 0.008
gb_market = {
    "Lionel Messi": 0.415,
    "Kylian Mbappé": 0.368,
    "Erling Haaland": 0.103,
    "Harry Kane": 0.090,
    "Ousmane Dembélé": 0.007,
    "Mikel Oyarzabal": 0.007,
}
gb_blend = Counter()
for k in set(ens["GOLDEN_BOOT"].keys()) | set(gb_market.keys()):
    gb_blend[k] = 0.65 * ens["GOLDEN_BOOT"].get(k, 0.0) + 0.35 * gb_market.get(k, 0.0)
print("  GBOOT_BLEND : " + ", ".join(f"{k}:{v:.4f}" for k, v in gb_blend.most_common(7)))

# GOLDEN BALL: Blend 60% Bracket-Coupled Sim (40% Team + 60% Star+GB) + 40% Racing Post UK July 8 vig-free
agg_gb_sim = Counter()
for res, wt in weights:
    for k, v in res["GBALL_TEAM"].items():
        agg_gb_sim[k] += wt * 0.40 * v
    for k, v in res["GBALL_STAR"].items():
        agg_gb_sim[k] += wt * 0.60 * v

# Racing Post UK Jul 8 (power/mult midpoint, Spain+Field ~0.20):
# Mbappe 7/4 -> 0.270, Messi 2/1 -> 0.246, Haaland 7/1 -> 0.083, Kane 8/1 -> 0.073,
# Bellingham 10/1 -> 0.059, Olise 10/1 -> 0.059, Yamal ~14/1 -> 0.055, Pedri ~18/1 -> 0.042, Dembele ~22/1 -> 0.028
rp_jul8 = {
    "Kylian Mbappé": 0.270,
    "Lionel Messi": 0.246,
    "Erling Haaland": 0.083,
    "Harry Kane": 0.073,
    "Jude Bellingham": 0.059,
    "Michael Olise": 0.059,
    "Lamine Yamal": 0.055,
    "Pedri": 0.042,
    "Ousmane Dembélé": 0.028,
    "Mikel Oyarzabal": 0.018,
}
agg_gb_final = Counter()
for pl in set(agg_gb_sim.keys()) | set(rp_jul8.keys()):
    agg_gb_final[pl] = 0.60 * agg_gb_sim.get(pl, 0.0) + 0.40 * rp_jul8.get(pl, 0.0)

print("  GBALL_SIM   : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb_sim.most_common(10)))
print("  GBALL_BLEND : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb_final.most_common(10)))
