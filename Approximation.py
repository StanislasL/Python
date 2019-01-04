# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:15:54 2017

@author: Stan

Approximation of integral

method n°1: rectangles
"""

a = float(0) #borne sup

b=float(1) #borne inf

n = float(input("precision?"))

c=float((b-a)/n)#incrément

p=float(0) #petite somme

while a<b:
    p= p + c*(1/(1+a))
    
    a = a + c


print(p)       