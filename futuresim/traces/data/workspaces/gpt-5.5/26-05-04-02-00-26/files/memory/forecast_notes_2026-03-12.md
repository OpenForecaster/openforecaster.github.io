# Forecast Notes - 2026-03-12

Snapshot:
- `state.json` absent. `market.csv`: 330 questions, 60 active, 270 resolved, 0 active without a prediction.
- New resolutions: `169286` -> Saudi Arabia; `214539` -> Kharg island; `679215` -> USS Tripoli; `764041` -> Burj Qalaouiyah; `857856` -> North Korea.

Calibration lessons:
- Treat duplicate/sister resolved markets as strong evidence. `503104` stays Peru because sister question `632535` already resolved Peru, even though current articles discuss the separate Spain-Argentina Finalissima thread.
- Saudi base questions were underweighted. `169286` resolved Saudi Arabia after the model chased Qatar/Iraq too hard; for related launch-area/base questions, Saudi/Prince Sultan evidence deserves more weight.
- Ship movement tails were too conventional: `679215` resolved USS Tripoli, which was missing from the earlier amphibious-ship tail.

Evidence reviewed:
- `657160` launch area country: Al Jazeera/Straits Times reporting says Araghchi asked for guarantees Saudi soil would not be used; Saudi intercepted missiles aimed at Prince Sultan Air Base, and sister base question resolved Saudi Arabia. Moved Saudi Arabia to first.
- `369030` F1 Chinese GP: March 12 Reuters/Straits Times says Aston Martin still faces a very tough weekend after powertrain/battery issues, with chances of even finishing in Shanghai looking remote. Increased Aston Martin.
- `833672` Hormuz participation refusal: March 12 Reuters/Straits Times has Germany saying the Hormuz issue can only be solved diplomatically, while France/Greece are preparing or joining escort/security moves. Spain remains first because of prior anti-war/base-use statements, but Germany is now a serious second.
- `668257` IRGC spokesman funeral: March 12 Al Jazeera identifies Ali Mohammad Naeini as the IRGC spokesman currently making war claims. Moved him above Ramezan Sharif, keeping a Naini spelling variant.
- `26340` Iranian raid at plant making fresh water/electricity: Al Jazeera and Straits Times report an Iranian drone damaged Bahrain's desalination facility near Muharraq, with related Gulf water-infrastructure coverage. This fits the later "plant makes electricity and fresh water" clue better than Qatar/UAE priors.
- No direct new evidence found for `581686`, `196640`, `529060`, `293527`, `219636`, `573851`, `506444`, `724111`, `739439`, `262505`, or the IQAir country/city questions.

Submitted updates:
- `657160`: Saudi Arabia 0.38, Qatar 0.20, Iraq 0.12, United Arab Emirates 0.10, Bahrain 0.06.
- `369030`: Aston Martin 0.62, Aston Martin Aramco 0.10, Haas 0.04, Williams 0.03, Alpine 0.02.
- `833672`: Spain 0.45, Germany 0.33, Italy 0.05, Japan 0.03, Greece 0.02.
- `668257`: Ali Mohammad Naeini 0.42, Ramezan Sharif 0.22, Ali Mohammad Naini 0.12, Hossein Salami 0.03, Esmail Qaani 0.02.
- `26340`: Bahrain 0.55, United Arab Emirates 0.14, Qatar 0.10, Saudi Arabia 0.05, Kuwait 0.03.

Kept unchanged:
- `503104` remains Peru 0.90 due resolved sister-market evidence, despite visible Spain-Argentina Finalissima articles.
- `167989`, `669234`, and `274734` remain on the March 11 distributions; today's evidence did not materially change the already-high Bodo/Glimt, Be'er Ya'akov, or DEATH BETS Act views.
