import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mtl
import seaborn as sns
import numpy as np
from IPython.display import Image

# DOGECOIN Data
doge = pd.read_csv(r"DOGE-USD.csv")

doge['doge_vol_diff'] = doge['volume'].diff(periods=1);
doge['change'] = ((doge['high'] - doge['low']) / doge['high']) * 100
doge['date'] = pd.to_datetime(doge['date'])

#doge['date'] = pd.date_range('2021-01-01', periods=200, freq='D')
#doge = doge.set_index(['date'])
#print(doge.loc['2021-01-26':'2021-02-12'])

doge_cols = doge.iloc[:, [0,2]]
print(doge_cols)
doge_cols.set_index(['date'])
doge_sub = doge_cols['date'].loc['2021-01-06':'2021-02-10']
print(doge_sub)

sns.set(style="darkgrid")
color = sns.color_palette()[2]

fig1, ax = plt.subplots(figsize=(15,7))
plot = sns.lineplot(ax=ax, x=doge_sub['date'].values, y=doge_sub['high'], color='g')
ax.set(xticks=doge_sub['date'].values)
x_dates = doge_sub['date'].dt.strftime('%Y-%m-%d')
ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
ax.get_yaxis().set_major_formatter(
    mtl.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
#        label.set_visible(False)
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Plot of GME Volume')
plt.show()