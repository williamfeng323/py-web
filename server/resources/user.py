from server.models.user import User
from server.app import auth, db

from flask_restful import Resource, reqparse, marshal_with, fields
import re
from functools import reduce


def email(email_str):
    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    if not EMAIL_REGEX.match(email_str):
        raise ValueError('Email is incorrect')
    else:
        return True

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'roles': fields.String,
    'date_created': fields.DateTime,
    'date_updated': fields.DateTime,
}
post_parser = reqparse.RequestParser()
post_parser.add_argument('email', required=True, type=email, help='missing email')
post_parser.add_argument('password', required=True, help='missing password')


class UserResource(Resource):
    @auth.login_required
    @marshal_with(user_fields)
    def get(self):
        args = post_parser.parse_args()
        return User.query.filter_by(email=args['email']).first()

    @marshal_with(user_fields)
    def post(self):
        args = post_parser.parse_args()
        if not reduce(lambda x,y: x in ['email', 'password'] and y in ['email', 'password'], args.keys()):
            return 'missing parameters', 404
        else:
            user = User(args.email.data, args.password.data)
            db.session.add(user)
            db.session.commit()
            return user, 201

    def put(self):
        pass

    def delete(self):
        pass