import pandas as pd

"""
Problems: sort the DataFrame based on Released_Year
"""

df = pd.read_csv('imdb_data.csv')
print(df.sort_values(by=['Released_Year']))

