# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:22:16 2020

@author: Sourick
"""
hundred,fifty,ten,five,two,one,remaining = (0,0,0,0,0,0,0)
money = int(input("Enter money : "))
if(money >= 100):
    hundred = money // 100
    money = money % 100

if(money >= 50):
    fifty = money // 50
    money = money % 50

if(money >= 10):
    ten = money // 10
    money = money % 10
    
if(money >= 5):
    five = money // 5
    money = money % 5
    
if(money >= 2):
    two = money // 2
    money = money % 2
    one = money

print("Number of Hundred's Notes : ",hundred)
print("Number of fifty's Notes : ",fifty)
print("Number of Ten Notes : ",ten)
print("Number of Five Notes : ",five)
print("Number of Two Notes : ",two)
print("Number of One Notes : ",one)