import { useState, useEffect, useCallback, useRef } from 'react';
import { STORAGE_KEYS, loadFromStorage, saveToStorage, generateId } from '../utils/storage';
import { REACTIONS } from '../utils/reactions';

export function useChemTracker() {
  const [records, setRecords] = useState({});       // reactionId -> { reviewCount, lastCorrect, lastReviewAt }
  const [history, setHistory] = useState([]);
  const [initialized, setInitialized] = useState(false);
  const reactionsRef = useRef(REACTIONS);

  useEffect(() => {
    const savedRecords = loadFromStorage(STORAGE_KEYS.PROGRESS, {});
    const savedHistory = loadFromStorage(STORAGE_KEYS.HISTORY, []);
    setRecords(savedRecords);
    setHistory(Array.isArray(savedHistory) ? savedHistory : []);
    setInitialized(true);
  }, []);

  useEffect(() => {
    if (initialized) saveToStorage(STORAGE_KEYS.PROGRESS, records);
  }, [records, initialized]);

  useEffect(() => {
    if (initialized) saveToStorage(STORAGE_KEYS.HISTORY, history);
  }, [history, initialized]);

  const markResult = useCallback((reactionId, correct) => {
    const now = new Date().toISOString();
    setRecords(prev => {
      const prevRec = prev[reactionId] || { reviewCount: 0, lastCorrect: 0, lastReviewAt: null };
      return {
        ...prev,
        [reactionId]: {
          reviewCount: prevRec.reviewCount + 1,
          lastCorrect: prevRec.lastCorrect + (correct ? 1 : 0),
          lastReviewAt: now,
        },
      };
    });
    setHistory(prev => {
      const reaction = reactionsRef.current.find(r => r.id === reactionId);
      const entry = {
        id: generateId(),
        reactionId,
        reactionName: reaction ? reaction.name : '',
        category: reaction ? reaction.category : '',
        correct,
        reviewedAt: now,
      };
      return [entry, ...prev];
    });
  }, []);

  const resetAll = useCallback(() => {
    setRecords({});
    setHistory([]);
  }, []);

  // Stats
  const stats = (() => {
    const total = REACTIONS.length;
    let reviewed = 0;
    let mastered = 0;
    let weak = 0;
    let notReviewed = 0;
    let todayReviewCount = 0;

    const todayStr = new Date().toISOString().slice(0, 10);
    history.forEach(h => {
      if (h.reviewedAt && h.reviewedAt.startsWith(todayStr)) todayReviewCount++;
    });

    REACTIONS.forEach(r => {
      const rec = records[r.id];
      if (!rec) { notReviewed++; return; }
      reviewed++;
      const rate = rec.lastCorrect / rec.reviewCount;
      if (rate >= 0.9 && rec.reviewCount >= 3) mastered++;
      if (rate < 0.5) weak++;
    });

    return { total, reviewed, mastered, weak, notReviewed, todayReviewCount };
  })();

  return {
    records,
    history,
    initialized,
    stats,
    markResult,
    resetAll,
  };
}
