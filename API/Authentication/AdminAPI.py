import jwt
from functools import wraps
from flask import request, jsonify
from flask_restful import Resource, reqparse
from flask_security import login_user
from flask_security.utils import verify_password
from config.validation import *
from models.models import User
from models.database import db
from config.security import user_datastore
from datetime import timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, verify_jwt_in_request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security.utils import hash_password
import secrets

admin_parser = reqparse.RequestParser()
admin_parser.add_argument('username')
admin_parser.add_argument('password')

class AdminLoginAPI(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        admin = None
        if '@' in username:
            admin = db.session.query(User).filter(User.email == username, User.is_admin==True).first()
        else:
            admin = db.session.query(User).filter(User.username == username, User.is_admin==True).first()

        if admin:
            if verify_password(password, admin.password):
                access_token = create_access_token(identity=admin.id, expires_delta=timedelta(seconds=1200))
                login_user(admin)
            else:
                raise BusinessValidationError(status_code=404, error_code="BE102", error_message="Incorrect password!")
        else:
           
            raise BusinessValidationError(status_code=404, error_code="BE101", error_message="Admin not found! Only for Admins")
        return jsonify({'status': 'success','message': 'Admin login Successful!', 'access_token': access_token, "username": username})


class SignupAdminAPI(Resource):
    def post(self):
        args = admin_parser.parse_args()
        username = args.get("username", None)
        email = args.get("email", None)
        password = args.get("password", None)


        if username is None:
            raise BusinessValidationError(status_code=400, error_code="BE1001", error_message="Please Enter Username!")
        if email is None:
            raise BusinessValidationError(status_code=400, error_code="BE1002", error_message="Please Enter Email!")
        if password is None:
            raise BusinessValidationError(status_code=400, error_code="BE1003", error_message="Please Enter Password!")
        
        user_namecheck = db.session.query(User).filter(User.username == username).first()
        user_mailcheck = db.session.query(User).filter(User.email == email).first()
            

        if user_namecheck:
            raise BusinessValidationError(status_code=400, error_code="BE105", error_message="Username already exists!")
        if not '@' in email:
            raise BusinessValidationError(status_code=400, error_code="BE104", error_message="Invalid email")
        if user_mailcheck:
            raise BusinessValidationError(status_code=400, error_code="BE106", error_message="Email Not Available!")
        

        new_user = User(username=username, email=email, password=  hash_password(password), active=True, is_admin=True)
        new_user.fs_uniquifier = secrets.token_hex(16)

        db.session.add(new_user)
        db.session.commit()
        return {'status': 'success','message': 'SignUp Successfull !!'}
    

def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        verify_jwt_in_request()  

        user_id = get_jwt_identity()  
        user = User.query.get(user_id) 

        if not user or not user.is_admin:
            response = jsonify(message="Admin required")
            response.status_code = 403
            return response

        return func(*args, **kwargs)

    return decorated_function