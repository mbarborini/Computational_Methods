"""
Created on Tue Nov 17 15:10:50 2020

@author: Matteo Barborini
@e-mail: matteo.barborini@uni.lu

 Testing Box-Muller transform to sample a general Gaussian distribution
 of mean value m and standard deviation sigma

    p(x) = 1 / sqrt(2 pi sigma^2 ) * e^{-(x-m)^2 / (2 sigma^2)}

Box-Muller transform
    x1, x2 random numbers in [0,1]
    
    y1 = sqrt(-2 log(x1)) cos(2 pi x2)
    y2 = sqrt(-2 log(x1)) sin(2 pi x2)
    
    y1 and y2 distributed according to a Gaussian with zero mean value
              and unitary variance
"""
# https://numpy.org/doc/stable/
import numpy as np
# https://matplotlib.org/contents.html
import matplotlib.pyplot as plot

# Simple Box-Muller transform
def boxMuller(x1,x2):
    y1 = np.sqrt(-2.0*np.log(x1))*np.cos(2.0*np.pi*x2)
    y2 = np.sqrt(-2.0*np.log(x1))*np.sin(2.0*np.pi*x2)
    return y1, y2

# Mean and standard error
mean = -2.0
sigma = 3.0

# Number of samples
n_samples = 100000

# Standard distribution
x=[]
# Gaussian distribution
y=[]

# Iterate for the number of samples.
for i in range(n_samples):
    x1 = np.random.uniform()
    x2 = np.random.uniform()
    y1, y2 = boxMuller(x1,x2)
    y1 = sigma*y1 + mean
    y2 = sigma*y2 + mean

    x.append(x1)
    x.append(x2)

    y.append(y1)
    y.append(y2)

# Plot Flat and Gaussian distribution
plot.hist(x, 50, density=True, facecolor='r', alpha=0.50)
plot.hist(y, 500, density=True, facecolor='g', alpha=0.50)

plot.xlabel('x')
plot.ylabel('Probability density')
plot.axis([-10.0, 10.0, 0, 1])
plot.grid(True)
plot.show()