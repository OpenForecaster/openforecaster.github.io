import random, math
from collections import Counter

random.seed(20260626)

# Updated Elo ratings as of 2026-06-26 after Groups A-F and I completed
BASE_ELO = {
    "France": 2140,      # 9 pts, 10 GF, 4-1 NOR (Dembele hat-trick), locked 1I
    "Spain": 2125,       # 33 unbeaten, 0 GA, Yamal & Pedri starting vs URU
    "Argentina": 2110,   # Defending champs, locked 1J, Messi 5g, Romero recovering
    "England": 2040,     # 4 pts, James hamstring doubt vs Panama
    "Brazil": 2030,      # Locked 1C, 3-0 SCO, +6 GD, 1 GA, Vinicius 4g, Neymar back
    "Netherlands": 2020, # Locked 1F, 7 pts, 10 GF, 19 WC group games unbeaten
    "Portugal": 2015,    # 4 pts, +5 GD, facing Colombia
    "Germany": 1995,     # Locked 1E, lost 1-2 ECU, Schlotterbeck OUT for tournament, conceded every game
    "Colombia": 1965,    # 6 pts, essentially home crowd in Miami vs Portugal
    "Morocco": 1920,     # Locked 2C vs Netherlands
    "Norway": 1910,      # Locked 2I vs Ivory Coast, full XI rested vs France
    "Switzerland": 1900, # Locked 1B
    "Japan": 1900,       # Locked 2F vs Brazil
    "Mexico": 1885,      # Locked 1A, 3-0-0, Azteca home advantage
    "Uruguay": 1880,     # 2 pts, defensive errors, Araujo/De Arrascaeta out
    "Croatia": 1875,     # 3 pts, faces Ghana
    "United States": 1865, # Locked 1D vs Bosnia, Pulisic back
    "Ecuador": 1865,     # Locked 3E (4 pts), beat Germany 2-1, 1 loss in 22
    "Belgium": 1860,     # 2 pts, Doku/Lukaku not 90-min fit
    "Sweden": 1850,      # Locked 3F (4 pts), qualified
    "Ivory Coast": 1845, # Locked 2E vs Norway
    "Senegal": 1840,     # Locked 3I (3 pts, +2 GD, 5-0 vs Iraq)
    "Austria": 1835,     # 3 pts
    "Canada": 1835,      # Locked 2B vs South Africa (Kone broken leg)
    "Egypt": 1825,       # 4 pts in Group G
    "Ghana": 1825,       # 4 pts in Group L, clean sheets
    "South Korea": 1815, # 3A (3 pts, -1 GD)
    "Australia": 1815,   # Locked 2D vs 2G
    "Paraguay": 1810,    # Locked 3D (4 pts)
    "Scotland": 1805,    # Locked 3C (3 pts, -2 GD)
    "Algeria": 1800,     # 3 pts
    "Bosnia and Herzegovina": 1790, # Locked 3B -> M81 vs USA!
    "Iran": 1785,        # 2 pts
    "South Africa": 1775,# Locked 2A vs Canada
    "DR Congo": 1770,    # 1 pt
    "Cape Verde": 1765,  # 2 pts
    "Saudi Arabia": 1745,# 1 pt
    "New Zealand": 1720, # 1 pt
    "Uzbekistan": 1715,  # 0 pts
    "Jordan": 1690,      # 0 pts
    "Panama": 1690,      # 0 pts
}

# Exact FIFA 2026 third-place eligible groups per match
# Note: M81 (1D USA) is ALREADY confirmed vs 3B (Bosnia and Herzegovina)!
THIRD_SLOTS = {
    "M74": ["A", "B", "C", "D", "F"],
    "M77": ["C", "D", "F", "G", "H"],
    "M79": ["C", "E", "F", "H", "I"],
    "M80": ["E", "H", "I", "J", "K"],
    "M82": ["A", "E", "H", "I", "J"],
    "M85": ["E", "F", "G", "I", "J"],
    "M87": ["D", "E", "I", "J", "L"],
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

def sim_match_score(ea, eb, avg_goals=2.65):
    # Expected win share via Elo
    diff = ea - eb
    wa = 1.0 / (1.0 + 10.0 ** (-diff / 420.0))
    # Split total goals proportionally with mild compression
    lam_a = avg_goals * (0.15 + 0.70 * wa)
    lam_b = avg_goals * (0.15 + 0.70 * (1.0 - wa))
    return poisson(lam_a), poisson(lam_b)

def rank_group_4(teams_stats, h2h):
    # teams_stats: dict team -> [pts, gd, gf]
    # Simplified FIFA tiebreak: pts -> h2h pts -> h2h gd -> overall gd -> overall gf -> random
    by_pts = {}
    for t, (pts, gd, gf) in teams_stats.items():
        by_pts.setdefault(pts, []).append(t)
    ranked = []
    for pts in sorted(by_pts.keys(), reverse=True):
        grp = by_pts[pts]
        if len(grp) == 1:
            ranked.extend(grp)
        else:
            def key_fn(t):
                h_pts = 0
                h_gd = 0
                h_gf = 0
                for opp in grp:
                    if opp == t: continue
                    if (t, opp) in h2h:
                        ga, gb = h2h[(t, opp)]
                        h_gf += ga
                        h_gd += (ga - gb)
                        h_pts += 3 if ga > gb else (1 if ga == gb else 0)
                return (h_pts, h_gd, h_gf, teams_stats[t][1], teams_stats[t][2], random.random())
            grp.sort(key=key_fn, reverse=True)
            ranked.extend(grp)
    return ranked

def sim_remaining_groups(ELO):
    # Returns dict grp -> (1st, 2nd, 3rd, (pts3, gd3, gf3))
    g = {}
    # COMPLETED GROUPS:
    g["A"] = ("Mexico", "South Africa", "South Korea", (3, -1, 3))
    g["B"] = ("Switzerland", "Canada", "Bosnia and Herzegovina", (4, 0, 4)) # 3B locked into M81
    g["C"] = ("Brazil", "Morocco", "Scotland", (3, -2, 3)) # lost 0-3 to BRA, beat HAI, lost to MAR
    g["D"] = ("United States", "Australia", "Paraguay", (4, 0, 3))
    g["E"] = ("Germany", "Ivory Coast", "Ecuador", (4, 0, 3))
    g["F"] = ("Netherlands", "Japan", "Sweden", (4, -1, 7)) # 5-1 TUN, 1-5 NED, 1-1 JPN -> 4 pts, +0 GD! Wait: 5-1=+4, 1-5=-4, 1-1=0 -> GD=0, GF=7!
    g["F"] = ("Netherlands", "Japan", "Sweden", (4, 0, 7))
    g["I"] = ("France", "Norway", "Senegal", (3, 2, 8)) # 1-3 FRA, 2-3 NOR, 5-0 IRQ -> 8 GF, 6 GA, +2 GD!

    # GROUP G: Egypt 4 (+2, 4 GF), Iran 2 (0, 2 GF), Belgium 2 (0, 1 GF), NZ 1 (-2, 2 GF)
    # Earlier matches: BEL 1-1 EGY, IRN 1-1 NZ?, EGY 3-1 NZ, BEL 0-0 IRN -> check: EGY 1-1 BEL, 3-1 NZ -> 4 pts, +2 GD, 4 GF;
    # BEL 1-1 EGY, 0-0 IRN -> 2 pts, 0 GD, 1 GF; IRN 2-2 NZ? (more GF than BEL), 0-0 BEL -> 2 pts, 0 GD, 2 GF; NZ 1-3 EGY, 2-2 IRN -> 1 pt, -2 GD, 3 GF
    sG = {"Egypt": [4, 2, 4], "Iran": [2, 0, 2], "Belgium": [2, 0, 1], "New Zealand": [1, -2, 3]}
    hG = {("Belgium","Egypt"):(1,1), ("Egypt","Belgium"):(1,1),
          ("Egypt","New Zealand"):(3,1), ("New Zealand","Egypt"):(1,3),
          ("Belgium","Iran"):(0,0), ("Iran","Belgium"):(0,0),
          ("Iran","New Zealand"):(2,2), ("New Zealand","Iran"):(2,2)}
    ge, gi = sim_match_score(ELO["Egypt"], ELO["Iran"], 2.3)
    gb, gn = sim_match_score(ELO["Belgium"], ELO["New Zealand"], 2.7)
    for (a, b, ga, gb_) in [("Egypt","Iran",ge,gi), ("Belgium","New Zealand",gb,gn)]:
        hG[(a,b)]=(ga,gb_); hG[(b,a)]=(gb_,ga)
        sG[a][1]+=ga-gb_; sG[a][2]+=ga; sG[a][0]+=3 if ga>gb_ else (1 if ga==gb_ else 0)
        sG[b][1]+=gb_-ga; sG[b][2]+=gb_; sG[b][0]+=3 if gb_>ga else (1 if ga==gb_ else 0)
    rG = rank_group_4(sG, hG)
    g["G"] = (rG[0], rG[1], rG[2], tuple(sG[rG[2]]))

    # GROUP H: Spain 4 (+4, 4 GF), Uruguay 2 (0, 3 GF), Cape Verde 2 (0, 2 GF), Saudi Arabia 1 (-4, 1 GF)
    # Matches: ESP 0-0 CPV, URU 1-1 KSA, ESP 4-0 KSA, URU 2-2 CPV
    sH = {"Spain": [4, 4, 4], "Uruguay": [2, 0, 3], "Cape Verde": [2, 0, 2], "Saudi Arabia": [1, -4, 1]}
    hH = {("Spain","Cape Verde"):(0,0), ("Cape Verde","Spain"):(0,0),
          ("Uruguay","Saudi Arabia"):(1,1), ("Saudi Arabia","Uruguay"):(1,1),
          ("Spain","Saudi Arabia"):(4,0), ("Saudi Arabia","Spain"):(0,4),
          ("Uruguay","Cape Verde"):(2,2), ("Cape Verde","Uruguay"):(2,2)}
    # Calibrate Spain vs Uruguay directly to Opta: 62.2% ESP, 22.1% Draw, 15.8% URU
    r = random.random()
    if r < 0.622:
        # Spain win
        gsp, guru = random.choice([(1,0),(2,0),(2,1),(3,1),(2,0),(3,0)])
    elif r < 0.843:
        gsp = guru = random.choice([0,1,1,2])
    else:
        guru, gsp = random.choice([(1,0),(2,1),(2,1),(2,0)])
    gcpv, gksa = sim_match_score(ELO["Cape Verde"], ELO["Saudi Arabia"], 2.4)
    for (a, b, ga, gb_) in [("Spain","Uruguay",gsp,guru), ("Cape Verde","Saudi Arabia",gcpv,gksa)]:
        hH[(a,b)]=(ga,gb_); hH[(b,a)]=(gb_,ga)
        sH[a][1]+=ga-gb_; sH[a][2]+=ga; sH[a][0]+=3 if ga>gb_ else (1 if ga==gb_ else 0)
        sH[b][1]+=gb_-ga; sH[b][2]+=gb_; sH[b][0]+=3 if gb_>ga else (1 if ga==gb_ else 0)
    rH = rank_group_4(sH, hH)
    g["H"] = (rH[0], rH[1], rH[2], tuple(sH[rH[2]]))

    # GROUP J: Argentina 6 (LOCKED 1J!), Austria 3 (0 GD), Algeria 3 (-1 GD), Jordan 0
    # Matches: ARG 3-0 ALG, AUT beat JOR (~2-0), ARG 2-0 AUT, ALG beat JOR (~2-0)
    sJ = {"Argentina": [6, 5, 5], "Austria": [3, 0, 2], "Algeria": [3, -1, 2], "Jordan": [0, -4, 0]}
    hJ = {("Argentina","Algeria"):(3,0), ("Algeria","Argentina"):(0,3),
          ("Argentina","Austria"):(2,0), ("Austria","Argentina"):(0,2),
          ("Austria","Jordan"):(2,0), ("Jordan","Austria"):(0,2),
          ("Algeria","Jordan"):(2,0), ("Jordan","Algeria"):(0,2)}
    gaut, galg = sim_match_score(ELO["Austria"], ELO["Algeria"], 2.5)
    hJ[("Austria","Algeria")]=(gaut,galg); hJ[("Algeria","Austria")]=(galg,gaut)
    sJ["Austria"][1]+=gaut-galg; sJ["Austria"][2]+=gaut; sJ["Austria"][0]+=3 if gaut>galg else (1 if gaut==galg else 0)
    sJ["Algeria"][1]+=galg-gaut; sJ["Algeria"][2]+=galg; sJ["Algeria"][0]+=3 if galg>gaut else (1 if gaut==galg else 0)
    # Argentina locked 1J
    rJ_rest = rank_group_4({k:v for k,v in sJ.items() if k != "Argentina"}, hJ)
    g["J"] = ("Argentina", rJ_rest[0], rJ_rest[1], tuple(sJ[rJ_rest[1]]))

    # GROUP K: Colombia 6 (+3 GD, 3 GF), Portugal 4 (+5 GD, 6 GF), DR Congo 1 (-1 GD, 1 GF), Uzbekistan 0 (-7 GD, 0 GF)
    sK = {"Colombia": [6, 3, 3], "Portugal": [4, 5, 6], "DR Congo": [1, -1, 1], "Uzbekistan": [0, -7, 0]}
    hK = {("Portugal","DR Congo"):(1,1), ("DR Congo","Portugal"):(1,1),
          ("Portugal","Uzbekistan"):(5,0), ("Uzbekistan","Portugal"):(0,5),
          ("Colombia","DR Congo"):(1,0), ("DR Congo","Colombia"):(0,1),
          ("Colombia","Uzbekistan"):(2,0), ("Uzbekistan","Colombia"):(0,2)}
    # Portugal vs Colombia in Miami (pro-Colombia crowd ~+15 Elo for COL)
    gpor, gcol = sim_match_score(ELO["Portugal"], ELO["Colombia"] + 15, 2.5)
    gcod, guzb = sim_match_score(ELO["DR Congo"], ELO["Uzbekistan"], 2.3)
    for (a, b, ga, gb_) in [("Portugal","Colombia",gpor,gcol), ("DR Congo","Uzbekistan",gcod,guzb)]:
        hK[(a,b)]=(ga,gb_); hK[(b,a)]=(gb_,ga)
        sK[a][1]+=ga-gb_; sK[a][2]+=ga; sK[a][0]+=3 if ga>gb_ else (1 if ga==gb_ else 0)
        sK[b][1]+=gb_-ga; sK[b][2]+=gb_; sK[b][0]+=3 if gb_>ga else (1 if ga==gb_ else 0)
    rK = rank_group_4(sK, hK)
    g["K"] = (rK[0], rK[1], rK[2], tuple(sK[rK[2]]))

    # GROUP L: England 4 (+2, 4 GF), Ghana 4 (+1, 1 GF), Croatia 3 (0, 4 GF), Panama 0 (-3, 0 GF)
    # Matches: ENG 4-2 CRO, GHA 1-0 PAN, ENG 0-0 GHA, CRO 2-0 PAN
    sL = {"England": [4, 2, 4], "Ghana": [4, 1, 1], "Croatia": [3, 0, 4], "Panama": [0, -3, 0]}
    hL = {("England","Croatia"):(4,2), ("Croatia","England"):(2,4),
          ("Ghana","Panama"):(1,0), ("Panama","Ghana"):(0,1),
          ("England","Ghana"):(0,0), ("Ghana","England"):(0,0),
          ("Croatia","Panama"):(2,0), ("Panama","Croatia"):(0,2)}
    geng, gpan = sim_match_score(ELO["England"], ELO["Panama"], 2.8)
    gcro, ggha = sim_match_score(ELO["Croatia"], ELO["Ghana"], 2.4)
    for (a, b, ga, gb_) in [("England","Panama",geng,gpan), ("Croatia","Ghana",gcro,ggha)]:
        hL[(a,b)]=(ga,gb_); hL[(b,a)]=(gb_,ga)
        sL[a][1]+=ga-gb_; sL[a][2]+=ga; sL[a][0]+=3 if ga>gb_ else (1 if ga==gb_ else 0)
        sL[b][1]+=gb_-ga; sL[b][2]+=gb_; sL[b][0]+=3 if gb_>ga else (1 if ga==gb_ else 0)
    rL = rank_group_4(sL, hL)
    g["L"] = (rL[0], rL[1], rL[2], tuple(sL[rL[2]]))

    return g, (gsp, guru, geng, gpor)

def assign_thirds(g):
    # Bosnia (3B) is ALREADY locked into M81 vs USA!
    # Rank remaining 11 third-place teams by (pts, gd, gf, random), take top 7 + B = 8 total
    others = []
    for grp, (_, _, team3, stats3) in g.items():
        if grp == "B": continue
        others.append((stats3[0], stats3[1], stats3[2], random.random(), grp, team3))
    others.sort(reverse=True)
    adv = {grp: team3 for _, _, _, _, grp, team3 in others[:7]}
    # Assign 7 remaining slots M74, M77, M79, M80, M82, M85, M87
    slots = list(THIRD_SLOTS.keys())
    random.shuffle(slots)
    assigned = {"M81": "Bosnia and Herzegovina"}
    used = set()
    def bt(idx):
        if idx == len(slots): return True
        s = slots[idx]
        cands = [grp for grp in THIRD_SLOTS[s] if grp in adv and grp not in used]
        random.shuffle(cands)
        for grp in cands:
            assigned[s] = adv[grp]
            used.add(grp)
            if bt(idx + 1): return True
            used.remove(grp)
        return False
    if not bt(0):
        # Fallback if random order hits rare edge case
        for s in slots:
            if s not in assigned:
                for grp, t3 in adv.items():
                    if grp not in used:
                        assigned[s] = t3; used.add(grp); break
    return assigned, adv

N = 100000
counts = {k: Counter() for k in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final", "Senegal_Qual", "Spain_1H", "Spain_2H", "Spain_3H", "Portugal_1K", "England_1L"]}

# Golden Boot simulation players: (name, team, curr_goals, curr_assists, ko_gpg, ko_apg, md3_left)
GB_PLAYERS = [
    ("Lionel Messi", "Argentina", 5, 1, 0.72, 0.35, True),      # May rest vs Jordan (~35% plays full/part)
    ("Kylian Mbappé", "France", 4, 1, 0.88, 0.25, False),       # France penalties, 4g + 1a in 3 games
    ("Ousmane Dembélé", "France", 4, 0, 0.52, 0.30, False),     # 4g in 3 games (hat-trick vs 2nd-string NOR), lower historical gpg than Mbappe
    ("Vinícius Júnior", "Brazil", 4, 1, 0.56, 0.28, False),     # 4g in 3 games, Brazil talisman
    ("Erling Haaland", "Norway", 4, 0, 0.85, 0.12, False),      # 4g in 2 games, rested vs FRA
    ("Harry Kane", "England", 2, 1, 0.68, 0.20, True),          # Plays eliminated Panama Saturday!
    ("Mikel Oyarzabal", "Spain", 2, 1, 0.50, 0.22, True),       # Plays Uruguay tonight!
    ("Deniz Undav", "Germany", 3, 0, 0.45, 0.15, False),        # 3g in 3 games
    ("Brian Brobbey", "Netherlands", 3, 0, 0.45, 0.12, False),  # 3g in 3 games
    ("Jonathan David", "Canada", 3, 0, 0.45, 0.15, False),      # 3g in 3 games
    ("Cristiano Ronaldo", "Portugal", 2, 0, 0.55, 0.10, True),  # Plays Colombia Saturday
    ("Lamine Yamal", "Spain", 1, 1, 0.38, 0.40, True),          # Plays Uruguay tonight
    ("Michael Olise", "France", 1, 2, 0.30, 0.45, False),
    ("Cody Gakpo", "Netherlands", 2, 1, 0.42, 0.22, False),
    ("Field", "NONE", 0, 0, 0, 0, False),
]
gb_wins = Counter()

for _ in range(N):
    # Epistemic uncertainty sigma=55 Elo
    ELO = {t: r + random.gauss(0, 55) for t, r in BASE_ELO.items()}
    def play_ko(a, b, venue=None):
        ba = 45 if (venue == "Azteca" and a == "Mexico") else (30 if (venue == "USA" and a == "United States") else 0)
        bb = 45 if (venue == "Azteca" and b == "Mexico") else (30 if (venue == "USA" and b == "United States") else 0)
        p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / 440.0))
        return (a, b) if random.random() < p else (b, a)

    g, (gsp, guru, geng, gpor) = sim_remaining_groups(ELO)
    th, adv = assign_thirds(g)
    if "I" in adv: counts["Senegal_Qual"]["Yes"] += 1
    if g["H"][0] == "Spain": counts["Spain_1H"]["Yes"] += 1
    elif g["H"][1] == "Spain": counts["Spain_2H"]["Yes"] += 1
    elif g["H"][2] == "Spain": counts["Spain_3H"]["Yes"] += 1
    if g["K"][0] == "Portugal": counts["Portugal_1K"]["Yes"] += 1
    if g["L"][0] == "England": counts["England_1L"]["Yes"] += 1

    # Track knockout games played per team (including 3rd-place playoff / final = up to 5 KO games!)
    ko_games = Counter()
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
        ("M97", w["M89"], w["M90"], None),     # Boston QF
        ("M98", w["M93"], w["M94"], "USA"),    # LA QF
        ("M99", w["M91"], w["M92"], None),     # Miami QF
        ("M100", w["M95"], w["M96"], None),    # Kansas City QF
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

    # 3rd place & Final
    ko_games[l101] += 1; ko_games[l102] += 1
    w103, _ = play_ko(l101, l102)
    ko_games[w101] += 1; ko_games[w102] += 1
    w104, _ = play_ko(w101, w102)

    counts["ThirdPlace"][w103] += 1
    counts["Champion"][w104] += 1

    # Golden Boot draw
    best_key = (-1, -1, -1.0)
    best_name = None
    for name, team, cg, ca, gpg, apg, md3 in GB_PLAYERS:
        if team == "NONE":
            # Random dark horse from the wider field (e.g. Alvarez, Lautaro, Musiala, Wirtz, Saka, Diaz, Salah, etc.)
            fg = 2 + poisson(3.5)
            key = (fg, poisson(1.5), random.random())
            if key > best_key:
                best_key = key; best_name = "Field"
            continue
        goals = cg
        assists = ca
        if md3:
            if name == "Lionel Messi":
                # Scaloni signaled Messi may rest vs Jordan (~65% rested/brief cameo -> 0.25 exp goals; ~35% starts -> 1.15 exp goals)
                if random.random() < 0.35:
                    goals += poisson(1.15); assists += poisson(0.45)
                else:
                    goals += poisson(0.18); assists += poisson(0.10)
            elif name == "Harry Kane":
                # England vs eliminated Panama: Kane starts ~85% (England still needs win to guarantee 1L!)
                goals += poisson(0.42 * max(geng, 1.5))
                assists += poisson(0.20)
            elif name == "Mikel Oyarzabal":
                goals += poisson(0.38 * gsp)
                assists += poisson(0.20)
            elif name == "Lamine Yamal":
                goals += poisson(0.28 * gsp)
                assists += poisson(0.35 * max(gsp, 0.5))
            elif name == "Cristiano Ronaldo":
                goals += poisson(0.40 * gpor)
                assists += poisson(0.10)
        # Knockout games
        ng = ko_games[team]
        if ng > 0:
            # Slight form variance per tournament
            mult = max(0.4, random.gauss(1.0, 0.20))
            goals += poisson(ng * gpg * mult)
            assists += poisson(ng * apg)
        key = (goals, assists, random.random())
        if key > best_key:
            best_key = key; best_name = name
    gb_wins[best_name] += 1

print(f"Diagnostics: Senegal_Qual={counts['Senegal_Qual']['Yes']/N:.3f}, Spain_1H={counts['Spain_1H']['Yes']/N:.3f}, Spain_2H={counts['Spain_2H']['Yes']/N:.3f}, Spain_3H={counts['Spain_3H']['Yes']/N:.3f}, Port_1K={counts['Portugal_1K']['Yes']/N:.3f}, Eng_1L={counts['England_1L']['Yes']/N:.3f}")
for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final"]:
    print(f"\n=== {key} ===")
    top = counts[key].most_common(8)
    for t, cnt in top:
        print(f"  {t:22s}: {cnt/N:.4f}")
    print(f"  Top5 sum = {sum(cnt for _, cnt in top[:5])/N:.4f}")

print("\n=== GOLDEN BOOT SIM ===")
for name, cnt in gb_wins.most_common(12):
    print(f"  {name:22s}: {cnt/N:.4f}")
