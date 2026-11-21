import random
import math
from collections import Counter, defaultdict

random.seed(20260718)

# =============================================================================
# 2026-07-18 UPDATES — POST-M103 (ENG 6-4 FRA) & FINAL EVE (ESP vs ARG)
# =============================================================================
# COMPLETED KNOCKOUT MATCHES & RESOLVED MARKETS:
# - M101 (Dallas, Jul 14): SPAIN 2-0 FRANCE — Oyarzabal 22' (pen, won by Yamal), Porro 58' (a: Olmo).
#     * Resolved qid 935518 = Spain.
# - M102 (Atlanta, Jul 15): ARGENTINA 2-1 ENGLAND — Gordon 55' (a: Rogers); Enzo Fernandez 85' (a: Messi),
#     Lautaro Martinez 90+2' (a: Messi). No ET. Resolved qid 439898 = Argentina.
# - Final Referee (Jul 16): Resolved qid 524604 = Slavko Vincic (SVN).
# - M103 3RD-PLACE PLAYOFF (Miami, Sat Jul 18): ENGLAND 6-4 FRANCE (COMPLETED!)
#     * Scorers: ENG — Declan Rice 3', Ezri Konsa, Bukayo Saka x3 (incl. 87' pen), Jude Bellingham 90+' (7th WC goal).
#                FRA — Kylian Mbappe 48', 66' (a: Olise) -> 10 GOALS AT WC2026 & 22 ALL-TIME RECORD!,
#                      Bradley Barcola 54', Ousmane Dembele 90+6' (6th WC goal).
#     * Michael Olise had 2 assists (WC record 7 assists). Kane & Bellingham started on bench (Bellingham came on & scored).
#     * GOLDEN BOOT STANDINGS LOCKED FOR NON-FINALISTS:
#         - Kylian Mbappe (FRA, DONE): 10g, 3a (743m; ~18% epistemic chance of uncredited 4th assist on Barcola/Dembele)
#         - Lionel Messi (ARG, Final left): 8g, 4a (661m) — NEEDS 2+ GOALS vs Spain (+ tiebreaker if 2g)!
#         - Erling Haaland (NOR, DONE): 7g (ELIMINATED)
#         - Jude Bellingham (ENG, DONE): 7g (ELIMINATED)
#         - Harry Kane (ENG, DONE): 6g (ELIMINATED)
#         - Ousmane Dembele (FRA, DONE): 6g (ELIMINATED)
#         - Mikel Oyarzabal (ESP, Final left): 5g, 1a (needs 5+ goals in Final -> <0.1%)
#
# - M104 FINAL (Sun Jul 19, 3pm ET, MetLife NJ): SPAIN vs ARGENTINA (qid=241292)
#     * July 18 Closing-Eve Markets & Models (slight +0.9% move toward Spain vs Jul 17):
#         - Polymarket ($123.5M vol, Bettors Insider Jul 18): Spain 59.15% / Arg 40.15% -> norm 59.57% / 40.43%.
#         - Polymarket "Team to Advance" ($911K 24h vol): Spain 59.5% / Arg 40.5%.
#         - FanDuel To Lift (Jul 18): ESP -156 / ARG +136 (was -150/+130) -> vig-free 58.99% / 41.01%.
#         - FanDuel 90m: ESP +130 / Draw +190 / ARG +270; BetMGM/DK 90m: +125/+200/+255; Kalshi 90m: +124/+197/+239.
#           Mean devigged 90m: 41.7% ESP / 31.9% Draw / 26.4% ARG -> Dixon-Coles (rho=-0.10) fit lam_ESP=1.21, lam_ARG=0.91.
#         - Opta Supercomputer (Al Jazeera Jul 18): 59.46% Spain / 40.54% Argentina (up from 57.8% Jul 17).
#     * July 18 Team News & Weather:
#         - De la Fuente confirmed Lamine Yamal in "perfect physical condition" after full training; only depth pieces
#           Yeremy Pino & Victor Munoz out. Spain allowed 1 GA in 7 games (0.31 xGA/gm, joint-lowest since 1966; 11 SOT).
#         - Argentina: Messi fit; Romero & Paredes recovered from cramps; De Paul & Montiel return to XI; Alvarez starts;
#           Facundo Medina doubt. Argentina 7-0-0 (14-game win streak, 19 GF) but played 2x ET & 1 fewer rest day.
#         - Sat NJ thunderstorms disrupted both teams' training (Spain moved indoors; Argentina delayed 45m) -> neutral.

ELO = {
    "Spain":     2104,  # +3 Jul 18 Polymarket 59.5% / FD -156 / Opta 59.46% / Yamal "perfect physical condition"
    "Argentina": 2041,  # -1 Jul 18 FD +136 / +270 90m drift
}

DIV = 415.0
REST_FINAL = 6.0   # Tue->Sun vs Wed->Sun + 0 ET for Spain vs 2x ET for Argentina

def pwin(t1, t2, div=DIV, bonus1=0.0):
    return 1.0 / (1.0 + 10.0 ** (-((ELO[t1] + bonus1) - ELO[t2]) / div))

m104 = {
    "Spain": pwin("Spain", "Argentina", DIV, REST_FINAL),
    "Argentina": 1.0 - pwin("Spain", "Argentina", DIV, REST_FINAL),
}

def show_exact(title, d, top=5):
    print(f"\n=== {title} ===")
    items = sorted(d.items(), key=lambda x: -x[1])
    tot = sum(p for _, p in items[:top])
    for i, (t, p) in enumerate(items[:top], 1):
        print(f"  {i:2d}. {t:18s}: {p*100:5.2f}%")
    print(f"  [Sum: {tot*100:.2f}%]")

show_exact("WORLD CUP CHAMPION M104 (241292) - JULY 18 CLOSING-EVE CALIBRATED", m104, 2)

# === JOINT COUPLED FINAL + GOLDEN BOOT + GOLDEN BALL SIMULATION (200k MC) ===
def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while True:
        k += 1; p *= random.random()
        if p <= L: return k - 1

def run_gb_mc(N=200000, lam_esp=1.24, lam_arg=0.95, messi_sh=0.475, oy_sh=0.33,
              shape=4.5, p_mb_4a=0.18, knock_p=0.03):
    gb_counts = Counter()
    stats = Counter()
    for _ in range(N):
        # Match tempo + player variance (overdispersed when shape is not None)
        gm_match = random.gammavariate(shape * 1.5, 1.0 / (shape * 1.5)) if shape else 1.0
        gm_messi = random.gammavariate(shape * 2.0, 1.0 / (shape * 2.0)) if shape else 1.0
        gm_oy    = random.gammavariate(shape * 2.0, 1.0 / (shape * 2.0)) if shape else 1.0
        if random.random() < knock_p:
            gm_messi *= 0.30
        if random.random() < knock_p:
            gm_oy *= 0.30

        # 90 minutes
        mg90 = poisson(lam_arg * messi_sh * gm_match * gm_messi)
        oa90 = poisson(lam_arg * (1.0 - messi_sh) * gm_match)
        ag90 = mg90 + oa90

        og90 = poisson(lam_esp * oy_sh * gm_match * gm_oy)
        oe90 = poisson(lam_esp * (1.0 - oy_sh) * gm_match)
        eg90 = og90 + oe90

        if mg90 >= 1: stats["m_gs_90"] += 1
        et = (ag90 == eg90)
        if et: stats["et"] += 1

        mg, og = mg90, og90
        if et:
            mg += poisson(lam_arg * messi_sh * 0.30 * gm_match * gm_messi)
            og += poisson(lam_esp * oy_sh * 0.30 * gm_match * gm_oy)

        if mg >= 1: stats["m_gs_tot"] += 1
        if mg >= 2: stats["m_2plus"] += 1
        if mg >= 3: stats["m_3plus"] += 1

        # Messi assists & minutes
        ma = 4 + poisson(0.32 * (1.30 if et else 1.0) * gm_match)
        m_mins = 661 + (120 if et else 90)

        # Oyarzabal assists & minutes
        oya = 1 + poisson(0.20 * (1.30 if et else 1.0) * gm_match)
        oy_mins = 575 + (110 if et else 82)

        # Mbappe locked at 10g (82% 3a / 18% 4a, 743m)
        mba = 4 if random.random() < p_mb_4a else 3
        mb_mins = 743

        cands = [
            ("Kylian Mbappe",   (10,     mba, -mb_mins)),
            ("Lionel Messi",    (8 + mg, ma,  -m_mins)),
            ("Mikel Oyarzabal", (5 + og, oya, -oy_mins)),
        ]
        winner = max(cands, key=lambda x: x[1])[0]
        gb_counts[winner] += 1

    label = f"OVERDISPERSED (k={shape})" if shape else "STANDARD POISSON"
    print(f"\n=== GOLDEN BOOT (201629) POST-M103 (Mbappe=10g) - {label} (N={N}) ===")
    for i, (name, c) in enumerate(gb_counts.most_common(5), 1):
        print(f"  {i:2d}. {name:20s}: {c/N*100:6.3f}%")
    print(f"  [Check: ET={stats['et']/N*100:.1f}%, Messi>=1(90m)={stats['m_gs_90']/N*100:.1f}%, "
          f"Messi>=2(tot)={stats['m_2plus']/N*100:.2f}%, Messi>=3(tot)={stats['m_3plus']/N*100:.2f}%]")
    return {k: v / N for k, v in gb_counts.items()}

gb_od = run_gb_mc(200000, lam_esp=1.26, lam_arg=0.98, messi_sh=0.49, shape=4.5, p_mb_4a=0.15)
gb_po = run_gb_mc(200000, lam_esp=1.26, lam_arg=0.98, messi_sh=0.49, shape=None, p_mb_4a=0.15)

# 75/25 blend favoring overdispersed (captures penalty + game-state correlation in Finals)
gb_blend = {k: 0.75 * gb_od.get(k, 0.0) + 0.25 * gb_po.get(k, 0.0)
            for k in ["Kylian Mbappe", "Lionel Messi", "Mikel Oyarzabal"]}
show_exact("GOLDEN BOOT (201629) - 75/25 OVERDISP/POISSON BLEND", gb_blend, 3)

# === GOLDEN BALL (581542) POST-M103 BAYESIAN UPDATE ===
# Prior Jul 17 (market-calibrated to Kalshi 90% Messi & FanDuel -1000 Messi / +600 Rodri / +2500 Yamal,Oyarzabal / +3300 Mbappe):
#   Messi 85.0%, Rodri 8.0%, Yamal 2.0%, Oyarzabal 2.0%, Mbappe 1.0%.
# July 18 causal updates:
#   1. Mbappe scored 2g vs England -> locked at 10g (first back-to-back Golden Boot likely, 90.5%) & 22 all-time WC record,
#      stripping Messi's Golden Boot halo (60% -> 9.4%). HOWEVER France LOST 6-4 (4-0 down at HT, 4th place), capping Mbappe's ceiling.
#   2. Conditional on Spain winning Final (~59.4%): Messi runner-up GB drops 76.5% -> 72.5% (-4.0pp pure causal effect
#      of losing Golden Boot to a 10g Mbappe), Spain champion player rises 21.5% -> 23.5% (Rodri lead), Mbappe rises 1.3% -> 3.5%
#      (Forlan 2010 4th-place outsider path if Spain wins ugly & Messi blanks).
#   3. Conditional on Argentina winning Final (~40.6%): Messi remains 98.5% * 99.0% = 97.5% lock.
esp_int = {
    "Rodri":           0.630,
    "Lamine Yamal":    0.150,
    "Mikel Oyarzabal": 0.150,
    "Unai Simon":      0.030,
    "Fabian Ruiz":     0.020,
    "Dani Olmo":       0.015,
    "Other_ESP":       0.005,
}
arg_int = {
    "Lionel Messi":      0.990,
    "Enzo Fernandez":    0.005,
    "Julian Alvarez":    0.003,
    "Emiliano Martinez": 0.002,
}
non_fin_int = {
    "Kylian Mbappe":   0.85,  # Boosted vs Bellingham after 10g + 22 all-time WC record
    "Jude Bellingham": 0.12,  # 7g, 3rd place England
    "Michael Olise":   0.03,  # Record 7 assists
}
assert abs(sum(esp_int.values()) - 1.0) < 1e-9
assert abs(sum(arg_int.values()) - 1.0) < 1e-9
assert abs(sum(non_fin_int.values()) - 1.0) < 1e-9

gb_ball = defaultdict(float)
p_esp = m104["Spain"]
p_arg = m104["Argentina"]

# Scenario 1: Spain wins Final (~59.4%)
for k, v in esp_int.items():     gb_ball[k] += p_esp * 0.235 * v
for k, v in arg_int.items():     gb_ball[k] += p_esp * 0.725 * v
for k, v in non_fin_int.items(): gb_ball[k] += p_esp * 0.040 * v

# Scenario 2: Argentina wins Final (~40.6%)
for k, v in arg_int.items():     gb_ball[k] += p_arg * 0.983 * v
for k, v in esp_int.items():     gb_ball[k] += p_arg * 0.010 * v
for k, v in non_fin_int.items(): gb_ball[k] += p_arg * 0.007 * v

show_exact("GOLDEN BALL (581542) - JULY 18 POST-M103 BAYESIAN MODEL", gb_ball, 8)
