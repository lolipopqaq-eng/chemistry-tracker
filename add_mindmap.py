import sys, json
sys.stdout.reconfigure(encoding='utf-8')
raw = json.load(open('src/data/textbook-data.json', 'r', encoding='utf-8'))

mindmaps = {
    'ch1': {
        'title': '第一章 物质及其变化 · 总览',
        'root': {
            'icon': '🧪',
            'name': '物质及其变化',
            'children': [
                {
                    'icon': '📦',
                    'name': '物质的分类',
                    'children': [
                        {
                            'name': '纯净物',
                            'children': [
                                {
                                    'name': '单质',
                                    'children': [
                                        {'name': '金属（Na/Fe/Al/Cu）'},
                                        {'name': '非金属（O₂/Cl₂/S/N₂）'},
                                    ]
                                },
                                {
                                    'name': '化合物',
                                    'children': [
                                        {
                                            'name': '氧化物',
                                            'children': [
                                                {'name': '酸性（CO₂/SO₂/SO₃）'},
                                                {'name': '碱性（Na₂O/CaO/CuO）'},
                                                {'name': '两性（Al₂O₃）'},
                                                {'name': '不成盐（CO/NO）'},
                                            ]
                                        },
                                        {'name': '酸（HCl/H₂SO₄/HNO₃/CH₃COOH）'},
                                        {'name': '碱（NaOH/Ca(OH)₂/NH₃·H₂O）'},
                                        {'name': '盐（NaCl/Na₂CO₃/NaHCO₃/CuSO₄）'},
                                    ]
                                },
                            ]
                        },
                        {
                            'name': '混合物',
                            'children': [
                                {
                                    'name': '溶液（<1nm）',
                                    'children': [
                                        {'name': '均一稳定透明'},
                                        {'name': '无丁达尔效应'},
                                    ]
                                },
                                {
                                    'name': '胶体（1-100nm）',
                                    'children': [
                                        {'name': '介稳体系，有丁达尔效应'},
                                        {'name': '常见胶体：Fe(OH)₃/AgI/豆浆/云雾'},
                                        {'name': '聚沉：加热/加电解质/加相反胶体'},
                                        {'name': '应用：明矾净水/制豆腐/三角洲'},
                                    ]
                                },
                                {
                                    'name': '浊液（>100nm）',
                                    'children': [
                                        {'name': '悬浊液（泥水）'},
                                        {'name': '乳浊液（油水）'},
                                    ]
                                },
                            ]
                        },
                    ]
                },
                {
                    'icon': '⚡',
                    'name': '离子反应',
                    'children': [
                        {'name': '电解质：酸/碱/盐/活泼金属氧化物（水溶液或熔融导电）'},
                        {'name': '非电解质：大多数有机物/非金属氧化物/NH₃'},
                        {'name': '强电解质：完全电离（强酸/强碱/大部分盐）'},
                        {'name': '弱电解质：部分电离（弱酸/弱碱/H₂O）'},
                        {'name': '离子方程式：写→拆→删→查'},
                        {'name': '不拆：单质/气体/沉淀/弱电解质/氧化物'},
                    ]
                },
                {
                    'icon': '🔥',
                    'name': '氧化还原反应',
                    'children': [
                        {'name': '特征：化合价变化（判断依据）'},
                        {'name': '本质：电子转移（得失/偏移）'},
                        {'name': '口诀：升失氧化还原剂，降得还原氧化剂'},
                        {'name': '四大反应：置换（全部氧化还原），复分解（全部不是）'},
                        {'name': '氧化性：氧化剂>氧化产物'},
                        {'name': '还原性：还原剂>还原产物'},
                    ]
                },
            ]
        }
    },
    'ch2': {
        'title': '第二章 海水中的重要元素——钠和氯 · 总览',
        'root': {
            'icon': '🧪',
            'name': '钠和氯',
            'children': [
                {
                    'icon': '🥄',
                    'name': '钠及其化合物',
                    'children': [
                        {'name': 'Na（银白/质软/密度0.97/保存煤油）'},
                        {'name': 'Na₂O（氧化钠/白色）'},
                        {'name': 'Na₂O₂（过氧化钠/淡黄/供氧剂）'},
                        {'name': 'NaOH（烧碱/强碱/潮解）'},
                        {'name': 'Na₂CO₃（纯碱/苏打）'},
                        {'name': 'NaHCO₃（小苏打/热稳定性差）'},
                    ]
                },
                {
                    'icon': '🧫',
                    'name': '氯及其化合物',
                    'children': [
                        {'name': 'Cl₂（黄绿色/有毒/密度>空气）'},
                        {'name': 'HClO（次氯酸/弱酸/强氧化/漂白）'},
                        {'name': 'HCl（盐酸/强酸）'},
                    ]
                },
                {
                    'icon': '🧮',
                    'name': '物质的量',
                    'children': [
                        {'name': 'n=N/N_A；n=m/M；n=V/22.4'},
                        {'name': 'c=n/V；稀释c₁V₁=c₂V₂'},
                        {'name': '配制溶液：计算→称量→溶解→转移→洗涤→定容→摇匀'},
                    ]
                },
            ]
        }
    },
    'ch3': {
        'title': '第三章 铁 金属材料 · 总览',
        'root': {
            'icon': '🪨',
            'name': '铁和金属材料',
            'children': [
                {
                    'icon': '🪙',
                    'name': '铁及其化合物',
                    'children': [
                        {'name': 'Fe（银白/可变价+2/+3）'},
                        {'name': 'FeO（氧化亚铁/黑）'},
                        {'name': 'Fe₂O₃（铁红/赤铁矿/红棕）'},
                        {'name': 'Fe₃O₄（磁铁矿/黑/有磁性）'},
                        {'name': 'Fe(OH)₂（白→灰绿→红褐）'},
                        {'name': 'Fe(OH)₃（红褐沉淀）'},
                        {'name': 'Fe²⁺→Fe³⁺：Cl₂/O₂氧化'},
                        {'name': 'Fe³⁺检验：KSCN→血红色'},
                    ]
                },
                {
                    'icon': '🪶',
                    'name': '铝及其化合物',
                    'children': [
                        {'name': 'Al（银白/两性/与酸碱反应）'},
                        {'name': 'Al₂O₃（两性氧化物）'},
                        {'name': 'Al(OH)₃（两性氢氧化物）'},
                        {'name': '铝热反应：焊接铁轨'},
                    ]
                },
                {
                    'icon': '🔩',
                    'name': '金属材料',
                    'children': [
                        {'name': '合金：硬度↑熔点↓'},
                        {'name': '钢：碳素钢/合金钢'},
                    ]
                },
            ]
        }
    },
    'ch4': {
        'title': '第四章 物质结构 元素周期律 · 总览',
        'root': {
            'icon': '🔄',
            'name': '物质结构·周期律',
            'children': [
                {
                    'icon': '⚛️',
                    'name': '原子结构',
                    'children': [
                        {'name': '原子核（质子+中子）'},
                        {'name': '质量数=质子数+中子数'},
                        {'name': '核外电子排布：K2/L8/M18/N32'},
                        {'name': '最外层≤8，次外层≤18'},
                    ]
                },
                {
                    'icon': '📊',
                    'name': '元素周期表',
                    'children': [
                        {'name': '7周期（短123/长456/不完全7）'},
                        {'name': '16族（主7+副7+VIII+0）'},
                        {'name': '同周期左→右：金属性↓非金属性↑半径↓'},
                        {'name': '同主族上→下：金属性↑非金属性↓半径↑'},
                    ]
                },
                {
                    'icon': '🔗',
                    'name': '化学键',
                    'children': [
                        {'name': '离子键：阴阳离子间静电（NaCl/MgO/NaOH）'},
                        {'name': '共价键：共用电子对（极性/非极性）'},
                        {'name': '分子间力（范德华+氢键：H₂O/NH₃/HF）'},
                    ]
                },
            ]
        }
    },
    'ch5': {
        'title': '第五章 化工生产中的重要非金属元素 · 总览',
        'root': {
            'icon': '🧪',
            'name': '非金属元素',
            'children': [
                {
                    'icon': '🟡',
                    'name': '硫及其化合物',
                    'children': [
                        {'name': 'S（硫磺/黄/不溶水/溶CS₂）'},
                        {'name': 'SO₂（无色刺激/有毒/可逆漂白）'},
                        {'name': 'H₂SO₄（浓）：吸水/脱水/强氧化'},
                    ]
                },
                {
                    'icon': '💨',
                    'name': '氮及其化合物',
                    'children': [
                        {'name': 'N₂（稳定/N≡N/占空气78%）'},
                        {'name': 'NH₃（无色刺激/极易溶1:700）'},
                        {'name': 'NO（无色毒）/NO₂（红棕刺激毒）'},
                        {'name': 'HNO₃（硝酸/强氧化/见光分解）'},
                    ]
                },
                {
                    'icon': '💎',
                    'name': '硅及其化合物',
                    'children': [
                        {'name': 'Si（半导体/芯片）'},
                        {'name': 'SiO₂（石英/原子晶体/光导纤维）'},
                        {'name': '硅酸盐：陶瓷/玻璃/水泥'},
                    ]
                },
            ]
        }
    },
    'ch6': {
        'title': '第六章 化学反应与能量 · 总览',
        'root': {
            'icon': '⚡',
            'name': '化学反应与能量',
            'children': [
                {
                    'icon': '🔥',
                    'name': '化学反应与热能',
                    'children': [
                        {'name': '放热反应（燃烧/中和/金属+酸/多化合）'},
                        {'name': '吸热反应（多分解/Ba(OH)₂+NH₄Cl/C+CO₂）'},
                        {'name': 'ΔH=生成物总能量-反应物总能量'},
                    ]
                },
                {
                    'icon': '🔋',
                    'name': '原电池',
                    'children': [
                        {'name': '化学能→电能'},
                        {'name': '负极（活泼金属）失e⁻氧化'},
                        {'name': '正极（不活泼）得e⁻还原'},
                        {'name': '盐桥：平衡电荷/闭合回路'},
                    ]
                },
                {
                    'icon': '⚖️',
                    'name': '化学反应的速率和限度',
                    'children': [
                        {'name': '速率影响：浓度↑温度↑压强↑催化剂+→速↑'},
                        {'name': '化学平衡：v正=v逆≠0'},
                        {'name': '勒夏特列原理'},
                    ]
                },
            ]
        }
    },
    'ch7': {
        'title': '第七章 有机化合物 · 总览',
        'root': {
            'icon': '🧬',
            'name': '有机化合物',
            'children': [
                {
                    'icon': '🔵',
                    'name': '甲烷与烷烃',
                    'children': [
                        {'name': 'CₙH₂ₙ₊₂；正四面体'},
                        {'name': '取代反应（光照Cl₂）'},
                    ]
                },
                {
                    'icon': '🟢',
                    'name': '乙烯与烯烃',
                    'children': [
                        {'name': 'CₙH₂ₙ；平面120°'},
                        {'name': '加成反应（Br₂/H₂/H₂O）'},
                        {'name': '加聚反应→聚乙烯PE'},
                    ]
                },
                {
                    'icon': '🍷',
                    'name': '乙醇与乙酸',
                    'children': [
                        {'name': '乙醇：与Na/催化氧化/酯化'},
                        {'name': '乙酸：弱酸性/酯化反应'},
                    ]
                },
                {
                    'icon': '🍞',
                    'name': '基本营养物质',
                    'children': [
                        {'name': '糖类（葡萄糖/淀粉/蔗糖）'},
                        {'name': '油脂（皂化反应）'},
                        {'name': '蛋白质（盐析可逆/变性不可逆）'},
                    ]
                },
            ]
        }
    },
    'ch8': {
        'title': '第八章 化学与可持续发展 · 总览',
        'root': {
            'icon': '🌍',
            'name': '化学与可持续发展',
            'children': [
                {
                    'icon': '🏭',
                    'name': '自然资源的开发利用',
                    'children': [
                        {'name': '金属冶炼：电解K→Al/热还原Zn→Cu/热分解Hg→Ag'},
                        {'name': '海水提溴：Cl₂氧化Br⁻→空气吹出'},
                        {'name': '海水提镁：MgCl₂熔融电解'},
                    ]
                },
                {
                    'icon': '💊',
                    'name': '化学品的合理使用',
                    'children': [
                        {'name': '化肥（N/P/K）'},
                        {'name': '农药（有机磷/拟除虫菊酯）'},
                        {'name': '食品添加剂（防腐/抗氧化/膨松）'},
                    ]
                },
                {
                    'icon': '🌿',
                    'name': '绿色化学',
                    'children': [
                        {'name': '原子经济性（100%利用）'},
                        {'name': '酸雨（pH<5.6）/温室效应/臭氧层'},
                    ]
                },
            ]
        }
    },
    'ch9': {
        'title': '选修一 化学反应原理 · 总览',
        'root': {
            'icon': '⚡',
            'name': '化学反应原理',
            'children': [
                {
                    'icon': '🔥',
                    'name': '反应热',
                    'children': [
                        {'name': '焓变ΔH=生成物能量-反应物能量'},
                        {'name': '盖斯定律：ΔH与路径无关'},
                        {'name': '热化学方程式需标状态和ΔH'},
                        {'name': '燃烧热/中和热（ΔH=-57.3kJ/mol）'},
                    ]
                },
                {
                    'icon': '⏱️',
                    'name': '速率与平衡',
                    'children': [
                        {'name': 'v=Δc/Δt；速率比=系数比'},
                        {'name': 'K只与温度有关'},
                        {'name': '勒夏特列原理：T/P/c→移'},
                    ]
                },
                {
                    'icon': '💧',
                    'name': '水溶液中的离子',
                    'children': [
                        {'name': '弱电解质部分电离'},
                        {'name': 'Kw=[H⁺][OH⁻]=1×10⁻¹⁴'},
                        {'name': 'pH=-lg[H⁺]；盐水解'},
                        {'name': 'Ksp沉淀溶解平衡'},
                    ]
                },
                {
                    'icon': '🔋',
                    'name': '化学反应与电能',
                    'children': [
                        {'name': '原电池（化学→电）'},
                        {'name': '电解池（电→化学）'},
                        {'name': '金属腐蚀与防护'},
                    ]
                },
            ]
        }
    },
    'ch10': {
        'title': '选修二 物质结构与性质 · 总览',
        'root': {
            'icon': '⚛️',
            'name': '物质结构与性质',
            'children': [
                {
                    'icon': '🔄',
                    'name': '原子结构与性质',
                    'children': [
                        {'name': '能层KLMN；能级spdf'},
                        {'name': '构造原理1s<2s<2p<3s<3p<4s<3d'},
                        {'name': 'Hund规则：简并轨道分占且自旋平行'},
                        {'name': '电负性：F(4.0)>O(3.5)>N(3.0) >Cl(3.2)'},
                    ]
                },
                {
                    'icon': '📐',
                    'name': '分子结构与性质',
                    'children': [
                        {'name': 'σ键（头碰头）/π键（肩并肩）'},
                        {'name': '配位键：[Cu(NH₃)₄]²⁺/NH₄⁺/H₃O⁺'},
                        {'name': '杂化：sp→直线/sp²→平面/sp³→四面体'},
                        {'name': 'VSEPR：CH₄正四面体/NH₃三角锥/H₂O V形'},
                        {'name': '极性/非极性；手性分子'},
                    ]
                },
                {
                    'icon': '💎',
                    'name': '晶体结构与性质',
                    'children': [
                        {'name': '离子晶体/金属晶体/共价晶体/分子晶体'},
                        {'name': 'NaCl晶胞(4+4)/CsCl晶胞(1+1)'},
                        {'name': '石墨：混合型晶体'},
                        {'name': '配合物数：NaCl=6/CsCl=8'},
                    ]
                },
            ]
        }
    },
    'ch11': {
        'title': '选修三 有机化学基础 · 总览',
        'root': {
            'icon': '🧬',
            'name': '有机化学基础',
            'children': [
                {
                    'icon': '📋',
                    'name': '有机物的分类与研究方法',
                    'children': [
                        {'name': '按碳骨架（链状/环状）'},
                        {'name': '按官能团（-X/-OH/-CHO/-COOH/-COO-)'},
                        {'name': '命名：选主链→编号→命名'},
                        {'name': '结构分析：MS/IR/NMR'},
                    ]
                },
                {
                    'icon': '⛽',
                    'name': '烃',
                    'children': [
                        {'name': '烷烃（CₙH₂ₙ₊₂）/取代'},
                        {'name': '烯烃（CₙH₂ₙ）/加成/加聚/顺反'},
                        {'name': '炔烃（CₙH₂ₙ₋₂）/加成'},
                        {'name': '芳香烃（苯/甲苯）：易取代难加成'},
                    ]
                },
                {
                    'icon': '🧪',
                    'name': '烃的衍生物',
                    'children': [
                        {'name': '卤代烃（水解/消去）'},
                        {'name': '醇/酚（氧化/酯化/FeCl₃显色）'},
                        {'name': '醛/酮（银镜/新制Cu(OH)₂）'},
                        {'name': '羧酸/酯（酯化/水解/皂化）'},
                    ]
                },
                {
                    'icon': '🧬',
                    'name': '生物大分子',
                    'children': [
                        {'name': '糖类（单/二/多糖）'},
                        {'name': '蛋白质（氨基酸→肽键→盐析/变性）'},
                        {'name': '核酸（DNA/RNA）'},
                    ]
                },
                {
                    'icon': '🧶',
                    'name': '合成高分子',
                    'children': [
                        {'name': '加聚（烯/二烯/无副）'},
                        {'name': '缩聚（两种单体+小分子）'},
                        {'name': '酚醛树脂/涤纶/聚乳酸PLA'},
                    ]
                },
            ]
        }
    },
}

for ch in raw:
    cid = ch['id']
    if cid in mindmaps:
        ch['mindMap'] = mindmaps[cid]

json.dump(raw, open('src/data/textbook-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK 全部mindMap写入')
