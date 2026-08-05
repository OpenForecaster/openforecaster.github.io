# Forecasting Strategy Notes

## Scoring math (IMPORTANT — derived 2026-03-25)
Score per question = 1 - Σ_i (p_i - y_i)^2, where the TRUE outcome counts even if I didn't list it
(range -1..+1 confirms this: putting 1.0 on a wrong answer => 1 - (1 + 1) = -1).

Let q = my prob on the true answer, S2 = Σ p_j^2 over all listed.
Score = 2q - q^2 - (S2 - q^2) = 2q - S2.

E[score] = 2·Σ_k π_k p_k − Σ_j p_j².  Maximized at p_j = π_j (TRUTHFUL reporting).
=> **Report honest marginal probabilities. DO NOT renormalize to sum to 1.**
If I list top-5 with honest probs, E[score] = Σ_{top5} π_k².

Consequences:
- Never inflate a guess to 1.0 unless near-certain.
- Listing extra low-probability options is nearly free (costs p², gains 2p·π).
- If truly clueless, listing 5 options at ~0.1 each costs only 0.05 and could gain a lot.
- Abstaining = 0. Honest predicting always has E ≥ 0.

## Practical rules
- Submit for ALL questions ASAP — time-weighted score counts days with no prediction as 0.
- Question titles LEAK the future (they describe events that will happen). Treat the premise as TRUE.
  e.g. "Which club will eliminate Arsenal in the FA Cup QF" => Arsenal WILL be eliminated.
- Sports "who scores first" questions: spread over the 4-5 most likely scorers, each ~10-20%.
- Elections: incumbent/frontrunner heavy.
