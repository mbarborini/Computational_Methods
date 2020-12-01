"""
Created on Tue Nov 24 11:25:06 2020

@author: Matteo Barboini
@e-mail: matteo.barborini@gmail.com

 - Compute the mean value and standard error of a series
   mean, st_err = meanAndStdErr( a )

 - Compute autocorrelation function
   rho_k = autoCorrFunc(a, T_max)

 - Compute the reblocked array
   reblocked_a = reblock(a, T_block)
   
"""
# https://numpy.org/doc/stable/
import numpy as np

# Mean value and standard error
def meanAndStdErr( a ):
    n_elements = np.size(a)
    
    # Mean Value and Variance
    mean, variance = meanAndVar(a)

    # Standard error 
    std_err = np.sqrt(variance / float(n_elements))
    
    return mean, std_err

# Mean value and standard error
def meanAndVar( a ):
    n_elements = np.size(a)
    
    # Mean Value
    mean = np.sum(a) / float(n_elements)
    
    # Variance
    variance = np.sum((a[:]-mean)**2) / float(n_elements-1)

    return mean, variance


# Autocorrelation function for time <= T_max
def autoCorrFunc( a, T_max=100 ):
    n_elements = np.size(a)
    
    # Mean Value
    mean = np.sum(a) / float(n_elements)
    
    # Initialize empty correlation vector
    corr = np.zeros(T_max)
    
    # Variance is the first element
    for t in range(T_max):
        for i in range(n_elements-T_max):
            corr[t] += (a[i]-mean) * (a[i+t]-mean)
        
    # Renormalize
    corr[:] = corr[:] / corr[0]

    return corr[:]

# Reblock array for blocks of length T_block
def reblock( a, T_block ):
    n_elements = np.size(a)
    
    # Number of blocks
    n_blocks = int (n_elements / T_block)
    
    # Mean Value of blocks
    blocks = np.zeros(n_blocks)
    for t in range(n_blocks):
        blocks[t] = np.sum(a[t*T_block:(t+1)*T_block]) / float(T_block)
    
    return blocks[:]