from random import randint
from flask import *
from flask_mail import *
import flask_bcrypt
import bcrypt
import pymongo


MAIL_SERVER='smtp.gmail.com'
MAIL_PORT=465
MAIL_USE_TLS = False
MAIL_USE_SSL= True
MAIL_USERNAME = 'meetyourmentor150@gmail.com'
MAIL_PASSWORD = 'fkffwsdunbvbqonc'

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
db_client = pymongo.MongoClient("mongodb://localhost:27017")


db = db_client["users"]
db_user_profile = db.user_profile
db_user_problem_solved = db.user_problem_solved

db_admin = db_client["admin"]
db_admin_profile = db_admin.admin_profile
db_admin_problemset = db_admin.problemset
technical_issue_face = db_admin.contact_us

app = Flask(__name__)
app.config.from_object(__name__)
mail = Mail(app)

app.secret_key = "testing"

from app.routes import index
from app.routes import c_tutorial
from app.routes import admin
from app.routes import problems
from app.routes import login
from app.routes import SignUp
from app.routes import verify
from app.routes import SignOut
from app.routes import admin_login
from app.routes import admin_SignOut
from app.routes import contest
from app.routes import change_pass
from app.routes import video_tutorial
from app.routes import animation_tutorial
from app.routes import contact
