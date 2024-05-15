from flask import Flask
from app.extensions import db, login_manager
from app.config import Config
from app.utils.dummy_data import add_dummy_portfolio_data

main = Flask(__name__)
main.config.from_object(Config)

db.init_app(main)
login_manager.init_app(main)

with main.app_context():
    from app.models import User, Portfolio
    db.create_all()
    #add_dummy_portfolio_data()

from app.routes import *

if __name__ == '__main__':
    main.run(debug=False)
