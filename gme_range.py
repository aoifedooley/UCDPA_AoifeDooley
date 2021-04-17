# REF https://www.kaggle.com/jayashree4/gamestop-stock-prices-visualization-and

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

gme = pd.read_csv(r"GME_stock.csv")

# Converting the date column into datetime index
gme['date'] = pd.to_datetime(gme['date'])
gme.set_index('date',inplace=True)

# Plotting the open, close, high, low, volume and adjusted close value for the term of 12 months
fig1 = px.line(gme, x=gme.index, y=gme.columns,
              title='Plot of values for a 12 month period')
fig1.update_xaxes(
    dtick="M12",
    tickformat="%b\n%Y")
fig1.show()

fig2 = px.line(gme, x=gme.index, y=gme.columns,
              range_x=['2020-12-01','2021-01-28'],
              title='Plot of values for December 20 and January 21')
fig2.show()