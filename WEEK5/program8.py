# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:22:03 2020

@author: Sourick
"""

temp = 0
a = input("Enter some values : ").split()
n = len(a)
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

print("After Sorting")        
for i in a:
    print(i , end = " ")