const fs = require('fs');

// Helper
function r(id, name, equation, category, opts) {
  return { id, name, equation, category, ...opts };
}

// r with id prefix
function ri(prefix, name, eq, cat, opts) {
  return r(prefix + '_' + (opts && opts._id || name.replace(/[^a-zA-Z0-9]/g,'')), name, eq, cat, opts || {});
}

const chapters = [];

// ================================================================
// CHAPTER 1
// ================================================================
chapters.push({
  id: 'ch1', name: '第一章 物质及其变化',
  sections: [{
    id: 'ch1_elec', name: '电解质与离子反应',
    substances: [
      { id: 'ch1_hcl', name: 'HCl 盐酸', icon: '\uD83E\uDDEA', note: '强酸、强电解质',
        reactions: [
          r('ch1_hcl1', 'HCl 电离', 'HCl = H\u207a + Cl\u207b', '电离', {note: '强电解质完全电离'}),
          r('ch1_hcl2', 'HCl + NaOH', 'HCl + NaOH = NaCl + H\u2082O', '中和', {note: '\uD83D\uDCAF H\u207a + OH\u207b = H\u2082O'}),
          r('ch1_hcl3', 'HCl + Na\u2082CO\u2083', '2HCl + Na\u2082CO\u2083 = 2NaCl + H\u2082O + CO\u2082\u2191', '与盐', {phenomenon: '产生气泡', note: 'CO\u2083\u00b2\u207b + 2H\u207a = H\u2082O + CO\u2082\u2191'}),
        ]},
    ],
  }],
});

// ================================================================
// CHAPTER 2
// ================================================================
chapters.push({
  id: 'ch2', name: '\u7B2C\u4E8C\u7AE0 \u6D77\u6C34\u4E2D\u7684\u91CD\u8981\u5143\u7D20\u2014\u2014\u94A0\u548C\u6C2F',
  sections: [
    {
      id: 'ch2_na', name: '\u94A0\u53CA\u5176\u5316\u5408\u7269',
      substances: [
        { id: 'ch2_na_metal', name: 'Na \u94A0\u5355\u8D28', icon: '\uD83E\uDD48', note: '\u94F6\u767D\u8272\u3001\u8D28\u8F6F\u3001\u5BC6\u5EA60.97\u3001\u7194\u70B9\u4F4E\u3001\u4FDD\u5B58\u5728\u7164\u6CB9\u4E2D',
          reactions: [
            r('ch2_na1', 'Na + O\u2082\uff08\u5E38\u6E29\uff09', '4Na + O\u2082 = 2Na\u2082O', '\u4E0E\u6C27\u6C14', {phenomenon: '\u94F6\u767D\u8272\u91D1\u5C5E\u94A0\u8868\u9762\u53D8\u6697', note: '\u26A0 \u6CE8\u610F\u6761\u4EF6\uff1A\u5E38\u6E29'}),
          ],
        },
      ],
    },
  ],
});

console.log('ch1, ch2 minimal added');
console.log('JSON:', JSON.stringify(chapters).length, 'chars');
