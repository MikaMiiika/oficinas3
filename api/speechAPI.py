from flask import request
from flask_restful import Resource, reqparse
from pomodb import *
from utils import timestamp as t
from speech import *
import werkzeug

class SpeechAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        pass

    def get(self, activity_name):
        pass

    def post(self):
        json = request.get_json()
        return ConvertSpeech(json)