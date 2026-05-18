import rawData from '../data/textbook-data.json';

const TEXTBOOK = {
  name: '人教版化学（五册）',
  chapters: rawData,
};

// 辅助函数：展平所有反应（含所在章节/物质信息）
export function flattenReactions(tb) {
  const all = [];
  tb.chapters.forEach(ch => {
    ch.sections.forEach(sec => {
      sec.substances.forEach(sub => {
        sub.reactions.forEach(r => {
          all.push({
            ...r,
            substanceId: sub.id,
            substanceName: sub.name,
            substanceIcon: sub.icon,
            substanceNote: sub.note,
            sectionId: sec.id,
            sectionName: sec.name,
            chapterId: ch.id,
            chapterName: ch.name,
          });
        });
      });
    });
  });
  return all;
}

export default TEXTBOOK;
export { TEXTBOOK };
