export function getMasteryLevel(reviewCount, lastCorrect) {
  if (reviewCount === 0) return { level: 0, label: '未复习', cls: 'level-none' };
  const correctRate = lastCorrect / reviewCount;
  if (correctRate >= 0.9 && reviewCount >= 3) return { level: 4, label: '已掌握 ✅', cls: 'level-mastered' };
  if (correctRate >= 0.7 && reviewCount >= 2) return { level: 3, label: '较熟悉 👍', cls: 'level-good' };
  if (correctRate >= 0.4) return { level: 2, label: '还需复习 🔄', cls: 'level-ok' };
  return { level: 1, label: '薄弱 😰', cls: 'level-weak' };
}
