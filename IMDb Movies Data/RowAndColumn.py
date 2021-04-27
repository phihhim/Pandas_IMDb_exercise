import pandas as pd

"""
Problem: Count the number of rows and columns of the DataFrame (movies_metadata.csv file)
"""

data = pd.read_csv("imdb_data.csv")
row, column = data.shape
print("Number of rows:", row)
print("Number of columns:", column)