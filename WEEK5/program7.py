# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 13:15:40 2020

@author: Sourick
"""
a = input("Enter some values : ").split()
set_table = set(a)
a = list(set_table)
a.sort()
print("All values : ")
for i in a:
    print(i,end = " ")