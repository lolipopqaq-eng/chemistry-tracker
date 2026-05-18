import sys, json
sys.stdout.reconfigure(encoding='utf-8')
raw = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))

# 用id索引
by_id = {}
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            by_id[sub['id']] = sub

# ===== 选修一 补充更多反应 =====
ch9_add_reactions = {
    'ch9_thermo': [
        {'id': 'ch9_t1', 'name': '甲烷燃烧热', 'equation': 'CH₄(g) + 2O₂(g) = CO₂(g) + 2H₂O(l)', 'category': '燃烧热', 'note': '💯 燃烧热生成液态水'},
        {'id': 'ch9_t2', 'name': 'H₂燃烧热', 'equation': 'H₂(g) + ½O₂(g) = H₂O(l)', 'category': '燃烧热', 'note': ''},
    ],
    'ch9_electrochem': [
        {'id': 'ch9_e5', 'name': '电解水', 'equation': '2H₂O =(电解) 2H₂↑ + O₂↑', 'category': '电解', 'phenomenon': '阴极产生H₂，阳极产生O₂'},
        {'id': 'ch9_e6', 'name': '电解NaCl溶液', 'equation': '2NaCl + 2H₂O =(电解) 2NaOH + H₂↑ + Cl₂↑', 'category': '氯碱工业', 'note': ''},
        {'id': 'ch9_e7', 'name': '电解熔融NaCl', 'equation': '2NaCl(熔融) =(电解) 2Na + Cl₂↑', 'category': '电解', 'note': '💯 制金属钠'},
    ],
    'ch9_acid_base': [
        {'id': 'ch9_h1', 'name': 'CH₃COOH电离', 'equation': 'CH₃COOH ⇌ CH₃COO⁻ + H⁺', 'category': '电离', 'note': '💯 弱电解质部分电离'},
        {'id': 'ch9_h2', 'name': 'NH₃·H₂O电离', 'equation': 'NH₃·H₂O ⇌ NH₄⁺ + OH⁻', 'category': '电离', 'note': '💯 弱碱'},
        {'id': 'ch9_h3', 'name': 'H₂O的电离', 'equation': 'H₂O ⇌ H⁺ + OH⁻', 'category': '电离', 'note': '💯 Kw=1×10⁻¹⁴(25℃)'},
    ],
    'ch9_hydrolysis': [
        {'id': 'ch9_hy1', 'name': 'NH₄⁺水解', 'equation': 'NH₄⁺ + H₂O ⇌ NH₃·H₂O + H⁺', 'category': '水解', 'note': '强酸弱碱盐→酸性'},
        {'id': 'ch9_hy2', 'name': 'CH₃COO⁻水解', 'equation': 'CH₃COO⁻ + H₂O ⇌ CH₃COOH + OH⁻', 'category': '水解', 'note': '强碱弱酸盐→碱性'},
        {'id': 'ch9_hy3', 'name': 'CO₃²⁻水解（第一步）', 'equation': 'CO₃²⁻ + H₂O ⇌ HCO₃⁻ + OH⁻', 'category': '水解', 'note': ''},
        {'id': 'ch9_hy4', 'name': 'HCO₃⁻水解', 'equation': 'HCO₃⁻ + H₂O ⇌ H₂CO₃ + OH⁻', 'category': '水解', 'note': ''},
        {'id': 'ch9_hy5', 'name': 'Al³⁺双水解（灭火器）', 'equation': 'Al³⁺ + 3HCO₃⁻ = Al(OH)₃↓ + 3CO₂↑', 'category': '双水解', 'note': '💯 泡沫灭火器原理'},
    ],
    'ch9_balance': [
        {'id': 'ch9_keq1', 'name': '可逆反应平衡表达式', 'equation': 'aA + bB ⇌ cC + dD', 'category': '平衡常数', 'note': 'K=c(C)ᶜc(D)ᵈ/a(A)ᵃb(B)ᵇ'},
    ],
    'ch9_corrosion': [
        {'id': 'ch9_c1', 'name': '钢铁吸氧腐蚀(负极)', 'equation': 'Fe - 2e⁻ = Fe²⁺', 'category': '腐蚀', 'note': '电化学腐蚀负极'},
        {'id': 'ch9_c2', 'name': '钢铁吸氧腐蚀(正极)', 'equation': 'O₂ + 2H₂O + 4e⁻ = 4OH⁻', 'category': '腐蚀', 'note': '💯 吸氧腐蚀为主'},
    ],
    'ch9_ksp': [
        {'id': 'ch9_ksp1', 'name': 'AgCl沉淀溶解平衡', 'equation': 'AgCl(s) ⇌ Ag⁺(aq) + Cl⁻(aq)', 'category': '沉淀溶解', 'note': 'Ksp=[Ag⁺][Cl⁻]'},
        {'id': 'ch9_ksp2', 'name': '沉淀转化AgCl→AgI', 'equation': 'AgCl + I⁻ = AgI↓ + Cl⁻', 'category': '沉淀转化', 'note': '💯 溶解度小的→更小的'},
    ],
    'ch9_battery': [
        {'id': 'ch9_b1', 'name': 'H₂-O₂燃料电池(酸性)', 'equation': '2H₂ + O₂ = 2H₂O', 'category': '燃料电池', 'note': '清洁能源'},
    ],
}

for sub_id, rxns in ch9_add_reactions.items():
    if sub_id in by_id:
        existing = by_id[sub_id].get('reactions', [])
        existing_ids = {r['id'] for r in existing}
        for r in rxns:
            if r['id'] not in existing_ids:
                existing.append(r)
        by_id[sub_id]['reactions'] = existing

# ===== 选修一 补知识点 =====
ch9_add_know = {
    'ch9_thermo': [
        {'q': '热化学方程式中必须注明物质的____和____', 'a': '状态(s/l/g/aq)、ΔH值'},
        {'q': 'ΔH与计量数成____比', 'a': '正'},
        {'q': '可逆反应的ΔH按____反应计算', 'a': '完全'},
    ],
    'ch9_electrochem': [
        {'q': '电解池阳极接电源____极，发生____反应', 'a': '正、氧化'},
        {'q': '电解池阴极接电源____极，发生____反应', 'a': '负、还原'},
        {'q': '电镀时镀件接____极，镀层金属接____极', 'a': '阴、阳'},
    ],
    'ch9_corrosion': [
        {'q': '钢铁腐蚀主要形式是____腐蚀', 'a': '电化学（吸氧）'},
        {'q': '牺牲阳极法保护的金属作____极', 'a': '阳'},
        {'q': '外加电流法将被保护金属接电源____极', 'a': '负'},
    ],
}

for sub_id, know_list in ch9_add_know.items():
    if sub_id in by_id:
        existing = by_id[sub_id].get('knowledge', [])
        existing_ids = {k['q'] for k in existing}
        for k in know_list:
            if k['q'] not in existing_ids:
                existing.append(k)
        by_id[sub_id]['knowledge'] = existing

# ===== 选修二+三: 知识点已经在之前add_knowledge.py里写了，但反应太少 =====
# 选修二主要是概念，所以补充大量知识点
ch10_add_know = {
    'ch10_atom_sub': [
        {'q': '能层K层最多____个电子；L层最多____个；M层最多____个', 'a': '2、8、18'},
        {'q': 's轨道____个轨道，最多____个电子', 'a': '1、2'},
        {'q': 'p轨道____个轨道，最多____个电子', 'a': '3、6'},
        {'q': 'd轨道____个轨道，最多____个电子', 'a': '5、10'},
        {'q': '洪特规则特例：Cr的电子排布为____', 'a': '[Ar]3d⁵4s¹'},
        {'q': '洪特规则特例：Cu的电子排布为____', 'a': '[Ar]3d¹⁰4s¹'},
    ],
    'ch10_mol_sub': [
        {'q': 'sp杂化的中心原子价层电子对数为____，构型____', 'a': '2、直线形'},
        {'q': 'sp²杂化的中心原子价层电子对数为____，构型____', 'a': '3、平面三角形'},
        {'q': 'sp³杂化的中心原子价层电子对数为____，构型____', 'a': '4、正四面体'},
        {'q': 'CH₄的中心原子C为____杂化，键角____', 'a': 'sp³、109°28′'},
        {'q': 'NH₃的中心原子N为____杂化，分子构型____', 'a': 'sp³、三角锥'},
        {'q': 'H₂O的中心原子O为____杂化，分子构型____', 'a': 'sp³、V形'},
        {'q': 'C₂H₄中C为____杂化，键角____', 'a': 'sp²、120°'},
        {'q': 'C₂H₂中C为____杂化，分子构型____', 'a': 'sp、直线'},
        {'q': 'BF₃中B为____杂化，分子构型____', 'a': 'sp²、平面三角形'},
        {'q': '如何判断杂化类型？', 'a': '价层电子对数=σ键数+孤对电子数；2→sp、3→sp²、4→sp³'},
    ],
    'ch10_crystal_sub': [
        {'q': '金刚石中C为____杂化，属于____晶体', 'a': 'sp³、共价'},
        {'q': '石墨中C为____杂化，属于____型晶体', 'a': 'sp²、混合'},
        {'q': 'SiO₂为____晶体，硬度____', 'a': '共价、大'},
        {'q': '干冰为____晶体，升华____热', 'a': '分子、吸'},
    ],
    'ch10_crystal_sub2': [
        {'q': 'NaCl晶胞中Na⁺位于____位置；Cl⁻位于____位置', 'a': '棱心和体心、顶点和面心'},
        {'q': '配位数指____', 'a': '紧邻的异号离子数'},
        {'q': '金属晶体熔沸点变化规律：同周期从左到右____', 'a': '先升后降'},
    ],
}

for sub_id, know_list in ch10_add_know.items():
    if sub_id in by_id:
        existing = by_id[sub_id].get('knowledge', [])
        existing_ids = {k['q'] for k in existing}
        for k in know_list:
            if k['q'] not in existing_ids:
                existing.append(k)
        by_id[sub_id]['knowledge'] = existing

# ===== 选修三 补充更多有机反应 =====
ch11_add_reactions = {
    'ch11_alkyl': [
        {'id': 'ch11_al1', 'name': '乙炔+2Br₂(完全加成)', 'equation': 'C₂H₂ + 2Br₂ = CHBr₂CHBr₂', 'category': '加成', 'phenomenon': '溴水褪色', 'note': '💯 乙炔含两个π键'},
        {'id': 'ch11_al2', 'name': '乙炔+H₂(部分加成)', 'equation': 'C₂H₂ + H₂ →(催化剂/△) C₂H₄', 'category': '加成', 'note': '不完全加成生成乙烯'},
        {'id': 'ch11_al3', 'name': '乙炔+HCl', 'equation': 'C₂H₂ + HCl →(催化剂) CH₂=CHCl', 'category': '加成', 'note': '💯 制氯乙烯(聚氯乙烯PVC单体)'},
        {'id': 'ch11_al4', 'name': '丙烯+Br₂', 'equation': 'CH₃CH=CH₂ + Br₂ → CH₃CHBrCH₂Br', 'category': '加成', 'note': '双键加成'},
    ],
    'ch11_alkane_sub': [
        {'id': 'ch11_an1', 'name': '丙烷完全燃烧', 'equation': 'C₃H₈ + 5O₂ =(点燃) 3CO₂ + 4H₂O', 'category': '燃烧', 'note': ''},
        {'id': 'ch11_an2', 'name': '甲烷高温裂解', 'equation': 'CH₄ →(高温) C + 2H₂', 'category': '裂解', 'note': '💯 制氢气'},
    ],
    'ch11_alkene_sub': [
        {'id': 'ch11_en1', 'name': '丙烯加聚（聚丙烯）', 'equation': 'nCH₃CH=CH₂ →(催化剂) [CH(CH₃)-CH₂]ₙ', 'category': '加聚', 'note': '💯 聚丙烯PP'},
    ],
    'ch11_aromatic_sub': [
        {'id': 'ch11_ar1', 'name': '苯+Cl₂(取代)', 'equation': 'C₆H₆ + Cl₂ →(FeCl₃) C₆H₅Cl + HCl', 'category': '取代', 'note': '氯苯生成'},
        {'id': 'ch11_ar2', 'name': '甲苯硝化', 'equation': 'C₆H₅CH₃ + 3HNO₃ →(浓H₂SO₄/△) C₆H₂(CH₃)(NO₂)₃ + 3H₂O', 'category': '取代', 'note': '💯 TNT炸药'},
        {'id': 'ch11_ar3', 'name': '甲苯+酸性KMnO₄', 'equation': 'C₆H₅CH₃ →(KMnO₄/H⁺) C₆H₅COOH', 'category': '氧化', 'note': '💯 甲苯可被氧化，苯不行'},
    ],
    'ch11_alcohol_detail': [
        {'id': 'ch11_ac2', 'name': '乙醇分子间脱水', 'equation': '2C₂H₅OH →(浓H₂SO₄/140℃) C₂H₅OC₂H₅ + H₂O', 'category': '取代', 'note': '💯 140℃→醚'},
        {'id': 'ch11_ac3', 'name': '乙醇消去（制乙烯）', 'equation': 'C₂H₅OH →(浓H₂SO₄/170℃) C₂H₄↑ + H₂O', 'category': '消去', 'note': '💯 170℃→烯'},
    ],
    'ch11_phenol': [
        {'id': 'ch11_ph3', 'name': '苯酚钠+CO₂', 'equation': 'C₆H₅ONa + CO₂ + H₂O → C₆H₅OH + NaHCO₃', 'category': '复分解', 'note': '💯 酸性H₂CO₃>苯酚'},
    ],
    'ch11_aldehyde_sub': [
        {'id': 'ch11_al4b', 'name': '乙醛+Cu(OH)₂', 'equation': 'CH₃CHO + 2Cu(OH)₂ + NaOH →(△) CH₃COONa + Cu₂O↓ + 3H₂O', 'category': '氧化', 'phenomenon': '砖红色沉淀', 'note': ''},
    ],
    'ch11_hac': [
        {'id': 'ch11_hac1', 'name': '乙二酸+KMnO₄', 'equation': 'H₂C₂O₄ + 2KMnO₄ + 3H₂SO₄ → K₂SO₄ + 2MnSO₄ + 8H₂O + 10CO₂↑', 'category': '氧化', 'phenomenon': '紫红色褪去', 'note': '💯 草酸还原性'},
        {'id': 'ch11_hac2', 'name': '乙酸乙酯酸性水解', 'equation': 'CH₃COOC₂H₅ + H₂O ⇌(H⁺/△) CH₃COOH + C₂H₅OH', 'category': '水解', 'note': '可逆反应'},
        {'id': 'ch11_hac3', 'name': '乙酸乙酯碱性水解(皂化)', 'equation': 'CH₃COOC₂H₅ + NaOH →(△) CH₃COONa + C₂H₅OH', 'category': '皂化', 'note': '💯 不可逆'},
    ],
    'ch11_protein_detail': [
        {'id': 'ch11_pr2', 'name': '蛋白质黄色反应', 'equation': '蛋白质 + 浓HNO₃ →(△) 黄色', 'category': '检验', 'note': '💯 含苯环的蛋白质'},
    ],
    'ch11_poly_detail': [
        {'id': 'ch11_pol2', 'name': '苯酚+甲醛(酚醛树脂)', 'equation': 'nC₆H₅OH + nHCHO →(催化剂) 酚醛树脂 + nH₂O', 'category': '缩聚', 'note': '💯 电木'},
        {'id': 'ch11_pol3', 'name': '聚氯乙烯PVC制备', 'equation': 'nCH₂=CHCl →(催化剂) [CH₂-CHCl]ₙ', 'category': '加聚', 'note': '由氯乙烯加聚'},
    ],
    'ch11_halide_sub': [
        {'id': 'ch11_hal3', 'name': '1-溴丙烷消去', 'equation': 'CH₃CH₂CH₂Br + NaOH →(醇/△) CH₃CH=CH₂↑ + NaBr + H₂O', 'category': '消去', 'note': '💯 扎伊采夫规则'},
    ],
    'ch11_ester_sub': [
        {'id': 'ch11_es1', 'name': '乙二醇+对苯二甲酸缩聚', 'equation': 'nHOCH₂CH₂OH + nHOOC-C₆H₄-COOH →(催化剂) 涤纶 + (2n-1)H₂O', 'category': '缩聚', 'note': '💯 涤纶(PET)'},
    ],
    'ch11_poly_sub': [
        {'id': 'ch11_ps1', 'name': '聚乳酸PLA制备', 'equation': 'n乳酸 →(催化剂) [OCH(CH₃)CO]ₙ + nH₂O', 'category': '缩聚', 'note': '💯 可降解塑料'},
    ],
}

for sub_id, rxns in ch11_add_reactions.items():
    if sub_id in by_id:
        existing = by_id[sub_id].get('reactions', [])
        existing_ids = {r['id'] for r in existing}
        for r in rxns:
            if r['id'] not in existing_ids:
                existing.append(r)
        by_id[sub_id]['reactions'] = existing

# 统计
total_rxn = 0
total_know = 0
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            total_rxn += len(sub.get('reactions', []))
            total_know += len(sub.get('knowledge', []))
print(f'最终统计：总反应={total_rxn}，总知识点={total_know}')

json.dump(raw, open('src/data/textbook-data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK')
