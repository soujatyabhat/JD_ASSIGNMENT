# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 07:58:09 2020

@author: Sourick
"""
even = []
odd = []
a = input("Enter some positive values : ").split()
for i in range(len(a)):
    
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("List of even numbers from given list : ")
for i in even:
    print(i, end = " ")
    
print()

print("List of odd numbers from given list : ")
for i in odd:
    print(i, end = " ")
        

