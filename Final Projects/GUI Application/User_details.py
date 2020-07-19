# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 22:44:31 2020

@author: Sourick
"""

def gapping(n):
    name = ''
    for i in range(0,len(n)):
        if n[i] >= 'A' and n[i] <= 'Z' and i != 0 :
            name += ' ' + n[i]
        else:
            name += n[i]
    return name

fpt = open("about.txt","r")
new_string = str(fpt.read())
new_list = list(new_string.split(' '))


print("Name :",gapping(new_list[0]))
print("Address : ",new_list[1])
print("Phone Number: ",new_list[2])
print("Date: ",new_list[3])
print("Email : ",new_list[4])

