# Forecast notes - 2026-01-09

State/market:
- `state.json` was absent again.
- `market.csv` had 330 rows: 299 active, 31 resolved, and no active questions without a current prediction.
- New resolutions seen in the market snapshot included `45659` = Indonesia, `459037` = Nigeria, `46876` = Taiwan, `797906` = Supreme Military Committee, and `891998` = Marta Kostyuk.

Calibration lessons:
- Country bans/regulatory questions can jump to countries that appear only in follow-up legal/regulatory reporting; leave some room for Indonesia-style late entrants.
- Tennis draw questions need wider draw/opposite-half coverage. The Kostyuk miss was too narrow.
- Official body-name questions punish semantic closeness. Include exact phrases from reporting, not only paraphrases.

Jan 9 evidence and updates:
- `69214`: Iran reporting now gives a specific Lordegan, Chaharmahal and Bakhtiari clue: Fars said gunmen killed two security force members and wounded 30 others there. Moved top probability from Ilam to Chaharmahal and Bakhtiari, with Lorestan/Ilam/Kermanshah still live.
- `80352`: Fox reporting tied the Jan. 30 funding fight directly to ICE and the Homeland Security bill. Raised Department of Homeland Security sharply.
- `806810`: Reuters/Straits and Al Jazeera describe the Board of Peace overseeing a committee of Palestinian technocrats. Shifted top weight to Palestinian Technocratic Committee / Technocratic Committee rather than the Board itself.
- `71`: Mladenov met Hussein al-Sheikh in Ramallah about Gaza implementation, with no Abbas meeting expected. Moved al-Sheikh above Mohammad Mustafa but kept the distribution moderate.
- `943026`: Grok limited image generation/editing on X to paid subscribers after backlash, with EU/UK/Ireland scrutiny increasing. Raised Grok again.
- `474377` and `16281`: Sky/Independent say Ole Gunnar Solskjaer will hold in-person talks Saturday, Carrick has already met leadership, and Solskjaer/Carrick remain front-runners. Raised Ole, left Carrick substantial, and nudged Man City lower in the linked "next team" market.
- `974205`, `904367`, `756891`: Reuters/Al Jazeera report renewed fighting in Aleppo's Sheikh Maksoud/Ashrafiyah after Kurdish groups rejected withdrawal terms. Raised Aleppo and gave PKK/YPG a bit more room for the short-name group question because Syrian official media frames SDF as PKK terrorists.
- `599463`: Minnesota/ICE reporting still points most strongly to Tim Walz for the DOJ governor question. Raised Walz slightly.
- `118127`: Jan 9 reporting says Chinese, Russian and Iranian warships arrived in South Africa, UAE ships were expected, and Indonesia/Ethiopia/Brazil would send observers. No explicit exclusion report found. Reduced Russia/China-style stale weight and moved diffuse probability to remaining BRICS non-participants India/Egypt/Saudi Arabia plus small Israel/Iran.

Questions left mostly unchanged:
- `291796`: no new useful Nipah evidence; Kerala remains the default.
- `934187`: no new NIDA prime-minister survey evidence found.
- `214384`: ICE action continued nationally, but I did not find a new official northeastern-state crackdown replacing New York.
- Australian Open/Venus opponent questions still lack draw-specific evidence as of Jan 9.
