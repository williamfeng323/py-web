# from flask import g
from wtforms.validators import Email
from flask_security import RoleMixin, UserMixin
from server.models.base import Base
from server.app import db, flaskBcrypt

roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(Base, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name, desc):
        self.name = name
        self.description = desc

    def __repr__(self):
        return '<Role %r -- %r>' % self.name


class User(Base, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, info={'validators': Email()})
    password_digest = db.Column(db.String(12), nullable=False)
    active = db.Column(db.Boolean, default=True)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, email, password):
        self.email = email
        self.password = flaskBcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<User %r>' % self.email
