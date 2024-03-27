from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from models import User, Portfolio
from forms import LoginForm, RegistrationForm, PortfolioForm, SellForm
from utils import get_data


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)  # Implement this with Flask-Login
            return redirect(url_for('portfolio'))
        else:
            form.username.errors.append('Invalid username or password.')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('New user has been created!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/')
def main():
    data = get_data()
    # Iterate through each item in the data list
    for item in data:
        # Iterate through each key, value pair in the item
        for key, value in item.items():
            # Check if the value is NoneType, replace it with 0
            if value is None:
                item[key] = 0

        # Existing logic to extract and assign coin_id
        img_src = item['image']
        idx1 = img_src.find('images')
        idx_st = idx1 + 7
        idx2 = img_src.find('/large')
        coin_id = img_src[idx_st:idx2]
        item['cid'] = coin_id

    return render_template('index.html', data=data)



@app.route('/crypto/<int:rank>/<string:name>', methods=['GET'])
def crypto(rank, name):
    data = get_data()
    index = rank - 1
    dic = data[index]
    ticker = dic["symbol"] + 'usd'

    return render_template('crypto.html', ticker=ticker, dic=dic)


@app.route('/services', methods=['GET', 'POST'])
@login_required
def services():
    buy_form = PortfolioForm(prefix="buy")
    sell_form = SellForm(prefix="sell")  # Notice the prefix to differentiate
    if buy_form.validate_on_submit() and buy_form.submit.data:
        new_entry = Portfolio(username=current_user.username, ticker=buy_form.ticker.data, amount=buy_form.amount.data, price=buy_form.price.data)
        db.session.add(new_entry)
        db.session.commit()
        flash('Transaction successful!', 'success')
        return redirect(url_for('portfolio'))
    elif sell_form.validate_on_submit() and sell_form.submit.data:
        # Implement sell logic, e.g., finding a matching entry and removing it
        # This is a simplification. Adjust based on your application's logic.
        Portfolio.query.filter_by(username=current_user.username, ticker=sell_form.ticker.data).delete()
        db.session.commit()
        flash('Sell transaction successful!', 'success')
        return redirect(url_for('portfolio'))
    return render_template('services.html', buy_form=buy_form, sell_form=sell_form)



@app.route('/portfolio')
@login_required
def portfolio():
    portfolio_entries = Portfolio.query.filter_by(username=current_user.username).all()
    print(portfolio_entries)
    return render_template('portfolio.html', data=portfolio_entries)


@app.route('/contacts')
def contacts():
    return render_template('contact.html')