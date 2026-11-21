import math

# ==============================================================================
# PART 1: Q1 (277746) — EXACT 96-PLAYER ATP CINCINNATI TREE DP (AUG 14 UPDATE)
# Confirmed Day 1 (Thu Aug 13) Results & Withdrawals:
#   - Thiago Agustin Tirante def. Jan Choinski 7-6(9), 6-7(7), 7-6(4) [176m] -> LOCKED vs Djokovic R2!
#   - Martin Landaluce def. Jack Draper 6-3, 7-5 -> LOCKED vs Matteo Arnaldi R2!
#   - Rinky Hijikata def. Gael Monfils 2-6, 7-6(5), 6-3 -> LOCKED vs Luciano Darderi R2!
#   - Mattia Bellucci def. Zachary Svajda 7-6(0), 7-6(4) -> LOCKED vs Jakub Mensik R2!
#   - Cameron Norrie def. Dino Prizmic 3-6, 6-1, 6-4 -> LOCKED vs Zverev R2!
#   - Terence Atmane def. Marton Fucsovics 3-1 ret. -> LOCKED vs Etcheverry R2!
#   - Corentin Moutet WITHDREW -> LuckyLoser vs Hurkacz R1
#   - Denis Shapovalov def. Adrian Mannarino 6-1, 6-4 -> LOCKED vs Jodar R2!
#   - Jan-Lennard Struff def. Roman Andres Burruchaga 7-6(4), 2-6, 6-3 -> LOCKED vs Tabilo R2!
#   - Mariano Navone def. Raphael Collignon 6-3, 7-6(3) -> LOCKED vs Blockx R2!
#   - Miomir Kecmanovic def. Camilo Ugo Carabelli 6-3, 6-3 -> LOCKED vs Cobolli R2!
#   - Tallon Griekspoor WITHDREW -> LuckyLoser vs Botic van de Zandschulp R1
#   - Ben Shelton def. Brandon Nakashima 6-3, 7-6(4) in Montreal Final Thu night
#     (neither withdrawn as of Aug 14 9pm; still keep ~10% Shelton / ~15% Nakashima late WD risk)
# ==============================================================================

def build_atp_draw(shelton_wd=False, nakashima_wd=False):
    q1_tree = (
        (
            (
                ("Alexander Zverev", "Cameron Norrie"),
                ("Terence Atmane", "Tomas Martin Etcheverry"),
            ),
            (
                ("Tommy Paul", ("LuckyLoser_Moutet", "Hubert Hurkacz")),
                (("Qualifier_1", "Adolfo Daniel Vallejo"), "Valentin Vacherot"),
            ),
        ),
        (
            (
                ("Rafael Jodar", "Denis Shapovalov"),
                ("Jan-Lennard Struff", "Alejandro Tabilo"),
            ),
            (
                ("Alexander Blockx", "Mariano Navone"),
                ("Miomir Kecmanovic", "Flavio Cobolli"),
            ),
        ),
    )

    q2_tree = (
        (
            (
                ("Novak Djokovic", "Thiago Agustin Tirante"),
                ("Martin Landaluce", "Matteo Arnaldi"),
            ),
            (
                ("Luciano Darderi", "Rinky Hijikata"),
                ("Mattia Bellucci", "Jakub Mensik"),
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

    nak_slot = "LuckyLoser_Nak" if nakashima_wd else "Brandon Nakashima"
    q3_tree = (
        (
            (
                ("Taylor Fritz", ("Alex Michelsen", "Jesper de Jong")),
                (("Daniel Merida", "Marin Cilic"), "Zizou Bergs"),
            ),
            (
                ("Joao Fonseca", ("Botic van de Zandschulp", "LuckyLoser_Griekspoor")),
                (("Qualifier_6", "Kamil Majchrzak"), "Casper Ruud"),
            ),
        ),
        (
            (
                ("Andrey Rublev", ("Tomas Machac", "Pablo Carreno Busta")),
                (("Nuno Borges", "Thanasi Kokkinakis"), "Francisco Cerundolo"),
            ),
            (
                (nak_slot, ("Aleksandar Kovacevic", "Karen Khachanov")),
                (("Hamad Medjedovic", "Qualifier_7"), "Daniil Medvedev"),
            ),
        ),
    )

    sh_slot = "LuckyLoser_Sh" if shelton_wd else "Ben Shelton"
    q4_tree = (
        (
            (
                (sh_slot, ("Qualifier_8", "Jenson Brooksby")),
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
    return ((q1_tree, q2_tree), (q3_tree, q4_tree))


base_elo = {
    "Alexander Zverev": 2106,
    "Novak Djokovic": 2070,
    "Ben Shelton": 2065,            # Won Montreal without dropping a set!
    "Taylor Fritz": 2052,
    "Rafael Jodar": 2030,
    "Alex de Minaur": 2005,
    "Daniil Medvedev": 2004,
    "Felix Auger-Aliassime": 1978,
    "Joao Fonseca": 1982,
    "Lorenzo Musetti": 1974,
    "Jakub Mensik": 1985,
    "Jiri Lehecka": 1975,
    "Andrey Rublev": 1970,
    "Arthur Fils": 1962,
    "Flavio Cobolli": 1945,
    "Tommy Paul": 1945,
    "Learner Tien": 1940,
    "Brandon Nakashima": 1938,
    "Casper Ruud": 1930,
    "Ugo Humbert": 1925,
    "Karen Khachanov": 1918,
    "Tomas Machac": 1915,
    "Matteo Berrettini": 1905,
    "Hubert Hurkacz": 1900,
    "Alex Michelsen": 1890,
    "Valentin Vacherot": 1885,
    "Francisco Cerundolo": 1885,
    "Matteo Arnaldi": 1880,
    "Luciano Darderi": 1878,
    "Stefanos Tsitsipas": 1875,
    "Denis Shapovalov": 1872,       # Breezed past Mannarino 6-1, 6-4
    "Grigor Dimitrov": 1865,
    "Frances Tiafoe": 1855,
    "Zizou Bergs": 1855,
    "Alejandro Tabilo": 1850,
    "Cameron Norrie": 1848,
    "Tomas Martin Etcheverry": 1845,
    "Arthur Rinderknech": 1845,
    "Alexander Blockx": 1840,
    "Botic van de Zandschulp": 1835,
    "Fabian Marozsan": 1835,
    "Juncheng Shang": 1835,
    "Ignacio Buse": 1830,
    "Nuno Borges": 1830,
    "Hamad Medjedovic": 1825,
    "Jenson Brooksby": 1825,
    "Lorenzo Sonego": 1825,
    "Aleksandar Kovacevic": 1820,
    "Terence Atmane": 1820,
    "Miomir Kecmanovic": 1828,      # Beat Carabelli 6-3, 6-3
    "Arthur Fery": 1815,
    "Thanasi Kokkinakis": 1815,
    "Jan-Lennard Struff": 1812,
    "Marin Cilic": 1805,
    "Daniel Merida": 1800,
    "Martin Landaluce": 1790,
    "Rinky Hijikata": 1790,         # Beat Monfils in 3
    "Mattia Bellucci": 1792,        # Beat Svajda 7-6(0), 7-6(4), tricky lefty
    "Pablo Carreno Busta": 1785,
    "Sebastian Baez": 1775,
    "Jesper de Jong": 1770,
    "Adam Walton": 1770,
    "Thiago Agustin Tirante": 1760, # #65 (career-high #53), 20 aces vs Choinski, slight fatigue from 176m 3-TB R1
    "Kamil Majchrzak": 1765,
    "Daniel Altmaier": 1765,
    "James Duckworth": 1765,
    "Yannick Hanfmann": 1760,
    "Vit Kopriva": 1750,
    "Valentin Royer": 1745,
    "Mariano Navone": 1745,
    "Adolfo Daniel Vallejo": 1730,
    "Juan Manuel Cerundolo": 1720,
    "LuckyLoser_Nak": 1715,
    "LuckyLoser_Sh": 1715,
    "LuckyLoser_Moutet": 1715,
    "LuckyLoser_Griekspoor": 1715,
}
for i in range(1, 13):
    base_elo[f"Qualifier_{i}"] = 1725

h2h_deltas = {
    ("Jakub Mensik", "Novak Djokovic"): +30,
    ("Alex de Minaur", "Novak Djokovic"): -40,
    ("Taylor Fritz", "Novak Djokovic"): -50,
    ("Alexander Zverev", "Novak Djokovic"): +10,
    ("Alexander Zverev", "Cameron Norrie"): +55,  # Zverev is 7-0 vs Norrie!
    ("Hamad Medjedovic", "Daniil Medvedev"): +25,
    ("Andrey Rublev", "Daniil Medvedev"): -35,
    ("Brandon Nakashima", "Daniil Medvedev"): +15,
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

print("=== PART 1: Q1 (277746) DJOKOVIC DEFEATER SENSITIVITY ON TIRANTE ELO ===")
for tir_elo in [1725, 1745, 1760, 1775]:
    el = {**base_elo, "Thiago Agustin Tirante": tir_elo}
    regimes = [
        ("Base", el.copy(), 400.0, 0.50),
        ("Rust-Upset", {**el, "Novak Djokovic": el["Novak Djokovic"] - 35, "Martin Landaluce": el["Martin Landaluce"] + 25}, 420.0, 0.25),
        ("Chalk-Class", {**el, "Novak Djokovic": el["Novak Djokovic"] + 30, "Martin Landaluce": el["Martin Landaluce"] - 20}, 380.0, 0.25),
    ]
    djo_blend = {}
    djo_t = 0.0
    p_r2_loss = 0.0
    tree = build_atp_draw(False, False)
    for rname, elos, sc, w in regimes:
        titles, elims = solve_tree(tree, elos, ["Novak Djokovic"], scale=sc)
        djo_t += w * titles["Novak Djokovic"]
        p_r2_loss += w * win_prob("Thiago Agustin Tirante", "Novak Djokovic", elos, scale=sc)
        dc = {k: v / (1 - titles["Novak Djokovic"]) for k, v in elims["Novak Djokovic"].items()}
        for k, v in dc.items():
            djo_blend[k] = djo_blend.get(k, 0.0) + w * v
    top7 = ", ".join(f"{k}:{v:.4f}" for k, v in sorted(djo_blend.items(), key=lambda x: -x[1])[:7])
    print(f"  Tirante={tir_elo} | P(R2_loss)={p_r2_loss:.3f} | DjoT={djo_t:.3f} | {top7}")


# ==============================================================================
# PART 2: Q3 (260735) — DRAFTKINGS DE-VIGGING + POST-TORONTO FINAL WTA TREE DP
# ==============================================================================
print("\n=== PART 2: Q3 (260735) DRAFTKINGS AUG 13 ODDS DE-VIGGING ===")
dk_american = {
    "Aryna Sabalenka": 220,
    "Elena Rybakina": 650,
    "Coco Gauff": 650,
    "Iga Swiatek": 800,
    "Mirra Andreeva": 900,
    "Jessica Pegula": 1100,
    "Amanda Anisimova": 1600,
    "Marta Kostyuk": 2000,
    "Linda Noskova": 2800,
    "Elina Svitolina": 3000,
    "Madison Keys": 3000,
}
dk_raw = {k: 100.0 / (v + 100.0) for k, v in dk_american.items()}
# Add estimated field raw sum across remaining ~85 WTA players in 96-player draw
# (Alexandrova ~+4000, Shnaider ~+4000, Ostapenko ~+4500, Navarro ~+4500, Eala ~+5000, Jovic ~+5500, Mertens ~+6000, etc.)
# Typically remaining 85 players sum to ~0.24 - 0.28 raw implied probability on DraftKings
field_raw_list = [0.024, 0.024, 0.022, 0.022, 0.020, 0.018, 0.016, 0.014, 0.012, 0.010] + [0.002] * 40
# Total field raw = 0.182 + 0.080 = 0.262 -> Total book sum = 1.079 + 0.262 = 1.341 (typical DK WTA 1000 vig ~34%)
all_raw = list(dk_raw.values()) + field_raw_list
total_overround = sum(all_raw)

# Power method de-vig: find k > 1 such that sum(p^k) = 1.0
lo, hi = 1.0, 2.5
for _ in range(80):
    mid = (lo + hi) / 2
    if sum(p ** mid for p in all_raw) > 1.0:
        lo = mid
    else:
        hi = mid
k_pow = (lo + hi) / 2

print(f"Total book overround = {total_overround:.3f} | Power-method exponent k = {k_pow:.4f}")
print(f"{'Player':22s} | {'DK':>6s} | {'Raw':>6s} | {'Prop':>6s} | {'Power':>6s}")
for p, am in dk_american.items():
    r = dk_raw[p]
    print(f"{p:22s} | +{am:<5d} | {r:6.3f} | {r/total_overround:6.3f} | {r**k_pow:6.3f}")

print("\n=== PART 2B: FULL 32-POD WTA CINCINNATI TREE DP (POST-TORONTO FINAL!) ===")
# Exact 4-quarter structure verified from Aug 11 official WTA draw + RotoWire Aug 13 + WTA Aug 14:
# Q1: [1] Sabalenka (R2: Talia Gibson) -> [16] Alexandrova/Krejcikova -> [8] Svitolina / [20] Keys / Eva Lys (Osaka WD)
# Q2: [4] Gauff -> [13] Iva Jovic -> [5] Andreeva (R2: Oliynykova) -> [10] Kostyuk
# Q3: [3] Pegula -> Emma Navarro / Sorana Cirstea / [17] Eala -> [6] Noskova -> [9] Anisimova
# Q4: [7] Swiatek (R2: Arango) -> [21] Mertens / [12] Bencic (hip) -> [2] Rybakina -> [26] Ostapenko / [14] Shnaider

# Model explicitly includes R2/R3 early-round matches so NO ad-hoc scaling needed!
def build_wta_draw(swiatek_wd=False, rybakina_wd=False):
    sw_slot = "LL_Swiatek" if swiatek_wd else "Iga Swiatek"
    ry_slot = "LL_Rybakina" if rybakina_wd else "Elena Rybakina"

    # Each quarter has 8 pods (R2 -> R3 -> R16 -> QF)
    q1 = (
        (
            (("Aryna Sabalenka", "Talia Gibson"), ("Q1_R3a", "Q1_R3b")),
            (("Ekaterina Alexandrova", "Q1_R2b"), ("Barbora Krejcikova", "Q1_R2c")),
        ),
        (
            (("Elina Svitolina", "Q1_R2d"), ("Q1_R3c", "Q1_R3d")),
            (("Madison Keys", "Q1_R2e"), ("Eva Lys", "Q1_R2f")),
        ),
    )
    q2 = (
        (
            (("Coco Gauff", "Q2_R2a"), ("Q2_R3a", "Q2_R3b")),
            (("Iva Jovic", "Q2_R2b"), ("Q2_R3c", "Q2_R3d")),
        ),
        (
            (("Mirra Andreeva", "Oleksandra Oliynykova"), ("Q2_R3e", "Q2_R3f")),
            (("Marta Kostyuk", "Q2_R2d"), ("Q2_R3g", "Q2_R3h")),
        ),
    )
    q3 = (
        (
            (("Jessica Pegula", "Q3_R2a"), ("Emma Navarro", "Q3_R2b")),
            (("Sorana Cirstea", "Q3_R2c"), ("Alexandra Eala", "Q3_R2d")),
        ),
        (
            (("Linda Noskova", "Q3_R2e"), ("Q3_R3a", "Q3_R3b")),
            (("Amanda Anisimova", "Q3_R2f"), ("Q3_R3c", "Q3_R3d")),
        ),
    )
    q4 = (
        (
            ((sw_slot, "Emiliana Arango"), ("Q4_R3a", "Q4_R3b")),
            (("Elise Mertens", "Q4_R2b"), ("Belinda Bencic", "Q4_R2c")),
        ),
        (
            ((ry_slot, "Q4_R2d"), ("Jelena Ostapenko", "Q4_R2e")),
            (("Diana Shnaider", "Q4_R2f"), ("Q4_R3c", "Q4_R3d")),
        ),
    )
    return ((q1, q2), (q3, q4))

wta_elo_pre = {
    "Aryna Sabalenka": 2175,       # 25-2 HC in 2026, Brisbane/IW/Miami titles, 2024 Cincy champ, rested
    "Elena Rybakina": 2075,        # AO champ, SF IW/Miami/Canada
    "Coco Gauff": 2060,            # 2023 Cincy champ, Toronto SF, 5-0 vs Andreeva
    "Iga Swiatek": 2055,           # Pre-Toronto final (defending Cincy champ)
    "Mirra Andreeva": 2045,        # 2026 RG champ, rested, 2 WTA 1000 HC titles 2025
    "Jessica Pegula": 2010,        # 2024 Cincy F, 2026 Dubai champ
    "Amanda Anisimova": 1975,
    "Linda Noskova": 1970,         # 2026 Wimbledon champ!
    "Marta Kostyuk": 1965,
    "Elina Svitolina": 1965,       # 40-12 in 2026, Toronto SF fatigue
    "Madison Keys": 1945,
    "Ekaterina Alexandrova": 1945, # Just beat Sabalenka in Toronto
    "Diana Shnaider": 1940,
    "Jelena Ostapenko": 1930,
    "Emma Navarro": 1925,
    "Alexandra Eala": 1925,
    "Iva Jovic": 1920,
    "Elise Mertens": 1910,
    "Sorana Cirstea": 1905,
    "Barbora Krejcikova": 1900,
    "Belinda Bencic": 1865,        # Hip injury WD Toronto
    "Talia Gibson": 1865,          # Hot HC form (2nd wk IW/Miami, beat Chwalinska)
    "Eva Lys": 1855,
    "Emiliana Arango": 1815,       # Clay-leaning, beat 46yo Venus
    "Oleksandra Oliynykova": 1790, # Only 2nd Top-10 match
    "LL_Swiatek": 1830,
    "LL_Rybakina": 1830,
}
# Generic R2/R3 opponents (ranked ~#35-90)
for q in ["Q1", "Q2", "Q3", "Q4"]:
    for s in ["R2a", "R2b", "R2c", "R2d", "R2e", "R2f", "R3a", "R3b", "R3c", "R3d", "R3e", "R3f", "R3g", "R3h"]:
        wta_elo_pre[f"{q}_{s}"] = 1855 if s.startswith("R3") else 1835

wta_h2h = {
    ("Coco Gauff", "Mirra Andreeva"): +65,     # Gauff 5-0 H2H vs Andreeva!
    ("Marta Kostyuk", "Mirra Andreeva"): +20,  # Kostyuk 2-1 H2H vs Andreeva
    ("Iga Swiatek", "Elena Rybakina"): +25,    # Swiatek just crushed Ryb 6-2 6-3 (now 7-6 H2H)
    ("Jelena Ostapenko", "Iga Swiatek"): +45,  # Famous Ostapenko H2H dominance over Swiatek
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

# Pre-Toronto Final baseline check vs DraftKings power de-vig
t_pre = solve_wta(build_wta_draw(False, False), wta_elo_pre)
print("--- Pre-Toronto Final Model vs DraftKings Power De-Vig ---")
for p in ["Aryna Sabalenka", "Elena Rybakina", "Coco Gauff", "Iga Swiatek", "Mirra Andreeva", "Jessica Pegula", "Amanda Anisimova", "Linda Noskova", "Marta Kostyuk", "Elina Svitolina"]:
    dk_p = dk_raw[p] ** k_pow
    print(f"  {p:22s}: model_pre={t_pre[p]:.4f}  dk_power={dk_p:.4f}  dk_prop={dk_raw[p]/total_overround:.4f}")

# Post-Toronto Final update (Aug 14):
# - Swiatek won 6-2, 6-3 in 75 min: +35 Elo form upgrade, -20 Elo back-to-back turnaround drag => net +15 Elo when playing, PLUS 10% late WD risk before R2
# - Rybakina lost 6-2, 6-3 flat/fatigued after 2h33m Osaka + 3-set Gauff + final: -30 Elo fatigue/form drop when playing, PLUS 15% late WD risk before R2
# - Svitolina lost 3-set SF Wed: -10 Elo fatigue
# - Gauff lost 3-set SF Wed (extra Thu+Fri rest): neutral (0)
wta_elo_post = {
    **wta_elo_pre,
    "Iga Swiatek": wta_elo_pre["Iga Swiatek"] + 15,
    "Elena Rybakina": wta_elo_pre["Elena Rybakina"] - 30,
    "Elina Svitolina": wta_elo_pre["Elina Svitolina"] - 10,
}

p_sw_wd = 0.10
p_ry_wd = 0.15
wta_post_blend = {}
for sw_wd, ws in [(False, 1 - p_sw_wd), (True, p_sw_wd)]:
    for ry_wd, wr in [(False, 1 - p_ry_wd), (True, p_ry_wd)]:
        res = solve_wta(build_wta_draw(sw_wd, ry_wd), wta_elo_post)
        for k, v in res.items():
            wta_post_blend[k] = wta_post_blend.get(k, 0.0) + ws * wr * v

print("\n--- Post-Toronto Final WTA Cincinnati Model (sw_wd=10%, ry_wd=15%) ---")
for k, v in sorted(wta_post_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"  {k:22s}: {v:.4f}")

# Sensitivity check: what if Swiatek WD=5% & Rybakina WD=10%, and Swiatek net Elo = +25 (stronger form boost)?
wta_elo_hot = {**wta_elo_post, "Iga Swiatek": wta_elo_pre["Iga Swiatek"] + 25}
wta_hot_blend = {}
for sw_wd, ws in [(False, 0.95), (True, 0.05)]:
    for ry_wd, wr in [(False, 0.90), (True, 0.10)]:
        res = solve_wta(build_wta_draw(sw_wd, ry_wd), wta_elo_hot)
        for k, v in res.items():
            wta_hot_blend[k] = wta_hot_blend.get(k, 0.0) + ws * wr * v

print("\n--- Sensitivity (Swiatek hot +25, sw_wd=5%, ry_wd=10%) ---")
for k, v in sorted(wta_hot_blend.items(), key=lambda x: -x[1])[:8]:
    print(f"  {k:22s}: {v:.4f}")
