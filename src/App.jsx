import { useState, useMemo, useRef } from 'react';
import { useChemTracker } from './hooks/useChemTracker';
import { REACTIONS, CATEGORIES } from './utils/reactions';
import { STORAGE_KEYS, saveToStorage } from './utils/storage';
import Stats from './components/Stats';
import ReactionCard from './components/ReactionCard';
import ReactionDetail from './components/ReactionDetail';
import ReactionHistory from './components/ReactionHistory';
import ConfirmModal from './components/ConfirmModal';
import './styles/app.css';

export default function App() {
  const { records, history, stats, markResult, resetAll } = useChemTracker();

  const [categoryFilter, setCategoryFilter] = useState('全部');
  const [detailReaction, setDetailReaction] = useState(null);
  const [confirmReset, setConfirmReset] = useState(false);
  const [importError, setImportError] = useState(null);
  const fileInputRef = useRef(null);

  const filteredReactions = useMemo(() => {
    if (categoryFilter === '全部') return REACTIONS;
    return REACTIONS.filter(r => r.category === categoryFilter);
  }, [categoryFilter]);

  // Export
  const handleExport = () => {
    const data = {
      version: 1,
      exportedAt: new Date().toISOString(),
      records,
      history,
    };
    const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    const dateStr = new Date().toISOString().slice(0, 10);
    a.download = `化学复习_NaOH反应_${dateStr}.json`;
    a.click();
    URL.revokeObjectURL(url);
  };

  // Import
  const handleImport = (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setImportError(null);
    const reader = new FileReader();
    reader.onload = (event) => {
      try {
        const data = JSON.parse(event.target.result);
        if (!data.records || !data.history) throw new Error('文件格式不正确');
        saveToStorage(STORAGE_KEYS.PROGRESS, data.records);
        saveToStorage(STORAGE_KEYS.HISTORY, data.history);
        window.location.reload();
      } catch (err) {
        setImportError(err.message || '导入失败');
      }
    };
    reader.readAsText(file);
    e.target.value = '';
  };

  // Detail view
  if (detailReaction) {
    return (
      <ReactionDetail
        reaction={detailReaction}
        record={records[detailReaction.id]}
        history={history}
        onBack={() => setDetailReaction(null)}
        onMarkResult={(id, correct) => {
          markResult(id, correct);
          // refresh record
        }}
      />
    );
  }

  return (
    <div className="app">
      <header className="header">
        <h1>🧪 NaOH 反应方程式复习</h1>
        <div className="subtitle">氢氧化钠全反应汇总 · 高考必背版 · 共 {REACTIONS.length} 个反应</div>
      </header>

      <Stats stats={stats} />

      <div className="toolbar">
        <div className="category-tabs">
          {CATEGORIES.map(c => (
            <button
              key={c}
              className={categoryFilter === c ? 'active' : ''}
              onClick={() => setCategoryFilter(c)}
            >
              {c}
            </button>
          ))}
        </div>
        <div className="toolbar-right">
          <button className="btn-export" onClick={handleExport}>💾 导出</button>
          <button className="btn-export" style={{ background: '#8e8e93' }} onClick={() => fileInputRef.current?.click()}>
            📂 导入
          </button>
          <input ref={fileInputRef} type="file" accept=".json" onChange={handleImport} style={{ display: 'none' }} />
          <button className="btn-reset" onClick={() => setConfirmReset(true)}>重置</button>
        </div>
      </div>

      {importError && (
        <div style={{ background: '#fff5f5', border: '1px solid var(--danger)', borderRadius: 'var(--radius)', padding: '10px 14px', fontSize: '13px', color: 'var(--danger)', marginBottom: '12px' }}>
          ❌ {importError}
        </div>
      )}

      <div className="reaction-list">
        {filteredReactions.map(r => (
          <ReactionCard
            key={r.id}
            reaction={r}
            record={records[r.id]}
            onClick={(reaction) => setDetailReaction(reaction)}
            onMarkResult={(id, correct) => markResult(id, correct)}
          />
        ))}
      </div>

      <div className="section-title">
        <span>📜 全部复习记录</span>
        <span className="count">共 {history.length} 条</span>
      </div>
      <ReactionHistory history={history} compact={false} />

      {confirmReset && (
        <ConfirmModal
          message="确定要重置所有复习数据吗？这会清除所有记录。"
          onConfirm={() => { resetAll(); setConfirmReset(false); }}
          onCancel={() => setConfirmReset(false)}
        />
      )}
    </div>
  );
}
