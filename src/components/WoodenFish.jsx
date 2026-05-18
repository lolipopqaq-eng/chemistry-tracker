import { useState, useEffect } from 'react';

const FISH_SAYINGS = [
  '铛～～～',
  '善哉善哉',
  '阿弥陀佛',
  '随喜赞叹',
  '我佛慈悲',
  '功德圆满',
  '法喜充满',
  '佛光普照',
  '祥云瑞彩',
  '六时吉祥',
];

const COMBO_SAYINGS = {
  3: ['🙏 三声佛号，功德无量', '🙏 三生有幸，福慧双修'],
  5: ['✨ 五福临门，善哉善哉！', '✨ 五行运转，功德圆满！'],
  7: ['🌟 七级浮屠，法力无边！', '🌟 七宝庄严，随喜赞叹！'],
  10: ['🔥 十方世界，大慈大悲！', '🔥 十善圆满，功德无量！'],
  15: ['🎉 十五连击！佛光普照！', '🎉 功德如海，善莫大焉！'],
  20: ['👑 二十连击！我佛赞叹！', '👑 大成至善，功德圆满！'],
};

function getMilestone(combo) {
  const keys = Object.keys(COMBO_SAYINGS).map(Number).sort((a, b) => b - a);
  for (const k of keys) {
    if (combo === k) return COMBO_SAYINGS[k][Math.floor(Math.random() * COMBO_SAYINGS[k].length)];
  }
  return null;
}

// 每位学生每次敲的功德数（随机1-5）
function getFishBonus() {
  return Math.floor(Math.random() * 5) + 1;
}

function getFishTitle(hits) {
  if (hits >= 1000) return '🍚 已敲一吨木鱼';
  if (hits >= 500) return '🪷 功德如海';
  if (hits >= 200) return '🧘 得道高僧';
  if (hits >= 100) return '📿 功德圆满';
  if (hits >= 50) return '🙏 善信弟子';
  return '🐟 初入佛门';
}

export default function WoodenFish() {
  const [hits, setHits] = useState(() => {
    try {
      return parseInt(localStorage.getItem('wooden_fish') || '0');
    } catch { return 0; }
  });
  const [floating, setFloating] = useState(null);
  const [combo, setCombo] = useState(0);

  useEffect(() => {
    localStorage.setItem('wooden_fish', String(hits));
  }, [hits]);

  const knock = () => {
    const newCombo = combo + 1;
    setCombo(newCombo);
    const bonus = getFishBonus();
    setHits(h => h + bonus);

    const milestone = getMilestone(newCombo);
    let msg;
    if (milestone) {
      msg = milestone;
    } else if (newCombo >= 20) {
      const sayings = ['👑 功德如海！', '👑 善莫大焉！', '👑 佛光万丈！'];
      msg = sayings[Math.floor(Math.random() * sayings.length)];
    } else {
      msg = `给冯老师集功德 +${bonus}  ${FISH_SAYINGS[Math.floor(Math.random() * FISH_SAYINGS.length)]}`;
    }
    setFloating(msg);
    setTimeout(() => setFloating(null), 1500);
  };

  return (
    <div className="wooden-fish-area">
      <div className="wooden-fish-box" onClick={knock}>
        <div className="wooden-fish-emoji">🪘</div>
        <div className="wooden-fish-text">敲木鱼给冯老师积功德</div>
        <div className="wooden-fish-count">功德：{hits}</div>
        <div className="wooden-fish-title">{getFishTitle(hits)}</div>
        {combo >= 3 && <div className="wooden-fish-combo">🔥 {combo}连</div>}
      </div>
      {floating && <div className="wooden-fish-float">{floating}</div>}
    </div>
  );
}
