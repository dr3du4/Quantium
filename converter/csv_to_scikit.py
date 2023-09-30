import numpy as np
import pandas as pd

def csv_to_scikit(input_file):
    df = pd.read_csv(input_file,header=0)
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

    d = {"data": numpy_array, "target": targets, "feature_names": np.array(arr,"<U10")}
    return d