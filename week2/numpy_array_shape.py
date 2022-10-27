"""Numpy Arrayss"""
import numpy as np

m = np.ones((2, 3))
print(m)

print(m.ndim)
# returns the number of dimensions in an array
# 2
print(m.shape)
# returns a tuple with a number of elements along each axis
# (2, 3)
print(m.size)
# returns the total number of elements in an array
# 6

print(m.flatten())
# flattens an n-dimensional array to 1 dimension
# [1. 1. 1. 1. 1. 1.]

n = np.zeros(6)
print(n)
o = np.expand_dims(n, 0)
p = np.expand_dims(m, 1)
print(o)
print(o.shape)
print(p)
print(p.shape)
