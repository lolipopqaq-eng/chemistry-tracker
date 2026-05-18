import { useState } from 'react';
import { getMasteryLevel } from '../utils/status';
import { formatDateTime } from '../utils/storage';

export default function ReactionCard({ reaction, record, onClick, onMarkResult }) {
  const [showEquation, setShowEquation] = useState(false);
  const rec = record || { reviewCount: 0, lastCorrect: 0, lastReviewAt: null };
  const mastery = getMasteryLevel(rec.reviewCount, rec.lastCorrect);

  return (
    <div className={`reaction-card level-${mastery.level}`}>
      <div onClick={() => onClick(reaction)}>
        <div className="card-header">
          <div className="card-name">{reaction.name}</div>
          <span className={`card-badge ${mastery.cls}`}>{mastery.label}</span>
        </div>

        <div className="card-equation-toggle" onClick={(e) => { e.stopPropagation(); setShowEquation(!showEquation); }}>
          {showEquation ? (
            <>
              <div className="card-equation">{reaction.equation}</div>
              <div className="card-equation-hint">点击收起</div>
            </>
          ) : (
            <div className="card-equation-hint">👆 点击查看化学方程式</div>
          )}
        </div>

        <div className="card-category">
          <span className="tag">{reaction.category}</span>
          <span className="tag" style={{ marginLeft: 4 }}>{reaction.section}</span>
        </div>

        {reaction.note && <div className="card-note">💡 {reaction.note}</div>}

        <div className="card-meta">
          <span>📖 复习 {rec.reviewCount} 次</span>
          {rec.reviewCount > 0 && (
            <span>✅ 正确率 {Math.round(rec.lastCorrect / rec.reviewCount * 100)}%</span>
          )}
          {rec.lastReviewAt && (
            <span>🕐 上次：{formatDateTime(rec.lastReviewAt)}</span>
          )}
        </div>
      </div>

      <div className="card-actions">
        <button className="btn-know" onClick={(e) => { e.stopPropagation(); onMarkResult(reaction.id, true); }}>
          ✅ 会了
        </button>
        <button className="btn-not-know" onClick={(e) => { e.stopPropagation(); onMarkResult(reaction.id, false); }}>
          ❌ 不会
        </button>
      </div>
    </div>
  );
}
