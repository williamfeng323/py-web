# from flask import g
from wtforms.validators import Email
from server.app import db, flaskBcrypt
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, info={'validators': Email()})
    password = db.Column(db.String(12), nullable=False)
    role = db.Column(db.String(12), nullable=False, default='user')
    date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, email, password):
        self.email = email
        self.password = flaskBcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.email
