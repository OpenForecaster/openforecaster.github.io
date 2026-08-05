# -*- coding: utf-8 -*-
"""Master forecast dict. {qid: {outcome: prob}}. Probs sum <=1.0, <=5 outcomes.
Context (as of 2026-03-25):
- US-Iran war (Operation Epic Fury) since Feb 28 2026. US+Israel vs Iran.
- Iran supreme leader Ali Khamenei killed -> son Mojtaba Khamenei. FM = Abbas Araghchi.
- Mediators: Pakistan (army chief/Field Marshal Asim Munir), Turkey (FM Hakan Fidan), Oman.
- Trump 15-pt ceasefire plan via Pakistan (Mar 25). Strait of Hormuz mined/closed.
- Gulf states (UAE) intercepting Iranian fire. Israel struck.
- Ukraine-Russia: Ukraine drone-striking Russian ports (Primorsk, Ust-Luga); new Russian offensive; US wants Ukraine to cede Donbas; UK boarding shadow-fleet tankers; Merz (Germany) says Ukraine doesn't need Taurus.
- F1 2026: Mercedes dominant (Antonelli, Russell 1-2s); Verstappen/Red Bull.
- Tennis: Alcaraz (won AO+Qatar, then slumps), Sinner (#2), Gauff(#4).
- NBA: Wembanyama/Spurs surging (MVP leader), Giannis/Bucks tanking (no deadline trade), Knicks strong.
- Football: Salah leaving Liverpool. Mbappe (Real) torn knee.
- Bangladesh PM = Tarique Rahman.
- Anthropic suing DoD re Claude use. OpenAI shutting Sora.
"""
F = {}

# ============ IRAN / US / ISRAEL / HORMUZ CLUSTER ============
F['299105'] = {"F-15E Strike Eagle":0.34, "F/A-18E Super Hornet":0.24, "F-35 Lightning II":0.16, "F-16 Fighting Falcon":0.16, "B-2 Spirit":0.10}  # 2 crew ejected -> 2-seat a/c
F['660351'] = {"Israel":0.42, "United Arab Emirates":0.24, "Saudi Arabia":0.14, "Qatar":0.10, "Bahrain":0.10}  # 281 missiles/drones target
F['597530'] = {"China":0.34, "Oman":0.20, "India":0.16, "Pakistan":0.16, "Japan":0.14}  # Hormuz exemption
F['77558'] = {"United Arab Emirates":0.30, "Saudi Arabia":0.26, "Oman":0.16, "Egypt":0.14, "Bahrain":0.14}  # Meloni after Qatar
F['583783'] = {"Abbas Araghchi":0.50, "Ali Bagheri Kani":0.20, "Majid Takht-Ravanchi":0.12, "Kazem Gharibabadi":0.10, "Mohammad Javad Zarif":0.08}  # Iran delegation head
F['638577'] = {"Oman":0.26, "Saudi Arabia":0.22, "Qatar":0.20, "China":0.16, "Iraq":0.16}  # Iran FM tour after Pakistan
F['793188'] = {"Iran":0.28, "United States":0.24, "Saudi Arabia":0.20, "Oman":0.16, "China":0.12}  # Pak PM last stop
F['727712'] = {"Asim Munir":0.34, "Shehbaz Sharif":0.30, "Ishaq Dar":0.20, "Bilawal Bhutto Zardari":0.16}  # Pak Tehran visit
F['481741'] = {"Donald Trump":0.30, "Marco Rubio":0.24, "Steve Witkoff":0.20, "JD Vance":0.14, "Pete Hegseth":0.12}  # US rejects Iran counterproposal
F['90872'] = {"Israel":0.30, "Saudi Arabia":0.20, "United Arab Emirates":0.16, "Qatar":0.12, "Jordan":0.12}  # LAX Iranian arms broker destination
F['128594'] = {"United Arab Emirates":0.26, "Saudi Arabia":0.22, "Bahrain":0.18, "Kuwait":0.14, "Qatar":0.12}  # Velayat-e Faqih cell arrests
F['905740'] = {"Delta":0.28, "Griselda":0.20, "Saker":0.16, "Kropyva":0.12, "Delphi":0.10}  # Ukrainian C2 platform at Prince Sultan AB  (Delta most likely)
F['213933'] = {"UNICEF":0.24, "IFRC":0.20, "Red Crescent":0.16, "OCHA":0.12, "WHO":0.10}  # generators/motor pumps to Iran relief
F['899138'] = {"Israel":0.30, "Saudi Arabia":0.22, "Qatar":0.16, "Italy":0.10, "Greece":0.08}  # Trump stop after war
F['261650'] = {"Mohammad Javad Zarif":0.20, "Abbas Araghchi":0.18, "Masoud Pezeshkian":0.14, "Mojtaba Khamenei":0.12, "Antonio Guterres":0.08}  # Gulf NATO proposal on Al Jazeera
F['965659'] = {"satellite system":0.24, "maritime escort coalition":0.20, "drone":0.14, "convoy":0.12, "app":0.08}  # US launch to guide ships out of Hormuz
F['222182'] = {"MQ-4C Triton":0.26, "RQ-4 Global Hawk":0.22, "MQ-9 Reaper":0.20, "RQ-170 Sentinel":0.16, "ScanEagle":0.10}  # US drone Iran intercepts in Hormuz
F['89772'] = {"United Arab Emirates":0.30, "Saudi Arabia":0.24, "Qatar":0.18, "Bahrain":0.14, "Kuwait":0.10}  # Gulf country intercepts 2 Iran drones
F['61483'] = {"Mohammad Javad Azari Jahromi":0.18, "Abolfazl Fateh":0.14, "Hassan Firoozabadi":0.12}  # Iran cyberspace HQ head (uncertain)
F['879060'] = {"Israel":0.30, "United Arab Emirates":0.24, "Qatar":0.18, "Bahrain":0.14, "Saudi Arabia":0.14}  # 2 countries Iran ballistic missiles toward (multi)
F['376096'] = {"Lindsey Graham":0.22, "Ted Cruz":0.16, "Rand Paul":0.16, "Tom Cotton":0.12, "Tim Kaine":0.10}  # US senator challenges Pakistan mediator role
F['738968'] = {"Beirut":0.26, "Damascus":0.20, "Tehran":0.14, "Baghdad":0.12}  # city targeted in Israeli strike triggering flare-up
F['907565'] = {"Israel":0.24, "United States":0.20, "Saudi Arabia":0.12, "Ukraine":0.10}  # who cancels Switzerland trip under US-Iran memo
F['622780'] = {"Riyadh":0.26, "Doha":0.22, "Abu Dhabi":0.20, "Muscat":0.16, "Manama":0.16}  # US SecState meets Gulf FMs
F['734891'] = {"Bavar-373":0.30, "Khordad-15":0.22, "Arman":0.16, "Majid":0.12, "15th Khordad":0.10}  # Iran domestic ADS intercepts US drone
F['502300'] = {"Abbas Araghchi":0.34, "Ali Bagheri Kani":0.20, "Mohammad Javad Zarif":0.16, "Masoud Pezeshkian":0.14, "Mojtaba Khamenei":0.16}  # Tehran top negotiator signs framework
F['384398'] = {"Oman":0.34, "Turkey":0.22, "Saudi Arabia":0.18, "China":0.14, "Qatar":0.12}  # country mediating US-Iran talks alongside Pakistan
F['147720'] = {"Abdul Aziz al-Mutairi":0.16, "Ahmad al-Hamidawi":0.16, "Abu Alaa al-Walai":0.12}  # Kataib Hezbollah commander charged Manhattan (uncertain)
F['204607'] = {"Masoud Pezeshkian":0.24, "Mojtaba Khamenei":0.22, "Abbas Araghchi":0.18, "Ali Khamenei":0.10}  # Trump willing to speak with
F['869693'] = {"Khor Fakkan":0.20, "Fujairah":0.18, "Sohar":0.16, "Muscat":0.12, "Dubai":0.10}  # port where US seizes MV Touska

# Israel/Gaza/Lebanon
F['829924'] = {"Maroun al-Ras":0.18, "Bint Jbeil":0.16, "Aitaroun":0.14, "Yaroun":0.12, "Blida":0.10}  # southern Lebanese town surrounded
F['864352'] = {"Tyre":0.22, "Sidon":0.18, "Nabatieh":0.16, "Bafta":0.10}  # Lebanese city evacuation order
F['655455'] = {"Sidon":0.18, "Tyre":0.16, "Nabatieh":0.14, "Beirut":0.10}  # two-missile Israeli drone bombing
F['651194'] = {"Jenin":0.22, "Gaza City":0.20, "Nablus":0.14, "Tubas":0.12, "Ramallah":0.10}  # Israeli airstrike near Al-Qassam mosque
F['793435'] = {"Bezalel Smotrich":0.24, "Itamar Ben-Gvir":0.22, "Israel Katz":0.18, "Amichai Eliyahu":0.12}  # Israeli minister convoy
F['873844'] = {"Almeria":0.18, "Las Palmas":0.14}  # Messi acquires Spanish club (uncertain)
F['430728'] = {"Russia":0.30, "Georgia":0.16, "Jordan":0.12}  # country discusses 16 nationals killed fighting abroad
F['441315'] = {"United States":0.30, "France":0.18, "Germany":0.12}  # Trump suggests handles Hezbollah
F['183188'] = {"West Bank":0.20, "Golan Heights":0.16}  # Israel settlement-construction funds location

# Ukraine-Russia
F['826730'] = {"Novorossiysk":0.22, "Feodosia":0.18, "Sevastopol":0.16, "Kerch":0.12}  # Ukraine strikes 2 Russian landing ships
F['119565'] = {"Alexander Novak":0.22, "Alexander Kozlov":0.16, "Sergei Tsivilev":0.14, "Vitaly Savelyev":0.12}  # Russian minister Putin dispatches
F['347255'] = {"London":0.18, "Berlin":0.16, "Paris":0.14, "Rome":0.10}  # where Ukraine president meets FR/DE/UK leaders
F['417584'] = {"Kharkiv":0.20, "Kyiv":0.16, "Odesa":0.14, "Dnipro":0.12}  # Ukrainian city residential high-rise hit
F['34985'] = {"John Kennedy":0.0, "Bill Cassidy":0.20, "Jeff Landry":0.16, "Steve Scalise":0.14, "Garret Graves":0.10}  # Louisiana GOP Senate runoff

# validate
if __name__ == '__main__':
    import sys
    for q,o in F.items():
        s=sum(o.values())
        assert s<=1.0+1e-9, (q,s)
        assert len(o)<=5, (q,len(o))
    print("OK", len(F), "forecasts")

# ============ SPORTS: FOOTBALL ============
F['776644'] = {"Cole Palmer":0.30, "Moises Caicedo":0.20, "Enzo Fernandez":0.16, "Romeo Lavia":0.12, "Nicolas Jackson":0.10}  # Chelsea midfielder not playing vs Man City
F['327626'] = {"Manchester City":0.22, "Liverpool":0.20, "Newcastle United":0.16, "Chelsea":0.14, "Tottenham Hotspur":0.12}  # eliminate Arsenal FA Cup QF
F['350996'] = {"Robert Lewandowski":0.26, "Raphinha":0.20, "Lamine Yamal":0.18, "Ferran Torres":0.10, "Frenkie de Jong":0.08}  # Barca winning goal vs Atletico
F['432067'] = {"Erling Haaland":0.34, "Omar Marmoush":0.18, "Phil Foden":0.16, "Jeremy Doku":0.10, "Savinho":0.08}  # Man City opener vs Burnley
F['993293'] = {"Robert Lewandowski":0.28, "Lamine Yamal":0.22, "Raphinha":0.20, "Ferran Torres":0.10, "Gavi":0.06}  # Barca first goal vs Celta Vigo
F['407333'] = {"Kylian Mbappe":0.24, "Vinicius Junior":0.22, "Jude Bellingham":0.18, "Rodrygo":0.14, "Brahim Diaz":0.08}  # Real Madrid opener vs Betis
F['639098'] = {"Son Heung-min":0.22, "James Maddison":0.18, "Dominic Solanke":0.16, "Brennan Johnson":0.12, "Dejan Kulusevski":0.10}  # Spurs winner vs Sunderland
F['161050'] = {"Bruno Fernandes":0.22, "Alejandro Garnacho":0.18, "Rasmus Hojlund":0.14, "Marcus Rashford":0.12, "Kobbie Mainoo":0.08}  # Man Utd winner vs Liverpool
F['371136'] = {"Ollie Watkins":0.26, "Morgan Rogers":0.20, "Leon Bailey":0.12, "Youri Tielemans":0.10, "John McGinn":0.08}  # Aston Villa opener vs Liverpool
F['190217'] = {"Achraf Hakimi":0.45, "Warren Zaire-Emery":0.16, "Desire Doue":0.12, "Georginio Rutter":0.08}  # PSG right-back CL SF 2nd leg
F['722040'] = {"Dino Toppmoller":0.20, "Benni McCarthy":0.12, "Daniel Peretz":0.08}  # Bayern acting coach CL SF (Kompany suspended? uncertain)
F['593343'] = {"Liverpool":0.12, "Manchester City":0.10, "Chelsea":0.10, "Tottenham Hotspur":0.09, "Newcastle United":0.08}  # Arsenal 2026-27 PL opener (spread)
F['912804'] = {"Inter Milan":0.26, "AC Milan":0.20, "Atalanta":0.16, "Juventus":0.14, "Bologna":0.10}  # Italian Cup (Coppa Italia) winner
F['896840'] = {"Al-Ittihad":0.28, "Al-Hilal":0.26, "Al-Nassr":0.20, "Al-Ahli":0.16}  # Saudi Pro League winner
F['507993'] = {"Mamelodi Sundowns":0.40, "Orlando Pirates":0.24, "Kaizer Chiefs":0.16, "Stellenbosch":0.10}  # South African Premiership
F['796483'] = {"Mohamed Salah":0.22, "Bukayo Saka":0.14, "Cole Palmer":0.12, "Alexander Isak":0.10, "Ollie Watkins":0.08}  # PL Player of Season
F['244762'] = {"Real Madrid Castilla":0.18}  # Arbeloa leaves which club (he coaches Castilla) - uncertain
F['671712'] = {"WTA":0.30, "ATP":0.22, "ITF":0.18, "Grand Slam Board":0.14}  # org in GS revenue-sharing dialogue
F['385416'] = {"Roberto De Zerbi":0.22, "Andoni Iraola":0.16, "Graham Potter":0.14, "Oliver Glasner":0.12, "Kieran McKenna":0.10}  # Chelsea next permanent manager
F['600383'] = {"Ruben Amorim":0.18, "Gareth Southgate":0.14, "Thomas Frank":0.12, "Mauricio Pochettino":0.10, "Kieran McKenna":0.08}  # Man Utd permanent manager
F['313921'] = {"Enzo Maresca":0.26, "Pep Guardiola":0.16, "Xabi Alonso":0.12, "Roberto De Zerbi":0.10, "Vincent Kompany":0.08}  # Man City manager replacing Guardiola
F['335788'] = {"Bo Svensson":0.16, "Sandro Wagner":0.12}  # Union Berlin head coach (uncertain)
F['824613'] = {"Johan Boskamp":0.12}  # Ghana head coach (uncertain - spread)
F['382614'] = {"Nazmul Hassan":0.18, "Faruque Ahmed":0.16, "Saber Chowdhury":0.12}  # Bangladesh interim cricket board head
F['287813'] = {"Law 218":0.16, "Law 144":0.12, "DS 29181":0.10}  # Bolivia agrarian reform law (uncertain)
F['250786'] = {"Urawa Red Diamonds":0.16, "Wuhan Jianghan University":0.14, "Melbourne City":0.12}  # AFC Women's CL final Naegohyang opponent
F['755944'] = {"Uzbekistan":0.18, "Qatar":0.14, "South Korea":0.12, "Iraq":0.10, "United Arab Emirates":0.10}  # Iran WC warm-up opponent
F['919933'] = {"United Israel":0.14, "National Unity":0.12, "Israel Forward":0.10}  # Bennett+Lapid new party name (uncertain)
F['721466'] = {"Emam Ashour":0.16, "Mohamed Sherif":0.12}  # Egyptian Pro League suspension (uncertain)
F['229471'] = {"Matthijs de Ligt":0.18, "Leny Yoro":0.16, "Harry Maguire":0.12, "Victor Lindelof":0.10}  # Man Utd centre-back suspended
F['463187'] = {"Jarrod Bowen":0.18, "Mohammed Kudus":0.14, "Lucas Paqueta":0.12}  # Arsenal-West Ham disallowed equalizer
F['635710'] = {"Vinicius Junior":0.20, "Jude Bellingham":0.16, "Rodrygo":0.12, "David Alaba":0.10}  # Real Madrid player omitted El Clasico
F['870813'] = {"Vinicius Junior":0.22, "Rodrygo":0.18, "Raphinha":0.16, "Endrick":0.10}  # Brazil forward out with calf injury
F['581141'] = {"Reece James":0.18, "Trent Alexander-Arnold":0.14, "Kyle Walker":0.12, "Rico Lewis":0.10}  # replace Livramento England WC squad
F['542717'] = {"Anthony Gordon":0.14, "Morgan Gibbs-White":0.12, "Noni Madueke":0.10}  # England 127th Black debutant (uncertain)
F['156130'] = {"Suryakumar Yadav":0.28, "Shubman Gill":0.22, "Hardik Pandya":0.16, "Rishabh Pant":0.10, "Jasprit Bumrah":0.08}  # India T20I captain
F['80657'] = {"University of Leeds":0.16, "University of Manchester":0.12, "UCL":0.10, "University of Sheffield":0.08}  # UK university redundancies (uncertain)
F['536265'] = {"Gerber":0.18, "Aptamil":0.14, "Heinz":0.10, "Organix":0.08}  # baby-food brand rat poison recall (uncertain)
F['556711'] = {"Australia":0.18, "Saudi Arabia":0.16, "China":0.14, "Bahrain":0.10, "Iraq":0.08}  # drawn into Japan Group F (WC draw)

# ============ SPORTS: F1 / MotoGP ============
F['221686'] = {"George Russell":0.26, "Kimi Antonelli":0.22, "Max Verstappen":0.22, "Lando Norris":0.14, "Oscar Piastri":0.10}  # Miami GP pole
F['665320'] = {"Mercedes":0.34, "McLaren":0.24, "Red Bull":0.20, "Ferrari":0.16}  # Miami GP constructor winner
F['354992'] = {"Max Verstappen":0.20, "George Russell":0.18, "Kimi Antonelli":0.16, "Lando Norris":0.14, "Oscar Piastri":0.12}  # Miami qualify 3rd
F['188803'] = {"Kimi Antonelli":0.24, "George Russell":0.22, "Max Verstappen":0.20, "Lando Norris":0.14, "Oscar Piastri":0.10}  # F1 leader after Canadian GP
F['165056'] = {"Max Verstappen":0.20, "George Russell":0.18, "Kimi Antonelli":0.18, "Lando Norris":0.14, "Oscar Piastri":0.12}  # 3rd in champ before Monaco
F['66287'] = {"Mercedes":0.30, "McLaren":0.24, "Ferrari":0.20, "Red Bull":0.18}  # Barcelona constructor winner
F['660626'] = {"Max Verstappen":0.18, "George Russell":0.16, "Lando Norris":0.16, "Oscar Piastri":0.14, "Charles Leclerc":0.12}  # Barcelona 3rd place
F['519536'] = {"Max Verstappen":0.26, "George Russell":0.20, "Kimi Antonelli":0.16, "Lando Norris":0.14, "Oscar Piastri":0.10}  # Austrian GP winner
F['310636'] = {"Marc Marquez":0.34, "Francesco Bagnaia":0.22, "Jorge Martin":0.16, "Pedro Acosta":0.10}  # MotoGP leader after French GP
F['562636'] = {"Marc Marquez":0.28, "Francesco Bagnaia":0.20, "Jorge Martin":0.16, "Pedro Acosta":0.12, "Francesco Bagnaia":0.0}  # Czech MotoGP winner

# ============ SPORTS: NBA / GOLF / TENNIS / BOXING / OTHER ============
F['979878'] = {"Victor Wembanyama":0.34, "Shai Gilgeous-Alexander":0.22, "Nikola Jokic":0.16, "Luka Doncic":0.10, "Cade Cunningham":0.08}  # NBA MVP
F['583390'] = {"AJ Dybantsa":0.30, "Darryn Peterson":0.18, "Cameron Boozer":0.16, "Koa Peat":0.10, "Nate Ament":0.08}  # NBA Draft #1
F['360663'] = {"San Antonio Spurs":0.20, "Oklahoma City Thunder":0.16, "Houston Rockets":0.14, "New York Knicks":0.10, "Golden State Warriors":0.08}  # Giannis team
F['977017'] = {"Minnesota Timberwolves":0.46, "Denver Nuggets":0.40}  # Wolves-Nuggets Game 4
F['139613'] = {"Boston Celtics":0.52, "Philadelphia 76ers":0.30}  # Philly-Boston series
F['67348'] = {"Shai Gilgeous-Alexander":0.18, "Jalen Brunson":0.14, "Anthony Edwards":0.12, "Luka Doncic":0.10}  # NBA Finals G2 go-ahead FT
F['119754'] = {"Victor Wembanyama":0.14, "Anthony Edwards":0.12, "Jalen Brunson":0.10}  # NBA Finals G4 winning tip-in
F['996413'] = {"Jalen Brunson":0.26, "Karl-Anthony Towns":0.18, "OG Anunoby":0.12, "Mikal Bridges":0.10}  # Knicks 7th postseason triple-double
F['893744'] = {"Scottie Scheffler":0.20, "Rory McIlroy":0.16, "Jon Rahm":0.12, "Xander Schauffele":0.10, "Collin Morikawa":0.08}  # Masters winner
F['254200'] = {"Scottie Scheffler":0.18, "Rory McIlroy":0.14, "Jon Rahm":0.12, "Xander Schauffele":0.10, "Bryson DeChambeau":0.08}  # US Open golf winner
F['988210'] = {"Citizen Bull":0.12, "Baeza":0.10, "Sovereignty":0.10, "Journalism":0.10, "Cornucopian":0.08}  # Kentucky Derby (wide open)
F['915408'] = {"Sweden":0.16, "Austria":0.14, "France":0.12, "Italy":0.10, "Switzerland":0.08}  # Eurovision winner
F['499127'] = {"Hellen Obiri":0.18, "Sifan Hassan":0.14, "Sharon Lokedi":0.12, "Yalemzerf Yehualaw":0.10}  # Boston Marathon women
F['559024'] = {"Carlos Alcaraz":0.16, "Daniil Medvedev":0.12, "Jack Draper":0.10, "Tommy Paul":0.08}  # defeats Sinner French Open R2 (upset)
F['217220'] = {"Carlos Alcaraz":0.18, "Novak Djokovic":0.14, "Jack Draper":0.10, "Tommy Paul":0.08}  # Kouame French Open R2 opponent
F['720539'] = {"Aryna Sabalenka":0.20, "Iga Swiatek":0.18, "Mirra Andreeva":0.12, "Elena Rybakina":0.10}  # defeats Gauff French Open
F['666275'] = {"Carlos Alcaraz":0.16, "Jannik Sinner":0.14, "Jack Draper":0.10, "Ben Shelton":0.08}  # defeats Norrie Wimbledon R1
F['212559'] = {"Deontay Wilder":0.22, "Tyson Fury":0.20, "Joseph Parker":0.14, "Filip Hrgovic":0.10}  # Joshua Riyadh opponent
F['314546'] = {"Michael Chandler":0.26, "Conor McGregor":0.0, "Dustin Poirier":0.16, "Charles Oliveira":0.12, "Justin Gaethje":0.10}  # McGregor UFC opponent
F['60426'] = {"Daniel Dubois":0.24, "Joseph Parker":0.18, "Filip Hrgovic":0.14, "Zhilei Zhang":0.10, "Agit Kabayel":0.08}  # WBA successor to Usyk
F['284263'] = {"Fabiano Caruana":0.30, "Hikaru Nakamura":0.24, "Gukesh Dommaraju":0.0, "Ian Nepomniachtchi":0.14, "Ding Liren":0.10}  # Gukesh challenger (Carlsen excluded)
F['130734'] = {"Ali Farag":0.26, "Paul Coll":0.18, "Diego Elias":0.16, "Mostafa Asal":0.12}  # PSA men's World Championship
F['802784'] = {"Aryna Sabalenka":0.24, "Sifan Hassan":0.14, "Sydney McLaughlin-Levrone":0.12, "Alessandra Tripoli":0.0}  # Laureus Sportswoman
F['14338'] = {"Coca-Cola 600":0.20, "Nashville":0.14, "Charlotte":0.12}  # Kyle Busch final NASCAR race
F['278361'] = {"Russia":0.20, "Belarus":0.16, "Iran":0.12}  # IOC country full identity
F['75576'] = {"Katie Porter":0.18, "Gavin Newsom":0.0, "Antonio Villaraigosa":0.14, "Eleni Kounalakis":0.12, "Betty Yee":0.10}  # Emerson CA gov primary
print("batch2 appended")

# ============ WORLD CUP 2026 GOALS / MATCHES ============
F['20480'] = {"Christian Pulisic":0.45, "Tyler Adams":0.16, "Weston McKennie":0.10, "Matt Turner":0.0}  # US captain WC
F['523850'] = {"Christian Pulisic":0.30, "Folarin Balogun":0.18, "Ricardo Pepi":0.14, "Tim Weah":0.10, "Gio Reyna":0.08}  # US first WC double since 1930
F['800177'] = {"Christian Pulisic":0.26, "Folarin Balogun":0.18, "Ricardo Pepi":0.12, "Tim Weah":0.10}  # US final goal vs Paraguay
F['200337'] = {"Bebe":0.16, "Dally":0.14, "Ryan Mendes":0.12, "Garry Rodrigues":0.10, "Kenny Rocha":0.08}  # Cape Verde first WC goal
F['447494'] = {"Cristiano Ronaldo":0.26, "Bruno Fernandes":0.18, "Rafael Leao":0.14, "Diogo Jota":0.10, "Goncalo Ramos":0.08}  # Portugal opener Group K
F['497440'] = {"Cristiano Ronaldo":0.24, "Bruno Fernandes":0.18, "Rafael Leao":0.14, "Bernardo Silva":0.10, "Diogo Jota":0.08}  # Portugal winner vs Nigeria
F['514723'] = {"Luis Diaz":0.22, "Jhon Cordoba":0.16, "James Rodriguez":0.14, "Miguel Borja":0.10}  # Colombia disallowed vs Portugal
F['893085'] = {"Luis Diaz":0.22, "Jhon Cordoba":0.16, "James Rodriguez":0.14, "Miguel Borja":0.10, "Luis Sinisterra":0.08}  # Colombia first goal Group K
F['482087'] = {"Cedric Bakambu":0.22, "Yoane Wissa":0.18, "Silas Katompa":0.14, "Meschack Elia":0.10}  # DR Congo first WC goal
F['144247'] = {"Eldor Shomurodov":0.28, "Oston Urunov":0.18, "Otabek Shukurov":0.10, "Jaloliddin Masharipov":0.08}  # Uzbekistan first WC goal
F['49405'] = {"Ousmane Dembele":0.20, "Marcus Thuram":0.16, "Antoine Griezmann":0.14, "Bradley Barcola":0.10, "Randal Kolo Muani":0.08}  # France first vs Iraq
F['19116'] = {"Lionel Messi":0.30, "Julián Alvarez":0.18, "Lautaro Martinez":0.14, "Nahuel Molina":0.08}  # Argentina assist vs Austria
F['56157'] = {"Sadio Mane":0.24, "Ismaila Sarr":0.18, "Nicolas Jackson":0.14, "Habib Diallo":0.10}  # Senegal first vs France
F['526797'] = {"Sadio Mane":0.30, "Idrissa Gueye":0.16, "Kalidou Koulibaly":0.08}  # Senegalese first to score at 2 WCs
F['563723'] = {"Kevin De Bruyne":0.16, "Romelu Lukaku":0.14, "Jeremy Doku":0.12, "Youri Tielemans":0.10}  # Belgium player leaves for childbirth
F['122629'] = {"Sebastien Haller":0.18, "Simon Adingra":0.16, "Nicolas Pepe":0.12, "Maxwel Cornet":0.08}  # Ivory Coast forward auth Canada
F['464656'] = {"Sebastien Haller":0.20, "Simon Adingra":0.16, "Franck Kessie":0.12, "Nicolas Pepe":0.10}  # Ivory Coast winner vs France
F['134159'] = {"Salem Al-Dawsari":0.30, "Firas Al-Buraikan":0.20, "Saleh Al-Shehri":0.14, "Abdullah Al-Hamdan":0.08}  # Saudi first vs Uruguay
F['478073'] = {"Mohamed Salah":0.30, "Omar Marmoush":0.22, "Trezeguet":0.12, "Mostafa Mohamed":0.10}  # Egypt first goal Group G
F['982169'] = {"Alexander Isak":0.28, "Viktor Gyokeres":0.22, "Dejan Kulusevski":0.14, "Emil Forsberg":0.08}  # Sweden first vs Tunisia
F['20324'] = {"Cody Gakpo":0.24, "Memphis Depay":0.20, "Xavi Simons":0.14, "Brian Brobbey":0.10, "Donyell Malen":0.08}  # Netherlands first Group F
F['923634'] = {"Patrik Schick":0.26, "Adam Hlozek":0.18, "Tomas Soucek":0.14, "Vaclav Cerny":0.08}  # Czechia opener vs South Africa
F['915754'] = {"Kaoru Mitoma":0.16, "Takefusa Kubo":0.14, "Takehiro Tomiyasu":0.10, "Wataru Endo":0.08}  # Japan replace injured captain
F['812233'] = {"Lamine Yamal":0.22, "Dani Olmo":0.16, "Alvaro Morata":0.14, "Nico Williams":0.12, "Pedri":0.08}  # Spain opener warm-up
F['596856'] = {"Ecuador":0.14, "Mexico":0.12, "Morocco":0.10, "Japan":0.08}  # Argentina defeat final warm-up
F['276967'] = {"Sergio Ramos":0.10}  # player red card tackle on Ismael Kone (uncertain)
F['230283'] = {"Achraf Hakimi":0.16, "Sofiane Diab":0.10}  # assist Morocco-Scotland (uncertain)
F['195361'] = {"Sanju Samson":0.14, "Yashasvi Jaiswal":0.12, "Riyan Parag":0.10}  # IPL eliminator player of match RR-SRH
F['726490'] = {"Islamabad United":0.22, "Peshawar Zalmi":0.18, "Multan Sultans":0.16, "Lahore Qalandars":0.12, "Quetta Gladiators":0.10}  # PSL winner
F['278085'] = {"Egypt":0.16, "South Africa":0.14, "Morocco":0.12, "DR Congo":0.10}  # CAF Confederation Cup final return leg host

# ============ ELECTIONS / POLITICS ============
F['692616'] = {"All India Trinamool Congress":0.50, "BJP":0.28, "INC":0.10}  # West Bengal election
F['464226'] = {"DMK":0.46, "AIADMK":0.26, "BJP":0.12, "NTK":0.06}  # Tamil Nadu election
F['431712'] = {"Rafael Lopez Aliaga":0.14, "Mario Meza Cuadra":0.10}  # Peru runoff vs Fujimori (uncertain)
F['984668'] = {"Gustavo Petro":0.18, "Vicky Davila":0.14, "German Vargas Lleras":0.10, "Maria Fernanda Cabal":0.08}  # Colombia first-round leader
F['399152'] = {"Kim Reynolds":0.30}  # Iowa GOP gov primary (incumbent) - low info
F['32537'] = {"Angus King":0.20}  # Maine Dem Senate primary (uncertain)
F['923435'] = {"Muriel Bowser":0.0, "Robert White":0.16, "Trayon White":0.10}  # DC Dem mayoral primary
F['963308'] = {"Lindsey Boylan":0.16, "Zohran Mamdani":0.0, "Yuh-Line Niou":0.12}  # Nadler seat Dem primary
F['795702'] = {"Stacey Abrams":0.18, "Lucy McBath":0.14, "Jason Carter":0.10}  # Georgia Dem gov primary
F['746420'] = {"Brian Kemp":0.20, "Vernon Jones":0.12, "Geoff Duncan":0.10}  # Georgia GOP gov runoff vs Rick Jackson
F['883794'] = {"The Nationals":0.40, "Liberal Party":0.20, "Independent":0.16}  # Farrer (Australia) party
F['592683'] = {"Sussan Ley":0.18}  # Farrer winner (uncertain - Nationals hold)
F['287636'] = {"Robert Golob":0.34, "Janez Jansa":0.24}  # Slovenia PM
F['368203'] = {"Viktor Orban":0.40, "Peter Magyar":0.30}  # Hungary PM
F['607727'] = {"Guxo List":0.28, "LDK":0.20, "AAK":0.10, "PDK":0.10}  # Osmani party list
F['829683'] = {"PSD":0.22, "PNL":0.18, "AUR":0.14, "USR":0.10, "PMP":0.06}  # Romania replacement PM party
F['138890'] = {"Francis Escudero":0.28, "Juan Miguel Zubiri":0.20, "Vicente Sotto":0.14, "Alan Peter Cayetano":0.10}  # Philippines Senate president
F['916578'] = {"Germany":0.24, "Greece":0.18, "Norway":0.14, "Canada":0.10}  # UNSC WEOG seat w/ Portugal
F['659827'] = {"Democratic Alliance":0.24, "ANC":0.20, "EFF":0.10}  # Farmgate report court challenge winner
F['455791'] = {"Nancy Pelosi":0.20, "Lateefah Simon":0.16, "Christine Pelosi":0.10}  # Pelosi endorsement CA-11 (her district)
F['673870'] = {"Susan Collins":0.16, "Lisa Murkowski":0.30}  # GOP senator sole supporter of Senate measure (her party)
F['322623'] = {"Angela Rayner":0.16, "Yvette Cooper":0.12, "Rachel Reeves":0.10}  # Labour MP abandons leadership bid
F['226441'] = {"Angela Rayner":0.16, "Andy Burnham":0.12, " Wes Streeting":0.0}  # Labour contender calls Brexit catastrophic mistake
F['593643'] = {"Labour":0.40, "Reform UK":0.24, "Conservative":0.16}  # Makerfield by-election Labour nominee -> winner
F['764201'] = {"Reform UK":0.30}  # party first UK parliamentary election in Makerfield
F['912811'] = {"Labour":0.20, "Conservative":0.16}  # party council areas Reform UK migrant detention pledge
F['737606'] = {"Gordon Brown":0.18, "Tony Blair":0.14, "David Cameron":0.10, "Theresa May":0.08}  # former UK PM Starmer appoints
F['740282'] = {"Narendra Modi":0.20, "Mohan Bhagwat":0.16}  # resignation demanded at Cockroach Janta Party rally
F['708699'] = {"Vishva Hindu Parishad":0.16, "Bajrang Dal":0.12, "RSS":0.10}  # org calls namaz show of strength

# ============ APPOINTMENTS / DELEGATIONS / DIPLOMACY ============
F['881473'] = {"To Lam":0.16, "Luong Cuong":0.14}  # Japan PM Vietnamese counterpart (Vietnam top leader)
F['70966'] = {"Asaad al-Shibani":0.22, "Ahmed al-Sharaa":0.16}  # Syria delegation Lebanon talks leader
F['679514'] = {"Mmusi Maimane":0.14, "Tony Leon":0.10}  # SA ambassador to US (uncertain)
F['523557'] = {"Mohammed Shia al-Sudani":0.30}  # Iraq PM-designate named by president
F['610527'] = {"William Barr":0.16, "Jeff Sessions":0.12, "Eric Holder":0.10, "Michael Mukasey":0.08}  # former US AG House Oversight closed-door
F['89814'] = {"Mario Zamora":0.18}  # Costa Rica security minister (incumbent) 
F['820934'] = {"Jasveen Sangha":0.18, "Erik Fleming":0.12, "Kenneth Iwamasa":0.10}  # final sentenced Matthew Perry case
F['646081'] = {"Madeleine King":0.16, "Chris Bowen":0.12}  # Australia overseas diesel shipment announcer
F['356778'] = {"Angus Campbell":0.18, "Simon Stuart":0.14}  # head of Australian Defence Force
F['68941'] = {"Western Australia":0.24, "New South Wales":0.18, "Victoria":0.14, "Queensland":0.10}  # Ben Roberts-Smith court state
F['634534'] = {"Matt Turner":0.28, "Zack Steffen":0.18, "Patrick Schulte":0.12, "Ethan Horvath":0.08}  # US first-choice GK WC
F['813864'] = {"Marc-Andre ter Stegen":0.30, "Oliver Baumann":0.14, "Alexander Nubel":0.10}  # GK Nagelsmann replaces Germany #1
F['356699'] = {"Manchester":0.12, "London":0.10}  # city commuter+long-distance train collide (uncertain)
F['96126'] = {"Potters Bar":0.10, "Hayes":0.08}  # town two London-bound trains collision (uncertain)
F['303507'] = {"Han Zheng":0.20, "Wang Huning":0.16, "Cai Qi":0.12, "Ding Xuexiang":0.10}  # highest Chinese official greets Trump Beijing
F['855937'] = {"Antena 3":0.16, "La Sexta":0.12, "TVE":0.10}  # Spanish TV channel Milei leaked recordings
F['217413'] = {"Mariano Rajoy":0.18, "Jose Luis Rodriguez Zapatero":0.12, "Jose Maria Aznar":0.10}  # former Spanish PM investigated airline bailout
F['839333'] = {"Jose Luis Martinez-Almeida":0.16}  # who presents Machado Madrid gold medal (uncertain)
F['711332'] = {"Donald Tusk":0.14, "Yair Lapid":0.10}  # Poland president strip state honour from (uncertain)
F['208894'] = {"Miguel Diaz-Canel":0.20}  # who announces Ramiro Valdes death (Cuba)
F['605050'] = {"Philemon Yang":0.14, "Helga Schmid":0.12}  # UNGA 81st president
F['868524'] = {"Clementine Nkweta-Salami":0.12}  # Coalition for Atrocity Prevention Sudan statement to UNHRC
F['529979'] = {"Todd Lyons":0.0, "Caleb Vitello":0.18, "Gary Shreffler":0.12}  # successor acting ICE director
F['654858'] = {"Mohammad Radwan":0.10}  # Syria agriculture minister (uncertain)
F['845372'] = {"Spain":0.18, "France":0.14}  # country airlifts MT Marivex crew
F['500590'] = {"Anthony Taylor":0.12, "Szymon Marciniak":0.10, "Daniele Orsato":0.08}  # referee Mexico-South Africa WC opener
F['657924'] = {"Reid Wiseman":0.16, "Victor Glover":0.14}  # Artemis III commander
F['846721'] = {"Pam Bondi":0.20, "Kash Patel":0.14, "James Comey":0.10}  # US official charges from WHCD
print("batch3 appended")

# ============ DISASTERS / INCIDENTS / LOCATIONS ============
F['398343'] = {"Ternate":0.24, "Tobelo":0.18, "Bitung":0.14, "Manado":0.12, "Tidore":0.10}  # Indonesian city quake fatality (N Molucca Sea)
F['801535'] = {"Iwate":0.22, "Miyagi":0.20, "Aomori":0.16, "Hokkaido":0.14, "Fukushima":0.10}  # Japan prefecture offshore quake
F['926607'] = {"Samar":0.20, "Leyte":0.16, "Mindanao":0.14, "Mindoro":0.10, "Luzon":0.10}  # Philippine island epicenter
F['699330'] = {"Sucre":0.20, "Miranda":0.16, "Carabobo":0.14, "Aragua":0.12, "Vargas":0.10}  # Venezuelan state twin quakes
F['30914'] = {"Petare":0.18, "Catia":0.14, "El Valle":0.10, "Chacao":0.08}  # Caracas district 22-storey rubble
F['356699'] = {"Mumbai":0.12, "Delhi":0.10, "Kolkata":0.08, "Chennai":0.08}  # city train collision (uncertain)
F['96126'] = {"Reading":0.10, "Slough":0.08, "Hayes":0.08}  # town London-bound trains collision (uncertain)
F['978710'] = {"Baton Rouge":0.16, "New Orleans":0.14, "Shreveport":0.10, "Lafayette":0.08}  # Louisiana shooting location
F['773935'] = {"Tamaulipas":0.18, "Sinaloa":0.16, "Jalisco":0.12, "Sonora":0.10, "Nuevo Leon":0.08}  # Mexican state US officials crash
F['715198'] = {"Lviv":0.14, "Kyiv":0.12}  # cemetery discovery location (uncertain)
F['465412'] = {"Gao":0.20, "Timbuktu":0.16, "Kidal":0.14, "Menaka":0.12, "Bourem":0.08}  # northern Malian town JNIM/FLA
F['146757'] = {"El Fasher":0.24, "Khartoum":0.16, "Kordofan":0.12, "Kassala":0.08}  # Sudanese city RSF offensive
F['523555'] = {"Juba":0.14, "Nairobi":0.12, "Addis Ababa":0.10, "Khartoum":0.08}  # departure location Juba crash flight
F['722131'] = {"Lake Chad":0.16, "Sambisa":0.12}  # joint US-Nigerian ISIL strike location (uncertain)
F['425800'] = {"Mina al-Ahmadi":0.14, "Ras Laffan":0.12, "Yanbu":0.10, "Fujairah":0.08}  # port maritime drone oil terminal
F['329861'] = {"Qatargas":0.16, "RasGas":0.12}  # factory Ras Laffan explosion (uncertain)
F['421126'] = {"Quetta":0.22, "Peshawar":0.18, "Karachi":0.14, "Lahore":0.10}  # Pakistani city blast paramilitary gate
F['153557'] = {"Bangkok":0.14, "Jakarta":0.12}  # construction-site collapse location (uncertain)
F['197064'] = {"Maharashtra":0.14, "Delhi":0.12, "Tamil Nadu":0.10, "Gujarat":0.08, "Uttar Pradesh":0.08}  # Indian state commercial fire
F['608792'] = {"Kaduna":0.18, "Katsina":0.16, "Zamfara":0.12, "Sokoto":0.10, "Borno":0.08}  # Nigerian state school closures abduction
F['927519'] = {"Kaduna":0.18, "Katsina":0.14, "Zamfara":0.12, "Sokoto":0.10, "Niger":0.08}  # Nigerian state kidnapping children
F['743167'] = {"Phoenix":0.12, "Dubai":0.10}  # town skydiving-plane crash (uncertain)
F['581070'] = {"Phuket":0.20, "Koh Samui":0.16, "Koh Phangan":0.12, "Koh Tao":0.10}  # Thai island confiscated plots
F['90400'] = {"Willesden":0.16, "Wembley":0.14, "Kilburn":0.12, "Harlesden":0.10}  # NW London neighbourhood arson Persian media
F['735499'] = {"Burundi":0.18, "DR Congo":0.14, "Nigeria":0.12, "Uganda":0.10}  # country 65,399 malaria cases
F['676234'] = {"DR Congo":0.20, "Nigeria":0.16, "Ethiopia":0.12, "Chad":0.10}  # country 500+ child measles deaths
F['82467'] = {"United States":0.24, "Germany":0.14, "United Kingdom":0.12}  # country admit Ebola patient from DRC
F['507868'] = {"France":0.16, "Spain":0.14, "Germany":0.12, "Netherlands":0.10}  # country 9 hikers Halmahera eruption
F['532496'] = {"Victoria":0.22, "New South Wales":0.18, "Queensland":0.14, "Western Australia":0.10}  # Australian state first mainland H5N1
F['845372'] = {"Spain":0.18, "France":0.14}  # country airlift MT Marivex crew

# ============ TECH ============
F['338908'] = {"DeepSeek-V3.2":0.22, "DeepSeek-Lite":0.18, "DeepSeek-R1-Lite":0.14, "DeepSeek-V3-Lite":0.12, "DeepSeek-R2":0.10}  # DeepSeek faster/lower-cost model
F['297949'] = {"Claude Opus 5":0.22, "Claude Sonnet 5":0.18, "Claude 5":0.16, "Claude Opus 4.5":0.10, "Claude Fable":0.08}  # Anthropic newest Claude designation
F['268355'] = {"Starbase":0.22, "Hawthorne":0.16, "McGregor":0.12, "Cape Canaveral":0.10}  # SpaceX facility Anthropic Claude computing
F['602042'] = {"SPACE":0.28, "SPX":0.18, "SPACEX":0.14, "SXPX":0.10, "X":0.08}  # SpaceX Nasdaq ticker
F['398458'] = {"Livermore":0.22, "Oak Ridge":0.16, "Beijing":0.12, "Tokyo":0.08, "Stuttgart":0.06}  # TOP500 #1 location (El Capitan-Livermore)
F['871230'] = {"El Capitan":0.20, "Frontier":0.18, "Aurora":0.14, "Fugaku":0.10, "Lumi":0.08}  # TOP500 #2 supercomputer
F['724161'] = {"GR00T N1":0.22, "GR00T":0.18, "Isaac GR00T":0.12, "Nova":0.08}  # Nvidia humanoid robot reference design
F['846313'] = {"Windows":0.30, "Ubuntu":0.16, "NVIDIA OS":0.12, "Linux":0.10}  # OS for RTX Spark AI PCs
F['657629'] = {"Telegram":0.22, "Signal":0.18, "WhatsApp":0.14, "Discord":0.08}  # messaging app India blocks
F['843409'] = {"Te Doy Mi Vida":0.10}  # Shakira WC song title (uncertain)
F['412040'] = {"Tayfun":0.18, "Gokbuke":0.12}  # Türkiye first ICBM prototype SAHA (uncertain)

# ============ SCOTUS / LEGAL ============
F['910286'] = {"John Roberts":0.18, "Brett Kavanaugh":0.16, "Amy Coney Barrett":0.12, "Samuel Alito":0.10}  # SCOTUS Section 2 redistricting opinion
F['620859'] = {"John Roberts":0.18, "Brett Kavanaugh":0.14, "Elena Kagan":0.12, "Amy Coney Barrett":0.10}  # SCOTUS Damon Landor opinion
F['893892'] = {"Brett Kavanaugh":0.16, "John Roberts":0.14, "Samuel Alito":0.12, "Clarence Thomas":0.10}  # SCOTUS Roundup opinion
F['333674'] = {"John Roberts":0.16, "Brett Kavanaugh":0.14, "Samuel Alito":0.12, "Sonia Sotomayor":0.10}  # SCOTUS Muk Choi Lau opinion
F['844962'] = {"United States":0.40, "Texas":0.30}  # SCOTUS sides with (federal firearm ban)
F['351470'] = {"9th Circuit":0.20, "5th Circuit":0.16, "2nd Circuit":0.12, "4th Circuit":0.10, "DC Circuit":0.08}  # federal appeals court release order
F['937942'] = {"2nd Circuit":0.20, "Supreme Court":0.16, "DC Circuit":0.12, "3rd Circuit":0.08}  # court Khalil detention challenge
F['48174'] = {"District of Columbia":0.18, "Eastern District of Virginia":0.14, "Southern District of Florida":0.10}  # Kash Patel lawsuit district
F['383542'] = {"New York":0.18, "Delaware":0.14, "California":0.12, "Florida":0.08}  # Justin Sun lawsuit state
F['890247'] = {"New York":0.16, "Florida":0.12, "Virginia":0.10, "New Jersey":0.08}  # James Comey case state
F['934727'] = {"Tanya Chutkan":0.14, "James Boasberg":0.10}  # federal judge anti-weaponisation injunction (uncertain)
F['136074'] = {"Jay Clayton":0.16, "Andrew Giuliani":0.12, "Marc Mukasey":0.10}  # attorney Manhattan top fed prosecutor
F['186080'] = {"Esteban Isaias":0.10}  # returned to US Medicare fraud (uncertain)
print("batch4a appended")

# ============ ORGANIZATIONS / COUNTRIES / MISC (FINAL BATCH) ============
F['578115'] = {"World Economic Forum":0.18, "McKinsey":0.14, "Goldman Sachs":0.12, "IMF":0.10, "OECD":0.08}  # org AI jobs survey
F['487623'] = {"Pakistan":0.18, "Lebanon":0.14, "Egypt":0.12, "Sri Lanka":0.10, "Kenya":0.08}  # country 8pm closing fuel crisis
F['146726'] = {"United Nations":0.18, "World Bank":0.12, "International Crisis Group":0.10}  # org Haftar loans investigation
F['85884'] = {"Ahmed Youssouf":0.14, "Aden Mohamed Abdillahi":0.10}  # Djibouti runner-up (uncertain)
F['199254'] = {"IOM":0.24, "UNHCR":0.20, "OCHA":0.14, "IMPACT":0.10}  # org displaced households survey
F['676856'] = {"Jens Stoltenberg":0.16, "Mark Rutte":0.14}  # who removes Spain from CIMIC (uncertain)
F['724016'] = {"Emam Ashour":0.16, "Mohamed Magdy":0.10}  # Egyptian Pro League suspension (uncertain)
F['390917'] = {"China":0.34, "India":0.18, "Russia":0.12, "Mexico":0.08}  # WADA target PED industry
F['225146'] = {"Lin Yu-ting":0.24, "Chen Nien-chin":0.16, "Wu Shih-yi":0.10}  # Taiwan boxer bronze 60kg Asian Boxing
F['58896'] = {"Lakurawa":0.20, "bandits":0.16, "ISWAP":0.12, "Ansaru":0.10}  # rebel group Jilli-axis airstrike
F['127767'] = {"Jair Bolsonaro":0.22, "Eduardo Bolsonaro":0.12}  # Brazil Fed Police investigate posts (defame Lula)
F['632512'] = {"Riyadh":0.16, "Doha":0.14, "Ankara":0.10, "Astana":0.08}  # city Ukraine-Syria presidents talks
F['443588'] = {"Marshall Islands":0.24, "Tuvalu":0.18, "Vanuatu":0.14, "Solomon Islands":0.10}  # Pacific emissions levy
F['390748'] = {"Steve Witkoff":0.22, "Morgan Ortagus":0.16, "Massad Boulos":0.12}  # US ME envoy praise Lebanese banker
F['702685'] = {"Tulkarm":0.22, "Nur Shams":0.18, "Jenin":0.16, "Balata":0.10}  # West Bank camp women inspections
F['591655'] = {"Saudi Arabia":0.18, "United Arab Emirates":0.14, "India":0.12, "Qatar":0.08}  # country US defence partnership
F['182480'] = {"Yvette Cooper":0.20, "Keir Starmer":0.16, "Shabana Mahmood":0.10}  # fast-track UK anti-Semitism law
F['532929'] = {"Gerber":0.18, "Aptamil":0.12, "Heinz":0.10, "Hipp":0.08}  # baby-food recall rat poison
F['306024'] = {"Nigeria":0.18, "Brazil":0.14, "Ecuador":0.10, "Angola":0.08, "Iraq":0.08}  # country leave OPEC+OPEC
F['901922'] = {"FTC":0.34, "DOJ":0.26, "Federal Communications Commission":0.10}  # agency NFL anticompetitive
F['735244'] = {"Scattered Spider":0.14, "LockBit":0.12, "Anonymous":0.10, "Killnet":0.08}  # group Canvas cyberattack
F['601987'] = {"New York Post":0.16, "Breitbart":0.12, "Wall Street Journal":0.10, "The Atlantic":0.08}  # newspaper Trump-Meloni interview
F['108214'] = {"ABC":0.18, "CBS":0.14, "NBC":0.12, "Comedy Central":0.10}  # broadcaster FCC late-night WHCD
F['142723'] = {"Cyprus":0.18, "Greece":0.16, "Malta":0.12, "Egypt":0.10}  # coast Israel intercept Sumud Flotilla
F['233086'] = {"RIMPAC":0.24, "Cobra Gold":0.16, "African Lion":0.12, "Talisman Sabre":0.08}  # exercise missing US service members
F['743215'] = {"El Nino":0.34, "La Nina":0.24, "Indian Ocean Dipole":0.10}  # Pacific climate pattern WMO alert
F['46784'] = {"Home Office":0.30, "Foreign Office":0.16, "Cabinet Office":0.10}  # UK dept vetting Washington envoy
F['64633'] = {"Massad Boulos":0.20, "Marco Rubio":0.16, "Mauricio Claver-Carone":0.12}  # oversee US Venezuela plan
F['9330'] = {"European Commission":0.24, "European External Action Service":0.20, "European Council":0.12}  # EU institution Art 42.7 blueprint
F['185413'] = {"Washington":0.20, "Camp David":0.16, "Riyadh":0.10, "Doha":0.08}  # Israel-Lebanon leaders invited
F['268214'] = {"Fratelli Tutti":0.0, "Pacem in Terris":0.12, "Dilexit Nos":0.0, "Caritas in Veritate":0.0}  # Pope Leo XIV encyclical (guess peace theme)
F['253961'] = {"Viktor Orban":0.24, "Emmanuel Macron":0.16, "Olaf Scholz":0.12, "Friedrich Merz":0.10}  # Putin preferred European counterpart
F['439122'] = {"United States":0.16, "Russia":0.12}  # defendant coalition challenge (uncertain)
F['723846'] = {"Odesa":0.28, "Chornomorsk":0.22, "Yuzhne":0.14, "Mykolaiv":0.10}  # Ukrainian port cargo vessel
F['672865'] = {"China":0.16, "India":0.12, "South Africa":0.10}  # shadow-fleet tanker heading (uncertain)
F['259295'] = {"Brazil":0.16, "Argentina":0.12, "United States":0.12, "China":0.10}  # country Bolivia humanitarian airlift
F['34500'] = {"St Peter's Square":0.34, "St John Lateran":0.12}  # square Pope Leo XIV Sunday Mass
F['88868'] = {"Morocco":0.12, "Algeria":0.10}  # national team warm-up vs Chile cancelled (uncertain)
F['686516'] = {"House of Representatives":0.50, "Senate":0.30}  # chamber $70bn ICE funding first pass
F['444151'] = {"Zinedine Zidane":0.26, "Carlo Ancelotti":0.22, "Jose Mourinho":0.12}  # manager Perez bring back Real Madrid
F['569488'] = {"Tedros Adhanom":0.20, "Hans Kluge":0.14}  # WHO official MV Hondius evacuation
F['194143'] = {"Saudi Arabia":0.20, "United Arab Emirates":0.16, "United Kingdom":0.10, "Japan":0.08}  # country $5bn India ties
F['518119'] = {"Ramesh Lekhak":0.12}  # Nepal home minister resign (uncertain)
F['797135'] = {"Nayib Bukele":0.16, "Bernardo Arevalo":0.12}  # inauguration Herzog attends Central America (uncertain)
F['22859'] = {"Denmark":0.12, "France":0.10, "Norway":0.10, "Sweden":0.08}  # Modi visit after Netherlands
F['599425'] = {"Marco Rubio":0.18, "Brian Nichols":0.12, "Mike Pompei":0.0}  # US delegation Havana security talks
F['751763'] = {"Mexico":0.26, "Colombia":0.18, "Ecuador":0.12, "Bolivia":0.08}  # country deny US drug ops authorization
F['720775'] = {"WFP":0.22, "UNHCR":0.16, "UNICEF":0.12, "WHO":0.10}  # org Trump humanitarian funding
F['247231'] = {"Gnanasara Thero":0.14}  # Sri Lanka temple abuse custody (uncertain)
F['51685'] = {"Japan Rugby Football Union":0.24, "Rugby Australia":0.18, "World Rugby":0.12}  # rugby org suspend Eddie Jones
F['460485'] = {"Ali Day":0.0, "Muhammad Ali Day":0.24, "Day of the Greatest":0.16, "World Boxing Day":0.12}  # global observance Ali anniversary
F['713763'] = {"Helge Lund":0.16}  # BP interim chair (uncertain)
F['687584'] = {"Russia":0.24, "Iran":0.18, "North Korea":0.10}  # delegation absent FIFA Congress (turned back)
F['130521'] = {"Iraq":0.24, "Saudi Arabia":0.20, "United Arab Emirates":0.16, "United States":0.12}  # India 3rd crude supplier
F['354245'] = {"Germany":0.16, "United Kingdom":0.14, "France":0.10, "Spain":0.08}  # largest % increase Chinese EV imports
F['972370'] = {"Pete Hegseth":0.16, "Howard Lutnick":0.12, "Marco Rubio":0.10}  # cabinet official UFC agreement
F['76517'] = {"Maryam Nawaz":0.20, "Hamza Shehbaz":0.12}  # Dynasty money-laundering remand (uncertain)
F['580096'] = {"Imran Khan":0.20, "Bilawal Bhutto Zardari":0.12, "Omar Ayub":0.10}  # Pakistani leader meet Shehbaz
F['464071'] = {"Washington Hilton":0.34, "Washington Convention Center":0.16}  # rescheduled WHCD location
F['479187'] = {"Boeing E-7 Wedgetail":0.34, "Saab Globaleye":0.20, "Bombardier Global 6000":0.10}  # Canada early-warning aircraft
F['429893'] = {"Naqoura":0.20, "Ras al-Naqoura":0.14, "Beirut":0.10}  # Israel-Lebanon military talks location
F['416791'] = {"Wang Yi":0.30, "Han Zheng":0.18, "Shen Mingming":0.08}  # present China white paper
F['625905'] = {"Rami Abdulrahman":0.12}  # released Mousa al-Omar complaint (uncertain)
F['494514'] = {"Hamas":0.30, "Palestinian Islamic Jihad":0.20, "Popular Front":0.08}  # armed group tunnel Gaza ceasefire
F['483550'] = {"China":0.16, "Japan":0.12, "India":0.10, "Russia":0.08}  # country diplomat dead Yangon
F['710526'] = {"United States":0.24, "European Union":0.18, "India":0.12, "Iran":0.08}  # Armenia strategic partner
F['585196'] = {"Israel Katz":0.16, "Herzi Halevi":0.12, "Avichai Mandelblit":0.0}  # Knesset burden on forces (uncertain)
F['388712'] = {"F-16":0.24, "A-10":0.20, "F-15":0.16, "F-35":0.08}  # 2 fighter models US reduce NATO
F['710687'] = {"South Africa":0.24, "Egypt":0.18, "Morocco":0.14, "Nigeria":0.08}  # Africa Industrialisation Index #1
F['314569'] = {"Kazakhstan":0.16, "Russia":0.12, "France":0.10, "Serbia":0.08}  # country Xi visit June 8-9
F['240927'] = {"Tulsi Gabbard":0.20, "Richard Grenell":0.16}  # acting DNI
F['845664'] = {"UNRWA":0.24, "Francesca Albanese":0.16, "Antonio Guterres":0.10}  # Israel sever ties UN report
F['648564'] = {"Nigeria":0.22, "Zimbabwe":0.18, "Mozambique":0.12, "Malawi":0.10}  # first repatriate from South Africa
F['782824'] = {"Bill Owens":0.12}  # CBS 60 Minutes EP (uncertain)
F['151195'] = {"DP World":0.24, "Maersk":0.20, "MSC":0.16, "CMA CGM":0.10}  # shipping group Mombasa terminal
F['891597'] = {"China":0.18, "Saudi Arabia":0.12, "United Arab Emirates":0.10}  # country Indonesia thanks repatriation
F['669987'] = {"Abu Musa":0.28, "Greater Tunb":0.20, "Lesser Tunb":0.14, "Larak":0.10}  # Iranian island US strike
F['995497'] = {"Yongin":0.18, "Pyongtaek":0.16, "Cheongju":0.08}  # South Korea chip-packaging cluster
F['570913'] = {"Philippines":0.16, "Indonesia":0.12, "Bangladesh":0.10}  # consul Libyan released campaigners (uncertain)
F['420274'] = {"Marjorie Taylor Greene":0.12}  # US rep resign calls (uncertain)
F['696982'] = {"Nepal":0.24, "Bangladesh":0.18, "China":0.14, "Pakistan":0.10, "Myanmar":0.08}  # neighbor border India demolish
F['154721'] = {"Ministry of Oil":0.18, "Ministry of Electricity":0.14, "Ministry of Defence":0.10}  # Iraqi ministry corruption
F['724156'] = {"C-63":0.18, "C-11":0.12, "C-18":0.10}  # Canada bill social-media/AI safety
F['577124'] = {"Bad Bunny":0.18, "Drake":0.14, "Kendrick Lamar":0.12, "J Balvin":0.10}  # rapper WC ceremony Katy Perry
F['417035'] = {"Model Y":0.26, "Model 3":0.22, "Cybertruck":0.16, "Model S":0.10}  # Tesla model Texas crash
F['255123'] = {"Najah al-Sudani":0.0, "Mohammed Shia al-Sudani":0.20}  # PMF disengage political (uncertain)
F['86424'] = {"Shanghai":0.26, "Hong Kong":0.20, "Guangzhou":0.14, "Chengdu":0.08}  # UK FS after Beijing
F['689275'] = {"Texas":0.18, "Arizona":0.16, "Florida":0.10, "California":0.08}  # state 15 charged impeding immigration
F['964578'] = {"Kuryu Matsuki":0.12, "Rindo Taguchi":0.10}  # youngest Japan WC squad (uncertain)
F['879727'] = {"Mahmoud Abbas":0.24, "Hussein al-Sheikh":0.18, "Jibril Rajoub":0.12, "Marwan Barghouti":0.08}  # Fatah Central Committee
F['368900'] = {"Poland":0.22, "Czech Republic":0.16, "Germany":0.12, "Slovakia":0.08}  # country tighten Ukrainian refugee rules
F['494681'] = {"United Kingdom":0.24, "France":0.20, "Norway":0.12, "Denmark":0.08}  # country seize Russian tanker English Channel
F['2693'] = {"MetLife Stadium":0.14, "SoFi Stadium":0.10}  # WC venue resales capped (uncertain)
F['32938'] = {"United States":0.16, "Saudi Arabia":0.12, "United Arab Emirates":0.10}  # country India oil reserves deal Modi
F['125200'] = {"Syria":0.16, "Sudan":0.12, "Lebanon":0.08}  # government reforms before aid (uncertain)
F['487686'] = {"Steve Witkoff":0.16, "Marco Rubio":0.12, "Massad Boulos":0.10}  # US official Lebanon deconfliction
F['456839'] = {"Munich":0.16, "Frankfurt":0.14, "Berlin":0.12, "Hamburg":0.08}  # German arrest Kazakhstan spy
F['515929'] = {"Najib Razak":0.12}  # Malaysia regulator account (uncertain)
F['346479'] = {"Chile":0.16, "United States":0.14, "Mexico":0.10, "Japan":0.08}  # host FIFA U-15 World Cup
F['531981'] = {"State Department":0.20, "DOJ":0.14, "DHS":0.10}  # US body two-tiered policing post
F['424035'] = {"Pam Bondi":0.40}  # sign DOJ directive tax claims Trump
F['259778'] = {"Bassirou Diomaye Faye":0.28}  # lead Senegal welcome pardoned supporters
F['244068'] = {"England":0.20, "Brazil":0.16, "France":0.12, "Germany":0.08}  # national team €418m left-out players
F['768170'] = {"The Hague":0.16, "Brussels":0.12, "Vilnius":0.08}  # NATO summit military mission signal
F['85916'] = {"Chelsea":0.34, "Arsenal":0.16, "Lyon":0.10}  # Sam Kerr club through 2030 (she's at Chelsea)
F['473041'] = {"Sonko":0.18, "Faye":0.14, "Diop":0.10, "Ndiaye":0.08}  # Senegal PM surname
F['276195'] = {"Santiago Pena":0.14, "Javier Milei":0.12, "Bukele":0.10}  # head of state travel LA USA-Paraguay
F['235729'] = {"Jonathan David":0.30, "Cyle Larin":0.24, "Tajon Buchanan":0.12, "Alphonso Davies":0.08}  # Canada first WC goal home
F['434096'] = {"Mia Mottley":0.24, "Philip Pierre":0.12}  # head of state reparatory justice bodies (CARICOM)
F['727356'] = {"Kahleah Copper":0.14}  # Phoenix Mercury suspension (uncertain)
F['529663'] = {"Ferdinand Marcos Jr":0.30, "Sara Duterte":0.12}  # order investigation Philippine school shooting
F['823927'] = {"United Kingdom":0.18, "France":0.16, "Germany":0.12, "Norway":0.08}  # country backstop G7 Ukraine air defence
F['844193'] = {"Doha":0.14, "Rabat":0.10, "Tunis":0.08}  # DRC pre-World Cup training camp (uncertain)
F['273832'] = {"EPA":0.26, "DOJ":0.22, "DOE":0.10}  # agency dismiss xAI data center lawsuit
F['813894'] = {"Liverpool":0.20, "Tottenham Hotspur":0.16, "Chelsea":0.12, "Manchester City":0.08}  # Anthony Gordon club
F['539593'] = {"Mbandaka":0.18, "Goma":0.14, "Bukavu":0.10}  # Africa CDC DRC Ebola city
F['904017'] = {"United Airlines":0.16, "Delta Air Lines":0.12, "Southwest Airlines":0.10}  # airline Geoffrey Wall licensing
F['709621'] = {"Mohamed Abdullahi Farmajo":0.24, "Sharif Sheikh Ahmed":0.20, "Hassan Sheikh Mohamud":0.10}  # former Somali president protest
F['787625'] = {"Saudi Arabia":0.16, "Qatar":0.12, "Egypt":0.08}  # countries joint peace fund Israel-Palestine (multi)
F['786553'] = {"Peter Kyle":0.20, "Keir Starmer":0.16, "Lisa Nandy":0.10}  # announce Britain under-16 social-media ban
F['105885'] = {"Colombia":0.14, "Brazil":0.10}  # two countries rescue Venezuelan quake survivor (multi, uncertain)
print("batch4b appended")
