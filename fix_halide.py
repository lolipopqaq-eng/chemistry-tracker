import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))

for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            for r in sub.get('reactions', []):
                # 改通用RX名
                if r['name'] == '卤代烃水解' and 'RX' in r.get('equation',''):
                    r['name'] = '溴乙烷水解(制乙醇)'
                    r['equation'] = 'CH₃CH₂Br + NaOH →(H₂O/△) CH₃CH₂OH + NaBr'
                    r['note'] = '💯 卤代烃→醇'
                elif r['name'] == '卤代烃消去' and 'RX' in r.get('equation',''):
                    r['name'] = '溴乙烷消去(制乙烯)'
                    r['equation'] = 'CH₃CH₂Br + NaOH →(C₂H₅OH/△) CH₂=CH₂↑ + NaBr + H₂O'
                    r['note'] = '💯 卤代烃→烯烃'
                    
                # 改其他抽象名
                if 'RX' in r.get('equation',''):
                    if '取代' in r.get('name','') or '水解' in r.get('name',''):
                        r['name'] = '溴乙烷水解'
                        r['equation'] = 'CH₃CH₂Br + NaOH →(H₂O/△) CH₃CH₂OH + NaBr'
                    elif '消去' in r.get('name',''):
                        r['name'] = '溴乙烷消去'
                        r['equation'] = 'CH₃CH₂Br + NaOH →(C₂H₅OH/△) CH₂=CH₂↑ + NaBr + H₂O'

json.dump(d, open('src/data/textbook-data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)

# 统计
total = 0
for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            total += len(sub.get('reactions', []))
print(f'OK 总反应={total}')
