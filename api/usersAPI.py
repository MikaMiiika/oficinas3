from flask import request
from flask_restful import Resource, abort
from pomodb import *
from utils import timestamp as t

class UsersAPI(Resource):
    def __init__(self):
        super(UsersAPI, self).__init__()

    def get(self):
        json = select('users')
        user = User(many=True)

        try:
            user = user.load(json)
        except ValidationError as e:
            return e.messages
        return user

    def post(self):
        json = request.get_json()
        user = User()
        try:
            user = user.load(json)
            insert('users', **user)
        except ValidationError as e:
            abort(404, message='These fields are wrong: ' + str(e))
        except errors.DuplicateKeyError:
            abort(404, message='User already exists')
        return user['_id']