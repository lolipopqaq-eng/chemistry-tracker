import json
raw = json.load(open('src/data/textbook-data.json', 'r', encoding='utf-8'))
total = 0
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            total += len(sub['reactions'])
print('总反应数:', total)
print('总章节数:', len(raw))
for ch in raw:
    print(ch['id'], ':', ch['name'])
    for sec in ch['sections']:
        subst = [s['name'] for s in sec['substances']]
        print('  ', sec['id'], ':', sec['name'], '-', len(subst), '种物质')
