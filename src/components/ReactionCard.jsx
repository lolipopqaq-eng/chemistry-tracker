import { useState } from 'react';
import { getMasteryLevel } from '../utils/status';
import { formatDateTime } from '../utils/storage';

// 解析方程
function renderEquation(eq) {
  // 带条件: '2Na + O₂ →(点燃) Na₂O₂'
  const match = eq.match(/^(.+?)→\((.+?)\)(.+)$/);
  if (match) {
    const [, left, condition, right] = match;
    return (
      <div className="eq-box">
        <span className="eq-left">{left.trim()}</span>
        <span className="eq-arrow-block">
          <span className="eq-cond">{condition.trim()}</span>
          <span className="eq-arrow">→</span>
        </span>
        <span className="eq-right">{right.trim()}</span>
      </div>
    );
  }
  // 简单箭头
  const simpleMatch = eq.match(/^(.+?)→(.+)$/);
  if (simpleMatch) {
    const [, left, right] = simpleMatch;
    if (left.includes('不反应') || left.includes('加热不分解')) {
      return <span>{eq}</span>;
    }
    return (
      <div className="eq-box">
        <span className="eq-left">{left.trim()}</span>
        <span className="eq-arrow">→</span>
        <span className="eq-right">{right.trim()}</span>
      </div>
    );
  }
  return <span>{eq}</span>;
}

export default function ReactionCard({ reaction, record, onClick, onMarkResult }) {
  const [showEquation, setShowEquation] = useState(false);
  const [showPhenomenon, setShowPhenomenon] = useState(false);
  const rec = record || { reviewCount: 0, lastCorrect: 0, lastReviewAt: null };
  const mastery = getMasteryLevel(rec.reviewCount, rec.lastCorrect);

  return (
    <div className={`reaction-card level-${mastery.level}`}>
      <div onClick={() => onClick(reaction)}>
        <div className="card-header">
          <div className="card-name">{reaction.name}</div>
          <span className={`card-badge ${mastery.cls}`}>{mastery.label}</span>
        </div>

        <div className="card-toggle" onClick={(e) => { e.stopPropagation(); setShowEquation(!showEquation); }}>
          {showEquation ? (
            <>
              <div className="card-equation">{renderEquation(reaction.equation)}</div>
              <div className="card-toggle-hint">▲ 收起</div>
            </>
          ) : (
            <div className="card-toggle-hint">📝 点击查看化学方程式</div>
          )}
        </div>

        {reaction.phenomenon && (
          <div className="card-toggle" onClick={(e) => { e.stopPropagation(); setShowPhenomenon(!showPhenomenon); }}>
            {showPhenomenon ? (
              <>
                <div className="card-phenomenon">👁️ {reaction.phenomenon}</div>
                <div className="card-toggle-hint">▲ 收起</div>
              </>
            ) : (
              <div className="card-toggle-hint">👁️ 点击查看实验现象</div>
            )}
          </div>
        )}

        <div className="card-category">
          <span className="tag">{reaction.category}</span>
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
