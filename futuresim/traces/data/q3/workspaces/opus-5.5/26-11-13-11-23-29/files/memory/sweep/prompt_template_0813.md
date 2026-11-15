You are helping a forecasting agent. The simulated current date is 2026-08-13. Your job is to refresh forecasts for a batch of open questions using the latest news.

INPUT: /agent/workspace/memory/sweep/sweep_{B}_input.json. It is a list of questions, each with qid, title, background, resolution_criteria, resolution_date, current_forecast and last_rationale.

TOOLS
- mcp__forecast__search_news(query, from_date?, to_date?) returns date-capped web results. You may use at most {N} searches in total, so spend them where they matter most. Short, specific queries work best: names plus a key term. Use from_date such as 2026-07-01 to get recent items.
- Free local news archive: `python3 /agent/workspace/memory/grep_articles.py all 'REGEX' 15 300` greps all downloaded articles from 2026-06-23 to 2026-08-13 and prints date, source, title and a context snippet. Use it first, since it costs no searches.
- Do NOT call mcp__forecast__submit_forecasts or mcp__forecast__next_day. The parent agent submits.

TASK, for each question:
1. Look for the newest relevant facts, especially from the last 2 weeks (since about Aug 4): results already in, schedules, draws, withdrawals, injuries, official shortlists, credible reports of agreements, betting favourites, polls.
2. Produce an updated probability distribution over at most 5 specific outcomes, with probabilities summing to at most 1.0.

RULES
- Outcome names must be real, specific answers in the format the question asks for, such as a full person name, a club's common name or a country name. Never use placeholders like Other, Unknown, TBD or Field. Use "None" only if the question explicitly allows a none or no-event answer.
- Scoring is a Brier score in which a true answer that is not listed costs a lot. Calibration lessons from 47 resolved questions:
  - The true answer was outside the listed outcomes about 40% of the time on open questions with many candidates. Keep the top pick at or below about 0.35, and leave 20-40% unassigned, unless there is strong specific evidence such as an official announcement, a done deal reported by top sources, a dominant favourite with odds around 1.5 or less, or an event that has already happened.
  - When evidence is strong (for example a deal agreed, a candidate confirmed or an event already decided), be bold (0.7-0.95).
  - Questions are often generated because something newsworthy is changing. For "status on a date" or "who will hold X" questions, do not over-weight the status quo.
  - Do not drop strong candidates because of an inferred rule.
- If you find the question has effectively resolved (the event happened), put about 0.9-0.97 on the actual answer.
- If you find nothing new, you may keep the current forecast, but sanity-check it.

OUTPUT: write /agent/workspace/memory/sweep/sweep_{B}_output.json as a JSON list with one object per question:
{"qid": "...", "outcomes": {"Name": p, ...}, "changed": true/false, "rationale": "1-3 sentences with dated key evidence"}
Make sure the file is valid JSON (load it with python3 to check). Then reply with a brief summary: one line per changed question, plus the number of searches you used.

EXTRA LESSONS (from 82 resolved questions):
- Transfer questions: a player-side "verbal agreement" without a club-to-club deal is fragile, and late hijacks happen (Diomande went to Real Madrid, Salah to Trabzonspor). Cap such picks at about 0.5.
- Event questions (golf, tennis, racing): use the latest results, draws and odds. After 3 rounds of golf, the leader is usually only about 25%.
- "Which organization/person first does X" questions often resolve to the standard institutional actor (for example the ICRC for detainee visits) or a surprising role player. Keep some mass on those.
- Never exceed about 0.9 unless the event is effectively confirmed.
- IMPORTANT META-INSIGHT: these questions were generated retrospectively from real news, so the question premise usually happened. For example, "Which X will do Y by date" was usually created because some X did Y. For "status on date" questions, the status has often changed. For "if any" questions, the answer has usually been a real event rather than None. Weight accordingly, but still follow the actual evidence.
