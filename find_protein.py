import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))
for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            tag = sub['name'] + sub['id']
            if '蛋白' in tag or '氨基酸' in tag:
                print(sub['id'], sub['name'])
