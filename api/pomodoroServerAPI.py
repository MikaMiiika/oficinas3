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

    def set_sucess_header(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    def get(self):
        print("Entrou GET")
        print(self.path)

        if self.path == '/':
            print("<html><body><h1>Oláaaaaaa</h1></body></html>")
            self.set_sucess_header()
            self.wfile.write(bytes("<html><body><h1>Oláaaaaaa</h1></body></html>", "utf-8"))
            return

        if self.path == '/error':
            # 404: Codigo padrao de resposta para o erro 'Object Not Found'
            self.send_error(404, "Object not found.")
            return


    def post(self):
        print("Entrou POST")
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        jsonObject = self.getJSON(data)
        print("Conteúdo recebido: " + str(jsonObject))

        if self.path == '/pomodoroSound':
            self.set_sucess_header()
            self.wfile.write(bytes("<html><body><h1>Teste Sound POST OK</h1></body></html>", "utf-8"))
            return
            # bytesSound = jsonObject['bytes_sound']
            # taskName = jsonObject['task_name']
            # pomodoroId = jsonObject['pomodoro_id']
            # soundName = pomodoroId + "." + taskName
            # wavFile = WAVUtil.bytesToWAV(bytesSound, soundName)
