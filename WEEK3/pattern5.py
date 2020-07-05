# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:35:34 2020

@author: Sourick
------------------------------------------
Display The pattern following pattern :
------------------------------------------

          *  
        * * *  
       * * * * *  
      * * * * * * *  
     * * * * * * * * *  
    * * * * * * * * * * * 
"""

n = int(input("Enter a value : "))
gap = n
rgn,display = 1,1
for i in range (1,n+1):
    for j in range(1,gap):
        print("",end = " ")    
        
    for k in range(1,rgn+1):
        print("*",end = " ")
        
    print(" ")
    gap -= 1
    rgn += 2

