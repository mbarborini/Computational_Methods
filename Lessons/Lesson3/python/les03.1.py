import numpy as np 
import matplotlib.pyplot as plt
import harmosc as ho
import ode 

# Integration variables
t0 = 0.0             # initial time
tf = 100.0           # Final time
dt = 0.05            # Time step
n = int((tf-t0)/dt)  # Number of integration steps

# Initial condition of the system
x0 = 2.0
v0 = 3.0

# Exact solution is
# x(t) = A cos(omega t + delta)
delta=np.arctan(-v0/(ho.omega*x0))
A = x0 / np.cos(delta)

# Arrays that contain the time evolution
t = np.zeros(n) # Time evolution
x = np.zeros(n) # Position evolution
v = np.zeros(n) # Velocity evoution
ene = np.zeros(n) # Evoluction of the energy

x_exact = np.zeros(n) # Exact Position evolution
v_exact = np.zeros(n) # Exact Velocity evoution

#print('Array x:',x)
#print('Array t:',t)
#print('Array v:',v)

x[0] = x0     # Initial position
v[0] = v0     # Initial velocity
t[0] = t0     # Intial time
ene[0] = ho.energy(x0,v0)
x_exact[0] = x0     # Initial position
v_exact[0] = v0     # Initial velocity
#print('Array x:',x)
#print('Array t:',t)
#print('Array v:',v)

# Start the loop over time steps
# Loop for i in [0:n-1]
for i in range(0,n-1):
    x[i+1], v[i+1] = ode.euler(dt,ho.phi,x[i],v[i])
    ene[i+1] = ho.energy(x[i+1], v[i+1])
    t[i+1] = t[i] + dt
    angle = ho.omega*t[i+1]+delta
    x_exact[i+1] = A * np.cos(angle)
    v_exact[i+1] = -ho.omega * A * np.sin(angle)

#print('Array x:',x)
#print('Array t:',t)
#print('Array v:',v)

#print(ene)
plt.plot(t[:], x[:],'b--',label='Position')
plt.plot(t[:], v[:],'r-',label='Velocity')
plt.legend()
plt.xlabel('t')
plt.ylabel('')
plt.axis([0, 100,-6,+6])
plt.show()

plt.plot(t[:], x[:]-x_exact[:],'b--',label='Position')
plt.plot(t[:], v[:]-v_exact[:],'r-',label='Velocity')
plt.legend()
plt.xlabel('t')
plt.ylabel('Error')
plt.axis([0, 100,-6,+6])
plt.show()

plt.plot(t[:], ene[:],'b--',label='Position')
#plt.legend()
plt.xlabel('t')
plt.ylabel('Energy')
plt.axis([0, 100,17.0 ,35])
plt.show()
