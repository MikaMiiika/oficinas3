from flask import request
from flask_restful import Resource, reqparse
from pomodb import *
from utils import timestamp as t
from api import WAVUtil
import json

class PomodoroServerAPI(Resource):

    def __init__(self):
        pass

    def getJSON(jsonInBytes):
        jsonObject = ""

        try:
            jsonObject = json.loads(jsonInBytes)
        except ValueError:
            print("JSON recebido é inválido.")
            return None

        return jsonObject

    def get(self):
        print("Entrou GET")
        print("<html><body><h1>Oláaaaaaa</h1></body></html>")
        return "<html><body><h1>Oláaaaaaa</h1></body></html>"


    def post(self):
        print("Entrou POST")
        json = request.get_json()
        print("Conteúdo recebido: " + str(json))
        return "POST OK"
        # bytesSound = jsonObject['bytes_sound']
        # taskName = jsonObject['task_name']
        # pomodoroId = jsonObject['pomodoro_id']
        # soundName = pomodoroId + "." + taskName
        # wavFile = WAVUtil.bytesToWAV(bytesSound, soundName)
