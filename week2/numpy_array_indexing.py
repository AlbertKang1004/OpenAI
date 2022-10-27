"""Numpy Array Slicing & Indexing"""

import numpy as np

arr = np.array([[1, 2],
                [3, 4]])

print(arr[0, 1])
# get the element in the first row, second column

print(arr[:, 1])
# get all element in the second column

print(arr[0])
# get all element in the first row

arr_bigger = np.array([[1,  2,  3,  4],
                       [5,  6,  7,  8],
                       [9,  10, 11, 12],
                       [13, 14, 15, 16]])

print(arr_bigger[1:3, 2:4])
# crop the array from second row to the third row,
# and third column to the forth column

