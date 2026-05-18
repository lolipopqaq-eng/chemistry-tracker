import { useState } from 'react';
import { getMasteryLevel } from '../utils/status';
import { formatDateTime } from '../utils/storage';

function renderEquation(eq) {
  if (eq.includes('不反应') || eq.includes('加热不分解')) {
    return <span>{eq}</span>;
  }

  const condMatch = eq.match(/^(.+?)([=→])\((.+?)\)(.+)$/);
  if (condMatch) {
    const [, left, arrow, condition, right] = condMatch;
    return (
      <div className="eq-box">
        <span className="eq-left">{left.trim()}</span>
        <span className="eq-arrow-block">
          <span className="eq-cond">{condition.trim()}</span>
          <span className="eq-arrow">{arrow}</span>
        </span>
        <span className="eq-right">{right.trim()}</span>
      </div>
    );
  }

  const revMatch = eq.match(/^(.+?)⇌(.+)$/);
  if (revMatch) {
    return (
      <div className="eq-box">
        <span className="eq-left">{revMatch[1].trim()}</span>
        <span className="eq-arrow">⇌</span>
        <span className="eq-right">{revMatch[2].trim()}</span>
      </div>
    );
  }

  const eqMatch = eq.match(/^(.+?)=(.*)$/);
  if (eqMatch && !eqMatch[1].includes('→')) {
    return (
      <div className="eq-box">
        <span className="eq-left">{eqMatch[1].trim()}</span>
        <span className="eq-arrow">=</span>
        <span className="eq-right">{eqMatch[2].trim()}</span>
      </div>
    );
  }

  const arrMatch = eq.match(/^(.+?)→(.+)$/);
  if (arrMatch) {
    return (
      <div className="eq-box">
        <span className="eq-left">{arrMatch[1].trim()}</span>
        <span className="eq-arrow">→</span>
        <span className="eq-right">{arrMatch[2].trim()}</span>
      </div>
    );
  }

  return <span>{eq}</span>;
}

export default function ReactionCard({ reaction, record, onClick, onMarkResult }) {
  const [showEquation, setShowEquation] = useState(false);
  const [showPhenomenon, setShowPhenomenon] = useState(false);
  const [showNote, setShowNote] = useState(false);
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

        {reaction.note && (
          <div className="card-toggle" onClick={(e) => { e.stopPropagation(); setShowNote(!showNote); }}>
            {showNote ? (
              <>
                <div className="card-note">💡 {reaction.note}</div>
                <div className="card-toggle-hint">▲ 收起提示</div>
              </>
            ) : (
              <div className="card-toggle-hint">💡 点击查看考点提示</div>
            )}
          </div>
        )}

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
