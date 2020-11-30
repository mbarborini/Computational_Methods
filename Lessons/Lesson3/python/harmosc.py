import numpy as np
'''
 Harmonic oscillator:
    dot x(t) = v(t)
    dot v(t) = phi(t) = - omega**2 x(t)
'''

# Global variable of the module.
m = 3.0  # Mass
k = 2.0  # Harmonic constant
omega=np.sqrt(k/m) # Frequency

# Function to compute Phi(x)
def phi(x):
    global omega
    #print('Position  : ',x)
    #print('Frequency: ', omega)
    return -omega**2 * x 

# Function to compute the energy of the oscillator
def energy(x,v):
    global m, k
    return 0.5*m*v**2+0.5*k*x**2






