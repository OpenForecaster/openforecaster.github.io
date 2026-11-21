import math
import random
from collections import Counter

# ==============================================================================
# PART A: Q2 (277746) SENSITIVITY CHECK (De Minaur vs Landaluce vs Zverev)
# ==============================================================================
from tennis_aug13_model import build_draw, base_elo, h2h_deltas, solve_tree

print("=== PART A: Q2 (277746) SENSITIVITY CHECK ===")
tree = build_draw(False, False)
for djo_e in [2055, 2070, 2085]:
    for adm_h2h in [-40, -20]:
        for land_e in [1780, 1805]:
            elos = {**base_elo, "Novak Djokovic": djo_e, "Martin Landaluce": land_e}
            old = h2h_deltas[("Alex de Minaur", "Novak Djokovic")]
            h2h_deltas[("Alex de Minaur", "Novak Djokovic")] = adm_h2h
            titles, elims = solve_tree(tree, elos, ["Novak Djokovic"])
            h2h_deltas[("Alex de Minaur", "Novak Djokovic")] = old
            cond = {k: v / (1 - titles["Novak Djokovic"]) for k, v in elims["Novak Djokovic"].items()}
            top6 = ", ".join(f"{k.split()[-1]}:{v:.3f}" for k, v in sorted(cond.items(), key=lambda x: -x[1])[:6])
            print(f"  djo={djo_e} adm_h2h={adm_h2h:3d} land={land_e} (DjoT={titles['Novak Djokovic']:.3f}) -> {top6}")

# ==============================================================================
# PART B: Q5 (891014) 2026 US OPEN MEN'S SINGLES — 2D BAYESIAN MIXTURE + BO5 SIM
# ==============================================================================
print("\n=== PART B: Q5 (891014) 2026 US OPEN MEN'S SINGLES ===")
# Sinner states (Aug 13 post-Cincy WD, Gazzetta: shockwave therapy, "almost certain" to play NY, flying ~Aug 17, 12d training, zero HC warmups):
#   - Near-Peak / Healthy:  0.64  (Elo 2285 BO5 — unstoppable hard court monster, already won Wimby w/ 0 warmups)
#   - Rusty / Mildly Knee-Limited: 0.27 (Elo 2160 BO5 — still elite but vulnerable to Zverev/Djoko/Alcaraz/hot server)
#   - WD / Mid-tournament Retirement: 0.09 (OUT)
sinner_states = [
    ("Healthy",     0.64, 2285),
    ("Limited",     0.27, 2160),
    ("WD_Retire",   0.09, None),
]

# Alcaraz states (Aug 13: out since Apr 14 [116d+], Gazzetta Aug 11: at 60% vs 80-90% threshold, trip "not on solid footing", Roddick "surprised if he rocks up", dropping to #3 seed):
#   - WD / Retires:          0.46 (OUT)
#   - Plays Rusty/75-80%:    0.40 (Elo 2135 BO5 — talented but 4.5 months off into BO5!)
#   - Plays Near-Peak:       0.14 (Elo 2255 BO5 — full Alcaraz)
alcaraz_states = [
    ("WD",          0.46, None),
    ("Rusty",       0.40, 2135),
    ("NearPeak",    0.14, 2255),
]

# Field BO5 US Open hard-court Elos (calibrated to 2026 results: Zverev RG champ + Wimby F + #2 seed; Djoko 4x USO champ; Fritz 2024 USO F + DC champ; Shelton Montreal F 10-0 sets + 2023 USO SF)
# Note: BO5 compresses upsets vs BO3! Effective Elo scale for BO5 is ~315 (instead of 400 for BO3):
#   e.g. +100 BO3 Elo -> p_bo3 = 0.640 -> per-set ~0.60 -> BO5 ~0.683 -> equivalent scale ~300-320!
def p_bo5(ea, eb):
    # Convert BO3 Elo diff to BO5 win prob via exact set-win prob mapping
    # Standard tennis calibration: Elo diff d with scale 400 gives BO3 win prob p3.
    # Solve p_s^2*(3 - 2*p_s) = p3 for single-set win prob p_s, then p5 = p_s^3*(10 - 15*p_s + 6*p_s^2)
    p3 = 1.0 / (1.0 + 10.0 ** (-(ea - eb) / 400.0))
    # Newton's method for p_s in [0,1]
    ps = p3
    for _ in range(8):
        f = ps*ps*(3 - 2*ps) - p3
        df = 6*ps*(1 - ps) + 1e-12
        ps = max(1e-6, min(1 - 1e-6, ps - f / df))
    return ps**3 * (10 - 15*ps + 6*ps*ps)

# Build realistic 128-player US Open field (with proper ATP 1-32 seeding structure!)
# Seeds 1-2 opposite halves; 3-4 drawn to SFs; 5-8 drawn to QFs; 9-16 R4; 17-32 R3; 33-128 unseeded
field_base = [
    # (Name, SeedTier, BO3_HC_Elo, is_US)
    ("Jannik Sinner",        1, 2285, False),
    ("Alexander Zverev",     2, 2135, False),  # Confirmed moving to #2 seed!
    ("Carlos Alcaraz",       3, 2255, False),  # Drops to #3 seed Mon Aug 17!
    ("Novak Djokovic",       4, 2110, False),  # 4x USO champ, BO5 beast
    ("Taylor Fritz",         5, 2065, True),   # Top-8 seed, 2024 USO F, DC champ
    ("Ben Shelton",          6, 2060, True),   # Top-8 seed, Montreal F 10-0 sets, 2023 USO SF
    ("Alex de Minaur",       7, 2025, False),
    ("Daniil Medvedev",      8, 2020, False),  # Former USO champ, BO5 bump despite Cincy slump
    ("Felix Auger-Aliassime",9, 1995, False),
    ("Rafael Jodar",        10, 2020, False),
    ("Lorenzo Musetti",     11, 1985, False),
    ("Jakub Mensik",        12, 2000, False),
    ("Learner Tien",        13, 1975, True),   # Montreal SF -> Top-16 seed!
    ("Andrey Rublev",       14, 1980, False),
    ("Jiri Lehecka",        15, 1985, False),
    ("Casper Ruud",         16, 1955, False),
    ("Tommy Paul",          17, 1975, True),   # Solid BO5 player, 17-24 seed
    ("Brandon Nakashima",   18, 1970, True),   # DC SF + Montreal F -> Top-20 seed!
    ("Frances Tiafoe",      19, 1965, True),   # 2x USO SF home magic vs hand surgery caution
    ("Arthur Fils",         20, 1980, False),
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
    ("Alex Michelsen",      32, 1915, True),   # US bubble seed
]
# Add 96 unseeded players including remaining US men!
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

def place_128_draw(players, rng):
    """Standard ATP 128-draw seeding placement."""
    # players sorted by rank/seed order (top 32 are seeds)
    seeds = players[:32]
    unseeded = players[32:]
    rng.shuffle(unseeded)
    bracket = [None] * 128
    # Seed 1 at 0, Seed 2 at 127
    bracket[0] = seeds[0]
    bracket[127] = seeds[1]
    # Seeds 3-4 at 63 or 64
    s34 = [seeds[2], seeds[3]]
    rng.shuffle(s34)
    bracket[63], bracket[64] = s34[0], s34[1]
    # Seeds 5-8 at {31, 32, 95, 96}
    s58 = list(seeds[4:8])
    rng.shuffle(s58)
    for pos, p in zip([31, 32, 95, 96], s58):
        bracket[pos] = p
    # Seeds 9-16 at {15, 16, 47, 48, 79, 80, 111, 112}
    s916 = list(seeds[8:16])
    rng.shuffle(s916)
    for pos, p in zip([15, 16, 47, 48, 79, 80, 111, 112], s916):
        bracket[pos] = p
    # Seeds 17-24 and 25-32 at remaining 8-blocks (positions 7,8,23,24,39,40,55,56,71,72,87,88,103,104,119,120)
    # Specifically in ATP draws, 17-24 play 9-16 in R3, 25-32 play 1-8 in R3:
    pos_25_32 = [7, 24, 39, 56, 71, 88, 103, 120]   # R3 against seeds 1-8!
    pos_17_24 = [8, 23, 40, 55, 72, 87, 104, 119]   # R3 against seeds 9-16!
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

# Precompute BO5 win prob lookup cache
def sim_us_open(n_trials_per_cell=4000, seed=42):
    rng = random.Random(seed)
    champ_probs = Counter()
    us_unique_probs = Counter()
    us_cond_probs = Counter()
    us_tie_rate = 0.0

    # Build generic unseeded pool
    non_us_unseeded = []
    for k in range(128 - 32 - len(us_unseeded)):
        # Rank 33..118 Elo tapers smoothly from 1915 down to 1715
        elo = 1915 - (k * 200.0 / (128 - 32 - len(us_unseeded)))
        non_us_unseeded.append((f"Field_{k}", elo, False))
    us_uns_list = [(n, e, True) for n, e in us_unseeded]

    for s_name, ps, s_elo in sinner_states:
        for a_name, pa, a_elo in alcaraz_states:
            w = ps * pa
            # Build active player list (removing WD players, shifting seeds up!)
            active = []
            for name, _, elo, is_us in field_base:
                if name == "Jannik Sinner":
                    if s_elo is None:
                        continue
                    active.append((name, s_elo, is_us))
                elif name == "Carlos Alcaraz":
                    if a_elo is None:
                        continue
                    active.append((name, a_elo, is_us))
                else:
                    active.append((name, elo, is_us))
            # Pad back to 128 if 1 or 2 WDs
            extra = []
            for k in range(32 - len(active)):
                pass
            pool = active + us_uns_list + non_us_unseeded
            while len(pool) < 128:
                pool.append((f"LL_{len(pool)}", 1710, False))
            pool = pool[:128]

            # Cache win probs by player index
            elos = [p[1] for p in pool]
            names = [p[0] for p in pool]
            is_us = [p[2] for p in pool]
            idxs = list(range(128))
            # Precompute p_bo5 matrix for fast lookup (only distinct Elo values!)
            p_cache = {}
            def get_p(i, j):
                key = (elos[i], elos[j])
                v = p_cache.get(key)
                if v is None:
                    v = p_bo5(elos[i], elos[j])
                    p_cache[key] = v
                return v

            c_cnt = Counter()
            u_uniq = Counter()
            u_ties = 0

            for _ in range(n_trials_per_cell):
                br = place_128_draw(idxs, rng)
                # Track rounds won by each US player
                us_rounds = {}
                cur = br
                rnd = 0
                while len(cur) > 1:
                    rnd += 1
                    nxt = []
                    for k in range(0, len(cur), 2):
                        a, b = cur[k], cur[k+1]
                        if rng.random() < get_p(a, b):
                            winner = a
                        else:
                            winner = b
                        nxt.append(winner)
                        if is_us[winner]:
                            us_rounds[winner] = rnd
                    cur = nxt
                champ = cur[0]
                c_cnt[names[champ]] += 1
                # Determine furthest US player
                if us_rounds:
                    max_r = max(us_rounds.values())
                    best_us = [u for u, r in us_rounds.items() if r == max_r]
                    if len(best_us) == 1:
                        u_uniq[names[best_us[0]]] += 1
                    else:
                        u_ties += 1
                else:
                    u_ties += 1

            for nm, cnt in c_cnt.items():
                champ_probs[nm] += w * cnt / n_trials_per_cell
            non_tie = n_trials_per_cell - u_ties
            us_tie_rate += w * u_ties / n_trials_per_cell
            for nm, cnt in u_uniq.items():
                us_unique_probs[nm] += w * cnt / n_trials_per_cell
                us_cond_probs[nm] += w * cnt / max(1, non_tie)

    print("Q5 (891014) US Open Men's Singles Winner TOP 10:")
    for k, v in champ_probs.most_common(10):
        print(f"  {k:24s}: {v:.4f}")
    print(f"  Top-5 sum = {sum(v for _, v in champ_probs.most_common(5)):.4f}")

    print(f"\nQ3 (408930) Furthest US Man (tie_rate={us_tie_rate:.3f}):")
    print("  [Conditional on unique furthest US man (if ties void / tiebreak)]:")
    for k, v in us_cond_probs.most_common(9):
        print(f"    {k:24s}: {v:.4f}")
    print(f"    Top-5 sum (cond) = {sum(v for _, v in us_cond_probs.most_common(5)):.4f}")
    print("  [Unconditional unique winner probability (if tie=no winner)]:")
    for k, v in us_unique_probs.most_common(9):
        print(f"    {k:24s}: {v:.4f}")
    print(f"    Top-5 sum (uncond) = {sum(v for _, v in us_unique_probs.most_common(5)):.4f}")

sim_us_open(n_trials_per_cell=6000)
