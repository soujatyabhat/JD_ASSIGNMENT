# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:41:27 2020

@author: Sourick

----------------------------------------
check a number is perfect number or not
----------------------------------------
"""
n = int(input("Enter number : "))
temp,sum = n,0
for i in range(1,n):
    if n % i == 0:
        sum += i
    
if sum is temp:
    print("Given value is Perfect") 
else:
    print("Given value is not perfect")

