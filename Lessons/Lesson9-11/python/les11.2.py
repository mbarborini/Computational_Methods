import numpy as np
import matplotlib.pyplot as plt
import boxMuller as bm
import meanAndStdErr as me
import metropolisHastings as mh
"""
Created on Tue Nov 24 10:33:35 2020

@author: Matteo Barborini

The quantum Harmonic oscillator's ground state with Metropolis-Hastings 
algorithm

Variational Monte Carlo (VMC)

 m = h_bar =1
 
 Hamiltonian :
     H = - 0.5 * d^2_x + 0.5 * w**2 * x**2

 Trial Wave function:
     psi_T (x) = exp(-0.5*(w+dw)*x^2 )
    
 Sample the distribution function 
   |Psi_T(x) |^2 = exp (-(w+dw)*x^2)

"""
# Frequency of the potential energy:
w = 1.0

# Local energy of the Harmonic oscillator's ground state
def locEneGS(x,w,dw):
    T_loc = 0.5 *( (w+dw) - (w+dw)**2 * x**2 )  
    V_loc = 0.5 * w**2 * x**2
    return T_loc + V_loc

# Square of the trial wave function (Not normalized) P(x)
def sqrTrialWaveFunction( x,w ):
    return np.exp(-(w)*x**2)


# Number of MC sampling to integrate.    
n_sample = 100000
# Number of thermalization steps for Metropolis
n_therm  = 1000

# Define arrays of the mean values and standard error of the integral for 
# different values of the error dw
mean_value_e_loc = []
std_err_e_loc = []

# List of values of dw
dw_list = np.arange(-0.5, 0.6, 0.1)

for dw in dw_list:
    # Values of the local energy for variance computation
    values_e_loc = []

    # Iterate for the number of samples.
    x = 0.0

    # Thermalization (or equilibration steps)
    for i in range(n_therm):
       x = mh.metropolisHastings( x, (w+dw), sqrTrialWaveFunction, mh.uniTransProb )

    # Start sampling for local energy
    for i in range(n_sample):
       x = mh.metropolisHastings( x, (w+dw), sqrTrialWaveFunction, mh.uniTransProb )
       e_loc = locEneGS(x,w,dw)
       values_e_loc.append(e_loc)
    
    # Compute Mean value and Std err.
    mean_value, std_err = me.meanAndStdErr(values_e_loc)
    mean_value_e_loc.append(mean_value)
    std_err_e_loc.append(std_err)
    
# Plot dots
plt.errorbar(dw_list, mean_value_e_loc, yerr=std_err_e_loc, fmt='o')
plt.xlabel(f'$\Delta \omega$')
plt.ylabel(f'$E[\psi_T]$')
plt.axis([-0.6, 0.6, 0.5, 0.7])
plt.grid(True)
plt.show()
    