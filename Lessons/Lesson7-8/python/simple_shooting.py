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
Vext = 1000.0

# function of the energy
def factor(E,x):
    if x < L:
        V = V0
    else:
        V = Vext
    return -2.0 * (E-V)

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

# Arrays of the integration process
x   = np.zeros(nx)
psi = np.zeros(nx)

# Initial conditions at (x0=0):
x0 = 0.0
# Even solutions
psi0     = 1.0
der_psi0 = 0.0
# Odd solutions
#psi0     = 0.0
#der_psi0 = 1.0

# Initialize position array
x[0]   = x0
for ix in range(nx-1):
    x[ix+1] = x[ix]+dx
    
# Initialize wave function arrays
psi[0] = psi0
der_psi = der_psi0

# Choose energy for the shooting
E=0.2

# Euler-Cromer integration scheme (let's shoot!)
for ix in range(nx-1):
    der_psi = der_psi + factor(E,x[ix]) * psi[ix] * dx
    psi[ix+1] = psi[ix] + der_psi * dx

# Plot the final shooting
plt.plot(x, psi, 'b--',label='E={}'.format(E))
plt.legend()
plt.axis([0, L, -1.0,1.0])
plt.xlabel('x')
plt.ylabel('Psi(x)')
plt.show()



