# Forecast notes - 2026-03-09

Snapshot:
- market.csv: 330 rows, 74 active, 256 resolved; 0 active without predictions. state.json absent.
- predictions/2026-03-09.json: 9 updates submitted.
- Mar 9 local articles include future-published entries; continue filtering date_publish > simulation date.

Resolved today:
- q399040 Iran World Cup relocation: Mexico. My Canada 0.45 / Mexico 0.40 split was close but wrong-top.
- q605397 Israeli target in Iraq: Kataib Imam Ali. I missed this by overweighting better-known Iraqi militias; include less obvious PMF faction names on future Iraq militia questions.
- q932855 China AFC WAC quarterfinal opponent: Taiwan. I had Chinese Taipei 0.32; exact-resolution naming used Taiwan.
- q935869 Liverpool/Galatasaray only goal: Mario Lemina. I included Osimhen but missed Galatasaray midfield/scorer depth.

Updates submitted:
- q211346 RCB IPL opener opponent: Punjab Kings 0.42, Chennai Super Kings 0.16, Kolkata Knight Riders 0.10, Mumbai Indians 0.07, Sunrisers Hyderabad 0.04. Defending champion vs prior finalist is the best schedule prior; no direct schedule article found by Mar 9.
- q425983 PSG substitute brace: Goncalo/Goncalo-with-cedilla Ramos combined 0.42, No player 0.16, Barcola 0.10, Doue 0.06. Question wording suggests a sub brace, but exact UEFA spelling is a risk.
- q559340 cyber persona: Handala Hack/Handala/Handla Hack combined 0.39, Predatory Sparrow 0.08, CyberAv3ngers 0.05. No direct medical-device claim found; pro-Iran hacktivist wording became more plausible than anti-Iran Predatory Sparrow.
- q807049 Real Madrid/Man City first UCL hat trick: Jude Bellingham 0.22, Vinicius variants combined 0.21, Rodrygo 0.06, Phil Foden 0.05. Dropped Mbappe because he already has a UCL hat trick.
- q828811 Beirut apartment organisation: Quds Force 0.52, Islamic Revolutionary Guard Corps 0.18, IRGC 0.10, IRGC Quds Force 0.08, Lebanon Corps 0.04. Same-day Al Jazeera says Israel targeted Quds Force commanders operating in Beirut.
- q742975 CENTCOM aircraft lost in western Iraq: LUCAS 0.70, long-name variants 0.14, one-way attack drone 0.03, MQ-9 Reaper 0.02. Evidence points to the low-cost one-way attack drone, not MQ-9.
- q857856 Mar 13 AFC WAC QF loser staying alive: North Korea 0.50, Australia 0.42, DPR Korea 0.03, China 0.01, Uzbekistan 0.01. China beat North Korea, so Australia vs North Korea is the relevant QF.
- q506444 AFC WAC semifinal winner vs South Korea: Australia 0.60, South Korea 0.28, North Korea 0.03, China 0.02, Japan 0.01. Market background says Australia and South Korea are set for the semifinal; include South Korea because criteria asks for the advancing nation.
- q833672 Hormuz military participation refusal: Spain 0.50, Germany 0.18, Italy 0.08, Japan 0.04, Greece 0.03. France/Greece are tied to a defensive escort mission, so reduce them.

Watch next:
- Exact names matter. Prefer common news names where prior resolutions used them, but include official/diacritic variants when the criteria says exact official name.
- For AFC questions, Taiwan resolved as Taiwan, not Chinese Taipei. North Korea could still be reported as DPR Korea in official AFC contexts.
- q742 should be revisited immediately if CENTCOM/DOD uses a different short designation than LUCAS.
- Search results can surface future-published articles despite date caps; ignore any result with publication date after the simulation day.
