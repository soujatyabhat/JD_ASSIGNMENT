# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:59:33 2020

@author: Sourick

--------------------------------------------
Find out the sum of : 1!+2!+3!+4!+……………..
--------------------------------------------

"""
n = int(input("Enter a value : "))
fact,sum = 1,0
for i in range(1,n+1):
    for j in range (i,0,-1):
        fact *= j
    
    sum += fact
    fact = 1
print("The sum is : ",sum)

    
        
        
        

