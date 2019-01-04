# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:35:20 2017

@author: Stan

roses
"""

import tkinter as tki
import math as mt

fen=tki.Tk()

can1=tki.Canvas(fen,width=600,height=600,bg='cyan')
can1.pack


def afficher(d,n):
    for i in range(0,360):
        k= (n.get()+7)/d.get()
        x= mt.cos(k*i)*mt.cos(i)+300
        y= mt.cos(k*i)*mt.sin(i)+300
        can1.create_oval(x,y,20,20)

n = tki.Scale(fen, orient='horizontal', from_=1, to=100,command=afficher)
n.pack()

d = tki.Scale(fen,orient='horizontal',from_=1, to=100,command=afficher)
d.pack()


can1.pack()
fen.mainloop()














