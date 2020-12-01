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

"""
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

# Error in the frequency
dw = 0.1

# List of local energies
values_e_loc = []

# Change the diffusion constant
mh.D = 0.5

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
mean_value_e_loc, std_err_e_loc = me.meanAndStdErr(values_e_loc)

# Compute reblocked array
reblocked_e_loc = me.reblock(values_e_loc,20)

# Compute Mean value and Std err of reblocked array
rb_mean_value_e_loc, rb_std_err_e_loc = me.meanAndStdErr(reblocked_e_loc)

print('GS energy : ', mean_value_e_loc,'+/- ', std_err_e_loc)
print('GS energy : ', rb_mean_value_e_loc,'+/- ', rb_std_err_e_loc)

corr = me.autoCorrFunc(values_e_loc)
reblocked_corr = me.autoCorrFunc(reblocked_e_loc)

# Plot correlation
plt.plot(np.arange(0,100,1), corr[:], 'b--',label='Corr')
plt.plot(np.arange(0,100,1), reblocked_corr[:], 'r--',label='Corr')
plt.ylabel('R(t)')
plt.xlabel('t')
plt.axis([0, 50, 0, 1.0])
plt.grid(True)
plt.show()

