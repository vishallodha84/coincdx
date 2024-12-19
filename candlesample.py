import requests
import pandas as pd
from datetime import datetime
import time
import pandas_ta as ta

def conver_date_to_epoch(start_date_str, end_date_str, date_format='%Y-%m-%d'):
    start_epoch = int(time.mktime(datetime.strptime(start_date_str,date_format).timetuple()))
    end_epoch = int(time.mktime(datetime.strptime(end_date_str,date_format).timetuple()))
    return start_epoch, end_epoch



def convert_epoch_to_human_readable(df):
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    return df

# start_date_str = '2024-01-01'
# end_date_str = '2024-07-15'
# from_epoch, to_epoch = conver_date_to_epoch(start_date_str,end_date_str)
# print(from_epoch,to_epoch)
# exit(0)


def get_candlestick_data(symbol, from_epoch, to_epoch, interval):
    url = "https://public.coindcx.com/market_data/candlesticks"
    query_params = {
        # "pair": "B-MKR_USDT",
        # # "from": 1704100940,
        # # "to": 1705483340,
        # "from": from_epoch,
        # "to": to_epoch,
        # "resolution": "1D",
        "pair": symbol,
        "from": from_epoch,
        "to": to_epoch,
        "resolution": interval,  # '1' OR '5' OR '60' OR '1D'
        "pcode": "f"
    }
    response = requests.get(url, params=query_params)
    if response.status_code == 200:
        data = response.json()
        # Process the data as needed
        df = pd.DataFrame(data['data'])
        df = convert_epoch_to_human_readable(df)
        df['rsi'] = ta.rsi(close=df['close'],length=14)
        # df.to_csv('esi_excel.csv')
        # print(df)
        df.to_csv(f'{symbol}_rsi_value.csv')
        df.to_excel(f'{symbol}_rsi_value.xlsx')
        return df
    else:
        print(f"Error: {response.status_code}, {response.text}")




start_date_str = '2024-01-01'
end_date_str = '2024-07-15'
from_epoch, to_epoch = conver_date_to_epoch(start_date_str,end_date_str)
symbol_list = ['B-BTC_USDT', 'B-ETH_USDT', 'B-DOGE_USDT', 'B-SOL_USDT']


for symbol in symbol_list :
    get_candlestick_data(symbol, from_epoch, to_epoch, "5")