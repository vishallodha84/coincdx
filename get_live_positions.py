import hmac
import hashlib
import base64
import json
import time
import requests
import pandas as pd



def get_positions(key, secret):
    # python3
    secret_bytes = bytes(secret, encoding='utf-8')
    # Generating a timestamp
    timeStamp = int(round(time.time() * 1000))
    body = {
            "timestamp":timeStamp , # EPOCH timestamp in seconds
            "page": "1", #no. of pages needed
            "size": "10" #no. of records needed
            }
    json_body = json.dumps(body, separators = (',', ':'))
    signature = hmac.new(secret_bytes, json_body.encode(), hashlib.sha256).hexdigest()
    url = "https://api.coindcx.com/exchange/v1/derivatives/futures/positions"
    headers = {
        'Content-Type': 'application/json',
        'X-AUTH-APIKEY': key,
        'X-AUTH-SIGNATURE': signature
    }

    response = requests.post(url, data = json_body, headers = headers)
    data = response.json()
    df = pd.DataFrame(data)
    # df.to_csv('live_positions.csv')
    df.to_excel('live_positions_again.xlsx')
    # print(df)
    return df


# Enter your API Key and Secret here. If you don't have one, you can generate it from the website.
key = "xxxx"
secret = "xxxx"

print(get_positions(key,secret))
