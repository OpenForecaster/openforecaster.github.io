import random
from collections import Counter

# Include epistemic uncertainty in true team strength (sigma=55 Elo per tournament draw)
# AND slight uncertainty in group-outcome probabilities!
random.seed(42)

BASE_ELO = {
    "France": 2125,      # DraftKings +400 #1 fav
    "Spain": 2120,       # 33 unbeaten, Yamal back
    "Argentina": 2105,   # Defending champs, locked 1J, Messi 5g
    "England": 2050,     # Beat CRO 4-2, drew GHA 0-0, Rice/James injury watch
    "Germany": 2030,     # Locked 1E, 7-1 CUW, 2-1 CIV
    "Portugal": 2015,    # 1-1 COD, 5-0 UZB
    "Netherlands": 2005, # 2-2 JPN, 5-1 SWE
    "Brazil": 1995,      # 1-1 MAR, 3-0 HAI, Raphinha injured, Opta #8
    "Colombia": 1955,    # 2-0-0
    "Morocco": 1915,
    "Norway": 1915,      # 2-0-0, Haaland 4g
    "Uruguay": 1900,
    "Switzerland": 1895, # Locked 1B
    "Japan": 1895,       # 2-2 NED, 4-0 TUN
    "Belgium": 1880,
    "Croatia": 1875,
    "Mexico": 1865,
    "United States": 1865,
    "Sweden": 1845,
    "Ecuador": 1845,
    "Canada": 1835,
    "Austria": 1835,
    "Ivory Coast": 1830,
    "South Korea": 1825,
    "Egypt": 1820,
    "Ghana": 1815,
    "Senegal": 1815,
    "Czechia": 1810,
    "Australia": 1805,
    "Paraguay": 1800,
    "Scotland": 1805,
    "Algeria": 1790,
    "Bosnia and Herzegovina": 1785,
    "Iran": 1780,
    "Cape Verde": 1760,
    "South Africa": 1750,
    "Saudi Arabia": 1745,
    "DR Congo": 1765,
    "New Zealand": 1715,
    "Curacao": 1680,
    "Iraq": 1695,
    "Uzbekistan": 1715,
}

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

def sample_dist(items):
    r = random.random()
    c = 0.0
    for val, prob in items:
        c += prob
        if r <= c:
            return val
    return items[-1][0]

def sample_groups():
    g = {}
    a2, a3 = sample_dist([(("South Korea", "Czechia"), 0.50), (("South Korea", "South Africa"), 0.22), (("Czechia", "South Korea"), 0.16), (("South Africa", "South Korea"), 0.12)])
    g["A"] = ("Mexico", a2, a3, 0.55)
    g["B"] = ("Switzerland", "Canada", "Bosnia and Herzegovina", 0.99)
    c1, c2, c3, c3q = sample_dist([
        (("Brazil", "Morocco", "Scotland", 0.55), 0.56),
        (("Morocco", "Brazil", "Scotland", 0.55), 0.26),
        (("Morocco", "Scotland", "Brazil", 0.90), 0.08),
        (("Brazil", "Scotland", "Morocco", 0.90), 0.05),
        (("Scotland", "Morocco", "Brazil", 0.90), 0.03),
        (("Scotland", "Brazil", "Morocco", 0.90), 0.02),
    ])
    g["C"] = (c1, c2, c3, c3q)
    d2, d3 = sample_dist([(("Australia", "Paraguay"), 0.63), (("Paraguay", "Australia"), 0.37)])
    g["D"] = ("United States", d2, d3, 0.72)
    e2, e3 = sample_dist([(("Ivory Coast", "Ecuador"), 0.80), (("Ecuador", "Ivory Coast"), 0.17), (("Ivory Coast", "Curacao"), 0.03)])
    g["E"] = ("Germany", e2, e3, 0.65)
    f1, f2, f3, f3q = sample_dist([
        (("Netherlands", "Japan", "Sweden", 0.70), 0.58),
        (("Netherlands", "Sweden", "Japan", 0.95), 0.20),
        (("Japan", "Netherlands", "Sweden", 0.65), 0.16),
        (("Sweden", "Netherlands", "Japan", 0.90), 0.04),
        (("Japan", "Sweden", "Netherlands", 0.95), 0.02),
    ])
    g["F"] = (f1, f2, f3, f3q)
    g1, g2, g3, g3q = sample_dist([
        (("Egypt", "Belgium", "Iran", 0.35), 0.38),
        (("Belgium", "Egypt", "Iran", 0.45), 0.25),
        (("Egypt", "Iran", "Belgium", 0.50), 0.14),
        (("Iran", "Belgium", "Egypt", 0.92), 0.14),
        (("Iran", "Egypt", "Belgium", 0.40), 0.05),
        (("Belgium", "New Zealand", "Egypt", 0.90), 0.04),
    ])
    g["G"] = (g1, g2, g3, g3q)
    h1, h2, h3, h3q = sample_dist([
        (("Spain", "Cape Verde", "Uruguay", 0.50), 0.34),
        (("Spain", "Uruguay", "Cape Verde", 0.65), 0.38),
        (("Spain", "Saudi Arabia", "Uruguay", 0.45), 0.10),
        (("Uruguay", "Spain", "Cape Verde", 0.65), 0.14),
        (("Uruguay", "Cape Verde", "Spain", 0.95), 0.02),
        (("Cape Verde", "Spain", "Uruguay", 0.60), 0.02),
    ])
    g["H"] = (h1, h2, h3, h3q)
    i1, i2 = sample_dist([(("France", "Norway"), 0.77), (("Norway", "France"), 0.23)])
    i3 = "Senegal" if random.random() < 0.72 else "Iraq"
    g["I"] = (i1, i2, i3, 0.35)
    j2, j3 = sample_dist([(("Austria", "Algeria"), 0.66), (("Algeria", "Austria"), 0.34)])
    g["J"] = ("Argentina", j2, j3, 0.55)
    k1, k2 = sample_dist([(("Colombia", "Portugal"), 0.54), (("Portugal", "Colombia"), 0.46)])
    k3 = "DR Congo" if random.random() < 0.65 else "Uzbekistan"
    g["K"] = (k1, k2, k3, 0.45)
    l1, l2, l3, l3q = sample_dist([
        (("England", "Croatia", "Ghana", 0.95), 0.38),
        (("England", "Ghana", "Croatia", 0.85), 0.42),
        (("Ghana", "England", "Croatia", 0.75), 0.12),
        (("Croatia", "England", "Ghana", 0.90), 0.06),
        (("Ghana", "Croatia", "England", 0.95), 0.02),
    ])
    g["L"] = (l1, l2, l3, l3q)
    return g

def assign_thirds(g):
    scored = [(random.random() + qprob * 1.5, grp, team3) for grp, (_, _, team3, qprob) in g.items()]
    scored.sort(reverse=True)
    adv = {grp: team3 for _, grp, team3 in scored[:8]}
    slots = list(THIRD_SLOTS.keys())
    random.shuffle(slots)
    assigned = {}
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
    bt(0)
    return assigned

N = 100000
counts = {k: Counter() for k in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_QF", "Reach_SF", "Reach_Final"]}

for _ in range(N):
    # Draw latent tournament strength with sigma=55 Elo
    ELO = {t: r + random.gauss(0, 55) for t, r in BASE_ELO.items()}
    def play_ko(a, b, venue=None):
        ba = 45 if (venue == "Azteca" and a == "Mexico") else (30 if (venue == "USA" and a == "United States") else 0)
        bb = 45 if (venue == "Azteca" and b == "Mexico") else (30 if (venue == "USA" and b == "United States") else 0)
        p = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + ba) - (ELO[b] + bb)) / 440.0))
        return (a, b) if random.random() < p else (b, a)

    g = sample_groups()
    th = assign_thirds(g)
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

    w89, _ = play_ko(w74, w77)
    w90, _ = play_ko(w73, w75)
    w91, _ = play_ko(w76, w78)
    w92, _ = play_ko(w79, w80, venue="Azteca")
    w93, _ = play_ko(w83, w84)
    w94, _ = play_ko(w81, w82, venue="USA")
    w95, _ = play_ko(w86, w88)
    w96, _ = play_ko(w85, w87)
    for t in (w89, w90, w91, w92, w93, w94, w95, w96): counts["Reach_QF"][t] += 1

    w97, _ = play_ko(w89, w90)
    w98, _ = play_ko(w93, w94, venue="USA")
    w99, _ = play_ko(w91, w92)
    w100, _ = play_ko(w95, w96)
    counts["QF_Boston"][w97] += 1
    counts["QF_KC"][w100] += 1
    for t in (w97, w98, w99, w100): counts["Reach_SF"][t] += 1

    w101, l101 = play_ko(w97, w98, venue="USA")
    w102, l102 = play_ko(w99, w100)
    counts["SF1_Dallas"][w101] += 1
    counts["SF2_Atlanta"][w102] += 1
    counts["Reach_Final"][w101] += 1
    counts["Reach_Final"][w102] += 1

    # Note: Third-place playoff has slightly higher variance (rotated lineups/motivation)
    w103, _ = play_ko(l101, l102)
    w104, _ = play_ko(w101, w102)
    counts["ThirdPlace"][w103] += 1
    counts["Champion"][w104] += 1

print(f"Japan calibration -> Reach_QF={counts['Reach_QF']['Japan']/N:.3f} (Opta 0.208), Reach_SF={counts['Reach_SF']['Japan']/N:.3f} (Opta 0.094)")
for key in ["QF_Boston", "QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final"]:
    print(f"\n=== {key} ===")
    top = counts[key].most_common(8)
    for t, cnt in top:
        print(f"  {t:20s}: {cnt/N:.4f}")
    print(f"  Top5 sum = {sum(cnt for _, cnt in top[:5])/N:.4f}")
