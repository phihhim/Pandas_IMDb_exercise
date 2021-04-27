import pandas as pd

"""
Problems: create a smaller DataFrame with a subset of all features
"""
data = pd.read_csv('imdb_data.csv')
smaller_data = data[["Series_Title","IMDB_Rating","Overview"]]
print("Subset of imdb's data: ")
print(smaller_data)