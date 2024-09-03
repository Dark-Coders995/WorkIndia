import jwt
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_security import login_user
from flask_security.utils import verify_password
from config.validation import *
from models.models import User, Train
from models.database import db
from config.security import user_datastore
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from API.Authentication.AdminLogin import *

class AddTrain(Resource):
    @jwt_required
    @admin_required
    def post(self):
        data = request.get_json()
        source = data.get('source')
        destination = data.get('destination')
        train_name = data.get('name')
        total_seats = data.get('seats')
        new_train = Train(name=train_name, 
                          from_station=source, 
                          to_station=destination, 
                          total_seats=total_seats, 
                          available_seats=total_seats)
        db.session.add(new_train)
        db.session.commit()
        return {'message': 'Train added successfully'}, 201