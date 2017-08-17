import os
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')


class Config(object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + os.environ['DATABASE_USER']+':' + os.environ['DATABASE_PASSWORD'] \
                              + os.environ['DATABASE_URL']
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_SALT = 'get_crazy_when_guess_it'
    SECURITY_UNAUTHORIZED_VIEW = None
    # SECURITY_LOGIN_URL = None

    WTF_CSRF_HEADERS = ['GTA_CSRF_TOKEN']
class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEBUG = False
    DEVELOPMENT = True


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    TESTING = True
    WTF_CSRF_ENABLED = False
