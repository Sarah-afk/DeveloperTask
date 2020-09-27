from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_caching import Cache
import os

#initialize app
app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'secret key'
#specifying the location of sqlite3 database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getcwd()+'/logs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['CACHE_TYPE'] = 'simple'

CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials", "Access-Control-Allow-Origin", "Access-Control-Allow-Headers", "x-access-token"], supports_credentials=True)

#initialize SQALchemy database
db = SQLAlchemy(app)

cache = Cache()
cache.init_app(app)

#creating a database table with all the different required columns
class Logs(db.Model):
    __tablename__ = 'Logs'
    id = db.Column(db.Integer, primary_key=True)
    input = db.Column(db.Integer)
    output = db.Column(db.String(100000))
    
    time = db.Column(db.Integer)
    runtime = db.Column(db.Integer)
