import math

# ==============================================================================
# ATP CINCINNATI 2026 — EXACT 96-PLAYER TREE DP (AUG 15 UPDATE)
# Confirmed Results incorporated (Thu Aug 13, Fri Aug 14, Sat Aug 15):
# Q1:
#   R1: Norrie d. Prizmic; Atmane d. Fucsovics; Hurkacz d. LL Shimabukuro 6-2 6-4;
#       Shapovalov d. Mannarino; Struff d. Burruchaga; Navone d. Collignon; Kecmanovic d. Carabelli
#   R2 DONE (Aug 15): Blockx d. Navone 6-3 6-4; Cobolli d. Kecmanovic 6-1 4-6 6-3
# Q2:
#   R1: Tirante d. Choinski; Landaluce d. Draper; Hijikata d. Monfils; Bellucci d. Svajda;
#       Berrettini d. Droguet 3-6 6-2 6-4; Hanfmann d. Q3; Duckworth d. Q4; Halys d. Kopriva
#   R2 DONE (Aug 15): Tirante d. DJOKOVIC 2-6 6-4 6-4!! Landaluce d. Arnaldi 6-4 4-6 6-4!!
# Q3:
#   R1: Michelsen d. de Jong; O'Connell d. Majchrzak; Carreno Busta d. Machac!!
#       Kovacevic d. Khachanov 5-7 6-3 7-6(2)!! Trungelliti d. Medjedovic 7-5 7-6(2)!!
#       Griekspoor WD -> LL vs van de Zandschulp
# Q4:
#   R1: Jaime Faria d. Brooksby 6-3 6-2; Altmaier d. Q11; Baez d. Dimitrov 1-6 6-3 6-4;
#       J.M. Cerundolo d. Q12; Tsitsipas d. Royer 7-6(4) 7-5
# ==============================================================================

def build_atp_draw(shelton_wd=False, nakashima_wd=False):
    q1_tree = (
        (
            (
                ("Alexander Zverev", "Cameron Norrie"),
                ("Terence Atmane", "Tomas Martin Etcheverry"),
            ),
            (
                ("Tommy Paul", "Hubert Hurkacz"),
                (("Qualifier_1", "Adolfo Daniel Vallejo"), "Valentin Vacherot"),
            ),
        ),
        (
            (
                ("Rafael Jodar", "Denis Shapovalov"),
                ("Jan-Lennard Struff", "Alejandro Tabilo"),
            ),
            (
                "Alexander Blockx",
                "Flavio Cobolli",
            ),
        ),
    )

    q2_tree = (
        (
            (
                "Thiago Agustin Tirante",
                "Martin Landaluce",
            ),
            (
                ("Luciano Darderi", "Rinky Hijikata"),
                ("Mattia Bellucci", "Jakub Mensik"),
            ),
        ),
        (
            (
                ("Jiri Lehecka", "Matteo Berrettini"),
                ("Yannick Hanfmann", "Arthur Fils"),
            ),
            (
                ("Arthur Fery", "James Duckworth"),
                ("Quentin Halys", "Alex de Minaur"),
            ),
        ),
    )

    nak_slot = "LuckyLoser_Nak" if nakashima_wd else "Brandon Nakashima"
    q3_tree = (
        (
            (
                ("Taylor Fritz", "Alex Michelsen"),
                (("Daniel Merida", "Marin Cilic"), "Zizou Bergs"),
            ),
            (
                ("Joao Fonseca", ("Botic van de Zandschulp", "LuckyLoser_Griekspoor")),
                ("Christopher O'Connell", "Casper Ruud"),
            ),
        ),
        (
            (
                ("Andrey Rublev", "Pablo Carreno Busta"),
                (("Nuno Borges", "Thanasi Kokkinakis"), "Francisco Cerundolo"),
            ),
            (
                (nak_slot, "Aleksandar Kovacevic"),
                ("Marco Trungelliti", "Daniil Medvedev"),
            ),
        ),
    )

    sh_slot = "LuckyLoser_Sh" if shelton_wd else "Ben Shelton"
    q4_tree = (
        (
            (
                (sh_slot, "Jaime Faria"),
                (("Adam Walton", "Qualifier_9"), "Ignacio Buse"),
            ),
            (
                ("Ugo Humbert", ("Fabian Marozsan", "Qualifier_10")),
                ("Daniel Altmaier", "Lorenzo Musetti"),
            ),
        ),
        (
            (
                ("Learner Tien", "Sebastian Baez"),
                (("Juncheng Shang", "Lorenzo Sonego"), "Frances Tiafoe"),
            ),
            (
                ("Arthur Rinderknech", "Juan Manuel Cerundolo"),
                ("Stefanos Tsitsipas", "Felix Auger-Aliassime"),
            ),
        ),
    )
    return ((q1_tree, q2_tree), (q3_tree, q4_tree))


base_elo = {
    "Alexander Zverev": 2106,
    "Ben Shelton": 2068,            # Won Montreal 10-0 sets; minor turnaround drag baked in vs peak ~2085
    "Taylor Fritz": 2046,           # Lost Montreal R2 to Tirante, rested & healthy
    "Rafael Jodar": 2030,           # Montreal SF, 3d rest
    "Alex de Minaur": 2008,         # #5 seed
    "Daniil Medvedev": 2004,        # #4 seed, bet365 +1800
    "Jakub Mensik": 1988,           # #14 seed, dangerous big server
    "Joao Fonseca": 1982,
    "Felix Auger-Aliassime": 1974,  # Back injury WD Montreal
    "Lorenzo Musetti": 1974,
    "Jiri Lehecka": 1975,
    "Andrey Rublev": 1972,
    "Arthur Fils": 1962,
    "Flavio Cobolli": 1948,         # Won R2 vs Kecmanovic
    "Tommy Paul": 1945,
    "Learner Tien": 1940,
    "Brandon Nakashima": 1938,      # Montreal Finalist (slight fatigue drag vs peak ~1955)
    "Casper Ruud": 1930,
    "Ugo Humbert": 1925,
    "Matteo Berrettini": 1905,
    "Hubert Hurkacz": 1905,         # Routed Shimabukuro 6-2 6-4
    "Alex Michelsen": 1898,         # Beat de Jong; good H2H vs Fritz
    "Valentin Vacherot": 1885,
    "Francisco Cerundolo": 1885,
    "Luciano Darderi": 1878,
    "Stefanos Tsitsipas": 1878,     # Beat Royer
    "Denis Shapovalov": 1872,
    "Frances Tiafoe": 1855,
    "Zizou Bergs": 1855,
    "Alejandro Tabilo": 1850,
    "Cameron Norrie": 1848,
    "Alexander Blockx": 1850,       # Beat Navone 6-3 6-4 -> R3
    "Tomas Martin Etcheverry": 1845,
    "Arthur Rinderknech": 1845,
    "Aleksandar Kovacevic": 1838,   # Beat Khachanov 5-7 6-3 7-6(2) on fast HC!
    "Botic van de Zandschulp": 1835,
    "Fabian Marozsan": 1835,
    "Juncheng Shang": 1835,
    "Ignacio Buse": 1830,
    "Nuno Borges": 1830,
    "Lorenzo Sonego": 1825,
    "Terence Atmane": 1820,
    "Thiago Agustin Tirante": 1820, # Beat Fritz (Montreal) & Djokovic (Cincy)! Ranked #50
    "Arthur Fery": 1815,
    "Thanasi Kokkinakis": 1815,
    "Jan-Lennard Struff": 1812,
    "Quentin Halys": 1810,          # Big server, beat Kopriva
    "Pablo Carreno Busta": 1810,    # Beat Machac!
    "Martin Landaluce": 1810,       # Beat Draper & Arnaldi! -> R3
    "Marin Cilic": 1805,
    "Daniel Merida": 1800,
    "Mattia Bellucci": 1795,
    "Rinky Hijikata": 1790,
    "Christopher O'Connell": 1790,  # Qualified + beat Majchrzak
    "Sebastian Baez": 1790,         # Beat Dimitrov
    "Jaime Faria": 1785,            # Ranked #79, qualified + routed Brooksby 6-3 6-2
    "Daniel Altmaier": 1780,        # Won R1
    "James Duckworth": 1775,        # Won R1
    "Adam Walton": 1770,
    "Yannick Hanfmann": 1770,       # Won R1
    "Marco Trungelliti": 1750,      # 36yo #90 Q, won 2 Q + beat Medjedovic 7-5 7-6(2)!
    "Juan Manuel Cerundolo": 1745,  # Won R1
    "Adolfo Daniel Vallejo": 1730,
    "LuckyLoser_Nak": 1720,
    "LuckyLoser_Sh": 1720,
    "LuckyLoser_Griekspoor": 1720,
    "Qualifier_1": 1730,
    "Qualifier_9": 1730,
    "Qualifier_10": 1730,
}

h2h_deltas = {
    ("Alexander Zverev", "Cameron Norrie"): +55,       # 7-0 H2H
    ("Andrey Rublev", "Pablo Carreno Busta"): +45,     # 4-0 H2H
    ("Andrey Rublev", "Daniil Medvedev"): -35,         # Medvedev ~7-2 H2H
    ("Brandon Nakashima", "Daniil Medvedev"): +15,     # Hot HC form vs Med
    ("Brandon Nakashima", "Aleksandar Kovacevic"): +15,# Won Brisbane SF 2026
    ("Alex Michelsen", "Taylor Fritz"): +15,           # Tennis Tonic shows 2-1 Michelsen
    ("Taylor Fritz", "Daniil Medvedev"): +20,
    ("Joao Fonseca", "Casper Ruud"): +35,
    ("Tommy Paul", "Hubert Hurkacz"): +10,             # 3-2 H2H
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

print("--- Match Win-Prob Sanity Checks (Base) ---")
for a, b in [
    ("Daniil Medvedev", "Marco Trungelliti"),
    ("Brandon Nakashima", "Aleksandar Kovacevic"),
    ("Daniil Medvedev", "Brandon Nakashima"),
    ("Daniil Medvedev", "Aleksandar Kovacevic"),
    ("Andrey Rublev", "Pablo Carreno Busta"),
    ("Daniil Medvedev", "Andrey Rublev"),
    ("Daniil Medvedev", "Francisco Cerundolo"),
    ("Taylor Fritz", "Alex Michelsen"),
    ("Taylor Fritz", "Daniil Medvedev"),
    ("Ben Shelton", "Jaime Faria"),
    ("Alexander Zverev", "Cameron Norrie"),
    ("Rafael Jodar", "Denis Shapovalov"),
]:
    print(f"  P({a} beats {b}) = {win_prob(a, b, base_elo):.3f}")

# Multi-regime blend + small late WD mixture for Montreal finalists (Shelton 6%, Nakashima 8%)
regimes = [
    ("Base", base_elo.copy(), 400.0, 0.50),
    ("Upset-Heat", {**base_elo,
                    "Daniil Medvedev": base_elo["Daniil Medvedev"] - 28,
                    "Marco Trungelliti": base_elo["Marco Trungelliti"] + 20,
                    "Aleksandar Kovacevic": base_elo["Aleksandar Kovacevic"] + 15,
                    "Brandon Nakashima": base_elo["Brandon Nakashima"] - 20, # Montreal fatigue
                    "Ben Shelton": base_elo["Ben Shelton"] - 20,             # Montreal fatigue
                    "Alexander Zverev": base_elo["Alexander Zverev"] - 15}, 420.0, 0.25),
    ("Chalk-HotFinalists", {**base_elo,
                    "Daniil Medvedev": base_elo["Daniil Medvedev"] + 22,
                    "Marco Trungelliti": base_elo["Marco Trungelliti"] - 25,
                    "Brandon Nakashima": base_elo["Brandon Nakashima"] + 20, # Hot form carries over
                    "Ben Shelton": base_elo["Ben Shelton"] + 20,             # Hot form carries over
                    "Alexander Zverev": base_elo["Alexander Zverev"] + 15}, 380.0, 0.25),
]

p_sh_wd = 0.06
p_nak_wd = 0.08

title_blend = {}
med_blend = {}
for rname, elos, sc, rw in regimes:
    r_titles = {}
    r_med = {}
    for sh_wd, ws in [(False, 1 - p_sh_wd), (True, p_sh_wd)]:
        for nak_wd, wn in [(False, 1 - p_nak_wd), (True, p_nak_wd)]:
            tree = build_atp_draw(sh_wd, nak_wd)
            t, el = solve_tree(tree, elos, ["Daniil Medvedev"], scale=sc)
            w_sub = ws * wn
            for k, v in t.items():
                r_titles[k] = r_titles.get(k, 0.0) + w_sub * v
            med_cond = {k: v / (1 - t["Daniil Medvedev"]) for k, v in el["Daniil Medvedev"].items()}
            for k, v in med_cond.items():
                r_med[k] = r_med.get(k, 0.0) + w_sub * v
    print(f"\n[{rname}] TOP 8 TITLE: " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(r_titles.items(), key=lambda x: -x[1])[:8]))
    print(f"[{rname}] MED DEFEAT (MedT={r_titles['Daniil Medvedev']:.3f}): " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(r_med.items(), key=lambda x: -x[1])[:8]))
    for k, v in r_titles.items():
        title_blend[k] = title_blend.get(k, 0.0) + rw * v
    for k, v in r_med.items():
        med_blend[k] = med_blend.get(k, 0.0) + rw * v

print("\n=== FINAL BLENDED Q2 (372528) CINCINNATI ATP CHAMPION TOP 12 ===")
for k, v in sorted(title_blend.items(), key=lambda x: -x[1])[:12]:
    print(f"  {k:26s}: {v:.4f}")

print("\n=== FINAL BLENDED Q1 (418046) MEDVEDEV DEFEATER TOP 10 ===")
for k, v in sorted(med_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"  {k:26s}: {v:.4f}")
