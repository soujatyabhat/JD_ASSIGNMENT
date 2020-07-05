# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 22:43:55 2020

@author: Sourick
"""

class time():
    h,m = 0,0
    def __init__(self,h,m):
        self.h = h
        self.m = m
        
    def display(self):
        print("Time: " ,self.h ,":",self.m)
        
def add(obj1,obj2):
    add_min , div_min , hour , minute = 0,0,0,0
    add_min = obj1.m + obj2.m
    div_min = int(add_min) // 60
    hour = obj1.h + obj2.h + div_min
    minute =  add_min % 60
    print("Total time is ",hour,":", minute)
   
    
obj1 = time(1,30)
obj1.display()
obj2 = time(1,32)
obj2.display()
add(obj1,obj2)
