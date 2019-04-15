from flask import Flask
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']


from routes import *
import models

if __name__ == '__main__':
    app.run()