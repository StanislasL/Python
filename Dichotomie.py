
"""
Created on Wed Feb  1 13:27:53 2017

Dichotomie

precision: k

difficultie: 10^-k


@author: Stan
"""
import math

#definir la fonction, ici un polynome
def f(x):
    y = math.log(x)
    #retourne l'image y = f(x)
    return (y)


#definition des bornes    
a = float(input("borne inf"))
b = float(input("borne sup"))   




def dichotome(a,b):
    for i in range (0,1000):
    
        if f((a+b)/2) > 0:
            b = (a+b)/2
        else:
            a = (a+b)/2
    return (a)
            
if f(a)<0 and f(b)>0:
    print(dichotome(a,b))
else:
    print('impossible')
   