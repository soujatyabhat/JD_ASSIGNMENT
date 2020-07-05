# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 08:40:27 2020

@author: Sourick
"""
temp = float(input("Enter temperature : "))
convert = input("Convert into (Press C for celius and F for fahrenheit ):")
if convert == 'c':
    print("The value of Celcius is : ", (temp - 32) / 1.8)
else:
   print("The value of Fahrehein is : ", (temp * 1.8) + 32)
    

    

    

    
