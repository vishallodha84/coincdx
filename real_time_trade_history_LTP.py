import requests  # Install requests module first.
# url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair={instrument_name}"
#sample_url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair=B-MKR_USDT"
# url = "https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair=B-BTC_USDT"
# response = requests.get(url)
# data = response.json()
# last_tradeed_price = data[0]['price']
# print(last_tradeed_price)

def get_ltp(symbol_name):
    url = f"https://api.coindcx.com/exchange/v1/derivatives/futures/data/trades?pair={symbol_name}"
    response = requests.get(url)
    data = response.json()
    last_tradeed_price = data[0]['price']
    return last_tradeed_price

symbol_1 = 'B-BTC_USDT'
symbol_2 = 'B-ETH_USDT'
symbol_3 = 'B-DOGH_USDT'
symbol_4 = 'B-XRP_USDT'

print(get_ltp(symbol_1))
print(get_ltp(symbol_2))
print(get_ltp(symbol_3))
print(get_ltp(symbol_4))