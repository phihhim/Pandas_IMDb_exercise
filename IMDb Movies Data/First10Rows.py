import pandas as pd

"""
Problems: display the first 10 rows of the DataFrame
"""

df = pd.read_csv('imdb_data.csv')
print("First 10 movies: ")
print(df.iloc[:10])
