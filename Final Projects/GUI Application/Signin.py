# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 12:45:38 2020

@author: Sourick
"""

from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("250x160")
top.resizable(0,0)
top.title("Signin")
top.config(bg = "cyan")

flag1 = 0
fpt = ''
def opn():
    global fpt
    fpt = open("record.txt","r")

def check(a):
    new_list = list(a.split(' '))
    email_check = new_list.count(email.get())
    password_check = new_list.count(password.get())
    if email_check > 0 and password_check > 0:
        return True
    else:
        return False
    
def add():  
    opn()
    global fpt,flag1
    for line in fpt:
        a = line
        flag = check(a)
        if flag == True:
            flag1 = 1
            break
    if flag1 == 1:
         messagebox.showinfo("Conglatunation","Welcome to our portal")
    else:
         messagebox.showerror("Failure","Password or Email has not matched")
         email.delete(0, END)
         password.delete(0, END)   
    fpt.close()   
            
    
label1 = Label(top,text = "Enter Email ID : ",bg = "cyan").place(x = 5, y = 20)
email = Entry(top)
email.place(x = 100, y = 20)

label2 = Label(top,text = "Enter password: ",bg = "cyan").place(x = 5, y = 60)
password = Entry(top,show = "*")
password.place(x = 100, y = 60)

submit = Button(text = "Submit",bg = "green",fg = "white",width = "8",command = add).place(x = 40, y = 100)
reset = Button(text = "Reset",bg = "red",fg = "white",width = "8").place(x = 120, y = 100)

top.mainloop()
