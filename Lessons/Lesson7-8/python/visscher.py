import numpy as np
import matplotlib.pyplot as plt
"""
Solving time dependent Schrodinger equation with Visscher's algorithm

ihbar d_t psi(x,t) = - hbar^2 / 2m d_x^2 psi(x,t) + V(x) psi(x,t)

Created on Tue Nov  4 10:18:41 2020

@author: Matteo Barborini
@e-mail: matteo.barborini@gmail.com

    Visscher algorithm
    ==================
    
    psi(x,t) = R(x,t) + i I(x,t)

    H = - hbar^2 / 2m d^2_x + V(x)

    V(x) = 0.0

    d_t R(x,t) = H I(x,t)
    d_t I(x,t) = - H R(x,t)

    General equations of Vissher algorithm
    R(x,t+Dt/2) = R(x,t-Dt/2) + H I(x,t) Dt
    I(x,t+Dt/2) = I(x,t-Dt/2) - H R(x,t) Dt

    Translated in time
    R(x,t+Dt) = R(x,t)         + Dt H I(x,t+Dt/2)
    I(x,t+3Dt/2) = I(x,t+Dt/2) - Dt H R(x,t+Dt)

    To self-start the algorithm we need R(x,t), I(x,t+Dt/2)

""" 

"""
    Initial condition
    psi(x,0) = (1/(2*pi*w^2))^{1/4} * exp( -(x-x0)^2/(4w^2) ) exp(i k0(x-x0))
"""
x0 = -15.0
w  = 1.0
k0 = 2.0 

# Space Integration variables
xmin = -25.0
xmax = 25.0
dx = 0.1
nx = int((xmax-xmin)/dx)+1

# Time integration variables
t0 = 0.0
T  = 7.0
dt = 0.001
nt = int((T-t0)/dt)+1

# Arrays for the integration
# Real/ Immmaginary parts
R = np.zeros(nx)
I = np.zeros(nx)
# New Real/Immaginary parts
Rnew = np.zeros(nx)
Inew = np.zeros(nx)
# Square modulus of the wave function
Psi2 = np.zeros(nx)

# Array of the positions
x = np.zeros(nx)
x[0] = xmin 
for ix in range(nx-1):
    x[ix+1] = x[ix] + dx

"""
    Building Initial condition
    psi(x,0) = (1/(2*pi*w^2))^{1/4} * exp( -(x-x0)^2/(4w^2) ) exp(i k0(x-x0))
"""
C = (1.0/(2.0*np.pi*w**2))**(0.25)
for ix in range(nx):
    R[ix] = C * np.exp(-(x[ix]-x0)**2 / (4.0*w**2)) * np.cos(k0*(x[ix]-x0))
    I[ix] = C * np.exp(-(x[ix]-x0)**2 / (4.0*w**2)) * np.sin(k0*(x[ix]-x0))
    Psi2[ix] = R[ix]**2 + I[ix]**2

# Project the I(x,t) at time I(x,t0+Dt/2)
for ix in range(nx):
    I[ix] = C * np.exp( -(x[ix]-x0-0.5*k0*dt)**2 /(4.0*w**2) ) * np.sin(k0*( x[ix]-x0 - k0*dt / 4.0 ))

# Plot the initial state
plt.plot(x, R, 'r:',label='R(x,t0)')
plt.plot(x, I, 'b--',label='I(x,t0)')
#plt.plot(x, Inew, 'b.-',label='I(x,t0+dt)')
plt.plot(x, Psi2, 'g--',label='|psi(x,t0)|^2')
#plt.legend()
#plt.axis([-25, 25, -1,1])
#plt.xlabel('x')
#plt.ylabel('')
#plt.show()


"""
    Visscher's evolution

    Translated in time
    R(x,t+Dt) = R(x,t)         + Dt H I(x,t+Dt/2)
    I(x,t+3Dt/2) = I(x,t+Dt/2) - Dt H R(x,t+Dt)

    H I(x,t+Dt/2) = - 0.5 * d^2_x I(x,t+Dt/2) = -0.5*[ I(x+Dx,t+Dt/2) + I(x-Dx,t+Dt/2) - 2.0 I(x,t+Dt/2)] / Dx**2
    H R(x,t+Dt)   = - 0.5 * d^2_x R(x,t+Dt)   = -0.5*[ R(x+Dx,t+Dt) + R(x-Dx,t+Dt) - 2.0 R(x,t+Dt)] / Dx**2

    R(x,t+Dt) = R(x,t)          - Dt / (2.0 Dx**2) * [ I(x+Dx,t+Dt/2) + I(x-Dx,t+Dt/2) - 2.0 I(x,t+Dt/2)]
    I(x,t+3/2Dt) =  I(x,t+Dt/2) + Dt / (2.0 Dx**2) * [ R(x+Dx,t+Dt) + R(x-Dx,t+Dt) - 2.0 R(x,t+Dt)]

    To self-start the algorithm we need R(x,t), I(x,t+Dt/2)
"""
#I[:] = Inew[:] 
for it in range(nt):

    # Update the Real part of the wave function
    for ix in range(1,nx-1):
        Rnew[ix] = R[ix] - 0.5*dt/dx**2 * ( I[ix-1] + I[ix+1] - 2.0 * I[ix] )

    # Update the immaginary part of the wave function
    for ix in range(1,nx-1):
        Inew[ix] = I[ix] + 0.5*dt/dx**2 * ( Rnew[ix-1] + Rnew[ix+1] -2.0 * Rnew[ix])

    for ix in range(nx):
        Psi2[ix] = Rnew[ix]**2 + I[ix] * Inew[ix]

    R[:] = Rnew[:]
    I[:] = Inew[:]



# Plot the initial state
plt.plot(x, R, 'r:',label='R(x,T)')
plt.plot(x, I, 'b--',label='I(x,T)')
plt.plot(x, Psi2, 'g--',label='|psi(x,T)|^2')
plt.legend()
plt.axis([-25, 25, -1,1])
plt.xlabel('x')
plt.ylabel('')
plt.show()





