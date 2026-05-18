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

# ===== 蛋白质全面补全 =====
# ch7_protein (必修二)
add('ch7_protein', [
    {'id':'ch7_pr2','name':'蛋白质水解(酸催化)','equation':'蛋白质 + nH₂O →(酸/酶/△) 氨基酸','category':'水解','note':'💯 最终产物：α-氨基酸'},
    {'id':'ch7_pr3','name':'氨基酸两性(-NH₂)','equation':'RCH(NH₂)COOH + H⁺ = RCH(NH₃⁺)COOH','category':'两性','note':'💯 氨基显碱性'},
    {'id':'ch7_pr4','name':'氨基酸两性(-COOH)','equation':'RCH(NH₂)COOH + OH⁻ = RCH(NH₂)COO⁻ + H₂O','category':'两性','note':'💯 羧基显酸性'},
    {'id':'ch7_pr5','name':'氨基酸缩合(二肽)','equation':'2H₂NCH₂COOH →(催化剂) H₂NCH₂CONHCH₂COOH + H₂O','category':'缩合','note':'💯 肽键 -CONH-'},
])

# ch11_protein_detail (选修三)
add('ch11_protein_detail', [
    {'id':'ch11_pr3','name':'蛋白质本质水解','equation':'多肽 + nH₂O →(酸/碱/酶/△) 各种α-氨基酸','category':'水解','note':'💯 多种氨基酸混合物'},
    {'id':'ch11_pr4','name':'氨基酸两性电离','equation':'H₃N⁺CHRCOO⁻ ⇌ H₂NCHRCOOH + H⁺','category':'电离','note':'💯 等电点pH'},
    {'id':'ch11_pr5','name':'盐析(可逆沉淀)','equation':'蛋白质 + 饱和(NH₄)₂SO₄ →(可逆) 蛋白质沉淀','category':'盐析','note':'💯 物理变化，可恢复'},
    {'id':'ch11_pr6','name':'变性(不可逆)','equation':'蛋白质 →(加热/酸/碱/重金属/酒精) 变性蛋白质','category':'变性','note':'💯 化学变化，不可逆'},
    {'id':'ch11_pr7','name':'缩二脲反应','equation':'蛋白质 + CuSO₄(NaOH) = 紫红色络合物','category':'检验','note':'💯 多肽/蛋白质专有反应'},
])

# 新增知识点
add_know('ch7_protein', [
    {'q':'蛋白质的两种性质分别是什么？','a':'盐析(可逆，物理变化)；变性(不可逆，化学变化)'},
    {'q':'哪些因素会导致蛋白质变性？','a':'加热、强酸/强碱、重金属盐、酒精、紫外线'},
    {'q':'检验蛋白质的方法','a':'①黄蛋白反应(浓HNO₃→黄色)；②缩二脲反应(紫色)'},
])
add_know('ch11_protein_detail', [
    {'q':'氨基酸的通式是什么？','a':'H₂N-CHR-COOH (R为侧链基团)'},
    {'q':'多肽中连接氨基酸的键叫什么？','a':'肽键(-CO-NH-)，脱水缩合形成'},
    {'q':'氨基酸的共性有哪些？','a':'①能成盐(两性)；②脱水缩合(形成肽键)'},
])

# ===== 选修二·原子结构知识点补全（分组，做完跳到下一节） =====
# 这个功能是前端交互，需要改KnowledgeCard组件
# 先在知识点上加分组字段
add_know('ch10_atom_sub', [
    {'q':'原子核由什么构成？','a':'质子(Z)和中子(N)；质量数A=Z+N'},
    {'q':'能层符号依次为____','a':'K(1) L(2) M(3) N(4) ...'},
    {'q':'s轨道有____个轨道，最多____个电子','a':'1、2'},
    {'q':'p轨道有____个轨道，最多____个电子','a':'3、6'},
    {'q':'d轨道有____个轨道，最多____个电子','a':'5、10'},
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
