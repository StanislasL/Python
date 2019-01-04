# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:06:19 2017

@author: Stan
Approximation of integral

method n°3: simpson
"""
a = float(0) #borne sup

b=float(1) #borne inf

n = float(input("precision?"))

c=float((b-a)/n)#incrément

t=float(0) #petite somme

while a<b:
  
    t= t + c*((1/(1+a+c)) + (1/(1+a)))/6 + (2/3)*(1/((2*a+c)/2))*c
    
    a = a + c


print(t)    
