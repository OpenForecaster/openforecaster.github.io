import random
from collections import Counter

# ==============================================================================
# PART 1: Q2 (372528) — ATP CINCINNATI OPEN 2026 EXACT TREE DP (TUE AUG 18)
# ==============================================================================
# Verified R3 results through Tue Aug 18 (11 of 16 R3 matches COMPLETED!):
# Q1:
#   - Zverev d. Atmane 7-6(4) 7-6(6)
#   - Paul vs Vallejo (pending)
#   - Jodar d. Tabilo 6-2 6-1
#   - Cobolli d. Blockx 7-5 4-6 7-5
# Q2:
#   - Tirante d. Landaluce 7-6(5) 7-6(4)
#   - Hijikata vs Mensik (pending)
#   - Fils d. Lehecka 6-1 6-7(7) 6-3
#   - de Minaur d. Fery 7-5 7-6(3)
# Q3:
#   - Fritz d. Merida 6-3 6-4
#   - O'Connell d. Fonseca (w/o, abdominal injury) -> Fritz is 3-0 H2H (0 sets lost!)
#   - Borges d. Rublev 6-3 6-4
#   - Nakashima d. Medvedev (confirmed via market.csv qid 418046 resolved 2026-08-18!)
# Q4:
#   - Faria vs Walton (pending)
#   - Musetti d. Zheng 6-1 6-3
#   - Tien vs Tiafoe (pending)
#   - JM Cerundolo vs Auger-Aliassime (pending)

def build_atp_draw_aug18():
    q1 = (
        (
            "Alexander Zverev",
            ("Tommy Paul", "Adolfo Daniel Vallejo"),
        ),
        (
            "Rafael Jodar",
            "Flavio Cobolli",
        ),
    )
    q2 = (
        (
            "Thiago Agustin Tirante",
            ("Rinky Hijikata", "Jakub Mensik"),
        ),
        (
            "Arthur Fils",
            "Alex de Minaur",
        ),
    )
    q3 = (
        (
            "Taylor Fritz",
            "Christopher O'Connell",
        ),
        (
            "Nuno Borges",
            "Brandon Nakashima",
        ),
    )
    q4 = (
        (
            ("Jaime Faria", "Adam Walton"),
            "Lorenzo Musetti",
        ),
        (
            ("Learner Tien", "Frances Tiafoe"),
            ("Juan Manuel Cerundolo", "Felix Auger-Aliassime"),
        ),
    )
    return ((q1, q2), (q3, q4))

atp_elo = {
    "Alexander Zverev": 2105,       # ATP-leading 46th win; survived dangerous Atmane 7-6 7-6
    "Taylor Fritz": 2064,           # Crisp 6-3 6-4 vs Merida (8 aces, 83m), DC champ, fresh!
    "Rafael Jodar": 2036,           # Demolished Tabilo 6-2 6-1! Montreal SF, super sharp!
    "Felix Auger-Aliassime": 1998,  # #2 seed, beat Tsitsipas 6-3 7-5; pending R3 vs JM Cerundolo
    "Alex de Minaur": 1998,         # Beat Fery 7-5 7-6(3) despite 29 UEs & blowing 5-1 set 2 lead
    "Lorenzo Musetti": 1992,        # Crushed Zheng 6-1 6-3 in 71m, already in R16 vs Faria/Walton!
    "Jakub Mensik": 1986,           # Pending R3 vs Hijikata, then Tirante in R16!
    "Arthur Fils": 1982,            # Impressive 6-1 6-7 6-3 upset of #9 Lehecka!
    "Brandon Nakashima": 1980,      # DC SF + Montreal F + JUST BEAT MEDVEDEV!! Peak HC form!
    "Tommy Paul": 1952,             # Pending R3 vs Vallejo
    "Flavio Cobolli": 1952,         # RG finalist, battled past Blockx 7-5 4-6 7-5 (tired?)
    "Learner Tien": 1948,           # Pending R3 vs Tiafoe
    "Frances Tiafoe": 1890,         # Blitzed Sonego 6-3 6-4; pending R3 vs Tien
    "Nuno Borges": 1890,            # Crushed Rublev 6-3 6-4 in 72m!
    "Thiago Agustin Tirante": 1852, # Beat Djokovic & Landaluce 7-6 7-6
    "Jaime Faria": 1820,            # Beat Shelton 6-4 6-4
    "Rinky Hijikata": 1805,
    "Christopher O'Connell": 1800,  # Walkover vs Fonseca
    "Adam Walton": 1798,
    "Adolfo Daniel Vallejo": 1785,
    "Juan Manuel Cerundolo": 1775,  # Clay specialist
}

atp_h2h = {
    ("Taylor Fritz", "Christopher O'Connell"): +35,          # VERIFIED 3-0 H2H without dropping a set!
    ("Felix Auger-Aliassime", "Juan Manuel Cerundolo"): +25, # Huge fast-HC advantage vs clay specialist
    ("Alexander Zverev", "Taylor Fritz"): -15,               # Fritz won several recent big HC matches vs Zverev (USO/Wimb/LC)
    ("Taylor Fritz", "Brandon Nakashima"): +15,              # Fritz matchup edge on serve
}

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

tree_atp = build_atp_draw_aug18()
atp_regimes = [
    ("Base", atp_elo, atp_h2h, 400.0, 0.50),
    ("Form/Hot (Fritz+Jodar+Nak+Fils+Mus)", {
        **atp_elo,
        "Taylor Fritz": atp_elo["Taylor Fritz"] + 15,
        "Rafael Jodar": atp_elo["Rafael Jodar"] + 18,
        "Brandon Nakashima": atp_elo["Brandon Nakashima"] + 20,
        "Arthur Fils": atp_elo["Arthur Fils"] + 15,
        "Lorenzo Musetti": atp_elo["Lorenzo Musetti"] + 12,
        "Alexander Zverev": atp_elo["Alexander Zverev"] - 10,
        "Alex de Minaur": atp_elo["Alex de Minaur"] - 15,
    }, atp_h2h, 410.0, 0.25),
    ("Chalk/Pedigree (Zverev+FAA+ADM)", {
        **atp_elo,
        "Alexander Zverev": atp_elo["Alexander Zverev"] + 18,
        "Felix Auger-Aliassime": atp_elo["Felix Auger-Aliassime"] + 18,
        "Alex de Minaur": atp_elo["Alex de Minaur"] + 15,
        "Rafael Jodar": atp_elo["Rafael Jodar"] - 20,
        "Brandon Nakashima": atp_elo["Brandon Nakashima"] - 18,
    }, atp_h2h, 390.0, 0.25),
]

atp_blend = {}
print("=== PART 1: Q2 (372528) ATP CINCINNATI 2026 (AUG 18) ===")
for rname, elos, h2h, sc, rw in atp_regimes:
    res = solve_tree(tree_atp, elos, h2h, sc)
    print(f"  [{rname}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(res.items(), key=lambda x: -x[1])[:8]))
    for k, v in res.items():
        atp_blend[k] = atp_blend.get(k, 0.0) + rw * v

print("\n  FINAL ATP BLEND TOP 12:")
for k, v in sorted(atp_blend.items(), key=lambda x: -x[1])[:12]:
    print(f"    {k:26s}: {v:.4f}")
print(f"  Top-5 sum = {sum(v for _, v in sorted(atp_blend.items(), key=lambda x: -x[1])[:5]):.4f}")

# Sensitivity: check if FAA already WON vs LOST R3 (just to understand risk)
print("\n  [Note: P(FAA beats JM Cerundolo) =", round(win_prob("Felix Auger-Aliassime", "Juan Manuel Cerundolo", atp_elo, atp_h2h), 3), "]")
print("  [Note: P(Mensik beats Hijikata) =", round(win_prob("Jakub Mensik", "Rinky Hijikata", atp_elo, atp_h2h), 3), "]")

# ==============================================================================
# PART 2: Q3 (260735) — WTA CINCINNATI OPEN 2026 EXACT TREE DP (TUE AUG 18)
# ==============================================================================
# Verified R3 results through Tue Aug 18 (9 of 16 R3 matches COMPLETED!):
# Q1:
#   - Sabalenka vs Xinyu Wang (pending)
#   - Bejlek vs Alexandrova (pending)
#   - Keys d. Siniakova 6-1 6-3
#   - Xiyu Wang d. Svitolina (w/o, right ankle injury!)
# Q2:
#   - Gauff d. Ann Li (straight sets, 6-x 7-6)
#   - Bouzkova vs Jovic (pending)
#   - Kostyuk vs Stephens (pending)
#   - Andreeva d. Tjen 6-1 7-6
# Q3:
#   - Noskova vs Tauson (pending)
#   - Anisimova d. Eala 4-6 6-4 6-2
#   - Cirstea vs Kalinskaya (pending)
#   - Pegula d. Navarro 7-5 6-2
# Q4:
#   - Swiatek vs Parry (R16 LOCKED)
#   - Shnaider vs Chwalinska (pending)
#   - Rybakina d. Frech 6-4 7-6(2)

def build_wta_draw_aug18():
    q1 = (
        (
            ("Aryna Sabalenka", "Xinyu Wang"),
            ("Sara Bejlek", "Ekaterina Alexandrova"),
        ),
        (
            "Madison Keys",
            "Xiyu Wang",
        ),
    )
    q2 = (
        (
            "Coco Gauff",
            ("Marie Bouzkova", "Iva Jovic"),
        ),
        (
            ("Marta Kostyuk", "Sloane Stephens"),
            "Mirra Andreeva",
        ),
    )
    q3 = (
        (
            ("Linda Noskova", "Clara Tauson"),
            "Amanda Anisimova",
        ),
        (
            ("Sorana Cirstea", "Anna Kalinskaya"),
            "Jessica Pegula",
        ),
    )
    q4 = (
        (
            "Iga Swiatek",
            "Diane Parry",
        ),
        (
            ("Diana Shnaider", "Maja Chwalinska"),
            "Elena Rybakina",
        ),
    )
    return ((q1, q2), (q3, q4))

wta_elo = {
    "Aryna Sabalenka": 2168,        # Pending R3 vs Xinyu Wang; Svitolina WD clears Q1 slightly
    "Iga Swiatek": 2088,            # 8-match win streak, defending champ, ALREADY in R16 vs Parry
    "Coco Gauff": 2065,             # Clean R3 win over #28 Li, ALREADY in R16, 5-0 H2H vs Andreeva
    "Mirra Andreeva": 2055,         # Survived Tjen 6-1 7-6 (some set 2 nerves), ALREADY in R16
    "Elena Rybakina": 2050,         # Survived rain-delayed Frech 6-4 7-6(2), admitted fatigue, in R16
    "Jessica Pegula": 2025,         # Crisp 7-5 6-2 over Navarro, 2024 finalist, ALREADY in R16!
    "Amanda Anisimova": 1982,       # Beat Eala 4-6 6-4 6-2, ALREADY in R16!
    "Linda Noskova": 1975,          # Pending R3 vs Tauson (back pain)
    "Madison Keys": 1968,           # Crushed Siniakova 6-1 6-3, 2019 champ, faces Xiyu Wang in R16!
    "Marta Kostyuk": 1962,          # Pending R3 vs Stephens
    "Ekaterina Alexandrova": 1945,  # Pending R3 vs Bejlek
    "Diana Shnaider": 1942,         # Pending R3 vs Chwalinska
    "Anna Kalinskaya": 1925,        # Pending R3 vs Cirstea
    "Iva Jovic": 1922,              # Pending R3 vs Bouzkova
    "Marie Bouzkova": 1905,
    "Sorana Cirstea": 1905,
    "Xinyu Wang": 1895,
    "Clara Tauson": 1892,
    "Maja Chwalinska": 1885,
    "Sara Bejlek": 1865,
    "Xiyu Wang": 1865,              # Walkover vs Svitolina
    "Sloane Stephens": 1860,
    "Diane Parry": 1845,
}

wta_h2h = {
    ("Coco Gauff", "Mirra Andreeva"): +65,     # 5-0 H2H!
    ("Marta Kostyuk", "Mirra Andreeva"): +20,  # 2-1 H2H
    ("Iga Swiatek", "Elena Rybakina"): +25,    # Crushed Ryb 6-2 6-3 in Toronto F
    ("Iga Swiatek", "Diana Shnaider"): +25,    # Beat her 6-2 6-1 in Toronto QF
}

tree_wta = build_wta_draw_aug18()
wta_regimes = [
    ("Base", wta_elo, wta_h2h, 400.0, 0.55),
    ("Toronto-Fatigue (Swi/Ryb tired)", {
        **wta_elo,
        "Iga Swiatek": wta_elo["Iga Swiatek"] - 22,
        "Elena Rybakina": wta_elo["Elena Rybakina"] - 22,
    }, wta_h2h, 400.0, 0.30),
    ("Swiatek-Hot / Saba-Rusty", {
        **wta_elo,
        "Iga Swiatek": wta_elo["Iga Swiatek"] + 15,
        "Aryna Sabalenka": wta_elo["Aryna Sabalenka"] - 15,
    }, wta_h2h, 400.0, 0.15),
]

wta_blend = {}
print("\n=== PART 2: Q3 (260735) WTA CINCINNATI 2026 (AUG 18) ===")
for rname, elos, h2h, sc, rw in wta_regimes:
    res = solve_tree(tree_wta, elos, h2h, sc)
    print(f"  [{rname}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(res.items(), key=lambda x: -x[1])[:8]))
    for k, v in res.items():
        wta_blend[k] = wta_blend.get(k, 0.0) + rw * v

print("\n  FINAL WTA BLEND TOP 10:")
for k, v in sorted(wta_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"    {k:26s}: {v:.4f}")
print(f"  Top-5 sum = {sum(v for _, v in sorted(wta_blend.items(), key=lambda x: -x[1])[:5]):.4f}")
print("  [Note: P(Sabalenka beats Xinyu Wang) =", round(win_prob("Aryna Sabalenka", "Xinyu Wang", wta_elo, wta_h2h), 3), "]")

# ==============================================================================
# PART 3: Q4 (772246) — 2026 US OPEN MIXED DOUBLES MONTE CARLO SIMULATOR
# ==============================================================================
# OFFICIAL AUG 17 USTA ANNOUNCEMENT:
# 16-Team Main Draw (Aug 25-26, Fast-4 no-ad sets + 10-pt MTB = high variance!):
#   SEEDS (Top 4 direct entries by combined singles ranking):
#     #1: Sabalenka and Djokovic
#     #2: Rybakina and Fritz
#     #3: Shnaider and Medvedev
#     #4: Swiatek and Ruud (2025 US Open mixed doubles finalists; note Ruud retired Cinci R2)
#   UNSEEDED DIRECT ENTRIES (2):
#     #5: Bencic and Cobolli (note Bencic retired Cinci R2)
#     #6: Anisimova and Tien
#   CONFIRMED MAIN-DRAW WILD CARDS (5 of 8, ALL UNSEEDED):
#     WC1: Errani and Vavassori (2-time defending champions 2024 & 2025!! Pure doubles synergy!)
#     WC2: Townsend and Zverev (WTA #1/2x Slam doubles champ + ATP #2/#3 serve!)
#     WC3: Eala and Auger-Aliassime (DC champ + ATP #2 Cinci seed, athletic pair)
#     WC4: Fernandez and Tiafoe (2023 RG doubles F + electric NY crowd)
#     WC5: Svitolina and Monfils (spouses; note Svitolina Cinci ankle WD Aug 18)
#   REMAINING 3 MAIN-DRAW WILD CARDS (TBD, ALL UNSEEDED):
#     Likely pool: Venus Williams/Bublik, Osaka/Nishikori, Boulter/de Minaur, Ruse/Borges,
#                  maybe Andreeva/Rublev or Pegula/partner or Serena/partner
#   2 QUALIFIERS from 8-TEAM QUALIFYING TOURNAMENT ON AUG 24 (ALL UNSEEDED):
#     6 Confirmed Qualifying Teams (ALL elite doubles specialists!!):
#       Q1: Siniakova and Patten (11x + 2x Slam doubles champs!)
#       Q2: Dabrowski and Heliovaara (Multi-Slam doubles/mixed champs!)
#       Q3: Stefani and Skupski (Multi-Slam doubles/mixed champs!)
#       Q4: Krunic and Pavic (Multi-Slam mixed/doubles champ Pavic!)
#       Q5: Ostapenko and Arevalo (2024 USO doubles champ + multi-Slam doubles champ!)
#       Q6: Routliffe and Glasspool (2023 USO doubles champ + top-10 doubles!)
#     Plus 2 Qualifying Wild Cards (QWC1, QWC2 - weaker American/singles pairs)

# Fast-4 Mixed Doubles Ratings (scale=400, higher variance ~scale 460-500 for Fast-4 no-ad!)
# Calibrated to 2025 US Open Fan Week mixed doubles where:
#   - Pure doubles champions (Errani/Vavassori) dominated singles super-teams (~60-65% vs top singles pairs)
#   - Djokovic/Danilovic lost R1; Swiatek/Ruud reached Final; Pegula/Draper reached SF
#   - Sabalenka + Djokovic have massive serve/return firepower (better than Djokovic/Danilovic!),
#     but limited mixed doubles chemistry + Djokovic heat/age + Sabalenka deep Cinci fatigue -> ~1940-1960

mixed_ratings_base = {
    # Main draw seeds
    "Sabalenka and Djokovic": 1955,
    "Rybakina and Fritz": 1950,       # Huge serves for Fast-4!
    "Shnaider and Medvedev": 1955,    # Olympic doubles silver + Medvedev beat Djok in 2025 R1
    "Swiatek and Ruud": 1955,         # 2025 finalists! Slightly discounted for Ruud Cinci retirement
    # Unseeded confirmed direct entries
    "Bencic and Cobolli": 1885,       # Bencic hip injury watch
    "Anisimova and Tien": 1895,       # Sharp singles form, limited doubles pedigree
    # Confirmed WCs (unseeded)
    "Errani and Vavassori": 2075,     # 2x defending champs, elite mixed specialists (~63-67% vs Sab/Djok!)
    "Townsend and Zverev": 2015,      # World-class doubles queen Townsend + Zverev serve (~58% vs Sab/Djok!)
    "Fernandez and Tiafoe": 1940,     # Strong doubles hands (Fernandez) + Ashe energy
    "Eala and Auger-Aliassime": 1930, # Athletic + FAA huge serve & doubles bronze/gold pedigree
    "Svitolina and Monfils": 1855,    # Svitolina ankle injury + Monfils aging
    # 3 Remaining Main Draw WCs (generic placeholders representing typical WC strength)
    "WC_TBD_1": 1900,
    "WC_TBD_2": 1880,
    "WC_TBD_3": 1860,
    # Qualifying 8 teams (6 confirmed doubles specialists + 2 Q-WCs)
    "Siniakova and Patten": 2065,     # 11x Slam doubles + 2x Slam doubles — monster doubles team!
    "Dabrowski and Heliovaara": 2040, # Elite Slam doubles/mixed champs
    "Stefani and Skupski": 2025,      # Elite Slam doubles/mixed champs
    "Ostapenko and Arevalo": 2020,    # 2024 USO W doubles + multi-Slam M doubles
    "Routliffe and Glasspool": 2015,  # 2023 USO W doubles + top-10 M doubles
    "Krunic and Pavic": 2005,         # Multi-Slam mixed champ Pavic
    "QWC_1": 1840,
    "QWC_2": 1840,
}

def sim_mixed(ratings, scale=480.0, n_trials=150000, seed=42, p_play=0.82, p_sab_djok_bonus=0):
    rng = random.Random(seed)
    r = dict(ratings)
    r["Sabalenka and Djokovic"] += p_sab_djok_bonus

    qual_pool = [
        "Siniakova and Patten", "Dabrowski and Heliovaara", "Stefani and Skupski",
        "Ostapenko and Arevalo", "Routliffe and Glasspool", "Krunic and Pavic",
        "QWC_1", "QWC_2"
    ]
    unseeded_fixed = [
        "Bencic and Cobolli", "Anisimova and Tien",
        "Errani and Vavassori", "Townsend and Zverev",
        "Fernandez and Tiafoe", "Eala and Auger-Aliassime",
        "Svitolina and Monfils",
        "WC_TBD_1", "WC_TBD_2", "WC_TBD_3",
    ]

    p_cache = {}
    def mp(a, b):
        k = (a, b)
        v = p_cache.get(k)
        if v is None:
            v = 1.0 / (1.0 + 10.0 ** (-(r[a] - r[b]) / scale))
            p_cache[k] = v
        return v

    elim_cnt = Counter()
    qual_cnt = Counter()
    win_cnt = 0

    for _ in range(n_trials):
        # 1) Simulate 8-team Qualifying (2 pods of 4 -> 2 qualifiers!)
        # Seed top-4 doubles teams in qualifying (1 per pod/semi) or shuffle 2 brackets
        qp = qual_pool[:]
        rng.shuffle(qp)
        # Pod A: qp[0..3], Pod B: qp[4..7]
        qa1 = qp[0] if rng.random() < mp(qp[0], qp[1]) else qp[1]
        qa2 = qp[2] if rng.random() < mp(qp[2], qp[3]) else qp[3]
        q_win_a = qa1 if rng.random() < mp(qa1, qa2) else qa2

        qb1 = qp[4] if rng.random() < mp(qp[4], qp[5]) else qp[5]
        qb2 = qp[6] if rng.random() < mp(qp[6], qp[7]) else qp[7]
        q_win_b = qb1 if rng.random() < mp(qb1, qb2) else qb2

        qual_cnt[q_win_a] += 1
        qual_cnt[q_win_b] += 1

        # 2) Build 16-team Main Draw with 4 seeds:
        #    Slot 0 = #1 Sabalenka/Djokovic
        #    Slot 15 = #2 Rybakina/Fritz
        #    Slots 7 & 8 (SF lines: slot 4-7 vs 0-3, slot 8-11 vs 12-15 -> wait!)
        #    Standard 16-draw bracket:
        #      Top half: [0..7], Bottom half: [8..15]
        #      Top quarter: [0..3] (#1 at 0)
        #      2nd quarter: [4..7] (#3 or #4 at 4)
        #      3rd quarter: [8..11] (#3 or #4 at 11)
        #      Bottom quarter: [12..15] (#2 at 15)
        uns = unseeded_fixed + [q_win_a, q_win_b]
        rng.shuffle(uns)
        s34 = ["Shnaider and Medvedev", "Swiatek and Ruud"]
        if rng.random() < 0.5:
            s34 = [s34[1], s34[0]]

        br = [None] * 16
        br[0] = "Sabalenka and Djokovic"
        br[4] = s34[0]
        br[11] = s34[1]
        br[15] = "Rybakina and Fritz"
        ui = 0
        for i in range(16):
            if br[i] is None:
                br[i] = uns[ui]
                ui += 1

        # 3) Play out 4 rounds (R16 -> QF -> SF -> F)
        cur = br
        eliminated = False
        while len(cur) > 1:
            nxt = []
            for k in range(0, len(cur), 2):
                a, b = cur[k], cur[k+1]
                if rng.random() < mp(a, b):
                    w, l = a, b
                else:
                    w, l = b, a
                if l == "Sabalenka and Djokovic":
                    elim_cnt[w] += 1
                    eliminated = True
                nxt.append(w)
            cur = nxt
        if not eliminated:
            win_cnt += 1

    p_win_cond = win_cnt / n_trials
    p_elim_cond = 1.0 - p_win_cond
    print(f"\n  [scale={scale}, Sab/Djok={r['Sabalenka and Djokovic']}, p_play={p_play}]")
    print(f"    P(Sab/Djok win title | play) = {p_win_cond:.3f} | P(eliminated | play) = {p_elim_cond:.3f} | Uncond P(elim) = {p_play*p_elim_cond:.3f}")
    print(f"    P(Siniakova/Patten qualify)  = {qual_cnt['Siniakova and Patten']/n_trials:.3f}")
    print("    Top 10 Eliminators (UNCOND = p_play*P | COND_PLAY = P | COND_ELIM = P/P_elim):")
    for k, c in elim_cnt.most_common(12):
        p_cp = c / n_trials
        print(f"      {k:28s}: uncond={p_play*p_cp:.4f} | cond_play={p_cp:.4f} | cond_elim={p_cp/p_elim_cond:.4f}")
    return {k: c / n_trials for k, c in elim_cnt.items()}, p_elim_cond

print("\n=== PART 3: Q4 (772246) US OPEN MIXED DOUBLES MONTE CARLO (AUG 18) ===")
c1, e1 = sim_mixed(mixed_ratings_base, scale=480.0, n_trials=150000, seed=42, p_play=0.80, p_sab_djok_bonus=0)
c2, e2 = sim_mixed(mixed_ratings_base, scale=520.0, n_trials=150000, seed=43, p_play=0.80, p_sab_djok_bonus=-35) # Sab/Djok weaker in doubles (like 2025 Djok R1 exit)
c3, e3 = sim_mixed(mixed_ratings_base, scale=440.0, n_trials=150000, seed=44, p_play=0.80, p_sab_djok_bonus=+35) # Sab/Djok stronger firepower

# Blend 50% Base, 30% Sab/Djok doubles-rusty, 20% Sab/Djok firepower
blend_uncond = Counter()
blend_cond_elim = Counter()
for k in set(c1) | set(c2) | set(c3):
    u = 0.80 * (0.50 * c1.get(k, 0) + 0.30 * c2.get(k, 0) + 0.20 * c3.get(k, 0))
    ce = 0.50 * (c1.get(k, 0) / e1) + 0.30 * (c2.get(k, 0) / e2) + 0.20 * (c3.get(k, 0) / e3)
    blend_uncond[k] = u
    blend_cond_elim[k] = ce

print("\n=== FINAL BLEND Q4 (772246) US OPEN MIXED DOUBLES (UNCOND vs COND_ELIM) ===")
for k, _ in blend_uncond.most_common(12):
    print(f"  {k:28s}: uncond(p_play=0.80)={blend_uncond[k]:.4f} | cond_elim={blend_cond_elim[k]:.4f}")
