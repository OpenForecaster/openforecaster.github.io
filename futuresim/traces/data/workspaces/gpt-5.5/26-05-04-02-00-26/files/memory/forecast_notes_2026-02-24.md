# Forecast Notes - 2026-02-24

Snapshot:
- `state.json` absent. `market.csv`: 330 questions, 144 active, 186 resolved, 0 active without a prediction.
- New resolutions: `392014` -> Uvira; `632535` -> Peru; `726747` -> Manchester.

Calibration lessons:
- DRC miss: Uvira/South Kivu can be the answer for mass-grave/atrocity reporting even when Goma/Bukavu dominate generic priors.
- Spain warm-up miss: Peru was not in the tail. For sister/duplicate fixture questions, use newly resolved ground truth immediately.
- Mosque city: Manchester anti-Islam protest coverage was a real clue; Manchester was in the set and resolved correctly at only 0.10.

Evidence reviewed:
- Spain friendly: sister question `632535` resolved to Peru, so active `503104` was moved strongly to Peru.
- Champions League: Reuters/Irish Times reported Newcastle beat Qarabag 9-3 aggregate and "will now play Barcelona or Chelsea" in the knockouts. Removed all other tails on `915784`.
- T20 World Cup: Al Jazeera reported England beat Pakistan by two wickets and became the first team into the semifinals; Pakistan are close to elimination. Raised England sharply for South Africa's semifinal opponent.
- Gorton/Denton: Feb 24 AFP/Straits Times cited Omnisis: Greens 20%, Reform 17%, Labour 15%, with the seat "so close between us and Reform". Moved Spencer up, Goodwin second, Stogia lower.
- Iran: fresh Reuters/Al Jazeera/Straits Times reporting kept Geneva as the Thursday talks venue; Trump warned of a "very bad day" if no deal; the US has its largest Middle East military buildup since 2003; Iran threatens US bases; Ford carrier reached Souda Bay en route.
- Maritime/Iran: Reuters/Baird reported Iran is near a deal to buy Chinese CM-302 supersonic anti-ship missiles while US naval forces gather near Iran. Raised Strait of Hormuz/Gulf of Oman for the later cargo-ship projectile question.
- No direct evidence found for: ICE/student housing university, Turkish migrant-boat/coastguard province, Barcelona midfielder hamstring injury, Swedish/Russian drone ship, or prediction-market-ban senator.

Submitted updates:
- `503104`: Peru 0.90.
- `915784`: Barcelona 0.50, Chelsea 0.50.
- `333107`: England 0.68, New Zealand 0.19, Pakistan 0.04, Sri Lanka 0.035.
- `55315`: Hannah Spencer 0.45, Matthew Goodwin 0.32, Angeliki Stogia 0.18.
- `415069`: Switzerland 0.90 for the next indirect-talks host country.
- `489902`: Geneva 0.93 for technical talks city.
- `443306`: Geneva 0.82 for final collapsed talks city.
- `58660`: Tehran 0.62 for multiple explosions during strikes.
- `739634`: Iran 0.93 for World Cup nonparticipation.
- `209948`: Iranian airspace 0.75.
- `937255`: Strait of Hormuz 0.35, Gulf of Oman 0.18.

Kept unchanged:
- `422164`, `811321`, `812182`, `661416`, `412823` because search/local checks did not produce direct identifying evidence.
- `656436` remains heavily UK due Diego Garcia/Fairford reporting; broad "Arab nations" base-access concern was not enough to displace the direct UK evidence.
