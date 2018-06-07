from flask import Flask, g, make_response
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@auth.verify_password
def verify_password(username, password):
    user = selectUser(_id=username)
    if not user or not pwd_context.verify(password, user['password']):
        return False
    g.user = user
    return True

@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    abort(403, message='Unauthorized access')

from .activityListAPI import *
from .activitiesAPI import *
from .activityAPI import *
from .userAPI import *
from .userFieldAPI import *
from .usersAPI import *
from .loginAPI import *
from .WAVUtil import *
from .pomodoroServerAPI import *

class hello(Resource):
    def get(self):
        return "Mika linda <3"

class index(Resource):
    def get(self):
        return "Por favor funciona."

api.add_resource(hello,             '/')
api.add_resource(index,             '/index')
api.add_resource(LoginAPI,          '/api/login')
api.add_resource(UsersAPI,          '/api/users')
api.add_resource(UserAPI,           '/api/users/<user_id>')
api.add_resource(UserFieldAPI,      '/api/userfield/<field>')
api.add_resource(ActivitiesAPI,     '/api/activity')
api.add_resource(ActivityAPI,       '/api/activity/<activity_name>')
api.add_resource(ActivityListAPI,   '/api/activitylist')
api.add_resource(PomodoroServerAPI, '/api/pomodoroserver')