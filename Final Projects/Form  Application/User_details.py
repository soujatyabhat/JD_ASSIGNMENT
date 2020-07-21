# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:01:21 2020

@author: Sourick
"""
from tkinter import *
top = Tk()
top.geometry("240x200")
top.title("User Details")
top.resizable(0,0)
top.config(bg = "pink")
def gapping(n):
    name = ''
    for i in range(0,len(n)):
        if n[i] >= 'A' and n[i] <= 'Z' and i != 0 :
            name += ' ' + n[i]
        else:
            name += n[i]
    return name

def display():
    fpt = open("about.txt","r")
    new_string = str(fpt.read())
    new_list = list(new_string.split(' '))
    
    name = "Name : " + gapping(new_list[0])
    var1.set(name)
    
    address = "Address : " + gapping(new_list[1])
    var2.set(address)
    
    phone = "Phone Number : " + gapping(new_list[2])
    var3.set(phone)
    
    date = "DOB : " + gapping(new_list[3])
    var4.set(date)
    
    email = "Email : " + gapping(new_list[4])
    var5.set(email)

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
var5 = StringVar()


label1 = Label(top,text = "", textvariable=var1, bg = "pink").place(x = 25, y = 20)

label2 = Label(top,text = "",textvariable=var2,bg = "pink").place(x = 25, y = 50)

label3 = Label(top,text = "",textvariable=var3,bg = "pink").place(x = 25, y = 80)

label3 = Label(top,text = "",textvariable=var4,bg = "pink").place(x = 25, y = 110)

label3 = Label(top,text = "",textvariable=var5,bg = "pink").place(x = 25, y = 140)

display()
top.mainloop()
