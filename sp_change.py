import pandas as pd
import matplotlib as mtl
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

# Converting the date column into datetime index
gme_doge['date'] = pd.to_datetime(gme['date'], infer_datetime_format=True)
gme_doge.set_index('date')
gme_doge.sort_index()

date_range = gme_doge[gme_doge['date'].isin(pd.date_range('2021-01-13', '2021-02-05'))]
print(date_range.shape)
print(date_range)

# MERGED TABLES GRAPH
sns.set(style="darkgrid")
fig, ax = plt.subplots(figsize=(15,7))
plot = sns.lineplot(ax=ax, x=date_range['date'].values, y=date_range['change_gme'], color='cornflowerblue', legend='brief', label='GME')
plot = sns.lineplot(ax=ax, x=date_range['date'].values, y=date_range['change_doge'], color='midnightblue', legend='brief', label='DOGE')
ax.set(xticks=date_range['date'].values)
x_dates = date_range['date'].dt.strftime('%b-%d')
ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
ax.get_yaxis().set_major_formatter(
    mtl.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
plt.xlabel('Date')
plt.ylabel('Share Price Increase (%)')
plt.title('Percentage Increase in Share Price of GME and DOGE')
plt.show()

fig.savefig('graphs/sp_change.png')




