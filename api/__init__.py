from flask import Flask, g
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = selectUser(_id=username)
    if not user or not pwd_context.verify(password, user['password']):
        return False
    g.user = user
    return True

from .activitiesAPI import *
from .activityAPI import *
from .userAPI import *
from .userFieldAPI import *
from .usersAPI import *


class hello(Resource):
    def get(self):
        return "Hello World!"

class index(Resource):
    def get(self):
        return "Hello World!"

api.add_resource(hello, '/')
api.add_resource(index, '/index')
api.add_resource(UsersAPI, '/api/users')
api.add_resource(UserAPI, '/api/users/<user_id>')
api.add_resource(UserFieldAPI, '/api/users/<user_id>/<field>')
api.add_resource(ActivitiesAPI, '/api/activity')
api.add_resource(ActivityAPI, '/api/activity/<activity_name>')