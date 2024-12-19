from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
import pandas as pd
# Fetch Japan export data
japan_exports = pdr.get_data_fred("XTEXVA01JPQ667S", start="2010-01-01", end="2024-12-31")

# Fetch Japan import data
japan_imports = pdr.get_data_fred("XTIMVA01JPQ667S", start="2010-01-01", end="2024-12-31")

# Merge imports, exports, and unemployment rate data
japan_trade_data = pd.merge(
    japan_exports, japan_imports, left_index=True, right_index=True, how="inner"
)

# Plot Japan's exports and imports
japan_trade_data.plot(figsize=(12, 6), title="Japan Exports and Imports (2010-2024)")
plt.ylabel("Value (in Millions)")
plt.xlabel("Date")
plt.grid()
plt.legend(["Exports", "Imports"])
plt.savefig("/Users/sanhorn/Desktop/UIUC/Junior/econ460/Final Project/Plots/jp_imports_exports_piechart.png")
plt.show()
