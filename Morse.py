# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:10:54 2017

@author: Stan
"""

import time
"""import RPi.GPIO as GPIO"""


#setup of led module

"""GPIO.setmode(GPIO.BOARD)
LED = 22
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.LOW)"""




#setup of variable
texte = str(input("insérer texte"))
morse = []
dic = {"A": [1,3], "B":[3,1,1,1], "C": [3,1,3,1], "D": [3,1,1], "E": [1], "F": [1,1,3,1], "G": [3,3,1], "S":[1,1,1], "O":[3,3,3],"H":[1,1,1,1],"I": [1,1],"J":[1,3,3,3],"K":[3,1,3],"L":[1,3,1,1],"M":[3,3],"N":[3,1],"P":[1,3,3,1],"Q":[3,3,1,3],"R":[1,3,1],"T":[3],"U":[1,1,3], "V": [1,1,1,3],"W":[1,3,3],"X":[3,1,1,3], "Y":[3,1,3,3],"Z":[3,3,1,1], " ":[7]}


#traduit le texte en morse
for i in range(len(texte)):
    morse.append(dic[texte[i]])
print(morse)
"""for i in range(len(texte)):
    time.sleep(3)
    for j in len(morse[i]):
        if morse[i[j]]== 1:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED, GPIO.LOW)
        elif morse[i[j]]== 3:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(LED, GPIO.LOW)
        elif morse[i[j]]==7:
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(7)
            GPIO.output(LED, GPIO.LOW)"""
