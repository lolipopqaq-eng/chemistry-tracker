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

# ===== 1. 金属单质：Na, Mg, Al, Fe, Zn, Cu =====
# Al
add('ch3_al', [
    {'id':'ch3_al10','name':'Al+O₂','equation':'4Al + 3O₂ = 2Al₂O₃','category':'与非金属','note':'💯 常温钝化，氧化膜致密'},
    {'id':'ch3_al11','name':'Al+H₂SO₄(稀)','equation':'2Al + 3H₂SO₄ = Al₂(SO₄)₃ + 3H₂↑','category':'与酸','note':''},
    {'id':'ch3_al12','name':'Al+S','equation':'2Al + 3S =(△) Al₂S₃','category':'与非金属','note':''},
    {'id':'ch3_al13','name':'Al+N₂','equation':'2Al + N₂ =(高温) 2AlN','category':'与非金属','note':''},
])

# Mg
add('ch3_mg', [
    {'id':'ch3_mg1','name':'Mg+O₂','equation':'2Mg + O₂ =(点燃) 2MgO','phenomenon':'耀眼白光','category':'与非金属','note':''},
    {'id':'ch3_mg2','name':'Mg+N₂(燃烧)','equation':'3Mg + N₂ =(点燃) Mg₃N₂','category':'与非金属','note':'💯 Mg能在N₂中燃烧'},
    {'id':'ch3_mg3','name':'Mg+CO₂(燃烧)','equation':'2Mg + CO₂ =(点燃) 2MgO + C','category':'氧化还原','phenomenon':'剧烈燃烧，有黑色C','note':'💯 不能用CO₂灭Mg火'},
    {'id':'ch3_mg4','name':'Mg+H₂SO₄(稀)','equation':'Mg + H₂SO₄ = MgSO₄ + H₂↑','category':'与酸','note':'💯 反应剧烈'},
    {'id':'ch3_mg5','name':'Mg+HCl','equation':'Mg + 2HCl = MgCl₂ + H₂↑','category':'与酸','note':''},
])

# Zn
add('ch3_single_metals', [
    {'id':'ch3_zn1','name':'Zn+HCl','equation':'Zn + 2HCl = ZnCl₂ + H₂↑','category':'与酸','note':'💯 实验室制H₂'},
    {'id':'ch3_zn2','name':'Zn+H₂SO₄(稀)','equation':'Zn + H₂SO₄ = ZnSO₄ + H₂↑','category':'与酸','note':''},
    {'id':'ch3_zn3','name':'Zn+CuSO₄','equation':'Zn + CuSO₄ = ZnSO₄ + Cu','category':'置换','note':'💯 原电池负极Zn'},
])

# ===== 2. 非金属单质：H₂, C, Si, N₂, O₂, S, Cl₂ =====
add('ch1_oxidation', [
    {'id':'ch1_h2_1','name':'H₂+CuO','equation':'H₂ + CuO =(△) Cu + H₂O','category':'氧化还原','note':'💯 H₂的还原性'},
])

add('ch2_hcl', [
    {'id':'ch2_hcl1','name':'H₂+Cl₂(燃烧)','equation':'H₂ + Cl₂ =(点燃) 2HCl','category':'化合','phenomenon':'苍白色火焰','note':''},
])

add('ch5_c_solid', [
    {'id':'ch5_c4','name':'C+2H₂SO₄(浓)','equation':'C + 2H₂SO₄(浓) =(△) CO₂↑ + 2SO₂↑ + 2H₂O','category':'氧化还原','note':'💯 浓硫酸强氧化性'},
])

# ===== 3. 氧化物 =====
# CuO
add('ch3_cuo', [
    {'id':'ch3_cuo1','name':'CuO+HCl','equation':'CuO + 2HCl = CuCl₂ + H₂O','category':'与酸','note':''},
    {'id':'ch3_cuo2','name':'CuO+H₂SO₄','equation':'CuO + H₂SO₄ = CuSO₄ + H₂O','category':'与酸','phenomenon':'蓝色溶液','note':'💯 CuSO₄溶液蓝色'},
    {'id':'ch3_cuo3','name':'CuO+HNO₃','equation':'CuO + 2HNO₃ = Cu(NO₃)₂ + H₂O','category':'与酸','note':''},
    {'id':'ch3_cuo4','name':'CuO+CO','equation':'CuO + CO =(△) Cu + CO₂','category':'氧化还原','note':'💯 CO还原CuO'},
    {'id':'ch3_cuo5','name':'CuO+H₂','equation':'CuO + H₂ =(△) Cu + H₂O','category':'氧化还原','note':'💯 H₂还原CuO'},
])

# Al₂O₃
add('ch3_al2o3', [
    {'id':'ch3_al2o3_1','name':'Al₂O₃+HCl','equation':'Al₂O₃ + 6HCl = 2AlCl₃ + 3H₂O','category':'与酸','note':'💯 两性氧化物'},
    {'id':'ch3_al2o3_2','name':'Al₂O₃+NaOH','equation':'Al₂O₃ + 2NaOH = 2NaAlO₂ + H₂O','category':'与碱','note':''},
])

# ===== 4. 酸 =====
# H₂SO₄
add('ch5_h2so4_concentrated', [
    {'id':'ch5_h2so4_1','name':'Fe+H₂SO₄(浓)(钝化)','equation':'Fe + H₂SO₄(浓) =(常温) Fe氧化物钝化膜','category':'钝化','note':'💯 浓硫酸+Fe→钝化'},
    {'id':'ch5_h2so4_2','name':'Al+H₂SO₄(浓)(钝化)','equation':'Al + H₂SO₄(浓) =(常温) Al氧化物钝化膜','category':'钝化','note':'💯 可用铝罐装浓硫酸'},
])

# HNO₃
add('ch5_hno3', [
    {'id':'ch5_hno3_1','name':'Cu+浓HNO₃','equation':'Cu + 4HNO₃(浓) = Cu(NO₃)₂ + 2NO₂↑ + 2H₂O','category':'与金属','phenomenon':'红棕色气体','note':''},
    {'id':'ch5_hno3_2','name':'Cu+稀HNO₃','equation':'3Cu + 8HNO₃(稀) = 3Cu(NO₃)₂ + 2NO↑ + 4H₂O','category':'与金属','note':''},
    {'id':'ch5_hno3_3','name':'Fe+稀HNO₃(少量)','equation':'Fe + 4HNO₃(稀) = Fe(NO₃)₃ + NO↑ + 2H₂O','category':'与金属','note':'💯 少量Fe→Fe³⁺'},
    {'id':'ch5_hno3_4','name':'Fe+稀HNO₃(过量)','equation':'3Fe + 8HNO₃(稀) = 3Fe(NO₃)₂ + 2NO↑ + 4H₂O','category':'与金属','note':'💯 过量Fe→Fe²⁺'},
    {'id':'ch5_hno3_5','name':'C+浓HNO₃','equation':'C + 4HNO₃(浓) =(△) CO₂↑ + 4NO₂↑ + 2H₂O','category':'氧化还原','note':''},
])

# H₂S
add('ch5_so2', [
    {'id':'ch5_h2s1','name':'H₂S完全燃烧','equation':'2H₂S + 3O₂ =(点燃) 2H₂O + 2SO₂','category':'燃烧','note':''},
    {'id':'ch5_h2s2','name':'H₂S+SO₂','equation':'2H₂S + SO₂ = 3S↓ + 2H₂O','category':'氧化还原','phenomenon':'黄色沉淀','note':'💯 H₂S+SO₂→S+H₂O'},
])

# ===== 5. NO,NO₂更多 =====
add('ch5_no2', [
    {'id':'ch5_no2_r1','name':'NO₂+SO₂','equation':'NO₂ + SO₂ = NO + SO₃','category':'氧化还原','note':''},
])

# ===== 6. 选修三大幅补充 =====
# 更多卤代烃
add('ch11_halide_sub', [
    {'id':'ch11_hal6','name':'1,2-二溴乙烷+NaOH(消去)','equation':'CH₂BrCH₂Br + 2NaOH →(C₂H₅OH/△) CH≡CH↑ + 2NaBr + 2H₂O','category':'消去','note':'💯 二溴代烷二倍消去'},
    {'id':'ch11_hal7','name':'CHCl₃+O₂(光气)','equation':'2CHCl₃ + O₂ →(光照) 2COCl₂ + 2HCl','category':'氧化','note':'💯 光气剧毒！CHCl₃避光密封'},
])

# 更多醇
add('ch11_alcohol_detail', [
    {'id':'ch11_oh8','name':'2-丙醇催化氧化','equation':'2CH₃CHOHCH₃ + O₂ →(Cu/△) 2CH₃COCH₃ + 2H₂O','category':'催化氧化','note':'💯 仲醇→酮'},
    {'id':'ch11_oh9','name':'甲醇+Na','equation':'2CH₃OH + 2Na = 2CH₃ONa + H₂↑','category':'与有机物','note':''},
])

# 更多醛
add('ch11_aldehyde_sub', [
    {'id':'ch11_ald4','name':'乙醛+H₂(还原)','equation':'CH₃CHO + H₂ →(Ni/△) CH₃CH₂OH','category':'还原','note':'💯 醛基+H₂→醇'},
    {'id':'ch11_ald5','name':'乙醛+O₂(氧化)','equation':'2CH₃CHO + O₂ →(催化剂/△) 2CH₃COOH','category':'氧化','note':'💯 乙醛→乙酸，工业制乙酸'},
])

# 更多酮
add('ch11_ketone', [
    {'id':'ch11_ke1','name':'丙酮+H₂(还原)','equation':'CH₃COCH₃ + H₂ →(Ni/△) CH₃CHOHCH₃','category':'还原','note':'💯 酮+H₂→仲醇'},
]) if 'ch11_ketone' in by_id else None

# 更多羧酸
add('ch11_hac', [
    {'id':'ch11_hac4','name':'甲酸银镜','equation':'HCOOH + 2Ag(NH₃)₂OH →(△) (NH₄)₂CO₃ + 2Ag↓ + 2NH₃ + H₂O','category':'银镜','note':'💯 HCOOH有醛基'},
])

# 更多酯
add('ch11_ester_sub', [
    {'id':'ch11_es3','name':'乙酸乙酯+H₂O(酸性水解)','equation':'CH₃COOC₂H₅ + H₂O ⇌(H⁺/△) CH₃COOH + C₂H₅OH','category':'水解','note':'💯 酯在酸性中可逆水解'},
])

# 更多糖类
add('ch11_sugar_sub', [
    {'id':'ch11_su1','name':'蔗糖水解','equation':'C₁₂H₂₂O₁₁ + H₂O →(酸或酶/△) C₆H₁₂O₆(葡萄糖) + C₆H₁₂O₆(果糖)','category':'水解','note':''},
    {'id':'ch11_su2','name':'麦芽糖水解','equation':'C₁₂H₂₂O₁₁ + H₂O →(酸或酶/△) 2C₆H₁₂O₆(葡萄糖)','category':'水解','note':''},
])

# 氨基酸缩合
add('ch11_amino_acid', [
    {'id':'ch11_aa1','name':'氨基酸缩合(二肽)','equation':'2H₂NCH₂COOH →(催化剂) H₂NCH₂CONHCH₂COOH + H₂O','category':'缩合','note':'💯 肽键-CONH-'},
])

# 更多合成高分子
add('ch11_poly_sub', [
    {'id':'ch11_ps2','name':'聚丙烯腈(腈纶)','equation':'nCH₂=CHCN →(催化剂) [CH₂-CH(CN)]ₙ','category':'加聚','note':'💯 腈纶(人造羊毛)'},
    {'id':'ch11_ps3','name':'顺丁橡胶制备','equation':'nCH₂=CH-CH=CH₂ →(催化剂) [CH₂-CH=CH-CH₂]ₙ','category':'加聚','note':'💯 1,3-丁二烯加聚'},
    {'id':'ch11_ps4','name':'聚异戊二烯(天然橡胶)','equation':'nCH₂=C(CH₃)-CH=CH₂ →(催化剂) 聚异戊二烯','category':'加聚','note':'💯 天然橡胶单体'},
])

# ===== 7. 更多知识点 =====
add_know('ch5_h2so4_concentrated', [
    {'q':'浓H₂SO₄具有哪些特性？','a':'吸水性(干燥剂)、脱水性(碳化)、强氧化性(Cu/C/Fe/Al钝化)'},
])
add_know('ch5_hno3', [
    {'q':'浓HNO₃和稀HNO₃与Cu反应产物区别','a':'浓HNO₃→NO₂(红棕)；稀HNO₃→NO(无色)'},
])
add_know('ch5_so2', [
    {'q':'SO₂的漂白性有什么特点？（与Cl₂比较）','a':'SO₂与有色物质化合(可逆，加热恢复)；Cl₂氧化(不可逆)'},
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
