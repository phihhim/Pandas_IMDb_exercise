import pandas as pd

"""
Problem: Get the information of the DataFrame (movies_metadata.csv file)including data types and memory usage
"""
data = pd.read_csv("imdb_data.csv")
print("Database Info:")
print(data.info(verbose=False))

print("\n")
print("Data type:")
print(data.dtypes)

print("\n")
print("Memory Usage:")
print(data.memory_usage())

