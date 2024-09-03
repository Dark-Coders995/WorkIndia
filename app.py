from imports import *


def create_app():
    app_create = Flask(__name__)
    if os.getenv('ENV', "development") == "production":
        raise Exception("Currently no production config is setup.")
    else:
        print("Staring Local Development")
        app_create.config.from_object(LocalDevelopmentConfig)
        #CORS(app_create, resources={r"/api/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"]}})
    db.init_app(app_create)
    api_create = Api(app_create)
    api_create.init_app(app_create)
    JWTManager(app_create)
    migrate = Migrate(app_create, db)
    security.init_app(app_create, user_datastore)
    app_create.app_context().push()
    return app_create, api_create


app, api = create_app()

api.add_resource(LoginAPI, '/api/login')
api.add_resource(SignupAPI, '/api/signup')


api.add_resource(SignupAdminAPI , '/api/admin/signup')
api.add_resource(AdminLoginAPI , '/api/admin/login')
api.add_resource(AddTrain , '/api/admin/addTrain')


api.add_resource(CheckAvailability , '/api/checkTrain/<string:source>/to/<string:destination>')
api.add_resource(AllBookingsAPI , '/api/bookings')
api.add_resource(BookTrainAPI , '/api/bookTrain/<int:train_id>')
api.add_resource(BookingDetailsAPI , '/api/BookingDetails/<int:booking_id>')

@app.route('/')
def login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)