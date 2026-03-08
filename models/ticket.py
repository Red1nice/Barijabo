from database import db

class Ticket(db.Model):

    id=db.Column(db.Integer,primary_key=True)

    title=db.Column(db.String(200))

    transport_type=db.Column(db.String(20))

    seat=db.Column(db.String(10))

    price=db.Column(db.Float)

    pnr=db.Column(db.String(50))

    featured=db.Column(db.Boolean,default=False)

    seller_id=db.Column(db.Integer)
