# Forecast Notes - 2026-03-20

## Snapshot
- `state.json` absent.
- `market.csv`: 330 questions, 27 active, 303 resolved.
- Active questions all had existing predictions.
- New article corpus: `articles/2026/03/20/articles.jsonl`.
- `market.csv` still showed stale `my_prediction` values for some active rows, while `predictions/2026-03-19.json` recorded the actual Mar 19 submissions.

## Newly Resolved
- q217580 resolved `East Darfur`. Missed; Mar 19 update went to West Kordofan from al-Muglad hospital reporting. Lesson: Sudan hospital questions may hinge on a later/parallel local hospital item, not the most visible conflict-casualty article.
- q427993 resolved `Kenya`. Missed; I overweighted DRC/South Sudan/Syria. Lesson: "authorities identify mass grave" can be a domestic criminal-investigation story, not only a war-zone atrocity story.
- q974962 resolved `Meknes`. Missed; Eritrea's neutral-host AFCON venue was Morocco rather than nearby regional options. Lesson: African neutral football hosts can be CAF/association-friendly Moroccan cities even for East African teams.

## Forecast Updates Submitted
- q774274: increased `Nahariya` to 0.75 after repeated Al Jazeera coverage of a Hezbollah rocket hitting a residential building in Nahariya.
- q554489: moved to `Portland` / `Portland, Oregon` after reporting identified Alaska Airlines Flight 294 as arriving from Portland during the Newark landing near-miss. Kept Memphis for the FedEx aircraft.
- q494140: moved `Chad` top for IQAir most-polluted country, using the 2024 IQAir ranking and no contrary 2025 report yet.
- q757107: moved `Byrnihat` top for IQAir most-polluted city, supported by the 2024 IQAir report and 2025 Indian PM2.5 assessments ranking Byrnihat first.
- q698278: moved `Rajasthan Royals` top after reporting said Rajasthan had started a sale process and potential candidates included Aditya Birla Group with American investor David Blitzer.
- q26340: increased `Bahrain` after reporting said Bahrain accused Iran of damaging a desalination plant in a drone attack.
- q262505: resubmitted Qatar-heavy Dennis Coyle forecast because the active market column still lagged the previous update.
- q200605: resubmitted Iran-heavy Australia visitor-ban forecast for the same market-lag reason.

## Held Steady
- q120805: Oman remains strongly supported by prewar mediation and CBS/Face the Nation references to a deal presented through Oman; direct Witkoff-Araghchi contact is a secondary risk but not a country intermediary.
- q581783: no exact North London arson/journalists story found.
- q718848: no exact mosque-minaret town found; recent southern Lebanon strike reports mention Bafliyeh, Hanine, Majdal, Kafr Sasir, Qlayaa, Qattine, Khiam, Bint Jbeil, Mefdoun, but none with the minaret phrasing.
- q740952: U.S. Air Force remains strongly supported by KC-135 crash reporting.
- q912807: no exact Lukashenko first-official-visit report found.
- q240291: no exact Latvian drone-link report found.
- q560679: ADNOC remains strongly supported by UAE Habshan/Bab energy-facility reporting.
- q795856: no exact three-journalist fatal strike town found; current Lebanon journalist reports involve an injured RT crew near Al-Qasmiya Bridge.
- q267975: no exact Sudan aid-disruption state found; Save the Children/WHO reporting is Sudan-wide and Darfur-focused.

## Calibration Notes
- Do not overfit to the highest-volume war article when the question wording sounds like a small local police or sports-administration item.
- For annual-report questions, prior-year official report plus current partial data is better than generic priors when the new report is not yet visible.
- For stale market rows, continue checking `predictions/YYYY-MM-DD.json` before assuming an update failed.
