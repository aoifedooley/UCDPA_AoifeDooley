import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

wsb = pd.read_csv(r"reddit_wsb.csv")
print(wsb["body"].count())

# SEPARATE TIMESTAMP COLUMN TO DATE AND TIME
wsb["date"] = pd.to_datetime(wsb["timestamp"]).dt.date
wsb["time"] = pd.to_datetime(wsb["timestamp"]).dt.time
wsb["date"] = pd.to_datetime((wsb["date"]))
wsb.dropna()
pd.set_option('display.max_columns', None)
print(wsb.columns)
print(wsb.head())

print(wsb["body"].count())

#wsb.set_index("date")

# 28TH JAN
date_28 = wsb.loc[wsb["date"] == "2021-01-28"]
# print(date_28.info())
print("ISNA()")
print(date_28.isna())
date_28.fillna("0", inplace=True)
print(date_28.isna())
print(date_28.head())
print(date_28.count())

# 29TH JAN
date_29 = wsb.loc[wsb["date"] == "2021-01-29"]
# print(date_29.info())
print(date_29.head())
print(date_29.count())

# 30TH JAN
date_30 = wsb.loc[wsb["date"] == "2021-01-30"]
# print(date_30.info())
print(date_30.head())
print(date_30.count())

# 14TH FEB
date_14 = wsb.loc[wsb["date"] == "2021-02-14"]
# print(date_30.info())
print(date_14.head())
print(date_14.count())

#plot_28 = date_28.count()
#plot_28.plot(kind='bar')
#plt.show()

#plot_28 = date_28.value_counts().index
#plot_29 = date_29.value_counts().index
#plot_30 = date_30.value_counts().index
#plot_14 = date_14.value_counts().index

#group = wsb.groupby("title").sum()

#x = [plot_28, plot_29, plot_30, plot_14]
#y = wsb['title'].value_counts().values
#plt.bar(x,y)
#plt.show()

xs = date_28.value_counts().index
ys = wsb['title'].value_counts().values

plt.figure(figsize=(14,6))

sns.barplot(x=xs, y=ys)

plt.title("WSB Reddit Forum Posts", fontsize=15)

plt.xlabel("Days", fontsize=15)
plt.ylabel("Number of Posts", fontsize=15)

plt.show()

#average_posts = wsb.groupby("date")["title"].sum()
#print(average_posts)

#average_posts.plot(kind='bar')
#plt.show()