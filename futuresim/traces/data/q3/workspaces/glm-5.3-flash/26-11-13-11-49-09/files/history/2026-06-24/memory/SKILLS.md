# Forecasting Skills & Workflow

## Day-1 workflow (proven)
1. Read market.csv → dump compact question list to memory/compact.txt (qid | date | title | criteria).
2. Grep local articles corpus (articles/YYYY/MM/DD/articles.jsonl) for clusters — free context.
3. search_news (max_results 4-7) for: tournament standings/odds, election primaries, active geopolitical events. ~2 searches per topic cluster.
4. Submit ALL questions day 1 with priors; refine daily for questions resolving within ~3 days.

## Odds conversion: moneyline → prob = 1/(1+odds/100) for +odds; prob = odds/(odds+100) for -odds; then normalize (remove ~8% vig by scaling).

## Outcome naming
- Answer format matters: full names ("Neeraj Chopra"), club common names ("Bayern Munich"), countries ("South Korea" not "Korea Republic").
- NO placeholders/question marks in outcome names (violates rules) — e.g. "Lijiao? Gong" was a mistake; resubmit to overwrite.
- Multi-word sets (e.g. PaK districts) submitted as single outcome strings.

## Probability allocation
- 5 outcomes max; allocate 0.6–0.95 total mass (implicit tail on unlisted outcomes).
- Conditional "if X" questions: scale by P(condition) ~0.5–0.7 for active rumors, ~0.85–0.95 for near-certain events.
- For void-able questions, my mass ≈ P(event happens) — leaving unallocated = implicit P(void/no answer).

## Day-2 watchlist (from day 1, 2026-06-24)
- June 26: Wimbledon draw → refine Wimbledon predictions (Sinner/Zverev halves; women's paths).
- Jun 25-27: WC group conclusions (E,F,H,I,J,K,L) → update bracket QF/SF predictions (Q199448, Q457239, Q935518, Q439898, Q241292, Q592683).
- Jun 30/Jul 2: T20 semis → update Q258607/Q799550.
- Watch: Salah signing (Q810891), Jaylen Brown trade (Q344207), Seahawks approval (Q902592), Moldova PM (Q76066), Dugan sentencing Jul 8 (Q213487), TN-9 Trump endorsement (Q362674), UK leader resignation (Q754639), Typhoon Bavi (Q446236/Q66613), England-India T20 (Q562262).
- Long-lead research when time: Emmy nominations (~mid-July), Asian Games entries, Leagues Cup format, US Open fields.

## Sources found useful
- ESPN/FIFA/CBS standings pages (via search_news), Polymarket/Ballotpedia for US primaries, Crash.net/motogp.com standings, FanDuel odds for golf/tennis, Sportico/Semafor for sales, local corpus: hindustantimes (India), cbsnews (US), straitstimes (SEA/Asia), aljazeera (MidEast), ndtv, irishtimes, koreaherald, khaleejtimes, gabonmediatime (Gabon/fr).
