# Forecasting Agent Persistent Memory & Daily Runbook

## Current Status (End of Day 1: 2026-06-24)
- **Active questions forecasted**: 252 / 252 (0 missing, 0 validation issues; probability sums min=0.20, median=0.86, mean=0.78, max=1.00).
- **Search budget**: ~2,594 of 3,000 `search_news` calls remaining (~97 days left → ~26.7 searches/day average). Always pass `"max_results": 10` on every `search_news` call!
- **Local articles DB**: `/agent/workspace/memory/articles.db` (SQLite FTS5, opened with `?nolock=1` when indexing and `?immutable=1` when querying — required because workspace filesystem does not support POSIX/WAL file locks!).
- **Per-question state**: `/agent/workspace/memory/forecasts/<qid>.json` stores `outcomes`, `watch_keywords`, `key_facts`, `last_updated`, `next_review_trigger`.
- **World Cup Monte Carlo Simulator**: `/agent/workspace/memory/wc2026_sim_final.py` (update daily as World Cup matches resolve through July 19!).

## Daily Execution Runbook (Days 2–98)
1. **Verify previous day's submissions** (on Day 2 only, spot-check `predictions/2026-06-24.json` & `market.csv` `my_prediction` to ensure all 252/252 recorded cleanly; submit any missed qids immediately).
2. **Run Daily Triage** (indexes new `articles/YYYY/MM/DD/articles.jsonl`, logs newly resolved questions + BSS to `memory/resolved_log.jsonl`, scans today's ~3,000 local articles against `watch_keywords`, selects priority questions & computes dynamic daily search budget):
   ```bash
   python3 /agent/workspace/scripts/daily_triage.py --today <YYYY-MM-DD> --searches-remaining <N>
   ```
3. **Review Newly Resolved Post-Mortems**: Check `newly_resolved` output for any formatting mismatches or calibration lessons and append lessons to this file.
4. **Run Parallel Daily Update Workflow**:
   Call `run_workflow` with `ScriptPath="/agent/workspace/scripts/run_daily_update.py"` and `Args={"today": "<YYYY-MM-DD>"}`.
   - Agents inspect matched local articles first, spend search credits selectively (always `max_results=10`, using `from_date`), call `submit_forecasts` for any changed/unpredicted questions, and update `/agent/workspace/memory/forecasts/<qid>.json`.
   - For FIFA World Cup days (June 25 – July 19), ensure `wc2026_sim_final.py` is updated with completed match results for coherent bracket probabilities across all 9 World Cup questions!
5. **Audit & Advance**: Confirm 0 unpredicted active questions, update remaining search count in `memory/MEMORY.md`, and call `mcp__forecast__next_day()`.

## Key Technical Notes & Lessons
- **Exact Brier Skill Score**: `BSS = 1 - sum((p_i - y_i)^2)` across all outcomes → optimal submitted probability for each of the top `<= 5` outcomes equals its TRUE unnormalized marginal probability `q_i`. NEVER inflate open-field top-5 sums to 1.0!
- **Max results**: `search_news` accepts `max_results=10` (2× default 5) for 1 search credit — always use `10`.
- **SQLite URI flags**: Always use `?nolock=1` (write) and `?immutable=1` (read) on `/agent/workspace/memory/articles.db`.
- **Key-quoting caution**: Ensure outcome dictionary keys have no stray embedded quotes or leading/trailing whitespace.
