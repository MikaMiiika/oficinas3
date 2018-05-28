from flask_pymongo import PyMongo
#from flask_mongo_sessions import MongoDBSessionInterface

from api import *

app.config['MONGO_DBNAME'] = 'smartdb'
#app.config['MONGO_URI'] = 'mongodb://smart:admin@%s:27017/smartdb' % (os.environ['MONGODB_34_RHEL7_PORT_27017_TCP_ADDR'])

app.config['MONGO_URI'] = 'mongodb://smart:admin@localhost:27017/smartdb'

mongo = PyMongo(app)
#with app.app_context():
#    app.session_interface = MongoDBSessionInterface(app, mongo.db, 'sessions')

from .general import *
from .users import *
from .activities import *
from .schemas import *
