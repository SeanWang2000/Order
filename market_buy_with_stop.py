from binance.um_futures import UMFutures
from function_db import get_min_low_price, get_best_askprices, truncate_decimal, get_max_precision

def main():

    key=''
    secret=''
    cm_futures_client = UMFutures(key=key, secret=secret)


    symbol = input("symbol:")
    loss = float(input("loss:"))
    stop_timeframe = input("止損時框:")
    stop_Kamount = int(input("止損K棒數:"))
    x = get_max_precision(symbol)
    entry = get_best_askprices(symbol)
    stop = get_min_low_price(symbol,stop_timeframe,stop_Kamount)
    fee = 0.0005
    openusd = loss / (fee * (1 + stop / entry) + (1 / entry) * abs(stop - entry))
    quantity = truncate_decimal(openusd/entry,x)
    params = {
        'symbol': symbol,
        'side': 'BUY',
        'type': 'MARKET',
        'quantity': quantity
    }

    response = cm_futures_client.new_order(**params)

    params = {
        'symbol': symbol,
        'side': 'SELL',
        'type': 'STOP_MARKET',
        "stopPrice": stop,
        'timeInForce': 'GTC',
        'quantity': quantity
    }

    response = cm_futures_client.new_order(**params)

if __name__ == "__main__":
    main()