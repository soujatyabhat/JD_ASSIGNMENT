# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:31:16 2020

@author: Sourick
"""
array = []
for i in range(10): 
   n = input()
   array.append(n)
    
array.sort()
for i in array:
    print(i , end = " ")