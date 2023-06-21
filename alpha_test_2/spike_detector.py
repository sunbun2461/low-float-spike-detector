import os
import pandas as pd

dir_path = '/Users/thomasario/Coding/AI/Low_float_ground_up/alpha_hist_data_2'
csv_files = [f for f in os.listdir(dir_path) if f.endswith('.csv')]
csv_files = sorted(csv_files, key=lambda x: os.path.getmtime(os.path.join(dir_path, x)))

spikes_count = {}
top_spikes = []

for filename in reversed(csv_files):
    file_path = os.path.join(dir_path, filename)
    
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Add a column for the ticker based on the filename
        ticker = filename.split('_')[0]
        df['ticker'] = ticker
        
        # Convert the 'time' column to datetime
        df['time'] = pd.to_datetime(df['time'])
        
        # Calculate the percent change relative to the previous day's closing price
        df['percent_change'] = pd.to_numeric(df['close'], errors='coerce').pct_change() * 100
        
        # Find spikes where the percent change is greater than or equal to 25%
        df['spike'] = df['percent_change'] >= 25
        
        # Calculate the cumulative percent change for each spike
        spike_indices = df[df['spike']].index
        for i in range(len(spike_indices) - 1):
            start_index = spike_indices[i]
            end_index = spike_indices[i+1]
            df.loc[start_index:end_index, 'cumulative_percent'] = df.loc[start_index:end_index, 'percent_change'].cumsum()
        
        # Save the modified DataFrame to a new CSV file with spikes
        spikes_dir = os.path.join(dir_path, 'spikes')
        os.makedirs(spikes_dir, exist_ok=True)
        spikes_file = os.path.splitext(filename)[0] + '_spikes.csv'
        spikes_file_path = os.path.join(spikes_dir, spikes_file)
        df.to_csv(spikes_file_path, index=False)
        
        # Count the total number of spikes for the ticker
        total_spikes = df['spike'].sum()
        spikes_count[ticker] = spikes_count.get(ticker, 0) + total_spikes
        
        # Find the highest top 5 percentage spikes
        top_spike_percentages = df.loc[df['spike'], 'percent_change'].nlargest(25)
        top_spikes.extend(top_spike_percentages)
        
        print(f"Ticker: {ticker}, Total Spikes: {total_spikes}")
    except KeyError:
        print(f"Skipping file: {filename} - 'time' column not found")

# Count the total number of spikes overall
total_spikes_overall = sum(spikes_count.values())

# Print the total number of spikes overall
print(f"Total Spikes Overall: {total_spikes_overall}")

# Print the highest top 5 percentage spikes
print("Top 25 Percentage Spikes:")
for i, spike_percentage in enumerate(sorted(top_spikes, reverse=True)[:25], 1):
    print(f"Rank {i}: {spike_percentage}%")
