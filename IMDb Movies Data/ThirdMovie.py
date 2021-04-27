import pandas as pd

"""
Problem: Get the details of the third movie of the DataFrame (movies_metadata.csv file)
"""
data = pd.read_csv("imdb_data.csv")
print("Third Movie's Data: ")
print(data.iloc[2])