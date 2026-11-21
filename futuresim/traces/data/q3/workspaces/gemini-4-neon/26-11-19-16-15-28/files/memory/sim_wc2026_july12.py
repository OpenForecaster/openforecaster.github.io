import random, math
from collections import Counter

# ==============================================================================
# STEP 0: EXACT VIG-FREE CONVERSION OF ALL JULY 12, 2026 BETTING MARKETS
# ==============================================================================
def am_to_prob(odds):
    return (-odds / (-odds + 100.0)) if odds < 0 else (100.0 / (odds + 100.0))

def dec_to_prob(dec):
    return 1.0 / dec

def vig_free_probs(raw_probs):
    s = sum(raw_probs)
    prop = [p / s for p in raw_probs]
    # Power-law vig removal: sum(p_i^k) = 1
    lo, hi = 1.0, 2.5
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if sum(p**mid for p in raw_probs) > 1.0:
            lo = mid
        else:
            hi = mid
    k = 0.5 * (lo + hi)
    pw = [p**k for p in raw_probs]
    # Shin / midpoint blend (standard sharp market estimator)
    mid_p = [0.5 * (a + b) for a, b in zip(prop, pw)]
    return prop, pw, mid_p, s - 1.0

print("=== JULY 12, 2026 SF1 (FRANCE vs SPAIN) TO ADVANCE ===")
sf1_books = [
    ("Circa (SHARP)", [am_to_prob(-145), am_to_prob(+125)]),
    ("FanDuel",       [am_to_prob(-150), am_to_prob(+122)]),
    ("DraftKings/SI", [am_to_prob(-155), am_to_prob(+125)]),
]
sf1_mids = []
for name, rp in sf1_books:
    pr, pw, md, vig = vig_free_probs(rp)
    sf1_mids.append(md[0])
    print(f"  {name:18s} (vig {vig*100:4.2f}%): prop={pr[0]:.4f}/{pr[1]:.4f} | pow={pw[0]:.4f}/{pw[1]:.4f} | mid={md[0]:.4f}/{md[1]:.4f}")

print("\n=== JULY 12, 2026 SF1 (FRANCE vs SPAIN) 3-WAY -> ADVANCE (51.5% FRA in ET+pens) ===")
sf1_3way = [
    ("Kalshi",     [am_to_prob(+124), am_to_prob(+217), am_to_prob(+217)]),
    ("BetMGM",     [am_to_prob(+125), am_to_prob(+220), am_to_prob(+220)]),
    ("bet365",     [am_to_prob(+130), am_to_prob(+225), am_to_prob(+225)]),
    ("DK/FD RW",   [am_to_prob(+135), am_to_prob(+220), am_to_prob(+220)]),
    ("FD Res",     [am_to_prob(+130), am_to_prob(+210), am_to_prob(+230)]),
    ("Opta (Jul12)", [0.421, 0.261, 0.318]),
]
for name, rp in sf1_3way:
    pr, pw, md, vig = vig_free_probs(rp)
    adv_50 = md[0] + 0.50 * md[1]
    adv_52 = md[0] + 0.52 * md[1]
    print(f"  {name:14s} (vig {vig*100:4.2f}%): 90m={md[0]:.3f}/{md[1]:.3f}/{md[2]:.3f} -> Adv(50/50)={adv_50:.4f}, Adv(52/48)={adv_52:.4f}")

print("\n=== JULY 12, 2026 SF2 (ENGLAND vs ARGENTINA) TO ADVANCE ===")
sf2_books = [
    ("Circa (SHARP)",   [am_to_prob(-135), am_to_prob(+115)]),
    ("DraftKings/SI",   [am_to_prob(-135), am_to_prob(+110)]),
    ("FanDuel",         [am_to_prob(-134), am_to_prob(+110)]),
    ("Caesars",         [am_to_prob(-136), am_to_prob(+106)]),
    ("Sportscasting",   [am_to_prob(-130), am_to_prob(+106)]),
    ("BleacherReport",  [am_to_prob(-128), am_to_prob(+104)]),
    ("1xBet",           [dec_to_prob(1.77), dec_to_prob(2.05)]),
    ("Stake",           [dec_to_prob(1.73), dec_to_prob(2.07)]),
    ("TonyBet",         [dec_to_prob(1.74), dec_to_prob(2.01)]),
    ("ToonieBet",       [dec_to_prob(1.80), dec_to_prob(2.05)]),
    ("22Bet",           [dec_to_prob(1.77), dec_to_prob(2.03)]),
]
sf2_mids = []
for name, rp in sf2_books:
    pr, pw, md, vig = vig_free_probs(rp)
    sf2_mids.append(md[0])
    print(f"  {name:18s} (vig {vig*100:4.2f}%): prop={pr[0]:.4f}/{pr[1]:.4f} | pow={pw[0]:.4f}/{pw[1]:.4f} | mid={md[0]:.4f}/{md[1]:.4f}")
print(f"  --> Mean of 11 books: ENG={sum(sf2_mids)/len(sf2_mids):.4f} / ARG={1 - sum(sf2_mids)/len(sf2_mids):.4f}")
print(f"  --> Sharp/US top4 (Circa,DK,FD,Caesars): ENG={sum(sf2_mids[:4])/4:.4f} / ARG={1 - sum(sf2_mids[:4])/4:.4f}")

print("\n=== JULY 12, 2026 SF2 3-WAY -> ADVANCE (48.5% ENG in ET+pens due to Emi Martinez pens) ===")
sf2_3way = [
    ("SI/DK",       [am_to_prob(+155), am_to_prob(+200), am_to_prob(+205)]),
    ("FanDuel",     [am_to_prob(+155), am_to_prob(+195), am_to_prob(+210)]),
    ("Sportscast",  [am_to_prob(+160), am_to_prob(+190), am_to_prob(+210)]),
    ("Caesars",     [am_to_prob(+146), am_to_prob(+200), am_to_prob(+200)]),
    ("1xBet",       [dec_to_prob(2.62), dec_to_prob(3.16), dec_to_prob(3.16)]),
    ("Stake",       [dec_to_prob(2.50), dec_to_prob(3.05), dec_to_prob(3.00)]),
]
for name, rp in sf2_3way:
    pr, pw, md, vig = vig_free_probs(rp)
    adv_50 = md[0] + 0.50 * md[1]
    adv_485 = md[0] + 0.485 * md[1]
    print(f"  {name:14s} (vig {vig*100:4.2f}%): 90m={md[0]:.3f}/{md[1]:.3f}/{md[2]:.3f} -> Adv(50/50)={adv_50:.4f}, Adv(48.5)={adv_485:.4f}")

print("\n=== JULY 12, 2026 WORLD CUP CHAMPION ODDS (SI / DraftKings) ===")
champ_raw = [am_to_prob(+150), am_to_prob(+320), am_to_prob(+340), am_to_prob(+360)]
pr, pw, md, vig = vig_free_probs(champ_raw)
teams_c = ["France", "Spain", "England", "Argentina"]
for t, p1, p2, m in zip(teams_c, pr, pw, md):
    print(f"  {t:10s}: prop={p1:.4f} | pow={p2:.4f} | mid={m:.4f}")
print(f"  Total vig: {vig*100:.2f}%")

# ==============================================================================
# STEP 1: JOINT 4-TEAM BRACKET + THIRD-PLACE + GOLDEN BOOT + GOLDEN BALL SIM
#
# LOCKED FINAL FOUR (July 12, 2026):
# - SF1 (Dallas, Jul 14): France vs Spain
#   * Market consensus (Circa 57.1%, FD 57.3%, DK 57.8%, Kalshi 3way ~56.3%): ~57.2% FRA / 42.8% ESP
#   * Opta: 55.2% FRA (90m 42.1/26.1/31.8), AJ blurb 53%
# - SF2 (Atlanta, Jul 15): England vs Argentina
#   * Market consensus (Circa 55.2%, DK 54.7%, FD 54.6%, Caesars 54.4%, 11-book avg 54.2%): ~54.5% ENG / 45.5% ARG
#   * Opta: 50.94% ENG / 49.06% ARG
#   * Fundamentals: BOTH went 120m on Saturday Jul 11 (Argentina has played TWO 120m KO games;
#     Messi visibly fatigued; Argentina conceded 6 goals in 3 KO games vs Cape Verde/Egypt/Switzerland
#     and only beat 10-man Switzerland in 112'; England has Quansah banned [Konsa/James available]
#     and Declan Rice recovering from midweek illness + minor Tuchel-Bellingham media spat,
#     while Argentina gets strong Atlanta pro-Argentina crowd + Emi Martinez shootout edge).
# ==============================================================================

# 1. MARKET-CALIBRATED ELO (matches Circa/DK/FD SF1 ~57.2%, SF2 ~54.5%, DK Champion ~37.3/21.9/20.9/19.9)
ELO_MARKET = {
    "France":    2196,
    "Spain":     2142,
    "England":   2122,
    "Argentina": 2092,  # +5 Atlanta crowd -> net ENG +25 -> ~53.6-54.2% ENG!
}

# 2. BALANCED MARKET + FUNDAMENTAL/OPTA BLEND
ELO_BALANCED = {
    "France":    2190,
    "Spain":     2142,
    "England":   2116,
    "Argentina": 2096,  # +6 Atlanta crowd -> ~52.3-52.8% ENG
}

# 3. OPTA / SPAIN-DEFENSE & ARGENTINA-PEDIGREE MODEL
ELO_OPTA = {
    "France":    2180,
    "Spain":     2152,  # Opta has Spain 27% champ vs France 33%!
    "England":   2104,
    "Argentina": 2098,  # Opta has ENG 50.94% vs ARG 49.06%
}

# 4. UPSET-CONSERVATIVE / HIGH-VARIANCE MODEL
ELO_CONSERVATIVE = {
    "France":    2182,
    "Spain":     2138,
    "England":   2112,
    "Argentina": 2094,
}

def poisson(lam):
    if lam <= 0: return 0
    L = math.exp(-lam)
    k = 0; p = 1.0
    while p > L:
        k += 1; p *= random.random()
    return k - 1

def run_sim(label, base_elo, scale=405.0, sigma=38.0,
            fra_sf1_mod=3.0,    # +1 rest day (Jul 9 vs Jul 10) minus slight Mbappe/Tchouameni knock caution
            eng_sf2_mod=3.0,    # +7 fresher than double-ET Argentina minus -4 Atlanta Argentina crowd & Rice/Quansah
            # Calibrated DIRECTLY to July 12 FanDuel Anytime Goalscorer odds (incl. ET):
            #   Mbappe +115 (~42.5% -> lam_SF1 ~0.56 vs Spain; vs ENG/ARG in Fin/3P ~0.72-0.85 -> avg base ~0.76)
            #   Kane   +120 (~41.5% -> lam_SF2 ~0.54 vs ARG; vs FRA/ESP ~0.55-0.70 -> avg base ~0.64)
            #   Messi  +130 (~39.5% -> lam_SF2 ~0.50 vs ENG; vs FRA/ESP ~0.52-0.66 -> avg base ~0.59)
            #   Bellingham +750 first (~18-20% anytime? No, +750 first ~11% first -> ~26-28% anytime -> lam ~0.35-0.42!)
            mbappe_base=0.76, messi_base=0.58, kane_base=0.64, bell_base=0.40,
            mbappe_sf_miss=0.03, messi_sf_miss=0.03, tp_rot_miss=0.08,
            win_goal_ratio=1.65, N=300000, seed=20260712):
    random.seed(seed)
    counts = {k: Counter() for k in ["SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final"]}
    gb_wins = Counter()
    gb_tie_breaks = Counter()
    gball_team_wins = Counter()
    gball_star_wins = Counter()

    # Exact post-QF4 tournament stats (July 12, 2026):
    # Mbappe:     8g, 3a, 512 mins (2 games left: SF1 + FIN/3P)
    # Messi:      8g, 2a, 555 mins (0g, +1a, +120m vs SUI! 2 games left: SF2 + FIN/3P)
    # Kane:       6g, 1a, 555 mins (2 games left: SF2 + FIN/3P)
    # Bellingham: 6g, 1a, 500 mins (2 games left: SF2 + FIN/3P; confirmed NO suspension!)
    # Dembele:    5g, 2a, 510 mins (2 games left: SF1 + FIN/3P)
    # Oyarzabal:  4g, 1a, 495 mins (2 games left: SF1 + FIN/3P)
    # Alvarez:    3g, 1a, 510 mins (+1g vs SUI)
    # Lautaro:    2g, 0a, 240 mins (+1g vs SUI)
    # Yamal:      1g, 1a, 485 mins
    # Merino:     2g, 0a, 120 mins
    players = [
        ("Kylian Mbappé",   "France",    8, 3, mbappe_base, 0.28, 512),
        ("Lionel Messi",    "Argentina", 8, 2, messi_base,  0.24, 555),
        ("Harry Kane",      "England",   6, 1, kane_base,   0.16, 555),
        ("Jude Bellingham", "England",   6, 1, bell_base,   0.20, 500),
        ("Ousmane Dembélé", "France",    5, 2, 0.42,        0.26, 510),
        ("Mikel Oyarzabal", "Spain",     4, 1, 0.40,        0.16, 495),
        ("Julián Álvarez",  "Argentina", 3, 1, 0.42,        0.18, 510),
        ("Lamine Yamal",    "Spain",     1, 1, 0.28,        0.30, 485),
        ("Field",           "NONE",      0, 0, 0,           0,    350),
    ]

    # GOLDEN BALL INTRA-TEAM SHARES (updated July 12):
    # - Argentina: Messi 8g/2a (still overwhelmingly Argentina's narrative ~89%, Alvarez/Mac Allister/Emi ~11%)
    # - France: Mbappe 8g/3a (~68%), Olise tournament-high 6 assists chasing Pele's record (~18%!), Dembele 5g (~10%), Other (~4%)
    # - Spain: Yamal POTM vs Belgium (~44%, tempered slightly by only 1g & quiet tournament noted by FanDuel/AJ),
    #          Rodri (~19%), Pedri (~12%), Fabian Ruiz (~9%), Oyarzabal (~8%), Merino/Other (~8%)
    # - England: Bellingham 6g/1a back-to-back KO braces (~65%!), Kane 6g/1a (~26%), Rice/Saka/Pickford (~9%)
    TEAM_SHARES = {
        "Argentina": [("Lionel Messi", 0.89), ("Julián Álvarez", 0.05), ("Other_ARG", 0.06)],
        "France":    [("Kylian Mbappé", 0.68), ("Michael Olise", 0.18), ("Ousmane Dembélé", 0.10), ("Other_FRA", 0.04)],
        "Spain":     [("Lamine Yamal", 0.44), ("Rodri", 0.19), ("Pedri", 0.12), ("Fabián Ruiz", 0.09), ("Mikel Oyarzabal", 0.08), ("Other_ESP", 0.08)],
        "England":   [("Jude Bellingham", 0.65), ("Harry Kane", 0.26), ("Other_ENG", 0.09)],
    }

    TEAM_STAR_MULT = {
        "Argentina": 1.40,
        "France":    1.42,
        "England":   1.26,
        "Spain":     0.98,
    }

    def bp(a, b, ma=0, mb=0):
        return 1.0 / (1.0 + 10.0 ** (-((base_elo[a] + ma) - (base_elo[b] + mb)) / scale))

    print(f"\n==================== {label} ====================")
    print(f"  Base: SF1 FRA-ESP={bp('France','Spain',fra_sf1_mod,0):.4f} | SF2 ENG-ARG={bp('England','Argentina',eng_sf2_mod,0):.4f}")

    for _ in range(N):
        ELO = {t: r + random.gauss(0, sigma) for t, r in base_elo.items()}
        team_matches = {}

        def play_ko(a, b, mod_a=0, mod_b=0, stage="KO"):
            p_a = 1.0 / (1.0 + 10.0 ** (-((ELO[a] + mod_a) - (ELO[b] + mod_b)) / scale))
            a_won = (random.random() < p_a)
            team_matches.setdefault(a, []).append((b, base_elo[b], a_won, p_a, stage))
            team_matches.setdefault(b, []).append((a, base_elo[a], not a_won, 1.0 - p_a, stage))
            return (a, b) if a_won else (b, a)

        w101, l101 = play_ko("France", "Spain", mod_a=fra_sf1_mod, mod_b=0, stage="SF")
        w102, l102 = play_ko("England", "Argentina", mod_a=eng_sf2_mod, mod_b=0, stage="SF")

        counts["SF1_Dallas"][w101] += 1
        counts["SF2_Atlanta"][w102] += 1
        counts["Reach_Final"][w101] += 1
        counts["Reach_Final"][w102] += 1

        # Third-place playoff: slight motivation edge for England/Spain vs deflated Argentina/France? Keep neutral (0 mod)
        w103, l103 = play_ko(l101, l102, mod_a=0, mod_b=0, stage="3P")
        # Final: slight fatigue/crowd neutral
        w104, l104 = play_ko(w101, w102, mod_a=0, mod_b=0, stage="FIN")

        counts["ThirdPlace"][w103] += 1
        counts["Champion"][w104] += 1

        # GOLDEN BOOT
        best_key = (-1, -1, -9999)
        best_name = None
        mb_g = ms_g = 0
        for pname, team, cg, ca, gpg, apg, gmins in players:
            if team == "NONE":
                fg = 2 + poisson(0.9)
                key = (fg, poisson(0.7), -500)
                if key > best_key: best_key = key; best_name = "Field"
                continue
            goals = cg; assists = ca; mins = gmins
            ms = list(team_matches.get(team, []))

            eff_ms = []
            for opp, oe, won, p_win, stg in ms:
                if pname == "Kylian Mbappé" and stg == "SF":
                    mp = mbappe_sf_miss
                elif pname == "Lionel Messi" and stg == "SF":
                    mp = messi_sf_miss
                elif stg == "3P":
                    # Stars chasing Golden Boot usually play 3P (esp Mbappe/Messi/Kane/Bellingham), ~6-9% rest/rotation
                    mp = tp_rot_miss * (0.75 if pname in ("Kylian Mbappé", "Lionel Messi", "Harry Kane", "Jude Bellingham") else 1.25)
                else:
                    mp = 0.025
                if random.random() > mp:
                    eff_ms.append((opp, oe, won, p_win, stg))

            eff_ng = len(eff_ms)
            if eff_ng > 0:
                mult = max(0.35, random.gauss(1.0, 0.22))
                exp_g = 0.0
                for opp, oe, won, p_win, stg in eff_ms:
                    # Opponent defensive adjustment:
                    # Spain: 1 goal conceded in 6 games (0.80x)
                    # France: 2 goals conceded in 6 games (0.82x)
                    # England: 6 goals conceded in 6 games (0.94x)
                    # Argentina: 7 goals conceded in 6 games, 6 in 3 KO games! (1.06x)
                    opp_def = {"Spain": 0.80, "France": 0.82, "England": 0.94, "Argentina": 1.06}.get(opp, 0.95)
                    # Stage multiplier: SF=0.96, FIN=0.92, 3P=1.24 (open game!)
                    stg_mult = 1.24 if stg == "3P" else (0.92 if stg == "FIN" else 0.96)
                    mu = gpg * mult * opp_def * stg_mult
                    denom = 1.0 + p_win * (win_goal_ratio - 1.0)
                    mu_adj = (mu * win_goal_ratio / denom) if won else (mu / denom)
                    exp_g += mu_adj
                goals += poisson(exp_g)
                assists += poisson(eff_ng * apg)
            mins += eff_ng * (88 if pname == "Lionel Messi" else 87)
            if pname == "Kylian Mbappé": mb_g = goals
            if pname == "Lionel Messi": ms_g = goals
            key = (goals, assists, -mins)
            if key > best_key:
                best_key = key; best_name = pname
        gb_wins[best_name] += 1
        if mb_g == ms_g and best_name in ("Kylian Mbappé", "Lionel Messi"):
            gb_tie_breaks[best_name] += 1

        # GOLDEN BALL MODEL 1: Team Finish
        r = random.random()
        if r < 0.56: gb_team = w104
        elif r < 0.86: gb_team = l104
        elif r < 0.95: gb_team = w103
        else: gb_team = l103
        shares = TEAM_SHARES[gb_team]
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
            sm = TEAM_STAR_MULT[t]
            gb_bonus = 1.38 if t == gb_winner_team else 1.0
            weights.append((t, bw * sm * gb_bonus))
        tot_w = sum(x[1] for x in weights)
        u = random.random() * tot_w; cum = 0.0
        gb_team2 = w104
        for t, wt in weights:
            cum += wt
            if u <= cum:
                gb_team2 = t; break
        shares2 = list(TEAM_SHARES[gb_team2])
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
    for key in ["SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final"]:
        out[key] = {t: cnt/N for t, cnt in counts[key].most_common(6)}
    out["GOLDEN_BOOT"] = {n: c/N for n, c in gb_wins.most_common(6)}
    out["GBALL_TEAM"] = {n: c/N for n, c in gball_team_wins.most_common(12)}
    out["GBALL_STAR"] = {n: c/N for n, c in gball_star_wins.most_common(12)}
    print("  SF1_Dallas :", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF1_Dallas"].items()))
    print("  SF2_Atlanta:", ", ".join(f"{k}:{v:.4f}" for k, v in out["SF2_Atlanta"].items()))
    print("  ThirdPlace :", ", ".join(f"{k}:{v:.4f}" for k, v in out["ThirdPlace"].items()))
    print("  Champion   :", ", ".join(f"{k}:{v:.4f}" for k, v in out["Champion"].items()))
    print("  GOLDEN_BOOT:", ", ".join(f"{n}:{c/N:.4f}" for n, c in gb_wins.most_common(6)))
    print(f"  Tiebreaks (Mb==Ms): {dict(gb_tie_breaks)} (rate={(gb_tie_breaks['Kylian Mbappé']+gb_tie_breaks['Lionel Messi'])/N:.3f})")
    return out

r1 = run_sim("1. MARKET-CALIBRATED (50%)", ELO_MARKET, scale=405.0, sigma=36.0,
             fra_sf1_mod=3.0, eng_sf2_mod=3.0,
             mbappe_base=0.76, messi_base=0.58, kane_base=0.64, bell_base=0.40, N=300000)

r2 = run_sim("2. BALANCED MKT+FUND (25%)", ELO_BALANCED, scale=410.0, sigma=40.0,
             fra_sf1_mod=2.0, eng_sf2_mod=2.0,
             mbappe_base=0.75, messi_base=0.60, kane_base=0.63, bell_base=0.42, N=250000)

r3 = run_sim("3. OPTA / SPAIN-ARG FORM (15%)", ELO_OPTA, scale=410.0, sigma=40.0,
             fra_sf1_mod=1.0, eng_sf2_mod=1.0,
             mbappe_base=0.74, messi_base=0.63, kane_base=0.61, bell_base=0.40, N=200000)

r4 = run_sim("4. UPSET-CONSERVATIVE (10%)", ELO_CONSERVATIVE, scale=425.0, sigma=48.0,
             fra_sf1_mod=0.0, eng_sf2_mod=1.5,
             mbappe_base=0.73, messi_base=0.61, kane_base=0.62, bell_base=0.39, N=200000)

weights = [(r1, 0.50), (r2, 0.25), (r3, 0.15), (r4, 0.10)]
print("\n==================== JULY 12 WEIGHTED ENSEMBLE (50/25/15/10) ====================")
ens = {}
for key in ["SF1_Dallas", "SF2_Atlanta", "ThirdPlace", "Champion", "Reach_Final", "GOLDEN_BOOT"]:
    agg = Counter()
    for res, wt in weights:
        for k, v in res[key].items():
            agg[k] += wt * v
    ens[key] = dict(agg)
    print(f"  {key:12s}: " + ", ".join(f"{k}:{v:.4f}" for k, v in agg.most_common(6)))

agg_gb_sim = Counter()
for res, wt in weights:
    for k, v in res["GBALL_TEAM"].items():
        agg_gb_sim[k] += wt * 0.40 * v
    for k, v in res["GBALL_STAR"].items():
        agg_gb_sim[k] += wt * 0.60 * v
print("  GBALL_SIM   : " + ", ".join(f"{k}:{v:.4f}" for k, v in agg_gb_sim.most_common(10)))

# ==============================================================================
# BLEND WITH JULY 12 DIRECT MARKET LINES
# ==============================================================================
print("\n=== FINAL BLENDS WITH JULY 12 SPORTSBOOK CONSENSUS ===")
# SF1: Market sharp consensus (Circa 57.1%, FD 57.3%, Kalshi 3way ~56.3%, DK 57.8% public-shaded) -> 57.1% FRA
sf1_mkt = {"France": 0.571, "Spain": 0.429}
sf1_final = {t: 0.55 * sf1_mkt[t] + 0.45 * ens["SF1_Dallas"][t] for t in sf1_mkt}
print("  SF1 Final (55% Mkt / 45% Ens):", {k: round(v, 4) for k, v in sf1_final.items()})

# SF2: Market sharp consensus (Circa 55.2%, DK 54.7%, FD 54.6%, Caesars 54.4%, 11-book avg 54.2%) -> 54.5% ENG
# Opta: 50.94% ENG -> our 4-model ensemble already includes Opta + market!
sf2_mkt = {"England": 0.545, "Argentina": 0.455}
sf2_final = {t: 0.60 * sf2_mkt[t] + 0.40 * ens["SF2_Atlanta"][t] for t in sf2_mkt}
print("  SF2 Final (60% Mkt / 40% Ens):", {k: round(v, 4) for k, v in sf2_final.items()})

# Champion: DK/SI July 12 vig-free mid (FRA 0.373, ESP 0.219, ENG 0.208, ARG 0.199)
champ_mkt = {"France": md[0], "Spain": md[1], "England": md[2], "Argentina": md[3]}
champ_final = {t: 0.55 * champ_mkt[t] + 0.45 * ens["Champion"][t] for t in champ_mkt}
print("  Champ Mkt (DK/SI Jul 12)     :", {k: round(v, 4) for k, v in champ_mkt.items()})
print("  Champ Final (55% Mkt / 45% Ens):", {k: round(v, 4) for k, v in champ_final.items()})

# Golden Ball: Bayesian update of July 11 Market Golden Ball conditioned on QF4 (ARG 3-1 SUI a.e.t., Messi 0g/1a!)
# July 11 Market Golden Ball BEFORE QF4 (when ARG was 73.4% to advance, ENG was 52.5% to reach Final):
#   Mbappe 0.310, Messi 0.206, Bellingham 0.138, Kane 0.064, Olise 0.061, Yamal 0.059, Dembele 0.036, Rodri 0.026, Pedri 0.022
# Conditioning on ARG winning QF4 (eliminating SUI 0.266 -> 0, raising ARG Reach_Final 0.388 -> 0.460 = 1.186x, Champ 0.167 -> 0.200 = 1.198x),
# PARTLY tempered by Messi going scoreless vs Switzerland & looking fatigued (slight -4% narrative drag vs average win where Messi scores),
# AND England's Reach_Final shifting 0.525 -> 0.540 (+1.03x) / Champ 0.222 -> 0.210 (-0.95x):
#   - Messi: 0.206 * 1.19 * 0.96 = 0.235!
#   - Mbappe: ~0.305 (slight boost from Messi scoreless in Golden Boot -> Mbappe GB prob 0.585 -> 0.625!)
#   - Bellingham: ~0.138 (England now favorite in SF2 ~54%, back-to-back KO braces, massive media narrative!)
#   - Kane: ~0.061
#   - Olise: ~0.063 (6 assists, chasing Pele's all-time record!)
#   - Yamal: ~0.058 (1g, quiet tournament so far)
#   - Dembele: ~0.036, Rodri: ~0.027, Pedri: ~0.022
mkt_gball_jul12 = {
    "Kylian Mbappé": 0.305,
    "Lionel Messi": 0.235,
    "Jude Bellingham": 0.138,
    "Michael Olise": 0.063,
    "Harry Kane": 0.061,
    "Lamine Yamal": 0.058,
    "Ousmane Dembélé": 0.036,
    "Rodri": 0.027,
    "Pedri": 0.022,
}
print("\n=== GOLDEN BALL BLEND (50% SIM / 50% MARKET BAYES) ===")
gb_blend = {}
for pl in set(list(mkt_gball_jul12.keys()) + list(agg_gb_sim.keys())):
    if pl.startswith("Other"): continue
    gb_blend[pl] = 0.50 * agg_gb_sim.get(pl, 0.0) + 0.50 * mkt_gball_jul12.get(pl, 0.0)
for pl, v in sorted(gb_blend.items(), key=lambda x:-x[1])[:10]:
    print(f"  {pl:18s}: Blend={v:.4f} (Sim={agg_gb_sim.get(pl,0):.4f}, Mkt={mkt_gball_jul12.get(pl,0):.4f})")
