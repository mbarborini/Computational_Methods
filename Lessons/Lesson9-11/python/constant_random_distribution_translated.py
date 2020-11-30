"""
Created on Tue Nov 17 15:10:50 2020

@author: matteo
"""
# https://numpy.org/doc/stable/
import numpy as np
# https://matplotlib.org/contents.html
import matplotlib.pyplot as plot


# Dimension of the sample 
n_sample = 100000

# List of random numbers
x = []

# Random numbers extracted with constant probability inside the interval [0,1]
# np.random.uniform()
for ix in range(n_sample):
    random_num = 2.0*np.random.uniform()-1.0
    x.append(random_num)
    
# Plot simple histogram
plot.hist(x, 50, density=True, facecolor='r', alpha=0.50)

# Final plot
plot.xlabel('x')
plot.ylabel('probability density')
#plot.title('Histogram of probability')
#plot.text(60, .025, r'$\mu=100,\ \sigma=15$')
plot.axis([-1.1, 1.1, 0, 2])
plot.grid(True)
