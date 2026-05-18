import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))

# 册名映射
volume_names = {
    'ch1': '必修第一册',
    'ch2': '必修第一册',
    'ch3': '必修第一册',
    'ch4': '必修第一册',
    'ch5': '必修第二册',
    'ch6': '必修第二册',
    'ch7': '必修第二册',
    'ch8': '必修第二册',
    'ch9': '选修第一册',
    'ch10': '选修第二册',
    'ch11': '选修第三册',
}

for ch in d:
    vol = volume_names.get(ch['id'], '')
    ch['name'] = f'{vol}·{ch["name"]}'

json.dump(d, open('src/data/textbook-data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK 册名已加入')
