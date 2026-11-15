#!/usr/bin/env python3
"""Record an override: ov.py QID '{"A":0.5}' 'rationale' [date]"""
import json, sys, datetime
fn = '/agent/workspace/memory/overrides.json'
d = json.load(open(fn))
q, outs, rat = sys.argv[1], json.loads(sys.argv[2]), sys.argv[3]
date = sys.argv[4] if len(sys.argv) > 4 else ''
assert sum(outs.values()) <= 1.0001 and len(outs) <= 5
d[q] = {"outcomes": outs, "rationale": rat, "updated": date}
json.dump(d, open(fn, 'w'), indent=1, ensure_ascii=False)
print('ok', q)
