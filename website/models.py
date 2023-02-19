from . import db
from flask_login import UserMixin


class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.Date)
    language = db.Column(db.String(35))
    interval = db.Column(db.Integer)
    stars = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    data = db.Column(db.String(400))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    jmeno = db.Column(db.String(40))
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(40))
    role = db.Column(db.String(15))
    password = db.Column(db.String(100))
    notes = db.relationship("Note")