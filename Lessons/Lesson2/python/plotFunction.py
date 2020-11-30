# For options of matplotlib refer to tutorials:
# https://matplotlib.org/tutorials/
import matplotlib.pyplot as plt
import numpy as np

# Create x values from 0 ti Pi, with a step of 0.01
x = np.arange(0.0, np.pi, 0.01)

y = np.sin(x)
# PLot sin with red dots
plt.plot(x, np.sin(x), 'r--')
plt.axis([0, np.pi, 0, 1.5])
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()
