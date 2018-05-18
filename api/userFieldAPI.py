from flask import request
from flask_restful import Resource, reqparse
from pomodb import *
from utils import timestamp as t


#probs there's a better solution than this BUT this was faster to develop
class UserFieldAPI(Resource):
    def __init__(self):
        super(UserFieldAPI, self).__init__()

    def get(self, user_id, field):
        json = selectUser(_id=user_id)
        user = User()

        try:
            user = user.load(json)
        except ValidationError as e:
            return e.messages
        return user[field]

    def put(self, user_id, field):
        json = request.get_json()
        if field == 'faces':
            faces = selectUser(_id=user_id)
            faces = faces['faces']
            for key, data in json.items():
                faces[int(key)] = data
                updateOne('users', user_id, faces=faces)
        else:
            updateOne('users', user_id, **dict([(field, json)]))


