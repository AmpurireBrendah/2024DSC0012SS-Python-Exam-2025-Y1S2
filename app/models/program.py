from app.extensions import db
from datetime import datetime

class Program(db.Model):
    __tablename__ = 'programs'
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(100),nullabe=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())

    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "start_date":self.start_date,
            "end_date":self.end_date,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }