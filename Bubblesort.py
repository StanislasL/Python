# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:33:11 2017

@author: Stan
"""
from random import randint
UnsortedA = []
for i in range(10):
    UnsortedA.append( randint(0, 10) )

UnsortedB = list(UnsortedA)


def bubbleSort(UnsortedA):
    for j in range(len(UnsortedA)-1,0,-1):
        for i in range(j):
            if UnsortedA[i]>UnsortedA[i+1]:
                a = UnsortedA[i]
                UnsortedA[i] = UnsortedA[i+1]
                UnsortedA[i+1] = a
    return(UnsortedA)
    
print(bubbleSort(UnsortedA))