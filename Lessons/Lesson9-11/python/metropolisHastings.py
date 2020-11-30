import numpy as np
"""
Created on Tue Nov 24 11:25:06 2020

@author: Matteo Barboini
@e-mail: matteo.barborini@gmail.com

     Metropolis-Hastings algorithm in 1d
     
     Input variables
     x : initial position
     p : probability density to sample (Not normalized)
     t : transition probability
"""

# Transition probability amplitude
D = 1.0

# Propose a move with uniform probability in an interval [-D,+D]
# If dx != 0 returns the probability of the move (constant)
def uniTransProb(dx):
    global D
    if dx == 0.0:
        return (2.0*np.random.uniform()-1.0 ) * D
    else:
        return 0.5 / D

# Execute the metropolis-Hastrings dynamic at a position x, to sample 
# probability p(x) with a transition probability T(x)
def metropolisHastings(x,omega, P, T):
    
    # Extract a random move according to probability T
    dx = T(0.0)
    
    # New position
    x_new = x + dx
    
    # Compute ratio for acceptance probability
    A = P(x_new,omega) / P(x,omega) * T(x-x_new) / T(x_new-x)
    
    # Check acceptance
    if A >=1.0:
        #Accept move
        return x_new
    elif np.random.uniform() <= A :
        # Accept move
        return x_new
    else:
        # Refuse move
        return x
"""
    0         A                      1
   |---------|----------------------|
   
   Extract a random number nu in [0,1] with uniform probability
   
   1) nu <= A I accept the move (verified)
   
   2) nu > A  I refuse the move (not verified)
   
"""

    
"""
    Alternative way:
    if A >=1.0:
        #Accept move
        return x_new
    else:
        if np.random.uniform() <= A :
            # Accept move
            return x_new
        else:
            # Refuse move
            return x
    
"""            
    

