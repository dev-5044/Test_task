import os
from time import sleep

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

# init
API = os.getenv('HMAC_API_KEY')
SECRET = os.getenv('HMAC_SECRET_KEY')
client = Client(API, SECRET)
price = {'BTCUSDT': None, 'error':False}

API = os.getenv('HMAC_API_KEY')
SECRET = os.getenv('HMAC_SECRET_KEY')

def btc_pairs_trade(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':
        price['BTCUSDT'] = float(msg['c'])
        print(price)
    else:
        price['error']:True
        
bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_pairs_trade)
bsm.start()