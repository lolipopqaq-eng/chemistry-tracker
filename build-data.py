#!/usr/bin/env python3
"""Generate textbook-data.json from embedded chemistry data."""
import json, os

OUT = r'C:\Users\11384\.openclaw\workspace\chemistry-tracker\src\data\textbook-data.json'

def r(id, name, equation, category, **opts):
    return {"id": id, "name": name, "equation": equation,
            "category": category, **opts}

chapters = []

# ====== ch1 ======
ch1 = {
    "id": "ch1",
    "name": "第一章 物质及其变化",
    "sections": [{
        "id": "ch1_elec",
        "name": "电解质与离子反应",
        "substances": [
            {
                "id": "ch1_hcl", "name": "HCl 盐酸", "icon": "🧪",
                "note": "强酸、强电解质",
                "reactions": [
                    r("ch1_hcl1", "HCl 电离", "HCl = H⁺ + Cl⁻", "电离", note="强电解质完全电离"),
                    r("ch1_hcl2", "HCl + NaOH", "HCl + NaOH = NaCl + H₂O", "中和", note="💯 H⁺ + OH⁻ = H₂O"),
                    r("ch1_hcl3", "HCl + Na₂CO₃", "2HCl + Na₂CO₃ = 2NaCl + H₂O + CO₂↑", "与盐",
                      phenomenon="产生气泡", note="CO₃²⁻ + 2H⁺ = H₂O + CO₂↑"),
                ],
            },
            {
                "id": "ch1_naoh", "name": "NaOH 氢氧化钠", "icon": "🧴",
                "note": "强碱、强电解质",
                "reactions": [
                    r("ch1_naoh1", "NaOH 电离", "NaOH = Na⁺ + OH⁻", "电离", note="强电解质完全电离"),
                    r("ch1_naoh2", "NaOH + HCl", "NaOH + HCl = NaCl + H₂O", "中和", note="中和反应"),
                    r("ch1_naoh3", "NaOH + CuSO₄", "2NaOH + CuSO₄ = Cu(OH)₂↓ + Na₂SO₄", "复分解",
                      phenomenon="蓝色沉淀", note="复分解反应条件：有沉淀"),
                ],
            },
            {
                "id": "ch1_na2so4", "name": "Na₂SO₄ 硫酸钠", "icon": "🧂",
                "note": "盐、强电解质",
                "reactions": [
                    r("ch1_ns1", "Na₂SO₄ 电离", "Na₂SO₄ = 2Na⁺ + SO₄²⁻", "电离", note="强电解质完全电离"),
                ],
            },
            {
                "id": "ch1_feoh3", "name": "Fe(OH)₃胶体", "icon": "🧫",
                "note": "胶体制备",
                "reactions": [
                    r("ch1_col1", "Fe(OH)₃胶体制备", "FeCl₃ + 3H₂O =(加热) Fe(OH)₃(胶体) + 3HCl", "水解",
                      phenomenon="溶液呈红褐色", note="💯 丁达尔效应！不能写↓"),
                ],
            },
        ],
    }],
}
chapters.append(ch1)
print("ch1 done")

# ====== ch2 ======
ch2 = {
    "id": "ch2",
    "name": "第二章 海水中的重要元素——钠和氯",
    "sections": [
        {
            "id": "ch2_na",
            "name": "钠及其化合物",
            "substances": [
                {
                    "id": "ch2_na_metal", "name": "Na 钠单质", "icon": "🥈",
                    "note": "银白色、质软、密度0.97、熔点低、保存在煤油中",
                    "reactions": [
                        r("ch2_na1", "Na + O₂（常温）", "4Na + O₂ = 2Na₂O", "与氧气",
                          phenomenon="银白色金属钠表面变暗", note="⚠ 注意条件：常温"),
                        r("ch2_na2", "Na + O₂（点燃）", "2Na + O₂ =(点燃) Na₂O₂", "与氧气",
                          phenomenon="发出黄色火焰，生成淡黄色固体", note="⚠ 产物颜色：淡黄色"),
                        r("ch2_na3", "Na + H₂O", "2Na + 2H₂O = 2NaOH + H₂↑", "与水",
                          phenomenon="浮=熔=游=响=红", note="💯 必考！浮熔游响红"),
                        r("ch2_na4", "Na + Cl₂", "2Na + Cl₂ =(点燃) 2NaCl", "与氯气",
                          phenomenon="钠在氯气中剧烈燃烧，产生白烟", note="⚠ 白烟是NaCl固体颗粒"),
                    ],
                },
                {
                    "id": "ch2_na2o", "name": "Na₂O 氧化钠", "icon": "⬜",
                    "note": "白色固体，碱性氧化物",
                    "reactions": [
                        r("ch2_o1", "Na₂O + H₂O", "Na₂O + H₂O = 2NaOH", "与水", note="碱性氧化物通性"),
                        r("ch2_o2", "Na₂O + CO₂", "Na₂O + CO₂ = Na₂CO₃", "与CO₂", note="碱性氧化物+酸性氧化物=盐"),
                        r("ch2_o3", "Na₂O + HCl", "Na₂O + 2HCl = 2NaCl + H₂O", "与酸", note="碱性氧化物通性"),
                    ],
                },
                {
                    "id": "ch2_na2o2", "name": "Na₂O₂ 过氧化钠", "icon": "🟡",
                    "note": "淡黄色固体，供氧剂",
                    "reactions": [
                        r("ch2_p1", "Na₂O₂ + H₂O", "2Na₂O₂ + 2H₂O = 4NaOH + O₂↑", "与水",
                          phenomenon="产生气泡，酚酞先变红后褪色", note="⚠ Na₂O₂既是氧化剂又是还原剂"),
                        r("ch2_p2", "Na₂O₂ + CO₂", "2Na₂O₂ + 2CO₂ = 2Na₂CO₃ + O₂", "与CO₂",
                          phenomenon="淡黄色固体变白", note="💯 供氧剂原理！必考"),
                        r("ch2_p3", "Na₂O₂ + HCl", "2Na₂O₂ + 4HCl = 4NaCl + 2H₂O + O₂↑", "与酸",
                          note="类似与H₂O的反应"),
                    ],
                },
                {
                    "id": "ch2_naoh", "name": "NaOH 氢氧化钠", "icon": "🧪",
                    "note": "白色固体、强碱、潮解、腐蚀性",
                    "reactions": [
                        r("r01", "Al + NaOH", "2Al + 2NaOH + 2H₂O = 2NaAlO₂ + 3H₂↑", "与单质",
                          phenomenon="铝逐渐溶解，产生气泡", note="💯 Al的两性体现"),
                        r("r02", "Si + NaOH", "Si + 2NaOH + H₂O = Na₂SiO₃ + 2H₂↑", "与单质", note="Si与碱的歧化反应"),
                        r("r03", "Cl₂ + NaOH（常温）", "Cl₂ + 2NaOH = NaCl + NaClO + H₂O", "与单质",
                          phenomenon="黄绿色气体褪去", note="⚠ 歧化反应，制84消毒液"),
                        r("r04", "Cl₂ + NaOH（加热）", "3Cl₂ + 6NaOH = 5NaCl + NaClO₃ + 3H₂O", "与单质",
                          note="加热歧化，产物不同"),
                        r("r05", "S + NaOH", "3S + 6NaOH = 2Na₂S + Na₂SO₃ + 3H₂O", "与单质", note="硫的歧化"),
                        r("r06", "NaOH + CO₂（过量CO₂）", "NaOH + CO₂ = NaHCO₃", "与酸性氧化物", note="⚠ 注意量！CO₂过量"),
                        r("r07", "NaOH + CO₂（过量NaOH）", "2NaOH + CO₂ = Na₂CO₃ + H₂O", "与酸性氧化物", note="⚠ 注意量！NaOH过量"),
                        r("r08", "NaOH + SO₂", "2NaOH + SO₂ = Na₂SO₃ + H₂O", "与酸性氧化物", note="SO₂过量生成NaHSO₃"),
                        r("r09", "NaOH + SiO₂", "2NaOH + SiO₂ = Na₂SiO₃ + H₂O", "与酸性氧化物",
                          note="💯 玻璃瓶不能用磨口玻璃塞"),
                        r("r10", "NaOH + HCl", "NaOH + HCl = NaCl + H₂O", "中和", note="强酸强碱中和"),
                        r("r11", "NaOH + CH₃COOH", "NaOH + CH₃COOH = CH₃COONa + H₂O", "中和", note="弱酸也能中和"),
                        r("r12", "NaOH + H₂S", "2NaOH + H₂S = Na₂S + 2H₂O", "中和", note="二元酸中和"),
                        r("r13", "Al₂O₃ + NaOH", "Al₂O₃ + 2NaOH = 2NaAlO₂ + H₂O", "两性", note="💯 Al₂O₃两性"),
                        r("r14", "Al(OH)₃ + NaOH", "Al(OH)₃ + NaOH = NaAlO₂ + 2H₂O", "两性", note="💯 Al(OH)₃两性，高考必考"),
                        r("r15", "NH₄Cl + NaOH", "NH₄Cl + NaOH = NaCl + NH₃↑ + H₂O", "与盐",
                          phenomenon="湿润红色石蕊试纸变蓝", note="💯 实验室制NH₃"),
                        r("r16", "CuSO₄ + NaOH", "CuSO₄ + 2NaOH = Cu(OH)₂↓ + Na₂SO₄", "与盐",
                          phenomenon="蓝色絮状沉淀", note="⚠ 沉淀颜色：蓝色"),
                        r("r17", "FeCl₃ + NaOH", "FeCl₃ + 3NaOH = Fe(OH)₃↓ + 3NaCl", "与盐",
                          phenomenon="红褐色沉淀", note="⚠ 沉淀颜色：红褐色"),
                        r("r18", "NaHCO₃ + NaOH", "NaHCO₃ + NaOH = Na₂CO₃ + H₂O", "与盐", note="酸式盐+碱=正盐"),
                        r("r19", "卤代烃水解", "CH₃CH₂Br + NaOH →(H₂O/△) CH₃CH₂OH + NaBr", "有机",
                          note="水溶液，取代反应"),
                        r("r20", "卤代烃消去", "CH₃CH₂Br + NaOH →(醇/△) CH₂=CH₂↑ + NaBr + H₂O", "有机",
                          note="醇溶液，消去反应"),
                        r("r21", "油脂皂化", "油脂 + NaOH →(△) 高级脂肪酸钠 + 甘油", "有机", note="碱性水解"),
                        r("r22", "苯酚 + NaOH", "C₆H₅OH + NaOH →(常温) C₆H₅ONa + H₂O", "有机",
                          phenomenon="苯酚由浑浊变澄清", note="酚羟基显弱酸性"),
                    ],
                },
                {
                    "id": "ch2_na2co3", "name": "Na₂CO₃ 碳酸钠", "icon": "🧂",
                    "note": "白色粉末、易溶、热稳定性高",
                    "reactions": [
                        r("n01", "Na₂CO₃ + HCl（少量）", "Na₂CO₃ + HCl = NaHCO₃ + NaCl", "与酸",
                          phenomenon="开始无气泡", note="💯 逐滴加盐酸，先无气泡后有气泡"),
                        r("n02", "Na₂CO₃ + HCl（过量）", "Na₂CO₃ + 2HCl = 2NaCl + H₂O + CO₂↑", "与酸",
                          phenomenon="立即产生气泡", note="💯 与n01对比记忆"),
                        r("n03", "Na₂CO₃ + Ca(OH)₂", "Na₂CO₃ + Ca(OH)₂ = CaCO₃↓ + 2NaOH", "与碱",
                          phenomenon="白色沉淀", note="工业制烧碱"),
                        r("n04", "Na₂CO₃ + Ba(OH)₂", "Na₂CO₃ + Ba(OH)₂ = BaCO₃↓ + 2NaOH", "与碱",
                          phenomenon="白色沉淀", note="类似n03"),
                        r("n05", "Na₂CO₃ + NaOH", "Na₂CO₃ + NaOH = 不反应", "与碱", note="不反应"),
                        r("n06", "Na₂CO₃ + CaCl₂", "Na₂CO₃ + CaCl₂ = CaCO₃↓ + 2NaCl", "与盐",
                          phenomenon="白色沉淀", note="💯 检验CO₃²⁻的方法"),
                        r("n07", "Na₂CO₃ + BaCl₂", "Na₂CO₃ + BaCl₂ = BaCO₃↓ + 3NaCl", "与盐",
                          phenomenon="白色沉淀", note="💯 同样可检验CO₃²⁻"),
                        r("n08", "Na₂CO₃ + CO₂ + H₂O", "Na₂CO₃ + H₂O + CO₂ = 2NaHCO₃", "与CO₂",
                          phenomenon="溶液变浑浊", note="制小苏打"),
                        r("n09", "CO₃²⁻水解", "CO₃²⁻ + H₂O ⇌ HCO₃⁻ + OH⁻", "水解",
                          note="💯 溶液显碱性，俗称纯碱"),
                        r("n10", "Na₂CO₃加热", "Na₂CO₃ 加热不分解", "热稳定性", note="💯 对比：NaHCO₃加热分解"),
                    ],
                },
                {
                    "id": "ch2_nahco3", "name": "NaHCO₃ 碳酸氢钠", "icon": "🥤",
                    "note": "白色细小晶体，可溶于水",
                    "reactions": [
                        r("h01", "NaHCO₃ + HCl", "NaHCO₃ + HCl = NaCl + H₂O + CO₂↑", "与酸",
                          phenomenon="直接冒气泡", note="💯 与Na₂CO₃对比"),
                        r("h02", "NaHCO₃ + NaOH", "NaHCO₃ + NaOH = Na₂CO₃ + H₂O", "与碱", note="酸式盐+碱=正盐"),
                        r("h03", "NaHCO₃少量 + Ca(OH)₂", "HCO₃⁻ + OH⁻ + Ca²⁺ = CaCO₃↓ + H₂O", "与碱",
                          phenomenon="白色沉淀", note="⚠ 注意量！少量"),
                        r("h04", "NaHCO₃过量 + Ca(OH)₂", "2HCO₃⁻ + 2OH⁻ + Ca²⁺ = CaCO₃↓ + CO₃²⁻ + 2H₂O", "与碱",
                          phenomenon="白色沉淀", note="⚠ 注意量！过量"),
                        r("h05", "NaHCO₃受热分解", "2NaHCO₃ =(加热) Na₂CO₃ + H₂O + CO₂↑", "分解",
                          phenomenon="水珠产生，气体使澄清石灰水变浑浊", note="💯 唯一受热易分解的钠盐！必考"),
                        r("h06", "NaHCO₃ + CO₂", "NaHCO₃ + CO₂ = 不反应", "与CO₂", note="不反应"),
                        r("h07", "NaHCO₃ + Na₂CO₃", "NaHCO₃ + Na₂CO₃ = 不反应", "与碳酸钠", note="不反应"),
                        r("h08", "HCO₃⁻水解", "HCO₃⁻ + H₂O ⇌ H₂CO₃ + OH⁻", "水解",
                          note="💯 碱性：Na₂CO₃ > NaHCO₃"),
                        r("h09", "Na₂CO₃=NaHCO₃", "Na₂CO₃ + CO₂ + H₂O = 2NaHCO₃", "转化",
                          phenomenon="溶液变浑浊", note="通CO₂"),
                        r("h10", "NaHCO₃=Na₂CO₃", "NaHCO₃ + NaOH = Na₂CO₃ + H₂O", "转化", note="加碱"),
                    ],
                },
            ],
        },
        {
            "id": "ch2_cl",
            "name": "氯及其化合物",
            "substances": [
                {
                    "id": "ch2_cl2", "name": "Cl₂ 氯气", "icon": "🟢",
                    "note": "黄绿色、刺激性气味、有毒、密度>空气",
                    "reactions": [
                        r("cl1", "Cl₂ + Cu", "Cu + Cl₂ =(点燃) CuCl₂", "与金属",
                          phenomenon="棕黄色烟", note="⚠ 产物颜色：棕黄色"),
                        r("cl2", "Cl₂ + H₂", "H₂ + Cl₂ =(点燃) 2HCl", "与非金属",
                          phenomenon="苍白色火焰，瓶口白雾", note="💯 苍白色火焰"),
                        r("cl3", "Cl₂ + H₂O", "Cl₂ + H₂O ⇌ HCl + HClO", "与水", note="💯 可逆反应！"),
                        r("cl4", "Cl₂ + NaOH", "Cl₂ + 2NaOH = NaCl + NaClO + H₂O", "与碱", note="制84消毒液"),
                        r("cl5", "Cl₂ + Ca(OH)₂", "2Cl₂ + 2Ca(OH)₂ = CaCl₂ + Ca(ClO)₂ + 2H₂O", "与碱",
                          note="制漂白粉"),
                        r("cl6", "Cl₂ + Fe", "2Fe + 3Cl₂ =(点燃) 2FeCl₃", "与金属",
                          phenomenon="棕褐色烟", note="⚠ 生成Fe³⁺ 不是Fe²⁺"),
                        r("cl7", "Cl₂ + NaBr", "Cl₂ + 2NaBr = 2NaCl + Br₂", "置换",
                          phenomenon="溶液变橙黄色", note="💯 氧化性：Cl₂ > Br₂"),
                        r("cl8", "Cl₂ + KI", "Cl₂ + 2KI = 2KCl + I₂", "置换",
                          phenomenon="溶液变棕黄，淀粉变蓝", note="💯 氧化性：Cl₂ > I₂"),
                    ],
                },
                {
                    "id": "ch2_hclo", "name": "HClO 次氯酸", "icon": "🧴",
                    "note": "弱酸性、强氧化性、漂白性（不可逆）",
                    "reactions": [
                        r("hclo1", "HClO 光照分解", "2HClO =(光照) 2HCl + O₂↑", "分解",
                          phenomenon="氯水颜色变浅", note="💯 氯水需避光保存"),
                    ],
                },
                {
                    "id": "ch2_nacl", "name": "NaCl 氯化钠", "icon": "🧂",
                    "note": "白色晶体，易溶于水",
                    "reactions": [
                        r("nacl1", "电解饱和食盐水", "2NaCl + 2H₂O =(电解) 2NaOH + H₂↑ + Cl₂↑", "电解",
                          phenomenon="阴极H₂无色、阳极Cl₂黄绿色", note="💯 氯碱工业"),
                    ],
                },
            ],
        },
    ],
}
chapters.append(ch2)
print("ch2 done")

print(f'Total chapters built: {len(chapters)}')

# Write JSON
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)
print(f'Wrote {OUT}')
print(f'Size: {os.path.getsize(OUT)} bytes')
