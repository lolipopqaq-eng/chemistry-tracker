import sys
sys.stdout.reconfigure(encoding='utf-8')

import json, re

# 扫描所有5本课本PDF
import pdfplumber

pdf_paths = [
    (r'C:\Users\11384\Desktop\学习\高考\化学\人教版化学必修第一册【高清教材】.pdf', '必修第一册'),
    (r'C:\Users\11384\Desktop\学习\高考\化学\人教版化学必修第二册【高清教材】.pdf', '必修第二册'),
    (r'C:\Users\11384\Desktop\学习\高考\化学\人教版化学选修第一册【高清教材】.pdf', '选修第一册'),
    (r'C:\Users\11384\Desktop\学习\高考\化学\人教版化学选修第二册【高清教材】.pdf', '选修第二册'),
    (r'C:\Users\11384\Desktop\学习\高考\化学\人教版化学选修第三册【高清教材】.pdf', '选修第三册'),
]

# 找所有含 = 或 → 或 ⇌ 的反应行
all_eqs = set()
for pdf_path, name in pdf_paths:
    print(f'\n===== 扫描 {name} =====')
    plumber = pdfplumber.open(pdf_path)
    for pnum, page in enumerate(plumber.pages):
        text = page.extract_text()
        if not text:
            continue
        lines = text.split('\n')
        for line in lines:
            # 找含反应式的行
            if re.search(r'[=→⇌]', line):
                # 去掉无关行（目录、页码等）
                clean = line.strip()
                if len(clean) > 4 and re.search(r'[A-Za-z0-9\u2080-\u2089⁺⁻]{2,}[=→⇌]', clean):
                    if clean not in all_eqs:
                        all_eqs.add(clean)
                        print(f'  p{pnum+1}: {clean[:80]}')
    plumber.close()

print(f'\n共找到 {len(all_eqs)} 个含反应式的行')
