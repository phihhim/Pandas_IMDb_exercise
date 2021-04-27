import pandas as pd

"""
Problem: Get the columns of the DataFrame
"""

data = pd.read_csv("imdb_data.csv")
print("Name of role:")
df = pd.DataFrame(data.columns)
print(df)