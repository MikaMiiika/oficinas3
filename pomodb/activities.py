from pomodb import *
from utils import timestamp as t
from operator import itemgetter

def getActivityTime(userID, name, start, ended):
    activities = mongo.db.activities
    start = t.timeToTimestamp(start)
    ended = t.timeToTimestamp(ended)

    if exists(name):
        cur = activities.aggregate([{'$match': {'name': name,
                                                'userID': userID,
                                                'timeStarted': {'$gt': start},
                                                'timeEnded': {'$lt': ended}}},
                                    {'$group': {'_id': '$name',
                                                'sum': {'$sum': '$timeSpent'}}}])

        for doc in cur:
            return doc


def getActivitiesTime(userID, start, end):
    activities = mongo.db.activities
    activitiesName = activities.distinct('name')

    actList = []

    for a in activitiesName:
        actList.append(getActivityTime(userID, a, start, end))

    #actListOrdered = sorted(actList, key=itemgetter('sum'), reverse=True)
    return actList