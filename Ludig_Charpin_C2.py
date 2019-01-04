
"""
@author: Stanislas LUDIG and Henri CHARPIN
"""

from random import randint
#import of the necessary modules



SortedA = []
#creating an empty list that will be sorted


UnsortedA = []
#creating an empty lis that will be fullfilled with random integers

for i in range(100):
    UnsortedA.append( randint(0, 1000) )
#fulfilling the list with random numbers


#defining a function that is able to find the maximum of a function
def maxi(UnsortedA):
    maximum = UnsortedA[0]    
#starting with the first value and saying it's is maximum    
    l = len(UnsortedA)    
#assigning the lenght of the list (which is going to change) to a variable    
    for i in range(0,l):
#loop that check if every value of the list is greater than the one before
        if maximum >= UnsortedA[i]:
#if no, the maximum stay the same            
            maximum = maximum
        else:
#if yes, the maximum takes the value checked            
            maximum = UnsortedA[i]
    return(maximum)
#returning the maximu of the list



for i in range(0,100):
#there are 100 numbers in this list so we have to iterate 100 time
    m = maxi(UnsortedA)
#assigning the value of the maximum to a variable    
    SortedA.append(m)
#adding this value to the sorted list
    UnsortedA.remove(m)
#removing the maximum value from the unsorted list

#printing the sorted list
print(SortedA)



#Comment:
#We tried to do it first with NDarrays and using a defined by user function
#but it is impossible (We believe so...)

#In fact a function, as far as we know can only return one variable, so here the value of the max
#We cannot just remove a value in an array, we have to replace it by another
#we could have find the maximum and put it in front of the array and then look for 
#the maximum after the first value, but
#In an array there exist no function deleting a value  without knowing its index
#and the function doesn't give us its index
#there would be an alternative using the numpy.where(UnsortedA==max) but the answer is a tupple
#and not its index.







    
    
    



    