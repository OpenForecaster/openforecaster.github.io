import math
import random
from collections import Counter

# ==============================================================================
# FORECASTING MODELS — SATURDAY AUG 22, 2026
# Batch: tennis_and_motor (669987, 260735, 372528, 772246)
# ==============================================================================

def shin_devig(dec_odds_dict):
    """Exact Shin (1993) devigging for multi-runner markets."""
    qs = {k: 1.0 / d for k, d in dec_odds_dict.items()}
    s = sum(qs.values())
    if s <= 1.0:
        return {k: v / s for k, v in qs.items()}
    # Solve for z in [0, 1) such that sum_i p_i(z) = 1
    # p_i(z) = (sqrt(z^2 + 4*(1-z)*q_i^2/s) - z) / (2*(1-z))
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
    lo, hi = 1.0, 3.0
    for _ in range(100):
        k_exp = 0.5 * (lo + hi)
        tot = sum(q ** k_exp for q in qs.values())
        if tot > 1.0:
            lo = k_exp
        else:
            hi = k_exp
    k_exp = 0.5 * (lo + hi)
    return {name: q ** k_exp for name, q in qs.items()}, k_exp

def prop_devig(dec_odds_dict):
    qs = {k: 1.0 / d for k, d in dec_odds_dict.items()}
    s = sum(qs.values())
    return {k: q / s for k, q in qs.items()}


# ==============================================================================
# PART 1: Q1 (qid=669987) — 2026 F1 DUTCH GRAND PRIX (POST-QUALIFYING SAT AUG 22)
# ==============================================================================
# Grid: P1 Norris (1:11.163), P2 Russell (+0.102), P3 Antonelli (+0.133),
#       P4 Piastri (+0.142), P5 Hamilton (+0.331), P6 Leclerc (+0.395), P7 Verstappen
# Weather Sun Aug 23: ~20C, cool & partly sunny, LOW chance of rain, 15 km/h breeze.
# Sprint Sat Aug 22: P1 Russell, P2 Leclerc (passed Norris lap 18 on softs), P3 Norris,
#       P4 Antonelli (damaged floor), P5 Piastri, P6 Verstappen, P7 Hamilton.

bet365 = {
    "Lando Norris": 13/8 + 1,      # 2.625
    "George Russell": 2/1 + 1,     # 3.000
    "Kimi Antonelli": 12/5 + 1,    # 3.400
    "Lewis Hamilton": 16/1 + 1,    # 17.0
    "Charles Leclerc": 20/1 + 1,   # 21.0
    "Oscar Piastri": 25/1 + 1,     # 26.0
    "Max Verstappen": 40/1 + 1,    # 41.0
    "Field_Rest": 55.0,            # ~1.8% raw for Lawson 100-1 + others 250-1
}

us_book = {
    "Lando Norris": 2.60,          # +160
    "George Russell": 3.25,        # +225
    "Kimi Antonelli": 3.50,        # +250
    "Lewis Hamilton": 15.0,        # +1400
    "Charles Leclerc": 17.0,       # +1600
    "Oscar Piastri": 21.0,         # +2000
    "Max Verstappen": 41.0,        # +4000
    "Field_Rest": 55.0,
}

# Average sharp odds (also incorporating Hills/Paddy Antonelli 5-2=3.50 & Piastri 20-1=21.0)
consensus_odds = {
    "Lando Norris": 2.61,
    "George Russell": 3.12,
    "Kimi Antonelli": 3.45,
    "Lewis Hamilton": 16.0,
    "Charles Leclerc": 19.0,
    "Oscar Piastri": 23.0,
    "Max Verstappen": 41.0,
    "Field_Rest": 55.0,
}

b_shin, bz = shin_devig(bet365)
u_shin, uz = shin_devig(us_book)
c_shin, cz = shin_devig(consensus_odds)
c_pow, ck = power_devig(consensus_odds)
c_prop = prop_devig(consensus_odds)

# Fundamental / Zandvoort Pole-Conversion + Race-Pace model:
# 5/5 modern Zandvoort wins from pole, cool/dry Sunday favors track position,
# BUT Sprint showed Mercedes superior race pace + McLaren rear tyre deg + Mercedes 2v1 strategy pincer
# Also Piastri looked fastest through Q1/Q2 and won here from pole in 2025 (+0.142s off pole)
f1_fund = {
    "Lando Norris": 0.380,     # Pole at Zandvoort (5/5) + Hungary pole->win, tempered by Sprint deg
    "George Russell": 0.255,   # P2 + dominant Sprint win + Mercedes pace
    "Kimi Antonelli": 0.205,   # P3 + championship leader + fixed floor + S1 mistake cost pole
    "Oscar Piastri": 0.055,    # P4 (+0.142s!), 2025 Zandvoort winner, needs Norris/Merc trouble
    "Lewis Hamilton": 0.045,   # P5, strong Ferrari race pace, recovered from Fri setup error
    "Charles Leclerc": 0.040,  # P6, blazing Sprint pace (P2, passed Norris)
    "Max Verstappen": 0.015,   # P7, needs chaos/SC/rain
    "Field_Rest": 0.005,
}

# Market-anchored blend: 65% Sharp Market (Shin+Power average) + 35% Fundamental Zandvoort model
# (Sharp post-qualifying F1 betting markets incorporate full telemetry, tyre sets, deg, & weather!)
f1_mkt = {k: 0.50 * c_shin[k] + 0.50 * c_pow[k] for k in consensus_odds}
f1_final = {k: 0.65 * f1_mkt[k] + 0.35 * f1_fund[k] for k in consensus_odds}

print("=== Q1 (669987) 2026 F1 DUTCH GRAND PRIX (POST-QUALI SAT AUG 22) ===")
print(f"Overrounds: Bet365={sum(1/v for v in bet365.values()):.3f} (z={bz:.4f}), US={sum(1/v for v in us_book.values()):.3f} (z={uz:.4f}), Cons={sum(1/v for v in consensus_odds.values()):.3f} (z={cz:.4f}, k={ck:.3f})")
print(f"{'Driver':18s} | {'B365_Sh':7s} | {'US_Sh':7s} | {'Con_Sh':7s} | {'Con_Pow':7s} | {'Con_Prp':7s} | {'Fund':7s} | {'FINAL':7s}")
for k in sorted(f1_final, key=lambda x: -f1_final[x]):
    print(f"{k:18s} | {b_shin[k]:7.4f} | {u_shin[k]:7.4f} | {c_shin[k]:7.4f} | {c_pow[k]:7.4f} | {c_prop[k]:7.4f} | {f1_fund[k]:7.4f} | {f1_final[k]:7.4f}")
top5_f1 = sorted([(k, v) for k, v in f1_final.items() if k != "Field_Rest"], key=lambda x: -x[1])[:5]
print("Top-5 sum:", round(sum(v for _, v in top5_f1), 4), "| Top-5:", [(k, round(v, 3)) for k, v in top5_f1])


# ==============================================================================
# HELPER FOR TENNIS TREES
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
# PART 2: Q2 (qid=260735) — WTA CINCINNATI 2026 — ONLY 3 PLAYERS LEFT!
# ==============================================================================
# COMPLETED:
#   - QF2 (Fri night): Coco Gauff d. Marta Kostyuk 6-2, 6-2 (70 min!) -> KOSTYUK OUT!
#   - SF2 (Sat afternoon): Jessica Pegula d. Iga Swiatek 7-5, 4-6, 6-4 (2h47m!) -> SWIATEK OUT! PEGULA IN FINAL!
# REMAINING:
#   - SF1 (Sat night 7:30 PM ET): Coco Gauff (#4) vs Sara Bejlek (#35)
#   - FINAL (Sun Aug 23): Jessica Pegula (#3) vs Winner(Gauff, Bejlek)

wta_tree = (
    "Jessica Pegula",
    ("Coco Gauff", "Sara Bejlek"),
)

# Updated Elo after Pegula BEAT Swiatek 7-5 4-6 6-4 (proves hip held up & elite #3 fast-HC level,
# though 2h47m battle + Thu 2h14m QF leaves minor fatigue/hip-flare risk)
# and Gauff crushed Kostyuk 6-2 6-2 in 70m!
wta_elo = {
    "Coco Gauff": 2082,      # Upgraded +12 after 6-2 6-2 demolition of Kostyuk; 2023 Cinci champ, super fresh!
    "Jessica Pegula": 2055,  # Upgraded +60 from discounted 1995 after beating Swiatek 7-5 4-6 6-4! Slight -10 fatigue vs peak 2065.
    "Sara Bejlek": 1962,     # Beat Krejcikova, #1 Sabalenka, Keys (2h37m); first WTA 1000 SF.
}

wta_h2h = {
    ("Coco Gauff", "Sara Bejlek"): +42,     # Style/athleticism/experience/freshness edge -> ~72.0% Gauff
    ("Coco Gauff", "Jessica Pegula"): +5,   # Virtually coin-flip on fast HC: Pegula's clean flat returns/H2H vs Gauff's freshness/defense -> ~54.6% Gauff
    ("Jessica Pegula", "Sara Bejlek"): +38, # Flat error-free counterpunching nightmare for Bejlek + Final pedigree -> ~68.0% Pegula
}

wta_regimes = [
    ("Base (Balanced: Gauff ~72% SF, ~55% vs Pegula; Pegula ~68% vs Bejlek)", wta_elo, wta_h2h, 400.0, 0.03, 0.45),
    ("Pegula Fatigue / Hip Flare Overnight (wd=8%, -35 Elo)", {
        **wta_elo, "Jessica Pegula": wta_elo["Jessica Pegula"] - 35
    }, wta_h2h, 400.0, 0.08, 0.20),
    ("Pegula Peak Fast-HC / H2H Edge Over Gauff (wd=1%, +25 Elo, h2h -15)", {
        **wta_elo, "Jessica Pegula": wta_elo["Jessica Pegula"] + 25
    }, {**wta_h2h, ("Coco Gauff", "Jessica Pegula"): -15}, 400.0, 0.01, 0.20),
    ("Bejlek Cinderella Surge / High Parity", {
        **wta_elo, "Sara Bejlek": wta_elo["Sara Bejlek"] + 45
    }, wta_h2h, 420.0, 0.03, 0.15),
]

print("\n=== Q2 (260735) WTA CINCINNATI — SAT AUG 22 EVENING (EXHAUSTIVE 3 PLAYERS) ===")
for a, b in [("Coco Gauff", "Sara Bejlek"), ("Coco Gauff", "Jessica Pegula"), ("Jessica Pegula", "Sara Bejlek")]:
    print(f"  Base P({a:15s} d. {b:15s}) = {win_prob(a, b, wta_elo, wta_h2h):.3f}")

wta_blend = {}
for name, elos, h2h, sc, pwd, w in wta_regimes:
    r_play = solve_tree(wta_tree, elos, h2h, sc)
    # If Pegula withdraws pre-final (pwd), SF1 winner wins title directly
    r_wd = solve_tree(("Coco Gauff", "Sara Bejlek"), elos, h2h, sc)
    r = {k: (1.0 - pwd) * r_play.get(k, 0.0) + pwd * r_wd.get(k, 0.0) for k in elos}
    print(f"  [{name:68s} w={w:.2f}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(r.items(), key=lambda x: -x[1])))
    for k, v in r.items():
        wta_blend[k] = wta_blend.get(k, 0.0) + w * v

print("FINAL WTA BLEND (sum =", round(sum(wta_blend.values()), 4), "):")
for k, v in sorted(wta_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:20s}: {v:.4f}")


# ==============================================================================
# PART 3: Q3 (qid=372528) — ATP CINCINNATI 2026 — ONLY 3 PLAYERS LEFT!
# ==============================================================================
# COMPLETED:
#   - QF4 (Fri night): Frances Tiafoe d. Lorenzo Musetti 7-6(2), 7-5 -> MUSETTI OUT!
#   - SF1 (Sat afternoon): Arthur Fils d. Flavio Cobolli 6-3, 6-4 (67m, 22W, 6 aces!) -> COBOLLI OUT! FILS IN FINAL!
# REMAINING:
#   - SF2 (Sat night 7:30 PM ET): Frances Tiafoe (#17) vs Brandon Nakashima (#27)
#       KEY NEW FACT: Tiafoe leads H2H 6-1 / 7-1 (5-1 on hard courts!), 2024 Cinci finalist, 7-3 vs Americans in 2026!
#   - FINAL (Sun Aug 23): Arthur Fils (#21, super fresh!) vs Winner(Tiafoe, Nakashima)

atp_tree = (
    "Arthur Fils",
    ("Frances Tiafoe", "Brandon Nakashima"),
)

atp_elo = {
    "Arthur Fils": 2075,        # Upgraded +33 after 67m 6-3 6-4 destruction of #7 Cobolli (following 64m Tirante, 6-3 6-4 de Minaur!)
    "Brandon Nakashima": 2020,  # 12-2 summer HC, Montreal F, beat Fritz 7-6(9) 4-6 6-3; week 3 heavy mileage
    "Frances Tiafoe": 2012,     # Upgraded +27 after beating #10 Musetti 7-6(2) 7-5 (after #2 FAA 6-3 6-4); 2024 Cinci finalist!
}

atp_h2h = {
    # Tiafoe leads H2H 6-1 / 7-1 (5-1 HC!) + Sat night Cinci crowd + Nakashima 3-week load -> ~56.5% Tiafoe!
    ("Frances Tiafoe", "Brandon Nakashima"): +54,
    # Fils super fresh (67m finish 3pm Sat) & blistering level vs Sat-night SF winner + US home crowd -> ~61.5-63% Fils!
    ("Arthur Fils", "Frances Tiafoe"): +25,     # diff = 63+25 = +88 -> 62.4% Fils
    ("Arthur Fils", "Brandon Nakashima"): +25,  # diff = 55+25 = +80 -> 61.3% Fils
}

atp_regimes = [
    ("Base (Fils fresh weapons ~62%, Tiafoe H2H 6-1/7-1 ~56.5%)", atp_elo, atp_h2h, 400.0, 0.45),
    ("Fils Dominant / Unstoppable Peak (~67-68% in Final)", {
        **atp_elo, "Arthur Fils": atp_elo["Arthur Fils"] + 38
    }, atp_h2h, 390.0, 0.20),
    ("US Crowd + First-Final Nerves for Fils (American wins ~45%)", {
        **atp_elo, "Arthur Fils": atp_elo["Arthur Fils"] - 35
    }, atp_h2h, 410.0, 0.20),
    ("Nakashima Red-Hot August Overrides Historical H2H (50/50 SF2)", {
        **atp_elo, "Brandon Nakashima": atp_elo["Brandon Nakashima"] + 25
    }, {**atp_h2h, ("Frances Tiafoe", "Brandon Nakashima"): +15}, 400.0, 0.15),
]

print("\n=== Q3 (372528) ATP CINCINNATI — SAT AUG 22 EVENING (EXHAUSTIVE 3 PLAYERS) ===")
for a, b in [("Frances Tiafoe", "Brandon Nakashima"), ("Arthur Fils", "Frances Tiafoe"), ("Arthur Fils", "Brandon Nakashima")]:
    print(f"  Base P({a:18s} d. {b:18s}) = {win_prob(a, b, atp_elo, atp_h2h):.3f}")

atp_blend = {}
for name, elos, h2h, sc, w in atp_regimes:
    r = solve_tree(atp_tree, elos, h2h, sc)
    print(f"  [{name:66s} w={w:.2f}] " + ", ".join(f"{k}:{v:.3f}" for k, v in sorted(r.items(), key=lambda x: -x[1])))
    for k, v in r.items():
        atp_blend[k] = atp_blend.get(k, 0.0) + w * v

print("FINAL ATP BLEND (sum =", round(sum(atp_blend.values()), 4), "):")
for k, v in sorted(atp_blend.items(), key=lambda x: -x[1]):
    print(f"  {k:20s}: {v:.4f}")


# ==============================================================================
# PART 4: Q4 (qid=772246) — US OPEN 2026 MIXED DOUBLES (UPDATED AUG 22)
# ==============================================================================
# New confirmed Aug 22 facts:
#   - Serena Williams & Carlos Alcaraz received a Wild Card ("Williams and Alcaraz" replaces WC_TBD_1!)
#   - Jessica Pegula & Taylor Fritz confirmed ("Pegula and Fritz" replaces "Rybakina and Fritz" as #2 seed!)
#   - Sabalenka & Djokovic explicitly re-confirmed! (Still rested -> p_play ~ 0.89!)
#   - Tiafoe still alive in Cinci SF Sat night (minor fatigue/WD drag on Fernandez & Tiafoe)

mixed_ratings = {
    "Sabalenka and Djokovic": 1950,
    "Pegula and Fritz": 1945,          # Replaced Rybakina/Fritz as #2 seed (Pegula in Cinci Final Sun!)
    "Shnaider and Medvedev": 1955,
    "Swiatek and Ruud": 1950,          # Swiatek lost Cinci SF Sat -> gets Sun-Mon rest
    "Bencic and Cobolli": 1875,        # Cobolli out of Cinci SF Sat afternoon
    "Anisimova and Tien": 1900,        # Rested
    "Errani and Vavassori": 2075,      # Defending champs, elite doubles specialists
    "Townsend and Zverev": 2025,       # Rested, elite doubles + top-5 singles
    "Fernandez and Tiafoe": 1925,      # Slight -15 fatigue/WD tweak due to Tiafoe Cinci SF/F run
    "Eala and Auger-Aliassime": 1940,  # Rested
    "Svitolina and Monfils": 1850,
    "Williams and Alcaraz": 1905,      # Confirmed Aug 22 WC! Elite Alcaraz + 44yo Serena (knee/rust)
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

def sim_mixed(ratings, scale=480.0, n_trials=150000, seed=201, bonus=0):
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
        "Svitolina and Monfils", "Williams and Alcaraz",
        "WC_TBD_2", "WC_TBD_3",
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
        br[15] = "Pegula and Fritz"
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

c1, e1 = sim_mixed(mixed_ratings, scale=480.0, n_trials=150000, seed=201, bonus=0)
c2, e2 = sim_mixed(mixed_ratings, scale=520.0, n_trials=150000, seed=202, bonus=-35)
c3, e3 = sim_mixed(mixed_ratings, scale=440.0, n_trials=150000, seed=203, bonus=+35)

blend_u89 = Counter()
blend_ce = Counter()
for k in set(c1) | set(c2) | set(c3):
    blend_u89[k] = 0.89 * (0.50 * c1.get(k, 0) + 0.30 * c2.get(k, 0) + 0.20 * c3.get(k, 0))
    blend_ce[k] = 0.50 * (c1.get(k, 0) / e1) + 0.30 * (c2.get(k, 0) / e2) + 0.20 * (c3.get(k, 0) / e3)

print("\n=== Q4 (772246) US OPEN MIXED DOUBLES (SAT AUG 22, p_play=0.89) ===")
for k, _ in blend_u89.most_common(10):
    print(f"  {k:28s}: uncond(0.89)={blend_u89[k]:.4f} | cond_elim={blend_ce[k]:.4f} | mid={0.5*(blend_u89[k]+blend_ce[k]):.4f}")
