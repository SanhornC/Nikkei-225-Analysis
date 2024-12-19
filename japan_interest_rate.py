from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

japan_interest_rate = pdr.get_data_fred("IR3TIB01JPQ156N", start="2024-01-01", end="2024-12-31")

# Plot Japan interest rate
japan_interest_rate.plot(figsize=(12, 6), title="Japan Interest Rate (2010-2024)", color="blue")
plt.ylabel("Interest Rate (%)")
plt.xlabel("Date")
plt.grid()
plt.savefig("/Users/sanhorn/Desktop/UIUC/Junior/econ460/Final Project/Plots/jp_interest_rate2024.png")
plt.show()
