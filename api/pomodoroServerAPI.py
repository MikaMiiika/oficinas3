from flask import request
from flask_restful import Resource, reqparse
from pomodb import *
from utils import timestamp as t
from api import WAVUtil
from speech import convertSpeech
import json


class PomodoroServerAPI(Resource):
    decorators = [auth.login_required]

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

        user_id = g.user['_id']
        hexString = json['audio']
        frequencia = json['frequencia']
        faceID = json['faceID']
        fullFileName = str(frequencia) + "." + str(faceID)
        filePath = WAVUtil.criarArquivoWAV(hexString, frequencia, fullFileName)
        activityName = convertSpeech.ConvertSpeech(filePath)

        # updateOne('users', user_id, **dict([(field, json)]))
        return activityName