from flask import request
from flask_restful import Resource, reqparse
from pomodb import *
from utils import timestamp as t

class ActivityListAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        pass

    def get(self):
        acts = {}
        acts['activities'] = getActivityList(g.user['_id'])

        list = ActivityList()
        list = list.dump(acts)
        print(list)
        return list
