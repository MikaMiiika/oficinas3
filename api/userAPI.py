from flask import request
from flask_restful import Resource
from pomodb import *

class UserAPI(Resource):
    def __init__(self):
        super(UserAPI, self).__init__()

    def get(self, user_id):
        json = selectUser(_id=user_id)
        user = User()

        try:
            user = user.load(json)
        except ValidationError as e:
            return e.messages
        return user