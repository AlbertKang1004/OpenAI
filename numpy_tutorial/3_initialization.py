"""Numpy Tutorial"""

import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# All 0s matrix
print(np.zeros(5))
print(np.zeros((3, 2)))
print(np.zeros((1, 3, 4)), '\n')

# All 1s matrix
print(np.ones((3, 2)), '\n')

# Any other number
print(np.full((2, 2), 99, dtype='float32'), '\n')

# Any other number (full_line)
print(np.full_like(a, 4), '\n')

# Random decimal numbers
print(np.random.rand(3, 4))
print(np.random.random_sample(a.shape), '\n')

# Random Integer values
print(np.random.randint(4, 7, size=(3, 3)), '\n')
# starts at 0 if no start specified

# Identity Matrix
print(np.identity(3), '\n')

# Repeating Array
print(np.repeat(np.array([[1, 2, 3]]), 3, axis=0), '\n')

output = np.ones((5, 5))
output[1:-1, 1:-1] = 0
output[2, 2] = 9

print(output, '\n')

# Copying array
a = np.array([1, 2, 3])
b = a.copy()
print(b, '\n')
