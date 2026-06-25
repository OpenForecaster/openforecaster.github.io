# Forecast Notes - 2026-02-19

Snapshot:
- `state.json` not present.
- `market.csv`: 330 questions, 158 active, 172 resolved, 0 active without a current prediction.
- New resolutions: `325000` Hamas; `434350` Keshav Maharaj.

Calibration notes:
- I badly overweighted the generic Hezbollah prior on `325000`; the correct IDF-named group was Hamas. For Lebanon questions, do not assume "Lebanon = Hezbollah" when the target wording says command centre or named armed group; Hamas/PIJ sites can be struck in Lebanon too.
- I also overweighted current national-team captaincy for `434350`; CSA named Keshav Maharaj rather than Aiden Markram. For post-tournament bilateral tours, rotation/rest can dominate the standing captain prior.

Main evidence and updates:
- Men's Olympic hockey: the semifinal bracket is now Canada vs Finland and United States vs Slovakia. The U.S. beat Sweden in overtime; Canada and Finland also survived overtime quarterfinals. Canada captain Sidney Crosby left the quarterfinal injured, lowering Canada's edge and making the U.S. the slight gold favorite due to the Slovakia semifinal.
  - `221278`: United States 0.38, Canada 0.35, Finland 0.18, Slovakia 0.08.
- Winter Olympics medals: Fox/medal-table coverage says Italy and the U.S. are tied on 26 total medals, with Norway on 34. Italy needs four more medals to finish on the expected 30-medal national record.
  - `162065`: Italy 0.84, United States 0.04, Canada 0.03, Switzerland 0.03, Netherlands 0.02.
- T20 World Cup: Al Jazeera confirmed the Super Eight schedule and that points/NRR reset. Group 1 plays India-South Africa on Feb. 22 and Zimbabwe-West Indies on Feb. 23 before the Feb. 25 table. Zimbabwe also beat Sri Lanka, increasing its upset credibility against West Indies.
  - `992626`: West Indies 0.34, India 0.30, South Africa 0.18, Zimbabwe 0.14.
  - `333107`: England 0.34, New Zealand 0.30, Pakistan 0.18, Sri Lanka 0.08.
- Iran escalation: Trump issued a 10-day/10-15 day ultimatum to Iran; reports say U.S. forces could be ready for strikes as soon as the weekend. Poland urged citizens to leave Iran. This increases the probability that Iran becomes the country affected in World Cup participation questions and that Iranian airspace is the key aviation constraint.
  - `739634`: Iran 0.64, Israel 0.05, Ukraine 0.025, Russia 0.015.
  - `917339`: US-Israel war on Iran 0.42, Israel-Iran war 0.16, US-Iran war 0.12, war with Israel 0.08, regional conflict 0.05.
  - `209948`: Iranian airspace 0.45, Iraqi airspace 0.08, Israeli airspace 0.07, Jordanian airspace 0.04, Gulf airspace 0.03.
  - `58660`: Tehran 0.38, Isfahan 0.20, Shiraz 0.06, Tabriz 0.05, Kermanshah 0.04.
- US-Iran venue questions: current reporting still describes Geneva talks mediated by Oman and no new venue, but the last completed talks are now repeatedly framed as Geneva, and the ultimatum compresses timelines.
  - `415069`: Switzerland 0.52, Oman 0.27, Qatar 0.04, Turkey 0.02, United Arab Emirates 0.01.
  - `489902`: Geneva 0.64, Muscat 0.18, Doha 0.03, Vienna 0.02, Istanbul 0.01.
  - `443306`: Geneva 0.45, Muscat 0.22, Doha 0.09, Istanbul 0.03, Vienna 0.02.
- UK base-access dispute: Fox/Independent report that the UK is refusing permission for Trump to use Diego Garcia/RAF bases for potential Iran strikes. This makes "United Kingdom" the leading answer for the base-access trade-threat question, which was absent from the prior forecast.
  - `656436`: United Kingdom 0.55, Pakistan 0.10, Qatar 0.08, Turkey 0.06, Oman 0.04.

Questions intentionally left unchanged:
- `26859`, `493481`: no direct Afghan province/condemnation statement found today.
- `59953`: no direct Greek island capsize reporting found.
- `109135`: Ukraine reporting still does not match the two-explosions/police-response pattern.
- `489825`, `73075`: no direct acronym or French ambassador-summons evidence today.
- `812182`, `811321`, `915784`: searches did not produce direct resolving evidence.
