from app.extensions import db
from datetime import datetime

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(100),nullabe=False)
    code= db.Column(db.String(100),nullable=False,unique=True)
    duration= db.Column(db.String(100),nullabe=False)
    program_id= db.Column(db.Integer,db.ForeignKey('programs.id'))
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "code":self.code,
            "duration":self.duration,
            "program_id":self.program_id,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }