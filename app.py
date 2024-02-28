from flask import Flask, render_template, request, redirect, url_for
import requests
import json
from pycoingecko import CoinGeckoAPI
import cachetools.func

app = Flask(__name__)


cg = CoinGeckoAPI()


@cachetools.func.ttl_cache(ttl=3600)
def get_data():
    reqdata = cg.get_coins_markets(vs_currency='usd',
                                   order='market_cap_desc',
                                   per_page='100',
                                   price_change_percentage='1h,24h,7d')
    print("data retrieved")
    return reqdata


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Here you would add your logic to check the username and password
        # For now, let's just redirect to the home page
        return redirect(url_for('main'))
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)