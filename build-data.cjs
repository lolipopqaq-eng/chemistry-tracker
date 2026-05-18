const fs = require('fs');
const path = 'C:\\Users\\11384\\.openclaw\\workspace\\chemistry-tracker\\src\\utils\\textbook.js';

// Helper to create reaction object
function r(id, name, equation, category, opts = {}) {
  return { id, name, equation, category, ...opts };
}

// Build all chapters as a data structure, then serialize
const ch1 = {
  id: 'ch1',
  name: '第一章 物质及其变化',
  sections: [{
    id: 'ch1_elec',
    name: '电解质与离子反应',
    substances: [
      {
        id: 'ch1_hcl',
        name: 'HCl 盐酸',
        icon: '🧪',
        note: '强酸、强电解质',
        reactions: [
          r('ch1_hcl1', 'HCl 电离', 'HCl = H\u207a + Cl\u207b', '电离', {note: '强电解质完全电离'}),
          r('ch1_hcl2', 'HCl + NaOH', 'HCl + NaOH = NaCl + H\u2082O', '中和', {note: ' \uD83D\uDCAF H\u207a + OH\u207b = H\u2082O'}),
          r('ch1_hcl3', 'HCl + Na\u2082CO\u2083', '2HCl + Na\u2082CO\u2083 = 2NaCl + H\u2082O + CO\u2082\u2191', '与盐', {phenomenon: '产生气泡', note: 'CO\u2083\u00b2\u207b + 2H\u207a = H\u2082O + CO\u2082\u2191'}),
        ],
      },
      {
        id: 'ch1_naoh',
        name: 'NaOH 氢氧化钠',
        icon: '🧴',
        note: '强碱、强电解质',
        reactions: [
          r('ch1_naoh1', 'NaOH 电离', 'NaOH = Na\u207a + OH\u207b', '电离', {note: '强电解质完全电离'}),
          r('ch1_naoh2', 'NaOH + HCl', 'NaOH + HCl = NaCl + H\u2082O', '中和', {note: '中和反应'}),
          r('ch1_naoh3', 'NaOH + CuSO\u2084', '2NaOH + CuSO\u2084 = Cu(OH)\u2082\u2193 + Na\u2082SO\u2084', '复分解', {phenomenon: '蓝色沉淀', note: '复分解反应条件：有沉淀'}),
        ],
      },
      {
        id: 'ch1_na2so4',
        name: 'Na\u2082SO\u2084 硫酸钠',
        icon: '🧂',
        note: '盐、强电解质',
        reactions: [
          r('ch1_ns1', 'Na\u2082SO\u2084 电离', 'Na\u2082SO\u2084 = 2Na\u207a + SO\u2084\u00b2\u207b', '电离', {note: '强电解质完全电离'}),
        ],
      },
      {
        id: 'ch1_feoh3',
        name: 'Fe(OH)\u2083胶体',
        icon: '🧫',
        note: '胶体制备',
        reactions: [
          r('ch1_col1', 'Fe(OH)\u2083胶体制备', 'FeCl\u2083 + 3H\u2082O =(\u52a0\u70ed) Fe(OH)\u2083(\u80f6\u4f53) + 3HCl', '水解', {phenomenon: '溶液呈红褐色', note: ' \uD83D\uDCAF 丁达尔效应！不能写↓'}),
        ],
      },
    ],
  }],
};

console.log('ch1 built, icon check:', '🧪');

// Now serialize - we need to write JS, not JSON
// Approach: write the JSON-like structure with proper JS syntax
const chapters = [ch1];
const json = JSON.stringify(chapters, null, 2);
console.log('json length:', json.length);

// We'll write a .cjs that generates the file with proper formatting
const output = `const TEXTBOOK = {
  name: '人教版化学',
  chapters: ${json},
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
`;

fs.writeFileSync(path, output, 'utf8');
console.log('Done! File size:', fs.statSync(path).size);
