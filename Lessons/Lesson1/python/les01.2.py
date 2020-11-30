import numpy as np

# Integration Midpoint method
def intMidPoint(f,a,b,n):
    dx = (b-a)/n
    r = 0.0
    x = a + dx*0.5
    for i in range(n):
        r = r + f(x)
        x = x + dx
    r = r*xd
    return r

# Performing the integral of the sin function between 0 and pi 
# dividing the interval in 10 steps
k = intMidPoint(np.sin,0.0,np.pi,10)

# Printing the result of the integration
print('The integral of sin(x) between 0 and pi is :',k)
