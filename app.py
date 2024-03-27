from flask import Flask
from extensions import db, login_manager
from config import Config
from dummy_data import add_dummy_portfolio_data

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)

# No need to import load_user function here, since it's already imported in extensions.py

with app.app_context():
    from models import User, Portfolio
    db.create_all()
    #add_dummy_portfolio_data()

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
