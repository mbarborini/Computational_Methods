#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:12:14 2020

@author: vvassilevg
"""

import numpy as np
import matplotlib.pyplot as plt


def get_data(Dataset): #Function to get features and target from a Dataset file
    File = open(Dataset, 'r') #Opens the file for reading
    
    Data = []
    for line in File:
        if '#' not in line:
            Data.append(np.array(['1'] + line.split()))

    File.close()
    Data = np.array(Data).astype(float)
    
    X, y = Data[:,:-1], Data[:,-1].reshape(-1,1)
    
    return X, y
    
def min_max_normalization(A): #Feature scaling
    
    MinA = np.amin(A, axis=0)
    MaxA = np.amax(A, axis=0)
    
    for i in range(A.shape[1]):
        if MinA[i] != MaxA[i]:
            A[:,i] = (A[:,i] - MinA[i]) / (MaxA[i] - MinA[i])
            
    return A, MinA, MaxA

def hyp_f(X, Theta): #Computes hypothesis
    
    return X.dot(Theta)

def loss_function(X, y, Theta): #Computes the loss function
    
    sq_error = (hyp_f(X,Theta) - y)**2
    Loss = 0.5 * np.mean(sq_error)
    
    return Loss

def grad_loss(X, y, Theta, j): #Computes the partial derivative of the loss function
    
    error = hyp_f(X, Theta) - y
    grad = X[:,j] * error.ravel()
    
    return np.mean(grad)
   
    

Dataset = 'House_price.dat' #The name of the file containing our data

X, y = get_data(Dataset) #Getting data from dataset file

X_train, y_train = X[:,:], y [:,:] #Setting training set

X_train, MinX, MaxX = min_max_normalization(X_train) #Scaling features X
y_train, Miny, Maxy = min_max_normalization(y_train) #Scaling targets y


#Setting up GD
Max_step = 50 #Maximum number of iterations allowed
n_parameters = 2 #Number of parameters to optimize (Theta)
alpha = 0.01 #Learning rate

Theta = np.random.rand(n_parameters).reshape(-1,1) #Setting Theta randomly
#Theta = np.array([0.45, 0.75]).reshape(-1,1) #Setting Theta manually

Loss = [loss_function(X_train, y_train, Theta)]

print('Step: 0', 'Loss: ', Loss[0], 'Theta: ', Theta[0,0], Theta[1,0])

#Do GD
for Step in range(Max_step):
    grad = []
    for j in range(n_parameters):
        grad.append(grad_loss(X, y, Theta, j)) #Compute partial derivatives of the Loss
    
    Theta = Theta - alpha*np.array(grad).reshape(-1,1) #Update Theta
    Loss.append(loss_function(X_train, y_train, Theta))
    print('Step: ', Step + 1, 'Loss: ', Loss[Step+1], 'Theta: ', Theta[0,0], Theta[1,0])

#Plot the Loss function as a function of steps
#plt.plot(np.arange(len(Loss)), np.array(Loss))
#plt.xlabel('Step')
#plt.ylabel('Loss function')
#plt.show()   

#Recover the original scale of the data and the prediction
X = X_train[:,1]*(MaxX[1] - MinX[1]) + MinX[1]
y = y_train*(Maxy - Miny) + Miny
hyp = hyp_f(X_train,Theta).ravel()*(Maxy-Miny) + Miny


#Plot the original data with a scatter plot and the learned function with a full line
plt.scatter(X, y.ravel())
plt.plot(X, hyp, color='black')
plt.show()


