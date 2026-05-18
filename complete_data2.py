import sys, json
sys.stdout.reconfigure(encoding='utf-8')
raw = json.load(open('src/data/textbook-data.json', 'r', encoding='utf-8'))

by_id = {}
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            by_id[sub['id']] = sub

# === 补充选修二 ===
extra_knowledge = {
    # 选修二 原子结构
    'ch10_atom_sub': [
        {'q': '能层K、L、M、N对应的符号是____、____、____、____', 'a': '1s、2s2p、3s3p3d、4s4p4d4f'},
        {'q': '基态→激发态____能量，激发态→基态____能量', 'a': '吸收、发射'},
    ],
    # 选修二 分子结构
    'ch10_mol_sub': [
        {'q': '配位键形成条件：____+____', 'a': '孤对电子、空轨道'},
        {'q': '[Cu(NH₃)₄]²⁺中心离子是____，配体是____', 'a': 'Cu²⁺、NH₃'},
        {'q': '相似相溶：____分子易溶于____溶剂', 'a': '极性、极性'},
        {'q': '手性碳指连有____个不同基团的C', 'a': '4'},
    ],
    # 选修二 晶体
    'ch10_crystal_sub2': [
        {'q': 'NaCl配位数为____，CsCl配位数为____', 'a': '6、8'},
        {'q': '金属堆积：简单立方(Po)、体心立方(____)、面心立方(____)', 'a': 'Na/K/Fe、Cu/Au'},
        {'q': '均摊法：顶点____、棱心____、面心____', 'a': '1/8、1/4、1/2'},
    ],
    # 选修三 烷烃
    'ch11_alkane_sub': [
        {'q': '烷烃化学性质稳定，主要反应为____反应', 'a': '取代'},
        {'q': '甲烷与Cl₂取代（光照下）产物：____（分步取代）', 'a': 'CH₃Cl、CH₂Cl₂、CHCl₃、CCl₄'},
    ],
    # 选修三 烯烃
    'ch11_alkene_sub': [
        {'q': '乙烯使KMnO₄褪色属于____反应（鉴别烷/烯）', 'a': '氧化'},
        {'q': '顺反异构产生条件：双键两端各连两个____基团', 'a': '不同'},
    ],
    # 选修三 炔烃
    'ch11_alkyne_sub': [
        {'q': '乙炔俗称____气，分子式____', 'a': '电石、C₂H₂'},
        {'q': '乙炔+2Br₂产物：____', 'a': 'CHBr₂CHBr₂'},
    ],
    # 选修三 芳香烃
    'ch11_aromatic_sub': [
        {'q': '苯____（能/不能）使KMnO₄褪色', 'a': '不能'},
        {'q': '甲苯比苯____（易/难）发生取代（-CH₃活化苯环）', 'a': '易'},
        {'q': '甲苯可被KMnO₄氧化为____', 'a': '苯甲酸'},
    ],
    # 选修三 卤代烃
    'ch11_halide_sub': [
        {'q': '卤代烃水解条件：____；消去条件：____', 'a': 'NaOH水溶液/△、NaOH醇溶液/△'},
    ],
    # 选修三 醇/酚
    'ch11_alc_detail': [
        {'q': '醇消去反应条件：____/____℃', 'a': '浓硫酸、170'},
        {'q': '醇分子间脱水(140℃)生成____', 'a': '醚'},
        {'q': '伯醇氧化→____→____；仲醇氧化→____', 'a': '醛、羧酸、酮'},
    ],
    # 选修三 羧酸/酯
    'ch11_ester_sub': [
        {'q': '甲酸HCOOH既有____基又有____基（能银镜）', 'a': '羧、醛'},
        {'q': '乙二酸HOOC-COOH俗名____，有____性（使KMnO₄褪色）', 'a': '草酸、还原'},
        {'q': '酯在酸性条件下水解____（可逆/不可逆）；碱性条件下____', 'a': '可逆、不可逆'},
    ],
    # 选修三 生物大分子
    'ch11_nucleic': [
        {'q': 'DNA为____结构，RNA为____链', 'a': '双螺旋、单'},
        {'q': '核苷酸由____+____+____组成', 'a': '核苷、磷酸、碱基'},
    ],
    # 选修三 合成高分子
    'ch11_poly_sub': [
        {'q': '加聚反应特点：____产物', 'a': '无副'},
        {'q': '缩聚反应特点：有____生成', 'a': '小分子'},
        {'q': '酚醛树脂单质：____+____', 'a': '苯酚、甲醛'},
        {'q': '可降解塑料PLA（聚乳酸）由____发酵制得', 'a': '玉米淀粉'},
    ],
    # 第八章 海水提溴提镁
    'ch8_met_sub': [
        {'q': '海水提溴：Cl₂氧化Br⁻→____→吸收→再氧化', 'a': '空气吹出'},
        {'q': '金属活泼性越强，冶炼越____（难/易）', 'a': '难'},
    ],
}

for sub_id, know_list in extra_knowledge.items():
    if sub_id in by_id:
        existing = by_id[sub_id].get('knowledge', [])
        existing_ids = {k['q'] for k in existing}
        for k in know_list:
            if k['q'] not in existing_ids:
                existing.append(k)
        by_id[sub_id]['knowledge'] = existing

# 统计
total_rxns = 0
total_know = 0
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            total_rxns += len(sub.get('reactions', []))
            total_know += len(sub.get('knowledge', []))

print(f'总反应: {total_rxns}')
print(f'总知识点: {total_know}')
print(f'总物质: {sum(len(sec["substances"]) for ch in raw for sec in ch["sections"])}')

json.dump(raw, open('src/data/textbook-data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK')
