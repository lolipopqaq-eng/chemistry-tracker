import re

with open('textbook.js', 'r', encoding='utf-8') as f:
    content = f.read()

phenomena = {
    'ch2_na1': '银白色金属钠表面变暗（生成白色Na2O）',
    'ch2_na2': '钠剧烈燃烧，发出黄色火焰，生成淡黄色固体Na2O2',
    'ch2_na3': '钠浮在水面→熔成小球→四处游动→发出嘶嘶声→溶液变红（浮熔游响红）',
    'ch2_na4': '钠在氯气中剧烈燃烧，产生白烟（NaCl固体）',
    'cl1': '铜丝在氯气中剧烈燃烧，产生棕黄色烟',
    'cl2': '氢气在氯气中安静燃烧，发出苍白色火焰，瓶口有白雾',
    'cl6': '铁在氯气中剧烈燃烧，产生棕褐色烟',
    'cl7': '溶液从无色变为橙黄色（Br2生成）',
    'cl8': '溶液从无色变为棕黄色，加淀粉变蓝（I2生成）',
    'fe1': '铁丝剧烈燃烧，火星四射，生成黑色固体Fe3O4',
    'fe2': '铁溶解，产生无色气泡，溶液变浅绿色',
    'fe3': '常温下无明显现象（钝化）',
    'fe4': '铁表面析出红色固体，溶液从蓝色变浅绿色',
    'fe5': '铁在氯气中剧烈燃烧，产生棕褐色烟',
    'feoh1': '生成白色沉淀，迅速变灰绿，最终变红褐',
    'feoh2': '生成红褐色沉淀',
    'feoh3': '白色沉淀→灰绿色→红褐色',
    'feion1': '溶液从浅绿色变为棕黄色',
    'feion2': '溶液从棕黄色变为浅绿色',
    'feion3': '溶液变为血红色',
    'feion5': '铜溶解，溶液从棕黄色变为浅绿色',
    'n01': '开始无气泡，继续滴加后产生气泡',
    'n02': '立即产生无色气泡（CO2）',
    'n03': '产生白色沉淀（CaCO3）',
    'n04': '产生白色沉淀（BaCO3）',
    'n06': '产生白色沉淀（CaCO3）',
    'n07': '产生白色沉淀（BaCO3）',
    'n08': '通入CO2后溶液变浑浊（析出NaHCO3晶体）',
    'h05': '加热后试管口有水珠，气体使澄清石灰水变浑浊',
    'r01': '铝逐渐溶解，产生无色气泡',
    'r15': '加热产生刺激性气体，湿润红色石蕊试纸变蓝',
    'r16': '产生蓝色絮状沉淀',
    'r17': '产生红褐色沉淀',
    'r22': '苯酚溶液由浑浊变澄清',
    'feo1': '黑色固体FeO溶解，溶液变浅绿色',
    'feo2': '红棕色固体Fe2O3溶解，溶液变棕黄色',
    'feo4': '红棕色粉末逐渐变成银白色',
    'feo5': '剧烈反应，放出大量热，产生耀眼白光，铁水流出',
    'feoh4': '红褐色固体变成红棕色，试管口有水珠',
    'feion4': '浅绿色溶液逐渐变棕黄',
    'feion6': '溶液变色，加淀粉变蓝（I2）',
    'hclo1': '氯水颜色变浅，产生无色气泡',
    'nacl1': '两极产生气泡：阴极H2、阳极Cl2',
    'p1': '产生气泡，溶液变碱性',
    'p2': '淡黄色固体逐渐变白，产生O2',
}

# 注意过氧化钠的id其实是 ch2_p1 和 ch2_p2
# 但数据里是 p1/p2 格式，不对，我们加 ch2_ 前缀

lines = content.split('\n')
new_lines = []
for line in lines:
    new_lines.append(line)

# 用正则找每个 reaction 对象
# 匹配 {id:'xxx', ...}
pattern = r"(id:\s*'([^']+)')"
matches = list(re.finditer(pattern, content))
for m in matches:
    rid = m.group(2)
    if rid in phenomena:
        phen = phenomena[rid]
        # 找到这个 reaction 对象的闭合大括号
        start = m.start()
        # 往前找到 {
        brace_start = content.rfind('{', 0, start)
        # 从 id 行往后找，找到下一个 }, 或 }, 或   },
        end_idx = content.find('}', brace_start)
        if end_idx > brace_start:
            block = content[brace_start:end_idx+1]
            # 在最后一个逗号后插入 phenomenon
            if 'phenomenon' not in block:
                last_comma = block.rfind(',')
                if last_comma > 0:
                    indent = '    '
                    ins = f"\n{indent}phenomenon: '{phen}',"
                    new_block = block[:last_comma+1] + ins + block[last_comma+1:]
                    content = content[:brace_start] + new_block + content[end_idx+1:]
                    print(f"Added phenomenon for {rid}")

with open('textbook.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal phenomena added: checking...")
import json
# count
count = sum(1 for rid in phenomena if f"id: '{rid}'" in content)
print(f"Found {count} out of {len(phenomena)}")
