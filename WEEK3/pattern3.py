# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:32:33 2020

@author: Sourick
------------------------------------------
Display The pattern following pattern :
------------------------------------------
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * * * 
* * * * * * * * * * * 
* * * * * * * * * * * * 
"""
n = int(input("Enter a range :"))
for i in range(1,n+1):
    for j in range(1,i):
        print("*",end = " ")
    
    print()