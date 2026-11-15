#!/usr/bin/env python3
"""usage: grep_articles.py DATE_DIR(YYYY/MM/DD or 'all') PATTERN [maxn] [ctx]"""
import json, re, sys, glob
d = sys.argv[1]; pat = sys.argv[2]
maxn = int(sys.argv[3]) if len(sys.argv) > 3 else 8
ctx = int(sys.argv[4]) if len(sys.argv) > 4 else 300
files = sorted(glob.glob('/agent/workspace/articles/*/*/*/articles.jsonl')) if d == 'all' else [f'/agent/workspace/articles/{d}/articles.jsonl']
n = 0
for fn in files:
    for line in open(fn):
        a = json.loads(line)
        txt = (a.get('title') or '') + ' || ' + (a.get('content') or '')
        m = re.search(pat, txt, re.I)
        if m:
            s = max(0, m.start()-ctx); e = min(len(txt), m.end()+ctx)
            print('##', a.get('date_publish'), a.get('source'), (a.get('title') or '')[:120])
            print('   ', txt[s:e].replace('\n', ' '))
            n += 1
            if n >= maxn: sys.exit(0)
print(f'[{n} matches]')
