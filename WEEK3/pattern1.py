# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:09:29 2020

@author: Sourick
------------------------------------------
Display The pattern following pattern :
------------------------------------------
1  
2 3  
4 5 6  
7 8 9 10  
11 12 13 14 15 

"""
sum = 1
n = int(input("Enter a value : "))
for i in range(1,n+1):
    for j in range (1,i+1):
        print(sum,end = " ")
        sum += 1
    print(" ")