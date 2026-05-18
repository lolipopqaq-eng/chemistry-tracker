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

def add_know(sub_id, knows):
    if sub_id in by_id:
        existing = by_id[sub_id].get('knowledge', [])
        ex_ids = {k['q'] for k in existing}
        for k in knows:
            if k['q'] not in ex_ids:
                existing.append(k)

# ===== 必修一·第四章 无反应，只有知识点 =====
# 加两个电化学相关的反应
add_rxns('ch4_ionic', [
    {'id':'ch4_m1','name':'NaCl的形成（电子转移）','equation':'Na⁺ + :Cl:⁻ = NaCl','category':'离子键','note':'Na失1e⁻，Cl得1e⁻'},
])
add_rxns('ch4_covalent', [
    {'id':'ch4_m2','name':'H₂的形成','equation':'H· + ·H = H:H','category':'共价键','note':'共用电子对'},
])
# 第四章已经26个知识点，再补几个
add_know('ch4_atom', [
    {'q':'某元素原子最外层有5个电子，它属于____族','a':'VA'},
])
add_know('ch4_periodic', [
    {'q':'同一周期从左到右，原子半径逐渐____，金属性逐渐____','a':'减小、减弱'},
    {'q':'同一主族从上到下，原子半径逐渐____，金属性逐渐____','a':'增大、增强'},
    {'q':'元素金属性越强，其最高价氧化物对应水化物的____性越强','a':'碱'},
    {'q':'元素非金属性越强，其最高价氧化物对应水化物的____性越强','a':'酸'},
])

# ===== 必修二·第五章 硫氮 =====
add_rxns('ch5_si', [
    {'id':'ch5_si4','name':'SiO₂ + CaO','equation':'SiO₂ + CaO =(高温) CaSiO₃','category':'与碱性氧化物','note':'玻璃工业'},
])
add_know('ch5_si', [
    {'q':'芯片的主要成分是____；光导纤维的主要成分是____','a':'Si、SiO₂'},
])

# ===== 选修一 补更多 =====
add_rxns('ch9_electrochem', [
    {'id':'ch9_e8','name':'电镀铜（阴极）','equation':'Cu²⁺ + 2e⁻ = Cu','category':'电镀','note':'镀件接阴极'},
    {'id':'ch9_e9','name':'电镀铜（阳极）','equation':'Cu - 2e⁻ = Cu²⁺','category':'电镀','note':'镀层金属接阳极'},
])

# ===== 选修二 加配位相关反应 =====
add_rxns('ch10_mol_sub', [
    {'id':'ch10_m1','name':'[Cu(NH₃)₄]²⁺形成','equation':'Cu²⁺ + 4NH₃ = [Cu(NH₃)₄]²⁺','category':'配位','note':'💯 深蓝色溶液'},
    {'id':'ch10_m2','name':'[Ag(NH₃)₂]⁺形成','equation':'Ag⁺ + 2NH₃ = [Ag(NH₃)₂]⁺','category':'配位','note':'💯 银氨溶液的形成'},
    {'id':'ch10_m3','name':'NH₄⁺形成（配位键）','equation':'NH₃ + H⁺ = NH₄⁺','category':'配位','note':'N提供孤对电子，H⁺提供空轨道'},
    {'id':'ch10_m4','name':'H₃O⁺形成（配位键）','equation':'H₂O + H⁺ = H₃O⁺','category':'配位','note':'O提供孤对电子'},
])

# ===== 选修三 补更多 =====
add_rxns('ch11_alkyl', [
    {'id':'ch11_alkyl5','name':'乙炔制氯乙烯','equation':'CH≡CH + HCl →(HgCl₂/△) CH₂=CHCl','category':'加成','note':'制PVC单体'},
])

add_rxns('ch11_aromatic_sub', [
    {'id':'ch11_ar4','name':'苯+Br₂(取代)','equation':'C₆H₆ + Br₂ →(FeBr₃) C₆H₅Br + HBr','category':'取代','note':'溴苯无色油状'},
])

add_know('ch11_alkane_sub', [
    {'q':'烷烃通式____(n≥1)','a':'CₙH₂ₙ₊₂'},
])
add_know('ch11_alkene_sub', [
    {'q':'烯烃通式____(n≥2)','a':'CₙH₂ₙ'},
    {'q':'检验烯烃的方法：____','a':'使溴水褪色或使KMnO₄/H⁺褪色'},
])
add_know('ch11_alkyne_sub', [
    {'q':'炔烃通式____(n≥2)','a':'CₙH₂ₙ₋₂'},
])
add_know('ch11_aromatic_sub', [
    {'q':'苯不能使____褪色，也不能使____褪色','a':'溴水、酸性KMnO₄'},
    {'q':'甲苯能使____褪色，因为____基被氧化','a':'酸性KMnO₄、甲基'},
])

# ===== 统计 =====
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
