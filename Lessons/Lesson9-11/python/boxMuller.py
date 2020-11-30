import numpy as np
"""
Created on Tue Nov 24 11:25:06 2020

@author: Matteo Barboini
@e-mail: matteo.barborini@gmail.com

Box-Muller transform
    x1, x2 random numbers in [0,1]
    
    y1 = sqrt(-2 log(x1)) cos(2 pi x2)
    y2 = sqrt(-2 log(x1)) sin(2 pi x2)
    
    y1 and y2 distributed according to a Gaussian with zero mean value
              and unitary variance
              
              
"""
# additional value is saved (returned if non zero)
# The se are global variables
buff = False
y2 = 0.0

# Box muller transform, it returns a random number distributed according
# to a Gaussian with mean value (mean), and standard deviation (sigma)
def boxMuller( mean = 0.0, sigma = 1.0 ):
    
    # Tell python that you want to use the global variables
    global buff
    global y2
    
    if buff == True :
        buff = False
        return sigma * y2 + mean
    else:
        # Random numbers in unifrom [0,1]
        x1 = np.random.uniform()
        x2 = np.random.uniform()
    
        y1 = np.sqrt(-2.0*np.log(x1))*np.cos(2.0*np.pi*x2)
        y2 = np.sqrt(-2.0*np.log(x1))*np.sin(2.0*np.pi*x2)
        buff = True
        return sigma * y1 + mean



