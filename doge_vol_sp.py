import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mtl
import seaborn as sns
import numpy as np
from IPython.display import Image

# DOGE Data
doge = pd.read_csv(r"DOGE-USD.csv")

# DOGE Volume %
doge_vol_diff = doge['volume'].diff(periods=-1)
doge['vol_diff'] = ((doge["volume"] - doge_vol_diff) / doge["volume"]) * 100

# DOGE SP % INCREASE
doge["change"] = ((doge["high"] - doge["low"]) / doge["high"]) * 100

# Converting the date column into datetime index
doge['date'] = pd.to_datetime(doge['date'], infer_datetime_format=True)
doge.set_index('date', inplace=True)

fig1, ax = plt.subplots(figsize=(10, 5))
top = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=10)
bottom = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=10)
top.bar(doge.index, doge['high'], color='midnightblue')
bottom.bar(doge.index, doge['volume'], color='midnightblue')

top.axes.get_xaxis().set_visible(False)
top.set_title('DOGE Share Price Analysis')
top.set_ylabel('Highest Price')
bottom.set_ylabel('Volume')

plt.show()
fig1.savefig('graphs/doge_full_sp_vol.png')

doge.reset_index(inplace=True)

date_range = doge[doge['date'].isin(pd.date_range('2021-01-13', '2021-04-05'))]

sns.set(style="darkgrid")
fig2, ax = plt.subplots(figsize=(15,7))
plot = sns.lineplot(ax=ax, x=date_range['date'].values, y=date_range['volume'], color='midnightblue', label='DOGE')
ax.set(xticks=date_range['date'].values)
x_dates = date_range['date'].dt.strftime('%b-%d')
ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
ax.get_yaxis().set_major_formatter(
    mtl.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
for ind, label in enumerate(plot.get_xticklabels()):
    if ind % 2 == 0:  # every 5th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Volume Trend of DOGE')
plt.show()
fig2.savefig('graphs/doge_vol.png')