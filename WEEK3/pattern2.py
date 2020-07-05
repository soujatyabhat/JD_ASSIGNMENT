# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 09:31:00 2020

@author: Sourick

------------------------------------------
Display The pattern following pattern :
------------------------------------------
1  
1 0  
1 0 1  
1 0 1 0  
1 0 1 0 1  
1 0 1 0 1 0  
1 0 1 0 1 0 1  
1 0 1 0 1 0 1 0  
1 0 1 0 1 0 1 0 1  
"""


n = int(input("Enter a value :"))
for i in range (1,n+1):
    for j in range (1,i):
        print(j % 2, end = " ")
    
    print(" ")