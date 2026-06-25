# Forecasting Memory — Al Jazeera Q1 2026 Market

## SIM SETUP
- Sim date starts **2025-12-24**. 330 questions, all open-ended string answers, resolve Jan–Mar 2026.
- Articles in articles/YYYY/MM/DD/. New ones appear daily as sim advances.
- Predictions PERSIST across days until I change them. So: predict ALL questions ASAP (time-weighted), refine daily.

## SCORING MODEL (critical)
- BSS = 1 - Σ(p_i - y_i)² over outcomes; TRUE outcome ALWAYS counted (range -1..+1).
- If true answer in my list: 1 - Σ(p_i-y_i)². If NOT in list: score = -Σp_i² (mild if probs low).
- Proper scoring → report calibrated probs. Leave unallocated mass for "other" (don't force sum=1).
- For unpredictable specific-event Qs: list 2-4 plausible candidates at LOW/modest probs to cap downside.
- Strategy: high-confidence Qs → strong dist now. Unknowable Qs → low-conf guess now, sharpen when article appears near resolution.

## WORLD MODEL as of 2025-12-24
### Iran/Israel: NO active war, but RISING risk. Netanyahu (Dec20-22) pushing Trump for fresh strikes on Iran (ballistic missile rebuild, nuclear reconstruction). IRGC missile drills alarm Israel. June 2025 "12-day war" already happened (Op Midnight Hammer, US bombed Iran nuclear sites). => Large Iran-war Q cluster (HIMARS, Tehran strikes, Gulf refineries, US troops killed, Israeli town missile deaths) is SPECULATIVE round-2; meaningful prob but NOT certain. Modest confidence, sharpen as news arrives.
### Venezuela: Maduro under max US pressure (Caribbean buildup, strikes on boats ~80+ killed, tanker seizures, $50M bounty, family sanctions Dec19). Machado (Nobel) = US favorite; Edmundo González = claimed election winner. No transition yet. Q651727 interim president: if Maduro falls → González or Machado.
### Ukraine-Russia: ACTIVE peace talks Miami/Florida Dec20-22 (Witkoff, Kushner, Umerov, Dmitriev). Trilateral proposed. Possible deal momentum.
### NFL (SB LX Feb 8 @ Levi's): AFC seeds: 1 Denver(12-3),2 NE Patriots(12-3),3 Jax(11-4),4 Pittsburgh,5 LAChargers(11-4),6 Buffalo(11-4),7 Houston. NFC: 1 Seattle(12-3),2 Chicago(10-4),3 Philadelphia(9-5),4 TampaBay,5 LA Rams(11-4),6 SF49ers(10-4),7 GreenBay. Mahomes torn ACL, Chiefs OUT. Playoffs: WC Jan10-12, Div Jan17-18, Conf Champ Jan25, SB Feb8.
  - NFC QBs: Seattle=Sam Darnold, Rams=Stafford, Eagles=Hurts, Packers=Love, Bears=Caleb Williams, 49ers=Purdy, Bucs=Mayfield.
### AFCON 2025 (Morocco): Groups A Morocco/Mali/Zambia/Comoros; B Egypt/SA/Angola/Zim; C Nigeria/Tunisia/Uganda/Tanzania; D Senegal/DRCongo/Benin/Botswana; E Algeria/BurkinaFaso/EqGuinea/Sudan; F IvoryCoast/Cameroon/Gabon/Mozambique. Group stage ends Dec31, R16 Jan3, final Jan18 Rabat. Q799398 BG implies FINAL = Morocco vs Senegal (so Senegal wins their half).
### Bangladesh election Feb12 2026: BNP frontrunner (most seats), Jamaat-e-Islami 2nd, NCP 3rd. Awami League BANNED. Nominations Dec29, campaign from Jan22. => Q304287 main opposition likely Jamaat-e-Islami.
### Grammys Feb1 2026: AOTY nominees: Bad Bunny(DTMF), Clipse, Bieber(Swag), Kendrick(GNX), Lady Gaga(Mayhem), Leon Thomas(Mutt), Sabrina Carpenter(Man's Best Friend), Tyler(Chromakopia). Kendrick frontrunner(9 noms), Gaga 2nd, Bad Bunny strong.
### Chelsea: Maresca under pressure but "committed", contract to 2029. No appointment likely by Jan31 (Q165622 may void / low conf).

## TODO / OPEN
- Oscars 2026 (Jan22 noms): need frontrunners. Q886103 says a film gets RECORD 16 noms (all-time record is 14!) — distinctive.
- Men's UCL league phase standings + playoff draw (~late Jan) for 85609/35131/55999/261538.
- Tennis AO "who faces X round Y" — draw out ~Jan 8; unknowable now, sharpen post-draw.
