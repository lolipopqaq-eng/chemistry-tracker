import { useMemo, useState } from 'react';
import ReactionHistory from './ReactionHistory';
import { getMasteryLevel } from '../utils/status';
import { formatDateTime } from '../utils/storage';

export default function ReactionDetail({ reaction, record, history, onBack, onMarkResult }) {
  const [showResult, setShowResult] = useState(false);
  const [lastResult, setLastResult] = useState(null);

  const rec = record || { reviewCount: 0, lastCorrect: 0, lastReviewAt: null };
  const mastery = getMasteryLevel(rec.reviewCount, rec.lastCorrect);

  const reactionHistory = useMemo(() => {
    return history.filter(h => h.reactionId === reaction.id);
  }, [history, reaction.id]);

  const handleMark = (correct) => {
    onMarkResult(reaction.id, correct);
    setLastResult(correct);
    setShowResult(true);
    setTimeout(() => setShowResult(false), 2000);
  };

  return (
    <div className="detail-container">
      <button className="back-btn" onClick={onBack}>← 返回列表</button>

      <div className="detail-card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
          <div>
            <h2>{reaction.name}</h2>
            <span className="section-ref">{reaction.section}</span>
          </div>
          <span className={`card-badge ${mastery.cls}`}>{mastery.label}</span>
        </div>

        <div className="equation-lg">{reaction.equation}</div>

        <div className="meta-row">
          <span>🏷️ {reaction.category}</span>
          <span>📖 复习 {rec.reviewCount} 次</span>
          {rec.reviewCount > 0 && (
            <span>✅ 正确 {rec.lastCorrect}/{rec.reviewCount} ({Math.round(rec.lastCorrect / rec.reviewCount * 100)}%)</span>
          )}
          {rec.lastReviewAt && <span>🕐 上次：{formatDateTime(rec.lastReviewAt)}</span>}
        </div>

        {reaction.note && (
          <div style={{
            background: '#fff8ed',
            border: '1px solid #ffe0a0',
            borderRadius: '8px',
            padding: '8px 12px',
            fontSize: '13px',
            color: '#8a6d00',
            marginBottom: '14px',
          }}>
            💡 {reaction.note}
          </div>
        )}

        <div className="detail-actions">
          <button
            className="btn-know"
            onClick={() => handleMark(true)}
            style={{ flex: 1, border: 'none', borderRadius: '20px', padding: '10px 0', fontSize: '15px', fontFamily: 'var(--font)', cursor: 'pointer', fontWeight: 500 }}
          >
            ✅ 会了
          </button>
          <button
            className="btn-not-know"
            onClick={() => handleMark(false)}
            style={{ flex: 1, border: 'none', borderRadius: '20px', padding: '10px 0', fontSize: '15px', fontFamily: 'var(--font)', cursor: 'pointer', fontWeight: 500 }}
          >
            ❌ 不会
          </button>
        </div>

        {showResult && (
          <div style={{
            textAlign: 'center',
            padding: '8px',
            borderRadius: '8px',
            fontSize: '14px',
            fontWeight: 600,
            background: lastResult ? '#e8f5e9' : '#ffebee',
            color: lastResult ? 'var(--success)' : 'var(--danger)',
            marginTop: '8px',
            transition: 'opacity 0.3s',
          }}>
            {lastResult ? '✅ 已记录：这次会了！' : '❌ 已记录：这次不会，继续复习！'}
          </div>
        )}
      </div>

      <div className="section-title">
        <span>📜 复习记录</span>
        <span className="count">共 {reactionHistory.length} 条</span>
      </div>
      <ReactionHistory history={reactionHistory} compact={false} />
    </div>
  );
}
