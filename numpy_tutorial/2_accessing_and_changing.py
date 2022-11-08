"""Numpy Tutorial"""
import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)

# Get a specific element [r, c]
print(a[1, 5])
print(a[1, -2], '\n')

# Get a specific row
print(a[0, :], '\n')

# Get a specific column
print(a[:, 2], '\n')

# Getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:6:2], '\n')

# changing the element
print(a[1, 5])
a[1, 5] = 20
print(a[1, 5], '\n')

print(a)
a[:, 2] = [1, 2]
print(a, '\n')

# 3D example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(b, '\n')

# Get specific element (work outside in)
print(b[0, 1, 1])
print(b[0, :], '\n')

# Replace
print(b[:, 1, :])
b[:, 1, :] = [[9, 9], [8, 8]]
print(b[:, 1, :], '\n')
