from flask import request
from flask_restful import Resource, reqparse
from pomodb import *
from utils import timestamp as t

class ActivityAPI(Resource):
    def __init__(self):
        pass

    def get(self):
        return request.args.get('started')

    def post(self):
        pass
