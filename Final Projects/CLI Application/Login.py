# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:20:27 2020

@author: Sourick
"""

    
email = password =  " "
count = 0
print("Signin  Your Account")
fpt = open("add.txt","r")

def check(a):
    global email,password
    new_list = list(a.split(' '))
    email_check = new_list.count(email)
    password_check = new_list.count(password)
    if email_check > 0 and password_check > 0:
        return True
    else:
        return False


email = input("Enter Email ID:")
password = input("Enter Password: ")

for line in fpt:
    a = line
    flag = check(a)
    if flag == True:
        print("Welcome To ABC Enterprise")
        break
    
fpt.close()