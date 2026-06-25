# Day 1 (2025-12-24) first-cut predictions for all 330 questions.
# Format: qid -> dict(outcome -> prob). Probs sum to <= 1.0. Real answers only.
P = {
 # ===== ENTERTAINMENT =====
 "946810": {"Kendrick Lamar": 0.46, "Lady Gaga": 0.27, "Sabrina Carpenter": 0.14, "Bad Bunny": 0.07, "Tyler, the Creator": 0.06},  # Grammy AOTY
 "876347": {"Wicked: For Good": 0.16, "The Morning": 0.10, "Avatar: Fire and Ash": 0.10, "Bugonia": 0.08, "After the Hunt": 0.07},  # 98th Oscar most noms (2025 films) - low conf
 "886103": {"Jon M. Chu": 0.18, "Bong Joon Ho": 0.12, "Yorgos Lanthimos": 0.10, "James Cameron": 0.10, "Paul Thomas Anderson": 0.08},  # director of 16-nom film - low conf
 # ===== CHELSEA / FOOTBALL EUROPE =====
 "165622": {"Enzo Maresca": 0.22, "Graham Potter": 0.18, "Roberto Mancini": 0.14, "Thomas Frank": 0.12, "Kieran McKenna": 0.10},  # Chelsea next perm coach
 "474377": {"Ruben Amorim": 0.46, "Michael Carrick": 0.13, "Ruud van Nistelrooy": 0.11, "Gareth Southgate": 0.08, "Ralf Rangnick": 0.06},  # Man Utd derby
 "406433": {"Liverpool": 0.24, "Real Madrid": 0.18, "Manchester City": 0.13, "Chelsea": 0.10, "Tottenham Hotspur": 0.08},  # Marc Guehi club
 "348570": {"Manchester City": 0.40, "Arsenal": 0.18, "Liverpool": 0.14, "Chelsea": 0.10, "Manchester United": 0.08},  # Deloitte Money League top English
 "98159": {"Athletic Bilbao": 0.16, "Real Sociedad": 0.14, "Sevilla": 0.13, "Girona": 0.12, "Osasuna": 0.10},  # Atletico Copa QF opp
 "85609": {"Celtic": 0.16, "Sporting CP": 0.13, "Club Brugge": 0.12, "Brest": 0.11, "PSV": 0.10},  # Real Madrid UCL playoff opp
 "55999": {"Brest": 0.16, "Celtic": 0.13, "Club Brugge": 0.12, "Sporting CP": 0.11, "Feyenoord": 0.10},  # Benfica UCL playoff opp
 "35131": {"PSV": 0.15, "Feyenoord": 0.13, "Celtic": 0.12, "Club Brugge": 0.11, "Sporting CP": 0.10},  # eliminate Juventus
 "261538": {"Glasgow": 0.40, "Lisbon": 0.15, "Rotterdam": 0.12, "Eindhoven": 0.10, "Brest": 0.08},  # Newcastle UCL 1st leg city
 "220862": {"Arsenal": 0.30, "Liverpool": 0.20, "Tottenham Hotspur": 0.12, "Newcastle United": 0.10, "Aston Villa": 0.08},  # Man City League Cup final opp
 "903473": {"Antonio Silva": 0.18, "Nicolas Otamendi": 0.14, "Tomas Araujo": 0.12, "Orkun Kokcu": 0.10},  # Benfica player Vinicius racist remark
 "167989": {"Real Madrid": 0.30, "Bayern Munich": 0.16, "Inter Milan": 0.12, "Atletico Madrid": 0.10, "Borussia Dortmund": 0.08},  # Arsenal UCL QF opp
 "16281": {"Arsenal": 0.16, "Liverpool": 0.13, "Chelsea": 0.11, "Brighton": 0.10, "Tottenham": 0.08},  # club hands Carrick first defeat
 # ===== TENNIS =====
 "891998": {"Elena Rybakina": 0.25, "Coco Gauff": 0.16, "Iga Swiatek": 0.13, "Qinwen Zheng": 0.10, "Mirra Andreeva": 0.08},  # Sabalenka Brisbane final
 "793465": {"Elena Rybakina": 0.12, "Coco Gauff": 0.10, "Iga Swiatek": 0.09, "Ons Jabeur": 0.08, "Qinwen Zheng": 0.07},  # beats Venus Williams AO R1
 "2176": {"Jannik Sinner": 0.10, "Daniil Medvedev": 0.09, "Taylor Fritz": 0.08, "Alex de Minaur": 0.07, "Hubert Hurkacz": 0.06},  # Alcaraz AO R2 (he's top seed; R2 opp is low-ranked)
 "980781": {"Novak Djokovic": 0.12, "Daniil Medvedev": 0.10, "Taylor Fritz": 0.08, "Alex de Minaur": 0.07, "Tommy Paul": 0.06},  # Sinner AO R2
 "922844": {"Iga Swiatek": 0.12, "Coco Gauff": 0.10, "Elena Rybakina": 0.09, "Aryna Sabalenka": 0.07, "Jessica Pegula": 0.06},  # Sonmez AO R3
 "464874": {"Coco Gauff": 0.11, "Iga Swiatek": 0.10, "Elena Rybakina": 0.09, "Mirra Andreeva": 0.07, "Beatriz Haddad Maia": 0.06},  # Sabalenka AO R3
 "679570": {"Coco Gauff": 0.12, "Iga Swiatek": 0.10, "Elena Rybakina": 0.09, "Beatriz Haddad Maia": 0.07, "Karolina Muchova": 0.06},  # Osaka AO R3
 "400561": {"Mirra Andreeva": 0.11, "Emma Raducanu": 0.09, "Diana Shnaider": 0.08, "Linda Noskova": 0.07, "Marta Kostyuk": 0.06},  # AO debutante R16 vs Sabalenka
 "789844": {"Novak Djokovic": 0.13, "Daniil Medvedev": 0.11, "Taylor Fritz": 0.09, "Alex de Minaur": 0.08, "Holger Rune": 0.07},  # Alcaraz AO R16
 "286957": {"Aryna Sabalenka": 0.20, "Iga Swiatek": 0.15, "Coco Gauff": 0.12, "Elena Rybakina": 0.10, "Qinwen Zheng": 0.07},  # eliminates Madison Keys
 "287417": {"Coco Gauff": 0.14, "Iga Swiatek": 0.12, "Elena Rybakina": 0.10, "Qinwen Zheng": 0.09, "Mirra Andreeva": 0.07},  # Sabalenka AO QF
 "951896": {"Jannik Sinner": 0.30, "Carlos Alcaraz": 0.26, "Novak Djokovic": 0.16, "Daniil Medvedev": 0.10, "Taylor Fritz": 0.06},  # AO men's champion
 # ===== CRICKET =====
 "468637": {"United Arab Emirates": 0.45, "Sri Lanka": 0.20, "Oman": 0.13, "Bangladesh": 0.07},  # Bangladesh move T20WC to
 "110472": {"Ireland": 0.18, "Zimbabwe": 0.15, "West Indies": 0.12, "Afghanistan": 0.10, "Scotland": 0.08},  # replace Bangladesh T20WC
 "316535": {"Mitchell Marsh": 0.15, "Cameron Green": 0.13, "Nathan Ellis": 0.11, "Spencer Johnson": 0.09, "Riley Meredith": 0.07},  # Cummins replacement
 "190197": {"Ireland": 0.18, "West Indies": 0.15, "Bangladesh": 0.12, "Zimbabwe": 0.10, "Afghanistan": 0.08},  # Pakistan beat for Super Eight
 "307616": {"India": 0.24, "Australia": 0.18, "England": 0.13, "South Africa": 0.11, "New Zealand": 0.08},  # Pakistan Super Eight opener
 "454482": {"England": 0.20, "West Indies": 0.16, "India": 0.13, "Australia": 0.11, "Pakistan": 0.09},  # former champ fails Super Eight
 "992626": {"India": 0.26, "Australia": 0.18, "South Africa": 0.13, "England": 0.11, "Pakistan": 0.08},  # Group 1 top Super Eights
 "333107": {"India": 0.24, "Australia": 0.18, "England": 0.13, "New Zealand": 0.10, "West Indies": 0.08},  # SA T20WC semifinal opp
 "179817": {"Waqar Younis": 0.18, "Mike Hesson": 0.14, "Stephen Fleming": 0.11, "Tom Moody": 0.09, "Chandika Hathurusingha": 0.07},  # Sri Lanka coach
 "211346": {"Mumbai Indians": 0.20, "Chennai Super Kings": 0.16, "Royal Challengers Bengaluru": 0.12, "Kolkata Knight Riders": 0.10, "Delhi Capitals": 0.08},  # RCB IPL opener host
 "698278": {"Royal Challengers Bengaluru": 0.18, "Delhi Capitals": 0.14, "Lucknow Super Giants": 0.11, "Rajasthan Royals": 0.09, "Punjab Kings": 0.08},  # IPL franchise Blitzer buys
 # ===== AFCON =====
 "343689": {"Hakim Ziyech": 0.18, "Youssef En-Nesyri": 0.15, "Sofyan Amrabat": 0.12, "Nayef Aguerd": 0.12, "Azzedine Ounahi": 0.10},  # Morocco calf injury
 "703511": {"Senegal": 0.22, "Morocco": 0.18, "Nigeria": 0.12, "Egypt": 0.10, "Algeria": 0.09},  # knock DR Congo out
 "459037": {"Senegal": 0.22, "Algeria": 0.18, "Egypt": 0.15, "Nigeria": 0.12, "Ivory Coast": 0.10},  # Morocco semifinal opp
 "799398": {"Achraf Hakimi": 0.22, "Hakim Ziyech": 0.18, "Youssef En-Nesyri": 0.14, "Brahim Diaz": 0.10, "Sofiane Boufal": 0.08},  # Morocco missed penalty in final
 "573851": {"Senegal": 0.30, "Morocco": 0.25, "Nigeria": 0.12, "Egypt": 0.08, "Algeria": 0.07},  # appeals AFCON title ruling to CAS
 "932855": {"Australia": 0.20, "South Korea": 0.16, "Japan": 0.13, "North Korea": 0.10, "Vietnam": 0.08},  # China AFC Women's Asian Cup QF
 "506444": {"Australia": 0.20, "Japan": 0.16, "North Korea": 0.12, "South Korea": 0.10, "China": 0.08},  # beat South Korea to reach AFC Women's final
 "857856": {"Australia": 0.20, "Japan": 0.15, "South Korea": 0.12, "North Korea": 0.10, "China": 0.08},  # Women's WC qualifying playoff
 # ===== UKRAINE / RUSSIA =====
 "227432": {"Rustem Umerov": 0.28, "Oleksandr Syrskyi": 0.14, "Mykhailo Drapaty": 0.11, "Oleksandr Kamyshin": 0.10, "Pavlo Rybkin": 0.08},  # defence minister nominee
 "709715": {"Tymofiy Mylovanov": 0.20, "Oleksandr Kamyshin": 0.17, "Rostyslav Shurma": 0.12, "Yulia Svyrydenko": 0.10, "Vasyl Khmelnytsky": 0.07},  # econ dev adviser
 "117844": {"Petro Poroshenko": 0.30, "Yulia Tymoshenko": 0.18, "Dmytro Razumkov": 0.12, "Yurii Boyko": 0.09, "Vadym Rabinovich": 0.06},  # opposition leader charged
 "836984": {"Kyiv": 0.20, "Dnipro": 0.18, "Odesa": 0.12, "Kharkiv": 0.10, "Zaporizhzhia": 0.08},  # Oreshnik city
 "655453": {"Turkey": 0.24, "Saudi Arabia": 0.18, "Qatar": 0.13, "United Arab Emirates": 0.10, "Oman": 0.08},  # mediator 3-way US/Ukraine/Russia
 "48762": {"Istanbul": 0.26, "Riyadh": 0.18, "Geneva": 0.12, "Doha": 0.10, "Minsk": 0.07},  # city 3-way talks Jan 23-24
 "575662": {"Istanbul": 0.28, "Riyadh": 0.18, "Geneva": 0.12, "Doha": 0.10, "Jeddah": 0.08},  # 2nd round RU-UA talks Feb 4
 "391811": {"Pavlohrad": 0.15, "Kryvyi Rih": 0.12, "Nikopol": 0.11, "Kamianske": 0.09, "Dnipro": 0.08},  # Dnipropetrovsk drone on miners' bus
 "109135": {"Kharkiv": 0.16, "Kryvyi Rih": 0.12, "Zaporizhzhia": 0.11, "Odesa": 0.10, "Dnipro": 0.08},  # deadly attack 100+ shelters
 "336425": {"Donetsk": 0.18, "Mariupol": 0.12, "Makiivka": 0.10, "Horlivka": 0.09, "Yenakiieve": 0.07},  # eastern Ukrainian market shelling
 "768526": {"Saudi Arabia": 0.18, "Turkey": 0.14, "Iran": 0.12, "North Korea": 0.10, "China": 0.08},  # Zelensky says requested Ukrainian help vs drones
 "309487": {"Kherson": 0.16, "Zaporizhzhia": 0.13, "Donetsk": 0.11, "Luhansk": 0.09, "Kharkiv": 0.08},  # Ukrainian region retaken
 "529060": {"Oreshnik": 0.15, "Kinzhal": 0.13, "Iskander": 0.11, "Zircon": 0.09, "Kh-101": 0.07},  # missile type Ukraine destroyed
 "58660": {"Tehran": 0.25, "Baghdad": 0.16, "Damascus": 0.12, "Beirut": 0.10, "Dubai": 0.07},  # multiple explosions during strikes
 # ===== SYRIA / YEMEN / SOMALIA =====
 "369962": {"Syrian Democratic Forces": 0.26, "Kurdish YPG": 0.16, "ISIS": 0.13, "PKK": 0.10, "Syrian National Army": 0.08},  # Syria op target Aleppo
 "756891": {"Syrian Democratic Forces": 0.22, "Syrian National Army": 0.16, "PKK": 0.12, "ISIS": 0.10, "Maghawir al-Thawra": 0.07},  # armed group fighters east Aleppo
 "138247": {"Syrian Democratic Forces": 0.24, "People's Protection Units": 0.14, "PKK": 0.12, "Syrian National Army": 0.10, "ISIS": 0.07},  # org fighters Maskana/Deir Hafer
 "904367": {"Manbij": 0.18, "Raqqa": 0.14, "Deir ez-Zor": 0.12, "Tabqa": 0.10, "Hasakah": 0.08},  # Syrian army complete control NE city
 "974205": {"Raqqa": 0.18, "Manbij": 0.15, "Deir ez-Zor": 0.12, "Hasakah": 0.10, "Qamishli": 0.08},  # city SDF bracing assault
 "551676": {"Syrian Democratic Forces": 0.28, "Syrian army": 0.18, "United States": 0.12, "Russian forces": 0.08, "Iranian forces": 0.07},  # control al-Shaddadi base
 "797906": {"Presidential Protection Forces": 0.16, "National Army": 0.14, "Republican Guard": 0.12, "Joint Forces Command": 0.11, "National Shield Forces": 0.08},  # Yemen al-Alimi military body
 "783773": {"Ethiopia": 0.35, "Kenya": 0.15, "United Arab Emirates": 0.12, "Egypt": 0.08, "Eritrea": 0.07},  # Somalia separatist support
 "666021": {"Ethiopia": 0.45, "Kenya": 0.12, "United Arab Emirates": 0.10, "Egypt": 0.07, "Turkey": 0.06},  # Somalia severs agreements
 # ===== GREENLAND / NATO / ARCTIC =====
 "630728": {"Marco Rubio": 0.42, "Pete Hegseth": 0.14, "JD Vance": 0.12, "Keith Kellogg": 0.10, "Mike Waltz": 0.08},  # DK/Greenland request meeting
 "269293": {"White House": 0.36, "State Department": 0.22, "Pentagon": 0.12, "Capitol Hill": 0.08, "Blair House": 0.06},  # venue DK/Greenland US talks
 "85534": {"Northern Falcon": 0.16, "Viking Shield": 0.15, "Arctic Guardian": 0.13, "Nordic Sentinel": 0.12, "Baltic Sentry": 0.08},  # NATO Arctic mission name
 "822586": {"Tokyo": 0.22, "New Delhi": 0.18, "Singapore": 0.12, "Seoul": 0.12, "Hanoi": 0.08},  # Carney after Beijing
 "621718": {"Frederik": 0.20, "Mette Frederiksen": 0.18, "Jens-Frederik Nielsen": 0.12, "Mute Egede": 0.10, "Donald Trump": 0.08},  # Trump says reached Greenland deal with
 # ===== GAZA / PALESTINE / ISRAEL =====
 "71": {"Mohammad Mustafa": 0.20, "Salam Fayyad": 0.15, "Mohammed Dahlan": 0.12, "Hussein al-Sheikh": 0.10, "Nabil Shaath": 0.08},  # lead Palestinian tech committee Gaza
 "806810": {"Gaza Authority": 0.18, "Administrative Committee for Gaza": 0.15, "Palestinian Authority": 0.12, "Gaza Reconstruction Authority": 0.10, "Gaza Administration": 0.08},  # Palestinian body name
 "423343": {"Jenin": 0.22, "Tulkarm": 0.15, "Nablus": 0.12, "Tubas": 0.10, "Hebron": 0.08},  # Israeli raid wedding West Bank
 "789988": {"Giorgia Meloni": 0.12, "Emmanuel Macron": 0.11, "Narendra Modi": 0.10, "Olaf Scholz": 0.08, "Keir Starmer": 0.07},  # Netanyahu says visiting PM
 "988168": {"Instagram": 0.30, "TikTok": 0.20, "X": 0.15, "Facebook": 0.10, "YouTube": 0.07},  # platform bans Bisan Owda
 "320820": {"Egypt": 0.20, "Jordan": 0.18, "Qatar": 0.12, "United Arab Emirates": 0.10, "Turkey": 0.08},  # 24 children evacuated Gaza to
 "80868": {"Jenin": 0.16, "Tubas": 0.13, "Tulkarm": 0.11, "Nablus": 0.09, "Qalqilya": 0.08},  # village overnight Israeli West Bank
 "405816": {"Tubas": 0.14, "Jenin": 0.12, "Tammun": 0.10, "Tulkarm": 0.09, "Ya'bad": 0.07},  # West Bank town, Israel killed 2 Palestinians
 # ===== IRAN NUCLEAR / US-IRAN WAR (March cluster) =====
 "433526": {"Natanz": 0.30, "Fordow": 0.22, "Parchin": 0.18, "Isfahan": 0.12, "Khondab": 0.08},  # Iranian complex shielded facility
 "69214": {"Sistan-Baluchestan": 0.25, "Tehran": 0.18, "Kurdistan": 0.15, "Khuzestan": 0.10, "West Azerbaijan": 0.08},  # province 30 police lost
 "579252": {"Karaj": 0.15, "Tehran": 0.13, "Isfahan": 0.11, "Shiraz": 0.09, "Mashhad": 0.08},  # city wrestler sentenced
 "198725": {"Tehran": 0.20, "Zanjan": 0.12, "Ahvaz": 0.11, "Tabriz": 0.10, "Kerman": 0.08},  # city Narges Mohammadi exiled to
 "935533": {"Syria": 0.18, "Lebanon": 0.15, "Israel": 0.13, "Ukraine": 0.12, "Iran": 0.09},  # free Starlink country
 "45659": {"China": 0.24, "Italy": 0.15, "France": 0.10, "Brazil": 0.10, "Australia": 0.08},  # first to ban Grok
 "172391": {"Nowruz": 0.18, "Eid al-Fitr": 0.15, "Christmas": 0.12, "Eid al-Adha": 0.10, "Orthodox Christmas": 0.08},  # Syria national holiday
 "579233": {"Kurdish": 0.20, "Syriac": 0.16, "Arabic": 0.14, "Turkmen": 0.10, "Armenian": 0.08},  # Syria national language
 "489825": {"KOMALA": 0.14, "KDPI": 0.12, "PJAK": 0.10, "Kurdistan": 0.09, "KRF": 0.07},  # 6 Iranian Kurdish groups alliance acronym
 "172888": {"Mojtaba Khamenei": 0.18, "Ali Khamenei": 0.14, "Mohammad Ghalibaf": 0.11, "Ebrahim Raisi": 0.09, "Hossein Salami": 0.08},  # 3rd member Iran governing council
 "635419": {"Ahmad Jannati": 0.12, "Mohammad Yazdi": 0.10, "Mohammad Javad Larijani": 0.09, "Ali Movahedi-Kermani": 0.08, "Gholamhossein Mohseni Ejei": 0.07},  # Guardian Council member interim council
 "468437": {"Niloofar Ardalan": 0.12, "Katayoun Khosrowyar": 0.10, "Fereshteh Karimi": 0.08, "Dalila Ghaemi": 0.07, "Sahar Zanetti": 0.06},  # Iran women's football captain
 "917339": {"Gaza war": 0.25, "Yemen war": 0.18, "Syrian civil war": 0.14, "Israel-Iran conflict": 0.12, "Ukraine war": 0.08},  # conflict Iran cites for WC venue change
 "434350": {"Heinrich Klaasen": 0.14, "Aiden Markram": 0.12, "Rilee Rossouw": 0.10, "Reeza Hendricks": 0.09, "David Miller": 0.08},  # SA T20 captain vs NZ
 "883856": {"Andrey Averyanov": 0.12, "Igor Kostyukov": 0.10, "Sergei Surovikin": 0.09, "Yevgeny Nikiforov": 0.08, "Alexander Dvornikov": 0.07},  # senior officer shot Moscow
 "652747": {"Novichok": 0.30, "Radioactive polonium-210": 0.15, "Soman": 0.12, "VX": 0.10, "Sarin": 0.08},  # toxin in Navalny samples
 "815035": {"Isfahan": 0.18, "Tehran": 0.15, "Tabriz": 0.11, "Shiraz": 0.10, "Kermanshah": 0.08},  # Iranian city Israeli strike girls school
 "79608": {"Tehran": 0.18, "Isfahan": 0.14, "Tabriz": 0.11, "Ahvaz": 0.10, "Shiraz": 0.08},  # Iranian city 6 killed air raids
 "876124": {"Tehran": 0.16, "Isfahan": 0.13, "Bushehr": 0.11, "Natanz": 0.10, "Bandar Abbas": 0.08},  # town Russian media missile strike site
 "434027": {"Isfahan": 0.16, "Tehran": 0.13, "Tabriz": 0.10, "Natanz": 0.09, "Shiraz": 0.08},  # Iranian city missile strike site March
 "759458": {"Isfahan": 0.16, "Tehran": 0.13, "Tabriz": 0.10, "Shiraz": 0.09, "Ahvaz": 0.08},  # Iranian city hospital
 "943634": {"Shahriar": 0.14, "Eslamshahr": 0.12, "Robat Karim": 0.10, "Pardis": 0.08, "Malard": 0.07},  # town SW Tehran two schools
 "599755": {"Tehran Heart Center": 0.12, "Milad Hospital": 0.11, "Golestan Hospital": 0.09, "Imam Khomeini Hospital": 0.08, "Shariati Hospital": 0.07},  # Tehran hospital hit
 "971319": {"Tel Aviv": 0.15, "Haifa": 0.13, "Jerusalem": 0.11, "Ashdod": 0.09, "Beersheba": 0.08},  # extensive damage Iranian missiles
 "669234": {"Tel Aviv": 0.18, "Jerusalem": 0.13, "Haifa": 0.11, "Ramat Gan": 0.09, "Beersheba": 0.08},  # central Israel 2 killed
 "13213": {"Tel Aviv": 0.16, "Jerusalem": 0.13, "Haifa": 0.11, "Beersheba": 0.09, "Ashkelon": 0.08},  # Israeli town 9 deaths Iranian missile
 "724111": {"Zahedan": 0.14, "Khash": 0.12, "Iranshahr": 0.10, "Chabahar": 0.09, "Saravan": 0.08},  # checkpoint attack killed 13 IRGC
 "943026": {"Iran": 0.16, "Iraq": 0.13, "Syria": 0.11, "Yemen": 0.09, "Lebanon": 0.08},  # city cross-border air strike civilian center
 "864964": {"Ismail Haniyeh": 0.14, "Hassan Nasrallah": 0.12, "Qasem Soleimani": 0.10, "Mohammad Deif": 0.09, "Yahya Sinwar": 0.08},  # whose killing Iran avenging
 "58520": {"Israel Katz": 0.14, "Benjamin Netanyahu": 0.12, "Yoav Gallant": 0.10, "Herzi Halevi": 0.09, "Ron Dermer": 0.08},  # Israeli official says senior Iranian killed
 "768218": {"Ismail Haniyeh": 0.14, "Hassan Nasrallah": 0.12, "Mohammad Deif": 0.10, "Yahya Sinwar": 0.09, "Qasem Soleimani": 0.08},  # whose killing Hezbollah avenging
 "659262": {"Sakhnin": 0.14, "Umm al-Fahm": 0.12, "Nazareth": 0.10, "Tayibe": 0.09, "Baqa al-Gharbiyye": 0.08},  # Israeli Premier League footballer killed
 "668257": {"Hossein Salami": 0.14, "Mohammad Bagheri": 0.12, "Esmail Qaani": 0.10, "Gholamali Rashid": 0.09, "Ali Fadavi": 0.08},  # IRGC spokesman funeral
 "443306": {"Doha": 0.20, "Muscat": 0.16, "Riyadh": 0.12, "Geneva": 0.10, "Baghdad": 0.08},  # where final talks collapsed before strikes
 "131819": {"Aleppo": 0.14, "Damascus": 0.12, "Baghdad": 0.10, "Erbil": 0.09, "Beirut": 0.08},  # deadly cross-border air strike civilian treatment
 "214539": {"Abu Musa": 0.16, "Sirri": 0.13, "Larak": 0.10, "Hengam": 0.09, "Qeshm": 0.08},  # Iranian island US bombed
 "415069": {"Oman": 0.22, "Qatar": 0.16, "Iraq": 0.12, "Saudi Arabia": 0.10, "Bahrain": 0.08},  # host next US-Iran indirect talks March 2
 "489902": {"Muscat": 0.20, "Doha": 0.16, "Geneva": 0.12, "Baghdad": 0.10, "Rome": 0.08},  # city Iran-US technical talks early March
 "120805": {"Oman": 0.22, "Qatar": 0.16, "Saudi Arabia": 0.12, "Iraq": 0.10, "United Arab Emirates": 0.08},  # Trump 15-pt plan intermediaries to Iran
 "297818": {"Strait of Hormuz": 0.25, "Red Sea": 0.15, "Gulf of Aden": 0.12, "Bab el-Mandeb": 0.10, "Suez Canal": 0.08},  # waterway cargo ship ablaze
 "209948": {"Israeli airspace": 0.25, "Jordanian airspace": 0.16, "Iraqi airspace": 0.12, "Lebanese airspace": 0.10, "Saudi airspace": 0.08},  # airspace airline reopen
 "59501": {"United Arab Emirates": 0.22, "Qatar": 0.16, "Kuwait": 0.12, "Bahrain": 0.10, "Oman": 0.08},  # Gulf country >half Iran's exports
 "863162": {"Saudi Arabia": 0.24, "United Arab Emirates": 0.18, "Qatar": 0.12, "Kuwait": 0.10, "Bahrain": 0.08},  # Gulf country oil refinery hit
 "298918": {"Fujairah": 0.18, "Abu Dhabi": 0.15, "Sharjah": 0.11, "Dubai": 0.10, "Ras al-Khaimah": 0.08},  # UAE emirate oil facility smoke
 "560679": {"Microsoft": 0.15, "Amazon": 0.13, "Google": 0.11, "Oracle": 0.09, "Meta": 0.08},  # company Abu Dhabi site damaged
 "169286": {"United Arab Emirates": 0.20, "Qatar": 0.15, "Bahrain": 0.12, "Kuwait": 0.10, "Saudi Arabia": 0.08},  # country base US troops killed Iranian strike
 "70713": {"Qatar": 0.20, "Bahrain": 0.15, "United Arab Emirates": 0.12, "Kuwait": 0.10, "Iraq": 0.08},  # base location US troops killed
 "765155": {"Doha": 0.18, "Manama": 0.14, "Abu Dhabi": 0.11, "Kuwait City": 0.09, "Riyadh": 0.08},  # capital homes near US Embassy evacuated
 "779990": {"Riyadh": 0.16, "Jeddah": 0.13, "Mecca": 0.10, "Dammam": 0.09, "Abha": 0.08},  # Saudi city deadly military projectile
 "534224": {"Saudi Arabia": 0.20, "Oman": 0.15, "Qatar": 0.12, "Pakistan": 0.10, "China": 0.08},  # Pakistan ready to bring into Iran talks
 "584240": {"Saudi Arabia": 0.18, "Oman": 0.14, "Qatar": 0.11, "United Arab Emirates": 0.09, "Iraq": 0.08},  # Pakistan says help Iran talks
 "489669": {"England": 0.14, "Nigeria": 0.12, "Iran": 0.10, "Senegal": 0.09, "Morocco": 0.08},  # England defender goal/concedes pen WC
 "48811": {"Yafa an-Naseriyye": 0.10, "Kafr Kanna": 0.09, "Majd al-Krum": 0.08, "Sakhnin": 0.08, "Daliyat al-Karmel": 0.07},  # synagogue Michigan? no - site synagogue
 "350082": {"FBI": 0.15, "ATF": 0.12, "DHS": 0.10, "Joint Terrorism Task Force": 0.09, "Michigan State Police": 0.08},  # Michigan synagogue assailant - wait it's a name
 # (note: 350082 asks for the assailant's NAME in Michigan synagogue - fix below)
}
