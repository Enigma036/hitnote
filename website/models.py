from . import db


class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Date)
    language = db.Column(db.String(20))
    interval = db.Column(db.Integer)
    stars = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    data = db.Column(db.String(300))

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    jmeno = db.Column(db.String(30), unique=True)
    notes = db.relationship("Note")
    