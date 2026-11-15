#!/usr/bin/env python3
"""Search the local articles corpus. Usage:
python3 search_corpus.py "keyword1" ["keyword2" ...] [--max N] [--ctx N] [--or]
All keywords must match (AND) unless --or given. Prints matches with snippets.
"""
import json, sys, glob, re, argparse

def load_all():
    arts = []
    for f in glob.glob('articles/**/*.jsonl', recursive=True):
        for line in open(f):
            try:
                arts.append(json.loads(line))
            except Exception:
                pass
    return arts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('keywords', nargs='+')
    ap.add_argument('--max', type=int, default=15)
    ap.add_argument('--ctx', type=int, default=250)
    ap.add_argument('--or', dest='or_', action='store_true')
    ap.add_argument('--title-only', action='store_true')
    args = ap.parse_args()
    arts = load_all()
    kws = [k.lower() for k in args.keywords]
    hits = []
    for a in arts:
        text = (a.get('title','') + ' ' + a.get('content','')).lower()
        if args.title_only:
            text = a.get('title','').lower()
        matches = [k in text for k in kws]
        ok = any(matches) if args.or_ else all(matches)
        if ok:
            hits.append(a)
    print(f"### {len(hits)} matches for {args.keywords}")
    for a in hits[:args.max]:
        content = a.get('content','')
        low = content.lower()
        # find first keyword position for snippet
        pos = min([low.find(k) for k in kws if low.find(k) >= 0] or [0])
        start = max(0, pos - args.ctx//2)
        snippet = content[start:start+args.ctx].replace('\n',' ')
        print(f"- [{a.get('date_publish')}] {a.get('title')} ({a.get('source')})")
        print(f"  {snippet}")
    return hits

if __name__ == '__main__':
    main()
