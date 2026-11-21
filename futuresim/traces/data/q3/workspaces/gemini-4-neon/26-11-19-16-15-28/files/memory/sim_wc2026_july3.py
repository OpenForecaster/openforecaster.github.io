import random, math
from collections import Counter

# ==============================================================================
# JULY 3, 2026 WORLD CUP SIMULATION (Cutoff ~23:45 UTC / Jul 4 05:15 IST)
#
# Confirmed R32 Results (14 of 16 complete as of 2026-07-03 cutoff):
#   M73 (Jun 28): Canada 1-0 South Africa        -> Canada
#   M74 (Jun 29): Paraguay 1-1 Germany (4-3 p)   -> Paraguay (Germany OUT)
#   M75 (Jun 29): Morocco 1-1 Netherlands (3-2p) -> Morocco (Netherlands OUT)
#   M76 (Jun 29): Brazil 2-1 Japan AET           -> Brazil (Japan OUT)
#   M77 (Jun 30): France 3-0 Sweden              -> France (Sweden OUT)
#   M78 (Jun 30): Norway 2-1 Ivory Coast         -> Norway (Ivory Coast OUT)
#   M79 (Jun 30): Mexico 2-0 Ecuador             -> Mexico (Ecuador OUT)
#   M80 (Jul 01): England 2-1 DR Congo           -> England (DR Congo OUT; Kane 2g -> 5g)
#   M81 (Jul 01): United States 2-0 Bosnia       -> United States (Bosnia OUT; Balogun 3g + RED CARD suspended M94!)
#   M82 (Jul 01): Belgium 3-2 Senegal AET        -> Belgium (Senegal OUT; 125 mins fatigue)
#   M84 (Jul 02): Spain 3-0 Austria              -> Spain (Austria OUT; Oyarzabal 2g -> 4g; Yamal 85' MOTM; 0 SOT)
#   M83 (Jul 02): Portugal 2-1 Croatia           -> Portugal (Croatia OUT; Ronaldo pen 68' -> 3g, Ramos 90+4', Gvardiol 103' VAR offside)
#   M85 (Jul 02): Switzerland 2-0 Algeria        -> Switzerland (Algeria OUT; Embolo 10' [Manzambi a], Ndoye 46')
#   M88 (Jul 03): Egypt 1-1 Australia (4-2 pens) -> Egypt (Australia OUT; Ashour 13', Hany OG 55'; 120 mins; Salah started but off-colour)
#
# In-progress at July 3 cutoff (Jul 4 05:15:37 IST = 23:45:37 UTC Jul 3):
#   M86 (Jul 03 6pm ET): Argentina 1-1 Cape Verde at 84'!!
#     - 29' Lionel Messi 1-0 (assist Lisandro Martinez) -> Messi now 7 goals, 0 assists!
#     - 59' Deroy Duarte 1-1 (assist Ryan Mendes)
#     - 73' Big save by Vozinha on Messi; 84' still 1-1!
#     - Remaining: ~11-12 mins regulation (6' + ~5-6' stoppage) + 30' ET + Penalties!
#
# Remaining 1 Unplayed R32 Match (Jul 3 9:30pm ET = 01:30 UTC Jul 4):
#   M87: Colombia (-500) vs Ghana (+370) -> FD 79.7% COL / 20.3% GHA (extreme heat warning Kansas City)
# ==============================================================================

# 1. July 3 Base Blended Elo
ELO_JULY3_BASE = {
    "France": 2165,       # 4-0-0, 13-2 GD, Mbappé 6g/2a, Olise 5a; heat warning Philadelphia
    "Spain": 2110,        # 3-0 Austria (0 SOT allowed!), 0 GA in 4, 34 unbeaten, Yamal fit
    "Argentina": 2095,    # -15 Bayesian from 2110: 1-1 at 84' vs CPV despite dominating chances (still elite!)
    "England": 2045,      # -5 from 2050: delayed arrival to Mexico City, Rice/Saka carrying knocks, James/Quansah out
    "Brazil": 2025,       # Unchanged: Raphinha returns to training + Neymar fit offsets Paquetá hamstring injury
    "Portugal": 2015,     # -15 from 2030: escaped Croatia 2-1 (90+4' winner, 103' VAR let-off, Croatia had better chances, Ronaldo subbed 81')
    "Colombia": 1985,     # FD -500 vs GHA
    "Morocco": 1955,      # +5: Opta 52.7% reg / 25.6% draw (~68% adv vs CAN), FD -260, zero injuries, 5 full days rest
    "Norway": 1945,       # Beat CIV 2-1, Haaland 5g
    "Switzerland": 1925,  # +15 from 1910: clinical 2-0 vs Algeria, unbeaten 3W 1D, stays in Vancouver!
    "Mexico": 1915,       # 4-0-0, 0 GA, Azteca noon kickoff bonus (+50)
    "Belgium": 1905,      # Survived SEN 3-2 AET 125 mins (-10 fatigue M94)
    "United States": 1900,# Beat Bosnia 2-0 (+25 USA home; -18 Balogun suspended M94)
    "Canada": 1840,       # Beat RSA 1-0, Davies back, Kone broken ankle
    "Egypt": 1795,        # -5: beat AUS on pens after 120 mins, Salah off-colour, Fatouh/Abdelmonem injured
    "Paraguay": 1785,     # Beat GER pens, Alderete doubtful (knee)
    "Ghana": 1775,        # FD +370 vs COL
    "Cape Verde": 1755,   # +45 Bayesian from 1710: 0-0 ESP, 2-2 URU, 1-1 at 84' vs ARG!
}

# 2. Pure Mechanical Results-Only (July 2 Elos UNCHANGED; only lock POR/SUI/EGY + live 84' ARG-CPV at pre-match rates)
ELO_JULY3_PURE = {
    "France": 2165,
    "Argentina": 2110,
    "Spain": 2110,
    "England": 2050,
    "Portugal": 2030,
    "Brazil": 2025,
    "Colombia": 1985,
    "Morocco": 1950,
    "Norway": 1945,
    "Mexico": 1915,
    "Switzerland": 1910,
    "Belgium": 1905,
    "United States": 1900,
    "Canada": 1840,
    "Egypt": 1800,
    "Paraguay": 1785,
    "Ghana": 1775,
    "Cape Verde": 1710,
}

# 3. Market / Opta-Tilted (tighter scale=400, sigma=42, Morocco ~68% vs CAN, Azteca +55)
ELO_JULY3_MARKET = dict(ELO_JULY3_BASE)
ELO_JULY3_MARKET["Argentina"] = 2105
ELO_JULY3_MARKET["Spain"] = 2115
ELO_JULY3_MARKET["England"] = 2055
ELO_JULY3_MARKET["Portugal"] = 2020
ELO_JULY3_MARKET["Brazil"] = 2020
ELO_JULY3_MARKET["Morocco"] = 1970
ELO_JULY3_MARKET["Norway"] = 1955
ELO_JULY3_MARKET["Switzerland"] = 1930
ELO_JULY3_MARKET["United States"] = 1905
ELO_JULY3_MARKET["Canada"] = 1835
ELO_JULY3_MARKET["Paraguay"] = 1780
ELO_JULY3_MARKET["Ghana"] = 1765
ELO_JULY3_MARKET["Cape Verde"] = 1745

# 4. Upset-Conservative / Cautious ARG (scale=425, sigma=55, lower ARG live survival)
ELO_JULY3_CONSERVATIVE = dict(ELO_JULY3_BASE)
ELO_JULY3_CONSERVATIVE["France"] = 2155
ELO_JULY3_CONSERVATIVE["Argentina"] = 2085
ELO_JULY3_CONSERVATIVE["Spain"] = 2100
ELO_JULY3_CONSERVATIVE["England"] = 2040
ELO_JULY3_CONSERVATIVE["Brazil"] = 2020
ELO_JULY3_CONSERVATIVE["Mexico"] = 1920
ELO_JULY3_CONSERVATIVE["Cape Verde"] = 1765

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=410.0, sigma=48.0,
            azteca_bonus=50, usa_balogun_mod=-18,
            par_r16_mod=-10, mar_r16_mod=0, bel_r16_mod=-10,
            sui_van_bonus=10,
            # Live M86 (ARG 1-1 CPV at 84') params:
            arg_rate=2.10, cpv_rate=0.50, reg_mins=12.0, et_mult=0.85, arg_pen_p=0.60,
            esp_yamal_share=0.58,
            N=200000, seed=20260703):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"
    ]}
    ko_games_sum = Counter()
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()
    arg_r32_wins = 0
    arg_et_count = 0

    # Player list: (name, team, curr_g, curr_a, gpg, apg, curr_mins)
    # Updated through July 3 (23:45 UTC):
    # - Lionel Messi: 7 goals, 0 assists (~284 mins; M86 remaining simulated jointly below!)
    # - Cristiano Ronaldo: 3 goals, 0 assists (~351 mins; scored pen 68' vs CRO)
    # - Johan Manzambi: 3 goals, 2 assists (~340 mins; assisted Embolo vs ALG)
    # - Breel Embolo: 2 goals (scored vs ALG)
    players = [
        ("Kylian Mbappé", "France", 6, 2, 0.88, 0.28, 345),
        ("Lionel Messi", "Argentina", 7, 0, 0.68, 0.25, 284),   # UPDATED! 29' goal vs CPV -> 7g, 0a!
        ("Harry Kane", "England", 5, 0, 0.72, 0.16, 345),
        ("Erling Haaland", "Norway", 5, 0, 0.84, 0.12, 270),
        ("Ousmane Dembélé", "France", 4, 2, 0.46, 0.30, 340),
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.52, 0.20, 330),
        ("Vinícius Júnior", "Brazil", 4, 1, 0.54, 0.25, 355),
        ("Johan Manzambi", "Switzerland", 3, 2, 0.34, 0.16, 340), # UPDATED! Assist vs ALG
        ("Julián Quiñones", "Mexico", 3, 1, 0.42, 0.20, 340),
        ("Ismael Saibari", "Morocco", 3, 0, 0.35, 0.15, 370),
        ("Jonathan David", "Canada", 3, 0, 0.38, 0.15, 350),
        ("Matheus Cunha", "Brazil", 3, 0, 0.36, 0.15, 330),
        ("Cristiano Ronaldo", "Portugal", 3, 0, 0.40, 0.10, 351), # UPDATED! Pen 68' vs CRO -> 3g
        ("Folarin Balogun", "United States", 3, 0, 0.42, 0.12, 315), # Suspended M94
        ("Leandro Trossard", "Belgium", 2, 2, 0.38, 0.22, 360),
        ("Bradley Barcola", "France", 2, 0, 0.36, 0.22, 280),
        ("Jude Bellingham", "England", 2, 1, 0.32, 0.22, 300),
        ("Lamine Yamal", "Spain", 1, 1, 0.35, 0.38, 305),
        ("Field", "NONE", 0, 0, 0, 0, 300),
    ]

    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.87), ("Other_ARG", 0.13)], # 7g + 8 straight WC games narrative!
        "France": [("Kylian Mbappé", 0.53), ("Michael Olise", 0.24), ("Ousmane Dembélé", 0.17), ("Other_FRA", 0.06)],
        "Spain": [("Lamine Yamal", esp_yamal_share), ("Pedri", 0.20), ("Mikel Oyarzabal", 0.12), ("Other_ESP", round(1.0 - esp_yamal_share - 0.32, 2))],
        "England": [("Harry Kane", 0.52), ("Jude Bellingham", 0.30), ("Other_ENG", 0.18)],
        "Brazil": [("Vinícius Júnior", 0.58), ("Neymar", 0.08), ("Other_BRA", 0.34)],
        "Portugal": [("Bruno Fernandes", 0.38), ("Vitinha", 0.24), ("Cristiano Ronaldo", 0.20), ("Other_POR", 0.18)],
        "Norway": [("Erling Haaland", 0.82), ("Other_NOR", 0.18)],
        "Colombia": [("Luis Díaz", 0.45), ("James Rodríguez", 0.35), ("Other_COL", 0.20)],
        "Morocco": [("Achraf Hakimi", 0.44), ("Yassine Bounou", 0.24), ("Ismael Saibari", 0.22), ("Other_MAR", 0.10)],
        "Switzerland": [("Johan Manzambi", 0.35), ("Granit Xhaka", 0.35), ("Other_SUI", 0.30)],
        "Mexico": [("Julián Quiñones", 0.45), ("Raúl Jiménez", 0.25), ("Other_MEX", 0.30)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.38,  # Slight lift from Messi's 20th career WC goal / 7th of tourney
        "France": 1.20,
        "Spain": 1.08,
        "England": 1.02,
        "Brazil": 1.02,
        "Portugal": 0.94,
        "Norway": 1.14,
        "Morocco": 0.95,
        "Colombia": 0.90,
        "Switzerland": 0.88,
        "Mexico": 0.92,
    }

    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} (scale={scale}, sigma={sigma}) ====================")
    print(f"  Rem R32: COL-GHA={base_p('Colombia','Ghana'):.3f} | ARG-CPV(84' 1-1 live sim)")
    print(f"  Key R16: FRA-PAR={base_p('France','Paraguay',0,par_r16_mod):.3f} | MAR-CAN={base_p('Morocco','Canada',mar_r16_mod,0):.3f} | BRA-NOR={base_p('Brazil','Norway'):.3f} | ENG-MEX(Azt+{azteca_bonus})={base_p('England','Mexico',0,azteca_bonus):.3f}")
    print(f"           ESP-POR={base_p('Spain','Portugal'):.3f} | USA-BEL(noBal)={base_p('United States','Belgium',25+usa_balogun_mod,bel_r16_mod):.3f} | ARG-EGY={base_p('Argentina','Egypt'):.3f} | CPV-EGY={base_p('Cape Verde','Egypt'):.3f} | COL-SUI={base_p('Colombia','Switzerland',0,sui_van_bonus):.3f}")

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
            elif venue == "Vancouver":
                if a == "Switzerland": ba += sui_van_bonus
                if b == "Switzerland": bb += sui_van_bonus
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / scale))
            return (a, b) if random.random() < p else (b, a)

        team_opps = {}
        def record_match(a, b):
            team_opps.setdefault(a, []).append(base_elo[b])
            team_opps.setdefault(b, []).append(base_elo[a])

        # 14 CONFIRMED R32 WINNERS:
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
            "M83": "Portugal",
            "M84": "Spain",
            "M85": "Switzerland",
            "M88": "Egypt",
        }

        # LIVE M86: Argentina 1-1 Cape Verde at 84' (jointly simulate remaining goals & Messi goals!)
        # Perturb rates slightly with draw of ELO[ARG] - ELO[CPV] so team-strength uncertainty correlates!
        elo_shift = ((ELO["Argentina"] - ELO["Cape Verde"]) - (base_elo["Argentina"] - base_elo["Cape Verde"])) / 250.0
        r_arg = max(0.8, arg_rate * math.exp(0.35 * elo_shift))
        r_cpv = max(0.15, cpv_rate * math.exp(-0.35 * elo_shift))

        ga_reg = poisson(r_arg * (reg_mins / 90.0))
        gc_reg = poisson(r_cpv * (reg_mins / 90.0))
        arg_m86_rem_goals = ga_reg
        messi_m86_rem_mins = reg_mins
        m86_went_et = False

        if ga_reg > gc_reg:
            w["M86"] = "Argentina"
        elif gc_reg > ga_reg:
            w["M86"] = "Cape Verde"
        else:
            m86_went_et = True
            arg_et_count += 1
            messi_m86_rem_mins += 30.0
            ga_et = poisson(r_arg * (30.0 / 90.0) * et_mult)
            gc_et = poisson(r_cpv * (30.0 / 90.0) * et_mult)
            arg_m86_rem_goals += ga_et
            if ga_et > gc_et:
                w["M86"] = "Argentina"
            elif gc_et > ga_et:
                w["M86"] = "Cape Verde"
            else:
                w["M86"] = "Argentina" if random.random() < arg_pen_p else "Cape Verde"

        if w["M86"] == "Argentina":
            arg_r32_wins += 1

        # Messi's additional goals/assists in remaining M86 (coupled to arg_m86_rem_goals!)
        messi_m86_extra_g = 0
        messi_m86_extra_a = 0
        for _g in range(arg_m86_rem_goals):
            u_m = random.random()
            if u_m < 0.34:   # Messi scores ~34% of Argentina's goals
                messi_m86_extra_g += 1
            elif u_m < 0.56: # Messi assists ~22% of Argentina's other goals
                messi_m86_extra_a += 1

        # UNPLAYED M87: Colombia vs Ghana
        record_match("Colombia", "Ghana")
        w["M87"], _ = play_ko("Colombia", "Ghana")

        # R16:
        # Note: if M86 went to ET in humid Miami heat, mild -5 mod vs Egypt (who played 120m in AC Dallas)
        m95_a_mod = -5 if m86_went_et else 5
        r16_pairs = [
            ("M89", w["M74"], w["M77"], None, par_r16_mod, 0),                 # Paraguay vs France
            ("M90", w["M73"], w["M75"], None, 0, mar_r16_mod),                 # Canada vs Morocco
            ("M91", w["M76"], w["M78"], None, 0, 0),                           # Brazil vs Norway
            ("M92", w["M79"], w["M80"], "Azteca", 0, 0),                       # Mexico vs England (Azteca noon!)
            ("M93", w["M83"], w["M84"], None, 0, 0),                           # Portugal vs Spain
            ("M94", w["M81"], w["M82"], "USA", usa_balogun_mod, bel_r16_mod),  # USA (no Balogun) vs Belgium (fatigue)
            ("M95", w["M86"], w["M88"], None, m95_a_mod, 0),                   # ARG/CPV vs Egypt
            ("M96", w["M85"], w["M87"], "Vancouver", 0, 0),                    # Switzerland (Vancouver!) vs COL/GHA
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
                fg = 2 + poisson(2.4)
                key = (fg, poisson(1.2), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg; assists = ca
            mins = gmins
            if pname == "Lionel Messi":
                goals += messi_m86_extra_g
                assists += messi_m86_extra_a
                mins += int(messi_m86_rem_mins)
            opps = list(team_opps.get(team, []))
            if pname == "Folarin Balogun" and len(opps) > 0:
                opps = opps[1:] # Suspended for R16!
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
            mins += eff_ng * (82 if pname == "Lionel Messi" else 87)
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

    print(f"  Live M86: P(ARG adv)={arg_r32_wins/N:.4f} | P(CPV adv)={1-arg_r32_wins/N:.4f} | P(ET)={arg_et_count/N:.4f}")
    print("  Exp rem KO games (post-M86):", {t: round(ko_games_sum[t]/N, 2) for t in ["France", "Argentina", "Spain", "England", "Brazil", "Portugal", "Colombia", "Switzerland", "Norway", "Morocco", "Mexico", "Egypt", "Cape Verde"]})
    for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"]:
        top = counts[key].most_common(8)
        s = ", ".join(f"{t}:{cnt/N:.4f}" for t, cnt in top)
        print(f"  {key:12s}: {s}")
    print("  GOLDEN_BOOT :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(8)))
    print("  GBALL_TEAM  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_team_wins.most_common(8)))
    print("  GBALL_STAR  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_star_wins.most_common(8)))

run_sim("1. BASE BAYESIAN (Jul 3: ARG-CPV 84' live 74.6%, POR/SUI/EGY locked, Azteca+50)",
        ELO_JULY3_BASE, scale=410.0, sigma=48.0, azteca_bonus=50, mar_r16_mod=0,
        arg_rate=2.10, cpv_rate=0.50, reg_mins=12.0, et_mult=0.85, arg_pen_p=0.60, N=200000)

run_sim("2. PURE MECHANICAL (Jul 2 Elos unchanged + pre-match M86 rates -> 78.9% ARG)",
        ELO_JULY3_PURE, scale=410.0, sigma=48.0, azteca_bonus=45, mar_r16_mod=-5, sui_van_bonus=0,
        arg_rate=2.40, cpv_rate=0.45, reg_mins=12.0, et_mult=0.90, arg_pen_p=0.62, N=150000)

run_sim("3. MARKET / OPTA TILTED (scale=400, sigma=42, MAR Opta ~68%, Azteca+55)",
        ELO_JULY3_MARKET, scale=400.0, sigma=42.0, azteca_bonus=55, mar_r16_mod=0, sui_van_bonus=10,
        arg_rate=2.15, cpv_rate=0.48, reg_mins=12.0, et_mult=0.85, arg_pen_p=0.61, N=150000)

run_sim("4. CONSERVATIVE / CAUTIOUS ARG (scale=425, sigma=55, ARG live ~70.7%)",
        ELO_JULY3_CONSERVATIVE, scale=425.0, sigma=55.0, azteca_bonus=50, mar_r16_mod=-3, sui_van_bonus=8,
        arg_rate=1.85, cpv_rate=0.52, reg_mins=11.0, et_mult=0.80, arg_pen_p=0.58, N=150000)
