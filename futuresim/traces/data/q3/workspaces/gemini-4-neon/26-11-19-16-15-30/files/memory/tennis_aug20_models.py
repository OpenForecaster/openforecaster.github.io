import random
from collections import Counter

# ==============================================================================
# CINCINNATI OPEN 2026 & US OPEN MIXED DOUBLES MODELS — THURSDAY AUG 20, 2026
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
# PART 1: WTA CINCINNATI 2026 (qid=260735) — 7 PLAYERS REMAINING (PEGULA IN SF!)
# ==============================================================================
# Verified bracket Thu Aug 20 evening:
#   TOP HALF (Fri Aug 21 QFs):
#     QF1: Sara Bejlek vs Madison Keys
#     QF2: Coco Gauff vs Marta Kostyuk
#   BOTTOM HALF:
#     SF2 Spot #1 LOCKED: Jessica Pegula (d. Anisimova 6-4 2-6 7-6(4), MTO in set 2, near-retirement scare!)
#     QF4 (Thu Aug 20 night): Iga Swiatek vs Elena Rybakina

wta_tree_pegula_plays = (
    (
        ("Sara Bejlek", "Madison Keys"),
        ("Coco Gauff", "Marta Kostyuk"),
    ),
    (
        "Jessica Pegula",
        ("Iga Swiatek", "Elena Rybakina"),
    ),
)

# Tree if Pegula withdraws pre-SF due to Thursday physical scare (Swiatek/Rybakina winner gets walkover to Final!)
wta_tree_pegula_wd = (
    (
        ("Sara Bejlek", "Madison Keys"),
        ("Coco Gauff", "Marta Kostyuk"),
    ),
    ("Iga Swiatek", "Elena Rybakina"),
)

wta_elo = {
    "Iga Swiatek": 2102,       # #7 seed, defending champ, Toronto champ, 9-match HC win streak, crisp 6-3 6-3 vs Parry
    "Elena Rybakina": 2075,    # #2 seed, AO champ, crisp 6-4 6-4 vs Shnaider, playing for World No. 1!
    "Coco Gauff": 2072,        # #4 seed, 2023 Cinci champ, clean 6-3 6-2 vs Bouzkova (8/8 BPs saved), Sabalenka OUT of her half!
    "Marta Kostyuk": 2010,     # #10 seed, crushed RG champ Andreeva 4-6 6-0 6-2 (12 of 14 games), well rested!
    "Madison Keys": 1995,      # #19 seed, 2019 Cinci champ, 2025 AO champ, beat Siniakova 6-1 6-3 & Xiyu Wang 7-6(3) 6-4
    "Jessica Pegula": 1992,    # Base rating ~2025 discounted -33 Elo for set-2 MTO/near-retirement scare (offset by Fri rest day)
    "Sara Bejlek": 1938,       # #35, Abu Dhabi HC champ, stunned Krejcikova, Alexandrova, AND #1 Sabalenka 7-6(7) 6-4!
}

wta_h2h = {
    ("Iga Swiatek", "Elena Rybakina"): +25,    # Swiatek beat Ryb 6-2 6-3 in Toronto F last week & Cinci 2025 SF (~57.5% Swiatek)
    ("Iga Swiatek", "Coco Gauff"): +40,        # Historical Swiatek H2H dominance (~11-3/11-4, tempered by fast US HC -> ~60% Swiatek)
    ("Iga Swiatek", "Jessica Pegula"): -20,    # Pegula plays Swiatek very tough on fast US HC (USO 24, Montreal 23, Bad Homburg 25)
    ("Coco Gauff", "Marta Kostyuk"): +18,      # Gauff 2023 Cinci champ + H2H edge (~62.5% Gauff)
    ("Coco Gauff", "Madison Keys"): +12,       # Gauff defense/athleticism edge over Keys (~63% Gauff)
    ("Madison Keys", "Sara Bejlek"): +35,      # Big fast-HC power + Bejlek post-Sabalenka midnight-upset letdown risk (~63% Keys)
    ("Elena Rybakina", "Coco Gauff"): +10,     # Slight fast-HC serve edge Rybakina (~52% Ryb)
}

def solve_wta_with_wd(elos, h2h, scale, p_wd):
    r_play = solve_tree(wta_tree_pegula_plays, elos, h2h, scale)
    r_wd = solve_tree(wta_tree_pegula_wd, elos, h2h, scale)
    out = {}
    for k in elos:
        out[k] = (1.0 - p_wd) * r_play.get(k, 0.0) + p_wd * r_wd.get(k, 0.0)
    return out

wta_regimes = [
    ("Base (H2H + Moderate Pegula Injury Discount, wd=9%)", wta_elo, wta_h2h, 400.0, 0.09, 0.45),
    ("Pegula Compromised/Hurt (wd=18%, -40 extra Elo)", {
        **wta_elo,
        "Jessica Pegula": wta_elo["Jessica Pegula"] - 40,
    }, wta_h2h, 400.0, 0.18, 0.20),
    ("Pegula Recovers w/ Fri Rest (wd=3%, +33 Elo -> full 2025)", {
        **wta_elo,
        "Jessica Pegula": wta_elo["Jessica Pegula"] + 33,
    }, wta_h2h, 400.0, 0.03, 0.15),
    ("Fast-Cinci Power / Rybakina No.1 Push + Kostyuk/Keys Hot", {
        **wta_elo,
        "Elena Rybakina": wta_elo["Elena Rybakina"] + 25,
        "Marta Kostyuk": wta_elo["Marta Kostyuk"] + 22,
        "Madison Keys": wta_elo["Madison Keys"] + 20,
        "Sara Bejlek": wta_elo["Sara Bejlek"] + 15,
        "Iga Swiatek": wta_elo["Iga Swiatek"] - 15,
    }, {**wta_h2h, ("Iga Swiatek", "Elena Rybakina"): +5}, 410.0, 0.10, 0.20),
]

print("=== PART 1: WTA CINCINNATI 2026 (qid=260735) — THU AUG 20 ===")
for a, b in [
    ("Iga Swiatek", "Elena Rybakina"),
    ("Iga Swiatek", "Jessica Pegula"),
    ("Elena Rybakina", "Jessica Pegula"),
    ("Coco Gauff", "Marta Kostyuk"),
    ("Madison Keys", "Sara Bejlek"),
    ("Iga Swiatek", "Coco Gauff"),
    ("Elena Rybakina", "Coco Gauff"),
]:
    print(f"  P({a:16s} d. {b:16s}) = {win_prob(a, b, wta_elo, wta_h2h):.3f}")

wta_blend = {}
for rname, elos, h2h, sc, pwd, rw in wta_regimes:
    res = solve_wta_with_wd(elos, h2h, sc, pwd)
    print(f"  [{rname:58s} w={rw:.2f}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(res.items(), key=lambda x: -x[1])))
    for k, v in res.items():
        wta_blend[k] = wta_blend.get(k, 0.0) + rw * v

print("\nFINAL WTA BLEND (ALL 7 REMAINING PLAYERS):")
for k, v in sorted(wta_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:22s}: {v:.4f}")
print(f"Top-5 sum = {sum(v for _, v in sorted(wta_blend.items(), key=lambda x: -x[1])[:5]):.4f}")


# ==============================================================================
# PART 2: ATP CINCINNATI 2026 (qid=372528) — 7 PLAYERS REMAINING (COBOLLI IN SF!)
# ==============================================================================
# Verified bracket Thu Aug 20 evening:
#   TOP HALF:
#     SF1 Spot #1 LOCKED: Flavio Cobolli (d. Paul 2-6 6-3 6-4! 4th straight 3-setter, gets Fri rest day!)
#     QF2 (Thu Aug 20 night): Thiago Agustin Tirante vs Arthur Fils
#   BOTTOM HALF (Fri Aug 21 QFs):
#     QF3: Taylor Fritz vs Brandon Nakashima
#     QF4: Lorenzo Musetti vs Frances Tiafoe

atp_tree = (
    (
        "Flavio Cobolli",
        ("Thiago Agustin Tirante", "Arthur Fils"),
    ),
    (
        ("Taylor Fritz", "Brandon Nakashima"),
        ("Lorenzo Musetti", "Frances Tiafoe"),
    ),
)

atp_elo = {
    "Taylor Fritz": 2070,            # #6 (highest seed left!), DC champ, super fresh (crushed Merida & O'Connell 6-4 6-3)
    "Arthur Fils": 2032,             # #21, beat #9 Lehecka & demolished #5 de Minaur 6-3 6-4, 5th M1000 QF of 2026, healthy & fresh!
    "Flavio Cobolli": 1995,          # #7, RG finalist, Acapulco HC champ, beat Jodar & Paul, ALREADY in SF (gets Fri off! Slight 4x3-set wear)
    "Brandon Nakashima": 1990,       # #27, 11-2 summer HC (DC SF, Montreal F, beat Medvedev & Borges in 3 sets — slight cumulative fatigue)
    "Lorenzo Musetti": 1992,         # #10, crisp 6-1 6-3 vs Zheng & 7-5 6-2 vs Faria, fresh
    "Frances Tiafoe": 1978,          # #17, 2024 Cinci finalist! Beat #2 Auger-Aliassime 6-3 6-4, 4-0 last 4 vs Top 10!
    "Thiago Agustin Tirante": 1900,  # Beat Fritz (Montreal), Djokovic, Landaluce, #14 Mensik 5-7 6-4 6-4
}

atp_h2h = {
    ("Arthur Fils", "Thiago Agustin Tirante"): +22,  # Fast-HC power edge (~70.5% Fils)
    ("Arthur Fils", "Flavio Cobolli"): +15,          # Fils fresher legs + faster-HC serve/power (~57.5% Fils)
    ("Taylor Fritz", "Brandon Nakashima"): +20,      # Beat Nakashima in DC SF + Fritz much fresher (~64% Fritz)
    ("Taylor Fritz", "Frances Tiafoe"): +45,         # Fritz dominates Tiafoe historically (~7-1 H2H -> ~69% Fritz!)
    ("Taylor Fritz", "Lorenzo Musetti"): +15,        # Fast Cinci HC serve edge over Musetti (~63% Fritz)
    ("Frances Tiafoe", "Lorenzo Musetti"): +15,      # Fast Cinci HC + US home crowd (2024 finalist) offsets slight Elo gap (~50%!)
}

atp_regimes = [
    ("Base (Balanced + H2H + Fatigue)", atp_elo, atp_h2h, 400.0, 0.45),
    ("Freshness / Explosive Fast-HC (Fritz+Fils+Tiafoe, Cobolli tired)", {
        **atp_elo,
        "Taylor Fritz": atp_elo["Taylor Fritz"] + 18,
        "Arthur Fils": atp_elo["Arthur Fils"] + 20,
        "Frances Tiafoe": atp_elo["Frances Tiafoe"] + 18,
        "Flavio Cobolli": atp_elo["Flavio Cobolli"] - 25,
        "Brandon Nakashima": atp_elo["Brandon Nakashima"] - 15,
    }, atp_h2h, 395.0, 0.25),
    ("Cobolli Grit + Hot Underdogs (Cobolli+Nakashima+Musetti+Tirante)", {
        **atp_elo,
        "Flavio Cobolli": atp_elo["Flavio Cobolli"] + 22,
        "Brandon Nakashima": atp_elo["Brandon Nakashima"] + 22,
        "Lorenzo Musetti": atp_elo["Lorenzo Musetti"] + 15,
        "Thiago Agustin Tirante": atp_elo["Thiago Agustin Tirante"] + 25,
        "Taylor Fritz": atp_elo["Taylor Fritz"] - 12,
        "Arthur Fils": atp_elo["Arthur Fils"] - 15,
    }, atp_h2h, 415.0, 0.20),
    ("High-Parity 2026 Cinci Chaos", atp_elo, atp_h2h, 455.0, 0.10),
]

print("\n=== PART 2: ATP CINCINNATI 2026 (qid=372528) — THU AUG 20 ===")
for a, b in [
    ("Arthur Fils", "Thiago Agustin Tirante"),
    ("Arthur Fils", "Flavio Cobolli"),
    ("Flavio Cobolli", "Thiago Agustin Tirante"),
    ("Taylor Fritz", "Brandon Nakashima"),
    ("Lorenzo Musetti", "Frances Tiafoe"),
    ("Taylor Fritz", "Lorenzo Musetti"),
    ("Taylor Fritz", "Frances Tiafoe"),
    ("Taylor Fritz", "Arthur Fils"),
    ("Taylor Fritz", "Flavio Cobolli"),
]:
    print(f"  P({a:22s} d. {b:22s}) = {win_prob(a, b, atp_elo, atp_h2h):.3f}")

atp_blend = {}
for rname, elos, h2h, sc, rw in atp_regimes:
    res = solve_tree(atp_tree, elos, h2h, sc)
    print(f"  [{rname:64s} w={rw:.2f}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(res.items(), key=lambda x: -x[1])))
    for k, v in res.items():
        atp_blend[k] = atp_blend.get(k, 0.0) + rw * v

print("\nFINAL ATP BLEND (ALL 7 REMAINING PLAYERS):")
for k, v in sorted(atp_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:24s}: {v:.4f}")
print(f"Top-5 sum = {sum(v for _, v in sorted(atp_blend.items(), key=lambda x: -x[1])[:5]):.4f}")


# ==============================================================================
# PART 3: US OPEN MIXED DOUBLES (qid=772246) — UPDATED REST/PLAY PROBABILITY
# ==============================================================================
# Update from Aug 18 -> Aug 20:
#   - Sabalenka lost Cinci R16 on Wed night -> BOTH Djokovic & Sabalenka now have 6 full days rest before Aug 25!
#   - Hence p_play rises from ~0.80 to ~0.88 (no deep-Cinci-run withdrawal risk!).
#   - Zverev & Auger-Aliassime ALSO lost Cinci R16 -> Townsend/Zverev & Eala/FAA also fully rested!
#   - Anisimova lost Cinci QF -> Anisimova/Tien rested.
#   - Cobolli deep in Cinci SF (4x 3-setters) + Bencic injury watch -> Bencic/Cobolli slightly discounted.

mixed_ratings = {
    "Sabalenka and Djokovic": 1950,
    "Rybakina and Fritz": 1950,
    "Shnaider and Medvedev": 1955,
    "Swiatek and Ruud": 1950,
    "Bencic and Cobolli": 1865,
    "Anisimova and Tien": 1900,
    "Errani and Vavassori": 2075,
    "Townsend and Zverev": 2025,       # Both Zverev & Townsend rested!
    "Fernandez and Tiafoe": 1940,
    "Eala and Auger-Aliassime": 1940,  # Both rested!
    "Svitolina and Monfils": 1850,
    "WC_TBD_1": 1900,
    "WC_TBD_2": 1880,
    "WC_TBD_3": 1860,
    "Siniakova and Patten": 2065,
    "Dabrowski and Heliovaara": 2040,
    "Stefani and Skupski": 2025,
    "Ostapenko and Arevalo": 2020,
    "Routliffe and Glasspool": 2015,
    "Krunic and Pavic": 2005,
    "QWC_1": 1840,
    "QWC_2": 1840,
}

def sim_mixed(ratings, scale=480.0, n_trials=150000, seed=101, p_play=0.88, bonus=0):
    rng = random.Random(seed)
    r = dict(ratings)
    r["Sabalenka and Djokovic"] += bonus
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
    win_cnt = 0
    for _ in range(n_trials):
        qp = qual_pool[:]
        rng.shuffle(qp)
        qa1 = qp[0] if rng.random() < mp(qp[0], qp[1]) else qp[1]
        qa2 = qp[2] if rng.random() < mp(qp[2], qp[3]) else qp[3]
        q_win_a = qa1 if rng.random() < mp(qa1, qa2) else qa2
        qb1 = qp[4] if rng.random() < mp(qp[4], qp[5]) else qp[5]
        qb2 = qp[6] if rng.random() < mp(qp[6], qp[7]) else qp[7]
        q_win_b = qb1 if rng.random() < mp(qb1, qb2) else qb2

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
        cur = br
        eliminated = False
        while len(cur) > 1:
            nxt = []
            for k in range(0, len(cur), 2):
                a, b = cur[k], cur[k+1]
                w, l = (a, b) if rng.random() < mp(a, b) else (b, a)
                if l == "Sabalenka and Djokovic":
                    elim_cnt[w] += 1
                    eliminated = True
                nxt.append(w)
            cur = nxt
        if not eliminated:
            win_cnt += 1
    p_elim = 1.0 - win_cnt / n_trials
    return {k: c / n_trials for k, c in elim_cnt.items()}, p_elim

c1, e1 = sim_mixed(mixed_ratings, scale=480.0, n_trials=150000, seed=101, p_play=0.88, bonus=0)
c2, e2 = sim_mixed(mixed_ratings, scale=520.0, n_trials=150000, seed=102, p_play=0.88, bonus=-35)
c3, e3 = sim_mixed(mixed_ratings, scale=440.0, n_trials=150000, seed=103, p_play=0.88, bonus=+35)

blend_u88 = Counter()
blend_ce = Counter()
for k in set(c1) | set(c2) | set(c3):
    blend_u88[k] = 0.88 * (0.50 * c1.get(k, 0) + 0.30 * c2.get(k, 0) + 0.20 * c3.get(k, 0))
    blend_ce[k] = 0.50 * (c1.get(k, 0) / e1) + 0.30 * (c2.get(k, 0) / e2) + 0.20 * (c3.get(k, 0) / e3)

print("\n=== PART 3: Q3 (772246) US OPEN MIXED DOUBLES (AUG 20, p_play=0.88) ===")
for k, _ in blend_u88.most_common(10):
    print(f"  {k:28s}: uncond(0.88)={blend_u88[k]:.4f} | cond_elim={blend_ce[k]:.4f}")
