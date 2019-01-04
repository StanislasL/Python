"""
Wolram rule 110

Group 4


@author: Stanislas, Hugo Lebret and Alix
"""

#importing numpy and tkinter
import numpy as np
import tkinter as tki



#setting the size of the array
fw = 600
ng = 600
#setting the location of the first cell
sp = 300
#creating a 1D array of zero
now0=np.zeros(fw,dtype=int)
#creating te first living cell
now0[sp]=1  
#creating the array containing the nest generation
aft0=np.zeros(fw,dtype=int)


#creating a window (fenster in german)
fen=tki.Tk()
#creating a canvas with the size of the array multiply by the width of a rectangel (9), with cyan colour
can1=tki.Canvas(fen,width=fw*2,height=(fw*1)+1,bg='cyan')

#setting a list of color that we are going to use
farbe=['cyan','red']
#setting the coordontae of the first rectangle
y0=0


#creating a function showing a new array
def affiche():
    #when this two variables are changing in the function, they change in th whole programm
    global y0,new0
    # if we didn't reach the end of the canvas,
    if y0 < fw*1:
        #setting the x coordonate of the rectangle        
        x0=0
        #for each cell of the new array        
        for i in range(600):
            #create a rectangle(coordonates, color, outline)            
            can1.create_rectangle(x0,y0,x0+2 ,y0+2 ,fill=farbe[now0[i]], outline= 'cyan')
            #increasing the coordonates for the next cell            
            x0=2*i
        #increasing the coordonate for the next array
        y0+=2
        #calling for a new gen
        newgen()  
    #elsse if we reached the end of the canvas, erase an start again
    else:
        efface()
        
        
         
       
#defining the erase function        
def efface():
    #setting these variable as global variables    
    global now0,y0,fw
    #deleting all the canvas    
    can1.delete('all')
    #resetting all the variables to the begining
    fw=600 
    now0=np.zeros(fw,dtype=int)
    now0[sp]=1
    y0=0
    

#defining a function that create a new generation
def newgen():
    #setting this variable as global
    global now0
    #for each cell in the old array except the first and the last one to prevent the border problem    
    for p in range(1,fw-1):      
        #neighborhood = 100*the lect cell, 10*the middle cell, the right cell ==> the NB is written in binary        
        nb=100*now0[p-1]+10*now0[p]+now0[p+1]
        # the rule 110 says that when nb is greater than 100 or equal to 0, the the cell dies
        if (nb == 111) or (nb == 100) or (nb == 0):
            aft0[p]=0
        # if not, the cell lives
        else:
            aft0[p]=1
    #copying the new geneartion into the old one
    now0 = aft0.copy()
       


#creating a new button on the window( text is newgen, it ispink when we click on it, and the font become red, the delay is 500 ms before it action start, and if you stay clicking on it it reactivate every 100ms, ridge is a type of button, and it activate the function affiche)
butt=tki.Button(fen,text = 'Next Gen', activebackground= 'pink', activeforeground= 'red', repeatdelay=500, repeatinterval=100,overrelief= 'ridge', command=affiche)
#creating an erase button that will call the erase function
butt_erase=tki.Button(fen,text='erase',command=efface)
#creating a quit function to leave the window
butt_Q=tki.Button(fen,text='quitte',command=fen.destroy)
#the grid function position the buttons sticking to the east side of the window, in a certain row
butt.grid(row=0, sticky='E')
butt_erase.grid(row=1, sticky='E')
butt_Q.grid(row=2,sticky='E')
#setting the location of the canvas int the grid function
can1.grid(row=1,column=3,rowspan=3,padx=10,pady=3)

#ending the tkinter loop  
fen.mainloop()