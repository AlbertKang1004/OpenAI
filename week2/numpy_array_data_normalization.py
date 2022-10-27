"""Numpy Array Data Normalization"""

import numpy as np

A = np.array([[1, 1, 1], [4, 5, 6], [7, 8, 9]])


def standardize(features):
    """Data Normalization"""
    mean = np.mean(features, axis=0)
    print("Feature wise mean: ", mean)
    deviation = np.std(features, axis=0)
    print("Feature wise deviation: ", deviation)
    # to avoid division by 0
    std_feat = (features - mean) / (deviation + 1e-8)
    return std_feat


def min_max_normalization(features):
    """Min-Max Normalization"""
    return (features - np.min(features)) / (np.max(features) - np.min(features))


print(standardize(A))
print(min_max_normalization(A))


