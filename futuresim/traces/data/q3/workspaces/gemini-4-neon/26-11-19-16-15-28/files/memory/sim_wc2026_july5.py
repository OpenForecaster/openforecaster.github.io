import random, math
from collections import Counter

# ==============================================================================
# JULY 5, 2026 WORLD CUP SIMULATION
#
# 3 of 8 R16 Matches COMPLETE:
#   M89 (Jul 04, Philadelphia): France 1-0 Paraguay (Mbappe 70' pen [7g/2a])
#   M90 (Jul 04, Houston):      Morocco 3-0 Canada (Ounahi 50', 82', Rahimi 90+8';
#                               Saibari hamstring inj 21' & Chadi Riad major doubts QF)
#   M91 (Jul 05, NJ/NY):        NORWAY 2-1 BRAZIL!! (Haaland 79', 90' [7g/0a], both
#                               assisted by Schjelderup; Nyland saved Bruno Guimaraes pen;
#                               Neymar 90+10 pen; Ryerson returned; BRAZIL ELIMINATED!)
#
# LOCKED QF1 (Boston, M97, Thu Jul 9): FRANCE vs MOROCCO
#   - Opta Jul 5: France 74.9% / Morocco 25.1%
#   - Sportsbooks Jul 5: FRA -190 / Draw +380 / MAR +525 -> ~75.6% / 24.4% to qualify
#
# PARTIALLY LOCKED QF3 (Miami, M99, Sat Jul 11): NORWAY vs winner(England/Mexico)
#
# Remaining 5 R16 Matches:
#   M92 (Sun Jul 5, Azteca, delayed 1hr by lightning): England vs Mexico
#       - Confirmed XIs: Quansah, Rice, Saka, Gordon, Bellingham, Kane ALL START!
#       - Mexico unchanged (4-0-0, 0 GA); FIFA ADI 39/31/32 (~53.4% ENG); FD ~55.3% ENG
#   M93 (Mon Jul 6, Dallas):    Spain -225 / Portugal +179      -> 65.89% ESP / 34.11% POR
#   M94 (Mon Jul 6, Seattle):   USA vs Belgium — BALOGUN BAN SUSPENDED BY FIFA!
#       - Previously BEL -118 / USA -104 (51.5% / 48.5%) with Balogun suspended (-20 Elo)
#       - With Balogun (3g in 3 starts) cleared -> USA flips to slight ~52.5-53.5% fav!
#   M95 (Tue Jul 7, Atlanta):   Argentina -800 / Egypt +530     -> 84.85% ARG / 15.15% EGY
#       - Both played 120m; Messi tired, Salah nursing hamstring concern
#   M96 (Tue Jul 7, Vancouver): Colombia -166 / Switzerland+136 -> 59.56% COL / 40.44% SUI
# ==============================================================================

# 1. BASE BAYESIAN + MARKET BLEND
ELO_BASE = {
    "France": 2158,       # Opta 74.9% vs MAR; 5-0-0 (14-2 GD), no QF suspensions
    "Spain": 2115,        # Unbeaten in 34 (25W 9D), FD -225 vs POR
    "Argentina": 2092,    # 120m vs CPV, FD -800 vs EGY (Salah hamstring)
    "England": 2042,      # +4 recovery: Quansah, Rice, Saka ALL starting vs MEX
    "Portugal": 2005,     # FD +179 vs ESP
    "Colombia": 1995,     # FD -166 vs SUI
    "Morocco": 1980,      # Both Saibari & Chadi Riad major doubts (-20 QF, -10 later)
    "Norway": 1965,       # +40 Bayesian update: beat Brazil 2-1 on merit, Ryerson back, Haaland on fire
    "Switzerland": 1925,  # +10 Vancouver venue
    "Mexico": 1925,       # +70 Azteca ONLY (slight +8 Miami crowd vs NOR)
    "Belgium": 1905,      # -3 minimal rest/distraction
    "United States": 1900,# +25 USA home; Balogun CLEARED (0 penalty!)
    "Egypt": 1788,        # Salah hamstring + 120m+pens
}

# 2. MARKET-CAUTIOUS (slightly conservative on Norway regression, ADI/FD-tight on ENG-MEX)
ELO_MARKET = {
    "France": 2162,
    "Spain": 2118,
    "Argentina": 2095,
    "England": 2038,
    "Portugal": 2002,
    "Colombia": 2000,
    "Morocco": 1978,
    "Norway": 1950,       # +35 from 1915 (more regression toward pre-R16 market)
    "Mexico": 1924,       # +76 Azteca -> ENG-MEX ~55.4%
    "Switzerland": 1924,
    "Belgium": 1908,
    "United States": 1900,
    "Egypt": 1788,
}

# 3. PURE BAYESIAN / FORM-RESPONSIVE (rewards Norway beating Brazil + stronger England XI)
ELO_PURE = {
    "France": 2165,
    "Spain": 2110,
    "Argentina": 2100,
    "England": 2050,
    "Portugal": 2012,
    "Colombia": 1988,
    "Morocco": 1975,
    "Norway": 1980,       # +40 from 1940: Norway on par with Morocco/Colombia
    "Switzerland": 1925,
    "Mexico": 1918,       # +60 Azteca -> ENG-MEX ~59.9%
    "Belgium": 1905,
    "United States": 1900,
    "Egypt": 1795,
}

# 4. UPSET-CONSERVATIVE (wider variance, stronger Morocco/Norway/Mexico/Switzerland)
ELO_CONSERVATIVE = {
    "France": 2148,
    "Spain": 2105,
    "Argentina": 2082,
    "England": 2035,
    "Portugal": 2008,
    "Colombia": 1990,
    "Morocco": 1982,
    "Norway": 1968,
    "Switzerland": 1928,
    "Mexico": 1928,
    "Belgium": 1902,
    "United States": 1900,
    "Egypt": 1792,
}

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=410.0, sigma=48.0,
            azteca_bonus=70, mex_miami_bonus=8, usa_balogun_mod=0, bel_r16_mod=-3,
            sui_van_bonus=10, mar_saibari_qf=-20, mar_saibari_late=-10,
            arg_et_fatigue_r16=-5,
            haaland_gpg=0.96, mbappe_gpg=0.85, messi_gpg=0.68, kane_gpg=0.72,
            win_goal_ratio=1.75,
            esp_yamal_share=0.58,
            N=200000, seed=20260705):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_KC", "QF_Miami", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"
    ]}
    ko_games_sum = Counter()
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    # Active players as of July 5 (post Norway 2-1 Brazil; Brazil ELIMINATED; Balogun CLEARED):
    # (name, team, curr_g, curr_a, gpg, apg, curr_mins)
    # Confirmed official Golden Boot standings:
    #   Mbappe 7g 2a (~435m), Messi 7g 0a (~345m), Haaland 7g 0a (~355m),
    #   Kane 5g 0a (~345m), Dembele 4g 2a (~425m), Oyarzabal 4g 1a (~330m)
    players = [
        ("Kylian Mbappé", "France", 7, 2, mbappe_gpg, 0.27, 435),
        ("Lionel Messi", "Argentina", 7, 0, messi_gpg, 0.21, 345),
        ("Erling Haaland", "Norway", 7, 0, haaland_gpg, 0.08, 355),
        ("Harry Kane", "England", 5, 0, kane_gpg, 0.16, 345),
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.52, 0.20, 330),
        ("Ousmane Dembélé", "France", 4, 2, 0.44, 0.28, 425),
        ("Johan Manzambi", "Switzerland", 3, 2, 0.34, 0.16, 340),
        ("Julián Quiñones", "Mexico", 3, 1, 0.42, 0.20, 340),
        ("Cristiano Ronaldo", "Portugal", 3, 0, 0.40, 0.10, 351),
        ("Folarin Balogun", "United States", 3, 0, 0.45, 0.12, 315), # CLEARED for M94!
        ("Ismael Saibari", "Morocco", 3, 0, 0.32, 0.15, 392),        # Major doubt M97
        ("Azzedine Ounahi", "Morocco", 2, 0, 0.28, 0.18, 440),
        ("Leandro Trossard", "Belgium", 2, 2, 0.38, 0.22, 360),
        ("Bradley Barcola", "France", 2, 0, 0.35, 0.22, 345),
        ("Jude Bellingham", "England", 2, 1, 0.32, 0.22, 300),
        ("Lamine Yamal", "Spain", 1, 1, 0.35, 0.38, 305),
        ("Field", "NONE", 0, 0, 0, 0, 300),
    ]

    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.88), ("Other_ARG", 0.12)],
        "France": [("Kylian Mbappé", 0.55), ("Michael Olise", 0.23), ("Ousmane Dembélé", 0.16), ("Other_FRA", 0.06)],
        "Spain": [("Lamine Yamal", esp_yamal_share), ("Pedri", 0.20), ("Mikel Oyarzabal", 0.12), ("Other_ESP", round(1.0 - esp_yamal_share - 0.32, 2))],
        "England": [("Harry Kane", 0.52), ("Jude Bellingham", 0.30), ("Other_ENG", 0.18)],
        "Norway": [("Erling Haaland", 0.84), ("Martin Ødegaard", 0.10), ("Other_NOR", 0.06)],
        "Portugal": [("Bruno Fernandes", 0.38), ("Vitinha", 0.24), ("Cristiano Ronaldo", 0.20), ("Other_POR", 0.18)],
        "Colombia": [("Luis Díaz", 0.45), ("James Rodríguez", 0.33), ("Jhon Arias", 0.12), ("Other_COL", 0.10)],
        "Morocco": [("Achraf Hakimi", 0.44), ("Yassine Bounou", 0.24), ("Azzedine Ounahi", 0.18), ("Brahim Díaz", 0.14)],
        "Switzerland": [("Johan Manzambi", 0.35), ("Granit Xhaka", 0.35), ("Other_SUI", 0.30)],
        "Mexico": [("Julián Quiñones", 0.45), ("Raúl Jiménez", 0.25), ("Other_MEX", 0.30)],
        "United States": [("Christian Pulisic", 0.50), ("Folarin Balogun", 0.35), ("Other_USA", 0.15)],
        "Belgium": [("Thibaut Courtois", 0.30), ("Leandro Trossard", 0.30), ("Other_BEL", 0.40)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.40,
        "France": 1.22,
        "Norway": 1.22,   # Haaland 7g + historic upset narrative (like Forlan 2010 / Modric 2018)
        "Spain": 1.08,
        "England": 1.02,
        "Portugal": 0.94,
        "Morocco": 0.96,
        "Colombia": 0.90,
        "Switzerland": 0.88,
        "Mexico": 0.92,
    }

    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} (scale={scale}, sigma={sigma}) ====================")
    print(f"  LOCKED QF1: FRA-MAR(Saib{mar_saibari_qf})={base_p('France','Morocco',0,mar_saibari_qf):.3f}")
    print(f"  PROJ   QF3: ENG-NOR={base_p('England','Norway'):.3f} | NOR-MEX(Mia+{mex_miami_bonus})={base_p('Norway','Mexico',0,mex_miami_bonus):.3f}")
    print(f"  Rem R16: ENG-MEX(Azt+{azteca_bonus})={base_p('England','Mexico',0,azteca_bonus):.3f} | ESP-POR={base_p('Spain','Portugal'):.3f}")
    print(f"           USA-BEL(Bal{usa_balogun_mod})={base_p('United States','Belgium',25+usa_balogun_mod,bel_r16_mod):.3f} | ARG-EGY={base_p('Argentina','Egypt',arg_et_fatigue_r16,0):.3f} | COL-SUI={base_p('Colombia','Switzerland',0,sui_van_bonus):.3f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        team_matches = {} # team -> list of (opp_base_elo, won_bool, p_win)

        def play_ko(a, b, venue=None, mod_a=0, mod_b=0):
            ba = mod_a; bb = mod_b
            if venue == "Azteca":
                if a == "Mexico": ba += azteca_bonus
                if b == "Mexico": bb += azteca_bonus
            elif venue == "Miami":
                if a == "Mexico": ba += mex_miami_bonus
                if b == "Mexico": bb += mex_miami_bonus
            elif venue == "USA":
                if a == "United States": ba += 25
                if b == "United States": bb += 25
            elif venue == "Vancouver":
                if a == "Switzerland": ba += sui_van_bonus
                if b == "Switzerland": bb += sui_van_bonus
            p_a = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / scale))
            a_won = (random.random() < p_a)
            team_matches.setdefault(a, []).append((base_elo[b], a_won, p_a))
            team_matches.setdefault(b, []).append((base_elo[a], not a_won, 1.0 - p_a))
            return (a, b) if a_won else (b, a)

        # CONFIRMED R16 WINNERS (July 4 & July 5):
        w = {
            "M89": "France",
            "M90": "Morocco",
            "M91": "Norway",
        }
        counts["Reach_QF"]["France"] += 1
        counts["Reach_QF"]["Morocco"] += 1
        counts["Reach_QF"]["Norway"] += 1

        # REMAINING 5 R16 MATCHES:
        r16_pairs = [
            ("M92", "Mexico", "England", "Azteca", 0, 0),
            ("M93", "Portugal", "Spain", None, 0, 0),
            ("M94", "United States", "Belgium", "USA", usa_balogun_mod, bel_r16_mod),
            ("M95", "Argentina", "Egypt", None, arg_et_fatigue_r16, 0),
            ("M96", "Switzerland", "Colombia", "Vancouver", 0, 0),
        ]
        for mid, a, b, v, ma, mb in r16_pairs:
            w[mid], _ = play_ko(a, b, venue=v, mod_a=ma, mod_b=mb)
            counts["Reach_QF"][w[mid]] += 1

        # QUARTERFINALS:
        qf_pairs = [
            ("M97", w["M89"], w["M90"], None, 0, mar_saibari_qf),   # Boston QF: France vs Morocco
            ("M98", w["M93"], w["M94"], "USA", 0, 0),               # LA QF
            ("M99", w["M91"], w["M92"], "Miami", 0, 0),             # Miami QF: Norway vs ENG/MEX
            ("M100", w["M95"], w["M96"], None, 0, 0),               # Kansas City QF
        ]
        for mid, a, b, v, ma, mb in qf_pairs:
            w[mid], _ = play_ko(a, b, venue=v, mod_a=ma, mod_b=mb)
            counts["Reach_SF"][w[mid]] += 1

        counts["QF_Boston"][w["M97"]] += 1
        counts["QF_Miami"][w["M99"]] += 1
        counts["QF_KC"][w["M100"]] += 1

        # SEMIFINALS:
        sf1_ma = mar_saibari_late if w["M97"] == "Morocco" else 0
        w101, l101 = play_ko(w["M97"], w["M98"], venue="USA", mod_a=sf1_ma)
        w102, l102 = play_ko(w["M99"], w["M100"])

        counts["SF1_Dallas"][w101] += 1
        counts["SF2_Atlanta"][w102] += 1
        counts["Reach_Final"][w101] += 1
        counts["Reach_Final"][w102] += 1

        # THIRD PLACE & FINAL:
        tp_ma = mar_saibari_late if l101 == "Morocco" else 0
        fin_ma = mar_saibari_late if w101 == "Morocco" else 0
        w103, l103 = play_ko(l101, l102, mod_a=tp_ma)
        w104, l104 = play_ko(w101, w102, mod_a=fin_ma)

        counts["ThirdPlace"][w103] += 1
        counts["Champion"][w104] += 1
        for t, ms in team_matches.items():
            ko_games_sum[t] += len(ms)

        # GOLDEN BOOT (with unbiased goal-advancement correlation!):
        best_key = (-1, -1, -9999)
        best_name = None
        for pname, team, cg, ca, gpg, apg, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(2.0)
                key = (fg, poisson(1.2), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg
            assists = ca
            mins = gmins
            ms = list(team_matches.get(team, []))
            if pname == "Ismael Saibari" and len(ms) > 0:
                if random.random() < 0.80:
                    ms = ms[1:]
            miss_p = 0.05 if pname == "Lionel Messi" else 0.025
            eff_ms = [m for m in ms if random.random() > miss_p]
            eff_ng = len(eff_ms)
            if eff_ng > 0:
                mult = max(0.35, random.gauss(1.0, 0.25))
                exp_g = 0.0
                for oe, won, p_win in eff_ms:
                    opp_mult = max(0.75, min(1.38, 1.0 + (1920.0 - oe) / 420.0))
                    mu = gpg * mult * opp_mult
                    # Exact mean-preserving coupling with match outcome!
                    denom = 1.0 + p_win * (win_goal_ratio - 1.0)
                    mu_adj = (mu * win_goal_ratio / denom) if won else (mu / denom)
                    exp_g += mu_adj
                goals += poisson(exp_g)
                assists += poisson(eff_ng * apg)
            mins += eff_ng * (82 if pname == "Lionel Messi" else 87)
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
                gb_winner_team = team
                break
        weights = []
        for t, bw in f4_items:
            sm = TEAM_STAR_MULT.get(t, 0.85)
            gb_bonus = 1.32 if t == gb_winner_team else 1.0
            weights.append((t, bw * sm * gb_bonus))
        tot_w = sum(x[1] for x in weights)
        u = random.random() * tot_w; cum = 0.0
        gb_team2 = w104
        for t, wt in weights:
            cum += wt
            if u <= cum:
                gb_team2 = t
                break
        shares2 = list(TEAM_SHARES.get(gb_team2, [("Other_TEAM", 1.0)]))
        if gb_team2 == gb_winner_team and any(pl == best_name for pl, _ in shares2):
            adj = [(pl, sh * (1.8 if pl == best_name else 0.75)) for pl, sh in shares2]
            s_tot = sum(x[1] for x in adj)
            shares2 = [(pl, sh / s_tot) for pl, sh in adj]
        u = random.random(); cum = 0.0
        for pl, sh in shares2:
            cum += sh
            if u <= cum:
                gball_star_wins[pl] += 1
                break

    print("  Exp rem games:", {t: round(ko_games_sum[t]/N, 2) for t in ["France", "Morocco", "Argentina", "Spain", "England", "Norway", "Portugal", "Colombia", "Switzerland", "Mexico", "United States", "Belgium", "Egypt"]})
    out = {}
    for key in ["QF_Boston", "QF_KC", "QF_Miami", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"]:
        top = counts[key].most_common(8)
        out[key] = {t: cnt/N for t, cnt in top}
        s = ", ".join(f"{t}:{cnt/N:.4f}" for t, cnt in top)
        print(f"  {key:12s}: {s}")
    out["GOLDEN_BOOT"] = {n: c/N for n, c in gb_wins.most_common(8)}
    out["GBALL_TEAM"] = {n: c/N for n, c in gball_team_wins.most_common(8)}
    out["GBALL_STAR"] = {n: c/N for n, c in gball_star_wins.most_common(8)}
    print("  GOLDEN_BOOT :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(8)))
    print("  GBALL_TEAM  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_team_wins.most_common(8)))
    print("  GBALL_STAR  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_star_wins.most_common(8)))
    return out

r1 = run_sim("1. BASE BAYESIAN+MARKET BLEND", ELO_BASE, scale=410.0, sigma=48.0,
             azteca_bonus=70, mex_miami_bonus=8, usa_balogun_mod=0, bel_r16_mod=-3, sui_van_bonus=10,
             mar_saibari_qf=-20, mar_saibari_late=-10, arg_et_fatigue_r16=-5,
             haaland_gpg=0.96, win_goal_ratio=1.75, N=200000)

r2 = run_sim("2. MARKET-CAUTIOUS (regression on NOR, ADI/FD tight)", ELO_MARKET, scale=400.0, sigma=42.0,
             azteca_bonus=76, mex_miami_bonus=10, usa_balogun_mod=0, bel_r16_mod=-2, sui_van_bonus=8,
             mar_saibari_qf=-22, mar_saibari_late=-10, arg_et_fatigue_r16=-2,
             haaland_gpg=0.88, win_goal_ratio=1.60, N=200000)

r3 = run_sim("3. PURE BAYESIAN (form-responsive NOR 1980, ENG 2050)", ELO_PURE, scale=410.0, sigma=48.0,
             azteca_bonus=60, mex_miami_bonus=5, usa_balogun_mod=0, bel_r16_mod=-4, sui_van_bonus=10,
             mar_saibari_qf=-18, mar_saibari_late=-8, arg_et_fatigue_r16=-5,
             haaland_gpg=1.02, win_goal_ratio=1.85, N=150000)

r4 = run_sim("4. UPSET-CONSERVATIVE (wider sigma, strong MAR/NOR/MEX/SUI)", ELO_CONSERVATIVE, scale=425.0, sigma=55.0,
             azteca_bonus=74, mex_miami_bonus=8, usa_balogun_mod=0, bel_r16_mod=-3, sui_van_bonus=10,
             mar_saibari_qf=-14, mar_saibari_late=-6, arg_et_fatigue_r16=-8,
             haaland_gpg=0.94, win_goal_ratio=1.70, N=150000)

# Weighted Ensemble: 35% Base + 30% Market-Cautious + 20% Pure + 15% Conservative
weights = [(r1, 0.35), (r2, 0.30), (r3, 0.20), (r4, 0.15)]
print("\n==================== WEIGHTED ENSEMBLE (35/30/20/15) ====================")
for key in ["QF_Boston", "QF_KC", "QF_Miami", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "GOLDEN_BOOT"]:
    agg = Counter()
    for res, wt in weights:
        for k, v in res[key].items():
            agg[k] += wt * v
    top = agg.most_common(8)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in top))

agg_gb = Counter()
for res, wt in weights:
    for k, v in res["GBALL_TEAM"].items():
        agg_gb[k] += wt * 0.5 * v
    for k, v in res["GBALL_STAR"].items():
        agg_gb[k] += wt * 0.5 * v
print("  GOLDEN_BALL : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb.most_common(10)))
