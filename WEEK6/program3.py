# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:09:25 2020

@author: Sourick
"""


class student():
    def display(self,roll,name,stream,address,phone,age,marks):
        print("Roll : ",roll)
        print("Name : ",name)
        print("Stream : ",stream)
        print("Address : ",address)
        print("Phone : ",phone)
        print("Age : ",age)

        
    def setmarks(self,a,b,c):
        print("First Year : ",float(a))
        print("Second Year : ",float(b))
        print("Thrid Year : ",float(c))
        
obj = student()
r,n,s,a,ph,ag,mar = input("Enter basic details : ").split()
a,b,c = input("Enter marks details : ").split()
obj.display(r,n,s,a,ph,ag)
obj.setmarks(a,b,c)
