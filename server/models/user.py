# from flask import g
from wtforms.validators import Email, Regexp
from flask_security import RoleMixin, UserMixin
from flask_security.utils import hash_password
from server.models.base import Base
from server.app import db, app
import pdb

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
        return '<Role %r -- %r>' % (self.name, self.description)


class User(Base, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, info={'validators': Email()})
    password = db.Column(db.String(225), nullable=False,
                         info={'validators': Regexp(regex=r'((?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20})',
                                                    message='Invalid Password Format')})
    active = db.Column(db.Boolean())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(20))
    current_login_ip = db.Column(db.String(20))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, *mixed, **kwargs):
        super(User, self).__init__(*mixed, **kwargs)
        with app.app_context():
            self.password = hash_password(kwargs['password'])

    def __repr__(self):
        return '<User %r>' % self.email
