#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 10:21:25 2020

@author: vvassilevg
"""

#If you don't have scikit learn installed : write !pip install sklearn  on the ipython console (downright)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import rbf_kernel, laplacian_kernel, polynomial_kernel
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import KFold


def RBF(X1, X2, gamma): #Gaussian Kernel
    
    return rbf_kernel(X1, X2, gamma)

def Train(Kernel_matrix, Y, lam): #Calculating regression coefficients
    
    I = np.identity(Kernel_matrix.shape[0])
    K = Kernel_matrix + lam * I
    
    K_inv = np.linalg.inv(K)
    
    alphas = np.matmul(K_inv,Y)
    
    return alphas

def Predict(X_test, X_train, alphas, gamma): #Prediction of targets
    
    K_mat = RBF(X_test, X_train, gamma)
    
    Y = np.dot(alphas.T, K_mat.T)
    
    return Y

def KRR(lam_arr, gamma_arr, train_set, test_set):
    
    
    MAE_opt = 100000
    for lam, gamma in [(lam, gamma) for lam in lam_arr for gamma in gamma_arr]:
        
        K_mat = RBF(train_set[:,0].reshape(-1,1),train_set[:,0].reshape(-1,1), gamma)
        
        alpha_arr = Train(K_mat, train_set[:,1].reshape(-1,1), lam)
        
        Y_pred = Predict(test_set[:,0].reshape(-1,1), train_set[:,0].reshape(-1,1), alpha_arr, gamma)
        
        MAE = mean_absolute_error(test_set[:,1].ravel(), Y_pred.ravel())
        #print('lambda:' , lam, 'gamma:', gamma, 'MAE:', MAE)
        print('MAE_opt', MAE_opt)
        print()
        if MAE < MAE_opt:
            MAE_opt = MAE
            Y_pred_opt = Y_pred
            lam_opt, gamma_opt = lam, gamma
            alphas_opt = alpha_arr
            
    return Y_pred_opt, lam_opt, gamma_opt, alphas_opt, MAE_opt
        
        
    
lam_arr = np.array([1e-10, 1e-7]) 
gamma_arr = np.array([1e-3, 0.1])   

X = np.linspace(0,20, num=1000).reshape(-1,1)
Y = np.sin(X) + (np.random.rand(X.shape[0])*0.3 - 0.15).reshape(-1,1)


cross_Kfold = KFold(n_splits=5, shuffle=True)

i = 1
for train_index, test_index in cross_Kfold.split(X):
    print('FOLD : ', i)
    i = i + 1
    train_set = np.concatenate((X[train_index,:], Y[train_index,:]),axis=1)

    test_set = np.concatenate((X[test_index,:], Y[test_index,:]),axis=1)
    
    Y_pred, lam, gamma, alphas, MAE = KRR(lam_arr, gamma_arr, train_set, test_set)
    
    Yp_all = Predict(X, train_set[:,0].reshape(-1,1), alphas, gamma)
    
    plt.scatter(X,Y, color='black', label='original data')
    plt.plot(X, Yp_all.reshape(-1,1), color='red', label='KRR')
    plt.legend()
    plt.show()    


