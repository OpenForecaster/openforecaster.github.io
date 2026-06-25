#!/usr/bin/env python3
"""Dump all questions sorted by resolution date to a readable text file."""
import csv, json

with open('market.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))

rows.sort(key=lambda r: (r['resolution_date'], r['qid']))

with open('memory/questions_all.txt', 'w', encoding='utf-8') as out:
    for r in rows:
        out.write(f"=== {r['qid']} | resolves {r['resolution_date']} | {r['answer_type']}\n")
        out.write(f"TITLE: {r['title']}\n")
        if r['background'] and r['background'] != 'nan':
            out.write(f"BG: {r['background'][:600]}\n")
        if r['resolution_criteria'] and r['resolution_criteria'] != 'nan':
            out.write(f"RES: {r['resolution_criteria'][:600]}\n")
        out.write(f"PRED: {r['my_prediction']}\n\n")
print("wrote memory/questions_all.txt")
