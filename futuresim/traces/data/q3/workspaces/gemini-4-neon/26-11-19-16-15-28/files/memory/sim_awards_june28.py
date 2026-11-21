import random, math
from collections import Counter

# Import Model B blended Elos + test Golden Boot sensitivity + Golden Ball model
from sim_wc2026_june28 import ELO_BLENDED, ELO_MARKET

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def sim_gb(label, elo_map, messi_gpg, mbappe_gpg, haaland_gpg, vini_gpg, demb_gpg, kane_gpg, scale=410.0, sigma=50.0, N=100000):
    random.seed(20260628)
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
    players = [
        ("Lionel Messi", "Argentina", 6, 0, messi_gpg, 0.28, False, 210),
        ("Kylian Mbappé", "France", 4, 0, mbappe_gpg, 0.24, False, 260),
        ("Ousmane Dembélé", "France", 4, 0, demb_gpg, 0.30, False, 250),
        ("Vinícius Júnior", "Brazil", 4, 1, vini_gpg, 0.26, False, 265),
        ("Erling Haaland", "Norway", 4, 0, haaland_gpg, 0.12, False, 180),
        ("Harry Kane", "England", 3, 0, kane_gpg, 0.18, False, 255),
        ("Deniz Undav", "Germany", 3, 2, 0.42, 0.18, False, 250),
        ("Brian Brobbey", "Netherlands", 3, 0, 0.44, 0.12, False, 250),
        ("Matheus Cunha", "Brazil", 3, 0, 0.42, 0.15, False, 250),
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
    gb_wins = Counter()
    # Also simulate Golden Ball!
    # Historical Golden Ball facts:
    # - 11/11 last winners reached the Semifinals; ~75-80% reached the Final; ~50% won or ~30% runner-up, ~20% SF loser!
    # - Winner narrative strongly favors team's talisman + Golden Boot/goals/assists + media narrative (Messi last dance!)
    gball_wins = Counter()
    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in elo_map.items()}
        def play_ko(a, b, venue=None):
            ba = 40 if (venue == "Azteca" and a == "Mexico") else (25 if (venue == "USA" and a == "United States") else 0)
            bb = 40 if (venue == "Azteca" and b == "Mexico") else (25 if (venue == "USA" and b == "United States") else 0)
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / scale))
            return (a, b) if random.random() < p else (b, a)

        ko_games = Counter()
        w = {"M73": "Canada"}
        for mid, a, b, v in [
            ("M74", "Germany", "Paraguay", None), ("M75", "Netherlands", "Morocco", None),
            ("M76", "Brazil", "Japan", None), ("M77", "France", "Sweden", None),
            ("M78", "Ivory Coast", "Norway", None), ("M79", "Mexico", "Ecuador", "Azteca"),
            ("M80", "England", "DR Congo", None), ("M81", "United States", "Bosnia and Herzegovina", "USA"),
            ("M82", "Belgium", "Senegal", None), ("M83", "Portugal", "Croatia", None),
            ("M84", "Spain", "Austria", None), ("M85", "Switzerland", "Algeria", None),
            ("M86", "Argentina", "Cape Verde", None), ("M87", "Colombia", "Ghana", None),
            ("M88", "Australia", "Egypt", None),
        ]:
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v)
        for mid, a, b, v in [
            ("M89", w["M74"], w["M77"], None), ("M90", w["M73"], w["M75"], None),
            ("M91", w["M76"], w["M78"], None), ("M92", w["M79"], w["M80"], "Azteca"),
            ("M93", w["M83"], w["M84"], None), ("M94", w["M81"], w["M82"], "USA"),
            ("M95", w["M86"], w["M88"], None), ("M96", w["M85"], w["M87"], None),
        ]:
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v)
        for mid, a, b, v in [
            ("M97", w["M89"], w["M90"], None), ("M98", w["M93"], w["M94"], "USA"),
            ("M99", w["M91"], w["M92"], None), ("M100", w["M95"], w["M96"], None),
        ]:
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v)
        ko_games[w["M97"]] += 1; ko_games[w["M98"]] += 1
        w101, l101 = play_ko(w["M97"], w["M98"], venue="USA")
        ko_games[w["M99"]] += 1; ko_games[w["M100"]] += 1
        w102, l102 = play_ko(w["M99"], w["M100"])
        ko_games[l101] += 1; ko_games[l102] += 1
        w103, l103 = play_ko(l101, l102)
        ko_games[w101] += 1; ko_games[w102] += 1
        w104, l104 = play_ko(w101, w102)

        # Golden Boot
        best_key = (-1, -1, -9999)
        best_name = None
        p_goals = {}
        for pname, team, cg, ca, gpg, apg, played_r32, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(3.0)
                key = (fg, poisson(1.2), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg; assists = ca
            ng = ko_games[team]
            # Small injury/bench miss chance per KO game (higher for 39yo Messi ~5% per game, ~2.5% others)
            miss_p = 0.045 if pname == "Lionel Messi" else 0.025
            eff_ng = sum(1 for _ in range(ng) if random.random() > miss_p)
            if eff_ng > 0:
                mult = max(0.35, random.gauss(1.0, 0.25))
                if not played_r32:
                    opp = r32_opp_map.get(team)
                    opp_elo = elo_map.get(opp, 1850)
                    r32_boost = max(0.75, min(1.40, 1.0 + (1870 - opp_elo) / 320.0))
                    exp_g = gpg * mult * (r32_boost + max(0, eff_ng - 1) * 0.94)
                else:
                    exp_g = gpg * mult * (eff_ng * 0.90)
                goals += poisson(exp_g)
                assists += poisson(eff_ng * apg)
            mins = gmins + eff_ng * 85
            p_goals[pname] = goals
            key = (goals, assists, -mins)
            if key > best_key:
                best_key = key; best_name = pname
        gb_wins[best_name] += 1

        # Golden Ball conditional on Final 4:
        # Weighting: Champion ~55%, Runner-up ~30%, 3rd place ~10%, 4th place ~5%
        r = random.random()
        if r < 0.55:
            gb_team = w104
        elif r < 0.85:
            gb_team = l104
        elif r < 0.95:
            gb_team = w103
        else:
            gb_team = l103
        # Slight extra Messi/Mbappe/Yamal narrative bonus if they win Golden Boot while in Final 4
        # Conditional player share within winning/finalist team:
        TEAM_SHARES = {
            "Argentina": [("Lionel Messi", 0.84), ("Other_ARG", 0.16)],
            "France": [("Kylian Mbappé", 0.52), ("Ousmane Dembélé", 0.24), ("Michael Olise", 0.14), ("Other_FRA", 0.10)],
            "Spain": [("Lamine Yamal", 0.56), ("Pedri", 0.22), ("Other_ESP", 0.22)],
            "England": [("Jude Bellingham", 0.40), ("Harry Kane", 0.38), ("Other_ENG", 0.22)],
            "Brazil": [("Vinícius Júnior", 0.62), ("Neymar", 0.15), ("Other_BRA", 0.23)],
            "Portugal": [("Bruno Fernandes", 0.35), ("Cristiano Ronaldo", 0.30), ("Other_POR", 0.35)],
            "Norway": [("Erling Haaland", 0.80), ("Other_NOR", 0.20)],
            "Germany": [("Jamal Musiala", 0.38), ("Florian Wirtz", 0.35), ("Other_GER", 0.27)],
            "Netherlands": [("Virgil van Dijk", 0.30), ("Cody Gakpo", 0.28), ("Other_NED", 0.42)],
        }
        shares = TEAM_SHARES.get(gb_team, [("Other_TEAM", 1.0)])
        u = random.random(); cum = 0.0
        for pl, sh in shares:
            cum += sh
            if u <= cum:
                gball_wins[pl] += 1
                break

    print(f"\n=== {label} ===")
    print("  GOLDEN BOOT:")
    for n, c in gb_wins.most_common(7):
        print(f"    {n:20s}: {c/N:.4f}")
    print("  GOLDEN BALL:")
    for n, c in gball_wins.most_common(8):
        print(f"    {n:20s}: {c/N:.4f}")

sim_gb("BASE (Blended Elo, baseline gpg)", ELO_BLENDED, 0.68, 0.85, 0.85, 0.56, 0.48, 0.68)
sim_gb("CONSERVATIVE MESSI / HIGH MBAPPE+KANE", ELO_BLENDED, 0.56, 0.92, 0.88, 0.58, 0.50, 0.74)
sim_gb("MARKET ELO (higher England -> higher Kane/Bellingham)", ELO_MARKET, 0.65, 0.88, 0.85, 0.56, 0.48, 0.70)
