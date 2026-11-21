"""
Quantitative Forecasting Models — Sat Sep 19, 2026
Batch: asian_games_racket
  - qid=556932: Asian Games Women's Singles Squash Gold (EXACT HALVES + Sivasangari Doha SF Update!)
  - qid=700005: Asian Games Men's Singles Squash Gold (Verification check post-Bernama Sep 18)
  - qid=259249: PV Sindhu Furthest Round (Verification check post-Team Draw Sep 19)
"""
import math
import random
from collections import Counter


def rank_to_elo(r, scale=215.0):
    return 2300.0 - scale * math.log(r)


def sim_women_squash_exact_halves(n_trials=300000, seed=55693219):
    """
    NEW EVIDENCE Sep 18-19:
    1. Bernama (Sep 18) + Qatar Tribune (Sep 17):
       - Sivasangari Subramaniam (MAS, #1 seed, WR #5, defending AG champion) pushed World No. 1
         Hania El Hammamy to 12-10 in the 5th game (11-8, 9-11, 13-15, 11-8, 10-12 in 87m) in the
         Qatar Classic Platinum SF on Thu Sep 17!
       - Crucially: Coach Andrew Cross confirmed she had a QF WALKOVER in Doha (reduced tournament load!),
         finished Thu Sep 17 (7 full rest/acclimatization days before her R16 debut Thu Sep 24 after R1 bye!),
         and is healthy & departing with the Malaysian squad on Sat Sep 19!
       - Also Andrew Cross explicitly cautions: "Playing in Japan, at the home of Satomi, won't be easy."
    2. Hindustan Times (Sep 19, "Asian Games: Anahat Singh and the challenge within"):
       - CONFIRMS EXACT DRAW HALVES!
         - Top Half:    [1] Sivasangari Subramaniam (MAS) + [4] Aira Azman (MAS)
         - Bottom Half: [2] Satomi Watanabe (JPN) + [3] Anahat Singh (IND) [+ [7] Tanvi Khanna in Anahat's QF!]
       - Saurav Ghosal notes Satomi Watanabe is 1-0 vs Anahat (but Anahat pushed her to 5 games in Jan TOC:
         11-6, 11-6, 2-11, 8-11, 6-11) and is a better stylistic matchup for Anahat than Sivasangari
         (who just routed Anahat 11-4, 11-4 in London QF).
    """
    rng = random.Random(seed)

    # Sensitivity across 3 plausible calibration regimes:
    # Base Elo from PSA rank:
    #   WR #5  (Sivasangari): 1954
    #   WR #6  (Watanabe):    1915
    #   WR #20 (Anahat):      1656
    #   WR #21 (Aira Azman):  1645
    #   WR #24 (Chan Sin Yuk):1617
    #   WR #27 (Ho Tze-Lok):  1591
    #   WR #48 (Tanvi Khanna):1468
    #   WR #55 (Midorikawa):  1438
    scenarios = [
        # (name, weight, siva_boost, siva_sd, siva_play, wat_boost, wat_sd, wat_play, anahat_boost, match_bonus_anahat_vs_wat)
        (
            "S1: Base Posterior (Siva peak form +42, Doha travel sd=52; Wat home +18, fresh)",
            0.50,
            42.0, 52.0, 0.980,
            18.0, 48.0, 0.980,
            15.0, 35.0,
        ),
        (
            "S2: Siva Dominant Form (+55 Elo after WR#1 5-gamer; mild travel impact)",
            0.25,
            55.0, 48.0, 0.985,
            15.0, 50.0, 0.980,
            10.0, 30.0,
        ),
        (
            "S3: Home Court + Doha Recovery Drag (Siva +25 Elo, wider fatigue sd=62; Wat strong home +28)",
            0.25,
            25.0, 62.0, 0.970,
            28.0, 45.0, 0.985,
            20.0, 40.0,
        ),
    ]

    blend = Counter()
    h2h_siva_wat_wins = 0
    h2h_siva_wat_total = 0

    for sname, w, s_b, s_sd, s_p, w_b, w_sd, w_p, a_b, a_vs_w in scenarios:
        wins = Counter()
        sf_upset_wat = 0
        sf_upset_siva = 0
        final_sw = 0
        siva_beat_wat = 0

        for _ in range(n_trials):
            # Draw tournament ratings
            siva = ("Sivasangari Subramaniam", rng.gauss(rank_to_elo(5) + s_b, s_sd)) if rng.random() < s_p else ("Field_Sub", 1320.0)
            wat  = ("Satomi Watanabe", rng.gauss(rank_to_elo(6) + w_b, w_sd)) if rng.random() < w_p else ("Field_Sub", 1320.0)
            ana  = ("Anahat Singh", rng.gauss(rank_to_elo(20) + a_b, 58.0)) if rng.random() < 0.985 else ("Field_Sub", 1320.0)
            aira = ("Aira Azman", rng.gauss(rank_to_elo(21), 55.0)) if rng.random() < 0.985 else ("Field_Sub", 1320.0)
            chan = ("Chan Sin Yuk", rng.gauss(rank_to_elo(24), 55.0)) if rng.random() < 0.985 else ("Field_Sub", 1320.0)
            ho   = ("Ho Tze-Lok", rng.gauss(rank_to_elo(27), 55.0)) if rng.random() < 0.985 else ("Field_Sub", 1320.0)
            tanv = ("Tanvi Khanna", rng.gauss(rank_to_elo(48), 55.0)) if rng.random() < 0.985 else ("Field_Sub", 1320.0)
            mido = ("Akari Midorikawa", rng.gauss(rank_to_elo(55) + 15.0, 55.0)) if rng.random() < 0.985 else ("Field_Sub", 1320.0)

            def play(p1, p2):
                e1, e2 = p1[1], p2[1]
                # Style matchup adjustment: Anahat plays Watanabe tougher (TOC 5-gamer, Ghosal note)
                # while Sivasangari dominates Anahat & teammate Aira slightly more than pure Elo
                n1, n2 = p1[0], p2[0]
                if {n1, n2} == {"Anahat Singh", "Satomi Watanabe"}:
                    if n1 == "Anahat Singh":
                        e1 += a_vs_w
                    else:
                        e2 += a_vs_w
                elif {n1, n2} == {"Sivasangari Subramaniam", "Anahat Singh"}:
                    if n1 == "Sivasangari Subramaniam":
                        e1 += 35.0
                    else:
                        e2 += 35.0
                elif {n1, n2} == {"Sivasangari Subramaniam", "Aira Azman"}:
                    if n1 == "Sivasangari Subramaniam":
                        e1 += 25.0
                    else:
                        e2 += 25.0
                prob1 = 1.0 / (1.0 + 10.0 ** (-(e1 - e2) / 400.0))
                return p1 if rng.random() < prob1 else p2

            # Fixed exact halves from HT Sep 19:
            # Top half: [1] Sivasangari, [4] Aira Azman, + 2 of {Chan, Ho, Midorikawa}
            # Bot half: [2] Satomi Watanabe, [3] Anahat Singh (w/ [7] Tanvi Khanna in Anahat's QF!), + 1 of {Chan, Ho, Midorikawa}
            rem58 = [chan, ho, mido]
            rng.shuffle(rem58)
            q1_opp, q2_opp, q4_opp = rem58[0], rem58[1], rem58[2]
            # R16: each top-8 seed vs weak field (~1240 Elo)
            def r16(p):
                return play(p, ("Field_Weak", rng.gauss(1240.0, 50.0)))

            # Top half QFs:
            qf1 = play(r16(siva), r16(q1_opp))
            qf2 = play(r16(aira), r16(q2_opp))
            # Bot half QFs: (Anahat vs Tanvi Khanna confirmed as likely QF in HT Sep 19!)
            qf3 = play(r16(ana),  r16(tanv))
            qf4 = play(r16(wat),  r16(q4_opp))

            sf_top = play(qf1, qf2)
            sf_bot = play(qf3, qf4)

            if sf_top[0] != "Sivasangari Subramaniam":
                sf_upset_siva += 1
            if sf_bot[0] != "Satomi Watanabe":
                sf_upset_wat += 1

            champ = play(sf_top, sf_bot)
            if sf_top[0] == "Sivasangari Subramaniam" and sf_bot[0] == "Satomi Watanabe":
                final_sw += 1
                if champ[0] == "Sivasangari Subramaniam":
                    siva_beat_wat += 1

            wins[champ[0]] += 1

        print(f"\n  [{w:.2f}] {sname}")
        print(f"        Final=Siva vs Wat: {final_sw/n_trials:.3f} | Siva H2H win% in Final: {siva_beat_wat/final_sw:.3f} | Siva misses F: {sf_upset_siva/n_trials:.3f} | Wat misses F: {sf_upset_wat/n_trials:.3f}")
        for nm in ["Sivasangari Subramaniam", "Satomi Watanabe", "Anahat Singh", "Aira Azman", "Chan Sin Yuk", "Ho Tze-Lok"]:
            p = wins[nm] / n_trials
            blend[nm] += w * p
            print(f"        {nm:26s}: {p:.4f}")
        h2h_siva_wat_wins += w * (siva_beat_wat / final_sw)
        h2h_siva_wat_total += w

    print("\n  === FINAL BLENDED WOMEN'S SQUASH GOLD PROBABILITIES ===")
    top5_sum = 0.0
    for i, (nm, p) in enumerate(sorted(blend.items(), key=lambda x: -x[1])):
        print(f"    {nm:26s}: {p:.4f}")
        if i < 5:
            top5_sum += p
    print(f"  Blended Siva vs Wat Final H2H win%: {h2h_siva_wat_wins/h2h_siva_wat_total:.4f}")
    print(f"  Top-5 sum = {top5_sum:.4f} (Outside incl. Ho Tze-Lok ~{blend['Ho Tze-Lok']:.4f})")


if __name__ == "__main__":
    print("=" * 76)
    print("MODEL UPDATE: qid=556932 — Asian Games Women's Singles Squash Gold (Sep 19)")
    print("=" * 76)
    sim_women_squash_exact_halves()
