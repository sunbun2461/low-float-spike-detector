import pandas as pd
import requests
import os
import csv 
import datetime

API_KEY = "CSLRUN3DYH8OF0XK"

tickers_with_data = 0
tickers_without_data = 0

import time

with open('/Users/thomasario/Coding/AI/Low_float_ground_up/stocks-old.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        ticker = row[0]
        url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + ticker + "&outputsize=full&apikey=" + API_KEY
        response = requests.get(url)
        try:
            data = response.json()
        except json.decoder.JSONDecodeError:
            print(f"Error: No data found for {ticker}")
            tickers_without_data += 1
            continue
        if 'Time Series (Daily)' in data:
            df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
            df.columns = [col.split(".")[1] for col in df.columns]
            df['ticker'] = ticker
            df['date'] = pd.to_datetime(df.index)
            df.set_index('date', inplace=True)
            tickers_with_data += 1
            if not os.path.exists('alpha_hist_data'):
                os.makedirs('alpha_hist_data')
            df.to_csv(f'./alpha_hist_data/{ticker}_stock_data_full.csv', index=True, header=True)

            print(f"Earliest retrieved data for {ticker}: {df.index[-1]}")
        else:
            tickers_without_data += 1
            print(f"No data found for {ticker}")
        time.sleep(12) # Wait for 12 seconds before making the next API call

    print(f"Tickers with data: {tickers_with_data}")
    print(f"Tickers without data: {tickers_without_data}")
    print(f"Total tickers: {tickers_with_data + tickers_without_data}")
