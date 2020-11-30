"""
Created on Tue Nov 17 15:10:50 2020

@author: matteo
"""
# https://numpy.org/doc/stable/
import numpy as np
# https://matplotlib.org/contents.html
import matplotlib.pyplot as plot

# Circle function 
def circle(r,x,y):
    if x**2+y**2 <= r**2:
        return 1.0
    else:
        return 0.0


# Radius of the circle
r = 1.0

# Dimension of the sample 
n_sample = 100000

# List of random numbers
x_in = []
y_in = []
x_ou = []
y_ou = []

sum_f = 0.0

values_f = []

for i in range(n_sample):
    x = (2.0*np.random.uniform()-1.0)*r
    y = (2.0*np.random.uniform()-1.0)*r
    
    f = circle(r,x,y)
    values_f.append(f)
    sum_f += f
    
    # lot the dots
    if f == 1.0:
        x_in.append(x)
        y_in.append(y)
    else:
        x_ou.append(x)
        y_ou.append(y)
        
# Mean value
mean_value_f = sum_f / float(n_sample)

# Variance
var_f = 0.0
for i in range(n_sample):
    var_f += (values_f[i]- mean_value_f)**2

var_f = var_f / float(n_sample-1)

# Standard error 
std_err_f = np.sqrt(var_f / float(n_sample))

# Print the result
print('Area of the Circle :', mean_value_f*4.0*r**2, '+/-',std_err_f*4.0*r**2)
 
# Plot dots
plot.scatter(x_in,y_in,s=1,c='r')
plot.scatter(x_ou,y_ou,s=1,c='b')
plot.xlabel('x')
plot.ylabel('y')
plot.title('Area of a circle')
#plot.text(60, .025, r'$\mu=100,\ \sigma=15$')
plot.axis([-r*1.1, r*1.1, -r*1.1, r*1.1])
plot.grid(True)
plot.show()
