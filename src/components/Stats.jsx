export default function Stats({ stats }) {
  const items = [
    { key: 'total', label: '总反应', value: stats.total, cls: 'primary' },
    { key: 'reviewed', label: '已复习', value: stats.reviewed, cls: 'success' },
    { key: 'mastered', label: '已掌握', value: stats.mastered, cls: 'success' },
    { key: 'weak', label: '还薄弱', value: stats.weak, cls: 'danger' },
    { key: 'notReviewed', label: '未复习', value: stats.notReviewed, cls: 'warning' },
    { key: 'todayReviewCount', label: '今日复习', value: stats.todayReviewCount, cls: 'primary' },
  ];

  return (
    <div className="stats" style={{ gridTemplateColumns: 'repeat(3, 1fr)' }}>
      {items.map(item => (
        <div key={item.key} className={`stat-card ${item.cls}`}>
          <div className="number">{item.value}</div>
          <div className="label">{item.label}</div>
        </div>
      ))}
    </div>
  );
}
