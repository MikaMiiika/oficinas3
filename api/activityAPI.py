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
        started = started + " 00:00:00"
        ended = request.args.get('ended')
        ended = ended + " 00:00:00"
        return getActivityTime(userID, activity_name, started, ended)
