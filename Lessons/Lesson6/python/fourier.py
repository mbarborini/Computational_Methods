import numpy as np
'''
    Fourier's Heat equation

    d_t T(x,t) = D d^2_x T(x,t)

    lmbda  : Thermal conductivity
    sh     : Specific heat
    rho    : Density
    D      : Diffusion Constant
    
    L      : length of the system
'''
lmbda = 0.12
sh    = 0.113
rho   = 7.8

D = lmbda / (rho * sh)

L = 101.0

