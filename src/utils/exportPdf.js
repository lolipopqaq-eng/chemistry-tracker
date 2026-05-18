import { jsPDF } from 'jspdf';

// 用 html 方式生成 PDF，支持中文
export function exportWrongReactionsPDF(records, reactions) {
  const wrong = Object.entries(records).filter(([id, rec]) => {
    return rec.reviewCount > 0 && (1 - rec.lastCorrect / rec.reviewCount) > 0.3;
  });

  if (wrong.length === 0) {
    alert('没有错题可导出！继续复习吧 💪');
    return;
  }

  // 建一个隐藏的 div 用来做 PDF 内容
  const div = document.createElement('div');
  div.style.cssText = 'position:absolute;left:-9999px;top:0;width:800px;padding:20px;font-family:SimSun,Microsoft YaHei,sans-serif;';

  let html = `
    <div style="text-align:center;margin-bottom:16px;">
      <h1 style="font-size:22px;margin:0;">化学复习 - 错题集</h1>
      <p style="font-size:12px;color:#666;">导出时间：${new Date().toLocaleString('zh-CN')}</p>
    </div>
    <div style="font-size:13px;margin-bottom:12px;">
      总复习反应：${Object.keys(records).length} 个 · 待复习错题：${wrong.length} 个
    </div>
    <hr style="border:1px solid #ddd;" />
  `;

  wrong.forEach(([id, rec], idx) => {
    const r = reactions.find(rr => rr.id === id);
    if (!r) return;

    const rate = Math.round(rec.lastCorrect / rec.reviewCount * 100);
    const chName = r.chapterName || '';
    const subName = r.substanceName || '';
    const icon = r.substanceIcon || '';

    html += `
      <div style="margin:10px 0;padding:10px 12px;border:1px solid #e0e0e0;border-radius:8px;background:#fafafa;">
        <div style="font-size:14px;font-weight:bold;margin-bottom:4px;">
          ${idx + 1}. ${icon} ${r.name}
        </div>
        <div style="font-size:13px;font-family:'Times New Roman',serif;background:#fff;padding:6px 10px;border-radius:4px;margin:4px 0;border:1px solid #eee;">
          ${r.equation || ''}
        </div>
        <div style="font-size:11px;color:#888;">
          ${chName} - ${subName} · 复习${rec.reviewCount}次 · 正确率${rate}%
        </div>
        ${r.phenomenon ? `<div style="font-size:11px;color:#555;">👁️ ${r.phenomenon}</div>` : ''}
        ${r.note ? `<div style="font-size:11px;color:#e67e22;">💡 ${r.note}</div>` : ''}
      </div>
    `;
  });

  html += `<div style="text-align:center;font-size:10px;color:#aaa;margin-top:20px;">化学复习 - 错题集 PDF 导出</div>`;
  div.innerHTML = html;
  document.body.appendChild(div);

  // 用 window.print 打印为PDF（支持中文）
  const style = document.createElement('style');
  style.textContent = `
    @media print {
      body { margin: 0; padding: 0; }
      @page { margin: 10mm; }
    }
  `;
  document.head.appendChild(style);

  window.print();

  // 清理
  document.head.removeChild(style);
  document.body.removeChild(div);
}
