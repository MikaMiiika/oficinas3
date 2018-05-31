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
        if started is not None:
            started = started + " 00:00:00"
        else:
            started = "ALL"

        ended = request.args.get('ended')
        if ended is not None:
            ended = ended + " 00:00:00"
        else:
            ended = "ALL"
        return getActivitiesTime(userID, started, ended)

    def post(self):
        json = request.get_json()
        print(json)
        act = Activity()
        json['userID'] = g.user['_id']

        try:
            act = act.load(json)
            insert('activities', **act)
        except ValidationError as e:
            abort(404, message='These fields are wrong: ' + str(e))
        except errors.DuplicateKeyError:
            abort(404, message='User already exists')
        return act
