from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

# Fetch interest rate data from FRED
start_date = "2010-01-01"
end_date = "2024-12-31"
interest_rates = pdr.get_data_fred("FEDFUNDS", start=start_date, end=end_date)


nikkei_data = yf.Ticker("^N225").history(period="10y")[["Close"]]
nikkei_data.rename(columns={"Close": "Nikkei 225"}, inplace=True)

start_date = "2024-07-01"
end_date = "2024-11-30"

# Filter Nikkei 225 data
nikkei_filtered = nikkei_data.loc[start_date:end_date]

# Filter U.S. interest rate data
interest_filtered = interest_rates.loc[start_date:end_date]

# Plot Nikkei 225
plt.figure(figsize=(12, 6))
plt.plot(nikkei_filtered.index, nikkei_filtered["Nikkei 225"], label="Nikkei 225", color="blue")
plt.title("Nikkei 225 (July-August 2024)")
plt.ylabel("Nikkei 225 Index")
plt.xlabel("Date")
plt.grid()
plt.legend()
plt.savefig("/Users/sanhorn/Desktop/UIUC/Junior/econ460/Final Project/Plots/nikkei_july_nov.png")
plt.show()

# Plot U.S. Interest Rates
plt.figure(figsize=(12, 6))
plt.plot(interest_filtered.index, interest_filtered["FEDFUNDS"], label="U.S. Fed Funds Rate", color="red")
plt.title("U.S. Federal Funds Rate (July-August 2024)")
plt.ylabel("Interest Rate (%)")
plt.xlabel("Date")
plt.grid()
plt.legend()
plt.savefig("/Users/sanhorn/Desktop/UIUC/Junior/econ460/Final Project/Plots/us_interest_rate.png")
plt.show()


