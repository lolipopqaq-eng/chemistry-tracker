import sys
sys.stdout.reconfigure(encoding='utf-8')
c = open('src/utils/textbook.js', 'r', encoding='utf-8').read()

pairs = [
    ("equation: '2Na + O\u2082 = Na\u2082O\u2082'", "equation: '2Na + O\u2082 =(点燃) Na\u2082O\u2082'"),
    ("equation: '2Na + Cl\u2082 = 2NaCl'", "equation: '2Na + Cl\u2082 =(点燃) 2NaCl'"),
    ("equation: 'Cu + Cl\u2082 = CuCl\u2082'", "equation: 'Cu + Cl\u2082 =(点燃) CuCl\u2082'"),
    ("equation: 'H\u2082 + Cl\u2082 = 2HCl'", "equation: 'H\u2082 + Cl\u2082 =(点燃) 2HCl'"),
    ("equation: '2Fe + 3Cl\u2082 = 2FeCl\u2083'", "equation: '2Fe + 3Cl\u2082 =(点燃) 2FeCl\u2083'"),
    ("equation: '2NaHCO\u2083 = Na\u2082CO\u2083 + H\u2082O + CO\u2082\u2191'", "equation: '2NaHCO\u2083 =(加热) Na\u2082CO\u2083 + H\u2082O + CO\u2082\u2191'"),
    ("equation: '2NaCl + 2H\u2082O = 2NaOH + H\u2082\u2191 + Cl\u2082\u2191'", "equation: '2NaCl + 2H\u2082O =(电解) 2NaOH + H\u2082\u2191 + Cl\u2082\u2191'"),
    ("equation: '2HClO = 2HCl + O\u2082\u2191'", "equation: '2HClO =(光照) 2HCl + O\u2082\u2191'"),
]

for old, new in pairs:
    if old in c:
        c = c.replace(old, new)
        print(f'OK: {old[:40]}')
    else:
        print(f'MISS: {old[:40]}')

open('src/utils/textbook.js', 'w', encoding='utf-8').write(c)
print('\ndone')
