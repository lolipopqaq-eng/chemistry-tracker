// 教材结构定义：人教版化学必修第一册
// 结构：章 → 节 → 物质 → 化合物的反应

const TEXTBOOK = {
  name: '人教版化学必修第一册',
  chapters: [
    {
      id: 'ch1',
      name: '第一章 物质及其变化',
      sections: [
        {
          id: 'ch1_ion',
          name: '离子反应',
          substances: [
            {
              id: 'ch1_electrolyte',
              name: '强电解质/弱电解质',
              icon: '⚡',
              note: '强酸/强碱/大部分盐→强电解质；弱酸/弱碱→弱电解质',
              reactions: [
                { id: 'ch1_e1', name: 'CH₃COOH 电离', equation: 'CH₃COOH ⇌ CH₃COO⁻ + H⁺', category: '电离', note: '弱酸部分电离' },
                { id: 'ch1_e2', name: 'NH₃·H₂O 电离', equation: 'NH₃·H₂O ⇌ NH₄⁺ + OH⁻', category: '电离', note: '弱碱部分电离' },
                { id: 'ch1_e3', name: 'H₂O 电离', equation: 'H₂O ⇌ H⁺ + OH⁻', category: '电离', note: '水的电离，极微弱' },
              ],
            },
          ],
        },
        {
          id: 'ch1_redox',
          name: '氧化还原反应',
          substances: [
            {
              id: 'ch1_redox_rules',
              name: '氧化还原判断',
              icon: '⚡',
              note: '有化合价变化→氧化还原反应；置换全是，复分解全不是',
              reactions: [
                { id: 'ch1_r1', name: 'Fe + CuSO₄', equation: 'Fe + CuSO₄ → FeSO₄ + Cu', category: '氧化还原', note: '置换反应，全是氧化还原' },
                { id: 'ch1_r2', name: 'NaCl + AgNO₃', equation: 'NaCl + AgNO₃ → AgCl↓ + NaNO₃', category: '非氧化还原', note: '复分解反应，全不是氧化还原' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 'ch2',
      name: '第二章 海水中的重要元素——钠和氯',
      sections: [
        {
          id: 'ch2_na',
          name: '钠及其化合物',
          substances: [
            {
              id: 'ch2_na_metal',
              name: 'Na 钠单质',
              icon: '🥈',
              note: '银白色、质软、密度0.97g/cm³、熔点低、保存在煤油中',
              reactions: [
                { id: 'ch2_na1', name: 'Na + O₂（常温）', equation: '4Na + O₂ → 2Na₂O', category: '钠单质',
    phenomenon: '银白色金属钠表面变暗（生成白色Na2O）', note: '常温生成氧化钠（白色）' },
                { id: 'ch2_na2', name: 'Na + O₂（点燃）', equation: '2Na + O₂ →(点燃) Na₂O₂（淡黄色）', category: '钠单质',
    phenomenon: '钠浮在水面→熔成小球→四处游动→发出嘶嘶声→溶液变红（浮熔游响红）', note: '点燃生成过氧化钠（淡黄色）' },
                { id: 'ch2_na3', name: 'Na + H₂O', equation: '2Na + 2H₂O → 2NaOH + H₂↑', category: '钠单质',
    phenomenon: '钠在氯气中剧烈燃烧，产生白烟（NaCl固体）', note: '浮熔游响红，生成NaOH和H₂' },
                { id: 'ch2_na4', name: 'Na + Cl₂', equation: '2Na + Cl₂ →(点燃) 2NaCl', category: '钠单质', note: '剧烈燃烧，白烟' },
              ],
            },
            {
              id: 'ch2_na2o',
              name: 'Na₂O 氧化钠',
              icon: '⬜',
              note: '白色固体',
              reactions: [
                { id: 'ch2_o1', name: 'Na₂O + H₂O', equation: 'Na₂O + H₂O → 2NaOH', category: '氧化钠', note: '碱性氧化物与水反应' },
                { id: 'ch2_o2', name: 'Na₂O + CO₂', equation: 'Na₂O + CO₂ → Na₂CO₃', category: '氧化钠', note: '碱性氧化物与酸性氧化物反应' },
                { id: 'ch2_o3', name: 'Na₂O + HCl', equation: 'Na₂O + 2HCl → 2NaCl + H₂O', category: '氧化钠', note: '碱性氧化物与酸反应' },
              ],
            },
            {
              id: 'ch2_na2o2',
              name: 'Na₂O₂ 过氧化钠',
              icon: '🟡',
              note: '淡黄色固体，供氧剂',
              reactions: [
                { id: 'ch2_p1', name: 'Na₂O₂ + H₂O', equation: '2Na₂O₂ + 2H₂O → 4NaOH + O₂↑', category: '过氧化钠', note: '与水反应产氧' },
                { id: 'ch2_p2', name: 'Na₂O₂ + CO₂', equation: '2Na₂O₂ + 2CO₂ → 2Na₂CO₃ + O₂', category: '过氧化钠', note: '供氧剂原理，与CO₂反应产氧，高考必考' },
                { id: 'ch2_p3', name: 'Na₂O₂ + HCl', equation: '2Na₂O₂ + 4HCl → 4NaCl + 2H₂O + O₂↑', category: '过氧化钠', note: '与酸反应产氧' },
              ],
            },
            {
              id: 'ch2_naoh',
              name: 'NaOH 氢氧化钠（烧碱/火碱/苛性钠）',
              icon: '🧪',
              note: '白色固体、强碱、吸水潮解、腐蚀性',
              reactions: [
                { id: 'r01', name: '铝与氢氧化钠', equation: '2Al + 2NaOH + 2H₂O → 2NaAlO₂ + 3H₂↑', category: '单质反应',
    phenomenon: '铝逐渐溶解，产生无色气泡', note: '重点反应，Al的两性体现' },
                { id: 'r02', name: '硅与氢氧化钠', equation: 'Si + 2NaOH + H₂O → Na₂SiO₃ + 2H₂↑', category: '单质反应', note: 'Si的歧化反应' },
                { id: 'r03', name: '氯气与氢氧化钠（常温）', equation: 'Cl₂ + 2NaOH → NaCl + NaClO + H₂O', category: '单质反应', note: '歧化反应，常温产物为次氯酸盐' },
                { id: 'r04', name: '氯气与氢氧化钠（加热）', equation: '3Cl₂ + 6NaOH → 5NaCl + NaClO₃ + 3H₂O', category: '单质反应', note: '加热歧化，生成氯酸盐' },
                { id: 'r05', name: '硫与氢氧化钠', equation: '3S + 6NaOH → 2Na₂S + Na₂SO₃ + 3H₂O', category: '单质反应', note: '硫的歧化反应' },
                { id: 'r06', name: 'CO₂过量→碳酸氢钠', equation: 'NaOH + CO₂ → NaHCO₃', category: '酸性氧化物', note: 'CO₂过量，生成酸式盐' },
                { id: 'r07', name: 'NaOH过量→碳酸钠', equation: '2NaOH + CO₂ → Na₂CO₃ + H₂O', category: '酸性氧化物', note: 'NaOH过量，生成正盐' },
                { id: 'r08', name: 'SO₂与氢氧化钠', equation: '2NaOH + SO₂ → Na₂SO₃ + H₂O', category: '酸性氧化物', note: 'SO₂过量生成NaHSO₃' },
                { id: 'r09', name: 'SiO₂与氢氧化钠', equation: '2NaOH + SiO₂ → Na₂SiO₃ + H₂O', category: '酸性氧化物', note: '玻璃不能用磨口玻璃塞' },
                { id: 'r10', name: '普通强酸中和', equation: 'NaOH + HCl → NaCl + H₂O', category: '酸碱中和', note: '强酸强碱中和' },
                { id: 'r11', name: '弱酸中和', equation: 'NaOH + CH₃COOH → CH₃COONa + H₂O', category: '酸碱中和', note: '弱酸也反应' },
                { id: 'r12', name: '多元酸（H₂S）', equation: '2NaOH + H₂S → Na₂S + 2H₂O', category: '酸碱中和', note: '多元酸可分步反应' },
                { id: 'r13', name: '氧化铝与氢氧化钠', equation: 'Al₂O₃ + 2NaOH → 2NaAlO₂ + H₂O', category: '两性',
    phenomenon: '加热产生刺激性气体，湿润红色石蕊试纸变蓝', note: 'Al₂O₃的两性' },
                { id: 'r14', name: '氢氧化铝与氢氧化钠', equation: 'Al(OH)₃ + NaOH → NaAlO₂ + 2H₂O', category: '两性',
    phenomenon: '产生蓝色絮状沉淀', note: 'Al(OH)₃的两性，高考必考' },
                { id: 'r15', name: '铵盐制氨气', equation: 'NH₄Cl + NaOH → NaCl + NH₃↑ + H₂O', category: '复分解',
    phenomenon: '产生红褐色沉淀', note: '实验室制氨气' },
                { id: 'r16', name: '硫酸铜沉淀', equation: 'CuSO₄ + 2NaOH → Cu(OH)₂↓ + Na₂SO₄', category: '复分解', note: '蓝色沉淀' },
                { id: 'r17', name: '氯化铁沉淀', equation: 'FeCl₃ + 3NaOH → Fe(OH)₃↓ + 3NaCl', category: '复分解', note: '棕褐色沉淀' },
                { id: 'r18', name: '碳酸氢钠与氢氧化钠', equation: 'NaHCO₃ + NaOH → Na₂CO₃ + H₂O', category: '复分解', note: '酸式盐与碱反应' },
                { id: 'r19', name: '卤代烃水解（取代）', equation: 'CH₃CH₂Br + NaOH → CH₃CH₂OH + NaBr', category: '有机反应',
    phenomenon: '苯酚溶液由浑浊变澄清', note: '水溶液，取代反应' },
                { id: 'r20', name: '卤代烃消去', equation: 'CH₃CH₂Br + NaOH → CH₂=CH₂↑ + NaBr + H₂O', category: '有机反应', note: '醇溶液，消去反应' },
                { id: 'r21', name: '油脂皂化反应', equation: '油脂 + NaOH → 高级脂肪酸钠 + 甘油', category: '有机反应', note: '碱性水解，制肥皂' },
                { id: 'r22', name: '苯酚与氢氧化钠', equation: 'C₆H₅OH + NaOH → C₆H₅ONa + H₂O', category: '有机反应', note: '酚羟基显弱酸性' },
                { id: 'r23', name: '酯的碱性水解', equation: 'RCOOR\' + NaOH → RCOONa + R\'OH', category: '有机反应',
    phenomenon: '开始无气泡，继续滴加后产生气泡', note: '酯在碱性条件下彻底水解' },
              ],
            },
            {
              id: 'ch2_na2co3',
              name: 'Na₂CO₃ 碳酸钠（纯碱/苏打）',
              icon: '🧂',
              note: '白色粉末，易溶于水，热稳定性高',
              reactions: [
                { id: 'n01', name: 'Na₂CO₃ + 盐酸少量', equation: 'Na₂CO₃ + HCl → NaHCO₃ + NaCl（无气泡）', category: '与酸反应',
    phenomenon: '产生白色沉淀（CaCO3）', note: '逐滴加盐酸，先无气泡后出气泡' },
                { id: 'n02', name: 'Na₂CO₃ + 盐酸过量', equation: 'Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂↑（有气泡）', category: '与酸反应', note: '盐酸过量直接出气泡' },
                { id: 'n03', name: 'Na₂CO₃ + Ca(OH)₂', equation: 'Na₂CO₃ + Ca(OH)₂ → CaCO₃↓ + 2NaOH', category: '与碱反应',
    phenomenon: '产生白色沉淀（CaCO3）', note: '工业制烧碱' },
                { id: 'n04', name: 'Na₂CO₃ + Ba(OH)₂', equation: 'Na₂CO₃ + Ba(OH)₂ → BaCO₃↓ + 2NaOH', category: '与碱反应',
    phenomenon: '产生白色沉淀（BaCO3）', note: '生成白色沉淀' },
                { id: 'n05', name: 'Na₂CO₃ + NaOH', equation: 'Na₂CO₃ + NaOH → 不反应', category: '与碱反应', note: '碳酸钠和NaOH不反应' },
                { id: 'n06', name: 'Na₂CO₃ + CaCl₂', equation: 'Na₂CO₃ + CaCl₂ → CaCO₃↓ + 2NaCl', category: '与盐反应', note: '检验CO₃²⁻' },
                { id: 'n07', name: 'Na₂CO₃ + BaCl₂', equation: 'Na₂CO₃ + BaCl₂ → BaCO₃↓ + 2NaCl', category: '与盐反应', note: '白色沉淀，检验CO₃²⁻' },
                { id: 'n08', name: 'Na₂CO₃ + CO₂ + H₂O', equation: 'Na₂CO₃ + H₂O + CO₂ → 2NaHCO₃', category: '与CO₂', note: '制小苏打，饱和析出NaHCO₃晶体' },
                { id: 'n09', name: 'CO₃²⁻水解', equation: 'CO₃²⁻ + H₂O ⇌ HCO₃⁻ + OH⁻', category: '水解', note: '溶液显碱性，俗称纯碱' },
                { id: 'n10', name: 'Na₂CO₃加热', equation: 'Na₂CO₃ 加热不分解', category: '热稳定性', note: '稳定性：Na₂CO₃ > NaHCO₃' },
              ],
            },
            {
              id: 'ch2_nahco3',
              name: 'NaHCO₃ 碳酸氢钠（小苏打）',
              icon: '🥤',
              note: '白色细小晶体，可溶于水',
              reactions: [
                { id: 'h01', name: 'NaHCO₃ + HCl', equation: 'NaHCO₃ + HCl → NaCl + H₂O + CO₂↑', category: '与强酸', note: '直接冒气泡，高考必考' },
                { id: 'h02', name: 'NaHCO₃ + NaOH', equation: 'NaHCO₃ + NaOH → Na₂CO₃ + H₂O', category: '与强碱',
    phenomenon: '加热后试管口有水珠，气体使澄清石灰水变浑浊', note: '酸式盐遇碱变正盐' },
                { id: 'h03', name: 'NaHCO₃少量 + Ca(OH)₂', equation: 'HCO₃⁻ + OH⁻ + Ca²⁺ → CaCO₃↓ + H₂O', category: '与碱反应', note: '少量只生成CaCO₃沉淀' },
                { id: 'h04', name: 'NaHCO₃过量 + Ca(OH)₂', equation: '2HCO₃⁻ + 2OH⁻ + Ca²⁺ → CaCO₃↓ + CO₃²⁻ + 2H₂O', category: '与碱反应', note: '过量时产物有CO₃²⁻' },
                { id: 'h05', name: 'NaHCO₃受热分解', equation: '2NaHCO₃ →(Δ) Na₂CO₃ + H₂O + CO₂↑', category: '受热分解', note: '唯一受热易分解的钠盐' },
                { id: 'h06', name: 'NaHCO₃ + CO₂', equation: 'NaHCO₃ + CO₂ → 不反应', category: '与CO₂', note: '不反应' },
                { id: 'h07', name: 'NaHCO₃ + Na₂CO₃', equation: 'NaHCO₃ + Na₂CO₃ → 不反应', category: '与碳酸钠', note: '不反应' },
                { id: 'h08', name: 'NaHCO₃水解', equation: 'HCO₃⁻ + H₂O ⇌ H₂CO₃ + OH⁻', category: '水解', note: '显弱碱性，碱性：Na₂CO₃ > NaHCO₃' },
                { id: 'h09', name: 'Na₂CO₃→NaHCO₃', equation: 'Na₂CO₃ + CO₂ + H₂O → 2NaHCO₃', category: '相互转化',
    phenomenon: '铜丝在氯气中剧烈燃烧，产生棕黄色烟', note: '通CO₂' },
                { id: 'h10', name: 'NaHCO₃→Na₂CO₃', equation: 'NaHCO₃ + NaOH → Na₂CO₃ + H₂O', category: '相互转化',
    phenomenon: '氢气在氯气中安静燃烧，发出苍白色火焰，瓶口有白雾', note: '加碱' },
              ],
            },
          ],
        },
        {
          id: 'ch2_cl',
          name: '氯及其化合物',
          substances: [
            {
              id: 'ch2_cl2',
              name: 'Cl₂ 氯气',
              icon: '🟢',
              note: '黄绿色、刺激性气味、有毒、密度>空气',
              reactions: [
                { id: 'cl1', name: 'Cl₂ + Cu', equation: 'Cu + Cl₂ →(点燃) CuCl₂', category: '与金属',
    phenomenon: '铁在氯气中剧烈燃烧，产生棕褐色烟', note: '棕黄色烟' },
                { id: 'cl2', name: 'Cl₂ + H₂', equation: 'H₂ + Cl₂ →(点燃) 2HCl', category: '与非金属',
    phenomenon: '溶液从无色变为橙黄色（Br2生成）', note: '苍白色火焰，瓶口白雾' },
                { id: 'cl3', name: 'Cl₂ + H₂O', equation: 'Cl₂ + H₂O ⇌ HCl + HClO', category: '与水',
    phenomenon: '溶液从无色变为棕黄色，加淀粉变蓝（I2生成）', note: '氯水：浅黄绿色' },
                { id: 'cl4', name: 'Cl₂ + NaOH（制84）', equation: 'Cl₂ + 2NaOH → NaCl + NaClO + H₂O', category: '与碱', note: '制84消毒液' },
                { id: 'cl5', name: 'Cl₂ + Ca(OH)₂（制漂白粉）', equation: '2Cl₂ + 2Ca(OH)₂ → CaCl₂ + Ca(ClO)₂ + 2H₂O', category: '与碱',
    phenomenon: '氯水颜色变浅，产生无色气泡', note: '制漂白粉' },
                { id: 'cl6', name: 'Cl₂ + Fe', equation: '2Fe + 3Cl₂ →(点燃) 2FeCl₃', category: '与金属', note: '生成FeCl₃（棕褐色烟）' },
                { id: 'cl7', name: 'Cl₂ + NaBr', equation: 'Cl₂ + 2NaBr → 2NaCl + Br₂', category: '置换反应',
    phenomenon: '两极产生气泡：阴极H2、阳极Cl2', note: 'Cl₂氧化性>Br₂' },
                { id: 'cl8', name: 'Cl₂ + KI', equation: 'Cl₂ + 2KI → 2KCl + I₂', category: '置换反应', note: 'Cl₂氧化性>I₂，淀粉变蓝' },
              ],
            },
            {
              id: 'ch2_hclo',
              name: 'HClO 次氯酸',
              icon: '🧴',
              note: '弱酸性、强氧化性、漂白性（不可逆）',
              reactions: [
                { id: 'hclo1', name: 'HClO 光照分解', equation: '2HClO →(光照) 2HCl + O₂↑', category: '分解',
    phenomenon: '铁丝剧烈燃烧，火星四射，生成黑色固体Fe3O4', note: '氯水需避光保存' },
              ],
            },
            {
              id: 'ch2_nacl',
              name: 'NaCl 氯化钠',
              icon: '🧂',
              note: '白色晶体，易溶于水',
              reactions: [
                { id: 'nacl1', name: '电解饱和食盐水', equation: '2NaCl + 2H₂O →(电解) 2NaOH + H₂↑ + Cl₂↑', category: '电解',
    phenomenon: '铁溶解，产生无色气泡，溶液变浅绿色', note: '氯碱工业' },
              ],
            },
          ],
        },
      ],
    },
    {
      id: 'ch3',
      name: '第三章 铁 金属材料',
      sections: [
        {
          id: 'ch3_fe',
          name: '铁及其化合物',
          substances: [
            {
              id: 'ch3_fe_metal',
              name: 'Fe 铁单质',
              icon: '🔩',
              note: '银白色金属',
              reactions: [
                { id: 'fe1', name: 'Fe + O₂', equation: '3Fe + 2O₂ →(点燃) Fe₃O₄', category: '与氧气',
    phenomenon: '铁在氯气中剧烈燃烧，产生棕褐色烟', note: '火星四射，生成Fe₃O₄' },
                { id: 'fe2', name: 'Fe + 稀酸', equation: 'Fe + 2H⁺ → Fe²⁺ + H₂↑', category: '与酸',
    phenomenon: '红棕色固体Fe2O3溶解，溶液变棕黄色', note: '生成Fe²⁺（浅绿色）' },
                { id: 'fe3', name: 'Fe + 浓H₂SO₄/HNO₃', equation: 'Fe + 浓H₂SO₄/HNO₃ → 常温钝化', category: '与酸', note: '常温形成致密氧化膜' },
                { id: 'fe4', name: 'Fe + CuSO₄', equation: 'Fe + CuSO₄ → FeSO₄ + Cu', category: '置换反应',
    phenomenon: '红棕色粉末逐渐变成银白色', note: '湿法炼铜' },
                { id: 'fe5', name: 'Fe + Cl₂', equation: '2Fe + 3Cl₂ →(点燃) 2FeCl₃', category: '与非金属',
    phenomenon: '剧烈反应，放出大量热，产生耀眼白光，铁水流出', note: '生成Fe³⁺（棕褐色烟）' },
                { id: 'fe6', name: 'Fe + S', equation: 'Fe + S →(△) FeS', category: '与非金属', note: '生成FeS（黑色）' },
              ],
            },
            {
              id: 'ch3_feoxides',
              name: '铁的氧化物',
              icon: '🪨',
              note: 'FeO（黑色）/ Fe₂O₃（红棕色）/ Fe₃O₄（黑色有磁性）',
              reactions: [
                { id: 'feo1', name: 'FeO + HCl', equation: 'FeO + 2HCl → FeCl₂ + H₂O', category: '与酸',
    phenomenon: '生成白色沉淀，迅速变灰绿，最终变红褐', note: 'FeO是碱性氧化物' },
                { id: 'feo2', name: 'Fe₂O₃ + HCl', equation: 'Fe₂O₃ + 6HCl → 2FeCl₃ + 3H₂O', category: '与酸',
    phenomenon: '红褐色固体变成红棕色，试管口有水珠', note: 'Fe₂O₃是碱性氧化物，铁红' },
                { id: 'feo3', name: 'Fe₃O₄ + HCl', equation: 'Fe₃O₄ + 8HCl → FeCl₂ + 2FeCl₃ + 4H₂O', category: '与酸', note: 'Fe₃O₄可写成FeO·Fe₂O₃' },
                { id: 'feo4', name: '高温还原Fe₂O₃', equation: 'Fe₂O₃ + 3CO →(高温) 2Fe + 3CO₂', category: '氧化还原', note: '高炉炼铁原理' },
                { id: 'feo5', name: 'Fe₂O₃ + Al（铝热反应）', equation: 'Fe₂O₃ + 2Al →(高温) 2Fe + Al₂O₃', category: '氧化还原',
    phenomenon: '溶液从浅绿色变为棕黄色', note: '铝热反应，焊接铁轨' },
              ],
            },
            {
              id: 'ch3_feoh',
              name: '铁的氢氧化物',
              icon: '🧪',
              note: 'Fe(OH)₂白色→Fe(OH)₃红褐色',
              reactions: [
                { id: 'feoh1', name: 'Fe²⁺ + OH⁻', equation: 'Fe²⁺ + 2OH⁻ → Fe(OH)₂↓', category: '沉淀',
    phenomenon: '溶液变为血红色', note: '白色沉淀' },
                { id: 'feoh2', name: 'Fe³⁺ + OH⁻', equation: 'Fe³⁺ + 3OH⁻ → Fe(OH)₃↓', category: '沉淀',
    phenomenon: '铜溶解，溶液从棕黄色变为浅绿色', note: '红褐色沉淀' },
                { id: 'feoh3', name: 'Fe(OH)₂ 被氧化', equation: '4Fe(OH)₂ + O₂ + 2H₂O → 4Fe(OH)₃', category: '氧化',
    phenomenon: '溶液变色，加淀粉变蓝（I2）', note: '白→灰绿→红褐，高考必考' },
                { id: 'feoh4', name: 'Fe(OH)₃加热分解', equation: '2Fe(OH)₃ →(△) Fe₂O₃ + 3H₂O', category: '分解', note: '红褐色→红棕色' },
              ],
            },
            {
              id: 'ch3_feions',
              name: 'Fe²⁺ / Fe³⁺ 离子转化',
              icon: '🔄',
              note: 'Fe²⁺浅绿色，Fe³⁺棕黄色',
              reactions: [
                { id: 'feion1', name: 'Fe²⁺ → Fe³⁺（Cl₂氧化）', equation: '2Fe²⁺ + Cl₂ → 2Fe³⁺ + 2Cl⁻', category: '氧化', note: 'Fe²⁺被Cl₂氧化为Fe³⁺' },
                { id: 'feion2', name: 'Fe³⁺ → Fe²⁺（Fe还原）', equation: '2Fe³⁺ + Fe → 3Fe²⁺', category: '还原', note: 'Fe³⁺被Fe还原为Fe²⁺' },
                { id: 'feion3', name: 'Fe³⁺ 检验（KSCN）', equation: 'Fe³⁺ + 3SCN⁻ → Fe(SCN)₃（血红色）', category: '检验', note: 'Fe³⁺检验方法，高考必考' },
                { id: 'feion4', name: 'Fe²⁺ → Fe³⁺（O₂/H⁺）', equation: '4Fe²⁺ + O₂ + 4H⁺ → 4Fe³⁺ + 2H₂O', category: '氧化', note: 'Fe²⁺易被空气中O₂氧化' },
                { id: 'feion5', name: 'Fe³⁺ + Cu', equation: '2Fe³⁺ + Cu → 2Fe²⁺ + Cu²⁺', category: '氧化还原', note: 'FeCl₃溶液蚀刻铜电路板' },
                { id: 'feion6', name: 'Fe³⁺ + I⁻', equation: '2Fe³⁺ + 2I⁻ → 2Fe²⁺ + I₂', category: '氧化还原', note: 'Fe³⁺氧化I⁻' },
              ],
            },
            {
              id: 'ch3_fe_steel',
              name: '合金（钢铁）',
              icon: '🏗️',
              note: '合金硬度>成分金属，熔点<成分金属',
              reactions: [
                { id: 'fealloy1', name: '生铁炼钢', equation: '生铁 →(炼钢) 钢（降C、去S/P/Si）', category: '冶金', note: '生铁含碳量>钢' },
              ],
            },
          ],
        },
      ],
    },
  ],
};

// 展平所有反应，方便存储和查询
function flattenReactions(textbook) {
  const all = [];
  textbook.chapters.forEach(ch => {
    ch.sections.forEach(sec => {
      sec.substances.forEach(sub => {
        sub.reactions.forEach(r => {
          all.push({
            ...r,
            substanceId: sub.id,
            substanceName: sub.name,
            substanceIcon: sub.icon,
            substanceNote: sub.note,
            sectionId: sec.id,
            sectionName: sec.name,
            chapterId: ch.id,
            chapterName: ch.name,
          });
        });
      });
    });
  });
  return all;
}

const ALL_REACTIONS = flattenReactions(TEXTBOOK);

export { TEXTBOOK, ALL_REACTIONS };
