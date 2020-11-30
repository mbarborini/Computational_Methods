#Importing numpy module
import numpy as np

# Defining the Forward derivative.
def derForward(f,x,dx):
  der = (f(x+h)-f(x))/dx
  return der


# Performing the derivative of the sin function at pi/2 with 
# a discretization error of 0.1
a = derForward(np.sin,np.pi/2.0,0.1)

#printing the result
print('Forwards derivative  :',a)
