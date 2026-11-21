import random
import math
from collections import Counter, defaultdict

random.seed(20260624)

# Calibrated World Cup 2026 Elo-style strength ratings (reflecting FIFA/Elo + 2026 MD1-2 form + injuries + host advantage)
# Scale: 400 Elo diff => 90.9% win prob in knockout (1 / (1 + 10^(-d/400)))
# Note: in football knockouts (90m + ET + pens), variance is slightly higher than Elo/400 (closer to Elo/450 because penalties compress favorites!)
ELO = {
    # Tier 1: Elite title favorites
    "Spain": 2115,       # 33 unbeaten, Euro 2024 champs, Yamal back, crushed KSA 4-0
    "France": 2110,      # DraftKings +400 #1 fav, Mbappe firing, 2-0-0 (3-1 SEN, 3-0 IRQ)
    "Argentina": 2095,   # Defending champs, 2-0-0 (3-0 ALG, 2-0 AUT), Messi 5 goals
    # Tier 2: Major contenders
    "England": 2025,     # Beat CRO 4-2, drew GHA 0-0, Rice/James knocks
    "Germany": 2020,     # Locked 1E, 7-1 CUW, 2-1 CIV, strong resurgence
    "Netherlands": 2005, # 2-2 JPN, 5-1 SWE, very sharp
    "Portugal": 2000,    # 1-1 COD, 5-0 UZB, Ronaldo/Bruno/Vitinha
    "Brazil": 1980,      # 1-1 MAR, 3-0 HAI, Raphinha injured, Opta #8 overall
    # Tier 3: Dangerous dark horses / strong QF contenders
    "Colombia": 1955,    # 2-0-0 (3-1 UZB, 1-0 COD), Copa finalists
    "Japan": 1925,       # 2-2 NED, 4-0 TUN, Opta 20.8% QF / 9.41% SF
    "Morocco": 1925,     # 1-1 BRA, beat SCO, elite defense/midfield
    "Norway": 1920,      # 2-0-0 (4-1 IRQ, 3-2 SEN), Haaland + Odegaard
    "Uruguay": 1905,     # 1-1 KSA, 2-2 CPV, Bielsa defense leaky
    "Switzerland": 1900, # Locked 1B (7 pts), beat CAN 2-1
    "Belgium": 1885,     # Sluggish 2 draws (EGY, IRN)
    "Croatia": 1875,     # Lost 2-4 ENG, scraped 1-0 PAN
    "Mexico": 1870,      # Locked 1A + Azteca home advantage (+50 applied in MEX matches)
    "United States": 1870,# Locked 1D, 4-1 PAR, 2-0 AUS + home soil (+35)
    "Sweden": 1850,      # 5-1 TUN, 1-5 NED, high variance
    "Ecuador": 1845,
    "Canada": 1835,      # Locked 2B (4 pts, +5 GD)
    "Austria": 1835,     # 3-1 JOR, 0-2 ARG
    "Ivory Coast": 1830, # Lost 1-2 GER
    "South Korea": 1825,
    "Egypt": 1825,       # 4 pts, 3-1 NZL, drew BEL
    "Ghana": 1820,       # 4 pts, 0-0 ENG
    "Senegal": 1820,
    "Czechia": 1815,
    "Australia": 1810,   # Beat TUR 2-0, lost USA 0-2
    "Paraguay": 1805,    # Lost USA 1-4, beat TUR 1-0
    "Scotland": 1800,    # Beat HAI 1-0, lost MAR; Brazil 68.1% / Draw 19% / SCO 12.9% -> ~180 Elo gap matches!
    "Algeria": 1795,
    "Bosnia and Herzegovina": 1790, # Locked 3B (4 pts)
    "Iran": 1785,        # 2 draws vs BEL/NZL
    "Cape Verde": 1765,  # 0-0 ESP, 2-2 URU!
    "South Africa": 1755,
    "Saudi Arabia": 1745,
    "DR Congo": 1765,    # 1-1 POR, 0-1 COL
    "New Zealand": 1720,
    "Curacao": 1680,
    "Iraq": 1700,
    "Uzbekistan": 1720,
}

def ko_prob(a, b, venue_bonus_a=0, venue_bonus_b=0):
    diff = (ELO[a] + venue_bonus_a) - (ELO[b] + venue_bonus_b)
    # Use 440 divisor to account for knockout draw -> extra time -> penalty shootout variance
    return 1.0 / (1.0 + 10.0 ** (-diff / 440.0))

def play_ko(a, b, venue=None):
    ba = 45 if (venue == "Azteca" and a == "Mexico") else (30 if (venue == "USA" and a == "United States") else 0)
    bb = 45 if (venue == "Azteca" and b == "Mexico") else (30 if (venue == "USA" and b == "United States") else 0)
    p = ko_prob(a, b, ba, bb)
    return (a, b) if random.random() < p else (b, a)

def sample_dist(items):
    r = random.random()
    c = 0.0
    for val, prob in items:
        c += prob
        if r <= c:
            return val
    return items[-1][0]

# Sample Group Stage Outcomes (1st, 2nd, 3rd_team, 3rd_qualifies_prob_weight)
# Based on exact June 24, 2026 standings and final round fixtures!
def sample_groups():
    g = {}
    # Group A: Mexico 1A LOCKED (6 pts). South Korea vs South Africa, Mexico vs Czechia.
    # Korea needs win/draw for 2A (~70%), Czechia (~18%), South Africa (~12%)
    a2, a3 = sample_dist([
        (("South Korea", "Czechia"), 0.50),
        (("South Korea", "South Africa"), 0.22),
        (("Czechia", "South Korea"), 0.16),
        (("South Africa", "South Korea"), 0.12),
    ])
    g["A"] = ("Mexico", a2, a3, 0.55)

    # Group B: FINALIZED TODAY (June 24)! 1B Switzerland, 2B Canada, 3B Bosnia (4 pts, qualified!)
    g["B"] = ("Switzerland", "Canada", "Bosnia and Herzegovina", 0.99)

    # Group C: Brazil (4, +3) vs Scotland (3, 0); Morocco (4, +1) vs Haiti (0, -4).
    # Opta: Brazil beat SCO 68.1%, draw 19%, SCO win 12.9%. Morocco heavy fav (~80%) vs Haiti, could win by 3+ to pass Brazil GD if Brazil wins by 1 or draws!
    c1, c2, c3, c3q = sample_dist([
        (("Brazil", "Morocco", "Scotland", 0.55), 0.54),   # Brazil wins & holds GD (or Morocco fails to overtake)
        (("Morocco", "Brazil", "Scotland", 0.55), 0.28),   # Morocco overtakes Brazil on GD or Brazil draws Scotland
        (("Morocco", "Scotland", "Brazil", 0.90), 0.08),   # Scotland beats Brazil & Morocco beats Haiti
        (("Brazil", "Scotland", "Morocco", 0.90), 0.05),   # Brazil wins & Morocco shocks vs Haiti
        (("Scotland", "Morocco", "Brazil", 0.90), 0.03),   # Scotland wins & Morocco draws
        (("Scotland", "Brazil", "Morocco", 0.90), 0.02),
    ])
    g["C"] = (c1, c2, c3, c3q)

    # Group D: USA 1D LOCKED. Australia (3) vs Paraguay (3), Australia ahead on tiebreak/needs draw (~63% 2D)
    d2, d3 = sample_dist([
        (("Australia", "Paraguay"), 0.63),
        (("Paraguay", "Australia"), 0.37),
    ])
    g["D"] = ("United States", d2, d3, 0.72)

    # Group E: Germany 1E LOCKED. Ivory Coast vs Curacao (CIV needs 1 pt -> ~85% 2E), Ecuador vs Germany.
    e2, e3 = sample_dist([
        (("Ivory Coast", "Ecuador"), 0.80),
        (("Ecuador", "Ivory Coast"), 0.17),
        (("Ivory Coast", "Curacao"), 0.03),
    ])
    g["E"] = ("Germany", e2, e3, 0.65)

    # Group F: Netherlands (4, +4, 7GF) vs eliminated Tunisia (0, -9); Japan (4, +4, 6GF) vs Sweden (3, 0).
    # NED massive fav vs Tunisia (~88% win, likely by 2+ goals!). JPN vs SWE ~48% JPN, 25% draw, 27% SWE.
    f1, f2, f3, f3q = sample_dist([
        (("Netherlands", "Japan", "Sweden", 0.70), 0.56),   # NED 1F, JPN 2F
        (("Netherlands", "Sweden", "Japan", 0.95), 0.20),   # NED 1F, SWE beats JPN -> JPN 3F (4 pts qualifies!)
        (("Japan", "Netherlands", "Sweden", 0.65), 0.18),   # JPN wins bigger GD or NED slips
        (("Sweden", "Netherlands", "Japan", 0.90), 0.04),
        (("Japan", "Sweden", "Netherlands", 0.95), 0.02),
    ])
    g["F"] = (f1, f2, f3, f3q)

    # Group G: Egypt (4, +2) vs Iran (2, 0); Belgium (2, 0) vs New Zealand (1, -2).
    # Belgium heavy fav vs NZ (~72%), Egypt slight fav vs Iran (~45% EGY, 30% draw, 25% IRN).
    g1, g2, g3, g3q = sample_dist([
        (("Egypt", "Belgium", "Iran", 0.35), 0.38),
        (("Belgium", "Egypt", "Iran", 0.45), 0.25),   # EGY draws IRN & BEL wins big vs NZ
        (("Egypt", "Iran", "Belgium", 0.50), 0.14),   # BEL fails to beat NZ
        (("Iran", "Belgium", "Egypt", 0.92), 0.14),   # IRN beats EGY & BEL beats NZ
        (("Iran", "Egypt", "Belgium", 0.40), 0.05),
        (("Belgium", "New Zealand", "Egypt", 0.90), 0.04),
    ])
    g["G"] = (g1, g2, g3, g3q)

    # Group H: Spain (4, +4) vs Uruguay (2, 0); Cape Verde (2, 0) vs Saudi Arabia (1, -4).
    # Spain win ~55%, draw ~27%, Uruguay win ~18%! (Spain 1H ~82%, 2H ~15%, 3H ~3%!)
    h1, h2, h3, h3q = sample_dist([
        (("Spain", "Cape Verde", "Uruguay", 0.50), 0.34), # Spain beats Uruguay, CPV wins/draws
        (("Spain", "Uruguay", "Cape Verde", 0.65), 0.38), # Spain draws Uruguay OR Spain wins & CPV fails to win
        (("Spain", "Saudi Arabia", "Uruguay", 0.45), 0.10),
        (("Uruguay", "Spain", "Cape Verde", 0.65), 0.14), # Uruguay beats Spain, Spain 2H!
        (("Uruguay", "Cape Verde", "Spain", 0.95), 0.02), # Uruguay beats Spain AND CPV wins big
        (("Cape Verde", "Spain", "Uruguay", 0.60), 0.02),
    ])
    g["H"] = (h1, h2, h3, h3q)

    # Group I: France (6, +5) vs Norway (6, +4). Draw gives France 1I!
    # With Deschamps away + potential rotation on both sides: France win/draw ~72%, Norway win ~28%!
    i1, i2 = sample_dist([
        (("France", "Norway"), 0.72),
        (("Norway", "France"), 0.28),
    ])
    # 3I: Senegal vs Iraq (both 0 pts, winner gets 3 pts -> lowish chance of best-8 3rd ~35%)
    i3 = "Senegal" if random.random() < 0.72 else "Iraq"
    g["I"] = (i1, i2, i3, 0.35)

    # Group J: Argentina 1J LOCKED (6 pts). Austria (3, 0) vs Algeria (3, -2), Austria wins 2J on win/draw (~66%).
    j2, j3 = sample_dist([
        (("Austria", "Algeria"), 0.66),
        (("Algeria", "Austria"), 0.34),
    ])
    g["J"] = ("Argentina", j2, j3, 0.55)

    # Group K: Colombia (6, +3) vs Portugal (4, +5). Draw/win -> Colombia 1K; Portugal win -> Portugal 1K.
    # Portugal slightly stronger, say ~45% POR win, 55% COL win/draw.
    k1, k2 = sample_dist([
        (("Colombia", "Portugal"), 0.55),
        (("Portugal", "Colombia"), 0.45),
    ])
    k3 = "DR Congo" if random.random() < 0.65 else "Uzbekistan"
    g["K"] = (k1, k2, k3, 0.45)

    # Group L: England (4, +2) vs Panama (0, -2); Ghana (4, +1) vs Croatia (3, -1).
    # England beats Panama ~83%, draws ~12%, loses ~5%. Ghana vs Croatia: CRO ~46%, draw ~28%, GHA ~26%.
    l1, l2, l3, l3q = sample_dist([
        (("England", "Croatia", "Ghana", 0.95), 0.38), # ENG wins, CRO beats GHA -> GHA 4pts 3rd!
        (("England", "Ghana", "Croatia", 0.85), 0.41), # ENG wins, GHA win/draw -> CRO 3-4pts 3rd!
        (("Ghana", "England", "Croatia", 0.75), 0.13), # GHA overtakes ENG on GD or ENG draws PAN
        (("Croatia", "England", "Ghana", 0.90), 0.06), # ENG slips, CRO wins group
        (("Ghana", "Croatia", "England", 0.95), 0.02),
    ])
    g["L"] = (l1, l2, l3, l3q)
    return g

# Eligible 3rd-place groups for each of the 8 group-winner R32 slots:
THIRD_SLOTS = {
    "M74": ["A", "B", "C", "D", "F"],
    "M77": ["C", "D", "F", "G", "H"],
    "M79": ["C", "E", "F", "H", "I"],
    "M80": ["E", "H", "I", "J", "K"],
    "M81": ["B", "E", "F", "I", "J"],
    "M82": ["A", "E", "H", "I", "J"],
    "M85": ["E", "F", "G", "I", "J"],
    "M87": ["D", "E", "I", "J", "L"],
}

def assign_thirds(g):
    # Pick 8 advancing 3rd-place groups weighted by qualification probabilities
    scored = []
    for grp, (_, _, team3, qprob) in g.items():
        # noisy priority reflecting 4-pt vs 3-pt 3rd-place standings
        u = random.random() + qprob * 1.5
        scored.append((u, grp, team3))
    scored.sort(reverse=True)
    adv = {grp: team3 for _, grp, team3 in scored[:8]}

    # Greedy/backtracking bipartite matching to FIFA Annex C slots (always solvable for any 8 of 12)
    slots = list(THIRD_SLOTS.keys())
    random.shuffle(slots)
    assigned = {}
    used = set()
    def backtrack(idx):
        if idx == len(slots):
            return True
        s = slots[idx]
        cands = [grp for grp in THIRD_SLOTS[s] if grp in adv and grp not in used]
        random.shuffle(cands)
        for grp in cands:
            assigned[s] = adv[grp]
            used.add(grp)
            if backtrack(idx + 1):
                return True
            used.remove(grp)
        return False
    backtrack(0)
    return assigned

N = 60000
counts = {
    "QF_Boston": Counter(),
    "QF_LA": Counter(),
    "QF_Miami": Counter(),
    "QF_KC": Counter(),
    "SF1_Dallas": Counter(),
    "SF2_Atlanta": Counter(),
    "ThirdPlace": Counter(),
    "Champion": Counter(),
    "Reach_QF": Counter(),
    "Reach_SF": Counter(),
    "Reach_Final": Counter(),
}

for _ in range(N):
    g = sample_groups()
    th = assign_thirds(g)

    # Round of 32
    w73, _ = play_ko(g["A"][1], g["B"][1])
    w74, _ = play_ko(g["E"][0], th["M74"])
    w75, _ = play_ko(g["F"][0], g["C"][1])
    w76, _ = play_ko(g["C"][0], g["F"][1])
    w77, _ = play_ko(g["I"][0], th["M77"])
    w78, _ = play_ko(g["E"][1], g["I"][1])
    w79, _ = play_ko(g["A"][0], th["M79"], venue="Azteca")
    w80, _ = play_ko(g["L"][0], th["M80"])
    w81, _ = play_ko(g["D"][0], th["M81"], venue="USA")
    w82, _ = play_ko(g["G"][0], th["M82"])
    w83, _ = play_ko(g["K"][1], g["L"][1])
    w84, _ = play_ko(g["H"][0], g["J"][1])
    w85, _ = play_ko(g["B"][0], th["M85"])
    w86, _ = play_ko(g["J"][0], g["H"][1])
    w87, _ = play_ko(g["K"][0], th["M87"])
    w88, _ = play_ko(g["D"][1], g["G"][1])

    # Round of 16
    w89, _ = play_ko(w74, w77)
    w90, _ = play_ko(w73, w75)
    w91, _ = play_ko(w76, w78)
    w92, _ = play_ko(w79, w80, venue="Azteca")
    w93, _ = play_ko(w83, w84)
    w94, _ = play_ko(w81, w82, venue="USA")
    w95, _ = play_ko(w86, w88)
    w96, _ = play_ko(w85, w87)

    for t in (w89, w90, w91, w92, w93, w94, w95, w96):
        counts["Reach_QF"][t] += 1

    # Quarterfinals
    w97, _ = play_ko(w89, w90)  # Boston (July 9)
    w98, _ = play_ko(w93, w94, venue="USA")  # LA (July 10)
    w99, _ = play_ko(w91, w92)  # Miami (July 11)
    w100, _ = play_ko(w95, w96) # Kansas City (July 11)

    counts["QF_Boston"][w97] += 1
    counts["QF_LA"][w98] += 1
    counts["QF_Miami"][w99] += 1
    counts["QF_KC"][w100] += 1
    for t in (w97, w98, w99, w100):
        counts["Reach_SF"][t] += 1

    # Semifinals
    w101, l101 = play_ko(w97, w98, venue="USA") # Dallas (July 14)
    w102, l102 = play_ko(w99, w100)             # Atlanta (July 15)
    counts["SF1_Dallas"][w101] += 1
    counts["SF2_Atlanta"][w102] += 1
    counts["Reach_Final"][w101] += 1
    counts["Reach_Final"][w102] += 1

    # Third-place playoff (July 18) & Final (July 19)
    w103, _ = play_ko(l101, l102)
    w104, _ = play_ko(w101, w102)
    counts["ThirdPlace"][w103] += 1
    counts["Champion"][w104] += 1

print(f"Calibration Check -> Japan Reach_QF={counts['Reach_QF']['Japan']/N:.3f} (Opta 0.208), Reach_SF={counts['Reach_SF']['Japan']/N:.3f} (Opta 0.094)")
print()
for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final"]:
    print(f"=== {key} ===")
    top = counts[key].most_common(10)
    s5 = sum(c for _, c in top[:5]) / N
    for t, c in top:
        print(f"  {t:22s}: {c/N:.4f}")
    print(f"  [Top 5 sum = {s5:.4f}]")
    print()
