# Forecast notes - 2026-02-07

Snapshot:
- `state.json` absent again.
- `market.csv`: 330 rows, 190 active, 140 resolved, 0 active without prediction.
- Feb 7 article file has 1,951 rows, 1,774 with `date_publish <= 2026-02-07`; ignored future-dated rows.

New resolution / calibration:
- `180958` resolved Seattle Seahawks. Correct at 0.66.
- `534224` resolved Germany. Included only as 0.04 tail. Lesson: even with strong Goggia/Swiss/Austria/Vonn narratives, Olympic alpine silver has a wide tail; do not compress too much around pre-race favorites and one late training report.

Submitted updates:
- `901381`: Italian high-speed rail burned-cables section -> Bologna and Venice 0.78, Bologna and Milan 0.08, Milan and Venice 0.03, Milan and Bologna 0.02, Pesaro and Bologna 0.02. Evidence: Reuters/Straits says the fire targeted the line between Bologna and Venice; Irish Times/Reuters also says the Bologna high-speed station was temporarily closed and Bologna is the rail hub linking Milan and Venice.
- `190197`: Pakistan qualifying win -> Namibia 0.45, United States 0.24, Netherlands 0.08, India 0.05. Evidence: Pakistan beat Netherlands on Feb 7 but still has little margin after the planned India boycott; fixture list has Pakistan vs USA on Feb 10 and Pakistan vs Namibia on Feb 18, making Namibia the more likely clinching match if qualification remains unsettled.
- `487245`: country named as U.S. address tension source -> Iran 0.40, Venezuela 0.12, China 0.09, Russia 0.06, Israel 0.04. Evidence: Feb 7 coverage centers U.S.-Iran talks, new sanctions, the USS Abraham Lincoln deployment, and warnings of steep consequences if talks fail.

No-update checks:
- `318661`: no Colombia peace-talk resumption group signal.
- `398988`: no direct Lebanon abduction report; Hezbollah remains modal.
- `630740`: no Lebanon building-collapse city signal.
- `538697`: Gaza/peacekeeping coverage does not name the 8,000-troop country.
- `14689` / `527803`: no fatal school-shooting country/town signal.
- `312764`: no Egypt planning-minister reshuffle signal.
- `745180`: no Cyclone Gezani/Madagascar comparison signal.
- `613203`: no Tractor FC playoff opponent signal.
- `739916`: no second carrier named with USS Abraham Lincoln; current coverage only confirms the Lincoln's regional deployment.
- `795774`: no French far-right activist killing city.
- `652747`: no Navalny toxin sample report.
- `580089`: no motorcycle bomb district signal.
- `778783`: Sudan drone coverage mentioned strikes on aid/fuel convoys in North Kordofan, including Er-Rahad, but not the crowded-market strike killing at least 28; no update.
