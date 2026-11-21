import random, math
from collections import Counter

# Baseline June 28 Blended Elos (from sim_wc2026_june28.py)
ELO_JUNE28 = {
    "France": 2150,
    "Argentina": 2095,
    "Spain": 2095,
    "England": 2065,
    "Brazil": 2040,
    "Portugal": 2025,
    "Germany": 2015,
    "Netherlands": 2015,
    "Colombia": 1975,
    "Morocco": 1930,
    "Norway": 1930,
    "Belgium": 1915,
    "Switzerland": 1905,
    "Mexico": 1895,
    "Croatia": 1890,
    "United States": 1885,
    "Japan": 1880,
    "Ecuador": 1870,
    "Senegal": 1855,
    "Ivory Coast": 1855,
    "Canada": 1840,
    "Austria": 1830,
    "Sweden": 1825,
    "Ghana": 1810,
    "Australia": 1805,
    "Algeria": 1805,
    "Egypt": 1790,
    "Paraguay": 1765,
    "DR Congo": 1755,
    "Cape Verde": 1755,
    "Bosnia and Herzegovina": 1745,
    "South Africa": 1680,
}

# June 29 Bayesian-updated Elos:
# - Brazil: 2040 -> 2030 (won 2-1 vs Japan in 90+6', struggled 1H, Lucas Paqueta injured at HT, Casemiro booked; dominated 2H with Endrick)
# - Germany: 2015 -> 1990 (0 SOT in 1H vs Paraguay, 1-1 after 90', Musiala dropped for poor form, follows 1-2 Ecuador loss; ALSO -10 fatigue in R16 if ET)
# - Paraguay: 1765 -> 1785 (gritty 1-1 vs Germany in 90', though Enciso injured & Cubas booked)
# - France: 2150 -> 2155 (William Saliba returns to CB, Digne/Barcola stabilizing left flank)
ELO_JUNE29 = dict(ELO_JUNE28)
ELO_JUNE29["Brazil"] = 2030
ELO_JUNE29["Germany"] = 1990
ELO_JUNE29["Paraguay"] = 1785
ELO_JUNE29["France"] = 2155

# Also check exact Poisson-Skellam + Shootout calculation for Germany 1-1 Paraguay at 90' (+5' stoppage + 30' ET)
def poisson_pmf(k, lam):
    return math.exp(-lam) * (lam ** k) / math.factorial(k)

print("=== LIVE M74 (Germany 1-1 Paraguay at 90' + 5' stoppage + 30' ET + Pens) ===")
for label, lam_g, lam_p, p_pen in [
    ("Conservative (low ET tempo, 0.45 vs 0.16, pen 0.55)", 0.45, 0.16, 0.55),
    ("Base (moderate ET tempo, 0.52 vs 0.16, pen 0.565)", 0.52, 0.16, 0.565),
    ("Germany-leaning (Enciso off, 0.60 vs 0.14, pen 0.58)", 0.60, 0.14, 0.58),
    ("Paraguay-gritty (0.42 vs 0.18, pen 0.53)", 0.42, 0.18, 0.53),
]:
    pg_et = pp_et = p_draw = 0.0
    for g in range(8):
        for p in range(8):
            pr = poisson_pmf(g, lam_g) * poisson_pmf(p, lam_p)
            if g > p: pg_et += pr
            elif p > g: pp_et += pr
            else: p_draw += pr
    pg_adv = pg_et + p_draw * p_pen
    print(f"  {label}: Ger_ET={pg_et:.3f}, Par_ET={pp_et:.3f}, Pens={p_draw:.3f} => P(Ger adv)={pg_adv:.3f}")


def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1


def run_sim(label, base_elo, is_june29=True, p_ger_adv=0.67, ger_r16_fatigue=-10, scale=410.0, sigma=50.0, N=200000, seed=20260629):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"
    ]}
    ko_games_sum = Counter()
    gb_wins = Counter()
    gball_wins = Counter()

    r32_opp_map = {
        "Germany": "Paraguay", "Paraguay": "Germany",
        "France": "Sweden", "Sweden": "France",
        "Netherlands": "Morocco", "Morocco": "Netherlands",
        "Portugal": "Croatia", "Croatia": "Portugal",
        "Spain": "Austria", "Austria": "Spain",
        "United States": "Bosnia and Herzegovina", "Bosnia and Herzegovina": "United States",
        "Belgium": "Senegal", "Senegal": "Belgium",
        "Brazil": "Japan", "Japan": "Brazil",
        "Ivory Coast": "Norway", "Norway": "Ivory Coast",
        "Mexico": "Ecuador", "Ecuador": "Mexico",
        "England": "DR Congo", "DR Congo": "England",
        "Argentina": "Cape Verde", "Cape Verde": "Argentina",
        "Australia": "Egypt", "Egypt": "Australia",
        "Switzerland": "Algeria", "Algeria": "Switzerland",
        "Colombia": "Ghana", "Ghana": "Colombia",
        "Canada": "Netherlands",
    }

    # Player list: (name, team, curr_g, curr_a, gpg, apg, played_r32, gmins)
    if is_june29:
        players = [
            ("Lionel Messi", "Argentina", 6, 0, 0.65, 0.28, False, 200),
            ("Kylian Mbappé", "France", 4, 0, 0.87, 0.24, False, 260),
            ("Ousmane Dembélé", "France", 4, 0, 0.49, 0.30, False, 250),
            ("Vinícius Júnior", "Brazil", 4, 1, 0.56, 0.26, True, 355),   # BLANKED vs Japan!
            ("Erling Haaland", "Norway", 4, 0, 0.86, 0.12, False, 180),
            ("Harry Kane", "England", 3, 0, 0.70, 0.18, False, 255),
            ("Deniz Undav", "Germany", 3, 2, 0.38, 0.16, True, 148),      # BLANKED, subbed 62' vs Paraguay!
            ("Kai Havertz", "Germany", 3, 0, 0.44, 0.15, True, 340),      # Scored 54' vs Paraguay -> 3g! (still in ET!)
            ("Brian Brobbey", "Netherlands", 3, 0, 0.44, 0.12, False, 250),
            ("Matheus Cunha", "Brazil", 3, 0, 0.40, 0.15, True, 330),     # BLANKED vs Japan!
            ("Jonathan David", "Canada", 3, 0, 0.42, 0.15, True, 350),
            ("Ismael Saibari", "Morocco", 3, 0, 0.38, 0.15, False, 250),
            ("Johan Manzambi", "Switzerland", 3, 0, 0.34, 0.12, False, 250),
            ("Cristiano Ronaldo", "Portugal", 2, 0, 0.45, 0.10, False, 270),
            ("Mikel Oyarzabal", "Spain", 2, 1, 0.46, 0.22, False, 250),
            ("Cody Gakpo", "Netherlands", 2, 1, 0.38, 0.20, False, 260),
            ("Jude Bellingham", "England", 2, 1, 0.35, 0.22, False, 210),
            ("Leandro Trossard", "Belgium", 2, 1, 0.40, 0.20, False, 240),
            ("Lamine Yamal", "Spain", 1, 1, 0.35, 0.38, False, 220),
            ("Field", "NONE", 0, 0, 0, 0, False, 300),
        ]
    else:
        players = [
            ("Lionel Messi", "Argentina", 6, 0, 0.65, 0.28, False, 200),
            ("Kylian Mbappé", "France", 4, 0, 0.87, 0.24, False, 260),
            ("Ousmane Dembélé", "France", 4, 0, 0.49, 0.30, False, 250),
            ("Vinícius Júnior", "Brazil", 4, 1, 0.56, 0.26, False, 265),
            ("Erling Haaland", "Norway", 4, 0, 0.86, 0.12, False, 180),
            ("Harry Kane", "England", 3, 0, 0.70, 0.18, False, 255),
            ("Deniz Undav", "Germany", 3, 2, 0.42, 0.18, False, 86),
            ("Brian Brobbey", "Netherlands", 3, 0, 0.44, 0.12, False, 250),
            ("Matheus Cunha", "Brazil", 3, 0, 0.40, 0.15, False, 250),
            ("Jonathan David", "Canada", 3, 0, 0.42, 0.15, True, 350),
            ("Ismael Saibari", "Morocco", 3, 0, 0.38, 0.15, False, 250),
            ("Johan Manzambi", "Switzerland", 3, 0, 0.34, 0.12, False, 250),
            ("Cristiano Ronaldo", "Portugal", 2, 0, 0.45, 0.10, False, 270),
            ("Mikel Oyarzabal", "Spain", 2, 1, 0.46, 0.22, False, 250),
            ("Cody Gakpo", "Netherlands", 2, 1, 0.38, 0.20, False, 260),
            ("Jude Bellingham", "England", 2, 1, 0.35, 0.22, False, 210),
            ("Leandro Trossard", "Belgium", 2, 1, 0.40, 0.20, False, 240),
            ("Lamine Yamal", "Spain", 1, 1, 0.35, 0.38, False, 220),
            ("Field", "NONE", 0, 0, 0, 0, False, 300),
        ]

    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.84), ("Other_ARG", 0.16)],
        "France": [("Kylian Mbappé", 0.52), ("Ousmane Dembélé", 0.24), ("Michael Olise", 0.14), ("Other_FRA", 0.10)],
        "Spain": [("Lamine Yamal", 0.56), ("Pedri", 0.22), ("Other_ESP", 0.22)],
        "England": [("Jude Bellingham", 0.40), ("Harry Kane", 0.38), ("Other_ENG", 0.22)],
        "Brazil": [("Vinícius Júnior", 0.60), ("Neymar", 0.13), ("Casemiro/Other_BRA", 0.27)],
        "Portugal": [("Bruno Fernandes", 0.35), ("Cristiano Ronaldo", 0.30), ("Other_POR", 0.35)],
        "Norway": [("Erling Haaland", 0.80), ("Other_NOR", 0.20)],
        "Germany": [("Jamal Musiala", 0.36), ("Florian Wirtz", 0.36), ("Other_GER", 0.28)],
        "Netherlands": [("Virgil van Dijk", 0.30), ("Cody Gakpo", 0.28), ("Other_NED", 0.42)],
    }

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        def play_ko(a, b, venue=None, mod_a=0, mod_b=0):
            ba = (40 if (venue == "Azteca" and a == "Mexico") else (25 if (venue == "USA" and a == "United States") else 0)) + mod_a
            bb = (40 if (venue == "Azteca" and b == "Mexico") else (25 if (venue == "USA" and b == "United States") else 0)) + mod_b
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / scale))
            return (a, b) if random.random() < p else (b, a)

        ko_games = Counter()
        w = {}
        # M73 completed June 28: Canada beat South Africa 1-0
        w["M73"] = "Canada"

        if is_june29:
            # M76 COMPLETED June 29: Brazil beat Japan 2-1!
            w["M76"] = "Brazil"
            # M74 LIVE at 90' tied 1-1: use live conditional advancement prob!
            # Scale slightly by sampled ELO diff around base diff so correlation is preserved
            d_base = base_elo["Germany"] - base_elo["Paraguay"]
            d_samp = ELO["Germany"] - ELO["Paraguay"]
            # logit shift from Elo noise over remaining 35 mins (~0.4 weight of full game)
            logit0 = math.log(p_ger_adv / (1.0 - p_ger_adv))
            logit = logit0 + 0.40 * (d_samp - d_base) * math.log(10) / scale
            pg = 1.0 / (1.0 + math.exp(-logit))
            w["M74"] = "Germany" if random.random() < pg else "Paraguay"
            r32_rem = [
                ("M75", "Netherlands", "Morocco", None),
                ("M77", "France", "Sweden", None),
                ("M78", "Ivory Coast", "Norway", None),
                ("M79", "Mexico", "Ecuador", "Azteca"),
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
        else:
            r32_rem = [
                ("M74", "Germany", "Paraguay", None),
                ("M75", "Netherlands", "Morocco", None),
                ("M76", "Brazil", "Japan", None),
                ("M77", "France", "Sweden", None),
                ("M78", "Ivory Coast", "Norway", None),
                ("M79", "Mexico", "Ecuador", "Azteca"),
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
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v)

        # R16: apply fatigue to M74 winner if June 29 (played ~120 mins!)
        r16_pairs = [
            ("M89", w["M74"], w["M77"], None, ger_r16_fatigue if is_june29 else 0, 0),
            ("M90", w["M73"], w["M75"], None, 0, 0),
            ("M91", w["M76"], w["M78"], None, 0, 0),
            ("M92", w["M79"], w["M80"], "Azteca", 0, 0),
            ("M93", w["M83"], w["M84"], None, 0, 0),
            ("M94", w["M81"], w["M82"], "USA", 0, 0),
            ("M95", w["M86"], w["M88"], None, 0, 0),
            ("M96", w["M85"], w["M87"], None, 0, 0),
        ]
        for mid, a, b, v, ma, mb in r16_pairs:
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v, mod_a=ma, mod_b=mb)
            counts["Reach_QF"][w[mid]] += 1

        qf_pairs = [
            ("M97", w["M89"], w["M90"], None),
            ("M98", w["M93"], w["M94"], "USA"),
            ("M99", w["M91"], w["M92"], None),
            ("M100", w["M95"], w["M96"], None),
        ]
        for mid, a, b, v in qf_pairs:
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v)
            counts["Reach_SF"][w[mid]] += 1

        counts["QF_Boston"][w["M97"]] += 1
        counts["QF_KC"][w["M100"]] += 1

        ko_games[w["M97"]] += 1; ko_games[w["M98"]] += 1
        w101, l101 = play_ko(w["M97"], w["M98"], venue="USA")
        ko_games[w["M99"]] += 1; ko_games[w["M100"]] += 1
        w102, l102 = play_ko(w["M99"], w["M100"])

        counts["SF1_Dallas"][w101] += 1
        counts["SF2_Atlanta"][w102] += 1
        counts["Reach_Final"][w101] += 1
        counts["Reach_Final"][w102] += 1

        ko_games[l101] += 1; ko_games[l102] += 1
        w103, l103 = play_ko(l101, l102)
        ko_games[w101] += 1; ko_games[w102] += 1
        w104, l104 = play_ko(w101, w102)

        counts["ThirdPlace"][w103] += 1
        counts["Champion"][w104] += 1
        for t, cnt in ko_games.items():
            ko_games_sum[t] += cnt

        # Golden Boot
        best_key = (-1, -1, -9999)
        best_name = None
        for pname, team, cg, ca, gpg, apg, played_r32, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(3.0)
                key = (fg, poisson(1.2), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg; assists = ca
            # Small chance Havertz scores again in M74 extra time (~15% chance)
            if is_june29 and pname == "Kai Havertz":
                goals += poisson(0.15)
            ng = ko_games[team]
            miss_p = 0.045 if pname == "Lionel Messi" else 0.025
            eff_ng = sum(1 for _ in range(ng) if random.random() > miss_p)
            if eff_ng > 0:
                mult = max(0.35, random.gauss(1.0, 0.25))
                if not played_r32:
                    opp = r32_opp_map.get(team)
                    opp_elo = base_elo.get(opp, 1850)
                    r32_boost = max(0.75, min(1.40, 1.0 + (1870 - opp_elo) / 320.0))
                    exp_g = gpg * mult * (r32_boost + max(0, eff_ng - 1) * 0.94)
                else:
                    exp_g = gpg * mult * (eff_ng * 0.92)
                goals += poisson(exp_g)
                assists += poisson(eff_ng * apg)
            mins = gmins + eff_ng * 85
            key = (goals, assists, -mins)
            if key > best_key:
                best_key = key; best_name = pname
        gb_wins[best_name] += 1

        # Golden Ball
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
                gball_wins[pl] += 1
                break

    print(f"\n==================== {label} ====================")
    print("Exp rem KO games:", {t: round(ko_games_sum[t]/N, 2) for t in ["Argentina", "France", "England", "Spain", "Brazil", "Portugal", "Netherlands", "Germany", "Colombia", "Norway", "Canada", "Paraguay"]})
    for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion"]:
        top = counts[key].most_common(6)
        s = ", ".join(f"{t}:{cnt/N:.4f}" for t, cnt in top)
        print(f"  {key:12s}: {s}")
    print("  GOLDEN_BOOT :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(7)))
    print("  GOLDEN_BALL :", ", ".join(f"{n}:{c/N:.4f}" for n, c in gball_wins.most_common(7)))


run_sim("JUNE 28 BASELINE (pre-Brazil/Japan, pre-Ger/Par)", ELO_JUNE28, is_june29=False, N=150000)
run_sim("JUNE 29 BASE (Bra WON, Ger 1-1 Par @90' p=0.67, Ger-25/Bra-10)", ELO_JUNE29, is_june29=True, p_ger_adv=0.67, ger_r16_fatigue=-10, N=200000)
run_sim("JUNE 29 SENSITIVITY: Ger p=0.64, no Elo chg on Bra", dict(ELO_JUNE29, Brazil=2040), is_june29=True, p_ger_adv=0.64, ger_r16_fatigue=-10, N=120000)
run_sim("JUNE 29 SENSITIVITY: Ger p=0.70, mild Ger-15", dict(ELO_JUNE29, Germany=2000), is_june29=True, p_ger_adv=0.70, ger_r16_fatigue=-10, N=120000)
