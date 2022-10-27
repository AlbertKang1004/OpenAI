"""Numpy Datatypes"""
import numpy as np

# np.int_       same as Python's int
# np.uint8      from 0 to 255, excluding negatives
# np.float16    float using 16 bits
# np.float32    float using 32 bits

int_arr = np.array([-1, 2, 3])
print(int_arr.dtype)  # int64

float_arr = np.array([1.2, 3.4, 6.5])
print(float_arr.dtype)  # float64

uint_arr = np.array([1, 5, 10], dtype=np.uint8)
print(uint_arr.dtype)  # uint8


print(int_arr)
print(int_arr.astype(np.uint8))
# [-1  2  3] -> [255   2   3]

print(float_arr)
print(float_arr.astype(int))
# [1.2 3.4 6.5] -> [1 3 6]



