# ==============================================================================
# CINCINNATI OPEN 2026 EXACT TREE DP MODELS — WEDNESDAY AUG 19, 2026 (REFINED)
# ==============================================================================

def win_prob(a, b, elos, h2h, scale=400.0):
    diff = elos[a] - elos[b]
    if (a, b) in h2h:
        diff += h2h[(a, b)]
    elif (b, a) in h2h:
        diff -= h2h[(b, a)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def solve_tree(tree, elos, h2h, scale=400.0):
    def rec(node):
        if isinstance(node, str):
            return {node: 1.0}
        l, r = node
        dl, dr = rec(l), rec(r)
        out = {}
        for a, pa in dl.items():
            out[a] = pa * sum(pb * win_prob(a, b, elos, h2h, scale) for b, pb in dr.items())
        for b, pb in dr.items():
            out[b] = pb * sum(pa * win_prob(b, a, elos, h2h, scale) for a, pa in dl.items())
        return out
    return rec(tree)

# ==============================================================================
# PART 1: ATP CINCINNATI 2026 (qid=372528) — 12 PLAYERS REMAINING
# ==============================================================================
atp_tree = (
    (
        ("Tommy Paul", "Flavio Cobolli"),
        ("Thiago Agustin Tirante", "Arthur Fils"),
    ),
    (
        (
            ("Taylor Fritz", "Christopher O'Connell"),
            ("Nuno Borges", "Brandon Nakashima"),
        ),
        (
            ("Jaime Faria", "Lorenzo Musetti"),
            ("Frances Tiafoe", "Felix Auger-Aliassime"),
        ),
    ),
)

atp_elo = {
    "Taylor Fritz": 2066,            # #6 seed, DC champ, fresh, 3-0 vs O'Connell
    "Arthur Fils": 2020,             # #21 seed, beat #9 Lehecka & crushed #5 de Minaur 6-3 6-4, ALREADY in QF vs Tirante!
    "Felix Auger-Aliassime": 2016,   # #2 seed! Back healthy (d. Tsitsipas 6-3 7-5 & JM Cerundolo 7-5 6-1); elite fast-HC serve
    "Lorenzo Musetti": 1992,         # #10 seed, crushed Altmaier & Zheng 6-1 6-3; easy R16 vs Faria
    "Tommy Paul": 1990,              # #18 seed, beat Hurkacz, Vallejo, #1 Zverev (36 wins in 2026), ALREADY in QF!
    "Brandon Nakashima": 1984,       # #27 seed, 10-2 summer HC, Montreal F, beat Medvedev saving 3 MPs
    "Flavio Cobolli": 1980,          # #7 seed, RG finalist, beat Kecmanovic, Blockx & Jodar (all 3-setters), ALREADY in QF!
    "Frances Tiafoe": 1928,          # #17 seed, 2024 Cinci finalist, beat Sonego & Tien
    "Nuno Borges": 1895,             # Crushed Rublev 6-3 6-4 in 72m
    "Thiago Agustin Tirante": 1892,  # Beat Fritz (Montreal), Djokovic, Landaluce, #14 Mensik 5-7 6-4 6-4, ALREADY in QF!
    "Jaime Faria": 1832,             # Beat Shelton & Walton
    "Christopher O'Connell": 1800,   # Walkover vs Fonseca
}

atp_h2h = {
    ("Taylor Fritz", "Christopher O'Connell"): +35,  # Verified 3-0 H2H, 0 sets dropped (~85% Fritz)
    ("Taylor Fritz", "Brandon Nakashima"): +15,      # Fritz serve edge on fast HC
    ("Tommy Paul", "Flavio Cobolli"): +10,           # Fast US HC slight edge + Cobolli 3x 3-setters (2h30m today)
    ("Arthur Fils", "Thiago Agustin Tirante"): +18,  # Fast HC power mismatch vs clay-courter off 3-setter (~70% Fils)
    ("Felix Auger-Aliassime", "Lorenzo Musetti"): +15, # Fast Cincinnati HC favors FAA's serve over Musetti
}

atp_regimes = [
    ("Base (Balanced)", atp_elo, atp_h2h, 400.0, 0.45),
    ("Hot-Form / Upper-Half Freshness (Fils+Paul+Nak)", {
        **atp_elo,
        "Arthur Fils": atp_elo["Arthur Fils"] + 25,
        "Tommy Paul": atp_elo["Tommy Paul"] + 15,
        "Brandon Nakashima": atp_elo["Brandon Nakashima"] + 15,
        "Flavio Cobolli": atp_elo["Flavio Cobolli"] - 15,
        "Taylor Fritz": atp_elo["Taylor Fritz"] - 10,
    }, atp_h2h, 405.0, 0.25),
    ("Chalk / Pedigree (Fritz+FAA+Musetti+Cobolli)", {
        **atp_elo,
        "Taylor Fritz": atp_elo["Taylor Fritz"] + 22,
        "Felix Auger-Aliassime": atp_elo["Felix Auger-Aliassime"] + 18,
        "Lorenzo Musetti": atp_elo["Lorenzo Musetti"] + 15,
        "Flavio Cobolli": atp_elo["Flavio Cobolli"] + 15,
        "Arthur Fils": atp_elo["Arthur Fils"] - 18,
        "Tommy Paul": atp_elo["Tommy Paul"] - 15,
        "Thiago Agustin Tirante": atp_elo["Thiago Agustin Tirante"] - 25,
    }, atp_h2h, 385.0, 0.20),
    ("High-Parity Chaos (2026 Cinci Upset-Heavy)", atp_elo, atp_h2h, 450.0, 0.10),
]

print("=== PART 1: ATP CINCINNATI 2026 (qid=372528) — AUG 19 REFINED ===")
for a, b in [
    ("Taylor Fritz", "Christopher O'Connell"),
    ("Brandon Nakashima", "Nuno Borges"),
    ("Lorenzo Musetti", "Jaime Faria"),
    ("Felix Auger-Aliassime", "Frances Tiafoe"),
    ("Arthur Fils", "Thiago Agustin Tirante"),
    ("Tommy Paul", "Flavio Cobolli"),
    ("Felix Auger-Aliassime", "Lorenzo Musetti"),
]:
    print(f"  P({a} d. {b}) = {win_prob(a, b, atp_elo, atp_h2h):.3f}")

atp_blend = {}
for rname, elos, h2h, sc, rw in atp_regimes:
    res = solve_tree(atp_tree, elos, h2h, sc)
    print(f"  [{rname:48s} w={rw:.2f}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(res.items(), key=lambda x: -x[1])[:7]))
    for k, v in res.items():
        atp_blend[k] = atp_blend.get(k, 0.0) + rw * v

print("\nFINAL ATP BLEND (ALL 12 PLAYERS):")
for k, v in sorted(atp_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:26s}: {v:.4f}")
print(f"Top-5 sum = {sum(v for _, v in sorted(atp_blend.items(), key=lambda x: -x[1])[:5]):.4f}")

# ==============================================================================
# PART 2: WTA CINCINNATI 2026 (qid=260735) — 11 PLAYERS REMAINING
# ==============================================================================
wta_tree = (
    (
        (
            ("Aryna Sabalenka", "Sara Bejlek"),
            ("Madison Keys", "Xiyu Wang"),
        ),
        (
            ("Coco Gauff", "Marie Bouzkova"),
            "Marta Kostyuk",
        ),
    ),
    (
        ("Amanda Anisimova", "Jessica Pegula"),
        ("Iga Swiatek", "Elena Rybakina"),
    ),
)

wta_elo = {
    "Aryna Sabalenka": 2178,   # Demolished Xinyu Wang 6-1 6-3 in 54m! Q1 cleared (Alexandrova & Svitolina OUT!)
    "Iga Swiatek": 2095,       # #7 seed, defending champ, 9-match streak, beat Parry 6-3 6-3, ALREADY in QF!
    "Coco Gauff": 2065,        # #4 seed, 2023 champ, beat Ann Li 6-1 7-6(3), pending R16 vs Bouzkova
    "Elena Rybakina": 2065,    # #2 seed, AO champ, crisp 6-4 6-4 over Shnaider, ALREADY in QF!
    "Jessica Pegula": 2022,    # #3 seed, 2024 finalist, 25-6 HC in 2026, beat Cirstea in 3, ALREADY in QF!
    "Amanda Anisimova": 2014,  # #9 seed, crushed Wimbledon champ Noskova 6-1 6-4, ALREADY in QF!
    "Marta Kostyuk": 2005,     # #10 seed, crushed RG champ Andreeva 4-6 6-0 6-2 (12 of 14 games!), ALREADY in QF!
    "Madison Keys": 1972,      # 2019 champ, crushed Siniakova 6-1 6-3, pending R16 vs Xiyu Wang
    "Marie Bouzkova": 1916,    # #22 seed, beat Jovic
    "Sara Bejlek": 1882,       # Upset Krejcikova & Alexandrova 4-6 6-1 6-2 (clay-leaning lefty)
    "Xiyu Wang": 1865,         # Walkover vs injured Svitolina
}

wta_h2h = {
    ("Aryna Sabalenka", "Sara Bejlek"): +30,      # Fast-HC power mismatch (~87% Saba)
    ("Aryna Sabalenka", "Coco Gauff"): -35,       # Real H2H ~even (Gauff won USO 23, WTA Finals 24, RG 25 -> ~61% Saba, not 66%)
    ("Aryna Sabalenka", "Amanda Anisimova"): -45, # Real H2H favors Anisimova! (~64% Saba, not 72%)
    ("Aryna Sabalenka", "Madison Keys"): -25,     # Keys beat Sabalenka in 2025 AO Final (~74% Saba, not 77%)
    ("Aryna Sabalenka", "Elena Rybakina"): -15,   # Rybakina serve competitive on fast HC (~63% Saba)
    ("Aryna Sabalenka", "Iga Swiatek"): +15,      # Sabalenka fast-HC edge in Cinci (won 2024 Cinci SF 6-3 6-3 -> ~64% Saba)
    ("Iga Swiatek", "Elena Rybakina"): +22,       # Beat Rybakina 6-2 6-3 in Toronto F last week (~57% Swiatek)
    ("Jessica Pegula", "Amanda Anisimova"): +16,  # Pegula strong historical H2H edge (~53.5% Pegula)
}

wta_regimes = [
    ("Base (H2H-Calibrated)", wta_elo, wta_h2h, 400.0, 0.50),
    ("Toronto-Fatigue (Swi/Ryb tired, Saba/Peg/Ani fresh)", {
        **wta_elo,
        "Iga Swiatek": wta_elo["Iga Swiatek"] - 20,
        "Elena Rybakina": wta_elo["Elena Rybakina"] - 18,
        "Aryna Sabalenka": wta_elo["Aryna Sabalenka"] + 15,
    }, wta_h2h, 400.0, 0.25),
    ("Fast-Cinci Serve/Power (Ryb/Ani/Kos/Keys boost)", {
        **wta_elo,
        "Elena Rybakina": wta_elo["Elena Rybakina"] + 20,
        "Amanda Anisimova": wta_elo["Amanda Anisimova"] + 18,
        "Marta Kostyuk": wta_elo["Marta Kostyuk"] + 15,
        "Madison Keys": wta_elo["Madison Keys"] + 15,
        "Iga Swiatek": wta_elo["Iga Swiatek"] - 10,
    }, {**wta_h2h, ("Iga Swiatek", "Elena Rybakina"): +5, ("Jessica Pegula", "Amanda Anisimova"): +5}, 400.0, 0.15),
    ("Swiatek-Hot / Saba-Slip", {
        **wta_elo,
        "Iga Swiatek": wta_elo["Iga Swiatek"] + 18,
        "Aryna Sabalenka": wta_elo["Aryna Sabalenka"] - 20,
    }, wta_h2h, 400.0, 0.10),
]

print("\n=== PART 2: WTA CINCINNATI 2026 (qid=260735) — AUG 19 REFINED ===")
for a, b in [
    ("Aryna Sabalenka", "Sara Bejlek"),
    ("Aryna Sabalenka", "Madison Keys"),
    ("Aryna Sabalenka", "Coco Gauff"),
    ("Aryna Sabalenka", "Iga Swiatek"),
    ("Aryna Sabalenka", "Amanda Anisimova"),
    ("Coco Gauff", "Marie Bouzkova"),
    ("Coco Gauff", "Marta Kostyuk"),
    ("Jessica Pegula", "Amanda Anisimova"),
    ("Iga Swiatek", "Elena Rybakina"),
]:
    print(f"  P({a} d. {b}) = {win_prob(a, b, wta_elo, wta_h2h):.3f}")

wta_blend = {}
for rname, elos, h2h, sc, rw in wta_regimes:
    res = solve_tree(wta_tree, elos, h2h, sc)
    print(f"  [{rname:52s} w={rw:.2f}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(res.items(), key=lambda x: -x[1])[:7]))
    for k, v in res.items():
        wta_blend[k] = wta_blend.get(k, 0.0) + rw * v

print("\nFINAL WTA BLEND (ALL 11 PLAYERS):")
for k, v in sorted(wta_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:26s}: {v:.4f}")
print(f"Top-5 sum = {sum(v for _, v in sorted(wta_blend.items(), key=lambda x: -x[1])[:5]):.4f}")
