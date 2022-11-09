"""Numpy Tutorial"""

import numpy as np
filedata = np.genfromtxt('data.txt', delimiter=',')
print(filedata, '\n')
filedata = filedata.astype('int32')
print(filedata, '\n')

# Boolean Masking and Advanced Indexing
print(filedata > 50, '\n')

print(filedata[filedata > 50], '\n')

# You can index with a list in NumPy
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 8]], '\n')

print(np.any(filedata > 50, axis=0), '\n')
print(np.any((filedata > 50) & (filedata < 100)), '\n')

# Quiz
b = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28, 29, 30]])

print(b[2:4, 0:2], '\n')
print(b[[0, 1, 2, 3], [1, 2, 3, 4]], '\n')
