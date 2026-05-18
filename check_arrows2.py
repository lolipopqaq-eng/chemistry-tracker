import sys
sys.stdout.reconfigure(encoding='utf-8')
c = open('src/utils/textbook.js', 'r', encoding='utf-8').read()

# 有机反应ID（用箭头→）
organic = {'r19','r20','r21','r22','r23'}

import re

# 先看所有带条件的方程，检查是不是有机
for m in re.finditer(r"equation: '([^']+)'", c):
    eq = m.group(1)
    if '\u2192(' in eq:  # →(
        # 找到这个方程前面的 id
        start = max(0, m.start() - 200)
        before = c[start:m.start()]
        # 提取 id
        id_m = re.search(r"id: '([^']+)'", before)
        rid = id_m.group(1) if id_m else '??'
        print(f'{rid}: {eq}')
