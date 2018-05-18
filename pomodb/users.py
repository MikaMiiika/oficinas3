from pomodb import *

def selectUser(**fields):
    users = mongo.db.users

    if exists('users', **fields):
        user = users.find_one(fields)
        return user

    return "Error: Pomodoro doesn't exists"