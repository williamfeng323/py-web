import os
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../')


class Config(object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://' + os.environ['DATABASE_USER']+':' + os.environ['DATABASE_PASSWORD'] \
                              + os.environ['DATABASE_URL']


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