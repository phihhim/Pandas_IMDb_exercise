import pandas as pd

"""
Problems: Get the details of the columns title and genres of the DataFrame
"""
df = pd.read_csv('imdb_data.csv')
result = df[['Series_Title', 'Genre']]
print("Details of title and genres:")
print(result)