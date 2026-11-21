import random, math
from collections import Counter

# ==============================================================================
# JULY 2, 2026 WORLD CUP SIMULATION
# Confirmed R32 Results (11 of 16 complete as of 2026-07-02 cutoff):
#   M73 (Jun 28): Canada 1-0 South Africa        -> Canada
#   M74 (Jun 29): Paraguay 1-1 Germany (4-3 p)   -> Paraguay (Germany OUT)
#   M75 (Jun 29): Morocco 1-1 Netherlands (3-2p) -> Morocco (Netherlands OUT)
#   M76 (Jun 29): Brazil 2-1 Japan AET           -> Brazil (Japan OUT)
#   M77 (Jun 30): France 3-0 Sweden              -> France (Sweden OUT)
#   M78 (Jun 30): Norway 2-1 Ivory Coast         -> Norway (Ivory Coast OUT)
#   M79 (Jun 30): Mexico 2-0 Ecuador             -> Mexico (Ecuador OUT)
#   M80 (Jul 01): England 2-1 DR Congo           -> England (DR Congo OUT; Kane 2g -> 5g)
#   M81 (Jul 01): United States 2-0 Bosnia       -> United States (Bosnia OUT; Balogun 3rd g + RED CARD suspended M94!)
#   M82 (Jul 01): Belgium 3-2 Senegal AET        -> Belgium (Senegal OUT; 125 mins fatigue!)
#   M84 (Jul 02): Spain 3-0 Austria              -> Spain (Austria OUT; Oyarzabal 2g -> 4g; Yamal 85' MOTM; 0 SOT allowed!)
#
# In-progress at July 2 cutoff (~23:39 UTC):
#   M83 (Jul 02 7pm ET): Portugal vs Croatia -> 0-0 at 36' (Ruben Dias yellow 17'; pre-match FD 70.2% -> live ~66.0% POR!)
#
# Remaining 4 Unplayed R32 Matches (Jul 2 11pm ET & Jul 3):
#   M85 (Jul 02 11pm ET): Switzerland (-205) vs Algeria (+164) -> FD Jul 2 64.0% SUI / 36.0% ALG
#   M86 (Jul 03 6pm ET): Argentina (-2000) vs Cape Verde (+1160) -> FD 92.3% ARG
#   M87 (Jul 03 9:30pm ET): Colombia (-500) vs Ghana (+370) -> FD 79.7% COL
#   M88 (Jul 03 2pm ET): Egypt vs Australia -> Hassan unsure if Salah starts (partial training Wed)
# ==============================================================================

# 1. July 2 Base Blended Elo (incorporating Spain 3-0 Austria dominance/Yamal fit, Salah uncertainty, Azteca altitude)
ELO_JULY2_BASE = {
    "France": 2165,       # 4-0-0, 13-2 GD, Saliba back, Mbappé 6g/2a, Olise 5a
    "Argentina": 2110,    # 3-0-0, Messi 6g, FD -2000 vs CPV, FD -400 QF
    "Spain": 2110,        # +15 from 2095: dominant 3-0 vs Austria (0 SOT allowed!), 0 GA in 4, 34 unbeaten, Yamal 85' MOTM, Pino fit
    "England": 2050,      # -5 from 2055: Tuchel confirms Reece James/Quansah out + FIFA rule blocks Azteca matchday arrival
    "Portugal": 2030,     # Pre-match FD -280 vs CRO; live -32 mod in M83 ONLY for 0-0 at 36' + Dias YC
    "Brazil": 2025,       # Survived Japan 2-1 AET; FD -175 vs NOR
    "Colombia": 1985,     # FD -500 vs GHA
    "Morocco": 1950,      # Beat NED pens, FD -260 vs CAN
    "Norway": 1945,       # Beat CIV 2-1, Haaland 5g (5-day recovery vs Brazil)
    "Mexico": 1915,       # 4-0-0, 0 GA, beat Ecuador 2-0 (+45 Azteca altitude/FIFA arrival edge!)
    "Switzerland": 1910,  # Jul 2 FD -205 vs ALG (64.0%)
    "Belgium": 1905,      # Survived SEN 3-2 AET 125 mins (-12 fatigue M94; Tielemans/KDB rested Thu)
    "United States": 1900,# Beat Bosnia 2-0 (+25 USA home; -18 Balogun red card suspension M94 ONLY!)
    "Croatia": 1880,      # 0-0 at 36' vs POR
    "Canada": 1840,       # Beat RSA 1-0, Alphonso Davies returning
    "Egypt": 1800,        # -15 from 1815: Hassan unsure if Salah will start vs Australia
    "Algeria": 1810,      # Jul 2 FD +164 vs SUI
    "Paraguay": 1785,     # Beat GER pens, Enciso injured (-10 M89 mod)
    "Australia": 1785,    # Facing uncertain-Salah Egypt
    "Ghana": 1775,        # FD +370 vs COL
    "Cape Verde": 1710,   # FD +1160 vs ARG
}

# 2. Pure Mechanical Results-Only (July 1 Elos UNCHANGED, only locking USA & Spain R32 wins + Balogun RC + 36' POR-CRO)
ELO_JULY2_PURE_RESULTS = {
    "France": 2165,
    "Argentina": 2110,
    "Spain": 2095,        # Unchanged from July 1
    "England": 2055,      # Unchanged from July 1
    "Portugal": 2030,
    "Brazil": 2025,
    "Colombia": 1985,
    "Morocco": 1950,
    "Norway": 1945,
    "Mexico": 1915,
    "Switzerland": 1910,
    "Belgium": 1905,
    "United States": 1900,
    "Croatia": 1880,
    "Canada": 1840,
    "Egypt": 1815,        # Unchanged from July 1
    "Algeria": 1810,
    "Paraguay": 1785,
    "Australia": 1785,
    "Ghana": 1775,
    "Cape Verde": 1710,
}

# 3. Market + Spain/Azteca-Tilted (tighter scale/sigma)
ELO_JULY2_MARKET = dict(ELO_JULY2_BASE)
ELO_JULY2_MARKET["Argentina"] = 2120
ELO_JULY2_MARKET["Spain"] = 2115
ELO_JULY2_MARKET["England"] = 2060
ELO_JULY2_MARKET["Portugal"] = 2035
ELO_JULY2_MARKET["Brazil"] = 2020
ELO_JULY2_MARKET["Morocco"] = 1960
ELO_JULY2_MARKET["Norway"] = 1955
ELO_JULY2_MARKET["United States"] = 1905
ELO_JULY2_MARKET["Croatia"] = 1885
ELO_JULY2_MARKET["Canada"] = 1835
ELO_JULY2_MARKET["Algeria"] = 1805
ELO_JULY2_MARKET["Paraguay"] = 1780
ELO_JULY2_MARKET["Australia"] = 1780
ELO_JULY2_MARKET["Ghana"] = 1765
ELO_JULY2_MARKET["Cape Verde"] = 1690

# 4. Upset-Conservative / Higher-Variance
ELO_JULY2_CONSERVATIVE = dict(ELO_JULY2_BASE)
ELO_JULY2_CONSERVATIVE["France"] = 2155
ELO_JULY2_CONSERVATIVE["Argentina"] = 2095
ELO_JULY2_CONSERVATIVE["Spain"] = 2100
ELO_JULY2_CONSERVATIVE["England"] = 2045
ELO_JULY2_CONSERVATIVE["Mexico"] = 1920

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=410.0, sigma=48.0,
            azteca_bonus=45, por_live_mod=-32, usa_balogun_mod=-18,
            par_r16_mod=-10, mar_r16_mod=-5, bel_r16_mod=-12,
            esp_yamal_share=0.58,
            N=200000, seed=20260702):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"
    ]}
    ko_games_sum = Counter()
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    # Player list: (name, team, curr_g, curr_a, gpg, apg, curr_mins)
    players = [
        ("Kylian Mbappé", "France", 6, 2, 0.88, 0.28, 345),
        ("Lionel Messi", "Argentina", 6, 0, 0.68, 0.25, 200),
        ("Harry Kane", "England", 5, 0, 0.72, 0.16, 345),
        ("Erling Haaland", "Norway", 5, 0, 0.84, 0.12, 270),
        ("Ousmane Dembélé", "France", 4, 2, 0.46, 0.30, 340),
        ("Vinícius Júnior", "Brazil", 4, 1, 0.54, 0.25, 355),
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.52, 0.20, 330),   # UPDATED! Brace vs Austria -> 4g, 1a!
        ("Julián Quiñones", "Mexico", 3, 1, 0.42, 0.20, 340),
        ("Ismael Saibari", "Morocco", 3, 0, 0.35, 0.15, 370),
        ("Jonathan David", "Canada", 3, 0, 0.38, 0.15, 350),
        ("Matheus Cunha", "Brazil", 3, 0, 0.36, 0.15, 330),
        ("Johan Manzambi", "Switzerland", 3, 1, 0.34, 0.14, 250),
        ("Folarin Balogun", "United States", 3, 0, 0.42, 0.12, 315), # Suspended M94! Handled below
        ("Youri Tielemans", "Belgium", 2, 0, 0.25, 0.20, 380),
        ("Leandro Trossard", "Belgium", 2, 2, 0.38, 0.22, 360),
        ("Bradley Barcola", "France", 2, 0, 0.36, 0.22, 280),
        ("Cristiano Ronaldo", "Portugal", 2, 0, 0.42, 0.10, 270),
        ("Jude Bellingham", "England", 2, 1, 0.32, 0.22, 300),
        ("Lamine Yamal", "Spain", 1, 1, 0.35, 0.38, 305),
        ("Field", "NONE", 0, 0, 0, 0, 300),
    ]

    # Golden Ball within-team shares (Jul 2: Yamal MOTM 85 mins vs Austria -> slight lift within Spain)
    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.85), ("Other_ARG", 0.15)],
        "France": [("Kylian Mbappé", 0.53), ("Michael Olise", 0.24), ("Ousmane Dembélé", 0.17), ("Other_FRA", 0.06)],
        "Spain": [("Lamine Yamal", esp_yamal_share), ("Pedri", 0.20), ("Mikel Oyarzabal", 0.12), ("Other_ESP", round(1.0 - esp_yamal_share - 0.32, 2))],
        "England": [("Harry Kane", 0.52), ("Jude Bellingham", 0.30), ("Other_ENG", 0.18)],
        "Brazil": [("Vinícius Júnior", 0.58), ("Neymar", 0.10), ("Other_BRA", 0.32)],
        "Portugal": [("Bruno Fernandes", 0.38), ("Vitinha", 0.22), ("Cristiano Ronaldo", 0.22), ("Other_POR", 0.18)],
        "Norway": [("Erling Haaland", 0.82), ("Other_NOR", 0.18)],
        "Colombia": [("Luis Díaz", 0.45), ("James Rodríguez", 0.35), ("Other_COL", 0.20)],
        "Morocco": [("Achraf Hakimi", 0.44), ("Yassine Bounou", 0.24), ("Ismael Saibari", 0.22), ("Other_MAR", 0.10)],
        "Mexico": [("Julián Quiñones", 0.45), ("Raúl Jiménez", 0.25), ("Other_MEX", 0.30)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.35,
        "France": 1.20,
        "Spain": 1.08,   # Slightly up as Yamal MOTM narrative returns!
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
    print(f"  Rem R32: POR-CRO(36' 0-0)={base_p('Portugal','Croatia',por_live_mod,0):.3f} | SUI-ALG={base_p('Switzerland','Algeria'):.3f} | ARG-CPV={base_p('Argentina','Cape Verde'):.3f} | COL-GHA={base_p('Colombia','Ghana'):.3f} | EGY-AUS={base_p('Egypt','Australia'):.3f}")
    print(f"  Key R16: FRA-PAR={base_p('France','Paraguay',0,par_r16_mod):.3f} | MAR-CAN={base_p('Morocco','Canada',mar_r16_mod,0):.3f} | BRA-NOR={base_p('Brazil','Norway'):.3f} | ENG-MEX(Azt+{azteca_bonus})={base_p('England','Mexico',0,azteca_bonus):.3f} | USA-BEL(noBal)={base_p('United States','Belgium',25+usa_balogun_mod,bel_r16_mod):.3f} | ESP-POR={base_p('Spain','Portugal'):.3f} | ESP-CRO={base_p('Spain','Croatia'):.3f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        def play_ko(a, b, venue=None, mod_a=0, mod_b=0):
            ba = mod_a
            bb = mod_b
            if venue == "Azteca":
                if a == "Mexico": ba += azteca_bonus
                if b == "Mexico": bb += azteca_bonus
            elif venue == "USA":
                if a == "United States": ba += 25
                if b == "United States": bb += 25
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / scale))
            return (a, b) if random.random() < p else (b, a)

        team_opps = {}
        def record_match(a, b):
            team_opps.setdefault(a, []).append(base_elo[b])
            team_opps.setdefault(b, []).append(base_elo[a])

        # 11 CONFIRMED R32 WINNERS:
        w = {
            "M73": "Canada",
            "M74": "Paraguay",
            "M75": "Morocco",
            "M76": "Brazil",
            "M77": "France",
            "M78": "Norway",
            "M79": "Mexico",
            "M80": "England",
            "M81": "United States",
            "M82": "Belgium",
            "M84": "Spain",
        }
        # 5 REMAINING R32 MATCHES (M83 live 36' 0-0; M85-M88 unplayed):
        r32_rem = [
            ("M83", "Portugal", "Croatia", None, por_live_mod, 0),
            ("M85", "Switzerland", "Algeria", None, 0, 0),
            ("M86", "Argentina", "Cape Verde", None, 0, 0),
            ("M87", "Colombia", "Ghana", None, 0, 0),
            ("M88", "Egypt", "Australia", None, 0, 0),
        ]
        for mid, a, b, v, ma, mb in r32_rem:
            record_match(a, b)
            w[mid], _ = play_ko(a, b, venue=v, mod_a=ma, mod_b=mb)

        # R16:
        r16_pairs = [
            ("M89", w["M74"], w["M77"], None, par_r16_mod, 0),            # Paraguay vs France
            ("M90", w["M73"], w["M75"], None, 0, mar_r16_mod),            # Canada vs Morocco
            ("M91", w["M76"], w["M78"], None, 0, 0),                      # Brazil vs Norway
            ("M92", w["M79"], w["M80"], "Azteca", 0, 0),                  # Mexico vs England (Azteca!)
            ("M93", w["M83"], w["M84"], None, 0, 0),                      # POR/CRO vs Spain
            ("M94", w["M81"], w["M82"], "USA", usa_balogun_mod, bel_r16_mod), # USA (no Balogun) vs Belgium (fatigue)
            ("M95", w["M86"], w["M88"], None, 0, 0),                      # ARG/CPV vs EGY/AUS
            ("M96", w["M85"], w["M87"], None, 0, 0),                      # SUI/ALG vs COL/GHA
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
                fg = 2 + poisson(2.5)
                key = (fg, poisson(1.2), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg; assists = ca
            opps = list(team_opps.get(team, []))
            if pname == "Folarin Balogun" and len(opps) > 0:
                opps = opps[1:] # Suspended for R16!
            # Ronaldo has already played 36' of M83 with 0g -> scale first match by 0.63
            miss_p = 0.045 if pname == "Lionel Messi" else 0.025
            eff_opps = [oe for oe in opps if random.random() > miss_p]
            eff_ng = len(eff_opps)
            if eff_ng > 0:
                mult = max(0.35, random.gauss(1.0, 0.25))
                exp_g = 0.0
                for idx_m, oe in enumerate(eff_opps):
                    m_scale = 0.63 if (pname == "Cristiano Ronaldo" and idx_m == 0) else 1.0
                    opp_mult = max(0.75, min(1.38, 1.0 + (1920.0 - oe) / 420.0))
                    exp_g += gpg * mult * opp_mult * m_scale
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

    print("  Exp rem KO games:", {t: round(ko_games_sum[t]/N, 2) for t in ["Argentina", "France", "Spain", "England", "Brazil", "Portugal", "Colombia", "Norway", "Morocco", "Mexico", "Belgium", "United States"]})
    for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"]:
        top = counts[key].most_common(8)
        s = ", ".join(f"{t}:{cnt/N:.4f}" for t, cnt in top)
        print(f"  {key:12s}: {s}")
    print("  GOLDEN_BOOT :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(8)))
    print("  GBALL_TEAM  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_team_wins.most_common(8)))
    print("  GBALL_STAR  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_star_wins.most_common(8)))

run_sim("1. BASE BLENDED (Jul 2: ESP+15, Azteca+45, Balogun-18, POR-32 live, EGY-15)", ELO_JULY2_BASE, scale=410.0, sigma=48.0, azteca_bonus=45, por_live_mod=-32, usa_balogun_mod=-18, esp_yamal_share=0.58, N=200000)
run_sim("2. PURE RESULTS ONLY (Jul 1 Elos unchanged; only USA/ESP wins + Balogun RC + POR live)", ELO_JULY2_PURE_RESULTS, scale=410.0, sigma=48.0, azteca_bonus=40, por_live_mod=-32, usa_balogun_mod=-18, esp_yamal_share=0.55, N=150000)
run_sim("3. MARKET + SPAIN/AZTECA TILTED (scale=400, sigma=42, Azteca+50)", ELO_JULY2_MARKET, scale=400.0, sigma=42.0, azteca_bonus=50, por_live_mod=-32, usa_balogun_mod=-20, esp_yamal_share=0.60, N=150000)
run_sim("4. CONSERVATIVE / UPSET-HEAVY (scale=425, sigma=55, Azteca+45)", ELO_JULY2_CONSERVATIVE, scale=425.0, sigma=55.0, azteca_bonus=45, por_live_mod=-25, usa_balogun_mod=-15, par_r16_mod=-5, mar_r16_mod=-5, bel_r16_mod=-8, esp_yamal_share=0.57, N=150000)
