"""
Created on Tue Nov 17 15:10:50 2020

@author: Matteo Barborini
@e-mail: matteo.barborini@uni.lu

 Computation of the integral of the type
    I = A int |x|^{-3/5} e^{-x^2}

 We sample the probability distribution
    p(x) = 1 / sqrt(2 pi sigma^2 ) * e^{-x^2 / (2 sigma^2)}

 thus 
    sigma = 1 / sqrt(2)
 
 and consequently
    A = 1 / sqrt(pi)

 The local function will be
    h(x) = |x|^{-3/5}

"""
# https://numpy.org/doc/stable/
import numpy as np
# https://matplotlib.org/contents.html
import matplotlib.pyplot as plot
# BoxMuller tranform
import boxMuller as bm
# Tool for simple statistical analysis
import meanAndStdErr as me

# h(x) function
def h(x):
    return np.abs(x)**(-3/5)

# Mean and standard error of the Gaussian distribution
mean = 0.0
sigma = 1.0 / np.sqrt(2) 

# Number of samples
n_sample = 10000000

# Values of the function for variance computation
values_h = []

# Iterate for the number of samples.
for i in range(n_sample):
    # Random number distributed as a Gaussian of mean=mean and 
    # std deviation = sigma
    x = bm.boxMuller(mean,sigma)
    # Compute values of the h(x) function and appen to the array
    values_h.append(h(x))

# Mean Value of the function h and standard error
mean_value_h, std_err_h = me.meanAndStdErr(values_h)

# Print the result
print('Value of the integral :', mean_value_h, '+/-',std_err_h)