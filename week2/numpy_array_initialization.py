"""Numpy Arrays"""
import numpy as np
# Numpy arrays are a data structure similar to a Python list,
# but it has a lot of useful methods with better efficiency.

empty_arr = np.array([])
# creates an empty array
print(empty_arr)

lst = [1, 2, 3, 4]
# creates the array from a list
lst_arr = np.array(lst)
print(lst_arr)

lst_2d = [[1, 2], [3, 4]]
# creates 2-dimensional array
arr_2d = np.array(lst_2d)
print(arr_2d)

arr_with_ones = np.ones([2, 3])
# creates 2 * 3 array filled with 1
arr_with_zeros = np.zeros((2, 3))
# creates 2 * 3 array filled with 0, tuple is okay as a parameter
arr_with_numbers = np.full((2, 3), 4)
# creates 2 * 3 array filled with 4
print(arr_with_ones)
print(arr_with_zeros)
print(arr_with_numbers)

arr_random = np.random.random([2, 3])  # creates 2 * 3 array with random values between 0 and 1
print(arr_random)

arr_one_to_ten = np.arange(1, 11)  # end value exclusive
# [ 1 2 3 4 5 6 7 8 9 10]
print(arr_one_to_ten)

arr_even = np.arange(0, 21, 2)
# [ 0 2 4 6 8 10 12 14 16 18 20]
print(arr_even)

arr_same_distance = np.linspace(0, 5, 11)
# Array of 11 evenly spaced numbers between 0 and 5 (inclusive)
print(arr_same_distance)
