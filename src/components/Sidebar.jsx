import { useState } from 'react';

export default function Sidebar() {
  const [showDonate, setShowDonate] = useState(false);
  const [hits, setHits] = useState(() => {
    try { return parseInt(localStorage.getItem('wooden_fish') || '0'); } catch { return 0; }
  });
  const [combo, setCombo] = useState(0);
  const [floating, setFloating] = useState(null);

  const knock = () => {
    const newCombo = combo + 1;
    setCombo(newCombo);
    const bonus = Math.floor(Math.random() * 5) + 1;
    setHits(h => {
      const n = h + bonus;
      localStorage.setItem('wooden_fish', String(n));
      return n;
    });
    const msg = newCombo >= 10 ? '🔥 十方世界，大慈大悲！' :
                newCombo >= 7 ? '🌟 七级浮屠，法力无边！' :
                newCombo >= 5 ? '✨ 五福临门，功德圆满！' :
                newCombo >= 3 ? '🙏 三声佛号，功德无量' :
                `给冯老师集功德 +${bonus}`;
    setFloating(msg);
    setTimeout(() => setFloating(null), 1500);
  };

  return (
    <>
      <div className="sidebar-fixed">
        <div className="sidebar-donate" onClick={() => setShowDonate(true)}>
          🥇 如果对你有帮助，欢迎打赏支持
        </div>
        <div className="sidebar-fish" onClick={knock}>
          <span className="sidebar-fish-emoji">🪘</span>
          <span className="sidebar-fish-text">敲木鱼给冯老师积功德</span>
          <span className="sidebar-fish-count">{hits}</span>
          {combo >= 3 && <span className="sidebar-fish-combo">🔥{combo}连</span>}
        </div>
        {floating && <div className="sidebar-float">{floating}</div>}
      </div>
    </>
  );
}
