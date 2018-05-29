from pymongo import errors
from pomodb import *

def insert(collectionName, **fields):
    collection = mongo.db[collectionName]

    if '_id' in fields:
        if fields['_id'] is None:
            print(fields)
            fields.pop('_id', None)

    try:
        id = collection.insert(fields)
    except errors.DuplicateKeyError as e:
        raise e

    return str(id)


def select(collectionName):
    collection = mongo.db[collectionName]

    cur = collection.find()

    docs = []
    for doc in cur:
        doc['_id'] = str(doc['_id'])
        docs.append(doc)

    return docs


def updateOne(collectionName, id, **fields):
    collection = mongo.db[collectionName]

    if exists(collectionName, _id=id):
        collection.find_one_and_update({'_id': id}, {'$set': fields})
    else:
        return "Document not found"

d
def exists(collectionName, **fields):
    collection = mongo.db[collectionName]

    return bool(collection.find_one(fields))