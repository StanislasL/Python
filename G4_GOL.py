"""
Created on Thu Dec 22 09:24:53 2016

Group 4

Jeu de la vie V03 

@author: Stanislas, Hugo Lebret and Alix
"""


#importing the modules, here tkinter for the animation and numpy for the array
import tkinter as tki
import numpy as np


#creating a random array of 0 and 1 size 100x100
arrayV = np.random.randint(2,size=(100,100))

#defining the first function that check the state of the neighborhood of a cell and return an integer from 0 to 8
def check(arrayV,i,j):
    # setting our neighbourhood number as ato zero
    a=0
    #a first for loop to check each column    
    for z in range(-1,2):
        #another loop to check the three vzlues of each column        
        for s in range(-1,2):
            # a first If statement to uncount the state of the middle cell            
            if not(z==0 and s==0):
                # the secon If statement to add 1 tothe total (a) if the cell is alive ans zero if it is dead               
                if arrayV[i+z,j+s]==0:
                    a=a+0
                else:
                    a=a+1
    return(a)  # returning the total neighborhood


#creating a function that generate a new generation of array
def newgen(): 
    #the global function states that when the arrayV variable changes inside the function, it changes in all the programm  
    global  arrayV
    #creating an new aray of zeros from the same dimensions
    arrayN = np.zeros((100, 100), dtype='i')
    #goign through each column of the array except th first one and the last one to avoid the border problem
    for i in range(1,99):
        #going through each  row except the first and the last one to avoid the border problem
        for j in range(1,99):
            # calling the check function define above to get the total of the neighbourhood of the cells
            T=check(arrayV,i,j)
            # if the cell is alive,            
            if arrayV[i,j] == 1:
                #and the neighborhood greater than 3                
                if T > 3:
                    #the cell die because of overpopulation                    
                    arrayN[i,j] = 0
                # else if the neighborhood is smaller than 2
                elif T < 2:
                    #the cell die because for loneliness
                    arrayN[i,j] = 0
                #else if the neighborhood is equal to 2 or 3
                elif T == 2 or T == 3:
                    #the cell stays alive
                    arrayN[i,j] = 1
                
            #else if the cell was dead
            elif arrayV[i,j] == 0:
                #and the neighborhood is equal to 3
                if T == 3:
                    # then the cell can born
                    arrayN[i,j] = 1
                #else the cell stays dead
                else:
                    arrayN[i,j] = 0
    #the old generation is replaced by the new
    arrayV = arrayN.copy()
    
    
#defining a function that will animate the array using tkinter    
def newgen_show():
    #defining the width of a cell in pixel (br for 'breite' in german)
    br=5
    #defining a list of colors, the index 0 is white(dead) and 1 is black(alive)
    farbe=['white','black']
    #setting the first pixel    
    y0=0
    # for eache column
    for z in range(100):
        x0=0 # for eache row
        for s in range(100):
            #creating a rectangle in the canvas (coordonate of the top right angle, coordonate of the bottom left angle, filling the rectangle with the color list, the outline of the rectangle is white)            
            can1.create_rectangle(x0,y0,x0+br,y0+br,fill=farbe[arrayV[z,s]], outline= 'white')
            #increasing the coordonate with the length of the rectangle            
            x0=x0+br
         #increasing the coordonate with the length of the rectangle     
        y0=y0+br
    #calling the newgen function   
    for i in range (0,100):
        newgen()
            
    
 
#creating a new window (fenster in german) using TKinter            
fen=tki.Tk()
#creating a new button on the window( text is newgen, it ispink when we click on it, and the font become red, the delay is 500 ms before it action start, and if you stay clicking on it it reactivate every 10ms, ridge is a type of button, and it activate the function newgen_show)
but_Next=tki.Button(fen,text='next generation', activebackground= 'pink', activeforeground= 'red', repeatdelay=500, repeatinterval=10,overrelief= 'ridge', command=newgen_show)
#creating a quit button in the window, asking to destroy the window
but_Quit=tki.Button(fen,text='quitte',command=fen.destroy)
#creating our canvas in the window, with a blue background
can1=tki.Canvas(fen,height=500,width=500,bg='blue')
#the canvas is now on the left side of the window
can1.pack(side='left')
#flaunting the two buttons on the right side of the window
but_Next.pack(side='right')
but_Quit.pack()
#finishing the tkinter loop and destroying the window
fen.mainloop()
fen.destroy()
 
   

  
    