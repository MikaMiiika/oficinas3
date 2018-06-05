from flask import request
from flask_restful import Resource
from pomodb import *

class LoginAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        super(LoginAPI, self).__init__()

    def get(self):
        return {"message": "Authorized Access"}, 200
