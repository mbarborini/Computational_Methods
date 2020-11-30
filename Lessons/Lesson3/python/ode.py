'''
 Euler algorithm for harmonic oscillator.
    x(t+dt)=x(t)+v(t)dt
    v(t+dt)=v(t)+phi(t)dt

 Input: 
    x_i : Initial position
    v_i : Initial velocity
    phi : Initial - omega**2 x (Function)
    dt  : Time step

 Output:
    x_f : Final position
    v_f : Final velocity
'''
def euler(dt,phi,x_i,v_i):
    v_f = v_i + phi(x_i) * dt
    x_f = x_i + v_i * dt
    return x_f, v_f