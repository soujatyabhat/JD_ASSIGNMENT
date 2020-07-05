# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:00:50 2020

@author: Sourick
"""
p,r,t = (0,0,0)
p = float(input("Enter Principal : "))
r = float(input("Enter Rate :"))
t = float(input("Enter Time : "))
SI = (p * r * t) / 100
CI = (p * (pow(1 + (r / 100),t)))
print("The value of simple interest is : ",SI)
print("The value of compound interest is : ",CI)
