from pymongo import errors
from pomodb import *

from bson.objectid import ObjectId

class PomodoroList():
    def __init__(self):
        self.pomos = mongo.db.pomos

    #create a new pomo in list, without any owner
    def newPomo(self):
        try:
            id = self.pomos.insert({'owned': False, 'used': False})
        except errors.DuplicateKeyError:
            return "Error: Pomodoro already exists"
        return id

    def getPomoList(self):
        docs = []
        cur = self.pomos.find()
        for doc in cur:
            doc['_id'] = str(doc['_id'])
            docs.append(doc)

        return docs

    def getPomoNotOwned(self):
        if self.exists(pomoID):
            pomo = self.pomos.find_one({'owned': False})
            pomo['_id'] = str(pomo['_id'])
            return pomo
        return "Error: Pomodoro doesn't exists"

    def getPomoNotUsed(self):
        if self.exists(pomoID):
            pomo = self.pomos.find_one({'used': False})
            pomo['_id'] = str(pomo['_id'])
            return pomo
        return "Error: Pomodoro doesn't exists"

    #get a pomo status by ID
    def getPomoFromId(self, pomoID):
        if self.exists(pomoID):
            pomo = self.pomos.find_one({'_id': ObjectId(pomoID)})
            pomo['_id'] = str(pomo['_id'])
            return pomo
        return "Error: Pomodoro doesn't exists"

    def updatePomoOwned(self, pomoID, owned = False):
        if self.exists(pomoID):
            self.pomos.find_one_and_update({'_id': pomoID}, {'owned': owned})
        return "Error: Pomodoro doesn't exists"

    def updatePomoUsed(self, pomoID, used = False):
        if self.exists(pomoID):
            self.pomos.find_one_and_update({'_id': pomoID}, {'used': used})
        return "Error: Pomodoro doesn't exists"

    def exists(self, pomoID):
        return bool(self.pomos.find_one({'_id': ObjectId(pomoID)}))

    #check if owned or not
    def hasOwner(self, pomoID):
        return bool(self.pomos.find_one({'_id': ObjectId(pomoID),
                                         'owned': True}))