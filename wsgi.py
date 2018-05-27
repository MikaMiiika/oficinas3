from api import app as application

if __name__ == '__main__':
    #app.secret_key = 'mysecret'
    application.run(debug=True)