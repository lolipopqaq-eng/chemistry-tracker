import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))
for ch in d:
    total_r = 0
    total_k = 0
    for sec in ch['sections']:
        for sub in sec['substances']:
            total_r += len(sub.get('reactions',[]))
            total_k += len(sub.get('knowledge',[]))
    print(f'{ch["id"]}: {ch["name"]} → 反应{total_r} 知识点{total_k}')
