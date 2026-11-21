import random, math
from collections import Counter

# Test two Elo profiles:
# Profile A (Moderate updates from June 24-25 baseline)
# Profile B (Stronger form updates)
PROFILES = {
    "Moderate": {
        "France": 2135, "Spain": 2125, "Argentina": 2110, "England": 2045,
        "Brazil": 2020, "Netherlands": 2015, "Portugal": 2015, "Germany": 2005,
        "Colombia": 1965, "Morocco": 1920, "Norway": 1915, "Switzerland": 1900,
        "Japan": 1900, "Mexico": 1880, "Uruguay": 1885, "Croatia": 1875,
        "United States": 1865, "Ecuador": 1860, "Belgium": 1865, "Sweden": 1850,
        "Ivory Coast": 1840, "Senegal": 1840, "Austria": 1835, "Canada": 1835,
        "Egypt": 1825, "Ghana": 1820, "South Korea": 1815, "Australia": 1815,
        "Paraguay": 1810, "Scotland": 1805, "Algeria": 1800,
        "Bosnia and Herzegovina": 1790, "Iran": 1785, "South Africa": 1770,
        "DR Congo": 1770, "Cape Verde": 1765, "Saudi Arabia": 1745,
        "New Zealand": 1720, "Uzbekistan": 1715, "Jordan": 1690, "Panama": 1690,
    },
    "Conservative_Germany_High": {
        "France": 2130, "Spain": 2120, "Argentina": 2105, "England": 2050,
        "Brazil": 2010, "Netherlands": 2010, "Portugal": 2015, "Germany": 2015,
        "Colombia": 1960, "Morocco": 1915, "Norway": 1915, "Switzerland": 1895,
        "Japan": 1895, "Mexico": 1875, "Uruguay": 1890, "Croatia": 1875,
        "United States": 1865, "Ecuador": 1855, "Belgium": 1870, "Sweden": 1845,
        "Ivory Coast": 1835, "Senegal": 1835, "Austria": 1835, "Canada": 1835,
        "Egypt": 1820, "Ghana": 1815, "South Korea": 1815, "Australia": 1810,
        "Paraguay": 1805, "Scotland": 1805, "Algeria": 1795,
        "Bosnia and Herzegovina": 1785, "Iran": 1780, "South Africa": 1760,
        "DR Congo": 1765, "Cape Verde": 1760, "Saudi Arabia": 1745,
        "New Zealand": 1715, "Uzbekistan": 1715, "Jordan": 1690, "Panama": 1690,
    }
}

from sim_wc2026_june26 import THIRD_SLOTS, poisson, sim_match_score, rank_group_4, sim_remaining_groups, assign_thirds

# Full realistic 26-player Golden Boot roster (with realistic KO gpg calibrated to WC KO scoring rates ~0.88x group rate)
GB_ROSTER = [
    # (name, team, curr_g, curr_a, ko_gpg, ko_apg, md3_type)
    ("Lionel Messi", "Argentina", 5, 1, 0.62, 0.35, "messi"),
    ("Kylian Mbappé", "France", 4, 1, 0.80, 0.25, None),
    ("Ousmane Dembélé", "France", 4, 0, 0.52, 0.30, None),
    ("Vinícius Júnior", "Brazil", 4, 1, 0.56, 0.25, None),
    ("Erling Haaland", "Norway", 4, 0, 0.82, 0.12, None),
    ("Harry Kane", "England", 2, 1, 0.66, 0.20, "kane"),
    ("Mikel Oyarzabal", "Spain", 2, 1, 0.48, 0.22, "esp_fwd"),
    ("Deniz Undav", "Germany", 3, 0, 0.44, 0.12, None),
    ("Brian Brobbey", "Netherlands", 3, 0, 0.46, 0.12, None),
    ("Jonathan David", "Canada", 3, 0, 0.45, 0.15, None),
    ("Ismaila Sarr", "Senegal", 3, 0, 0.40, 0.15, None),
    ("Cristiano Ronaldo", "Portugal", 2, 0, 0.52, 0.10, "por_fwd"),
    ("Lamine Yamal", "Spain", 1, 1, 0.36, 0.40, "esp_wing"),
    ("Cody Gakpo", "Netherlands", 2, 1, 0.42, 0.20, None),
    ("Julian Alvarez", "Argentina", 1, 1, 0.42, 0.18, "arg_fwd"),
    ("Lautaro Martinez", "Argentina", 0, 0, 0.42, 0.10, "arg_fwd"),
    ("Bukayo Saka", "England", 2, 1, 0.35, 0.25, "eng_wing"),
    ("Jude Bellingham", "England", 1, 1, 0.34, 0.20, "eng_wing"),
    ("Bruno Fernandes", "Portugal", 1, 2, 0.36, 0.35, "por_mid"),
    ("Luis Diaz", "Colombia", 2, 1, 0.42, 0.20, "col_fwd"),
    ("Nicolas Pepe", "Ivory Coast", 2, 0, 0.38, 0.15, None),
    ("Michael Olise", "France", 1, 2, 0.28, 0.40, None),
    ("Jamal Musiala", "Germany", 1, 1, 0.34, 0.22, None),
    ("Florian Wirtz", "Germany", 2, 1, 0.35, 0.25, None),
    ("Rodrygo", "Brazil", 1, 1, 0.38, 0.20, None),
    ("Nico Williams", "Spain", 1, 1, 0.32, 0.25, "esp_wing"),
    ("Mohamed Salah", "Egypt", 2, 1, 0.48, 0.20, "egy_fwd"),
    ("Alexander Isak", "Sweden", 2, 0, 0.50, 0.12, None),
]

for pname, base_elo in PROFILES.items():
    random.seed(12345)
    N = 60000
    counts = {k: Counter() for k in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final"]}
    gb_wins = Counter()
    ko_avg = Counter()

    for _ in range(N):
        ELO = {t: r + random.gauss(0, 55) for t, r in base_elo.items()}
        def play_ko(a, b, venue=None):
            ba = 45 if (venue == "Azteca" and a == "Mexico") else (30 if (venue == "USA" and a == "United States") else 0)
            bb = 45 if (venue == "Azteca" and b == "Mexico") else (30 if (venue == "USA" and b == "United States") else 0)
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / 440.0))
            return (a, b) if random.random() < p else (b, a)

        g, (gsp, guru, geng, gpor) = sim_remaining_groups(ELO)
        th, adv = assign_thirds(g)

        ko_games = Counter()
        r32_pairs = [
            ("M73", g["A"][1], g["B"][1], None), ("M74", g["E"][0], th["M74"], None),
            ("M75", g["F"][0], g["C"][1], None), ("M76", g["C"][0], g["F"][1], None),
            ("M77", g["I"][0], th["M77"], None), ("M78", g["E"][1], g["I"][1], None),
            ("M79", g["A"][0], th["M79"], "Azteca"), ("M80", g["L"][0], th["M80"], None),
            ("M81", g["D"][0], th["M81"], "USA"), ("M82", g["G"][0], th["M82"], None),
            ("M83", g["K"][1], g["L"][1], None), ("M84", g["H"][0], g["J"][1], None),
            ("M85", g["B"][0], th["M85"], None), ("M86", g["J"][0], g["H"][1], None),
            ("M87", g["K"][0], th["M87"], None), ("M88", g["D"][1], g["G"][1], None),
        ]
        w = {}
        for mid, a, b, v in r32_pairs:
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v)

        r16_pairs = [
            ("M89", w["M74"], w["M77"], None), ("M90", w["M73"], w["M75"], None),
            ("M91", w["M76"], w["M78"], None), ("M92", w["M79"], w["M80"], "Azteca"),
            ("M93", w["M83"], w["M84"], None), ("M94", w["M81"], w["M82"], "USA"),
            ("M95", w["M86"], w["M88"], None), ("M96", w["M85"], w["M87"], None),
        ]
        for mid, a, b, v in r16_pairs:
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v)

        qf_pairs = [
            ("M97", w["M89"], w["M90"], None), ("M98", w["M93"], w["M94"], "USA"),
            ("M99", w["M91"], w["M92"], None), ("M100", w["M95"], w["M96"], None),
        ]
        for mid, a, b, v in qf_pairs:
            ko_games[a] += 1; ko_games[b] += 1
            w[mid], _ = play_ko(a, b, venue=v)

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

        for t in ["Argentina", "France", "Spain", "Brazil", "England", "Norway", "Germany", "Netherlands"]:
            ko_avg[t] += ko_games[t]

        if pname == "Moderate":
            best_key = (-1, -1, -1.0)
            best_name = None
            for name, team, cg, ca, gpg, apg, md3 in GB_ROSTER:
                goals, assists = cg, ca
                if md3 == "messi":
                    if random.random() < 0.35:
                        goals += poisson(1.05); assists += poisson(0.40)
                    else:
                        goals += poisson(0.15); assists += poisson(0.08)
                elif md3 == "kane":
                    goals += poisson(0.42 * max(geng, 1.4)); assists += poisson(0.18)
                elif md3 == "esp_fwd":
                    goals += poisson(0.36 * gsp); assists += poisson(0.18)
                elif md3 == "esp_wing":
                    goals += poisson(0.24 * gsp); assists += poisson(0.25)
                elif md3 == "por_fwd":
                    goals += poisson(0.38 * gpor); assists += poisson(0.10)
                elif md3 == "por_mid":
                    goals += poisson(0.22 * gpor); assists += poisson(0.25)
                elif md3 == "arg_fwd":
                    goals += poisson(0.70); assists += poisson(0.20)
                elif md3 == "eng_wing":
                    goals += poisson(0.22 * max(geng, 1.2)); assists += poisson(0.20)
                elif md3 == "col_fwd":
                    goals += poisson(0.35); assists += poisson(0.18)
                elif md3 == "egy_fwd":
                    goals += poisson(0.50); assists += poisson(0.20)
                ng = ko_games[team]
                if ng > 0:
                    mult = max(0.35, random.gauss(1.0, 0.25))
                    goals += poisson(ng * gpg * mult)
                    assists += poisson(ng * apg)
                key = (goals, assists, random.random())
                if key > best_key:
                    best_key = key; best_name = name
            gb_wins[best_name] += 1

    print(f"\n==================== PROFILE: {pname} ====================")
    for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final"]:
        top = counts[key].most_common(6)
        s = ", ".join(f"{t}:{c/N:.3f}" for t, c in top)
        print(f"  {key:12s}: {s}")
    if pname == "Moderate":
        print("  Avg KO games:", ", ".join(f"{t}:{ko_avg[t]/N:.2f}" for t in ["Argentina","France","Spain","Brazil","England","Norway","Germany","Netherlands"]))
        print("\n  === FULL 28-PLAYER GOLDEN BOOT ===")
        for name, c in gb_wins.most_common(12):
            print(f"    {name:20s}: {c/N:.4f}")
