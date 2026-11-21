import math

def am_to_p(o):
    return (-o)/(-o+100) if o < 0 else 100/(o+100)

si_odds = {
    "France": 370, "Argentina": 470, "England": 550, "Spain": 600,
    "Brazil": 1200, "Portugal": 1200, "Netherlands": 1600, "Germany": 1600,
    "Norway": 3300, "Colombia": 3500, "United States": 4000, "Morocco": 4500,
    "Mexico": 4500, "Belgium": 5000, "Japan": 5500, "Switzerland": 5500,
    "Senegal": 10000, "Ecuador": 12500, "Ivory Coast": 12500, "Croatia": 15000,
    "Egypt": 20000, "Canada": 22500, "Sweden": 22500, "Ghana": 25000,
    "Australia": 25000, "Austria": 40000, "Algeria": 40000, "Paraguay": 50000,
    "DR Congo": 200000, "Cape Verde": 250000, "Bosnia and Herzegovina": 250000, "South Africa": 250000,
}

raw = {k: am_to_p(v) for k, v in si_odds.items()}
lo, hi = 1.0, 2.0
for _ in range(60):
    mid = (lo+hi)/2
    if sum(p**mid for p in raw.values()) > 1.0:
        lo = mid
    else:
        hi = mid
k_pow = (lo+hi)/2
target = {t: p**k_pow for t, p in raw.items()}

# Exact locked bracket (pre-Canada-SA match, matching SI June 28 pre-KO odds)
# Tree structure:
# SF1 (Dallas):
#   QF_Boston (M97):
#     M89: (M74: Germany vs Paraguay) vs (M77: France vs Sweden)
#     M90: (M73: South Africa vs Canada) vs (M75: Netherlands vs Morocco)
#   QF_LA (M98):
#     M93: (M83: Portugal vs Croatia) vs (M84: Spain vs Austria)
#     M94: (M81: United States vs Bosnia and Herzegovina) vs (M82: Belgium vs Senegal)
# SF2 (Atlanta):
#   QF_Miami (M99):
#     M91: (M76: Brazil vs Japan) vs (M78: Ivory Coast vs Norway)
#     M92: (M79: Mexico vs Ecuador) vs (M80: England vs DR Congo)
#   QF_KC (M100):
#     M95: (M86: Argentina vs Cape Verde) vs (M88: Australia vs Egypt)
#     M96: (M85: Switzerland vs Algeria) vs (M87: Colombia vs Ghana)

BRACKET = [
    # SF1_Boston
    [[["Germany", "Paraguay"], ["France", "Sweden"]],
     [["South Africa", "Canada"], ["Netherlands", "Morocco"]]],
    # SF1_LA
    [[["Portugal", "Croatia"], ["Spain", "Austria"]],
     [["United States", "Bosnia and Herzegovina"], ["Belgium", "Senegal"]]],
    # SF2_Miami
    [[["Brazil", "Japan"], ["Ivory Coast", "Norway"]],
     [["Mexico", "Ecuador"], ["England", "DR Congo"]]],
    # SF2_KC
    [[["Argentina", "Cape Verde"], ["Australia", "Egypt"]],
     [["Switzerland", "Algeria"], ["Colombia", "Ghana"]]],
]

def exact_bracket_probs(elo, scale=400.0, venue_bonuses=True):
    def win_p(a, b, r_idx):
        # r_idx: 0=R32, 1=R16, 2=QF, 3=SF, 4=Final
        ba = bb = 0.0
        if venue_bonuses:
            if r_idx in (0, 1):
                if a == "Mexico": ba += 40
                if b == "Mexico": bb += 40
            if r_idx in (0, 1, 2, 3):
                if a == "United States": ba += 25
                if b == "United States": bb += 25
        return 1.0 / (1.0 + 10.0 ** (-((elo[a] + ba) - (elo[b] + bb)) / scale))

    def eval_node(node, r_idx):
        if isinstance(node, str):
            return {node: 1.0}
        left = eval_node(node[0], r_idx - 1)
        right = eval_node(node[1], r_idx - 1)
        res = {}
        for a, pa in left.items():
            for b, pb in right.items():
                p = win_p(a, b, r_idx)
                res[a] = res.get(a, 0.0) + pa * pb * p
                res[b] = res.get(b, 0.0) + pa * pb * (1.0 - p)
        return res

    qf_boston = eval_node(BRACKET[0], 2)
    qf_la = eval_node(BRACKET[1], 2)
    qf_miami = eval_node(BRACKET[2], 2)
    qf_kc = eval_node(BRACKET[3], 2)

    # SF1
    sf1 = {}
    for a, pa in qf_boston.items():
        for b, pb in qf_la.items():
            p = win_p(a, b, 3)
            sf1[a] = sf1.get(a, 0.0) + pa * pb * p
            sf1[b] = sf1.get(b, 0.0) + pa * pb * (1.0 - p)
    # SF2
    sf2 = {}
    for a, pa in qf_miami.items():
        for b, pb in qf_kc.items():
            p = win_p(a, b, 3)
            sf2[a] = sf2.get(a, 0.0) + pa * pb * p
            sf2[b] = sf2.get(b, 0.0) + pa * pb * (1.0 - p)
    # Final
    champ = {}
    for a, pa in sf1.items():
        for b, pb in sf2.items():
            p = win_p(a, b, 4)
            champ[a] = champ.get(a, 0.0) + pa * pb * p
            champ[b] = champ.get(b, 0.0) + pa * pb * (1.0 - p)
    return champ, sf1, sf2, qf_boston, qf_kc

# Fit Elo to match SI June 28 target championship probs AND FanDuel R32 lines!
elo = {t: 1900.0 for t in si_odds}
# Iterative multiplicative update
for it in range(400):
    champ, _, _, _, _ = exact_bracket_probs(elo, scale=400.0)
    mean_e = sum(elo.values()) / len(elo)
    for t in elo:
        ratio = target[t] / max(champ[t], 1e-9)
        elo[t] += 35.0 * math.log(ratio)
    # re-center so France = 2150
    shift = 2150.0 - elo["France"]
    for t in elo:
        elo[t] += shift

champ, sf1, sf2, qf_b, qf_kc = exact_bracket_probs(elo, scale=400.0)
print("FITTED MARKET-IMPLIED ELOS (anchored France=2150, scale=400):")
for t in sorted(elo, key=lambda x: -elo[x]):
    print(f"  {t:24s}: Elo={elo[t]:6.1f} | Target={target[t]:.4f} Fit={champ[t]:.4f}")

print("\nCHECK AGAINST FANDUEL R32 LINES:")
for a, b, fd_p in [("Canada", "South Africa", 0.736), ("Brazil", "Japan", 0.720), ("Germany", "Paraguay", 0.839), ("Netherlands", "Morocco", 0.622)]:
    p = 1.0 / (1.0 + 10.0 ** (-(elo[a] - elo[b]) / 400.0))
    print(f"  {a} vs {b}: Market-Elo P={p:.3f} vs FanDuel P={fd_p:.3f} (diff={elo[a]-elo[b]:+.1f})")
