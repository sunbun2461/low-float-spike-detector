
import os
import pandas as pd

path = "alpha_hist_data_2/spikes"
true_count = 0
percent_changes = []

for filename in os.listdir(path):
    if filename.endswith(".csv"):
        file_path = os.path.join(path, filename)
        df = pd.read_csv(file_path)
        true_count += df['spike'].value_counts().get(True, 0)
        if df['spike'].value_counts().get(True, 0) > 0:
            percent_changes.append(df.loc[df['spike'] == True, 'percent_change'])
            
print("Percent changes for TRUE entries in spikes column:", percent_changes)
print("Number of TRUE entries in spikes column:", true_count)


