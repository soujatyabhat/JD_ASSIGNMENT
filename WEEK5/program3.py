# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:11:13 2020

@author: Sourick
"""
n = []
temp_size = [] #It stores length of words 
minimum_word = [] #It stores the position where minimum length's words is / are blonging
maximum_word = [] #It stores the position where mimaximum length's words is / are blonging

def count(find,what,length):
    if what == 0:
        for i in range(length):
            if temp_size[i] == find:
                minimum_word.append(i)
    elif what == 1:
        for i in range(length):
            if temp_size[i] == find:
                maximum_word.append(i)
    
    
  
n = input("Enter Sentence : ").split()
for i in n:
    temp_size.append(len(i))
 
length = len(temp_size)
minimum = min(temp_size)
maximum = max(temp_size)

count(minimum,0,length)
count(maximum,1,length)

print("The Minimum Words in sentence is / are: ")
for i in minimum_word:
    print(n[i],end = " ")
    
print("\n")

print("The Maximum Words in sentence is / are: ")
for i in maximum_word:
    print(n[i],end = " ")

        




