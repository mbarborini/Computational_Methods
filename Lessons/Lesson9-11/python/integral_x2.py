# https://numpy.org/doc/stable/
import numpy as np
# https://matplotlib.org/contents.html
import matplotlib.pyplot as plot

# Box-Muller transform
def boxMuller(x1,x2):
    y1 = np.sqrt(-2.0*np.log(x1))*np.cos(2.0*np.pi*x2)
    y2 = np.sqrt(-2.0*np.log(x1))*np.sin(2.0*np.pi*x2)
    return y1, y2

# h(x) function
def h(x):
    return x**2

# Mean and standard error
mean = 0.0
sigma = 1.0 / np.sqrt(2) 

n_sample = 1000000

# Standard distribution
x=[]
# Gaussian distribution
y=[]

# Values of the function for variance computation
values_h = []

# Iterate for the number of samples.
sum_h = 0.0
for i in range(n_sample):
    x1 = np.random.uniform()
    x2 = np.random.uniform()
    y1, y2 = boxMuller(x1,x2)
    y1 = sigma*y1 + mean
    y2 = sigma*y2 + mean

    values_h.append(h(y1))
    values_h.append(h(y2))
    sum_h += h(y1) + h(y2)

# Mean Value of the function h
mean_value_h = sum_h / float(2* n_sample)

# Variance of the function h
var_h = 0.0
for i in range(2*n_sample):
    var_h += (values_h[i]- mean_value_h)**2

var_h = var_h / float(2*n_sample-1)

# Standard error 
std_err_h = np.sqrt(var_h / float(2*n_sample))

# Print the result
print('Value of the integral :', mean_value_h, '+/-',std_err_h)