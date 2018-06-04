from flask import request
from flask_restful import Resource, reqparse
from pomodb import *
from utils import timestamp as t

class ActivityAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        pass

    def get(self, activity_name):
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
        return getActivityTime(userID, activity_name, started, ended)
