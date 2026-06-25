#!/usr/bin/env python3
"""Daily article scanner: greps the newest articles for keywords tied to open questions.
Usage: python3 memory/daily_scan.py YYYY/MM/DD [extra keywords...]
Prints headline + matching keyword + snippet for review."""
import json, sys, glob, re

KEYWORDS = [
    # Jan resolvers
    ('Chelsea', 'head coach|sack|appoint|Maresca'),
    ('Ukraine', 'defence minister|defense minister|economic adviser|Oreshnik|Poroshenko|embassy.*damag'),
    ('Venezuela', 'interim president|sworn in|Maduro|Starlink|Delcy|Machado|Gonzalez'),
    ('Greenland', 'meeting|Rubio|Landry|mission|framework|Arctic'),
    ('AFCON', 'quarter|semi|knock|eliminat|penalty|calf'),
    ('measles', '\\d+ cases'),
    ('Nipah', 'Kerala|case'),
    ('Grok', 'ban|block'),
    ('carrier', 'Middle East|divert|Washington|Ford|Lincoln|Nimitz|Vinson'),
    ('Iran', 'protest|police killed|security personnel|complex|concrete|talks|Oman|wrestler|execution'),
    ('Syria', 'Aleppo|SDF|Kurdish|national language|Nowruz|Shaddadi|Raqqa|Tabqa|Deir Hafer|Maskana'),
    ('Somalia', 'agreement|sever|Ethiopia|UAE|separatist'),
    ('Yemen', 'Alimi|military|command|integrate'),
    ('Thailand', 'NIDA|poll|election'),
    ('Bangladesh', 'election|T20|World Cup|withdraw|replace|Jamaat|NCP'),
    ('TikTok', 'CEO|joint venture'),
    ('T20 World Cup', 'Bangladesh|boycott|Pakistan|move|Sri Lanka'),
    ('Australian Open', 'draw|first round|Venus|Sabalenka|Alcaraz|Sinner|Osaka|Sonmez'),
    ('Brisbane International', 'final|Sabalenka'),
    ('Portugal', 'presidential|Ventura|runoff|run-off'),
    ('Bulgaria', 'president|Radev|Iotova'),
    ('Minneapolis', 'shooting|agent|ICE|CBP|operation'),
    ('immigration', 'crackdown|operation|largest'),
    ('Epstein', 'Lutnick|Commerce|correspondence'),
    ('Oscar', 'nomination'),
    ('Grammy', 'Album of the Year'),
    ('UFC', 'Hall of Fame'),
    ('Fury', 'opponent|April'),
    ('Guehi', 'agreed|sign|deal'),
    ('Manchester United', 'Amorim|Carrick|interim|sacked'),
    ('Deloitte', 'Money League'),
    ('Champions League', 'playoff draw|round of 16|drawn'),
    ('Carabao', 'semi|final'),
    ('Oreshnik', '.'),
    ('Charlotte', 'plot|attack|FBI'),
    ('Austrian', 'ski|ruled out|crash'),
    ('Starlink', 'free'),
    ('armada', '.'),
    ('Massie', 'oil|Venezuela'),
    ('trade deficit', 'double'),
    ('basketball', 'rigging|fixing|league'),
    ('Betar', '.'),
    ('Washington Post', 'publisher|Lewis'),
    ('Norway', 'corruption|prime minister'),
    ('Harden', 'trade'),
    ('IAEA', 'special|meeting|request'),
    ('Gripen|Mirage|F-16', 'Ukraine'),
    ('Kosovo|playoff', 'World Cup'),
    ('NIDA', '.'),
    ('Crans-Montana', '.'),
    ('Sudan', 'siege|Babanusa|El Obeid|hospital|drone.*market'),
    ('Colombia', 'peace talks|ELN'),
    ('Mali', 'parties|dissolv'),
    ('Indonesia', 'plane|missing|surveillance'),
    ('Karachi', 'fire'),
    ('Spain', 'train|collision'),
    ('New Zealand', 'landslide'),
    ('Lukashenko', 'visit'),
    ('IQAir', '.'),
    ('Board of Peace', '.'),
    ('Qatar', 'peace body|invited'),
]

def main(date_path, extra):
    files = glob.glob(f'articles/{date_path}/articles.jsonl')
    if not files:
        print('no files for', date_path); return
    kws = KEYWORDS + [(k, '.') for k in extra]
    seen = set()
    for fp in files:
        with open(fp) as f:
            for line in f:
                try: a = json.loads(line)
                except: continue
                t = a.get('title','') or ''
                c = a.get('content','') or ''
                text = t + ' ' + c
                for kw, pat in kws:
                    if re.search(kw, text, re.I) and re.search(pat, text, re.I):
                        key = (t[:60], kw)
                        if key in seen: continue
                        seen.add(key)
                        m = re.search(kw, text, re.I)
                        s = max(0, m.start()-150)
                        print(f'## [{kw}] {t[:110]}')
                        print('   ', text[s:m.start()+350].replace(chr(10),' ')[:480])
                        print()
                        break

if __name__ == '__main__':
    date_path = sys.argv[1] if len(sys.argv) > 1 else '2025/12/24'
    main(date_path, sys.argv[2:])
