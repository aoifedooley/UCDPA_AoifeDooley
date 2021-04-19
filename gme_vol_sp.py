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

# GME SP % INCREASE
gme["change"] = ((gme["high"] - gme["low"]) / gme["high"]) * 100

# Converting the date column into datetime index
gme['date'] = pd.to_datetime(gme['date'], infer_datetime_format=True)
gme.set_index('date', inplace=True)

plt.figure(figsize=(10, 5))
top = plt.subplot2grid((4, 4), (0, 0), rowspan=3, colspan=10)
bottom = plt.subplot2grid((4, 4), (3, 0), rowspan=1, colspan=10)
top.bar(gme.index, gme['high'])
bottom.bar(gme.index, gme['volume'])


top.axes.get_xaxis().set_visible(False)
top.set_title('GME Stock')
top.set_ylabel('Highest Price')
bottom.set_ylabel('Volume')

plt.show()

date_range = gme[gme['date'].isin(pd.date_range('2021-01-13', '2021-02-05'))]

sns.set(style="darkgrid")
fig, ax = plt.subplots(figsize=(15,7))
plot = sns.lineplot(ax=ax, x=date_range['date'].values, y=date_range['volume'], color='cornflowerblue', label='GME')
ax.set(xticks=date_range['date'].values)
x_dates = date_range['date'].dt.strftime('%b-%d')
ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
ax.get_yaxis().set_major_formatter(
    mtl.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))

plt.xlabel('Date')
plt.ylabel('Volume')
plt.title('Volume Trend of GME')
plt.show()
