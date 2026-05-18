import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
c = open('src/utils/textbook.js', 'r', encoding='utf-8').read()
for m in re.finditer(r"equation: '([^']+)'", c):
    eq = m.group(1)
    if '\u2192(' in eq:
        print(f'HAS ARROW WITH COND: {eq}')
