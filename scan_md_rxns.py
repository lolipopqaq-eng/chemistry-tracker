import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# 读取思维导图全部内容
with open(r'C:\Users\11384\Desktop\学习\高考\化学\思维导图\化学_全部五册.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 提取所有含=或→或⇌的反应行（粗略）
all_rxns = []
for line in text.split('\n'):
    line = line.strip()
    # 找反应式：含有=、→、⇌（不是箭头说明文字）
    if ('=' in line or '→' in line or '⇌' in line) and line.startswith('-'):
        # 去掉开头的-和可能的前缀
        # 提取反应名和反应式
        # 格式: - 反应名: A+B=C
        name = line[1:].split(':')[0].strip() if ':' in line else ''
        eq = line.split(':')[-1].strip() if ':' in line else line[1:].strip()
        all_rxns.append((name, eq, line))
        print(f'  {name} | {eq}')

print(f'\n共找到{len(all_rxns)}个反应')
