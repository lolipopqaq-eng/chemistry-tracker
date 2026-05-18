import { useState } from 'react';
import teacherPhoto from '../assets/teacher-photo.png';

export default function TeacherCard() {
  const [showBig, setShowBig] = useState(false);
  const [copied, setCopied] = useState('');

  const copy = (text, label) => {
    navigator.clipboard.writeText(text).then(() => {
      setCopied(label);
      setTimeout(() => setCopied(''), 1500);
    });
  };

  return (
    <>
      <div className="teacher-card-top">
        <img
          src={teacherPhoto}
          alt="冯老师"
          className="teacher-photo"
          onClick={() => setShowBig(true)}
          style={{ cursor: 'pointer' }}
        />
        <div className="teacher-info">
          <div className="teacher-name">冯老师</div>
          <div className="teacher-desc">高中数学 · 系统复习</div>
          <div className="teacher-contact">
            <span>📞 <a href="tel:16655125178" onClick={(e) => { e.preventDefault(); copy('16655125178', '电话'); }}>16655125178</a></span>
            <span>💬 <a href="weixin://FengWei-ontheway" onClick={(e) => { e.preventDefault(); copy('FengWei-ontheway', '微信号'); }}>FengWei-ontheway</a></span>
          </div>
          {copied && <div className="copy-tip">✅ {copied}已复制</div>}
        </div>
      </div>

      {showBig && (
        <div className="photo-overlay" onClick={() => setShowBig(false)}>
          <img src={teacherPhoto} alt="冯老师" className="photo-big" />
          <div className="photo-close">点击任意位置关闭</div>
        </div>
      )}
    </>
  );
}
