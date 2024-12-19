import requests # Install requests module first.




def get_symbol_list():
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/active_instruments"

    response = requests.get(url)
    data = response.json()
    # print(data)
    return data

def get_ltp(symbol_name):
    url = f"https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair={symbol_name}"
    response = requests.get(url)
    data = response.json()
    last_tradeed_price = data[0]['price']
    return last_tradeed_price

symbol_list = get_symbol_list()

for symbol in symbol_list:
    ltp = get_ltp(symbol)
    print(symbol, ltp)
    # print()
# print(get_symbol_list())
