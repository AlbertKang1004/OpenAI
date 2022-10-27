"""Numpy Array Vectorization"""
import time

import numpy as np


def slow_operation(n=1000):
    """A function with a for loop"""
    arr = np.arange(n)
    diff = np.zeros(n - 1)

    for i in range(1, n):
        diff[i - 1] = np.sqrt(arr[i] ** 2 - arr[i - 1] ** 2)

    return sum(diff) / n


def fast_operation(n=1000):
    """A function with a for loop"""
    arr = np.arange(n)
    diff = np.sqrt(arr[1:] ** 2 - arr[:-1] ** 2)

    return sum(diff) / n


print(slow_operation())
print(fast_operation())
