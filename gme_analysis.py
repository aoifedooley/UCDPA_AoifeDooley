import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px

gme = pd.read_csv(r"GME_stock.csv")

print(gme.index)

# GME % INCREASE
gme["change"] = ((gme["high"] - gme["low"]) / gme["high"]) * 100
print(gme['change'].head(20))

# Converting the date column into datetime index
gme['date'] = pd.to_datetime(gme['date'])
gme.set_index('date')

#gme['change'].rolling(400).mean().plot()
#gme.plot(x='date', y='change', rot=90)
#plt.show()

#fig, ax = plt.subplots()
#ax.hist(gme['change'])
#gme['change'].plot.hist()
#plt.show()

#sns.displot(gme['change'])
#plt.show()

#sns.regplot(x="adj_close", y="change", data=gme)
#plt.show()

#sns.lmplot(x="open", y="close", col="date")
#plt.show()

date_range = gme[gme['date'].isin(pd.date_range('2021-01-11', '2021-02-05'))]
print(date_range)

#date_grouped = date_range.groupby('date').count()
#date_grouped.reset_index(inplace=True)
#plt.plot(x=date_grouped.index.values, y=date_grouped['change'])
#plt.show()

#fig, ax = plt.subplots(figsize=(12,12))
#ax.bar(date_range.index.values, date_range['change'], color='purple')
#plt.show()

#plt.figure(figsize=(15,7), dpi=100)
fig, ax = plt.subplots(figsize=(15,7))
plot = sns.lineplot(ax=ax, x=date_range['date'].values, y=date_range['change'].values)
ax.set(xticks=date_range['date'].values)
for ind, label in enumerate(plot.get_xticklabels()):
    if ind % 2 == 0:  # every 2nd label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.xlabel('Date')
plt.ylabel('Change in Stock Price (%)')
plt.title('Increase in GME Stock Price')
plt.show()

