import sys, json, re
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

def add_know(sub_id, knows):
    if sub_id in by_id:
        existing = by_id[sub_id].get('knowledge', [])
        ex_ids = {k['q'] for k in existing}
        for k in knows:
            if k['q'] not in ex_ids:
                existing.append(k)

# ===== 必修二·第五章 完整补全 =====
# S+O2 已加
# Fe+S
add('ch5_s_solid', [
    {'id':'ch5_sfs1','name':'Fe+S','equation':'Fe + S =(△) FeS','category':'与金属','note':'💯 Fe+S→FeS(黑色)'},
])
# SO3+H2O→H2SO4
add('ch5_so3', [
    {'id':'ch5_so3h2o','name':'SO₃+H₂O','equation':'SO₃ + H₂O = H₂SO₄','category':'化合','note':'💯 工业制硫酸最后一步'},
])

# 电解饱和食盐水（氯碱工业）
add('ch5_nacl', [
    {'id':'ch5_nacl_elec','name':'电解饱和食盐水','equation':'2NaCl + 2H₂O =(电解) 2NaOH + H₂↑ + Cl₂↑','category':'氯碱工业','note':'💯 阴极H₂，阳极Cl₂'},
])
# 实验室制NH3
add('ch5_nh4_sub', [
    {'id':'ch5_nh4_1','name':'实验室制NH₃','equation':'2NH₄Cl + Ca(OH)₂ =(△) CaCl₂ + 2NH₃↑ + 2H₂O','category':'制备','phenomenon':'刺激性气体，湿润红色石蕊试纸变蓝','note':'💯 铵盐+碱→NH₃'},
])
# NH3+HCl
add('ch5_nh3', [
    {'id':'ch5_nh3_5','name':'NH₃+HCl(白烟)','equation':'NH₃ + HCl = NH₄Cl','category':'化合','phenomenon':'大量白烟','note':'💯 检验NH₃'},
])

# 王水知识
add_know('ch5_hno3', [
    {'q':'王水能溶解什么金属？比例是多少？','a':'能溶解金(Au)和铂(Pt)；浓HNO₃:浓HCl=1:3(体积比)'},
])

# ===== 必修二·乙烯 =====
# C2H4+Br2
add('ch7_ethylene', [
    {'id':'ch7_e3','name':'乙烯+Br₂(溴水褪色)','equation':'C₂H₄ + Br₂ = CH₂BrCH₂Br','category':'加成','phenomenon':'溴水褪色','note':'💯 检验烯烃，1,2-二溴乙烷无色'},
])

# ===== 必修二·葡萄糖 =====
# C6H12O6+O2
add('ch7_glucose', [
    {'id':'ch7_g4','name':'葡萄糖氧化供能','equation':'C₆H₁₂O₆ + 6O₂ = 6CO₂ + 6H₂O','category':'氧化','note':'💯 有氧呼吸，释放能量'},
])

# ===== 必修二·蛋白质 =====
add('ch7_protein', [
    {'id':'ch7_pr6','name':'α-氨基酸通式','equation':'H₂N-CHR-COOH','category':'两性','note':'💯 R为侧链基团'},
])

# ===== 选修一·电解池 =====
# 电解CuCl2
add('ch9_electrochem', [
    {'id':'ch9_elec1','name':'电解CuCl₂(阴极)','equation':'Cu²⁺ + 2e⁻ = Cu','category':'电解','note':'💯 Cu析出'},
    {'id':'ch9_elec2','name':'电解CuCl₂(阳极)','equation':'2Cl⁻ - 2e⁻ = Cl₂↑','category':'电解','note':'💯 阳极Cl₂产生'},
])

# ===== 选修二·配位键 =====
add('ch10_mol_sub', [
    {'id':'ch10_m5','name':'配位键-NH₄⁺','equation':'NH₃ + H⁺ = NH₄⁺','category':'配位','note':'💯 N提供孤对电子'},
    {'id':'ch10_m6','name':'配位键-H₃O⁺','equation':'H₂O + H⁺ = H₃O⁺','category':'配位','note':'💯 O提供孤对电子'},
])

# ===== 选修三·苯 =====
add('ch11_aromatic_sub', [
    {'id':'ch11_bz2','name':'苯+Br₂(取代-溴苯)','equation':'C₆H₆ + Br₂ →(FeBr₃) C₆H₅Br + HBr','category':'取代','note':'💯 溴苯无色油状，比水重'},
    {'id':'ch11_bz3','name':'苯+HNO₃(硝化-硝基苯)','equation':'C₆H₆ + HNO₃ →(浓H₂SO₄/△) C₆H₅NO₂ + H₂O','category':'取代','note':'💯 硝基苯浅黄油状，苦杏仁味'},
])

# ===== 选修三·乙炔 =====
add('ch11_alkyne_sub', [
    {'id':'ch11_alkyne2','name':'乙炔制取(电石法)','equation':'CaC₂ + 2H₂O = C₂H₂↑ + Ca(OH)₂','category':'制备','note':'💯 电石+水→乙炔'},
    {'id':'ch11_alkyne3','name':'乙炔+2Br₂','equation':'C₂H₂ + 2Br₂ = CHBr₂CHBr₂','category':'加成','phenomenon':'溴水褪色','note':''},
])

# ===== 选修三·苯酚+Br₂ =====
add('ch11_phenol', [
    {'id':'ch11_ph6','name':'苯酚+Br₂(定量检验)','equation':'C₆H₅OH + 3Br₂ = C₆H₂Br₃OH↓ + 3HBr','category':'取代','phenomenon':'白色沉淀','note':'💯 2,4,6-三溴苯酚，定量检验'},
])

# ===== 选修三·丙酮+H₂ =====
# 找一个合适的物质
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            if '酮' in sub['id'] or 'ketone' in sub['id']:
                add(sub['id'], [
                    {'id':'ch11_ke2','name':'丙酮+H₂(还原→2-丙醇)','equation':'CH₃COCH₃ + H₂ →(Ni/△) CH₃CHOHCH₃','category':'还原','note':'💯 羰基+H₂→羟基'},
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
