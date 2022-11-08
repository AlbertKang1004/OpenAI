"""Numpy Tutorial"""

import numpy as np

a = np.array([1, 2, 3, 4])
print(a + 2)
print(a * 2, '\n')

b = np.array([1, 0, 1, 0])
print(a + b)
print(a * b, '\n')

# Take the trig
print(np.sin(a))
print(np.cos(a))
print(np.tan(a), '\n')

# Linear Algebra
a = np.ones((2, 3))
print(a)

b = np.full((3, 2), 2)
print(b)

print(np.matmul(a, b), '\n')

c = np.identity(3)
print(np.linalg.det(c), '\n')
