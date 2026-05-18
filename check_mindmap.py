import sys, json
sys.stdout.reconfigure(encoding='utf-8')
raw = json.load(open('src/data/textbook-data.json', 'r', encoding='utf-8'))
for ch in raw:
    has = 'mindMap' in ch
    print(f'{ch["id"]}: mindMap={has}')
