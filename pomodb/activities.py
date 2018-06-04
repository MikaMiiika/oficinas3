from pomodb import *
from utils import timestamp as t
from operator import itemgetter

def getActivityTime(userID, name, start, end):
    activities = mongo.db.activities

    if exists('activities', name=name):
        if (start != "ALL") or (end != "ALL"):
            start = t.timeToTimestamp(start)
            end = t.timeToTimestamp(end)

            cur = activities.aggregate([{'$match': {'name': name,
                                                    'userID': userID,
                                                    'timeStartedInt': {'$gt': start},
                                                    'timeEndedInt': {'$lt': end}}},
                                        {'$group': {'_id': '$name',
                                                    'sum': {'$sum': '$timeSpent'}}}])
        else:
            print('here')
            cur = activities.aggregate([{'$match': {'name': name,
                                                    'userID': userID}},
                                        {'$group': {'_id': '$name',
                                                    'sum': {'$sum': '$timeSpent'}}}])
        for doc in cur:
            return doc


def getActivitiesTime(userID, start, end):
    activities = mongo.db.activities
    activitiesName = activities.distinct('name')
    print(activitiesName)
    actList = []

    for a in activitiesName:
        actList.append(getActivityTime(userID, a, start, end))

    #actListOrdered = sorted(actList, key=itemgetter('sum'), reverse=True)
    return actList