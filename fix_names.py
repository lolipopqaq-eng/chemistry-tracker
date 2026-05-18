import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))

fixes = {
    '卤代烃水解': '溴乙烷水解(制乙醇)',
    '卤代烃消去': '溴乙烷消去(制乙烯)',
    '卤代烃取代': '溴乙烷取代',
    '烯烃+溴水': '乙烯+Br₂',
    '炔烃+溴水': '乙炔+2Br₂',
    '醇的消去': '乙醇消去(制乙烯)',
    '醇的催化氧化': '乙醇催化氧化(制乙醛)',
    '醇与Na反应': '乙醇+Na',
    '醛的银镜反应': '乙醛银镜反应',
    '羧酸与NaOH中和': '乙酸+NaOH',
    '酯化反应': '乙酸乙酯酯化',
}

count = 0
for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            for r in sub.get('reactions', []):
                for old, new in fixes.items():
                    if r['name'] == old:
                        print(f'修复: {old} → {new}')
                        r['name'] = new
                        count += 1

json.dump(d, open('src/data/textbook-data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'\n共修复 {count} 个反应名')
