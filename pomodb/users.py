from pomodb import *
from passlib.apps import custom_app_context as pwd_context


def selectUser(**fields):
    users = mongo.db.users

    if exists('users', **fields):
        user = users.find_one(fields)
        return user

    return "Error: Pomodoro doesn't exists"


def getFaceName(userID, faceID):
    user = selectUser(_id=userID)
    return user['faces'][faceID]

def hashPassword(password):
    hash = pwd_context.encrypt(password)
    return hash


def verifyPassword(password, hash):
    return pwd_context.verify(password, hash)


