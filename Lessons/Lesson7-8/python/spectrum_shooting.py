'''
    Solve the time-independent Schrodinger equation with the shooting method.
    - (hbar^2 / 2m ) psi'' = (E-V) psi

    psi'' = -2m / hbar^2 (E-V) psi

    m=1 
    hbar = 1

    psi'' = -2.0 *(E-V) psi

    Euler-Cromer as integrator method.
'''
import numpy as np
import matplotlib.pyplot as plt
'''
 Definition of the potential energy for an initinite well
            V_ext  for x<= -L  
    V(x) =  V_o    for -L < x < L
            V_ext  for x=> L

 Thus the wave function is 0 in x= +/-L 
'''       
L    = 1.0
V0   = 0.0
Vext = 10000.0

# function of the energy
def factor(E,x):
    if x < L:
        V = V0 
    else:
        V = Vext 
    return -2.0*(E-V) 

# Spatial integration interval
# Number of discretization steps included 0.
nx = 1001
'''
Number of segments in which we divide the space (nx)

 1   2   3   4   5   6   7               1000
---|---|---|---|---|---|---|-----   ----|---|

Number of points that I use for the integration are (nx+1) 
0   1   2   3   4   5            1000
|---|---|---|---|---|--        ---|
'''
dx = L / float(nx-1)

# Initial conditions for the integration
# Even solutions
psi0     = 1.0
der_psi0 = 0.0
# Odd solutions
#psi0     = 0.0
#der_psi0 = 1.0

# Build array of the wave function
psi = np.zeros(nx)
x = np.zeros(nx)

# Set initial values
psi[0]  = psi0 
der_psi = der_psi0

# Initialize position array
x0 = 0.0
x[0]   = x0
for ix in range(nx-1):
    x[ix+1] = x[ix]+dx

# Start first shooting loop with Euler
print('Initial conditions are:')
print(' Psi(0)    :',psi[0])
print(' der_psi(0):',der_psi)

# Compute first ne eigenvalues and plot corresponding eigenfuntions.
ne = 4

# Set initial energy to
E = 0.0

# Start the loops on the eigen values
for ie in range(ne):
    # Initialize energy variation and accuracy
    de = 0.1
    e_cut = 1.0e-5
    # Initialize first energy from previous
    E = E + de
    # Do a first shooting with energy:
    psi[0]  = psi0 
    der_psi = der_psi0
    for ix in range(nx-1):
        der_psi = der_psi + factor(E,x[ix]) * psi[ix] * dx
        psi[ix+1] = psi[ix] + der_psi * dx

    # Store value of the wave function in x=L
    # We need it to compare the signs!
    psi_old = psi[nx-1]
    
    while abs(de)>=e_cut:
        psi[0]  = psi0 
        der_psi = der_psi0

        for ix in range(nx-1):
            der_psi = der_psi + factor(E,x[ix]) * psi[ix] * dx
            psi[ix+1] = psi[ix] + der_psi * dx

        # Check sign variation (did we cross an eigenvalue?)
        if psi_old*psi[nx-1] < 0:
            de = -0.1*de
        # Update energy
        E = E + de
        # Store old wave function
        psi_old = psi[nx-1]

    # Plot Eigenfunction
    plt.plot(x, psi, 'b--',label='E_{} : {}'.format(ie,E))
    # print eigenvalue
    print('E_{} : {}'.format(ie,E))

# Print final picture        
plt.legend()
plt.axis([0, L, -1.0,1.0])
plt.xlabel('x')
plt.ylabel('Psi(x)')
plt.show()

        


