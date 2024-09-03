
from flask import jsonify, request
from flask_restful import Resource
from models.models import *
from models.database import db
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from API.Authentication.LoginAPI import *

class CheckAvailability(Resource):
    @jwt_required
    @user_required
    def get (self , source  , destination):

        if not source or not destination :
            return jsonify({'message': 'Missing required parameters: from_station and to_station'}), 400
        trains = Train.query.filter_by(from_station=source, to_station=destination).all()
        if not trains:
            return jsonify({'message': 'No trains found for the specified route'}), 404


        trains_data = [
            {
                'id': train.id,
                'name': train.name,
                'from_station': train.from_station,
                'to_station': train.to_station,
                'available_seats': train.available_seats
            }
            for train in trains
        ]

        return jsonify(trains_data)