# Forecast notes - 2026-03-01

Snapshot:
- `state.json` not present. `market.csv`: 330 rows, 109 active/unresolved, 221 resolved, 0 active without a prediction.
- Local article directory contained some records with future `date_publish`; I filtered those out and primarily relied on date-capped search evidence.

New resolutions:
- `232393` resolved South Africa. Feb 28 update had South Africa top at 0.22.
- `246419` resolved Bahrain. Good Feb 28 correction from UAE-heavy to Bahrain/UAE split.
- `414228` resolved Rawalpindi. Had it at 0.16 after moving weight to Bannu/Miranshah; lesson: exact question phrasing about "besides Islamabad" still pointed to the Islamabad-Rawalpindi cluster.
- `453556` resolved Oman. Missed with Jordan/Cyprus/Turkey; Oman continues to appear as a key evacuation/mediation hub.
- `560525` resolved Kuwait. Good Feb 28 correction after Kuwait base/runway evidence.
- `971319` resolved Ras Laffan. Missed; Qatar/Ras Laffan energy infrastructure needs much more weight in remaining Gulf energy questions.
- `994042` resolved IRIB. Good, and exact acronym was enough.

Evidence and reasoning:
- Direct Al Jazeera video: plumes of smoke from Dubai's Jebel Ali Port after debris from an intercepted missile. This makes `297818` very likely Dubai.
- Al Jazeera video: Palau-flagged tanker ablaze near the Strait of Hormuz after an unidentified projectile; `937255` should be high on Strait of Hormuz.
- Al Jazeera casualty tracker: Qatar's Al Udeid base was hit by two ballistic missiles and Qatar had injuries; Qatar/Ras Laffan signal is now stronger for refinery/base-damage questions.
- Bahrain/Manama: reports of Fifth Fleet/Juffair attacks and resident evacuations make Manama live for the embassy/evacuation capital-city question, despite prior Beirut lean.
- School-strike reporting consistently names Israeli/US strikes and Iranian accusations against Israel; increase `Israeli military` and `Israel` for the related school responsibility questions.
- Iraq tracker: Jurf al-Sakher/Jurf al-Nasr strike housed Kataib Hezbollah; sources within the group confirmed casualties. Use both `Kataib Hezbollah` and `Kataeb Hezbollah` spelling variants because exact labels matter.
- UAE/Abu Dhabi reporting: Al Salam Naval Base, Zayed Port, Jebel Ali and other sites damaged. Use `UAE` spelling in country forecasts where article style is likely, but keep official-name examples in mind because historical ground truth has used both.

Submitted updates:
- `297818`: Dubai 0.90, Abu Dhabi 0.04, Fujairah 0.02, Sharjah 0.01.
- `584240`: United States 0.52, Israel 0.10, Saudi Arabia 0.06, China 0.04, Qatar 0.03.
- `759458`: Tehran 0.88, Isfahan 0.04, Minab 0.03, Shiraz 0.02, Kermanshah 0.01.
- `937255`: Strait of Hormuz 0.85, Gulf of Oman 0.06, Persian Gulf 0.03, Arabian Sea 0.02, Red Sea 0.01.
- `768526`: Israel 0.45, UAE 0.16, Saudi Arabia 0.10, Qatar 0.06, Jordan 0.03.
- `765155`: Manama 0.38, Beirut 0.24, Muscat 0.14, Jerusalem 0.06, Baghdad 0.04.
- `863162`: Qatar 0.40, Bahrain 0.18, Kuwait 0.14, Saudi Arabia 0.10, UAE 0.06.
- `887402`: Israeli military 0.65, US military 0.18, Iranian military 0.03, Saudi military 0.02.
- `893235`: Israel 0.45, United States 0.12, Iran 0.08, Saudi Arabia 0.04, Pakistan 0.02.
- `605397`: Kataib Hezbollah 0.48, Kataeb Hezbollah 0.22, Harakat Hezbollah al-Nujaba 0.06, Asaib Ahl al-Haq 0.04, Kataib Sayyid al-Shuhada 0.03.
- `169286`: Qatar 0.45, Kuwait 0.18, Bahrain 0.10, UAE 0.08, Iraq 0.04.
- `657160`: Qatar 0.34, Iraq 0.13, UAE 0.10, Saudi Arabia 0.08, Kuwait 0.06.
- `26340`: UAE 0.26, Saudi Arabia 0.12, Qatar 0.12, Bahrain 0.08, Oman 0.07.
- `560679`: ADNOC 0.42, TAQA 0.08, Borouge 0.06, Masdar 0.04, Etihad Rail 0.02.
