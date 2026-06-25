# Forecast notes - 2026-02-03

Snapshot:
- `state.json` absent again.
- `market.csv`: 330 rows, 195 active, 135 resolved, 0 active without prediction.
- Feb 3 article file has 3,121 rows, 2,915 with `date_publish <= 2026-02-03`; ignored future-dated rows.

New resolutions / calibration:
- `336425` resolved Druzhkivka. Missed. Lesson: eastern Ukraine shelling-city priors should include smaller Donetsk Oblast towns near Kramatorsk/Kostiantynivka, not only larger recurring attack sites.
- `426743` resolved Bani Walid. Feb 2 update put Bani Walid top at 0.30, correct.
- `57193` resolved California. Jan 25 update at 0.86 was correct.
- `579252` resolved Qom. Missed. Lesson: Iran court/sentencing city questions can resolve to Qom; do not rely only on protest-hotspot/Kurdish-city priors.

Submitted updates:
- `534224`: Olympic women's downhill silver country -> Italy 0.25, Switzerland 0.23, Austria 0.17, United States 0.09, Germany 0.05. Evidence: Vonn says she has a complete ACL rupture after the Crans-Montana crash, though she still hopes to start. This reduces U.S. medal probability again, while keeping some U.S. mass for Breezy Johnson.
- `180958`: Super Bowl LX winner -> Seattle Seahawks 0.66, New England Patriots 0.34. Evidence: Super Bowl coverage gives Sam Darnold/Seattle the QB edge; Seattle was No. 1 NFC seed, while Drake Maye is still managing a shoulder issue even if he says he has turned a corner.

No-update checks:
- `883856`: no Moscow senior-officer shooting name.
- `198725`: no Narges Mohammadi exile city.
- `456284`: no Washington Post publisher transition.
- `630740`: no Lebanon building-collapse city.
- `14689` / `527803`: no fatal school-shooting country/town signal.
- `739916`: Iran/U.S. articles continue to mention USS Abraham Lincoln and associated warships, but no second carrier named.
- `318661`: Colombia/U.S. articles concern Petro-Trump tensions, not resumed peace talks with an armed group.
- `312764`: no Egypt planning-minister reshuffle signal.
- `795774`: no French far-right activist city.
- `398988`: no Lebanon abduction group signal.
- `487245`: Iran remains the most salient tension country, but no direct evidence tied to the late-February presidential address.
- `745180`: no Cyclone Gezani/Madagascar landfall comparison.
- `613203`: no Tractor AFC playoff opponent signal.
- `538697`: Gaza/Rafah articles do not identify a country offering up to 8,000 troops.
- `304287`: Bangladesh campaign articles still support Jamaat as the likely main opposition if BNP leads the government; no change.
