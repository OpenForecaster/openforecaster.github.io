import random, math
from collections import Counter

random.seed(20260627)

# Updated Elo ratings as of late 2026-06-27 after Groups A-I and L completed
BASE_ELO = {
    "France": 2145,      # Locked 1I (9 pts, 10 GF, 4-1 NOR), faces Sweden (no Hien)
    "Argentina": 2115,   # Locked 1J, Messi resting vs Jordan, Romero training, dream path (Cape Verde -> AUS/EGY)
    "Spain": 2095,       # Locked 1H (1-0 URU via Muslera howler), downgraded -30 for Pino broken collarbone + Nico Williams groin + labored attack
    "Brazil": 2035,      # Locked 1C (3-0 SCO, +6 GD, 1 GA, Neymar back), faces Japan
    "Netherlands": 2020, # Locked 1F (7 pts, 10 GF), faces Morocco
    "England": 2020,     # Locked 1L (2-0 PAN, sluggish 1st half, Tuchel frustrated, Reece James hamstring out/doubt)
    "Portugal": 2010,    # 0-0 at 21' vs Colombia in Miami
    "Germany": 1995,     # Locked 1E, lost 1-2 ECU, Schlotterbeck OUT, faces Paraguay
    "Colombia": 1975,    # Looking strong/organized at 0-0 (21') vs Portugal in Miami
    "Morocco": 1920,     # Locked 2C vs Netherlands
    "Norway": 1910,      # Locked 2I vs Ivory Coast (full XI rested vs FRA)
    "Belgium": 1905,     # Locked 1G! Exploded 5-1 vs NZ (Trossard 2, De Bruyne masterclass, Lukaku)
    "Switzerland": 1900, # Locked 1B
    "Japan": 1900,       # Locked 2F vs Brazil
    "Mexico": 1885,      # Locked 1A (3-0-0, Azteca home advantage)
    "Croatia": 1880,     # Locked 2L! Beat Ghana 2-1 (Vlasic winner) even with Gvardiol benched
    "United States": 1865, # Locked 1D vs Bosnia, Pulisic back
    "Ecuador": 1865,     # Locked 3E (4 pts), beat Germany 2-1
    "Ivory Coast": 1845, # Locked 2E vs Norway
    "Senegal": 1840,     # Locked 3I (3 pts, +2 GD, 5-0 IRQ)
    "Austria": 1835,     # 3 pts vs Algeria tonight
    "Canada": 1835,      # Locked 2B vs South Africa (Kone broken leg)
    "Sweden": 1830,      # Locked 3F vs France, downgraded -20 because starting CB Isak Hien OUT for tournament
    "Ghana": 1820,       # Locked 3L (4 pts, lost 1-2 CRO), CONFIRMED vs 1K in Kansas City!
    "South Korea": 1815, # 3A (3 pts, -1 GD)
    "Egypt": 1810,       # Locked 2G (5 pts, 1-1 IRN), downgraded -15 for Salah injury assessment + Fatouh injury
    "Paraguay": 1810,    # Locked 3D vs Germany
    "Australia": 1800,   # Locked 2D vs Egypt, downgraded -15 for Italiano & Leckie OUT for tournament
    "Algeria": 1800,     # 3 pts vs Austria tonight
    "Bosnia and Herzegovina": 1790, # Locked 3B vs USA
    "Iran": 1785,        # 3G (3 pts, 0 GD, waiting on J/K)
    "South Africa": 1775,# Locked 2A vs Canada
    "DR Congo": 1770,    # 1 pt vs Uzbekistan tonight (win = 4 pts = qualified!)
    "Cape Verde": 1765,  # Locked 2H (3 draws, 0 wins) -> CONFIRMED vs Argentina!
    "Uzbekistan": 1715,  # 0 pts, -7 GD
    "Jordan": 1690,      # 0 pts
}

# Remaining unassigned 3rd-place slots (M74=3D, M77=3F, M81=3B, M87=3L are ALL LOCKED!)
REMAINING_THIRD_SLOTS = {
    "M79": ["E", "I"],               # C, H eliminated; F locked M77
    "M80": ["E", "I", "J", "K"],     # H eliminated
    "M82": ["A", "I", "J"],          # Reuters confirmed Belgium faces A, I, or J! (E also theoretically eligible if needed)
    "M85": ["E", "G", "I", "J"],     # F locked M77
}

def poisson(lam):
    if lam <= 0:
        return 0
    L = math.exp(-lam)
    k = 0
    p = 1.0
    while p > L:
        k += 1
        p *= random.random()
    return k - 1

def sim_match_score(ea, eb, avg_goals=2.60, frac_remaining=1.0):
    diff = ea - eb
    wa = 1.0 / (1.0 + 10.0 ** (-diff / 420.0))
    lam_a = avg_goals * frac_remaining * (0.15 + 0.70 * wa)
    lam_b = avg_goals * frac_remaining * (0.15 + 0.70 * (1.0 - wa))
    return poisson(lam_a), poisson(lam_b)

def sim_remaining_two_groups(ELO):
    # Completed groups A-I and L:
    g = {
        "A": ("Mexico", "South Africa", "South Korea", (3, -1, 3)),
        "B": ("Switzerland", "Canada", "Bosnia and Herzegovina", (4, 0, 4)),
        "C": ("Brazil", "Morocco", "Scotland", (3, -2, 3)),
        "D": ("United States", "Australia", "Paraguay", (4, 0, 3)),
        "E": ("Germany", "Ivory Coast", "Ecuador", (4, 0, 3)),
        "F": ("Netherlands", "Japan", "Sweden", (4, 0, 7)),
        "G": ("Belgium", "Egypt", "Iran", (3, 0, 3)),
        "H": ("Spain", "Cape Verde", "Uruguay", (2, -1, 3)),
        "I": ("France", "Norway", "Senegal", (3, 2, 8)),
        "L": ("England", "Croatia", "Ghana", (4, 0, 2)),
    }

    # GROUP J: Argentina locked 1J; Austria (3 pts, 0 GD, 2 GF) vs Algeria (3 pts, -1 GD, 2 GF)
    gaut, galg = sim_match_score(ELO["Austria"], ELO["Algeria"], 2.45)
    aut_pts = 3 + (3 if gaut > galg else (1 if gaut == galg else 0))
    alg_pts = 3 + (3 if galg > gaut else (1 if gaut == galg else 0))
    aut_gd = 0 + (gaut - galg)
    alg_gd = -1 + (galg - gaut)
    aut_gf = 2 + gaut
    alg_gf = 2 + galg
    if (aut_pts, aut_gd, aut_gf) >= (alg_pts, alg_gd, alg_gf):
        g["J"] = ("Argentina", "Austria", "Algeria", (alg_pts, alg_gd, alg_gf))
    else:
        g["J"] = ("Argentina", "Algeria", "Austria", (aut_pts, aut_gd, aut_gf))

    # GROUP K: Colombia (6 pts) vs Portugal (4 pts) CURRENTLY 0-0 at 21' (frac_remaining=0.77, Miami crowd +15 COL)
    gpor, gcol = sim_match_score(ELO["Portugal"], ELO["Colombia"] + 15, 2.35, frac_remaining=0.77)
    # DR Congo (1 pt, -1 GD, 1 GF) vs Uzbekistan (0 pts, -7 GD, 0 GF) — same kickoff, ~0.77 remaining
    gcod, guzb = sim_match_score(ELO["DR Congo"], ELO["Uzbekistan"], 2.30, frac_remaining=0.77)
    if gpor > gcol:
        k1, k2 = "Portugal", "Colombia"
    else:
        k1, k2 = "Colombia", "Portugal"
    cod_pts = 1 + (3 if gcod > guzb else (1 if gcod == guzb else 0))
    uzb_pts = 0 + (3 if guzb > gcod else (1 if gcod == guzb else 0))
    cod_gd = -1 + (gcod - guzb)
    uzb_gd = -7 + (guzb - gcod)
    if (cod_pts, cod_gd, 1 + gcod) >= (uzb_pts, uzb_gd, guzb):
        g["K"] = (k1, k2, "DR Congo", (cod_pts, cod_gd, 1 + gcod))
    else:
        g["K"] = (k1, k2, "Uzbekistan", (uzb_pts, uzb_gd, guzb))

    return g, (gpor, gcol)

def assign_remaining_thirds(g):
    # Locked 3rd place qualifiers: B (M81), D (M74), F (M77), L (M87), plus E and I guaranteed in top 8!
    # Choose top 2 from remaining candidates {A, G, J, K} (C and H already below A and G)
    cands = []
    for grp in ["A", "G", "J", "K"]:
        team3 = g[grp][2]
        pts, gd, gf = g[grp][3]
        cands.append((pts, gd, gf, random.random(), grp, team3))
    cands.sort(reverse=True)
    # Top 2 advance along with E and I into M79, M80, M82, M85
    adv4 = {"E": g["E"][2], "I": g["I"][2]}
    for _, _, _, _, grp, t3 in cands[:2]:
        adv4[grp] = t3

    assigned = {
        "M74": "Paraguay",
        "M77": "Sweden",
        "M81": "Bosnia and Herzegovina",
        "M87": "Ghana",
    }
    slots = ["M80", "M85", "M82", "M79"]
    # Try exact match with Reuters constraint M82 in [A, I, J]
    used = set()
    def bt(idx, allow_e_m82=False):
        if idx == len(slots):
            return True
        s = slots[idx]
        elig = list(REMAINING_THIRD_SLOTS[s])
        if allow_e_m82 and s == "M82":
            elig.append("E")
        opts = [grp for grp in elig if grp in adv4 and grp not in used]
        random.shuffle(opts)
        for grp in opts:
            assigned[s] = adv4[grp]
            used.add(grp)
            if bt(idx + 1, allow_e_m82):
                return True
            used.remove(grp)
        return False

    if not bt(0, False):
        used.clear()
        bt(0, True)
    return assigned, adv4

def run_sim(sigma=55, N=120000):
    counts = {k: Counter() for k in [
        "QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final",
        "Col_1K", "Eng_vs_DRC", "Iran_Qual", "SK_Qual"
    ]}

    # Golden Boot players: (name, team, curr_goals, curr_assists, ko_gpg, ko_apg, md3_type)
    GB_PLAYERS = [
        ("Lionel Messi", "Argentina", 5, 0, 0.72, 0.32, "messi_bench"), # Confirmed starting on bench vs Jordan
        ("Kylian Mbappé", "France", 4, 0, 0.86, 0.25, None),
        ("Ousmane Dembélé", "France", 4, 0, 0.48, 0.30, None),
        ("Vinícius Júnior", "Brazil", 4, 1, 0.56, 0.28, None),
        ("Erling Haaland", "Norway", 4, 0, 0.85, 0.12, None),
        ("Harry Kane", "England", 3, 0, 0.65, 0.18, None),            # Scored 1 vs Panama -> 3 goals, group stage DONE
        ("Deniz Undav", "Germany", 3, 2, 0.44, 0.18, None),
        ("Brian Brobbey", "Netherlands", 3, 0, 0.45, 0.12, None),
        ("Matheus Cunha", "Brazil", 3, 0, 0.42, 0.15, None),
        ("Jonathan David", "Canada", 3, 0, 0.44, 0.15, None),
        ("Ismael Saibari", "Morocco", 3, 0, 0.38, 0.15, None),
        ("Johan Manzambi", "Switzerland", 3, 0, 0.36, 0.12, None),
        ("Cristiano Ronaldo", "Portugal", 2, 0, 0.52, 0.10, "ronaldo_live"), # 0-0 at 21' vs Colombia
        ("Mikel Oyarzabal", "Spain", 2, 1, 0.46, 0.22, None),         # Blanked vs Uruguay -> 2 goals, group stage DONE
        ("Cody Gakpo", "Netherlands", 2, 1, 0.42, 0.22, None),
        ("Leandro Trossard", "Belgium", 2, 1, 0.40, 0.20, None),
        ("Lamine Yamal", "Spain", 1, 1, 0.36, 0.38, None),
        ("Jude Bellingham", "England", 2, 1, 0.35, 0.22, None),
        ("Field", "NONE", 0, 0, 0, 0, None),
    ]
    gb_wins = Counter()
    ko_games_sum = Counter()

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in BASE_ELO.items()}
        def play_ko(a, b, venue=None):
            ba = 45 if (venue == "Azteca" and a == "Mexico") else (30 if (venue == "USA" and a == "United States") else 0)
            bb = 45 if (venue == "Azteca" and b == "Mexico") else (30 if (venue == "USA" and b == "United States") else 0)
            p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / 440.0))
            return (a, b) if random.random() < p else (b, a)

        g, (gpor, gcol) = sim_remaining_two_groups(ELO)
        th, adv4 = assign_remaining_thirds(g)
        if g["K"][0] == "Colombia": counts["Col_1K"]["Yes"] += 1
        if th["M80"] == "DR Congo": counts["Eng_vs_DRC"]["Yes"] += 1
        if "G" in adv4: counts["Iran_Qual"]["Yes"] += 1
        if "A" in adv4: counts["SK_Qual"]["Yes"] += 1

        ko_games = Counter()
        r32_opp = {}
        r32_pairs = [
            ("M73", g["A"][1], g["B"][1], None),
            ("M74", g["E"][0], th["M74"], None),
            ("M75", g["F"][0], g["C"][1], None),
            ("M76", g["C"][0], g["F"][1], None),
            ("M77", g["I"][0], th["M77"], None),
            ("M78", g["E"][1], g["I"][1], None),
            ("M79", g["A"][0], th["M79"], "Azteca"),
            ("M80", g["L"][0], th["M80"], None),
            ("M81", g["D"][0], th["M81"], "USA"),
            ("M82", g["G"][0], th["M82"], None),
            ("M83", g["K"][1], g["L"][1], None),
            ("M84", g["H"][0], g["J"][1], None),
            ("M85", g["B"][0], th["M85"], None),
            ("M86", g["J"][0], g["H"][1], None),
            ("M87", g["K"][0], th["M87"], None),
            ("M88", g["D"][1], g["G"][1], None),
        ]
        w = {}
        for mid, a, b, v in r32_pairs:
            ko_games[a] += 1; ko_games[b] += 1
            r32_opp[a] = b; r32_opp[b] = a
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

        # Golden Boot draw (incorporating soft R32 opponent bonus for Argentina vs Cape Verde, England vs DRC, etc.)
        best_key = (-1, -1, -1.0)
        best_name = None
        for name, team, cg, ca, gpg, apg, md3 in GB_PLAYERS:
            if team == "NONE":
                fg = 2 + poisson(3.3)
                key = (fg, poisson(1.4), random.random())
                if key > best_key:
                    best_key = key; best_name = "Field"
                continue
            goals = cg
            assists = ca
            if md3 == "messi_bench":
                # Confirmed starting on bench vs eliminated Jordan; Scaloni says he'll come on later (~25-30 mins)
                goals += poisson(0.28)
                assists += poisson(0.14)
            elif md3 == "ronaldo_live":
                goals += poisson(0.38 * gpor)
                assists += poisson(0.08)
            ng = ko_games[team]
            if ng > 0:
                mult = max(0.4, random.gauss(1.0, 0.20))
                # Opponent strength adjustment for R32 (game 1 of KO):
                opp = r32_opp.get(team)
                opp_elo = BASE_ELO.get(opp, 1850)
                # Softer R32 opp (like Cape Verde 1765 or DR Congo 1770) adds expected goals in R32
                r32_boost = max(0.75, min(1.45, 1.0 + (1870 - opp_elo) / 300.0))
                exp_g = gpg * mult * (r32_boost + max(0, ng - 1) * 0.96)
                goals += poisson(exp_g)
                assists += poisson(ng * apg)
            key = (goals, assists, random.random())
            if key > best_key:
                best_key = key; best_name = name
        gb_wins[best_name] += 1

    print(f"=== SIGMA={sigma} ===")
    print(f"Diag: Col_1K={counts['Col_1K']['Yes']/N:.3f}, Eng_vs_DRC={counts['Eng_vs_DRC']['Yes']/N:.3f}, Iran_Qual={counts['Iran_Qual']['Yes']/N:.3f}, SK_Qual={counts['SK_Qual']['Yes']/N:.3f}")
    print("Exp KO games:", {t: round(ko_games_sum[t]/N, 2) for t in ["Argentina", "France", "Spain", "England", "Brazil", "Netherlands", "Germany", "Portugal", "Colombia", "Norway"]})
    for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final"]:
        print(f"\n--- {key} ---")
        top = counts[key].most_common(7)
        for t, cnt in top:
            print(f"  {t:22s}: {cnt/N:.4f}")
        print(f"  Top5 sum = {sum(cnt for _, cnt in top[:5])/N:.4f}")
    print("\n--- GOLDEN BOOT ---")
    for name, cnt in gb_wins.most_common(10):
        print(f"  {name:22s}: {cnt/N:.4f}")

run_sim(sigma=55, N=120000)
