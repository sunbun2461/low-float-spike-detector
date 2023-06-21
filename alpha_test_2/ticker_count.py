
import os

dir_path = '/Users/thomasario/Coding/AI/Low_float_ground_up/alpha_hist_data_2'

tickers = set()

for file_name in os.listdir(dir_path):
    if file_name.endswith('.csv'):
        ticker = file_name.split('_')[0]
        tickers.add(ticker)

total_tickers = len(tickers)

print(total_tickers)



