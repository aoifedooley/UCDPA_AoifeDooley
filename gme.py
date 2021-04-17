import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

gme = pd.read_csv(r"GME_stock.csv")

# INFO
print("INFO")
print(gme.info())
print("")
# COLUMNS
print("COLUMNS")
print(gme.columns)
print("")
# TYPES
print("TYPES")
print(gme.dtypes)
print("")
# INDEX
print("INDEX")
print(gme.index)
print("")
# HEADER
print("HEADER")
print(gme.head())
print("")
# SHAPE
print("SHAPE")
print(gme.shape)
print("")
# DESCRIPTION
print("DESCRIPTION")
print(gme.describe())
# VALUES
print("VALUES")
print(gme.values)