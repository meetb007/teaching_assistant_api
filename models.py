from app import db


class TA(db.Model):
    __tablename__ = 'TA'
    id = db.Column(db.Integer, primary_key=True)
    native_english_speaker = db.Column(db.Integer, nullable=False)
    course_instructor = db.Column(db.Integer, nullable=False)
    course = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    class_size = db.Column(db.Integer, nullable=False)
    performance_score = db.Column(db.Integer, nullable=False)

    def __init__(self, native_english_speaker, course_instructor, course,
                 semester, class_size, performance_score):
        self.native_english_speaker = native_english_speaker
        self.course_instructor = course_instructor
        self.course = course
        self.semester = semester
        self.class_size = class_size
        self.performance_score = performance_score
