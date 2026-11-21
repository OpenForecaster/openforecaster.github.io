import math

# ==============================================================================
# CINCINNATI OPEN 2026 EXACT TREE DP — MONDAY AUG 17 UPDATE
# Covers:
#   1) 418046: If Daniil Medvedev loses at Cincinnati 2026, who defeats him?
#   2) 372528: Who will win ATP Cincinnati 2026 men's singles?
#   3) 260735: Who will win WTA Cincinnati 2026 women's singles?
# ==============================================================================

def build_atp_draw_aug17(alt_q12=False):
    # All 16 ATP R3 matchups confirmed (R2 100% completed through Mon Aug 17)!
    # alt_q12=False uses verified Aug 15/16 & TennisPeople results (Vallejo, Landaluce)
    # alt_q12=True checks Tennis Majors table swap (Vacherot, Arnaldi) for sensitivity
    q1 = (
        (
            ("Alexander Zverev", "Terence Atmane"),
            ("Tommy Paul", "Valentin Vacherot" if alt_q12 else "Adolfo Daniel Vallejo"),
        ),
        (
            ("Rafael Jodar", "Alejandro Tabilo"),
            ("Alexander Blockx", "Flavio Cobolli"),
        ),
    )
    q2 = (
        (
            ("Thiago Agustin Tirante", "Matteo Arnaldi" if alt_q12 else "Martin Landaluce"),
            ("Rinky Hijikata", "Jakub Mensik"),
        ),
        (
            ("Jiri Lehecka", "Arthur Fils"),
            ("Arthur Fery", "Alex de Minaur"),
        ),
    )
    q3 = (
        (
            ("Taylor Fritz", "Daniel Merida"),
            ("Joao Fonseca", "Christopher O'Connell"),
        ),
        (
            ("Andrey Rublev", "Nuno Borges"),
            ("Brandon Nakashima", "Daniil Medvedev"),
        ),
    )
    q4 = (
        (
            ("Jaime Faria", "Adam Walton"),
            ("Michael Zheng", "Lorenzo Musetti"),
        ),
        (
            ("Learner Tien", "Frances Tiafoe"),
            ("Juan Manuel Cerundolo", "Felix Auger-Aliassime"),
        ),
    )
    return ((q1, q2), (q3, q4))

atp_elo = {
    "Alexander Zverev": 2105,
    "Taylor Fritz": 2056,           # Clean 6-3 6-4 over Michelsen; Bergs out!
    "Rafael Jodar": 2026,           # bet365 +1100, Montreal SF; beat Shapo 7-5 4-6 7-5
    "Alex de Minaur": 2005,         # Survived Halys 1-6 6-3 7-6(4); Q2 wide open
    "Daniil Medvedev": 2002,        # Rallied 6-4 7-5 vs Trungelliti; 3-0 H2H vs Nakashima
    "Felix Auger-Aliassime": 1998,  # #2 seed, beat Tsitsipas 6-3 7-5 (healthy!), Q4 wide open!
    "Joao Fonseca": 1988,           # Beat Botic 6-4 7-6(2), faces O'Connell
    "Jakub Mensik": 1986,           # Survived Bellucci in 3
    "Andrey Rublev": 1980,          # Beat PCB 7-6(5) 6-1; 5-0 H2H vs Borges!
    "Lorenzo Musetti": 1978,        # Beat Altmaier 6-4 6-2 cleanly; cakewalk R3/R16!
    "Jiri Lehecka": 1976,           # Beat Berrettini in 3
    "Arthur Fils": 1966,            # Beat Van Assche/Hanfmann cleanly; leads Lehecka 3-2
    "Brandon Nakashima": 1952,      # Montreal F + crisp 6-2 7-5 over Kovacevic (1h21m, zero hangover!)
    "Tommy Paul": 1950,             # Beat Hurkacz in 3
    "Flavio Cobolli": 1950,         # Beat Kecmanovic in 3
    "Learner Tien": 1948,           # Beat Baez 6-3 7-6(4)
    "Frances Tiafoe": 1882,         # Blitzed Sonego 6-3 6-4 (healthy!)
    "Valentin Vacherot": 1885,
    "Matteo Arnaldi": 1880,
    "Alejandro Tabilo": 1855,
    "Alexander Blockx": 1852,
    "Nuno Borges": 1848,            # Beat F. Cerundolo 6-4 6-4
    "Thiago Agustin Tirante": 1835, # Upset Djokovic
    "Terence Atmane": 1830,
    "Daniel Merida": 1825,          # Upset #30 Bergs 6-3 6-2
    "Martin Landaluce": 1820,
    "Arthur Fery": 1820,
    "Jaime Faria": 1815,            # Upset #8 Shelton 6-4 6-4!
    "Michael Zheng": 1810,          # Upset #24 Humbert 6-4 6-3!
    "Rinky Hijikata": 1805,
    "Christopher O'Connell": 1800,
    "Adam Walton": 1795,            # Beat #29 Buse 6-4 6-3
    "Adolfo Daniel Vallejo": 1785,
    "Juan Manuel Cerundolo": 1775,  # Beat Rinderknech in 3; clay specialist
}

atp_h2h = {
    ("Daniil Medvedev", "Brandon Nakashima"): +22,     # VERIFIED 3-0 H2H (2-0 hard)! Tempered for Nakashima 2026 breakout form
    ("Andrey Rublev", "Nuno Borges"): +40,             # VERIFIED 5-0 H2H!
    ("Daniil Medvedev", "Andrey Rublev"): +32,         # Medvedev leads career H2H ~7-2
    ("Taylor Fritz", "Daniil Medvedev"): +20,          # Fritz strong recent HC matchup vs Medvedev
    ("Arthur Fils", "Jiri Lehecka"): +18,              # Fils leads 3-2 H2H
    ("Alexander Zverev", "Terence Atmane"): +10,       # 1-0 H2H
    ("Felix Auger-Aliassime", "Juan Manuel Cerundolo"): +25, # Massive fast-HC edge over clay specialist
}

def atp_win(a, b, elos, h2h, scale=400.0):
    diff = elos[a] - elos[b]
    if (a, b) in h2h:
        diff += h2h[(a, b)]
    elif (b, a) in h2h:
        diff -= h2h[(b, a)]
    return 1.0 / (1.0 + 10.0 ** (-diff / scale))

def solve_atp(tree, elos, h2h, targets, scale=400.0):
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
                pab = atp_win(a, b, elos, h2h, scale)
                wa += pb * pab
                if a in elim:
                    elim[a][b] = elim[a].get(b, 0.0) + pa * pb * (1.0 - pab)
                if b in elim:
                    elim[b][a] = elim[b].get(a, 0.0) + pa * pb * pab
            out[a] = pa * wa
        for b, pb in dr.items():
            out[b] = pb * sum(pa * atp_win(b, a, elos, h2h, scale) for a, pa in dl.items())
        return out
    return rec(tree), elim

print("=== KEY ATP MATCHUP PROBS (BASE) ===")
for a, b in [
    ("Daniil Medvedev", "Brandon Nakashima"),
    ("Andrey Rublev", "Nuno Borges"),
    ("Daniil Medvedev", "Andrey Rublev"),
    ("Taylor Fritz", "Daniel Merida"),
    ("Joao Fonseca", "Christopher O'Connell"),
    ("Taylor Fritz", "Joao Fonseca"),
    ("Taylor Fritz", "Daniil Medvedev"),
    ("Felix Auger-Aliassime", "Juan Manuel Cerundolo"),
    ("Alexander Zverev", "Terence Atmane"),
]:
    print(f"  P({a} d. {b}) = {atp_win(a, b, atp_elo, atp_h2h):.3f}")

# Multi-regime blend for ATP (captures H2H weight, Nakashima hot form vs fatigue, FAA health)
atp_regimes = [
    ("Base", atp_elo.copy(), atp_h2h.copy(), 400.0, 0.50),
    ("Nak-Hot / Med-Flat", {**atp_elo,
                            "Daniil Medvedev": atp_elo["Daniil Medvedev"] - 18,
                            "Brandon Nakashima": atp_elo["Brandon Nakashima"] + 20,
                            "Felix Auger-Aliassime": atp_elo["Felix Auger-Aliassime"] + 18},
     {**atp_h2h, ("Daniil Medvedev", "Brandon Nakashima"): +8}, 410.0, 0.25),
    ("Chalk / H2H-Strong", {**atp_elo,
                            "Daniil Medvedev": atp_elo["Daniil Medvedev"] + 15,
                            "Brandon Nakashima": atp_elo["Brandon Nakashima"] - 15,
                            "Felix Auger-Aliassime": atp_elo["Felix Auger-Aliassime"] - 15},
     {**atp_h2h, ("Daniil Medvedev", "Brandon Nakashima"): +35}, 390.0, 0.25),
]

tree_atp = build_atp_draw_aug17(alt_q12=False)
med_blend = {}
title_blend = {}
print("\n=== ATP REGIMES ===")
for rname, elos, h2h, sc, rw in atp_regimes:
    t, el = solve_atp(tree_atp, elos, h2h, ["Daniil Medvedev"], scale=sc)
    mc = {k: v / (1.0 - t["Daniil Medvedev"]) for k, v in el["Daniil Medvedev"].items()}
    print(f"  [{rname}] MedTitle={t['Daniil Medvedev']:.3f} | Defeater: " +
          ", ".join(f"{k}:{v:.3f}" for k, v in sorted(mc.items(), key=lambda x: -x[1])[:6]))
    print(f"             Title:    " +
          ", ".join(f"{k}:{v:.3f}" for k, v in sorted(t.items(), key=lambda x: -x[1])[:8]))
    for k, v in mc.items():
        med_blend[k] = med_blend.get(k, 0.0) + rw * v
    for k, v in t.items():
        title_blend[k] = title_blend.get(k, 0.0) + rw * v

print("\n=== FINAL BLEND Q1 (418046) MEDVEDEV DEFEATER TOP 10 ===")
for k, v in sorted(med_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"  {k:26s}: {v:.4f}")
print(f"  Top-5 sum = {sum(v for _, v in sorted(med_blend.items(), key=lambda x: -x[1])[:5]):.4f}")

print("\n=== FINAL BLEND Q2 (372528) ATP CINCINNATI CHAMPION TOP 12 ===")
for k, v in sorted(title_blend.items(), key=lambda x: -x[1])[:12]:
    print(f"  {k:26s}: {v:.4f}")
print(f"  Top-5 sum = {sum(v for _, v in sorted(title_blend.items(), key=lambda x: -x[1])[:5]):.4f}")

# Check sensitivity if Tennis Majors alt_q12 (Vacherot/Arnaldi) were right
t_alt, _ = solve_atp(build_atp_draw_aug17(alt_q12=True), atp_elo, atp_h2h, ["Daniil Medvedev"])
print("\n[Sens alt_q12] Title top 6: " + ", ".join(f"{k}:{v:.4f}" for k, v in sorted(t_alt.items(), key=lambda x: -x[1])[:6]))

# ==============================================================================
# PART 2: Q4 (260735) — WTA CINCINNATI EXACT TREE DP (AUG 17!)
# ALL R2 100% DONE + 2 R3 MATCHES DONE (Swiatek d. Sakkari, Parry d. Boisson)!
# ==============================================================================
def build_wta_draw_aug17():
    q1 = (
        (
            ("Aryna Sabalenka", "Xinyu Wang"),
            ("Sara Bejlek", "Ekaterina Alexandrova"),
        ),
        (
            ("Katerina Siniakova", "Madison Keys"),
            ("Xiyu Wang", "Elina Svitolina"),
        ),
    )
    q2 = (
        (
            ("Coco Gauff", "Ann Li"),
            ("Marie Bouzkova", "Iva Jovic"),
        ),
        (
            ("Marta Kostyuk", "Sloane Stephens"),
            ("Janice Tjen", "Mirra Andreeva"),
        ),
    )
    q3 = (
        (
            ("Linda Noskova", "Clara Tauson"),
            ("Alexandra Eala", "Amanda Anisimova"),
        ),
        (
            ("Sorana Cirstea", "Anna Kalinskaya"),
            ("Emma Navarro", "Jessica Pegula"),
        ),
    )
    q4 = (
        # SWIATEK AND PARRY ALREADY IN ROUND OF 16!! (WON R3 ON MONDAY AUG 17!)
        ("Iga Swiatek", "Diane Parry"),
        (
            ("Diana Shnaider", "Maja Chwalinska"),
            ("Magdalena Frech", "Elena Rybakina"),
        ),
    )
    return ((q1, q2), (q3, q4))

wta_elo = {
    "Aryna Sabalenka": 2168,        # Survived Gibson 6-2 7-6(2) on 6th MP in wind ("super tired")
    "Iga Swiatek": 2088,            # 8-match streak, beat Sakkari 4-6 6-1 6-1 -> ALREADY IN R16 vs Parry!!
    "Coco Gauff": 2060,             # Beat Samsonova 2-6 6-4 6-1 (stormed last 5 games!), 5-0 vs Andreeva
    "Mirra Andreeva": 2058,         # Crushed Oliynykova 6-1 6-0, fresh; faces tired Tjen
    "Elena Rybakina": 2055,         # Beat Townsend 6-3 6-4, Ostapenko OUT
    "Jessica Pegula": 2015,         # Beat Waltert 6-3 6-2
    "Amanda Anisimova": 1978,       # Beat Sonmez 6-2 6-3
    "Linda Noskova": 1975,          # Beat Boulter 6-3 6-3
    "Marta Kostyuk": 1962,          # Survived Kenin in 3
    "Ekaterina Alexandrova": 1945,  # Survived Blinkova in 3
    "Madison Keys": 1945,           # Survived Snigur in 3
    "Elina Svitolina": 1945,        # Saved 7 MPs vs Valentova (huge fatigue after Toronto SF!)
    "Diana Shnaider": 1942,
    "Alexandra Eala": 1938,
    "Emma Navarro": 1925,
    "Anna Kalinskaya": 1925,
    "Iva Jovic": 1922,              # Beat Korpatsch 6-4 6-3
    "Katerina Siniakova": 1910,
    "Marie Bouzkova": 1905,
    "Sorana Cirstea": 1905,
    "Xinyu Wang": 1895,             # Beat #31 Vekic in 3
    "Clara Tauson": 1892,           # Back pain vs Stearns
    "Ann Li": 1885,                 # #28 seed, beat Zhang Shuai
    "Maja Chwalinska": 1885,
    "Magdalena Frech": 1875,        # Beat Ostapenko 6-1 6-3
    "Sara Bejlek": 1865,            # Beat Krejcikova
    "Xiyu Wang": 1865,              # Beat Fernandez
    "Sloane Stephens": 1860,        # Beat #24 Potapova 6-2 6-4
    "Janice Tjen": 1850,            # Exhausting 7-6 5-7 7-5 vs Golubic
    "Diane Parry": 1845,            # Unseeded, two straight 3-setters (Mertens, Boisson)
}

wta_h2h = {
    ("Coco Gauff", "Mirra Andreeva"): +65,     # 5-0 H2H!
    ("Marta Kostyuk", "Mirra Andreeva"): +20,  # 2-1 H2H
    ("Iga Swiatek", "Elena Rybakina"): +25,    # Crushed Ryb 6-2 6-3 in Toronto F
    ("Iga Swiatek", "Diana Shnaider"): +25,    # Beat her 6-2 6-1 in Toronto QF
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

tree_wta = build_wta_draw_aug17()
print("\n=== PART 2: Q4 (260735) WTA CINCINNATI CHAMPION (AUG 17!) ===")
res_wta_base = solve_wta(tree_wta, wta_elo, 400.0)
elo_wta_fat = {**wta_elo, "Iga Swiatek": wta_elo["Iga Swiatek"] - 22, "Elena Rybakina": wta_elo["Elena Rybakina"] - 20}
res_wta_fat = solve_wta(tree_wta, elo_wta_fat, 400.0)
elo_wta_swi_hot = {**wta_elo, "Iga Swiatek": wta_elo["Iga Swiatek"] + 15, "Aryna Sabalenka": wta_elo["Aryna Sabalenka"] - 15}
res_wta_hot = solve_wta(tree_wta, elo_wta_swi_hot, 400.0)

for nm, r in [("Base", res_wta_base), ("Toronto-Fatigue", res_wta_fat), ("Swiatek-Hot/Saba-Tired", res_wta_hot)]:
    print(f"  [{nm}] " + ", ".join(f"{k}:{v:.4f}" for k, v in sorted(r.items(), key=lambda x: -x[1])[:7]))

wta_blend = {k: 0.55 * res_wta_base[k] + 0.30 * res_wta_fat[k] + 0.15 * res_wta_hot[k] for k in res_wta_base}
print("\n=== FINAL BLEND Q4 (260735) WTA CINCINNATI TOP 10 ===")
for k, v in sorted(wta_blend.items(), key=lambda x: -x[1])[:10]:
    print(f"  {k:26s}: {v:.4f}")
print(f"  Top-5 sum = {sum(v for _, v in sorted(wta_blend.items(), key=lambda x: -x[1])[:5]):.4f}")
