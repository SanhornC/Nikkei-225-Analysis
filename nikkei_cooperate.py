import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define tickers
tickers = {
    "Nikkei 225": "^N225",
    "Toyota": "7203.T",
    "Mitsubishi": "8058.T",
    "Sony": "6758.T",
    "Hitachi": "6501.T",
    "SoftBank": "9984.T"
}

# History 8 Years
data = {name: yf.Ticker(ticker).history(period="max") for name, ticker in tickers.items()}

common_index = data["Nikkei 225"].index  

for name, df in data.items():
    common_index = common_index.intersection(df.index)

for name in data:
    data[name] = data[name].reindex(common_index)

closing_prices = pd.DataFrame({
    name: df['Close'] for name, df in data.items()
})

closing_prices.index = common_index

# Plot stock prices
closing_prices.plot(figsize=(12, 6), title="max Historical Stock Prices")
plt.ylabel("Price (JPY)")
plt.xlabel("Date")
plt.legend(loc="best")
plt.grid()
plt.savefig("/Users/sanhorn/Desktop/UIUC/Junior/econ460/Final Project/Plots/max_historical_stock_prices.png")
plt.show()




