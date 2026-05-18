import { useState, useMemo, useRef } from 'react';
import TeacherCard from './components/TeacherCard';
import Sidebar from './components/Sidebar';
import { useChemTracker } from './hooks/useChemTracker';
import TEXTBOOK, { flattenReactions } from './utils/textbook';
import { STORAGE_KEYS, saveToStorage } from './utils/storage';
import Stats from './components/Stats';
import ReactionCard from './components/ReactionCard';
import KnowledgeCard from './components/KnowledgeCard';
import ReactionDetail from './components/ReactionDetail';
import ReactionHistory from './components/ReactionHistory';
import ConfirmModal from './components/ConfirmModal';
import './styles/app.css';

// 展平所有反应


export default function App() {
  const { records, history, stats, markResult, resetAll } = useChemTracker();

  const [activeChapter, setActiveChapter] = useState('ch2'); // 默认第二章
  const [activeSection, setActiveSection] = useState(null);
  const [activeSubstance, setActiveSubstance] = useState(null);
  const [detailReaction, setDetailReaction] = useState(null);
  const [confirmReset, setConfirmReset] = useState(false);
  const [importError, setImportError] = useState(null);
  const fileInputRef = useRef(null);

  const currentChapter = TEXTBOOK.chapters.find(ch => ch.id === activeChapter);

  // 选中的物质和它的反应
  const currentReactions = useMemo(() => {
    if (!currentChapter) return [];
    if (activeSubstance) {
      for (const sec of currentChapter.sections) {
        for (const sub of sec.substances) {
          if (sub.id === activeSubstance) {
            return sub.reactions.map(r => ({
              ...r,
              substanceId: sub.id,
              substanceName: sub.name,
              substanceIcon: sub.icon,
            }));
          }
        }
      }
    }
    return [];
  }, [currentChapter, activeSubstance]);

  const ALL_REACTIONS = useMemo(() => flattenReactions(TEXTBOOK), []);

  // 点击某个物质
  const handleSubstanceClick = (subId) => {
    setActiveSubstance(subId);
    setDetailReaction(null);
  };

  // 返回物质列表
  const handleBackToList = () => {
    setActiveSubstance(null);
    setDetailReaction(null);
  };

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

  // Detail view of a reaction
  if (detailReaction) {
    return (
      <>
        <ReactionDetail
          reaction={detailReaction}
          record={records[detailReaction.id]}
          history={history}
          onBack={() => setDetailReaction(null)}
          onMarkResult={(id, correct) => markResult(id, correct)}
        />

      </>
    );
  }

  return (
    <div className="app">
      <Sidebar />
      <header className="header">
        <TeacherCard />
        <h1>🧪 高考化学·必修第一册</h1>
        <div className="subtitle">按教材框架 · 逐物质攻克高考反应 · 共 {ALL_REACTIONS.length} 个反应</div>
      </header>

      <Stats stats={stats} />

      {/* 章切换 - 树状图 */}
      <div className="tree-view">
        {TEXTBOOK.chapters.filter(ch => ch.id === 'ch2').map(ch => (
          <div key={ch.id} className="tree-chapter">
            <div className="tree-chapter-title">{ch.name}</div>
            {ch.sections.map(sec => (
              <div key={sec.id} className="tree-section">
                <div className="tree-section-title">{sec.name}</div>
                {sec.substances.map(sub => {
                  const rxnCnt = sub.reactions.length;
                  const knowCnt = sub.knowledge ? sub.knowledge.length : 0;
                  return (
                    <div key={sub.id} className="tree-substance" onClick={() => handleSubstanceClick(sub.id)}>
                      <span className="tree-icon">{sub.icon}</span>
                      <span className="tree-name">{sub.name}</span>
                      <span className="tree-badge">
                        {rxnCnt > 0 && `📝${rxnCnt}`}
                        {knowCnt > 0 && ` 📖${knowCnt}`}
                      </span>
                    </div>
                  );
                })}
              </div>
            ))}
          </div>
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
      ) : (
        /* 某个物质的反应列表页 */
        <>
          <button className="back-btn" onClick={handleBackToList}>← 返回</button>

          {(() => {
            const sub = (() => {
              for (const sec of currentChapter.sections) {
                for (const s of sec.substances) {
                  if (s.id === activeSubstance) return { ...s, sectionName: sec.name };
                }
              }
              return null;
            })();
            return sub && (
              <div className="substance-header">
                <span className="substance-icon-large">{sub.icon}</span>
                <div>
                  <div className="substance-name-large">{sub.name}</div>
                  <div className="substance-meta">{sub.sectionName}</div>
                  {sub.note && <div className="substance-desc">{sub.note}</div>}
                </div>
              </div>
            );
          })()}

          {(() => {
            const sub = (() => {
              for (const sec of currentChapter.sections) {
                for (const s of sec.substances) {
                  if (s.id === activeSubstance) return s;
                }
              }
              return null;
            })();
            return sub && sub.knowledge && sub.knowledge.length > 0 ? (
              <KnowledgeCard knowledge={sub.knowledge} />
            ) : null;
          })()}

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

          {/* 按 category 分组 */}
          {(() => {
            const groups = {};
            currentReactions.forEach(r => {
              const cat = r.category || '其他';
              if (!groups[cat]) groups[cat] = [];
              groups[cat].push(r);
            });
            return Object.entries(groups).map(([cat, reactions]) => (
              <div key={cat} className="section-block">
                <div className="section-title">
                  <span>{cat}</span>
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
            ));
          })()}
        </>
      )}



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
