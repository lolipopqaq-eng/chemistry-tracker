// 碳酸钠 (Na₂CO₃) 全反应 - 高考极简背诵版
const NA2CO3_REACTIONS = [
  // 一、和酸反应
  {
    id: 'n01',
    name: 'Na₂CO₃ + 盐酸少量',
    equation: 'Na₂CO₃ + HCl → NaHCO₃ + NaCl（无气泡）',
    category: '碳酸钠',
    section: '一、与酸反应',
    note: '逐滴加盐酸，先无气泡，后出气泡（高考重点）',
  },
  {
    id: 'n02',
    name: 'Na₂CO₃ + 盐酸过量',
    equation: 'Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂↑（有气泡）',
    category: '碳酸钠',
    section: '一、与酸反应',
    note: '盐酸过量直接出气泡',
  },
  // 二、和碱反应
  {
    id: 'n03',
    name: 'Na₂CO₃ + Ca(OH)₂',
    equation: 'Na₂CO₃ + Ca(OH)₂ → CaCO₃↓ + 2NaOH',
    category: '碳酸钠',
    section: '二、与碱反应',
    note: '工业制烧碱方法，生成沉淀',
  },
  {
    id: 'n04',
    name: 'Na₂CO₃ + Ba(OH)₂',
    equation: 'Na₂CO₃ + Ba(OH)₂ → BaCO₃↓ + 2NaOH',
    category: '碳酸钠',
    section: '二、与碱反应',
    note: '生成白色沉淀',
  },
  {
    id: 'n05',
    name: 'Na₂CO₃ + NaOH',
    equation: 'Na₂CO₃ + NaOH → 不反应',
    category: '碳酸钠',
    section: '二、与碱反应',
    note: '碳酸钠和氢氧化钠不反应',
  },
  // 三、和盐反应
  {
    id: 'n06',
    name: 'Na₂CO₃ + CaCl₂',
    equation: 'Na₂CO₃ + CaCl₂ → CaCO₃↓ + 2NaCl',
    category: '碳酸钠',
    section: '三、与盐反应（沉淀）',
    note: '检验CO₃²⁻的方法：加Ca²⁺/Ba²⁺出白色沉淀',
  },
  {
    id: 'n07',
    name: 'Na₂CO₃ + BaCl₂',
    equation: 'Na₂CO₃ + BaCl₂ → BaCO₃↓ + 2NaCl',
    category: '碳酸钠',
    section: '三、与盐反应（沉淀）',
    note: '白色沉淀，同样用于检验CO₃²⁻',
  },
  // 四、与CO₂
  {
    id: 'n08',
    name: 'Na₂CO₃ + CO₂ + H₂O',
    equation: 'Na₂CO₃ + H₂O + CO₂ → 2NaHCO₃',
    category: '碳酸钠',
    section: '四、与CO₂反应',
    note: '饱和溶液会析出NaHCO₃晶体，工业制小苏打',
  },
  // 五、水解
  {
    id: 'n09',
    name: 'CO₃²⁻水解',
    equation: 'CO₃²⁻ + H₂O ⇌ HCO₃⁻ + OH⁻',
    category: '碳酸钠',
    section: '五、水解（选择题）',
    note: '溶液显碱性，俗称纯碱',
  },
  // 六、热稳定性
  {
    id: 'n10',
    name: 'Na₂CO₃加热',
    equation: 'Na₂CO₃ 加热不分解',
    category: '碳酸钠',
    section: '六、热稳定性',
    note: '稳定性：Na₂CO₃ > NaHCO₃（死记）',
  },
];

// 碳酸氢钠 (NaHCO₃) 必背反应
const NAHCO3_REACTIONS = [
  {
    id: 'h01',
    name: 'NaHCO₃ + 强酸（盐酸）',
    equation: 'NaHCO₃ + HCl → NaCl + H₂O + CO₂↑',
    category: '碳酸氢钠',
    section: '一、与强酸',
    note: '不管量多少，直接冒气泡，高考必考',
  },
  {
    id: 'h02',
    name: 'NaHCO₃ + NaOH',
    equation: 'NaHCO₃ + NaOH → Na₂CO₃ + H₂O',
    category: '碳酸氢钠',
    section: '二、与强碱',
    note: '酸式盐遇碱变正盐',
  },
  {
    id: 'h03',
    name: 'NaHCO₃少量 + Ca(OH)₂',
    equation: 'HCO₃⁻ + OH⁻ + Ca²⁺ → CaCO₃↓ + H₂O',
    category: '碳酸氢钠',
    section: '二、与碱反应（量与产物）',
    note: 'NaHCO₃少量时只生成碳酸钙沉淀',
  },
  {
    id: 'h04',
    name: 'NaHCO₃过量 + Ca(OH)₂',
    equation: '2HCO₃⁻ + 2OH⁻ + Ca²⁺ → CaCO₃↓ + CO₃²⁻ + 2H₂O',
    category: '碳酸氢钠',
    section: '二、与碱反应（量与产物）',
    note: 'NaHCO₃过量时产物中有CO₃²⁻',
  },
  {
    id: 'h05',
    name: 'NaHCO₃受热分解',
    equation: '2NaHCO₃ →(Δ) Na₂CO₃ + H₂O + CO₂↑',
    category: '碳酸氢钠',
    section: '三、受热分解（必考）',
    note: '唯一受热易分解的钠盐，高考必考',
  },
  {
    id: 'h06',
    name: 'NaHCO₃ + CO₂',
    equation: 'NaHCO₃ + CO₂ → 不反应',
    category: '碳酸氢钠',
    section: '四、与CO₂',
    note: '碳酸氢钠不与CO₂反应',
  },
  {
    id: 'h07',
    name: 'NaHCO₃ + Na₂CO₃',
    equation: 'NaHCO₃ + Na₂CO₃ → 不反应',
    category: '碳酸氢钠',
    section: '五、与碳酸钠',
    note: '两者不反应',
  },
  {
    id: 'h08',
    name: 'NaHCO₃水解',
    equation: 'HCO₃⁻ + H₂O ⇌ H₂CO₃ + OH⁻',
    category: '碳酸氢钠',
    section: '六、水解',
    note: '显弱碱性，碱性：Na₂CO₃ > NaHCO₃',
  },
  {
    id: 'h09',
    name: 'Na₂CO₃→NaHCO₃转化',
    equation: 'Na₂CO₃ + CO₂ + H₂O → 2NaHCO₃',
    category: '碳酸氢钠',
    section: '七、相互转化',
    note: '碳酸钠溶液通CO₂生成碳酸氢钠',
  },
  {
    id: 'h10',
    name: 'NaHCO₃→Na₂CO₃转化',
    equation: 'NaHCO₃ + NaOH → Na₂CO₃ + H₂O',
    category: '碳酸氢钠',
    section: '七、相互转化',
    note: '碳酸氢钠加碱变回碳酸钠',
  },
];

export { NA2CO3_REACTIONS, NAHCO3_REACTIONS };
