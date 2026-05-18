import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))
pending = []
for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            if sub.get('note') in ('待补充','待补') or (len(sub.get('reactions',[]))==0 and len(sub.get('knowledge',[]))==0):
                r = len(sub.get('reactions',[]))
                k = len(sub.get('knowledge',[]))
                pending.append((sub['id'], sub['name'], r, k, sub.get('note','')))
for p in pending:
    print(f'{p[0]}: {p[1]} | 反应{p[2]} 知识{p[3]} | note="{p[4]}"')
