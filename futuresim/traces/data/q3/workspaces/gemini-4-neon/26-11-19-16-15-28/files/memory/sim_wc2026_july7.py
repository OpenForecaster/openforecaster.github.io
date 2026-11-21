import random, math
from collections import Counter

# ==============================================================================
# JULY 7, 2026 WORLD CUP SIMULATION v2 — ALL 8 QUARTERFINALISTS LOCKED!
# Refined calibration:
#   - QF1 FRA-MAR anchored to FanDuel Jul 7 (76.7%) + Opta (74.9%) + Sportune (74.4%) -> ~75.5%
#   - QF2 ESP-BEL anchored to FanDuel Jul 7 (74.95%) + Onana ACL out -> ~75.0%
#   - QF3 ENG-NOR anchored to FanDuel Jul 7 (65.8%) + BetMGM Jul 6 (62.6%) -> ~64.2%
#   - QF4 ARG-SUI: BOTH played 210m in last 5 days (ARG 120m+90m, SUI 90m+120m),
#     so SUI has recency+Vancouver-KC flight (-10) + Manzambi knee brace/inj (-10),
#     ARG has KC crowd (+5) -> bridges Kalshi post-ET (~70%) & Elo/outrights (~73%) -> ~72.0%
#   - Golden Ball: includes France Mbappe share 0.62 (matching Oddschecker 7/4 vs Olise 6/1)
#     and 3rd Market-Updated Oddschecker Bayesian model!
# ==============================================================================

# 1. BASE BAYESIAN + MARKET BLEND
ELO_BASE = {
    "France": 2166,       # 5-0-0; Tchouameni probably out (-2 net vs already-priced)
    "Spain": 2132,        # 35 unbeaten, 6 straight clean sheets
    "Argentina": 2090,    # 2.90-0.97 xG vs Egypt in 90m; conceded 2 to CPV & 2 to EGY
    "England": 2064,      # FanDuel -225 vs NOR; Quansah suspended (-5 QF)
    "Morocco": 1978,      # Saibari expected out (-14 QF, -7 late) -> ~75.8% FRA
    "Norway": 1952,       # Beat Brazil 2-1 -> ~64.5% ENG / 35.5% NOR
    "Belgium": 1945,      # Crushed USA 4-1; Onana ACL (-14) -> ~75.3% ESP
    "Switzerland": 1934,  # 10 unbeaten, 0 GA in 120m vs COL; recency+travel (-10), Manzambi (-10)
}

# 2. MARKET-ANCHORED (tight to FanDuel Jul 7: FRA 76.7%, ESP 75.0%, ENG 65.8%; Kalshi/outrights ARG 71.5%)
ELO_MARKET = {
    "France": 2174,
    "Spain": 2128,
    "Argentina": 2086,
    "England": 2068,
    "Morocco": 1976,      # ~76.8% FRA / 23.2% MAR
    "Norway": 1946,       # ~66.0% ENG / 34.0% NOR
    "Belgium": 1948,      # -14 Onana -> ~75.0% ESP / 25.0% BEL
    "Switzerland": 1938,  # ~71.2% ARG / 28.8% SUI
}

# 3. PURE BAYESIAN / FORM-RESPONSIVE (Spain 6 CS, ARG 2.90 xG, NOR form)
ELO_PURE = {
    "France": 2166,
    "Spain": 2140,
    "Argentina": 2096,
    "England": 2060,
    "Morocco": 1976,
    "Norway": 1960,       # ~63.2% ENG / 36.8% NOR
    "Belgium": 1948,      # -16 Onana -> ~76.4% ESP
    "Switzerland": 1932,  # ~73.8% ARG / 26.2% SUI
}

# 4. UPSET-CONSERVATIVE (wider sigma, SUI/NOR/MAR/BEL resilience, ARG defensive leakage)
ELO_CONSERVATIVE = {
    "France": 2156,
    "Spain": 2122,
    "Argentina": 2078,
    "England": 2052,
    "Morocco": 1984,
    "Norway": 1958,
    "Belgium": 1948,
    "Switzerland": 1942,
}

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=410.0, sigma=45.0,
            fra_tchou_qf=-2, mar_saibari_qf=-14, mar_saibari_late=-7,
            bel_onana=-14,
            eng_quansah_qf=-5,
            arg_kc_crowd=5, sui_fatigue_qf=-10, sui_inj_qf=-10, sui_inj_late=-5,
            messi_gpg=0.70, mbappe_gpg=0.85, haaland_gpg=0.94, kane_gpg=0.73,
            win_goal_ratio=1.75,
            esp_yamal_share=0.45,
            N=250000, seed=20260707):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"
    ]}
    ko_games_sum = Counter()
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    players = [
        ("Lionel Messi", "Argentina", 8, 1, messi_gpg, 0.22, 435),
        ("Kylian Mbappé", "France", 7, 2, mbappe_gpg, 0.27, 435),
        ("Erling Haaland", "Norway", 7, 0, haaland_gpg, 0.08, 355),
        ("Harry Kane", "England", 6, 1, kane_gpg, 0.17, 435),
        ("Ousmane Dembélé", "France", 4, 2, 0.44, 0.28, 425),
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.50, 0.20, 415),
        ("Jude Bellingham", "England", 4, 1, 0.38, 0.22, 390),
        ("Johan Manzambi", "Switzerland", 3, 2, 0.34, 0.16, 340),
        ("Ismael Saibari", "Morocco", 3, 0, 0.32, 0.15, 392),
        ("Charles De Ketelaere", "Belgium", 2, 0, 0.45, 0.18, 320),
        ("Leandro Trossard", "Belgium", 2, 3, 0.38, 0.22, 440),
        ("Azzedine Ounahi", "Morocco", 2, 0, 0.28, 0.18, 440),
        ("Bradley Barcola", "France", 2, 0, 0.35, 0.22, 345),
        ("Julián Álvarez", "Argentina", 2, 1, 0.44, 0.18, 390),
        ("Breel Embolo", "Switzerland", 2, 2, 0.36, 0.16, 440),
        ("Lamine Yamal", "Spain", 1, 1, 0.34, 0.36, 395),
        ("Field", "NONE", 0, 0, 0, 0, 350),
    ]

    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.90), ("Other_ARG", 0.10)],
        "France": [("Kylian Mbappé", 0.62), ("Michael Olise", 0.23), ("Ousmane Dembélé", 0.10), ("Other_FRA", 0.05)],
        "Spain": [("Lamine Yamal", esp_yamal_share), ("Pedri", 0.26), ("Mikel Oyarzabal", 0.11), ("Unai Simón", 0.10), ("Other_ESP", round(1.0 - esp_yamal_share - 0.47, 2))],
        "England": [("Jude Bellingham", 0.47), ("Harry Kane", 0.41), ("Other_ENG", 0.12)],
        "Norway": [("Erling Haaland", 0.86), ("Martin Ødegaard", 0.09), ("Other_NOR", 0.05)],
        "Morocco": [("Achraf Hakimi", 0.42), ("Brahim Díaz", 0.22), ("Yassine Bounou", 0.20), ("Azzedine Ounahi", 0.16)],
        "Switzerland": [("Gregor Kobel", 0.32), ("Granit Xhaka", 0.32), ("Johan Manzambi", 0.22), ("Other_SUI", 0.14)],
        "Belgium": [("Charles De Ketelaere", 0.32), ("Thibaut Courtois", 0.26), ("Leandro Trossard", 0.22), ("Other_BEL", 0.20)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.38,  # Messi 8g/1a + iconic Egypt comeback
        "France": 1.28,     # Mbappe 7g/2a + Olise 5a (market #1 favorite)
        "Norway": 1.20,
        "England": 1.13,
        "Spain": 1.06,
        "Morocco": 0.96,
        "Belgium": 0.90,
        "Switzerland": 0.85,
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

        sf1_ma = mar_saibari_late if w97 == "Morocco" else 0
        sf1_mb = bel_onana if w98 == "Belgium" else 0
        w101, l101 = play_ko(w97, w98, mod_a=sf1_ma, mod_b=sf1_mb)

        sf2_mb = sui_inj_late if w100 == "Switzerland" else 0
        w102, l102 = play_ko(w99, w100, mod_a=0, mod_b=sf2_mb)

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
        for t, ms in team_matches.items():
            ko_games_sum[t] += len(ms)

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
            if pname == "Ismael Saibari" and len(ms) > 0 and random.random() < 0.78:
                ms = ms[1:]
            if pname == "Johan Manzambi" and len(ms) > 0 and random.random() < 0.70:
                ms = ms[1:]
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

        # GOLDEN BALL MODEL 1: Pure Team Finish
        r = random.random()
        if r < 0.55: gb_team = w104
        elif r < 0.85: gb_team = l104
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
        f4_items = [(w104, 0.50), (l104, 0.32), (w103, 0.12), (l103, 0.06)]
        gb_winner_team = None
        for pname, team, *_ in players:
            if pname == best_name:
                gb_winner_team = team; break
        weights = []
        for t, bw in f4_items:
            sm = TEAM_STAR_MULT.get(t, 0.85)
            gb_bonus = 1.30 if t == gb_winner_team else 1.0
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
            adj = [(pl, sh * (1.75 if pl == best_name else 0.75)) for pl, sh in shares2]
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
    print("  QF_Boston   :", ", ".join(f"{k}:{v:.4f}" for k, v in out["QF_Boston"].items()))
    print("  QF_LA       :", ", ".join(f"{k}:{v:.4f}" for k, v in out["QF_LA"].items()))
    print("  QF_Miami    :", ", ".join(f"{k}:{v:.4f}" for k, v in out["QF_Miami"].items()))
    print("  QF_KC       :", ", ".join(f"{k}:{v:.4f}" for k, v in out["QF_KC"].items()))
    print("  GOLDEN_BOOT :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(6)))
    return out

r1 = run_sim("1. BASE BAYESIAN+MARKET BLEND", ELO_BASE, scale=410.0, sigma=44.0,
             fra_tchou_qf=-2, mar_saibari_qf=-14, mar_saibari_late=-7, bel_onana=-14,
             eng_quansah_qf=-5, arg_kc_crowd=5, sui_fatigue_qf=-10, sui_inj_qf=-10, sui_inj_late=-5,
             messi_gpg=0.70, mbappe_gpg=0.85, haaland_gpg=0.94, kane_gpg=0.73,
             win_goal_ratio=1.75, esp_yamal_share=0.45, N=200000)

r2 = run_sim("2. MARKET-ANCHORED (FanDuel Jul 7 QFs)", ELO_MARKET, scale=400.0, sigma=38.0,
             fra_tchou_qf=-2, mar_saibari_qf=-14, mar_saibari_late=-7, bel_onana=-14,
             eng_quansah_qf=-4, arg_kc_crowd=4, sui_fatigue_qf=-9, sui_inj_qf=-8, sui_inj_late=-4,
             messi_gpg=0.68, mbappe_gpg=0.84, haaland_gpg=0.90, kane_gpg=0.72,
             win_goal_ratio=1.60, esp_yamal_share=0.43, N=200000)

r3 = run_sim("3. PURE BAYESIAN (Spain 6 CS, ARG 2.90 xG, NOR form)", ELO_PURE, scale=410.0, sigma=44.0,
             fra_tchou_qf=-3, mar_saibari_qf=-15, mar_saibari_late=-7, bel_onana=-16,
             eng_quansah_qf=-6, arg_kc_crowd=7, sui_fatigue_qf=-12, sui_inj_qf=-12, sui_inj_late=-6,
             messi_gpg=0.73, mbappe_gpg=0.86, haaland_gpg=0.98, kane_gpg=0.75,
             win_goal_ratio=1.85, esp_yamal_share=0.48, N=150000)

r4 = run_sim("4. UPSET-CONSERVATIVE (wider sigma, SUI/NOR/MAR/BEL resilience)", ELO_CONSERVATIVE, scale=425.0, sigma=50.0,
             fra_tchou_qf=-4, mar_saibari_qf=-12, mar_saibari_late=-5, bel_onana=-12,
             eng_quansah_qf=-6, arg_kc_crowd=3, sui_fatigue_qf=-8, sui_inj_qf=-8, sui_inj_late=-4,
             messi_gpg=0.66, mbappe_gpg=0.83, haaland_gpg=0.92, kane_gpg=0.71,
             win_goal_ratio=1.70, esp_yamal_share=0.44, N=150000)

weights = [(r1, 0.35), (r2, 0.30), (r3, 0.20), (r4, 0.15)]
print("\n==================== WEIGHTED ENSEMBLE v2 (35/30/20/15) ====================")
ens = {}
for key in ["QF_Boston", "QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final", "GOLDEN_BOOT"]:
    agg = Counter()
    for res, wt in weights:
        for k, v in res[key].items():
            agg[k] += wt * v
    ens[key] = dict(agg)
    top = agg.most_common(8)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in top))

# GOLDEN BALL: 3-model blend = 35% Bracket-Team + 35% Bracket-Star+GB + 30% Oddschecker-Market-Bayes
agg_gb_sim = Counter()
for res, wt in weights:
    for k, v in res["GBALL_TEAM"].items():
        agg_gb_sim[k] += wt * 0.45 * v
    for k, v in res["GBALL_STAR"].items():
        agg_gb_sim[k] += wt * 0.55 * v

# Oddschecker July 6 vig-free priors updated for July 7 bracket/GB shifts:
# Jul 6 vig-free Oddschecker: Mbappe 25.5%, Messi 17.5%, Olise 9.8%, Yamal 8.5%, Bellingham 6.8%, Haaland 7.0%, Kane 6.5%
# Jul 7 updates:
#   Messi: ARG Final 32.5->42.2% (+30%), GB 30.5->46.0% (+51%) -> ~23.5%
#   Mbappe: FRA Final flat 44.5->44.8%, GB 38.5->32.5% (-15%) -> ~23.0%
#   Yamal: ESP Final flat 38.5->38.5%, De la Fuente praise -> ~8.8%
#   Olise: FRA Final flat -> ~9.2%
#   Bellingham: ENG Final 32.0->33.1%, 44% bet share -> ~7.2%
#   Kane: ENG Final 32.0->33.1%, GB 11.8->8.3% -> ~6.0%
#   Haaland: NOR Final 16.5->13.7%, GB 17.5->12.5% -> ~5.5%
#   Pedri: ESP Final flat -> ~5.0%
oddschecker_jul7 = {
    "Lionel Messi": 0.235,
    "Kylian Mbappé": 0.230,
    "Michael Olise": 0.092,
    "Lamine Yamal": 0.088,
    "Jude Bellingham": 0.072,
    "Harry Kane": 0.060,
    "Erling Haaland": 0.055,
    "Pedri": 0.050,
    "Ousmane Dembélé": 0.025,
    "Mikel Oyarzabal": 0.018,
}

agg_gb_final = Counter()
all_pls = set(agg_gb_sim.keys()) | set(oddschecker_jul7.keys())
for pl in all_pls:
    agg_gb_final[pl] = 0.70 * agg_gb_sim.get(pl, 0.0) + 0.30 * oddschecker_jul7.get(pl, 0.0)

print("  GBALL_SIM   : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb_sim.most_common(10)))
print("  GBALL_BLEND : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb_final.most_common(10)))
