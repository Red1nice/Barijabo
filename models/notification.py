from database import db

class Notification(db.Model):

    id=db.Column(db.Integer,primary_key=True)

    user_id=db.Column(db.Integer)

    message=db.Column(db.String(200))

    seen=db.Column(db.Boolean,default=False)
