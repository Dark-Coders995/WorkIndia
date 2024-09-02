import os

curr_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    WTF_CSRF_ENABLED = False


class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/flask_db'
    DEBUG = True
    SECRET_KEY = 'Irtc23435' 
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'irctc@book35243'  
    JWT_SECRET_KEY = 'Irtct23435'