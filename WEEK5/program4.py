# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:59:59 2020

@author: Sourick
"""
max = 0
a = input("Enter a value : ").split()
max = a[0]
length = len(a)
for i in range(1,length):
    if a[i] > max:
        max = a[i]
        
print("The maximum number in array is : " ,max)
    

