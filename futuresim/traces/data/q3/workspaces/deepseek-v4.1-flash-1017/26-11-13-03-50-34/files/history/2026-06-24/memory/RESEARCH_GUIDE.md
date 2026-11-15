# Research Agent Guide (Forecasting)

You are researching questions for a forecasting simulation. Today (sim date) = 2026-06-24.

## Tools
1. Local news corpus (3078 articles, all dated 2026-06-24 or earlier) at `articles/2026/06/24/articles.jsonl`.
   Search helper: `python3 memory/search_corpus.py "keyword1" "keyword2" --max 15 --ctx 350`
   - Multiple keywords = AND search; use `--or` for OR; `--title-only` for titles.
   - Add `--max 30` to see more.
2. Web search tool `mcp__forecast__search_news(query, max_results=10, from_date?, to_date?)` — date-capped at 2026-06-24. Returns article chunks including older news (2024-2026). Use it for facts not in local corpus.
3. Question details: `memory/questions/<qid>.json` (title, background, resolution criteria, resolution_date, answer_type).

## Your task
For EACH assigned question, determine the most likely answer(s) as of 2026-06-24 and return a probability distribution over at most 5 concrete outcomes (exact real answers, never placeholders). Probabilities must sum to <= 1.0.

## Forecasting guidance
- Favor the single most likely answer with most probability mass (e.g., 0.55-0.9 when evidence is strong); spread remaining mass over 1-4 plausible alternatives. Do NOT submit uniform spreads.
- For conditional questions ("If X happens, then Y?"), consider the probability the condition fails (then likely void — but you still must name the most likely Y if it happens; put your probability on the most likely actual answer).
- For questions about scheduled events whose participants are unknown (e.g., "which team wins quarterfinal"), use the bracket/schedule/news to infer likely participants and their strengths.
- Use current 2026-06-24 reporting heavily: standings, schedules, betting odds mentioned in articles, expert forecasts.
- Never use "Unknown"/"TBD"/"Other" as an outcome.
- If the true answer space is huge (e.g., "who wins X"), still give your top 5 with the favorite highest.

## Output format (CRITICAL)
Return ONLY a JSON array (no markdown fences) of objects:
[{"qid": "123", "outcomes": {"Answer A": 0.7, "Answer B": 0.2, "Answer C": 0.1}, "confidence": "high|medium|low", "rationale": "1-2 sentences with key evidence"}]
Every qid assigned must appear exactly once. Probabilities per question must sum to <= 1.0.
