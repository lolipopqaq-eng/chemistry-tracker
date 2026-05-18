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
        # 清除待补充标记
        if by_id[sub_id].get('note') in ('待补充','待补'):
            by_id[sub_id]['note'] = ''

def add_know(sub_id, knows):
    if sub_id in by_id:
        existing = by_id[sub_id].get('knowledge', [])
        ex_ids = {k['q'] for k in existing}
        for k in knows:
            if k['q'] not in ex_ids:
                existing.append(k)

# ===================================
# 选修一·反应热/焓变
# ===================================
add('ch9_heat_s', [
    {'id':'ch9_hs1','name':'焓变定义','equation':'ΔH = H(产物) - H(反应物)','category':'热力学','note':'💯 ΔH<0放热，ΔH>0吸热'},
])
add_know('ch9_heat_s', [
    {'q':'ΔH的正负号如何判断？','a':'ΔH<0放热(环境温度升高)；ΔH>0吸热(环境温度降低)'},
    {'q':'热化学方程式必须注明什么？','a':'各物质状态(s/l/g/aq)和ΔH值'},
    {'q':'可逆反应的ΔH如何计算？','a':'按完全反应计算（反应的焓变与可逆性无关）'},
])

# ===================================
# 选修一·反应速率
# ===================================
add_know('ch9_rate_s', [
    {'q':'v=Δc/Δt中各符号含义','a':'v—反应速率；Δc—浓度变化；Δt—时间间隔'},
    {'q':'速率之比等于什么？','a':'化学计量数之比（不同物质表示同一反应速率）'},
    {'q':'温度升高10℃，反应速率一般增加多少？','a':'约2~4倍'},
    {'q':'影响反应速率的内因是什么？','a':'反应物本身的性质（化学键强弱）'},
])

# ===================================
# 选修一·化学平衡
# ===================================
add_know('ch9_eq_s', [
    {'q':'勒夏特列原理的内容','a':'改变影响平衡的一个因素，平衡向减弱这种改变的方向移动'},
    {'q':'催化剂对平衡有什么影响？','a':'同等程度改变正逆反应速率，不改变平衡位置和转化率'},
    {'q':'温度对K的影响「K只与____有关」','a':'温度'},
])

# ===================================
# 选修一·弱电解质的电离
# ===================================
add('ch9_ion_s', [
    {'id':'ch9_ion1','name':'CH₃COOH电离平衡','equation':'CH₃COOH ⇌ CH₃COO⁻ + H⁺','category':'电离','note':'💯 Ka越小酸性越弱'},
    {'id':'ch9_ion2','name':'NH₃·H₂O电离平衡','equation':'NH₃·H₂O ⇌ NH₄⁺ + OH⁻','category':'电离','note':'💯 Kb越小碱性越弱'},
])

# ===================================
# 选修一·水的电离/Kw/pH
# ===================================
add('ch9_kwp', [
    {'id':'ch9_kw1','name':'水的电离','equation':'H₂O ⇌ H⁺ + OH⁻','category':'电离','note':'💯 Kw=1.0×10⁻¹⁴(25℃)'},
])
add_know('ch9_kwp', [
    {'q':'pH=-lg[H⁺]，pH=7时[H⁺]=?','a':'1.0×10⁻⁷ mol/L'},
    {'q':'pH试纸使用注意事项','a':'①不能湿润；②用玻璃棒蘸取；③与标准比色卡对比'},
])

# ===================================
# 选修一·盐类的水解
# ===================================
add('ch9_hydrolysis', [
    {'id':'ch9_hy6','name':'NH₄⁺水解','equation':'NH₄⁺ + H₂O ⇌ NH₃·H₂O + H⁺','category':'水解','note':'💯 强酸弱碱盐→酸性'},
    {'id':'ch9_hy7','name':'Al³⁺水解','equation':'Al³⁺ + 3H₂O ⇌ Al(OH)₃ + 3H⁺','category':'水解','note':''},
])
add_know('ch9_hydrolysis', [
    {'q':'盐类水解的规律是什么？','a':'谁弱谁水解，都弱都水解，越弱越水解，谁强显谁性'},
])

# ===================================
# 选修一·原电池
# ===================================
add('ch9_primary', [
    {'id':'ch9_p1','name':'锌锰干电池(负极)','equation':'Zn - 2e⁻ = Zn²⁺','category':'电极反应','note':'💯 普通干电池'},
    {'id':'ch9_p2','name':'锌锰干电池(正极)','equation':'2MnO₂ + 2NH₄⁺ + 2e⁻ = Mn₂O₃ + 2NH₃ + H₂O','category':'电极反应','note':''},
    {'id':'ch9_p3','name':'铅蓄电池(放电负极)','equation':'Pb + SO₄²⁻ - 2e⁻ = PbSO₄','category':'电极反应','note':'💯 可充电'},
    {'id':'ch9_p4','name':'铅蓄电池(放电正极)','equation':'PbO₂ + 4H⁺ + SO₄²⁻ + 2e⁻ = PbSO₄ + 2H₂O','category':'电极反应','note':''},
])

# ===================================
# 选修一·电解池
# ===================================
add('ch9_electrol', [
    {'id':'ch9_el1','name':'电解CuCl₂(总)','equation':'CuCl₂ =(电解) Cu + Cl₂↑','category':'电解','note':'💯 阳极Cl₂，阴极Cu'},
    {'id':'ch9_el2','name':'电镀铜(一般)','equation':'Cu²⁺ + 2e⁻ = Cu','category':'电镀','note':'💯 镀件接阴极'},
])

# ===================================
# 选修一·金属腐蚀
# ===================================
add_know('ch9_corrosion', [
    {'q':'吸氧腐蚀和析氢腐蚀哪个为主？','a':'吸氧腐蚀为主（Fe-C-H₂O，中性或弱酸性）'},
    {'q':'牺牲阳极法保护的金属作什么极？','a':'阴极（被保护金属作正极，活泼金属作负极）'},
])

# ===================================
# 选修二·原子结构
# ===================================
add_know('ch10_ao', [
    {'q':'K层最多____个电子；L层____个；N层____个','a':'2、8、32'},
    {'q':'构造原理填充顺序（1s以后的顺序）','a':'1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s'},
    {'q':'洪特规则的内容','a':'简并轨道上的电子优先单独占据不同轨道且自旋平行'},
])

# ===================================
# 选修二·电子排布
# ===================================
add_know('ch10_econfig', [
    {'q':'Cr的电子排布式是____（洪特规则特例）','a':'[Ar]3d⁵4s¹（半满稳定）'},
    {'q':'Cu的电子排布式是____（洪特规则特例）','a':'[Ar]3d¹⁰4s¹（全满稳定）'},
])

# ===================================
# 选修二·杂化轨道
# ===================================
add('ch10_hybrid', [
    {'id':'ch10_h1','name':'sp杂化(BeCl₂)','equation':'Be + Cl₂ = BeCl₂','category':'杂化','note':'💯 sp→直线180°'},
    {'id':'ch10_h2','name':'sp²杂化(BF₃)','equation':'B + 3/2F₂ = BF₃','category':'杂化','note':'💯 sp²→平面三角形120°'},
    {'id':'ch10_h3','name':'sp³杂化(CH₄)','equation':'C + 2H₂ = CH₄','category':'杂化','note':'💯 sp³→正四面体109°28′'},
])
add_know('ch10_hybrid', [
    {'q':'杂化类型的判断方法','a':'价层电子对数=σ键数+孤对电子数；2→sp；3→sp²；4→sp³'},
    {'q':'NH₃的空间构型和杂化','a':'sp³杂化，三角锥形（一对孤对电子）'},
    {'q':'H₂O的空间构型和杂化','a':'sp³杂化，V形（两对孤对电子）'},
])

# ===================================
# 选修二·分子极性
# ===================================
add_know('ch10_polar', [
    {'q':'非极性分子的判断','a':'正负电荷中心重合。CH₄、CO₂、BF₃、CCl₄'},
    {'q':'极性分子的例子','a':'HCl、H₂O、NH₃、CHCl₃'},
    {'q':'手性碳的条件','a':'连有四个不同基团的碳原子'},
])

# ===================================
# 选修二·晶体
# ===================================
add_know('ch10_crytype', [
    {'q':'四种晶体类型的熔沸点比较','a':'共价晶体>离子晶体>金属晶体>分子晶体'},
    {'q':'石墨属于什么晶体？','a':'混合型晶体（层内共价键，层间范德华力，有自由电子）'},
])

# ===================================
# 选修二·晶胞
# ===================================
add_know('ch10_crycalc', [
    {'q':'均摊法中顶点、棱心、面心、体心的占位','a':'顶点1/8、棱心1/4、面心1/2、体心1'},
    {'q':'NaCl晶胞中Na⁺的配位数是____','a':'6'},
    {'q':'CsCl晶胞中Cs⁺的配位数是____','a':'8'},
])

# ===================================
# 选修三·全面补全
# ===================================

# 官能团分类
add_know('ch11_class', [
    {'q':'卤代烃的官能团','a':'-X(-F/-Cl/-Br/-I)'},
    {'q':'醇和酚的官能团都是-OH，区别是什么？','a':'醇：-OH连在烷基上；酚：-OH直接连在苯环上'},
    {'q':'醛基、羧基、酯基的写法','a':'醛基-CHO、羧基-COOH、酯基-COO-'},
])

# 烷烃
add('ch11_alkane', [
    {'id':'ch11_alk1','name':'甲烷燃烧','equation':'CH₄ + 2O₂ =(点燃) CO₂ + 2H₂O','category':'燃烧','phenomenon':'蓝色火焰','note':'💯 烷烃完全燃烧'},
    {'id':'ch11_alk2','name':'高温裂解制烯烃','equation':'C₄H₁₀ =(高温) C₂H₆ + C₂H₄','category':'裂解','note':'💯 长链→短链烯烃'},
    {'id':'ch11_alk3','name':'丙烷燃烧','equation':'C₃H₈ + 5O₂ =(点燃) 3CO₂ + 4H₂O','category':'燃烧','note':''},
])
add_know('ch11_alkane', [
    {'q':'烷烃的通式','a':'CₙH₂ₙ₊₂(n≥1)'},
])

# 烯烃
add('ch11_alkene', [
    {'id':'ch11_ene1','name':'丙烯+HBr','equation':'CH₃CH=CH₂ + HBr → CH₃CHBrCH₃','category':'加成','note':'💯 马氏规则(H加在含H多的C上)'},
    {'id':'ch11_ene2','name':'丙烯+H₂O','equation':'CH₃CH=CH₂ + H₂O →(H⁺/△) CH₃CHOHCH₃','category':'加成','note':'💯 2-丙醇'},
    {'id':'ch11_ene3','name':'丙烯+H₂','equation':'CH₃CH=CH₂ + H₂ →(Ni/△) CH₃CH₂CH₃','category':'加成','note':'💯 丙烷'},
])
add_know('ch11_alkene', [
    {'q':'烯烃的通式','a':'CₙH₂ₙ(n≥2)'},
    {'q':'顺反异构的条件','a':'双键碳上各连两个不同的基团'},
])

# 炔烃
add('ch11_alkyne', [
    {'id':'ch11_yne1','name':'乙炔+H₂(部分→乙烯)','equation':'C₂H₂ + H₂ →(Pd/△) C₂H₄','category':'加成','note':'💯 Pd催化剂可控'},
])
add_know('ch11_alkyne', [
    {'q':'炔烃的通式','a':'CₙH₂ₙ₋₂(n≥2)'},
])

# 芳香烃
add('ch11_aromatic', [
    {'id':'ch11_ar5','name':'苯+Cl₂(取代)','equation':'C₆H₆ + Cl₂ →(FeCl₃) C₆H₅Cl + HCl','category':'取代','note':'💯 氯苯，催化剂FeCl₃'},
    {'id':'ch11_ar6','name':'甲苯+3H₂','equation':'C₆H₅CH₃ + 3H₂ →(Ni/△) C₆H₁₁CH₃','category':'加成','note':'💯 甲基环己烷'},
])
add_know('ch11_aromatic', [
    {'q':'苯不能使____和____褪色','a':'溴水、酸性KMnO₄'},
    {'q':'甲苯能使____褪色，为什么？','a':'酸性KMnO₄，苯环活化使甲基被氧化为-COOH'},
])

# 卤代烃（已补充过溴乙烷，再加具体物质）
add('ch11_halo', [
    {'id':'ch11_hal8','name':'1,2-二溴乙烷+NaOH(水解→乙二醇)','equation':'CH₂BrCH₂Br + 2NaOH →(H₂O/△) CH₂OHCH₂OH + 2NaBr','category':'水解','note':'💯 卤代烃→二元醇'},
    {'id':'ch11_hal9','name':'CH₃Cl+NaOH','equation':'CH₃Cl + NaOH →(H₂O/△) CH₃OH + NaCl','category':'水解','note':''},
])

# 醇/酚
add('ch11_alc', [
    {'id':'ch11_alc1','name':'甲醇燃烧','equation':'2CH₃OH + 3O₂ =(点燃) 2CO₂ + 4H₂O','category':'燃烧','note':''},
    {'id':'ch11_alc2','name':'丙三醇(甘油)+Na','equation':'2C₃H₅(OH)₃ + 6Na = 2C₃H₅(ONa)₃ + 3H₂↑','category':'置换','note':''},
    {'id':'ch11_alc3','name':'丙三醇+HNO₃(硝化甘油)','equation':'C₃H₅(OH)₃ + 3HNO₃ →(浓H₂SO₄) C₃H₅(ONO₂)₃ + 3H₂O','category':'酯化','note':'💯 烈性炸药'},
])

# 醛/酮（彻底补全）
add('ch11_ald', [
    {'id':'ch11_ald6','name':'甲醛+O₂','equation':'HCHO + O₂ = CO₂ + H₂O','category':'氧化','note':'💯 甲醛有强还原性'},
    {'id':'ch11_ald7','name':'乙醛+H₂','equation':'CH₃CHO + H₂ →(Ni/△) CH₃CH₂OH','category':'还原','note':'💯 醛+H₂→醇'},
    {'id':'ch11_ald8','name':'乙醛+O₂','equation':'2CH₃CHO + O₂ →(催化剂) 2CH₃COOH','category':'氧化','note':'💯 乙醛→乙酸'},
    {'id':'ch11_ald9','name':'丙酮+H₂','equation':'CH₃COCH₃ + H₂ →(Ni/△) CH₃CHOHCH₃','category':'还原','note':'💯 酮+H₂→仲醇'},
    {'id':'ch11_ald10','name':'甲醛+银氨溶液','equation':'HCHO + 4Ag(NH₃)₂OH →(△) (NH₄)₂CO₃ + 4Ag↓ + 6NH₃ + 2H₂O','category':'银镜','note':'💯 甲醛有2个醛基当量'},
    {'id':'ch11_ald11','name':'乙醛+Cu(OH)₂(砖红沉淀)','equation':'CH₃CHO + 2Cu(OH)₂ + NaOH →(△) CH₃COONa + Cu₂O↓ + 3H₂O','category':'氧化','phenomenon':'砖红色沉淀','note':''},
])
add_know('ch11_ald', [
    {'q':'醛基的通式怎么写？','a':'-CHO（注意不是-COH）'},
    {'q':'检验醛基的两种方法','a':'①银镜反应（银镜生成）；②新制Cu(OH)₂（砖红色沉淀）'},
])

# 羧酸/酯
add('ch11_ac', [
    {'id':'ch11_ac1','name':'甲酸+Cu(OH)₂','equation':'HCOOH + 2Cu(OH)₂ = CO₂↑ + Cu₂O↓ + 3H₂O','category':'氧化','note':'💯 甲酸有醛基'},
    {'id':'ch11_ac2','name':'乙二酸(草酸)+KMnO₄','equation':'5H₂C₂O₄ + 2KMnO₄ + 3H₂SO₄ = K₂SO₄ + 2MnSO₄ + 10CO₂↑ + 8H₂O','category':'氧化','phenomenon':'紫红色褪去','note':''},
    {'id':'ch11_ac3','name':'酯的水解(酸性)','equation':'RCOOR\' + H₂O ⇌(H⁺/△) RCOOH + R\'OH','category':'水解','note':'💯 可逆反应'},
    {'id':'ch11_ac4','name':'酯的皂化(碱性)','equation':'RCOOR\' + NaOH →(△) RCOONa + R\'OH','category':'皂化','note':'💯 不可逆'},
])
add_know('ch11_ac', [
    {'q':'甲酸为什么能发生银镜反应？','a':'甲酸HCOOH结构中含有醛基(-CHO)'},
    {'q':'酯的两种水解方式区别','a':'酸性水解可逆→酸+醇；碱性水解不可逆→盐+醇(皂化)'},
])

# 糖类
add('ch11_carb', [
    {'id':'ch11_carb1','name':'葡萄糖发酵→乙醇','equation':'C₆H₁₂O₆ →(酒化酶) 2C₂H₅OH + 2CO₂↑','category':'发酵','note':'💯 酿酒原理'},
    {'id':'ch11_carb2','name':'纤维素水解','equation':'(C₆H₁₀O₅)ₙ + nH₂O →(酸/△) nC₆H₁₂O₆(葡萄糖)','category':'水解','note':''},
    {'id':'ch11_carb3','name':'葡萄糖→己六醇(H₂还原)','equation':'C₆H₁₂O₆ + H₂ →(Ni/△) C₆H₁₄O₆','category':'还原','note':''},
])
add_know('ch11_carb', [
    {'q':'如何检验淀粉是否完全水解？','a':'加I₂→不变蓝则完全水解（若无I₂可用碘水）'},
    {'q':'葡萄糖的检验方法','a':'银镜反应或与新制Cu(OH)₂共热→砖红色沉淀'},
])

# 蛋白质（全面补）
add('ch11_prot', [
    {'id':'ch11_pr8','name':'氨基酸两性(与酸)','equation':'H₂NCHRCOOH + HCl = Cl⁻H₃N⁺CHRCOOH','category':'两性','note':''},
    {'id':'ch11_pr9','name':'氨基酸两性(与碱)','equation':'H₂NCHRCOOH + NaOH = H₂NCHRCOONa + H₂O','category':'两性','note':''},
])

# 核酸
add_know('ch11_nucl', [
    {'q':'DNA的碱基组成','a':'腺嘌呤A、胸腺嘧啶T、胞嘧啶C、鸟嘌呤G'},
    {'q':'RNA的碱基组成','a':'A、U(尿嘧啶)、C、G'},
    {'q':'DNA和RNA的主要区别','a':'DNA双螺旋（T），RNA单链（U）'},
])

# 加聚
add('ch11_add', [
    {'id':'ch11_add1','name':'乙烯→聚乙烯','equation':'nCH₂=CH₂ →(催化剂) [CH₂-CH₂]ₙ','category':'加聚','note':'💯 PE，最常见塑料'},
    {'id':'ch11_add2','name':'丙烯→聚丙烯','equation':'nCH₃CH=CH₂ →(催化剂) [CH(CH₃)-CH₂]ₙ','category':'加聚','note':'💯 PP'},
    {'id':'ch11_add3','name':'氯乙烯→PVC','equation':'nCH₂=CHCl →(催化剂) [CH₂-CHCl]ₙ','category':'加聚','note':'💯 聚氯乙烯'},
    {'id':'ch11_add4','name':'1,3-丁二烯→顺丁橡胶','equation':'nCH₂=CH-CH=CH₂ →(催化剂) [CH₂-CH=CH-CH₂]ₙ','category':'加聚','note':''},
])

# 缩聚
add('ch11_cond', [
    {'id':'ch11_cond1','name':'乙二醇+对苯二甲酸→涤纶','equation':'nHOCH₂CH₂OH + nHOOC-C₆H₄-COOH →(催化剂) PET + (2n-1)H₂O','category':'缩聚','note':'💯 涤纶(PET)'},
    {'id':'ch11_cond2','name':'苯酚+甲醛→酚醛树脂','equation':'nC₆H₅OH + nHCHO →(催化剂) 酚醛树脂 + nH₂O','category':'缩聚','note':'💯 电木'},
    {'id':'ch11_cond3','name':'乳酸→聚乳酸(PLA)','equation':'nC₃H₆O₃ →(催化剂) [OCH(CH₃)CO]ₙ + nH₂O','category':'缩聚','note':'💯 可降解塑料'},
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
print('OK - 所有待补充已填完')
