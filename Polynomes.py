# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:43:25 2016

@author: Stan and Jeff

Demander un polynome de degres n, afficher sa dérivée ansi que sa primitive
"""

import numpy as np

degree = int(input("give the degree of the polynomial"))

poly = np.zeros(degree+1,dtype=float)
derivative = np.zeros(degree+1)
antiderivative = np.zeros(degree + 1)




for i in range(degree+1):
    myquestion = "give the coefficent for degree" + str(i)+":"    
    a = int(input(myquestion))
    poly[i] = a                                 #création des coefficients du polynome
    derivative[i] = (degree - i)* a              # création des coefficeints de la dérivée
    antiderivative[i] = a/(degree + 1 - i)      #création des coefficients de la primitive



    
mypoly = ""
myderivative = ""
myantiderivative = ""

for i in range(degree+1):
    mypoly = mypoly + str(poly[i]) + "x^" + str(i) + " + " # création de la chaine de carractère du polynome
    myderivative = myderivative + str(derivative[i]) + "x^" + str(i) + " + "            # création de la chaine de carractère de la dérivée
    myantiderivative = myantiderivative + str(antiderivative[i]) + "x^" + str(i) + " x "    # création de la chaine de carractère de la primitive
    

    

print (mypoly)
print (myantiderivative + " + " + "constante")
print (myderivative)