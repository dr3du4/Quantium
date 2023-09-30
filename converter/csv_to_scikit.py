import numpy as np
import pandas as pd

input_file = "iris.csv"

df = pd.read_csv(input_file,header=0)
dictionary = {}
arr = []

for ind in df[df.columns.values[len(df.columns.values)-1]].index:
    word = df[df.columns.values[len(df.columns.values)-1]][ind]
    arr.append(word)

arr = np.unique(arr)
print(arr)

dict = {}
for index,value in enumerate(arr):
    dict[value]=index
    
targets = []
for ind in df[df.columns.values[len(df.columns.values)-1]].index:
    word=df[df.columns.values[len(df.columns.values)-1]][ind]
    targets.append(dict[word])

original_headers = list(df.columns.values)

df = df._get_numeric_data()

numeric_headers = list(df.columns.values)
numpy_array = df.to_numpy()

numeric_headers.reverse()
reverse_df = df[numeric_headers]

print(targets)
print(numpy_array)

