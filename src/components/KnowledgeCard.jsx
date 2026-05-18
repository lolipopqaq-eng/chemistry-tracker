import { useState } from 'react';

export default function KnowledgeCard({ knowledge }) {
  const [showAnswer, setShowAnswer] = useState({});

  const toggle = (idx) => {
    setShowAnswer(prev => ({ ...prev, [idx]: !prev[idx] }));
  };

  if (!knowledge || knowledge.length === 0) return null;

  return (
    <div className="knowledge-block">
      <div className="knowledge-title">📖 知识点填空</div>
      {knowledge.map((item, idx) => (
        <div key={idx} className="knowledge-item" onClick={() => toggle(idx)}>
          <div className="knowledge-q">{idx + 1}. {item.q}</div>
          <div className={`knowledge-a ${showAnswer[idx] ? '' : 'hidden'}`}>
            {showAnswer[idx] ? item.a : '👆 点击查看答案'}
          </div>
        </div>
      ))}
    </div>
  );
}
