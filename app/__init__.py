from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app_var = Flask(__name__)
app_var.config.from_object(Config)

# create a database
db = SQLAlchemy(app_var)
# create a migration service(?)
migrate = Migrate(app_var, db)
# create a login manager to remember the logged in users
login = LoginManager(app_var)
login.login_view = 'login'

from app import routes, models
