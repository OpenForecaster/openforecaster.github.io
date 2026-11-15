# FINAL RETROSPECTIVE — Season complete (2026-09-30)

## FINAL RESULTS
- TW-Score: **1573.70** | Accuracy: 33.7% | Brier skill: 0.128
- All 252 questions predicted from Day 1 (2026-06-24) and resolved by 2026-09-30.

## TOP LESSONS (validated across 252 questions)

### 1. Diversification beats concentration in this sim
The world regularly defied establishment picks: Trabzonspor hijacked Salah; Angie Nixon beat Vindman (.88!); Hatcher beat Ogles; Elijah beat Mills; Koja beat Tamaki; Hull beat United; Leeds beat Forest; Al-Hilal signed Watkins/Martinelli; City bought everyone (Enzo record fee, Bouaddi, Elias). Top pick cap ~.50, second pick .25-.35. Hedges at .15-.35 rescued score repeatedly (death penalty over life, Barca over RM for Rodri, Trabzonspor for Salah/Fabinho, Apple over Nvidia, Sixth Circuit...).

### 2. String-matching is strict — full official names only
Cost me: "Yuki"→Yuki Kurihara (-.59), "Rumesh Tharanga"/"Pathirage"→"Rumesh Tharanga Pathirage" (x2), "Vladimir Z."→Volodymyr Zhuravlev, "permanent resident status"→"Permanent residency", "Judicial branch"→"Judiciary", "Tien Kung"→"Tiangong", "Aerial bomb"→"Aerial bombs". RULES: full names for non-household figures; standard pinyin; Ukrainian transliteration (Volodymyr/Mykhailo); match grader phrasing from how headlines print results.

### 3. Read answer granularity + exclusion criteria precisely
Dolphin landfall asked for a CITY (Yuhuan), I answered province (Zhejiang). Kyiv COUNTED as "away from eastern/southern fronts". BTC-type exclusions matter.

### 4. Cross-reference related questions
Enzo→City (resolved Aug 26) WAS the answer to "highest PL fee" (Sep 1) — I missed the link.

### 5. Sim-specific world rules discovered
- Türkiye wildcard: Trabzonspor (Salah, Fabinho), Turkish Airlines (Liverpool), Türkiye (Super Cup host). Always include Turkish options.
- UAE hosts everything (trilateral venue, port calls).
- The 76ers signed two stars (Brown, LeBron).
- Japan home-soil boosts at Japan-hosted Asian Games (Ohashi beat Qin) — but not deterministic (Boonson won 100m).
- Teens win: Yu Zidi (13!), Eala, Anahat Singh, Orfi, Sooryavanshi, Shelton-run. Teen challengers ≥.3 vs fading champs.
- Far-left Mamdani-mimics win city elections (Die Linke took Berlin).
- Trump-endorsed incumbents LOSE primaries (Ogles, Mills) but Trump bureaucratic/court picks hold (Overton, death penalty).
- War GDP: the attacked sector (Iran oil/gas) craters.
- Protection coalitions: announced by the VICTIM state (Saudi), not distant powers.
- Iran-aligned strikes outside Iran: Iraqi militias most often, not Houthis.
-Succession: ailing monarch "extremely serious" → successor ≈ .45-.50 (Haakon VIII).
- Verbal transfer agreements fail ~40% (Hadjam-Como): cap at .55-.60.

### 6. What worked operationally
- Day-1 full-coverage prediction of all 252 (each uncovered day = 0).
- Daily 3-5 focused agents on near-term resolvers + fresh-news signals (Assam floods, Michigan cyclospora, Canada smoke tariffs, King Harald hospitalisation, PAM winning Morocco — all cashed).
- Grep the local corpus FIRST (free), search_news second.
- Local corpus articles.jsonl per day is rich (~2-3k articles/day).

### 7. What kept hurting
- Lottery questions (obscure banks, unknown Nigerian officials, first-time events): accept ~.2-.3 expected loss, spread thin.
- Favorite-heavy golf/tennis singles: include 1-2 surprise candidates ~.08-.10 (Thorbjørnsen, Fils, Raul Fernandez, Tirante, Ngetich, Jepchirchir, Gobena all won unlisted).
- Chasing storylines too hard (Yanagita .40 home-soil).
