# Forecast Notes - 2026-03-19

## Snapshot
- `state.json` absent.
- `market.csv`: 330 questions, 30 active, 300 resolved.
- Active questions all had existing predictions.
- New article corpus: `articles/2026/03/19/articles.jsonl`.
- `predictions/2026-03-18.json` exists and contains six Mar 18 submissions, even though the refreshed `market.csv` `my_prediction` column still showed earlier forecasts for those rows.

## Newly Resolved
- q144493 resolved `Costa Rica`. Missed; prior kept Costa Rica low at 0.05 while overweighting Ecuador/Colombia. Lesson: drug-boat survivor transfer may go to the closest safe legal-processing partner, not the most prominent anti-drug-operation country.
- q244043 resolved `Jerusalem's Old City`. Mar 18 submission had `Old City` top; keep using exact wording variants for place names when the article may add possessive/city context.
- q50504 resolved `Bank of America`. Missed; Paris bank target was an international bank, not a French domestic bank.
- q655411 resolved `United States`. Previous forecast had US at 0.16 but overweighted Iran/Israel. Lesson: Sri Lanka/Mattala military-aircraft questions are likely to resolve to a publicly named US request even when Iran-war logistics dominate search results.
- q668257 resolved `Ali Mohammad Naini`. The Mar 18 funeral reports caused an overcorrection toward Gholamreza Soleimani. Lesson: when the title specifies a role like IRGC spokesman, keep role-matched candidates high even if same-day funeral coverage highlights other officials.
- q757234 resolved `Iranian Red Crescent`. Mar 18 update moved this to the top after rubble-rescue reporting.

## Forecast Updates Submitted
- q217580: updated to `West Kordofan` top after Al Jazeera reported a market and hospital struck simultaneously in al-Muglad, West Kordofan.
- q427993: added `Democratic Republic of the Congo` and `DR Congo` variants after DRC mass-grave reporting surfaced in Al Jazeera related links; kept South Sudan/Syria/Sudan as alternatives because exact "exhumed" wording was not found.
- q262505: resubmitted the Qatar-heavy Dennis Coyle release forecast from Mar 18 because the refreshed market column lagged that update.
- q200605: resubmitted the Iran-heavy Australia visitor-ban forecast from Mar 18 for the same market-lag reason.

## Held Steady
- q974962: no exact Eritrea vs Eswatini AFCON venue found in local articles or semantic search.
- q774274: Nahariya remains strongly supported by Al Jazeera video coverage.
- q120805: Oman remains the best fit for Trump/Iran intermediaries; Swiss protecting-power coverage is a secondary risk.
- q554489: no exact New York ground-vehicle landing collision found; search returned Newark near-miss and unrelated Denver deicing collision.
- q581783: no exact North London arson/journalists article found.
- q718848: no exact southern Lebanon mosque-minaret article found.
- q740952: U.S. Air Force remains strongly supported by KC-135 crash reporting.
- q494140/q757107: no official IQAir 2025 annual report found yet.
- q698278: no exact Bolt Ventures/IPL franchise acquisition article found.
- q912807: no exact Lukashenko first-official-visit report found.

## Calibration Notes
- Treat `predictions/YYYY-MM-DD.json` as the audit trail for submitted updates when `market.csv` lags.
- Do not let broad same-day articles override a question's narrow role or descriptor unless the wording also matches.
- For country/location answers with likely naming variants, split a modest amount across the most likely article phrasings.
