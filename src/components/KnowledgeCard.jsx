import { useState, useMemo } from 'react';

export default function KnowledgeCard({ knowledge, onComplete }) {
  const [revealed, setRevealed] = useState({});

  const toggle = (idx) => {
    setRevealed(prev => ({ ...prev, [idx]: !prev[idx] }));
  };

  const allRevealed = useMemo(() => {
    if (!knowledge || knowledge.length === 0) return false;
    return knowledge.every((_, i) => revealed[i]);
  }, [knowledge, revealed]);

  if (!knowledge || knowledge.length === 0) return null;

  return (
    <div className="knowledge-block">
      <div className="knowledge-title">📖 知识点填空</div>
      <div className="knowledge-hint">点击题目查看答案</div>
      {knowledge.map((item, idx) => (
        <div key={idx} className="knowledge-item" onClick={() => toggle(idx)}>
          <div className="knowledge-q">{item.q}</div>
          <div className={`knowledge-a ${revealed[idx] ? '' : 'hidden'}`}>
            {revealed[idx] ? item.a : '👆 点击查看答案'}
          </div>
        </div>
      ))}
      {allRevealed && knowledge.length >= 3 && onComplete && (
        <div className="knowledge-next" onClick={onComplete}>
          ✅ 全部看完 → 下一节
        </div>
      )}
    </div>
  );
}
