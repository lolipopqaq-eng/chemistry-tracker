import sys
sys.stdout.reconfigure(encoding='utf-8')
c = open('src/utils/textbook.js', 'r', encoding='utf-8').read()

# 确保方程里用 =(条件) 格式
# 先替换单纯的 = 为 =(条件) 哪里需要加
import re

# 查看当前方程
for m in re.findall(r"equation: '([^']+)'", c):
    if '点燃' in m or '加热' in m or '电解' in m or '光照' in m:
        print(f'  {m}')
    elif '=' in m and not m.startswith('不'):
        print(f'  {m}')

print('\nFound equations with conditions:')
