import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json', 'r', encoding='utf-8'))

# 查看 ch4（周期律）的现有结构
for ch in d:
    if ch['id'] == 'ch4':
        print(json.dumps(ch, ensure_ascii=False, indent=2)[:1000])
        break
