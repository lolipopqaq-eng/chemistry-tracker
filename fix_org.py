import sys
sys.stdout.reconfigure(encoding='utf-8')
c = open('src/utils/textbook.js', 'r', encoding='utf-8').read()

# r19: 卤代烃水解（水溶液，条件=H₂O/△）
c = c.replace(
    "id: 'r19', name: '卤代烃水解', equation: 'CH\u2083CH\u2082Br + NaOH = CH\u2083CH\u2082OH + NaBr'",
    "id: 'r19', name: '卤代烃水解', equation: 'CH\u2083CH\u2082Br + NaOH →(H\u2082O/△) CH\u2083CH\u2082OH + NaBr'"
)

# r20: 卤代烃消去（醇△）
c = c.replace(
    "id: 'r20', name: '卤代烃消去', equation: 'CH\u2083CH\u2082Br + NaOH = CH\u2082=CH\u2082↑ + NaBr + H\u2082O'",
    "id: 'r20', name: '卤代烃消去', equation: 'CH\u2083CH\u2082Br + NaOH →(醇/△) CH\u2082=CH\u2082↑ + NaBr + H\u2082O'"
)

# r21: 油脂皂化
c = c.replace(
    "id: 'r21', name: '油脂皂化', equation: '油脂 + NaOH = 高级脂肪酸钠 + 甘油'",
    "id: 'r21', name: '油脂皂化', equation: '油脂 + NaOH →(△) 高级脂肪酸钠 + 甘油'"
)

# r22: 苯酚+NaOH
c = c.replace(
    "id: 'r22', name: '苯酚 + NaOH', equation: 'C\u2086H\u2085OH + NaOH = C\u2086H\u2085ONa + H\u2082O'",
    "id: 'r22', name: '苯酚 + NaOH', equation: 'C\u2086H\u2085OH + NaOH →(常温) C\u2086H\u2085ONa + H\u2082O'"
)

# r23: 酯水解（注意上面没匹配到 r23 的数据，要检查）
# 在另一个物质里是 ch2_nahco3 下面的？不，酯在 NaOH 里
# 直接找
i = c.find("id: 'r23'")
if i >= 0:
    print('r23 found at', i)
    print(c[i:i+150])

open('src/utils/textbook.js', 'w', encoding='utf-8').write(c)
print('\ndone')
