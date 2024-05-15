from app.extensions import db
from app.models import Portfolio

def add_dummy_portfolio_data():
    dummy_data = [
        {"username": "admin", "ticker": "BTC", "amount": 1.5, "price": 45000},
        {"username": "admin", "ticker": "ETH", "amount": 10, "price": 3000},
        {"username": "admin", "ticker": "LTC", "amount": 20, "price": 200}
    ]

    for data in dummy_data:
        entry = Portfolio(username=data["username"], ticker=data["ticker"], amount=data["amount"], price=data["price"])
        db.session.add(entry)

    db.session.commit()
