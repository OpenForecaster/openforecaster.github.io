#!/usr/bin/env python3
"""Parse market.csv and dump question summaries."""
import csv, json, sys

def load(path='market.csv'):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

if __name__ == '__main__':
    rows = load()
    print(f"Total: {len(rows)}")
    # answer types
    from collections import Counter
    print(Counter(r['answer_type'] for r in rows))
    print(Counter(r['resolution_date'] for r in rows).most_common(30))
    print(Counter(r['is_resolved'] for r in rows))
