import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

gme = pd.read_csv(r"GME_stock.csv")
doge = pd.read_csv(r"DOGE-USD.csv")

# GME GRAPH

x = gme['date'].head(10)
y1 = gme['high'].head(10)
y2 = gme['low'].head(10)

plt.gca().invert_xaxis() # REF: https://stackoverflow.com/questions/2051744/reverse-y-axis-in-pyplot

plt.plot(x,y1, marker="o", linestyle="-", color="r", label="high price")
plt.plot(x,y2,marker="*", linestyle="-.", color="b", label='low price')
plt.title("Plot of GME Stock Price")
plt.xlabel("Date")
plt.ylabel("Share Price")
plt.legend()
plt.tight_layout()
plt.show()

# DOGE GRAPH

x = doge['date'].iloc[2316:2326]
y1 = doge['high'].tail(10)
y2 = doge['low'].tail(10)

plt.plot(x,y1, marker="o", linestyle="-", color="r", label="high price")
plt.plot(x,y2,marker="*", linestyle="-.", color="b", label='low price')
plt.title("Plot of DOGECOIN Stock Price")
plt.xlabel("Date")
plt.ylabel("Share Price")
plt.legend()
plt.tight_layout()
plt.show()