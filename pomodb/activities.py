from pomodb import *
from operator import itemgetter

def getActivityTotalTime(userID, name):
    activities = mongo.db.activities

    if exists(name):
        cur = activities.aggregate([{'$match': {'name': name,
                                                'userID': userID}},
                                        {'$group': {'_id': '$name',
                                                    'sum': {'$sum': '$timeSpent'}}}])

        for doc in cur:
            return doc


def getActivitiesTotalTime(self, userID):
    activities = mongo.db.activities
    activitiesName = activities.distinct('name')

    actList = []

    for a in activitiesName:
        actList.append(getActivityTotalTime(userID, a))

    actListOrdered = sorted(actList, key=itemgetter('sum'), reverse=True)
    return actListOrdered