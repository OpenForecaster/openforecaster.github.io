# Sweep brief (2026-08-21) — read together with memory/AGENT_BRIEF.md

OVERRIDES to AGENT_BRIEF.md:
- **Simulation "today" is 2026-08-21.** Search results are date-capped at 2026-08-21. Do NOT call mcp__forecast__next_day.
- Free local corpus (English only): /agent/workspace/articles/2026/MM/DD/articles.jsonl for every day 2026-06-24 .. 2026-08-21.
  Grep the last ~3 weeks first (e.g. `grep -il "keyword" /agent/workspace/articles/2026/08/*/articles.jsonl`), then use searches.
- Use non-English searches for local news (Spanish/Portuguese/Italian/French/German/Arabic/Chinese/Japanese/Korean etc.).

## Your job
For each qid in your list (work in order given):
1. Read the question row in /agent/workspace/market.csv (title, background, resolution_criteria, resolution_date) — use python csv module.
2. Read /agent/workspace/memory/research/<qid>.md (prior notes; may not exist) and the CURRENT forecast in /agent/workspace/memory/forecasts_current.json (key = qid).
   Many forecasts are STALE (last researched June/July). Assume important news may have happened since (injuries, withdrawals, appointments, collapsed deals, schedule changes, new favourites).
3. Do 1-4 targeted searches (use from_date ~2026-07-25 to get the latest), plus corpus grep.
4. If the evidence changes the picture, submit a new forecast with mcp__forecast__submit_forecasts and then record it:
   `python3 /agent/workspace/scripts/record.py QID '<json dict>' "short reason" 2026-08-21`
   If nothing material changed, do NOT resubmit (the existing forecast stays active) — just note "no change".
5. Append to the note file: `## UPDATE 2026-08-21 (sweep)` + key new facts with dates/sources + submitted dict (or "no change") + NEXT CHECK date/queries. Keep it short.

## Hard-won rules (from 140 resolved questions)
- LABEL RULE: never use composite outcome strings ("Taizhou (Wenling/Yuhuan)", "Honor Flash/Lightning"). One precise entity per outcome.
- SYNONYM RULE: the grader does NOT reliably equate synonyms ("Phase One" vs "Group stage", "External demand" vs "Net exports", "Houthis" vs "Ansarallah"). Use the phrasing most likely to appear in mainstream English reporting; if two phrasings are plausible, split mass across both labels.
- NAME-VARIANT RULE: "Turkey" vs "Türkiye" was NOT credited. Split country renames (Türkiye/Turkey, Czechia/Czech Republic, Côte d'Ivoire/Ivory Coast) — put more on the form the question itself uses. Transliteration variants of people (Zhuravlov/Zhuravlev) were credited.
- HIJACK RULE (transfers): unless an official announcement/medical is reported, cap a reported favourite at ~0.60-0.75 and keep 0.2+ on plausible rivals. Collapsed deals happen often (late August!).
- PRIMARY/ELECTION RULE: 2026 is an anti-establishment year; cap judgment-only favourites at ~0.65 without strong polling.
- TRIVIAL-QUESTION RULE: if the official schedule already answers the question, it probably exists because something changed — cap the "as scheduled" answer ~0.5.
- Question wording often leaks that an event happened (auto-generated from later articles); resolution_date ≈ date of the resolving news.
- Calibration: judgment-only top pick ≤0.35-0.40; strong reporting 0.5-0.65; direct credible report of done deal/official schedule 0.7-0.9. Never >0.85 when a rival is in the same situation.
- Sports: use bookmaker odds/rankings when findable; check injuries/withdrawals/entry lists.
- Max 5 outcomes; sum ≤ 1; no placeholders ("Other", "Unknown"); use "None"/"Draw" only where the question allows.

## Budget
About 3 searches per question on average (hard max 70 searches for your whole batch). Prioritise questions resolving soonest and those most likely to have changed.

## Final message
Compact table: `qid | old top pick→new forecast dict (or "no change") | confidence | next check | 1-line reason`, plus searches used.
