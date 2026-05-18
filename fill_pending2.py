import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open('src/data/textbook-data.json','r',encoding='utf-8'))

for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            did_something = False
            
            # 清除note里的待补充标记（只要有内容就不标）
            if sub.get('note') in ('待补充','待补'):
                sub['note'] = ''
                did_something = True
            
            sub_id = sub['id']
            
            # 补充缺失的知识点
            if sub_id == 'ch4_intermolecular':
                sub['knowledge'] = [
                    {'q': '范德华力的影响因素','a':'分子量越大→范德华力越大→熔沸点越高'},
                    {'q': '氢键形成的条件','a':'与电负性大的F/O/N相连的H原子'},
                    {'q': '冰的密度为什么比水小？','a':'水结冰时氢键使分子间形成较大空隙'},
                ]
            elif sub_id == 'ch6_equilibrium':
                sub['knowledge'] = [
                    {'q': '化学平衡的特征（5个字）','a':'逆等动定变'},
                    {'q': '勒夏特列原理的内容','a':'改变影响平衡的一个因素，平衡向减弱该改变的方向移动'},
                    {'q': '催化剂对化学平衡的影响','a':'同等改变正逆反应速率，不改变平衡位置和转化率'},
                ]
            elif sub_id == 'ch8_oil':
                sub['knowledge'] = [
                    {'q': '石油的分馏是什么变化？','a':'物理变化（利用沸点不同分离）'},
                    {'q': '石油的裂化和裂解的区别','a':'裂化→提高轻质油产量；裂解→制乙烯等短链烯烃'},
                    {'q': '煤的干馏是什么变化？','a':'化学变化（隔绝空气加强热）'},
                ]
            elif sub_id == 'ch8_greenchem':
                sub['knowledge'] = [
                    {'q': '原子经济性的含义','a':'无副产物，所有反应物转化为目标产物'},
                    {'q': '原子利用率的计算公式','a':'目标产物原子量÷所有产物原子量之和×100%'},
                    {'q': '哪类反应的原子利用率最高？','a':'加成反应（无副产物）'},
                ]
            elif sub_id == 'ch8_env':
                sub['knowledge'] = [
                    {'q': '酸雨的pH范围？主要成因？','a':'pH<5.6，SO₂和NOₓ的排放'},
                    {'q': '温室效应的主要气体','a':'CO₂、CH₄、N₂O'},
                    {'q': '臭氧层破坏的主要原因','a':'氟氯烃(氟利昂CFCl₃)的排放'},
                    {'q': '水体富营养化的原因','a':'含N/P的洗涤剂和化肥排入水体'},
                ]
            elif sub_id == 'ch9_rate_s':
                sub['knowledge'] = [
                    {'q': 'v=Δc/Δt中各字母含义','a':'v—反应速率；Δc—浓度变化；Δt—时间间隔'},
                    {'q': '速率之比等于什么？','a':'化学计量数之比'},
                    {'q': '温度升高10℃，反应速率一般增加____倍','a':'2~4倍'},
                    {'q': '影响反应速率的因素','a':'内因(物质本身性质)；外因(浓度/温度/压强/催化剂/表面积)'},
                ]
            elif sub_id == 'ch9_eq_s':
                sub['knowledge'] = [
                    {'q': 'K只与____有关','a':'温度'},
                    {'q': 'Qc与K的关系判断平衡移动方向','a':'Qc<K→正移；Qc=K→平衡；Qc>K→逆移'},
                    {'q': 'ΔH<0(放热)，升温时K怎么变？','a':'K减小（平衡逆移）'},
                ]
            elif sub_id == 'ch10_ao':
                sub['knowledge'] = [
                    {'q': '能层K/L/M/N最多电子数','a':'2/8/18/32'},
                    {'q': '核外电子排布遵守的三个原则','a':'能量最低原理、泡利不相容原理、洪特规则'},
                    {'q': 'd轨道最多容纳多少个电子？','a':'10个（5个轨道，各2个电子）'},
                ]
            elif sub_id == 'ch10_econfig':
                sub['knowledge'] = [
                    {'q': '写出Fe的电子排布式','a':'[Ar]3d⁶4s²'},
                    {'q': 'Cr的电子排布（洪特规则特例）','a':'[Ar]3d⁵4s¹（半满更稳定）'},
                    {'q': 'Cu的电子排布（洪特规则特例）','a':'[Ar]3d¹⁰4s¹（全满更稳定）'},
                ]
            elif sub_id == 'ch10_polar':
                sub['knowledge'] = [
                    {'q': '极性分子的判断依据','a':'正负电荷中心是否重合；不重合→极性分子'},
                    {'q': '非极性分子的例子','a':'CH₄、CO₂、BF₃、CCl₄、N₂、O₂'},
                    {'q': '手性碳的条件','a':'连有四个不同基团的碳原子'},
                ]
            elif sub_id == 'ch10_crytype':
                sub['knowledge'] = [
                    {'q': '四种晶体类型及熔沸点比较','a':'共价晶体>离子晶体>金属晶体>分子晶体'},
                    {'q': '石墨属于什么晶体？','a':'混合型晶体（层内共价键，层间范德华力，可导电）'},
                ]
            elif sub_id == 'ch10_crycalc':
                sub['knowledge'] = [
                    {'q': '均摊法中顶点/棱心/面心/体心的占位','a':'顶点1/8、棱心1/4、面心1/2、体心1'},
                    {'q': 'NaCl晶胞中Na⁺和Cl⁻各几个？','a':'各4个（共8个离子）'},
                    {'q': 'CsCl晶胞中Cs⁺和Cl⁻各几个？','a':'各1个'},
                    {'q': 'NaCl的配位数','a':'6（Na⁺周围6个Cl⁻）'},
                ]
            elif sub_id == 'ch11_class':
                sub['knowledge'] = [
                    {'q': '写出常见官能团：卤代烃/醇/酚/醛/羧酸/酯','a':'-X/-OH/-OH(连苯环)/-CHO/-COOH/-COO-'},
                    {'q': '醇和酚的-OH有何不同？','a':'醇-OH连烷基；酚-OH直接连苯环'},
                ]
            elif sub_id == 'ch11_nucl':
                sub['knowledge'] = [
                    {'q': 'DNA和RNA碱基差异','a':'DNA: A/T/C/G；RNA: A/U/C/G'},
                    {'q': '核酸的基本组成单位','a':'核苷酸（核苷+磷酸）'},
                    {'q': 'DNA是什么结构？','a':'双螺旋结构'},
                ]
            
            if sub_id in ('ch9_corrosion',) and len(sub.get('knowledge',[])) > 0:
                pass  # 已有

json.dump(d, open('src/data/textbook-data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)

# 统计
total_rxn = 0
total_know = 0
for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            total_rxn += len(sub.get('reactions', []))
            total_know += len(sub.get('knowledge', []))
print(f'最终统计：总反应={total_rxn}，总知识点={total_know}')

# 检查还有没有待补充
pending = 0
for ch in d:
    for sec in ch['sections']:
        for sub in sec['substances']:
            if sub.get('note') in ('待补充','待补'):
                print(f'仍有: {sub["id"]}')
                pending += 1
if pending == 0:
    print('所有"待补充"已清除 ✅')
