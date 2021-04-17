import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# REF: https://www.kaggle.com/sprakshith/beginner-s-guide-to-sentiment-analysis

wsb = pd.read_csv(r"reddit_wsb.csv")

wsb['timestamp'] = pd.to_datetime(wsb['timestamp'])

day_of_the_week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
days_order = list(day_of_the_week.values())

wsb['weekday'] = wsb['timestamp'].apply(lambda x : day_of_the_week[x.weekday()])

pd.set_option('display.max_columns', None)
print(wsb.columns)
print(wsb['weekday'].head(20))

xs = wsb['weekday'].value_counts().index
ys = wsb['weekday'].value_counts().values


fig, ax = plt.subplots(figsize=(15,7))
#plt.figure(figsize=(14,6))

sns.barplot(x=xs, y=ys, order=days_order)

plt.title("Number of r/WallSreetBets Forum Posts", fontsize=15)

plt.xlabel("Days", fontsize=15)
plt.ylabel("Number of Posts", fontsize=15)

plt.show()

fig.savefig('wsb_weekdays.png')