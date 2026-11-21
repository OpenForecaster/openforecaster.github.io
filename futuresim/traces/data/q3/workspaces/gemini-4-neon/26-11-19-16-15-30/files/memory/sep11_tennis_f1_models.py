import math

def american_to_prob(odds):
    return (-odds) / (-odds + 100.0) if odds < 0 else 100.0 / (odds + 100.0)

def devig_mult(raw_dict):
    s = sum(raw_dict.values())
    return {k: v / s for k, v in raw_dict.items()}

def devig_power(raw_dict):
    lo, hi = 0.5, 5.0
    for _ in range(100):
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
    for _ in range(80):
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

def devig_2way_summary(name, o1, o2, is_prob=False):
    p1, p2 = (o1, o2) if is_prob else (american_to_prob(o1), american_to_prob(o2))
    m = p1 / (p1 + p2)
    sh, _, _ = devig_shin_2way(p1, p2)
    pw, _ = devig_power({"a": p1, "b": p2})
    avg = (m + sh + pw["a"]) / 3.0
    print(f"  {name:35s}: raw={p1:.4f}/{p2:.4f} (vig={p1+p2-1:+.4f}) | Mult={m:.4f} Shin={sh:.4f} Pow={pw['a']:.4f} | Avg={avg:.4f}")
    return avg

# ==============================================================================
# Q1 (608158): 2026 US OPEN WOMEN'S FINAL — SABALENKA vs RYBAKINA (Sat Sep 12)
# ==============================================================================
print("=" * 95)
print("Q1 (608158): 2026 US OPEN WOMEN'S SINGLES FINAL (Sabalenka vs Rybakina)")
print("=" * 95)

kal_wta = 0.575  # Kalshi KXWTA-26USO (715k/637k vol) & Match market: 57-58c / 42-43c
print(f"  {'Kalshi KXWTA-26USO (715k/637k vol)':35s}: bid/ask 57-58c / 42-43c => Mid={kal_wta:.4f}")
fd_late = devig_2way_summary("FanDuel Research Sep 11 (-146/+122)", -146, 122)
dk_1pm  = devig_2way_summary("DraftKings Sep 11 1pm (-145/+119)", -145, 119)
fd_early = devig_2way_summary("FanDuel earlier SI.com (-134/+114)", -134, 114)
dkp_wta = 0.560  # DraftKings Predictions (Covers 12:01pm ET) & RotoWire: 56% / 44%
print(f"  {'DK Predictions / RotoWire Sep 11':35s}: 56% / 44% => {dkp_wta:.4f}")
fund_wta = 0.560  # 10-7 overall, 7-7 HC, 2-0 last 2 (IW/Miami), 19-0 USO streak, DR 1.835 vs 1.389; tempered by AO26 final loss & Rybakina No.1
print(f"  {'Fundamentals/H2H/Form Prior':35s}: {fund_wta:.4f}")

# Weighted ensemble (heaviest weight on deep Kalshi exchange + live afternoon FD/DK lines):
#   35% Kalshi (0.575)
#   25% FanDuel latest (0.5697)
#   20% DraftKings 1pm (0.5657)
#   10% DK Predictions (0.5600)
#   10% Fundamentals/Early FD (avg 0.5556)
wta_sab = 0.35 * kal_wta + 0.25 * fd_late + 0.20 * dk_1pm + 0.10 * dkp_wta + 0.10 * (0.5 * fund_wta + 0.5 * fd_early)
print(f"\n==> Q1 ENSEMBLE: Aryna Sabalenka = {wta_sab:.4f} ({wta_sab*100:.2f}%), Elena Rybakina = {1-wta_sab:.4f} ({(1-wta_sab)*100:.2f}%)")
print(f"    Rounded submission: Aryna Sabalenka = 0.57, Elena Rybakina = 0.43")

# ==============================================================================
# Q2 (891014): 2026 US OPEN MEN'S SINGLES — ZVEREV IN FINAL! SF2 SHELTON vs TIAFOE
# ==============================================================================
print("\n" + "=" * 95)
print("Q2 (891014): 2026 US OPEN MEN'S SINGLES (Zverev def. Khachanov 6-3, 7-6, 7-6 -> ONLY 3 LEFT!)")
print("=" * 95)

print("SF2 Shelton vs Tiafoe (Sep 11 lines):")
sf2_kal = 0.725  # Kalshi Sep 11 morning: 73% / 28%
print(f"  {'Kalshi Sep 11 morning (73%/28%)':35s}: Mid={sf2_kal:.4f}")
sf2_dk  = devig_2way_summary("DraftKings Sep 11 (-344/+265)", -344, 265)
sf2_cbs = devig_2way_summary("CBS Sports Sep 11 (-310/+245)", -310, 245)
sf2_an  = devig_2way_summary("ActionNetwork/DK (-325/+253)", -325, 253)
sf2_rw  = 0.725  # RotoWire 73%/28%
p_sh_sf2 = 0.30 * sf2_kal + 0.30 * sf2_dk + 0.20 * sf2_cbs + 0.10 * sf2_an + 0.10 * sf2_rw
print(f"  --> SF2 Consensus: Ben Shelton = {p_sh_sf2:.4f}, Frances Tiafoe = {1-p_sh_sf2:.4f}")

# Pre-SF1 SF1 consensus (Zverev vs Khachanov, Sep 11):
sf1_dk = devig_2way_summary("SF1 DK Sep 11 (-458/+340)", -458, 340)
sf1_cbs = devig_2way_summary("SF1 CBS Sep 11 (-450/+340)", -450, 340)
sf1_kal = 0.800  # Kalshi Sep 11 morning: 80% Zverev
p_zv_sf1 = 0.45 * sf1_kal + 0.30 * sf1_dk + 0.25 * sf1_cbs
print(f"  --> Pre-SF1 Consensus: Zverev = {p_zv_sf1:.4f}, Khachanov = {1-p_zv_sf1:.4f}")

# Exact Bayes Conditioning of Pre-SF1 Futures Markets on Event {Zverev wins SF1}:
# Recall:
#   P(Z wins title | Z wins SF1) = P(Z wins title) / P(Z wins SF1)
#   P(S wins title) = p_sh_sf2 * [p_zv_sf1 * P(S>Z) + (1 - p_zv_sf1) * P(S>K)]
#   P(T wins title) = (1-p_sh_sf2) * [p_zv_sf1 * P(T>Z) + (1 - p_zv_sf1) * P(T>K)]
# Given P(S>K) ~ 0.745 and P(T>K) ~ 0.51 (from Elo & Sep 10 lines), we can invert EVERY pre-SF1 market!
def condition_on_zverev_sf1(label, futures_norm, p_z_sf1, p_s_sf2, p_s_over_k=0.745, p_t_over_k=0.515):
    pz_cond = futures_norm["Alexander Zverev"] / p_z_sf1
    # From S & T marginals, invert P(S>Z) and P(T>Z):
    ps_over_z = (futures_norm["Ben Shelton"] / p_s_sf2 - (1 - p_z_sf1) * p_s_over_k) / p_z_sf1
    pt_over_z = (futures_norm["Frances Tiafoe"] / (1 - p_s_sf2) - (1 - p_z_sf1) * p_t_over_k) / p_z_sf1
    ps_cond_raw = p_s_sf2 * ps_over_z
    pt_cond_raw = (1 - p_s_sf2) * pt_over_z
    # Also enforce exact sum = 1.0 using pz_cond and relative split of S vs T:
    rem = 1.0 - pz_cond
    st_sum = ps_cond_raw + pt_cond_raw
    ps_cond = rem * (ps_cond_raw / st_sum)
    pt_cond = rem * (pt_cond_raw / st_sum)
    print(f"  {label:30s}: Zverev={pz_cond:.4f}, Shelton={ps_cond:.4f} (P(S>Z)={ps_cond/p_s_sf2:.3f}), Tiafoe={pt_cond:.4f} (P(T>Z)={pt_cond/(1-p_s_sf2):.3f}) [raw_sum={pz_cond+st_sum:.4f}]")
    return {"Alexander Zverev": pz_cond, "Ben Shelton": ps_cond, "Frances Tiafoe": pt_cond}

kal11_raw = {"Alexander Zverev": 0.50, "Ben Shelton": 0.38, "Frances Tiafoe": 0.09, "Karen Khachanov": 0.06}
kal11_mult = devig_mult(kal11_raw)
kal11_pow, _ = devig_power(kal11_raw)

dkp10_raw = {"Alexander Zverev": 0.53, "Ben Shelton": 0.40, "Frances Tiafoe": 0.12, "Karen Khachanov": 0.06}
dkp10_avg = {k: 0.5*(devig_mult(dkp10_raw)[k] + devig_power(dkp10_raw)[0][k]) for k in dkp10_raw}

kn10_raw = {
    "Alexander Zverev": american_to_prob(113),
    "Ben Shelton": american_to_prob(150),
    "Frances Tiafoe": american_to_prob(809),
    "Karen Khachanov": american_to_prob(1567),
}
kn10_avg = {k: 0.5*(devig_mult(kn10_raw)[k] + devig_power(kn10_raw)[0][k]) for k in kn10_raw}

ut10 = {"Alexander Zverev": 0.454, "Ben Shelton": 0.345, "Frances Tiafoe": 0.123, "Karen Khachanov": 0.078}

print("\nExact Bayes-Conditioned Post-SF1 Title Probabilities (Given Zverev beat Khachanov 3-0):")
c_kal_m = condition_on_zverev_sf1("Kalshi Sep 11 (Mult)", kal11_mult, 0.800, sf2_kal)
c_kal_p = condition_on_zverev_sf1("Kalshi Sep 11 (Pow)",  kal11_pow,  0.800, sf2_kal)
c_dkp10 = condition_on_zverev_sf1("DK Predictions Sep 10", dkp10_avg, 0.800, 0.730)
c_kn10  = condition_on_zverev_sf1("KhelNow Sportsbook Sep 10", kn10_avg, 0.797, 0.730)
c_ut10  = condition_on_zverev_sf1("UniversTennis Sep 10", ut10, 0.778, 0.725)

# Direct Fundamental H2H/Form Final Model (Zverev rested 3-0, 5-0 H2H vs Shelton, 9-1 vs Tiafoe):
#   - P(Zverev beats Shelton) = 0.575 (5-0 H2H, 3-0 HC, RG champ / Wim F, rested vs Shelton night match & peak Alcaraz form)
#   - P(Zverev beats Tiafoe)  = 0.725 (9-1 H2H, vastly higher hold/dominance)
fund_atp = {
    "Alexander Zverev": p_sh_sf2 * 0.575 + (1 - p_sh_sf2) * 0.725,
    "Ben Shelton":      p_sh_sf2 * 0.425,
    "Frances Tiafoe":   (1 - p_sh_sf2) * 0.275,
}
print(f"  {'Fundamental Final Model':30s}: Zverev={fund_atp['Alexander Zverev']:.4f}, Shelton={fund_atp['Ben Shelton']:.4f} (P(S>Z)=0.425), Tiafoe={fund_atp['Frances Tiafoe']:.4f} (P(T>Z)=0.275)")

# Plus small +0.005 rest/straight-set bonus to Zverev in market-derived estimates?
# Wait: Zverev needed two tight tiebreaks (9-7, 8-6) against #50 Khachanov (had service streak broken),
# which slightly tempers straight-set fatigue benefit -> net performance/fatigue adjustment ~ +0.003 (tiny, within rounding).
atp_final = {}
for p in ["Alexander Zverev", "Ben Shelton", "Frances Tiafoe"]:
    kal_avg = 0.5 * (c_kal_m[p] + c_kal_p[p])
    atp_final[p] = (
        0.40 * kal_avg
        + 0.15 * c_dkp10[p]
        + 0.15 * c_kn10[p]
        + 0.05 * c_ut10[p]
        + 0.25 * fund_atp[p]
    )
print(f"\n==> Q2 ENSEMBLE (Exact 3-Player Post-SF1):")
for p, v in atp_final.items():
    print(f"    {p:20s}: {v:.4f} ({v*100:.2f}%)")
print(f"    Sum = {sum(atp_final.values()):.4f}")
print(f"    Implied P(Zverev beats Shelton) if P(Z>T)=0.725: {(atp_final['Alexander Zverev'] - (1-p_sh_sf2)*0.725)/p_sh_sf2:.4f}")

# ==============================================================================
# Q3 (48458): 2026 F1 SPANISH GRAND PRIX AT MADRING (Sun Sep 13)
# ==============================================================================
print("\n" + "=" * 95)
print("Q3 (48458): 2026 F1 SPANISH GP — BAYESIAN UPDATE FROM PRE-FP1 MARKET + FRI FP1/FP2 PACE")
print("=" * 95)

# 1. Pre-FP1 Market Prior (Fri Sep 11 7:15 AM ET Covers/Prediction Market blended with Sep 8-10 4-book consensus):
covers_raw = {
    "Kimi Antonelli": 0.34,
    "Lando Norris": 0.22,
    "George Russell": 0.15,
    "Lewis Hamilton": 0.11,
    "Max Verstappen": 0.09,
    "Charles Leclerc": 0.08,
    "Oscar Piastri": 0.06,
    "Other": 0.02,
}
covers_m = devig_mult(covers_raw)
covers_p, _ = devig_power(covers_raw)
sep10_prior = {
    "Kimi Antonelli": 0.295,
    "Lando Norris": 0.195,
    "George Russell": 0.165,
    "Lewis Hamilton": 0.095,
    "Charles Leclerc": 0.090,
    "Max Verstappen": 0.080,
    "Oscar Piastri": 0.055,
    "Other": 0.025,
}

# Pre-practice consensus prior (50% Fri 7:15am Covers avg mult/pow + 50% Sep 8-10 multi-book prior):
f1_prior = {}
for d in sep10_prior:
    cov = 0.5 * (covers_m[d] + covers_p[d])
    f1_prior[d] = 0.5 * cov + 0.5 * sep10_prior[d]
s_pr = sum(f1_prior.values())
f1_prior = {d: v/s_pr for d, v in f1_prior.items()}

# 2. Friday FP1/FP2 Evidence Likelihood Multipliers (tempered for Friday fuel-load noise,
#    new-circuit overnight setup evolution, and 1 FP3 session remaining before Sat Qualifying!):
#
#    Let's carefully decompose Friday signal into TWO independent sub-signals:
#      (a) Single-lap / Qualifying potential (HIGH weight at Madring: only 2 Straight Mode zones, hard overtaking!)
#          - Antonelli: P2 FP1 (+0.286s), P1 FP2 (1:33.662) -> strong positive (+1.18x)
#          - Russell: P1 FP1 (1:34.077 by 0.286s!), within 0.1s on mediums in FP2, aborted soft lap -> strong positive (+1.20x)
#          - Leclerc: P3 FP1, P2 FP2 (+0.113s), FASTEST theoretical lap (1:33.478) -> strong positive (+1.28x)
#          - Hamilton: P4 FP1, P3 FP2 (+0.149s) -> positive (+1.12x)
#          - Verstappen: P5 FP1, P6 FP2 (+0.401s, fastest S2) -> neutral/slightly negative (-0.95x)
#          - Norris: P6 FP1 (+0.870s), ZERO FP2 running (gearbox failure, no penalty expected, "big setback") -> big negative (0.58x)
#          - Piastri: P8 FP1 (footwell issue), P7 FP2 (+0.538s), McLaren slow all 3 sectors -> negative (0.65x)
#          - Other: Lindblad P4 FP2 (+0.228s, crashed), Ocon P9 -> slight positive (1.10x)
#      (b) Long-run / Race pace & Tyre deg management (Motorsport.com telemetry + Monza Mercedes sandbagging!):
#          - Russell: #1 fastest long run! (+1.30x)
#          - Verstappen: #2 fastest long run (+0.13s/lap! Only challenger close to Merc!) (+1.32x)
#          - Antonelli: #3 long run (+0.55s behind Russell, still 0.35s ahead of Ferrari & 0.96s ahead of McLaren; Merc S3 battery edge) (+1.15x)
#          - Leclerc: +0.90s/lap off Russell (disappointing long runs, but Ferrari can fix overnight) (0.85x)
#          - Hamilton: +0.90s/lap off Russell (same) (0.85x)
#          - Norris: ZERO long runs + McLaren Piastri +1.51s/lap off Russell! (0.65x)
#          - Piastri: +1.51s/lap off Russell! (0.55x)
#          - Other: Ocon +0.92s, midfield far back (0.85x)
#
#    Wait: On Friday of a BRAND-NEW circuit (where red flag cut long runs short and teams do major overnight setup work),
#    how much weight should Friday practice get vs Season-to-date Pre-Practice Prior?
#    Let's test TWO damping temperatures (Conservative beta=0.65, Moderate beta=0.85, Full beta=1.00)!
#    Combined raw multiplier L_i = L_qualy^0.55 * L_race^0.45 (since Madring overtaking is very hard, Qualy ~55% / Race pace ~45%)

L_qualy = {
    "Kimi Antonelli": 1.18,
    "George Russell": 1.22,
    "Charles Leclerc": 1.30,
    "Lewis Hamilton": 1.15,
    "Max Verstappen": 0.95,
    "Lando Norris":   0.52,
    "Oscar Piastri":  0.62,
    "Other":          1.05,
}
L_race = {
    "Kimi Antonelli": 1.15,
    "George Russell": 1.32,
    "Charles Leclerc": 0.85,
    "Lewis Hamilton": 0.85,
    "Max Verstappen": 1.35,
    "Lando Norris":   0.60,
    "Oscar Piastri":  0.52,
    "Other":          0.85,
}

# Wait — also check Mercedes team-level dominance signal!
# Combined Mercedes prior = ~46.5%. After topping BOTH FP1 (1-2) and FP2 (P1) AND crushing Ferrari (+0.9s) & McLaren (+1.5s) on long runs,
# plus Monza precedent (Merc jumped +0.8s from Fri to Sun!), what should combined Mercedes win prob be? ~56-60%!
print(f"\n{'Driver':18s} | {'Cov11':6s} | {'Sep10':6s} | {'Prior':6s} | {'L_raw':6s} | {'b=0.65':6s} | {'b=0.85':6s} | {'b=1.00':6s}")
post = {}
for beta in [0.65, 0.85, 1.00]:
    un = {}
    for d in f1_prior:
        L = (L_qualy[d] ** 0.55) * (L_race[d] ** 0.45)
        un[d] = f1_prior[d] * (L ** beta)
    s = sum(un.values())
    post[beta] = {d: v / s for d, v in un.items()}

for d in sorted(post[0.85], key=lambda x: -post[0.85][x]):
    L = (L_qualy[d] ** 0.55) * (L_race[d] ** 0.45)
    cov = 0.5 * (covers_m[d] + covers_p[d])
    print(f"{d:18s} | {cov:6.4f} | {sep10_prior[d]:6.4f} | {f1_prior[d]:6.4f} | {L:6.3f} | {post[0.65][d]:6.4f} | {post[0.85][d]:6.4f} | {post[1.00][d]:6.4f}")

for beta in [0.65, 0.85, 1.00]:
    merc = post[beta]["Kimi Antonelli"] + post[beta]["George Russell"]
    ferr = post[beta]["Charles Leclerc"] + post[beta]["Lewis Hamilton"]
    mcl  = post[beta]["Lando Norris"] + post[beta]["Oscar Piastri"]
    top5 = sorted(post[beta].items(), key=lambda x: -x[1])[:5]
    top5_sum = sum(v for _, v in top5)
    print(f"\nbeta={beta:.2f}: Merc={merc:.3f}, Ferr={ferr:.3f}, McL={mcl:.3f}, Ver={post[beta]['Max Verstappen']:.3f} | Top5 sum={top5_sum:.3f} ({[(k, round(v,3)) for k,v in top5]})")
