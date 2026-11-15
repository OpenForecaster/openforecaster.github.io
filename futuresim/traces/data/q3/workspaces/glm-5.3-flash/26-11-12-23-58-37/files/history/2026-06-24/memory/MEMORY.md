# Agent Memory / Lessons Learned

## CRITICAL PROCESS RULES
1. **QIDs are NOT row numbers.** Always look up qid by grepping market.csv by title substring before submitting. (Session 1: ~8 wrong-ID errors; 2 overwrote good predictions — 243962 (Rodri) and 138739 (Christa Pike) — both caught & fixed via re-submission.)
2. **Keep /workspace/submitted.txt updated** with every submitted qid; diff against market.csv qids before ending session to ensure 100% coverage (a day with no prediction = daily score 0).
3. **Probability rules (score = 1 - Σ(p_i - y_i)^2 over outcomes):**
   - Conditional questions that may VOID ("If X happens, which Y?"): use UNCONDITIONAL probabilities — do NOT renormalize to 1. Void cost = Σp² only.
   - Must-resolve questions: assign residual mass across my 5 listed outcomes (top-5 usually covers 80-95%).
   - Unlisted outcome = p=0 → if it occurs, loss += 1 for that outcome. Ensure most-likely outcomes are listed.
   - Test matches / football matches: include "Draw" as outcome.
4. Max 5 outcomes; sum ≤ 1.0. No placeholders.

## SOURCES
- Web search (mcp search_news): broad Exa index, date-capped. Use for: standings, brackets, odds, form.
- Local corpus (articles/2026/06/24): only 1 day; titles.py greps titles. Weak.
- Betting odds tables are gold for sports questions — mine them.

## WORLD STATE — see WORLD_STATE.md (Iran war, WC bracket, F1, UK crisis, Fed/Warsh, PL 2025-26 results)

## Session 1 (2026-06-24) summary
- Submitted predictions on ALL 252 questions. Very wide confidence: strong (LeBron Lakers, Mbappe GB, Antonelli F1, Salah Al-Ittihad) → pure priors ( obscure transfers, Asian Games events, Nigerian suspension).
- TODO next session (2026-06-25):
  1. WC group stage final matches June 25-27 → R32 bracket firms. RE-DO QF/SF/final predictions with actual bracket. Boston QF = W89 v W90 [Germany/Paraguay/France/Sweden × SKorea/Switz/Netherlands/Morocco]; KC QF = W95 v W96 [Argentina/Uruguay/Australia/Iran × Canada/Belgium/Colombia/Croatia].
  2. Wimbledon draw June 26 → check Sinner/Djokovic/Zverev halves; Sabalenka/Rybakina/Swiatek paths. Update men's/women's title + first-finalist.
  3. T20 WC semis (Jun 30/31, final Jul 5): Australia 3-0 dominant. Check semis lineup; update winner/POT.
  4. Watch for: UK party leader resigning as MP (noms Jul 9); SK Hynix ADR pricing (Jul 10); Khamenei funeral Jul 4-9 (Russian official); Bavi typhoon; Moldova PM; Dugan sentencing Jul 8; Noul typhoon late July.
  5. England-India T20 series — check dates; if it starts early July, home England slight fav.
- Scores update: predictions persist until re-submitted; keep refining as news arrives. Prefer updating before question resolution dates.
