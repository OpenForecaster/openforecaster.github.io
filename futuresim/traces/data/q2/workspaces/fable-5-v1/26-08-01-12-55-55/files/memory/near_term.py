#!/usr/bin/env python3
"""List questions resolving within N days (default 8), with current predictions."""
import csv, sys, datetime
N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
TODAY = sys.argv[2] if len(sys.argv) > 2 else None
with open('market.csv') as f:
    rows = list(csv.DictReader(f))
if TODAY is None:
    # infer: max prediction date + 1 is a decent guess; better to pass explicitly
    TODAY = max(r['my_prediction_date'] for r in rows if r['my_prediction_date'] not in ('','None'))
end = (datetime.date.fromisoformat(TODAY) + datetime.timedelta(days=N)).isoformat()
sel = [r for r in rows if r['is_resolved'] == 'False' and r['resolution_date'] <= end]
sel.sort(key=lambda r: r['resolution_date'])
print(f"today={TODAY} horizon={end} n={len(sel)}")
for r in sel:
    print(f"{r['qid']} | {r['resolution_date']} | {r['title'][:100]}")
    print(f"   PRED: {r['my_prediction'][:180]}")
