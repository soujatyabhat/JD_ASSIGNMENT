# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:22:19 2020

@author: Sourick
"""
import random
def dice():
    contrl = input("Press 'y' to dice the roll :")
    n = random.randint(1,6)
    print("Your point is : ",n)
    return n

count = 0
n = dice()
while 1:
    if count >= 12:
        print("You are not allowed to roll sixes three times ")
        break
    if n == 6:
        count += 6
        n = dice()
    else:
        break
    
        
    

