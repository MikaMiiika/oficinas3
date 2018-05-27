from flask import request
from flask_restful import Resource, reqparse
from pomodb import *
from utils import timestamp as t

class ActivitiesAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        pass

    def get(self):
        userID = g.user['_id']
        started = request.args.get('started')
        started = started + " 00:00:00"
        ended = request.args.get('ended')
        ended = ended + " 00:00:00"
        return getActivitiesTime(userID, started, ended)

    def post(self):
        json = request.get_json()
        print(json)
        act = Activity()

        try:
            act = act.load(json)
            insert('users', **act)
        except ValidationError as e:
            abort(404, message='These fields are wrong: ' + str(e))
        except errors.DuplicateKeyError:
            abort(404, message='User already exists')
        return act
