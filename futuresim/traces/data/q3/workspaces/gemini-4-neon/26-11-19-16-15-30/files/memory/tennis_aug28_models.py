import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — FRIDAY AUG 28, 2026 (POST-DRAW! T-2d to US Open Start!)
# Batch: tennis (608158, 408930, 891014)
# EXACT 128-PLAYER FIXED-BRACKET SIMULATIONS + POST-DRAW MARKET CALIBRATION
# ==============================================================================

def shin_devig(dec_odds_dict):
    qs = {k: 1.0 / d for k, d in dec_odds_dict.items()}
    s = sum(qs.values())
    if s <= 1.0:
        return {k: v / s for k, v in qs.items()}, 0.0
    lo, hi = 0.0, 0.9999
    for _ in range(100):
        z = 0.5 * (lo + hi)
        tot = sum((math.sqrt(z*z + 4.0*(1.0 - z)*(q*q)/s) - z) / (2.0*(1.0 - z)) for q in qs.values())
        if tot > 1.0:
            lo = z
        else:
            hi = z
    z = 0.5 * (lo + hi)
    return {k: (math.sqrt(z*z + 4.0*(1.0 - z)*(q*q)/s) - z) / (2.0*(1.0 - z)) for k, q in qs.items()}, z

def power_devig(dec_odds_dict):
    qs = {k: 1.0 / d for k, d in dec_odds_dict.items()}
    lo, hi = 1.0, 3.5
    for _ in range(100):
        k_exp = 0.5 * (lo + hi)
        tot = sum(q ** k_exp for q in qs.values())
        if tot > 1.0:
            lo = k_exp
        else:
            hi = k_exp
    k_exp = 0.5 * (lo + hi)
    return {name: q ** k_exp for name, q in qs.items()}, k_exp

def devig_mid(dec_odds_dict):
    sh, z = shin_devig(dec_odds_dict)
    pw, ke = power_devig(dec_odds_dict)
    ov = sum(1.0 / d for d in dec_odds_dict.values())
    return {k: 0.5 * sh[k] + 0.5 * pw[k] for k in dec_odds_dict}, ov, z, ke

def p_bo3(ea, eb):
    return 1.0 / (1.0 + 10.0 ** (-(ea - eb) / 400.0))

def p_bo5(ea, eb):
    p3 = p_bo3(ea, eb)
    ps = p3
    for _ in range(8):
        f = ps*ps*(3 - 2*ps) - p3
        df = 6*ps*(1 - ps) + 1e-12
        ps = max(1e-6, min(1 - 1e-6, ps - f / df))
    return ps**3 * (10 - 15*ps + 6*ps*ps)


# ==============================================================================
# PART 1: EXACT 128-PLAYER OFFICIAL MEN'S SINGLES BRACKET (spaziotennis.com Aug 27)
# ==============================================================================
# 64 R1 matchups = 128 exact slots (Top half slots 0..63, Bottom half slots 64..127)
atp_bracket_raw = [
    # --- QUARTER 1 (Zverev [1] / Musetti [13] / Jodar [12] / De Minaur [6]) ---
    # Section 1 (Zverev 1)
    "Alexander Zverev", "Lorenzo Sonego",
    "Quentin Halys", "Facundo Diaz Acosta",
    "Q_1", "Alexei Popyrin",
    "Yannick Hanfmann", "Alejandro Tabilo",
    # Section 2 (Musetti 13)
    "Luciano Darderi", "Q_2",
    "Q_3", "Valentin Royer",
    "Dane Sweeny", "Corentin Moutet",
    "Arthur Fery", "Lorenzo Musetti",
    # Section 3 (Jodar 12)
    "Rafael Jodar", "Thanasi Kokkinakis",
    "Fabian Marozsan", "Michael Zheng",
    "Zachary Svajda", "Daniel Altmaier",
    "Juan Manuel Cerundolo", "Casper Ruud",
    # Section 4 (De Minaur 6)
    "Zizou Bergs", "Carlos Taberner",
    "Jesper De Jong", "Q_4",
    "Jan Choinski", "Botic van de Zandschulp",
    "Q_5", "Alex de Minaur",

    # --- QUARTER 2 (Auger-Aliassime [3] / Tien [14] / Fritz [9] / Cobolli [5]) ---
    # Section 5 (Auger-Aliassime 3)
    "Felix Auger-Aliassime", "Rinky Hijikata",
    "Roman Andres Burruchaga", "Karen Khachanov",
    "Alex Molcan", "Benjamin Bonzi",
    "Marcos Giron", "Ignacio Buse",
    # Section 6 (Tien 14)
    "Jakub Mensik", "Q_6",
    "Q_7", "Giovanni Mpetshi Perricard",
    "Adolfo Daniel Vallejo", "Gael Monfils",
    "Nuno Borges", "Learner Tien",
    # Section 7 (Fritz 9)
    "Taylor Fritz", "Darwin Blanch",
    "Mattia Bellucci", "Q_8",
    "Camilo Ugo Carabelli", "Jan-Lennard Struff",
    "Filip Misolic", "Francisco Cerundolo",
    # Section 8 (Cobolli 5)
    "Alexander Blockx", "Q_9",
    "Juncheng Shang", "Marco Trungelliti",
    "Q_10", "Q_11",
    "Francisco Comesana", "Flavio Cobolli",

    # --- QUARTER 3 (Medvedev [7] / Tiafoe [11] / Nakashima [16] / Djokovic [4]) ---
    # Section 9 (Medvedev 7)
    "Daniil Medvedev", "Q_12",
    "Stefan Gorzny", "Raphael Collignon",
    "Jaume Munar", "Terence Atmane",
    "Sho Shimabukuro", "Arthur Rinderknech",
    # Section 10 (Tiafoe 11)
    "Valentin Vacherot", "Aleksandar Kovacevic",
    "Kamil Majchrzak", "Hamad Medjedovic",
    "Aleksandar Vukic", "Q_13",
    "Martin Damm", "Frances Tiafoe",
    # Section 11 (Nakashima 16)
    "Brandon Nakashima", "Sebastian Baez",
    "Alex Michelsen", "Q_14",
    "Daniel Merida", "Marton Fucsovics",
    "Marin Cilic", "Andrey Rublev",
    # Section 12 (Djokovic 4)
    "Tomas Martin Etcheverry", "Vit Kopriva",
    "Martin Landaluce", "Q_15",
    "Matteo Berrettini", "Stan Wawrinka",
    "Mariano Navone", "Novak Djokovic",

    # --- QUARTER 4 (Shelton [8] / Fils [10] / Bublik [15] / Alcaraz [2]) ---
    # Section 13 (Shelton 8)
    "Ben Shelton", "Tallon Griekspoor",
    "Damir Dzumhur", "Hubert Hurkacz",
    "Miomir Kecmanovic", "Denis Shapovalov",
    "Luca Van Assche", "Cameron Norrie",
    # Section 14 (Fils 10)
    "Jiri Lehecka", "Pablo Carreno Busta",
    "Q_16", "Tomas Machac",
    "Q_17", "Jack Kennedy",
    "Stefanos Tsitsipas", "Arthur Fils",
    # Section 15 (Bublik 15)
    "Alexander Bublik", "J.J. Wolf",
    "Thiago Agustin Tirante", "Adrian Mannarino",
    "Dino Prizmic", "Alexander Shevchenko",
    "Q_18", "Tommy Paul",
    # Section 16 (Alcaraz 2)
    "Matteo Arnaldi", "James Duckworth",
    "Yibing Wu", "Adam Walton",
    "Jaime Faria", "Jenson Brooksby",
    "Roman Safiullin", "Carlos Alcaraz",
]
assert len(atp_bracket_raw) == 128, f"Expected 128 ATP slots, got {len(atp_bracket_raw)}"

# Exact US Men in main draw (+2 expected US qualifiers e.g. Basavareddy/Spizzirri assigned to Q_4 & Q_10):
us_men_set = {
    "Taylor Fritz", "Ben Shelton", "Frances Tiafoe", "Learner Tien",
    "Brandon Nakashima", "Tommy Paul",
    "Alex Michelsen", "Marcos Giron", "Zachary Svajda", "Jenson Brooksby",
    "Aleksandar Kovacevic", "Martin Damm", "Darwin Blanch", "J.J. Wolf",
    "Stefan Gorzny", "Jack Kennedy", "Michael Zheng",
    "Q_4", "Q_10",  # ~2 US qualifiers (e.g. Basavareddy/Spizzirri)
}

# Hard-court BO5 base Elo ratings (calibrated to Aug 26 pre-draw talent + confirmed 2026 form)
atp_base_elo = {
    # Top 4
    "Carlos Alcaraz": 2175,       # Mixture below! (Post mixed-doubles rust -> ~26% overall)
    "Alexander Zverev": 2138,     # #1 seed, RG champ + Wim F (18-2 Slams in 2026!)
    "Novak Djokovic": 2102,       # #4 seed, AO F + Wim SF, cut NY practice short -> mixture below
    "Felix Auger-Aliassime": 2010,# #3 seed, 2025 USO SF, FD/Caesars +2200
    # Tier 2 contenders
    "Arthur Fils": 2078,          # #10 seed, Cinci Masters champ (10-0 deciding sets), Kalshi 7%
    "Ben Shelton": 2075,          # #8 seed, Montreal Masters champ, 2023 USO SF
    "Taylor Fritz": 2064,         # #9 seed, 2024 USO F, 2026 DC champ, Kalshi 6% / FD +1100
    "Rafael Jodar": 2052,         # #12 seed, 19yo phenom, Kalshi 5% / FD +1100
    # Tier 3 seeds (1950-2020)
    "Daniil Medvedev": 2005,      # #7 seed, 2021 USO champ, FD +3300
    "Flavio Cobolli": 2000,       # #5 seed, RG F + Cinci SF, FD +3300
    "Jakub Mensik": 2005,         # #17 seed, RG SF + USO Mixed champ, FD +3300
    "Alex de Minaur": 1988,       # #6 seed, FD +5500
    "Frances Tiafoe": 2002,       # #11 seed, 2x USO SF + Cinci F, FD +5000 / Caesars +2500
    "Brandon Nakashima": 1996,    # #16 seed, Montreal F + Cinci SF, FD +5000 / Caesars +4000
    "Tommy Paul": 1988,           # #20 seed, beat Zverev in Cinci, FD +6500 / Caesars +4000
    "Learner Tien": 1978,         # #14 seed, rising lefty
    "Lorenzo Musetti": 1972,      # #13 seed, FD +5500
    "Jiri Lehecka": 1975,         # #18 seed
    "Andrey Rublev": 1972,        # #23 seed
    "Alexander Bublik": 1962,     # #15 seed
    "Casper Ruud": 1945,          # #19 seed
    "Tomas Machac": 1945,
    "Karen Khachanov": 1945,
    "Hubert Hurkacz": 1940,
    "Matteo Berrettini": 1935,
    "Tallon Griekspoor": 1928,
    "Alex Michelsen": 1925,
    "Stefanos Tsitsipas": 1925,
    "Alexei Popyrin": 1920,
    "Denis Shapovalov": 1915,
    "Giovanni Mpetshi Perricard": 1915,
    "Francisco Cerundolo": 1910,  # #24 seed (weaker on fast hard)
    "Cameron Norrie": 1905,       # #29 seed
    "Matteo Arnaldi": 1905,       # #30 seed
    "Arthur Rinderknech": 1900,   # #26 seed
    "Valentin Vacherot": 1898,    # #22 seed
    "Luciano Darderi": 1895,      # #21 seed
    "Alejandro Tabilo": 1895,     # #25 seed
    "Tomas Martin Etcheverry": 1895, # #27 seed
    "Alexander Blockx": 1892,     # #28 seed
    "Zizou Bergs": 1895,          # #31 seed
    "Ignacio Buse": 1885,         # #32 seed
    "Roman Safiullin": 1895,      # Beat Alcaraz Paris 2023
    "Lorenzo Sonego": 1895,
    "Juncheng Shang": 1895,
    "Nuno Borges": 1892,
    "Marcos Giron": 1885,
    "Jenson Brooksby": 1880,
    "Thanasi Kokkinakis": 1885,
    "Fabian Marozsan": 1885,
    "Miomir Kecmanovic": 1885,
    "Botic van de Zandschulp": 1880,
    "Jan-Lennard Struff": 1885,
    "Gael Monfils": 1875,
    "Marin Cilic": 1875,
    "Arthur Fery": 1875,          # Wimbledon SFist!
    "Sebastian Baez": 1865,
    "Flavio Comesana": 1860,
    "Francisco Comesana": 1865,
    "Corentin Moutet": 1865,
    "Quentin Halys": 1865,
    "Adrian Mannarino": 1860,
    "Mattia Bellucci": 1860,
    "Aleksandar Kovacevic": 1858,
    "Aleksandar Vukic": 1855,
    "Hamad Medjedovic": 1865,
    "Marton Fucsovics": 1860,
    "Jaume Munar": 1855,
    "Terence Atmane": 1855,
    "Stan Wawrinka": 1845,
    "Mariano Navone": 1845,
    "Zachary Svajda": 1840,
    "Daniel Altmaier": 1855,
    "Rinky Hijikata": 1845,
    "Benjamin Bonzi": 1855,
    "Pablo Carreno Busta": 1850,
    "Thiago Agustin Tirante": 1855, # Beat Djokovic in Cinci!
    "Dino Prizmic": 1850,
    "Alexander Shevchenko": 1845,
    "J.J. Wolf": 1835,
    "Yibing Wu": 1845,
    "Adam Walton": 1840,
    "Raphael Collignon": 1845,
    "Kamil Majchrzak": 1845,
    "Damir Dzumhur": 1840,
    "Luca Van Assche": 1835,
    "Jesper De Jong": 1840,
    "Yannick Hanfmann": 1840,
    "James Duckworth": 1835,
    "Vit Kopriva": 1835,
    "Camilo Ugo Carabelli": 1835,
    "Filip Misolic": 1835,
    "Juan Manuel Cerundolo": 1825,
    "Facundo Diaz Acosta": 1825,
    "Carlos Taberner": 1815,
    "Roman Andres Burruchaga": 1820,
    "Alex Molcan": 1825,
    "Adolfo Daniel Vallejo": 1820,
    "Marco Trungelliti": 1810,
    "Valentin Royer": 1825,
    "Dane Sweeny": 1810,
    "Jan Choinski": 1815,
    "Sho Shimabukuro": 1820,
    "Daniel Merida": 1815,
    "Martin Landaluce": 1825,
    "Jaime Faria": 1830,
    "Darwin Blanch": 1765,
    "Martin Damm": 1795,
    "Stefan Gorzny": 1765,
    "Jack Kennedy": 1755,
    "Michael Zheng": 1785,
}

def run_fixed_atp_mc(elo_overrides=None, n_trials=60000, seed=2026):
    rng = random.Random(seed)
    elos_base = []
    for nm in atp_bracket_raw:
        if nm.startswith("Q_"):
            el = 1830.0
        else:
            el = float(atp_base_elo.get(nm, 1840.0))
        if elo_overrides and nm in elo_overrides:
            el = float(elo_overrides[nm])
        elos_base.append(el)

    alc_idx = atp_bracket_raw.index("Carlos Alcaraz")
    djo_idx = atp_bracket_raw.index("Novak Djokovic")
    tia_idx = atp_bracket_raw.index("Frances Tiafoe")
    us_idxs = {i for i, nm in enumerate(atp_bracket_raw) if nm in us_men_set}

    # Health / rust mixtures:
    # Alcaraz: rusty in mixed doubles Tue Aug 25, first competitive BO5 singles since April (133d off!)
    #   NearPeak (2270, 0.28), MildRust (2165, 0.44), HeavyRust (2035, 0.24), WD/Re-injury (1750, 0.04)
    alc_mix = [(2270, 0.28), (2165, 0.44), (2035, 0.24), (1750, 0.04)]
    # Djokovic: 39yo, heat/humidity condition in Cinci + cut NY practice short this week
    #   Healthy (2125, 0.55), SlightWear (2065, 0.30), Heat/PhysicalFade (1975, 0.15)
    djo_mix = [(2125, 0.55), (2065, 0.30), (1975, 0.15)]
    # Tiafoe: skipped mixed doubles -> 7d rest after Cinci F leg/back niggle
    tia_mix = [(0, 0.78), (-35, 0.16), (-95, 0.06)]

    title_cnt = Counter()
    final_cnt = Counter()
    sf_cnt = Counter()
    qf_cnt = Counter()
    r4_cnt = Counter()
    uncond_us = Counter()
    tie_rate = 0.0
    us_max_rnd_dist = {nm: Counter() for nm in us_men_set}

    for ae, wa in alc_mix:
        for de, wd in djo_mix:
            for td, wt in tia_mix:
                w = wa * wd * wt
                tr = max(600, int(round(n_trials * w)))
                elos = list(elos_base)
                elos[alc_idx] = float(ae)
                elos[djo_idx] = float(de)
                elos[tia_idx] = elos_base[tia_idx] + float(td)

                pc = {}
                def gp(i, j):
                    k = (elos[i], elos[j])
                    v = pc.get(k)
                    if v is None:
                        v = p_bo5(elos[i], elos[j])
                        pc[k] = v
                    return v

                tc = Counter(); fc = Counter(); sc = Counter(); qc = Counter(); r4c = Counter()
                uc = Counter(); ties = 0
                rm = {i: Counter() for i in us_idxs}

                for _ in range(tr):
                    cur = list(range(128))
                    best_rnd = 0
                    best_us = []
                    rnd = 1
                    while len(cur) > 1:
                        nxt = []
                        if rnd == 4:
                            for p in cur: r4c[p] += 1
                        elif rnd == 5:
                            for p in cur: qc[p] += 1
                        elif rnd == 6:
                            for p in cur: sc[p] += 1
                        elif rnd == 7:
                            for p in cur: fc[p] += 1
                        for k in range(0, len(cur), 2):
                            a, b = cur[k], cur[k+1]
                            if rng.random() < gp(a, b):
                                win, los = a, b
                            else:
                                win, los = b, a
                            nxt.append(win)
                            if los in us_idxs:
                                rm[los][rnd] += 1
                                if rnd > best_rnd:
                                    best_rnd = rnd
                                    best_us = [los]
                                elif rnd == best_rnd:
                                    best_us.append(los)
                        cur = nxt
                        rnd += 1
                    champ = cur[0]
                    tc[champ] += 1
                    if champ in us_idxs:
                        rm[champ][8] += 1
                        best_rnd = 8
                        best_us = [champ]
                    if len(best_us) == 1:
                        uc[best_us[0]] += 1
                    else:
                        ties += 1

                for p, c in tc.items(): title_cnt[atp_bracket_raw[p]] += w * (c / tr)
                for p, c in fc.items(): final_cnt[atp_bracket_raw[p]] += w * (c / tr)
                for p, c in sc.items(): sf_cnt[atp_bracket_raw[p]] += w * (c / tr)
                for p, c in qc.items(): qf_cnt[atp_bracket_raw[p]] += w * (c / tr)
                for p, c in r4c.items(): r4_cnt[atp_bracket_raw[p]] += w * (c / tr)
                for p, c in uc.items(): uncond_us[atp_bracket_raw[p]] += w * (c / tr)
                for p, cnts in rm.items():
                    for r, c in cnts.items():
                        us_max_rnd_dist[atp_bracket_raw[p]][r] += w * (c / tr)
                tie_rate += w * (ties / tr)

    cond_us = {nm: v / (1.0 - tie_rate) for nm, v in uncond_us.items()}
    return title_cnt, final_cnt, sf_cnt, qf_cnt, r4_cnt, cond_us, uncond_us, tie_rate

# Run 4 regimes on the EXACT FIXED ATP BRACKET!
if __name__ == "__main__":
  atp_regimes = [
      ("Base (Aug 26 Talent + Exact Fixed Bracket)", 0.35, {}),
      ("Post-Draw Sharp Market (Fritz +12, Zverev +10, Fils +10, Jodar +6, Shelton -6)", 0.25, {
          "Taylor Fritz": 2076, "Alexander Zverev": 2148, "Arthur Fils": 2088,
          "Rafael Jodar": 2058, "Ben Shelton": 2069, "Tommy Paul": 1978,
      }),
      ("BO5 & NY Pedigree (Fritz +16, Tiafoe +14, Paul +14, Medvedev +15, Shelton -6, Fils -12, Tien -10)", 0.20, {
          "Taylor Fritz": 2080, "Frances Tiafoe": 2016, "Tommy Paul": 2002,
          "Daniil Medvedev": 2020, "Ben Shelton": 2069, "Arthur Fils": 2066,
          "Learner Tien": 1968, "Brandon Nakashima": 1986,
      }),
      ("Summer-2026 Hot-Form (Shelton +14, Fils +14, Nakashima +14, Tiafoe +10, Tien +12, Fritz -6)", 0.20, {
          "Ben Shelton": 2089, "Arthur Fils": 2092, "Brandon Nakashima": 2010,
          "Frances Tiafoe": 2012, "Learner Tien": 1990, "Taylor Fritz": 2058,
      }),
  ]

  mc_title = Counter(); mc_sf = Counter(); mc_qf = Counter(); mc_r4 = Counter()
  mc_cond = Counter(); mc_uncond = Counter(); mc_tie = 0.0
  print("=== EXACT FIXED-BRACKET ATP MC BY REGIME ===")
  for idx, (lbl, w, ov) in enumerate(atp_regimes):
      tc, fc, sc, qc, r4c, cu, uu, tr = run_fixed_atp_mc(elo_overrides=ov, n_trials=40000, seed=3100 + idx)
      mc_tie += w * tr
      for k, v in tc.items(): mc_title[k] += w * v
      for k, v in sc.items(): mc_sf[k] += w * v
      for k, v in qc.items(): mc_qf[k] += w * v
      for k, v in r4c.items(): mc_r4[k] += w * v
      for k, v in cu.items(): mc_cond[k] += w * v
      for k, v in uu.items(): mc_uncond[k] += w * v
      top_t = [(k, round(v, 3)) for k, v in tc.most_common(7)]
      top_u = [(k, round(v, 3)) for k, v in sorted(cu.items(), key=lambda x: -x[1])[:6]]
      print(f"Regime {idx+1} [{w:.2f}] {lbl}:")
      print("  Title:", top_t)
      print(f"  US Cond (tie={tr:.3f}):", top_u)

# ==============================================================================
# PART 2: POST-DRAW MEN'S SINGLES MULTI-MARKET CALIBRATION (Q3: 891014)
# ==============================================================================
# 1. FanDuel Post-Draw (Friday Aug 28, rg.org — FULL TOP-16!)
fd_atp_28 = {
    "Carlos Alcaraz":        3.40,  # +240
    "Alexander Zverev":      3.80,  # +280
    "Novak Djokovic":        8.00,  # +700
    "Taylor Fritz":         12.00,  # +1100
    "Rafael Jodar":         12.00,  # +1100
    "Ben Shelton":          13.00,  # +1200
    "Arthur Fils":          13.00,  # +1200
    "Felix Auger-Aliassime":23.00,  # +2200
    "Flavio Cobolli":       34.00,  # +3300
    "Jakub Mensik":         34.00,  # +3300
    "Daniil Medvedev":      34.00,  # +3300
    "Frances Tiafoe":       51.00,  # +5000
    "Brandon Nakashima":    51.00,  # +5000
    "Lorenzo Musetti":      56.00,  # +5500
    "Alex de Minaur":       56.00,  # +5500
    "Tommy Paul":           66.00,  # +6500
    "Field_Rest":           12.50,  # ~8% raw for Tien, Bublik, Lehecka, Rublev, Ruud, etc.
}

# 2. DraftKings Post-Draw (Friday Aug 28, sportingnews.com — top 7 + rest anchored to FD)
dk_atp_28 = dict(fd_atp_28)
dk_atp_28["Carlos Alcaraz"] = 3.50   # +250
dk_atp_28["Alexander Zverev"] = 4.00 # +300
dk_atp_28["Novak Djokovic"] = 8.00   # +700
dk_atp_28["Ben Shelton"] = 10.00     # +900
dk_atp_28["Rafael Jodar"] = 13.00    # +1200
dk_atp_28["Taylor Fritz"] = 13.00    # +1200
dk_atp_28["Arthur Fils"] = 13.00     # +1200

# 3. Caesars Post-Draw (Friday Aug 28, rg.org — lags on Alcaraz +170 & Shelton +800)
cz_atp_28 = {
    "Carlos Alcaraz":        2.70,  # +170
    "Alexander Zverev":      4.00,  # +300
    "Novak Djokovic":        8.50,  # +750
    "Ben Shelton":           9.00,  # +800
    "Taylor Fritz":         11.00,  # +1000
    "Rafael Jodar":         12.00,  # +1100
    "Arthur Fils":          13.00,  # +1200
    "Felix Auger-Aliassime":23.00,  # +2200
    "Frances Tiafoe":       26.00,  # +2500
    "Jakub Mensik":         31.00,  # +3000
    "Flavio Cobolli":       41.00,  # +4000
    "Daniil Medvedev":      41.00,  # +4000
    "Brandon Nakashima":    41.00,  # +4000
    "Tommy Paul":           41.00,  # +4000
    "Lorenzo Musetti":      51.00,  # +5000
    "Alex de Minaur":       61.00,  # +6000
    "Field_Rest":           12.50,
}

fd_m, fd_ov, fd_z, fd_k = devig_mid(fd_atp_28)
dk_m, dk_ov, dk_z, dk_k = devig_mid(dk_atp_28)
cz_m, cz_ov, cz_z, cz_k = devig_mid(cz_atp_28)

# 4. Kalshi Post-Draw (news.kalshi.com, Aug 28 — EXPLICITLY POST-DRAW!)
# Alcaraz 26% (27% shortly after draw, fell ~1% from 26% Thu morning -> 26%),
# Zverev 23% (+4% post-draw!), Djokovic 11%, Fils 7%, Fritz 6% (+2% post-draw!),
# Shelton 5% (-3% post-draw!), Jodar 5%, rest 17% distributed proportionally to FD!
kalshi_atp_28 = {
    "Carlos Alcaraz":   0.260,
    "Alexander Zverev": 0.230,
    "Novak Djokovic":   0.110,
    "Arthur Fils":      0.070,
    "Taylor Fritz":     0.060,
    "Ben Shelton":      0.050,
    "Rafael Jodar":     0.050,
}
rem_k = 1.0 - sum(kalshi_atp_28.values())
rem_fd = sum(v for k, v in fd_m.items() if k not in kalshi_atp_28)
for k, v in fd_m.items():
    if k not in kalshi_atp_28:
        kalshi_atp_28[k] = rem_k * (v / rem_fd)

# Final Q3 (891014) Post-Draw Blend:
# 45% Kalshi Post-Draw (Aug 28 sharp exchange)
# + 30% Post-Draw Sportsbooks (45% FanDuel + 40% DraftKings + 15% Caesars)
# + 25% Exact 128-Player Fixed-Bracket BO5 Monte Carlo
if __name__ == "__main__":
  atp_final = {}
  for k in fd_atp_28:
      if k == "Field_Rest": continue
      bks = 0.45 * fd_m[k] + 0.40 * dk_m[k] + 0.15 * cz_m[k]
      atp_final[k] = 0.45 * kalshi_atp_28[k] + 0.30 * bks + 0.25 * mc_title.get(k, 0.0)

  print(f"\n=== Q3 (891014) MEN'S SINGLES — POST-DRAW FRI AUG 28 ===")
  print(f"Overrounds: FD={fd_ov:.3f} (z={fd_z:.4f}), DK={dk_ov:.3f} (z={dk_z:.4f}), CZ={cz_ov:.3f} (z={cz_z:.4f})")
  print(f"{'Player':22s} | {'Kal28':6s} | {'FD_28':6s} | {'DK_28':6s} | {'CZ_28':6s} | {'FixMC':6s} | {'FINAL':6s}")
  for k, v in sorted(atp_final.items(), key=lambda x: -x[1])[:12]:
      print(f"{k:22s} | {kalshi_atp_28[k]:6.4f} | {fd_m[k]:6.4f} | {dk_m[k]:6.4f} | {cz_m[k]:6.4f} | {mc_title.get(k,0):6.4f} | {v:6.4f}")
  top7_m = sorted(atp_final.items(), key=lambda x: -x[1])[:7]
  print("ATP Top-7:", [(k, round(v, 4)) for k, v in top7_m])
  print("ATP Top-5 sum:", round(sum(v for _, v in top7_m[:5]), 4))

  print(f"\n=== Q2 (408930) FURTHEST U.S. MAN — POST-DRAW EXACT BRACKET (Tie Rate = {mc_tie:.4f}) ===")
  print(f"{'Player':22s} | {'Cond(Uniq)':10s} | {'Uncond':7s} | {'R4%':6s} | {'QF%':6s} | {'SF%':6s} | {'Win%':6s}")
  for k, v in sorted(mc_cond.items(), key=lambda x: -x[1])[:10]:
      print(f"{k:22s} | {v:10.4f} | {mc_uncond[k]:7.4f} | {mc_r4[k]:6.3f} | {mc_qf[k]:6.3f} | {mc_sf[k]:6.3f} | {mc_title[k]:6.4f}")
  top6_us = sorted(mc_cond.items(), key=lambda x: -x[1])[:6]
  print("US Top-6 (Cond):", [(k, round(v, 4)) for k, v in top6_us])
  print("US Top-5 sum (Cond):", round(sum(v for _, v in top6_us[:5]), 4))
  print("US Top-5 sum (Uncond):", round(sum(mc_uncond[k] for k, _ in top6_us[:5]), 4))


# ==============================================================================
# PART 3: EXACT 128-PLAYER OFFICIAL WOMEN'S SINGLES BRACKET (livetennis.it Aug 28)
# ==============================================================================
wta_bracket_raw = [
    # --- QUARTER 1 (Sabalenka [1] / Shnaider [15] / Kostyuk [11] / Noskova [6]) ---
    "Aryna Sabalenka", "Camila Osorio",
    "Renata Zarazua", "Polina Iatcenko",
    "Aoi Ito", "Oksana Selekhmeteva",
    "Kamilla Rakhimova", "Barbora Krejcikova",
    "Maja Chwalinska", "Taylor Townsend",
    "Taylah Preston", "Alycia Parks",
    "Hanne Vandewinkel", "Karolina Pliskova",
    "Daria Snigur", "Diana Shnaider",
    "Marta Kostyuk", "Storm Hunter",
    "Sloane Stephens", "Clara Tauson",
    "Kimberly Birrell", "Petra Marcinko",
    "McCartney Kessler", "Ekaterina Alexandrova",
    "Ann Li", "Antonia Ruzic",
    "Talia Gibson", "Donna Vekic",
    "Elvina Kalieva", "Lanlana Tararudee",
    "Katie Volynets", "Linda Noskova",

    # --- QUARTER 2 (Pegula [3] / Cirstea [16] / Svitolina [9] / Muchova [7]) ---
    "Jessica Pegula", "Elena-Gabriela Ruse",
    "Venus Williams", "Sofia Kenin",
    "Mananchaya Sawangkaew", "Panna Udvardy",
    "Shuai Zhang", "Leylah Fernandez",
    "Jasmine Paolini", "Veronika Erjavec",
    "Lucrezia Stefanini", "Dayana Yastremska",
    "Viktorija Golubic", "Diane Parry",
    "Julia Grabher", "Sorana Cirstea",
    "Elina Svitolina", "Solana Sierra",
    "Maya Joint", "Liudmila Samsonova",
    "Emiliana Arango", "Xinyu Wang",
    "Anna Blinkova", "Anna Kalinskaya",
    "Emma Navarro", "Lois Boisson",
    "Anouk Koevermans", "Caty McNally",
    "Claire Lee", "Katie Boulter",
    "Sinja Kraus", "Karolina Muchova",

    # --- QUARTER 3 (Andreeva [5] / Anisimova [10] / Eala [17] / Gauff [4]) ---
    "Mirra Andreeva", "Janice Tjen",
    "Gabriela Knutson", "Eva Lys",
    "Nikola Bartunkova", "Mayar Sherif",
    "Tatjana Maria", "Jelena Ostapenko",
    "Anastasia Potapova", "Tereza Valentova",
    "Arantxa Rus", "Leolia Jeanjean",
    "Lilli Tagger", "Tamara Korpatsch",
    "Ashlyn Krueger", "Amanda Anisimova",
    "Iva Jovic", "Magdalena Frech",
    "Magda Linette", "Francesca Jones",
    "Oleksandra Oliynykova", "Reese Brantmeier",
    "Mary Stoiana", "Alexandra Eala",
    "Sara Bejlek", "Cristina Bucsa",
    "Anhelina Kalinina", "Himeno Sakatsume",
    "Daria Kasatkina", "Paula Badosa",
    "Zeynep Sonmez", "Coco Gauff",

    # --- QUARTER 4 (Swiatek [8] / Bencic [12] / Osaka [13] / Rybakina [2]) ---
    "Iga Swiatek", "Xiyu Wang",
    "Nadia Podoroska", "Simona Waltert",
    "Harriet Dart", "Peyton Stearns",
    "Elsa Jacquemot", "Marie Bouzkova",
    "Madison Keys", "Alina Korneeva",
    "Lucie Havlickova", "Anna Bondar",
    "Qinwen Zheng", "Ksenia Liutova",
    "Yulia Putintseva", "Belinda Bencic",
    "Naomi Osaka", "Anastasia Zakharova",
    "Elisabetta Cocciaretto", "Katerina Siniakova",
    "Tamara Zidansek", "Maria Timofeeva",
    "Kaitlin Quevedo", "Elise Mertens",
    "Maria Sakkari", "Robin Montgomery",
    "Yuliia Starodubtseva", "Ella Seidel",
    "Darja Vidmanova", "Jessica Bouzas Maneiro",
    "Thea Frodin", "Elena Rybakina",
]
assert len(wta_bracket_raw) == 128, f"Expected 128 WTA slots, got {len(wta_bracket_raw)}"

# Hard-court BO3 base Elos calibrated to Aug 26 pre-draw multi-market consensus
# (before draw asymmetry! Notice Qinwen Zheng is ALSO unseeded in Q4 vs Bencic/Keys/Swiatek!!)
wta_base_elo = {
    "Aryna Sabalenka":   2152,   # Pre-draw ~21%, 2x defending champ
    "Iga Swiatek":       2132,   # Pre-draw ~15%, Toronto champ
    "Coco Gauff":        2120,   # Pre-draw ~14%, dominant Cinci champ
    "Elena Rybakina":    2122,   # Healthy baseline (2026 AO champ, Toronto F); injury mixture below!
    "Naomi Osaka":       2056,   # Pre-draw ~7%, 2x USO champ
    "Mirra Andreeva":    2040,   # #5 seed, 2026 RG champ
    "Jessica Pegula":    2036,   # #3 seed, 2024 USO F, Cinci F, 45 wins
    "Amanda Anisimova":  2018,   # #10 seed, DK +1600
    "Marta Kostyuk":     2005,   # #11 seed, DK +1800, beat Andreeva in Cinci
    "Karolina Muchova":  1992,   # #7 seed, Wim F + USO Mixed champ, DK +3000
    "Linda Noskova":     1985,   # #6 seed, Wim champ, DK +3000
    "Alexandra Eala":    1985,   # #17 seed, Washington DC champ, DK +2800
    "Belinda Bencic":    1982,   # #12 seed, DK +3500
    "Madison Keys":      1978,   # #22 seed, 2025 AO champ, DK +5000
    "Elina Svitolina":   1972,   # #9 seed, DK +4000
    "Qinwen Zheng":      1970,   # Unseeded comeback/injury return in Q4!
    "Barbora Krejcikova":1955,   # #27 seed, DK +5000
    "Iva Jovic":         1952,   # #14 seed, DK +5000
    "Diana Shnaider":    1952,   # #15 seed
    "Ekaterina Alexandrova": 1950, # #18 seed
    "Emma Navarro":      1945,   # #26 seed, DK +6000
    "Jasmine Paolini":   1940,   # #19 seed
    "Clara Tauson":      1940,
    "Paula Badosa":      1935,
    "Daria Kasatkina":   1935,
    "Anna Kalinskaya":   1935,   # #21 seed
    "Liudmila Samsonova":1932,
    "Sara Bejlek":       1932,   # #28 seed, beat Sabalenka in Cinci!
    "Jelena Ostapenko":  1930,   # #30 seed
    "Leylah Fernandez":  1930,   # #31 seed
    "Elise Mertens":     1925,   # #23 seed
    "Maja Chwalinska":   1920,   # #20 seed
    "Anastasia Potapova":1920,   # #24 seed
    "Marie Bouzkova":    1920,   # #25 seed
    "Sorana Cirstea":    1918,   # #16 seed
    "Donna Vekic":       1915,
    "Maria Sakkari":     1912,   # #32 seed
    "Ann Li":            1910,   # #29 seed
    "Magda Linette":     1910,
    "McCartney Kessler": 1910,
    "Magdalena Frech":   1905,
    "Ashlyn Krueger":    1905,
    "Katerina Siniakova":1905,
    "Maya Joint":        1905,
    "Dayana Yastremska": 1905,
    "Xinyu Wang":        1905,
    "Peyton Stearns":    1900,
    "Sofia Kenin":       1895,
    "Yulia Putintseva":  1895,
    "Katie Boulter":     1895,
    "Taylor Townsend":   1895,
    "Anhelina Kalinina": 1890,
    "Camila Osorio":     1885,
    "Eva Lys":           1885,
    "Jessica Bouzas Maneiro": 1885,
    "Karolina Pliskova": 1885,
    "Xiyu Wang":         1880,
    "Zeynep Sonmez":     1880,
    "Elena-Gabriela Ruse": 1880,
    "Alycia Parks":      1880,
    "Cristina Bucsa":    1875,
    "Elisabetta Cocciaretto": 1875,
    "Anna Blinkova":     1870,
    "Katie Volynets":    1870,
    "Shuai Zhang":       1865,
    "Sloane Stephens":   1855,
    "Venus Williams":    1760,
    "Thea Frodin":       1755,
}

def run_fixed_wta_mc(n_trials=80000, seed=5050):
    rng = random.Random(seed)
    elos_base = [float(wta_base_elo.get(nm, 1845.0)) for nm in wta_bracket_raw]
    ryb_idx = wta_bracket_raw.index("Elena Rybakina")
    sab_idx = wta_bracket_raw.index("Aryna Sabalenka")

    # Rybakina Achilles/ankle mixture (practiced Thu per AFP, retired Cinci QF, WD mixed):
    #   Healthy (2130, 0.44), MildlyLimited (2065, 0.30), Compromised (1975, 0.18), WD/Retire (1740, 0.08)
    ryb_mix = [(2130, 0.44), (2065, 0.30), (1975, 0.18), (1740, 0.08)]
    # Sabalenka form/pressure mixture (17-7 post-March slump vs 34-6 NY dominance):
    sab_mix = [(2195, 0.45), (2135, 0.35), (2045, 0.20)]

    title_cnt = Counter(); final_cnt = Counter(); sf_cnt = Counter(); qf_cnt = Counter()
    for re_e, wr in ryb_mix:
        for se_e, ws in sab_mix:
            w = wr * ws
            tr = max(2000, int(round(n_trials * w)))
            elos = list(elos_base)
            elos[ryb_idx] = float(re_e)
            elos[sab_idx] = float(se_e)
            pc = {}
            def gp(i, j):
                k = (elos[i], elos[j])
                v = pc.get(k)
                if v is None:
                    v = p_bo3(elos[i], elos[j])
                    pc[k] = v
                return v
            tc = Counter(); fc = Counter(); sc = Counter(); qc = Counter()
            for _ in range(tr):
                cur = list(range(128))
                rnd = 1
                while len(cur) > 1:
                    if rnd == 5:
                        for p in cur: qc[p] += 1
                    elif rnd == 6:
                        for p in cur: sc[p] += 1
                    elif rnd == 7:
                        for p in cur: fc[p] += 1
                    nxt = []
                    for k in range(0, len(cur), 2):
                        a, b = cur[k], cur[k+1]
                        nxt.append(a if rng.random() < gp(a, b) else b)
                    cur = nxt
                    rnd += 1
                tc[cur[0]] += 1
            for p, c in tc.items(): title_cnt[wta_bracket_raw[p]] += w * (c / tr)
            for p, c in fc.items(): final_cnt[wta_bracket_raw[p]] += w * (c / tr)
            for p, c in sc.items(): sf_cnt[wta_bracket_raw[p]] += w * (c / tr)
            for p, c in qc.items(): qf_cnt[wta_bracket_raw[p]] += w * (c / tr)
    return title_cnt, final_cnt, sf_cnt, qf_cnt

if __name__ == "__main__":
  wta_mc_t, wta_mc_f, wta_mc_sf, wta_mc_qf = run_fixed_wta_mc(n_trials=80000, seed=5050)

dk_wta_28 = {
    "Aryna Sabalenka":   4.20,  # +320
    "Coco Gauff":        6.00,  # +500
    "Iga Swiatek":       6.50,  # +550
    "Naomi Osaka":      11.50,  # +1000 table / +1200 text -> mid +1050 (11.50)
    "Elena Rybakina":   12.00,  # +1100
    "Jessica Pegula":   13.00,  # +1200
    "Mirra Andreeva":   15.00,  # +1400
    "Amanda Anisimova": 17.00,  # +1600
    "Marta Kostyuk":    19.00,  # +1800
    "Alexandra Eala":   29.00,  # +2800
    "Linda Noskova":    31.00,  # +3000
    "Karolina Muchova": 31.00,  # +3000
    "Belinda Bencic":   36.00,  # +3500
    "Elina Svitolina":  41.00,  # +4000
    "Iva Jovic":        51.00,  # +5000
    "Madison Keys":     51.00,  # +5000
    "Barbora Krejcikova":51.00, # +5000
    "Emma Navarro":     61.00,  # +6000
    "Field_Rest":       10.00,  # ~10% raw for Bejlek, Badosa, Tauson, Alexandrova, Shnaider, Qinwen Zheng, etc.
}
if __name__ == "__main__":
  dk_w, dkw_ov, dkw_z, dkw_k = devig_mid(dk_wta_28)

  wta_final = {}
  for k in dk_wta_28:
      if k == "Field_Rest": continue
      wta_final[k] = 0.55 * dk_w[k] + 0.45 * wta_mc_t.get(k, 0.0)

  print(f"\n=== Q1 (608158) WOMEN'S SINGLES — POST-DRAW FRI AUG 28 ===")
  print(f"DK Overround={dkw_ov:.3f} (z={dkw_z:.4f}, k={dkw_k:.3f})")
  print(f"{'Player':20s} | {'DK_28':6s} | {'FixMC':6s} | {'MC_SF':6s} | {'MC_F':6s} | {'FINAL':6s}")
  for k, v in sorted(wta_final.items(), key=lambda x: -x[1])[:12]:
      print(f"{k:20s} | {dk_w[k]:6.4f} | {wta_mc_t.get(k,0):6.4f} | {wta_mc_sf.get(k,0):6.3f} | {wta_mc_f.get(k,0):6.3f} | {v:6.4f}")
  top8_w = sorted(wta_final.items(), key=lambda x: -x[1])[:8]
  print("WTA Top-8:", [(k, round(v, 4)) for k, v in top8_w])
  print("WTA Top-5 sum:", round(sum(v for _, v in top8_w[:5]), 4))
