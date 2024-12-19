import hmac
import hashlib
import base64
import json
import time
import requests

# Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
key = "xxxx"
secret = "xxxxx"

# python3
secret_bytes = bytes(secret, encoding='utf-8')

# Generating a timestamp
timeStamp = int(round(time.time() * 1000))

def place_order(order_side, coin_name, limit_price, stop_price, limit_qty, leverage):

    body = {
            "timestamp":timeStamp , # EPOCH timestamp in seconds
        #     "order": {
        #     "side": "buy", # buy OR sell
        #     "pair": "B-SOL_USDT", # instrument.string
        #     "order_type": "limit_order", # market_order OR limit_order 
        #     "price": "160", #numeric value
        # # "stop_price": "0.2962", #numeric value
        #     "total_quantity": 1, #numerice value
        #     "leverage": 1, #numerice value
        #     "notification": "email_notification", # no_notification OR email_notification OR push_notification
        #     "time_in_force": "good_till_cancel", # good_till_cancel OR fill_or_kill OR immediate_or_cancel
        #     "hidden": False, # True or False
        #     "post_only": False # True or False
        #     }
        "order": {
            "side": order_side, # buy OR sell
            "pair": coin_name, # instrument.string
            "order_type": "limit_order", # market_order OR limit_order 
            "price": limit_price, #numeric value
            "stop_price": stop_price, #numeric value
            "total_quantity": limit_qty, #numerice value
            "leverage": leverage, #numerice value
            "notification": "email_notification", # no_notification OR email_notification OR push_notification
            "time_in_force": "good_till_cancel", # good_till_cancel OR fill_or_kill OR immediate_or_cancel
            "hidden": False, # True or False
            "post_only": False # True or False
            }
            }

    json_body = json.dumps(body, separators = (',', ':'))

    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()

    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/orders/create"

    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    # print(data)
    return data

order1 = place_order('buy',"B-SOL_USDT",160,0,1,1)
print("SOL order is placed:", order1)
