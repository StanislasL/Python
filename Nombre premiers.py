# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:42:37 2016

@author: Stan and Jeff

Trouver tous les nombres premiers jusqu'à un rang n
"""

from math import *

n = int(input ("prime numbers until wich rank?"))

prime = []  #liste des nombres premiers

dividers = []  # liste des diviseurs d'un nombre

i = int(1) # curseur pour diviseur

j = int(1) # les nombre à tester


while j <= n:  # boucle qui ajoute les nombres premiers à la liste
    
    i = 1
    
    while i <= sqrt(j):        # boucle qui vérifie si un nombre est premier
    
        if j%i == 0 :               # divise le nombre par le curseur, si le reste est zéro,
            dividers.append(i)      # alors i est un diviseur de j
        i = i + 1
        
    if len(dividers) == 1:          #si la longeur de la liste des diviseurs est égal à un alors j est seulement divisible par un et par lui meme
        prime.append(j)   
     
    dividers[:] = []                #suppression de tous les diviseurs
    j = j + 1                       #le nombre suivant peut être tester   
        
print(prime)


        
            
    
    
    