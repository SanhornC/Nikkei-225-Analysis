from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

# Fetch U.S. inflation rate (annual % change)
us_inflation = pdr.get_data_fred("EXPINF24YR", start="2000-01-01", end="2024-12-31")


plt.figure(figsize=(12, 6))
plt.plot(us_inflation.index, us_inflation, label="U.S. Inflation Rate", color="red")
plt.title("U.S. Inflation Rate (2000-2024)")
plt.ylabel("Inflation Rate (%)")
plt.xlabel("Date")
plt.grid()
plt.legend()
plt.savefig("/Users/sanhorn/Desktop/UIUC/Junior/econ460/Final Project/Plots/us_inflation_rate.png")
plt.show()