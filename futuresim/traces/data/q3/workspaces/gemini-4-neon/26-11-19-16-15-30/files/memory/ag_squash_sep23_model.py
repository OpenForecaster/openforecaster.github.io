"""
Quantitative Monte Carlo Model — Wed Sep 23, 2026
qid=700005: Asian Games Men's Singles Squash Gold (POST-R32 + CONFIRMED R16 MATCHUPS!)
qid=556932: Asian Games Women's Singles Squash Gold (Sanity check post-R32 + Anahat WR #17!)

VERIFIED WED SEP 23 MEN'S SINGLES SQUASH R32 & THU SEP 24 R16 MATCHUPS:
  - [1] Ng Eain Yow (MAS): NST Sep 23 "dominant Asian Games opener" -> p_play = 1.00!
  - [2] Abhay Singh (IND): beat Arkarahirunya (THA) -> Thu R16 vs Ravindu Laksiri (SRI) -> EASY R16! NO Al-Tamimi!
  - [3] Noor Zaman (PAK, WR #29): crushed Dalida (PHI) 11-2,11-4,11-3 -> Thu R16 vs Ammar Al Tamimi (KUW) -> EASY R16! NO Abdulla Al-Tamimi!
  - [4] Veer Chotrani (IND): beat Wakeel (SRI) -> Thu R16 vs [9] Sanjay Jeeva (MAS)!! -> TOUGH R16! Sanjay Jeeva LOCKED in #4's slot!
  - [5] Muhammad Ashab Irfan (PAK, WR #49 per Dawn): crushed Karam (LIB) 11-2,11-3,11-0 -> Thu R16 vs Mohammad Al Nasfan (KSA) -> EASY R16! NO Al-Tamimi!
  - THEREFORE [10] Abdulla Al-Tamimi (QAT, if playing & won R32) can ONLY occupy 1 of the 4 remaining R16 slots:
    {[1] Ng Eain Yow, [6] Alex Lau, [7] Ryunosuke Tsukue, [8] Henry Leung}!
"""
import math
import random
from collections import Counter


def rank_to_elo(r, scale=215.0):
    return 2300.0 - scale * math.log(r)


def sim_men_squash_sep23(n_trials=300000, seed=70000523):
    rng = random.Random(seed)
    wins = Counter()

    def draw_elo(p_play, states):
        if rng.random() > p_play:
            return None
        u = rng.random()
        cum = 0.0
        chosen = states[-1]
        for st in states:
            cum += st[0]
            if u <= cum:
                chosen = st
                break
        _, mu, sd = chosen
        return rng.gauss(mu, sd)

    def match(a, b):
        if a is None:
            return b
        if b is None:
            return a
        p_a = 1.0 / (1.0 + 10.0 ** (-(a[1] - b[1]) / 400.0))
        return a if rng.random() < p_a else b

    # Updated player states post-Wed Sep 23 R32:
    # Ashab Irfan Dawn explicitly gives WR #49 (slightly lower than #41 previously assumed, though crushed Karam 11-2,11-3,11-0).
    # Ng Eain Yow, Abhay Singh, Noor Zaman, Veer Chotrani, Ashab Irfan all confirmed healthy & in R16 (p_play = 1.0).
    # Note: slight 15% chance Al-Tamimi withdrew/lost/wasn't in R16 since zero Qatar press on him today -> p_play = 0.85 (vs 0.92 prior).
    def run_variant(tamimi_p=0.85, tamimi_vs_eain_yow_w=1.0, label="Base"):
        w = Counter()
        for _ in range(n_trials):
            s1 = ("Ng Eain Yow",          draw_elo(1.00, [(1.0, rank_to_elo(18) + 18, 50)])) # dominant opener!
            s2 = ("Abhay Singh",          draw_elo(1.00, [(1.0, rank_to_elo(24) + 5,  52)]))
            s3 = ("Noor Zaman",           draw_elo(1.00, [(1.0, rank_to_elo(29) + 8,  55)])) # 20-min rout!
            s4 = ("Veer Chotrani",        draw_elo(1.00, [(1.0, rank_to_elo(38),      55)]))
            s5 = ("Muhammad Ashab Irfan", draw_elo(1.00, [(1.0, rank_to_elo(46) + 5,  55)])) # WR #49 + 18-min rout!
            s6 = ("Alex Lau",             draw_elo(0.98, [(1.0, rank_to_elo(44) + 22, 55)]))
            s7 = ("Ryunosuke Tsukue",     draw_elo(0.98, [(1.0, rank_to_elo(48) + 22, 55)]))
            s8 = ("Henry Leung",          draw_elo(0.98, [(1.0, rank_to_elo(54),      55)]))

            # Replace any None with Field_Sub
            seeds = []
            for nm, e in [s1, s2, s3, s4, s5, s6, s7, s8]:
                seeds.append((nm, e) if e is not None else ("Field_Sub", 1320.0))

            # Standard 8-pod bracket:
            # Top half: Pod0=(#1), Pod1=(5-8), Pod2=(3/4), Pod3=(5-8)
            # Bot half: Pod4=(5-8), Pod5=(3/4), Pod6=(5-8), Pod7=(#2)
            p34 = [seeds[2], seeds[3]]
            rng.shuffle(p34)
            p58 = [seeds[4], seeds[5], seeds[6], seeds[7]]
            rng.shuffle(p58)
            pods = [seeds[0], p58[0], p34[0], p58[1], p58[2], p34[1], p58[3], seeds[1]]

            # Build EXACT known R16 opponents!
            # - Abhay Singh plays Ravindu Laksiri (SRI, ~1290)
            # - Noor Zaman plays Ammar Al Tamimi (KUW, ~1310)
            # - Veer Chotrani plays [9] Sanjay Jeeva (MAS, WR #63 -> ~1409)
            # - Ashab Irfan plays Mohammad Al Nasfan (KSA, ~1240)
            # - Remaining 4 slots (#1 Ng Eain Yow, #6 Alex Lau, #7 Tsukue, #8 Henry Leung):
            #   Abdulla Al-Tamimi (if active, prob tamimi_p) placed in one of those 4 slots!
            tamimi_e = draw_elo(tamimi_p, [
                (0.35, rank_to_elo(20) + 15, 55),
                (0.45, rank_to_elo(32),      55),
                (0.20, rank_to_elo(58),      55),
            ])
            sanjay_e = rng.gauss(rank_to_elo(63), 50.0)

            eligible_idxs = [i for i, p in enumerate(pods) if p[0] in ("Ng Eain Yow", "Alex Lau", "Ryunosuke Tsukue", "Henry Leung")]
            tamimi_idx = None
            if tamimi_e is not None and eligible_idxs:
                weights = [tamimi_vs_eain_yow_w if pods[i][0] == "Ng Eain Yow" else 1.0 for i in eligible_idxs]
                tot = sum(weights)
                u = rng.random() * tot
                acc = 0.0
                for idx, wt in zip(eligible_idxs, weights):
                    acc += wt
                    if u <= acc:
                        tamimi_idx = idx
                        break

            r16_opps = []
            for i, p in enumerate(pods):
                nm = p[0]
                if nm == "Abhay Singh":
                    r16_opps.append(("Ravindu Laksiri", rng.gauss(1290.0, 45.0)))
                elif nm == "Noor Zaman":
                    r16_opps.append(("Ammar Al Tamimi", rng.gauss(1310.0, 45.0)))
                elif nm == "Veer Chotrani":
                    r16_opps.append(("Sanjay Jeeva", sanjay_e))
                elif nm == "Muhammad Ashab Irfan":
                    r16_opps.append(("Mohammad Al Nasfan", rng.gauss(1240.0, 45.0)))
                elif i == tamimi_idx:
                    r16_opps.append(("Abdulla Al-Tamimi", tamimi_e))
                else:
                    r16_opps.append(("Field_Weak", rng.gauss(1240.0, 50.0)))

            qfs = [match(pods[i], r16_opps[i]) for i in range(8)]
            sfs = [match(qfs[0], qfs[1]), match(qfs[2], qfs[3]), match(qfs[4], qfs[5]), match(qfs[6], qfs[7])]
            fin = [match(sfs[0], sfs[1]), match(sfs[2], sfs[3])]
            champ = match(fin[0], fin[1])
            w[champ[0]] += 1

        print(f"\n--- {label} (tamimi_p={tamimi_p}, eain_yow_slot_w={tamimi_vs_eain_yow_w}) ---")
        for k, c in w.most_common(9):
            print(f"  {k:24s}: {c/n_trials:.4f}")
        top5 = sum(c for k, c in w.most_common(5)) / n_trials
        print(f"  Top-5 sum = {top5:.4f}")
        return {k: c / n_trials for k, c in w.items()}

    print("=" * 76)
    print("POST-SEP 23 MEN'S SINGLES SQUASH MC (qid=700005)")
    print("=" * 76)
    r1 = run_variant(tamimi_p=0.90, tamimi_vs_eain_yow_w=1.0, label="V1: Al-Tamimi active 90%, uniform over 4 open slots")
    r2 = run_variant(tamimi_p=0.80, tamimi_vs_eain_yow_w=0.6, label="V2: Al-Tamimi active 80%, slightly less likely in #1 slot (NST silence)")
    print("\n=== 50/50 BLEND (vs Prior: Eain Yow 0.31, Abhay 0.20, Noor 0.15, Al-Tamimi 0.08, Chotrani 0.07) ===")
    all_k = set(r1) | set(r2)
    bl = {k: 0.5 * r1.get(k, 0.0) + 0.5 * r2.get(k, 0.0) for k in all_k}
    for k, v in sorted(bl.items(), key=lambda x: -x[1])[:9]:
        print(f"  {k:24s}: {v:.4f}")


if __name__ == "__main__":
    sim_men_squash_sep23()
