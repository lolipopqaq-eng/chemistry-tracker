import { useState } from 'react';
import teacherPhoto from '../assets/teacher-photo.png';

export default function TeacherCard() {
  const [showBig, setShowBig] = useState(false);

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
            <span>📞 <a href="tel:16655125178">16655125178</a></span>
            <span>💬 微信：FengWei-ontheway</span>
          </div>
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
