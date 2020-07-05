# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:09:11 2020

@author: Sourick

---------------------------------------------
The series is : 5,10,15,20,25,………………….,n
--------------------------------------------
"""


n = int(input("Enter a range : "))
print("The series is  : ")
for i in range (1,n + 1):
    print(5 * i,end = " ")
  
print(" ")
i = 1
print("The series is  : ",end = "\n")
while(i != n):
    print(5 * i, end = " ")
    i += 1
    
    
