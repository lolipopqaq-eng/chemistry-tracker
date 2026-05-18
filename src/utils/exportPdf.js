import { jsPDF } from 'jspdf';
import 'jspdf-autotable';

export function exportWrongReactionsPDF(records, reactions, textbookData) {
  const doc = new jsPDF('p', 'mm', 'a4');

  // 标题
  doc.setFontSize(18);
  doc.text('化学复习 - 错题集', 105, 20, { align: 'center' });

  doc.setFontSize(10);
  doc.text(`导出时间：${new Date().toLocaleString('zh-CN')}`, 105, 28, { align: 'center' });

  // 统计
  const wrong = Object.entries(records).filter(([id, rec]) => {
    return rec.reviewCount > 0 && rec.lastCorrect / rec.reviewCount < 0.7;
  });

  doc.setFontSize(11);
  doc.text(`总复习反应：${Object.keys(records).length} 个`, 14, 38);
  doc.text(`错误率>30%：${wrong.length} 个`, 14, 44);

  let y = 52;

  wrong.forEach(([id, rec], idx) => {
    const r = reactions.find(rr => rr.id === id);
    if (!r) return;

    // 检查是否需要换页
    if (y > 260) {
      doc.addPage();
      y = 20;
    }

    // 题号
    doc.setFontSize(11);
    doc.setFont('Helvetica', 'bold');
    doc.text(`${idx + 1}. ${r.name}`, 14, y);
    y += 6;

    // 方程
    doc.setFontSize(10);
    doc.setFont('Helvetica', 'normal');
    const eqText = `  方程式：${r.equation || '(未显示)'}`;
    doc.text(eqText, 14, y);
    y += 5;

    // 所属章/物质
    const chName = r.chapterName || '';
    const subName = r.substanceName || '';
    doc.setFontSize(9);
    doc.setTextColor(100);
    doc.text(`  ${chName} - ${subName}`, 14, y);
    y += 4;

    // 复习情况
    const rate = Math.round(rec.lastCorrect / rec.reviewCount * 100);
    doc.text(`  复习 ${rec.reviewCount} 次 · 正确率 ${rate}%`, 14, y);
    y += 4;

    // 现象/提示
    if (r.phenomenon) {
      doc.text(`  现象：${r.phenomenon}`, 14, y);
      y += 4;
    }

    doc.setTextColor(0);
    y += 4;
  });

  // 页脚
  const pageCount = doc.internal.getNumberOfPages();
  for (let i = 1; i <= pageCount; i++) {
    doc.setPage(i);
    doc.setFontSize(8);
    doc.setTextColor(150);
    doc.text(`化学复习错题集 - 第 ${i} / ${pageCount} 页`, 105, 290, { align: 'center' });
  }

  doc.save('化学错题集.pdf');
}
