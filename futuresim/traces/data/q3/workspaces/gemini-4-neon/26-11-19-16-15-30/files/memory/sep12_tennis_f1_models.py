import math

def american_to_prob(odds):
    return (-odds) / (-odds + 100.0) if odds < 0 else 100.0 / (odds + 100.0)

def decimal_to_prob(dec):
    return 1.0 / dec

def devig_mult(raw_dict):
    s = sum(raw_dict.values())
    return {k: v / s for k, v in raw_dict.items()}

def devig_power(raw_dict):
    lo, hi = 0.5, 5.0
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if sum(v ** mid for v in raw_dict.values()) > 1.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    return {p: v ** k for p, v in raw_dict.items()}, k

def devig_shin_2way(p1, p2):
    s = p1 + p2
    lo, hi = 0.0, 0.5
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        q1 = (math.sqrt(mid*mid + 4*(1-mid)*p1*p1/s) - mid) / (2*(1-mid))
        q2 = (math.sqrt(mid*mid + 4*(1-mid)*p2*p2/s) - mid) / (2*(1-mid))
        if q1 + q2 > 1.0:
            lo = mid
        else:
            hi = mid
    z = 0.5 * (lo + hi)
    q1 = (math.sqrt(z*z + 4*(1-z)*p1*p1/s) - z) / (2*(1-z))
    return q1, 1.0 - q1, z

def devig_shin_nway(raw_dict):
    """Exact multi-outcome Shin devigging (Shin 1993)."""
    s = sum(raw_dict.values())
    lo, hi = 0.0, 0.5
    for _ in range(100):
        z = 0.5 * (lo + hi)
        qs = [(math.sqrt(z*z + 4*(1-z)*p*p/s) - z) / (2*(1-z)) for p in raw_dict.values()]
        if sum(qs) > 1.0:
            lo = z
        else:
            hi = z
    z = 0.5 * (lo + hi)
    return {k: (math.sqrt(z*z + 4*(1-z)*p*p/s) - z) / (2*(1-z)) for k, p in raw_dict.items()}, z

def devig_2way_summary(name, o1, o2, is_prob=False):
    p1, p2 = (o1, o2) if is_prob else (american_to_prob(o1), american_to_prob(o2))
    m = p1 / (p1 + p2)
    sh, _, _ = devig_shin_2way(p1, p2)
    pw, _ = devig_power({"a": p1, "b": p2})
    avg = (m + sh + pw["a"]) / 3.0
    print(f"  {name:42s}: raw={p1:.4f}/{p2:.4f} (vig={p1+p2-1:+.4f}) | Mult={m:.4f} Shin={sh:.4f} Pow={pw['a']:.4f} | Avg={avg:.4f}")
    return avg

# ==============================================================================
# Q1 (891014): 2026 US OPEN MEN'S FINAL — ZVEREV vs SHELTON (Sun Sep 13, 2pm ET)
# ==============================================================================
print("=" * 105)
print("Q1 (891014): 2026 US OPEN MEN'S SINGLES FINAL — ALEXANDER ZVEREV vs BEN SHELTON (2-PLAYER EXHAUSTIVE)")
print("=" * 105)

# Live Sat Sep 12 Market Quotes (chronological):
# 1. Kalshi KXATP-26USO (5.74M total vol, 3.80M OI) & Match (494k vol, 87% retail on Shelton):
#    - 02:53 AM ET (OddsShopper): Zverev 56-57c (mid 56.5%), Shelton 43-44c (mid 43.5%)
#    - 10:20 AM ET (Covers):      Zverev 56%, Shelton 44%
#    - Later Sep 12 (LoserWins):  Zverev 58c / Shelton 43c -> mid = 0.575 (58/(58+43)=0.5743)
kal_early = 0.5650
kal_cov   = 0.5600
kal_late  = devig_2way_summary("Kalshi Later Sep 12 (58c / 43c)", 0.58, 0.43, is_prob=True)
kal_blend = 0.45 * kal_late + 0.35 * kal_early + 0.20 * kal_cov
print(f"  {'Kalshi Exchange Blended (early/10am/late)':42s}: {kal_blend:.4f}")

# 2. Sportsbooks (note strong upward move on Zverev from Friday night open to Saturday noon!):
dk_open = devig_2way_summary("DraftKings Fri Night Open (-132/+109)", -132, 109)
dk_fut  = devig_2way_summary("DraftKings 12:36am Title (-150/+123)", -150, 123)
dk_noon = devig_2way_summary("DraftKings Sat 12pm ET (-152/+124)", -152, 124)
fd_sat  = devig_2way_summary("FanDuel Sat Sep 12 (-146/+122)", -146, 122)

# 3. Fundamentals / H2H / Matchup Prior:
#    - Zverev 5-0 H2H (10 of 11 sets, 10 straight sets, 4-0 tiebreaks, won fast-HC Cincy & ATP Finals 2025)
#    - Zverev 88-18 vs lefties; TennisViz edge Return (7.4 vs 6.8), FH (8.0 vs 7.3), BH (8.1 vs 7.1), Serve tied (8.8)
#    - Zverev 6th Slam final (RG champ, Wim F, 24-2 Slams 2026), rested 3-0 Fri day vs Shelton 1st Slam final, 3:33am QF & Fri night 4-setter
#    - Counterweights: Shelton 25-6 (.806) HC 2026 > Zverev 23-7 (.767), beat Alcaraz, deeper return breaking 14x in 3 matches, huge Ashe crowd, Zverev 1-4 in Slam finals
#    - Retail flow note: 87% Kalshi match vol & Caesars/DK futures liability on Shelton -> market prices lean slightly Shelton-heavy vs sharp true prob!
fund_zverev = 0.590  # Conservative fundamental estimate (VSiN sharp Zachary Cohen values Zverev up to -160 / ~60-65%, tempered for Ashe/Shelton form)
print(f"  {'Fundamentals / H2H / Tactical Prior':42s}: {fund_zverev:.4f}")

# Weighted ensemble (heaviest weight on latest Sat noon sharp lines + deep Kalshi exchange + FanDuel + fundamentals):
#   35% Kalshi blended (0.5681) [deepest liquidity, though retail-heavy Shelton flow]
#   25% DraftKings Sat 12pm ET (-152/+124 -> 0.5767) [latest & sharpest sportsbook move]
#   20% FanDuel Sat Sep 12 (-146/+122 -> 0.5699)
#   5%  DraftKings Open (-132/+109 -> 0.5453) [stale open, tiny weight]
#   15% Fundamentals / H2H / Sharp Edge (0.5900)
zverev_ens = (
    0.35 * kal_blend
    + 0.25 * dk_noon
    + 0.20 * fd_sat
    + 0.05 * dk_open
    + 0.15 * fund_zverev
)
# Also check pure latest-market average (Kalshi late 57.5, DK noon 57.7, FD 57.0):
latest_mkt = (kal_late + dk_noon + fd_sat) / 3.0
print(f"\n  Pure Latest-Market Consensus (Kalshi late + DK noon + FD): Zverev = {latest_mkt:.4f}, Shelton = {1-latest_mkt:.4f}")
print(f"==> Q1 FULL ENSEMBLE: Alexander Zverev = {zverev_ens:.4f} ({zverev_ens*100:.2f}%), Ben Shelton = {1-zverev_ens:.4f} ({(1-zverev_ens)*100:.2f}%)")
print(f"    Clean rounded submission: Alexander Zverev = 0.575, Ben Shelton = 0.425 (sum = 1.000)")

# ==============================================================================
# Q2 (48458): 2026 F1 SPANISH GRAND PRIX AT MADRING — POST-QUALIFYING MODEL
# ==============================================================================
print("\n" + "=" * 105)
print("Q2 (48458): 2026 F1 SPANISH GP AT MADRING — POST-QUALIFYING MARKET DEVIG + RACE MODEL")
print("=" * 105)

# Market 1: Snai / Betpassion (Agipronews, Sat Sep 12 19:24 CEST) — Full Top 6!
#   Antonelli 2.25, Norris 2.50, Verstappen 7.50, Hamilton 9.00, Leclerc 12.00, Russell 16.00
#   Imputed tail (Piastri P7 ~ 30.0 / 3.33%, Lawson/Colapinto/Lindblad/field ~ 2.0%):
snai_raw = {
    "Kimi Antonelli": decimal_to_prob(2.25),  # 0.4444
    "Lando Norris":   decimal_to_prob(2.50),  # 0.4000
    "Max Verstappen": decimal_to_prob(7.50),  # 0.1333
    "Lewis Hamilton": decimal_to_prob(9.00),  # 0.1111
    "Charles Leclerc":decimal_to_prob(12.00), # 0.0833
    "George Russell": decimal_to_prob(16.00), # 0.0625
    "Oscar Piastri":  decimal_to_prob(30.00), # 0.0333
    "Other":          0.0200,
}
print(f"Snai/Betpassion raw sum = {sum(snai_raw.values()):.4f}")
snai_mult = devig_mult(snai_raw)
snai_pow, snai_k = devig_power(snai_raw)
snai_shin, snai_z = devig_shin_nway(snai_raw)
print(f"  Snai Power k = {snai_k:.4f}, Shin z = {snai_z:.4f}")

# Market 2: US Sportsbooks (TheLines.com, Sat Sep 12 post-qualy):
#   Norris +145 (2.45), Antonelli +145 (2.45), Verstappen +700 (8.00), Russell +1500 (16.00)
#   Imputing Hamilton (+850 -> 9.50), Leclerc (+1100 -> 12.00), Piastri (+3000 -> 31.0), Other (2.0%) consistent with Snai ratios:
us_raw = {
    "Lando Norris":   american_to_prob(145),   # 0.4082
    "Kimi Antonelli": american_to_prob(145),   # 0.4082
    "Max Verstappen": american_to_prob(700),   # 0.1250
    "Lewis Hamilton": american_to_prob(850),   # 0.1053 (imputed from Snai 9.00 ratio)
    "Charles Leclerc":american_to_prob(1100),  # 0.0833 (imputed from Snai 12.00)
    "George Russell": american_to_prob(1500),  # 0.0625
    "Oscar Piastri":  american_to_prob(3000),  # 0.0323 (imputed)
    "Other":          0.0200,
}
print(f"US Sportsbooks raw sum = {sum(us_raw.values()):.4f}")
us_mult = devig_mult(us_raw)
us_pow, us_k = devig_power(us_raw)
us_shin, us_z = devig_shin_nway(us_raw)
print(f"  US Power k = {us_k:.4f}, Shin z = {us_z:.4f}")

# Let's inspect all devig methods side by side!
drivers = ["Kimi Antonelli", "Lando Norris", "Max Verstappen", "Lewis Hamilton", "Charles Leclerc", "George Russell", "Oscar Piastri", "Other"]
print(f"\n{'Driver':17s} | {'US_Mult':7s} {'US_Pow':7s} {'US_Shin':7s} | {'Sn_Mult':7s} {'Sn_Pow':7s} {'Sn_Shin':7s} | {'Mkt_Avg':7s}")
mkt_avg = {}
for d in drivers:
    # For multi-outcome F1 markets (22 runners, strong favorite-longshot bias), Shin + Power are strictly better than naive Mult;
    # Use 40% Shin + 40% Power + 20% Mult within each book, and weight 60% US books + 40% Snai (reducing slight Italian Antonelli shade):
    us_c = 0.40 * us_shin[d] + 0.40 * us_pow[d] + 0.20 * us_mult[d]
    sn_c = 0.40 * snai_shin[d] + 0.40 * snai_pow[d] + 0.20 * snai_mult[d]
    mkt_avg[d] = 0.60 * us_c + 0.40 * sn_c
    print(f"{d:17s} | {us_mult[d]:7.4f} {us_pow[d]:7.4f} {us_shin[d]:7.4f} | {snai_mult[d]:7.4f} {snai_pow[d]:7.4f} {snai_shin[d]:7.4f} | {mkt_avg[d]:7.4f}")
print(f"Market Consensus Sum = {sum(mkt_avg.values()):.4f}")

# Now build an INDEPENDENT Fundamental Grid + Race-Pace + Street-Circuit Monte Carlo Simulation!
# Let's model Sunday's 2026 Spanish GP at Madring (new high-speed street circuit, 32C, high tyre deg, 2-3 stops, very hard on-track overtaking, high Safety Car / crash rate):
# Base grid win equity on low-overtaking street/hybrid circuit (like Hungary/Zandvoort/Singapore/Imola/Jeddah blended, adjusted for high tyre deg + 2-3 pit stops enabling undercut/overcut!):
# Wait: On pure Monaco (0 passing, 1 stop), P1 ~55%, P2 ~18%.
# On high-deg hard-passing circuits (Hungary/Zandvoort/Singapore with 2 stops & SC risk), P1 ~40-45%, P2 ~25-30%, P3 ~12-14%, P4 ~7-9%, P5 ~5-6%, P6 ~4-5%, P7 ~2%.
# Now adjust by car/driver race-pace & weekend specifics:
#   - Norris (P1, 1:31.824): HUGE clean-air & track-position advantage; won last 2 poles (Hungary/Zandvoort); BUT missed FP2 (zero high-fuel tyre-deg data!) & McLaren Friday long-run looked weak -> slight negative pace offset vs Antonelli, net ~36-38%!
#   - Antonelli (P2, +0.011s): 7 wins in 13 races (54% season win rate!), won Monza from P19, P1 FP2/FP3, superior Mercedes race pace & S3 battery edge, can win via T1 start OR 2-3 stop undercut/overcut OR SC -> net ~37-39%!
#   - Verstappen (P3, +0.140s): #2 Friday long-run pace (+0.13s/lap behind Russell, faster than Antonelli/Ferrari/McLaren!), topped Q2, elite racecraft & tyre management -> net ~11-12%!
#   - Hamilton (P4, +0.189s): Provisional pole Q3 Run 1, 7x WC racecraft, ahead of Leclerc & Russell; Ferrari Friday long-run +0.90s off Russell -> net ~7-8%!
#   - Leclerc (P5, +0.195s): Only 0.006s off Hamilton, fastest theoretical Friday lap; starts behind Hamilton & Verstappen on hard-to-pass track -> net ~5-6%!
#   - Russell (P6, +0.325s): #1 Friday long-run pace!! Huge SC/2-stop undercut threat in a Mercedes, BUT stuck in P6 behind both Ferraris & Verstappen on a circuit where Verstappen says "you can't pass" -> net ~4.5-5.5%!
#   - Piastri (P7, +0.470s): Bad Q3, bad Friday long run (+1.51s off Russell), stuck P7 -> ~1.5%!
#   - Field (P8-P22): ~1.0-1.5% (massive multi-car chaos / red flag fluke).
fund_f1 = {
    "Kimi Antonelli":  0.375,
    "Lando Norris":    0.365,
    "Max Verstappen":  0.115,
    "Lewis Hamilton":  0.068,
    "Charles Leclerc": 0.048,
    "George Russell":  0.046,  # Wait sum check!
    "Oscar Piastri":   0.013,
    "Other":           0.010,
}
s_f = sum(fund_f1.values())
fund_f1 = {k: v / s_f for k, v in fund_f1.items()}

# Blend 75% Multi-Book Devigged Market + 25% Independent Grid/Pace Fundamental Model:
f1_ens = {d: 0.75 * mkt_avg[d] + 0.25 * fund_f1[d] for d in drivers}
print(f"\n{'Driver':17s} | {'Mkt_75%':7s} | {'Fund_25%':8s} | {'ENSEMBLE':8s}")
for d in sorted(f1_ens, key=lambda x: -f1_ens[x]):
    print(f"{d:17s} | {mkt_avg[d]:7.4f} | {fund_f1[d]:8.4f} | {f1_ens[d]:8.4f}")

top5 = sorted(f1_ens.items(), key=lambda x: -x[1])[:5]
outside = sorted(f1_ens.items(), key=lambda x: -x[1])[5:]
print(f"\nTop 5 sum = {sum(v for _, v in top5):.4f}: {[(k, round(v, 3)) for k, v in top5]}")
print(f"Outside sum = {sum(v for _, v in outside):.4f}: {[(k, round(v, 3)) for k, v in outside]}")

# Check sensitivity of #5 spot (Leclerc vs Russell) under pure market vs pure US vs Snai:
print("\nSensitivity check for #5 slot (Charles Leclerc vs George Russell):")
print(f"  Snai raw:        Leclerc 12.00 (8.33%) vs Russell 16.00 (6.25%) -> Leclerc +{snai_raw['Charles Leclerc']-snai_raw['George Russell']:.4f}")
print(f"  Snai Shin/Pow:   Leclerc {0.5*(snai_shin['Charles Leclerc']+snai_pow['Charles Leclerc']):.4f} vs Russell {0.5*(snai_shin['George Russell']+snai_pow['George Russell']):.4f}")
print(f"  Ensemble:        Leclerc {f1_ens['Charles Leclerc']:.4f} vs Russell {f1_ens['George Russell']:.4f}")
print("  Note: Brier difference between submitting #5 at 0.055 vs 0.045 is tiny, and Leclerc starts P5 ahead of Russell P6 AND is 12.00 vs 16.00 on Snai -> Leclerc clearly belongs at #5!")
