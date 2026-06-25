# Forecast Notes - 2026-03-17

Snapshot:
- state.json absent.
- market.csv: 330 rows, 42 active, 288 resolved, no active questions missing predictions.
- Newly resolved today:
  - q405816 -> Beit Awwa. Missed; I overfit nearby West Bank places in retrieved snippets.
  - q676065 -> Bernie Sanders. Missed; high-salience national speakers can beat local-politics priors.
  - q864964 -> Ali Larijani. Missed; for Iranian retaliation/assassination prompts, include senior security officials beyond the supreme leader/IRGC commanders.

Submissions:
- q388689: moved Lin Yu-ting return top to Asian Boxing Championships after HT boxing coverage identified the Asian meet in Mongolia from Mar 28-Apr 11 as the late-March boxing event.
- q398208: increased Hong Kong as the likely first intermediary for alleged US AI-server smuggling before onward Southeast Asia routing; Singapore remains the main alternative.
- q739439: increased Ismael Zambada Sicairos. Al Jazeera explicitly names him as "El Mayito Flaco" of the La Mayiza/Los Mayos faction.
- q144493: moved eastern Pacific boat-strike transfer top to Ecuador because US/Ecuador operations are the strongest contextual signal around the linked "one survivor" strike.
- q244043: moved Jerusalem strike top to Old City after Reuters/ST and Al Jazeera described missile/interceptor fragments at Old City holy sites, with Al-Aqsa and Holy Sepulchre as variants.
- q655411: modestly reweighted toward Iran but kept US/Israel tails; Mattala evidence is mostly Iranian repatriation aircraft, not an exact combat-aircraft landing request.
- q774274: raised Nahariya after Al Jazeera reported Hezbollah rocket hit a residential building there and its daily roundup again described Hezbollah targeting Nahariya with a wounded person.

Unchanged / watch:
- q724111 remains Tehran: Al Jazeera/Tasnim checkpoint reports directly tie Basij checkpoint strikes to Tehran/District 15 and northeastern Tehran.
- q512785 remains Taiwan: Mar17 Reuters/ST says the second Taiwan US arms package is proceeding, though exact $8.4bn wording has not surfaced.
- q668257 remains risky. Ali Mohammad Naeini was alive and speaking on Mar16, but he is still the official IRGC spokesman and a plausible future fatality if the prompt resolves from a later funeral report.
- q740952 remains US Air Force because multiple reports identify a US KC-135 crash in western Iraq; despite the question background mentioning South America, retrieved evidence is strongly US.

Calibration lessons:
- Recent misses show exact official wording can be hidden in small places or agency names. Preserve a variant slot for aliases, acronyms, and sub-agencies when the source-of-truth is official text.
- When the available evidence is a near miss rather than exact resolution language, increase directionally but leave meaningful mass unallocated or on alternatives.
