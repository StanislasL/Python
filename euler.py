# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:12:51 2017

@author: Stan
"""
import matplotlib.pyplot as plt
import numpy as np

n = int(input('precision?'))

def f(x):
    return np.exp(x)



def  euler (F,a, b,p):
    Y = [F(a)]
    for i in np.arange(a,b,p):
        Y.append(Y[-1]+p*F(i))
    plt.plot(np.arange(a,b+p,p),Y,lw=1.5)

a=0
b=3
p= (b-a)/n
euler(f,a,b,p)

plt.show    
plt.title("Euler's Method")
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
       
