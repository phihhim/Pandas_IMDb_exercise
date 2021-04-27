import pandas as pd

"""
Problem: Get the details of the movie with title 'Green Book' (movies_metadata.csv file)
"""
data = pd.read_csv("imdb_data.csv")
result = data.loc[data['Series_Title'] == 'Green Book']
print("Details of the movie 'Green Book:")
print(result)