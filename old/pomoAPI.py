from flask_restful import Resource, reqparse
from pomodb import *

class PomoAPI(Resource):
    def __init__(self):
        self.PomoList = PomodoroList()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('pomoID', type=str, location='json')
        self.parser.add_argument('owned', type=bool, location='json')
        self.parser.add_argument('used', type=bool, location='json')
        super(PomoAPI, self).__init__()

    def get(self):
        return self.PomoList.getPomoList()


    def post(self):
        args = self.parser.parse_args()
        pass

    def put(self):
        args = self.parser.parse_args()
        pass