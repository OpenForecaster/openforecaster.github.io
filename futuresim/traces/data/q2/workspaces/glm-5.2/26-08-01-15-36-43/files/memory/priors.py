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
"229471": {"Matthijs de Ligt": 0.18, "Lisandro Martinez": 0.16, "Harry Maguire": 0.12, "Leny Yoro": 0.10},

# [43] Who oversees US plan for Venezuela -> new elections. Special envoy. Massad Boulos? Marco Rubio? Low conf.
"64633": {"Massad Boulos": 0.18, "Marco Rubio": 0.16, "Mauricio Claver-Carone": 0.12},

# [44] Who presents Machado Madrid's gold medal. Spanish official/mayor. Madrid mayor Jose Luis Almeida. Low conf.
"839333": {"Jose Luis Martinez-Almeida": 0.22, "Isabel Diaz Ayuso": 0.16},

# [45] Country WADA targets to disrupt largest PED-production. China most likely (largest). Low-medium.
"390917": {"China": 0.40, "Russia": 0.14, "India": 0.10, "Iran": 0.06},

# [46] Spanish football club Messi acquires. He owns Inter Miami. Could buy a Spanish club. Low conf - maybe a lower-division club.
"873844": {"Real Sociedad": 0.10, "Girona": 0.10, "Espanyol": 0.08, "Elche": 0.08},

# [47] NW London neighbourhood of attempted arson on Persian-language media org. Areas: Harrow, Wembley, Edgware, Golders Green (Iranian/Jewish areas). Low conf.
"90400": {"Wembley": 0.16, "Harrow": 0.14, "Edgware": 0.12, "Golders Green": 0.10},

# [48] Who announces Australia's first overseas diesel shipment under strategic reserve. Energy minister or PM. Low conf.
"646081": {"Chris Bowen": 0.20, "Anthony Albanese": 0.18, "Madeleine King": 0.14},

# [49] UK dept Starmer says failed to inform him of security-vetting for Washington envoy. Likely Home Office or FCDO. Low conf.
"46784": {"Home Office": 0.28, "Foreign Office": 0.20, "Cabinet Office": 0.10},

# [50] Where Israel+Lebanon leaders invited by US president for first talks. US location: Washington, Camp David, or region. Low conf.
"185413": {"Washington": 0.18, "Camp David": 0.14, "Riyadh": 0.10, "Doha": 0.08},

# [51] Country Trump says he may stop in after US-Iran war ends. A visit. Could be Saudi, Israel, UAE, Qatar. Low conf.
"899138": {"Saudi Arabia": 0.18, "Israel": 0.14, "United Arab Emirates": 0.12, "Qatar": 0.10, "Turkey": 0.08},

# [52] Where investigators locate cemetery involved in discovery. Likely a specific country's mass grave. Low conf.
"715198": {"Bucha": 0.10, "Izium": 0.08},

# [53] Baby-food brand partial recall after rat poison in jars. Major brand. Low conf.
"532929": {"Gerber": 0.18, "Heinz": 0.14, "Aptamil": 0.08, "Hipp": 0.08},

# [54] Country charging Iranian national arrested at LAX. Prosecutors charge with... (country). Hmm "Which country will prosecutors charge the Iranian national arrested at LAX with" -> maybe " spying for"? The answer is a country he spied for? Low conf.
"90872": {"Iran": 0.20, "Israel": 0.10, "United States": 0.10},

# [55] Mexican state where 2 US officials killed in car crash. Border states. Low conf.
"773935": {"Tamaulipas": 0.16, "Sonora": 0.14, "Chihuahua": 0.12, "Jalisco": 0.10, "Sinaloa": 0.08},

# [56] Where Louisiana shooting (children + suspect shot by police) occurs. City in LA. Low conf.
"978710": {"New Orleans": 0.18, "Baton Rouge": 0.14, "Shreveport": 0.12, "Lafayette": 0.08},

# [57] Pacific country reverting to demand universal emissions levy (shipping). Marshall Islands, Tuvalu, Fiji. Low conf.
"443588": {"Marshall Islands": 0.20, "Tuvalu": 0.16, "Fiji": 0.12, "Vanuatu": 0.10},

# [58] Japanese prefecture offshore M7.5 quake (northern Japan Pacific). Tohoku/Hokkaido coast. Low conf.
"801535": {"Iwate": 0.18, "Miyagi": 0.16, "Hokkaido": 0.14, "Aomori": 0.12, "Fukushima": 0.08},

# [59] 2026 Laureus World Sportswoman. Top female athlete. Sydney McLaughlin, Aryna Sabalenka, Sifan Hassan. Low conf.
"802784": {"Sydney McLaughlin-Levrone": 0.18, "Aryna Sabalenka": 0.14, "Sifan Hassan": 0.10, "Aurora Magoni": 0.06},

# [60] Women's Boston Marathon 2026 winner. Top women: Hellen Obiri, Sifan Hassan, Sharon Lokedi. Low conf.
"499127": {"Hellen Obiri": 0.22, "Sifan Hassan": 0.16, "Sharon Lokedi": 0.14, "Yalemzerf Yehualaw": 0.08},

# [61] Where Ukraine strikes 2 Russian landing ships overnight Apr 20. Black Sea ports: Novorossiysk, Feodosia, Sevastopol. Low conf.
"826730": {"Novorossiysk": 0.22, "Feodosia": 0.18, "Sevastopol": 0.14, "Kerch": 0.10},

# [62] Port off which US forces seize MV Touska. Gulf/Red Sea port. Low conf.
"869693": {"Bandar Abbas": 0.14, "Hodeidah": 0.12, "Jebel Ali": 0.08, "Salalah": 0.08},

# [63] Country announcing arrests of cell linked to Velayat-e Faqih. Gulf/Western state. Low conf.
"128594": {"Bahrain": 0.16, "Saudi Arabia": 0.14, "United Arab Emirates": 0.12, "Germany": 0.08},

# [64] Federal district where Kash Patel defamation lawsuit filed. DC, SDNY, EDVA. Low conf.
"48174": {"District of Columbia": 0.30, "Southern District of New York": 0.18, "Eastern District of Virginia": 0.12},

# [65] Bayern acting coach CL semifinal first leg (Apr 29). If Kom sacked -> interim. Vincent Kompany current. If interim: maybe. Low conf.
"722040": {"Vincent Kompany": 0.22, "Dino Toppmoller": 0.14, "Marco Neppe": 0.08},

# [66] Israeli minister escorted by convoy fatally striking Palestinian teen. Multiple ministers travel with convoys. Low conf.
"793435": {"Itamar Ben-Gvir": 0.22, "Bezalel Smotrich": 0.16, "Israel Katz": 0.10, "Amichai Eliyahu": 0.08},

# [67] US state where Justin Sun files federal lawsuit. Crypto. NY, California, Florida, Delaware. Low conf.
"383542": {"New York": 0.20, "California": 0.18, "Florida": 0.12, "Delaware": 0.10},

# [68] Man City opening goal vs Burnley. Haaland, Foden, Doku. Low conf.
"432067": {"Erling Haaland": 0.34, "Phil Foden": 0.16, "Jeremy Doku": 0.12, "Omar Marmoush": 0.10},

# [69] Barcelona first goal vs Celta Vigo Apr 22. Lewandowski, Yamal, Raphinha. Low conf.
"993293": {"Robert Lewandowski": 0.26, "Lamine Yamal": 0.20, "Raphinha": 0.16, "Ferran Torres": 0.10},

# [70] City Israeli airstrike near Al-Qassam mosque kills 5. Gaza/Lebanon city. Low conf.
"651194": {"Jenin": 0.16, "Gaza City": 0.14, "Tyre": 0.10, "Tubas": 0.08},

# [71] Ukrainian C2 platform US deploys at Prince Sultan Air Base. Delta, GIS Art for War. Low conf.
"905740": {"Delta": 0.22, "Kropyva": 0.14, "GIS Art for War": 0.10},

# [72] Who resigns as Nepal home affairs minister. Current = Rabi Lamichhane? Low conf.
"518119": {"Rabi Lamichhane": 0.20, "Bal Krishna Khand": 0.12, "Hitraj Pandey": 0.08},

# [73] DeepSeek faster/lower-cost model in Apr 2026 preview. Likely named V4-lite or R2 or similar. Low conf.
"338908": {"DeepSeek-V4": 0.16, "DeepSeek-R2": 0.14, "DeepSeek-V3.5": 0.12, "DeepSeek-Lite": 0.10},

# [74] Who fast-tracks UK legislation re rising anti-Semitism. PM Starmer or Home Secretary. Low conf.
"182480": {"Keir Starmer": 0.28, "Yvette Cooper": 0.22, "Shabana Mahmood": 0.10},

# [75] Real Madrid opening goal vs Real Betis La Liga Apr 24. Mbappe, Bellingham, Vinicius. Low conf.
"407333": {"Kylian Mbappe": 0.28, "Jude Bellingham": 0.18, "Vinicius Junior": 0.16, "Rodrygo": 0.10},

# [76] Pacific climate pattern prompting WMO extreme-weather alert. El Nino/La Nina. Low conf.
"743215": {"La Nina": 0.24, "El Nino": 0.18, "El Nino-Southern Oscillation": 0.10},

# [77] EU institution tasked with blueprint for Article 42.7 response. EEAS, Council, Commission. Low conf.
"9330": {"European External Action Service": 0.24, "European Council": 0.18, "European Commission": 0.14},

# [78] Country reporting 65,399 malaria cases Jan-Apr 2026. High-burden: Nigeria, DRC, Uganda, Burkina Faso. Low conf.
"735499": {"Burkina Faso": 0.16, "Nigeria": 0.14, "Uganda": 0.12, "DRC": 0.10, "Mozambique": 0.08},

# [79] Country hosting next stop of Iran FM tour after Pakistan. Saudi, Turkey, Oman, India, China. Low conf.
"638577": {"Saudi Arabia": 0.16, "Turkey": 0.14, "Oman": 0.12, "India": 0.10, "China": 0.08},

# [80] 2026 World Cup venue with FIFA Marketplace resales capped. Specific venue. Low conf.
"2693": {"MetLife Stadium": 0.14, "AT&T Stadium": 0.12, "SoFi Stadium": 0.10, "Estadio Azteca": 0.08},

# [81] Team winning Game 4 of Min-Denver WC QF. NBA playoffs. Low conf - depends on series.
"977017": {"Minnesota Timberwolves": 0.34, "Denver Nuggets": 0.28},

# [82] Northern Malian town JNIM+FLA control after coordinated attacks. Low conf.
"465412": {"Tessalit": 0.16, "Kidal": 0.14, "Menaka": 0.12, "Gao": 0.10, "Bourem": 0.08},

# [83] Knicks 7th postseason triple-double in Game 4. Brunson. Low conf.
"996413": {"Jalen Brunson": 0.45, "OG Anunoby": 0.12, "Karl-Anthony Towns": 0.10},

# [84] US official stating criminal charges forthcoming from WHCD. DOJ official, FBI. Low conf.
"846721": {"Pam Bondi": 0.22, "Kash Patel": 0.16, "Dan Bongino": 0.10},

# [85] New party Bennett+Lapid establish. Name. Low conf.
"919933": {"Kol Yisrael": 0.08, "Israel Beitenu": 0.06, "Yesh Atid-Bennett": 0.06},

# [86] Anthony Joshua opponent Riyadh comeback Jul 25. Heavyweight. Low conf.
"212559": {"Deontay Wilder": 0.18, "Zhilei Zhang": 0.14, "Filip Hrgovic": 0.12, "Otto Wallin": 0.08},

# [87] Departure location of passenger flight crashing near Juba. South Sudan. Flights from Addis, Nairobi, Khartoum. Low conf.
"523555": {"Addis Ababa": 0.20, "Nairobi": 0.16, "Juba": 0.10, "Khartoum": 0.08},

# [88] City commuter+long-distance train collide. Could be many. Low conf.
"356699": {"Mumbai": 0.10, "Cairo": 0.08, "Jakarta": 0.08, "Istanbul": 0.06},

# [89] Who Iraq president names PM-designate. Mohammed Shia al-Sudani likely re-nominated. Low-medium.
"523557": {"Mohammed Shia al-Sudani": 0.40, "Mustafa al-Kadhimi": 0.14, "Haider al-Abadi": 0.10},

# [90] Nigerian state of late-April kidnapping of children from school. North: Kaduna, Zamfara, Katsina, Niger. Low conf.
"927519": {"Kaduna": 0.18, "Zamfara": 0.16, "Katsina": 0.12, "Niger": 0.10, "Sokoto": 0.08},

# [91] Country withdrawing from OPEC+OPEC+ by Apr 30. A member. Could be Angola (already left 2024), Nigeria, UAE, Saudi. Low conf.
"306024": {"Nigeria": 0.14, "United Arab Emirates": 0.12, "Iraq": 0.10, "Equatorial Guinea": 0.08},

# [92] Broadcaster channels FCC investigates after late-night host WHCD. Networks: CBS, NBC, ABC, CNN, Comedy Central. Low conf.
"108214": {"CBS": 0.18, "NBC": 0.14, "ABC": 0.12, "Comedy Central": 0.10},

# [93] Russian minister Putin dispatches to oversee Ukraine oil-strike response. Energy/Deputy PM. Novak (energy), Mishustin. Low conf.
"119565": {"Alexander Novak": 0.22, "Mikhail Mishustin": 0.14, "Alexander Bastrykin": 0.10},

# [94] US state where new federal case vs James Comey filed. DC, NY, Virginia, Florida. Low conf.
"890247": {"District of Columbia": 0.18, "New York": 0.16, "Virginia": 0.12, "Florida": 0.08},

# [95] US federal appeals court upholding release order for non-citizen arrested driving to work. Circuits: 9th, 4th, 2nd, 5th. Low conf.
"351470": {"Ninth Circuit": 0.18, "Fourth Circuit": 0.14, "Second Circuit": 0.12, "Fifth Circuit": 0.08},

# [96] Head of state first announcing plans to travel to LA for USA-Paraguay match. Low conf.
"276195": {"Santiago Pena": 0.14, "Milei": 0.10},

# [97] PSG right-back CL semifinal 2nd leg May 6. Hakimi, Mendes. Low conf.
"190217": {"Achraf Hakimi": 0.40, "Nuno Mendes": 0.20, "Warren Zaire-Emery": 0.06},

# [98] Country off whose coast Israel intercepts Global Sumud Flotilla. Mediterranean. Low conf.
"142723": {"Greece": 0.16, "Cyprus": 0.14, "Turkey": 0.10, "Lebanon": 0.08},

# [99] Spanish TV channel obtaining leaked recordings implicating Milei in smear campaign. Low conf.
"855937": {"Telecinco": 0.16, "La Sexta": 0.14, "Antena 3": 0.10, "TVE": 0.08},

# [100] US official publicly rejecting Iran's latest counterproposal. SecState Rubio likely. Low-medium.
"481741": {"Marco Rubio": 0.30, "Steve Witkoff": 0.16, "Pete Hegseth": 0.10, "Massad Boulos": 0.08},

# [101] Country recording 41% decline in tropical forest loss (lowest on record). Brazil (Amazon) likely. Low-medium.
"536265": {"Brazil": 0.34, "Indonesia": 0.14, "Colombia": 0.10, "Democratic Republic of the Congo": 0.06},

# [102] SCOTUS majority opinion writer, Section 2 redistricting case. Conservative justices. Low conf.
"910286": {"Brett Kavanaugh": 0.18, "John Roberts": 0.16, "Samuel Alito": 0.12, "Amy Coney Barrett": 0.10},

# [103] Former US AG appearing before House Oversight closed-door. Recent former AGs: Merrick Garland. Low-medium.
"610527": {"Merrick Garland": 0.40, "William Barr": 0.16, "Jeff Sessions": 0.08},

# [104] National team with 9 June warm-up vs Chile in Spain cancelled. A team. Low conf.
"88868": {"Morocco": 0.12, "Egypt": 0.10, "Ecuador": 0.08, "Peru": 0.08},

# [105] National delegation absent from FIFA 76th Congress (officials turned back). Low conf.
"687584": {"Russia": 0.16, "Iran": 0.12, "Syria": 0.08, "Myanmar": 0.08},

# [106] Where German authorities arrest Kazakhstan citizen spying for Russia. German cities: Berlin, Munich, Frankfurt, Cologne. Low conf.
"456839": {"Munich": 0.18, "Berlin": 0.16, "Frankfurt": 0.12, "Cologne": 0.08},

# [107] Country named defendant in coalition's challenge. Low conf.
"439122": {"United Kingdom": 0.12, "United States": 0.12, "Germany": 0.08},

# [108] Republican senator (her) sole party member supporting Apr 30 Senate measure curbing... Female GOP senators: Collins, Murkowski, Ernst, Capito. Low conf.
"673870": {"Susan Collins": 0.26, "Lisa Murkowski": 0.22, "Joni Ernst": 0.12, "Shelley Moore Capito": 0.08},

# [109] Head of state announcing int'l bodies for reparatory justice, cultural restoration. CARICOM leader. Low conf.
"434096": {"Mia Mottley": 0.20, "Philip Pierre": 0.12, "Andrew Holness": 0.10},

# [110] Who qualifies to face Keiko Fujimori in Peru 2026 runoff. Low conf.
"431712": {"Rafael Lopez Aliaga": 0.16, "Martin Vizcarra": 0.14, "Susel Paredes": 0.10, "Cesar Acuna": 0.08},
}

# Will fill MAY and JUNE in separate batches.
