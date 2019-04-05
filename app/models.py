from datetime import datetime

<<<<<<< HEAD
from app import db

class Tweet(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(280))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Tweet #{self.id}>"
=======
class Tweet:
    def __init__(self, text):
        self.id = None
        self.text = text
        self.created_at = datetime.now()
>>>>>>> df1b6b8718bfc5762252663c6cefef16e49a6ef1
