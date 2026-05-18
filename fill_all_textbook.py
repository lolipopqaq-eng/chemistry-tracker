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

def add_know(sub_id, knows):
    if sub_id in by_id:
        existing = by_id[sub_id].get('knowledge', [])
        ex_ids = {k['q'] for k in existing}
        for k in knows:
            if k['q'] not in ex_ids:
                existing.append(k)

# ===== 必修一·第一章 =====
# 资料卡片：胶体聚沉
add_know('ch1_colloid', [
    {'q':'胶体聚沉的三种方法','a':'①加热；②加电解质；③加相反电荷的胶体'},
    {'q':'丁达尔效应可用于____','a':'区分溶液和胶体'},
    {'q':'明矾净水的原理','a':'Al³⁺水解→Al(OH)₃胶体→吸附杂质'},
])

# 资料卡片：电解质
add_know('ch1_ionic', [
    {'q':'常见的强酸有哪些？','a':'HCl、H₂SO₄、HNO₃、HBr、HI、HClO₄'},
    {'q':'常见的强碱有哪些？','a':'NaOH、KOH、Ba(OH)₂、Ca(OH)₂'},
])

# ===== 必修一·第二章 =====
# 资料卡片：氯水保存
add_know('ch2_hclo', [
    {'q':'氯水为什么要避光保存？','a':'HClO光照分解：2HClO→2HCl+O₂↑'},
])

# ===== 必修一·第三章 =====
# 资料卡片：Fe²⁺/Fe³⁺补充
add('ch3_fecl2', [
    {'id':'ch3_fc2','name':'FeCl₂+NaOH','equation':'FeCl₂ + 2NaOH = Fe(OH)₂↓ + 2NaCl','category':'复分解','phenomenon':'白色沉淀→灰绿→红褐','note':'💯 Fe(OH)₂极易被氧化'},
])
add('ch3_fecl3', [
    {'id':'ch3_fc3','name':'FeCl₃+NaOH','equation':'FeCl₃ + 3NaOH = Fe(OH)₃↓ + 3NaCl','category':'复分解','phenomenon':'红褐色沉淀','note':''},
])

# ===== 必修一·第四章 元素周期律 =====
# 资料卡片：卤素性质递变
add_know('ch4_periodic', [
    {'q':'卤素单质氧化性顺序（从强到弱）','a':'F₂>Cl₂>Br₂>I₂'},
    {'q':'卤素阴离子还原性顺序（从强到弱）','a':'I⁻>Br⁻>Cl⁻>F⁻'},
    {'q':'同主族非金属性变化规律','a':'从上到下减弱（F>Cl>Br>I）'},
])

# ===== 必修二·第五章 =====
# 课本正文：NH₃实验室制法
add('ch5_nh3', [
    {'id':'ch5_nh3_4','name':'实验室制NH₃','equation':'2NH₄Cl + Ca(OH)₂ =(△) CaCl₂ + 2NH₃↑ + 2H₂O','category':'制备','note':'💯 加热铵盐和碱'},
])

# 课本正文：工业合成硝酸
add('ch5_no', [
    {'id':'ch5_no_2','name':'2NO+O₂→2NO₂','equation':'2NO + O₂ = 2NO₂','category':'氧化','note':'💯 NO遇空气立即变红棕色'},
])
add('ch5_no2', [
    {'id':'ch5_no2_2','name':'NO₂+SO₂(资料卡片)','equation':'NO₂ + SO₂ = NO + SO₃','category':'氧化','note':''},
])

# 课本正文：SiO₂制Si
add('ch5_si', [
    {'id':'ch5_si6','name':'SiO₂+2C(制粗硅)','equation':'SiO₂ + 2C =(高温) Si + 2CO↑','category':'制备','note':'💯 粗硅，后续纯化'},
    {'id':'ch5_si7','name':'Si+2Cl₂','equation':'Si + 2Cl₂ =(△) SiCl₄','category':'纯化','note':''},
])

# 资料卡片：海水提溴
add('ch5_br2', [])  # 已经有海水提溴反应在ch5_br2和ch8

# 资料卡片：王水
add_know('ch5_hno3', [
    {'q':'王水的组成是什么？能溶解什么？','a':'浓HNO₃:浓HCl=1:3(体积比)，能溶解金和铂'},
])

# ===== 必修二·第七章 有机 =====
# 资料卡片：乙醇+Na
add('ch7_ethanol', [
    {'id':'ch7_et4','name':'乙醇+Na','equation':'2C₂H₅OH + 2Na = 2C₂H₅ONa + H₂↑','category':'置换','note':'💯 -OH上的H被置换'},
])

# 资料卡片：乙酸酸性
add('ch7_hac', [
    {'id':'ch7_ha1','name':'乙酸+Na₂CO₃','equation':'2CH₃COOH + Na₂CO₃ = 2CH₃COONa + H₂O + CO₂↑','category':'与盐','note':'💯 酸性：H₂CO₃<CH₃COOH'},
])

# 资料卡片：乙酸乙酯制备注意事项
add_know('ch7_ethylester', [
    {'q':'乙酸乙酯制备中饱和Na₂CO₃的作用','a':'①吸收乙醇；②中和乙酸；③降低酯溶解度'},
    {'q':'乙酸乙酯制备中浓H₂SO₄的作用','a':'催化剂和吸水剂'},
])

# ===== 必修二·第八章 资源 =====
# 课本：海水提镁
add('ch8_develop', [
    {'id':'ch8_dev1','name':'海水提镁-电解MgCl₂','equation':'MgCl₂(熔融) =(电解) Mg + Cl₂↑','category':'电解','note':'💯 电解熔融MgCl₂'},
])

# 课本：铝冶炼
add('ch8_ch4_develop', [
    {'id':'ch8_dev2','name':'电解Al₂O₃(铝冶炼)','equation':'2Al₂O₃(熔融) =(电解/冰晶石) 4Al + 3O₂↑','category':'电解','note':'💯 冰晶石Na₃AlF₆作助熔剂'},
])

# ===== 选修一·补充更多 =====
# 原电池构造
add_know('ch9_electrochem', [
    {'q':'原电池的构成条件','a':'①两种活动性不同电极；②电解质溶液；③闭合回路'},
    {'q':'原电池正负极的判断','a':'负极→活泼金属→失电子→溶解；正极→不活泼→得电子→有气泡'},
    {'q':'盐桥的作用','a':'平衡两池电荷，形成闭合回路'},
])

# ===== 选修一·沉淀溶解平衡补充 =====
add_know('ch9_ksp', [
    {'q':'Ksp与温度的关系','a':'Ksp只与温度有关，温度升高Ksp一般增大'},
    {'q':'沉淀转化的规律','a':'溶解度大的沉淀向溶解度小的沉淀转化'},
])

# ===== 选修三·全文补全 =====
# 资料卡片：萃取
add_know('ch11_halide_sub', [
    {'q':'卤代烃的密度与什么有关？','a':'除CH₃Cl气体外，密度>水(比水重)'},
])

# 资料卡片：醇的物理性质
add_know('ch11_alcohol_detail', [
    {'q':'甲醇为什么不能喝？','a':'甲醇有毒，误饮致盲甚至死亡'},
    {'q':'乙醇的沸点为什么比等量烷烃高？','a':'乙醇分子间存在氢键'},
])

# 资料卡片：苯酚
add('ch11_phenol', [
    {'id':'ch11_ph5','name':'苯酚+NaOH(中和)','equation':'C₆H₅OH + NaOH = C₆H₅ONa + H₂O','category':'中和','note':'💯 苯酚弱酸性，与NaOH中和'},
])

# 资料卡片：氨基酸等电点
add_know('ch11_amino_acid', [
    {'q':'氨基酸的共性','a':'①两性(-NH₂与H⁺、-COOH与OH⁻)；②脱水缩合→肽键'},
])

# 资料卡片：核酸
add_know('ch11_nucleic_acid', [
    {'q':'DNA和RNA的碱基分别有哪些？','a':'DNA: A/T/C/G；RNA: A/U/C/G'},
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
