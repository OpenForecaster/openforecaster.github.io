#!/usr/bin/env python3
"""Compile all batch forecast JSONs into memory/all_forecasts.json and print a summary sorted by resolution date."""
import json, glob, csv, os, sys
rows = {r['qid']: r for r in csv.DictReader(open('/agent/workspace/market.csv'))}
allf = {}
for fn in sorted(glob.glob('/agent/workspace/memory/batches/batch_*_forecasts.json')):
    try:
        d = json.load(open(fn))
    except Exception as e:
        print("ERR", fn, e); continue
    b = os.path.basename(fn).replace('_forecasts.json','')
    for q, v in d.items():
        v['batch'] = b
        allf[str(q)] = v
# overrides from my own later updates
ov = '/agent/workspace/memory/overrides.json'
if os.path.exists(ov):
    for q, v in json.load(open(ov)).items():
        allf.setdefault(q, {}).update(v)
json.dump(allf, open('/agent/workspace/memory/all_forecasts.json','w'), indent=1)
missing = [q for q in rows if q not in allf]
print(f"compiled {len(allf)} forecasts; missing {len(missing)}: {missing}")
if '-v' in sys.argv:
    for q in sorted(allf, key=lambda q: rows.get(q,{}).get('resolution_date','')):
        r = rows.get(q, {})
        o = allf[q].get('outcomes', {})
        top = ', '.join(f"{k}:{v:.2f}" for k, v in sorted(o.items(), key=lambda x: -x[1]))
        print(f"{r.get('resolution_date','?')} {q} | {r.get('title','')[:90]}\n    -> {top}")
