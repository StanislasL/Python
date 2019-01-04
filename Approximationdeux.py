# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:47:15 2017

@author: Stan
Approximation of integral

method n°2: trapezoid
"""
a = float(0) #borne sup

b=float(1) #borne inf

n = float(input("precision?"))

c=float((b-a)/n)#incrément

t=float(0) #petite somme

while a<b:
    t= t + c*(1/(1+a)) + c*((1/(1+a+c))-(1/(1+a)))/2
    
    a = a + c


print(t)       
