# Forecasting Lessons Learned

## Key Mistakes & Corrections

### 1. Iran Province Question (Q69214) - FAILED
- **Mistake**: Predicted Ilam (0.35) and Lorestan (0.30), but truth was Isfahan
- **Root Cause**: The question asked what "state television will SAY" - this is a political framing, not factual reporting. State TV chose to report on Isfahan province (Fuladshahr had a death), even though the heaviest fighting was in Ilam/Lorestan. State media may deliberately emphasize certain provinces for political reasons.
- **Lesson**: For questions about what state-controlled media "will say," consider the regime's propaganda interests, not just ground truth.

### 2. Thailand NIDA Poll (Q934187) - SUCCESS
- **Success**: Correctly identified Natthaphong Ruengpanyawut (0.45) by reading current news
- **Lesson**: Market aggregates can be dangerously outdated (had Paetongtarn, Srettha, Pita, Prayut - all no longer relevant). Always verify current candidates/names.

### 3. Nipah Virus (Q291796) - PARTIAL
- **Result**: Predicted Kerala 0.40, truth was West Bengal 0.20. Brier +0.14 (positive but weak)
- **Lesson**: Historical patterns (Nipah always in Kerala) don't guarantee future events. Need broader distribution.

### 4. Manchester United Manager (Q474377) - PENDING
- **Key finding**: Ruben Amorim was SACKED on Jan 5, 2026. Market still had him at 0.50.
- **Updated to**: Darren Fletcher (interim, 0.40), Ole Gunnar Solskjaer (0.30), Michael Carrick (0.15)
- **Lesson**: Sports questions require checking latest news - managerial changes happen fast.

### 5. "No X" Outcomes Pattern
- Multiple questions where "No embassy damaged," "No exclusion," "No severance," "No group named" outcomes are in play
- Be cautious about overweighting these - they can be correct but should be calibrated carefully

## General Calibration Notes
- Market aggregates are useful baselines but often outdated for fast-moving events
- For Middle East questions, state media reports may differ from Western/independent reporting
- The TW-score rewards early, accurate predictions - don't wait for perfect info
