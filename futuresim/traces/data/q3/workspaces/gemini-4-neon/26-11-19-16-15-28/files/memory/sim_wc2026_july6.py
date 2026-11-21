import random, math
from collections import Counter

# ==============================================================================
# JULY 6, 2026 WORLD CUP SIMULATION
#
# 5 of 8 R16 Matches COMPLETE:
#   M89 (Jul 04, Philadelphia): France 1-0 Paraguay (Mbappe 70' pen [7g/2a])
#   M90 (Jul 04, Houston):      Morocco 3-0 Canada (Ounahi 50', 82', Rahimi 90+8';
#                               Saibari hamstring & Chadi Riad doubts for QF)
#   M91 (Jul 05, NJ/NY):        Norway 2-1 Brazil (Haaland 79', 90' [7g/0a]; BRA OUT)
#   M92 (Jul 05, Azteca):       ENGLAND 3-2 MEXICO!! (Bellingham 36', 38' [4g/1a],
#                               Kane 60' pen [6g/1a!]; Quansah 54' red -> suspended QF;
#                               Henderson wrist surgery out; MEX ELIMINATED!)
#   M93 (Jul 06, Dallas):       SPAIN 1-0 PORTUGAL!! (Mikel Merino 90+1', assist Ferran
#                               Torres; Spain unbeaten in 35, WC record 6 straight clean
#                               sheets / Unai Simon 609 mins; POR ELIMINATED!)
#
# LOCKED QUARTERFINALS (2 of 4 fully locked, 1 half-locked):
#   QF1 (Thu Jul 9, Boston, M97):  FRANCE vs MOROCCO
#       - Sportune Jul 5 To Qualify: FRA 1.27 / MAR 3.70 -> 74.4% / 25.6%
#       - Opta Jul 5: 74.9% FRA / 25.1% MAR; Betway Jul 6 90m: -175/+280/+500 -> ~73.5%
#       - Thuram back in training; Tchouameni adductor still doubtful; Olise/Barcola/Kone
#         NOT suspended (1 yellow each, FFF appealing Olise's booking).
#   QF2 (Fri Jul 10, LA, M98):     SPAIN vs winner(USA/Belgium)
#   QF3 (Sat Jul 11, Miami, M99):  ENGLAND vs NORWAY
#       - BetMGM Jul 5/6 90m: ENG -110 / Draw +260 / NOR +270 -> ~62.6% ENG / 37.4% NOR
#       - Quansah suspended (Spence/Konsa RB); Rice/Bellingham/Guehi/O'Reilly on 1 yellow
#         (available vs Norway!); Norway full strength.
#   QF4 (Sat/Sun Jul 11-12, KC, M100): winner(ARG/EGY) vs winner(COL/SUI)
#
# REMAINING 3 R16 MATCHES:
#   M94 (Mon Jul 6, Seattle, kickoff imminent): USA vs Belgium
#       - Pre-lineup Opta: 37.2% USA / 26.3% Draw / 36.5% BEL (~50.4% USA)
#       - OFFICIAL LINEUPS (HT Live): Balogun STARTS for USA; Belgium BENCHED
#         Kevin De Bruyne, Romelu Lukaku, AND Jeremy Doku!! -> ~55-56% USA!
#   M95 (Tue Jul 7, Atlanta): Argentina vs Egypt
#       - Deadspin/FD Jul 6: ARG -280 / Draw +370 / EGY +850 -> ~82.0% ARG
#       - Opta Jul 6: 69.1% / 18.5% / 12.3% -> ~79.8% ARG
#       - Both played 120m; Messi fatigued, Gonzalez/Medina doubtful; Salah hamstring,
#         Fatouh & El Fotouh injured.
#   M96 (Tue Jul 7, Vancouver): Colombia vs Switzerland
#       - Pre-Monday-training Deadspin (+130/+200/+225) & Bet365 (2.30/3.00/3.40):
#         ~56.8-57.2% COL / 42.8-43.2% SUI; Jhon Cordoba CONFIRMED OUT (adductor tear).
#       - BREAKING Reuters Mon Jul 6: Manzambi (3g/2a), Ruben Vargas, & Djibril Sow ALL
#         quit training early for medical exams ("huge issue" per Yakin)! Shifts COL
#         back up to ~59.5-60.5% COL / 39.5-40.5% SUI.
# ==============================================================================

# 1. BASE BAYESIAN + MARKET BLEND
ELO_BASE = {
    "France": 2156,       # 5-0-0 (14-2 GD), Tchouameni adductor doubt (-2)
    "Spain": 2124,        # +9: beat Portugal 1-0, unbeaten in 35, 6 straight clean sheets!
    "Argentina": 2088,    # -4: 120m fatigue, Gonzalez/Medina doubts; FD/Opta ~81.5% vs EGY
    "England": 2052,      # +10: beat Mexico 3-2 w/ 10 men at Azteca! BetMGM 62.6% vs NOR
    "Colombia": 1990,     # -5: Jhon Cordoba confirmed out for tournament (adductor tear)
    "Morocco": 1982,      # Saibari/Chadi Riad doubts (-15 QF, -8 late) -> ~74.5% FRA
    "Norway": 1966,       # Full strength, beat Brazil 2-1 -> ~61.5% ENG / 38.5% NOR
    "Switzerland": 1924,  # +10 Vancouver rest/no-travel; Manzambi/Vargas/Sow training scare!
    "United States": 1904,# +25 USA home; Balogun starts
    "Belgium": 1900,      # De Bruyne, Lukaku, Doku ALL benched for M94 kickoff!
    "Egypt": 1796,        # Salah hamstring + Fatouh/El Fotouh out
}

# 2. MARKET-ANCHORED (tight to BetMGM ENG-NOR 62.6%, Sportune FRA-MAR 74.4%, FD ARG-EGY 82%)
ELO_MARKET = {
    "France": 2158,
    "Spain": 2122,
    "Argentina": 2092,
    "England": 2054,
    "Colombia": 1994,
    "Morocco": 1982,
    "Norway": 1956,       # slightly more market regression -> ~62.7% ENG vs NOR
    "Switzerland": 1922,
    "United States": 1902,
    "Belgium": 1904,
    "Egypt": 1794,
}

# 3. PURE BAYESIAN / FORM-RESPONSIVE (rewards Spain 6 clean sheets, Norway beating Brazil, England resilience)
ELO_PURE = {
    "France": 2160,
    "Spain": 2132,        # Strong form boost for 35 unbeaten & 0 GA in tournament
    "Argentina": 2092,
    "England": 2056,
    "Colombia": 1986,
    "Morocco": 1980,
    "Norway": 1978,       # High respect for Norway beating Brazil
    "Switzerland": 1928,
    "United States": 1906,
    "Belgium": 1898,
    "Egypt": 1802,
}

# 4. UPSET-CONSERVATIVE (wider variance, stronger Morocco/Norway/Switzerland/Egypt/USA)
ELO_CONSERVATIVE = {
    "France": 2148,
    "Spain": 2116,
    "Argentina": 2080,
    "England": 2042,
    "Colombia": 1986,
    "Morocco": 1984,
    "Norway": 1968,
    "Switzerland": 1928,
    "United States": 1904,
    "Belgium": 1898,
    "Egypt": 1804,
}

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=410.0, sigma=48.0,
            bel_bench_r16=-18, sui_van_bonus=10, sui_inj_r16=-16, sui_inj_late=-6,
            mar_saibari_qf=-15, mar_saibari_late=-8,
            eng_quansah_qf=-5, arg_et_fatigue_r16=-8,
            haaland_gpg=0.95, mbappe_gpg=0.85, messi_gpg=0.67, kane_gpg=0.73,
            win_goal_ratio=1.75,
            esp_yamal_share=0.46,
            N=200000, seed=20260706):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"
    ]}
    ko_games_sum = Counter()
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    # Official July 6 Golden Boot leaderboard (11 remaining teams):
    # (name, team, curr_g, curr_a, gpg, apg, curr_mins)
    # Confirmed:
    #   Mbappe 7g 2a (~435m), Messi 7g 0a (~345m), Haaland 7g 0a (~355m),
    #   Kane 6g 1a (~435m), Dembele 4g 2a (~425m), Oyarzabal 4g 1a (~415m),
    #   Bellingham 4g 1a (~390m), Manzambi 3g 2a (~340m), Balogun 3g 0a (~315m)
    players = [
        ("Kylian Mbappé", "France", 7, 2, mbappe_gpg, 0.27, 435),
        ("Lionel Messi", "Argentina", 7, 0, messi_gpg, 0.20, 345),
        ("Erling Haaland", "Norway", 7, 0, haaland_gpg, 0.08, 355),
        ("Harry Kane", "England", 6, 1, kane_gpg, 0.17, 435),
        ("Ousmane Dembélé", "France", 4, 2, 0.44, 0.28, 425),
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.50, 0.20, 415),
        ("Jude Bellingham", "England", 4, 1, 0.38, 0.22, 390),
        ("Johan Manzambi", "Switzerland", 3, 2, 0.34, 0.16, 340),
        ("Folarin Balogun", "United States", 3, 0, 0.45, 0.12, 315),
        ("Ismael Saibari", "Morocco", 3, 0, 0.32, 0.15, 392),
        ("Azzedine Ounahi", "Morocco", 2, 0, 0.28, 0.18, 440),
        ("Leandro Trossard", "Belgium", 2, 2, 0.38, 0.22, 360),
        ("Bradley Barcola", "France", 2, 0, 0.35, 0.22, 345),
        ("Lamine Yamal", "Spain", 1, 1, 0.34, 0.36, 395),
        ("Field", "NONE", 0, 0, 0, 0, 300),
    ]

    # Calibrated to July 6 Oddschecker Golden Ball market (Mbappe 7/4, Messi 3/1, Olise 6/1, Bellingham 10/1)
    # Note: Bellingham (4g/1a + Azteca heroics -> 10/1!) now splits England near-even or ahead of Kane!
    # Note: Olise (5 assists, 6/1 on Oddschecker!) commands strong within-France share (~27% vs Mbappe ~54%)
    # Note: Spain won 1-0 via Merino (6 straight clean sheets, Simon 609m; Yamal 1g/1a, Pedri orchestrator)
    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.89), ("Other_ARG", 0.11)],
        "France": [("Kylian Mbappé", 0.54), ("Michael Olise", 0.27), ("Ousmane Dembélé", 0.13), ("Other_FRA", 0.06)],
        "Spain": [("Lamine Yamal", esp_yamal_share), ("Pedri", 0.26), ("Mikel Oyarzabal", 0.11), ("Unai Simón", 0.09), ("Other_ESP", round(1.0 - esp_yamal_share - 0.46, 2))],
        "England": [("Jude Bellingham", 0.47), ("Harry Kane", 0.41), ("Other_ENG", 0.12)],
        "Norway": [("Erling Haaland", 0.85), ("Martin Ødegaard", 0.10), ("Other_NOR", 0.05)],
        "Colombia": [("Luis Díaz", 0.48), ("James Rodríguez", 0.32), ("Jhon Arias", 0.11), ("Other_COL", 0.09)],
        "Morocco": [("Achraf Hakimi", 0.42), ("Brahim Díaz", 0.22), ("Yassine Bounou", 0.20), ("Azzedine Ounahi", 0.16)],
        "Switzerland": [("Johan Manzambi", 0.36), ("Granit Xhaka", 0.36), ("Other_SUI", 0.28)],
        "United States": [("Christian Pulisic", 0.50), ("Folarin Balogun", 0.35), ("Other_USA", 0.15)],
        "Belgium": [("Thibaut Courtois", 0.32), ("Leandro Trossard", 0.28), ("Other_BEL", 0.40)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.38,
        "France": 1.24,
        "Norway": 1.22,    # Haaland 7g + historic upset narrative
        "England": 1.12,   # Bellingham 4g + Kane 6g huge narrative momentum
        "Spain": 1.06,     # Collective juggernaut (unbeaten in 35, 6 clean sheets)
        "Morocco": 0.96,
        "Colombia": 0.90,
        "Switzerland": 0.86,
    }

    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} (scale={scale}, sigma={sigma}) ====================")
    print(f"  LOCKED QF1: FRA-MAR(Saib{mar_saibari_qf})={base_p('France','Morocco',0,mar_saibari_qf):.3f}")
    print(f"  LOCKED QF3: ENG(Quan{eng_quansah_qf})-NOR={base_p('England','Norway',eng_quansah_qf,0):.3f}")
    print(f"  Rem R16: USA-BEL(Bench{bel_bench_r16})={base_p('United States','Belgium',25,bel_bench_r16):.3f} | ARG-EGY(Fat{arg_et_fatigue_r16})={base_p('Argentina','Egypt',arg_et_fatigue_r16,0):.3f} | COL-SUI(Van+{sui_van_bonus},Inj{sui_inj_r16})={base_p('Colombia','Switzerland',0,sui_van_bonus+sui_inj_r16):.3f}")
    print(f"  Key SF/QF: FRA-ESP={base_p('France','Spain'):.3f} | ESP-USA(LA+25)={base_p('Spain','United States',0,25):.3f} | ESP-BEL={base_p('Spain','Belgium'):.3f}")

    m94_usa = 0; m95_arg = 0; m96_col = 0
    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        team_matches = {}

        def play_ko(a, b, venue=None, mod_a=0, mod_b=0):
            ba = mod_a; bb = mod_b
            if venue == "USA":
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

        # 5 CONFIRMED R16 WINNERS (July 4, 5, 6):
        w = {
            "M89": "France",
            "M90": "Morocco",
            "M91": "Norway",
            "M92": "England",
            "M93": "Spain",
        }
        for t in ["France", "Morocco", "Norway", "England", "Spain"]:
            counts["Reach_QF"][t] += 1

        # REMAINING 3 R16 MATCHES:
        w["M94"], _ = play_ko("United States", "Belgium", venue="USA", mod_a=0, mod_b=bel_bench_r16)
        w["M95"], _ = play_ko("Argentina", "Egypt", venue=None, mod_a=arg_et_fatigue_r16, mod_b=0)
        w["M96"], _ = play_ko("Switzerland", "Colombia", venue="Vancouver", mod_a=sui_inj_r16, mod_b=0)
        if w["M94"] == "United States": m94_usa += 1
        if w["M95"] == "Argentina": m95_arg += 1
        if w["M96"] == "Colombia": m96_col += 1
        for mid in ["M94", "M95", "M96"]:
            counts["Reach_QF"][w[mid]] += 1

        # QUARTERFINALS:
        qf_pairs = [
            ("M97", w["M89"], w["M90"], None, 0, mar_saibari_qf),   # Boston QF: France vs Morocco
            ("M98", w["M93"], w["M94"], "USA", 0, 0),               # LA QF: Spain vs USA/BEL
            ("M99", w["M91"], w["M92"], None, 0, eng_quansah_qf),   # Miami QF: Norway vs England
            ("M100", w["M95"], w["M96"], None, 0, sui_inj_late if w["M96"] == "Switzerland" else 0), # KC QF
        ]
        for mid, a, b, v, ma, mb in qf_pairs:
            w[mid], _ = play_ko(a, b, venue=v, mod_a=ma, mod_b=mb)
            counts["Reach_SF"][w[mid]] += 1

        counts["QF_Boston"][w["M97"]] += 1
        counts["QF_LA"][w["M98"]] += 1
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

        # GOLDEN BOOT (unbiased goal-advancement correlation):
        best_key = (-1, -1, -9999)
        best_name = None
        for pname, team, cg, ca, gpg, apg, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(1.7)
                key = (fg, poisson(1.0), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg
            assists = ca
            mins = gmins
            ms = list(team_matches.get(team, []))
            if pname == "Ismael Saibari" and len(ms) > 0:
                if random.random() < 0.65:
                    ms = ms[1:]
            if pname == "Johan Manzambi" and len(ms) > 0:
                if random.random() < 0.40:
                    ms = ms[1:]
            miss_p = 0.055 if pname == "Lionel Messi" else 0.025
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

    print(f"  Sim R16 rates: USA={m94_usa/N:.3f}, ARG={m95_arg/N:.3f}, COL={m96_col/N:.3f}")
    print("  Exp rem games:", {t: round(ko_games_sum[t]/N, 2) for t in ["France", "Morocco", "Spain", "Argentina", "England", "Norway", "Colombia", "Switzerland", "United States", "Belgium", "Egypt"]})
    out = {}
    for key in ["QF_Boston", "QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"]:
        top = counts[key].most_common(8)
        out[key] = {t: cnt/N for t, cnt in top}
        s = ", ".join(f"{t}:{cnt/N:.4f}" for t, cnt in top)
        print(f"  {key:12s}: {s}")
    out["GOLDEN_BOOT"] = {n: c/N for n, c in gb_wins.most_common(8)}
    out["GBALL_TEAM"] = {n: c/N for n, c in gball_team_wins.most_common(10)}
    out["GBALL_STAR"] = {n: c/N for n, c in gball_star_wins.most_common(10)}
    print("  GOLDEN_BOOT :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(8)))
    print("  GBALL_TEAM  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_team_wins.most_common(10)))
    print("  GBALL_STAR  :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_star_wins.most_common(10)))
    return out

r1 = run_sim("1. BASE BAYESIAN+MARKET BLEND", ELO_BASE, scale=410.0, sigma=48.0,
             bel_bench_r16=-18, sui_van_bonus=10, sui_inj_r16=-16, sui_inj_late=-6,
             mar_saibari_qf=-15, mar_saibari_late=-8, eng_quansah_qf=-5, arg_et_fatigue_r16=-8,
             haaland_gpg=0.95, kane_gpg=0.73, win_goal_ratio=1.75, esp_yamal_share=0.46, N=200000)

r2 = run_sim("2. MARKET-ANCHORED (BetMGM ENG-NOR, Sportune FRA-MAR, FD ARG-EGY)", ELO_MARKET, scale=400.0, sigma=42.0,
             bel_bench_r16=-10, sui_van_bonus=10, sui_inj_r16=-14, sui_inj_late=-5,
             mar_saibari_qf=-15, mar_saibari_late=-8, eng_quansah_qf=-4, arg_et_fatigue_r16=-6,
             haaland_gpg=0.88, kane_gpg=0.72, win_goal_ratio=1.60, esp_yamal_share=0.42, N=200000)

r3 = run_sim("3. PURE BAYESIAN (Spain 6 CS, Norway form, USA bench edge)", ELO_PURE, scale=410.0, sigma=48.0,
             bel_bench_r16=-24, sui_van_bonus=8, sui_inj_r16=-18, sui_inj_late=-6,
             mar_saibari_qf=-14, mar_saibari_late=-7, eng_quansah_qf=-6, arg_et_fatigue_r16=-10,
             haaland_gpg=1.00, kane_gpg=0.75, win_goal_ratio=1.85, esp_yamal_share=0.50, N=150000)

r4 = run_sim("4. UPSET-CONSERVATIVE (wider sigma, stronger MAR/NOR/SUI/EGY)", ELO_CONSERVATIVE, scale=425.0, sigma=55.0,
             bel_bench_r16=-14, sui_van_bonus=12, sui_inj_r16=-12, sui_inj_late=-5,
             mar_saibari_qf=-12, mar_saibari_late=-5, eng_quansah_qf=-6, arg_et_fatigue_r16=-10,
             haaland_gpg=0.92, kane_gpg=0.71, win_goal_ratio=1.70, esp_yamal_share=0.45, N=150000)

# Weighted Ensemble: 35% Base + 30% Market-Anchored + 20% Pure + 15% Conservative
weights = [(r1, 0.35), (r2, 0.30), (r3, 0.20), (r4, 0.15)]
print("\n==================== WEIGHTED ENSEMBLE (35/30/20/15) ====================")
for key in ["QF_Boston", "QF_LA", "QF_Miami", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "GOLDEN_BOOT"]:
    agg = Counter()
    for res, wt in weights:
        for k, v in res[key].items():
            agg[k] += wt * v
    top = agg.most_common(8)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in top))

agg_gb = Counter()
for res, wt in weights:
    for k, v in res["GBALL_TEAM"].items():
        agg_gb[k] += wt * 0.45 * v
    for k, v in res["GBALL_STAR"].items():
        agg_gb[k] += wt * 0.55 * v
print("  GOLDEN_BALL : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb.most_common(12)))
