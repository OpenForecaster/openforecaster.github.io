import random, math
from collections import Counter

# ==============================================================================
# JUNE 30, 2026 WORLD CUP SIMULATION
# Confirmed R32 Results as of 2026-06-30 cutoff (after FRA 3-0 SWE & NOR 2-1 CIV):
#   M73 (Jun 28): Canada 1-0 South Africa       -> Canada advances
#   M74 (Jun 29): Paraguay 1-1 Germany (4-3 p)  -> Paraguay advances (Germany OUT!)
#   M75 (Jun 29): Morocco 1-1 Netherlands (3-2p)-> Morocco advances (Netherlands OUT!)
#   M76 (Jun 29): Brazil 2-1 Japan              -> Brazil advances (Japan OUT!)
#   M77 (Jun 30): France 3-0 Sweden             -> France advances (Sweden OUT!)
#   M78 (Jun 30): Norway 2-1 Ivory Coast        -> Norway advances (Ivory Coast OUT!)
# Remaining R32 (unplayed as of June 30 cutoff):
#   M79 (Jun 30 9pm ET): Mexico vs Ecuador (Azteca; AP: Quito altitude offsets Azteca altitude -> +25)
#   M80..M88 (Jul 1-3): ENG-COD, USA-BIH, BEL-SEN, POR-CRO, ESP-AUT, SUI-ALG, ARG-CPV, COL-GHA, AUS-EGY
# ==============================================================================

# Baseline June 29 Elos (for comparison)
ELO_JUNE29 = {
    "France": 2155, "Argentina": 2095, "Spain": 2095, "England": 2065,
    "Brazil": 2030, "Portugal": 2025, "Germany": 1990, "Netherlands": 2015,
    "Colombia": 1975, "Morocco": 1930, "Norway": 1930, "Belgium": 1915,
    "Switzerland": 1905, "Mexico": 1895, "Croatia": 1890, "United States": 1885,
    "Japan": 1880, "Ecuador": 1870, "Senegal": 1855, "Ivory Coast": 1855,
    "Canada": 1840, "Austria": 1830, "Sweden": 1825, "Ghana": 1810,
    "Australia": 1805, "Algeria": 1805, "Egypt": 1790, "Paraguay": 1785,
    "DR Congo": 1755, "Cape Verde": 1755, "Bosnia and Herzegovina": 1745, "South Africa": 1680,
}

# June 30 Bayesian-updated Blended Elos:
# - France: 2155 -> 2165 (+10: crushed Sweden 3-0, hit woodwork twice, Saliba back, 4-0-0, 13 GF)
# - Morocco: 1930 -> 1945 (+15: matched Netherlands 1-1 AET, Hakimi post, Bounou shootout heroics, unbeaten)
# - Norway: 1930 -> 1935 (+5: beat Ivory Coast 2-1 via Haaland 86', slight pressure spell after 74')
# - Paraguay: 1785 (already +20 on Jun 29 for 1-1 vs GER; won pens; -10 R16 fatigue/Enciso injury mod)
# - Canada: 1840 (unchanged, beat SA 1-0, extra rest day vs Morocco's 120 mins -> Morocco -5 mod in M90)
ELO_JUNE30_BASE = dict(ELO_JUNE29)
ELO_JUNE30_BASE["France"] = 2165
ELO_JUNE30_BASE["Morocco"] = 1945
ELO_JUNE30_BASE["Norway"] = 1935

# Market-tilted June 30 Elo (anchored to SI June 28 market ratings + June 29-30 updates)
ELO_JUNE30_MARKET = {
    "France": 2165, "Spain": 2095, "England": 2085, "Argentina": 2080,
    "Portugal": 2040, "Brazil": 2035, "Norway": 1960, "Colombia": 1955,
    "Morocco": 1945, "Belgium": 1920, "Mexico": 1905, "United States": 1900,
    "Switzerland": 1900, "Croatia": 1885, "Ecuador": 1865, "Senegal": 1865,
    "Canada": 1845, "Austria": 1830, "Australia": 1805, "Egypt": 1805,
    "Ghana": 1800, "Algeria": 1795, "Paraguay": 1780, "DR Congo": 1745,
    "Cape Verde": 1735, "Bosnia and Herzegovina": 1730,
    "Germany": 1990, "Netherlands": 2015, "Japan": 1880, "Ivory Coast": 1855,
    "Sweden": 1825, "South Africa": 1680,
}

# Conservative / upset-compressed Elo (France 2155, Morocco 1950, Paraguay 1800, higher scale/sigma)
ELO_JUNE30_CONSERVATIVE = dict(ELO_JUNE30_BASE)
ELO_JUNE30_CONSERVATIVE["France"] = 2155
ELO_JUNE30_CONSERVATIVE["Morocco"] = 1950
ELO_JUNE30_CONSERVATIVE["Paraguay"] = 1800

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=410.0, sigma=50.0,
            messi_gpg=0.68, mbappe_gpg=0.87, haaland_gpg=0.85,
            dembele_gpg=0.47, kane_gpg=0.70, vini_gpg=0.55,
            mbappe_assists=0, par_r16_mod=-10, mar_r16_mod=-5,
            N=200000, seed=20260630):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"
    ]}
    ko_games_sum = Counter()
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    # Player list: (name, team, curr_g, curr_a, gpg, apg, played_r32, curr_mins)
    players = [
        ("Lionel Messi", "Argentina", 6, 0, messi_gpg, 0.28, False, 200),
        ("Kylian Mbappé", "France", 6, mbappe_assists, mbappe_gpg, 0.24, True, 350),
        ("Erling Haaland", "Norway", 5, 0, haaland_gpg, 0.12, True, 270),
        ("Ousmane Dembélé", "France", 4, 1, dembele_gpg, 0.30, True, 340),
        ("Vinícius Júnior", "Brazil", 4, 1, vini_gpg, 0.26, True, 355),
        ("Harry Kane", "England", 3, 0, kane_gpg, 0.18, False, 255),
        ("Ismael Saibari", "Morocco", 3, 0, 0.36, 0.15, True, 370),
        ("Jonathan David", "Canada", 3, 0, 0.40, 0.15, True, 350),
        ("Matheus Cunha", "Brazil", 3, 0, 0.38, 0.15, True, 330),
        ("Johan Manzambi", "Switzerland", 3, 0, 0.34, 0.12, False, 250),
        ("Bradley Barcola", "France", 2, 0, 0.36, 0.22, True, 280),
        ("Cristiano Ronaldo", "Portugal", 2, 0, 0.44, 0.10, False, 270),
        ("Mikel Oyarzabal", "Spain", 2, 1, 0.46, 0.22, False, 250),
        ("Jude Bellingham", "England", 2, 1, 0.35, 0.22, False, 210),
        ("Leandro Trossard", "Belgium", 2, 1, 0.40, 0.20, False, 240),
        ("Lamine Yamal", "Spain", 1, 1, 0.35, 0.38, False, 220),
        ("Field", "NONE", 0, 0, 0, 0, False, 300),
    ]

    # Team-level Golden Ball player shares (updated for June 30: Mbappé brace -> 6g, Olise 2a -> 5a!)
    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.85), ("Other_ARG", 0.15)],
        "France": [("Kylian Mbappé", 0.55), ("Michael Olise", 0.21), ("Ousmane Dembélé", 0.18), ("Other_FRA", 0.06)],
        "Spain": [("Lamine Yamal", 0.56), ("Pedri", 0.22), ("Other_ESP", 0.22)],
        "England": [("Harry Kane", 0.40), ("Jude Bellingham", 0.38), ("Other_ENG", 0.22)],
        "Brazil": [("Vinícius Júnior", 0.58), ("Neymar", 0.12), ("Other_BRA", 0.30)],
        "Portugal": [("Bruno Fernandes", 0.35), ("Cristiano Ronaldo", 0.30), ("Other_POR", 0.35)],
        "Norway": [("Erling Haaland", 0.82), ("Other_NOR", 0.18)],
        "Colombia": [("Luis Díaz", 0.45), ("James Rodríguez", 0.35), ("Other_COL", 0.20)],
        "Morocco": [("Achraf Hakimi", 0.45), ("Yassine Bounou", 0.25), ("Ismael Saibari", 0.20), ("Other_MAR", 0.10)],
    }

    # Star-power / narrative weights for Final-4 Golden Ball selection model
    # Reflects real FIFA TSG behavior (like Messi 2014, Modric 2018, Forlan 2010, Messi 2022)
    # where transcendent individual campaigns (Messi 6g+, Mbappe 6g+, Yamal, Haaland) carry extra pull
    # even as runner-up / 3rd place!
    TEAM_STAR_MULT = {
        "Argentina": 1.35,  # Messi last dance + 6+ goals narrative
        "France": 1.18,     # Mbappé chasing all-time WC record + Olise/Dembélé
        "Spain": 1.05,      # Lamine Yamal teenage sensation
        "England": 1.00,    # Kane/Bellingham
        "Brazil": 1.02,     # Vinícius Jr
        "Portugal": 0.98,   # Ronaldo/Bruno
        "Norway": 1.15,     # Haaland miracle run
        "Morocco": 0.95,    # Hakimi/Bounou fairytale
        "Colombia": 0.90,
    }

    # Check key single-match win probs at base_elo
    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} (scale={scale}, sigma={sigma}) ====================")
    print(f"  Single-match base probs: FRA vs PAR={base_p('France','Paraguay',0,par_r16_mod):.3f} | MAR vs CAN={base_p('Morocco','Canada',mar_r16_mod,0):.3f} | FRA vs MAR={base_p('France','Morocco'):.3f} | BRA vs NOR={base_p('Brazil','Norway'):.3f} | MEX vs ECU={base_p('Mexico','Ecuador',25,0):.3f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        def play_ko(a, b, venue=None, mod_a=0, mod_b=0):
            ba = mod_a
            bb = mod_b
            if venue == "Azteca_ECU":
                if a == "Mexico": ba += 25
                if b == "Mexico": bb += 25
            elif venue == "Azteca":
                if a == "Mexico": ba += 40
                if b == "Mexico": bb += 40
            elif venue == "USA":
                if a == "United States": ba += 25
                if b == "United States": bb += 25
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / scale))
            return (a, b) if random.random() < p else (b, a)

        team_opps = {} # team -> list of opponent base Elos for remaining KO games played
        def record_match(a, b):
            team_opps.setdefault(a, []).append(base_elo[b])
            team_opps.setdefault(b, []).append(base_elo[a])

        w = {
            "M73": "Canada",
            "M74": "Paraguay",
            "M75": "Morocco",
            "M76": "Brazil",
            "M77": "France",
            "M78": "Norway",
        }
        r32_rem = [
            ("M79", "Mexico", "Ecuador", "Azteca_ECU"),
            ("M80", "England", "DR Congo", None),
            ("M81", "United States", "Bosnia and Herzegovina", "USA"),
            ("M82", "Belgium", "Senegal", None),
            ("M83", "Portugal", "Croatia", None),
            ("M84", "Spain", "Austria", None),
            ("M85", "Switzerland", "Algeria", None),
            ("M86", "Argentina", "Cape Verde", None),
            ("M87", "Colombia", "Ghana", None),
            ("M88", "Australia", "Egypt", None),
        ]
        for mid, a, b, v in r32_rem:
            record_match(a, b)
            w[mid], _ = play_ko(a, b, venue=v)

        # R16:
        r16_pairs = [
            ("M89", w["M74"], w["M77"], None, par_r16_mod, 0),   # Paraguay vs France
            ("M90", w["M73"], w["M75"], None, 0, mar_r16_mod),   # Canada vs Morocco
            ("M91", w["M76"], w["M78"], None, 0, 0),             # Brazil vs Norway
            ("M92", w["M79"], w["M80"], "Azteca", 0, 0),         # Mex/Ecu vs Eng/COD
            ("M93", w["M83"], w["M84"], None, 0, 0),
            ("M94", w["M81"], w["M82"], "USA", 0, 0),
            ("M95", w["M86"], w["M88"], None, 0, 0),
            ("M96", w["M85"], w["M87"], None, 0, 0),
        ]
        for mid, a, b, v, ma, mb in r16_pairs:
            record_match(a, b)
            w[mid], _ = play_ko(a, b, venue=v, mod_a=ma, mod_b=mb)
            counts["Reach_QF"][w[mid]] += 1

        qf_pairs = [
            ("M97", w["M89"], w["M90"], None),
            ("M98", w["M93"], w["M94"], "USA"),
            ("M99", w["M91"], w["M92"], None),
            ("M100", w["M95"], w["M96"], None),
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

        # Golden Boot with PER-MATCH OPPONENT ELO ADJUSTMENT!
        best_key = (-1, -1, -9999)
        best_name = None
        player_final_goals = {}
        for pname, team, cg, ca, gpg, apg, played_r32, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(2.8)
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
                    # Opponent strength adjustment: Elo 1920 = 1.00; weak 1755 = 1.38; strong 2100 = 0.78
                    opp_mult = max(0.75, min(1.38, 1.0 + (1920.0 - oe) / 420.0))
                    exp_g += gpg * mult * opp_mult
                goals += poisson(exp_g)
                assists += poisson(eff_ng * apg)
            mins = gmins + eff_ng * (80 if pname == "Lionel Messi" else 87)
            player_final_goals[pname] = goals
            key = (goals, assists, -mins)
            if key > best_key:
                best_key = key; best_name = pname
        gb_wins[best_name] += 1

        # Golden Ball Model 1: Pure Team-Finish (55% Champ, 30% RU, 10% 3rd, 5% 4th)
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

        # Golden Ball Model 2: Star-power & Golden-Boot-weighted Final 4 selection
        # Base weights: Champ 0.50, RU 0.32, 3rd 0.12, 4th 0.06, multiplied by team star factor + GB winner boost!
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
        # Within team, boost Golden Boot winner if on that team!
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

    print("  Exp rem KO games:", {t: round(ko_games_sum[t]/N, 2) for t in ["Argentina", "France", "England", "Spain", "Brazil", "Portugal", "Colombia", "Norway", "Morocco", "Canada", "Paraguay"]})
    for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"]:
        top = counts[key].most_common(6)
        s = ", ".join(f"{t}:{cnt/N:.4f}" for t, cnt in top)
        print(f"  {key:12s}: {s}")
    print("  GOLDEN_BOOT :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(8)))
    print("  GBALL_TEAM  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_team_wins.most_common(8)))
    print("  GBALL_STAR  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_star_wins.most_common(8)))

run_sim("1. BASE BLENDED (Jun 30, Mbappé 0a)", ELO_JUNE30_BASE, scale=410.0, sigma=50.0, mbappe_assists=0, N=200000)
run_sim("2. MARKET-TILTED (Jun 30, Mbappé 0a)", ELO_JUNE30_MARKET, scale=400.0, sigma=45.0, mbappe_assists=0, N=150000)
run_sim("3. CONSERVATIVE / UPSET-HEAVY (scale=425, sigma=55, FRA 2155, MAR 1950, PAR 1800)", ELO_JUNE30_CONSERVATIVE, scale=425.0, sigma=55.0, par_r16_mod=-5, mar_r16_mod=-5, N=150000)
run_sim("4. GOLDEN BOOT SENS: Mbappé 1a, Messi gpg=0.72, Mbappé gpg=0.88", ELO_JUNE30_BASE, scale=410.0, sigma=50.0, messi_gpg=0.72, mbappe_gpg=0.88, mbappe_assists=1, N=150000)
run_sim("5. GOLDEN BOOT SENS: Mbappé 0a, Messi gpg=0.62, Mbappé gpg=0.90", ELO_JUNE30_BASE, scale=410.0, sigma=50.0, messi_gpg=0.62, mbappe_gpg=0.90, mbappe_assists=0, N=150000)
