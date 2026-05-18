import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json', 'r', encoding='utf-8'))
cats = {}
for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            for r in sub['reactions']:
                cat = r.get('category', '无')
                cats[cat] = cats.get(cat, 0) + 1
for c, n in sorted(cats.items(), key=lambda x: -x[1]):
    print(f'{n:>3}  {c}')
