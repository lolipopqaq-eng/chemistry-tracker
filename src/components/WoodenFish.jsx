import { useState, useEffect } from 'react';

const WOODEN_FISH = [
  '功德 +1',
  '功德 +3',
  '功德 +5',
  '铛～～～',
  '法力无边',
  '善哉善哉',
  '阿弥陀佛',
  '随喜赞叹',
];

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
    setHits(h => h + 1);

    const msg = newCombo >= 10 ? `🔥 ${newCombo}连击！大慈大悲！` :
                newCombo >= 5 ? `✨ ${newCombo}连击！功德无量！` :
                WOODEN_FISH[Math.floor(Math.random() * WOODEN_FISH.length)];
    setFloating(msg);
    setTimeout(() => setFloating(null), 1200);
  };

  return (
    <div className="wooden-fish-area">
      <div className="wooden-fish-box" onClick={knock}>
        <div className="wooden-fish-emoji">🐟</div>
        <div className="wooden-fish-text">敲木鱼</div>
        <div className="wooden-fish-count">功德：{hits}</div>
        {combo >= 5 && <div className="wooden-fish-combo">🔥 {combo}连</div>}
      </div>
      {floating && <div className="wooden-fish-float">{floating}</div>}
    </div>
  );
}
