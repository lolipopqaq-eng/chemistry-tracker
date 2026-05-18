import sys, json
sys.stdout.reconfigure(encoding='utf-8')
raw = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))

by_id = {}
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            by_id[sub['id']] = sub

def add(sub_id, rxns):
    if sub_id in by_id:
        existing = by_id[sub_id].get('reactions', [])
        ex_ids = {r['id'] for r in existing}
        for r in rxns:
            if r['id'] not in ex_ids:
                existing.append(r)

# ===== 必修一第四章·元素周期律 =====
add('ch4_periodic', [
    {'id':'ch4_r2','name':'Na与水','equation':'2Na + 2H₂O = 2NaOH + H₂↑','category':'与H₂O','note':'💯 同周期金属性Na>Mg>Al'},
    {'id':'ch4_r3','name':'Mg与水','equation':'Mg + 2H₂O =(热水) Mg(OH)₂ + H₂↑','category':'与H₂O','note':'💯 Mg需要热水才反应'},
    {'id':'ch4_r4','name':'Mg+Al+NaOH原电池','equation':'Mg+2H₂O →(NaOH) Mg(OH)₂+H₂↑','category':'原电池','note':'💯 Al作正极'},
])

# ===== 必修二第五章 =====
# S+O2
add('ch5_s_solid', [
    {'id':'ch5_s1v2','name':'S+O₂','equation':'S + O₂ =(点燃) SO₂','category':'与非金属','phenomenon':'蓝紫色火焰','note':'💯 SO₂刺激性气体'},
])

# SO2+O2→SO3（工业制硫酸）
add('ch5_so2', [
    {'id':'ch5_so2_o1','name':'2SO₂+O₂→2SO₃','equation':'2SO₂ + O₂ ⇌(催化剂/△) 2SO₃','category':'催化氧化','note':'💯 硫酸制造核心反应'},
])
# 需要SO₃物质
so3_sub = None
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            if sub['id'] == 'ch5_so3':
                so3_sub = sub
if so3_sub is None:
    # 如果SO₃没有单独物质，加在SxOy下或创建
    pass

# C+浓H₂SO₄
add('ch5_h2so4_concentrated', [
    {'id':'ch5_cs1','name':'C+浓H₂SO₄','equation':'C + 2H₂SO₄(浓) =(△) CO₂↑ + 2SO₂↑ + 2H₂O','category':'氧化还原','note':'💯 浓硫酸强氧化性'},
])

add('ch5_nh3', [
    {'id':'ch5_nh3_cat1','name':'氨催化氧化','equation':'4NH₃ + 5O₂ →(Pt-Rh/△) 4NO + 6H₂O','category':'催化氧化','note':'💯 工业制硝酸第一步'},
])

# ===== 必修二·原电池 =====
# 盐桥原电池已经有，补知识点
add('ch6_zn_cu', [
    {'id':'ch6_zn_salt','name':'盐桥原电池(Zn-Cu-H₂SO₄)','equation':'Zn + 2H⁺ = Zn²⁺ + H₂↑','category':'原电池','note':'💯 盐桥平衡电荷'},
])

# ===== 必修二·电解池（课本正文有） =====
# 电解饱和食盐水
add('ch5_nacl', [
    {'id':'ch5_nacl_elec','name':'电解饱和食盐水','equation':'2NaCl + 2H₂O =(电解) 2NaOH + H₂↑ + Cl₂↑','category':'电解','note':'💯 氯碱工业'},
])

# ===== 必修二·葡萄糖 =====
add('ch7_glucose', [
    {'id':'ch7_g3','name':'葡萄糖氧化供能','equation':'C₆H₁₂O₆ + 6O₂ = 6CO₂ + 6H₂O + 能量','category':'氧化','note':'💯 细胞呼吸'},
])

# ===== 选修一·盖斯定律相关（补反应） =====
# 中和热
add('ch9_thermo', [
    {'id':'ch9_neu1','name':'中和热(强酸+强碱)','equation':'H⁺ + OH⁻ = H₂O','category':'中和','note':'💯 ΔH=-57.3kJ/mol'},
])

# Ba(OH)2·8H2O+NH4Cl
add('ch9_thermo', [
    {'id':'ch9_e3','name':'Ba(OH)₂·8H₂O+NH₄Cl','equation':'Ba(OH)₂·8H₂O + 2NH₄Cl = BaCl₂ + 2NH₃↑ + 10H₂O','category':'吸热','phenomenon':'温度降低，有刺激性气味','note':'💯 典型的吸热反应'},
])

# ===== 选修一·电解池更多 =====
add('ch9_electrochem', [
    {'id':'ch9_en1','name':'电解精炼铜(阴极)','equation':'Cu²⁺ + 2e⁻ = Cu','category':'电镀','note':'💯 纯铜作阴极'},
    {'id':'ch9_en2','name':'电解精炼铜(阳极)','equation':'Cu - 2e⁻ = Cu²⁺','category':'电镀','note':'💯 粗铜作阳极,金/银/铂沉底'},
])

# ===== 选修三·苯更多 =====
add('ch11_aromatic_sub', [
    {'id':'ch11_bz1','name':'苯+H₂(加成)','equation':'C₆H₆ + 3H₂ →(Ni/△) C₆H₁₂','category':'加成','note':'💯 环己烷'},
])

# ===== 选修三·卤代烃 =====
add('ch11_halide_sub', [
    {'id':'ch11_hal4','name':'溴乙烷水解(制乙醇)','equation':'CH₃CH₂Br + NaOH →(H₂O/△) CH₃CH₂OH + NaBr','category':'水解','note':'💯 卤代烃→醇'},
    {'id':'ch11_hal5','name':'CH₃CH₂Br消去(制乙烯)','equation':'CH₃CH₂Br + NaOH →(C₂H₅OH/△) CH₂=CH₂↑ + NaBr + H₂O','category':'消去','note':'💯 卤代烃→烯烃'},
])

# ===== 选修三·醇更多 =====
add('ch11_alcohol_detail', [
    {'id':'ch11_oh5','name':'乙醇催化氧化→乙醛','equation':'2CH₃CH₂OH + O₂ →(Cu/△) 2CH₃CHO + 2H₂O','category':'催化氧化','note':'💯 Cu→CuO→Cu，交替'},
    {'id':'ch11_oh6','name':'CH₃CH₂OH消去(制乙烯)','equation':'C₂H₅OH →(浓H₂SO₄/170℃) C₂H₄↑ + H₂O','category':'消去','note':'💯 170℃分子内脱水'},
])

# ===== 选修三·丙三醇与HNO₃酯化 =====
add('ch11_alcohol_detail', [
    {'id':'ch11_oh7','name':'甘油+HNO₃(制硝化甘油)','equation':'C₃H₅(OH)₃ + 3HNO₃ →(浓H₂SO₄) C₃H₅(ONO₂)₃ + 3H₂O','category':'酯化','note':'💯 炸药'},
])

# ===== 选修三·酚醛树脂缩聚 =====
add('ch11_poly_detail', [
    {'id':'ch11_pol4','name':'酚醛树脂(线型→体型)','equation':'nC₆H₅OH + nHCHO →(催化剂) 线型→(BaCl₂/△) 体型树脂 + nH₂O','category':'缩聚','note':'💯 电木'},
])

# ===== 选修三·聚酯纤维 =====
add('ch11_ester_sub', [
    {'id':'ch11_es2','name':'涤纶(PET)','equation':'nHOCH₂CH₂OH + nHOOC-C₆H₄-COOH →(催化剂) [OCH₂CH₂OOC-C₆H₄-CO]ₙ + (2n-1)H₂O','category':'缩聚','note':'💯 聚对苯二甲酸乙二酯'},
])

# ===== 选修三·银镜反应（醛） =====
add('ch11_aldehyde_sub', [
    {'id':'ch11_ald2','name':'银氨溶液制备','equation':'AgNO₃ + NH₃·H₂O = AgOH↓ + NH₄NO₃','category':'制备','note':'💯 最初白色沉淀'},
    {'id':'ch11_ald3','name':'银氨溶液继续','equation':'AgOH + 2NH₃·H₂O = [Ag(NH₃)₂]OH + 2H₂O','category':'制备','note':'💯 沉淀溶解→银氨溶液'},
])

# ===== 必修二·铜的电解精炼相关知识点 =====
add('ch6_cu_elec', [
    {'id':'ch6_cu_e1','name':'粗铜电解精炼总反应','equation':'Cu(粗) + Cu²⁺(溶液) =(电解) Cu(纯) + Cu²⁺','category':'电解','note':'💯 阳极泥含Au/Ag/Pt'},
])

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
