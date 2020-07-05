# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:35:34 2020

@author: Sourick

------------------------------------------
Display The pattern following pattern :
------------------------------------------

     1  
   2 3 4  
 5 6 7 8 9  
10 11 12 13 14 15 16 
 
"""

n = int(input("Enter a value : "))
gap = n
rgn,display = 1,1
for i in range (1,n+1):
    for j in range(1,gap):
        print("",end = " ")    
        
    for k in range(1,rgn+1):
        print(display,end = " ")
        display += 1
        
    print(" ")
    gap -= 1
    rgn += 2

