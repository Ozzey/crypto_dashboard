from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

login_manager = LoginManager()
login_manager.login_view = 'login'  # 'login' is the endpoint name for the login route

# This function will be defined in models.py but we import it here
from models import load_user

login_manager.user_loader(load_user)
