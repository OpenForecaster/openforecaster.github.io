import math

# ==============================================================================
# PART 1: Q2 (277746 Djokovic) & Q3 (418046 Medvedev) — TIGHT BET365 CALIBRATION
# ==============================================================================
q1_tree = (
    (
        (
            ("Alexander Zverev", ("Cameron Norrie", "Dino Prizmic")),
            (("Marton Fucsovics", "Terence Atmane"), "Tomas Martin Etcheverry"),
        ),
        (
            ("Tommy Paul", ("Corentin Moutet", "Hubert Hurkacz")),
            (("Qualifier_1", "Adolfo Daniel Vallejo"), "Valentin Vacherot"),
        ),
    ),
    (
        (
            ("Rafael Jodar", ("Denis Shapovalov", "Adrian Mannarino")),
            (("Roman Andres Burruchaga", "Jan-Lennard Struff"), "Alejandro Tabilo"),
        ),
        (
            ("Alexander Blockx", ("Mariano Navone", "Raphael Collignon")),
            (("Camilo Ugo Carabelli", "Miomir Kecmanovic"), "Flavio Cobolli"),
        ),
    ),
)

q2_tree = (
    (
        (
            ("Novak Djokovic", ("Thiago Agustin Tirante", "Jan Choinski")),
            (("Martin Landaluce", "Jack Draper"), "Matteo Arnaldi"),
        ),
        (
            ("Luciano Darderi", ("Rinky Hijikata", "Gael Monfils")),
            (("Zachary Svajda", "Mattia Bellucci"), "Jakub Mensik"),
        ),
    ),
    (
        (
            ("Jiri Lehecka", ("Qualifier_2", "Matteo Berrettini")),
            (("Yannick Hanfmann", "Qualifier_3"), "Arthur Fils"),
        ),
        (
            ("Arthur Fery", ("Qualifier_4", "James Duckworth")),
            (("Vit Kopriva", "Qualifier_5"), "Alex de Minaur"),
        ),
    ),
)

q3_tree = (
    (
        (
            ("Taylor Fritz", ("Alex Michelsen", "Jesper de Jong")),
            (("Daniel Merida", "Marin Cilic"), "Zizou Bergs"),
        ),
        (
            ("Joao Fonseca", ("Botic van de Zandschulp", "Tallon Griekspoor")),
            (("Qualifier_6", "Kamil Majchrzak"), "Casper Ruud"),
        ),
    ),
    (
        (
            ("Andrey Rublev", ("Tomas Machac", "Pablo Carreno Busta")),
            (("Nuno Borges", "Thanasi Kokkinakis"), "Francisco Cerundolo"),
        ),
        (
            ("Brandon Nakashima", ("Aleksandar Kovacevic", "Karen Khachanov")),
            (("Hamad Medjedovic", "Qualifier_7"), "Daniil Medvedev"),
        ),
    ),
)

q4_tree = (
    (
        (
            ("Ben Shelton", ("Qualifier_8", "Jenson Brooksby")),
            (("Adam Walton", "Qualifier_9"), "Ignacio Buse"),
        ),
        (
            ("Ugo Humbert", ("Fabian Marozsan", "Qualifier_10")),
            (("Qualifier_11", "Daniel Altmaier"), "Lorenzo Musetti"),
        ),
    ),
    (
        (
            ("Learner Tien", ("Sebastian Baez", "Grigor Dimitrov")),
            (("Juncheng Shang", "Lorenzo Sonego"), "Frances Tiafoe"),
        ),
        (
            ("Arthur Rinderknech", ("Qualifier_12", "Juan Manuel Cerundolo")),
            (("Valentin Royer", "Stefanos Tsitsipas"), "Felix Auger-Aliassime"),
        ),
    ),
)

full_draw = ((q1_tree, q2_tree), (q3_tree, q4_tree))

# Tightly calibrated to Aug 12 bet365 live outright odds (vig ~1.18-1.20)
base_elo = {
    "Alexander Zverev": 2106,       # bet365 +400 (vf ~0.169)
    "Novak Djokovic": 2088,         # bet365 +600 (vf ~0.121)
    "Ben Shelton": 2052,            # bet365 +700 (vf ~0.106)
    "Taylor Fritz": 2046,           # bet365 +900 (vf ~0.085)
    "Rafael Jodar": 2032,           # bet365 +1100 (vf ~0.071)
    "Alex de Minaur": 2005,         # #5 seed
    "Daniil Medvedev": 2006,        # bet365 +1800 (vf ~0.045)
    "Felix Auger-Aliassime": 1978,  # bet365 +2200 (vf ~0.037, back injury WD Montreal!)
    "Joao Fonseca": 1982,           # bet365 +2500 (vf ~0.033)
    "Lorenzo Musetti": 1974,        # bet365 +2500 (vf ~0.033)
    "Jakub Mensik": 1985,           # bet365 +2800 (vf ~0.029, tough Q2/Top-half draw)
    "Jiri Lehecka": 1975,           # #9 seed
    "Andrey Rublev": 1970,          # #13 seed
    "Flavio Cobolli": 1945,         # #7 seed
    "Arthur Fils": 1952,            # #21 seed
    "Tommy Paul": 1945,             # #18 seed
    "Learner Tien": 1938,           # #16 seed, Montreal SF fatigue
    "Brandon Nakashima": 1928,      # #27 seed, Montreal SF (hot HC form tempered by Montreal SF/F turnaround + ~10% WD risk)
    "Casper Ruud": 1930,            # #11 seed
    "Ugo Humbert": 1925,            # #24 seed
    "Karen Khachanov": 1915,        # fresh, dangerous fast-HC serve/FH
    "Tomas Machac": 1915,           # fast HC threat
    "Matteo Berrettini": 1905,
    "Hubert Hurkacz": 1900,
    "Alex Michelsen": 1890,
    "Tallon Griekspoor": 1885,
    "Valentin Vacherot": 1885,
    "Francisco Cerundolo": 1885,
    "Matteo Arnaldi": 1880,         # #31 seed
    "Luciano Darderi": 1878,        # #19 seed, Montreal QF
    "Stefanos Tsitsipas": 1875,
    "Jack Draper": 1855,            # WC, arm injury / Montreal tears (includes arm-retirement/WD discount)
    "Denis Shapovalov": 1865,
    "Grigor Dimitrov": 1865,
    "Frances Tiafoe": 1855,         # hand cyst surgery uncertain
    "Zizou Bergs": 1855,
    "Alejandro Tabilo": 1850,
    "Tomas Martin Etcheverry": 1845,
    "Arthur Rinderknech": 1845,
    "Alexander Blockx": 1840,
    "Botic van de Zandschulp": 1835,
    "Fabian Marozsan": 1835,
    "Cameron Norrie": 1835,
    "Juncheng Shang": 1835,
    "Ignacio Buse": 1830,
    "Nuno Borges": 1830,
    "Hamad Medjedovic": 1825,       # big serve/FH Serb, beat Medvedev 6-3 6-2 Marseille 2025
    "Jenson Brooksby": 1825,
    "Lorenzo Sonego": 1825,
    "Aleksandar Kovacevic": 1820,
    "Terence Atmane": 1820,
    "Miomir Kecmanovic": 1820,
    "Arthur Fery": 1815,
    "Thanasi Kokkinakis": 1815,
    "Jan-Lennard Struff": 1810,
    "Corentin Moutet": 1810,
    "Marton Fucsovics": 1805,
    "Marin Cilic": 1805,
    "Gael Monfils": 1805,
    "Daniel Merida": 1800,
    "Rinky Hijikata": 1785,
    "Mattia Bellucci": 1785,
    "Adrian Mannarino": 1785,
    "Pablo Carreno Busta": 1785,
    "Sebastian Baez": 1775,
    "Dino Prizmic": 1770,
    "Jesper de Jong": 1770,
    "Adam Walton": 1770,
    "Thiago Agustin Tirante": 1762, # ~rank 75, hot NA HC swing form
    "Zachary Svajda": 1765,
    "Kamil Majchrzak": 1765,
    "Daniel Altmaier": 1765,
    "James Duckworth": 1765,
    "Raphael Collignon": 1765,
    "Yannick Hanfmann": 1760,
    "Vit Kopriva": 1750,
    "Martin Landaluce": 1745,
    "Valentin Royer": 1745,
    "Camilo Ugo Carabelli": 1740,
    "Mariano Navone": 1735,
    "Roman Andres Burruchaga": 1735,
    "Adolfo Daniel Vallejo": 1730,
    "Juan Manuel Cerundolo": 1720,
    "Jan Choinski": 1680,           # ~rank 140-160 Challenger player
}
for i in range(1, 13):
    base_elo[f"Qualifier_{i}"] = 1725

h2h_deltas = {
    ("Jakub Mensik", "Novak Djokovic"): +30,        # Beat Djoko 2025 Miami F
    ("Jack Draper", "Novak Djokovic"): +55,         # Beat Djoko IW 2026; reaching R3 implies arm is healthy
    ("Alex de Minaur", "Novak Djokovic"): -40,      # Djoko dominates H2H
    ("Taylor Fritz", "Novak Djokovic"): -50,        # Djoko dominates H2H
    ("Alexander Zverev", "Novak Djokovic"): +10,    # Fast HC serve vs 39yo Djoko
    ("Hamad Medjedovic", "Daniil Medvedev"): +25,   # Beat Medvedev 6-3 6-2 Marseille 2025 SF
    ("Andrey Rublev", "Daniil Medvedev"): -35,      # Medvedev ~7-2 H2H over Rublev
    ("Brandon Nakashima", "Daniil Medvedev"): +15,  # Clean HC game vs struggling Medvedev
    ("Botic van de Zandschulp", "Daniil Medvedev"): +20,
    ("Taylor Fritz", "Daniil Medvedev"): +20,
    ("Joao Fonseca", "Casper Ruud"): +35,
}

def win_prob(a, b, elos, scale=400.0):
    diff = elos[a] - elos[b]
    if (a, b) in h2h_deltas:
        diff += h2h_deltas[(a, b)]
    elif (b, a) in h2h_deltas:
        diff -= h2h_deltas[(b, a)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def solve_tree(tree, elos, target_players, scale=400.0):
    elim_by = {t: {} for t in target_players}
    def recurse(node):
        if isinstance(node, str):
            return {node: 1.0}
        left, right = node
        dl = recurse(left)
        dr = recurse(right)
        out = {}
        for a, pa in dl.items():
            wa = 0.0
            for b, pb in dr.items():
                pab = win_prob(a, b, elos, scale=scale)
                wa += pb * pab
                if a in elim_by:
                    elim_by[a][b] = elim_by[a].get(b, 0.0) + pa * pb * (1.0 - pab)
                if b in elim_by:
                    elim_by[b][a] = elim_by[b].get(a, 0.0) + pa * pb * pab
            out[a] = pa * wa
        for b, pb in dr.items():
            wb = 0.0
            for a, pa in dl.items():
                pba = win_prob(b, a, elos, scale=scale)
                wb += pa * pba
            out[b] = pb * wb
        return out
    return recurse(tree), elim_by

bet365_raw = {
    "Alexander Zverev": 1/5.0,
    "Novak Djokovic": 1/7.0,
    "Ben Shelton": 1/8.0,
    "Taylor Fritz": 1/10.0,
    "Rafael Jodar": 1/12.0,
    "Daniil Medvedev": 1/19.0,
    "Felix Auger-Aliassime": 1/23.0,
    "Lorenzo Musetti": 1/26.0,
    "Joao Fonseca": 1/26.0,
    "Jakub Mensik": 1/29.0,
}

print("--- REFINED Match Win-Prob Sanity Check (Base) ---")
for a, b in [
    ("Novak Djokovic", "Thiago Agustin Tirante"),
    ("Novak Djokovic", "Jan Choinski"),
    ("Novak Djokovic", "Matteo Arnaldi"),
    ("Novak Djokovic", "Jack Draper"),
    ("Novak Djokovic", "Jakub Mensik"),
    ("Novak Djokovic", "Alex de Minaur"),
    ("Novak Djokovic", "Alexander Zverev"),
    ("Daniil Medvedev", "Hamad Medjedovic"),
    ("Daniil Medvedev", "Qualifier_7"),
    ("Daniil Medvedev", "Brandon Nakashima"),
    ("Daniil Medvedev", "Karen Khachanov"),
    ("Daniil Medvedev", "Andrey Rublev"),
    ("Daniil Medvedev", "Taylor Fritz"),
]:
    print(f"  P({a} beats {b}) = {win_prob(a, b, base_elo):.3f}")

regimes = [
    ("Base-Market", base_elo.copy(), 400.0, 0.50),
    ("Rust-Upset", {**base_elo, "Novak Djokovic": base_elo["Novak Djokovic"] - 30, "Daniil Medvedev": base_elo["Daniil Medvedev"] - 30, "Jack Draper": base_elo["Jack Draper"] + 35, "Brandon Nakashima": base_elo["Brandon Nakashima"] + 20}, 420.0, 0.25),
    ("Chalk-Class", {**base_elo, "Novak Djokovic": base_elo["Novak Djokovic"] + 30, "Daniil Medvedev": base_elo["Daniil Medvedev"] + 30, "Jack Draper": base_elo["Jack Draper"] - 30, "Brandon Nakashima": base_elo["Brandon Nakashima"] - 25}, 380.0, 0.25),
]

djoko_blend, med_blend = {}, {}
for rname, elos, sc, w in regimes:
    titles, elims = solve_tree(full_draw, elos, ["Novak Djokovic", "Daniil Medvedev"], scale=sc)
    if rname == "Base-Market":
        print("\n--- TIGHT Calibration vs bet365 (raw / 1.18 vig-free) ---")
        for p, raw in bet365_raw.items():
            print(f"  {p:24s} model={titles[p]:.4f}  bet365_vf={raw/1.18:.4f}")
        print()
    djo_cond = {k: v / (1 - titles["Novak Djokovic"]) for k, v in elims["Novak Djokovic"].items()}
    med_cond = {k: v / (1 - titles["Daniil Medvedev"]) for k, v in elims["Daniil Medvedev"].items()}
    for k, v in djo_cond.items():
        djoko_blend[k] = djoko_blend.get(k, 0.0) + w * v
    for k, v in med_cond.items():
        med_blend[k] = med_blend.get(k, 0.0) + w * v
    print(f"[{rname}] DjoT={titles['Novak Djokovic']:.3f} | " + ", ".join(f"{k}: {v:.3f}" for k, v in sorted(djo_cond.items(), key=lambda x: -x[1])[:7]))
    print(f"[{rname}] MedT={titles['Daniil Medvedev']:.3f} | " + ", ".join(f"{k}: {v:.3f}" for k, v in sorted(med_cond.items(), key=lambda x: -x[1])[:7]))

print("\n=== FINAL BLENDED DJOKOVIC (qid=277746) TOP 8 ===")
for k, v in sorted(djoko_blend.items(), key=lambda x: -x[1])[:8]:
    print(f"  {k:26s}: {v:.4f}")

print("\n=== FINAL BLENDED MEDVEDEV (qid=418046) TOP 8 ===")
for k, v in sorted(med_blend.items(), key=lambda x: -x[1])[:8]:
    print(f"  {k:26s}: {v:.4f}")


# ==============================================================================
# PART 2: Q5 (260735) — WTA CINCINNATI QUICK IMPACT CHECK (Osaka WD + Ryb fatigue)
# ==============================================================================
print("\n=== PART 2: WTA CINCINNATI IMPACT CHECK (qid=260735) ===")
# Exact 4-quarter simplified 16-pod tree (matching Aug 11 official WTA draw)
# Q1: Sabalenka (1) vs Alexandrova (16)/Krejcikova vs Svitolina (8) vs Keys (20)/LL [Osaka OUT!]
# Q2: Gauff (4) vs Jovic (13) vs Andreeva (5) vs Kostyuk (10)/Tjen
# Q3: Pegula (3) vs Eala (17) vs Noskova (6) vs Anisimova (9)
# Q4: Swiatek (7) vs Mertens (21)/Bencic? (12) vs Rybakina (2) vs Shnaider (14)/Ostapenko (26)

wta_elo_pre = {
    "Aryna Sabalenka": 2165,
    "Iga Swiatek": 2065,        # Toronto resurgence, but playing Wed SF / Thu F
    "Elena Rybakina": 2060,     # AO champ, but heavy Toronto fatigue
    "Mirra Andreeva": 2015,     # Fresh 8-9d rest
    "Coco Gauff": 2020,         # Fresh via Bencic W/O, playing Wed SF / Thu F
    "Jessica Pegula": 1995,
    "Amanda Anisimova": 1965,
    "Linda Noskova": 1955,
    "Elina Svitolina": 1965,    # Playing Wed SF / Thu F
    "Naomi Osaka": 1970,
    "Ekaterina Alexandrova": 1945,
    "Diana Shnaider": 1935,
    "Madison Keys": 1935,
    "Alexandra Eala": 1925,
    "Marta Kostyuk": 1930,
    "Iva Jovic": 1910,
    "Elise Mertens": 1905,
    "Belinda Bencic": 1860,     # Hip injury WD Toronto
    "Jelena Ostapenko": 1900,
    "Field_Q1": 1830,
    "Field_Q2": 1830,
    "Field_Q3": 1830,
    "Field_Q4": 1830,
}

def wta_tree(osaka_out=False):
    osaka_slot = "Field_Q1" if osaka_out else "Naomi Osaka"
    q1 = ((("Aryna Sabalenka", "Ekaterina Alexandrova"), ("Elina Svitolina", osaka_slot)))
    q2 = ((("Coco Gauff", "Iva Jovic"), ("Mirra Andreeva", "Marta Kostyuk")))
    q3 = ((("Jessica Pegula", "Alexandra Eala"), ("Linda Noskova", "Amanda Anisimova")))
    q4 = ((("Iga Swiatek", "Elise Mertens"), ("Elena Rybakina", "Diana Shnaider")))
    return ((q1, q2), (q3, q4))

def solve_wta(tree, elos, scale=400.0):
    def rec(node):
        if isinstance(node, str):
            return {node: 1.0}
        l, r = node
        dl, dr = rec(l), rec(r)
        out = {}
        for a, pa in dl.items():
            out[a] = pa * sum(pb / (1 + 10 ** (-(elos[a] - elos[b]) / scale)) for b, pb in dr.items())
        for b, pb in dr.items():
            out[b] = pb * sum(pa / (1 + 10 ** (-(elos[b] - elos[a]) / scale)) for a, pa in dl.items())
        return out
    return rec(tree)

# Note: 16-player model ignores ~15-20% R2/R3 early-round upset attrition, so scale by ~0.78 to compare deltas cleanly
t_pre = solve_wta(wta_tree(osaka_out=False), wta_elo_pre)
wta_elo_post = {**wta_elo_pre, "Elena Rybakina": wta_elo_pre["Elena Rybakina"] - 25} # extra 2h33m 3-setter + late Wed SF + potential Thu F -> fatigue/WD risk
t_post = solve_wta(wta_tree(osaka_out=True), wta_elo_post)
for p in ["Aryna Sabalenka", "Iga Swiatek", "Elena Rybakina", "Mirra Andreeva", "Coco Gauff", "Jessica Pegula"]:
    # Scaled by 0.78 for R2/R3 attrition
    pre_s = t_pre[p] * 0.78
    post_s = t_post[p] * 0.78
    print(f"  {p:22s}: pre={pre_s:.4f} -> post={post_s:.4f} (delta={post_s - pre_s:+.4f})")
