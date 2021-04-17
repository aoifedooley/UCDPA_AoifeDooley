import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# GME Data
gme = pd.read_csv(r"GME_stock.csv")
print(gme.shape)
print(gme.dtypes)

# GME % INCREASE
gme["change"] = ((gme["high"] - gme["low"]) / gme["high"]) * 100

# DOGECOIN Data
doge = pd.read_csv(r"DOGE-USD.csv")
print(doge.shape)
print(doge.dtypes)

# DOGE % INCREASE
doge["change"] = ((doge["high"] - doge["low"]) / doge["high"]) * 100

# MERGE GME AND DOGECOIN TABLES
gme_doge = gme.merge(doge, on="date", how="left", suffixes=["_gme", "_doge"])
pd.set_option('display.max_columns', None)
print(gme_doge.head())
print(gme_doge.shape)

# Null values present as DOGE ranges from 2014-2021, whereas GME ranges from 2002-2021
print(gme_doge.isnull())
print(gme_doge.isnull().sum())

# MERGED TABLES GRAPH
x = gme_doge['date'].head(10)
y1 = gme_doge['change_gme'].head(10)
y2 = gme_doge['change_doge'].head(10)

plt.gca().invert_xaxis() # REF: https://stackoverflow.com/questions/2051744/reverse-y-axis-in-pyplot

plt.plot(x,y1, marker="o", linestyle="-", color="r", label="GME")
plt.plot(x,y2,marker="*", linestyle="-.", color="b", label='DOGECOIN')
plt.title("GME vs DOGE Stock Price")
plt.xlabel("Date")
plt.ylabel("Share Price")
plt.legend()
plt.tight_layout()
plt.show()