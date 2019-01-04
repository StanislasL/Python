# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:32:02 2018

@author: Stan
"""
def f(x,Q):
    y=0    
    for i in range(0,len(Q)):
        y=Q[i]*(x**i)+y
        
    return(y)

def df(x,Q):
    y = 0
    for i in range(1,len(Q)):
        y=Q[i]*i*(x**(i-1)) +y
   
    return(y)
    
def newtonroot(x,k,Q):
    for count in range (100):
        if abs(f(x,Q))>k:
            x = x - f(x,Q)/df(x,Q)
            
    print(x)
    return (x)


def Ruffini(C,x):

    n=len(C)
    Q=[0]*n;
    Q[0]=C[0];

    for k in range(1,n):
        Q[k]=Q[k-1]*x+C[k]
    
    return Q

P=[-3,-3,1,1]


for i in range(0,len(P)):
    P=Ruffini(P,newtonroot(1,0.000001,P))
    print(P)
    
    
