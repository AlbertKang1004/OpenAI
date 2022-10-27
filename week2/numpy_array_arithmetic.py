"""Numpy Array Arithmetic"""

import numpy as np

x = np.array([0, 1, 2])
y = np.array([9, 8, 7])

print('x + y = ', x + y)  # [9 9 9]
print('x - y = ', x - y)  # [-9 -7 -5]
print('x * y = ', x * y)  # [ 0  8 14]
print('x / y = ', x / y)
# [0.         0.125      0.28571429]

a = np.array([[1, 2, 3, 4], [9, 8, 0, 3]])
print(a)
print()

print('max : \t\t\t', np.max(a))
print('max axis 0 : \t', np.max(a, axis=0))
print('max axis 1 : \t', np.max(a, axis=1))
print()

print('min : \t\t\t', np.min(a))
print('min axis 0 : \t', np.min(a, axis=0))
print('min axis 1 : \t', np.min(a, axis=1))
print()

print('arg max : \t\t', np.argmax(a))
# returns location of the max value
print('arg max axis 0 :', np.argmax(a, axis=0))
print('arg min : \t\t', np.argmin(a))
print('arg min axis 1 :', np.argmin(a, axis=1))
print('sum : \t\t\t', np.sum(a))
print('sum axis 0 : \t', np.sum(a, axis=0))

b = np.array([1, 2, 3])
c = np.array([1, 2, 3])
d = np.array([4, 5, 6])
print(np.array_equal(b, c))  # True
print(np.array_equal(b, d))  # False

