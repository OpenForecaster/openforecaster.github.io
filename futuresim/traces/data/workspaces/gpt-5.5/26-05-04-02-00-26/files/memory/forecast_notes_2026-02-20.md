# Forecast Notes - 2026-02-20

Snapshot:
- `state.json` not present.
- `market.csv`: 330 questions, 156 active, 174 resolved, 0 active without a current prediction.
- New resolutions: `26859` Nangarhar and Paktika; `59953` Crete.

Calibration notes:
- Afghan province question: I overweighted common prior pairs and missed Nangarhar and Paktika. For official province-list questions, include asymmetrical pairs when reporting only partially confirms the geography.
- Greek capsize question: I assigned only 0.005 to Crete and missed. Do not overconcentrate on eastern Aegean islands when the question says "Greek island" but gives no route details; Crete is a frequent migration/disaster location and needs real mass.

Main evidence and updates:
- Men's Olympic hockey: Canada beat Finland 3-2 and the United States beat Slovakia 6-2, setting up a U.S.-Canada gold-medal final. The U.S. looked stronger in the semifinal; Canada survived a comeback and Crosby's status is uncertain.
  - `221278`: United States 0.55, Canada 0.45.
- Winter Olympics medals: CBS reports Norway leads with 37 medals, while Team USA and host Italy are tied on 27 total medals. Italy needs three more to finish on 30 total medals, and still has plausible remaining medal chances.
  - `162065`: Italy 0.88, United States 0.035, Canada 0.025, Switzerland 0.02, Netherlands 0.01.
- Afghanistan condemnation: With the province question now resolved from Afghan/Pakistan air-raid reporting, the first government using "strongly condemns" is very likely Afghanistan's own government.
  - `493481`: Afghanistan 0.84, Iran 0.04, China 0.015, Russia 0.01, India 0.005.
- T20 World Cup: Al Jazeera confirmed Group 1 and that points/NRR reset. Zimbabwe's upset of Sri Lanka raises its live upset chance against West Indies, but West Indies and India remain most likely to top the table by Feb. 25.
  - `992626`: West Indies 0.33, India 0.29, South Africa 0.18, Zimbabwe 0.15.
- Iran escalation: Reuters/Straits Times report the U.S. and Iran are sliding toward conflict, with Gulf states and Israel seeing conflict as likelier than settlement. Iran says a counterproposal may be ready in days and talks could happen again in about a week. Trump set a 10-15 day deadline; IAEA's March 2 Vienna meeting creates a small Austria/Vienna venue path.
  - `739634`: Iran 0.74, Israel 0.04, Ukraine 0.015, Russia 0.01.
  - `917339`: US-Israel war on Iran 0.36, US-Iran conflict 0.18, US-Iran war 0.14, Israel-Iran war 0.12, war with Israel 0.06.
  - `656436`: United Kingdom 0.68, Pakistan 0.06, Qatar 0.05, Turkey 0.04, Oman 0.03.
  - `415069`: Switzerland 0.50, Oman 0.28, Austria 0.06, Qatar 0.03, Turkey 0.015.
  - `489902`: Geneva 0.60, Muscat 0.17, Vienna 0.07, Doha 0.025, Istanbul 0.01.
  - `443306`: Geneva 0.40, Muscat 0.22, Vienna 0.10, Doha 0.08, Istanbul 0.02.
  - `209948`: Iranian airspace 0.55, Iraqi airspace 0.07, Israeli airspace 0.06, Jordanian airspace 0.035, Gulf airspace 0.03.
  - `58660`: Tehran 0.42, Isfahan 0.19, Shiraz 0.05, Tabriz 0.04, Kermanshah 0.035.

Questions intentionally left unchanged:
- `109135`: broad search found no matching Ukrainian store/police double-explosion incident; keep prior city distribution.
- `489825`: no evidence on the Iranian Kurdish alliance acronym.
- `73075`: no new public French ambassador-summons evidence; Charles Kushner remains the best extrapolation from the Bureau of Counterterrorism resolution.
- `648994`, `654360`, `392014`, `632535`, `726747`, `812182`, `915784`: no direct resolving evidence found today.
