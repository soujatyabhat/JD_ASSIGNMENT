# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 07:49:41 2020

@author: Sourick
"""
c = 1
a = input("Enter a string : ")
length = len(a)
n = length // 2
j = length - 1
for i in range (0,n):
    if a[i] != a[j]:
        c = 0
        break
    j -= 1
    
if (c == 0):
    print("The give string is not palidrome")
else:
    print("The given string is palidrome")
