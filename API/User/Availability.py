
from flask import jsonify, request
from flask_restful import Resource
from models.models import *
from models.database import db
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from API.Authentication.LoginAPI import *

check_train = reqparse.RequestParser()
check_train.add_argument("from_station")
check_train.add_argument("to_station")

class CheckAvailability(Resource):
    @jwt_required
    @user_required
    def get(self):
        args = check_train.parse_args()
        from_station = args.get('from_station')
        to_station = args.get('to_station')

        if not from_station or not to_station:
            return jsonify({'message': 'Missing required parameters: from_station and to_station'}), 400
        trains = Train.query.filter_by(from_station=from_station, to_station=to_station).all()

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
2