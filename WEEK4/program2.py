# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:52:23 2020

@author: Sourick
"""

def fizzbazz(n):
    if(n % 3 == 0 and n % 5 == 0):
        return 'fizzbuzz'
    elif(n % 3 == 0):
        return 'fizz'
    elif(n % 5 == 0):
        return 'buzz'
    else:
        return n
    

for i in range(1,20):
    print(fizzbazz(i))

