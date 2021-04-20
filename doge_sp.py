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

doge_range = doge[doge['date'].isin(pd.date_range('2021-01-20', '2021-04-05'))]

sns.set(style="darkgrid")
color = sns.color_palette()[2]

fig1, ax = plt.subplots(figsize=(15,7))
plot = sns.lineplot(ax=ax, x=doge_range['date'].values, y=doge_range['change'].values, color='g')
ax.set(xticks=doge_range['date'].values)
x_dates = doge_range['date'].dt.strftime('%b-%d')
ax.set_xticklabels(labels=x_dates, rotation=45, ha='right')
plt.ticklabel_format(style='plain', axis='y')
ax.get_yaxis().set_major_formatter(
    mtl.ticker.FuncFormatter(lambda y, p: format(int(y), ',')))
for ind, label in enumerate(plot.get_xticklabels()):
    if ind % 2 == 0:
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.xlabel('Date')
plt.ylabel('% Change in SP')
plt.title('Plot of DOGE SP Change')
plt.show()