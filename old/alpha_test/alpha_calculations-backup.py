
import pandas as pd
import numpy as np
import os
from ta.momentum import RSIIndicator
from ta.volume import VolumeWeightedAveragePrice

 

# Create a list of all the csv files in the alpha_hist_data directory
csv_files = [f for f in os.listdir('alpha_hist_data') if f.endswith('_stock_data_full.csv')]

# Create an empty dataframe to store the cleaned data
cleaned_data = pd.DataFrame()

# Loop through each csv file and clean the data
for file in csv_files:
    # Read in the csv file
    data = pd.read_csv(os.path.join('alpha_hist_data', file))


    # Drop any rows with missing values
    data.dropna(inplace=True)
    
    # Convert the date column to a datetime object
    data['date'] = pd.to_datetime(data['date'])
    
    # Add the cleaned data to the cleaned_data dataframe
    cleaned_data = pd.concat([cleaned_data, data])
    

cleaned_data.columns = cleaned_data.columns.str.strip()
print(cleaned_data.columns)

# Set the date column as the index
cleaned_data.set_index('date', inplace=True)


 

# Create a list of unique tickers in the cleaned_data dataframe
tickers = cleaned_data['ticker'].unique()

# Loop through each ticker and calculate the RSI
for ticker in tickers:
    # Filter the cleaned_data dataframe by the current ticker
    ticker_data = cleaned_data[cleaned_data['ticker'] == ticker].copy()
    
    # Calculate the RSI for the current ticker
    rsi = RSIIndicator(close=ticker_data['close'], window=14).rsi()
    
     
    # Filter the cleaned_data dataframe by the current ticker
    # ticker_data = cleaned_data[cleaned_data['ticker'] == ticker]
    
    
    # Calculate the VWAP for the current ticker
    vwap = VolumeWeightedAveragePrice(high=ticker_data['high'], low=ticker_data['low'], close=ticker_data['close'], volume=ticker_data['volume'], window=14).volume_weighted_average_price()

    # Add the VWAP values to the cleaned_data dataframe
    cleaned_data.loc[cleaned_data['ticker'] == ticker, 'vwap'] = vwap

    # Add the RSI values to the cleaned_data dataframe
    cleaned_data.loc[cleaned_data['ticker'] == ticker, 'rsi'] = rsi
    

    
    # Calculate the percent change in close price for each day
    ticker_data['percent_change'] = ticker_data['close'].pct_change()
    
    # Calculate the rolling sum of percent change for a 1 day period
    ticker_data['rolling_sum'] = ticker_data['percent_change'].rolling(window=1).sum()
    
    # Find instances where the rolling sum is greater than or equal to 0.5
    ticker_data['spikes'] = np.where(ticker_data['rolling_sum'] >= 0.25, ticker_data['rolling_sum']*100, np.nan)
    
    # Add the spikes values to the cleaned_data dataframe
    cleaned_data.loc[cleaned_data['ticker'] == ticker, 'spikes'] = ticker_data['spikes']
    
    # Drop the temporary columns
    # ticker_data.drop(['percent_change', 'rolling_sum', 'spikes'], axis=1, inplace=True, errors='ignore')
    
     

# Calculate the number of spikes, the average, and the highest
num_spikes = cleaned_data['spikes'].count()
avg_spikes = cleaned_data['spikes'].mean()
highest_spike = cleaned_data['spikes'].max()

print("Number of spikes:", num_spikes)
print("Average spike:", avg_spikes)
print("Highest spike:", highest_spike)





# Save the cleaned data to a new csv file
cleaned_data.to_csv('stock_data_full_clean.csv')




 





# Save the data to a new csv file in the root directory
# indicators_data.to_csv('stock_data_full_clean_rsi_vwap.csv', index=False)




