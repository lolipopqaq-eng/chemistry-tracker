const fs = require('fs');
let c = fs.readFileSync('src/utils/textbook.js', 'utf8');

// 修复 ch2_na2：equation里的（淡黄色）去掉，现象写对
c = c.replace(
  `id: 'ch2_na2', name: 'Na + O\u2082（点燃）', equation: '2Na + O\u2082 \u2192(点燃) Na\u2082O\u2082（淡黄色）', category: '钠单质',
    phenomenon: '钠浮在水面\u2192熔成小球\u2192四处游动\u2192发出嘶嘶声\u2192溶液变红（浮熔游响红）', note: '点燃生成过氧化钠（淡黄色）'`,
  `id: 'ch2_na2', name: 'Na + O\u2082（点燃）', equation: '2Na + O\u2082 \u2192(点燃) Na\u2082O\u2082', category: '钠单质',
    phenomenon: '钠剧烈燃烧，发出黄色火焰，生成淡黄色固体Na\u2082O\u2082', note: '点燃生成过氧化钠（淡黄色）'`
);


console.log('fixed');
fs.writeFileSync('src/utils/textbook.js', c, 'utf8');
