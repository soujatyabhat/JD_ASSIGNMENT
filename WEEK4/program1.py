# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 19:37:21 2020

@author: Sourick
"""
result = 0
print("Enter add for addition")
print("Enter 'sub' for sub for subtraction")
print("Enter 'mul' for multiplication")
print("Enter 'div' for divition")
choose = input("Enter your choose : ")
a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
try:
    if choose == 'add':  
        result = a + b
    elif choose == 'sub':
        result =  a - b
    elif choose == 'mul':
        result = a * b
    elif choose == 'div':
        result = a // b
    else:
        print("Invalid choose")
        
    print("The result is : ",result)
except:
    print("Exception occured during division.")
    

    
    

