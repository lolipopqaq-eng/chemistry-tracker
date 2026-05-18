import sys, json
sys.stdout.reconfigure(encoding='utf-8')
raw = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))

by_id = {}
for ch in raw:
    for sec in ch['sections']:
        for sub in sec['substances']:
            by_id[sub['id']] = sub

def add_rxns(sub_id, rxns):
    if sub_id in by_id:
        existing = by_id[sub_id].get('reactions', [])
        ex_ids = {r['id'] for r in existing}
        for r in rxns:
            if r['id'] not in ex_ids:
                existing.append(r)

# ===== 必修一·钠 =====
add_rxns('ch2_na', [
    {'id':'ch2_na_m1','name':'Na与乙醇反应','equation':'2Na + 2C₂H₅OH = 2C₂H₅ONa + H₂↑','category':'与有机物','note':'💯 Na浮在乙醇表面'},
    {'id':'ch2_na_m2','name':'Na与酚反应','equation':'2Na + 2C₆H₅OH = 2C₆H₅ONa + H₂↑','category':'与有机物','note':''},
])

# ===== NaOH补充（几十个反应） =====
add_rxns('ch2_naoh', [
    # 与酸
    {'id':'ch2_n20','name':'NaOH+H₂SO₄','equation':'2NaOH + H₂SO₄ = Na₂SO₄ + 2H₂O','category':'中和','note':''},
    {'id':'ch2_n21','name':'NaOH+HNO₃','equation':'NaOH + HNO₃ = NaNO₃ + H₂O','category':'中和','note':''},
    {'id':'ch2_n22','name':'NaOH+H₃PO₄','equation':'3NaOH + H₃PO₄ = Na₃PO₄ + 3H₂O','category':'中和','note':''},
    # 与酸性氧化物
    {'id':'ch2_n23','name':'NaOH+CO₂(少量)','equation':'2NaOH + CO₂ = Na₂CO₃ + H₂O','category':'与酸性氧化物','note':'💯 少量→碳酸盐'},
    {'id':'ch2_n24','name':'NaOH+CO₂(过量)','equation':'NaOH + CO₂ = NaHCO₃','category':'与酸性氧化物','note':'💯 过量→碳酸氢盐'},
    {'id':'ch2_n25','name':'NaOH+SO₂(少量)','equation':'2NaOH + SO₂ = Na₂SO₃ + H₂O','category':'与酸性氧化物','note':''},
    {'id':'ch2_n26','name':'NaOH+SO₃','equation':'2NaOH + SO₃ = Na₂SO₄ + H₂O','category':'与酸性氧化物','note':''},
    {'id':'ch2_n27','name':'NaOH+SiO₂','equation':'2NaOH + SiO₂ = Na₂SiO₃ + H₂O','category':'与酸性氧化物','note':'💯 玻璃被碱腐蚀'},
    # 与金属盐
    {'id':'ch2_n28','name':'NaOH+CuSO₄','equation':'2NaOH + CuSO₄ = Cu(OH)₂↓ + Na₂SO₄','category':'复分解','phenomenon':'蓝色沉淀','note':'💯 新制Cu(OH)₂用于检验醛基'},
    {'id':'ch2_n29','name':'NaOH+FeCl₃','equation':'3NaOH + FeCl₃ = Fe(OH)₃↓ + 3NaCl','category':'复分解','phenomenon':'红褐色沉淀','note':'💯 Fe³⁺检验'},
    {'id':'ch2_n30','name':'NaOH+FeCl₂','equation':'2NaOH + FeCl₂ = Fe(OH)₂↓ + 2NaCl','category':'复分解','phenomenon':'白色沉淀→灰绿→红褐','note':'💯 空气中被氧化'},
    {'id':'ch2_n31','name':'NaOH+MgCl₂','equation':'2NaOH + MgCl₂ = Mg(OH)₂↓ + 2NaCl','category':'复分解','phenomenon':'白色沉淀','note':''},
    {'id':'ch2_n32','name':'NaOH+AlCl₃(适量)','equation':'3NaOH + AlCl₃ = Al(OH)₃↓ + 3NaCl','category':'复分解','phenomenon':'白色沉淀','note':'💯 Al³⁺+3OH⁻'},
    {'id':'ch2_n33','name':'NaOH+AlCl₃(过量)','equation':'NaOH + Al(OH)₃ = NaAlO₂ + 2H₂O','category':'与两性氢氧化物','note':'💯 Al(OH)₃溶于强碱'},
    # 与两性物质
    {'id':'ch2_n34','name':'NaOH+Al₂O₃','equation':'2NaOH + Al₂O₃ = 2NaAlO₂ + H₂O','category':'与两性氧化物','note':''},
    {'id':'ch2_n35','name':'NaOH+Al(OH)₃','equation':'NaOH + Al(OH)₃ = NaAlO₂ + 2H₂O','category':'与两性氢氧化物','note':''},
    # 与有机物
    {'id':'ch2_n36','name':'NaOH+苯酚','equation':'NaOH + C₆H₅OH = C₆H₅ONa + H₂O','category':'与有机物','note':'💯 苯酚弱酸性'},
    {'id':'ch2_n37','name':'NaOH+乙酸','equation':'NaOH + CH₃COOH = CH₃COONa + H₂O','category':'与有机物','note':'中和反应'},
    {'id':'ch2_n38','name':'NaOH+乙酸乙酯(皂化)','equation':'CH₃COOC₂H₅ + NaOH →(△) CH₃COONa + C₂H₅OH','category':'皂化','note':'💯 不可逆'},
    {'id':'ch2_n39','name':'NaOH+氯乙烷(取代)','equation':'CH₃CH₂Cl + NaOH →(H₂O/△) CH₃CH₂OH + NaCl','category':'水解','note':'💯 卤代烃的水解'},
    {'id':'ch2_n40','name':'NaOH+氯乙烷(消去)','equation':'CH₃CH₂Cl + NaOH →(C₂H₅OH/△) CH₂=CH₂↑ + NaCl + H₂O','category':'消去','note':'💯 卤代烃消去→烯'},
    {'id':'ch2_n41','name':'NaOH+油脂','equation':'油脂 + 3NaOH →(△) 3脂肪酸钠 + 甘油','category':'皂化','note':'💯 制肥皂'},
    {'id':'ch2_n42','name':'NaOH+蛋白质','equation':'蛋白质 + NaOH →(△) 水解产物','category':'水解','note':'蛋白质碱性水解'},
    # 与非金属
    {'id':'ch2_n43','name':'NaOH+Cl₂(冷)','equation':'2NaOH + Cl₂ = NaCl + NaClO + H₂O','category':'歧化','note':'💯 制漂白液'},
    {'id':'ch2_n44','name':'NaOH+Cl₂(热)','equation':'6NaOH + 3Cl₂ =(△) 5NaCl + NaClO₃ + 3H₂O','category':'歧化','note':''},
    {'id':'ch2_n45','name':'NaOH+S(热)','equation':'6NaOH + 3S =(△) 2Na₂S + Na₂SO₃ + 3H₂O','category':'歧化','note':''},
    {'id':'ch2_n46','name':'NaOH+Si','equation':'2NaOH + Si + H₂O = Na₂SiO₃ + 2H₂↑','category':'与非金属','note':'💯 Si+强碱→H₂'},
    # 与酸式盐
    {'id':'ch2_n47','name':'NaOH+NaHCO₃','equation':'NaOH + NaHCO₃ = Na₂CO₃ + H₂O','category':'与酸式盐','note':''},
    {'id':'ch2_n48','name':'NaOH+NH₄Cl','equation':'NaOH + NH₄Cl = NaCl + NH₃↑ + H₂O','category':'与铵盐','phenomenon':'刺激性气体','note':'💯 实验室制NH₃'},
])

# ===== Na₂CO₃ =====
add_rxns('ch2_na2co3', [
    {'id':'ch2_c11','name':'Na₂CO₃+HCl(少量)','equation':'Na₂CO₃ + HCl = NaCl + NaHCO₃','category':'与酸','note':'💯 少量HCl→HCO₃⁻'},
    {'id':'ch2_c12','name':'Na₂CO₃+HCl(过量)','equation':'Na₂CO₃ + 2HCl = 2NaCl + H₂O + CO₂↑','category':'与酸','note':'💯 过量→CO₂'},
    {'id':'ch2_c13','name':'Na₂CO₃+Ca(OH)₂','equation':'Na₂CO₃ + Ca(OH)₂ = CaCO₃↓ + 2NaOH','category':'复分解','note':'💯 工业制碱'},
    {'id':'ch2_c14','name':'Na₂CO₃+BaCl₂','equation':'Na₂CO₃ + BaCl₂ = BaCO₃↓ + 2NaCl','category':'复分解','phenomenon':'白色沉淀','note':''},
    {'id':'ch2_c15','name':'Na₂CO₃+CaCl₂','equation':'Na₂CO₃ + CaCl₂ = CaCO₃↓ + 2NaCl','category':'复分解','note':''},
    {'id':'ch2_c16','name':'Na₂CO₃水解(第一步)','equation':'CO₃²⁻ + H₂O ⇌ HCO₃⁻ + OH⁻','category':'水解','note':'💯 使酚酞变红'},
    {'id':'ch2_c17','name':'Na₂CO₃+AlCl₃(双水解)','equation':'3Na₂CO₃ + 2AlCl₃ + 3H₂O = 2Al(OH)₃↓ + 3CO₂↑ + 6NaCl','category':'双水解','note':''},
])

# ===== NaHCO₃ =====
add_rxns('ch2_nahco3', [
    {'id':'ch2_hc1','name':'NaHCO₃+HCl','equation':'NaHCO₃ + HCl = NaCl + H₂O + CO₂↑','category':'与酸','note':'💯 治疗胃酸过多'},
    {'id':'ch2_hc2','name':'NaHCO₃+NaOH','equation':'NaHCO₃ + NaOH = Na₂CO₃ + H₂O','category':'与碱','note':''},
    {'id':'ch2_hc3','name':'NaHCO₃+Ca(OH)₂(少量)','equation':'NaHCO₃ + Ca(OH)₂ = CaCO₃↓ + NaOH + H₂O','category':'复分解','note':'💯 少量HCO₃⁻'},
    {'id':'ch2_hc4','name':'NaHCO₃+Ca(OH)₂(过量)','equation':'2NaHCO₃ + Ca(OH)₂ = CaCO₃↓ + Na₂CO₃ + 2H₂O','category':'复分解','note':'💯 过量HCO₃⁻'},
    {'id':'ch2_hc5','name':'NaHCO₃分解','equation':'2NaHCO₃ =(△) Na₂CO₃ + H₂O + CO₂↑','category':'分解','note':'💯 稳定性Na₂CO₃>NaHCO₃'},
])

# ===== Cl₂更多反应 =====
add_rxns('ch2_cl2', [
    {'id':'ch2_cl7','name':'Cl₂+NaBr','equation':'Cl₂ + 2NaBr = 2NaCl + Br₂','category':'置换','phenomenon':'溶液变橙','note':'💯 Cl₂>Br₂氧化性'},
    {'id':'ch2_cl8','name':'Cl₂+KI','equation':'Cl₂ + 2KI = 2KCl + I₂','category':'置换','phenomenon':'溶液变棕/淀粉变蓝','note':'💯 Cl₂>I₂'},
    {'id':'ch2_cl9','name':'Cl₂+SO₂+H₂O','equation':'Cl₂ + SO₂ + 2H₂O = H₂SO₄ + 2HCl','category':'氧化还原','note':'💯 SO₂漂白可逆,Cl₂不可逆'},
])

# ===== Fe更多反应 =====
add_rxns('ch3_fe_single', [
    {'id':'ch3_fe8','name':'Fe+CuSO₄','equation':'Fe + CuSO₄ = FeSO₄ + Cu','category':'置换','phenomenon':'Cu析出','note':'💯 Fe>Cu还原性'},
    {'id':'ch3_fe9','name':'Fe+AgNO₃','equation':'Fe + 2AgNO₃ = Fe(NO₃)₂ + 2Ag','category':'置换','note':''},
])

add_rxns('ch3_feo', [
    {'id':'ch3_fo3','name':'FeO+HCl','equation':'FeO + 2HCl = FeCl₂ + H₂O','category':'与酸','note':'💯 生成Fe²⁺'},
    {'id':'ch3_fo4','name':'FeO+HNO₃','equation':'3FeO + 10HNO₃(稀) = 3Fe(NO₃)₃ + NO↑ + 5H₂O','category':'氧化还原','note':'💯 稀HNO₃氧化FeO→Fe³⁺'},
])

add_rxns('ch3_fe2o3', [
    {'id':'ch3_f2o4','name':'Fe₂O₃+HI','equation':'Fe₂O₃ + 6HI = 2FeI₂ + I₂ + 3H₂O','category':'氧化还原','note':'💯 HI还原Fe³⁺→Fe²⁺'},
])

# ===== Cu =====
add_rxns('ch3_cu', [
    {'id':'ch3_cu2','name':'Cu+Cl₂','equation':'Cu + Cl₂ =(点燃) CuCl₂','category':'与非金属','phenomenon':'棕黄色烟','note':''},
    {'id':'ch3_cu3','name':'Cu+S','equation':'2Cu + S =(△) Cu₂S','category':'与非金属','note':'💯 S弱氧化→Cu⁺'},
    {'id':'ch3_cu4','name':'Cu+O₂','equation':'2Cu + O₂ =(△) 2CuO','category':'与非金属','phenomenon':'黑色','note':''},
    {'id':'ch3_cu5','name':'Cu+HNO₃(浓)','equation':'Cu + 4HNO₃(浓) = Cu(NO₃)₂ + 2NO₂↑ + 2H₂O','category':'与酸','phenomenon':'红棕色气体','note':''},
    {'id':'ch3_cu6','name':'Cu+HNO₃(稀)','equation':'3Cu + 8HNO₃(稀) = 3Cu(NO₃)₂ + 2NO↑ + 4H₂O','category':'与酸','note':''},
    {'id':'ch3_cu7','name':'Cu+H₂SO₄(浓)','equation':'Cu + 2H₂SO₄(浓) =(△) CuSO₄ + SO₂↑ + 2H₂O','category':'与酸','phenomenon':'刺激性气体','note':'💯 浓硫酸氧化性'},
    {'id':'ch3_cu8','name':'Cu+FeCl₃','equation':'Cu + 2FeCl₃ = 2FeCl₂ + CuCl₂','category':'氧化还原','note':'💯 腐蚀印刷电路板'},
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
