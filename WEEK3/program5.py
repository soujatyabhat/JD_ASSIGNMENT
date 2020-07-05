# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 22:54:12 2020

@author: Sourick

-----------------------------------------------------------
Write a program in python to print all the prime numbers
from 5 to 50 
-----------------------------------------------------------

"""
flag = 0
print("The Series is : ")
for i in range(2,200):
    temp = i
    for j in range(2,(temp//2)+1):
        if temp % j == 0:
            flag = 1
            break
    if flag == 0:
        print(i,end = " ")
    flag = 0
        

