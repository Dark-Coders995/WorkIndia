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

    fs_uniquifier = db.Column(db.String(255), unique=True , nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'))
    role = db.relationship('Role', backref=db.backref('users', lazy=True))
    def __repr__(self):
        return f"User( id = {self.id}, user_name = '{self.user_name}', email = '{self.email}')"
    
class Role(db.Model, RoleMixin):
    __tablename__ = 'Role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True , nullable=False)
    description = db.Column(db.String(255), nullable=False)
    def __repr__(self):
        return f"Role( id = {self.id}, name = '{self.name}', description = '{self.description}')"
    
class Train(db.Model):
    __tablename__ = "Train"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    from_station = db.Column(db.String(150), nullable=False)
    to_station = db.Column(db.String(150), nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)

class Booking(db.Model):
    __tablename__ = "Booking" 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    train_id = db.Column(db.Integer, db.ForeignKey('Train.id'), nullable=False)
    booking_time = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('bookings', lazy=True))
    train = db.relationship('Train', backref=db.backref('bookings', lazy=True))
    