from binance.um_futures import UMFutures
from myfunction import get_min_low_price, get_max_high_price, truncate_decimal, get_max_precision

def main():
    key='W2qkV5fvSLU3FfddjHTLmsdIFMGshFvvn3YmquAe6LFpiHoxjIisdUf2uDpVeXfh'
    secret='pQJYqX0JfspYkQpQM6bG7R9Tk93vz8tnc4b6ud9S1ToMYEfwJgHUa4SQljciBNQy'
    cm_futures_client = UMFutures(key=key, secret=secret)

    symbol = input("symbol:")
    loss = float(input("loss:"))
    entry_timeframe = input("進場時框:")
    entry_Kamount = int(input("進場K棒數:"))
    stop_timeframe = input("止損時框:")
    stop_Kamount = int(input("止損K棒數:"))
    x = get_max_precision(symbol)
    entry = get_min_low_price(symbol,entry_timeframe,entry_Kamount)
    stop = get_max_high_price(symbol,stop_timeframe,stop_Kamount)
    fee = 0.0005
    openusd = loss / (fee * (1 + stop / entry) + (1 / entry) * abs(stop - entry))
    quantity = truncate_decimal(openusd/entry,x)
    params = {
        'symbol': symbol,
        'side': 'SELL',
        'type': 'STOP_MARKET',
        "stopPrice": entry,
        'timeInForce': 'GTC',
        'quantity': quantity
    }
    response = cm_futures_client.new_order(**params)
    print(response)

if __name__ == "__main__":
    main()