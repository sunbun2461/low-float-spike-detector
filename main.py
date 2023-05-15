import finnhub
import pandas as pd
import requests
import chardet
import codecs


def get_ochl_volume_data():
    # Set API key for Finnhub
    FINNHUB_API_KEY = "ch7ibbhr01qt83gcaok0ch7ibbhr01qt83gcaokg"

    # Setup client
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)

    # Read in stocks.csv dataframe
    stocks_df = pd.read_csv('/Users/thomasario/Coding/AI/Low_float_ground_up/stocks.csv', nrows=50)
    
    # Create a new dataframe to store the OCHL volume data
    ochl_volume_df = pd.DataFrame()

    # Loop through each Ticker in the stocks dataframe
    for i in range(0, len(stocks_df), 50):
        # Retrieve OCHL volume data for the last year using Finnhub API
        for Ticker in stocks_df['Ticker'][i:i+50]:
            try:
                print(f"Working on {Ticker}")
                ochl_volume_data = finnhub_client.stock_candles(Ticker, 'D', int(pd.Timestamp("now").timestamp())-31536000, int(pd.Timestamp("now").timestamp()), adjusted=True, count=365) # retrieve OCHL volume data for the last year using Finnhub API

                # Create a new dataframe to store the OCHL volume data for this Ticker
                stock_ochl_volume_df = pd.DataFrame(ochl_volume_data, columns=['o','c','h','l','s','t','v'])
                stock_ochl_volume_df['Ticker'] = Ticker 

                # Set the index of the dataframe to be the date
                stock_ochl_volume_df.set_index('t', inplace=True)

                # Append the stock dataframe to the ochl_volume_df dataframe
                ochl_volume_df = pd.concat([ochl_volume_df, stock_ochl_volume_df])

                # Save the ochl_volume_df dataframe to a new csv file with name of Ticker and dates as filenames
                stock_ochl_volume_df = ochl_volume_df[ochl_volume_df['Ticker'] == Ticker]
                stock_ochl_volume_df.to_csv(f'./hist_data/{Ticker}_ochl_volume.csv')
                import time
                time.sleep(1)
            except:
                print(f"Problem with {Ticker}, moving on to next")
                continue


            

    # Calculate RSI for each stock and save to new csv file
    for Ticker in stocks_df['Ticker']:
        # Read in ochl_volume csv file
        with open(f'./hist_data/{Ticker}_ochl_volume.csv', 'rb') as f:
            result = chardet.detect(f.read())
        stock_ochl_volume_df = pd.read_csv(f'./hist_data/{Ticker}_ochl_volume.csv', encoding=result['encoding'])
        
        # Calculate RSI
        delta = stock_ochl_volume_df['c'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        # Add RSI column to dataframe
        stock_ochl_volume_df['RSI'] = rsi
        
        # Set the index of the dataframe to be the date
        stock_ochl_volume_df.set_index('t', inplace=True)
        
        # Save dataframe to new csv file with _rsi on the end
        stock_ochl_volume_df.to_csv(f'./hist_data/{Ticker}_ochl_volume_rsi.csv')



        
    # Calculate VWAP for each stock and save to new csv file
    for Ticker in stocks_df['Ticker']:
        # Read in ochl_volume_rsi csv file
        with open(f'./hist_data/{Ticker}_ochl_volume_rsi.csv', 'rb') as f:
            result = chardet.detect(f.read())
        stock_ochl_volume_rsi_df = pd.read_csv(f'./hist_data/{Ticker}_ochl_volume_rsi.csv', encoding=result['encoding'])
        
        # Calculate VWAP
        stock_ochl_volume_rsi_df['TP'] = (stock_ochl_volume_rsi_df['h'] + stock_ochl_volume_rsi_df['l'] + stock_ochl_volume_rsi_df['c']) / 3
        stock_ochl_volume_rsi_df['Cumulative TP'] = stock_ochl_volume_rsi_df['TP'] * stock_ochl_volume_rsi_df['v']
        stock_ochl_volume_rsi_df['Cumulative Volume'] = stock_ochl_volume_rsi_df['v'].cumsum()
        stock_ochl_volume_rsi_df['VWAP'] = stock_ochl_volume_rsi_df['Cumulative TP'] / stock_ochl_volume_rsi_df['Cumulative Volume']
        
        # Set the index of the dataframe to be the date
        stock_ochl_volume_rsi_df.set_index('t', inplace=True)
 
        # Save dataframe to new csv file with _vwap on the end
        stock_ochl_volume_rsi_df.to_csv(f'./hist_data/{Ticker}_ochl_volume_rsi_vwap.csv')





    # Loop through each Ticker in the stocks dataframe
    for Ticker in stocks_df['Ticker']:
        try:
            # Read in ochl_volume_rsi_vwap csv file
            with open(f'./hist_data/{Ticker}_ochl_volume_rsi_vwap.csv', 'rb') as f:
                result = chardet.detect(f.read())
            stock_ochl_volume_rsi_vwap_df = pd.read_csv(f'./hist_data/{Ticker}_ochl_volume_rsi_vwap.csv', encoding=result['encoding'])
            # Set the index of the dataframe to be the date
            stock_ochl_volume_rsi_vwap_df.set_index('t', inplace=True)
            # Create a new column to store the percentage change in stock price over a 48 hour period
            stock_ochl_volume_rsi_vwap_df['Price % Change'] = stock_ochl_volume_rsi_vwap_df['c'].pct_change(periods=1)

            # Create a new column to store whether the stock has spiked or not
            stock_ochl_volume_rsi_vwap_df['Spike'] = stock_ochl_volume_rsi_vwap_df.apply(lambda row: row['Price % Change'] if row['Price % Change'] >= 0.5 else 0, axis=1)

            # Save dataframe to new csv file with _spike on the end
            stock_ochl_volume_rsi_vwap_df.to_csv(f'./hist_data/{Ticker}_ochl_volume_rsi_vwap_spike.csv')

            # Create a new dataframe to store the spikes data
            spikes_df = pd.DataFrame(columns=['Ticker', 'Date', 'Price % Change'])

            # Loop through each row in the stock dataframe and add any spikes to the spikes dataframe
            for index, row in stock_ochl_volume_rsi_vwap_df.iterrows():
                if row['Spike'] > 0:
                    spikes_df = spikes_df._append({'Ticker': Ticker, 'Date': index, 'Price % Change': row['Price % Change']}, ignore_index=True)

            # Save the spikes dataframe to a new csv file with name of Ticker and dates as filenames
            spikes_df.to_csv(f'./hist_data/{Ticker}_spikes.csv', index=False)

            # Print number of stocks that spiked and what they were percentage wise
            num_spikes = len(spikes_df)
            percent_spikes = num_spikes / len(stock_ochl_volume_rsi_vwap_df) * 100
            print(f"{Ticker}: {num_spikes} stocks spiked ({percent_spikes:.2f}%)")
        except (pd.errors.EmptyDataError, pd.errors.ParserError, FileNotFoundError) as e:
            print(f"Error with {Ticker}: {e}")
            continue


    # Return the ochl_volume_df dataframe
    return ochl_volume_df

if __name__ == '__main__':
    # Call the get_ochl_volume_data() function to retrieve the data
    ochl_volume_df = get_ochl_volume_data()
    print(ochl_volume_df)

