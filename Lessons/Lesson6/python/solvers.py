import numpy as np
'''
 Euler algorithm for Fourier's Heat equation
    u(x,t+dt)=u(x,t)+C[u(x+dx,t) + u(x-dx,t) - 2 u(x,t)]
    C = D dt/dx^2

 Input: 
    u[1:3] : vector at time t
    C      : Discretization Constant

 Output:
    u_f : Final atmplitude at time t+dt at postion x = u[1]
'''
def eulerFourier(C,u):
    u_f = u[1] + C * (u[0]+u[2]-2.0*u[1])
    return u_f

'''
 Crank-Nicolson d vector of length L/dx elements 
    d(x,t)=u(x,t)+C[u(x+dx,t) + u(x-dx,t) - 2 u(x,t)]
    C = D dt/dx^2

 Input: 
    u      : Full vector at time t
    C      : Discretization Constant

 Output:
    d      : d vector (see notes)
'''
def crankNicolson_d_vec(C,u):
   nx = len(u)
   d=np.zeros(nx)
   # Boundary conditions
   d[0]  = u[0]
   d[nx-1] = u[nx-1]
   # Defining other elements of the d vector
   for ix in range(1,nx-1):
      d[ix] = u[ix] + C * (u[ix-1]+u[ix+1]-2.0*u[ix])
   return d

'''
 Thomas algorithm to solve linear systems with 
 tridiagonal matrices without inversion.
   A v = d

 Input: 
    d      : Vector
    C      : Discretization Constant (used to build A matrix)

 Output:
    u      : u vector at time t + Dt (see notes)
'''
def thomas_algo(C,d):
   nx = len(d)
   alpha=np.zeros(nx)
   beta=np.zeros(nx)
   u_f=np.zeros(nx)
   # Build alpha beta coefficients
   alpha[0]= 0.0
   beta[0] = d[0] / 1.0 # 0.0
   for ix in range(0,nx-2):
      gamma = (1.0+(2.0+alpha[ix])*C)
      alpha[ix+1] = -C/gamma
      beta[ix+1] = (d[ix+1]+C*beta[ix])/ gamma
   beta[nx-1] =d[nx-1]
   # Build solution
   u_f[nx-1]=beta[nx-1]
   for ix in range(0,nx):
      u_f[nx-2-ix] = beta[nx-2-ix] - alpha[nx-2-ix] * u_f[nx-1-ix]
   return u_f