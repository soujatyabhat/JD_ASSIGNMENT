# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:46:28 2020

@author: Sourick
"""
class temprature():
    c,f = 0,0
    def convertFahrenheit(self,c):
        temprature.f = (1.8 * c) + 32
        print("The Fahrenheit is : ",temprature.f)
    
    def convertCelsius(self,f):
        temprature.c = (f - 32) * 0.55
        print("The Celsius is : ",temprature.c)
        
obj = temprature()
ch = input("Convert into : ")
n = float(input("Enter temprature : "))
if ch == 'f':
    obj.convertFahrenheit(n)
elif ch == 'c':
    obj.convertCelsius(n)
    


        
        
        

