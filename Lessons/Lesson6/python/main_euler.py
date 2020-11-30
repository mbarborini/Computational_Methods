import numpy as np 
import matplotlib.pyplot as plt
import fourier as f
import solvers as s 

'''
 Solve diffusion equation with Euler

 d_t T(x,t) = D d^2_x T(x,t)

 @author Matteo Barborini
 @e-mail matteo.barborini@uni.lu
'''

# Time Integration variables
t0 = 0.0              # initial time
tf = 10000.0          # Final time
dt = 0.1             # Time step
nt = int((tf-t0)/dt)+1  # Number of time integration steps

# Space integration variables
x0 = 0.0
dx = 1.0             
nx = int((f.L-x0)/dx)

# Stability conditions of Euler
print(dt,'<=',dx**2/(2.0*f.D))

# Amplitude of the system u=T(x,t)
u    = np.zeros(nx)
unew = np.zeros(nx)

# Vector of the positions 
x = np.zeros(nx)
x[0] = x0
for ix in range(nx-1):
    x[ix+1] = x[ix] + dx

# Initial conditions of u in (0,L) 
u[1:nx-1] = 100.0 # Constant

# Boundary conditions
u[0] = 50.0
u[nx-1] = 0.0

unew[0] = 50.0
unew[nx-1] = 0.0

# Constant
C = f.D * dt / dx**2

for it in range(nt-1):
    
    for ix in range(1,nx-1):
        #print(C,u[0,ix-1:ix+2])
        #unew[ix] = u[ix] + C * ( u[ix+1] + u[ix-1] - 2.0 * u[ix] )
        unew[ix] = s.eulerFourier(C,u[ix-1:ix+2])
    
    u[:] = unew[:]

    # Plotting every 10000 steps
    if ( it % 10000 == 0): 
        plt.plot(x[:], u[:], 'b--',label='')

        
plt.legend()
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.axis([0, 100,0, 120])
plt.show()
