# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 15:44:44 2016

@author: Stan

aller voir ce site obliger http://www.tangentex.com/CalculSymbolique.htm
Etude de fonction
"""

# tout d'abord importer les biblis necéssaires et les variables

from __future__ import division

from sympy import *

init_session()

x, y, z, t = symbols('x y z t')

k, m, n = symbols('k m n', integer=True)

f, g, h = symbols('f g h', cls=Function)

init_printing()

# pour une fonction en 2D

plot(1/x**2, (x, -10,10))    # plot(fonction,(x allant de a,b))



# pour ploter une focntion 3d

from sympy.plotting import plot3d

plot3d(x**13+y**13, (x, -5,5), (y,-5,5))


