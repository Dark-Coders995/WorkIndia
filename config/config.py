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
    SQLITE_DB_DIR = os.path.join(curr_dir, '../database')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, 'grocery.db')
    DEBUG = True
    SECRET_KEY = 'Ayush23435' 
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'grocery@store35243'  
    JWT_SECRET_KEY = 'Ayush23435'