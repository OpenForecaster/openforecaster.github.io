import random, math
from collections import Counter

# ==============================================================================
# JULY 4, 2026 WORLD CUP SIMULATION
#
# All 16 R32 Matches COMPLETE (including Jul 3 late matches):
#   M86 (Jul 03): Argentina 3-2 Cape Verde AET (Messi 29' [7g], Duarte 59',
#                 L.Martinez 92', Lopes Cabral 103', Diney Borges 111' OG off Romero/Messi corner)
#   M87 (Jul 03): Colombia 1-0 Ghana (Jhon Arias 14' [assist L.Suarez]; Cordoba groin inj 8')
#
# First 2 R16 Matches COMPLETE (Jul 04):
#   M90 (Jul 04, Houston): Morocco 3-0 Canada (Ounahi 50', 82', Rahimi 90+8';
#                          Hakimi 1a, Brahim Diaz 2a; Saibari hamstring inj 22' - major doubt QF!)
#   M89 (Jul 04, Philadelphia): France 1-0 Paraguay (Mbappe 70' pen [7g/2a], won by Doue;
#                          38-39C heat; Tchouameni thigh & Thuram calf missed match)
#
# LOCKED QF1 (Boston, M97, Thu Jul 9): FRANCE vs MOROCCO (Canada & Paraguay ELIMINATED!)
#
# Remaining 6 R16 Matches & FanDuel July 4 "To Qualify" Vig-Free Implied Probs:
#   M91 (Sun Jul 5, NJ):        Brazil -270 / Norway +210       -> 69.35% BRA / 30.65% NOR
#   M92 (Sun Jul 5, Azteca 6p): England -138 / Mexico +113      -> 55.26% ENG / 44.74% MEX
#   M93 (Mon Jul 6, Dallas):    Spain -225 / Portugal +179      -> 65.89% ESP / 34.11% POR
#   M94 (Mon Jul 6, Seattle):   Belgium -118 / USA -104         -> 51.50% BEL / 48.50% USA
#   M95 (Tue Jul 7, Atlanta):   Argentina -800 / Egypt +530     -> 84.85% ARG / 15.15% EGY
#   M96 (Tue Jul 7, Vancouver): Colombia -166 / Switzerland+136 -> 59.56% COL / 40.44% SUI
# ==============================================================================

# 1. BASE BAYESIAN + MARKET BLEND (~60% Bayesian Elo / ~40% July 4 Market)
ELO_BASE = {
    "France": 2158,       # 5-0-0 (14-2 GD), 2 straight KO clean sheets; -7 for Tchouameni/Thuram doubts & tight 1-0 in heat
    "Spain": 2115,        # +5: 3-0 Austria (0 SOT allowed), 0 GA in 4, FD -225 vs POR
    "Argentina": 2092,    # Survived CPV 3-2 AET (defensive fragility + 120m fatigue, but still -800 vs EGY)
    "Brazil": 2045,       # +20: Raphinha back in training, Vini 4g, FD -270 (69.3%) vs NOR
    "England": 2038,      # -7: Rice/Saka knocks, James/Quansah out, <48h Azteca acclimatization (kickoff stays 6pm, NOT noon)
    "Portugal": 2005,     # -10: laboured 2-1 vs CRO, FD +179 (34.1%) vs ESP
    "Colombia": 1995,     # +10: dominant 1-0 vs GHA (FD -166 vs SUI); minor Cordoba groin injury
    "Morocco": 1980,      # +25 base strength (FD -330 vs CAN, 3-0 win, FIFA #6) -- minus Saibari QF injury mod (-20 in M97, -10 later)
    "Norway": 1925,       # -20: market recalibration (FD +210 = 30.7% vs BRA)
    "Switzerland": 1925,  # Unbeaten 3W 1D, 2-0 ALG, stays in Vancouver (+10 venue)
    "Mexico": 1925,       # +10: 4-0-0, 0 GA; Azteca venue bonus (+70 in M92 ONLY, 0 away from Azteca!)
    "Belgium": 1905,      # 5 days rest since Jul 1 (minimal fatigue -3); FD -118 vs USA
    "United States": 1900,# +25 USA home; -20 Balogun suspended M94
    "Egypt": 1788,        # -7: 120m+pens vs AUS, Salah off-colour, injuries, FD +530 vs ARG
}

# 2. MARKET-ANCHORED (tightly matches all 6 remaining FanDuel July 4 R16 lines!)
ELO_MARKET = {
    "France": 2162,
    "Spain": 2118,
    "Argentina": 2095,
    "Brazil": 2055,
    "England": 2035,
    "Portugal": 2002,
    "Colombia": 2000,
    "Morocco": 1978,
    "Mexico": 1922,       # +76 Azteca -> ENG-MEX = 55.3%
    "Switzerland": 1924,  # +8 Vancouver -> COL-SUI = 59.5%
    "Norway": 1915,       # BRA-NOR = 69.1%
    "Belgium": 1908,      # BEL-USA = 51.4% (with USA +25-22, BEL -2)
    "United States": 1900,
    "Egypt": 1788,        # ARG-EGY = 84.9%
}

# 3. PURE BAYESIAN / JULY-3-CLOSER (minimal drift from July 3 Elos; tests sensitivity to market moves)
ELO_PURE = {
    "France": 2165,
    "Spain": 2110,
    "Argentina": 2100,
    "England": 2048,
    "Brazil": 2030,
    "Portugal": 2012,
    "Colombia": 1988,
    "Morocco": 1970,
    "Norway": 1940,
    "Switzerland": 1925,
    "Mexico": 1918,       # +58 Azteca -> ENG-MEX = 59.8%
    "Belgium": 1905,
    "United States": 1900,
    "Egypt": 1795,
}

# 4. UPSET-CONSERVATIVE / CAUTIOUS FRA & ARG (wider variance, stronger Morocco/Mexico/Portugal/Switzerland)
ELO_CONSERVATIVE = {
    "France": 2148,
    "Spain": 2105,
    "Argentina": 2082,
    "Brazil": 2040,
    "England": 2032,
    "Portugal": 2008,
    "Colombia": 1990,
    "Morocco": 1982,      # Smaller Saibari hit (-14) -> MAR ~27% vs FRA
    "Norway": 1928,
    "Switzerland": 1928,
    "Mexico": 1928,       # +72 Azteca -> ENG-MEX ~54.3%
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
            azteca_bonus=70, usa_balogun_mod=-20, bel_r16_mod=-3,
            sui_van_bonus=10, mar_saibari_qf=-20, mar_saibari_late=-10,
            arg_et_fatigue_r16=-5,
            messi_assist_prob=0.40,
            esp_yamal_share=0.58,
            N=200000, seed=20260704):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"
    ]}
    ko_games_sum = Counter()
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    # Active players as of July 4 (post M86, M87, M89, M90):
    # (name, team, curr_g, curr_a, gpg, apg, curr_mins)
    # Note: Canada (Jonathan David) eliminated; Saibari injured (hamstring)
    players = [
        ("Kylian Mbappé", "France", 7, 2, 0.86, 0.27, 435),     # UPDATED: 70' pen vs PAR -> 7g/2a, 5 games (~435m)
        ("Lionel Messi", "Argentina", 7, 0, 0.69, 0.25, 320),   # UPDATED: 7g, 0-1a (handled via messi_assist_prob), 4 games (~320m)
        ("Harry Kane", "England", 5, 0, 0.72, 0.16, 345),
        ("Erling Haaland", "Norway", 5, 0, 0.84, 0.12, 270),
        ("Ousmane Dembélé", "France", 4, 2, 0.44, 0.28, 425),   # UPDATED: blanked vs PAR, ~425m, only QF+ left
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.52, 0.20, 330),
        ("Vinícius Júnior", "Brazil", 4, 1, 0.55, 0.25, 355),
        ("Johan Manzambi", "Switzerland", 3, 2, 0.34, 0.16, 340),
        ("Julián Quiñones", "Mexico", 3, 1, 0.42, 0.20, 340),
        ("Matheus Cunha", "Brazil", 3, 0, 0.36, 0.15, 330),
        ("Cristiano Ronaldo", "Portugal", 3, 0, 0.40, 0.10, 351),
        ("Folarin Balogun", "United States", 3, 0, 0.42, 0.12, 315), # Suspended M94
        ("Ismael Saibari", "Morocco", 3, 0, 0.32, 0.15, 392),   # Hamstring inj 22' vs CAN -> likely misses M97!
        ("Azzedine Ounahi", "Morocco", 2, 0, 0.28, 0.18, 440),  # 2g vs CAN
        ("Leandro Trossard", "Belgium", 2, 2, 0.38, 0.22, 360),
        ("Bradley Barcola", "France", 2, 0, 0.35, 0.22, 345),
        ("Jude Bellingham", "England", 2, 1, 0.32, 0.22, 300),
        ("Lamine Yamal", "Spain", 1, 1, 0.35, 0.38, 305),
        ("Field", "NONE", 0, 0, 0, 0, 300),
    ]

    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.88), ("Other_ARG", 0.12)], # Carrying team + 20th WC goal narrative
        "France": [("Kylian Mbappé", 0.55), ("Michael Olise", 0.23), ("Ousmane Dembélé", 0.16), ("Other_FRA", 0.06)],
        "Spain": [("Lamine Yamal", esp_yamal_share), ("Pedri", 0.20), ("Mikel Oyarzabal", 0.12), ("Other_ESP", round(1.0 - esp_yamal_share - 0.32, 2))],
        "England": [("Harry Kane", 0.52), ("Jude Bellingham", 0.30), ("Other_ENG", 0.18)],
        "Brazil": [("Vinícius Júnior", 0.60), ("Raphinha", 0.16), ("Neymar", 0.06), ("Other_BRA", 0.18)],
        "Portugal": [("Bruno Fernandes", 0.38), ("Vitinha", 0.24), ("Cristiano Ronaldo", 0.20), ("Other_POR", 0.18)],
        "Norway": [("Erling Haaland", 0.82), ("Other_NOR", 0.18)],
        "Colombia": [("Luis Díaz", 0.45), ("James Rodríguez", 0.33), ("Jhon Arias", 0.12), ("Other_COL", 0.10)],
        "Morocco": [("Achraf Hakimi", 0.44), ("Yassine Bounou", 0.24), ("Azzedine Ounahi", 0.18), ("Brahim Díaz", 0.14)],
        "Switzerland": [("Johan Manzambi", 0.35), ("Granit Xhaka", 0.35), ("Other_SUI", 0.30)],
        "Mexico": [("Julián Quiñones", 0.45), ("Raúl Jiménez", 0.25), ("Other_MEX", 0.30)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.40,
        "France": 1.22,
        "Spain": 1.08,
        "England": 1.02,
        "Brazil": 1.05,
        "Portugal": 0.94,
        "Norway": 1.14,
        "Morocco": 0.96,
        "Colombia": 0.90,
        "Switzerland": 0.88,
        "Mexico": 0.92,
    }

    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} (scale={scale}, sigma={sigma}) ====================")
    print(f"  LOCKED QF1: FRA-MAR(Saib{mar_saibari_qf})={base_p('France','Morocco',0,mar_saibari_qf):.3f}")
    print(f"  Rem R16: BRA-NOR={base_p('Brazil','Norway'):.3f} | ENG-MEX(Azt+{azteca_bonus})={base_p('England','Mexico',0,azteca_bonus):.3f} | ESP-POR={base_p('Spain','Portugal'):.3f}")
    print(f"           BEL-USA={base_p('Belgium','United States',bel_r16_mod,25+usa_balogun_mod):.3f} | ARG-EGY={base_p('Argentina','Egypt',arg_et_fatigue_r16,0):.3f} | COL-SUI={base_p('Colombia','Switzerland',0,sui_van_bonus):.3f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        def play_ko(a, b, venue=None, mod_a=0, mod_b=0):
            ba = mod_a; bb = mod_b
            if venue == "Azteca":
                if a == "Mexico": ba += azteca_bonus
                if b == "Mexico": bb += azteca_bonus
            elif venue == "USA":
                if a == "United States": ba += 25
                if b == "United States": bb += 25
            elif venue == "Vancouver":
                if a == "Switzerland": ba += sui_van_bonus
                if b == "Switzerland": bb += sui_van_bonus
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / scale))
            return (a, b) if random.random() < p else (b, a)

        team_opps = {}
        def record_match(a, b):
            team_opps.setdefault(a, []).append(base_elo[b])
            team_opps.setdefault(b, []).append(base_elo[a])

        # CONFIRMED R16 WINNERS (July 4):
        w = {
            "M89": "France",
            "M90": "Morocco",
        }
        counts["Reach_QF"]["France"] += 1
        counts["Reach_QF"]["Morocco"] += 1

        # REMAINING 6 R16 MATCHES:
        r16_pairs = [
            ("M91", "Brazil", "Norway", None, 0, 0),
            ("M92", "Mexico", "England", "Azteca", 0, 0),
            ("M93", "Portugal", "Spain", None, 0, 0),
            ("M94", "United States", "Belgium", "USA", usa_balogun_mod, bel_r16_mod),
            ("M95", "Argentina", "Egypt", None, arg_et_fatigue_r16, 0),
            ("M96", "Switzerland", "Colombia", "Vancouver", 0, 0),
        ]
        for mid, a, b, v, ma, mb in r16_pairs:
            record_match(a, b)
            w[mid], _ = play_ko(a, b, venue=v, mod_a=ma, mod_b=mb)
            counts["Reach_QF"][w[mid]] += 1

        # QUARTERFINALS:
        qf_pairs = [
            ("M97", w["M89"], w["M90"], None, 0, mar_saibari_qf),   # Boston QF: France vs Morocco
            ("M98", w["M93"], w["M94"], "USA", 0, 0),               # LA QF
            ("M99", w["M91"], w["M92"], None, 0, 0),                # Miami QF (no Azteca!)
            ("M100", w["M95"], w["M96"], None, 0, 0),               # Kansas City QF
        ]
        for mid, a, b, v, ma, mb in qf_pairs:
            record_match(a, b)
            w[mid], _ = play_ko(a, b, venue=v, mod_a=ma, mod_b=mb)
            counts["Reach_SF"][w[mid]] += 1

        counts["QF_Boston"][w["M97"]] += 1
        counts["QF_KC"][w["M100"]] += 1

        # SEMIFINALS:
        sf1_ma = mar_saibari_late if w["M97"] == "Morocco" else 0
        record_match(w["M97"], w["M98"])
        w101, l101 = play_ko(w["M97"], w["M98"], venue="USA", mod_a=sf1_ma)
        record_match(w["M99"], w["M100"])
        w102, l102 = play_ko(w["M99"], w["M100"])

        counts["SF1_Dallas"][w101] += 1
        counts["SF2_Atlanta"][w102] += 1
        counts["Reach_Final"][w101] += 1
        counts["Reach_Final"][w102] += 1

        # THIRD PLACE & FINAL:
        tp_ma = mar_saibari_late if l101 == "Morocco" else 0
        fin_ma = mar_saibari_late if w101 == "Morocco" else 0
        record_match(l101, l102)
        w103, l103 = play_ko(l101, l102, mod_a=tp_ma)
        record_match(w101, w102)
        w104, l104 = play_ko(w101, w102, mod_a=fin_ma)

        counts["ThirdPlace"][w103] += 1
        counts["Champion"][w104] += 1
        for t, opps in team_opps.items():
            ko_games_sum[t] += len(opps)

        # GOLDEN BOOT:
        best_key = (-1, -1, -9999)
        best_name = None
        for pname, team, cg, ca, gpg, apg, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(2.2)
                key = (fg, poisson(1.2), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg
            assists = ca + (1 if (pname == "Lionel Messi" and random.random() < messi_assist_prob) else 0)
            mins = gmins
            opps = list(team_opps.get(team, []))
            if pname == "Folarin Balogun" and len(opps) > 0:
                opps = opps[1:] # Suspended R16
            if pname == "Ismael Saibari" and len(opps) > 0:
                # Major doubt for QF (80% misses QF, 40% misses SF)
                if random.random() < 0.80:
                    opps = opps[1:]
            miss_p = 0.05 if pname == "Lionel Messi" else 0.025
            eff_opps = [oe for oe in opps if random.random() > miss_p]
            eff_ng = len(eff_opps)
            if eff_ng > 0:
                mult = max(0.35, random.gauss(1.0, 0.25))
                exp_g = 0.0
                for oe in eff_opps:
                    opp_mult = max(0.75, min(1.38, 1.0 + (1920.0 - oe) / 420.0))
                    exp_g += gpg * mult * opp_mult
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
            gb_bonus = 1.30 if t == gb_winner_team else 1.0
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

    print("  Exp rem games:", {t: round(ko_games_sum[t]/N, 2) for t in ["France", "Morocco", "Argentina", "Spain", "Brazil", "England", "Portugal", "Colombia", "Switzerland", "Norway", "Mexico", "Egypt"]})
    out = {}
    for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"]:
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
             azteca_bonus=70, usa_balogun_mod=-20, bel_r16_mod=-3, sui_van_bonus=10,
             mar_saibari_qf=-20, mar_saibari_late=-10, arg_et_fatigue_r16=-5, messi_assist_prob=0.40, N=200000)

r2 = run_sim("2. MARKET-ANCHORED (exact FD Jul 4 lines)", ELO_MARKET, scale=400.0, sigma=42.0,
             azteca_bonus=76, usa_balogun_mod=-22, bel_r16_mod=-2, sui_van_bonus=8,
             mar_saibari_qf=-22, mar_saibari_late=-10, arg_et_fatigue_r16=-2, messi_assist_prob=0.50, N=200000)

r3 = run_sim("3. PURE BAYESIAN (Jul 3 Elos + locked results)", ELO_PURE, scale=410.0, sigma=48.0,
             azteca_bonus=58, usa_balogun_mod=-18, bel_r16_mod=-6, sui_van_bonus=10,
             mar_saibari_qf=-18, mar_saibari_late=-8, arg_et_fatigue_r16=-5, messi_assist_prob=0.0, N=150000)

r4 = run_sim("4. UPSET-CONSERVATIVE (wider sigma, strong MAR/MEX/SUI)", ELO_CONSERVATIVE, scale=425.0, sigma=55.0,
             azteca_bonus=72, usa_balogun_mod=-20, bel_r16_mod=-4, sui_van_bonus=10,
             mar_saibari_qf=-14, mar_saibari_late=-6, arg_et_fatigue_r16=-8, messi_assist_prob=0.40, N=150000)

# Weighted Ensemble: 35% Base + 35% Market + 15% Pure + 15% Conservative
weights = [(r1, 0.35), (r2, 0.35), (r3, 0.15), (r4, 0.15)]
print("\n==================== WEIGHTED ENSEMBLE (35/35/15/15) ====================")
for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "GOLDEN_BOOT"]:
    agg = Counter()
    for res, wt in weights:
        for k, v in res[key].items():
            agg[k] += wt * v
    top = agg.most_common(7)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in top))

# Golden Ball combined: 50% GBALL_TEAM + 50% GBALL_STAR across ensemble
agg_gb = Counter()
for res, wt in weights:
    for k, v in res["GBALL_TEAM"].items():
        agg_gb[k] += wt * 0.5 * v
    for k, v in res["GBALL_STAR"].items():
        agg_gb[k] += wt * 0.5 * v
print("  GOLDEN_BALL : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb.most_common(8)))
