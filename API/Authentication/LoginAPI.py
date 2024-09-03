import jwt
from functools import wraps
from flask import jsonify
from flask_restful import Resource, reqparse
from flask_security import login_user
from flask_security.utils import verify_password
from config.validation import *
from models.models import User
from models.database import db
from config.security import user_datastore
from flask import request

from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity, verify_jwt_in_request
from datetime import timedelta


class LoginAPI(Resource):
	def post(self):
		data = request.get_json()
		username = data.get('username')
		password = data.get('password')
		user = None
		if '@' in username:
			user = db.session.query(User).filter(User.email == username).first()
		else:
			user = db.session.query(User).filter(User.username == username).first()
		
		if user:
			if not user.is_admin :

				if verify_password(password, user.password):

					access_token = create_access_token(identity=user.id, expires_delta=timedelta(seconds=1200))
					login_user(user)
				else:
					raise BusinessValidationError(status_code=404, error_code="BE102", error_message="Incorrect password!")
			else:
				raise BusinessValidationError(status_code=404, error_code="BE102", error_message="Only users are allowed!")
		else:
			raise BusinessValidationError(status_code=404, error_code="BE101", error_message="User not found!")
		
		return jsonify({'status': 'success','message': 'loggin Successfull !!', 'access_token': access_token, "username": username})
	

def user_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        verify_jwt_in_request()  

        user_id = get_jwt_identity() 
        user = User.query.get(user_id) 

        if not user or user.is_admin:
            return jsonify(message="User required"), 403

        return func(*args, **kwargs)

    return decorated_function