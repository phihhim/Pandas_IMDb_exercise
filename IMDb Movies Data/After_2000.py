import pandas as pd

"""
Problems: get movies released after 2000
"""

df = pd.read_csv('imdb_data.csv')
print(df.loc[df['Released_Year'] > '2000'])