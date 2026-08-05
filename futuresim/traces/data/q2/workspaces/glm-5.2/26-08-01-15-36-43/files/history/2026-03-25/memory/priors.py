# Master priors: qid -> {outcome: prob}
# Calibrated best-guesses. Max 5 outcomes, probs sum <= 1.0.
# Reasoning inline. Low confidence on unknowable specifics -> modest spreads.

P = {

# ===== APRIL =====

# [0] Indonesia M7.4 Northern Molucca Sea, first fatality city. North Maluku cities.
"398343": {"Ternate": 0.22, "Tobelo": 0.18, "Sofifi": 0.15, "Tidore": 0.12},

# [1] Chelsea midfielder not playing vs Man City after apologising re future. Likely a star wanting out -> Cole Palmer? He's Chelsea's star. Or someone like Enzo Fernandez, Moises Caicedo. "apologising for comments about his future" -> Palmer? Low conf. Midfielders: Palmer, Caicedo, Enzo, Lavia.
"776644": {"Cole Palmer": 0.28, "Moises Caicedo": 0.18, "Enzo Fernandez": 0.15, "Romeo Lavia": 0.10},

# [2] US fighter shot down over southern Iran, 2 ejected crew. Two-seat => F-15E Strike Eagle or F/A-18F. F-16 single seat.
"299105": {"F-15E Strike Eagle": 0.32, "F-35 Lightning II": 0.20, "F/A-18 Super Hornet": 0.18, "F-16 Fighting Falcon": 0.10},

# [3] Club that eliminates Arsenal in 2026 FA Cup QF. FA Cup QF April. Opponents unknown. Big clubs. Man City, Liverpool, etc. Arsenal often upset in cups. Low conf.
"327626": {"Manchester City": 0.16, "Liverpool": 0.14, "Manchester United": 0.12, "Newcastle United": 0.10, "Chelsea": 0.08},

# [4] Barcelona winning goal vs Atletico Madrid Apr 4. Barca forwards: Lewandowski, Raphinha, Yamal, Ferran.
"350996": {"Robert Lewandowski": 0.26, "Raphinha": 0.20, "Lamine Yamal": 0.16, "Ferran Torres": 0.10},

# [5] Country with 281 Iranian missiles/drones before first ceasefire. Israel primary target.
"660351": {"Israel": 0.50, "United Arab Emirates": 0.16, "Saudi Arabia": 0.10, "Qatar": 0.06},

# [6] Country Iran exempts from Strait of Hormuz ship-passage restrictions. Likely a neutral/friendly state. Oman co-controls strait; China/Russia/Pakistan friendly.
"597530": {"Oman": 0.24, "China": 0.20, "Pakistan": 0.14, "Qatar": 0.10},

# [7] Country Meloni visits after Qatar, by Apr 4. Diplomatic tour region. Could be UAE, Saudi, etc. Low conf.
"77558": {"United Arab Emirates": 0.20, "Saudi Arabia": 0.18, "Egypt": 0.12, "Turkey": 0.10, "Oman": 0.08},

# [8] City hosting Ukraine+Syria presidents talks. Likely a neutral capital: Riyadh, Ankara, Doha, Abu Dhabi.
"632512": {"Riyadh": 0.22, "Ankara": 0.18, "Doha": 0.16, "Abu Dhabi": 0.12},

# [9] Org publishing survey projecting 16k jobs cut/month from AI. Think tank. McKinsey, WEF, Goldman, PwC, IMF.
"578115": {"McKinsey & Company": 0.18, "World Economic Forum": 0.16, "Goldman Sachs": 0.14, "PwC": 0.10, "IMF": 0.08},

# [10] Country setting 8pm closing for markets/malls during fuel crisis. Fuel crisis from Hormuz blockade. Could be Pakistan, Sri Lanka, Lebanon, Egypt. Low conf.
"487623": {"Pakistan": 0.16, "Sri Lanka": 0.14, "Lebanon": 0.12, "Egypt": 0.10, "Kenya": 0.08},

# [11] Taiwan boxer bronze women's 60kg Asian Boxing Elite. Specific athlete unknown. Low conf - guess prominent Taiwanese boxer. Wu Shih-yi? Chen Nien-chin (66kg). 60kg -> Wu Shih-yi (Tokyo bronze).
"225146": {"Wu Shih-yi": 0.30, "Lin Li-chen": 0.12, "Chen Nien-chin": 0.10, "Huang Hsiao-wen": 0.10},

# [12] Country publicly discussing 16 nationals killed fighting in Russia/Ukraine war. Western country whose volunteers died. Could be Nepal, India, Cuba, Serbia, Georgia. 16 nationals -> Nepal had many. Low conf.
"430728": {"Nepal": 0.20, "India": 0.16, "Cuba": 0.12, "Georgia": 0.10, "Serbia": 0.08},

# [13] Who leads Bangladesh interim cricket-board committee. BCB interim. Could be a former cricketer/admin. Low conf.
"382614": {"Nazmul Hassan": 0.16, "Faruque Ahmed": 0.14, "Aminul Islam": 0.12, "Khaled Mahmud": 0.10},

# [14] Org publishing investigation into Haftar family loans (Tripoli offensive). UN Panel of Experts, Libyan audit, watchdog. Low conf.
"146726": {"UN Panel of Experts": 0.22, "Libyan Audit Bureau": 0.16, "Human Rights Watch": 0.10, "Global Witness": 0.08},

# [15] Australian state hosting Ben Roberts-Smith initial court appearance. He's in WA/Sydney. Federal case. Likely NSW (Sydney) or Victoria. Low conf.
"68941": {"New South Wales": 0.24, "Victoria": 0.18, "Queensland": 0.14, "Western Australia": 0.12},

# [16] Japan PM meets Vietnamese counterpart in Hanoi. Vietnam PM = Pham Minh Chinh (or new). "her" => Japan's PM is a woman. Hmm, Japan PM in 2026 a woman? Sanae Takaichi became PM? If female PM of Japan, meets Vietnamese counterpart = Pham Minh Chinh. Low conf.
"881473": {"Pham Minh Chinh": 0.34, "To Lam": 0.18, "Luong Cuong": 0.12},

# [17] Who leads Iran delegation in first round US-Iran talks. FM Araghchi most likely.
"583783": {"Abbas Araghchi": 0.45, "Ali Bagheri Kani": 0.18, "Majid Takht Ravanchi": 0.10},

# [18] Egyptian Pro League suspension for striking referee after Al-Ahly match. Player. Low conf - Al-Ahly player. Likely a fiery player. Unknown. Guess.
"724016": {"Mohamed Sherif": 0.16, "Hussein El Shahat": 0.14, "Emam Ashour": 0.12, "Afsha": 0.10},

# [19] Org releasing regional survey of displaced households in Sudan. IOM, UNHCR, OCHA, WHO. Low conf.
"199254": {"IOM": 0.22, "UNHCR": 0.18, "OCHA": 0.14, "REACH": 0.10},

# [20] Southern Lebanese town Israeli forces completely surround. Current focus = Khiam. Strong candidate.
"829924": {"Khiam": 0.34, "Bint Jbeil": 0.16, "Nabatieh": 0.12, "Marjayoun": 0.08},

# [21] US federal agency investigating NFL anticompetitive conduct. FTC or DOJ Antitrust.
"901922": {"Federal Trade Commission": 0.40, "Department of Justice": 0.30, "Federal Communications Commission": 0.06},

# [22] Runner-up in Djibouti Apr 10 presidential election. Incumbent Guelleh wins; runner-up = opposition. Low conf.
"85884": {"Omar Elmi": 0.14, "Aden Mohamed Abdou": 0.12, "Kadra Igal Hassan": 0.10, "Mohamed Daoud": 0.08},

# [23] Who instructs removal of Spain's reps from Civil-Military Coordination Centre. A commander/official. Could be UN, a general. Low conf.
"676856": {"Antonio Guterres": 0.12, "Antonio Laguens": 0.08, "Jean-Pierre Lacroix": 0.10},

# [24] Union Berlin new head coach. Bundesliga. Candidates: former coaches. Low conf.
"335788": {"Bo Svensson": 0.18, "Sandro Wagner": 0.14, "Thomas Letsch": 0.10, "Marco Gorter": 0.06},

# [25] Rebel group Nigerian forces pursuing in Jilli-axis airstrike. Bandits/Boko Haram/ISWAP. Jilli axis = Zamfara bandits. Low conf.
"58896": {"Lakurawa": 0.20, "ISWAP": 0.16, "Boko Haram": 0.12, "Ansaru": 0.10},

# [26] 2026 Masters winner. Top golfers.
"893744": {"Scottie Scheffler": 0.22, "Rory McIlroy": 0.14, "Xander Schauffele": 0.10, "Jon Rahm": 0.08, "Collin Morikawa": 0.07},

# [27] Hungary lawmakers elect PM by May 13. Orban's Fidesz dominates -> Viktor Orban. But question implies change? "elect as prime minister" - Orban re-elected. Strong.
"368203": {"Viktor Orban": 0.55, "Peter Magyar": 0.18},

# [28] Country signing major defence cooperation with US by Apr 15. Could be Saudi, UAE, Qatar, Philippines, Poland. Low conf.
"591655": {"Saudi Arabia": 0.16, "United Arab Emirates": 0.14, "Poland": 0.12, "Qatar": 0.10, "Philippines": 0.08},

# [29] Winning goal Tottenham vs Sunderland PL Apr 12. Spurs forwards: Solanke, Son, Maddison. Low conf.
"639098": {"Dominic Solanke": 0.20, "Son Heung-min": 0.18, "James Maddison": 0.14, "Brennan Johnson": 0.10},

# [30] Whose posts Brazil Federal Police investigate for defamation of incumbent (Lula). Likely a Bolsonaro (Jair or Eduardo) or supporter. Low conf.
"127767": {"Jair Bolsonaro": 0.22, "Eduardo Bolsonaro": 0.18, "Carlos Bolsonaro": 0.12, "Silveira": 0.08},

# [31] Head of Australian Defence Force by July 2026. Current CDF = Angus Campbell. Successor? Low conf.
"356778": {"Angus Campbell": 0.18, "Simon Stuart": 0.16, "Greg Bilton": 0.12, "Justin Jones": 0.10},

# [32] West Bank refugee camp women enter for inspections/strip searches. IDF operations. Camps: Jenin, Tulkarm, Nur Shams, Balata. Low conf.
"702685": {"Jenin": 0.20, "Tulkarm": 0.16, "Nur Shams": 0.12, "Balata": 0.10},

# [33] Ghana next men's national team coach. Candidates: various. Low conf.
"824613": {"Mas-Ud Didi Dramani": 0.14, "Bjorn Fredrik": 0.08, "John Paintsil": 0.08},

# [34] Agrarian-reform law Bolivia repeals. Law 1777? Law of Agrarian Reform (Ley de Reforma Agraria 1953 / INRA). Low conf.
"287813": {"Law 1777": 0.18, "INRA Law": 0.16, "Law 3545": 0.12},

# [35] Org donating generators/motor pumps to Iran relief. UAE Red Crescent, IRC, WHO. Low conf.
"213933": {"UAE Red Crescent": 0.18, "ICRC": 0.16, "WHO": 0.12, "OCHA": 0.08},

# [36] Who challenges Gukesh in next classical World Chess Championship match. Candidates winner 2026. Carlsen? Caruana? Nepomniachtchi? Hikaru? Low conf.
"284263": {"Magnus Carlsen": 0.24, "Fabiano Caruana": 0.18, "Hikaru Nakamura": 0.16, "Ian Nepomniachtchi": 0.12},

# [37] US Middle East envoy praising Lebanese banker. Special envoy. Could be Morgan Ortagus, Steve Witkoff. Low conf.
"390748": {"Morgan Ortagus": 0.18, "Steve Witkoff": 0.14, "Massad Boulos": 0.12},

# [38] Where two-missile Israeli drone strike hits group Apr 14. Location in Lebanon/Gaza. Low conf.
"655455": {"Beirut": 0.16, "Tyre": 0.14, "Sidon": 0.10, "Baflaya": 0.08},

# [39] Country Pakistan PM visits last on 3-country diplomatic tour for US-Iran mediation. Tour likely Saudi, Iran, Turkey/UAE. Low conf.
"793188": {"Turkey": 0.16, "Saudi Arabia": 0.14, "Iran": 0.12, "United Arab Emirates": 0.10},

# [40] Newspaper publishing Trump interview criticizing Meloni. NYT, WSJ, WashPost, Fox. Low conf.
"601987": {"The New York Times": 0.18, "The Wall Street Journal": 0.14, "Washington Post": 0.12, "New York Post": 0.08},

# [41] South Africa's next ambassador to US. A prominent figure. Low conf.
"679514": {"Tony Leon": 0.12, "Mmusi Maimane": 0.10, "Roelf Meyer": 0.08, "Ebrahim Rasool": 0.08},

# [42] Man United centre-back unavailable Apr 18 after suspension extension (impeding?). Likely a CB: De Ligt, Martinez, Maguire, Yoro. Low conf.
"229471": {"Matthijs de Ligt": 0.18, "Lisandro Martinez": 0.16, "Harry Maguire
[...truncated]