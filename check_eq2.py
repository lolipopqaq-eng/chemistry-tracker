import sys
sys.stdout.reconfigure(encoding='utf-8')
c = open('src/utils/textbook.js', 'r', encoding='utf-8').read()

# 有机反应ID列表（用箭头→）
organic_ids = {'r19','r20','r21','r22','r23'}

import re

# 把所有方程中的 =(点燃/加热/电解/光照) 保持不变
# 无机普通 = 保持不变
# 找有机反应的方程，改成带=的箭头 →(水溶液) / →(醇△) 等
# 其实有机的条件也需要

# 看看有机方程现在的内容
for m in re.finditer(r"id: '(r1[89]|r2[0-3])'", c):
    start = m.start()
    end = c.find('}', start)
    block = c[start:end]
    eq_match = re.search(r"equation: '([^']+)'", block)
    if eq_match:
        print(f'{m.group(1)}: {eq_match.group(1)}')

# 可逆反应（cl3: Cl₂+H₂O, h08, n09, ch1_e1/ch1_e2/ch1_e3）
# 现在的 ⇌ 保持不动
print(f'\n可逆符号⇌: {c.count("⇌")}个')
