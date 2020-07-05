# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:08:59 2020

@author: Sourick
"""
max = 0
a = input("Enter a value : ").split()
length = len(a)
for i in range(length):
    temp = int(a[i])
    if temp % 2 == 0:
        print(a[i] ,end = " ")
        