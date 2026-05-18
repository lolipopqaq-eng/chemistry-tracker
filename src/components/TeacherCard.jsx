export default function TeacherCard() {
  return (
    <div className="teacher-card-top">
      <img src="/teacher-photo.jpg" alt="冯老师" className="teacher-photo" />
      <div className="teacher-info">
        <div className="teacher-name">冯老师</div>
        <div className="teacher-desc">高考化学 · 系统复习</div>
        <div className="teacher-contact">
          <span>📞 <a href="tel:16655125178">16655125178</a></span>
          <span>💬 微信：FengWei-ontheway</span>
        </div>
      </div>
    </div>
  );
}
