import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json', 'r', encoding='utf-8'))
for ch in d:
    total = 0
    info = []
    for sec in ch['sections']:
        for sub in sec['substances']:
            n = len(sub['reactions'])
            total += n
            info.append(f'{sub["name"]}({n})')
    print(f'{ch["id"]}: {ch["name"]} [{total}个反应]')
    for i in info:
        print(f'    {i}')
    print()
