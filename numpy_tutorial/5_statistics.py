"""Numpy Tutorial"""

import numpy as np

stats = np.array([[1, 2, 3], [4, 5, 6]])
print(np.min(stats))
print(np.max(stats), '\n')

print(np.min(stats, axis=1))
print(np.sum(stats, axis=0))

