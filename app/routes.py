import json
import os

from app.main import db, main
from app.models import User, Portfolio
from app.forms import LoginForm, RegistrationForm, PortfolioForm, SellForm

from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, current_user, login_user, logout_user

from app.utils.data import get_data
from app.utils.sentiment_analysis import create_sentiment_plot



@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('portfolio'))
        else:
            form.username.errors.append('Invalid username or password.')
    return render_template('login.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
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


@main.route('/')
def home():
    data = get_data()
    for item in data:
        for key, value in item.items():
            if value is None:
                item[key] = 0
        img_src = item['image']
        idx1 = img_src.find('images')
        idx_st = idx1 + 7
        idx2 = img_src.find('/large')
        coin_id = img_src[idx_st:idx2]
        item['cid'] = coin_id
    return render_template('index.html', data=data)



@main.route('/crypto/<int:rank>/<string:name>', methods=['GET'])
def crypto(rank, name):
    data = get_data()
    index = rank - 1
    dic = data[index]
    ticker = dic["symbol"] + 'usd'
    return render_template('crypto.html', ticker=ticker, dic=dic)


@main.route('/news')
def news():
    current_dir = os.path.dirname(__file__)
    json_data = os.path.join(current_dir, 'Dataset', 'news.json')
    with open(json_data) as json_file:
        news_data = json.load(json_file)
    for i in range(len(news_data)):
        news_data[i]["ID"] = "news" + str(news_data[i]["index"])
    fig = create_sentiment_plot()
    sentiment_plot_html = fig.to_html(full_html=False)
    return render_template('news.html', news=news_data, sentiment_plot=sentiment_plot_html)



@main.route('/services', methods=['GET', 'POST'])
@login_required
def services():
    buy_form = PortfolioForm(prefix="buy")
    sell_form = SellForm(prefix="sell")
    if buy_form.validate_on_submit() and buy_form.submit.data:
        new_entry = Portfolio(username=current_user.username, ticker=buy_form.ticker.data, amount=buy_form.amount.data, price=buy_form.price.data)
        db.session.add(new_entry)
        db.session.commit()
        flash('Transaction successful!', 'success')
        return redirect(url_for('portfolio'))
    elif sell_form.validate_on_submit() and sell_form.submit.data:
        Portfolio.query.filter_by(username=current_user.username, ticker=sell_form.ticker.data).delete()
        db.session.commit()
        flash('Sell transaction successful!', 'success')
        return redirect(url_for('portfolio'))
    return render_template('services.html', buy_form=buy_form, sell_form=sell_form)



@main.route('/portfolio')
@login_required
def portfolio():
    portfolio_entries = Portfolio.query.filter_by(username=current_user.username).all()
    print(portfolio_entries)
    return render_template('portfolio.html', data=portfolio_entries)


@main.route('/contacts')
def contacts():
    return render_template('contact.html')


