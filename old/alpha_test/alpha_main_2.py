
import csv
import requests
import os
import time
import pandas as pd

API_KEY = "CSLRUN3DYH8OF0XK"
INTERVAL = "60min"
ADJUSTED = "false"
csv_count = 0

with open('stocks.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        SYMBOL = row[0]
        if not os.path.exists("alpha_hist_data_2"):
            os.makedirs("alpha_hist_data_2")
        for year in range(1, 3):
            for month in range(1, 13):
                SLICE = f"year{year}month{month}"
                CSV_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol={SYMBOL}&interval={INTERVAL}&slice={SLICE}&adjusted={ADJUSTED}&apikey={API_KEY}"
                with requests.Session() as s:
                    download = s.get(CSV_URL)
                    decoded_content = download.content.decode('utf-8')
                    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                    my_list = list(cr)
                    df = pd.DataFrame(my_list)
                    print(SYMBOL)
                    print(df)
                    with open(f"alpha_hist_data_2/{SYMBOL}_{INTERVAL}_{SLICE}.csv", "w") as f:
                        writer = csv.writer(f)
                        writer.writerows(my_list)
                    csv_count += 1
                    print(f"Total CSV files created: {csv_count}")
                time.sleep(11)




