from random import randint
from flask import *
from flask_mail import *
import pymongo

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
db_client = pymongo.MongoClient("mongodb://localhost:27017")


db = db_client["users"]
db_user_profile = db.user_profile

db_admin = db_client["admin"]
db_admin_profile = db_admin.admin_profile
db_admin_problemset = db_admin.problemset

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

app.secret_key = "testing"

from app.routes import index
from app.routes import c_tutorial
from app.routes import admin
from app.routes import problems

