import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math, numpy as np
from IPython.display import Image


# GME Data
gme = pd.read_csv(r"GME_stock.csv")

gme['gme_vol_diff'] = gme['volume'].diff(periods=-1);
pd.set_option('display.max_columns', None)
print(gme.columns)
print(gme.head(5))

doge = pd.read_csv(r"DOGE-USD.csv")

doge['doge_vol_diff'] = doge['volume'].diff(periods=1);
pd.set_option('display.max_columns', None)
print(doge.columns)
print(doge.tail(5))

#print(math.isclose(np.var(gme['volume']), 0))

sns.displot(data=gme, x='high', hue='volume', kind='kde', palette='tab10', rug=True)
plt.show()