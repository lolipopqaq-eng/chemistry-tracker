const fs = require('fs');
let c = fs.readFileSync('src/utils/reactions.js', 'utf8');
c = c.replace(
  "RCOOR' + NaOH \\\\xrightarrow{\\\\\\\\Delta} RCOONa + R'OH",
  "RCOOR' + NaOH → RCOONa + R'OH"
);
fs.writeFileSync('src/utils/reactions.js', c);
console.log('Fixed');
