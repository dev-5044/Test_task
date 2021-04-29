import os
import pandas as pd
import sys
from time import sleep
import logging
import colorlog
from time import sleep
from multiprocessing import Value, Manager
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
import sys
import logging
import colorlog

logger = logging.getLogger('')
logger.setLevel(logging.INFO)
sh = logging.StreamHandler(sys.stdout)
sh.setFormatter(colorlog.ColoredFormatter('%(log_color)s [%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S'))
logger.addHandler(sh)

LIMIT = Manager().Value('s', 0)
QUANTITY = Manager().Value('s', 0)


# init
api_key = os.getenv('HMAC_API_KEY')
api_secret = os.getenv('HMAC_SECRET_KEY')
client = Client(api_key, api_secret)


def stop_trading():
    bsm.stop_socket(conn_key)
    reactor.stop()
    
price = {'BTCUSDT': None, 'error':False}

def btc_pairs_trade(msg):
    if msg['e'] != 'error':
        price['BTCUSDT'] = float(msg['c'])
        
    else:
        price['error']:True
        
def create_new_order(operation=None, quantity=None): # создаем сделку
    if operation is None and quantity is None:
        obj.status = 'CLOSE'
        stop_trading()
    else:
        try:
            order = client.create_test_order(symbol='BTCUSDT', side=operation, type='MARKET', quantity=quantity)
        except BinanceAPIException as e:
            logger.exception("Error while user_login_or_signin:\n%s" % e)
        except BinanceOrderException as e:
            logger.exception("Error while user_login_or_signin:\n%s" % e)
        finally:
            obj.status = 'CLOSE'
            stop_trading()
    
    
    
def start_trade(obj):
    df = pd.DataFrame(columns=['price'])
    bsm = BinanceSocketManager(client)
    conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_pairs_trade)
    bsm.start()
        
    while not price['BTCUSDT']:
        # wait for WebSocket to start streaming data
        sleep(0.1)
    timer = 0
    while  True:
        # обновляем данные если они изменились
        if obj.limit != LIMIT.value:
            obj.limit = LIMIT.value
        if obj.quantity != QUANTITY.value:
            obj.quantity = QUANTITY.value
        
        obj.price = price['BTCUSDT']
        df = df.append({'price': price['BTCUSDT']}, ignore_index=True)
        df['MA'] = df.rolling(window=9).mean()
        timer += 1
        if timer == 9:  # проверяем после закрытия 9 свечи
            MA = df['MA'].iloc[-1]
            obj.ma = MA
            obj.save()
            if price['BTCUSDT'] >= MA + obj.limit:
                create_new_order(operation='SELL', quantity=obj.quantity)
            if price['BTCUSDT'] <= MA - obj.limit:
                create_new_order(operation='BUY', quantity=obj.quantity)
            if price['BTCUSDT'] == MA:
                create_new_order()
            timer = 0
        obj.save()
        sleep(300)
    
    bsm = BinanceSocketManager(client)
    conn_key = bsm.start_symbol_ticker_socket('BTCUSDT', btc_pairs_trade)
    bsm.start()
