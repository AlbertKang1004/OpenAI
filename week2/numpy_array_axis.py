"""Numpy Array Axis"""

import numpy as np

arr = np.array([
    [0, 2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9, 11]
])

print(arr.sum())
print(arr.sum(axis=0))  # Sum of columns
print(arr.sum(axis=1))  # Sum of rows
