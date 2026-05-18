import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))

total_all = 0
for ch in d:
    ch_total = 0
    print(f'\n{ch["name"]}:')
    for sec in ch['sections']:
        sec_r = 0
        for sub in sec['substances']:
            n = len(sub.get('reactions', []))
            sec_r += n
        if sec_r > 0:
            print(f'  {sec["name"]}: {sec_r}反应')
        ch_total += sec_r
    total_all += ch_total
    print(f'  小计: {ch_total}反应')
print(f'\n总数: {total_all}反应')
