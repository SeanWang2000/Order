import requests
from math import floor
import datetime

def get_max_high_price(symbol, interval, limit):

    
    url = 'https://fapi.binance.com/fapi/v1/klines'

    
    params = {
        'symbol': symbol,          # 交易兌
        'interval': interval,      # 時間間隔
        'limit': limit             # K線數量
    }

    
    response = requests.get(url, params=params)

    
    if response.status_code == 200:
        
        klines = response.json()
        high_price = [float(kline[2]) for kline in klines[:limit]]
        max_high_price = max(high_price)
        return float(max_high_price)
    else:

        print(f"请求失败：{response.status_code}, {response.text}")
        return None
    
def get_min_low_price(symbol, interval, limit):
    
    url = 'https://fapi.binance.com/fapi/v1/klines'

    
    params = {
        'symbol': symbol,          # 交易兌
        'interval': interval,      # 時間間隔
        'limit': limit             # K線數量
    }

    
    response = requests.get(url, params=params)

    
    if response.status_code == 200:
        
        klines = response.json()
        low_price = [float(kline[3]) for kline in klines[:limit]]
        min_low_price = min(low_price)
        return float(min_low_price)
    else:
        
        print(f"请求失败：{response.status_code}, {response.text}")
        return None
    
def get_best_askprices(symbol):
    url = 'https://fapi.binance.com/fapi/v1/ticker/bookTicker'
    params = {'symbol': symbol}  
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return float(data['askPrice'])
    else:
        return None  
    
def get_best_bidprices(symbol):
    url = 'https://fapi.binance.com/fapi/v1/ticker/bookTicker'
    params = {'symbol': symbol}  
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return float(data['bidPrice'])
    else:
        return None  

def get_max_precision(symbol):
    url = 'https://fapi.binance.com/fapi/v1/ticker/bookTicker'
    params = {'symbol': symbol}  
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        ask_quantity = data['askQty']
        number_str = str(ask_quantity)
    
    # 檢查是否有小數點
    if '.' in number_str:
        # 如果有小數點，則計算小數位數
        decimal_places = len(number_str.split('.')[1])
    else:
        # 如果沒有小數點，則小數位數為 0
        decimal_places = 0
    
    return decimal_places
    
def truncate_decimal(number, decimal_places):
    multiplier = 10 ** decimal_places
    truncated_number = floor(number * multiplier) / multiplier
    return truncated_number

def get_depth_info(symbol, limit):
    url = 'https://fapi.binance.com/fapi/v1/depth'
    params = {
        'symbol': symbol,
        'limit': limit
    }
    response = requests.get(url, params=params)
    depth_info = response.json()
    return depth_info

def calculate_average_price(symbol, limit, usdt_amount, asks_or_bids):
    total_amount = 0.0
    total_cost = 0.0
    url = 'https://fapi.binance.com/fapi/v1/depth'
    params = {
        'symbol': symbol,
        'limit': limit
    }
    response = requests.get(url, params=params)
    depth_info = response.json()
    print(depth_info[asks_or_bids])

    
    for price, quantity in depth_info[asks_or_bids]:
        price = float(price)
        quantity = float(quantity)
        
        if usdt_amount >= price * quantity:
            
            total_amount += quantity
            total_cost += price * quantity
            
            usdt_amount -= price * quantity
        else:
            
            total_amount += usdt_amount / price
            total_cost += usdt_amount
            usdt_amount = 0
            
            break

    
    if usdt_amount > 0:
        
        highest_price = float(depth_info['asks'][-1][0])
        total_amount += usdt_amount / highest_price
        total_cost += usdt_amount

    
    return total_cost / total_amount if total_amount > 0 else 0.0

