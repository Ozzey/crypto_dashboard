import requests
import json
from pycoingecko import CoinGeckoAPI
import cachetools.func

cg = CoinGeckoAPI()

@cachetools.func.ttl_cache(ttl=3600)
def get_data():
    reqdata = cg.get_coins_markets(vs_currency='usd',
                                   order='market_cap_desc',
                                   per_page='100',
                                   price_change_percentage='1h,24h,7d')
    print("data retrieved")
    return reqdata


