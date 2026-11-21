import math
from collections import defaultdict

def win_prob(p1, p2, elos, scale, h2h=None):
    diff = elos[p1] - elos[p2]
    if h2h:
        if (p1, p2) in h2h: diff += h2h[(p1, p2)]
        elif (p2, p1) in h2h: diff -= h2h[(p2, p1)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def bracket_dp(tree, elos, scale, h2h=None):
    if isinstance(tree, str): return {tree: 1.0}
    L = bracket_dp(tree[0], elos, scale, h2h)
    R = bracket_dp(tree[1], elos, scale, h2h)
    out = defaultdict(float)
    for p1, pr1 in L.items():
        for p2, pr2 in R.items():
            w1 = win_prob(p1, p2, elos, scale, h2h)
            out[p1] += pr1 * pr2 * w1
            out[p2] += pr1 * pr2 * (1.0 - w1)
    return dict(out)

# ============================================================
# 1. WOMEN'S REALISTIC FUNDAMENTAL + MARKET CALIBRATED ELO (scale=400)
# ============================================================
# Calibrate directly to realistic match-level tennis probs + DK Predictions Sep 5 AM!
welos = {
    "Aryna Sabalenka": 2110,     # #1 defending 2x champ, 6-0 sets, 16 straight US Open wins
    "Coco Gauff": 2085,          # #4 2023 champ, Cincy champ, beat Badosa & Bucsa
    "Iga Swiatek": 2050,         # #8 2022 champ, Toronto champ, tight 7-6 7-6 vs Bouzkova
    "Elena Rybakina": 2025,      # #2 AO 2026 champ, sharp R1-R2 but ankle & Starodubtseva R3
    "Jessica Pegula": 1995,      # #3 2024 finalist, top-half soft draw
    "Mirra Andreeva": 1990,      # #5 2026 RG champ, beat Bartunkova, plays Potapova R4!
    "Naomi Osaka": 1965,         # #13 2x US Open champ, plays Mertens R3
    "Linda Noskova": 1945,       # #6 plays Kostyuk R4
    "Marta Kostyuk": 1935,       # #11 plays Noskova R4
    "Amanda Anisimova": 1950,    # (pre-sat)
    "Madison Keys": 1925,        # (pre-sat)
    "Zheng Qinwen": 1925,        # Olympic champ, beat Keys from 0-5 down, plays Swiatek R4
    "Alexandra Eala": 1925,      # #17, 10-2 summer hard, Wash champ, 0-2 vs Jovic
    "Iva Jovic": 1915,           # #14, 2-0 vs Eala this year
    "Emma Navarro": 1920,        # #26 beat Muchova, 2024 SF
    "Anna Kalinskaya": 1895,     # #21 beat Svitolina
    "Elise Mertens": 1875,       # #23 plays Osaka
    "Anastasia Potapova": 1875,  # #24 beat Anisimova 6-2 7-5
    "Sorana Cirstea": 1850,      # #16 beat Paolini 6-3 6-3
    "Taylor Townsend": 1830,     # #96 beat Shnaider
    "Marie Bouzkova": 1855,      # (pre-sat)
    "Yuliia Starodubtseva": 1820,# beat Rybakina at RG
    "Cristina Bucsa": 1810,      # (pre-sat)
    "Nikola Bartunkova": 1795,   # (pre-sat)
}
wh2h = {
    ("Iva Jovic", "Alexandra Eala"): 25,
    ("Yuliia Starodubtseva", "Elena Rybakina"): 25,
    ("Naomi Osaka", "Elise Mertens"): 25,
    ("Aryna Sabalenka", "Taylor Townsend"): 25,
}
w_pre = (
    ((("Aryna Sabalenka", "Taylor Townsend"), ("Marta Kostyuk", "Linda Noskova")),
     (("Jessica Pegula", "Sorana Cirstea"), ("Anna Kalinskaya", "Emma Navarro"))),
    (((("Mirra Andreeva", "Nikola Bartunkova"), ("Anastasia Potapova", "Amanda Anisimova")),
      (("Coco Gauff", "Cristina Bucsa"), ("Iva Jovic", "Alexandra Eala"))),
     ((("Iga Swiatek", "Marie Bouzkova"), ("Zheng Qinwen", "Madison Keys")),
      (("Naomi Osaka", "Elise Mertens"), ("Elena Rybakina", "Yuliia Starodubtseva"))))
)
w_post = (
    ((("Aryna Sabalenka", "Taylor Townsend"), ("Marta Kostyuk", "Linda Noskova")),
     (("Jessica Pegula", "Sorana Cirstea"), ("Anna Kalinskaya", "Emma Navarro"))),
    ((("Mirra Andreeva", "Anastasia Potapova"),
      ("Coco Gauff", ("Iva Jovic", "Alexandra Eala"))),
     (("Iga Swiatek", "Zheng Qinwen"),
      (("Naomi Osaka", "Elise Mertens"), ("Elena Rybakina", "Yuliia Starodubtseva"))))
)

print("=== WOMEN'S REALISTIC MATCHUPS ===")
for a, b in [
    ("Aryna Sabalenka", "Taylor Townsend"),
    ("Aryna Sabalenka", "Linda Noskova"),
    ("Aryna Sabalenka", "Jessica Pegula"),
    ("Aryna Sabalenka", "Coco Gauff"),
    ("Aryna Sabalenka", "Iga Swiatek"),
    ("Jessica Pegula", "Sorana Cirstea"),
    ("Coco Gauff", "Alexandra Eala"),
    ("Coco Gauff", "Mirra Andreeva"),
    ("Mirra Andreeva", "Anastasia Potapova"),
    ("Iva Jovic", "Alexandra Eala"),
    ("Iga Swiatek", "Zheng Qinwen"),
    ("Iga Swiatek", "Elena Rybakina"),
    ("Elena Rybakina", "Yuliia Starodubtseva"),
    ("Naomi Osaka", "Elise Mertens"),
]:
    print(f"  {a:22s} vs {b:22s}: {win_prob(a,b,welos,400,wh2h):.3f}")

wp_pre = bracket_dp(w_pre, welos, 400, wh2h)
wp_post = bracket_dp(w_post, welos, 400, wh2h)
print("\n=== WOMEN'S TITLE DP (REALISTIC MATCHUPS) ===")
for p, v in sorted(wp_post.items(), key=lambda x: -x[1])[:12]:
    print(f"  {p:22s}: pre_sat={wp_pre[p]:.4f} -> POST_SAT={v:.4f}")
print(f"  Top-5 post sum = {sum(v for _, v in sorted(wp_post.items(), key=lambda x: -x[1])[:5]):.4f}")

# ============================================================
# 2. MEN'S #5 SLOT & REALISTIC FUNDAMENTAL + MARKET CHECK (scale=400)
# ============================================================
melos = {
    "Carlos Alcaraz": 2215,
    "Alexander Zverev": 2065,    # fatigued after 9h26m
    "Ben Shelton": 2015,         # Montreal champ, 54 UEs vs Shapo
    "Daniil Medvedev": 2005,     # 9-0 sets, 2021 champ
    "Taylor Fritz": 2005,        # (pre-sat)
    "Frances Tiafoe": 1925,      # 2x US Open SF, beat Vacherot 3-0
    "Learner Tien": 1915,        # #14, 0 sets dropped, Canada SF
    "Jakub Mensik": 1910,        # #17, Miami champ
    "Karen Khachanov": 1905,     # beat #3 FAA & Bonzi 3-0, 2022 US Open SF
    "Alex Michelsen": 1895,      # 9-0 sets, beat Nakashima & Merida 3-0
    "Tommy Paul": 1900,          # #20, beat Bublik in 5
    "Stefanos Tsitsipas": 1895,  # beat Fils & Lehecka
    "Francisco Cerundolo": 1885, # #24, beat Fritz from 0-2 down
    "Flavio Cobolli": 1885,      # (pre-sat)
    "Alexander Blockx": 1860,    # #28, beat Cobolli in 4
    "Lorenzo Musetti": 1865,     # (pre-sat)
    "Luciano Darderi": 1840,     # #21, beat Musetti 3-0
    "Alejandro Tabilo": 1845,    # #25, lefty, plays Zverev
    "Tomas Martin Etcheverry": 1825, # #27, beat Navone 3-0
    "Botic van de Zandschulp": 1840, # crushed De Minaur 3-0
    "Zizou Bergs": 1825,
    "Michael Zheng": 1785,
    "Arthur Gea": 1770,
    "Benjamin Bonzi": 1790,
}
mh2h = {
    ("Carlos Alcaraz", "Tommy Paul"): 40,
    ("Carlos Alcaraz", "Ben Shelton"): 20,
    ("Daniil Medvedev", "Frances Tiafoe"): 25,
}
m_pre = (
    (((("Alexander Zverev", "Alejandro Tabilo"), ("Luciano Darderi", "Lorenzo Musetti")),
      (("Michael Zheng", "Arthur Gea"), ("Zizou Bergs", "Botic van de Zandschulp"))),
     ((("Karen Khachanov", "Benjamin Bonzi"), ("Jakub Mensik", "Learner Tien")),
      (("Francisco Cerundolo", "Taylor Fritz"), ("Alexander Blockx", "Flavio Cobolli")))),
    ((("Daniil Medvedev", "Frances Tiafoe"), ("Alex Michelsen", "Tomas Martin Etcheverry")),
     (("Ben Shelton", "Stefanos Tsitsipas"), ("Tommy Paul", "Carlos Alcaraz")))
)
m_post = (
    (((("Alexander Zverev", "Alejandro Tabilo"), "Luciano Darderi"),
      (("Michael Zheng", "Arthur Gea"), ("Zizou Bergs", "Botic van de Zandschulp"))),
     (("Karen Khachanov", ("Jakub Mensik", "Learner Tien")),
      ("Francisco Cerundolo", "Alexander Blockx"))),
    ((("Daniil Medvedev", "Frances Tiafoe"), ("Alex Michelsen", "Tomas Martin Etcheverry")),
     (("Ben Shelton", "Stefanos Tsitsipas"), ("Tommy Paul", "Carlos Alcaraz")))
)

print("\n=== MEN'S REALISTIC MATCHUPS ===")
for a, b in [
    ("Carlos Alcaraz", "Tommy Paul"),
    ("Carlos Alcaraz", "Ben Shelton"),
    ("Carlos Alcaraz", "Daniil Medvedev"),
    ("Carlos Alcaraz", "Alexander Zverev"),
    ("Alexander Zverev", "Alejandro Tabilo"),
    ("Alexander Zverev", "Luciano Darderi"),
    ("Ben Shelton", "Stefanos Tsitsipas"),
    ("Daniil Medvedev", "Frances Tiafoe"),
    ("Alex Michelsen", "Tomas Martin Etcheverry"),
    ("Learner Tien", "Jakub Mensik"),
    ("Learner Tien", "Karen Khachanov"),
    ("Karen Khachanov", "Francisco Cerundolo"),
    ("Francisco Cerundolo", "Alexander Blockx"),
]:
    print(f"  {a:22s} vs {b:22s}: {win_prob(a,b,melos,400,mh2h):.3f}")

mp_pre = bracket_dp(m_pre, melos, 400, mh2h)
mp_post = bracket_dp(m_post, melos, 400, mh2h)
print("\n=== MEN'S TITLE DP (REALISTIC MATCHUPS) ===")
for p, v in sorted(mp_post.items(), key=lambda x: -x[1])[:12]:
    print(f"  {p:22s}: pre_sat={mp_pre[p]:.4f} -> POST_SAT={v:.4f}")
print(f"  Top-5 post sum = {sum(v for _, v in sorted(mp_post.items(), key=lambda x: -x[1])[:5]):.4f}")
