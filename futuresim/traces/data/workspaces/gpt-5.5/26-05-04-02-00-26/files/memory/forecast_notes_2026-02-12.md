# Forecast Notes - 2026-02-12

Snapshot:
- `state.json` absent.
- `market.csv`: 330 questions, 177 active, 153 resolved, no active questions missing a forecast.
- Feb 12 article batch: 3,361 rows, 3,335 with `date_publish <= 2026-02-12`.

New resolutions / scoring lessons:
- `304287` resolved Jamaat-e-Islami. Latest forecast had 0.58; good update after the IRI poll and election coverage.
- `739916` resolved Gerald R Ford. I moved too far to George Washington / George H.W. Bush after the Korea/Japan deployment pieces; keep some weight on the prior explicitly named asset when news says multiple carriers are plausible.
- `795774` resolved Lyon. I had Lyon top but only 0.14; city/location questions often need higher concentration once a specific article names a city.

Forecasts updated:
- `190197`: India beat Namibia heavily and now leads Group A on NRR over Pakistan. Pakistan remains likely to qualify, but the clinching win is more likely later against Namibia than directly against India. Updated to Namibia 0.52, India 0.31, Netherlands 0.05, United States 0.03.
- `454482`: West Indies beat England and lead Group C; England are the former champion with the clearest current failure risk. Sri Lanka now has two wins, reducing its risk. Updated to England 0.38, Sri Lanka 0.16, Australia 0.08, West Indies 0.07, Pakistan 0.04.
- `778783`: Sudan reporting keeps pointing to Kordofan. Recent named places include el-Obeid, Um Rawaba, Er-Rahad, Kadugli, and Dilling; removed Darfur/less-central candidates. Updated to el-Obeid 0.20, Um Rawaba 0.13, Er-Rahad 0.10, Kadugli 0.09, Dilling 0.06.
- `548734`: Strong signal for Storm Nils. It is now directly reported as battering France/Spain with French flooding and power outages. Updated to Storm Nils 0.72, Storm Marta 0.10, Storm Oriana 0.06, Storm Leonardo 0.04, Storm Kristin 0.03.
- `22203`: Bangladesh main opposition resolving as Jamaat implies a BNP-led government. Current interim-adviser names became too stale. BNP family coverage names Zaima Rahman and Zubaida Rahman; Zaima was campaigning publicly. Updated to Zaima Rahman 0.18, Zubaida Rahman 0.12, Sharmeen S Murshid 0.08, Syeda Rizwana Hasan 0.06, Rumeen Farhana 0.05.

No-change checks:
- No new signal for Navalny toxin, Italy rail city pair, Rousey opponent, Russian town explosion, Benfica/Vinicius player, Iranian frigate, France-US ambassador/office, Lebanon command centre group, Afghanistan provinces, Pakistan motorcycle-bomb district, Greek island, or South Africa T20 captain.

Carry-forward lessons:
- For exact-string location questions, track article spellings (`el-Obeid`, `Um Rawaba`) because prior spelling variants can waste probability.
- When a question is generated around a future article pattern, update away from stale opening priors once a nearby article names the relevant object even if official resolution is not yet posted.
