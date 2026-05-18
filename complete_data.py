import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

raw = json.load(open('src/data/textbook-data.json', 'r', encoding='utf-8'))

# 用id索引现有数据
by_id = {}
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            by_id[sub['id']] = sub

# === 新增/补充知识点 ===
new_knowledge = {
    'ch1_elec': [
        {'q': '树状分类法：物质分为____和____', 'a': '纯净物、混合物'},
        {'q': '纯净物分为____和____', 'a': '单质、化合物'},
        {'q': '氧化物分为____、____、____、____', 'a': '酸性氧化物、碱性氧化物、两性氧化物、不成盐氧化物'},
        {'q': '酸性氧化物举例：____', 'a': 'CO₂、SO₂、SO₃'},
        {'q': '碱性氧化物举例：____', 'a': 'Na₂O、CaO、CuO'},
    ],
    'ch1_elec2': [
        {'q': '溶液粒子直径____nm，胶体____nm，浊液____nm', 'a': '<1、1-100、>100'},
        {'q': '区分溶液和胶体的方法是____', 'a': '丁达尔效应'},
        {'q': '胶体聚沉的方法有____（举两例）', 'a': '加热、加电解质'},
        {'q': 'Fe(OH)₃胶体制备方程式：____', 'a': 'FeCl₃+3H₂O→(△)Fe(OH)₃(胶体)+3HCl'},
    ],
    'ch1_redox': [
        {'q': '氧化还原反应的判断依据是____', 'a': '化合价变化'},
        {'q': '氧化还原反应的本质是____', 'a': '电子转移'},
        {'q': '口诀：升失____，降得____', 'a': '氧化还原剂、还原氧化剂'},
        {'q': '四种基本反应中，全部是氧化还原的是____反应', 'a': '置换'},
        {'q': '四种基本反应中，全部不是氧化还原的是____反应', 'a': '复分解'},
    ],
}

# === 新增物质（id/name/icon/note/reactions）===
new_substances = [
    # 第一章 胶体/氧化还原
    {
        'id': 'ch1_colloid',
        'name': '胶体',
        'icon': '🧫',
        'note': '分散系(1-100nm)，介稳体系',
        'section': 'ch1_elec',
        'reactions': [
            {'id': 'ch1_col1', 'name': 'Fe(OH)₃胶体制备', 'equation': 'FeCl₃ + 3H₂O = Fe(OH)₃(胶体) + 3HCl', 'category': '制备', 'phenomenon': '溶液变为红褐色', 'note': '💯 注意写胶体二字非沉淀↓'},
        ],
        'knowledge': [
            {'q': '胶体粒子直径范围：____', 'a': '1-100nm'},
            {'q': '丁达尔效应可用于区分____和____', 'a': '溶液、胶体'},
            {'q': 'Fe(OH)₃胶体为____色', 'a': '红褐'},
        ],
    },
    {
        'id': 'ch1_redox_sub',
        'name': '氧化还原反应',
        'icon': '⚡',
        'note': '特征：化合价变化；本质：电子转移',
        'section': 'ch1_elec',
        'reactions': [],
        'knowledge': [
            {'q': '氧化还原特征：____；本质：____', 'a': '化合价变化、电子转移'},
            {'q': '升失氧还，降得还氧——升价____电子，发生____反应，作____剂', 'a': '失去、氧化、还原'},
        ],
    },
    # 第二章 补充物质的量
    {
        'id': 'ch2_mole',
        'name': '物质的量',
        'icon': '🧮',
        'note': 'n=N/N_A，N_A=6.02×10²³/mol',
        'section': 'ch2_na',
        'reactions': [],
        'knowledge': [
            {'q': 'n = N / ____，N_A = ____', 'a': 'N_A、6.02×10²³/mol'},
            {'q': 'n = m / ____', 'a': 'M'},
            {'q': '标况下气体：n = V / ____', 'a': '22.4L/mol'},
            {'q': 'c = n / ____；稀释公式：____', 'a': 'V、c₁V₁=c₂V₂'},
        ],
    },
    # 第四章 补充物质（周期律已有了knowledge，不用加）
    # 第五章 补充硅
    {
        'id': 'ch5_si',
        'name': '硅及其化合物',
        'icon': '💎',
        'note': 'SiO₂原子晶体，Si半导体材料',
        'section': 'ch5_n',
        'reactions': [
            {'id': 'ch5_si1', 'name': 'SiO₂ + HF（氢氟酸腐蚀玻璃）', 'equation': 'SiO₂ + 4HF = SiF₄↑ + 2H₂O', 'category': '与酸', 'note': '💯 唯一能腐蚀玻璃的酸！'},
            {'id': 'ch5_si2', 'name': 'SiO₂ + NaOH', 'equation': 'SiO₂ + 2NaOH = Na₂SiO₃ + H₂O', 'category': '与碱', 'note': '💯 试剂瓶要用橡胶塞'},
            {'id': 'ch5_si3', 'name': 'SiO₂ + C（制粗硅）', 'equation': 'SiO₂ + 2C =(高温) Si + 2CO↑', 'category': '工业制取', 'note': '💯 制粗硅反应'},
        ],
        'knowledge': [
            {'q': '光导纤维的主要成分是____', 'a': 'SiO₂'},
            {'q': '芯片的主要成分是____', 'a': 'Si'},
            {'q': '硅酸盐工业：____、____、____', 'a': '陶瓷、玻璃、水泥'},
            {'q': '水泥的原料：____+____', 'a': '石灰石、黏土'},
            {'q': '玻璃的原料：____+____+____', 'a': '纯碱、石灰石、石英'},
        ],
    },
    # 第六章 补充原电池详细
    {
        'id': 'ch6_battery_sub',
        'name': '原电池',
        'icon': '🔋',
        'note': '化学能→电能',
        'section': 'ch6_energy',
        'reactions': [
            {'id': 'ch6_bat1', 'name': 'Zn-Cu原电池(负极)', 'equation': 'Zn - 2e⁻ = Zn²⁺', 'category': '电极反应', 'note': '💯 负极失电子，发生氧化'},
            {'id': 'ch6_bat2', 'name': 'Zn-Cu原电池(正极)', 'equation': '2H⁺ + 2e⁻ = H₂↑', 'category': '电极反应', 'note': '💯 正极得电子，发生还原'},
        ],
    },
    # 第七章 补充更多有机反应
    {
        'id': 'ch7_oil',
        'name': '油脂',
        'icon': '🧴',
        'note': '油(不饱和)+脂肪(饱和)',
        'section': 'ch7_nutrient',
        'reactions': [
            {'id': 'ch7_oil1', 'name': '油脂皂化', 'equation': '油脂 + NaOH →(△) 高级脂肪酸钠 + 甘油', 'category': '皂化反应', 'note': '💯 制肥皂原理'},
        ],
        'knowledge': [
            {'q': '油含____键，常温为液态', 'a': '不饱和'},
            {'q': '饱和油脂叫____，不饱和油脂叫____', 'a': '脂肪、油'},
        ],
    },
    # 第八章 补充金属冶炼/海水提溴/提镁
    {
        'id': 'ch8_metallurgy',
        'name': '金属冶炼',
        'icon': '🏭',
        'note': 'K→Al电解法，Zn→Cu热还原法，Hg→Ag热分解法',
        'section': 'ch8_resources',
        'reactions': [
            {'id': 'ch8_met1', 'name': '电解Al₂O₃制铝', 'equation': '2Al₂O₃(熔融) =(电解) 4Al + 3O₂↑', 'category': '电解', 'note': '💯 冰晶石Na₃AlF₆作助熔剂'},
            {'id': 'ch8_met2', 'name': '电解MgCl₂制镁', 'equation': 'MgCl₂(熔融) =(电解) Mg + Cl₂↑', 'category': '电解', 'note': '海水提镁'},
            {'id': 'ch8_met3', 'name': 'Cl₂氧化Br⁻提溴', 'equation': '2Br⁻ + Cl₂ = Br₂ + 2Cl⁻', 'category': '氧化', 'note': '💯 海水提溴'},
        ],
    },
    # 选修一 补充
    {
        'id': 'ch9_thermo',
        'name': '热化学',
        'icon': '🔥',
        'note': '热化学方程式需标状态(s/l/g/aq)和ΔH',
        'section': 'ch9_heat',
        'reactions': [],
        'knowledge': [
            {'q': '热化学方程式必须注明的: (1)物质____ (2)____值', 'a': '状态、ΔH'},
            {'q': 'ΔH与系数成____比', 'a': '正'},
            {'q': '可逆反应的ΔH按____反应计算', 'a': '完全'},
            {'q': '盖斯定律：ΔH只与____有关，与____无关', 'a': '始态/终态、路径'},
            {'q': '燃烧热：1mol纯物质完全燃烧生成____氧化物', 'a': '稳定'},
            {'q': '中和热ΔH = ____（稀强酸+稀强碱）', 'a': '-57.3kJ/mol'},
        ],
    },
    {
        'id': 'ch9_electrochem',
        'name': '电解池',
        'icon': '⚡',
        'note': '电解：电能→化学能',
        'section': 'ch9_electro',
        'reactions': [
            {'id': 'ch9_e1', 'name': '电解CuCl₂溶液', 'equation': 'CuCl₂ =(电解) Cu + Cl₂↑', 'category': '电解', 'phenomenon': '阴极析出红色固体，阳极产生黄绿色气体', 'note': '💯 基本电解反应'},
            {'id': 'ch9_e2', 'name': '电解饱和食盐水(氯碱)', 'equation': '2NaCl + 2H₂O =(电解) 2NaOH + H₂↑ + Cl₂↑', 'category': '电解', 'phenomenon': '阳极黄绿气体，阴极无色气体', 'note': '💯 氯碱工业'},
            {'id': 'ch9_e3', 'name': '电解精炼铜(阴极)', 'equation': 'Cu²⁺ + 2e⁻ = Cu', 'category': '电解', 'note': '纯铜作阴极'},
            {'id': 'ch9_e4', 'name': '电解精炼铜(阳极)', 'equation': 'Cu - 2e⁻ = Cu²⁺', 'category': '电解', 'note': '粗铜作阳极，阳极泥含Au/Ag'},
        ],
    },
    # 选修二
    {
        'id': 'ch10_econfig',
        'name': '电子排布',
        'icon': '⚛️',
        'note': '构造原理：1s<2s<2p<3s<3p<4s<3d',
        'section': 'ch10_atom',
        'reactions': [],
        'knowledge': [
            {'q': 's轨道有____个，最多____个电子', 'a': '1、2'},
            {'q': 'p轨道有____个，最多____个电子', 'a': '3、6'},
            {'q': 'd轨道有____个，最多____个电子', 'a': '5、10'},
            {'q': '洪特规则：简并轨道电子优先____占据且自旋____', 'a': '单独、平行'},
            {'q': 'Li电子排布：____；Na：____；K：____', 'a': '1s²2s¹、[Ne]3s¹、[Ar]4s¹'},
            {'q': '电负性最大的是____（4.0）', 'a': 'F'},
            {'q': '第一电离能反常：N____O，Mg____Al', 'a': '>、>'},
        ],
    },
    {
        'id': 'ch10_geometry',
        'name': '分子空间构型',
        'icon': '📐',
        'note': 'VSEPR+杂化轨道理论',
        'section': 'ch10_mol',
        'reactions': [],
        'knowledge': [
            {'q': 'sp杂化空间构型为____，键角____', 'a': '直线形、180°'},
            {'q': 'sp²杂化空间构型为____，键角____', 'a': '平面三角形、120°'},
            {'q': 'sp³杂化空间构型为____，键角____', 'a': '正四面体、109°28′'},
            {'q': 'CH₄构型____；NH₃构型____；H₂O构型____', 'a': '正四面体、三角锥、V形'},
            {'q': '键角大小：CH₄____NH₃____H₂O', 'a': '>、>'},
            {'q': '极性分子举例：____', 'a': 'HCl、H₂O、NH₃、CHCl₃'},
            {'q': '非极性分子举例：____', 'a': 'CH₄、CO₂、BF₃、CCl₄'},
        ],
    },
    {
        'id': 'ch10_crystal_sub',
        'name': '晶体类型',
        'icon': '💎',
        'note': '离子/金属/共价/分子晶体',
        'section': 'ch10_crystal',
        'reactions': [],
        'knowledge': [
            {'q': '离子晶体举例：____', 'a': 'NaCl、CsCl'},
            {'q': '共价晶体举例：____', 'a': '金刚石、Si、SiO₂'},
            {'q': '分子晶体举例：____', 'a': '冰、干冰、I₂'},
            {'q': '熔沸点：____晶体 > ____晶体 > ____晶体 > ____晶体', 'a': '共价、离子、金属、分子'},
            {'q': '石墨属于____型晶体（层间____力）', 'a': '混合、范德华'},
            {'q': 'NaCl晶胞中，Na⁺____个，Cl⁻____个', 'a': '4、4'},
        ],
    },
    # 选修三 补充有机
    {
        'id': 'ch11_halide_d',
        'name': '卤代烃',
        'icon': '🧪',
        'note': 'R-X，不溶于水，密度>水',
        'section': 'ch11_deriv',
        'reactions': [
            {'id': 'ch11_hal1', 'name': '卤代烃水解', 'equation': 'RX + NaOH →(H₂O/△) ROH + NaX', 'category': '取代', 'note': '💯 制醇'},
            {'id': 'ch11_hal2', 'name': '卤代烃消去', 'equation': 'RX + NaOH →(醇/△) 烯烃 + NaX + H₂O', 'category': '消去', 'note': '💯 扎伊采夫规则'},
        ],
    },
    {
        'id': 'ch11_alcohol_detail',
        'name': '醇',
        'icon': '🍷',
        'note': 'R-OH，官能团羟基',
        'section': 'ch11_deriv',
        'reactions': [
            {'id': 'ch11_alc1', 'name': '乙醇 + Na', 'equation': '2C₂H₅OH + 2Na = 2C₂H₅ONa + H₂↑', 'category': '与金属', 'phenomenon': '产生无色气体', 'note': 'OH上的H可被Na置换'},
        ],
    },
    {
        'id': 'ch11_phenol',
        'name': '苯酚',
        'icon': '🧴',
        'note': 'C₆H₅OH，弱酸性，与FeCl₃显紫色',
        'section': 'ch11_deriv',
        'reactions': [
            {'id': 'ch11_ph1', 'name': '苯酚+Br₂(定量检验)', 'equation': 'C₆H₅OH + 3Br₂ = C₆H₂Br₃OH↓ + 3HBr', 'category': '取代', 'phenomenon': '产生白色沉淀', 'note': '💯 邻对位取代，定量检验'},
            {'id': 'ch11_ph2', 'name': '苯酚+NaOH', 'equation': 'C₆H₅OH + NaOH → C₆H₅ONa + H₂O', 'category': '酸碱', 'note': '苯酚弱酸性'},
        ],
    },
    {
        'id': 'ch11_aldehyde_sub',
        'name': '醛',
        'icon': '🔬',
        'note': '官能团-CHO，可银镜反应',
        'section': 'ch11_deriv',
        'reactions': [
            {'id': 'ch11_al1', 'name': '银镜反应', 'equation': 'RCHO + 2[Ag(NH₃)₂]OH →(△) RCOONH₄ + 2Ag↓ + 3NH₃ + H₂O', 'category': '氧化', 'phenomenon': '试管壁析出银白色银镜', 'note': '💯 醛基的特征反应'},
            {'id': 'ch11_al2', 'name': '与新制Cu(OH)₂反应', 'equation': 'RCHO + 2Cu(OH)₂ + NaOH →(△) RCOONa + Cu₂O↓ + 3H₂O', 'category': '氧化', 'phenomenon': '产生砖红色沉淀', 'note': '💯 醛基的鉴别反应'},
            {'id': 'ch11_al3', 'name': '甲醛HCHO结构特殊', 'equation': 'HCHO + 4[Ag(NH₃)₂]OH →(△) (NH₄)₂CO₃ + 4Ag↓ + 6NH₃ + 2H₂O', 'category': '氧化', 'note': '⚠ HCHO相当于两个醛基'},
        ],
    },
    {
        'id': 'ch11_sugar_detail',
        'name': '糖类',
        'icon': '🍬',
        'note': '单糖/二糖/多糖，C,H,O',
        'section': 'ch11_bio',
        'reactions': [
            {'id': 'ch11_sug1', 'name': '葡萄糖有氧呼吸(△', 'equation': 'C₆H₁₂O₆ + 6O₂ = 6CO₂ + 6H₂O + 能量', 'category': '氧化', 'note': '有氧呼吸，释放能量'},
            {'id': 'ch11_sug2', 'name': '蔗糖水解', 'equation': 'C₁₂H₂₂O₁₁ + H₂O →(△/H⁺) C₆H₁₂O₆(葡) + C₆H₁₂O₆(果)', 'category': '水解', 'note': '蔗糖非还原性'},
            {'id': 'ch11_sug3', 'name': '麦芽糖水解', 'equation': 'C₁₂H₂₂O₁₁ + H₂O →(△/H⁺) 2C₆H₁₂O₆(葡)', 'category': '水解', 'note': '麦芽糖有还原性'},
        ],
    },
    {
        'id': 'ch11_protein_detail',
        'name': '蛋白质',
        'icon': '🧬',
        'note': '氨基酸→多肽，盐析可逆，变性不可逆',
        'section': 'ch11_bio',
        'reactions': [
            {'id': 'ch11_pro1', 'name': '氨基酸缩合(形成肽键)', 'equation': '氨基酸 + 氨基酸 →(△) 二肽 + H₂O', 'category': '缩合', 'note': '肽键—CONH—'},
        ],
    },
    {
        'id': 'ch11_poly_detail',
        'name': '加聚与缩聚',
        'icon': '🧶',
        'note': '加聚无副产物，缩聚有小分子',
        'section': 'ch11_poly',
        'reactions': [
            {'id': 'ch11_pol1', 'name': '乙烯加聚(PE)', 'equation': 'nCH₂=CH₂ →(催化剂) [CH₂-CH₂]ₙ', 'category': '加聚', 'note': '💯 聚乙烯PE'},
        ],
    },
    # 第六章 补充平衡
    {
        'id': 'ch6_balance_sub',
        'name': '化学平衡',
        'icon': '⚖️',
        'note': 'v正=v逆，各组分量不变',
        'section': 'ch6_rate',
        'reactions': [],
        'knowledge': [
            {'q': '平衡标志：____', 'a': 'v正=v逆≠0，各组分量不变'},
            {'q': '升温平衡向____方向移动', 'a': '吸热'},
            {'q': '加压平衡向____方向移动', 'a': '气体体积减小'},
            {'q': '催化剂____（能/不能）使平衡移动', 'a': '不能'},
        ],
    },
]

# 先补充已经有的substances的knowledge
for sub_id, know_list in new_knowledge.items():
    if sub_id in by_id:
        existing = by_id[sub_id].get('knowledge', [])
        existing_ids = {k['q'] for k in existing}
        for k in know_list:
            if k['q'] not in existing_ids:
                existing.append(k)
        by_id[sub_id]['knowledge'] = existing

# 新增substance到对应section
for ns in new_substances:
    found = False
    for ch in raw:
        for sec in ch['sections']:
            if sec['id'] == ns['section']:
                sub_entry = {
                    'id': ns['id'],
                    'name': ns['name'],
                    'icon': ns.get('icon', '📚'),
                    'note': ns.get('note', ''),
                    'reactions': ns.get('reactions', []),
                    'knowledge': ns.get('knowledge', []),
                }
                sec['substances'].append(sub_entry)
                found = True
                break
        if found:
            break

# 统计
total_rxns = 0
total_know = 0
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            total_rxns += len(sub.get('reactions', []))
            total_know += len(sub.get('knowledge', []))

print(f'总反应数: {total_rxns}')
print(f'总知识点: {total_know}')
print(f'总物质数: {sum(len(sec["substances"]) for ch in raw for sec in ch["sections"])}')

json.dump(raw, open('src/data/textbook-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK')
