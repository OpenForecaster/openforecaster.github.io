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
