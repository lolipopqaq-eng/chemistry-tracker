import sys, json, re
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

def add_know(sub_id, knows):
    if sub_id in by_id:
        existing = by_id[sub_id].get('knowledge', [])
        ex_ids = {k['q'] for k in existing}
        for k in knows:
            if k['q'] not in ex_ids:
                existing.append(k)

# ===== 必修一·第一章 =====
# Fe(OH)3胶体制备（课本正文）
add_rxns('ch1_colloid', [
    {'id':'ch1_cl1','name':'Fe(OH)₃胶体制备','equation':'FeCl₃ + 3H₂O =(△) Fe(OH)₃(胶体) + 3HCl','category':'制备','note':'💯 向沸水中滴加FeCl₃饱和溶液'},
])

# 离子方程式知识
add_know('ch1_ionic', [
    {'q':'可以拆成离子的物质：____','a':'强酸(HCl/H₂SO₄/HNO₃)、强碱(NaOH/KOH/Ba(OH)₂)、可溶盐'},
    {'q':'不可以拆的物质：____','a':'单质、气体、沉淀、弱电解质、氧化物'},
    {'q':'检验CO₃²⁻的方法','a':'加盐酸→产生CO₂→通入澄清石灰水变浑浊'},
])

# ===== 必修一·第二章 Cl₂更多 =====
# 现在Cl₂已有不少，加Ca(OH)₂相关的
add_rxns('ch2_caoh2', [
    {'id':'ch2_ca1','name':'Cl₂+Ca(OH)₂(制漂白粉)','equation':'2Cl₂ + 2Ca(OH)₂ = CaCl₂ + Ca(ClO)₂ + 2H₂O','category':'制备','note':'💯 制漂白粉'},
    {'id':'ch2_ca2','name':'漂白粉+CO₂+H₂O','equation':'Ca(ClO)₂ + CO₂ + H₂O = CaCO₃↓ + 2HClO','category':'复分解','note':'💯 漂白原理'},
    {'id':'ch2_ca3','name':'84+洁厕灵(危险!)','equation':'NaClO + 2HCl = NaCl + Cl₂↑ + H₂O','category':'氧化还原','note':'⚠️ 混合产生Cl₂有毒气体！'},
])

# 加Na₂O
add_rxns('ch2_na2o', [
    {'id':'ch2_o1','name':'Na₂O+H₂O','equation':'Na₂O + H₂O = 2NaOH','category':'与H₂O','note':''},
])

# ===== Fe更多 =====
add_rxns('ch3_fe_single', [
    {'id':'ch3_fe10','name':'Fe+O₂(燃烧)','equation':'3Fe + 2O₂ =(点燃) Fe₃O₄','category':'与非金属','phenomenon':'火星四射','note':'💯 生成Fe₃O₄'},
])

add_rxns('ch3_fe3o4', [
    {'id':'ch3_f34','name':'Fe₃O₄+酸','equation':'Fe₃O₄ + 8H⁺ = Fe²⁺ + 2Fe³⁺ + 4H₂O','category':'与酸','note':'💯 Fe₃O₄既是FeO·Fe₂O₃'},
])

# Fe³⁺检验
add_rxns('ch3_fecl3', [
    {'id':'ch3_fcl3','name':'Fe³⁺+KSCN','equation':'Fe³⁺ + 3SCN⁻ = Fe(SCN)₃','category':'检验','phenomenon':'血红色','note':'💯 Fe³⁺的特征检验'},
])

# ===== 必修一·第三章 Al =====
add_rxns('ch3_al', [
    {'id':'ch3_al8','name':'铝热反应','equation':'2Al + Fe₂O₃ =(高温) Al₂O₃ + 2Fe','category':'铝热','phenomenon':'剧烈放热、铁水流出','note':'💯 焊接铁轨'},
    {'id':'ch3_al9','name':'Al+HCl','equation':'2Al + 6HCl = 2AlCl₃ + 3H₂↑','category':'与酸','note':''},
])

# ===== 必修二·第五章 =====
# S + Fe（课本正文）
add_rxns('ch5_s_solid', [
    {'id':'ch5_sf1','name':'Fe+S','equation':'Fe + S =(△) FeS','category':'与非金属','note':'💯 S弱氧化性→Fe²⁺'},
])

# SO₂更多
add_rxns('ch5_so2', [
    {'id':'ch5_so2_a3','name':'SO₂+H₂O','equation':'SO₂ + H₂O ⇌ H₂SO₃','category':'与H₂O','note':'💯 亚硫酸，弱酸'},
])

# N₂
add_rxns('ch5_n2', [
    {'id':'ch5_n2_1','name':'N₂+O₂(放电)','equation':'N₂ + O₂ =(放电/高温) 2NO','category':'与非金属','note':''},
    {'id':'ch5_n2_2','name':'N₂+3H₂(合成氨)','equation':'N₂ + 3H₂ ⇌(高温高压/催化剂) 2NH₃','category':'哈伯法','note':'💯 工业制氨'},
])

# NO/NO₂
add_rxns('ch5_no', [
    {'id':'ch5_no_1','name':'2NO+O₂','equation':'2NO + O₂ = 2NO₂','category':'氧化','note':'💯 NO遇空气→NO₂'},
])
add_rxns('ch5_no2', [
    {'id':'ch5_no2_1','name':'NO₂+H₂O(制硝酸)','equation':'3NO₂ + H₂O = 2HNO₃ + NO','category':'与H₂O','note':'💯 工业制硝酸'},
])

# NH₃
add_rxns('ch5_nh3', [
    {'id':'ch5_nh3_3','name':'NH₃+HCl','equation':'NH₃ + HCl = NH₄Cl','category':'化合','phenomenon':'白烟','note':'💯 检验NH₃'},
])

# NH₄⁺检验知识
add_know('ch5_nh4_sub', [
    {'q':'铵根(NH₄⁺)的检验方法','a':'加NaOH溶液→加热→产生NH₃→湿润红色石蕊试纸变蓝'},
])

# Si
add_rxns('ch5_si', [
    {'id':'ch5_si5','name':'SiO₂+HF(玻璃雕刻)','equation':'SiO₂ + 4HF = SiF₄↑ + 2H₂O','category':'与酸','note':'💯 HF腐蚀玻璃'},
])

# ===== 必修二·第六章 =====
add_rxns('ch6_c6', [
    {'id':'ch6_ce1','name':'C+CO₂(吸热)','equation':'C + CO₂ =(高温) 2CO','category':'氧化还原','note':'💯 吸热反应'},
])
add_rxns('ch6_zn_cu', [
    {'id':'ch6_zn1','name':'Zn-Cu原电池(负极)','equation':'Zn - 2e⁻ = Zn²⁺','category':'电极反应','note':'💯 负极：Zn失电子'},
    {'id':'ch6_zn2','name':'Zn-Cu原电池(正极)','equation':'2H⁺ + 2e⁻ = H₂↑','category':'电极反应','note':'💯 正极：H⁺得电子'},
])

# ===== 必修二·第七章 =====
# 甲烷取代
add_rxns('ch7_alkane', [
    {'id':'ch7_m1','name':'CH₄+Cl₂(一氯)','equation':'CH₄ + Cl₂ →(光照) CH₃Cl + HCl','category':'取代','note':'💯 光照取代，四种产物'},
    {'id':'ch7_m2','name':'CH₄+Cl₂(二氯)','equation':'CH₃Cl + Cl₂ →(光照) CH₂Cl₂ + HCl','category':'取代','note':''},
    {'id':'ch7_m3','name':'CH₄+Cl₂(三氯)','equation':'CH₂Cl₂ + Cl₂ →(光照) CHCl₃ + HCl','category':'取代','note':''},
    {'id':'ch7_m4','name':'CH₄+Cl₂(四氯)','equation':'CHCl₃ + Cl₂ →(光照) CCl₄ + HCl','category':'取代','note':''},
])

# 乙烯
add_rxns('ch7_ethylene', [
    {'id':'ch7_e2','name':'乙烯+H₂O(水合法)','equation':'C₂H₄ + H₂O →(H₃PO₄/△) CH₃CH₂OH','category':'加成','note':'💯 工业制乙醇'},
])

# 聚乙烯
add_rxns('ch7_pe', [
    {'id':'ch7_pe1','name':'乙烯加聚(PE)','equation':'nCH₂=CH₂ →(催化剂) [CH₂-CH₂]ₙ','category':'加聚','note':'💯 聚乙烯PE，最广泛塑料'},
])

# 乙醇催化氧化（课本正文）
add_rxns('ch7_ethanol', [
    {'id':'ch7_et3','name':'乙醇催化氧化(制乙醛)','equation':'2CH₃CH₂OH + O₂ →(Cu或Ag/△) 2CH₃CHO + 2H₂O','category':'催化氧化','note':'💯 Cu→黑→红'},
])

# 葡萄糖（课本正文检验）
add_rxns('ch7_glucose', [
    {'id':'ch7_g1','name':'葡萄糖银镜反应','equation':'CH₂OH(CHOH)₄CHO + 2Ag(NH₃)₂OH →(△) CH₂OH(CHOH)₄COONH₄ + 2Ag↓ + 3NH₃ + H₂O','category':'银镜','phenomenon':'银镜生成','note':'💯 醛基检验'},
    {'id':'ch7_g2','name':'葡萄糖+Cu(OH)₂','equation':'CH₂OH(CHOH)₄CHO + 2Cu(OH)₂ + NaOH →(△) CH₂OH(CHOH)₄COONa + Cu₂O↓ + 3H₂O','category':'氧化','phenomenon':'砖红色沉淀','note':''},
])

# 淀粉水解
add_rxns('ch7_starch', [
    {'id':'ch7_st1','name':'淀粉水解(制葡萄糖)','equation':'(C₆H₁₀O₅)ₙ + nH₂O →(酸或酶/△) nC₆H₁₂O₆','category':'水解','note':'💯 最终产物葡萄糖'},
])

# 蛋白质检验
add_rxns('ch7_protein', [
    {'id':'ch7_pr1','name':'浓硝酸使蛋白质变黄','equation':'蛋白质 + 浓HNO₃ →(△) 黄色','category':'检验','note':'💯 黄蛋白反应，检验含苯环蛋白质'},
])

# ===== 选修一·电化学 =====
add_rxns('ch9_electrochem', [
    {'id':'ch9_e10','name':'电解CuCl₂','equation':'CuCl₂ =(电解) Cu + Cl₂↑','category':'电解','note':'💯 阴极Cu析出，阳极Cl₂产生'},
])

# ===== 选修三·炔烃 =====
add_rxns('ch11_alkyne_sub', [
    {'id':'ch11_alkyne1','name':'乙炔制取(电石法)','equation':'CaC₂ + 2H₂O = C₂H₂↑ + Ca(OH)₂','category':'制备','note':'💯 电石+水→乙炔'},
])

# ===== 选修三·醛酮 =====
add_rxns('ch11_aldehyde_sub', [
    {'id':'ch11_ald1','name':'甲醛的银镜反应','equation':'HCHO + 4Ag(NH₃)₂OH →(△) (NH₄)₂CO₃ + 4Ag↓ + 6NH₃ + 2H₂O','category':'银镜','note':'💯 甲醛相当于含2个醛基'},
])

# ===== 选修三·酚 =====
add_rxns('ch11_phenol', [
    {'id':'ch11_ph4','name':'苯酚+FeCl₃(显色)','equation':'6C₆H₅OH + FeCl₃ = H₃[Fe(OC₆H₅)₆] + 3HCl','category':'检验','phenomenon':'紫色','note':'💯 FeCl₃显色反应'},
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
