"""Flask app for Cupcakes"""
from flask import Flask, Blueprint
from secrets import FLASK_SECRET_KEY
from config import DB_NAME
from models import connect_db
from models.cupcake import Cupcake
from routes.api import api


app = Flask(__name__)

app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.register_blueprint(api, url_prefix='/api')
