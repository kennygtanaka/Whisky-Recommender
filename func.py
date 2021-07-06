import pandas as pd
import numpy as np
from scipy.spatial import distance

def get_indexs(data, whisky):
    names = []
    for n in data.Whisky:
        if whisky in n:
            names.append(n)
    indices = []
    for i in names:
        index = data.index
        condition = data['Whisky'] == i
        inx = index[condition].values.astype(int)[0]
        indices.append(inx)
    return list(indices)[0]

def get_distance(data, ind):
    ones = [1] * 36
    sixteen = [7] * 14
    weights = ones + sixteen
    distances ={}
    other_i = list(range(0, len(data)))
    other_i.remove(ind)
    one =  data.iloc[ind][1:].to_list()
    for n in other_i:
        two = data.iloc[n][1:].to_list()
        dist = distance.cosine(one, two, weights)
        distances[n] = dist
    distances = dict(sorted(distances.items(), key=lambda item: item[1], reverse = True))
    distances = {k: distances[k] for k in list(distances)[:10]}
    print(distances)
    dist_keys = list(distances.keys())
    return dist_keys
