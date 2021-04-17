import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

doge = pd.read_csv(r"DOGE-USD.csv")

# INFO
print("INFO")
print(doge.info())
print("")
# COLUMNS
print("COLUMNS")
print(doge.columns)
print("")
# TYPES
print("TYPES")
print(doge.dtypes)
print("")
# INDEX
print("INDEX")
print(doge.index)
print("")
# HEADER
print("HEADER")
print(doge.head())
print("")
# SHAPE
print("SHAPE")
print(doge.shape)
print("")
# DESCRIPTION
print("DESCRIPTION")
print(doge.describe())
# VALUES
print("VALUES")
print(doge.values)