from flask_pymongo import PyMongo
#from flask_mongo_sessions import MongoDBSessionInterface
import os
from api import *

app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL']

#app.config['MONGO_URI'] = 'mongodb://smart:admin@localhost:27017/smartdb'

mongo = PyMongo(app)
#with app.app_context():
#    app.session_interface = MongoDBSessionInterface(app, mongo.db, 'sessions')

from .general import *
from .users import *
from .activities import *
from .schemas import *
