# Superforecasting Rules & Scoring Playbook

## 1. Exact Scoring Formula (CRITICAL!)
- **Brier Skill Score (BSS)** = `1 - Σ(p_i - y_i)^2` summed over ALL possible outcomes (including unsubmitted outcomes with implicit `p = 0`).
- Expected BSS for submitting up to `k <= 5` outcomes with probabilities `p_1..p_k` (sum `<= 1.0`) when true probabilities are `q_1..q_k`:
  `E[BSS] = Σ_{i=1..k} (2 * q_i * p_i - p_i^2)`
- **Optimal strategy**: Set `p_i = q_i` (the TRUE marginal probability of outcome `i`)!
  - **DO NOT renormalize the top 5 outcomes to sum to 1.0** when significant probability lies outside your top 5!
  - If top 5 candidates truly cover only 35% of total probability (e.g., open-field golf/tennis/political/transfer/event question), submit probabilities summing to `~0.35` (e.g. `0.10, 0.08, 0.07, 0.05, 0.05`). Inflating them to sum to `1.0` produces NEGATIVE expected BSS!
  - If the event is exhaustive within `<= 5` outcomes (e.g., a 2-team series, 3-way football match Win/Lose/Draw, 2-fighter UFC bout, or a settled race with 2-5 real contenders), probabilities SHOULD sum close to `1.0` (e.g., `0.95` to `1.00`).
  - Even small positive probabilities (`0.05`, `0.08`, `0.12`) earn positive expected BSS (`+q^2`) when well-calibrated, whereas abstaining earns `0`.
  - Never over-bet on weak guesses: if true `q = 0.15` and you submit `p = 0.50`, `E[BSS] = 2(0.15)(0.50) - 0.25 = -0.10` (NEGATIVE!).

## 2. Conditional vs. Explicit-"None" Questions
- **READ `resolution_criteria` CAREFULLY!**
- If criteria explicitly define an outcome string like `"None"`, `"Draw"`, `"No winning scorer"`, or `"No organization qualified"`, include that exact string when it has real probability!
- If criteria say **"If no qualifying X occurs, the question is void"** (or "If X happens, which Y?" with no "None" option), predict the **conditional probability** `P(Y | X occurs)` — do NOT allocate probability to "None" or placeholders!
- NEVER use placeholders like `"Unknown"`, `"TBD"`, `"Other"`, `"N/A"`.

## 3. Exact Answer Formatting
- Always match `Accepted Answer Format` in `resolution_criteria` verbatim:
  - Full name vs. surname vs. regnal name with ordinal.
  - Full NBA/MLB/NFL team names (e.g., `Houston Rockets`, `Los Angeles Dodgers`), standard football club names (e.g., `Real Madrid`, `Manchester City`, `Arsenal`, `Paris Saint-Germain`), common English country names (e.g., `United States`, `United Kingdom`, `China`, `Mexico`), full U.S. state names (e.g., `Texas`, `California`), full English month names (`September`, `August`).
  - Multi-entity alphabetical or `and`-joined formats when specified (`Argentina, Brazil` or `District A and District B`).

## 4. Evidence & Search Discipline
- Today's simulation date is strictly respected; never hallucinate 2026 events without evidence!
- First check local SQLite FTS5 index (`python3 /agent/workspace/scripts/index_articles.py search "..."`) — FREE!
- Use `mcp__forecast__search_news` selectively and efficiently (we have a 3,000 total budget across ~98 days). Combine related questions into shared queries where possible.
- Remember: facts from **early-to-mid 2026** (transfers, deaths, elections, tournaments, standings, injuries, current champions, schedules) MUST be verified via `search_news` or local articles, because 2026 has already had major real-world events by June 24, 2026!

## 5. Calibration Benchmarks
- **99% (0.98–0.99)**: Event has officially occurred and been confirmed by authoritative source matching criteria, just awaiting resolution date.
- **85–95%**: Heavy structural favorite / near-lock (e.g., reigning healthy monarch for next 2 months, dominant leader with huge gap, formally agreed deal pending signature).
- **60–80%**: Clear favorite with realistic upset path (e.g., strong favorite in a 2-way match, leading candidate with big polling lead).
- **30–55%**: Leading contender in a competitive 2-4 way field.
- **10–25%**: Favorite in a wide-open multi-candidate field (e.g., World Cup winner, Grand Slam winner, PGA tournament, transfer rumors with multiple suitors, surprise news event).
- **3–10%**: Speculative candidate in a huge field (e.g., unknown future news event like "which US state will sue X", "which country will announce Y", long-shot athlete). Keep total sum realistic (often `0.15–0.45` total across 5 candidates)!
