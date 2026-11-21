import random, math
from collections import Counter

# ---------------------------------------------------------
# 1. Exact Shin/Logit-style market calibration to SI June 28 + FanDuel R32 lines
# ---------------------------------------------------------
def am_to_p(o):
    return (-o)/(-o+100) if o < 0 else 100/(o+100)

si_odds = {
    "France": 370, "Argentina": 470, "England": 550, "Spain": 600,
    "Brazil": 1200, "Portugal": 1200, "Netherlands": 1600, "Germany": 1600,
    "Norway": 3300, "Colombia": 3500, "United States": 4000, "Morocco": 4500,
    "Mexico": 4500, "Belgium": 5000, "Japan": 5500, "Switzerland": 5500,
    "Senegal": 10000, "Ecuador": 12500, "Ivory Coast": 12500, "Croatia": 15000,
    "Egypt": 20000, "Canada": 22500, "Sweden": 22500, "Ghana": 25000,
    "Australia": 25000, "Austria": 40000, "Algeria": 40000, "Paraguay": 50000,
    "DR Congo": 200000, "Cape Verde": 250000, "Bosnia and Herzegovina": 250000, "South Africa": 250000,
}

# Check what power_k matches BOTH top-of-book and FanDuel R32 lines!
# Note: in a 32-way market with favorite-longshot bias, Shin's model or higher power_k on tail
# concentrates more mass on top teams and sharpens Elo spreads.
def shin_devig(odds_dict):
    raw = {k: am_to_p(v) for k, v in odds_dict.items()}
    S = sum(raw.values())
    # Solve for insider fraction z such that sum_i [ (sqrt(z^2 + 4*(1-z)*p_i^2/S) - z) / (2*(1-z)) ] = 1
    lo, hi = 0.0, 0.25
    for _ in range(60):
        z = (lo + hi) / 2
        tot = sum((math.sqrt(z*z + 4*(1-z)*(p*p)/S) - z) / (2*(1-z)) for p in raw.values())
        if tot > 1.0:
            lo = z
        else:
            hi = z
    z = (lo + hi) / 2
    return z, {k: (math.sqrt(z*z + 4*(1-z)*(p*p)/S) - z) / (2*(1-z)) for k, p in raw.items()}

z_shin, si_shin = shin_devig(si_odds)
print(f"SI Shin z={z_shin:.5f}")
for t in ["France", "Argentina", "England", "Spain", "Brazil", "Portugal", "Netherlands", "Germany", "Norway", "Colombia", "Morocco", "Canada"]:
    print(f"  {t:15s}: Shin={si_shin[t]:.4f}")

# ---------------------------------------------------------
# 2. Define 3 Elo sets for sensitivity & blending (scale=400 in KO matches)
# ---------------------------------------------------------
# Model A: Market-calibrated (anchored to SI Shin + FanDuel R32 sharp spreads!)
# Let's verify R32 implied match probs for Model A and Model B!
ELO_MARKET = {
    "France": 2150,
    "Spain": 2095,
    "England": 2085,       # SI +550 (very high), DK +750 -> blend ~2085
    "Argentina": 2080,
    "Brazil": 2045,        # FanDuel -310 vs Japan (72% -> +165 diff -> Japan 1880)
    "Portugal": 2040,
    "Germany": 2030,       # FanDuel -750 vs Paraguay (84% -> +285 diff -> Paraguay 1745)
    "Netherlands": 2015,   # FanDuel -188 vs Morocco (62% -> +86 diff -> Morocco 1929)
    "Norway": 1955,
    "Colombia": 1955,
    "Morocco": 1930,
    "Belgium": 1920,
    "Mexico": 1905,        # +40 Azteca venue bonus in R32 & R16
    "United States": 1900, # +25 home bonus
    "Switzerland": 1900,
    "Japan": 1880,
    "Croatia": 1885,
    "Ecuador": 1865,
    "Senegal": 1865,
    "Ivory Coast": 1860,
    "Canada": 1845,        # Already beat South Africa 1-0! (FanDuel -340 -> 73.6%)
    "Sweden": 1835,
    "Austria": 1830,
    "Australia": 1805,
    "Egypt": 1805,
    "Ghana": 1800,
    "Algeria": 1795,
    "Paraguay": 1755,
    "DR Congo": 1745,
    "Cape Verde": 1735,
    "Bosnia and Herzegovina": 1730,
    "South Africa": 1680,  # Eliminated!
}

# Model B: Blended Superforecaster (Market + June 28 fundamental/injury/form news!)
# Specific June 28 adjustments vs pure market:
# - France: 2150 (Deschamps returns, 9 pts, 10 GF, Mbappé+Dembélé firing, Sweden missing CB Hien)
# - Argentina: 2095 (defending champs, 9 pts, rested 9 starters vs Jordan, Messi 6g, Romero back, huge depth)
# - Spain: 2095 (Pino confirmed SPRAIN not broken collarbone -> +5 vs June 27, still Williams adductor moderate)
# - England: 2065 (blend SI +550 and DK +750; 4-2 Croatia shows high ceiling, but sluggish Ghana/Panama + Reece James & Quansah BOTH injured at RB!)
# - Brazil: 2040 (6-0 last two games, Neymar more mins vs Japan, slight drag from Raphinha hamstring; Japan missing Kubo+Endo)
# - Portugal: 2025 (sluggish vs Colombia, only 2 SOT, 41yo Ronaldo played 90 mins & looked off pace, tough Croatia->Spain path)
# - Germany: 2015 (lost 1-2 Ecuador, Schlotterbeck OUT, but Brown back & Paraguay missing suspended Diego Gomez)
# - Netherlands: 2015 (10 GF, Brobbey firing, Gakpo staying with camp after tragedy, tough Morocco tie)
# - Colombia: 1975 (dominated Portugal 24-13 shots, unbeaten 1K, though coach warns on finishing)
# - Morocco: 1930 (unbeaten, 7 pts, Saibari 3g, FanDuel 37.8% vs Netherlands)
# - Norway: 1930 (rested full XI vs France, Haaland 4g in 2 games)
# - Belgium: 1915 (5-1 NZ, De Bruyne + Trossard firing)
# - Switzerland: 1905 (7 GF, unbeaten 1B, Manzambi 3g)
# - Mexico: 1895 (3-0-0, 0 conceded, +40 Azteca bonus)
# - Japan: 1880 (unbeaten, but missing Endo & likely Kubo)
# - Croatia: 1890 (slow starters hitting stride, Modric/Vlasic beat Ghana 2-1)
# - United States: 1885 (+25 home bonus, Pulisic back)
# - Ecuador: 1870 (beat Germany 2-1, only 2 GA)
# - Senegal: 1855 (5-0 Iraq, unbeaten?)
# - Ivory Coast: 1855 (strong attack)
# - Canada: 1840 (beat SA 1-0 late without Davies starting; already in R16!)
# - Sweden: 1825 (missing CB Hien)
# - Austria: 1830 (3-3 thriller vs Algeria)
# - Australia: 1805 (Italiano/Leckie out, but Egypt hit harder!)
# - Egypt: 1790 (Salah hamstring strain doubt, Fatouh hamstring tear OUT, Abdelmonem ankle bruise!)
# - Ghana: 1810 (held England 0-0, close 1-2 Croatia)
# - Algeria: 1805 (3-3 thriller vs Austria)
# - Paraguay: 1765 (missing suspended Diego Gomez, Alderete knee doubt, Almiron back)
# - DR Congo: 1755 (3-1 Uzbekistan, Wissa)
# - Cape Verde: 1755 (unbeaten 0-0 Spain, 2-2 Uruguay, 0-0 Saudi, though capt Ryan Mendes probe distraction)
# - Bosnia and Herzegovina: 1745
ELO_BLENDED = {
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

# Model C: Pure June 27 Fundamental Elo (from sim_wc2026_june27.py) on LOCKED June 28 bracket
ELO_OLD = {
    "France": 2145, "Argentina": 2115, "Spain": 2095, "Brazil": 2035,
    "Netherlands": 2020, "England": 2020, "Portugal": 2010, "Germany": 1995,
    "Colombia": 1975, "Morocco": 1920, "Norway": 1910, "Belgium": 1905,
    "Switzerland": 1900, "Japan": 1900, "Mexico": 1885, "Croatia": 1880,
    "United States": 1865, "Ecuador": 1865, "Ivory Coast": 1845, "Senegal": 1840,
    "Austria": 1835, "Canada": 1835, "Sweden": 1830, "Ghana": 1820,
    "Egypt": 1810, "Paraguay": 1810, "Australia": 1800, "Algeria": 1800,
    "Bosnia and Herzegovina": 1790, "South Africa": 1775, "DR Congo": 1770, "Cape Verde": 1765,
}

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_mc(name, base_elo, scale=410.0, sigma=50.0, N=150000, seed=20260628):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"
    ]}
    ko_games_sum = Counter()

    # Check R32 win probs at base_elo
    print(f"\n================ {name} (scale={scale}, sigma={sigma}) ================")
    for a, b in [("Brazil", "Japan"), ("Germany", "Paraguay"), ("Netherlands", "Morocco"), ("France", "Sweden"), ("England", "DR Congo"), ("Argentina", "Cape Verde"), ("Portugal", "Croatia"), ("Spain", "Austria"), ("Colombia", "Ghana"), ("Australia", "Egypt")]:
        p = 1.0 / (1.0 + 10.0 ** (-(base_elo[a] - base_elo[b]) / scale))
        print(f"  R32 {a:12s} vs {b:12s}: {p:.3f}")

    # Golden Boot players AS OF JUNE 28 (AFTER ALL GROUP STAGE + CANADA-SA!)
    # Messi: 6 goals (0 pens), 0 assists, 3 matches (~210 mins)
    # Mbappé: 4 goals (0 pens), 0 assists, 3 matches
    # Dembélé: 4 goals (0 pens), 0 assists, 3 matches
    # Vinícius Jr: 4 goals (0 pens), 1 assist, 3 matches
    # Haaland: 4 goals (0 pens), 0 assists, 2 matches (~180 mins - fewest minutes tiebreak edge!)
    # Kane: 3 goals, 0 assists, 3 matches
    # Undav: 3 goals, 2 assists, 3 matches
    # Brobbey: 3 goals, 0 assists, 3 matches
    # Cunha: 3 goals, 0 assists, 3 matches
    # Saibari: 3 goals, 0 assists, 3 matches
    # Manzambi: 3 goals, 0 assists, 3 matches
    # Jonathan David: 3 goals, 0 assists, 4 matches (ALREADY PLAYED R32 & BLANKED!)
    # Ronaldo: 2 goals, 0 assists, 3 matches (played 270 mins, blanked vs Colombia)
    # Oyarzabal: 2 goals, 1 assist, 3 matches
    # Gakpo: 2 goals, 1 assist, 3 matches
    # Bellingham: 2 goals, 1 assist, 3 matches
    # Trossard: 2 goals, 1 assist, 3 matches
    # Lautaro Martinez: 1 goal (pen vs Jordan), Alvarez, etc.
    # Yamal: 1 goal, 1 assist
    GB_PLAYERS = [
        ("Lionel Messi", "Argentina", 6, 0, 0.72, 0.30, False),
        ("Kylian Mbappé", "France", 4, 0, 0.85, 0.25, False),
        ("Ousmane Dembélé", "France", 4, 0, 0.46, 0.30, False),
        ("Vinícius Júnior", "Brazil", 4, 1, 0.56, 0.28, False),
        ("Erling Haaland", "Norway", 4, 0, 0.85, 0.12, False),
        ("Harry Kane", "England", 3, 0, 0.68, 0.18, False),
        ("Deniz Undav", "Germany", 3, 2, 0.42, 0.18, False),
        ("Brian Brobbey", "Netherlands", 3, 0, 0.44, 0.12, False),
        ("Matheus Cunha", "Brazil", 3, 0, 0.40, 0.15, False),
        ("Jonathan David", "Canada", 3, 0, 0.42, 0.15, True),  # already played R32!
        ("Ismael Saibari", "Morocco", 3, 0, 0.38, 0.15, False),
        ("Johan Manzambi", "Switzerland", 3, 0, 0.34, 0.12, False),
        ("Cristiano Ronaldo", "Portugal", 2, 0, 0.46, 0.10, False),
        ("Mikel Oyarzabal", "Spain", 2, 1, 0.46, 0.22, False),
        ("Cody Gakpo", "Netherlands", 2, 1, 0.38, 0.20, False),
        ("Jude Bellingham", "England", 2, 1, 0.35, 0.22, False),
        ("Leandro Trossard", "Belgium", 2, 1, 0.40, 0.20, False),
        ("Lamine Yamal", "Spain", 1, 1, 0.35, 0.38, False),
        ("Field", "NONE", 0, 0, 0, 0, False),
    ]
    gb_wins = Counter()

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
        "Canada": "Netherlands", # R16 opponent placeholder
    }

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        def play_ko(a, b, venue=None):
            ba = 40 if (venue == "Azteca" and a == "Mexico") else (25 if (venue == "USA" and a == "United States") else 0)
            bb = 40 if (venue == "Azteca" and b == "Mexico") else (25 if (venue == "USA" and b == "United States") else 0)
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / scale))
            return (a, b) if random.random() < p else (b, a)

        ko_games = Counter()
        w = {}
        # M73 ALREADY COMPLETED: Canada beat South Africa 1-0!
        w["M73"] = "Canada"
        # Remaining 15 R32 matches:
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

        r16_pairs = [
            ("M89", w["M74"], w["M77"], None),
            ("M90", w["M73"], w["M75"], None),
            ("M91", w["M76"], w["M78"], None),
            ("M92", w["M79"], w["M80"], "Azteca"),
            ("M93", w["M83"], w["M84"], None),
            ("M94", w["M81"], w["M82"], "USA"),
            ("M95", w["M86"], w["M88"], None),
            ("M96", w["M85"], w["M87"], None),
        ]
        for mid, a, b, v in r16_pairs:
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v)
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
        w103, _ = play_ko(l101, l102)
        ko_games[w101] += 1; ko_games[w102] += 1
        w104, _ = play_ko(w101, w102)

        counts["ThirdPlace"][w103] += 1
        counts["Champion"][w104] += 1
        for t, cnt in ko_games.items():
            ko_games_sum[t] += cnt

        # Golden Boot draw
        best_key = (-1, -1, -1.0)
        best_name = None
        for pname, team, cg, ca, gpg, apg, played_r32 in GB_PLAYERS:
            if team == "NONE":
                fg = 2 + poisson(3.0)
                key = (fg, poisson(1.2), random.random())
                if key > best_key:
                    best_key = key; best_name = "Field"
                continue
            goals = cg
            assists = ca
            ng = ko_games[team]
            if ng > 0:
                mult = max(0.4, random.gauss(1.0, 0.20))
                if not played_r32:
                    opp = r32_opp_map.get(team)
                    opp_elo = base_elo.get(opp, 1850)
                    r32_boost = max(0.75, min(1.45, 1.0 + (1870 - opp_elo) / 300.0))
                    exp_g = gpg * mult * (r32_boost + max(0, ng - 1) * 0.96)
                else:
                    exp_g = gpg * mult * (ng * 0.92)
                goals += poisson(exp_g)
                assists += poisson(ng * apg)
            # Fewest minutes tiebreak edge: Messi (~210m) & Haaland (~180m) played fewer group mins than Mbappé/Vini/Kane/Dembélé (~270m)
            min_edge = 0.65 if pname in ("Erling Haaland", "Lionel Messi") else 0.50
            key = (goals, assists, min_edge + random.uniform(-0.3, 0.3))
            if key > best_key:
                best_key = key; best_name = pname
        gb_wins[best_name] += 1

    print("Exp rem KO games:", {t: round(ko_games_sum[t]/N, 2) for t in ["Argentina", "France", "England", "Spain", "Brazil", "Portugal", "Netherlands", "Germany", "Colombia", "Norway", "Canada"]})
    for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final", "Reach_SF"]:
        print(f"\n--- {key} ---")
        top = counts[key].most_common(7)
        for t, cnt in top:
            print(f"  {t:22s}: {cnt/N:.4f}")
        print(f"  Top5 sum = {sum(cnt for _, cnt in top[:5])/N:.4f}")
    print("\n--- GOLDEN BOOT ---")
    for pname, cnt in gb_wins.most_common(10):
        print(f"  {pname:22s}: {cnt/N:.4f}")

run_mc("MODEL A: MARKET-CALIBRATED", ELO_MARKET, scale=400.0, sigma=45.0, N=120000)
run_mc("MODEL B: BLENDED SUPERFORECASTER", ELO_BLENDED, scale=410.0, sigma=50.0, N=150000)
run_mc("MODEL C: OLD JUNE 27 ELO ON LOCKED BRACKET", ELO_OLD, scale=440.0, sigma=55.0, N=100000)
