from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from old.pomoAPI import *
from .activityAPI import *
from .userAPI import *
from .userFieldAPI import *
from .usersAPI import *

api.add_resource(ActivityAPI, '/api/activity')
api.add_resource(UsersAPI, '/api/users')
api.add_resource(UserAPI, '/api/users/<user_id>')
api.add_resource(UserFieldAPI, '/api/users/<user_id>/<field>')