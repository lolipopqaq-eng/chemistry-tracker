import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))
pending = 0
for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            if sub.get('note') in ('待补充','待补'):
                print(f'{sub["id"]} {sub["name"]} - 仍待补充')
                pending += 1
            elif len(sub.get('reactions',[])) == 0 and len(sub.get('knowledge',[])) == 0:
                if sub.get('note','') and sub.get('note') not in ('待补充','待补'):
                    print(f'{sub["id"]} {sub["name"]} - note="{sub["note"]}"')
if pending == 0:
    print('全部已填写完毕！')
