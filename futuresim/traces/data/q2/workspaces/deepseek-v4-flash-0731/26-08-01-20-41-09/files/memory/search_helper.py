import json, sys, re
ARTS_FILE = 'articles/2026/03/25/articles.jsonl'
with open(ARTS_FILE) as f:
    arts = [json.loads(l) for l in f]

def search(terms, maxhits=10, must_all=True, date_from=None, date_to=None):
    """Search locally over articles. terms: list of substrings (case-insens)."""
    hits = []
    for a in arts:
        blob = ((a.get('title') or '') + ' ' + (a.get('content') or '')).lower()
        dp = (a.get('date_publish') or '')[:10]
        if date_from and dp < date_from: continue
        if date_to and dp > date_to: continue
        ok = all(t.lower() in blob for t in terms) if must_all else any(t.lower() in blob for t in terms)
        if ok:
            hits.append(a)
            if len(hits) >= maxhits: break
    return hits

def show(hits, n=None):
    for a in (hits if n is None else hits[:n]):
        print(a.get('date_publish','')[:10], '|', a.get('source',''), '|', (a.get('title','') or '')[:120])
        # print first 300 chars of content
        c = (a.get('content') or '')
        if c: print('   ', c[:250].replace('\n',' '))
        print()

if __name__ == '__main__':
    terms = sys.argv[1:] or ['earthquake']
    show(search(terms))
