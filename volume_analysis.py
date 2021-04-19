# merge gme and doge
# compare volume over month of dec jan and feb - distplot

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mtl
import seaborn as sns
import numpy as np
from IPython.display import Image


# GME Data
gme = pd.read_csv(r"GME_stock.csv")
# GME Volume %
gme_vol_diff = gme['volume'].diff(periods=-1)
gme['vol_diff'] = ((gme["volume"] - gme_vol_diff) / gme["volume"]) * 100
print(gme.head())

# DOGECOIN Data
doge = pd.read_csv(r"DOGE-USD.csv")
# GME Volume %
doge_vol_diff= doge['volume'].diff(periods=1)
doge['vol_diff'] = ((doge["volume"] - doge_vol_diff) / doge["volume"]) * 100
print(doge.head())

# MERGE GME AND DOGECOIN TABLES
gme_doge = gme.merge(doge, on="date", how="left", suffixes=["_gme", "_doge"])
gme_doge.dropna()
pd.set_option('display.max_columns', None)
print(gme_doge.head(5))
print(gme_doge.shape)

# Converting the date column into datetime index
gme_doge['date'] = pd.to_datetime(gme['date'], infer_datetime_format=True)
gme_doge.set_index('date')
gme_doge.sort_index()

date_range = gme_doge[gme_doge['date'].isin(pd.date_range('2021-01-13', '2021-02-02'))]
print(date_range.shape)
print(date_range)

sns.set(style="darkgrid")
color = sns.color_palette()[2]

fig1, ax = plt.subplots(figsize=(15,7))
plot = sns.lineplot(ax=ax, x=date_range['date'].values, y=date_range['vol_diff_gme'], color='cornflowerblue', label='GME')
plot = sns.lineplot(ax=ax, x=date_range['date'].values, y=date_range['vol_diff_doge'], color='midnightblue', label='DOGE')
ax.set(xticks=date_range['date'].values)
x_dates = date_range['date'].dt.strftime('%Y-%m-%d')
ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
ax.get_yaxis().set_major_formatter(
    mtl.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
#        label.set_visible(False)
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Plot of GME Volume')
plt.show()

fig1.savefig('vol_analysis.png')


#date_range_2 = gme_doge[gme_doge['date'].isin(pd.date_range('2020-01-01', '2021-03-05'))]

fig2, ax = plt.subplots(figsize=(15,7))
plot = sns.factorplot(ax=ax, x=date_range['vol_diff_gme'].values, y=date_range['vol_diff_doge'], color=color)
#plot = sns.scatterplot(ax=ax, x=date_range['date'].values, y=date_range['low_gme'], color=color)
ax.set(xticks=date_range['vol_diff_gme'].values)
#x_dates = date_range['date'].dt.strftime('%Y-%m-%d')
#ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
#ax.get_yaxis().set_major_formatter(
#    mtl.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('GME High Share Price')
plt.show()
