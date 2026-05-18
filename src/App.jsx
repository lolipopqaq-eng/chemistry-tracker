import { useState, useMemo, useRef } from 'react';
import { useChemTracker } from './hooks/useChemTracker';
import { REACTIONS } from './utils/reactions';
import { NA2CO3_REACTIONS, NAHCO3_REACTIONS } from './utils/carbonate';
import { STORAGE_KEYS, saveToStorage } from './utils/storage';
import Stats from './components/Stats';
import ReactionCard from './components/ReactionCard';
import ReactionDetail from './components/ReactionDetail';
import ReactionHistory from './components/ReactionHistory';
import ConfirmModal from './components/ConfirmModal';
import './styles/app.css';

const GROUPS = [
  { key: 'naoh', label: '🧪 NaOH 氢氧化钠', reactions: REACTIONS },
  { key: 'na2co3', label: '🧂 Na₂CO₃ 碳酸钠', reactions: NA2CO3_REACTIONS },
  { key: 'nahco3', label: '🥤 NaHCO₃ 碳酸氢钠', reactions: NAHCO3_REACTIONS },
];

export default function App() {
  const { records, history, stats, markResult, resetAll } = useChemTracker();

  const [activeGroup, setActiveGroup] = useState('naoh');
  const [detailReaction, setDetailReaction] = useState(null);
  const [confirmReset, setConfirmReset] = useState(false);
  const [importError, setImportError] = useState(null);
  const fileInputRef = useRef(null);

  const currentGroup = GROUPS.find(g => g.key === activeGroup);
  const currentReactions = currentGroup?.reactions || [];

  // 按 section 分组
  const groupedReactions = useMemo(() => {
    const groups = {};
    currentReactions.forEach(r => {
      const sec = r.section || '其他';
      if (!groups[sec]) groups[sec] = [];
      groups[sec].push(r);
    });
    return groups;
  }, [currentReactions]);

  // 全部反应（用于统计）
  const ALL_REACTIONS = useMemo(
    () => [...REACTIONS, ...NA2CO3_REACTIONS, ...NAHCO3_REACTIONS],
    []
  );

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
    a.download = `化学复习_${new Date().toISOString().slice(0, 10)}.json`;
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
        onMarkResult={(id, correct) => markResult(id, correct)}
      />
    );
  }

  return (
    <div className="app">
      <header className="header">
        <h1>🧪 高考必背反应复习</h1>
        <div className="subtitle">NaOH · Na₂CO₃ · NaHCO₃ 全反应汇总 · 共 {ALL_REACTIONS.length} 个反应</div>
      </header>

      <Stats stats={stats} />

      {/* 三大板块切换标签 */}
      <div className="group-tabs">
        {GROUPS.map(g => (
          <button
            key={g.key}
            className={activeGroup === g.key ? 'active' : ''}
            onClick={() => setActiveGroup(g.key)}
          >
            {g.label}
            <span className="count-badge">{g.reactions.length}</span>
          </button>
        ))}
      </div>

      <div className="toolbar">
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

      {/* 按小分类分组展示 */}
      {Object.entries(groupedReactions).map(([section, reactions]) => (
        <div key={section} className="section-block">
          <div className="section-title">
            <span>{section}</span>
            <span className="count">{reactions.length} 个反应</span>
          </div>
          <div className="reaction-list">
            {reactions.map(r => (
              <ReactionCard
                key={r.id}
                reaction={r}
                record={records[r.id]}
                onClick={(reaction) => setDetailReaction(reaction)}
                onMarkResult={(id, correct) => markResult(id, correct)}
              />
            ))}
          </div>
        </div>
      ))}

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
