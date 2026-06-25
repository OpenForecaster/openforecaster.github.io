# Forecast notes - 2026-03-08

Snapshot:
- market.csv: 330 rows, 78 active, 252 resolved; 0 active without predictions. state.json absent.
- predictions/2026-03-08.json: 6 updates submitted.
- Mar 8 articles: 1767 total in local file; 1659 usable with date_publish <= 2026-03-08, 108 future-dated and ignored.

Resolved today:
- q179817 Sri Lanka coach: Gary Kirsten. Missed; I over-weighted obvious Sri Lanka cricket names.
- q271330 Australia missiles recipient: United Arab Emirates. Missed; broad country diversification would have helped.
- q304016 airline suspending 2026 outlook: Air New Zealand. Missed; avoid overfitting US/Europe airline priors.
- q309487 Ukrainian region almost entirely retaken: Dnipropetrovsk. Missed; exact-location questions need broad regional coverage.

Updates submitted:
- q399040 Iran World Cup relocation: Canada 0.45, Mexico 0.40, Qatar 0.03, UAE 0.02, Turkey 0.01. Evidence still says all Iran games are in the US and analysts discuss Canada/Mexico as the relevant non-US host alternatives; concentrated away from non-host countries.
- q932855 China AFC WAC quarterfinal opponent: Australia 0.56, Chinese Taipei 0.32, Vietnam 0.04, Philippines 0.03, South Korea 0.01. South Korea topped Group A after 3-3 with Australia; Australia is A2 and will play either China or North Korea. China must beat North Korea to avoid Australia.
- q935869 Liverpool first-leg only goal: Salah 0.18, Wirtz 0.09, Victor Osimhen 0.08, Gakpo 0.06, Darwin Nunez 0.04. Local Mar 8 TV listings identify Galatasaray v Liverpool, so included Galatasaray's main striker rather than only Liverpool players.
- q828811 Beirut apartment organisation: Quds Force 0.40, Islamic Revolutionary Guard Corps 0.32, IRGC Quds Force 0.10, Hezbollah 0.05, Jamaa Islamiya 0.02. Mar 8 Al Jazeera says the Ramada/Raouche apartment strike targeted IRGC/Quds Force commanders.
- q857856 March 13 AFC WAC QF loser staying alive in playoff: Australia 0.42, China 0.30, North Korea 0.18, Chinese Taipei 0.03, Vietnam 0.02. The March 13 QF is now likely Australia vs China/North Korea, so old Philippines/Vietnam weighting was stale.
- q506444 team beating South Korea to final: Australia 0.45, China 0.18, North Korea 0.12, Japan 0.04, Chinese Taipei 0.03. Bracket path points to winner of Australia vs China/North Korea as the likely semifinal opponent for South Korea.

Watch next:
- Mar 9: China vs North Korea and Group C closeout should settle q932 and sharpen q857/q506.
- q605 remains ambiguous: evidence still points mostly to Kataib/Kataeb Hezbollah, but keep an eye for an "Islamic Resistance in Iraq" umbrella claim.
- q828 may resolve as either "Quds Force" or "Islamic Revolutionary Guard Corps"; use exact wording from official/Al Jazeera reports.
- Continue filtering future-dated search hits; NDTV/other articles have leaked future publish dates in results.
