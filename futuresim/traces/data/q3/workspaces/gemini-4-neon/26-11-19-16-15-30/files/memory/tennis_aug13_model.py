import math
import random
from collections import Counter

# ==============================================================================
# PART 1: EXACT 96-PLAYER ATP CINCINNATI OPEN TREE DP (AUG 13 UPDATE)
# Updates vs Aug 12:
#   - Jack Draper LOST R1 to Martin Landaluce (6-3, 7-5) -> Landaluce in R2 vs Arnaldi!
#   - Dino Prizmic LOST R1 to Cameron Norrie (3-6, 6-1, 6-4) -> Norrie in R2 vs Zverev!
#   - Brandon Nakashima & Ben Shelton reached Montreal Final (Thu Aug 13 8pm EST):
#       * Model WD-to-Lucky-Loser risk (Shelton ~15%, Nakashima ~20%) + turnaround fatigue
#         vs upgraded true fast-HC skill (Shelton 10-0 sets, Nakashima beat Darderi & Jodar).
#   - Calibrate against 3 live books: BetMGM (Aug 13), bet365 (Aug 12), 1xBet (Aug 12).
# ==============================================================================

def build_draw(shelton_wd=False, nakashima_wd=False):
    q1_tree = (
        (
            (
                ("Alexander Zverev", "Cameron Norrie"),  # Norrie d. Prizmic Aug 13!
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
                ("Martin Landaluce", "Matteo Arnaldi"),  # Landaluce d. Draper 6-3 7-5 Aug 13!
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

    nak_slot = "LuckyLoser_Nak" if nakashima_wd else "Brandon Nakashima"
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


# Base Elo calibrated to consensus of BetMGM (Aug 13), bet365 (Aug 12), 1xBet (Aug 12)
# Vig-free consensus targets:
#   Zverev: BetMGM 16.7%, bet365 16.9%, 1xBet 15.0% -> ~16.3%
#   Djokovic: BetMGM 12.0%, bet365 12.1%, 1xBet 5.6% -> ~10.2% (weighted 70% US/UK + 30% 1xBet; boosted slightly by Draper exit)
#   Fritz: BetMGM 9.3%, bet365 8.5%, 1xBet 9.2% -> ~9.1%
#   Shelton: BetMGM 8.4%, bet365 10.6%, 1xBet 6.9% -> ~8.7% (reflecting ~15% WD + slight fatigue vs blistering form!)
#   Jodar: BetMGM 5.6%, bet365 7.1%, 1xBet 8.3% -> ~6.8%
#   Medvedev: bet365 4.5%, 1xBet 5.6% -> ~4.8%
#   De Minaur: 1xBet 4.2% -> ~4.4%
#   FAA: bet365 3.7%, 1xBet 5.6% -> ~4.0%

base_elo = {
    "Alexander Zverev": 2106,
    "Novak Djokovic": 2070,         # Slightly toned down from 2088 to reflect 1xBet 15.00 / age-rust, still ~10.8% title after Draper exit
    "Ben Shelton": 2060,            # When playing (post-15% WD mixture -> ~8.8% title)
    "Taylor Fritz": 2052,           # Rested, healthy quote, ~9.2% title
    "Rafael Jodar": 2030,           # Rested 3d after Montreal SF, ~6.7% title
    "Alex de Minaur": 2005,
    "Daniil Medvedev": 2004,
    "Felix Auger-Aliassime": 1978,
    "Joao Fonseca": 1982,
    "Lorenzo Musetti": 1974,
    "Jakub Mensik": 1985,
    "Jiri Lehecka": 1975,
    "Andrey Rublev": 1970,
    "Arthur Fils": 1962,            # 1xBet 15.00
    "Flavio Cobolli": 1945,
    "Tommy Paul": 1945,
    "Learner Tien": 1940,
    "Brandon Nakashima": 1938,      # Form UP (+25 from Montreal F) minus fatigue (-15) when he plays (20% WD modeled explicitly!)
    "Casper Ruud": 1930,
    "Ugo Humbert": 1925,
    "Karen Khachanov": 1918,
    "Tomas Machac": 1915,
    "Matteo Berrettini": 1905,
    "Hubert Hurkacz": 1900,
    "Alex Michelsen": 1890,
    "Tallon Griekspoor": 1885,
    "Valentin Vacherot": 1885,
    "Francisco Cerundolo": 1885,
    "Matteo Arnaldi": 1880,
    "Luciano Darderi": 1878,
    "Stefanos Tsitsipas": 1875,
    "Denis Shapovalov": 1865,
    "Grigor Dimitrov": 1865,
    "Frances Tiafoe": 1855,
    "Zizou Bergs": 1855,
    "Alejandro Tabilo": 1850,
    "Cameron Norrie": 1848,         # Won R1, Montreal R4, Los Cabos SF
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
    "Miomir Kecmanovic": 1820,
    "Arthur Fery": 1815,
    "Thanasi Kokkinakis": 1815,
    "Jan-Lennard Struff": 1810,
    "Corentin Moutet": 1810,
    "Marton Fucsovics": 1805,
    "Marin Cilic": 1805,
    "Gael Monfils": 1805,
    "Daniel Merida": 1800,
    "Martin Landaluce": 1790,       # Upgraded from 1745: World #64, 8-3 in ATP 1000s in 2026, just beat Draper 6-3 7-5!
    "Rinky Hijikata": 1785,
    "Mattia Bellucci": 1785,
    "Adrian Mannarino": 1785,
    "Pablo Carreno Busta": 1785,
    "Sebastian Baez": 1775,
    "Jesper de Jong": 1770,
    "Adam Walton": 1770,
    "Thiago Agustin Tirante": 1765,
    "Zachary Svajda": 1765,
    "Kamil Majchrzak": 1765,
    "Daniel Altmaier": 1765,
    "James Duckworth": 1765,
    "Raphael Collignon": 1765,
    "Yannick Hanfmann": 1760,
    "Vit Kopriva": 1750,
    "Valentin Royer": 1745,
    "Camilo Ugo Carabelli": 1740,
    "Mariano Navone": 1735,
    "Roman Andres Burruchaga": 1735,
    "Adolfo Daniel Vallejo": 1730,
    "Juan Manuel Cerundolo": 1720,
    "Jan Choinski": 1680,
    "LuckyLoser_Nak": 1715,
    "LuckyLoser_Sh": 1715,
}
for i in range(1, 13):
    base_elo[f"Qualifier_{i}"] = 1725

h2h_deltas = {
    ("Jakub Mensik", "Novak Djokovic"): +30,
    ("Alex de Minaur", "Novak Djokovic"): -40,
    ("Taylor Fritz", "Novak Djokovic"): -50,
    ("Alexander Zverev", "Novak Djokovic"): +10,
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

# Mixture over (Shelton WD: 0.16, Nakashima WD: 0.22) x 3 Elo regimes (Base 0.50, Rust-Upset 0.25, Chalk 0.25)
p_sh_wd = 0.16
p_nak_wd = 0.22
wd_scenarios = [
    (False, False, (1 - p_sh_wd) * (1 - p_nak_wd)),
    (True,  False, p_sh_wd * (1 - p_nak_wd)),
    (False, True,  (1 - p_sh_wd) * p_nak_wd),
    (True,  True,  p_sh_wd * p_nak_wd),
]

regimes = [
    ("Base", base_elo.copy(), 400.0, 0.50),
    ("Rust-Upset", {**base_elo, "Novak Djokovic": base_elo["Novak Djokovic"] - 35, "Daniil Medvedev": base_elo["Daniil Medvedev"] - 30, "Martin Landaluce": base_elo["Martin Landaluce"] + 25, "Brandon Nakashima": base_elo["Brandon Nakashima"] + 20}, 420.0, 0.25),
    ("Chalk-Class", {**base_elo, "Novak Djokovic": base_elo["Novak Djokovic"] + 30, "Daniil Medvedev": base_elo["Daniil Medvedev"] + 30, "Martin Landaluce": base_elo["Martin Landaluce"] - 20, "Brandon Nakashima": base_elo["Brandon Nakashima"] - 25}, 380.0, 0.25),
]

title_blend = {}
djoko_blend = {}
med_blend = {}

for sh_wd, nak_wd, w_wd in wd_scenarios:
    tree = build_draw(shelton_wd=sh_wd, nakashima_wd=nak_wd)
    for rname, elos, sc, w_reg in regimes:
        w = w_wd * w_reg
        titles, elims = solve_tree(tree, elos, ["Novak Djokovic", "Daniil Medvedev"], scale=sc)
        for p, v in titles.items():
            title_blend[p] = title_blend.get(p, 0.0) + w * v
        djo_cond = {k: v / (1 - titles["Novak Djokovic"]) for k, v in elims["Novak Djokovic"].items()}
        med_cond = {k: v / (1 - titles["Daniil Medvedev"]) for k, v in elims["Daniil Medvedev"].items()}
        for k, v in djo_cond.items():
            djoko_blend[k] = djoko_blend.get(k, 0.0) + w * v
        for k, v in med_cond.items():
            med_blend[k] = med_blend.get(k, 0.0) + w * v

print("=== Q1 (372528) CINCINNATI WINNER TOP 12 ===")
for k, v in sorted(title_blend.items(), key=lambda x: -x[1])[:12]:
    print(f"  {k:26s}: {v:.4f}")

print("\n=== Q2 (277746) DJOKOVIC DEFEATER TOP 10 (POST-DRAPER LOSS!) ===")
for k, v in sorted(djoko_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"  {k:26s}: {v:.4f}")

print("\n=== Q4 (418046) MEDVEDEV DEFEATER TOP 10 (POST-NAKASHIMA MONTREAL FINAL!) ===")
for k, v in sorted(med_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"  {k:26s}: {v:.4f}")

# Sensitivity check on Q4 if Nakashima WD prob is 0.10 vs 0.22 vs 0.30
for p_n in [0.10, 0.22, 0.35]:
    mb = {}
    for nak_wd, w_n in [(False, 1-p_n), (True, p_n)]:
        tree = build_draw(False, nak_wd)
        for rname, elos, sc, w_reg in regimes:
            titles, elims = solve_tree(tree, elos, ["Daniil Medvedev"], scale=sc)
            mc = {k: v / (1 - titles["Daniil Medvedev"]) for k, v in elims["Daniil Medvedev"].items()}
            for k, v in mc.items():
                mb[k] = mb.get(k, 0.0) + w_n * w_reg * v
    top5 = ", ".join(f"{k}:{v:.3f}" for k, v in sorted(mb.items(), key=lambda x: -x[1])[:6])
    print(f"  [Q4 sens p_nak_wd={p_n:.2f}] {top5}")
