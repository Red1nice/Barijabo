from database import db
from datetime import datetime

class Message(db.Model):

    id=db.Column(db.Integer,primary_key=True)

    sender_id=db.Column(db.Integer)

    receiver_id=db.Column(db.Integer)

    text=db.Column(db.Text)

    time=db.Column(db.DateTime,default=datetime.utcnow)
