c = open('textbook.js', 'r', encoding='utf-8').read()

old = "{ id: 'ch2_na2', name: 'Na + O\u2082（点燃）', equation: '2Na + O\u2082 \u2192(点燃) Na\u2082O\u2082（淡黄色）', category: '钠单质',\n    phenomenon: '钠浮在水面\u2192熔成小球\u2192四处游动\u2192发出嘶嘶声\u2192溶液变红（浮熔游响红）', note: '点燃生成过氧化钠（淡黄色）' }"

new = "{ id: 'ch2_na2', name: 'Na + O\u2082（点燃）', equation: '2Na + O\u2082 \u2192(点燃) Na\u2082O\u2082', category: '钠单质',\n    phenomenon: '钠剧烈燃烧，发出黄色火焰，生成淡黄色固体Na\u2082O\u2082', note: '点燃生成过氧化钠（淡黄色）' }"

if old in c:
    c = c.replace(old, new)
    open('textbook.js', 'w', encoding='utf-8').write(c)
    print('replaced ok')
else:
    print('not found')
    i = c.find('ch2_na2')
    print(repr(c[i:i+250]))
