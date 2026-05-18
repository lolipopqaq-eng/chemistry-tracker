import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# 读取思维导图全部五册
with open(r'C:\Users\11384\Desktop\学习\高考\化学\思维导图\化学_全部五册.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 逐行提取含反应式的行
lines = text.split('\n')
rxns_from_md = []
current_chapter = ''
current_section = ''
for line in lines:
    line_stripped = line.strip()
    if line_stripped.startswith('## '):
        current_chapter = line_stripped.replace('## ','')
    elif line_stripped.startswith('### '):
        current_section = line_stripped.replace('### ','')
    
    # 找含化学式的行
    if ('=' in line_stripped or '→' in line_stripped) and not line_stripped.startswith('#'):
        rxns_from_md.append({
            'chapter': current_chapter,
            'section': current_section,
            'text': line_stripped
        })

print(f'思维导图共 {len(rxns_from_md)} 条含反应式的行\n')

# 读取现有数据
raw = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))

by_id = {}
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            by_id[sub['id']] = sub

# 提取所有现有反应的equation（简化比对）
existing_eqs = set()
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            for r in sub.get('reactions', []):
                # 提取核心反应物产物（去掉条件）
                eq = r['equation']
                # 去括号内容（条件）
                eq_clean = re.sub(r'\(.*?\)', '', eq)
                # 去空格
                eq_clean = eq_clean.replace(' ', '')
                existing_eqs.add(eq_clean)

# 比对思维导图的每个反应是否已在数据中
missing = []
for item in rxns_from_md:
    line = item['text']
    # 提取反应式部分（去除箭头前面的说明文字）
    # 格式举例: "- 与H₂O：2Na+2H₂O→2NaOH+H₂↑(浮熔游响红)"
    # 格式举例: "- 2Na₂O₂+2CO₂→2Na₂CO₃+O₂"
    
    # 先去掉开头的 -
    clean = line.lstrip('- ')
    
    # 去掉末尾的括号注释
    clean = re.sub(r'（[^）]*）$', '', clean)
    
    # 提取反应式：找 = 或 → 或 ⇌
    match = re.search(r'[=→⇌]', clean)
    if not match:
        continue
    
    # 提取完整反应式
    # 尝试各种模式
    # 模式1: "文字：反应式" 
    if '：' in clean:
        parts = clean.split('：')
        potential_eq = parts[-1].strip()
    else:
        potential_eq = clean
    
    # 去除末尾的括号注释
    potential_eq = re.sub(r'（[^）]*）', '', potential_eq)
    potential_eq = re.sub(r'\([^)]*\)', '', potential_eq)
    
    # 如果含多个箭头，取最后一个反应式
    # 去掉空格
    eq_compare = potential_eq.replace(' ', '')
    
    # 检查是否已经在数据中
    found = False
    for ex in existing_eqs:
        # 核心产物是否匹配
        if len(eq_compare) > 5 and (eq_compare in ex or ex in eq_compare):
            found = True
            break
    
    if not found and len(eq_compare) > 5 and '=' in eq_compare or '→' in eq_compare or '⇌' in eq_compare:
        missing.append(item)
        print(f'❌ 缺失: {item["chapter"]} | {item["section"]}')
        print(f'   原文: {line}')
        print(f'   提取: {potential_eq}')
        print()

print(f'\n共缺 {len(missing)} 个反应')
