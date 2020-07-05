# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 23:02:36 2020

@author: Sourick
"""
year = int(input("Enter a year : "))
if year % 100 == 0:
    if year % 400 == 0:
        print("The given year is leap Year")
    else:
        print("The given is not leap Year")
else:
    if year % 4 == 0:
        print("The given year is leap Year")
    else:
        print("The given year is not leap year")



