import os
import psycopg2
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager, set_login_view


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('secretKey')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('sqlDatabaseUri') 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view ='login'
login_manager.login_message_category = 'info'


from FlickFanatic import routes 

