from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

japan_unemployment_rate = pdr.get_data_fred("LRUN64TTJPM156S", start="2010-01-01", end="2024-12-31")

japan_unemployment_rate.plot(figsize=(12, 6), title="Japan Unemployment Rate (2010-2024)", color="red")
plt.ylabel("Unemployment Rate (%)")
plt.xlabel("Date")
plt.grid()
plt.savefig("/Users/sanhorn/Desktop/UIUC/Junior/econ460/Final Project/Plots/jp_employment_rate.png")
plt.show()