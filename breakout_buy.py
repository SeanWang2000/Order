from binance.um_futures import UMFutures
from function_db import get_min_low_price, get_max_high_price, truncate_decimal, get_max_precision

def main():

    key=''
    secret=''
    cm_futures_client = UMFutures(key=key, secret=secret)

    symbol = input("symbol:")
    loss = float(input("loss:"))
    entry_timeframe = input("進場時框:")
    entry_Kamount = int(input("進場K棒數:"))
    stop_timeframe = input("止損時框:")
    stop_Kamount = int(input("止損K棒數:"))
    x = get_max_precision(symbol)
    entry = get_max_high_price(symbol,entry_timeframe,entry_Kamount)
    stop = get_min_low_price(symbol,stop_timeframe,stop_Kamount)
    fee = 0.0005
    openusd = loss / (fee * (1 + stop / entry) + (1 / entry) * abs(stop - entry))
    quantity = truncate_decimal(openusd/entry,x)
    params = {
        'symbol': symbol,
        'side': 'BUY',
        'type': 'STOP_MARKET',
        "stopPrice": entry,
        'timeInForce': 'GTC',
        'quantity': quantity
    }

    response = cm_futures_client.new_order(**params)

if __name__ == "__main__":
    main()