# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:51:32 2017
nexton mehod to find the roots of a function
@author: Stan
"""


#how does it works?
#start somewhere called x0, we aproximate the fuction at the tangent of f(x0)
#we look for the intersection of the tangent with the x absciss
#we take the new x and we look for the tagnet and the new x again and again
#if converges verry fast to the root
#this method doesn't always work, we have to do a smart guesse to find x0
#
#x0
#tangent: y = f'(x0)(x-x0)+ f(x0)
#U1 = (-f(U0)/f'(U0))+U0
#
#




def f(x):
    y = x*x*x + x*x - 3*x -3
    return(y)

def df(x):
    y = 3*x*x +2*x -3
    return(y)
    
def newtonroot(x,k):
    for count in range (100):
        if abs(f(x))>k:
            x = x - f(x)/df(x)
            

    return (x)

print(newtonroot(0,0.0000001))
print(newtonroot(100,0.0000001))
print(newtonroot(-100,0.0000001))    


