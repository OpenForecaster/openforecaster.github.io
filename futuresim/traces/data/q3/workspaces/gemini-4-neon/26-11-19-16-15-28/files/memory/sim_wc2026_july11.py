import random, math
from collections import Counter

# ==============================================================================
# STEP 0: EXACT VIG-FREE CONVERSION OF JULY 11 BETTING LINES
# ==============================================================================
def am_to_prob(odds):
    return (-odds / (-odds + 100.0)) if odds < 0 else (100.0 / (odds + 100.0))

def vig_free_2way(o1, o2):
    p1, p2 = am_to_prob(o1), am_to_prob(o2)
    s = p1 + p2
    prop = (p1 / s, p2 / s)
    # Power law: p1^k + p2^k = 1
    lo, hi = 1.0, 2.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if p1**mid + p2**mid > 1.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    pw = (p1**k, p2**k)
    return prop, pw, (0.5*(prop[0]+pw[0]), 0.5*(prop[1]+pw[1]))

print("=== JULY 11 CLOSING ODDS VIG-FREE ===")
for name, o1, o2 in [
    ("QF4 Yahoo ARG-SUI (-350/+265)", -350, +265),
    ("QF4 BleacherReport ARG-SUI (-325/+250)", -325, +250),
    ("QF4 FanDuel est (-320/+245)", -320, +245),
    ("QF3 Yahoo/BR closing ENG-NOR (-230/+184)", -230, +184),
    ("SF1 SI.com FRA-ESP (-144/+118)", -144, +118),
]:
    pr, pw, mid = vig_free_2way(o1, o2)
    print(f"  {name:42s}: prop={pr[0]:.4f}/{pr[1]:.4f}, pow={pw[0]:.4f}/{pw[1]:.4f}, mid={mid[0]:.4f}/{mid[1]:.4f}")

# Opta 90-min ARG 57.1%, Draw 24.2%, SUI 18.7% -> with ~60% ARG in ET+pens:
opta_arg = 0.571 + 0.242 * 0.60
print(f"  QF4 Opta Supercomputer (60/40 ET+pens)    : ARG={opta_arg:.4f} / SUI={1-opta_arg:.4f}")
# Consensus QF4 ARG-SUI: blend markets (avg mid ~0.738) with Opta (0.716) -> ~0.734 ARG / 0.266 SUI!

# ==============================================================================
# JULY 11, 2026 WORLD CUP SIMULATION — POST-QF3 (ENGLAND 2-1 NORWAY A.E.T.)
#
# LOCKED BRACKET:
# - SF1 (Dallas, Jul 14): France vs Spain (LOCKED; zero suspensions)
# - SF2 (Atlanta, Jul 15): England vs Winner(Argentina vs Switzerland)
#   * England beat Norway 2-1 in extra time (Schjelderup 36', Bellingham 45+2', 95')
#   * Norway ELIMINATED! (Haaland OUT at 7g/0a!)
#   * Jude Bellingham now 6g/1a (back-to-back KO braces!); Harry Kane 6g/1a (0g vs NOR)
#   * England SF2 factors: Quansah 2nd match ban (-3), 120-min Miami heat fatigue (-5 if
#     ARG/SUI finishes in 90m, ~76% of the time; 0 if ARG/SUI also goes to ET), minor
#     residual yellow-card check caution (-1.5) -> avg net ~ -8.3 Elo vs fresh opponent
#   * Note: Reece James & Bukayo Saka returned cleanly off the bench; Stones+Guehi sharp!
# ==============================================================================

# 1. MARKET-CALIBRATED ELO (anchored to Jul 10 post-QF2 DK/Kalshi + Jul 11 QF4 closing odds!)
# Check conditional Champion implied by Jul 10 DK/Kalshi:
# - DK: ENG 15.9% / 0.667 = 23.8%; ARG 17.2% / 0.735 = 23.4% -> ENG slightly ahead neutral!
# - Kalshi: ENG 15.1% / 0.644 = 23.4%; ARG 18.0% / 0.733 = 24.6% -> ARG slightly ahead neutral!
# - Avg: ARG ~24.0%, ENG ~23.6% neutral -> ARG ~2124 vs ENG ~2116 (neutral 51.1% ARG / 48.9% ENG)!
ELO_MARKET = {
    "France": 2194,
    "Spain": 2138,
    "Argentina": 2124,
    "England": 2114,      # -2 slight tick from drawing 90m vs Norway before ET win
    "Switzerland": 1970,  # Matches Jul 11 closing QF4 ~73.8% ARG / 26.2% SUI
}

# 2. BALANCED BAYESIAN + MARKET BLEND
ELO_BALANCED = {
    "France": 2190,
    "Spain": 2140,
    "Argentina": 2114,
    "England": 2098,
    "Switzerland": 1960,
}

# 3. PURE BAYESIAN / SPAIN-H2H FORM
ELO_BAYESIAN = {
    "France": 2178,
    "Spain": 2146,
    "Argentina": 2106,
    "England": 2084,
    "Switzerland": 1952,
}

# 4. UPSET-CONSERVATIVE
ELO_CONSERVATIVE = {
    "France": 2180,
    "Spain": 2134,
    "Argentina": 2100,
    "England": 2086,
    "Switzerland": 1960,
}

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=405.0, sigma=40.0,
            fra_sf1_net=2.5,       # +5 extra rest day (Jul 9 vs Jul 10) - 2.5 minor Mbappe ankle caution
            eng_sf_pen_fresh=-9.5, # Quansah ban (-3.5) + 120-min Miami heat fatigue (-4.5) + residual yellow caution (-1.5)
            eng_sf_pen_et=-5.0,    # If QF4 ARG-SUI also goes to ET (~24%), fatigue cancels!
            arg_kc_crowd=6,
            sui_fatigue_qf=-9,
            sui_inj_qf=-12,        # Manzambi OUT + Jaquez OUT + Aebischer doubtful
            sui_inj_late=-8,       # Manzambi + Xhaka/Zakaria yellow card risk if SUI advances
            messi_gpg=0.66, mbappe_gpg=0.88, kane_gpg=0.70, bell_gpg=0.53,
            mbappe_sf_miss=0.025,
            tp_rot_miss=0.08,
            win_goal_ratio=1.70,
            N=250000, seed=20260711):
    random.seed(seed)
    counts = {k: Counter() for k in [
        "QF_KC", "SF1_Dallas", "SF2_Atlanta",
        "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"
    ]}
    gb_wins = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    # Exact updated stats through QF3 (Jul 11):
    # Mbappe: 8g, 3a, 512 mins (2 guaranteed games: SF1 + FIN/3P)
    # Messi:  8g, 1a, 435 mins (QF4 + if win SF2+FIN/3P)
    # Kane:   6g, 1a, 555 mins (played 120m vs NOR; 2 guaranteed games)
    # Bellingham: 6g, 1a, 500 mins (subbed ~110m ET vs NOR; 2 guaranteed games)
    # Dembele: 5g, 2a, 510 mins (2 guaranteed games)
    # Oyarzabal: 4g, 1a, 495 mins (2 guaranteed games)
    players = [
        ("Kylian Mbappé", "France", 8, 3, mbappe_gpg, 0.28, 512),
        ("Lionel Messi", "Argentina", 8, 1, messi_gpg, 0.22, 435),
        ("Harry Kane", "England", 6, 1, kane_gpg, 0.16, 555),
        ("Jude Bellingham", "England", 6, 1, bell_gpg, 0.20, 500),
        ("Ousmane Dembélé", "France", 5, 2, 0.47, 0.28, 510),
        ("Mikel Oyarzabal", "Spain", 4, 1, 0.45, 0.18, 495),
        ("Johan Manzambi", "Switzerland", 3, 2, 0.30, 0.14, 340),
        ("Julián Álvarez", "Argentina", 2, 1, 0.44, 0.18, 390),
        ("Breel Embolo", "Switzerland", 2, 2, 0.36, 0.16, 440),
        ("Lamine Yamal", "Spain", 1, 1, 0.32, 0.34, 485),
        ("Mikel Merino", "Spain", 2, 0, 0.25, 0.10, 120),
        ("Field", "NONE", 0, 0, 0, 0, 350),
    ]

    # UPDATED GOLDEN BALL INTRA-TEAM SHARES AFTER QF3 (Bellingham's heroic 2nd straight KO brace!!):
    # - England: Bellingham now tied with Kane at 6 goals FROM MIDFIELD + back-to-back KO braces
    #   (2 vs Mexico w/ 10 men, 2 vs Norway incl. ET winner), while Kane went 0g in 120m & lost ball
    #   on Norway's goal! Bellingham surges to ~64% of England's share, Kane drops to ~27%, Other ~9%!
    # - Spain: Yamal officially won POTM vs Belgium despite 0 goals; Pedri was benched in QF2 ->
    #   Yamal ~46%, Rodri ~18%, Pedri ~12%, Fabian Ruiz ~9%, Oyarzabal ~7%, Other ~8%
    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.91), ("Other_ARG", 0.09)],
        "France": [("Kylian Mbappé", 0.70), ("Michael Olise", 0.16), ("Ousmane Dembélé", 0.10), ("Other_FRA", 0.04)],
        "Spain": [("Lamine Yamal", 0.46), ("Rodri", 0.18), ("Pedri", 0.12), ("Fabián Ruiz", 0.09), ("Mikel Oyarzabal", 0.07), ("Other_ESP", 0.08)],
        "England": [("Jude Bellingham", 0.64), ("Harry Kane", 0.27), ("Other_ENG", 0.09)],
        "Switzerland": [("Gregor Kobel", 0.38), ("Granit Xhaka", 0.36), ("Johan Manzambi", 0.10), ("Other_SUI", 0.16)],
    }

    # Star-power multiplier for Golden Ball voting:
    # England moves UP slightly (1.15 -> 1.24) because Bellingham's 6g back-to-back KO heroics create
    # a Messi/Mbappe-caliber superstar narrative!
    TEAM_STAR_MULT = {
        "Argentina": 1.42,
        "France": 1.42,
        "England": 1.24,
        "Spain": 1.00,
        "Switzerland": 0.80,
    }

    def base_p(a, b, ba=0, bb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ba) - (base_elo[b] + bb)) / scale))

    print(f"\n==================== {label} ====================")
    print(f"  Base: SF1 FRA-ESP={base_p('France','Spain',fra_sf1_net,0):.4f} | QF4 ARG-SUI={base_p('Argentina','Switzerland',arg_kc_crowd,sui_fatigue_qf+sui_inj_qf):.4f} | SF2 ENG-ARG(90m)={base_p('England','Argentina',eng_sf_pen_fresh,0):.4f} | SF2 ENG-SUI={base_p('England','Switzerland',eng_sf_pen_fresh,sui_inj_late):.4f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        team_matches = {}

        def play_ko(a, b, mod_a=0, mod_b=0, stage="KO"):
            p_a = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + mod_a) - (ELO[b] + mod_b)) / scale))
            a_won = (random.random() < p_a)
            team_matches.setdefault(a, []).append((base_elo[b], a_won, p_a, stage))
            team_matches.setdefault(b, []).append((base_elo[a], not a_won, 1.0 - p_a, stage))
            return (a, b) if a_won else (b, a)

        w97 = "France"
        w98 = "Spain"
        w99 = "England"  # LOCKED JULY 11: England 2-1 Norway (a.e.t.)!
        w100, _ = play_ko("Argentina", "Switzerland", mod_a=arg_kc_crowd, mod_b=sui_fatigue_qf + sui_inj_qf, stage="QF")
        qf4_went_et = (random.random() < 0.242)  # Opta 24.2% draw/ET prob

        counts["QF_KC"][w100] += 1
        for t in (w97, w98, w99, w100):
            counts["Reach_SF"][t] += 1

        w101, l101 = play_ko(w97, w98, mod_a=fra_sf1_net, mod_b=0, stage="SF")

        sf2_ma = eng_sf_pen_et if qf4_went_et else eng_sf_pen_fresh
        sf2_mb = sui_inj_late if w100 == "Switzerland" else 0
        w102, l102 = play_ko(w99, w100, mod_a=sf2_ma, mod_b=sf2_mb, stage="SF")

        counts["SF1_Dallas"][w101] += 1
        counts["SF2_Atlanta"][w102] += 1
        counts["Reach_Final"][w101] += 1
        counts["Reach_Final"][w102] += 1

        tp_mb = sui_inj_late if l102 == "Switzerland" else 0
        w103, l103 = play_ko(l101, l102, mod_a=0, mod_b=tp_mb, stage="3P")

        fin_mb = sui_inj_late if w102 == "Switzerland" else 0
        w104, l104 = play_ko(w101, w102, mod_a=0, mod_b=fin_mb, stage="FIN")

        counts["ThirdPlace"][w103] += 1
        counts["Champion"][w104] += 1

        # GOLDEN BOOT
        best_key = (-1, -1, -9999)
        best_name = None
        for pname, team, cg, ca, gpg, apg, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(1.2)
                key = (fg, poisson(0.8), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg; assists = ca; mins = gmins
            ms = list(team_matches.get(team, []))
            if pname == "Johan Manzambi":
                if len(ms) > 0 and ms[0][3] == "QF":
                    ms = ms[1:]
                if len(ms) > 0 and ms[0][3] == "SF" and random.random() < 0.70:
                    ms = ms[1:]
            # Small residual probability (~4%) Bellingham picked up an unreported booking in QF3
            if pname == "Jude Bellingham" and len(ms) >= 1 and random.random() < 0.04:
                ms = ms[1:]

            eff_ms = []
            for oe, won, p_win, stg in ms:
                if pname == "Kylian Mbappé" and stg == "SF":
                    mp = mbappe_sf_miss
                elif stg == "3P":
                    mp = tp_rot_miss * (0.65 if pname in ("Kylian Mbappé", "Lionel Messi", "Harry Kane", "Jude Bellingham") else 1.2)
                else:
                    mp = 0.045 if pname == "Lionel Messi" else 0.025
                if random.random() > mp:
                    eff_ms.append((oe, won, p_win, stg))

            eff_ng = len(eff_ms)
            if eff_ng > 0:
                mult = max(0.35, random.gauss(1.0, 0.25))
                exp_g = 0.0
                for oe, won, p_win, stg in eff_ms:
                    opp_mult = max(0.75, min(1.38, 1.0 + (1920.0 - oe) / 420.0))
                    if team == "France" and stg == "SF":
                        opp_mult *= 0.90
                    stg_mult = 1.12 if stg == "3P" else (0.92 if stg == "FIN" else 1.0)
                    mu = gpg * mult * opp_mult * stg_mult
                    denom = 1.0 + p_win * (win_goal_ratio - 1.0)
                    mu_adj = (mu * win_goal_ratio / denom) if won else (mu / denom)
                    exp_g += mu_adj
                goals += poisson(exp_g)
                assists += poisson(eff_ng * apg)
            mins += eff_ng * (85 if pname == "Lionel Messi" else 87)
            key = (goals, assists, -mins)
            if key > best_key:
                best_key = key; best_name = pname
        gb_wins[best_name] += 1

        # GOLDEN BALL MODEL 1: Team Finish
        r = random.random()
        if r < 0.56: gb_team = w104
        elif r < 0.86: gb_team = l104
        elif r < 0.95: gb_team = w103
        else: gb_team = l103
        shares = TEAM_SHARES.get(gb_team, [("Other_TEAM", 1.0)])
        u = random.random(); cum = 0.0
        for pl, sh in shares:
            cum += sh
            if u <= cum:
                gball_team_wins[pl] += 1
                break

        # GOLDEN BALL MODEL 2: Star-power + Golden Boot coupled
        f4_items = [(w104, 0.52), (l104, 0.31), (w103, 0.11), (l103, 0.06)]
        gb_winner_team = None
        for pname, team, *_ in players:
            if pname == best_name:
                gb_winner_team = team; break
        weights = []
        for t, bw in f4_items:
            sm = TEAM_STAR_MULT.get(t, 0.85)
            gb_bonus = 1.38 if t == gb_winner_team else 1.0
            weights.append((t, bw * sm * gb_bonus))
        tot_w = sum(x[1] for x in weights)
        u = random.random() * tot_w; cum = 0.0
        gb_team2 = w104
        for t, wt in weights:
            cum += wt
            if u <= cum:
                gb_team2 = t; break
        shares2 = list(TEAM_SHARES.get(gb_team2, [("Other_TEAM", 1.0)]))
        if gb_team2 == gb_winner_team and any(pl == best_name for pl, _ in shares2):
            adj = [(pl, sh * (1.80 if pl == best_name else 0.72)) for pl, sh in shares2]
            s_tot = sum(x[1] for x in adj)
            shares2 = [(pl, sh / s_tot) for pl, sh in adj]
        u = random.random(); cum = 0.0
        for pl, sh in shares2:
            cum += sh
            if u <= cum:
                gball_star_wins[pl] += 1
                break

    out = {}
    for key in ["QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final"]:
        out[key] = {t: cnt/N for t, cnt in counts[key].most_common(8)}
    out["GOLDEN_BOOT"] = {n: c/N for n, c in gb_wins.most_common(8)}
    out["GBALL_TEAM"] = {n: c/N for n, c in gball_team_wins.most_common(12)}
    out["GBALL_STAR"] = {n: c/N for n, c in gball_star_wins.most_common(12)}
    print("  SF1_Dallas :", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF1_Dallas"].items()))
    print("  SF2_Atlanta:", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF2_Atlanta"].items()))
    print("  ThirdPlace :", ", ".join(f"{k}:{v:.4f}" for k, v in list(out["ThirdPlace"].items())[:6]))
    print("  Champion   :", ", ".join(f"{k}:{v:.4f}" for k, v in list(out["Champion"].items())[:6]))
    print("  GOLDEN_BOOT:", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(6)))
    return out

r1 = run_sim("1. MARKET-CALIBRATED (45%)", ELO_MARKET, scale=405.0, sigma=38.0,
             fra_sf1_net=2.5, eng_sf_pen_fresh=-9.5, eng_sf_pen_et=-5.0,
             arg_kc_crowd=6, sui_fatigue_qf=-9, sui_inj_qf=-12, sui_inj_late=-8,
             messi_gpg=0.65, mbappe_gpg=0.88, kane_gpg=0.70, bell_gpg=0.54,
             mbappe_sf_miss=0.025, win_goal_ratio=1.68, N=250000)

r2 = run_sim("2. BALANCED BAYES+MARKET (30%)", ELO_BALANCED, scale=410.0, sigma=42.0,
             fra_sf1_net=2.5, eng_sf_pen_fresh=-10.0, eng_sf_pen_et=-5.0,
             arg_kc_crowd=6, sui_fatigue_qf=-9, sui_inj_qf=-12, sui_inj_late=-8,
             messi_gpg=0.67, mbappe_gpg=0.87, kane_gpg=0.70, bell_gpg=0.53,
             mbappe_sf_miss=0.025, win_goal_ratio=1.72, N=250000)

r3 = run_sim("3. PURE BAYESIAN / SPAIN-H2H (12.5%)", ELO_BAYESIAN, scale=410.0, sigma=44.0,
             fra_sf1_net=1.0, eng_sf_pen_fresh=-11.0, eng_sf_pen_et=-5.5,
             arg_kc_crowd=7, sui_fatigue_qf=-10, sui_inj_qf=-13, sui_inj_late=-9,
             messi_gpg=0.70, mbappe_gpg=0.86, kane_gpg=0.71, bell_gpg=0.52,
             mbappe_sf_miss=0.03, win_goal_ratio=1.78, N=200000)

r4 = run_sim("4. UPSET-CONSERVATIVE (12.5%)", ELO_CONSERVATIVE, scale=425.0, sigma=50.0,
             fra_sf1_net=0.0, eng_sf_pen_fresh=-8.5, eng_sf_pen_et=-4.5,
             arg_kc_crowd=4, sui_fatigue_qf=-8, sui_inj_qf=-11, sui_inj_late=-7,
             messi_gpg=0.65, mbappe_gpg=0.85, kane_gpg=0.68, bell_gpg=0.50,
             mbappe_sf_miss=0.035, win_goal_ratio=1.68, N=200000)

weights = [(r1, 0.45), (r2, 0.30), (r3, 0.125), (r4, 0.125)]
print("\n==================== JULY 11 WEIGHTED ENSEMBLE (45/30/12.5/12.5) ====================")
ens = {}
for key in ["QF_KC", "SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_SF", "Reach_Final", "GOLDEN_BOOT"]:
    agg = Counter()
    for res, wt in weights:
        for k, v in res[key].items():
            agg[k] += wt * v
    ens[key] = dict(agg)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in agg.most_common(8)))

agg_gb_sim = Counter()
for res, wt in weights:
    for k, v in res["GBALL_TEAM"].items():
        agg_gb_sim[k] += wt * 0.40 * v
    for k, v in res["GBALL_STAR"].items():
        agg_gb_sim[k] += wt * 0.60 * v
print("  GBALL_SIM   : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb_sim.most_common(12)))

# ==============================================================================
# BAYESIAN CONDITIONING OF JULY 10 MARKET CONSENSUS ON QF3 (ENG 2-1 NOR a.e.t.)
# ==============================================================================
# July 10 consensus market Champion (DK + Kalshi):
#   FRA 0.375, ESP 0.225, ARG 0.176, ENG 0.155, NOR 0.051, SUI 0.018
# Pre-QF3 market P(ENG beats NOR) = 0.660 (Jul 10 0.652 -> Jul 11 closing -230/+184 = 0.667)
# Exact Bayes conditional on ENG winning QF3 (before ET fatigue tweak):
#   ENG: 0.155 / 0.660 = 0.2348 -> with slight -1.2% 120-min Miami heat fatigue & 1-1 90m tick -> ~0.223
#   Now check relative conditional ratios from our Market Model (r1) vs Jul 10 Market Model:
#   In Jul 10 r1: FRA 0.370, ESP 0.233, ARG 0.176, ENG 0.149, NOR 0.049, SUI 0.023
#   Let's compute the exact Bayes shift implied by market-calibrated r1!
mkt_champ_bayes = {
    "France": 0.363,      # 0.375 * (r1_FRA_post / r1_FRA_pre) ~ 0.375 * 0.968
    "Spain": 0.218,       # 0.225 * 0.968
    "England": 0.224,     # 0.155 / 0.660 = 0.2348 minus ~1.1% ET heat fatigue
    "Argentina": 0.176 * 0.925,  # faces ENG 100% vs 66% ENG/34% NOR (~0.905), partly offset by QF4 firming +1% & ENG ET fatigue (+1.5%)
    "Switzerland": 0.018 * 0.85,
}
# Normalize exact Bayesian market to 1.000
s_m = sum(mkt_champ_bayes.values())
mkt_champ_bayes = {k: v/s_m for k, v in mkt_champ_bayes.items()}
print("\n  MARKET BAYES CHAMP:", ", ".join(f"{k}:{v:.4f}" for k, v in sorted(mkt_champ_bayes.items(), key=lambda x:-x[1])))
champ_blend = {t: 0.55 * mkt_champ_bayes[t] + 0.45 * ens["Champion"][t] for t in mkt_champ_bayes}
print("  CHAMPION BLEND (55% MktBayes / 45% Ens):", ", ".join(f"{t}:{v:.4f}" for t, v in sorted(champ_blend.items(), key=lambda x:-x[1])))

# GOLDEN BALL BAYESIAN MARKET UPDATE (conditioning Jul 10 market Bayes on ENG 2-1 NOR a.e.t. + Bellingham brace!)
# Jul 10 market Bayes was:
#   Mbappe 0.312, Messi 0.215, Haaland 0.077, Kane 0.070, Olise 0.062, Bellingham 0.058, Yamal 0.055, Dembele 0.036, Rodri 0.025, Pedri 0.022
# Condition on QF3 (ENG beat NOR; Haaland OUT 0.077 -> 0.000; England Reach_SF 0.66->1.00, Reach_Final 0.334->0.53, Champ 0.155->0.223):
# - England total market Golden Ball equity was Kane 0.070 + Bellingham 0.058 + other_ENG 0.012 = 0.140.
#   Conditional on ENG winning QF3 (0.660): 0.140 / 0.660 = 0.212!
#   Plus Bellingham's heroic 2nd straight KO brace (now 6g/1a tied with Kane from midfield!) boosts England's
#   star narrative slightly -> ~0.222 total England equity, split ~62% Bellingham (~0.138), ~29% Kane (~0.064), ~9% Other (~0.020)!
# - Haaland: 0.077 -> 0.001 (eliminated in QF, subbed off at 105')
# - Mbappe: slight -1.5% from ENG>NOR in Final, +2% from Haaland eliminated -> ~0.310
# - Messi: slight -5% from facing ENG 100% in SF2, +2% from Haaland eliminated -> ~0.206
# - Yamal: +8% from POTM vs Belgium confirmation & Haaland out, -1.5% from ENG>NOR -> ~0.059
# - Olise: ~0.061, Dembele ~0.036, Rodri ~0.026, Pedri ~0.022
mkt_gball_jul11 = {
    "Kylian Mbappé": 0.310,
    "Lionel Messi": 0.206,
    "Jude Bellingham": 0.138,
    "Harry Kane": 0.064,
    "Michael Olise": 0.061,
    "Lamine Yamal": 0.059,
    "Ousmane Dembélé": 0.036,
    "Rodri": 0.026,
    "Pedri": 0.022,
}
print("\n=== GOLDEN BALL BLEND (50% SIM / 50% MARKET BAYES) ===")
gb_blend = {}
for pl in set(list(mkt_gball_jul11.keys()) + list(agg_gb_sim.keys())):
    if pl.startswith("Other"): continue
    gb_blend[pl] = 0.50 * agg_gb_sim.get(pl, 0.0) + 0.50 * mkt_gball_jul11.get(pl, 0.0)
for pl, v in sorted(gb_blend.items(), key=lambda x:-x[1])[:10]:
    print(f"  {pl:18s}: Blend={v:.4f} (Sim={agg_gb_sim.get(pl,0):.4f}, Mkt={mkt_gball_jul11.get(pl,0):.4f})")
