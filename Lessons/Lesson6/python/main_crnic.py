import numpy as np 
import matplotlib.pyplot as plt
import fourier as f
import solvers as s 

'''
 Solve diffusion equation with Crank-Nicolson
 @author Matteo Barborini
 @e-mail matteo.barborini@uni.lu
'''

# Integration variables
t0 = 0.0              # initial time
tf = 10000.0            # Final time
dt = 0.1              # Time step
nt = int((tf-t0)/dt)  # Number of time integration steps

dx = 1.0              # Space discretization step
nx = int(f.L/dx)
# Amplitude of the system
u = np.zeros((2,nx))

# Vector for plotting
x = np.zeros(nx)
for ix in range(nx-1):
    x[ix+1] = x[ix] + dx

# Initial conditions of u in (0,L) 
u[0,1:nx-1] = 100.0 # Constant

# Constant
C = f.D * dt / dx**2

for it in range(nt-1):
    d = s.crankNicolson_d_vec(C,u[0,:])
    u[1,:] = s.thomas_algo(C,d[:])
    u[0,:]=u[1,:]
    if ( it % 10000 == 0): plt.plot(x[:], u[0,:], 'b--',label='')

#plt.plot(x[:], u[0,:], 'b--',label='Position')
plt.legend()
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.axis([0, 100,0, 120])
plt.show()
