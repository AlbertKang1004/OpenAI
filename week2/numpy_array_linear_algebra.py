"""Numpy Linear Algebra"""

import numpy as np

# Matrix 3x4
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

# Matrix 4x2
b = np.array([[1, 2],
              [3, 4],
              [5, 6],
              [7, 8]])

# Matrix multiplication 3x4 @ 4x2 = 3x2
c = np.matmul(a, b)
print(c)
print(a @ b)  # @ is same as np.matmul()
