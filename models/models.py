from flask_security import UserMixin, RoleMixin
from models.database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from werkzeug.security import generate_password_hash, check_password_hash


import datetime
from datetime import datetime
from pytz import timezone

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True , nullable=False)
    email = db.Column(db.String(255), unique=True , nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean)
    cart = db.relationship('Cart', backref='User', lazy=True)

    fs_uniquifier = db.Column(db.String(255), unique=True , nullable=False)
    def __repr__(self):
        return f"User( id = {self.id}, user_name = '{self.user_name}', email = '{self.email}')"
    
class Role(db.Model, RoleMixin):
    __tablename__ = 'Role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True , nullable=False)
    description = db.Column(db.String(255), nullable=False)
    def __repr__(self):
        return f"Role( id = {self.id}, name = '{self.name}', description = '{self.description}')"
    