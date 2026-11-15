import random, math, sys, itertools
from collections import defaultdict, Counter
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 1)
N = int(sys.argv[2]) if len(sys.argv)>2 else 20000
R = {'France':2095,'Spain':2075,'Argentina':2048,'England':2055,'Portugal':2000,'Brazil':2010,'Germany':1995,'Netherlands':1995,
'Norway':1950,'Colombia':1945,'Japan':1930,'Morocco':1925,'Croatia':1915,'Uruguay':1925,'Belgium':1905,'Switzerland':1885,'Ecuador':1890,
'USA':1910,'Mexico':1905,'Austria':1860,'Senegal':1850,'Canada':1830,'Paraguay':1830,'Sweden':1830,'Scotland':1790,'Iran':1790,
'South Korea':1790,'Australia':1770,'Algeria':1780,'Egypt':1790,'Ivory Coast':1800,'Czechia':1770,'Bosnia':1740,'Ghana':1730,
'Cape Verde':1700,'Saudi Arabia':1680,'Iraq':1690,'DR Congo':1740,'Uzbekistan':1720,'South Africa':1700,'New Zealand':1650,
'Haiti':1550,'Curacao':1600,'Qatar':1650,'Turkey':1870,'Tunisia':1700,'Jordan':1680,'Panama':1720}
groups = {
'A':['Mexico','South Korea','Czechia','South Africa'],'B':['Switzerland','Canada','Bosnia','Qatar'],
'C':['Brazil','Morocco','Scotland','Haiti'],'D':['USA','Australia','Paraguay','Turkey'],
'E':['Germany','Ivory Coast','Ecuador','Curacao'],'F':['Netherlands','Japan','Sweden','Tunisia'],
'G':['Egypt','Belgium','Iran','New Zealand'],'H':['Spain','Uruguay','Cape Verde','Saudi Arabia'],
'I':['France','Norway','Senegal','Iraq'],'J':['Argentina','Austria','Algeria','Jordan'],
'K':['Colombia','Portugal','DR Congo','Uzbekistan'],'L':['England','Ghana','Croatia','Panama']}
played = [ # (home, away, hg, ag)
('Mexico','South Africa',2,0),('South Korea','Czechia',2,1),('Mexico','South Korea',1,0),('Czechia','South Africa',1,1),
('Canada','Qatar',6,0),('Canada','Bosnia',1,1),('Switzerland','Bosnia',2,1),('Switzerland','Qatar',1,1),('Switzerland','Canada',2,1),('Bosnia','Qatar',3,1),
('Brazil','Morocco',1,1),('Scotland','Haiti',1,0),('Brazil','Haiti',3,0),('Morocco','Scotland',1,0),
('USA','Paraguay',4,1),('Australia','Turkey',2,0),('USA','Australia',2,0),('Paraguay','Turkey',1,0),
('Germany','Curacao',7,1),('Ivory Coast','Ecuador',1,0),('Germany','Ivory Coast',2,1),('Ecuador','Curacao',0,0),
('Netherlands','Japan',2,2),('Sweden','Tunisia',5,1),('Netherlands','Sweden',5,1),('Japan','Tunisia',4,0),
('Belgium','Egypt',1,1),('Iran','New Zealand',1,1),('Egypt','New Zealand',3,1),('Belgium','Iran',0,0),
('Spain','Cape Verde',0,0),('Saudi Arabia','Uruguay',1,1),('Spain','Saudi Arabia',4,0),('Uruguay','Cape Verde',2,2),
('France','Senegal',3,1),('Norway','Iraq',4,1),('France','Iraq',3,0),('Norway','Senegal',3,2),
('Argentina','Algeria',3,0),('Austria','Jordan',3,1),('Argentina','Austria',2,0),('Algeria','Jordan',2,1),
('Colombia','Uzbekistan',3,1),('Portugal','DR Congo',1,1),('Colombia','DR Congo',1,0),('Portugal','Uzbekistan',5,0),
('England','Croatia',4,2),('Ghana','Panama',1,0),('England','Ghana',0,0),('Croatia','Panama',1,0)]
remaining = [('Czechia','Mexico'),('South Africa','South Korea'),('Scotland','Brazil'),('Morocco','Haiti'),
('Turkey','USA'),('Paraguay','Australia'),('Ecuador','Germany'),('Curacao','Ivory Coast'),('Japan','Sweden'),('Tunisia','Netherlands'),
('Egypt','Iran'),('New Zealand','Belgium'),('Uruguay','Spain'),('Cape Verde','Saudi Arabia'),('Norway','France'),('Senegal','Iraq'),
('Argentina','Jordan'),('Algeria','Austria'),('Portugal','Colombia'),('DR Congo','Uzbekistan'),('England','Panama'),('Croatia','Ghana')]
# dead-rubber/rest adjustments (already-qualified teams resting)
rest = {('Argentina','Jordan'):('Argentina',-120),('Turkey','USA'):('USA',-80),('Ecuador','Germany'):('Germany',-90)}
def we(a,b):
    return 1/(1+10**(-(R[a]-R[b])/400))
def pois(l):
    L=math.exp(-l);k=0;p=1.0
    while True:
        p*=random.random()
        if p<L: return k
        k+=1
def match_goals(a,b,adj=0):
    w = 1/(1+10**(-(R[a]-R[b]+adj)/400))
    la = 1.3*math.exp(2.2*(w-0.5)); lb = 1.3*math.exp(-2.2*(w-0.5))
    return pois(la), pois(lb), la, lb
third_allowed = {74:'ABCDF',77:'CDFGH',79:'CEFHI',80:'EHIJK',81:'BEFIJ',82:'AEHIJ',85:'EFGIJ',87:'DEIJL'}
def rank_group(g, res):
    teams = groups[g]
    st = {t:[0,0,0] for t in teams} # pts, gd, gf
    for (a,b,x,y) in res:
        st[a][1]+=x-y; st[a][2]+=x; st[b][1]+=y-x; st[b][2]+=y
        if x>y: st[a][0]+=3
        elif x<y: st[b][0]+=3
        else: st[a][0]+=1; st[b][0]+=1
    def key_sort(ts):
        # group by points then h2h
        out=[]
        bypts = defaultdict(list)
        for t in ts: bypts[st[t][0]].append(t)
        for p in sorted(bypts, reverse=True):
            tied = bypts[p]
            if len(tied)==1: out+=tied; continue
            h = {t:[0,0,0] for t in tied}
            for (a,b,x,y) in res:
                if a in h and b in h:
                    h[a][1]+=x-y; h[a][2]+=x; h[b][1]+=y-x; h[b][2]+=y
                    if x>y: h[a][0]+=3
                    elif x<y: h[b][0]+=3
                    else: h[a][0]+=1; h[b][0]+=1
            tied.sort(key=lambda t:(h[t][0],h[t][1],h[t][2],st[t][1],st[t][2],random.random()), reverse=True)
            out+=tied
        return out
    order = key_sort(teams)
    return order, st
PL = {'Messi':('Argentina',5,0.42),'Mbappe':('France',4,0.42),'Haaland':('Norway',4,0.45),'Kane':('England',2,0.40),
'Oyarzabal':('Spain',2,0.28),'Undav':('Germany',3,0.22),'David':('Canada',3,0.35),'Ronaldo':('Portugal',2,0.30),'Vinicius':('Brazil',2,0.28),
'Lautaro/Alvarez':('Argentina',0,0.25),'Yamal':('Spain',1,0.15),'Dembele/Olise':('France',1,0.15),'Havertz':('Germany',1,0.20),'Gakpo/Depay':('Netherlands',2,0.25)}
G = {}
def credit(team, goals, factor=None):
    for p,(t,g0,sh) in PL.items():
        if t!=team or goals==0: continue
        s = sh*(factor.get(p,1.0) if factor else 1.0)
        k = sum(1 for _ in range(goals) if random.random()<s)
        G[p]+=k
def ko(a,b):
    x,y,la,lb = match_goals(a,b)
    credit(a,x); credit(b,y)
    if x!=y: return a if x>y else b
    x2=pois(la/3); y2=pois(lb/3); credit(a,x2); credit(b,y2)
    if x2!=y2: return a if x2>y2 else b
    return a if random.random()<0.5 else b
counts = defaultdict(Counter)
gb = Counter(); gbgoals=Counter()
for it in range(N):
    for p,(t,g0,sh) in PL.items(): G[p]=g0
    res = defaultdict(list)
    for (a,b,x,y) in played:
        g=[k for k,v in groups.items() if a in v][0]; res[g].append((a,b,x,y))
    for (a,b) in remaining:
        adj=0
        if (a,b) in rest:
            t,d = rest[(a,b)]; adj = d if t==a else -d
        x,y,_,_ = match_goals(a,b,adj)
        fac = {'Messi':0.55} if (a,b)==('Argentina','Jordan') else None
        credit(a,x,fac); credit(b,y,fac)
        g=[k for k,v in groups.items() if a in v][0]; res[g].append((a,b,x,y))
    first={};second={};third={};thirdst={}
    for g in groups:
        order, st = rank_group(g, res[g])
        first[g],second[g],third[g]=order[0],order[1],order[2]
        thirdst[g]=st[order[2]]
    best = sorted(groups, key=lambda g:(thirdst[g][0],thirdst[g][1],thirdst[g][2],random.random()), reverse=True)[:8]
    bestset=set(best)
    # random valid matching
    slots=list(third_allowed.keys())
    assign=None
    for _ in range(200):
        random.shuffle(slots)
        avail=set(bestset); a={}
        ok=True
        for s in slots:
            opts=[g for g in third_allowed[s] if g in avail]
            if not opts: ok=False;break
            g=random.choice(opts); a[s]=g; avail.remove(g)
        if ok: assign=a;break
    if assign is None:
        # brute force
        for perm in itertools.permutations(best):
            if all(perm[i] in third_allowed[s] for i,s in enumerate(sorted(third_allowed))):
                assign={s:perm[i] for i,s in enumerate(sorted(third_allowed))};break
    T=lambda s: third[assign[s]]
    W={}
    W[73]=ko(second['A'],second['B']); W[74]=ko(first['E'],T(74)); W[75]=ko(first['F'],second['C']); W[76]=ko(first['C'],second['F'])
    W[77]=ko(first['I'],T(77)); W[78]=ko(second['E'],second['I']); W[79]=ko(first['A'],T(79)); W[80]=ko(first['L'],T(80))
    W[81]=ko(first['D'],T(81)); W[82]=ko(first['G'],T(82)); W[83]=ko(second['K'],second['L']); W[84]=ko(first['H'],second['J'])
    W[85]=ko(first['B'],T(85)); W[86]=ko(first['J'],second['H']); W[87]=ko(first['K'],T(87)); W[88]=ko(second['D'],second['G'])
    W[89]=ko(W[74],W[77]); W[90]=ko(W[73],W[75]); W[91]=ko(W[76],W[78]); W[92]=ko(W[79],W[80])
    W[93]=ko(W[83],W[84]); W[94]=ko(W[81],W[82]); W[95]=ko(W[86],W[88]); W[96]=ko(W[85],W[87])
    W[97]=ko(W[89],W[90]); W[98]=ko(W[93],W[94]); W[99]=ko(W[91],W[92]); W[100]=ko(W[95],W[96])
    W[101]=ko(W[97],W[98]); W[102]=ko(W[99],W[100])
    L101 = W[98] if W[101]==W[97] else W[97]; L102 = W[100] if W[102]==W[99] else W[99]
    W[103]=ko(L101,L102); W[104]=ko(W[101],W[102])
    for m in (97,98,99,100,101,102,103,104): counts[m][W[m]]+=1
    mx = max(G.values()); top=[p for p in G if G[p]==mx]
    gb[random.choice(top)]+=1; gbgoals[mx]+=1
    counts['QF97a'][W[89]]+=1; counts['QF97b'][W[90]]+=1
    counts['QF100a'][W[95]]+=1; counts['QF100b'][W[96]]+=1
    counts['F1'][W[101]]+=1; counts['F2'][W[102]]+=1
    counts['1I'][first['I']]+=1; counts['1F'][first['F']]+=1; counts['1C'][first['C']]+=1; counts['1K'][first['K']]+=1; counts['1H'][first['H']]+=1; counts['1L'][first['L']]+=1; counts['1G'][first['G']]+=1
names={97:'Boston QF',98:'LA QF',99:'Miami QF',100:'KC QF',101:'SF1 Dallas',102:'SF2 Atlanta',103:'3rd place',104:'CHAMPION','QF97a':'Boston QF side A (W89)','QF97b':'Boston QF side B (W90)','QF100a':'KC side A (W95)','QF100b':'KC side B (W96)','F1':'Finalist SF1','F2':'Finalist SF2'}
for m in counts:
    top = counts[m].most_common(9)
    print(names.get(m,m), ' | '.join(f'{t} {c/N:.3f}' for t,c in top))

print('GOLDEN BOOT (named pool only):', ' | '.join(f'{p} {c/N:.3f}' for p,c in gb.most_common()))
print('winning tally dist:', sorted((k, round(v/N,3)) for k,v in gbgoals.items()))
