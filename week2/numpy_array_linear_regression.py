"""Numpy Array Linear Regression"""

import numpy as np
import matplotlib.pyplot as plt

# Generate some data in an array
# sample = np.array([[1,3],[2,4],[3,5.5],[4,8.2],[5,10],[6,11],[7,13], [8,14.2], [9,19], [10,20.3]])
# Some random data
sample = np.array([[x + np.random.random(), x*2 + np.random.random()] for x in range(10)])

# Get the x and y values
x = sample[:, 0]
y = sample[:, 1]

# Find the number of samples in the data
n = x.size

# Calculate the mean values for x and y
xm, ym = np.mean(x), np.mean(y)

# Calculate the coefficients - this is math you don't need to know, don't worry
b1 = (np.sum(y*x) - n*ym*xm) / (np.sum((x - xm)**2))
b0 = ym - b1*xm

# print the results
print("The coefficients are b0 %2.2f and b1 %2.2f " % (b0, b1))

# Plot the original data
plt.plot(x, y, 'o')
# Plot the linear regression
plt.plot(x, x*b1 + b0)
plt.show()
