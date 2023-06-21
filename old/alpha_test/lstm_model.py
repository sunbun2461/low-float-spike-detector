import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Load the cleaned data
cleaned_data = pd.read_csv('spike_data.csv')

# Select relevant features and target variable
features = ['rsi', 'vwap', 'volume']  # Adjust this based on your desired features
target = 'spikes'

# Drop rows with missing values in the target variable
cleaned_data.dropna(subset=[target], inplace=True)

tickers = cleaned_data['ticker'].unique()

# Create a dictionary to store models and evaluation metrics
models = {}

# Iterate over each ticker
for ticker in tickers:
    print(f"Training model for ticker: {ticker}")

    # Split the data into training and testing datasets
    X_train, X_test, y_train, y_test = train_test_split(cleaned_data[features], cleaned_data[target], test_size=0.2, random_state=42)

    # Create and fit the imputer to handle missing values
    imputer = SimpleImputer()
    imputer.fit(X_train)

    # Transform the training and testing data by filling missing values
    X_train = imputer.transform(X_train)
    X_test = imputer.transform(X_test)

    # Reshape the data for LSTM
    X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
    X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

    # Create and train the LSTM model
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(1, len(features))))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, epochs=50, verbose=0)

    # Make predictions on the testing dataset
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    models[ticker] = {'model': model, 'mse': mse, 'r2': r2}

    print("Mean Squared Error:", mse)
    print("R-squared:", r2)

# Further analysis or usage with the saved models and metrics
# You can access the models and their results using the ticker as the key
for ticker, model_info in models.items():
    model = model_info['model']
    mse = model_info['mse']
    r2 = model_info['r2']
    
    # Perform additional analysis or use the models as needed
    # For example, you can make predictions on new data using the stored models
    # or compare the evaluation metrics across different tickers.
