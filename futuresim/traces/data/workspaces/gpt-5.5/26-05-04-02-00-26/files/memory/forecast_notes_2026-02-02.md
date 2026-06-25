# Forecast notes - 2026-02-02

Snapshot:
- `state.json` absent again.
- `market.csv`: 330 rows, 199 active, 131 resolved, 0 active without prediction.
- Feb 2 article file has 2,778 rows, 2,605 with `date_publish <= 2026-02-02`; ignored future-dated rows.

New resolutions / calibration:
- `220862` resolved Arsenal. Feb 1 update to Arsenal 0.68 was correct.
- `243685` resolved Union Consultative Council. Missed. Lesson: Myanmar panel names may be newly branded "consultative council" labels, not only existing junta bodies.
- `453736` resolved Saif al-Islam Gaddafi. Included but underweighted at 0.15.
- `492629` resolved Darius Garland. Missed entirely. Lesson: NBA trade questions can involve younger star guards not in the stale veteran-salary matching set.
- `955662` resolved Alagoas. Missed. Lesson: Brazil crash priors should include smaller northeastern states for severe bus crashes, not just the largest/highway-heavy states.
- `976004` resolved Zintan. Included but too low at 0.05.
- `995305` resolved Tehran. Missed. Lesson: market-fire city priors should include Tehran; do not overfocus on Russia/South Asia when Iran protest/crackdown context is active.

Submitted update:
- `426743`: Saif burial town -> Bani Walid 0.30, Zintan 0.24, Sirte 0.22, Sabha 0.05, Tripoli 0.03. Evidence: `453736` resolving Saif confirms the person, and `976004` resolving Zintan for forensic experts points to Zintan as a live death/probe location. Kept Bani Walid and Sirte high as likely loyalist/family burial sites.

No-update checks:
- `336425`: no clean eastern Ukraine market-shelling city; narrow searches were noisy/old. Keep Kostiantynivka prior.
- `57193`: no relevant Supreme Court congressional-map signal.
- `579252`: no Saleh Mohammadi city beyond earlier Fox report; no Amnesty/city hit.
- `630740`: no Lebanon building-collapse city.
- `883856`: no Moscow senior-officer shooting name.
- `14689` / `527803`: no school-shooting country/town signal.
- `739916`: Iran-tension articles confirm USS Abraham Lincoln and associated warships in the region but do not name a second carrier.
- `198725`: Narges Mohammadi appears only as a signatory in unrelated Iran-crackdown coverage; no exile city.
- `534224`: no new actionable women's downhill medal signal.
- `312764`: no Egypt planning-minister reshuffle signal.
- `795774`: no French far-right activist city.
- `456284`: no Washington Post publisher transition.
- `318661`, `398988`, `538697`: no Colombia talks, Lebanon abduction, or Gaza 8,000-troop signal.
- `487245`: Iran tensions remain active, but no direct clue for the late-February address question.
- `745180`: no Cyclone Gezani/Madagascar article.
- `613203`: no Tractor AFC playoff signal.
- `180958`: Super Bowl articles preview Seahawks-Patriots; no strong movement from Seattle 0.63 / New England 0.37.
- `304287`: Bangladesh articles still frame BNP and Jamaat as the main parties with Awami League banned; current Jamaat-as-opposition view remains intact.
