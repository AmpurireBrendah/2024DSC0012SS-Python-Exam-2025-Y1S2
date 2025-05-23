from app.extensions import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(100),nullabe=False)
    address= db.Coolumn(db.String(100),nullabe=False)
    email= db.Column(db.String(100),nullabe=False,unique=True)
    gender= db.Column(db.String(50),nullable=False)
    contact= db.Column(db.String(100),nullabe=False)
    program_id= db.Column(db.Integer,db.ForeignKey('programs.id'))
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "address":self.address,
            "gender":self.gender,
            "email":self.email,
            "contact":self.contact,
            "program_id":self.program_id,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }