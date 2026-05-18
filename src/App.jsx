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
  const [openSections, setOpenSections] = useState({});
  const [searchText, setSearchText] = useState('');

  const toggleSection = (secId) => {
    setOpenSections(prev => ({ ...prev, [secId]: !prev[secId] }));
  };

  // 搜索过滤
  const filteredChapters = useMemo(() => {
    if (!searchText.trim()) return TEXTBOOK.chapters;
    const q = searchText.trim().toLowerCase();
    return TEXTBOOK.chapters.map(ch => {
      const matchedSections = ch.sections.map(sec => {
        const matchedSubs = sec.substances.filter(sub => 
          sub.name.toLowerCase().includes(q) ||
          sub.reactions.some(r => r.name.toLowerCase().includes(q)) ||
          sub.knowledge?.some(k => k.q.includes(q))
        );
        return { ...sec, substances: matchedSubs };
      }).filter(sec => sec.substances.length > 0);
      return { ...ch, sections: matchedSections };
    }).filter(ch => ch.sections.length > 0);
  }, [searchText]);
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
      {/* 左侧导航栏 */}
      <nav className="side-nav">
        <div className="side-nav-header">
          <div className="side-nav-logo">🧪</div>
          <div className="side-nav-title">高考化学</div>
        </div>
        <div className="side-nav-chapters">
          {TEXTBOOK.chapters.map(ch => (
            <div
              key={ch.id}
              className={`side-nav-item ${activeChapter === ch.id ? 'active' : ''}`}
              onClick={() => { setActiveChapter(ch.id); setActiveSubstance(null); }}
            >
              <span className="side-nav-ch-name">
                {ch.name.replace(/^第.+? /, '')}
              </span>
              <span className="side-nav-ch-count">
                {ch.sections.reduce((a,s) => a + s.substances.reduce((b,sub) => b + sub.reactions.length, 0), 0)}
              </span>
            </div>
          ))}
        </div>
        <div className="side-nav-footer">
          <Sidebar />
        </div>
      </nav>

      {/* 主内容区 */}
      <main className="main-content">
        {/* 顶部栏 */}
        <div className="top-bar">
          <div className="top-bar-left">
            <TeacherCard />
          </div>
          <div className="top-bar-right">
            <div className="search-box">
              <input
                type="text"
                placeholder="搜索物质、反应…"
                value={searchText}
                onChange={e => setSearchText(e.target.value)}
              />
            </div>
            <div className="top-bar-actions">
              <button className="btn-icon" onClick={handleExport} title="导出">💾</button>
              <button className="btn-icon" onClick={() => fileInputRef.current?.click()} title="导入">📂</button>
              <input ref={fileInputRef} type="file" accept=".json" onChange={handleImport} style={{ display: 'none' }} />
            </div>
          </div>
        </div>

        <Stats stats={stats} />

        {importError && (
          <div className="import-error">
            ❌ {importError}
          </div>
        )}

        {!activeSubstance ? (
          /* 首页 - 当前章的物质网格 */
          <>
            <div className="content-header">
              <h2>{currentChapter?.name || ''}</h2>
              <span className="content-count">
                共 {currentChapter?.sections.reduce((a,s) => a + s.substances.length, 0) || 0} 个物质
                · {ALL_REACTIONS.length} 个反应
              </span>
            </div>

            {currentChapter?.sections.map(sec => {
              const isSecOpen = openSections[sec.id] ?? true;
              return (
                <div key={sec.id} className="content-section">
                  <div className="content-section-header" onClick={() => toggleSection(sec.id)}>
                    <span className={`fold-arrow ${isSecOpen ? 'open' : ''}`}>▶</span>
                    {sec.name}
                    <span className="content-section-count">
                      {sec.substances.length} 物质
                    </span>
                  </div>
                  {isSecOpen && (
                    <div className="substance-grid">
                      {sec.substances.map(sub => (
                        <div key={sub.id} className="substance-card" onClick={() => handleSubstanceClick(sub.id)}>
                          <div className="substance-icon">{sub.icon}</div>
                          <div className="substance-name">{sub.name}</div>
                          <div className="substance-count">
                            {sub.reactions.length > 0 && `📝${sub.reactions.length}`}
                            {sub.knowledge && sub.knowledge.length > 0 && ` 📖${sub.knowledge.length}`}
                          </div>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              );
            })}

            <div className="content-header" style={{marginTop:'24px'}}>
              <span>📜 全部复习记录</span>
              <span className="content-count">共 {history.length} 条</span>
            </div>
            <ReactionHistory history={history} compact={false} />

            <button className="btn-reset-bottom" onClick={() => setConfirmReset(true)}>重置所有数据</button>
          </>
        ) : (
          /* 物质详情 - 反应列表页 */
          <>
            <button className="back-btn" onClick={handleBackToList}>← 返回 {currentChapter?.name?.replace(/^第.+? /, '') || ''}</button>

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

            {/* 按 category 分组 */}
            {(() => {
              const groups = {};
              currentReactions.forEach(r => {
                const cat = r.category || '其他';
                if (!groups[cat]) groups[cat] = [];
                groups[cat].push(r);
              });
              return Object.entries(groups).map(([cat, reactions]) => (
                <div key={cat} className="content-section">
                  <div className="content-section-header" style={{cursor:'default'}}>
                    {cat}
                    <span className="content-section-count">{reactions.length} 个反应</span>
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
      </main>

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
