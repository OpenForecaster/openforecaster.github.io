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

### 5. "No X" Outcomes Pattern - CRITICAL FAILURE (Feb 3 batch)
- **Q336425** (Ukraine market shelling): Predicted "No city identified" 0.50. Truth: **Druzhkivka**. Brier -0.32.
- **Q426743** (Gaddafi burial): Predicted "No burial reported" 0.75. Truth: **Bani Walid** (had it at 0.05). Brier -0.48.
- **Q57193** (SCOTUS map ruling): Predicted "No such ruling" 0.70. Truth: **California** (had it at 0.12). Brier -0.28.
- **Q579252** (AI wrestler execution): Predicted "No such report" 0.70. Truth: **Qom** (not in my options). Brier -0.52.
- **CRITICAL LESSON**: "No event" outcomes are NOT safe defaults. In all 4 cases, the event DID happen within the timeframe. I overweighted "no news found" as evidence for "no event occurred." Events DO happen even when my search doesn't find them.
- **Root Cause**: My search tool may have limited coverage/dates. Just because I don't find evidence doesn't mean the event didn't happen. The resolution may use sources I can't access.

### 6. Market aggregates are often wrong but events still occur
- Pattern: Many resolved questions have answers outside the market-listed options AND outside my search results
- Q102687 (Norwegian PM): Truth was Thorbjorn Jagland - not in market
- Q449104 (Minerals stockpile): Truth was Project Vault - completely unexpected
- Q453736 (Al Jazeera Libya): Truth was Saif al-Islam Gaddafi
- Q492629 (Harden trade): Truth was Darius Garland
- Q955662 (Brazil bus crash): Truth was Alagoas
- Q976004 (Libya forensic experts): Truth was Zintan
- Q995305 (Market fire): Truth was Tehran

### 7. Feb 9 Batch Results - MIXED, KEY LESSONS
- **Q14689** (fatal mass shooting country): Truth=Canada. Had USA 0.30, no Canada. Brier -0.12. Canada had a school shooting I missed!
- **Q312764** (Egypt planning minister): Truth=Ahmed Rostom. Had Rania Al-Mashat 0.30. Brier -0.12. Another completely unknown name.
- **Q487245** (Trump address tensions country): Truth=Iran. Had Iran at 0.15. Brier +0.16. SUCCESS - correctly identified Iran as plausible.
- **Q527803** (Canada school shooting town): Truth=Tumbler Ridge. Had only major cities. Brier -0.03. Tiny BC town, completely unexpected but small error (only 0.39 total probability allocated).
- **Q745180** (cyclone Gezani rivals): Truth=Geralda. Had Batsirai/Freddy 0.22 each. Brier -0.14. Geralda was not in my research at all.
- **LESSON**: Canada had a school shooting in Tumbler Ridge - I failed to detect this in news. Q14689 and Q527803 were connected.
- **LESSON**: "Outsider" answers continue to dominate - 4 of 5 questions had answers NOT in my options list
- **Cumulative stats**: Accuracy 6.7%, Brier -0.021, TW-Score -2071.30

## General Calibration Notes
- Market aggregates are useful baselines but often outdated for fast-moving events
- For Middle East questions, state media reports may differ from Western/independent reporting
- The TW-score rewards early, accurate predictions - don't wait for perfect info
- **CRITICAL**: Never overweight "no event" outcomes based on limited search results
- **CRITICAL**: Spread probability more evenly across specific answers — events are more likely to occur than not
- **CRITICAL**: Consider the search tool's limitations — it may not capture all relevant news, especially from non-English sources or regional outlets
- **NEW**: Answers continue to overwhelmingly fall outside my listed options (~80%+ of resolved questions). Strategy may need fundamental rethinking.
- **NEW**: For country/city identification questions, tiny/obscure locations are frequently the answer (Tumbler Ridge, not Toronto/Vancouver/Montreal)

### 8. Final 3 Questions (March 28, 2026) - ALL FAILED
- **Q144312** (Jerusalem Palm Sunday worship statement): Truth = **Emmanuel Macron**. Had Pope Francis 0.30, Guterres 0.25, King Abdullah 0.20. Brier -0.23.
  - **Lesson**: French presidents (Macron) are active Middle East mediators. Didn't even consider him.
- **Q26340** (Iranian raid kills worker at power/water plant): Truth = **Kuwait**. Had Iraq 0.35, Pakistan 0.25, Afghanistan/Azerbaijan/UAE. Brier -0.24.
  - **Lesson**: Iran attacked many Gulf states during the war, but I only focused on neighboring countries. Kuwait was hit too.
- **Q267975** (Sudan aid disruption state): Truth = **White Nile State**. Had East Darfur 0.30, North Darfur 0.25, West Darfur 0.20, South Kordofan, Blue Nile. Brier -0.23.
  - **Lesson**: White Nile State - completely outside the Darfur/Kordofan/Blue Nile conflict zones I considered. Aid disruptions happen in unexpected places.

## FINAL SESSION STATISTICS
- **Total**: 330 questions, 330 resolved
- **Accuracy**: 11.8% (39/330 where top outcome matched truth)
- **Brier Skill Score**: -0.062
- **Time-Weighted Score**: -6514.36
- **Correct predictions** (~17% had at least one option matching): North Korea, UAE, Japan, Israel Katz, Bernie Sanders, UAE arms sale, UAE facilitation, Pakistan polluted country, Iran visitor ban, Ukraine drone, Houthis, Snapchat, and a few others
- **Key failure pattern**: ~83% of answers were NOT in my top options. The search tool's limited coverage systematically prevented identifying the correct answer.
- **Most common failure**: Predicting specific named entities that weren't the answer, while the actual answer was something I never found in search results.
- **Best performers**: Questions about ongoing war events (Houthis, Ukraine drone, Iran visitor ban) where the combatant was predictable from the conflict context.

## STRATEGIC INSIGHTS FOR FUTURE
1. **The search tool is the binding constraint** - answers consistently fell in the gap between what I could find and what actually happened
2. **Market options often mislead** - many market-listed options made no sense for the question context
3. **"No event" is almost never right but neither are my specific guesses** - the truth tends to be a specific entity I didn't consider
4. **Wider probability distribution helps marginally** - spreading across 5 options minimized individual Brier losses but didn't solve the fundamental problem
5. **Time-weighted scoring rewards early submission** - but submitting early with wrong probabilities still yields negative scores
