import random, math
from collections import Counter

# ==============================================================================
# JULY 1, 2026 WORLD CUP SIMULATION
# Confirmed R32 Results (9 of 16 complete as of 2026-07-01 cutoff):
#   M73 (Jun 28): Canada 1-0 South Africa        -> Canada
#   M74 (Jun 29): Paraguay 1-1 Germany (4-3 p)   -> Paraguay (Germany OUT)
#   M75 (Jun 29): Morocco 1-1 Netherlands (3-2p) -> Morocco (Netherlands OUT)
#   M76 (Jun 29): Brazil 2-1 Japan AET           -> Brazil (Japan OUT)
#   M77 (Jun 30): France 3-0 Sweden              -> France (Sweden OUT)
#   M78 (Jun 30): Norway 2-1 Ivory Coast         -> Norway (Ivory Coast OUT)
#   M79 (Jun 30): Mexico 2-0 Ecuador             -> Mexico (Ecuador OUT)
#   M80 (Jul 01): England 2-1 DR Congo           -> England (DR Congo OUT; Kane 2g -> 5g!)
#   M82 (Jul 01): Belgium 3-2 Senegal AET        -> Belgium (Senegal OUT; 120 mins!)
#
# Remaining 7 R32 Matches (unplayed at 2026-07-01 cutoff, with FanDuel Jul 1 devigged):
#   M81 (Jul 01 8pm ET): USA (-600) vs Bosnia (+410)       -> FD 81.4%, Opta 76.6%
#   M83 (Jul 02 7pm ET): Portugal (-280) vs Croatia (+220) -> FD 70.2%
#   M84 (Jul 02 3pm ET): Spain (-950) vs Austria (+610)    -> FD 86.5%
#   M85 (Jul 02 11pm ET): Switzerland (-205) vs Algeria (+164) -> FD 64.0%
#   M86 (Jul 03 6pm ET): Argentina (-2000) vs Cape Verde (+1160) -> FD 92.3%
#   M87 (Jul 03 9:30pm ET): Colombia (-500) vs Ghana (+370) -> FD 79.7%
#   M88 (Jul 03 2pm ET): Egypt (-142) vs Australia (+116)  -> FD 55.9%
# ==============================================================================

# 1. Blended Fundamental + Market Elo (calibrated to Jul 1 FanDuel R32 + Winner/QF odds + Jul 1 results)
ELO_JULY1_BASE = {
    "France": 2165,       # 4-0-0, 13-2 GD, Saliba back, Mbappé 6g/2a, Olise 5a
    "Argentina": 2110,    # 3-0-0, Messi 6g, FD -2000 vs CPV, FD -400 QF, Sky 9/2, Poly 19%
    "Spain": 2095,        # 34 unbeaten, 0 GA, FD -950 vs AUT (Williams/Pino out for AUT)
    "England": 2055,      # -10 from 2065: shaky 2-1 vs DRC, Reece James & Quansah out injured
    "Portugal": 2030,     # FD -280 vs CRO (70.2%)
    "Brazil": 2025,       # Survived Japan 2-1 AET; FD -175 vs NOR (+115)
    "Colombia": 1985,     # Beat/dominated Group K (0-0 POR 24-13 shots), FD -500 vs GHA
    "Morocco": 1950,      # Beat NED pens, FD -260 vs CAN (~68% devigged)
    "Norway": 1945,       # Beat CIV 2-1, Haaland 5g, FD +115 vs BRA (~42% devigged)
    "Mexico": 1915,       # +20 from 1895: 4-0-0, 0 GA, beat Ecuador 2-0 cleanly (+40 Azteca!)
    "Switzerland": 1910,  # 4-1 BIH, beat CAN, FD -205 vs ALG (64.0%)
    "Belgium": 1905,      # -10 from 1915: trailed SEN 2-0 at 85', needed 120+5' VAR pen (-12 fatigue M94)
    "United States": 1900,# +15 from 1885: Pulisic fit, FD -600 vs BIH, FD +105 QF (+25 USA home)
    "Croatia": 1880,      # FD +220 vs POR
    "Canada": 1840,       # Beat RSA 1-0, Alphonso Davies back, fitness edge vs MAR
    "Egypt": 1815,        # FD -142 vs AUS (55.9%); Salah gym video "road back begins"
    "Algeria": 1810,      # FD +164 vs SUI
    "Austria": 1795,      # FD +610 vs ESP
    "Paraguay": 1785,     # Beat GER pens, Enciso injured (-10 M89 mod)
    "Australia": 1785,    # FD +116 vs EGY
    "Ghana": 1775,        # FD +370 vs COL
    "Bosnia and Herzegovina": 1715, # FD +410 vs USA (with +25 USA home -> ~79% USA)
    "Cape Verde": 1710,   # FD +1160 vs ARG (~90.5% ARG)
}

# 2. Pure Market-Calibrated Elo (tighter match to FanDuel/SkyBet/Polymarket July 1)
ELO_JULY1_MARKET = {
    "France": 2165,
    "Argentina": 2120,
    "Spain": 2095,
    "England": 2070,
    "Portugal": 2035,
    "Brazil": 2020,
    "Colombia": 1985,
    "Morocco": 1960,
    "Norway": 1955,
    "Mexico": 1915,
    "Switzerland": 1910,
    "United States": 1905,
    "Belgium": 1905,
    "Croatia": 1885,
    "Canada": 1835,
    "Egypt": 1820,
    "Algeria": 1805,
    "Austria": 1780,
    "Paraguay": 1780,
    "Australia": 1780,
    "Ghana": 1765,
    "Bosnia and Herzegovina": 1705,
    "Cape Verde": 1690,
}

# 3. Upset-Conservative / Higher-Variance Elo (larger scale & sigma, gentler favorites)
ELO_JULY1_CONSERVATIVE = dict(ELO_JULY1_BASE)
ELO_JULY1_CONSERVATIVE["France"] = 2155
ELO_JULY1_CONSERVATIVE["Argentina"] = 2095
ELO_JULY1_CONSERVATIVE["England"] = 2050
ELO_JULY1_CONSERVATIVE["Mexico"] = 1920

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=410.0, sigma=48.0,
            messi_gpg=0.68, mbappe_gpg=0.88, kane_gpg=0.72, haaland_gpg=0.84,
            dembele_gpg=0.46, vini_gpg=0.54,
            kane_curr_g=5, mbappe_assists=2, dembele_assists=2,
            par_r16_mod=-10, mar_r16_mod=-5, bel_r16_mod=-12,
            N=200000, seed=20260701):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"
    ]}
    r32_win = Counter()
    ko_games_sum = Counter()
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    # Player list: (name, team, curr_g, curr_a, gpg, apg, curr_mins)
    players = [
        ("Kylian Mbappé", "France", 6, mbappe_assists, mbappe_gpg, 0.28, 345),
        ("Lionel Messi", "Argentina", 6, 0, messi_gpg, 0.25, 200),
        ("Harry Kane", "England", kane_curr_g, 0, kane_gpg, 0.16, 345),
        ("Erling Haaland", "Norway", 5, 0, haaland_gpg, 0.12, 270),
        ("Ousmane Dembélé", "France", 4, dembele_assists, dembele_gpg, 0.30, 340),
        ("Vinícius Júnior", "Brazil", 4, 1, vini_gpg, 0.25, 355),
        ("Julián Quiñones", "Mexico", 3, 1, 0.42, 0.20, 340),
        ("Ismael Saibari", "Morocco", 3, 0, 0.35, 0.15, 370),
        ("Jonathan David", "Canada", 3, 0, 0.38, 0.15, 350),
        ("Matheus Cunha", "Brazil", 3, 0, 0.36, 0.15, 330),
        ("Johan Manzambi", "Switzerland", 3, 0, 0.34, 0.12, 250),
        ("Youri Tielemans", "Belgium", 2, 0, 0.25, 0.20, 380),
        ("Leandro Trossard", "Belgium", 2, 2, 0.38, 0.22, 360),
        ("Bradley Barcola", "France", 2, 0, 0.36, 0.22, 280),
        ("Cristiano Ronaldo", "Portugal", 2, 0, 0.42, 0.10, 270),
        ("Mikel Oyarzabal", "Spain", 2, 1, 0.46, 0.22, 250),
        ("Jude Bellingham", "England", 2, 1, 0.32, 0.22, 300),
        ("Lamine Yamal", "Spain", 1, 1, 0.35, 0.38, 220),
        ("Field", "NONE", 0, 0, 0, 0, 300),
    ]

    # Golden Ball within-team shares (updated July 1: Kane heroics 5g, Olise 5a + Henry/Sagnol Ballon d'Or push!)
    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.85), ("Other_ARG", 0.15)],
        "France": [("Kylian Mbappé", 0.53), ("Michael Olise", 0.24), ("Ousmane Dembélé", 0.17), ("Other_FRA", 0.06)],
        "Spain": [("Lamine Yamal", 0.54), ("Pedri", 0.23), ("Other_ESP", 0.23)],
        "England": [("Harry Kane", 0.50), ("Jude Bellingham", 0.32), ("Other_ENG", 0.18)],
        "Brazil": [("Vinícius Júnior", 0.58), ("Neymar", 0.10), ("Other_BRA", 0.32)],
        "Portugal": [("Bruno Fernandes", 0.36), ("Vitinha", 0.22), ("Cristiano Ronaldo", 0.24), ("Other_POR", 0.18)],
        "Norway": [("Erling Haaland", 0.82), ("Other_NOR", 0.18)],
        "Colombia": [("Luis Díaz", 0.45), ("James Rodríguez", 0.35), ("Other_COL", 0.20)],
        "Morocco": [("Achraf Hakimi", 0.44), ("Yassine Bounou", 0.24), ("Ismael Saibari", 0.22), ("Other_MAR", 0.10)],
        "Mexico": [("Julián Quiñones", 0.45), ("Raúl Jiménez", 0.25), ("Other_MEX", 0.30)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.35,
        "France": 1.20,
        "Spain": 1.04,
        "England": 1.02,
        "Brazil": 1.02,
        "Portugal": 0.96,
        "Norway": 1.14,
        "Morocco": 0.95,
        "Colombia": 0.90,
        "Mexico": 0.92,
    }

    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} (scale={scale}, sigma={sigma}) ====================")
    print(f"  Key R32 probs: USA-BIH={base_p('United States','Bosnia and Herzegovina',25,0):.3f} | ESP-AUT={base_p('Spain','Austria'):.3f} | POR-CRO={base_p('Portugal','Croatia'):.3f} | SUI-ALG={base_p('Switzerland','Algeria'):.3f} | ARG-CPV={base_p('Argentina','Cape Verde'):.3f} | COL-GHA={base_p('Colombia','Ghana'):.3f} | EGY-AUS={base_p('Egypt','Australia'):.3f}")
    print(f"  Key R16 probs: FRA-PAR={base_p('France','Paraguay',0,par_r16_mod):.3f} | MAR-CAN={base_p('Morocco','Canada',mar_r16_mod,0):.3f} | BRA-NOR={base_p('Brazil','Norway'):.3f} | ENG-MEX(Azt)={base_p('England','Mexico',0,40):.3f} | USA-BEL={base_p('United States','Belgium',25,bel_r16_mod):.3f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        def play_ko(a, b, venue=None, mod_a=0, mod_b=0):
            ba = mod_a
            bb = mod_b
            if venue == "Azteca":
                if a == "Mexico": ba += 40
                if b == "Mexico": bb += 40
            elif venue == "USA":
                if a == "United States": ba += 25
                if b == "United States": bb += 25
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / scale))
            return (a, b) if random.random() < p else (b, a)

        team_opps = {}
        def record_match(a, b):
            team_opps.setdefault(a, []).append(base_elo[b])
            team_opps.setdefault(b, []).append(base_elo[a])

        # 9 CONFIRMED R32 WINNERS:
        w = {
            "M73": "Canada",
            "M74": "Paraguay",
            "M75": "Morocco",
            "M76": "Brazil",
            "M77": "France",
            "M78": "Norway",
            "M79": "Mexico",
            "M80": "England",
            "M82": "Belgium",
        }
        # 7 REMAINING R32 MATCHES:
        r32_rem = [
            ("M81", "United States", "Bosnia and Herzegovina", "USA"),
            ("M83", "Portugal", "Croatia", None),
            ("M84", "Spain", "Austria", None),
            ("M85", "Switzerland", "Algeria", None),
            ("M86", "Argentina", "Cape Verde", None),
            ("M87", "Colombia", "Ghana", None),
            ("M88", "Egypt", "Australia", None),
        ]
        for mid, a, b, v in r32_rem:
            record_match(a, b)
            w[mid], _ = play_ko(a, b, venue=v)
            r32_win[w[mid]] += 1

        # R16:
        r16_pairs = [
            ("M89", w["M74"], w["M77"], None, par_r16_mod, 0),   # Paraguay vs France
            ("M90", w["M73"], w["M75"], None, 0, mar_r16_mod),   # Canada vs Morocco
            ("M91", w["M76"], w["M78"], None, 0, 0),             # Brazil vs Norway
            ("M92", w["M79"], w["M80"], "Azteca", 0, 0),         # Mexico vs England (Azteca!)
            ("M93", w["M83"], w["M84"], None, 0, 0),             # POR/CRO vs ESP/AUT
            ("M94", w["M81"], w["M82"], "USA", 0, bel_r16_mod),  # USA/BIH vs Belgium (120m fatigue!)
            ("M95", w["M86"], w["M88"], None, 0, 0),             # ARG/CPV vs EGY/AUS
            ("M96", w["M85"], w["M87"], None, 0, 0),             # SUI/ALG vs COL/GHA
        ]
        for mid, a, b, v, ma, mb in r16_pairs:
            record_match(a, b)
            w[mid], _ = play_ko(a, b, venue=v, mod_a=ma, mod_b=mb)
            counts["Reach_QF"][w[mid]] += 1

        qf_pairs = [
            ("M97", w["M89"], w["M90"], None),    # Boston QF
            ("M98", w["M93"], w["M94"], "USA"),   # LA QF
            ("M99", w["M91"], w["M92"], None),    # Miami QF
            ("M100", w["M95"], w["M96"], None),   # Kansas City QF
        ]
        for mid, a, b, v in qf_pairs:
            record_match(a, b)
            w[mid], _ = play_ko(a, b, venue=v)
            counts["Reach_SF"][w[mid]] += 1

        counts["QF_Boston"][w["M97"]] += 1
        counts["QF_KC"][w["M100"]] += 1

        record_match(w["M97"], w["M98"])
        w101, l101 = play_ko(w["M97"], w["M98"], venue="USA")
        record_match(w["M99"], w["M100"])
        w102, l102 = play_ko(w["M99"], w["M100"])

        counts["SF1_Dallas"][w101] += 1
        counts["SF2_Atlanta"][w102] += 1
        counts["Reach_Final"][w101] += 1
        counts["Reach_Final"][w102] += 1

        record_match(l101, l102)
        w103, l103 = play_ko(l101, l102)
        record_match(w101, w102)
        w104, l104 = play_ko(w101, w102)

        counts["ThirdPlace"][w103] += 1
        counts["Champion"][w104] += 1
        for t, opps in team_opps.items():
            ko_games_sum[t] += len(opps)

        # Golden Boot
        best_key = (-1, -1, -9999)
        best_name = None
        for pname, team, cg, ca, gpg, apg, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(2.6)
                key = (fg, poisson(1.2), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg; assists = ca
            opps = team_opps.get(team, [])
            miss_p = 0.045 if pname == "Lionel Messi" else 0.025
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
            mins = gmins + eff_ng * (80 if pname == "Lionel Messi" else 87)
            key = (goals, assists, -mins)
            if key > best_key:
                best_key = key; best_name = pname
        gb_wins[best_name] += 1

        # Golden Ball Model 1: Pure Team Finish
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

        # Golden Ball Model 2: Star-power & Golden-Boot-weighted Final 4
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

    print("  Exp rem KO games:", {t: round(ko_games_sum[t]/N, 2) for t in ["Argentina", "France", "England", "Spain", "Brazil", "Portugal", "Colombia", "Norway", "Morocco", "Mexico", "Belgium", "United States"]})
    for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"]:
        top = counts[key].most_common(8)
        s = ", ".join(f"{t}:{cnt/N:.4f}" for t, cnt in top)
        print(f"  {key:12s}: {s}")
    print("  GOLDEN_BOOT :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(8)))
    print("  GBALL_TEAM  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_team_wins.most_common(8)))
    print("  GBALL_STAR  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_star_wins.most_common(8)))

run_sim("1. BASE BLENDED (Jul 1, Kane 5g, Mbappé 2a)", ELO_JULY1_BASE, scale=410.0, sigma=48.0, N=200000)
run_sim("2. MARKET-CALIBRATED (Jul 1, Kane 5g, Mbappé 2a)", ELO_JULY1_MARKET, scale=400.0, sigma=42.0, N=150000)
run_sim("3. CONSERVATIVE / UPSET-HEAVY (scale=425, sigma=55)", ELO_JULY1_CONSERVATIVE, scale=425.0, sigma=55.0, par_r16_mod=-5, mar_r16_mod=-5, bel_r16_mod=-8, N=150000)
run_sim("4. GB CALIBRATION CHECK (Kane 5g, lower Messi gpg=0.62, Mbappé 0.90, Kane 0.76)", ELO_JULY1_BASE, scale=410.0, sigma=48.0, messi_gpg=0.62, mbappe_gpg=0.90, kane_gpg=0.76, N=150000)
run_sim("5. GB SENSITIVITY (Kane 5g, higher Messi gpg=0.72, Mbappé 0.86, Kane 0.68)", ELO_JULY1_BASE, scale=410.0, sigma=48.0, messi_gpg=0.72, mbappe_gpg=0.86, kane_gpg=0.68, N=150000)
