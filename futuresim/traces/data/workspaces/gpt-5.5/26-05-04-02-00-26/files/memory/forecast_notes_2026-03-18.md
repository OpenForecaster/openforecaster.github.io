# Forecast Notes - 2026-03-18

## Snapshot
- `state.json` absent.
- `market.csv`: 330 questions, 36 active, 294 resolved.
- Active questions all had existing predictions.
- New article corpus: `articles/2026/03/18/articles.jsonl`.

## Newly Resolved
- q388689 resolved `Asian Boxing Championships`; prior forecast had this at 0.30. Hit.
- q398208 resolved `Taiwan`; prior forecast had this at 0.05 after overweighting Hong Kong. Lesson: "intermediary before SE Asia" can be Taiwan when AI/server supply chains are involved.
- q512785 resolved `United Arab Emirates`; prior forecast had this at 0.01. Lesson: arms-sale background pointing to a Middle East partner was more useful than keyword evidence around Taiwan.
- q666706 resolved `Hawaii`; prior forecast missed. Lesson: celebrity obit location questions can resolve to hospitalization/vacation states, not home state.
- q724111 resolved `Tabriz`; prior forecast missed. Lesson: exact local incident details can be hidden behind broader Tehran/Iran reporting.
- q739439 resolved `Omar Oswaldo Torres`; prior forecast missed. Lesson: active detainee questions may resolve to less globally visible local cartel figures.

## Forecast Updates Submitted
- q668257: moved to `Gholamreza Soleimani` / spelling variant after Mar 18 funeral reports named Gholamreza Soleimani with Ali Larijani. Kept IRGC spokesman alternatives at lower weight because title wording may be noisy.
- q244043: tightened around `Old City` and specific holy-site fragments after reports placed Iranian fire/debris near Temple Mount, Western Wall, Jewish Quarter, and Church of the Holy Sepulchre.
- q757234: moved from Syria/Gaza/Lebanon rescue orgs toward `Iranian Red Crescent` after Mar 18 rubble-rescue articles and Red Crescent video references.
- q144493: modestly increased `Ecuador` for eastern Pacific drug-boat transfer after continued Ecuador/US anti-drug-operation evidence.
- q262505: increased `Qatar` for Dennis Coyle release/facilitation after reports of Qatar-mediated Kabul/Washington talks.
- q200605: increased `Iran` for Australia's proposed visitor ban after direct reporting that the law was aimed at people from Iran.

## Held Steady
- q50504: no reliable Paris bank target evidence found; kept BNP Paribas / Societe Generale mix.
- q655411: no exact Mattala combat-aircraft article found; kept Iran/US/Israel mix.
- q217580: no exact Sudan teaching-hospital attack evidence found; kept North Darfur top with Sudan conflict-state spread.
- q974962: no exact Eritrea vs Eswatini AFCON venue evidence found; kept Asmara/Benghazi/Cairo spread.
- q427993: no exact mass-grave evidence found; kept Syria/Sudan/Libya/Mexico/Iraq spread.
- q774274: no new Hezbollah northern-community target evidence found; kept Nahariya strongly top.

## Calibration Notes
- Exact-answer questions often hinge on a local official or article phrasing that is not the most common public clue.
- When a question background identifies a narrow class of counterparties, keep a meaningful probability on those candidates even if keyword search surfaces a different high-profile country.
- Add spelling variants when names are transliterated from Persian/Arabic and the resolution may use article wording.
