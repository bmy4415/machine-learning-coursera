import numpy as np
import pandas as pd


def get_rating_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    df = df.groupby(['source', 'target'])['rating'].first().unstack().fillna(0)
    return df.values


def get_frequent_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    df['rating'] = 1
    df = df.groupby(['source', 'target'])['rating'].count().unstack().fillna(0)
    return df.values
