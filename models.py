from flask_sqlalchemy import SQLAlchemy
from app import app
import time

db = SQLAlchemy(app)


class file_results(db.Model):
    time = db.Column( db.Integer, primary_key = True)
    ip = db.Column(db.String(16), primary_key=True)
    filename = db.Column(db.String(100))
    Aresult = db.Column(db.Integer)
    Presult = db.Column(db.Integer)
    Dresult = db.Column(db.Integer)

    def __init__(self, filename, ip, file_result):
        self.time = int(time.time())
        self.ip = ip
        self.filename = filename
        self.Aresult = file_result[0]
        self.Presult = file_result[1]
        self.Dresult = file_result[2]


