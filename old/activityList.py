from pymongo import errors
from pomodb import *
from operator import itemgetter
from utils import timestamp as t

from bson.objectid import ObjectId

class ActivityList():
    def __init__(self):
        self.activities = mongo.db['activities']

    def newActivity(self, userID, name, time_started, time_ended):
        time_started = t.timeToTimestamp(time_started)
        time_ended = t.timeToTimestamp(time_ended)

        activity = {'userID': userID,
                    'name': name,
                    'timeStarted': time_started,
                    'timeEnded': time_ended,
                    'timeSpent': time_ended - time_started}

        try:
            id = self.activities.insert(activity)
        except errors.DuplicateKeyError:
            return "Error: Activity already exists"
        return id

    def getActivityTotalTime(self, userID, name):
        a = self.activities.distinct('name')
        print(a)

        if self.exists(name):
            cur = self.activities.aggregate([{'$match': {'name': name,
                                                         'userID': userID}},
                                            {'$group': {'_id': '$name',
                                                        'sum': {'$sum': '$timeSpent'}}}])

            for doc in cur:
                return doc

    def getActivitiesTotalTime(self, userID):
        activitiesName = self.activities.distinct('name')

        actList = []

        for a in activitiesName:
            actList.append(self.getActivityTotalTime(userID, a))

        actListOrdered = sorted(actList, key=itemgetter('sum'), reverse=True)
        return actListOrdered

    def exists(self, name):
        return bool(self.activities.find_one({'name': name}))