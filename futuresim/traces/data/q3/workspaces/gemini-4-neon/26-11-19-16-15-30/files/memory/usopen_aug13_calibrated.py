import random
from collections import Counter

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

# Step 1: Verify calibration on Aug 5 Kalshi anchor!
# On Aug 5 (pre-Sinner knee, post-Alcaraz Cincy WD): Kalshi had Sinner=0.57, Alcaraz=0.12!
# With Sinner healthy Elo = 2360 (13,450 pts, 5/5 Masters 2026, Wimbledon champ w/ 0 warmups, 2024 USO champ)
# and Alcaraz healthy Elo = 2300 (AO 2026 champ), let's check both Aug 5 anchor and Aug 13 update!

field_base = [
    ("Jannik Sinner",        1, 2365, False),
    ("Alexander Zverev",     2, 2135, False),  # Confirmed moving to #2 seed Mon Aug 17!
    ("Carlos Alcaraz",       3, 2300, False),  # Drops to #3 seed Mon Aug 17!
    ("Novak Djokovic",       4, 2115, False),  # 4x USO champ, BO5 giant
    ("Taylor Fritz",         5, 2070, True),   # Top-8 seed, 2024 USO F, DC champ, rested
    ("Ben Shelton",          6, 2065, True),   # Top-8 seed, Montreal F (10-0 sets!), 3 titles in 2026, 2023 USO SF
    ("Alex de Minaur",       7, 2020, False),
    ("Daniil Medvedev",      8, 2020, False),
    ("Felix Auger-Aliassime",9, 1990, False),
    ("Rafael Jodar",        10, 2015, False),
    ("Lorenzo Musetti",     11, 1980, False),
    ("Jakub Mensik",        12, 2000, False),
    ("Learner Tien",        13, 1980, True),   # Montreal SF -> LOCKED Top-16 USO seed!
    ("Andrey Rublev",       14, 1980, False),
    ("Jiri Lehecka",        15, 1980, False),
    ("Casper Ruud",         16, 1955, False),
    ("Brandon Nakashima",   17, 1975, True),   # DC SF + Montreal F -> #16-20 USO seed, peak NA HC form!
    ("Tommy Paul",          18, 1975, True),   # #17-20 USO seed, strong BO5 floor
    ("Frances Tiafoe",      19, 1975, True),   # #17-20 USO seed, 2x USO SF Ashe boost vs hand cyst caution
    ("Arthur Fils",         20, 1975, False),
    ("Flavio Cobolli",      21, 1945, False),
    ("Joao Fonseca",        22, 1985, False),
    ("Karen Khachanov",     23, 1955, False),
    ("Ugo Humbert",         24, 1945, False),
    ("Tomas Machac",        25, 1940, False),
    ("Francisco Cerundolo", 26, 1910, False),
    ("Valentin Vacherot",   27, 1900, False),
    ("Luciano Darderi",     28, 1905, False),
    ("Matteo Berrettini",   29, 1930, False),
    ("Matteo Arnaldi",      30, 1910, False),
    ("Hubert Hurkacz",      31, 1925, False),
    ("Alex Michelsen",      32, 1915, True),
]
us_unseeded = [
    ("Sebastian Korda", 1915),
    ("Reilly Opelka", 1875),
    ("Jenson Brooksby", 1865),
    ("Marcos Giron", 1855),
    ("Aleksandar Kovacevic", 1850),
    ("Ethan Quinn", 1835),
    ("Zachary Svajda", 1820),
    ("J.J. Wolf", 1815),
    ("Nishesh Basavareddy", 1810),
    ("Mackenzie McDonald", 1810),
]
non_us_unseeded = [
    (f"Field_{k}", 1915 - (k * 200.0 / (128 - 32 - len(us_unseeded))), False)
    for k in range(128 - 32 - len(us_unseeded))
]
us_uns_list = [(n, e, True) for n, e in us_unseeded]

def run_mixture(label, sinner_states, alcaraz_states, n_trials=6000, seed=101):
    rng = random.Random(seed)
    champ_probs = Counter()
    us_cond = Counter()
    us_uncond = Counter()
    tie_rate = 0.0
    for sn, ps, se in sinner_states:
        for an, pa, ae in alcaraz_states:
            w = ps * pa
            active = []
            for name, _, elo, is_us in field_base:
                if name == "Jannik Sinner":
                    if se is None: continue
                    active.append((name, se, is_us))
                elif name == "Carlos Alcaraz":
                    if ae is None: continue
                    active.append((name, ae, is_us))
                else:
                    active.append((name, elo, is_us))
            pool = active + us_uns_list + non_us_unseeded
            while len(pool) < 128:
                pool.append((f"LL_{len(pool)}", 1710, False))
            pool = pool[:128]
            elos = [p[1] for p in pool]
            names = [p[0] for p in pool]
            is_us = [p[2] for p in pool]
            idxs = list(range(128))
            p_cache = {}
            def get_p(i, j):
                k = (elos[i], elos[j])
                v = p_cache.get(k)
                if v is None:
                    v = p_bo5(elos[i], elos[j])
                    p_cache[k] = v
                return v
            c_cnt = Counter()
            u_cnt = Counter()
            ties = 0
            for _ in range(n_trials):
                br = place_128_draw(idxs, rng)
                us_r = {}
                cur = br
                rnd = 0
                while len(cur) > 1:
                    rnd += 1
                    nxt = []
                    for k in range(0, len(cur), 2):
                        a, b = cur[k], cur[k+1]
                        winner = a if rng.random() < get_p(a, b) else b
                        nxt.append(winner)
                        if is_us[winner]:
                            us_r[winner] = rnd
                    cur = nxt
                c_cnt[names[cur[0]]] += 1
                if us_r:
                    mr = max(us_r.values())
                    best = [u for u, r in us_r.items() if r == mr]
                    if len(best) == 1:
                        u_cnt[names[best[0]]] += 1
                    else:
                        ties += 1
                else:
                    ties += 1
            for nm, cnt in c_cnt.items():
                champ_probs[nm] += w * cnt / n_trials
            nt = n_trials - ties
            tie_rate += w * ties / n_trials
            for nm, cnt in u_cnt.items():
                us_uncond[nm] += w * cnt / n_trials
                us_cond[nm] += w * cnt / max(1, nt)
    print(f"\n=== {label} ===")
    print("  Q5 Champion Top 8:")
    for k, v in champ_probs.most_common(8):
        print(f"    {k:24s}: {v:.4f}")
    print(f"  Q3 Furthest US (cond on unique; tie={tie_rate:.3f}) Top 8:")
    for k, v in us_cond.most_common(8):
        print(f"    {k:24s}: {v:.4f}")

# Check 1: Aug 5 Kalshi Anchor (Sinner 93/5/2, Alcaraz 40/40/20)
run_mixture(
    "ANCHOR CHECK: Aug 5 Kalshi (Target Sinner~0.57, Alcaraz~0.12)",
    [("Healthy", 0.93, 2365), ("Limited", 0.05, 2200), ("WD", 0.02, None)],
    [("WD", 0.40, None), ("Rusty", 0.42, 2145), ("NearPeak", 0.18, 2300)],
    n_trials=4000
)

# Check 2: Aug 13 Updated Posterior
# Sinner: official Cincy WD (right knee tendon inflammation, shockwave therapy), zero HC warmups,
#         Gazzetta Aug 11: USO attendance "almost certain", flying ~Aug 17 (12d training on NY courts)
#         -> Healthy/Full-by-Week2: 0.65 (Elo 2365), Mildly limited/rusty: 0.26 (Elo 2200), WD/Retire: 0.09
# Alcaraz: out since Apr 14 (116d+), Gazzetta Aug 11: at 60% vs 80-90% threshold, trip not on solid footing,
#          Roddick: "surprised if he rocks up", drops to #3 seed behind Zverev
#          -> WD/Retire: 0.48, Plays rusty/75-80%: 0.39 (Elo 2140), Plays near-peak: 0.13 (Elo 2300)
run_mixture(
    "AUG 13 UPDATED POSTERIOR (Sinner 65/26/9, Alcaraz 48/39/13)",
    [("Healthy", 0.65, 2365), ("Limited", 0.26, 2200), ("WD", 0.09, None)],
    [("WD", 0.48, None), ("Rusty", 0.39, 2140), ("NearPeak", 0.13, 2300)],
    n_trials=10000
)
