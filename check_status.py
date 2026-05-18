import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))
for ch in d:
    if ch['id'] in ('ch10','ch11','ch9'):
        total_rxn = 0
        total_know = 0
        total_sub = 0
        for sec in ch['sections']:
            for sub in sec['substances']:
                total_sub += 1
                total_rxn += len(sub.get('reactions',[]))
                total_know += len(sub.get('knowledge',[]))
        print(f'{ch["id"]}: {total_sub}物质 {total_rxn}反应 {total_know}知识点')
