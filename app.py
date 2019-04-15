from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yash:Hisar*123@localhost/diagnose_results'

from routes import *
import models

if __name__ == '__main__':
    app.run()