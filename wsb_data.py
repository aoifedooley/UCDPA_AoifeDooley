import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mtl
import seaborn as sns
import numpy as np

wsb = pd.read_csv(r"reddit_wsb.csv")
print(wsb["body"].count())

# SEPARATE TIMESTAMP COLUMN TO DATE AND TIME
wsb['date'] = pd.to_datetime(wsb['timestamp']).dt.date
wsb['time'] = pd.to_datetime(wsb['timestamp']).dt.time
wsb['date'] = pd.to_datetime((wsb['date']))
wsb.drop(['created', 'timestamp'], 1, inplace=True)
pd.set_option('display.max_columns', None)
print(wsb.columns)
print(wsb.head())

print(wsb['body'].count())

wsb.set_index('date')

def missing_data(data):
    total = data.isnull().sum()
    percent = (data.isnull().sum()/data.isnull().count()*100)
    tt = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    types = []
    for col in data.columns:
        dtype = str(data[col].dtype)
        types.append(dtype)
    tt['Types'] = types
    return(np.transpose(tt))

print(missing_data(wsb))

wsb.fillna('n/a', inplace=True)
print(missing_data(wsb))

wsb_data = wsb[(wsb['score'] > 7000) & (wsb['comms_num'] > 500)]
print('WSB DATA')
print(wsb_data)

print('MAX SCORE')
max_score = wsb.loc[wsb['score'].idxmax()]
print(max_score)


sns.set(style="darkgrid")
fig, ax = plt.subplots(figsize=(15,7))
plot = sns.scatterplot(ax=ax, x=wsb_data['score'].values, y=wsb_data['date'].values, hue='score', legend='brief', label='Score')
plt.xlabel('Score of Post')
plt.ylabel('# of Comments')
plt.title('r/WSB')
plt.show()