const TEXTBOOK = {
  name: '人教版化学必修第一册',
  chapters: [
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
              note: '银白色、质软、密度0.97、熔点低、保存在煤油中',
              reactions: [
                { id: 'ch2_na1', name: 'Na + O₂（常温）', equation: '4Na + O₂ = 2Na₂O', category: '与氧气', phenomenon: '银白色金属钠表面变暗', note: '⚠ 注意条件：常温' },
                { id: 'ch2_na2', name: 'Na + O₂（点燃）', equation: '2Na + O₂ = Na₂O₂', category: '与氧气', phenomenon: '发出黄色火焰，生成淡黄色固体', note: '⚠ 产物颜色：淡黄色' },
                { id: 'ch2_na3', name: 'Na + H₂O', equation: '2Na + 2H₂O = 2NaOH + H₂↑', category: '与水', phenomenon: '浮=熔=游=响=红', note: '💯 必考！浮熔游响红' },
                { id: 'ch2_na4', name: 'Na + Cl₂', equation: '2Na + Cl₂ = 2NaCl', category: '与氯气', phenomenon: '钠在氯气中剧烈燃烧，产生白烟', note: '⚠ 白烟是NaCl固体颗粒' },
              ],
            },
            {
              id: 'ch2_na2o',
              name: 'Na₂O 氧化钠',
              icon: '⬜',
              note: '白色固体，碱性氧化物',
              reactions: [
                { id: 'ch2_o1', name: 'Na₂O + H₂O', equation: 'Na₂O + H₂O = 2NaOH', category: '与水', note: '碱性氧化物通性' },
                { id: 'ch2_o2', name: 'Na₂O + CO₂', equation: 'Na₂O + CO₂ = Na₂CO₃', category: '与CO₂', note: '碱性氧化物+酸性氧化物=盐' },
                { id: 'ch2_o3', name: 'Na₂O + HCl', equation: 'Na₂O + 2HCl = 2NaCl + H₂O', category: '与酸', note: '碱性氧化物通性' },
              ],
            },
            {
              id: 'ch2_na2o2',
              name: 'Na₂O₂ 过氧化钠',
              icon: '🟡',
              note: '淡黄色固体，供氧剂',
              reactions: [
                { id: 'ch2_p1', name: 'Na₂O₂ + H₂O', equation: '2Na₂O₂ + 2H₂O = 4NaOH + O₂↑', category: '与水', phenomenon: '产生气泡，酚酞先变红后褪色', note: '⚠ 注意Na₂O₂既是氧化剂又是还原剂' },
                { id: 'ch2_p2', name: 'Na₂O₂ + CO₂', equation: '2Na₂O₂ + 2CO₂ = 2Na₂CO₃ + O₂', category: '与CO₂', phenomenon: '淡黄色固体变白', note: '💯 供氧剂原理！必考' },
                { id: 'ch2_p3', name: 'Na₂O₂ + HCl', equation: '2Na₂O₂ + 4HCl = 4NaCl + 2H₂O + O₂↑', category: '与酸', note: '类似与H₂O的反应' },
              ],
            },
            {
              id: 'ch2_naoh',
              name: 'NaOH 氢氧化钠',
              icon: '🧪',
              note: '白色固体、强碱、潮解、腐蚀性',
              reactions: [
                { id: 'r01', name: 'Al + NaOH', equation: '2Al + 2NaOH + 2H₂O = 2NaAlO₂ + 3H₂↑', category: '与单质', phenomenon: '铝逐渐溶解，产生气泡', note: '💯 Al的两性体现' },
                { id: 'r02', name: 'Si + NaOH', equation: 'Si + 2NaOH + H₂O = Na₂SiO₃ + 2H₂↑', category: '与单质', note: 'Si与碱的歧化反应' },
                { id: 'r03', name: 'Cl₂ + NaOH（常温）', equation: 'Cl₂ + 2NaOH = NaCl + NaClO + H₂O', category: '与单质', phenomenon: '黄绿色气体褪去', note: '⚠ 歧化反应，制84消毒液' },
                { id: 'r04', name: 'Cl₂ + NaOH（加热）', equation: '3Cl₂ + 6NaOH = 5NaCl + NaClO₃ + 3H₂O', category: '与单质', note: '加热歧化，产物不同' },
                { id: 'r05', name: 'S + NaOH', equation: '3S + 6NaOH = 2Na₂S + Na₂SO₃ + 3H₂O', category: '与单质', note: '硫的歧化' },
                { id: 'r06', name: 'NaOH + CO₂（过量CO₂）', equation: 'NaOH + CO₂ = NaHCO₃', category: '与酸性氧化物', note: '⚠ 注意量！CO₂过量' },
                { id: 'r07', name: 'NaOH + CO₂（过量NaOH）', equation: '2NaOH + CO₂ = Na₂CO₃ + H₂O', category: '与酸性氧化物', note: '⚠ 注意量！NaOH过量' },
                { id: 'r08', name: 'NaOH + SO₂', equation: '2NaOH + SO₂ = Na₂SO₃ + H₂O', category: '与酸性氧化物', note: 'SO₂过量生成NaHSO₃' },
                { id: 'r09', name: 'NaOH + SiO₂', equation: '2NaOH + SiO₂ = Na₂SiO₃ + H₂O', category: '与酸性氧化物', note: '💯 玻璃瓶不能用磨口玻璃塞' },
                { id: 'r10', name: 'NaOH + HCl', equation: 'NaOH + HCl = NaCl + H₂O', category: '中和', note: '强酸强碱中和' },
                { id: 'r11', name: 'NaOH + CH₃COOH', equation: 'NaOH + CH₃COOH = CH₃COONa + H₂O', category: '中和', note: '弱酸也能中和' },
                { id: 'r12', name: 'NaOH + H₂S', equation: '2NaOH + H₂S = Na₂S + 2H₂O', category: '中和', note: '二元酸中和' },
                { id: 'r13', name: 'Al₂O₃ + NaOH', equation: 'Al₂O₃ + 2NaOH = 2NaAlO₂ + H₂O', category: '两性', note: '💯 Al₂O₃两性' },
                { id: 'r14', name: 'Al(OH)₃ + NaOH', equation: 'Al(OH)₃ + NaOH = NaAlO₂ + 2H₂O', category: '两性', note: '💯 Al(OH)₃两性，高考必考' },
                { id: 'r15', name: 'NH₄Cl + NaOH', equation: 'NH₄Cl + NaOH = NaCl + NH₃↑ + H₂O', category: '与盐', phenomenon: '湿润红色石蕊试纸变蓝', note: '💯 实验室制NH₃' },
                { id: 'r16', name: 'CuSO₄ + NaOH', equation: 'CuSO₄ + 2NaOH = Cu(OH)₂↓ + Na₂SO₄', category: '与盐', phenomenon: '蓝色絮状沉淀', note: '⚠ 沉淀颜色：蓝色' },
                { id: 'r17', name: 'FeCl₃ + NaOH', equation: 'FeCl₃ + 3NaOH = Fe(OH)₃↓ + 3NaCl', category: '与盐', phenomenon: '红褐色沉淀', note: '⚠ 沉淀颜色：红褐色' },
                { id: 'r18', name: 'NaHCO₃ + NaOH', equation: 'NaHCO₃ + NaOH = Na₂CO₃ + H₂O', category: '与盐', note: '酸式盐+碱=正盐' },
                { id: 'r19', name: '卤代烃水解', equation: 'CH₃CH₂Br + NaOH = CH₃CH₂OH + NaBr', category: '有机', note: '水溶液，取代反应' },
                { id: 'r20', name: '卤代烃消去', equation: 'CH₃CH₂Br + NaOH = CH₂=CH₂↑ + NaBr + H₂O', category: '有机', note: '醇溶液，消去反应' },
                { id: 'r21', name: '油脂皂化', equation: '油脂 + NaOH = 高级脂肪酸钠 + 甘油', category: '有机', note: '碱性水解' },
                { id: 'r22', name: '苯酚 + NaOH', equation: 'C₆H₅OH + NaOH = C₆H₅ONa + H₂O', category: '有机', phenomenon: '苯酚由浑浊变澄清', note: '酚羟基显弱酸性' },
                { id: 'r23', name: '酯的碱性水解', equation: "RCOOR' + NaOH = RCOONa + R'OH", category: '有机', note: '碱性条件下彻底水解' },
              ],
            },
            {
              id: 'ch2_na2co3',
              name: 'Na₂CO₃ 碳酸钠',
              icon: '🧂',
              note: '白色粉末、易溶、热稳定性高',
              reactions: [
                { id: 'n01', name: 'Na₂CO₃ + HCl（少量）', equation: 'Na₂CO₃ + HCl = NaHCO₃ + NaCl', category: '与酸', phenomenon: '开始无气泡', note: '💯 逐滴加盐酸，先无气泡后有气泡' },
                { id: 'n02', name: 'Na₂CO₃ + HCl（过量）', equation: 'Na₂CO₃ + 2HCl = 2NaCl + H₂O + CO₂↑', category: '与酸', phenomenon: '立即产生气泡', note: '💯 与n01对比记忆' },
                { id: 'n03', name: 'Na₂CO₃ + Ca(OH)₂', equation: 'Na₂CO₃ + Ca(OH)₂ = CaCO₃↓ + 2NaOH', category: '与碱', phenomenon: '白色沉淀', note: '工业制烧碱' },
                { id: 'n04', name: 'Na₂CO₃ + Ba(OH)₂', equation: 'Na₂CO₃ + Ba(OH)₂ = BaCO₃↓ + 2NaOH', category: '与碱', phenomenon: '白色沉淀', note: '类似n03' },
                { id: 'n05', name: 'Na₂CO₃ + NaOH', equation: 'Na₂CO₃ + NaOH = 不反应', category: '与碱', note: '不反应' },
                { id: 'n06', name: 'Na₂CO₃ + CaCl₂', equation: 'Na₂CO₃ + CaCl₂ = CaCO₃↓ + 2NaCl', category: '与盐', phenomenon: '白色沉淀', note: '💯 检验CO₃²⁻的方法' },
                { id: 'n07', name: 'Na₂CO₃ + BaCl₂', equation: 'Na₂CO₃ + BaCl₂ = BaCO₃↓ + 3NaCl', category: '与盐', phenomenon: '白色沉淀', note: '💯 同样可检验CO₃²⁻' },
                { id: 'n08', name: 'Na₂CO₃ + CO₂ + H₂O', equation: 'Na₂CO₃ + H₂O + CO₂ = 2NaHCO₃', category: '与CO₂', phenomenon: '溶液变浑浊', note: '制小苏打' },
                { id: 'n09', name: 'CO₃²⁻水解', equation: 'CO₃²⁻ + H₂O ⇌ HCO₃⁻ + OH⁻', category: '水解', note: '💯 溶液显碱性，俗称纯碱' },
                { id: 'n10', name: 'Na₂CO₃加热', equation: 'Na₂CO₃ 加热不分解', category: '热稳定性', note: '💯 对比：NaHCO₃加热分解' },
              ],
            },
            {
              id: 'ch2_nahco3',
              name: 'NaHCO₃ 碳酸氢钠',
              icon: '🥤',
              note: '白色细小晶体，可溶于水',
              reactions: [
                { id: 'h01', name: 'NaHCO₃ + HCl', equation: 'NaHCO₃ + HCl = NaCl + H₂O + CO₂↑', category: '与酸', phenomenon: '直接冒气泡', note: '💯 与Na₂CO₃对比' },
                { id: 'h02', name: 'NaHCO₃ + NaOH', equation: 'NaHCO₃ + NaOH = Na₂CO₃ + H₂O', category: '与碱', note: '酸式盐+碱=正盐' },
                { id: 'h03', name: 'NaHCO₃少量 + Ca(OH)₂', equation: 'HCO₃⁻ + OH⁻ + Ca²⁺ = CaCO₃↓ + H₂O', category: '与碱', phenomenon: '白色沉淀', note: '⚠ 注意量！少量' },
                { id: 'h04', name: 'NaHCO₃过量 + Ca(OH)₂', equation: '2HCO₃⁻ + 2OH⁻ + Ca²⁺ = CaCO₃↓ + CO₃²⁻ + 2H₂O', category: '与碱', phenomenon: '白色沉淀', note: '⚠ 注意量！过量' },
                { id: 'h05', name: 'NaHCO₃受热分解', equation: '2NaHCO₃ = Na₂CO₃ + H₂O + CO₂↑', category: '分解', phenomenon: '水珠产生，气体使澄清石灰水变浑浊', note: '💯 唯一受热易分解的钠盐！必考' },
                { id: 'h06', name: 'NaHCO₃ + CO₂', equation: 'NaHCO₃ + CO₂ = 不反应', category: '与CO₂', note: '不反应' },
                { id: 'h07', name: 'NaHCO₃ + Na₂CO₃', equation: 'NaHCO₃ + Na₂CO₃ = 不反应', category: '与碳酸钠', note: '不反应' },
                { id: 'h08', name: 'HCO₃⁻水解', equation: 'HCO₃⁻ + H₂O ⇌ H₂CO₃ + OH⁻', category: '水解', note: '💯 碱性：Na₂CO₃ > NaHCO₃' },
                { id: 'h09', name: 'Na₂CO₃=NaHCO₃', equation: 'Na₂CO₃ + CO₂ + H₂O = 2NaHCO₃', category: '转化', phenomenon: '溶液变浑浊', note: '通CO₂' },
                { id: 'h10', name: 'NaHCO₃=Na₂CO₃', equation: 'NaHCO₃ + NaOH = Na₂CO₃ + H₂O', category: '转化', note: '加碱' },
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
                { id: 'cl1', name: 'Cl₂ + Cu', equation: 'Cu + Cl₂ = CuCl₂', category: '与金属', phenomenon: '棕黄色烟', note: '⚠ 产物颜色：棕黄色' },
                { id: 'cl2', name: 'Cl₂ + H₂', equation: 'H₂ + Cl₂ = 2HCl', category: '与非金属', phenomenon: '苍白色火焰，瓶口白雾', note: '💯 苍白色火焰' },
                { id: 'cl3', name: 'Cl₂ + H₂O', equation: 'Cl₂ + H₂O ⇌ HCl + HClO', category: '与水', note: '💯 可逆反应！' },
                { id: 'cl4', name: 'Cl₂ + NaOH', equation: 'Cl₂ + 2NaOH = NaCl + NaClO + H₂O', category: '与碱', note: '制84消毒液' },
                { id: 'cl5', name: 'Cl₂ + Ca(OH)₂', equation: '2Cl₂ + 2Ca(OH)₂ = CaCl₂ + Ca(ClO)₂ + 2H₂O', category: '与碱', note: '制漂白粉' },
                { id: 'cl6', name: 'Cl₂ + Fe', equation: '2Fe + 3Cl₂ = 2FeCl₃', category: '与金属', phenomenon: '棕褐色烟', note: '⚠ 生成Fe³⁺ 不是Fe²⁺' },
                { id: 'cl7', name: 'Cl₂ + NaBr', equation: 'Cl₂ + 2NaBr = 2NaCl + Br₂', category: '置换', phenomenon: '溶液变橙黄色', note: '💯 氧化性：Cl₂ > Br₂' },
                { id: 'cl8', name: 'Cl₂ + KI', equation: 'Cl₂ + 2KI = 2KCl + I₂', category: '置换', phenomenon: '溶液变棕黄，淀粉变蓝', note: '💯 氧化性：Cl₂ > I₂' },
              ],
            },
            {
              id: 'ch2_hclo',
              name: 'HClO 次氯酸',
              icon: '🧴',
              note: '弱酸性、强氧化性、漂白性（不可逆）',
              reactions: [
                { id: 'hclo1', name: 'HClO 光照分解', equation: '2HClO = 2HCl + O₂↑', category: '分解', phenomenon: '氯水颜色变浅', note: '💯 氯水需避光保存' },
              ],
            },
            {
              id: 'ch2_nacl',
              name: 'NaCl 氯化钠',
              icon: '🧂',
              note: '白色晶体，易溶于水',
              reactions: [
                { id: 'nacl1', name: '电解饱和食盐水', equation: '2NaCl + 2H₂O = 2NaOH + H₂↑ + Cl₂↑', category: '电解', phenomenon: '阴极H₂无色、阳极Cl₂黄绿色', note: '💯 氯碱工业' },
              ],
            },
          ],
        },
      ],
    },
  ],
};

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
