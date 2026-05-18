import sys
sys.stdout.reconfigure(encoding='utf-8')
c = open('src/utils/textbook.js', 'r', encoding='utf-8').read()

# 无机反应：=(条件)
c = c.replace("equation: '2Na + O\u2082 \u2192(点燃) Na\u2082O\u2082'", "equation: '2Na + O\u2082 =(点燃) Na\u2082O\u2082'")
c = c.replace("equation: '2Na + Cl\u2082 \u2192(点燃) 2NaCl'", "equation: '2Na + Cl\u2082 =(点燃) 2NaCl'")
c = c.replace("equation: '2NaHCO\u2083 \u2192(加热) Na\u2082CO\u2083 + H\u2082O + CO\u2082\u2191'", "equation: '2NaHCO\u2083 =(加热) Na\u2082CO\u2083 + H\u2082O + CO\u2082\u2191'")
c = c.replace("equation: 'Cu + Cl\u2082 \u2192(点燃) CuCl\u2082'", "equation: 'Cu + Cl\u2082 =(点燃) CuCl\u2082'")
c = c.replace("equation: 'H\u2082 + Cl\u2082 \u2192(点燃) 2HCl'", "equation: 'H\u2082 + Cl\u2082 =(点燃) 2HCl'")
c = c.replace("equation: '2Fe + 3Cl\u2082 \u2192(点燃) 2FeCl\u2083'", "equation: '2Fe + 3Cl\u2082 =(点燃) 2FeCl\u2083'")
c = c.replace("equation: '2HClO \u2192(光照) 2HCl + O\u2082\u2191'", "equation: '2HClO =(光照) 2HCl + O\u2082\u2191'")
c = c.replace("equation: '2NaCl + 2H\u2082O \u2192(电解) 2NaOH + H\u2082\u2191 + Cl\u2082\u2191'", "equation: '2NaCl + 2H\u2082O =(电解) 2NaOH + H\u2082\u2191 + Cl\u2082\u2191'")

open('src/utils/textbook.js', 'w', encoding='utf-8').write(c)

# 检查还有没有无机带了箭头
import re
for m in re.finditer(r"equation: '([^']+)'", c):
    eq = m.group(1)
    if '\u2192' in eq:
        print(f'STILL ARROW: {eq}')
print('done')
