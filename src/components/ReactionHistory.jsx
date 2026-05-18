import { formatDateTime } from '../utils/storage';

export default function ReactionHistory({ history, compact }) {
  if (history.length === 0) {
    return <div className="empty-state" style={compact ? { padding: '16px 0', fontSize: '13px' } : {}}>暂无复习记录 📝</div>;
  }

  return (
    <div className="history-list">
      {history.map(h => (
        <div key={h.id} className="history-item">
          <div className="left">
            {!compact && <span style={{ fontWeight: 500 }}>{h.reactionName}</span>}
            <span className={h.correct ? 'res-correct' : 'res-wrong'}>
              {h.correct ? '✅ 会了' : '❌ 不会'}
            </span>
          </div>
          <span className="time">{formatDateTime(h.reviewedAt)}</span>
        </div>
      ))}
    </div>
  );
}
