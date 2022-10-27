"""Numpy Array Broadcasting"""

import numpy as np

arr = np.ones((3, 2))
print(arr * 5)

arr = np.array([3, 5, 7, 5, 2, 7, 9])
min = arr.min()  # scalar
max = arr.max()  # scalar

print((arr - min) / (max - min))

# Representing Image
img = np.random.random((5, 5, 3))
print(img.shape)
print(img)

# 0 to 1
print("min: ", img.min())
print("max", img.max())

# change it to 0 to 255 using normalization
img = (img * 255).astype(np.uint8)
# also change it to uint8 which is optimized for colours
print("min: ", img.min())
print("max", img.max())
print(img)

blue_mask = np.array([1, 0, 0])
img_blue = img * blue_mask
print(img_blue)
