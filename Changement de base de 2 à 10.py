"""
Created on Wed Jan 11 13:38:09 2017

@author: Stan

Changing a number from a basis to another basis
basis in 2,10
"""


n = int(input("nombre?"))
#b = int(input("base du nombre?"))
f = int(input("base finale du nombre?"))

def tobaseten(n,b):    
    g = 0    
    for i in range (0,len(str(n))):
        g = g + (n - 10*int(n/10))*b**i
        n = int(n/10)
    return(g)
    
        
def tofinalbase(n,f):
    g=0
    i=0
    while n > f:
        r = n%f
        g = g + (r*f**i)*10**i
        n = (n-r)/f
        i = i + 1
    return(g)


print(tofinalbase(n,f))

        
        
            
        
