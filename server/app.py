import os
from flask import Flask
# import flask_restful as restful
from flask_restful import reqparse, Api
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt
# from flask_assets import YAMLLoader, Environment


basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')

app = Flask(__name__)
app.config.from_object('server.configuration.config')
# Initial Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)
# Restful Api
api = Api(app)
# Encryption
flaskBcrypt = Bcrypt(app)
# HTTP authentication
auth = HTTPBasicAuth()

# Assets loader
# loader = YAMLLoader('app/config/asset_config.yml')
# env = loader.load_environment()
# asset = Environment(app)
#
# asset.register('vendor-css', env['vendor-css'])
# asset.register('vendor-js', env['vendor-js'])

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


from server.resources.user import UserResource
api.add_resource(UserResource, '/users')

