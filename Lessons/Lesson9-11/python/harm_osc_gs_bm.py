import numpy as np
import matplotlib.pyplot as plt
import boxMuller as bm
import meanAndStdErr as me
"""
Created on Tue Nov 24 10:33:35 2020

@author: Matteo Barborini

The quantum Harmonic oscillator's ground state with 
direct sampling of the Gaussian distribution

Variational Monte Carlo (VMC)

 m = h_bar =1
 
 Hamiltonian :
     H = - 0.5 * d^2_x + 0.5 * w**2 * x**2

 Trial Wave function:
     psi_T (x) = exp(-0.5*(w+dw)*x^2 )

    Norm_const = ((w+dw)/ pi )^(1/4)
    
 Sample the distribution function 
   |Psi_T(x) * Norm_const |^2 = ((w+dw)/pi)^(1/2)  * exp (-(w+dw)*x^2)
   
 Gaussian distribution function
   G(x) = (1/(2 pi * sigma^2 ))^(1/2) * exp(-0.5 * x^2 / sigma^2)
   
   2 * sigma^2 = 1 / (w+dw)  -- >> sigma = sqrt(1 / (2(w+dw)))

"""
# Frequency of the potential energy:
w = 1.0

# Local energy of the Harmonic oscillator's ground state
def locEneGS(x,w,dw):
    T_loc = 0.5 *( (w+dw) - (w+dw)**2 * x**2 )  
    V_loc = 0.5 * w**2 * x**2
    return T_loc + V_loc

# Number of MC sampling to integrate.    
n_sample = 100000

# Define arrays of the mean values and standard error of the integral for 
# different values of the error dw
mean_value_e_loc = []
std_err_e_loc = []

# List of values of dw
dw_list = np.arange(-0.5, 0.6, 0.1)

for dw in dw_list:
    # Values of the local energy for variance computation
    values_e_loc = []
    
    # Parameters of the distribution function
    sigma = 1.0 / np.sqrt(2.0*(w+dw))
    mean = 0.0

    # Iterate for the number of samples
    for i in range(n_sample):
       x = bm.boxMuller(mean,sigma)
       e_loc = locEneGS(x,w,dw)
       values_e_loc.append(e_loc)
    
    # Compute Mean value and Std err.
    mean_value, std_err = me.meanAndStdErr(values_e_loc)
    
    # Append the values to the two arrays
    mean_value_e_loc.append(mean_value)
    std_err_e_loc.append(std_err)
    

# Plot dots
plt.errorbar(dw_list, mean_value_e_loc, yerr=std_err_e_loc, fmt='o')
plt.xlabel(f'$\Delta \omega$')
plt.ylabel(f'$E[\psi_T]$')
plt.axis([-0.6, 0.6, 0.5, 0.7])
plt.grid(True)
plt.show()
    