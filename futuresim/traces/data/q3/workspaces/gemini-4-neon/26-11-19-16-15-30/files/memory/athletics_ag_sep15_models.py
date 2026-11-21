"""
Quantitative models for batch olympic_athletics_asian_games on 2026-09-15:
  1. qid=574485: PSA Women's World Squash No. 1 on Sep 21, 2026 (T+3d)
  2. qid=67348:  2026 Asian Games Men's Basketball Bronze Medal (T+5d)
  3. qid=784475: 2026 World Athletics Road Running Championships Copenhagen Women's Half Marathon (T+5d)
"""
import math
import random
from collections import Counter


# ==============================================================================
# MODEL 1: Q1 (qid=574485) — PSA WOMEN'S WORLD NO. 1 ON SEPT 21, 2026
# ==============================================================================
# Official PSA Squash Tour rule (Sep 9, 2026):
#   - Orfi becomes #1 iff she matches or betters El Hammamy's finish in Doha.
#   - El Hammamy stays #1 iff she wins the title OR betters Orfi's finish.
# Official Tournament State as of Tue Sep 15, 2026:
#   - Nour El Sherbini (#3) LOST in R16 to Rachel Arnold 3-1 -> 0.000!
#   - Nouran Gohar (#5) WITHDREW INJURED from Tue Sep 15 QF vs El Hammamy!
#   - El Hammamy is ALREADY in Thu Sep 17 SF (walkover + 2 rest days) vs Sivasangari Subramaniam!
#   - Orfi plays Wed Sep 16 QF vs [6] Fayrouz Aboelkheir; winner plays Rachel Arnold / Jasmine Hutton in Thu SF.

def model_squash_no1():
    print("=" * 72)
    print("MODEL 1: qid=574485 — PSA Women's World No. 1 (Sep 21, 2026)")
    print("=" * 72)

    def exact_orfi_prob(p_h_sf, p_o_qf, p_o_sf, p_o_fin):
        # Case 1: El Hammamy loses SF -> Orfi #1 iff Orfi wins QF (ties at SF or better)
        c1 = (1.0 - p_h_sf) * p_o_qf
        # Case 2: El Hammamy wins SF -> Orfi #1 iff Orfi wins QF, wins SF, AND beats El Hammamy in Final
        c2 = p_h_sf * p_o_qf * p_o_sf * p_o_fin
        return c1 + c2

    scenarios = [
        ("Base case (rested Hammamy 0.79 SF; Orfi 0.85 QF, 0.925 SF; 50/50 Final)", 0.79, 0.85, 0.925, 0.50),
        ("Orfi form edge in Final (0.78 SF; 0.86 QF, 0.93 SF; 0.525 Orfi Final)",    0.78, 0.86, 0.930, 0.525),
        ("Hammamy rest+Doha edge (0.81 SF; 0.84 QF, 0.92 SF; 0.475 Orfi Final)",     0.81, 0.84, 0.920, 0.475),
        ("Sivasangari upset risk (0.75 SF; 0.85 QF, 0.925 SF; 0.50 Final)",          0.75, 0.85, 0.925, 0.50),
        ("Aboelkheir rivalry test (0.80 SF; 0.81 QF, 0.92 SF; 0.50 Final)",          0.80, 0.81, 0.920, 0.50),
    ]
    weights = [0.40, 0.22, 0.22, 0.08, 0.08]
    blend_orfi = 0.0
    for (name, ph, pq, ps, pf), w in zip(scenarios, weights):
        po = exact_orfi_prob(ph, pq, ps, pf)
        blend_orfi += w * po
        print(f"  [{w:.2f}] {name}\n        -> Orfi={po:.4f}, El Hammamy={1-po:.4f}")

    # Monte Carlo integrating smooth parameter uncertainty (Beta/Normal priors around base)
    rng = random.Random(57448515)
    mc_orfi = []
    for _ in range(100000):
        ph = min(0.92, max(0.62, rng.gauss(0.79, 0.045)))
        pq = min(0.94, max(0.70, rng.gauss(0.85, 0.040)))
        ps = min(0.98, max(0.82, rng.gauss(0.925, 0.025)))
        pf = min(0.65, max(0.35, rng.gauss(0.505, 0.045)))
        mc_orfi.append(exact_orfi_prob(ph, pq, ps, pf))
    mc_mean = sum(mc_orfi) / len(mc_orfi)
    print(f"\n  Weighted scenario blend: Amina Orfi={blend_orfi:.4f}, Hania El Hammamy={1-blend_orfi:.4f}")
    print(f"  100k Bayesian MC mean:   Amina Orfi={mc_mean:.4f}, Hania El Hammamy={1-mc_mean:.4f}")


# ==============================================================================
# MODEL 2: Q2 (qid=67348) — 2026 ASIAN GAMES MEN'S BASKETBALL BRONZE MEDAL
# ==============================================================================
# Official Bracket (aichi-nagoya2026.org, Sep 14, 2026):
#   Half 1: QF1 = China vs Saudi Arabia; QF2 = Chinese Taipei vs Japan -> SF1 = W(QF1) vs W(QF2)
#   Half 2: QF4 = South Korea vs Jordan; QF3 = Iran vs Bahrain         -> SF2 = W(QF4) vs W(QF3)
#   Bronze Medal Match (Sun Sep 20): L(SF1) vs L(SF2)

def normal_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def model_asian_games_basketball():
    print("\n" + "=" * 72)
    print("MODEL 2: qid=67348 — 2026 Asian Games Men's Basketball Bronze Medal")
    print("=" * 72)

    # Base team strength ratings (expected net margin vs avg QF team in Nagoya, incl. Japan HCA ~+2.0)
    # Calibrated to group results:
    #   China: 3-0 (+128: +38 KAZ, +46 BAH, +44 PHI) -> +18.5
    #   South Korea: 3-0 (+87: +16 KSA, +54 INA, +17 JPN) -> +12.5
    #   Iran: 2-1 (+10: -6 QAT, +3 TPE, +13 JOR) -> +5.0
    #   Japan (host): 2-1 (+34: +45 INA, +6 KSA, -17 KOR) -> +4.8
    #   Chinese Taipei: 2-1 (+22: +3 JOR, -3 IRN, +22 QAT) -> +3.8
    #   Jordan: 1-2 (-5: -3 TPE, +11 QAT, -13 IRN) -> -1.5
    #   Saudi Arabia: 1-2 (-11: -16 KOR, -6 JPN, +11 INA) -> -4.5
    #   Bahrain: 2-1 (+4 PHI, -46 CHN, beat KAZ) -> -5.5
    base_ratings = {
        "China": 18.5,
        "South Korea": 12.5,
        "Iran": 5.0,
        "Japan": 4.8,
        "Chinese Taipei": 3.8,
        "Jordan": -1.5,
        "Saudi Arabia": -4.5,
        "Bahrain": -5.5,
    }
    # Uncertainty in true latent strength (pts) per team (higher for teams with sparse overlap like CHN/BAH)
    rating_sd = {
        "China": 3.0,
        "South Korea": 2.5,
        "Iran": 2.5,
        "Japan": 2.5,
        "Chinese Taipei": 2.5,
        "Jordan": 2.5,
        "Saudi Arabia": 2.5,
        "Bahrain": 3.0,
    }

    # Check implied head-to-head probabilities at base ratings (game SD = 11.5 pts, FIBA 40-min basketball)
    game_sd_base = 11.5
    print("  Base implied H2H win probabilities (game_sd=11.5):")
    for a, b in [
        ("China", "Saudi Arabia"),
        ("Japan", "Chinese Taipei"),
        ("Iran", "Bahrain"),
        ("South Korea", "Jordan"),
        ("China", "Japan"),
        ("China", "Chinese Taipei"),
        ("South Korea", "Iran"),
        ("China", "South Korea"),
        ("Iran", "Japan"),
        ("Iran", "Chinese Taipei"),
    ]:
        p = normal_cdf((base_ratings[a] - base_ratings[b]) / game_sd_base)
        print(f"    {a:15s} vs {b:15s}: {p:.3f} / {1-p:.3f} (diff={base_ratings[a]-base_ratings[b]:+.1f})")

    # Run 200,000 hierarchical Monte Carlo simulations (sampling true ratings + game noise)
    rng = random.Random(6734815)
    n_sims = 200000
    bronze_counts = Counter()
    gold_counts = Counter()
    bronze_match_appear = Counter()

    def play(t1, t2, r, sd):
        # Single-game basketball outcome with slight fat-tail / upset variance via Student-t-like mixture
        eff_sd = sd * (1.25 if rng.random() < 0.15 else 1.0)
        margin = (r[t1] - r[t2]) + rng.gauss(0.0, eff_sd)
        return (t1, t2) if margin > 0 else (t2, t1)

    for _ in range(n_sims):
        r = {t: base_ratings[t] + rng.gauss(0.0, rating_sd[t]) for t in base_ratings}
        sd = rng.uniform(10.5, 12.5)

        w_qf1, _ = play("China", "Saudi Arabia", r, sd)
        w_qf2, _ = play("Chinese Taipei", "Japan", r, sd)
        w_qf3, _ = play("Iran", "Bahrain", r, sd)
        w_qf4, _ = play("South Korea", "Jordan", r, sd)

        w_sf1, l_sf1 = play(w_qf1, w_qf2, r, sd)
        w_sf2, l_sf2 = play(w_qf4, w_qf3, r, sd)

        bronze_match_appear[l_sf1] += 1
        bronze_match_appear[l_sf2] += 1

        # Slight motivation variance in Bronze match (favorites upset in SF sometimes slightly flatter -> +10% sd)
        bronze_w, _ = play(l_sf1, l_sf2, r, sd * 1.08)
        gold_w, _ = play(w_sf1, w_sf2, r, sd)

        bronze_counts[bronze_w] += 1
        gold_counts[gold_w] += 1

    print("\n  200k Hierarchical MC Results (Base + Uncertainty):")
    print(f"  {'Country':16s} {'Bronze%':>9s} {'InBronze%':>10s} {'Gold%':>9s}")
    for team, cnt in bronze_counts.most_common():
        print(f"  {team:16s} {cnt/n_sims:9.4f} {bronze_match_appear[team]/n_sims:10.4f} {gold_counts[team]/n_sims:9.4f}")
    top5 = bronze_counts.most_common(5)
    print("  Top-5 sum:", round(sum(c for _, c in top5) / n_sims, 4))

    # Sensitivity test: What if China & Korea are slightly less dominant (e.g. CHN +15.5, KOR +10.5)
    # because FIBA single-elimination games are tighter than group blowouts?
    tight_ratings = {
        "China": 15.5,
        "South Korea": 10.5,
        "Iran": 5.0,
        "Japan": 5.2,
        "Chinese Taipei": 4.0,
        "Jordan": -1.0,
        "Saudi Arabia": -4.0,
        "Bahrain": -5.0,
    }
    bc2 = Counter()
    for _ in range(100000):
        r = {t: tight_ratings[t] + rng.gauss(0.0, 2.5) for t in tight_ratings}
        sd = rng.uniform(11.0, 13.0)
        w_qf1, _ = play("China", "Saudi Arabia", r, sd)
        w_qf2, _ = play("Chinese Taipei", "Japan", r, sd)
        w_qf3, _ = play("Iran", "Bahrain", r, sd)
        w_qf4, _ = play("South Korea", "Jordan", r, sd)
        w_sf1, l_sf1 = play(w_qf1, w_qf2, r, sd)
        w_sf2, l_sf2 = play(w_qf4, w_qf3, r, sd)
        bw, _ = play(l_sf1, l_sf2, r, sd * 1.08)
        bc2[bw] += 1
    print("\n  Sensitivity (Tighter Knockout Margins: CHN +15.5, KOR +10.5, JPN +5.2):")
    for team, cnt in bc2.most_common():
        print(f"    {team:16s}: {cnt/100000:.4f}")

    # Blend 60% base + 40% tighter-knockout
    print("\n  Blended (60% Base / 40% Tighter Knockout):")
    all_teams = list(base_ratings.keys())
    blended = {t: 0.60 * (bronze_counts[t] / n_sims) + 0.40 * (bc2[t] / 100000) for t in all_teams}
    for t, p in sorted(blended.items(), key=lambda x: -x[1]):
        print(f"    {t:16s}: {p:.4f}")
    top5_b = sorted(blended.items(), key=lambda x: -x[1])[:5]
    print("  Blended Top-5 sum:", round(sum(p for _, p in top5_b), 4))


# ==============================================================================
# MODEL 3: Q3 (qid=784475) — COPENHAGEN 2026 WRRC WOMEN'S HALF MARATHON
# ==============================================================================
# Official Sep 15 FloTrack Entry List:
#   EJGAYEHU TAYE IS ABSENT! (Likina Amebaw is in 5K; Tesfay/Yehualaw/Feysa/Gidey all absent!)
#   Top entrants confirmed on Sep 15 entry list:
#     1. Agnes Jebet Ngetich (KEN) - 1:03:04 PB (#2 all-time), 1:03:08 (2025), 28:46 10k WR, 2026 World XC champ
#     2. Lilian Kasait Rengeruk (KEN) - 1:03:32 PB (#5 all-time), 2023 Riga 5km silver, 2024 World XC silver, strong kick
#     3. Tsigie Gebreselama (ETH) - 1:04:21 PB, 4th Riga 2023 WRRC HM, 2x World XC medalist, 29:48 10,000m
#     4. Veronica Loleo (KEN) - ~1:05:45-1:06:00 tier Kenyan #3
#     5. Ftaw Zeray (ETH) - ~1:06:00-1:06:20 tier Ethiopian #2 (former Copenhagen HM 1:06:04!)
#     6. Daisilah Jerono (KEN) - ~1:06:10-1:06:30 tier Kenyan #4
#     7. Field: Weini Kelati (USA 1:06:09), Rebecca Chelangat (UGA), Esther Chebet (UGA),
#               Karoline Bjerkeli Grovdal (NOR), Baraky Redae (ETH), Melal Siyoum (ETH),
#               Meselech Alemayehu (ETH), Julia Paternain (URU), Nazret Weldu (ERI), etc.

def model_copenhagen_hm():
    print("\n" + "=" * 72)
    print("MODEL 3: qid=784475 — Copenhagen 2026 WRRC Women's Half Marathon")
    print("=" * 72)

    # Model two race regimes (unpaced World Championship HM):
    #   - Regime 1 (55%): Honest / Hard Pace (Ngetich/Kenya push pace on flat, fast Copenhagen course -> PB/fitness heavily rewarded)
    #   - Regime 2 (45%): Tactical / Kick Race (like Riga 2023 1:07:25 -> gaps compress & 5k/10k kickers Rengeruk/Gebreselama gain!)
    # Each athlete also has a 3.5% independent DNS/DNF/disaster probability (5 days out).
    # Parameters: (name, p_start_healthy, base_sec_honest, kick_bonus_tactical, sd_sec)
    # Note: 1:03:00 = 3780s, 1:04:00 = 3840s, 1:05:00 = 3900s, 1:06:00 = 3960s
    athletes = [
        ("Agnes Jebet Ngetich",   0.965, 3810,  0, 42),
        ("Lilian Kasait Rengeruk",0.965, 3848, -16, 44),
        ("Tsigie Gebreselama",    0.965, 3862, -14, 46),
        ("Veronica Loleo",        0.965, 3922, -6, 52),
        ("Ftaw Zeray",            0.965, 3932, -4, 54),
        ("Daisilah Jerono",       0.965, 3938, -4, 54),
        ("Weini Kelati",          0.965, 3965, -8, 52),
        ("Rebecca Chelangat",     0.965, 3972, -5, 55),
        ("Karoline Grovdal",      0.965, 3980, -12, 55),
        ("Ethiopia_Other_1",      0.965, 3975, -5, 60),
        ("Ethiopia_Other_2",      0.965, 3995, -5, 60),
        ("Rest_of_Field_Best",    0.980, 3975, -8, 55),
    ]

    rng = random.Random(78447515)
    n_sims = 200000
    wins = Counter()

    for _ in range(n_sims):
        tactical = rng.random() < 0.45
        best_t = 1e9
        winner = None
        for name, p_ok, mu_h, kick, sd in athletes:
            if rng.random() > p_ok:
                continue
            if tactical:
                # Compress distance gaps to 45% of honest gaps + add kick bonus + higher relative randomness
                mu = 3950 + 0.45 * (mu_h - 3810) + kick
                eff_sd = sd * 0.72
            else:
                mu = mu_h
                eff_sd = sd
            # Occasional bad day (+70..+160s) with 7% chance
            bad_day = rng.uniform(70, 160) if rng.random() < 0.07 else 0.0
            t = rng.gauss(mu, eff_sd) + bad_day
            if t < best_t:
                best_t = t
                winner = name
        wins[winner] += 1

    print("  200k Blended Honest(55%)/Tactical(45%) Championship HM MC:")
    for name, cnt in wins.most_common():
        print(f"    {name:25s}: {cnt/n_sims:.4f}")
    top5 = wins.most_common(5)
    print("  Top-5 sum:", round(sum(c for _, c in top5) / n_sims, 4))


if __name__ == "__main__":
    model_squash_no1()
    model_asian_games_basketball()
    model_copenhagen_hm()
