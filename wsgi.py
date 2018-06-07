# -*- coding: utf-8 -*-

from api import app as application
from api import pomodoroServer

if __name__ == '__main__':
    #app.secret_key = 'mysecret'
    application.run(debug=True)
    pomodoroServer.run()