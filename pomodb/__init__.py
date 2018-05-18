from flask_pymongo import PyMongo
from api import *

app.config['MONGO_DBNAME'] = 'smartdb'
app.config['MONGO_URI'] = 'mongodb://smart:admin@localhost:27017/smartdb'

mongo = PyMongo(app)

from .general import *
from .users import *
from .activities import *
from .schemas import *
