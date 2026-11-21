import math
import random
from collections import Counter

# ==============================================================================
# PART 1: Q3 (418046) — EXACT 96-PLAYER ATP CINCINNATI TREE DP (AUG 16 UPDATE)
# ALL CONFIRMED RESULTS THROUGH SUNDAY AUG 16 EVENING:
# Q1 (R2 100% DONE Sat Aug 15):
#   Zverev d. Norrie 3-6 6-3 6-3; Atmane d. Etcheverry 6-3 7-6(4)
#   Paul d. Hurkacz 6-4 6-7(3) 6-3; Vallejo d. Vacherot 6-3 6-3
#   Jodar d. Shapovalov 7-5 4-6 7-5; Tabilo d. Struff 6-3 6-4
#   Blockx d. Navone 6-3 6-4; Cobolli d. Kecmanovic 6-1 4-6 6-3
# Q2 (R2 100% DONE Sat Aug 15):
#   Tirante d. Djokovic 2-6 6-4 6-4; Landaluce d. Arnaldi 6-4 4-6 6-4
#   Hijikata d. Darderi 6-4 6-2; Mensik d. Bellucci 7-5 2-6 7-6(5)
#   Lehecka d. Berrettini 6-4 6-7(3) 6-3; Fils d. Hanfmann 7-6(5) 6-1
#   Fery d. Duckworth 6-4 2-6 7-6(4); de Minaur d. Halys 1-6 6-3 7-6(4)
# Q3 (MEDVEDEV'S QUARTER — SUN AUG 16):
#   Fritz d. Michelsen 6-3 6-4 -> R3!
#   Fonseca d. van de Zandschulp 6-4 7-6(2) -> R3!
#   O'Connell d. Ruud 7-5 1-2 ret. -> R3 (faces Fonseca)!
#   Rublev d. Carreno Busta (cruised) -> R3!
#   Borges vs F. Cerundolo (R2 confirmed matchup, Kokkinakis OUT)
#   Nakashima vs Kovacevic (R2 confirmed NO WD by Nakashima!)
#   Medvedev d. Trungelliti 6-4 7-5 -> R3! (Trungelliti OUT!)
# Q4 (SUN AUG 16):
#   Shelton vs Faria (R2 confirmed NO WD by Shelton!)
#   Tien d. Baez -> R3!
#   Rinderknech vs J.M. Cerundolo (R2 confirmed)
#   Auger-Aliassime d. Tsitsipas 6-3 7-5 -> R3!
# ==============================================================================

def build_atp_draw_aug16():
    q1 = (
        (
            ("Alexander Zverev", "Terence Atmane"),
            ("Tommy Paul", "Adolfo Daniel Vallejo"),
        ),
        (
            ("Rafael Jodar", "Alejandro Tabilo"),
            ("Alexander Blockx", "Flavio Cobolli"),
        ),
    )
    q2 = (
        (
            ("Thiago Agustin Tirante", "Martin Landaluce"),
            ("Rinky Hijikata", "Jakub Mensik"),
        ),
        (
            ("Jiri Lehecka", "Arthur Fils"),
            ("Arthur Fery", "Alex de Minaur"),
        ),
    )
    q3 = (
        (
            (
                "Taylor Fritz",
                (("Daniel Merida", "Marin Cilic"), "Zizou Bergs"),
            ),
            (
                "Joao Fonseca",
                "Christopher O'Connell",
            ),
        ),
        (
            (
                "Andrey Rublev",
                ("Nuno Borges", "Francisco Cerundolo"),
            ),
            (
                ("Brandon Nakashima", "Aleksandar Kovacevic"),
                "Daniil Medvedev",
            ),
        ),
    )
    q4 = (
        (
            (
                ("Ben Shelton", "Jaime Faria"),
                (("Adam Walton", "Qualifier_9"), "Ignacio Buse"),
            ),
            (
                ("Ugo Humbert", ("Fabian Marozsan", "Qualifier_10")),
                ("Daniel Altmaier", "Lorenzo Musetti"),
            ),
        ),
        (
            (
                "Learner Tien",
                (("Juncheng Shang", "Lorenzo Sonego"), "Frances Tiafoe"),
            ),
            (
                ("Arthur Rinderknech", "Juan Manuel Cerundolo"),
                "Felix Auger-Aliassime",
            ),
        ),
    )
    return ((q1, q2), (q3, q4))

atp_elo = {
    "Alexander Zverev": 2102,
    "Ben Shelton": 2070,
    "Taylor Fritz": 2054,            # Beat Michelsen 6-3 6-4 cleanly!
    "Rafael Jodar": 2026,
    "Alex de Minaur": 2004,
    "Daniil Medvedev": 2002,         # Beat Trungelliti 6-4 7-5 (rallied from 2-5 set 2)
    "Jakub Mensik": 1986,
    "Joao Fonseca": 1988,            # Beat Botic 6-4 7-6(2), faces O'Connell!
    "Felix Auger-Aliassime": 1988,   # Looked sharp/healthy beating Tsitsipas 6-3 7-5!
    "Andrey Rublev": 1980,           # Cruised past Carreno Busta!
    "Jiri Lehecka": 1978,
    "Lorenzo Musetti": 1974,
    "Arthur Fils": 1966,
    "Flavio Cobolli": 1950,
    "Tommy Paul": 1950,
    "Learner Tien": 1948,
    "Brandon Nakashima": 1940,       # Montreal F (slight fatigue baked in vs ~1955 peak)
    "Ugo Humbert": 1925,
    "Francisco Cerundolo": 1885,
    "Frances Tiafoe": 1855,
    "Zizou Bergs": 1855,
    "Alejandro Tabilo": 1855,
    "Alexander Blockx": 1852,
    "Arthur Rinderknech": 1845,
    "Aleksandar Kovacevic": 1842,    # Beat Khachanov in 3 on fast HC!
    "Nuno Borges": 1838,             # Beat Kokkinakis; 1-1 H2H vs Cerundolo
    "Fabian Marozsan": 1835,
    "Juncheng Shang": 1835,
    "Ignacio Buse": 1830,
    "Lorenzo Sonego": 1825,
    "Terence Atmane": 1830,
    "Thiago Agustin Tirante": 1835,
    "Martin Landaluce": 1820,
    "Arthur Fery": 1820,
    "Rinky Hijikata": 1805,
    "Marin Cilic": 1805,
    "Daniel Merida": 1800,
    "Christopher O'Connell": 1795,
    "Jaime Faria": 1785,
    "Daniel Altmaier": 1780,
    "Adolfo Daniel Vallejo": 1775,   # Beat Vacherot 6-3 6-3
    "Adam Walton": 1770,
    "Juan Manuel Cerundolo": 1745,
    "Qualifier_9": 1730,
    "Qualifier_10": 1730,
}

atp_h2h = {
    ("Andrey Rublev", "Daniil Medvedev"): -35,         # Medvedev leads career H2H ~7-2
    ("Brandon Nakashima", "Daniil Medvedev"): +15,     # Hot HC form vs Medvedev
    ("Brandon Nakashima", "Aleksandar Kovacevic"): +15,# 1-0 H2H (Brisbane SF 2026)
    ("Taylor Fritz", "Daniil Medvedev"): +20,
    ("Andrey Rublev", "Francisco Cerundolo"): -10,     # Cerundolo has given Rublev trouble before
}

def atp_win(a, b, elos, scale=400.0):
    diff = elos[a] - elos[b]
    if (a, b) in atp_h2h:
        diff += atp_h2h[(a, b)]
    elif (b, a) in atp_h2h:
        diff -= atp_h2h[(b, a)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def solve_atp(tree, elos, targets, scale=400.0):
    elim = {t: {} for t in targets}
    def rec(node):
        if isinstance(node, str):
            return {node: 1.0}
        l, r = node
        dl, dr = rec(l), rec(r)
        out = {}
        for a, pa in dl.items():
            wa = 0.0
            for b, pb in dr.items():
                pab = atp_win(a, b, elos, scale)
                wa += pb * pab
                if a in elim:
                    elim[a][b] = elim[a].get(b, 0.0) + pa * pb * (1.0 - pab)
                if b in elim:
                    elim[b][a] = elim[b].get(a, 0.0) + pa * pb * pab
            out[a] = pa * wa
        for b, pb in dr.items():
            out[b] = pb * sum(pa * atp_win(b, a, elos, scale) for a, pa in dl.items())
        return out
    return rec(tree), elim

print("=== PART 1: Q3 (418046) MEDVEDEV DEFEATER (AUG 16 POST-R2) ===")
for a, b in [
    ("Brandon Nakashima", "Aleksandar Kovacevic"),
    ("Daniil Medvedev", "Brandon Nakashima"),
    ("Daniil Medvedev", "Aleksandar Kovacevic"),
    ("Francisco Cerundolo", "Nuno Borges"),
    ("Andrey Rublev", "Francisco Cerundolo"),
    ("Andrey Rublev", "Nuno Borges"),
    ("Daniil Medvedev", "Andrey Rublev"),
    ("Taylor Fritz", "Daniil Medvedev"),
    ("Joao Fonseca", "Christopher O'Connell"),
    ("Taylor Fritz", "Joao Fonseca"),
]:
    print(f"  P({a} d. {b}) = {atp_win(a, b, atp_elo):.3f}")

atp_regimes = [
    ("Base", atp_elo.copy(), 400.0, 0.50),
    ("Upset-Fatigue", {**atp_elo,
                       "Daniil Medvedev": atp_elo["Daniil Medvedev"] - 25,
                       "Brandon Nakashima": atp_elo["Brandon Nakashima"] - 22,
                       "Aleksandar Kovacevic": atp_elo["Aleksandar Kovacevic"] + 15,
                       "Ben Shelton": atp_elo["Ben Shelton"] - 20}, 420.0, 0.25),
    ("Chalk-Hot", {**atp_elo,
                   "Daniil Medvedev": atp_elo["Daniil Medvedev"] + 22,
                   "Brandon Nakashima": atp_elo["Brandon Nakashima"] + 22,
                   "Ben Shelton": atp_elo["Ben Shelton"] + 20}, 380.0, 0.25),
]

tree_atp = build_atp_draw_aug16()
med_blend = {}
title_blend = {}
for rname, elos, sc, rw in atp_regimes:
    t, el = solve_atp(tree_atp, elos, ["Daniil Medvedev"], scale=sc)
    mc = {k: v / (1.0 - t["Daniil Medvedev"]) for k, v in el["Daniil Medvedev"].items()}
    print(f"  [{rname}] MedTitle={t['Daniil Medvedev']:.3f} | " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(mc.items(), key=lambda x: -x[1])[:7]))
    for k, v in mc.items():
        med_blend[k] = med_blend.get(k, 0.0) + rw * v
    for k, v in t.items():
        title_blend[k] = title_blend.get(k, 0.0) + rw * v

print("\nFINAL BLENDED Q3 (418046) MEDVEDEV DEFEATER TOP 10:")
for k, v in sorted(med_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"  {k:26s}: {v:.4f}")
print(f"  Top-5 sum = {sum(v for _, v in sorted(med_blend.items(), key=lambda x: -x[1])[:5]):.4f}")

# Sensitivity check: what if H2H Nakashima vs Medvedev is 0 instead of +15?
atp_h2h[("Brandon Nakashima", "Daniil Medvedev")] = 0
t_s, el_s = solve_atp(tree_atp, atp_elo, ["Daniil Medvedev"], scale=400.0)
mc_s = {k: v / (1.0 - t_s["Daniil Medvedev"]) for k, v in el_s["Daniil Medvedev"].items()}
print("  [Sens Nak-Med H2H=0] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(mc_s.items(), key=lambda x: -x[1])[:6]))

# ==============================================================================
# PART 2: Q1 (260735) — WTA CINCINNATI TREE DP (AUG 16 POST-R2 UPDATE!)
# CONFIRMED R2 RESULTS (Sat Aug 15 & Sun Aug 16):
# Q1: Sabalenka d. Gibson 6-2 7-6(2) -> R3!
#     Sara Bejlek d. Krejcikova 7-6(5) 6-4 -> Krejcikova OUT!
#     Madison Keys d. Snigur 4-6 6-3 6-3 -> R3!
#     Svitolina vs Tereza Valentova (pending Sun evening)
#     Alexandrova, Eva Lys (pending/unreported)
# Q2: Mirra Andreeva d. Oliynykova 6-1 6-0 -> R3!
#     Marta Kostyuk d. Kenin 4-6 6-3 7-5 -> R3! (faces Stephens/Potapova)
#     Coco Gauff, Iva Jovic (pending/unreported)
# Q3: Jessica Pegula d. Waltert 6-3 6-2 -> R3!
#     Emma Navarro d. Kalinina 3-6 6-4 6-2 -> R3!
#     Sorana Cirstea d. Bartunkova 7-6(5) 6-3 -> R3!
#     Alexandra Eala d. Ruse 6-1 3-0 ret. -> R3 (faces Anisimova!!)!
#     Amanda Anisimova d. Sonmez 6-2 6-3 -> R3 (faces Eala!!)!
#     Linda Noskova d. Boulter 6-3 6-3 -> R3!
#     Maja Chwalinska d. Bucsa 6-2 6-2; Clara Tauson d. Stearns; Kalinskaya d. McNally
# Q4: Iga Swiatek d. Arango 6-3 6-0 -> R3 (0% WD! faces Maria Sakkari!)
#     Maria Sakkari d. Rakhimova 6-2 5-7 6-1 -> R3 (faces Swiatek!)
#     Elena Rybakina d. Townsend 6-3 6-4 -> R3 (0% WD!)
#     Magdalena Frech d. Jelena Ostapenko 6-1 6-3 -> OSTAPENKO OUT!!
#     Diana Shnaider d. Maria 6-2 7-5 -> R3!
#     Mertens, Bencic (pending/unreported)
# ==============================================================================

def build_wta_draw_aug16():
    q1 = (
        (
            ("Aryna Sabalenka", ("Q1_R3a", "Q1_R3b")),
            (("Ekaterina Alexandrova", "Q1_R2b"), "Sara Bejlek"),
        ),
        (
            (("Elina Svitolina", "Tereza Valentova"), ("Q1_R3c", "Q1_R3d")),
            ("Madison Keys", ("Eva Lys", "Q1_R2f")),
        ),
    )
    q2 = (
        (
            (("Coco Gauff", "Q2_R2a"), ("Q2_R3a", "Q2_R3b")),
            (("Iva Jovic", "Q2_R2b"), ("Q2_R3c", "Q2_R3d")),
        ),
        (
            ("Mirra Andreeva", ("Q2_R3e", "Q2_R3f")),
            ("Marta Kostyuk", ("Sloane Stephens", "Anastasia Potapova")),
        ),
    )
    q3 = (
        (
            ("Jessica Pegula", "Emma Navarro"),
            ("Sorana Cirstea", "Anna Kalinskaya"),
        ),
        (
            ("Linda Noskova", "Maja Chwalinska"),
            ("Amanda Anisimova", "Alexandra Eala"),
        ),
    )
    q4 = (
        (
            ("Iga Swiatek", "Maria Sakkari"),
            (("Elise Mertens", "Q4_R2b"), ("Belinda Bencic", "Q4_R2c")),
        ),
        (
            ("Elena Rybakina", "Magdalena Frech"),
            ("Diana Shnaider", "Clara Tauson"),
        ),
    )
    return ((q1, q2), (q3, q4))

wta_elo = {
    "Aryna Sabalenka": 2170,        # Won R2 6-2 7-6(2) vs hot Gibson (needed 6 MPs, slight wind/fatigue note)
    "Iga Swiatek": 2080,            # Crushed Rybakina in Toronto F + crushed Arango 6-3 6-0 in 71m! Zero WD!
    "Coco Gauff": 2060,             # 2023 Cincy champ, Toronto SF, 5-0 vs Andreeva
    "Mirra Andreeva": 2058,         # Crushed Oliynykova 6-1 6-0 in 65m, saved 7/7 BPs, super fresh!
    "Elena Rybakina": 2055,         # Beat Townsend 6-3 6-4 ("happy with serve", low-stress start, zero WD!)
    "Jessica Pegula": 2015,         # Beat Waltert 6-3 6-2 (25-6 HC in 2026)
    "Amanda Anisimova": 1978,       # Beat Sonmez 6-2 6-3
    "Linda Noskova": 1975,          # Beat Boulter 6-3 6-3
    "Marta Kostyuk": 1962,          # Survived Kenin in 2.5h 3-setter
    "Elina Svitolina": 1955,        # Toronto SF fatigue, plays Valentova
    "Madison Keys": 1945,           # Survived Snigur in 3 sets
    "Ekaterina Alexandrova": 1945,
    "Diana Shnaider": 1942,         # Beat Maria 6-2 7-5
    "Alexandra Eala": 1938,         # 8 of last 9 wins, DC champ, faces Anisimova R3
    "Emma Navarro": 1925,           # Beat Kalinina in 3
    "Anna Kalinskaya": 1925,        # Beat McNally 6-3 6-4
    "Iva Jovic": 1920,
    "Elise Mertens": 1910,
    "Sorana Cirstea": 1905,
    "Clara Tauson": 1895,           # Playing through back pain vs Stearns
    "Maria Sakkari": 1890,          # Survived 3-set Rakhimova; faces Swiatek
    "Anastasia Potapova": 1885,
    "Maja Chwalinska": 1885,        # RG finalist, beat Bucsa 6-2 6-2
    "Magdalena Frech": 1875,        # Beat Ostapenko 6-1 6-3!
    "Belinda Bencic": 1865,         # Hip injury question
    "Sara Bejlek": 1860,            # Beat Pliskova + Krejcikova!
    "Eva Lys": 1855,
    "Tereza Valentova": 1850,
    "Sloane Stephens": 1835,
}
for q in ["Q1", "Q2", "Q3", "Q4"]:
    for s in ["R2a", "R2b", "R2c", "R2f", "R3a", "R3b", "R3c", "R3d", "R3e", "R3f"]:
        wta_elo[f"{q}_{s}"] = 1855 if s.startswith("R3") else 1835

wta_h2h = {
    ("Coco Gauff", "Mirra Andreeva"): +65,     # 5-0 H2H!
    ("Marta Kostyuk", "Mirra Andreeva"): +20,  # 2-1 H2H
    ("Iga Swiatek", "Elena Rybakina"): +25,    # Just crushed Ryb 6-2 6-3
    ("Iga Swiatek", "Maria Sakkari"): +35,     # Beat her at IW 2026 & strong recent HC H2H
    ("Iga Swiatek", "Diana Shnaider"): +25,    # Just beat her 6-2 6-1 in Toronto QF
}

def wta_win(a, b, elos, scale=400.0):
    diff = elos[a] - elos[b]
    if (a, b) in wta_h2h:
        diff += wta_h2h[(a, b)]
    elif (b, a) in wta_h2h:
        diff -= wta_h2h[(b, a)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def solve_wta(tree, elos, scale=400.0):
    def rec(node):
        if isinstance(node, str):
            return {node: 1.0}
        l, r = node
        dl, dr = rec(l), rec(r)
        out = {}
        for a, pa in dl.items():
            out[a] = pa * sum(pb * wta_win(a, b, elos, scale) for b, pb in dr.items())
        for b, pb in dr.items():
            out[b] = pb * sum(pa * wta_win(b, a, elos, scale) for a, pa in dl.items())
        return out
    return rec(tree)

tree_wta = build_wta_draw_aug16()
print("\n=== PART 2: Q1 (260735) WTA CINCINNATI CHAMPION (AUG 16 POST-R2) ===")
wta_regimes = [
    ("Base", wta_elo.copy(), 400.0, 0.50),
    ("Gauff-Already-Won-R2", wta_elo.copy(), 400.0, 0.25), # Check if Gauff already won/wins R2
    ("Toronto-Fatigue-Hits-R3", {**wta_elo,
                                 "Iga Swiatek": wta_elo["Iga Swiatek"] - 25,
                                 "Elena Rybakina": wta_elo["Elena Rybakina"] - 25}, 410.0, 0.25),
]
# Actually run clean sensitivity:
res_base = solve_wta(tree_wta, wta_elo, 400.0)
print("  [Base (Gauff still in R2)]")
for k, v in sorted(res_base.items(), key=lambda x: -x[1])[:8]:
    print(f"    {k:22s}: {v:.4f}")

# Sensitivity: Toronto finalists slight fatigue (-20 Swiatek, -20 Rybakina)
elo_fat = {**wta_elo, "Iga Swiatek": wta_elo["Iga Swiatek"] - 20, "Elena Rybakina": wta_elo["Elena Rybakina"] - 20}
res_fat = solve_wta(tree_wta, elo_fat, 400.0)
print("  [Toronto-Fatigue (-20 Swi/Ryb)]")
for k, v in sorted(res_fat.items(), key=lambda x: -x[1])[:8]:
    print(f"    {k:22s}: {v:.4f}")

# Blend 65% Base + 35% Toronto-Fatigue
wta_blend = {k: 0.65 * res_base[k] + 0.35 * res_fat[k] for k in res_base}
print("  [FINAL BLEND (65% Base / 35% Fatigue)]")
for k, v in sorted(wta_blend.items(), key=lambda x: -x[1])[:8]:
    print(f"    {k:22s}: {v:.4f}")

# ==============================================================================
# PART 3: Q5 (891014) — US OPEN MEN'S SINGLES (AUG 16 CALIBRATED UPDATE)
# Updates since Aug 13:
#   - Sinner: Eurosport Aug 15 confirms physio wrapping up, flying to NYC right after
#     Aug 16 birthday -> health posterior ticks slightly up: 65/26/9 -> 68/25/7
#   - Alcaraz: Eurosport Aug 15 ("più no che sì", Spanish insiders increasingly pessimistic,
#     closer to WD -> Laver Cup) + Tennis365 Aug 16 (Rusedski "shocked if he plays")
#     -> health posterior drops: 48/39/13 -> 60% WD / 31% Rusty / 9% NearPeak!
#   - Djokovic: Lost Cincy R2 to #50 Tirante 2-6 6-4 6-4, physically distressed in heat
#     (hands & knees, MTO) -> age-39 BO5 heat vulnerability trims Elo 2115 -> 2085
#   - Shelton: Won Montreal 10-0 sets -> Elo 2065 -> 2075; Fritz beat Michelsen cleanly (2072)
#   - FAA: Healthy again (beat Tsitsipas 6-3 7-5)
# ==============================================================================
def p_bo5(ea, eb):
    p3 = 1.0 / (1.0 + 10.0 ** (-(ea - eb) / 400.0))
    ps = p3
    for _ in range(8):
        f = ps*ps*(3 - 2*ps) - p3
        df = 6*ps*(1 - ps) + 1e-12
        ps = max(1e-6, min(1 - 1e-6, ps - f / df))
    return ps**3 * (10 - 15*ps + 6*ps*ps)

def place_128_draw(players, rng):
    seeds = players[:32]
    unseeded = players[32:]
    rng.shuffle(unseeded)
    bracket = [None] * 128
    bracket[0] = seeds[0]
    bracket[127] = seeds[1]
    s34 = [seeds[2], seeds[3]]
    rng.shuffle(s34)
    bracket[63], bracket[64] = s34[0], s34[1]
    s58 = list(seeds[4:8])
    rng.shuffle(s58)
    for pos, p in zip([31, 32, 95, 96], s58):
        bracket[pos] = p
    s916 = list(seeds[8:16])
    rng.shuffle(s916)
    for pos, p in zip([15, 16, 47, 48, 79, 80, 111, 112], s916):
        bracket[pos] = p
    pos_25_32 = [7, 24, 39, 56, 71, 88, 103, 120]
    pos_17_24 = [8, 23, 40, 55, 72, 87, 104, 119]
    s1724 = list(seeds[16:24])
    s2532 = list(seeds[24:32])
    rng.shuffle(s1724)
    rng.shuffle(s2532)
    for pos, p in zip(pos_17_24, s1724):
        bracket[pos] = p
    for pos, p in zip(pos_25_32, s2532):
        bracket[pos] = p
    ui = 0
    for i in range(128):
        if bracket[i] is None:
            bracket[i] = unseeded[ui]
            ui += 1
    return bracket

uso_field = [
    ("Jannik Sinner",        1, 2365),
    ("Alexander Zverev",     2, 2135),  # #2 seed Mon Aug 17!
    ("Carlos Alcaraz",       3, 2300),  # #3 seed Mon Aug 17!
    ("Novak Djokovic",       4, 2085),  # Trimmed 2115 -> 2085 after Cincy heat collapse
    ("Taylor Fritz",         5, 2072),
    ("Ben Shelton",          6, 2075),  # Won Montreal 10-0 sets!
    ("Alex de Minaur",       7, 2020),
    ("Daniil Medvedev",      8, 2020),
    ("Felix Auger-Aliassime",9, 2000),
    ("Rafael Jodar",        10, 2015),
    ("Lorenzo Musetti",     11, 1980),
    ("Jakub Mensik",        12, 2000),
    ("Learner Tien",        13, 1980),
    ("Andrey Rublev",       14, 1985),
    ("Jiri Lehecka",        15, 1980),
    ("Casper Ruud",         16, 1945),  # Retired in Cincy R2
    ("Brandon Nakashima",   17, 1975),
    ("Tommy Paul",          18, 1975),
    ("Frances Tiafoe",      19, 1975),
    ("Arthur Fils",         20, 1975),
    ("Flavio Cobolli",      21, 1945),
    ("Joao Fonseca",        22, 1990),
    ("Karen Khachanov",     23, 1955),
    ("Ugo Humbert",         24, 1945),
    ("Tomas Machac",        25, 1940),
    ("Francisco Cerundolo", 26, 1910),
    ("Valentin Vacherot",   27, 1900),
    ("Luciano Darderi",     28, 1905),
    ("Matteo Berrettini",   29, 1930),
    ("Matteo Arnaldi",      30, 1910),
    ("Hubert Hurkacz",      31, 1925),
    ("Alex Michelsen",      32, 1915),
]
unseeded_uso = [(f"Field_{k}", 1915 - (k * 200.0 / 96.0)) for k in range(96)]

def sim_uso_men(sinner_states, alcaraz_states, n_trials=8000, seed=42):
    rng = random.Random(seed)
    probs = Counter()
    for sn, ps, se in sinner_states:
        for an, pa, ae in alcaraz_states:
            w = ps * pa
            active = []
            for nm, _, el in uso_field:
                if nm == "Jannik Sinner":
                    if se is None: continue
                    active.append((nm, se))
                elif nm == "Carlos Alcaraz":
                    if ae is None: continue
                    active.append((nm, ae))
                else:
                    active.append((nm, el))
            pool = (active + unseeded_uso + [("LL_1", 1710), ("LL_2", 1710)])[:128]
            elos = [p[1] for p in pool]
            names = [p[0] for p in pool]
            idxs = list(range(128))
            pc = {}
            def gp(i, j):
                k = (elos[i], elos[j])
                v = pc.get(k)
                if v is None:
                    v = p_bo5(elos[i], elos[j])
                    pc[k] = v
                return v
            cnt = Counter()
            for _ in range(n_trials):
                cur = place_128_draw(idxs, rng)
                while len(cur) > 1:
                    nxt = []
                    for k in range(0, len(cur), 2):
                        a, b = cur[k], cur[k+1]
                        nxt.append(a if rng.random() < gp(a, b) else b)
                    cur = nxt
                cnt[names[cur[0]]] += 1
            for nm, c in cnt.items():
                probs[nm] += w * c / n_trials
    return probs

print("\n=== PART 3: Q5 (891014) US OPEN MEN'S SINGLES (AUG 16 UPDATE) ===")
p_uso = sim_uso_men(
    [("Healthy", 0.68, 2365), ("Limited", 0.25, 2200), ("WD", 0.07, None)],
    [("WD", 0.60, None), ("Rusty", 0.31, 2135), ("NearPeak", 0.09, 2300)],
    n_trials=8000
)
for k, v in p_uso.most_common(10):
    print(f"  {k:24s}: {v:.4f}")
