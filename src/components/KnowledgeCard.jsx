import { useState, useEffect, useMemo, useRef } from 'react';

export default function KnowledgeCard({ knowledge, onComplete }) {
  const [revealed, setRevealed] = useState({});
  const containerRef = useRef(null);

  const toggle = (idx) => {
    setRevealed(prev => {
      const next = { ...prev, [idx]: !prev[idx] };
      return next;
    });
  };

  const allRevealed = useMemo(() => {
    if (!knowledge || knowledge.length === 0) return false;
    return knowledge.every((_, i) => revealed[i]);
  }, [knowledge, revealed]);

  // 全部揭示后自动触发跳转
  useEffect(() => {
    if (allRevealed && knowledge.length >= 2) {
      const timer = setTimeout(() => {
        if (onComplete) onComplete();
      }, 1200); // 1.2秒后自动跳转
      return () => clearTimeout(timer);
    }
  }, [allRevealed]);

  if (!knowledge || knowledge.length === 0) return null;

  return (
    <div className="knowledge-block" ref={containerRef}>
      <div className="knowledge-title">📖 知识点填空</div>
      <div className="knowledge-hint">思考后点击题目查看答案</div>
      {knowledge.map((item, idx) => (
        <div key={idx} className="knowledge-item" onClick={() => toggle(idx)}>
          <div className="knowledge-q">{item.q}</div>
          <div className={`knowledge-a ${revealed[idx] ? '' : 'hidden'}`}>
            {revealed[idx] ? item.a : '👆 点击查看答案'}
          </div>
        </div>
      ))}
      {allRevealed && knowledge.length >= 2 && (
        <div className="knowledge-done">全部掌握 ✓ 正在进入下一节...</div>
      )}
    </div>
  );
}
