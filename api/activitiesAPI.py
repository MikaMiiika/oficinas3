from flask import request
from flask_restful import Resource, reqparse
from pomodb import *
from utils import timestamp as t
import time

class ActivitiesAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        pass

    def get(self):
        userID = g.user['_id']
        started1 = request.args.get('started1')
        if started1 is not None:
            started1 = started1 + " 00:00:00"
            ended1 = request.args.get('ended1')
            ended1 = ended1 + " 00:00:00"
            act1 = getActivitiesTime(userID, started1, ended1)

            for a1 in act1:
                a1['sum1'] = a1.pop('sum')
            print(act1)
            started2 = request.args.get('started2')
            started2 = started2 + " 00:00:00"
            ended2 = request.args.get('ended2')
            ended2 = ended2 + " 00:00:00"
            act2 = getActivitiesTime(userID, started2, ended2)

            for a2 in act2:
                found = False
                for a1 in act1:
                    if a1['_id'] == a2['_id']:
                        a1['sum2'] = a2['sum']
                        found = True
                        break

                if not found:
                    a2['sum2'] = a2.pop('sum')
                    act1.append(a2)


            started3 = request.args.get('started3')
            started3 = started3 + " 00:00:00"
            ended3 = request.args.get('ended3')
            ended3 = ended3 + " 00:00:00"
            act3 = getActivitiesTime(userID, started3, ended3)
            print(act3)

            for a3 in act3:
                found = False
                for a1 in act1:
                    if a1['_id'] == a3['_id']:
                        a1['sum3'] = a3['sum']
                        found = True
                        break

                if not found:
                    print(a3)
                    a3['sum3'] = a3.pop('sum')
                    act1.append(a3)

            return act1

        else:
            started = request.args.get('started')
            if started is not None:
                started = started + " 00:00:00"
            else:
                started = "ALL"

            ended = request.args.get('ended')
            if ended is not None:
                ended = ended + " 00:00:00"
            else:
                ended = "ALL"
            return getActivitiesTime(userID, started, ended)

    def post(self):
        json = request.get_json()
        timeEnded = str(time.time()).split('.')[0]

        a = {}
        a['userID'] = g.user['_id']
        a['name'] = getFaceName(a['userID'], json['faceID'])
        a['timeEndedInt'] = int(timeEnded)
        a['timeStartedInt'] = int(timeEnded) - int(json['delta'])
        act = Activity()

        try:
            act = act.load(a)
            insert('activities', **act)
        except ValidationError as e:
            abort(404, message='These fields are wrong: ' + str(e))
        except errors.DuplicateKeyError:
            abort(404, message='User already exists')
        return act
