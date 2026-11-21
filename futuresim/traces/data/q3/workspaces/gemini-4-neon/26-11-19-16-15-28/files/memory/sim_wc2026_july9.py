import random, math
from collections import Counter

# ==============================================================================
# JULY 9, 2026 WORLD CUP SIMULATION — POST-QF1 (FRANCE 2-0 MOROCCO!)
# Key July 9 updates:
#   - QF1 COMPLETED: France 2-0 Morocco (Mbappe 60', Dembele 66' [assist Mbappe])
#       * France 100% LOCKED into SF1 (Dallas, July 14); Morocco ELIMINATED!
#       * France dominated 21-4 shots (8-1 on target), 3rd straight KO clean sheet, 6/6 wins (+3 Elo Bayesian update)
#       * ZERO France yellow-card suspensions (Olise/Kone/Barcola all clean; cards wipe after QF -> fra_card_sf = 0!)
#       * Rest advantage in SF1: France gets 5 days rest (Jul 9 -> Jul 14) vs 4 days for ESP/BEL (Jul 10 LA -> Jul 14 Dallas): +5 Elo
#       * Minor fitness caution: Mbappe precautionary sub 77' (right ankle knock, walked/jumped post-match, says "I'm fine"),
#         Kone knee knock, Tchouameni adductor still recovering -> -3 Elo SF1 caution => net SF1 mod for France = +2 Elo!
#   - QF2 (Jul 10, LA): ESP-BEL DK -340/+260 (~74.6% ESP / 25.4% BEL) steady; Belgium without Onana (ACL)
#   - QF3 (Jul 11, Miami): ENG-NOR DK -225/+180 (~65.9% ENG / 34.1% NOR) steady;
#       * NEW: Jarell Quansah officially banned 2 matches (misses QF3 AND SF2 if ENG advances! -> eng_quansah_sf = -3)
#   - QF4 (Jul 11, KC): ARG-SUI DK -275/+215 (~70.4%), Lucky Rebel -305/+245 (~72.7%), BO -295/+250 (~72.8%) -> ~72.0% ARG / 28.0% SUI
#       * Sports Mole Jul 9: Manzambi remains major doubt (Jashari expected to start), Aebischer & Jaquez unlikely,
#         Ruben Vargas now fit enough to start (+2 Elo for SUI vs Jul 8)
#   - Golden Boot Post-QF1:
#       * Kylian Mbappe: 8g, 3a (512 mins) — GUARANTEED 2 more games (SF1 + Final/3P), LEADS tiebreaker +2 assists!
#       * Lionel Messi: 8g, 1a (435 mins) — plays QF4 vs SUI (72% -> 3 games, 28% -> 1 game)
#       * Erling Haaland: 7g, 0a (355 mins) — plays QF3 vs ENG (34.5% -> 3 games, 65.5% -> 1 game)
#       * Harry Kane: 6g, 1a (435 mins) — plays QF3 vs NOR (65.5% -> 3 games, 34.5% -> 1 game)
#       * Ousmane Dembele: 5g, 2a (510 mins) — GUARANTEED 2 more games!
#       * Mikel Oyarzabal: 4g, 1a (415 mins) — plays QF2 vs BEL
#       * Jude Bellingham: 4g, 1a (390 mins) — plays QF3 vs NOR
# ==============================================================================

# 1. MARKET-CALIBRATED ELO (anchored to Jul 8-9 DK/BO/SI/AP/FD outrights + QFs + FRA 2-0 MAR update)
ELO_MARKET = {
    "France": 2195,       # +3 post-2-0 dominance over Morocco (21-4 shots, 3rd KO CS)
    "Spain": 2124,        # ~74.5% vs BEL
    "Argentina": 2094,    # ~72.0% vs SUI
    "England": 2077,      # ~65.8% vs NOR
    "Norway": 1966,
    "Belgium": 1948,
    "Switzerland": 1950,  # +2 Vargas ready to start
}

# 2. BALANCED BAYESIAN + MARKET BLEND
ELO_BALANCED = {
    "France": 2183,       # +3 post-MAR
    "Spain": 2128,        # Respects 35 unbeaten / 6 CS
    "Argentina": 2092,
    "England": 2071,
    "Norway": 1960,
    "Belgium": 1948,
    "Switzerland": 1944,
}

# 3. PURE BAYESIAN / SPAIN-DEFENSE FORM
ELO_BAYESIAN = {
    "France": 2172,       # +4 post-MAR
    "Spain": 2138,        # 35 unbeaten, 0 GA in 5 WC matches
    "Argentina": 2094,
    "England": 2065,
    "Norway": 1958,
    "Belgium": 1948,
    "Switzerland": 1938,
}

# 4. UPSET-CONSERVATIVE
ELO_CONSERVATIVE = {
    "France": 2173,
    "Spain": 2122,
    "Argentina": 2082,
    "England": 2061,
    "Norway": 1966,
    "Belgium": 1952,
    "Switzerland": 1950,
}

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=410.0, sigma=42.0,
            fra_sf1_net=2,         # +5 extra rest day vs ESP/BEL, -3 minor ankle/knee/Tchouameni caution, 0 card bans!
            bel_onana=-14,
            eng_quansah_qf=-5, eng_sf_pen=-7,  # -3 Quansah 2-match ban + -4 yellow-card tightrope
            arg_kc_crowd=6, sui_fatigue_qf=-9, sui_inj_qf=-8, sui_inj_late=-4,
            messi_gpg=0.66, mbappe_gpg=0.88, haaland_gpg=0.92, kane_gpg=0.73,
            mbappe_sf_miss=0.045,  # slight ankle-knock caution in SF1
            tp_rot_miss=0.08,      # slight 3rd-place playoff rotation risk (lower for GB chasers)
            win_goal_ratio=1.72,
            N=200000, seed=20260709):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"
    ]}
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    # Post-QF1 player stats: (name, team, goals, assists, gpg, apg, mins)
    players = [
        ("Kylian Mbappé", "France", 8, 3, mbappe_gpg, 0.28, 512),     # +1g, +1a, +77m vs Morocco!
        ("Lionel Messi", "Argentina", 8, 1, messi_gpg, 0.22, 435),
        ("Erling Haaland", "Norway", 7, 0, haaland_gpg, 0.08, 355),
        ("Harry Kane", "England", 6, 1, kane_gpg, 0.17, 435),
        ("Ousmane Dembélé", "France", 5, 2, 0.47, 0.28, 510),         # +1g, +85m vs Morocco!
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.48, 0.20, 415),
        ("Jude Bellingham", "England", 4, 1, 0.38, 0.22, 390),
        ("Johan Manzambi", "Switzerland", 3, 2, 0.34, 0.16, 340),
        ("Charles De Ketelaere", "Belgium", 2, 0, 0.45, 0.18, 320),
        ("Leandro Trossard", "Belgium", 2, 3, 0.38, 0.22, 440),
        ("Bradley Barcola", "France", 2, 0, 0.30, 0.20, 360),         # lost starting spot to Doue
        ("Julián Álvarez", "Argentina", 2, 1, 0.44, 0.18, 390),
        ("Breel Embolo", "Switzerland", 2, 2, 0.36, 0.16, 440),
        ("Lamine Yamal", "Spain", 1, 1, 0.32, 0.34, 395),
        ("Field", "NONE", 0, 0, 0, 0, 350),
    ]

    # Updated Golden Ball intra-team shares post-QF1:
    # - France: Mbappe 0.70 (8g/3a, 20 career WC goals, QF1 goal+assist), Olise 0.15 (5a, avoided ban), Dembele 0.11 (2025 Ballon d'Or + 5g/2a + QF1 clincher!), Other 0.04
    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.91), ("Other_ARG", 0.09)],
        "France": [("Kylian Mbappé", 0.70), ("Michael Olise", 0.15), ("Ousmane Dembélé", 0.11), ("Other_FRA", 0.04)],
        "Spain": [("Lamine Yamal", 0.38), ("Pedri", 0.28), ("Mikel Oyarzabal", 0.14), ("Unai Simón", 0.12), ("Other_ESP", 0.08)],
        "England": [("Harry Kane", 0.46), ("Jude Bellingham", 0.43), ("Other_ENG", 0.11)],
        "Norway": [("Erling Haaland", 0.88), ("Martin Ødegaard", 0.08), ("Other_NOR", 0.04)],
        "Switzerland": [("Gregor Kobel", 0.34), ("Granit Xhaka", 0.32), ("Johan Manzambi", 0.20), ("Other_SUI", 0.14)],
        "Belgium": [("Charles De Ketelaere", 0.32), ("Thibaut Courtois", 0.26), ("Leandro Trossard", 0.22), ("Other_BEL", 0.20)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.42,  # Messi 8g/1a + iconic narrative
        "France": 1.42,     # UP from 1.36: Mbappe 8g/3a (joint top scorer, 20 career WC goals) + Dembele 5g/2a + Olise 5a + 16 goals!
        "Norway": 1.24,     # Haaland 7g
        "England": 1.15,    # Kane 6g + Bellingham 4g
        "Spain": 1.00,      # Collective depth
        "Belgium": 0.88,
        "Switzerland": 0.84,
    }

    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} (scale={scale}, sigma={sigma}) ====================")
    print(f"  QF2 ESP-BEL = {base_p('Spain','Belgium',0,bel_onana):.4f} / {1-base_p('Spain','Belgium',0,bel_onana):.4f}")
    print(f"  QF3 ENG-NOR = {base_p('England','Norway',eng_quansah_qf,0):.4f} / {1-base_p('England','Norway',eng_quansah_qf,0):.4f}")
    print(f"  QF4 ARG-SUI = {base_p('Argentina','Switzerland',arg_kc_crowd,sui_fatigue_qf+sui_inj_qf):.4f} / {1-base_p('Argentina','Switzerland',arg_kc_crowd,sui_fatigue_qf+sui_inj_qf):.4f}")
    print(f"  SF1 FRA-ESP = {base_p('France','Spain',fra_sf1_net,0):.4f} / {1-base_p('France','Spain',fra_sf1_net,0):.4f}")
    print(f"  SF1 FRA-BEL = {base_p('France','Belgium',fra_sf1_net,bel_onana):.4f} / {1-base_p('France','Belgium',fra_sf1_net,bel_onana):.4f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        team_matches = {}

        def play_ko(a, b, mod_a=0, mod_b=0, stage="KO"):
            p_a = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + mod_a) - (ELO[b] + mod_b)) / scale))
            a_won = (random.random() < p_a)
            team_matches.setdefault(a, []).append((base_elo[b], a_won, p_a, stage))
            team_matches.setdefault(b, []).append((base_elo[a], not a_won, 1.0 - p_a, stage))
            return (a, b) if a_won else (b, a)

        # QF1 ALREADY DONE: France beat Morocco!
        w97 = "France"
        w98, _ = play_ko("Spain", "Belgium", mod_a=0, mod_b=bel_onana, stage="QF")
        w99, _ = play_ko("England", "Norway", mod_a=eng_quansah_qf, mod_b=0, stage="QF")
        w100, _ = play_ko("Argentina", "Switzerland", mod_a=arg_kc_crowd, mod_b=sui_fatigue_qf + sui_inj_qf, stage="QF")

        counts["QF_LA"][w98] += 1
        counts["QF_Miami"][w99] += 1
        counts["QF_KC"][w100] += 1
        for t in (w97, w98, w99, w100):
            counts["Reach_SF"][t] += 1

        sf1_ma = fra_sf1_net
        sf1_mb = bel_onana if w98 == "Belgium" else 0
        w101, l101 = play_ko(w97, w98, mod_a=sf1_ma, mod_b=sf1_mb, stage="SF")

        sf2_ma = eng_sf_pen if w99 == "England" else 0
        sf2_mb = sui_inj_late if w100 == "Switzerland" else 0
        w102, l102 = play_ko(w99, w100, mod_a=sf2_ma, mod_b=sf2_mb, stage="SF")

        counts["SF1_Dallas"][w101] += 1
        counts["SF2_Atlanta"][w102] += 1
        counts["Reach_Final"][w101] += 1
        counts["Reach_Final"][w102] += 1

        tp_ma = bel_onana if l101 == "Belgium" else 0
        tp_mb = sui_inj_late if l102 == "Switzerland" else 0
        w103, l103 = play_ko(l101, l102, mod_a=tp_ma, mod_b=tp_mb, stage="3P")

        fin_ma = bel_onana if w101 == "Belgium" else 0
        fin_mb = sui_inj_late if w102 == "Switzerland" else 0
        w104, l104 = play_ko(w101, w102, mod_a=fin_ma, mod_b=fin_mb, stage="FIN")

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
            if pname == "Johan Manzambi" and len(ms) > 0 and ms[0][3] == "QF" and random.random() < 0.72:
                ms = ms[1:]
            # Yellow-card SF suspension risk for Kane & Bellingham (~13% if ENG advances)
            if pname in ("Harry Kane", "Jude Bellingham") and len(ms) >= 2 and random.random() < 0.13:
                ms = [ms[0]] + ms[2:]

            eff_ms = []
            for oe, won, p_win, stg in ms:
                if pname == "Kylian Mbappé" and stg == "SF":
                    mp = mbappe_sf_miss
                elif stg == "3P":
                    # Golden Boot leaders strongly prefer to play 3P, though some minor rest risk
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
                    # 3rd place playoff slightly more open (~1.12x goals), Final slightly tighter (~0.92x)
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
    for key in ["QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"]:
        out[key] = {t: cnt/N for t, cnt in counts[key].most_common(8)}
    out["GOLDEN_BOOT"] = {n: c/N for n, c in gb_wins.most_common(8)}
    out["GBALL_TEAM"] = {n: c/N for n, c in gball_team_wins.most_common(10)}
    out["GBALL_STAR"] = {n: c/N for n, c in gball_star_wins.most_common(10)}
    print("  QF_KC      :", ", ".join(f"{k}:{v:.4f}" for k, v in out["QF_KC"].items()))
    print("  SF1_Dallas :", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF1_Dallas"].items()))
    print("  SF2_Atlanta:", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF2_Atlanta"].items()))
    print("  ThirdPlace :", ", ".join(f"{k}:{v:.4f}" for k, v in list(out["ThirdPlace"].items())[:6]))
    print("  Champion   :", ", ".join(f"{k}:{v:.4f}" for k, v in list(out["Champion"].items())[:5]))
    print("  GOLDEN_BOOT:", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(6)))
    return out

r1 = run_sim("1. MARKET-CALIBRATED (40%)", ELO_MARKET, scale=405.0, sigma=38.0,
             fra_sf1_net=2, bel_onana=-14, eng_quansah_qf=-5, eng_sf_pen=-7,
             arg_kc_crowd=5, sui_fatigue_qf=-9, sui_inj_qf=-7, sui_inj_late=-4,
             messi_gpg=0.65, mbappe_gpg=0.88, haaland_gpg=0.90, kane_gpg=0.73,
             mbappe_sf_miss=0.04, win_goal_ratio=1.68, N=200000)

r2 = run_sim("2. BALANCED BAYES+MARKET (30%)", ELO_BALANCED, scale=410.0, sigma=42.0,
             fra_sf1_net=2, bel_onana=-14, eng_quansah_qf=-5, eng_sf_pen=-7,
             arg_kc_crowd=6, sui_fatigue_qf=-9, sui_inj_qf=-8, sui_inj_late=-4,
             messi_gpg=0.67, mbappe_gpg=0.87, haaland_gpg=0.92, kane_gpg=0.73,
             mbappe_sf_miss=0.045, win_goal_ratio=1.72, N=200000)

r3 = run_sim("3. PURE BAYESIAN / SPAIN-CS (15%)", ELO_BAYESIAN, scale=410.0, sigma=44.0,
             fra_sf1_net=1, bel_onana=-15, eng_quansah_qf=-6, eng_sf_pen=-8,
             arg_kc_crowd=7, sui_fatigue_qf=-10, sui_inj_qf=-9, sui_inj_late=-5,
             messi_gpg=0.70, mbappe_gpg=0.86, haaland_gpg=0.95, kane_gpg=0.74,
             mbappe_sf_miss=0.05, win_goal_ratio=1.80, N=150000)

r4 = run_sim("4. UPSET-CONSERVATIVE (15%)", ELO_CONSERVATIVE, scale=425.0, sigma=50.0,
             fra_sf1_net=0, bel_onana=-12, eng_quansah_qf=-6, eng_sf_pen=-8,
             arg_kc_crowd=4, sui_fatigue_qf=-8, sui_inj_qf=-7, sui_inj_late=-4,
             messi_gpg=0.65, mbappe_gpg=0.85, haaland_gpg=0.90, kane_gpg=0.71,
             mbappe_sf_miss=0.06, win_goal_ratio=1.68, N=150000)

weights = [(r1, 0.40), (r2, 0.30), (r3, 0.15), (r4, 0.15)]
print("\n==================== JULY 9 WEIGHTED ENSEMBLE (40/30/15/15) ====================")
ens = {}
for key in ["QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final", "GOLDEN_BOOT"]:
    agg = Counter()
    for res, wt in weights:
        for k, v in res[key].items():
            agg[k] += wt * v
    ens[key] = dict(agg)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in agg.most_common(8)))

# GOLDEN BALL: Combine 40% Team-Finish + 60% Star+GB Coupled
agg_gb_sim = Counter()
for res, wt in weights:
    for k, v in res["GBALL_TEAM"].items():
        agg_gb_sim[k] += wt * 0.40 * v
    for k, v in res["GBALL_STAR"].items():
        agg_gb_sim[k] += wt * 0.60 * v
print("  GBALL_SIM   : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb_sim.most_common(10)))

# Also check Bayesian conditioning on July 8 market odds for Champion & Reach-Final!
# July 8 market consensus Champion: FRA 32.6%, ESP 19.4%, ARG 18.7%, ENG 15.7%, NOR 5.5%, MAR 3.2%, SUI 2.8%, BEL 2.5%
# Note: Conditioning on FRA beating MAR (76% prob) eliminates MAR (3.2% -> 0%), boosts FRA by ~1/0.76 = 1.316x!
# Wait: FRA's win over MAR ALSO hurts ESP/BEL slightly in SF1 (since facing FRA is harder than facing MAR!)
# Let's check the exact multiplier ratio from July 8 sim -> July 9 sim and apply it to July 8 market consensus!
print("\n--- MARKET CONSENSUS BAYESIAN UPDATE CHECK ---")
# July 8 sim ensemble Champion: let's compare with July 9 sim!
