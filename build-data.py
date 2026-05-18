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

# ====== ch3 ======
ch3 = {
    "id": "ch3",
    "name": "第三章 铁 金属材料",
    "sections": [
        {
            "id": "ch3_fe",
            "name": "铁及其化合物",
            "substances": [
                {
                    "id": "ch3_fe_metal", "name": "Fe 铁单质", "icon": "🔩",
                    "note": "纯铁银白色，有延展性，可被磁铁吸引",
                    "reactions": [
                        r("ch3_fe1", "Fe + O₂（点燃）", "3Fe + 2O₂ =(点燃) Fe₃O₄", "与氧气",
                          phenomenon="剧烈燃烧，火星四射，生成黑色固体", note="💯 产物为Fe₃O₄，不是Fe₂O₃！"),
                        r("ch3_fe2", "Fe + Cl₂（点燃）", "2Fe + 3Cl₂ =(点燃) 2FeCl₃", "与氯气",
                          phenomenon="棕褐色烟", note="⚠ 生成Fe³⁺ 不是Fe²⁺"),
                        r("ch3_fe3", "Fe + S（加热）", "Fe + S =(加热) FeS", "与硫",
                          phenomenon="黑色固体生成", note="⚠ 生成FeS 不是Fe₂S₃"),
                        r("ch3_fe4", "Fe + HCl", "Fe + 2HCl = FeCl₂ + H₂↑", "与酸",
                          phenomenon="铁溶解，产生气泡，溶液变浅绿色", note="💯 生成Fe²⁺ 浅绿色"),
                        r("ch3_fe5", "Fe + H₂SO₄（稀）", "Fe + H₂SO₄ = FeSO₄ + H₂↑", "与酸",
                          phenomenon="铁溶解，产生气泡", note="💯 钝化现象：常温浓H₂SO₄/HNO₃"),
                        r("ch3_fe6", "Fe + CuSO₄", "Fe + CuSO₄ = FeSO₄ + Cu", "置换",
                          phenomenon="铁表面析出红色固体，溶液由蓝色变浅绿色", note="💯 湿法炼铜原理"),
                        r("ch3_fe7", "Fe + H₂O（高温）", "3Fe + 4H₂O =(高温) Fe₃O₄ + 4H₂↑", "与水",
                          phenomenon="生成黑色固体，产生可燃性气体", note="⚠ 高温！不是Fe₂O₃"),
                    ],
                },
                {
                    "id": "ch3_feo", "name": "FeO 氧化亚铁", "icon": "⬛",
                    "note": "黑色固体，碱性氧化物，不稳定空气中易氧化",
                    "reactions": [
                        r("ch3_feo1", "FeO + HCl", "FeO + 2HCl = FeCl₂ + H₂O", "与酸", note="生成Fe²⁺"),
                        r("ch3_feo2", "FeO + H₂SO₄（稀）", "FeO + H₂SO₄ = FeSO₄ + H₂O", "与酸", note="碱性氧化物通性"),
                    ],
                },
                {
                    "id": "ch3_fe2o3", "name": "Fe₂O₃ 氧化铁", "icon": "🟤",
                    "note": "红棕色固体，俗称铁锈、铁红，碱性氧化物",
                    "reactions": [
                        r("ch3_fe2o3_1", "Fe₂O₃ + HCl", "Fe₂O₃ + 6HCl = 2FeCl₃ + 3H₂O", "与酸",
                          phenomenon="红棕色固体溶解，溶液变黄色", note="⚠ 生成Fe³⁺ 黄色溶液"),
                        r("ch3_fe2o3_2", "Fe₂O₃ + H₂SO₄", "Fe₂O₃ + 3H₂SO₄ = Fe₂(SO₄)₃ + 3H₂O", "与酸", note="碱性氧化物通性"),
                        r("ch3_fe2o3_3", "Fe₂O₃ + CO（炼铁）", "Fe₂O₃ + 3CO =(高温) 2Fe + 3CO₂", "还原",
                          phenomenon="红棕色粉末变黑", note="💯 高炉炼铁原理！"),
                        r("ch3_fe2o3_4", "Fe₂O₃ + Al（铝热）", "Fe₂O₃ + 2Al =(高温) Al₂O₃ + 2Fe", "铝热反应",
                          phenomenon="剧烈反应，放出大量热，铁水流出", note="💯 焊接铁轨"),
                    ],
                },
                {
                    "id": "ch3_fe3o4", "name": "Fe₃O₄ 四氧化三铁", "icon": "⚫",
                    "note": "黑色固体，磁铁矿，有磁性，可写成FeO·Fe₂O₃",
                    "reactions": [
                        r("ch3_fe3o4_1", "Fe₃O₄ + HCl", "Fe₃O₄ + 8HCl = FeCl₂ + 2FeCl₃ + 4H₂O", "与酸", note="生成Fe²⁺ + 2Fe³⁺"),
                    ],
                },
                {
                    "id": "ch3_fecl2", "name": "FeCl₂ 氯化亚铁", "icon": "🟢",
                    "note": "浅绿色溶液（水合Fe²⁺），Fe²⁺显还原性",
                    "reactions": [
                        r("ch3_fecl2_1", "FeCl₂ + Cl₂", "2FeCl₂ + Cl₂ = 2FeCl₃", "氧化",
                          phenomenon="溶液由浅绿色变黄色", note="💯 Fe²⁺被氧化为Fe³⁺"),
                        r("ch3_fecl2_2", "FeCl₂ + NaOH", "FeCl₂ + 2NaOH = Fe(OH)₂↓ + 2NaCl", "沉淀",
                          phenomenon="白色沉淀→灰绿色→红褐色", note="💯 Fe(OH)₂特征颜色变化！必考"),
                        r("ch3_fecl2_3", "FeCl₂ + KSCN", "FeCl₂ + KSCN → 不变红色", "检验",
                          phenomenon="溶液无明显变化", note="💯 Fe²⁺遇KSCN不变色"),
                    ],
                },
                {
                    "id": "ch3_fecl3", "name": "FeCl₃ 氯化铁", "icon": "🟡",
                    "note": "棕黄色溶液（水合Fe³⁺），Fe³⁺显氧化性",
                    "reactions": [
                        r("ch3_fecl3_1", "FeCl₃ + Fe", "2FeCl₃ + Fe = 3FeCl₂", "还原",
                          phenomenon="溶液由棕色变浅绿色", note="💯 刻蚀电路板原理！"),
                        r("ch3_fecl3_2", "FeCl₃ + Cu", "2FeCl₃ + Cu = 2FeCl₂ + CuCl₂", "氧化",
                          phenomenon="Cu溶解，溶液颜色变化", note="💯 刻蚀印刷电路板"),
                        r("ch3_fecl3_3", "FeCl₃ + NaOH", "FeCl₃ + 3NaOH = Fe(OH)₃↓ + 3NaCl", "沉淀",
                          phenomenon="红褐色沉淀", note="⚠ 直接生成红褐色"),
                        r("ch3_fecl3_4", "FeCl₃ + KSCN", "FeCl₃ + 3KSCN = Fe(SCN)₃ + 3KCl", "检验",
                          phenomenon="溶液变血红色", note="💯 特征反应！必考"),
                        r("ch3_fecl3_5", "FeCl₃ + KI", "2FeCl₃ + 2KI = 2FeCl₂ + I₂ + 2KCl", "氧化还原",
                          phenomenon="溶液变棕黄色，淀粉变蓝", note="💯 Fe³⁺氧化性 > I₂"),
                    ],
                },
                {
                    "id": "ch3_feoh2", "name": "Fe(OH)₂ 氢氧化亚铁", "icon": "⬜",
                    "note": "白色沉淀，极易被氧化",
                    "reactions": [
                        r("ch3_feoh2_1", "Fe(OH)₂ + O₂ + H₂O", "4Fe(OH)₂ + O₂ + 2H₂O = 4Fe(OH)₃", "氧化",
                          phenomenon="白色→灰绿色→红褐色", note="💯 特征颜色变化！制备时要隔离O₂"),
                        r("ch3_feoh2_2", "Fe(OH)₂ + HCl", "Fe(OH)₂ + 2HCl = FeCl₂ + 2H₂O", "与酸", note="生成Fe²⁺"),
                    ],
                },
                {
                    "id": "ch3_feoh3", "name": "Fe(OH)₃ 氢氧化铁", "icon": "🟤",
                    "note": "红褐色沉淀",
                    "reactions": [
                        r("ch3_feoh3_1", "Fe(OH)₃ + HCl", "Fe(OH)₃ + 3HCl = FeCl₃ + 3H₂O", "与酸", note="中和反应"),
                        r("ch3_feoh3_2", "Fe(OH)₃加热分解", "2Fe(OH)₃ =(加热) Fe₂O₃ + 3H₂O", "分解",
                          phenomenon="红褐色固体变为红棕色", note="⚠ 注意颜色变化"),
                    ],
                },
            ],
        },
        {
            "id": "ch3_metal",
            "name": "金属材料",
            "substances": [
                {
                    "id": "ch3_al", "name": "Al 铝", "icon": "🪞",
                    "note": "银白色金属、密度小、有延展性、表面有致密氧化膜",
                    "reactions": [
                        r("ch3_al1", "Al + O₂", "4Al + 3O₂ = 2Al₂O₃", "与氧气",
                          phenomenon="铝表面变暗，生成致密氧化膜", note="💯 致密氧化膜使铝耐腐蚀"),
                        r("ch3_al2", "Al + HCl", "2Al + 6HCl = 2AlCl₃ + 3H₂↑", "与酸",
                          phenomenon="铝逐渐溶解，产生气泡", note="💯 铝与酸反应生成H₂"),
                        r("ch3_al3", "Al + NaOH", "2Al + 2NaOH + 2H₂O = 2NaAlO₂ + 3H₂↑", "与碱",
                          phenomenon="铝逐渐溶解，产生气泡", note="💯 铝的两性体现！大多数金属不与碱反应"),
                        r("ch3_al4", "铝热反应", "2Al + Fe₂O₃ =(高温) Al₂O₃ + 2Fe", "铝热反应",
                          phenomenon="剧烈反应，放出大量热，铁水流出", note="💯 冶炼金属/焊接铁轨"),
                    ],
                },
                {
                    "id": "ch3_al2o3", "name": "Al₂O₃ 氧化铝", "icon": "⬜",
                    "note": "白色固体，两性氧化物，熔点高（耐火材料）",
                    "reactions": [
                        r("ch3_al2o3_1", "Al₂O₃ + HCl", "Al₂O₃ + 6HCl = 2AlCl₃ + 3H₂O", "与酸",
                          note="💯 两性体现"),
                        r("ch3_al2o3_2", "Al₂O₃ + NaOH", "Al₂O₃ + 2NaOH = 2NaAlO₂ + H₂O", "与碱",
                          note="💯 两性氧化物！必考"),
                        r("ch3_al2o3_3", "Al₂O₃电解", "2Al₂O₃ =(电解/冰晶石) 4Al + 3O₂↑", "电解",
                          note="💯 工业炼铝，加冰晶石降低熔点"),
                    ],
                },
                {
                    "id": "ch3_aloh3", "name": "Al(OH)₃ 氢氧化铝", "icon": "⬜",
                    "note": "白色胶状沉淀，两性氢氧化物",
                    "reactions": [
                        r("ch3_aloh3_1", "Al(OH)₃ + HCl", "Al(OH)₃ + 3HCl = AlCl₃ + 3H₂O", "与酸",
                          phenomenon="白色沉淀溶解", note="💯 两性体现"),
                        r("ch3_aloh3_2", "Al(OH)₃ + NaOH", "Al(OH)₃ + NaOH = NaAlO₂ + 2H₂O", "与碱",
                          phenomenon="白色沉淀溶解", note="💯 两性氢氧化物！高考必考"),
                        r("ch3_aloh3_3", "Al(OH)₃加热分解", "2Al(OH)₃ =(加热) Al₂O₃ + 3H₂O", "分解",
                          note="不溶性碱受热分解"),
                    ],
                },
            ],
        },
    ],
}
chapters.append(ch3)
print("ch3 done")

# ====== ch4 ======
ch4 = {
    "id": "ch4",
    "name": "第四章 物质结构 元素周期律",
    "sections": [
        {
            "id": "ch4_structure",
            "name": "原子结构与元素周期表",
            "substances": [
                {
                    "id": "ch4_atom", "name": "原子结构", "icon": "⚛️",
                    "note": "原子核(质子+中子)+核外电子；质量数=质子数+中子数",
                    "reactions": [],
                },
                {
                    "id": "ch4_isotope", "name": "同位素", "icon": "🔬",
                    "note": "质子数相同、中子数不同的原子互称同位素",
                    "reactions": [],
                },
                {
                    "id": "ch4_periodic", "name": "元素周期表", "icon": "📊",
                    "note": "7周期(短1-3，长4-7)；16族(7主+7副+Ⅷ+0)",
                    "reactions": [],
                },
            ],
        },
        {
            "id": "ch4_law",
            "name": "元素周期律",
            "substances": [
                {
                    "id": "ch4_trend", "name": "周期律", "icon": "📈",
                    "note": "原子半径：同周期左→右递减；同主族上→下递增。金属性：同周期左→右减弱。非金属性：同周期左→右增强",
                    "reactions": [],
                },
            ],
        },
        {
            "id": "ch4_bond",
            "name": "化学键",
            "substances": [
                {
                    "id": "ch4_ionic", "name": "离子键", "icon": "🔗",
                    "note": "阴、阳离子间的静电作用，如NaCl、MgO",
                    "reactions": [],
                },
                {
                    "id": "ch4_covalent", "name": "共价键", "icon": "🔗",
                    "note": "原子间通过共用电子对形成。非极性(同种原子)；极性(不同原子)",
                    "reactions": [],
                },
                {
                    "id": "ch4_intermolecular", "name": "分子间作用力", "icon": "💨",
                    "note": "范德华力+氢键(使H₂O沸点异常高)",
                    "reactions": [],
                },
            ],
        },
    ],
}
chapters.append(ch4)
print("ch4 done")

# ====== ch5 (必修二第五章 非金属元素) ======
ch5 = {
    "id": "ch5",
    "name": "第五章 化工生产中的重要非金属元素",
    "sections": [
        {
            "id": "ch5_s",
            "name": "硫及其化合物",
            "substances": [
                {
                    "id": "ch5_so2", "name": "SO₂ 二氧化硫", "icon": "💨",
                    "note": "无色有刺激性气味气体，有毒，易溶于水(1:40)",
                    "reactions": [
                        r("ch5_so2_1", "SO₂ + H₂O", "SO₂ + H₂O ⇌ H₂SO₃", "与水", note="💯 酸性氧化物通性，可逆反应"),
                        r("ch5_so2_2", "SO₂ + NaOH（少量）", "SO₂ + 2NaOH = Na₂SO₃ + H₂O", "与碱", note="尾气吸收"),
                        r("ch5_so2_3", "SO₂ + NaOH（过量）", "SO₂ + NaOH = NaHSO₃", "与碱", note="生成亚硫酸氢钠"),
                        r("ch5_so2_4", "SO₂ + O₂", "2SO₂ + O₂ ⇌ 2SO₃", "氧化", note="💯 工业制硫酸第二步，催化剂/加热"),
                        r("ch5_so2_5", "SO₂ + KMnO₄（酸性）", "5SO₂ + 2KMnO₄ + 2H₂O = K₂SO₄ + 2MnSO₄ + 2H₂SO₄", "还原性",
                          phenomenon="紫红色褪去", note="💯 体现SO₂还原性，区别于漂白性"),
                        r("ch5_so2_6", "SO₂ + 品红", "SO₂ 使品红褪色（加热复原）", "漂白性",
                          phenomenon="品红溶液褪色，加热后恢复红色", note="💯 可逆漂白！区别于Cl₂的不可逆漂白"),
                    ],
                },
                {
                    "id": "ch5_h2so4", "name": "H₂SO₄(浓) 浓硫酸", "icon": "🧪",
                    "note": "无色油状液体，吸水性(干燥剂)、脱水性(碳化)、强氧化性",
                    "reactions": [
                        r("ch5_h2so4_1", "Cu + H₂SO₄(浓)", "Cu + 2H₂SO₄(浓) =(加热) CuSO₄ + SO₂↑ + 2H₂O", "强氧化性",
                          phenomenon="铜溶解，产生刺激性气味气体，溶液变蓝色", note="💯 浓硫酸强氧化性！必考"),
                        r("ch5_h2so4_2", "C + H₂SO₄(浓)", "C + 2H₂SO₄(浓) =(加热) CO₂↑ + 2SO₂↑ + 2H₂O", "强氧化性",
                          phenomenon="碳逐渐消失，产生无色有刺激性气味气体", note="💯 产物检验：先品红→KMnO₄→品红→澄清石灰水"),
                        r("ch5_h2so4_3", "Fe/Al + H₂SO₄(浓/常温)", "Fe(Al) + H₂SO₄(浓) =(常温) 钝化", "钝化",
                          note="💯 常温钝化，可用铁罐/铝罐运输浓硫酸"),
                        r("ch5_h2so4_4", "蔗糖+浓硫酸", "C₁₂H₂₂O₁₁ =(浓H₂SO₄) 12C + 11H₂O", "脱水性",
                          phenomenon="蔗糖变黑(脱水)，体积膨胀(生成气体)", note="⚠ 脱水性(化学变化)区别于吸水性(物理)"),
                    ],
                },
            ],
        },
        {
            "id": "ch5_n",
            "name": "氮及其化合物",
            "substances": [
                {
                    "id": "ch5_n2", "name": "N₂ 氮气", "icon": "💨",
                    "note": "无色无味气体，N≡N结构稳定，常温不活泼",
                    "reactions": [
                        r("ch5_n2_1", "N₂ + O₂", "N₂ + O₂ =(放电) 2NO", "与氧气", note="💯 放电/高温条件，闪电固氮"),
                        r("ch5_n2_2", "N₂ + H₂", "N₂ + 3H₂ ⇌(催化剂/高温高压) 2NH₃", "与氢气", note="💯 工业合成氨！可逆反应"),
                    ],
                },
                {
                    "id": "ch5_nh3", "name": "NH₃ 氨", "icon": "💨",
                    "note": "无色有刺激性气味气体，极易溶于水(1:700)，碱性气体",
                    "reactions": [
                        r("ch5_nh3_1", "NH₃ + H₂O", "NH₃ + H₂O ⇌ NH₃·H₂O ⇌ NH₄⁺ + OH⁻", "与水",
                          phenomenon="形成喷泉，溶液显碱性", note="💯 氨溶于水显碱性，但NH₃·H₂O是弱碱"),
                        r("ch5_nh3_2", "NH₃ + HCl", "NH₃ + HCl = NH₄Cl", "与酸",
                          phenomenon="产生大量白烟", note="💯 检验NH₃的方法"),
                        r("ch5_nh3_3", "NH₃催化氧化", "4NH₃ + 5O₂ =(催化剂/加热) 4NO + 6H₂O", "催化氧化",
                          note="💯 工业制硝酸第一步！必考"),
                        r("ch5_nh3_4", "实验室制NH₃", "2NH₄Cl + Ca(OH)₂ =(加热) CaCl₂ + 2NH₃↑ + 2H₂O", "制备",
                          note="💯 固+固加热，向下排空气法收集"),
                        r("ch5_nh3_5", "NH₄Cl加热", "NH₄Cl =(加热) NH₃↑ + HCl↑", "分解",
                          note="⚠ 遇冷又化合生成NH₄Cl，不是升华"),
                        r("ch5_nh3_6", "NH₃ + CO₂ + NaCl + H₂O", "NH₃ + CO₂ + NaCl + H₂O = NaHCO₃↓ + NH₄Cl", "侯氏制碱",
                          note="💯 侯德榜制碱法，先通NH₃再通CO₂"),
                    ],
                },
                {
                    "id": "ch5_hno3", "name": "HNO₃ 硝酸", "icon": "🧪",
                    "note": "无色有刺激性气味液体，强酸，强氧化性，见光分解",
                    "reactions": [
                        r("ch5_hno3_1", "Cu + HNO₃(浓)", "Cu + 4HNO₃(浓) = Cu(NO₃)₂ + 2NO₂↑ + 2H₂O", "强氧化性",
                          phenomenon="铜溶解，产生红棕色气体，溶液变蓝色", note="💯 浓硝酸生成NO₂，稀硝酸生成NO"),
                        r("ch5_hno3_2", "Cu + HNO₃(稀)", "3Cu + 8HNO₃(稀) = 3Cu(NO₃)₂ + 2NO↑ + 4H₂O", "强氧化性",
                          phenomenon="铜溶解，产生无色气体(遇空气变红棕色)，溶液变蓝色", note="💯 稀硝酸生成NO"),
                        r("ch5_hno3_3", "C + HNO₃(浓)", "C + 4HNO₃(浓) =(加热) CO₂↑ + 4NO₂↑ + 2H₂O", "强氧化性", note="碳被氧化"),
                        r("ch5_hno3_4", "Fe/Al + HNO₃(浓/常温)", "Fe(Al) + HNO₃(浓) =(常温) 钝化", "钝化", note="💯 常温钝化"),
                        r("ch5_hno3_5", "HNO₃见光分解", "4HNO₃ =(光照/加热) 4NO₂↑ + O₂↑ + 2H₂O", "分解",
                          note="💯 硝酸常呈黄色(溶有NO₂)，需避光保存"),
                    ],
                },
            ],
        },
    ],
}
chapters.append(ch5)
print("ch5 done")

# ====== ch6 (必修二第六章 化学反应与能量) ======
ch6 = {
    "id": "ch6",
    "name": "第六章 化学反应与能量",
    "sections": [
        {
            "id": "ch6_energy",
            "name": "化学反应与能量变化",
            "substances": [
                {
                    "id": "ch6_heat", "name": "放热与吸热", "icon": "🔥",
                    "note": "放热(ΔH<0)：金属+酸/中和/燃烧。吸热(ΔH>0)：Ba(OH)₂·8H₂O+NH₄Cl/C+CO₂/分解",
                    "reactions": [
                        r("ch6_heat1", "Ba(OH)₂·8H₂O+NH₄Cl", "Ba(OH)₂·8H₂O + 2NH₄Cl = BaCl₂ + 2NH₃↑ + 10H₂O", "吸热反应",
                          phenomenon="烧杯底部结冰(吸热)", note="💯 典型吸热反应！必考"),
                    ],
                },
                {
                    "id": "ch6_battery", "name": "原电池", "icon": "🔋",
                    "note": "负极(活泼金属)→失e⁻→氧化；正极→得e⁻→还原。电子：负极→外电路→正极",
                    "reactions": [
                        r("ch6_batt1", "Zn-Cu原电池", "负极：Zn - 2e⁻ = Zn²⁺   正极：2H⁺ + 2e⁻ = H₂↑", "原电池",
                          phenomenon="Zn片溶解，Cu片上有气泡产生，电流表指针偏转", note="💯 负极Zn被氧化，正极H⁺被还原"),
                    ],
                },
            ],
        },
        {
            "id": "ch6_rate",
            "name": "化学反应的速率与限度",
            "substances": [
                {
                    "id": "ch6_equilibrium", "name": "化学平衡", "icon": "⚖️",
                    "note": "v正=v逆≠0，各组分量不变(逆等动定变)。勒夏特列原理：改变条件→平衡向减弱该改变的方向移动",
                    "reactions": [],
                },
            ],
        },
    ],
}
chapters.append(ch6)
print("ch6 done")

# ====== ch7 (必修二第七章 有机化合物) ======
ch7 = {
    "id": "ch7",
    "name": "第七章 有机化合物",
    "sections": [
        {
            "id": "ch7_alkane",
            "name": "认识有机化合物",
            "substances": [
                {
                    "id": "ch7_ch4", "name": "CH₄ 甲烷", "icon": "💧",
                    "note": "正四面体结构；无色无味气体，难溶于水，烷烃通式CₙH₂ₙ₊₂",
                    "reactions": [
                        r("ch7_ch4_1", "CH₄ + Cl₂", "CH₄ + Cl₂ →(光照) CH₃Cl + HCl", "取代",
                          note="💯 逐步取代，产物为混合物：CH₃Cl/CH₂Cl₂/CHCl₃/CCl₄"),
                        r("ch7_ch4_2", "CH₄燃烧", "CH₄ + 2O₂ →(点燃) CO₂ + 2H₂O", "燃烧",
                          phenomenon="蓝色火焰", note="完全燃烧"),
                    ],
                },
            ],
        },
        {
            "id": "ch7_alkene",
            "name": "乙烯与高分子材料",
            "substances": [
                {
                    "id": "ch7_c2h4", "name": "C₂H₄ 乙烯", "icon": "🔬",
                    "note": "含碳碳双键(C=C)，使KMnO₄褪色，植物生长调节剂",
                    "reactions": [
                        r("ch7_c2h4_1", "C₂H₄ + Br₂", "CH₂=CH₂ + Br₂ → CH₂BrCH₂Br", "加成",
                          phenomenon="溴水褪色", note="💯 加成反应，溴水褪色"),
                        r("ch7_c2h4_2", "乙烯加聚", "nCH₂=CH₂ →(催化剂) [CH₂-CH₂]ₙ", "加聚",
                          note="💯 生成聚乙烯(PE)"),
                        r("ch7_c2h4_3", "C₂H₄ + H₂O", "CH₂=CH₂ + H₂O →(催化剂/加热加压) CH₃CH₂OH", "加成",
                          note="💯 工业制乙醇"),
                    ],
                },
            ],
        },
        {
            "id": "ch7_alcohol",
            "name": "乙醇与乙酸",
            "substances": [
                {
                    "id": "ch7_ethanol", "name": "C₂H₅OH 乙醇", "icon": "🍺",
                    "note": "官能团：-OH(羟基)",
                    "reactions": [
                        r("ch7_eth_1", "C₂H₅OH + Na", "2CH₃CH₂OH + 2Na → 2CH₃CH₂ONa + H₂↑", "与钠",
                          phenomenon="产生气泡(比水与钠反应缓和)", note="💯 -OH中H被置换"),
                        r("ch7_eth_2", "乙醇催化氧化", "2CH₃CH₂OH + O₂ →(Cu或Ag/△) 2CH₃CHO + 2H₂O", "催化氧化",
                          phenomenon="铜丝变黑(生成CuO)再变红(被还原)", note="💯 生成乙醛！醇→醛→酸"),
                        r("ch7_eth_3", "乙醇+乙酸（酯化）", "CH₃COOH + C₂H₅OH ⇌(浓H₂SO₄/△) CH₃COOC₂H₅ + H₂O", "酯化",
                          phenomenon="产生有果香味的油状液体", note="💯 酸脱羟基醇脱氢，浓硫酸催化吸水！必考"),
                    ],
                },
                {
                    "id": "ch7_acid", "name": "CH₃COOH 乙酸", "icon": "🧪",
                    "note": "官能团：-COOH(羧基)，弱酸性(>H₂CO₃)",
                    "reactions": [
                        r("ch7_ac_1", "CH₃COOH + Na₂CO₃", "2CH₃COOH + Na₂CO₃ → 2CH₃COONa + H₂O + CO₂↑", "酸性",
                          phenomenon="产生气泡", note="💯 强酸制弱酸，证明乙酸酸性>碳酸"),
                        r("ch7_ac_2", "CH₃COOH + NaOH", "CH₃COOH + NaOH → CH₃COONa + H₂O", "中和", note="中和反应"),
                    ],
                },
            ],
        },
        {
            "id": "ch7_nutrient",
            "name": "基本营养物质",
            "substances": [
                {
                    "id": "ch7_sugar", "name": "糖类", "icon": "🍬",
                    "note": "单糖(葡/果不水解)→二糖(蔗糖→葡+果；麦芽糖→2葡)→多糖(淀粉→遇I₂变蓝)",
                    "reactions": [
                        r("ch7_sug_1", "葡萄糖发酵", "C₆H₁₂O₆ →(酒化酶) 2C₂H₅OH + 2CO₂↑", "发酵", note="工业制酒原理"),
                    ],
                },
                {
                    "id": "ch7_protein", "name": "蛋白质", "icon": "🥩",
                    "note": "氨基酸→肽链；盐析(可逆)/变性(不可逆/加热/重金属盐)",
                    "reactions": [],
                },
                {
                    "id": "ch7_oil", "name": "油脂", "icon": "🫒",
                    "note": "高级脂肪酸甘油酯，可水解",
                    "reactions": [
                        r("ch7_oil_1", "油脂+NaOH（皂化）", "油脂 + 3NaOH →(△) 3高级脂肪酸钠 + 甘油", "皂化",
                          note="💯 制肥皂(高级脂肪酸钠)"),
                    ],
                },
            ],
        },
    ],
}
chapters.append(ch7)
print("ch7 done")

# ====== ch8 (必修二第八章 化学与可持续发展) ======
ch8 = {
    "id": "ch8",
    "name": "第八章 化学与可持续发展",
    "sections": [
        {
            "id": "ch8_resources",
            "name": "自然资源的开发利用",
            "substances": [
                {
                    "id": "ch8_metal", "name": "金属冶炼", "icon": "🔨",
                    "note": "热分解(Hg/Ag)→热还原(Fe/Cu)→电解(Na/Mg/Al)；活泼性越强越难冶炼",
                    "reactions": [
                        r("ch8_m1", "电解熔融NaCl", "2NaCl(熔融) =(电解) 2Na + Cl₂↑", "电解", note="💯 制钠"),
                        r("ch8_m2", "电解熔融MgCl₂", "MgCl₂(熔融) =(电解) Mg + Cl₂↑", "电解", note="💯 制镁"),
                        r("ch8_m3", "电解Al₂O₃", "2Al₂O₃ =(电解/冰晶石) 4Al + 3O₂↑", "电解", note="💯 制铝"),
                    ],
                },
                {
                    "id": "ch8_oil", "name": "石油与煤", "icon": "⛽",
                    "note": "石油：分馏(物理)、裂化裂解(化学)。煤：干馏(化学)、气化、液化",
                    "reactions": [],
                },
            ],
        },
        {
            "id": "ch8_green",
            "name": "绿色化学与环境保护",
            "substances": [
                {
                    "id": "ch8_greenchem", "name": "绿色化学", "icon": "🌿",
                    "note": "原子经济性(无副产物)；原子利用率=目标产物原子量/所有产物原子量×100%",
                    "reactions": [],
                },
                {
                    "id": "ch8_env", "name": "环境保护", "icon": "🌍",
                    "note": "酸雨(pH<5.6，SO₂+NOₓ)、温室效应(CO₂)、臭氧层破坏(氟氯烃)、水体富营养化(N/P)",
                    "reactions": [],
                },
            ],
        },
    ],
}
chapters.append(ch8)
print("ch8 done")

print(f'Total chapters built: {len(chapters)}')

# Write JSON
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(chapters, f, ensure_ascii=False, indent=2)
print(f'Wrote {OUT}')
print(f'Size: {os.path.getsize(OUT)} bytes')
