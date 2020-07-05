# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:10:14 2020

@author: Sourick
"""

class circle():
    PI = 3.142
    radius,area,circumference = 0,0,0
    
    def get_area(self,radius):
        circle.radius = radius
        circle.area = circle.PI * (circle.radius ** 2)
        print("The area of given circle is : ",circle.area)
        
    def getCircumference(self,radius):
        circle.radius = radius
        circle.circumference = (2 * circle.radius * circle.PI)
        print("The area of given circle is : ",circle.circumference)
        
obj = circle()
obj.get_area(2)
obj.getCircumference(34)
       
