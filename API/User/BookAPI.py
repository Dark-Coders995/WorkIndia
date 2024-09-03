
from flask import jsonify, request
from flask_restful import Resource
from models.models import *
from models.database import db
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from API.Authentication.LoginAPI import *
import threading

class BookingDetailsAPI(Resource):
    @jwt_required()
    @user_required
    def get(self, booking_id):
        user_id = get_jwt_identity()
        booking = Booking.query.filter_by(id=booking_id, user_id=user_id).first_or_404()
        train = Train.query.get_or_404(booking.train_id)
        if booking:
            booking_data = {
                'id': booking.id,
                'train_name': train.name,
                'from_station': train.from_station,
                'to_station': train.to_station,
                'booking_time' : booking.booking_time
            }
            return booking_data, 200
        return jsonify({'message': 'Booking not found'}), 404

class AllBookingsAPI(Resource):
    @jwt_required
    @user_required
    def get(self):
        user_id = get_jwt_identity()
        bookings = Booking.query.filter_by(user_id=user_id).all()
        bookings_data = []
        for booking in bookings:
            train = Train.query.get(booking.train_id)
            if train:
                bookings_data.append({
                    'id': booking.id,
                    'train_name': train.name,
                    'from_station': train.from_station,
                    'to_station': train.to_station,
                    'booking_time': booking.booking_time
                })
    
        return jsonify(bookings_data)

class BookTrainAPI(Resource):
    @jwt_required
    @user_required
    def post(self , train_id):
        train = Train.query.get_or_404(train_id)
        user_id = get_jwt_identity
        if train.available_seats > 0:
            lock = threading.Lock()
            with lock:
                if train.available_seats > 0:
                    train.available_seats -= 1
                    booking = Booking(user_id=user_id, train_id=train_id)
                    db.session.add(booking)
                    db.session.commit()
                    response = jsonify({'message': 'Booking successful!', 'booking_id': booking.id})
                    response.status_code = 201
                    return response
                else:
                    return jsonify({'message': 'No seats available.'}), 400
        else:
            return jsonify({'message': 'No seats available.'}), 400
