# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:05:52 2020

@author: Sourick
"""

a = int(input("Enter a fist side : "))
b = int(input("Enter a second side : "))
c = int(input("Enter a third side : "))
if a == b and b == c:
    print("Equilateral triangle.")
elif a == b or a == c or b == c:
    print("Isosceles triangle.")
else:
    print("Scalene triangle")
