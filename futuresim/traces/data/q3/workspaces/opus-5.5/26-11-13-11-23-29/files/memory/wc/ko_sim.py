#!/usr/bin/env python3
"""World Cup 2026 knockout simulator. Edit R32 pairings + ELO, run: python3 ko_sim.py [nsims]
Match numbers follow FIFA: R32 73-88, R16 89-96, QF 97-100, SF 101-102, 3rd 103, F 104."""
import random, sys, collections, json
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
ELO = json.load(open('/agent/workspace/memory/wc/elo.json'))
R32 = json.load(open('/agent/workspace/memory/wc/r32.json'))  # {"73": ["A","B"], ...} use team names; "W73" refs for later rounds
HOSTS = {"United States": "US", "Mexico": "MX", "Canada": "CA"}
# venue country for each match (for host advantage)
VENUE = {73:"US",74:"US",75:"MX",76:"US",77:"US",78:"US",79:"MX",80:"US",81:"US",82:"US",83:"CA",84:"US",85:"CA",86:"US",87:"US",88:"US",
         89:"US",90:"US",91:"US",92:"MX",93:"US",94:"US",95:"US",96:"CA",97:"US",98:"US",99:"US",100:"US",101:"US",102:"US",103:"US",104:"US"}
R16 = {89:(74,77),90:(73,75),91:(76,78),92:(79,80),93:(83,84),94:(81,82),95:(86,88),96:(85,87)}
QF = {97:(89,90),98:(93,94),99:(91,92),100:(95,96)}
SF = {101:(97,98),102:(99,100)}
HOME_ADV = 100
import os.path
RESULTS = json.load(open('/agent/workspace/memory/wc/results.json')) if os.path.exists('/agent/workspace/memory/wc/results.json') else {}
import os
SHRINK = float(os.environ.get("SHRINK", "1.0"))
def p_adv(a, b, m):
    ra = ELO.get(a, 1700); rb = ELO.get(b, 1700)
    v = VENUE[m]
    if HOSTS.get(a) == v: ra += HOME_ADV
    if HOSTS.get(b) == v: rb += HOME_ADV
    return 1/(1+10**(-SHRINK*(ra-rb)/400))
def play(a, b, m):
    if str(m) in RESULTS:
        w = RESULTS[str(m)]
        return (a, b) if w == a else (b, a)
    return (a, b) if random.random() < p_adv(a, b, m) else (b, a)
cnt = collections.defaultdict(collections.Counter)
for _ in range(N):
    W = {}; L = {}
    for m, (a, b) in R32.items():
        w, l = play(a, b, int(m)); W[int(m)] = w; L[int(m)] = l
    for rnd in (R16, QF, SF):
        for m, (x, y) in rnd.items():
            w, l = play(W[x], W[y], m); W[m] = w; L[m] = l
    w3, _ = play(L[101], L[102], 103); W[103] = w3
    wf, lf = play(W[101], W[102], 104); W[104] = wf
    for m in list(R16) + list(QF) + list(SF) + [103, 104]:
        cnt[m][W[m]] += 1
    cnt['finalist'][W[101]] += 1; cnt['finalist'][W[102]] += 1
def top(m, k=8):
    return [(t, round(c/N, 3)) for t, c in cnt[m].most_common(k)]
for m in [97, 98, 99, 100, 101, 102, 103, 104, 'finalist']:
    print(m, top(m))
