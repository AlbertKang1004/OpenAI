"""Numpy Practice"""

import numpy as np
a = np.array([1, 2, 3], dtype='int16')
print(a, '\n')

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b, '\n')

# Get Dimension
print(a.ndim)
print(b.ndim, '\n')

# Get Shape
print(a.shape)
print(b.shape, '\n')

# Get Type
print(a.dtype)
print(b.dtype, '\n')

# Get Size
print(a.itemsize)
print(b.itemsize, '\n')

# Get total size
print(a.nbytes)
print(b.nbytes, '\n')
