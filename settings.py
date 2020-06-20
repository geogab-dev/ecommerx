FLASK_APP = 'run'
FLASK_ENV = 'development'
DEBUG = True
SECRET_KEY = '733fa1a0ce48f381ca1e6d71f077'
HOST = 'localhost'
PORT = 5000
TESTING = False
API_NAME = 'flask-api'
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_USERNAME = 'root'
MONGODB_PASSWORD = 'rootpassword'
MONGODB_DB = 'flaskapi'
MONGODB_SETTINGS = {
    'db': 'flaskapi',
    'host': f'mongodb://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@localhost:{MONGODB_PORT}/{MONGODB_DB}?authSource=admin'
}
