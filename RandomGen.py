# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 22:13:00 2018

@author: stan

Prologin quizz

Gen random modulo linear
"""

n = 1
x = 42

while n <334:
    x = (1337*x + 404)%100
    n = n+1

print (x)