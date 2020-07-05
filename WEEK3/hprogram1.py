# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 08:21:20 2020

@author: Sourick

first n terms of the series: 14 + 24 + 44 + 74 + 114 + ………. .

"""
Multiplier,sum  = 10,14
while 1:
    n = int(input("Enter a value : "))
    if n < 10:
        break
    else:
        print("Invalid Input!!!!")

for i in range(0,n):
    sum += (Multiplier * i)
    print(sum)
    


