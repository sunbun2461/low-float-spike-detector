pip install -r requirements.txt




Sure, here's a revised version of your request with a focus on your file structure and adding more bullet points:

---

## Project Overview

This project aims to develop a machine learning model to predict low float stocks that are potentially about to spike. To accomplish this, we will analyze various technical indicators, including VWAP and RSI, to determine patterns that can indicate a potential spike.

### File Structure

The project's file structure is organized as follows:

- `data/`: This directory contains all the data files used in the project, including historical stock prices and financial statements.
- `models/`: This directory contains all the machine learning models developed for the project.
- `notebooks/`: This directory contains all the Jupyter notebooks used for data cleaning, preprocessing, and analysis.
- `scripts/`: This directory contains all the scripts used for running the machine learning models and generating predictions.
- `README.md`: This file provides an overview of the project, its objectives, and file structure.

### Technical Indicators

The following technical indicators will be used to determine patterns and signals for a potential spike in a low float stock:

- VWAP (Volume Weighted Average Price)
- RSI (Relative Strength Index)
- Historical stock prices
- Financial statements (Income Statement, Balance Sheet, Cash Flow Statement)

### Hypothesis

We believe that the following factors may be associated with a potential spike in low float stocks:

- Strong and increasing trading volume
- Favorable financial statements (e.g., high revenue, low debt)
- Positive market sentiment and news
- Increasing demand for a company's products or services

### Machine Learning

We will use a supervised learning approach to develop a machine learning model that can predict whether a low float stock is about to spike. We will train our model on historical data and use various metrics to evaluate its performance, including accuracy, precision, recall, and F1-score.

To train our model, we will use a decision tree-based approach that involves the following steps:

1. Preprocessing the data by cleaning, normalizing, and scaling it.
2. Splitting the data into training and testing sets.
3. Training the model on the training set using a decision tree algorithm.
4. Evaluating the model's performance on the testing set using various metrics.
5. Optimizing the model's hyperparameters using cross-validation.

### Conclusion

By analyzing various technical indicators and developing a machine learning model to predict potential spikes in low float stocks, we hope to identify profitable investment opportunities and generate significant returns. Our project's file structure and methodology ensure that our analysis is rigorous and transparent, enabling us to identify patterns and signals that can provide valuable insights into the stock market.



=====================================================================================
=====================================================================================


The Volume Weighted Average Price (VWAP) and the Relative Strength Index (RSI) are two commonly used technical indicators in trading analysis. In the context of your application, we can use these indicators to help identify potential stocks that are about to spike. 

The VWAP is a trend indicator that calculates the average price of a stock based on its trading volume. This indicator can help us determine the average price that market participants are paying for a stock, which can be useful in identifying price levels that may be significant to the market. By monitoring the VWAP, we can determine if a stock's price is above or below its average value, which can help us identify potential opportunities for buying or selling.

On the other hand, the RSI is a momentum indicator that measures the strength of a stock's recent price movements. It is calculated by comparing the average gains and losses of a stock over a specified period of time. The RSI value can range from 0 to 100, with values above 70 typically indicating overbought conditions and values below 30 indicating oversold conditions. By monitoring the RSI, we can identify when a stock is overbought or oversold, which can help us identify potential opportunities for buying or selling.

In your application, we can use these indicators to identify stocks that are potentially undervalued or overvalued based on their current price relative to their VWAP and RSI values. By analyzing historical data, we can also identify patterns in these indicators that are associated with stock price spikes. For example, we may find that stocks with RSI values below 30 and prices below their VWAP tend to experience price spikes shortly after. 

Overall, the VWAP and RSI indicators can be valuable tools in helping us identify potential opportunities for trading and predicting price movements in the stock market. By leveraging machine learning algorithms to analyze these indicators and other relevant data, we can develop a more robust and accurate trading strategy.



=====================================================================================

=====================================================================================







Welcome to Alpha Vantage! Your API key is: CSLRUN3DYH8OF0XK.

Sure, here's a README that summarizes our project and its objectives:

---

# Low Float Penny Stock Trading Bot

This project aims to build a trading bot for low float penny stocks using technical analysis indicators such as VWAP and RSI to make buy and sell decisions. The bot will make use of historical and real-time stock market data to identify low float stocks that are likely to experience large price movements in the future. 

## Objectives

The primary objectives of this project are:

1. Collecting historical and real-time stock market data for low float penny stocks using APIs.
2. Analyzing the data using technical analysis indicators such as VWAP and RSI to identify patterns that can predict large price movements.
3. Building a trading bot that uses these patterns to make buy and sell decisions.
4. Evaluating the bot's performance over time and making improvements as needed.

## Approach

We will be using Python to build this app since it has a lot of libraries and frameworks that can be useful for web scraping, data analysis, and machine learning. We will also use APIs such as Alpha Vantage, Yahoo Finance, and IEX Cloud to retrieve stock market data.

To identify patterns in the data, we will use machine learning algorithms such as linear regression, decision trees, and neural networks. We will train these models on historical data and use them to make predictions about future price movements.

Finally, we will build a trading bot that uses these predictions to make buy and sell decisions. We will use a scheduler library, like schedule, to run the Python script at a specific time interval, such as every 10 minutes.

## Folder Structure

- `api/`: Contains the code for making API requests.
- `historical_data/`: Contains the CSV file with historical data.
- `models/`: Can be used to store any machine learning models we may use.
- `utils/`: Contains various utility functions including those for data processing and text notifications.

## Conclusion

This app has the potential to identify profitable trading opportunities in low float penny stocks using technical analysis indicators and machine learning algorithms. By continuously analyzing and improving the bot's performance, we can potentially achieve better returns on investment over time.



## RSI VWAP AND SPIKE DETECTION



It would make sense to implement the spike detection functionality now, so that we can use it in conjunction with the RSI and VWAP indicators.

As for the RSI and VWAP indicators, using both of them together could give us more confidence in our predictions. Here are some ideas for how to use them:

We could identify stocks where the RSI has crossed above the oversold threshold (typically 30), which indicates that the stock may be oversold and due for a price increase. We could then look for confirmation of this by checking if the VWAP is trending upwards, which could indicate increased buying pressure. If both conditions are met, we could consider buying the stock.

On the other hand, if the RSI has crossed below the overbought threshold (typically 70), which indicates that the stock may be overbought and due for a price decrease, we could look for confirmation of this by checking if the VWAP is trending downwards, which could indicate increased selling pressure. If both conditions are met, we could consider shorting the stock.

We could also look for divergences between the RSI and VWAP. For example, if the stock price is trending upwards but the RSI is trending downwards, this could indicate a bearish divergence and a potential price decrease. Similarly, if the stock price is trending downwards but the VWAP is trending upwards, this could indicate a bullish divergence and a potential price increase.

We could combine the RSI and VWAP into a single score or signal, such as a weighted average of the two. This could give us a more nuanced understanding of the stock's overall trend and momentum, and could help us identify potential buying or selling opportunities more effectively.



## INDICATORS AND GATHER INFO CODE 

Sure, here's an outline of the functions we'll need based on your idea:

1. **get_spikes(data, threshold):** This function will take in a DataFrame of historical OHLCV data and a threshold value (e.g. 50%) and return a new DataFrame containing only the rows where the price increased by at least the threshold percentage in one day.

2. **get_avg_volume(data, start_time, end_time):** This function will take in a DataFrame of OHLCV data and a start and end time (e.g. the hour leading up to the spike start) and return the average volume during that time period.

3. **get_rsi(data, window):** This function will take in a DataFrame of OHLCV data and a window value (e.g. 14) and return a new DataFrame containing the RSI values for each row.

4. **get_vwap(data, window):** This function will take in a DataFrame of OHLCV data and a window value (e.g. 20) and return a new DataFrame containing the VWAP values for each row.

5. **find_spikes(data, rsi_threshold, vwap_trend):** This function will take in a DataFrame of OHLCV data, an RSI threshold value (e.g. 30), and a Boolean value indicating whether the VWAP trend should be upward or not. It will then use the above functions to find the average volume during the hour leading up to historical price spikes where the RSI was above the threshold and the VWAP trend met the specified criteria. The function will return the average volume for those spikes.

Let me know if this outline makes sense or if you have any further suggestions!