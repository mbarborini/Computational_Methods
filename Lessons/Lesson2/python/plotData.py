# For options of matplotlib refer to tutorials:
# https://matplotlib.org/tutorials/
import matplotlib.pyplot as plt
import numpy as np

# Creat lists with x values and y values
x=[1, 2, 3, 4]
y=[1, 4, 9, 16]

# Plot blue circles 
plt.plot(x, y, 'bo')
plt.axis([0, 5, 0, 18])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
